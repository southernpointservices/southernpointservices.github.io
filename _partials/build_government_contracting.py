#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
/* Full-bleed infrastructure photograph behind the page hero. The gradient
   runs near-opaque at the bottom so the hero hands off to the white section
   below it without a hard seam, and keeps the headline/CTA legible. */
.page-hero{
    background-image:
        linear-gradient(180deg,
            rgba(15,16,21,.82) 0%,      /* darkest under the fixed nav bar */
            rgba(15,16,21,.55) 24%,     /* opens up so the photo reads */
            rgba(15,16,21,.93) 88%),    /* closes to meet the white section */
        url('/assets/images/gc-infrastructure.jpg');
    background-size:cover;
    background-position:center 40%;
}

@media(max-width:980px){
    .page-hero{
        background-image:
            linear-gradient(180deg,
                rgba(15,16,21,.90) 0%,
                rgba(15,16,21,.58) 30%,
                rgba(15,16,21,.94) 90%),
            url('/assets/images/gc-infrastructure-m.jpg');
    }
}

.gc-split{
    padding:20px 0;
}

.gc-note{
    max-width:800px;
}

.gc-note p + p{
    margin-top:14px;
}
"""

GC_AREAS = [
    ("Contract Pursuit",
     "Identifying and evaluating public-sector opportunities aligned with Southern Point's actual capabilities — not pursuing scope the business isn't positioned to deliver."),
    ("Contract Support",
     "Providing staffing, professional services, and operational support once a contract is underway, structured around the specific requirement."),
    ("Strategic Partnerships",
     "Working with qualified organizations where a requirement calls for specialized capabilities beyond Southern Point's direct scope of work."),
    ("Supplier &amp; Subcontractor Network",
     "Developing relationships with qualified firms capable of supporting specific scopes of work as opportunities call for them."),
]

def gc_rows():
    out = []
    for i, (title, body) in enumerate(GC_AREAS, start=1):
        out.append(f"""
<div class="editorial-row">
<div class="row-num">0{i}</div>
<div>
<h3>{title}</h3>
<p>{body}</p>
</div>
</div>""")
    return "\n".join(out)

body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span>Government Contracting</div>
<div class="eyebrow eyebrow-light">GOVERNMENT CONTRACTING</div>
<h1>Public-Sector Opportunities. Qualified Resources. Coordinated Delivery.</h1>
<p>Southern Point pursues public-sector opportunities aligned with its capabilities and, where appropriate, works with qualified contractors, vendors, subcontractors, and specialized partners to support delivery.</p>
<div class="btn-row" style="margin-top:10px;">
<a class="btn btn-red" href="/contact/">Discuss an Opportunity</a>
<a class="btn btn-outline-white" href="/opportunities/">View Opportunities</a>
</div>
</div>
</section>

<section class="gc-split">
<div class="container">
<div class="section-label">HOW SOUTHERN POINT APPROACHES THIS</div>
<h2 class="section-title" style="max-width:760px;">A capability, not a claim.</h2>
<div class="gc-note">
<p>Government contracting is an area Southern Point is actively developing as part of its broader workforce and professional-services capability — evaluated the same way any engagement is: against what the business can actually deliver, directly or through qualified partners.</p>
<p>Southern Point does not represent itself as holding contracts, certifications, or past performance it does not have. Where a specific set-aside, certification, or clearance applies to an opportunity, Southern Point will state its current status plainly rather than imply otherwise.</p>
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">WHAT THIS COVERS</div>
<h2 class="section-title" style="color:#fff;">Four parts of how Southern Point supports public-sector work.</h2>
<div class="editorial-list" style="margin-top:30px;">
{gc_rows()}
</div>
</div>
</section>

<section>
<div class="container">
<div class="card" style="max-width:800px;">
<div class="section-label">BEING CLEAR ABOUT WHAT THIS IS</div>
<p>Southern Point pursues public-sector opportunities directly and, when a requirement calls for capabilities beyond its own, works with qualified partners to help deliver the work — coordinated by Southern Point, with clear accountability for the engagement, rather than simply passed along. Southern Point is not a large prime contractor or an established supplier network; it is developing relationships with qualified contractors, vendors, subcontractors, and specialized partners as real opportunities call for them.</p>
</div>
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">RELATED CAPABILITIES</div>
<h2 class="section-title">Backed by Southern Point's core services.</h2>
<p class="section-intro">Government contracting draws on the same staffing, professional-services, workforce, and specialized-solutions capabilities Southern Point provides to commercial and institutional clients.</p>
<a class="btn btn-outline" href="/services/" style="margin-top:16px;">Explore Services</a>
</div>
</section>

<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">HAVE A PUBLIC-SECTOR REQUIREMENT?</div>
<h2 class="section-title">Let's talk about the opportunity.</h2>
<p style="max-width:600px; margin:0 auto 10px;">Share the opportunity or requirement through a short conversation, and Southern Point will follow up to discuss fit and next steps.</p>
<a class="btn btn-red" href="/contact/" style="margin-top:20px;">Contact Southern Point</a>
</div>
</section>
"""

html = build(
    title="Government Contracting | Southern Point",
    description="Southern Point pursues public-sector opportunities aligned with its capabilities and coordinates qualified contractors, vendors, and specialized partners to support delivery.",
    extra_style=STYLE,
    body_html=body,
    section="government-contracting",
    canonical="https://southernpointllc.com/government-contracting/",
)

out_dir = f"{BASE}/government-contracting"
os.makedirs(out_dir, exist_ok=True)
with open(f"{out_dir}/index.html", "w") as f:
    f.write(html)

print("wrote government-contracting/index.html")
