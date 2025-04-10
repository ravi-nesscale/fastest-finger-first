# kbc/kbc/api/player.py

import frappe

@frappe.whitelist(allow_guest=True)
def create_simple_player(player_name, email, password):
    # Check if player already exists
    if frappe.db.exists("Players", {"email": email}):
        return {"status": "exists", "message": "Player already exists."}

    doc = frappe.get_doc({
        "doctype": "Players",
        "player_name": player_name,
        "email": email,
        "password": password
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {"status": "success", "message": "Player added."}
