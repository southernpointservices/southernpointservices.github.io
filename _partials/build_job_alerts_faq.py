#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

# ---------------------------------------------------------------------------
# /job-alerts/
# ---------------------------------------------------------------------------
STYLE_ALERTS = """
.alerts-layout{
    display:grid;
    grid-template-columns:1fr 1.2fr;
    gap:60px;
    align-items:start;
}

@media(max-width:900px){
    .alerts-layout{grid-template-columns:1fr;}
}
"""

alerts_body = """
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span>Job Alerts</div>
<div class="eyebrow eyebrow-light">FOR JOB SEEKERS</div>
<h1>Get Notified About New Openings.</h1>
<p>Tell us what you're looking for and a member of the Southern Point team will personally reach out when a matching opportunity is posted &mdash; no account required, and no cost to candidates.</p>
</div>
</section>

<section>
<div class="container alerts-layout">

<div>
<div class="section-label">HOW JOB ALERTS WORK</div>
<div class="process-grid" style="grid-template-columns:1fr;">
<div class="step">
<div class="step-number">01</div>
<h3>You Tell Us What You Want</h3>
<p>Industry, role type, location, and work arrangement &mdash; whatever matters most to your search.</p>
</div>
<div class="step">
<div class="step-number">02</div>
<h3>We Watch For A Match</h3>
<p>When a new opening fits what you're looking for, a real person on our team reaches out directly.</p>
</div>
<div class="step">
<div class="step-number">03</div>
<h3>You Decide What's Next</h3>
<p>No obligation &mdash; you choose whether to move forward on any opportunity we flag for you.</p>
</div>
</div>

<div style="margin-top:36px; padding-top:28px; border-top:1px solid var(--sp-line-dark);">
<div class="section-label">DON'T WANT TO WAIT?</div>
<p>Browse current openings right now instead of waiting for a match.</p>
<a href="/jobs.html" style="display:inline-block; margin-top:12px; font-weight:800; color:var(--sp-bronze-dark);">View Current Openings &rarr;</a>
</div>
</div>

<div class="form-card">
<form
action="https://formsubmit.co/contact@southernpointllc.com"
method="POST">

<input type="hidden" name="_subject" value="Job Alert Signup — Southern Point">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://southernpointllc.com/job-alerts/?submitted=1">
<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">

<div class="section-label">YOUR ALERT PREFERENCES</div>

<div class="form-row">
<div>
<label class="form-label first">Full Name</label>
<input class="form-input" type="text" name="Full Name" required>
</div>
<div>
<label class="form-label first">Email</label>
<input class="form-input" type="email" name="Email" required>
</div>
</div>

<label class="form-label">Industry of Interest</label>
<select class="form-select" name="Industry of Interest" required>
<option value="">Select an industry</option>
<option>Technology</option>
<option>Healthcare</option>
<option>Sales</option>
<option>Operations</option>
<option>Administrative</option>
<option>Not sure / open to options</option>
</select>

<div class="form-row">
<div>
<label class="form-label">Desired Role Type</label>
<select class="form-select" name="Desired Role Type" required>
<option value="">Select a role type</option>
<option>Temporary</option>
<option>Temp-to-Hire</option>
<option>Direct Hire</option>
<option>Contract</option>
<option>Open to any</option>
</select>
</div>
<div>
<label class="form-label">Preferred Location</label>
<input class="form-input" type="text" name="Preferred Location" placeholder="City, State, or Remote" required>
</div>
</div>

<label class="form-label">Anything Else We Should Know?</label>
<textarea class="form-textarea" name="Additional Notes" rows="3" placeholder="Specific job titles, must-haves, or availability."></textarea>

<label class="form-consent">
<input type="checkbox" required>
I consent to Southern Point contacting me about matching job opportunities.
</label>

<button type="submit" class="btn btn-block">Sign Up For Job Alerts</button>

<p class="form-note">There is no cost to sign up, and no obligation to apply to anything we send your way.</p>

</form>
</div>

</div>
</section>

<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center; color:var(--sp-bronze-light);">PREFER TO SEARCH NOW?</div>
<h2 class="section-title" style="color:#fff;">Current openings are always open to browse.</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/jobs.html">Find Jobs</a>
<a class="btn btn-outline-white" href="/submit-resume/">Submit Resume</a>
</div>
</div>
</section>
"""

