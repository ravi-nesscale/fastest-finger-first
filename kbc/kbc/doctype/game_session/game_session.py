import frappe
from frappe.model.document import Document

class GameSession(Document):
    def validate(self):
        total = 0
        max_time_ms = 9999  # 5 minutes = 300,000 ms

        for question in self.total_questions:
            if question.select_option == question.correct_answer and question.time_spent:
                minutes, seconds, milliseconds = map(int, question.time_spent.split(":"))

                time_taken_ms = (minutes * 60 * 1000) + (seconds * 1000) + milliseconds

                points = max(0, max_time_ms - time_taken_ms)

                question.question_point = points
            else:
                question.question_point = 0

            total += question.question_point

        self.total_points = total


    def on_update(self):
        self.sync_with_leaderboard()

    def sync_with_leaderboard(self):
        if not (self.user_id and self.user_name and self.total_points is not None):
            return  # Do nothing if required fields are missing

        leaderboard = frappe.get_all(
            "KBC Leaderboard",
            filters={"player_id": self.user_id},
            limit=1
        )

        if leaderboard:
            # Update existing leaderboard record
            lb_doc = frappe.get_doc("KBC Leaderboard", leaderboard[0].name)
            lb_doc.player_name = self.user_name
            lb_doc.total_points = self.total_points
            lb_doc.save()
        else:
            # Create new leaderboard record
            frappe.get_doc({
                "doctype": "KBC Leaderboard",
                "player_id": self.user_id,
                "player_name": self.user_name,
                "total_points": self.total_points
            }).insert()
