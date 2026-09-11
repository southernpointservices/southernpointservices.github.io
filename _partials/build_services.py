#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

INDUSTRIES = [
    ("Technology", "technology"), ("Healthcare", "healthcare"), ("Sales", "sales"),
    ("Operations", "operations"), ("Administrative", "administrative"),
]

def industries_line():
    links = ", ".join(f'<a href="/industries/{slug}/">{name}</a>' for name, slug in INDUSTRIES)
    return f'<p class="industries-line">Serving organizations across {links}.</p>'

SHARED_STYLE = """
.industries-line{
    font-size:16px;
    color:var(--sp-muted);
    max-width:700px;
}

.industries-line a{
    color:var(--sp-bronze-dark);
    font-weight:700;
    text-decoration:none;
    border-bottom:1px solid var(--sp-line-dark);
}

.industries-line a:hover{
    border-color:var(--sp-bronze-dark);
}

.dark .industries-line{ color:#C7C1B3; }
.dark .industries-line a{ color:var(--sp-bronze-light); border-color:var(--sp-line-dark); }

.service-split{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:0;
    align-items:stretch;
}

.service-split .split-copy{
    display:flex;
    flex-direction:column;
    justify-content:center;
    padding:60px;
}

.service-split .photo-frame{
    min-height:420px;
}

@media(max-width:900px){
    .service-split{grid-template-columns:1fr;}
    .service-split .split-copy{padding:44px 24px;}
    .service-split .photo-frame{min-height:280px;}
}
"""

def service_split(photo_src, alt, label, title, body_html, dark=False, reverse=False):
    section_class = "dark" if dark else ""
    copy = f"""
<div class="split-copy">
<div class="section-label"{' style="color:var(--sp-bronze-light);"' if dark else ''}>{label}</div>
<h2 class="section-title"{' style="color:#fff;"' if dark else ''}>{title}</h2>
{body_html}
</div>"""
    photo = f"""
<div class="photo-frame">
<img class="photo" src="/assets/images/{photo_src}" alt="{alt}">
</div>"""
    order = photo + copy if reverse else copy + photo
    return f"""
<section class="{section_class}">
<div class="service-split">
{order}
</div>
</section>"""

# =============================================================================
# /services/  (hub)
# =============================================================================
HUB_STYLE = SHARED_STYLE + """
"""

PILLARS = [
    ("01", "Staffing &amp; Recruiting", "staffing-recruiting",
     "The right people for the work that matters.",
     "Southern Point connects organizations with qualified talent through flexible staffing and recruiting solutions — temporary, temp-to-hire, direct hire, and contract."),
    ("02", "Professional Services", "professional-services",
     "Support that keeps organizations moving.",
     "Flexible professional resources for organizations that need additional capacity, support, or expertise across administrative, operational, and technical functions."),
    ("03", "Workforce Solutions", "workforce-solutions",
     "Flexible resources for changing requirements.",
     "Organizations don't always need the same people, skills, or capacity. Southern Point helps build workforce solutions around actual organizational requirements."),
    ("04", "Specialized Solutions", "specialized-solutions",
     "Flexible resources for specialized requirements.",
     "Some requirements call for specialized professionals, local resources, vendors, or external service providers. Southern Point coordinates appropriate resources when a need extends beyond an organization's existing capacity."),
]

def pillar_rows():
    out = []
    for num, name, slug, tagline, desc in PILLARS:
        out.append(f"""
<a class="editorial-row" href="/services/{slug}/" style="text-decoration:none; color:inherit;">
<div class="row-num">{num}</div>
<div>
<h3>{name} &mdash; {tagline}</h3>
<p>{desc}</p>
<span class="row-link">Explore {name} &rarr;</span>
</div>
</a>""")
    return "\n".join(out)

