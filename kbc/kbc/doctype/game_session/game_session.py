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
