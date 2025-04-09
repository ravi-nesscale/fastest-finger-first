import frappe
import json

@frappe.whitelist(allow_guest=True)
def save_single_answer(data=None):
    try:
        if isinstance(data, str):
            data = json.loads(data)

        answer = data.get("answer")
        if not answer:
            return {"status": "error", "message": "No answer provided"}

        # Fixed user details
        user_id = "admin@example.com"
        user_name = "Administrator"

        # Get or create Game Session
        session = frappe.get_all("Game Session", filters={"user_id": user_id}, limit=1)
        if session:
            doc = frappe.get_doc("Game Session", session[0].name)
        else:
            doc = frappe.new_doc("Game Session")
            doc.user_id = user_id
            doc.user_name = user_name
            doc.insert(ignore_permissions=True)

        # Update or append child entry
        exists = False
        for q in doc.total_questions:
            if q.question_name == answer["question_name"]:
                q.select_option = answer["select_option"]
                q.time_spent = answer["time_spent"]
                exists = True
                break

        if not exists:
            doc.append("total_questions", {
                "question_name": answer["question_name"],
                "select_option": answer["select_option"],
                "time_spent": answer["time_spent"]
            })

        doc.save(ignore_permissions=True)
        frappe.db.commit()

        return {"status": "success"}

    except Exception as e:
        frappe.log_error(title="Game Session Error", message=frappe.get_traceback())
        return {"status": "error", "message": str(e)}
