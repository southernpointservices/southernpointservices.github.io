#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
.opp-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:1px;
    background:var(--sp-line);
    border:1px solid var(--sp-line);
    margin-top:30px;
}

.opp-card{
    background:#ffffff;
    padding:32px 30px;
    display:flex;
    flex-direction:column;
    transition:background-color .2s ease;
}

.opp-card:hover{
    background:#FAF7F1;
}

.opp-status{
    display:inline-flex;
    align-items:center;
    gap:7px;
    font-size:11px;
    font-weight:700;
    letter-spacing:.4px;
    text-transform:uppercase;
    color:var(--sp-muted-2);
    margin-top:auto;
    padding-top:18px;
}

.opp-status::before{
    content:"";
    width:6px;
    height:6px;
    background:var(--sp-muted-2);
    border-radius:50%;
    flex-shrink:0;
}

.opp-status.is-open{
    color:var(--sp-burgundy);
}

.opp-status.is-open::before{
    background:var(--sp-burgundy);
}

.opp-card h3{
    font-size:21px;
    letter-spacing:-.3px;
    margin:14px 0 10px;
}

.opp-card p{
    color:var(--sp-muted);
    font-size:14px;
    line-height:1.6;
    flex-grow:1;
}

.opp-card a.row-link{
    display:inline-block;
    margin-top:16px;
    font-size:12px;
    font-weight:800;
    letter-spacing:.4px;
    color:var(--sp-burgundy);
}

@media(max-width:900px){
    .opp-grid{ grid-template-columns:repeat(2,1fr); }
}

@media(max-width:600px){
    .opp-grid{ grid-template-columns:1fr; }
}
"""

# (label, title, description, status_text, is_open, href)
CATEGORIES = [
    ("01", "Government Opportunities",
     "Public-sector opportunities Southern Point is pursuing or evaluating, and where Southern Point coordinates qualified partners to support delivery.",
     "Pursued directly — contact to discuss", False, "/government-contracting/"),
    ("02", "Workforce",
     "Open positions Southern Point is actively recruiting for, across temporary, temp-to-hire, direct hire, and contract roles.",
     "Live openings on the job board", True, "/jobs.html"),
    ("03", "Professional Services",
     "Engagements for administrative, operational, program, and project support capacity.",
     "No open engagements posted — contact to discuss", False, "/services/professional-services/"),
    ("04", "Technology",
     "Technical support, systems, and application-support opportunities across Southern Point's technology focus area.",
     "View current technology openings", True, "/jobs.html?category=Technology"),
    ("05", "Operations",
     "Coordination, process, and logistics opportunities that keep day-to-day operations running.",
     "View current operations openings", True, "/jobs.html?category=Operations"),
    ("06", "Strategic Partnerships",
     "Opportunities to work with Southern Point as a qualified contractor, vendor, subcontractor, or specialized partner.",
     "Developing relationships — contact to introduce your firm", False, "/contact/"),
]

def opp_cards():
    out = []
    for num, title, desc, status_text, is_open, href in CATEGORIES:
        status_class = "opp-status is-open" if is_open else "opp-status"
        out.append(f"""
<a class="opp-card" href="{href}" style="text-decoration:none; color:inherit;">
<div class="card-number">{num}</div>
<h3>{title}</h3>
<p>{desc}</p>
<span class="{status_class}">{status_text}</span>
</a>""")
    return "\n".join(out)

body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span>Opportunities</div>
<div class="eyebrow eyebrow-light">OPPORTUNITIES</div>
<h1>Where Southern Point Is Putting People and Resources to Work.</h1>
<p>A single entry point across the ways organizations and professionals work with Southern Point — open workforce positions, public-sector pursuits, professional-services engagements, and partnership opportunities.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">SIX WAYS TO GET INVOLVED</div>
<h2 class="section-title" style="max-width:760px;">Find the opportunity that fits.</h2>
<p class="section-intro">Each category links to where that opportunity actually lives — the job board for open roles, or a direct conversation for pursuits and partnerships Southern Point doesn't yet have publicly posted.</p>
<div class="opp-grid">
{opp_cards()}
</div>
</div>
</section>

<section class="tint">
<div class="container" style="text-align:center;">
<div class="section-label" style="justify-content:center;">DON'T SEE THE RIGHT FIT?</div>
<h2 class="section-title">Opportunities are added as they become real.</h2>
<p class="section-intro" style="margin:0 auto;">Southern Point doesn't post placeholder opportunities to look busier than it is. If you have a requirement, a role, or a capability that isn't reflected above, reach out directly.</p>
<a class="btn btn-outline" href="/contact/" style="margin-top:16px;">Contact Southern Point</a>
</div>
</section>

<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">FOR ORGANIZATIONS AND CANDIDATES</div>
<h2 class="section-title">Two ways to start.</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/request-talent/">Find Talent</a>
<a class="btn btn-outline-white" href="/jobs.html">Find Jobs</a>
</div>
</div>
</section>
"""

html = build(
    title="Opportunities | Southern Point",
    description="A single entry point across Southern Point's open workforce positions, public-sector pursuits, professional-services engagements, and partnership opportunities.",
    extra_style=STYLE,
    body_html=body,
    section="opportunities",
    canonical="https://southernpointllc.com/opportunities/",
)

out_dir = f"{BASE}/opportunities"
os.makedirs(out_dir, exist_ok=True)
with open(f"{out_dir}/index.html", "w") as f:
    f.write(html)

print("wrote opportunities/index.html")