hub_body = f"""
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">WHAT WE DO</div>
<h1>Workforce, Professional, and Operational Solutions.</h1>
<p>Southern Point helps organizations access the people, support, and resources they need to move forward — through staffing and recruiting, professional services, workforce solutions, and specialized resource coordination.</p>
</div>
</section>

<section>
<div class="container">
<div class="photo-frame ratio-wide">
<img class="photo" src="/assets/images/services-hub.jpg" alt="Southern Point's four service divisions at work across organizations">
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">FOUR WAYS WE HELP</div>
<h2 class="section-title" style="color:#fff;">Built to grow with what your organization needs.</h2>
<div class="editorial-list" style="margin-top:30px;">
{pillar_rows()}
</div>
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">INDUSTRIES WE SERVE</div>
<h2 class="section-title">Focused expertise across five areas.</h2>
{industries_line()}
</div>
</section>

<section style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">READY TO START?</div>
<h2 class="section-title">Tell us what you're trying to solve.</h2>
<div class="btn-row" style="justify-content:center;">
<a class="btn btn-red" href="/request-talent/">Find Talent</a>
<a class="btn btn-outline" href="/contact/">Discuss Your Needs</a>
</div>
</div>
</section>
"""

# =============================================================================
# /services/staffing-recruiting/
# =============================================================================
ENGAGEMENT_MODELS = [
    ("Temporary Staffing", "Short-term coverage for leave, seasonal volume, or unexpected gaps — without a permanent commitment."),
    ("Temp-to-Hire", "Bring a candidate on temporarily and convert to a permanent hire once you've confirmed the fit."),
    ("Direct Hire", "Southern Point sources and screens candidates for permanent roles you hire directly."),
    ("Contract Staffing", "Project-based and fixed-term engagements for defined scopes of work."),
]

STAFFING_WHY = [
    ("Candidate Sourcing", "Southern Point sources candidates against the specific role, not a generic applicant pool."),
    ("Structured Screening", "Every candidate is screened for relevant experience and fit before you ever see a resume."),
    ("Speed", "A streamlined process means less time between identifying a need and having qualified candidates to consider."),
    ("Industry Knowledge", "Focused work across Technology, Healthcare, Sales, Operations, and Administrative roles — not every field at once."),
    ("Talent Acquisition", "From a single hire to filling multiple similar roles at once, Southern Point manages the search end to end."),
    ("Ongoing Partnership", "Southern Point stays engaged after placement rather than disappearing once a candidate starts."),
]

def editorial_rows(items, start=1):
    out = []
    for i, (title, body) in enumerate(items, start=start):
        out.append(f"""
<div class="editorial-row">
<div class="row-num">0{i}</div>
<div>
<h3>{title}</h3>
<p>{body}</p>
</div>
</div>""")
    return "\n".join(out)

staffing_body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/services/">Services</a><span>/</span>Staffing &amp; Recruiting</div>
<div class="eyebrow eyebrow-light">SERVICES / STAFFING &amp; RECRUITING</div>
<h1>The Right People For The Work That Matters.</h1>
<p>Southern Point connects organizations with qualified talent through flexible staffing and recruiting solutions built around how your organization actually hires — not a one-size-fits-all process.</p>
<div class="btn-row" style="margin-top:10px;">
<a class="btn btn-red" href="/request-talent/">Request Talent</a>
<a class="btn btn-outline-white" href="/contact/">Discuss Your Hiring Needs</a>
</div>
</div>
</section>

{service_split(
    "services-staffing.jpg",
    "Southern Point sourcing and screening candidates for an open role",
    "HOW WE WORK",
    "Structured sourcing, not a resume dump.",
    "<p>Every search starts with the actual role, not a generic template. Southern Point sources candidates against your specific requirements, screens for experience and fit before you ever see a resume, and stays engaged through onboarding — across temporary, temp-to-hire, direct hire, and contract engagements.</p>",
)}

