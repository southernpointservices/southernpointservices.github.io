#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

# ---------------------------------------------------------------------------
# Shared style additions used across the job-seekers pages
# ---------------------------------------------------------------------------
STYLE_HUB = """
.industries-line{
    font-size:16px;
    color:var(--sp-muted);
    max-width:640px;
    margin-top:16px;
}

.industries-line a{
    color:var(--sp-bronze-dark);
    font-weight:700;
    text-decoration:underline;
    text-underline-offset:3px;
}
"""

STYLE_HOW = """
.faq-wrap{margin-top:10px;}
"""

STYLE_RESOURCES = """
.editorial-row .res-list{
    margin:0;
    padding-left:18px;
    color:var(--sp-muted);
    font-size:14px;
    line-height:1.8;
}
"""

STYLE_SUBMIT = """
.submit-layout{
    display:grid;
    grid-template-columns:1fr 1.3fr;
    gap:60px;
    align-items:start;
}

.submit-side .step{margin-bottom:0;}

@media(max-width:900px){
    .submit-layout{grid-template-columns:1fr;}
}
"""

# ---------------------------------------------------------------------------
# /job-seekers/  (hub)
# ---------------------------------------------------------------------------
BENEFITS = [
    ("Real Conversations", "You'll talk to an actual person about the role, not just submit into a black box."),
    ("Roles Matched To You", "Southern Point places candidates against real requirements, not a keyword match."),
    ("No Cost To Apply", "Southern Point's services to job seekers are free — employers, not candidates, pay for staffing services."),
    ("Multiple Path Types", "Temporary, temp-to-hire, direct hire, and contract roles, so you can find the arrangement that fits your life."),
    ("Focused Industries", "Technology, Healthcare, Sales, Operations, and Administrative — roles our team actually understands."),
    ("Ongoing Support", "Southern Point stays reachable through onboarding, not just through the interview."),
]

INDUSTRIES = [
    ("Technology", "technology"), ("Healthcare", "healthcare"), ("Sales", "sales"),
    ("Operations", "operations"), ("Administrative", "administrative"),
]

def editorial_rows(items, start=1, dark=False):
    rows = []
    for i, (title, body) in enumerate(items, start=start):
        rows.append(f"""
<div class="editorial-row">
<div class="row-num">{i:02d}</div>
<div>
<h3{' style="color:#fff;"' if dark else ''}>{title}</h3>
<p>{body}</p>
</div>
</div>""")
    return f'<div class="editorial-list">{"".join(rows)}</div>'

def industries_line():
    links = ", ".join(f'<a href="/industries/{slug}/">{name}</a>' for name, slug in INDUSTRIES[:-1])
    last_name, last_slug = INDUSTRIES[-1]
    return f'<p class="industries-line">Southern Point places candidates across <a href="/industries/{INDUSTRIES[0][1]}/">{INDUSTRIES[0][0]}</a>, <a href="/industries/{INDUSTRIES[1][1]}/">{INDUSTRIES[1][0]}</a>, <a href="/industries/{INDUSTRIES[2][1]}/">{INDUSTRIES[2][0]}</a>, <a href="/industries/{INDUSTRIES[3][1]}/">{INDUSTRIES[3][0]}</a>, and <a href="/industries/{INDUSTRIES[4][1]}/">{INDUSTRIES[4][0]}</a>.</p>'

