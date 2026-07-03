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
@frappe.whitelist()
def get_random_joke():
    import requests
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    if response.status_code == 200:
        joke = response.json()
        return {
            'setup': joke['setup'],
            'punchline': joke['punchline']
        }
    else:
        frappe.throw('Failed to fetch joke!')
@frappe.whitelist()
def get_weather():
    import requests
    response = requests.get('https://wttr.in/Pune?format=j1')
    if response.status_code == 200:
        data = response.json()
        temp = data['current_condition'][0]['temp_C']
        weather = data['current_condition'][0]['weatherDesc'][0]['value']
        return {
            'city': 'Pune',
            'temperature': f'{temp}°C',
            'condition': weather
        }
    else:
        frappe.throw('Failed to fetch weather!')
