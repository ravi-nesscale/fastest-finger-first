import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_questions():
    data = frappe.get_all(
        "Question",  # The doctype name
        fields=["name", "question_text", "option_1", "option_2", "option_3", "option_4", "correct_answer"],
        order_by="name desc"
    )
    if not data:
        return {"message": "No questions available"}
        
    return {"message": data}


@frappe.whitelist(allow_guest=True)
def add_question(question_text, option_1, option_2, option_3, option_4, correct_answer):
    try:
        # Log the incoming data
        frappe.log_error(f"Received Data: question_text={question_text}, option_1={option_1}, option_2={option_2}, option_3={option_3}, option_4={option_4}, correct_answer={correct_answer}", _("Add Question"))

        # Ensure all fields are provided
        if not (question_text and option_1 and option_2 and option_3 and option_4 and correct_answer):
            return {"error": "All fields are required"}

        # Insert the question into the Question doctype
        new_question = frappe.get_doc({
            "doctype": "Question",
            "question_text": question_text,
            "option_1": option_1,
            "option_2": option_2,
            "option_3": option_3,
            "option_4": option_4,
            "correct_answer": correct_answer,
        })

        new_question.insert(ignore_permissions=True)
        
        # Log success
        frappe.log_error(f"Successfully added question: {new_question.name}", _("Add Question"))

        return {"message": "Question added successfully"}
    
    except Exception as e:
        # Log the error with traceback
        frappe.log_error(frappe.get_traceback(), _("Add Question Error"))
        return {"error": f"Failed to add question: {str(e)}"}

@frappe.whitelist(allow_guest=True)
def delete_question(question_name):
    # Fetch the question using its name
    question = frappe.get_doc("Question", question_name)
    
    # Delete the question
    question.delete()
    
    return {"message": "Question deleted successfully"}
