#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
.solutions-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
    margin-top:15px;
}

.solution-card h3{
    font-size:19px;
}

.industries-strip{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:14px;
    margin-top:25px;
}

.industry-chip{
    border:1px solid #E2D9C4;
    padding:20px 16px;
    text-align:center;
    font-weight:800;
    font-size:13px;
    transition:.2s ease;
}

.industry-chip:hover{
    border-color:#B8863E;
    color:#B8863E;
    transform:translateY(-2px);
}

@media(max-width:850px){
    .solutions-grid{
        grid-template-columns:1fr 1fr;
    }
    .industries-strip{
        grid-template-columns:repeat(2,1fr);
    }
}

@media(max-width:560px){
    .solutions-grid{
        grid-template-columns:1fr;
    }
}
"""

SOLUTIONS = [
    ("Temporary Staffing", "Short-term coverage for leave, seasonal volume, or unexpected gaps — without a permanent commitment."),
    ("Temp-to-Hire", "Bring a candidate on temporarily and convert to a permanent hire once you've confirmed the fit."),
    ("Direct Hire", "Southern Point sources and screens candidates for permanent roles you hire directly."),
    ("Contract Staffing", "Project-based and fixed-term engagements for defined scopes of work."),
    ("High-Volume Staffing", "Coordinated sourcing and screening when you need to fill multiple similar roles at once."),
    ("Workforce Solutions", "Ongoing, flexible workforce support structured around how your organization actually operates."),
]

WHY = [
    ("Candidate Sourcing", "Southern Point sources candidates against the specific role, not a generic applicant pool."),
    ("Structured Screening", "Every candidate is screened for relevant experience and fit before you ever see a resume."),
    ("Speed", "A streamlined process means less time between identifying a need and having qualified candidates to consider."),
    ("Industry Knowledge", "Focused work across Technology, Healthcare, Sales, Operations, and Administrative roles — not every field at once."),
    ("Workforce Flexibility", "Temporary, temp-to-hire, direct hire, and contract models mean the engagement fits the need, not the other way around."),
    ("Ongoing Partnership", "Southern Point stays engaged after placement rather than disappearing once a candidate starts."),
]

INDUSTRIES = [
    ("Technology", "technology"), ("Healthcare", "healthcare"), ("Sales", "sales"),
    ("Operations", "operations"), ("Administrative", "administrative"),
]

def solution_cards():
    out = []
    for i, (title, body) in enumerate(SOLUTIONS, start=1):
        out.append(f"""
<div class="card solution-card">
<div class="card-number">0{i}</div>
<h3>{title}</h3>
<p>{body}</p>
</div>""")
    return "\n".join(out)

def why_cards():
    out = []
    for i, (title, body) in enumerate(WHY, start=1):
        out.append(f"""
<div class="card">
<div class="card-number">0{i}</div>
<h3>{title}</h3>
<p>{body}</p>
</div>""")
    return "\n".join(out)

def industry_chips():
    return "\n".join(f'<a class="industry-chip" href="/industries/{slug}/">{name}</a>' for name, slug in INDUSTRIES)

body = f"""
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">FOR EMPLOYERS</div>
<h1>Great Companies Start With Great People.</h1>
<p>Southern Point provides talent acquisition, recruiting, and workforce solutions built around how your organization actually hires — not a one-size-fits-all staffing process.</p>
<div class="btn-row" style="margin-top:10px;">
<a class="btn btn-red" href="/request-talent/">Request Talent</a>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-label">STAFFING SOLUTIONS</div>
<h2 class="section-title">Different needs call for different engagements.</h2>
<p class="section-intro">Southern Point structures every engagement around the role and timeline, not a single fixed service.</p>
<div class="solutions-grid">
{solution_cards()}
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label">WHY SOUTHERN POINT</div>
<h2 class="section-title">What organizations get by working with us.</h2>
<div class="grid-3">
{why_cards()}
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

<section class="tint">
<div class="container">
<div class="section-label">INDUSTRIES WE SERVE</div>
<h2 class="section-title">Focused expertise across five areas.</h2>
<div class="industries-strip">
{industry_chips()}
</div>
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

html = build(
    title="For Employers | Southern Point Staffing Solutions",
    description="Southern Point provides talent acquisition, recruiting, and workforce solutions for organizations — temporary, temp-to-hire, direct hire, and contract staffing across five industries.",
    extra_style=STYLE,
    body_html=body,
    section="employers",
    canonical="https://southernpointllc.com/employers.html",
)

with open(f"{BASE}/employers.html", "w") as f:
    f.write(html)

print("wrote employers.html")
