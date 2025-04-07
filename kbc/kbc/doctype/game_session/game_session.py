# Copyright (c) 2025, ravi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GameSession(Document):
    def validate(self):
        pass
        # Check if the selected option is the same as the correct answer
        # self.is_correct = self.selected_option == self.correct_answer
