# Job data — `jobs.json`

This file is the single source of truth for everything shown on `/jobs.html`. It starts empty (`[]`) on purpose — the site never shows placeholder or fake listings. Add a real object to the array for every real opening, in this shape:

```json
{
  "id": "customer-success-manager-2026-09",
  "title": "Customer Success Manager",
  "companyLabel": "Technology & Professional Services",
  "category": "Technology",
  "location": "Remote",
  "workArrangement": "Remote",
  "employmentType": "Full-time",
  "description": "Work with customers to build strong relationships, coordinate solutions, and support long-term account success.",
  "postedDate": "2026-09-01",
  "applyType": "internal",
  "applyUrl": "",
  "status": "active",
  "responsibilities": [
    "Manage a portfolio of customer accounts from onboarding through renewal.",
    "Coordinate with internal teams to resolve customer issues quickly."
  ],
  "requirements": [
    "2+ years in a customer-facing role.",
    "Comfortable working across email, phone, and video calls."
  ],
  "benefits": [
    "Remote-first schedule.",
    "Paid time off."
  ]
}
```

## Field reference

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Unique, URL-safe (lowercase, hyphens). Never reuse an id for a different role — it's also the value used in the `/jobs.html?job=<id>` detail-view link. |
| `title` | yes | Job title as shown on the card and detail page. |
| `companyLabel` | no | Short line shown under the title (a category/department label, or a real company name if you want to name the employer). Falls back to `category` if omitted. |
| `category` | yes | One of the filter categories already on the page: `Technology`, `Healthcare`, `Sales`, `Operations`, `Administrative`. Add a new one only if you also add a matching checkbox in `jobs.html`. |
| `location` | yes | Free text shown on the card, e.g. `"Houston, TX"`, `"Remote"`, `"Nationwide"`. The location filter dropdown does substring matching against this. |
| `workArrangement` | yes | `Remote`, `Hybrid`, or `On-site`. |
| `employmentType` | yes | `Full-time`, `Part-time`, `Contract`, or `Internship`. |
| `description` | yes | 1–2 sentence summary shown on the card and as the "About This Role" section on the detail page. |
| `postedDate` | yes | `YYYY-MM-DD`. Drives the "Fresh" tag (≤7 days old), the relative "posted X days ago" text, and Newest sort. |
| `applyType` | yes | `"internal"` shows an **Apply Now** button that opens the on-site Quick Apply form. `"external"` shows an **Apply on Company Site** button that opens `applyUrl` in a new tab. |
| `applyUrl` | only if `applyType` is `"external"` | Full URL to the original posting. |
| `status` | yes | The page only ever shows jobs where this is exactly `"active"` — set it to anything else (e.g. `"closed"`) or delete the entry to take a role down. |
| `responsibilities` | no | Array of short strings, shown as a bulleted "Responsibilities" section on the job's detail page. Omit entirely if you don't have this detail yet — the section just won't render. |
| `requirements` | no | Array of short strings, shown as a bulleted "Requirements" section on the detail page. Optional, same as above. |
| `benefits` | no | Array of short strings, shown as a bulleted "Benefits" section on the detail page. Optional, same as above. |

Every job also gets its own shareable detail view automatically at `/jobs.html?job=<id>` — there's nothing extra to build per job. If a link points to an `id` that isn't in this file (or isn't `"active"`), the page shows a friendly "no longer available" message instead of an error.

## How to add or remove a job

1. Edit this file directly on GitHub (same workflow already used for the HTML pages — open the file, click the pencil icon, edit, commit to `main`).
2. Add a new object to the array, or delete one to take a role down. Keep it valid JSON — a trailing comma or missing bracket will make `jobs.html` fail to load any jobs, so double-check with a JSON validator if you're not sure.
3. GitHub Pages republishes automatically within a minute or two of the commit.

## Migrating this to a live Google Sheet later

Southern Point's other internal tools already lean on Google Sheets, so this file is deliberately structured so a spreadsheet can replace it without touching the rest of the site:

1. Create a Google Sheet with one column per field above (`id`, `title`, `companyLabel`, `category`, `location`, `workArrangement`, `employmentType`, `description`, `postedDate`, `applyType`, `applyUrl`, `status`, and optionally `responsibilities`/`requirements`/`benefits` as pipe- or comma-separated text you split into an array).
2. Share it as "Anyone with the link — Viewer."
3. In `jobs.html`, change the one line `fetch('data/jobs.json')` to fetch the sheet's published CSV export instead:
   `https://docs.google.com/spreadsheets/d/<SHEET_ID>/export?format=csv`
4. Add a small CSV-to-object parser (or a tiny library like PapaParse from a CDN) in place of `response.json()`, mapping each row to the same field names used above.

Everything else — rendering, filtering, sorting, the Quick Apply modal — reads from the same in-memory array either way, so nothing downstream needs to change.