<section>
<div class="container">
<div class="section-label">ENGAGEMENT MODELS</div>
<h2 class="section-title">Different needs call for different engagements.</h2>
<p class="section-intro">Southern Point structures every engagement around the role and timeline, not a single fixed service.</p>
<div class="editorial-list" style="margin-top:30px;">
{editorial_rows(ENGAGEMENT_MODELS)}
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">WHY SOUTHERN POINT</div>
<h2 class="section-title" style="color:#fff;">What organizations get by working with us.</h2>
<div class="editorial-list" style="margin-top:30px;">
{editorial_rows(STAFFING_WHY)}
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-label">HOW IT WORKS</div>
<h2 class="section-title">A simple, five-step process.</h2>
<div class="process-grid">
<div class="step"><div class="step-number">01</div><h3>Tell Us What You Need</h3><p>Share the role, requirements, timeline, and engagement type.</p></div>
<div class="step"><div class="step-number">02</div><h3>We Source Candidates</h3><p>Southern Point identifies candidates matched to the specific role.</p></div>
<div class="step"><div class="step-number">03</div><h3>We Screen &amp; Match</h3><p>Candidates are screened for experience, reliability, and fit.</p></div>
<div class="step"><div class="step-number">04</div><h3>You Hire</h3><p>You make the final decision on who joins your team.</p></div>
<div class="step"><div class="step-number">05</div><h3>We Support the Relationship</h3><p>Southern Point stays engaged through onboarding and beyond.</p></div>
</div>
</div>
</section>

{service_split(
    "homepage-candidates.jpg",
    "A candidate reviewing current openings with Southern Point",
    "FOR CANDIDATES",
    "Looking for your next opportunity?",
    '<p style="margin-bottom:20px;">Current openings are posted directly from Southern Point’s job board — search now, submit your resume for future consideration, or sign up for alerts so we reach out when a fit comes up.</p><div class="btn-row"><a class="btn btn-red" href="/jobs.html">Find Jobs</a><a class="btn btn-outline" href="/submit-resume/">Submit Resume</a><a class="btn btn-outline" href="/job-alerts/">Job Alerts</a></div>',
    reverse=True,
)}

<section class="tint">
<div class="container">
<div class="section-label">INDUSTRIES WE SERVE</div>
<h2 class="section-title">Focused expertise across five areas.</h2>
{industries_line()}
</div>
</section>

<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">READY TO START?</div>
<h2 class="section-title">Let's talk about your hiring needs.</h2>
<p style="max-width:600px; margin:0 auto 10px;">Tell Southern Point what you're looking for through a short intake form, and we'll follow up to discuss next steps.</p>
<a class="btn btn-red" href="/request-talent/" style="margin-top:20px;">Request Talent</a>
</div>
</section>
"""

# =============================================================================
# /services/professional-services/
# =============================================================================
PROFESSIONAL_CATEGORIES = [
    ("Administrative Support", "Administrative resources that help organizations maintain day-to-day operations."),
    ("Operations Support", "Resources that help teams maintain organizational efficiency and continuity."),
    ("Program Support", "Professional resources supporting ongoing programs and initiatives."),
    ("Project Support", "Additional personnel and coordination support for projects and organizational initiatives."),
    ("Customer Support", "Customer-facing and service-support resources."),
    ("Technical Support", "Technical and technology-oriented support where qualified personnel are available."),
]

professional_body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/services/">Services</a><span>/</span>Professional Services</div>
<div class="eyebrow eyebrow-light">SERVICES / PROFESSIONAL SERVICES</div>
<h1>Professional Support Built Around Your Organization.</h1>
<p>Southern Point provides flexible professional resources to help organizations increase capacity and support ongoing initiatives — administrative, operational, and technical support where qualified personnel are available.</p>
<div class="btn-row" style="margin-top:10px;">
<a class="btn btn-red" href="/contact/">Discuss Your Support Needs</a>
</div>
</div>
</section>

{service_split(
    "services-professional.jpg",
    "Professional support in action at an organization Southern Point serves",
    "HOW THIS DIFFERS FROM STAFFING",
    "Additional capacity, not just headcount.",
    "<p>Professional Services is about giving organizations flexible access to support and coordination — the people and process that keep a program, project, or operation moving — rather than a single placement against one job requisition. Southern Point structures this around the actual scope of work involved, not unsupported claims about advanced consulting or engineering capability.</p>",
)}

<section>
<div class="container">
<div class="section-label">SUPPORT CATEGORIES</div>
<h2 class="section-title">Capacity where your team needs it.</h2>
<div class="editorial-list" style="margin-top:30px;">
{editorial_rows(PROFESSIONAL_CATEGORIES)}
</div>
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">INDUSTRIES WE SERVE</div>
<h2 class="section-title">Focused expertise across five areas.</h2>
{industries_line()}
</div>
</section>

<section style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">READY TO TALK IT THROUGH?</div>
<h2 class="section-title">Tell us what your team needs support with.</h2>
<a class="btn btn-red" href="/contact/" style="margin-top:10px;">Discuss Your Support Needs</a>
</div>
</section>
"""

