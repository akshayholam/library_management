app_name = "library_management"
app_title = "Library Management"
app_publisher = "Akshaye"
app_description = "Library Management System"
app_email = "akshayholam3738@gmail.com"
app_license = "mit"

doc_events = {
    "Article": {
        "after_save": "library_management.library_management.api.send_notification"
    }
}

fixtures = [
    {
        "doctype": "Report",
        "filters": [
            ["name", "in", ["My First Report"]]
        ]
    },
    {
        "doctype": "DocType",
        "filters": [
            ["module", "in", ["Library Management", "Custom"]]
        ]
    },
    {
        "doctype": "Client Script",
        "filters": [
            ["module", "in", ["Library Management", "Custom"]]
        ]
    },
    {
        "doctype": "Server Script",
        "filters": [
            ["name", "in", ["Article Server Script"]]
        ]
    }
]