hub_body = f"""
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">FOR JOB SEEKERS</div>
<h1>Find Work That Actually Fits.</h1>
<p>Southern Point connects job seekers with temporary, temp-to-hire, direct hire, and contract opportunities across five focus industries — with a real person guiding the process, at no cost to you.</p>
<div class="btn-row" style="margin-top:10px;">
<a class="btn btn-red" href="/jobs.html">Find Jobs</a>
<a class="btn btn-outline-white" href="/submit-resume/">Submit Resume</a>
</div>
</div>
</section>

<section>
<div class="container">
<div class="photo-frame ratio-wide">
<img class="photo" src="/assets/images/homepage-candidates.jpg" alt="A candidate starting a new role placed by Southern Point">
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-label">WHY CANDIDATES WORK WITH US</div>
<h2 class="section-title">What you get working with Southern Point.</h2>
{editorial_rows(BENEFITS)}
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:#D8B67A;">HOW IT WORKS</div>
<h2 class="section-title" style="color:#fff;">A straightforward process, start to finish.</h2>
<p style="color:#C7C1B3; max-width:640px;">Search current openings or submit your resume for general consideration. From there, Southern Point reviews your background, has a real conversation with you about fit and goals, and presents you to opportunities that actually match — not a mass application blast.</p>
<a class="btn btn-outline-white" href="/job-seekers/how-it-works/" style="margin-top:20px;">See the Full Process</a>
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">EXPLORE BY INDUSTRY</div>
<h2 class="section-title">Opportunities across five focus areas.</h2>
{industries_line()}
</div>
</section>

<section>
<div class="container">
<div class="section-label">CANDIDATE RESOURCES</div>
<h2 class="section-title">Resume tips, interview prep, and more.</h2>
<p class="section-intro">Whether you're polishing a resume or prepping for an interview, Southern Point's candidate resources are built around what actually helps you land the right role.</p>
<a class="btn btn-outline" href="/job-seekers/resources/" style="margin-top:16px;">View Candidate Resources</a>
</div>
</section>

<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">READY TO GET STARTED?</div>
<h2 class="section-title">Search current openings or submit your resume.</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/jobs.html">Find Jobs</a>
<a class="btn btn-outline-white" href="/submit-resume/">Submit Resume</a>
</div>
</div>
</section>
"""

# ---------------------------------------------------------------------------
# /job-seekers/how-it-works/
# ---------------------------------------------------------------------------
FAQS = [
    ("Does it cost anything to work with Southern Point?", "No. Southern Point's services to candidates are free. Employers pay for staffing services, not job seekers."),
    ("What kinds of roles does Southern Point place?", "Temporary, temp-to-hire, direct hire, and contract roles across five focus areas: Technology, Healthcare, Sales, Operations, and Administrative."),
    ("Do I need to apply to a specific job to get started?", "No. You can apply to a current opening on the Find Jobs page, or submit your resume for general consideration and Southern Point will reach out about relevant matches."),
    ("How long does the process take?", "It depends on the role and how quickly a matching opportunity comes up. Southern Point aims to follow up on every submission within a few business days."),
    ("Will someone actually contact me?", "Yes. A member of the Southern Point team reviews submissions and reaches out directly rather than relying on automated screening alone."),
]

def faq_html():
    out = []
    for q, a in FAQS:
        out.append(f"""
<div class="faq-item">
<div class="faq-question"><span>{q}</span><span class="faq-icon">+</span></div>
<div class="faq-answer"><p>{a}</p></div>
</div>""")
    return "\n".join(out)

how_body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/job-seekers/">For Job Seekers</a><span>/</span>How It Works</div>
<div class="eyebrow eyebrow-light">FOR JOB SEEKERS</div>
<h1>How The Process Works.</h1>
<p>From first submission to your first day, here's what to expect when you work with Southern Point.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">THE PROCESS</div>
<h2 class="section-title">Five steps, start to finish.</h2>
<div class="process-grid">
<div class="step"><div class="step-number">01</div><h3>You Apply</h3><p>Apply to a current opening or submit your resume for general consideration.</p></div>
<div class="step"><div class="step-number">02</div><h3>We Review</h3><p>A recruiter reviews your background against current and upcoming openings.</p></div>
<div class="step"><div class="step-number">03</div><h3>We Talk</h3><p>If there's a potential fit, we reach out to talk through the role and your goals.</p></div>
<div class="step"><div class="step-number">04</div><h3>We Present You</h3><p>Southern Point presents your background to the employer for roles that fit.</p></div>
<div class="step"><div class="step-number">05</div><h3>You Get Hired</h3><p>If it's a match, we help coordinate offer details, onboarding, and your start date.</p></div>
</div>
</div>
</section>

