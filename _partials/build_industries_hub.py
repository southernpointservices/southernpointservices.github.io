#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

INDUSTRIES = [
    ("Technology", "technology", "Technical support, systems, and application-support roles for technology-driven organizations."),
    ("Healthcare", "healthcare", "Administrative and operational staffing support for healthcare organizations — non-clinical roles."),
    ("Sales", "sales", "Sales development, account management, and business development talent across industries."),
    ("Operations", "operations", "Coordination, process, and logistics support that keeps day-to-day operations running."),
    ("Administrative", "administrative", "Administrative assistants, office coordinators, and front-office support at every level."),
]

STYLE = """
.industry-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
    margin-top:15px;
}

.industry-card{
    border:1px solid #E2D9C4;
    padding:0;
    overflow:hidden;
    transition:.2s ease;
    display:flex;
    flex-direction:column;
}

.industry-card:hover{
    border-color:#B8863E;
    transform:translateY(-3px);
}

.industry-card .visual-panel{
    aspect-ratio:16/10;
}

.industry-card-body{
    padding:26px;
    flex:1;
    display:flex;
    flex-direction:column;
}

.industry-card-body h3{
    font-size:19px;
    margin-bottom:10px;
}

.industry-card-body p{
    color:#5B5548;
    font-size:14px;
    flex:1;
}

.industry-card-body a{
    margin-top:16px;
    font-size:11px;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.6px;
    color:#B8863E;
}

@media(max-width:850px){
    .industry-grid{
        grid-template-columns:1fr 1fr;
    }
}

@media(max-width:560px){
    .industry-grid{
        grid-template-columns:1fr;
    }
}
"""

cards = "\n".join(f"""
<a href="/industries/{slug}/" class="industry-card">
<div class="visual-panel"><div class="visual-panel-graphic"></div></div>
<div class="industry-card-body">
<h3>{name}</h3>
<p>{desc}</p>
<span>Explore {name} Staffing &rarr;</span>
</div>
</a>""" for name, slug, desc in INDUSTRIES)

body = f"""
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">INDUSTRIES WE SERVE</div>
<h1>Staffing Built Around Your Industry.</h1>
<p>Southern Point focuses its recruiting and workforce support on five core areas — Technology, Healthcare, Sales, Operations, and Administrative — rather than trying to be a generalist staffing firm for every field. That focus is what lets us actually understand the roles we staff.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">EXPLORE BY INDUSTRY</div>
<h2 class="section-title">Five focus areas, staffed with real depth.</h2>
<p class="section-intro">Each industry page below covers the roles Southern Point commonly staffs, the challenges organizations in that space typically face, and how our process is built to address them.</p>
<div class="industry-grid">
{cards}
</div>
</div>
</section>

<section class="dark">
<div class="container split">
<div>
<div class="section-label">WHY INDUSTRY FOCUS MATTERS</div>
<h2 class="section-title">Depth beats a generic candidate pool.</h2>
<p>A staffing partner that tries to cover every industry equally usually understands none of them well. Southern Point staffs within five focus areas so that sourcing, screening, and candidate conversations are grounded in what the role actually requires — not a one-size-fits-all process.</p>
</div>
<div class="card">
<div class="section-label" style="color:#D8B67A;">DON'T SEE YOUR INDUSTRY?</div>
<h3 style="color:#fff;">Let's talk about it anyway.</h3>
<p>If your hiring need falls outside these five areas, reach out — Southern Point may still be able to help, or can point you in a useful direction.</p>
<a class="btn btn-outline-white" href="/contact/" style="margin-top:10px;">Contact Southern Point</a>
</div>
</div>
</section>

<section class="tint">
<div class="container" style="text-align:center;">
<div class="section-label" style="justify-content:center;">READY TO GET STARTED?</div>
<h2 class="section-title">Whichever side of the table you're on.</h2>
<div class="btn-row" style="justify-content:center;">
<a class="btn btn-red" href="/request-talent/">Request Talent</a>
<a class="btn btn-outline" href="/jobs.html">Find Jobs</a>
</div>
</div>
</section>
"""

html = build(
    title="Industries We Serve | Southern Point Staffing",
    description="Southern Point provides focused staffing support across five industries: Technology, Healthcare, Sales, Operations, and Administrative.",
    extra_style=STYLE,
    body_html=body,
    section="industries",
    canonical="https://southernpointllc.com/industries/",
)

with open(f"{BASE}/industries/index.html", "w") as f:
    f.write(html)

print("wrote industries hub")
