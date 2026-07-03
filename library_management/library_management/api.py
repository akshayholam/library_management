import frappe

def send_notification(doc, method):
    frappe.msgprint(f'Hook triggered! Article "{doc.article_name}" was saved!')

@frappe.whitelist()
def get_articles():
    articles = frappe.get_list('Article',
        fields=['name', 'article_name', 'author', 'status'],
        order_by='creation desc'
    )
    return articles
@frappe.whitelist()
def get_article(name):
    article = frappe.get_doc('Article', name)
    return article