<section>
<div class="container split">
<div>
<div class="section-label">WHAT TO EXPECT</div>
<h2 class="section-title">A real process, not a black box.</h2>
<p class="section-intro">Southern Point reviews every submission individually. If your background doesn't match a current opening, it stays on file for future roles that fit — you don't need to reapply every time a new position opens.</p>
<a class="btn btn-outline" href="/submit-resume/" style="margin-top:16px;">Submit Your Resume</a>
</div>
<div class="photo-frame ratio-landscape">
<img class="photo" src="/assets/images/homepage-candidates.jpg" alt="A candidate meeting with a Southern Point recruiter">
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-label">COMMON QUESTIONS</div>
<h2 class="section-title">Frequently asked questions.</h2>
<div class="faq-wrap">
{faq_html()}
</div>
</div>
</section>

<section class="tint" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">READY WHEN YOU ARE</div>
<h2 class="section-title">Take the next step.</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/jobs.html">Find Jobs</a>
<a class="btn btn-outline" href="/submit-resume/">Submit Resume</a>
</div>
</div>
</section>
"""

# ---------------------------------------------------------------------------
# /job-seekers/resources/
# ---------------------------------------------------------------------------
RESOURCE_SECTIONS = [
    ("Resume Tips", [
        "Lead with measurable results (numbers, scope, outcomes) instead of just listing duties.",
        "Match your resume language to the role — mirror key terms from the job description where genuinely accurate.",
        "Keep formatting clean and consistent; most resumes are scanned quickly before being read closely.",
        "List the most relevant experience first, even if it means reordering roles by relevance rather than strict date order.",
    ]),
    ("Interview Preparation", [
        "Research the company and the specific role, not just the industry in general.",
        "Prepare two or three concrete examples that show how you've handled real challenges.",
        "Bring thoughtful questions about the role, team, and expectations — not just about pay and schedule.",
        "Follow up with a short, genuine thank-you note within a day of the interview.",
    ]),
    ("What To Expect From Southern Point", [
        "A recruiter will review your background and reach out if there's a potential fit.",
        "You'll have a real conversation about the role, timeline, and your goals before anything moves forward.",
        "There is no cost to you at any point in the process.",
        "Your information stays on file for future opportunities, even if the first conversation doesn't lead to a placement.",
    ]),
    ("Staying Ready Between Roles", [
        "Keep your resume updated even when you're not actively searching.",
        "Stay reachable — missed calls and full voicemail boxes cost candidates real opportunities.",
        "Be direct with your recruiter about availability, must-haves, and deal-breakers so time isn't wasted on either side.",
        "Revisit the Find Jobs page periodically — new openings are added as employers submit them.",
    ]),
]

def resource_rows():
    rows = []
    for i, (title, items) in enumerate(RESOURCE_SECTIONS, start=1):
        lis = "\n".join(f"<li>{item}</li>" for item in items)
        rows.append(f"""
<div class="editorial-row">
<div class="row-num">{i:02d}</div>
<div>
<h3>{title}</h3>
<ul class="res-list">
{lis}
</ul>
</div>
</div>""")
    return f'<div class="editorial-list">{"".join(rows)}</div>'

resources_body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/job-seekers/">For Job Seekers</a><span>/</span>Resources</div>
<div class="eyebrow eyebrow-light">FOR JOB SEEKERS</div>
<h1>Candidate Resources.</h1>
<p>Practical guidance for resumes, interviews, and staying prepared between roles.</p>
</div>
</section>

<section>
<div class="container">
{resource_rows()}
</div>
</section>

<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">PUT IT INTO ACTION</div>
<h2 class="section-title">Ready to take the next step?</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/jobs.html">Find Jobs</a>
<a class="btn btn-outline-white" href="/submit-resume/">Submit Resume</a>
</div>
</div>
</section>
"""

