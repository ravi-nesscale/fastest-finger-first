# kbc/api/game_session.py

import frappe
import json

@frappe.whitelist(allow_guest=True)
def save_single_answer(data):
    try:
        if isinstance(data, str):
            data = json.loads(data)

        user_id = data.get("user_id")
        user_name = data.get("user_name")
        question_name = data.get("question_name")
        select_option = data.get("select_option")  # not select_option
        time_spent = data.get("time_spent")

        if not all([user_id, question_name, select_option]):
            return {"message": "Missing required fields"}

        session = frappe.get_all("Game Session", filters={"user_id": user_id}, fields=["name"])
        if session:
            doc = frappe.get_doc("Game Session", session[0]["name"])
        else:
            doc = frappe.new_doc("Game Session")
            doc.user_id = user_id
            doc.user_name = user_name

        # Update or add question entry
        updated = False
        for row in doc.total_questions:
            if row.question_name == question_name:
                row.select_option = select_option
                row.time_spent = time_spent
                updated = True
                break

        if not updated:
            doc.append("total_questions", {
                "question_name": question_name,
                "select_option": select_option,
                "time_spent": time_spent,
            })

        doc.save(ignore_permissions=True)
        frappe.db.commit()

        return {"message": "success"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "save_single_answer Error")
        return {"message": f"Error: {str(e)}"}
