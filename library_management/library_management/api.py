import frappe

def send_notification(doc, method):
    frappe.msgprint(f'Hook triggered! Article "{doc.article_name}" was saved!')
