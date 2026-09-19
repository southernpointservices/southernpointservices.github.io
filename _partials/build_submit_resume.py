#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build
from build_job_seekers import submit_body, STYLE_SUBMIT

BASE = "/home/claude/southern-point-site"

html = build(
    title="Submit Your Resume | Southern Point Staffing",
    description="Submit your resume to Southern Point for general consideration — no current opening required, and no cost to candidates.",
    extra_style=STYLE_SUBMIT,
    body_html=submit_body,
    section="job-seekers",
    canonical="https://southernpointllc.com/submit-resume/",
)

out_dir = f"{BASE}/submit-resume"
os.makedirs(out_dir, exist_ok=True)
with open(f"{out_dir}/index.html", "w") as f:
    f.write(html)
print("wrote submit-resume/index.html")

# ---------------------------------------------------------------------------
# Redirect stub at the old /job-seekers/submit-resume/ URL so any existing
# link or bookmark still lands on the right page instead of a dead end.
# ---------------------------------------------------------------------------
REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Submit Your Resume | Southern Point Staffing</title>
<meta http-equiv="refresh" content="0; url=/submit-resume/">
<link rel="canonical" href="https://southernpointllc.com/submit-resume/">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<p>This page has moved. If you are not redirected automatically, <a href="/submit-resume/">click here to submit your resume</a>.</p>
</body>
</html>
"""

old_dir = f"{BASE}/job-seekers/submit-resume"
os.makedirs(old_dir, exist_ok=True)
with open(f"{old_dir}/index.html", "w") as f:
    f.write(REDIRECT)
print("wrote job-seekers/submit-resume/index.html (redirect stub)")