# =============================================================================
# /services/workforce-solutions/
# =============================================================================
WORKFORCE_ITEMS = [
    ("Workforce Planning", "Understanding current and future workforce requirements."),
    ("Talent Acquisition", "Identifying and recruiting qualified professionals."),
    ("Workforce Augmentation", "Providing additional resources when internal capacity is limited."),
    ("Contract Resources", "Flexible access to professionals based on organizational or project requirements."),
]

workforce_body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/services/">Services</a><span>/</span>Workforce Solutions</div>
<div class="eyebrow eyebrow-light">SERVICES / WORKFORCE SOLUTIONS</div>
<h1>Flexible Resources For Changing Requirements.</h1>
<p>Organizations don't always need the same people, skills, or capacity. Southern Point helps build workforce solutions around actual organizational requirements — not a fixed model applied regardless of the situation.</p>
<div class="btn-row" style="margin-top:10px;">
<a class="btn btn-red" href="/contact/">Discuss Your Workforce Needs</a>
</div>
</div>
</section>

{service_split(
    "services-workforce.jpg",
    "A team planning workforce capacity with Southern Point",
    "HOW WE APPROACH IT",
    "Requirements first, then the model that fits.",
    "<p>Before recommending an approach, Southern Point works to understand what's actually driving the need — a temporary spike, a structural gap, a project with a defined end date, or a longer-term capacity question. The workforce solution follows from that understanding, rather than defaulting to a single staffing model across every request.</p>",
    dark=True,
)}

<section>
<div class="container">
<div class="section-label">WHAT THIS INCLUDES</div>
<h2 class="section-title">A strategic view of workforce capacity.</h2>
<div class="editorial-list" style="margin-top:30px;">
{editorial_rows(WORKFORCE_ITEMS)}
</div>
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">INDUSTRIES WE SERVE</div>
<h2 class="section-title">Focused expertise across five areas.</h2>
{industries_line()}
</div>
</section>

<section style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">READY TO TALK IT THROUGH?</div>
<h2 class="section-title">Let's talk about your workforce needs.</h2>
<a class="btn btn-red" href="/contact/" style="margin-top:10px;">Discuss Your Workforce Needs</a>
</div>
</section>
"""

# =============================================================================
# /services/specialized-solutions/
# =============================================================================
SPECIALIZED_ITEMS = [
    "Specialized professionals",
    "Local resources",
    "Technical personnel",
    "Field personnel",
    "Vendors",
    "External service providers",
]

specialized_list = "\n".join(f"<li>{item}</li>" for item in SPECIALIZED_ITEMS)

specialized_body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/services/">Services</a><span>/</span>Specialized Solutions</div>
<div class="eyebrow eyebrow-light">SERVICES / SPECIALIZED SOLUTIONS</div>
<h1>When The Requirement Doesn't Fit A Standard Solution.</h1>
<p>Some projects and organizational needs call for resources beyond a standard staffing or professional-services engagement. Southern Point can coordinate appropriate resources when a requirement extends beyond an organization's existing capacity.</p>
</div>
</section>

{service_split(
    "services-specialized.jpg",
    "A specialized, hands-on work moment coordinated through Southern Point",
    "WHAT THIS CAN INCLUDE",
    "Coordination for requirements that don't fit a standard mold.",
    f'<ul style="color:var(--sp-muted); font-size:15px; line-height:2; padding-left:20px;">{specialized_list}</ul>',
)}

<section>
<div class="container">
<div class="card" style="max-width:800px;">
<div class="section-label">BEING CLEAR ABOUT WHAT THIS IS</div>
<p>Southern Point does not directly perform specialized field services such as electrical, construction, EV installation, or engineering work. When a requirement calls for that kind of expertise, we help identify and coordinate appropriate outside resources on your behalf — we don't claim to perform that work ourselves.</p>
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light); justify-content:center;">WHO THIS SERVES</div>
<h2 class="section-title" style="color:#fff; text-align:center;">Commercial, institutional, and government-adjacent organizations alike.</h2>
<p style="max-width:720px; margin:0 auto; text-align:center; color:#C7C1B3;">Southern Point's flexible delivery model is built to work across commercial businesses, healthcare and technology organizations, prime contractors, and other institutional clients — including government-related requirements, which Southern Point supports through direct inquiry and appropriate documentation rather than as its public-facing identity.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">RELATED FOCUS INDUSTRIES</div>
<h2 class="section-title">Specialized requirements often sit alongside these areas.</h2>
{industries_line()}
</div>
</section>

<section class="tint" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">HAVE A REQUIREMENT LIKE THIS?</div>
<h2 class="section-title">Let's talk through what you need.</h2>
<a class="btn btn-red" href="/contact/" style="margin-top:10px;">Discuss Your Requirement</a>
</div>
</section>
"""

