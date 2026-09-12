#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
.leader-block{
    max-width:640px;
}

.leader-name{
    font-family:var(--font-display);
    font-size:clamp(24px,2.6vw,30px);
    color:#fff;
    margin-bottom:4px;
}

.leader-title{
    color:#D8B67A;
    font-size:13px;
    font-weight:700;
    letter-spacing:.4px;
    text-transform:uppercase;
    margin-bottom:18px;
}

.leader-note{
    color:#CFC9BB;
    font-size:16px;
}

.word-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:0;
    margin-top:20px;
}

.word-item{
    padding:0 28px;
    border-left:1px solid var(--sp-line-dark);
}

.word-item:first-child{
    border-left:none;
    padding-left:0;
}

.word-item strong{
    display:block;
    font-family:var(--font-display);
    font-size:clamp(28px,3vw,38px);
    color:var(--sp-bronze-light);
    letter-spacing:-1px;
    margin-bottom:12px;
}

.word-item p{
    color:#C7C1B3;
    font-size:14px;
}

@media(max-width:900px){
    .word-grid{grid-template-columns:1fr 1fr; row-gap:34px;}
    .word-item{border-left:none; padding-left:0; padding-right:0;}
    .word-item:nth-child(odd){padding-right:20px;}
    .word-item:nth-child(even){padding-left:20px; border-left:1px solid var(--sp-line-dark);}
}
@media(max-width:560px){
    .word-grid{grid-template-columns:1fr; row-gap:28px;}
    .word-item:nth-child(even){border-left:none; padding-left:0;}
}
"""

WHY = [
    ("Responsive", "Clear communication and timely follow-through."),
    ("Flexible", "Solutions designed around actual organizational requirements."),
    ("Resourceful", "Access to qualified talent and specialized resources."),
    ("Accountable", "Engaged from initial requirement through delivery."),
]

def why_items():
    out = []
    for title, body in WHY:
        out.append(f"""
<div class="word-item">
<strong>{title}.</strong>
<p>{body}</p>
</div>""")
    return "\n".join(out)

VALUES = [
    ("Real Relationships", "Southern Point works to actually understand the people and organizations it serves, rather than treating either side as a transaction."),
    ("Honesty Over Hype", "If a role or a candidate isn't a fit, Southern Point says so directly instead of pushing a placement that won't last."),
    ("Responsiveness", "Hiring moves fast. Southern Point aims to follow up quickly with both employers and candidates rather than letting momentum stall."),
    ("Focused Expertise", "Rather than staffing every industry at once, Southern Point concentrates on Technology, Healthcare, Sales, Operations, and Administrative roles — areas the team can genuinely understand."),
    ("Accountability", "Southern Point stays engaged after a placement is made, rather than disappearing once a candidate starts."),
    ("Long-Term Thinking", "The goal is a placement that works months and years later — not just a quick fill."),
]

def value_rows():
    rows = []
    for i, (title, body) in enumerate(VALUES, start=1):
        rows.append(f"""
<div class="editorial-row">
<div class="row-num">{i:02d}</div>
<div class="row-body">
<h3>{title}</h3>
<p>{body}</p>
</div>
</div>""")
    return f'<div class="editorial-list">{"".join(rows)}</div>'

body = f"""
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">ABOUT SOUTHERN POINT</div>
<h1>Workforce. Professional Services. Solutions.</h1>
<p>Southern Point is a Houston-based workforce and professional services company serving organizations and job seekers nationwide — built around real conversations and focused expertise rather than a high-volume, one-size-fits-all approach.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">WHO WE ARE</div>
<h2 class="section-title" style="max-width:760px;">A partner built to actually understand what you need.</h2>
<p class="section-intro" style="max-width:760px;">Southern Point Professional Services helps organizations access the people, support, and resources they need to move forward — through staffing and recruiting, professional services, workforce solutions, and specialized resource coordination. Southern Point is built to grow into additional service areas over time, starting from what the business can genuinely deliver today.</p>
<p class="section-intro" style="margin-top:14px; max-width:760px;">Across five focus industries — Technology, Healthcare, Sales, Operations, and Administrative — Southern Point works with employers across temporary, temp-to-hire, direct hire, and contract engagement models, and works with job seekers at no cost to them — employers, not candidates, pay for staffing services.</p>
</div>
</section>

<section class="dark" id="approach">
<div class="container">
<p class="statement-xl" style="max-width:840px;">Understand the requirement, <span class="accent">then</span> build the right solution.</p>
<p class="section-intro" style="margin-top:24px; max-width:640px;">Every engagement starts with an actual conversation — understanding what an organization actually needs before recommending an approach. Southern Point structures each engagement around what the situation actually calls for, whether that's a staffing placement, professional support, a broader workforce solution, or coordinating a more specialized resource, then stays involved through delivery rather than stepping away once the work begins.</p>
</div>
</section>

<section id="why" class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">WHY SOUTHERN POINT</div>
<h2 class="section-title" style="color:#fff;">What guides how we work.</h2>
<div class="word-grid">
{why_items()}
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
{value_rows()}
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:#D8B67A;">LEADERSHIP</div>
<h2 class="section-title" style="color:#fff;">Led directly, not layered.</h2>
<div class="leader-block" style="margin-top:22px;">
<div class="leader-name">DeJaun Henry Jr.</div>
<div class="leader-title">Founder, Southern Point Professional Services</div>
<p class="leader-note">Southern Point is operated directly by its founder, keeping the staffing process hands-on and accountable rather than routed through layers of account managers.</p>
</div>
</div>
</section>

<section class="tint" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">LET'S WORK TOGETHER</div>
<h2 class="section-title">Whether you're hiring or looking to be hired.</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/request-talent/">Find Talent</a>
<a class="btn btn-outline" href="/jobs.html">Find Jobs</a>
</div>
</div>
</section>
"""

html = build(
    title="About Southern Point | Workforce & Professional Services",
    description="Southern Point is a Houston-based workforce and professional services company helping organizations and job seekers nationwide across five focus industries.",
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
