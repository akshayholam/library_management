# Copyright (c) 2026, Akshaye and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class Article(Document):
    def before_save(self):
        frappe.msgprint(f'Article {self.article_name} is being saved!')
    
    def after_save(self):
        frappe.msgprint(f'Article {self.article_name} saved successfully!')
