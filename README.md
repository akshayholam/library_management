### Library Management

Library Management System

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app library_management
```

### Contributing

### Print Formats (Rishab Industries)

This app includes 4 custom Jinja print formats, originally built for Rishab Industries, along with supporting custom fields:

| Print Format | DocType | Purpose |
|---|---|---|
| Credit Note - RIP | Sales Invoice | Printed when "Is Return" is checked |
| Tax Invoice - RIP | Sales Invoice | Standard GST tax invoice |
| Delivery Challan - RIP | Delivery Note | 3-copy delivery challan (Original/Duplicate/Triplicate) |
| Rishab PO Format | Purchase Order | Purchase order with Indian number formatting |

**Custom Fields added on Delivery Note:**
- `challan_type` (Select: Returnable / Non-Returnable)
- `total_weight_kg` (Float)
- `dc_department` (Data)
- `dc_ref_person` (Data)

#### Dependencies

These print formats reference GST-related fields (`company_gstin`, `billing_address_gstin`, `gst_hsn_code`, etc.) that come from the **[India Compliance](https://github.com/resilient-tech/india-compliance)** app. India Compliance must be installed on the target site for these fields to populate correctly; without it, the print formats will still install but the GST sections may render blank.

#### Known limitations

- **Rishab PO Format** references a company logo at `/files/download.jpg`. This file is site-specific and is **not** included in this repo's fixtures — the logo will not display until the file is manually re-uploaded on the target site at that path. (The other 3 formats embed the logo as base64 directly in the template, so they are self-contained.)
- Indian comma formatting (`1,23,420/-`) and date formats (DD-MM-YYYY) are hardcoded in the Jinja templates, not controlled by site-wide Number Format/Date Format settings.
- These formats were built and tested against **ERPNext v15** / **Frappe v15**.

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/library_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
