import frappe
import json

@frappe.whitelist()
def submit_game_session(data):
    data = json.loads(data)
    user_id = data.get("user_id")
    questions = data.get("questions", [])

    if not user_id or not questions:
        return {"status": "error", "message": "Missing user_id or questions"}

    # Create Game Session
    doc = frappe.new_doc("Game Session")
    doc.user_id = user_id
    doc.user_name = frappe.db.get_value("User", user_id, "full_name")

    # Add questions to child table
    for q in questions:
        doc.append("total_questions", {
            "question_name": q.get("question_name"),
            "selected_option": q.get("selected_option"),
            "time_spent": q.get("time_spent"),
        })

    doc.save(ignore_permissions=True)
    frappe.db.commit()

    return {"status": "success", "message": "Game session submitted"}
