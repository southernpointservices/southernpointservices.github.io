#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

INDUSTRIES = [
    ("01", "Technology", "technology", "Technical support, systems, and application-support roles for technology-driven organizations."),
    ("02", "Healthcare", "healthcare", "Administrative and operational staffing support for healthcare organizations — non-clinical roles."),
    ("03", "Sales", "sales", "Sales development, account management, and business development talent across industries."),
    ("04", "Operations", "operations", "Coordination, process, and logistics support that keeps day-to-day operations running."),
    ("05", "Administrative", "administrative", "Administrative assistants, office coordinators, and front-office support at every level."),
]

STYLE = """
/* =========================
   INDUSTRY DIRECTORY
   (same editorial-row language as the homepage industries section)
========================= */
.division-list{
    margin-top:10px;
    border-top:1px solid var(--sp-line-dark);
}

.division-row{
    display:grid;
    grid-template-columns:90px 1fr auto;
    gap:30px;
    align-items:center;
    padding:32px 0;
    border-bottom:1px solid var(--sp-line-dark);
    transition:.2s ease;
    text-decoration:none;
    color:inherit;
}

.division-row:hover{
    background:rgba(184,134,62,.06);
}

.division-num{
    font-family:var(--font-display);
    font-size:34px;
    color:var(--sp-bronze);
}

.division-body h3{
    font-size:24px;
    margin-bottom:6px;
    color:#fff;
}

.division-body p{
    color:#C7C1B3;
    font-size:14px;
    max-width:560px;
}

.division-arrow{
    font-family:var(--font-display);
    font-size:14px;
    font-weight:600;
    color:var(--sp-bronze-light);
    white-space:nowrap;
}

@media(max-width:700px){
    .division-row{grid-template-columns:50px 1fr; row-gap:10px;}
    .division-arrow{grid-column:2;}
}

/* =========================
   FINAL DUAL CTA
========================= */
.cta-split{
    display:grid;
    grid-template-columns:1fr 1fr;
    position:relative;
}

.cta-half{
    padding:70px 60px;
    text-align:center;
}

.cta-half:first-child{
    border-right:1px solid var(--sp-line-dark);
}

.cta-half h3{
    font-size:clamp(24px,2.6vw,32px);
    margin-bottom:16px;
    color:#fff;
}

.cta-half p{
    color:#C7C1B3;
    max-width:380px;
    margin:0 auto 24px;
}

@media(max-width:850px){
    .cta-split{grid-template-columns:1fr;}
    .cta-half:first-child{border-right:none; border-bottom:1px solid var(--sp-line-dark);}
    .cta-half{padding:50px 30px;}
}
"""

rows = "\n".join(f"""
<a href="/industries/{slug}/" class="division-row">
<div class="division-num">{num}</div>
<div class="division-body">
<h3>{name}</h3>
<p>{desc}</p>
</div>
<div class="division-arrow">Explore {name} &rarr;</div>
</a>""" for num, name, slug, desc in INDUSTRIES)

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
<div class="photo-frame ratio-wide">
<img class="photo" src="/assets/images/industries-hub.jpg" alt="A mixed professional environment representing Southern Point's five focus industries">
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:#D8B67A;">EXPLORE BY INDUSTRY</div>
<h2 class="section-title" style="color:#fff;">Five focus areas, staffed with real depth.</h2>
<p class="section-intro" style="color:#C7C1B3;">Each industry page below covers the roles Southern Point commonly staffs, the challenges organizations in that space typically face, and how our process is built to address them.</p>
<div class="division-list">
{rows}
</div>
</div>
</section>

<section>
<div class="container split">
<div>
<div class="section-label">WHY INDUSTRY FOCUS MATTERS</div>
<h2 class="section-title">Depth beats a generic candidate pool.</h2>
<p>A staffing partner that tries to cover every industry equally usually understands none of them well. Southern Point staffs within five focus areas so that sourcing, screening, and candidate conversations are grounded in what the role actually requires — not a one-size-fits-all process.</p>
</div>
<div>
<div class="section-label">DON'T SEE YOUR INDUSTRY?</div>
<h2 class="section-title">Let's talk about it anyway.</h2>
<p>If your hiring need falls outside these five areas, reach out — Southern Point may still be able to help, or can point you in a useful direction.</p>
<a class="btn btn-outline" href="/contact/" style="margin-top:16px;">Contact Southern Point</a>
</div>
</div>
</section>

<section class="dark">
<div class="cta-split">
<div class="cta-half">
<div class="section-label" style="justify-content:center; color:var(--sp-bronze-light);">FOR ORGANIZATIONS</div>
<h3>Need talent for one of these industries?</h3>
<p>Tell Southern Point what you're looking for and we'll follow up to discuss next steps.</p>
<a class="btn btn-red" href="/request-talent/">Request Talent</a>
</div>
<div class="cta-half">
<div class="section-label" style="justify-content:center; color:var(--sp-bronze-light);">FOR CANDIDATES</div>
<h3>Looking for your next role?</h3>
<p>Search current openings across all five focus industries.</p>
<a class="btn btn-outline-white" href="/jobs.html">Find Jobs</a>
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