PAGES = [
    ("services", hub_body, HUB_STYLE,
     "Services | Southern Point Workforce &amp; Professional Services",
     "Southern Point provides staffing and recruiting, professional services, workforce solutions, and specialized resource coordination for organizations nationwide.",
     "https://southernpointllc.com/services/", "services"),
    ("services/staffing-recruiting", staffing_body, SHARED_STYLE,
     "Staffing & Recruiting | Southern Point",
     "Southern Point provides temporary, temp-to-hire, direct hire, and contract staffing and recruiting across five focus industries.",
     "https://southernpointllc.com/services/staffing-recruiting/", "services"),
    ("services/professional-services", professional_body, SHARED_STYLE,
     "Professional Services | Southern Point",
     "Flexible administrative, operations, program, project, customer, and technical support resources for organizations that need additional capacity.",
     "https://southernpointllc.com/services/professional-services/", "services"),
    ("services/workforce-solutions", workforce_body, SHARED_STYLE,
     "Workforce Solutions | Southern Point",
     "Workforce planning, talent acquisition, workforce augmentation, and contract resources built around your organization's actual requirements.",
     "https://southernpointllc.com/services/workforce-solutions/", "services"),
    ("services/specialized-solutions", specialized_body, SHARED_STYLE,
     "Specialized Solutions | Southern Point",
     "Southern Point coordinates specialized professionals, local resources, and external service providers when a requirement extends beyond standard staffing.",
     "https://southernpointllc.com/services/specialized-solutions/", "services"),
]

for path, body_html, style, title, description, canonical, section in PAGES:
    html = build(
        title=title,
        description=description,
        extra_style=style,
        body_html=body_html,
        section=section,
        canonical=canonical,
    )
    out_dir = f"{BASE}/{path}"
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/index.html", "w") as f:
        f.write(html)
    print(f"wrote {path}/index.html")

# ---------------------------------------------------------------------------
# Redirect stub at the old /employers.html URL — the Staffing & Recruiting
# page at /services/staffing-recruiting/ is now canonical.
# ---------------------------------------------------------------------------
REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Staffing & Recruiting | Southern Point</title>
<meta http-equiv="refresh" content="0; url=/services/staffing-recruiting/">
<link rel="canonical" href="https://southernpointllc.com/services/staffing-recruiting/">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<p>This page has moved. If you are not redirected automatically, <a href="/services/staffing-recruiting/">click here to visit Staffing &amp; Recruiting</a>.</p>
</body>
</html>
"""

with open(f"{BASE}/employers.html", "w") as f:
    f.write(REDIRECT)
print("wrote employers.html (redirect stub)")