# ---------------------------------------------------------------------------
# /job-seekers/submit-resume/
# ---------------------------------------------------------------------------
submit_body = """
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span>Submit Resume</div>
<div class="eyebrow eyebrow-light">FOR JOB SEEKERS</div>
<h1>Submit Your Resume.</h1>
<p>Don't see the right opening today? Submit your resume for general consideration and Southern Point will reach out when a matching opportunity comes up.</p>
</div>
</section>

<section>
<div class="container submit-layout">

<div class="submit-side">
<div class="section-label">WHAT HAPPENS NEXT</div>
<div class="process-grid" style="grid-template-columns:1fr;">
<div class="step">
<div class="step-number">01</div>
<h3>We Review Your Background</h3>
<p>A recruiter reviews your resume against current and upcoming openings.</p>
</div>
<div class="step">
<div class="step-number">02</div>
<h3>We Reach Out</h3>
<p>If there's a potential fit, we'll contact you to talk through the role and your goals.</p>
</div>
<div class="step">
<div class="step-number">03</div>
<h3>You Stay On File</h3>
<p>Even without an immediate match, your information stays on file for future openings.</p>
</div>
</div>

<div style="margin-top:36px; padding-top:28px; border-top:1px solid var(--sp-line-dark);">
<div class="section-label">PREFER TO APPLY DIRECTLY?</div>
<p>Browse current openings and apply to a specific role instead.</p>
<a href="/jobs.html" style="display:inline-block; margin-top:12px; font-weight:800; color:#B8863E;">View Current Openings &rarr;</a>
</div>
</div>

<div class="form-card">
<form
id="submitResumeForm"
action="https://formsubmit.co/southernpoint.services@gmail.com"
method="POST"
enctype="multipart/form-data">

<input type="hidden" name="_subject" value="Resume Submission — Southern Point">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://southernpointllc.com/submit-resume/?submitted=1">
<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">

<div class="section-label">YOUR INFORMATION</div>

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

<div class="form-row">
<div>
<label class="form-label">Phone</label>
<input class="form-input" type="tel" name="Phone" required>
</div>
<div>
<label class="form-label">Location</label>
<input class="form-input" type="text" name="Location" placeholder="City, State" required>
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
<label class="form-label">Current or Most Recent Title</label>
<input class="form-input" type="text" name="Current Title" required>
</div>
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
</div>

<label class="form-label">Resume (PDF or Word)</label>
<input class="form-input" type="file" name="Resume" accept=".pdf,.doc,.docx" required>

<label class="form-label">Anything Else We Should Know?</label>
<textarea class="form-textarea" name="Additional Notes" rows="4" placeholder="Availability, certifications, schedule preferences, or anything else worth sharing."></textarea>

<label class="form-consent">
<input type="checkbox" required>
I consent to Southern Point contacting me regarding potential job opportunities.
</label>

<button type="submit" class="btn btn-block">Submit Resume</button>

<p class="form-note">There is no cost to submit your resume or to work with Southern Point as a candidate.</p>

</form>
</div>

</div>
</section>
"""

# ---------------------------------------------------------------------------
# write pages
# ---------------------------------------------------------------------------
pages = [
    ("job-seekers", hub_body, STYLE_HUB,
     "For Job Seekers | Southern Point Staffing",
     "Search current openings or submit your resume for general consideration. Southern Point connects job seekers with temporary, temp-to-hire, direct hire, and contract roles at no cost.",
     "https://southernpointllc.com/job-seekers/"),
    ("job-seekers/how-it-works", how_body, STYLE_HOW,
     "How It Works | Southern Point Job Seekers",
     "Here's exactly what happens after you apply or submit your resume to Southern Point, from initial review through your first day.",
     "https://southernpointllc.com/job-seekers/how-it-works/"),
    ("job-seekers/resources", resources_body, STYLE_RESOURCES,
     "Candidate Resources | Southern Point Job Seekers",
     "Practical resume tips, interview preparation guidance, and advice for staying ready between roles.",
     "https://southernpointllc.com/job-seekers/resources/"),
]

# submit-resume now lives at the top-level /submit-resume/ path — see
# build_submit_resume.py, which imports submit_body/STYLE_SUBMIT from here
# and also writes a redirect stub at the old /job-seekers/submit-resume/ URL.

for path, body_html, style, title, description, canonical in pages:
    html = build(
        title=title,
        description=description,
        extra_style=style,
        body_html=body_html,
        section="job-seekers",
        canonical=canonical,
    )
    out_dir = f"{BASE}/{path}"
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/index.html", "w") as f:
        f.write(html)
    print(f"wrote {path}/index.html")
