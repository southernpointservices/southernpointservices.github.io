#!/usr/bin/env python3
"""
Internal build helper (not part of the shipped site) — stitches
header.html + page content + footer.html into a final page, and marks
the correct top-level nav link active. Keeps ~20 pages byte-identical
in their header/footer instead of hand-copy-pasting each time.

Usage: called from other build scripts, not run directly with args.
"""
import re

HEADER = open("/home/claude/southern-point-site/_partials/header.html").read()
FOOTER = open("/home/claude/southern-point-site/_partials/footer.html").read()

ACTIVE_HREFS = {
    "services": ['<a href="/services/">Services</a>'],
    "industries": ['<a href="/industries/">Industries</a>'],
    "job-seekers": ['<a href="/services/">Services</a>'],
    "about": ['<a href="/about/">About</a>'],
    "resources": ['<a href="/resources/">Resources</a>'],
    "contact": ['<a class="nav-text-link" href="/contact/">Contact</a>'],
}


def header_with_active(section):
    html = HEADER
    for target in ACTIVE_HREFS.get(section, []):
        if 'class="' in target:
            # Merge into the existing class attribute rather than
            # appending a second (invalid) class="..." attribute.
            replacement = target.replace('class="', 'class="active ', 1)
        else:
            replacement = target.replace('">', '" class="active">', 1)
        html = html.replace(target, replacement)
    return html


def build(title, description, extra_style, body_html, section, canonical, og_type="website"):
    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Southern Point">

<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32">
<link rel="icon" href="/favicon-16x16.png" type="image/png" sizes="16x16">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<link rel="stylesheet" href="/assets/css/site.css">

<style>
{extra_style}
</style>
</head>


<body>

{header_with_active(section)}

<main>
{body_html}
</main>

{FOOTER}

</body>
</html>
"""
    return head
