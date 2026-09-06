#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
.values-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
    margin-top:15px;
}

.leader-card{
    display:flex;
    gap:26px;
    align-items:center;
    padding:32px;
}

.leader-mark{
    flex-shrink:0;
    width:96px;
    height:96px;
    border-radius:50%;
    background:linear-gradient(155deg,#15171E 0%,#B8863E 130%);
    color:#fff;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:900;
    font-size:28px;
    letter-spacing:1px;
}

.leader-name{
    font-size:19px;
    font-weight:800;
    margin-bottom:3px;
}

.leader-title{
    color:#D8B67A;
    font-size:13px;
    font-weight:700;
}

.leader-note{
    color:#CFC9BB;
    margin-top:10px;
    max-width:560px;
    font-size:14px;
}

@media(max-width:850px){
    .values-grid{grid-template-columns:1fr 1fr;}
}

@media(max-width:560px){
    .values-grid{grid-template-columns:1fr;}
    .leader-card{flex-direction:column; text-align:center;}
}
"""

VALUES = [
    ("Real Relationships", "Southern Point works to actually understand the people and organizations it serves, rather than treating either side as a transaction."),
    ("Honesty Over Hype", "If a role or a candidate isn't a fit, Southern Point says so directly instead of pushing a placement that won't last."),
    ("Responsiveness", "Hiring moves fast. Southern Point aims to follow up quickly with both employers and candidates rather than letting momentum stall."),
    ("Focused Expertise", "Rather than staffing every industry at once, Southern Point concentrates on Technology, Healthcare, Sales, Operations, and Administrative roles — areas the team can genuinely understand."),
    ("Accountability", "Southern Point stays engaged after a placement is made, rather than disappearing once a candidate starts."),
    ("Long-Term Thinking", "The goal is a placement that works months and years later — not just a quick fill."),
]

def value_cards():
    out = []
    for i, (title, body) in enumerate(VALUES, start=1):
        out.append(f"""
<div class="card">
<div class="card-number">0{i}</div>
<h3>{title}</h3>
<p>{body}</p>
</div>""")
    return "\n".join(out)

body = f"""
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">ABOUT SOUTHERN POINT</div>
<h1>Staffing, Done The Way It Should Be.</h1>
<p>Southern Point is a Houston-based staffing and recruiting company serving organizations and job seekers nationwide — built around real conversations and focused industry expertise rather than a high-volume, one-size-fits-all approach.</p>
</div>
</section>

<section>
<div class="container split">
<div>
<div class="section-label">WHO WE ARE</div>
<h2 class="section-title">A staffing partner built to actually know the roles it fills.</h2>
<p>Southern Point Professional Services connects organizations with qualified talent across five focus industries: Technology, Healthcare, Sales, Operations, and Administrative. Rather than trying to cover every industry at once, Southern Point stays focused so that sourcing, screening, and candidate conversations are grounded in what a role actually requires.</p>
<p style="margin-top:14px;">Southern Point works with employers across temporary, temp-to-hire, direct hire, and contract staffing models, and works with job seekers at no cost to them — employers, not candidates, pay for staffing services.</p>
</div>
<div class="visual-panel"><div class="visual-panel-mark">Southern Point</div></div>
</div>
</section>

<section class="dark">
<div class="container split">
<div class="visual-panel tone-light"><div class="visual-panel-mark">Our Approach</div></div>
<div>
<div class="section-label" style="color:#D8B67A;">OUR APPROACH</div>
<h2 class="section-title">Real conversations, not a keyword match.</h2>
<p>Every engagement starts with an actual conversation — with the employer about the role and the team, and with the candidate about their background and goals. Southern Point structures each engagement type (temporary, temp-to-hire, direct hire, or contract) around what the situation actually calls for, then stays involved through onboarding rather than stepping away once a placement is made.</p>
</div>
</div>
</section>

<section class="tint">
<div class="container" style="text-align:center; max-width:780px; margin-left:auto; margin-right:auto;">
<div class="section-label" style="justify-content:center;">OUR MISSION</div>
<h2 class="section-title">Connect the right people with the right opportunities — and stay accountable for the outcome.</h2>
<p class="section-intro">Southern Point measures success by placements that last, not just placements that happen.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">OUR VALUES</div>
<h2 class="section-title">What guides how Southern Point operates.</h2>
<div class="values-grid">
{value_cards()}
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:#D8B67A;">LEADERSHIP</div>
<h2 class="section-title">Led directly, not layered.</h2>
<div class="card leader-card" style="margin-top:10px;">
<div class="leader-mark">DH</div>
<div>
<div class="leader-name">DeJaun Henry Jr.</div>
<div class="leader-title">Founder, Southern Point Professional Services</div>
<p class="leader-note">Southern Point is operated directly by its founder, keeping the staffing process hands-on and accountable rather than routed through layers of account managers.</p>
</div>
</div>
</div>
</section>

<section class="tint" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">LET'S WORK TOGETHER</div>
<h2 class="section-title">Whether you're hiring or looking to be hired.</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/request-talent/">Request Talent</a>
<a class="btn btn-outline" href="/jobs.html">Find Jobs</a>
</div>
</div>
</section>
"""

html = build(
    title="About Southern Point | Staffing & Recruiting",
    description="Southern Point is a Houston-based staffing and recruiting company serving organizations and job seekers nationwide across five focus industries.",
    extra_style=STYLE,
    body_html=body,
    section="about",
    canonical="https://southernpointllc.com/about/",
)

import os
os.makedirs(f"{BASE}/about", exist_ok=True)
with open(f"{BASE}/about/index.html", "w") as f:
    f.write(html)

print("wrote about/index.html")