# ---------------------------------------------------------------------------
# /faq/  (general, both audiences)
# ---------------------------------------------------------------------------
STYLE_FAQ = """
.faq-tabs{
    display:flex;
    gap:12px;
    margin-bottom:10px;
    flex-wrap:wrap;
}

.faq-tab-label{
    font-size:11px;
    font-weight:800;
    letter-spacing:1px;
    text-transform:uppercase;
    color:var(--sp-bronze-dark);
    background:#ffffff;
    border:1px solid var(--sp-ink);
    padding:7px 13px;
    display:inline-block;
    margin-bottom:16px;
}
"""

CANDIDATE_FAQS = [
    ("Does it cost anything to work with Southern Point as a candidate?", "No. Southern Point's services to candidates are always free. Employers pay for staffing services, not job seekers."),
    ("What kinds of roles does Southern Point place?", "Temporary, temp-to-hire, direct hire, and contract roles across five focus areas: Technology, Healthcare, Sales, Operations, and Administrative."),
    ("Do I need to apply to a specific job to get started?", "No. You can apply to a current opening on the Find Jobs page, submit your resume for general consideration, or sign up for job alerts."),
    ("Will a real person actually contact me?", "Yes. A member of the Southern Point team reviews every submission and reaches out directly rather than relying on automated screening alone."),
]

EMPLOYER_FAQS = [
    ("How does Southern Point charge for staffing services?", "Southern Point is paid by the employer, based on the engagement type and role. Reach out through Request Talent for specifics on your situation."),
    ("What engagement models are available?", "Temporary, temp-to-hire, direct hire, and contract staffing &mdash; structured around the role and timeline rather than a single fixed process."),
    ("How quickly can Southern Point start sourcing candidates?", "Southern Point typically follows up on a new request within one business day to discuss the role, timeline, and next steps."),
    ("What industries does Southern Point serve?", "Southern Point focuses on five industries: Technology, Healthcare, Sales, Operations, and Administrative &mdash; deliberately, rather than trying to cover every field."),
]

GENERAL_FAQS = [
    ("Where is Southern Point located?", "Southern Point is headquartered in Houston, Texas, and serves organizations and candidates nationwide."),
    ("How do I get in touch with Southern Point?", "Use the Contact page, or the Request Talent and Submit Resume forms depending on whether you're hiring or looking for work."),
]

def faq_group(items):
    out = []
    for q, a in items:
        out.append(f"""
<div class="faq-item">
<div class="faq-question"><span>{q}</span><span class="faq-icon">+</span></div>
<div class="faq-answer"><p>{a}</p></div>
</div>""")
    return "\n".join(out)

faq_body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span>FAQs</div>
<div class="eyebrow eyebrow-light">FREQUENTLY ASKED QUESTIONS</div>
<h1>Questions, Answered.</h1>
<p>Common questions from candidates and employers about how Southern Point works. Have something else on your mind? <a href="/contact/" style="color:#fff; text-decoration:underline;">Reach out directly</a>.</p>
</div>
</section>

<section>
<div class="container">
<span class="faq-tab-label">FOR CANDIDATES</span>
<div class="faq-wrap">
{faq_group(CANDIDATE_FAQS)}
</div>
</div>
</section>

<section class="tint">
<div class="container">
<span class="faq-tab-label">FOR EMPLOYERS</span>
<div class="faq-wrap">
{faq_group(EMPLOYER_FAQS)}
</div>
</div>
</section>

<section>
<div class="container">
<span class="faq-tab-label">GENERAL</span>
<div class="faq-wrap">
{faq_group(GENERAL_FAQS)}
</div>
</div>
</section>

<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center; color:var(--sp-bronze-light);">STILL HAVE QUESTIONS?</div>
<h2 class="section-title" style="color:#fff;">Let's talk it through.</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/contact/">Contact Southern Point</a>
</div>
</div>
</section>
"""

pages = [
    ("job-alerts", alerts_body, STYLE_ALERTS,
     "Job Alerts | Southern Point Staffing",
     "Sign up for job alerts and Southern Point will personally reach out when a matching opportunity is posted — no cost, no account required.",
     "https://southernpointllc.com/job-alerts/",
     "job-seekers"),
    ("faq", faq_body, STYLE_FAQ,
     "FAQs | Southern Point Staffing",
     "Answers to common questions from candidates and employers about how Southern Point's staffing and recruiting process works.",
     "https://southernpointllc.com/faq/",
     "resources"),
]

for path, body_html, style, title, description, canonical, section in pages:
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
