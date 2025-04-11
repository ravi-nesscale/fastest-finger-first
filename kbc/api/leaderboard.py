import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_leaderboard():
    try:
        data = frappe.get_all(
            "KBC Leaderboard",
            fields=["player_id", "player_name", "total_points"],
            order_by="total_points desc"
        )
        return data
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Leaderboard Error"))
        return []
