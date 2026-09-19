#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
/* =========================
   HERO — split-screen: copy left, photograph right.
   NOTE: .hero-shell overrides the default `section{padding:118px 0}`
   to 0 — hero-copy/hero-visual/hero-stat-strip manage their own
   padding, so this doesn't stack on top of it (that stacking was
   the root cause of the old hero's oversized dead space).
========================= */
.hero-shell{
    position:relative;
    background:var(--sp-near-black);
    color:#ffffff;
    padding:0;
    overflow:hidden;
}

.hero-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    align-items:stretch;
}

.hero-copy{
    display:flex;
    flex-direction:column;
    justify-content:center;
    padding:222px max(48px, calc((100vw - 1180px) / 2 + 24px)) 80px max(24px, calc((100vw - 1180px) / 2));
}

.hero-copy .eyebrow-line{
    font-size:11px;
    font-weight:800;
    letter-spacing:2px;
    text-transform:uppercase;
    color:var(--sp-bronze-light);
    margin-bottom:26px;
}

.hero-copy h1{
    font-size:clamp(38px,4.6vw,62px);
    line-height:1.06;
    letter-spacing:-1.8px;
    margin-bottom:26px;
    max-width:600px;
}

.hero-copy .hero-text{
    max-width:480px;
    font-size:17px;
    line-height:1.6;
    color:#D8D3C6;
    margin-bottom:34px;
}

/* Right panel — photograph with a floating card over it previewing
   the three pillars covered in the next section. */
.hero-visual{
    position:relative;
    overflow:hidden;
    min-height:560px;
    /* Photograph sits under a midnight gradient so the pillar card and the
       header nav stay legible over it at every viewport width. The gradient
       is part of the composition, not a fix — it ties the photo to the
       near-black left column so the split reads as one hero, not two panels. */
    background-image:
        linear-gradient(180deg,
            rgba(15,16,21,.72) 0%,      /* keeps the nav links legible over the sky */
            rgba(15,16,21,.30) 22%,
            rgba(15,16,21,.80) 100%),
        url('/assets/images/hero-houston-skyline.jpg');
    background-size:cover;
    background-position:center;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:40px;
}

/* Bronze grid + glow are held back to a whisper now that a photograph
   carries the panel — they read as a faint brand texture over the image
   rather than the graphic treatment they were before. */
.hero-visual::before{
    content:"";
    position:absolute;
    inset:0;
    background-image:
        repeating-linear-gradient(0deg, rgba(216,182,122,.07) 0 1px, transparent 1px 56px),
        repeating-linear-gradient(90deg, rgba(216,182,122,.07) 0 1px, transparent 1px 56px);
    opacity:.35;
    mix-blend-mode:overlay;
    pointer-events:none;
}

.hero-visual::after{
    content:"";
    position:absolute;
    top:-18%;
    right:-12%;
    width:65%;
    height:65%;
    background:radial-gradient(circle, rgba(184,134,62,.28), transparent 72%);
    opacity:.5;
    pointer-events:none;
}

.hero-pillar-card{
    position:relative;
    z-index:1;
    width:100%;
    max-width:380px;
    border:1px solid rgba(216,182,122,.28);
    background:rgba(15,16,21,.6);
    padding:34px 32px;
}

.hero-pillar-card .eyebrow-light{
    margin-bottom:6px;
}

.hero-pillar-row{
    display:flex;
    align-items:baseline;
    gap:16px;
    padding:16px 0;
    border-top:1px solid var(--sp-line-dark);
}

.hero-pillar-row:first-of-type{
    border-top:none;
}

.hero-pillar-num{
    font-family:var(--font-display);
    font-size:14px;
    color:var(--sp-bronze-light);
    flex-shrink:0;
}

.hero-pillar-title{
    font-size:16px;
    font-weight:600;
    letter-spacing:-.2px;
    color:#fff;
}

/* Full-width stat strip beneath the split — closes out the hero
   with real information instead of empty space. */
.hero-stat-strip{
    display:flex;
    gap:44px;
    flex-wrap:wrap;
    padding:30px 0;
    border-top:1px solid var(--sp-line-dark);
}

.hero-stat-strip .stat strong{
    color:#fff;
}

.hero-stat-strip .stat span{
    color:#9C9484;
}

@media(max-width:980px){
    .hero-grid{grid-template-columns:1fr;}
    .hero-copy{padding:150px 24px 46px;}
    .hero-visual{
        min-height:400px;
        padding:28px;
        /* Phone-sized render of the same photograph. Sources are low-res, so
           each variant is rendered at its exact device-pixel box and the
           browser blits it 1:1 rather than upscaling a desktop-width file. */
        background-image:
            linear-gradient(180deg,
                rgba(15,16,21,.72) 0%,
                rgba(15,16,21,.34) 22%,
                rgba(15,16,21,.82) 100%),
            url('/assets/images/hero-houston-skyline-m.jpg');
    }
    /* More body than the desktop card: on mobile the photo sits directly
       behind the card rather than off to one side, so .6 wasn't enough. */
    .hero-pillar-card{padding:26px 24px; background:rgba(15,16,21,.8);}
}

/* =========================
   WHAT WE DO — 3-pillar
========================= */
.pillar-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:0;
    margin-top:36px;
    border-top:1px solid var(--sp-line);
}

.pillar-item{
    padding:34px 34px 4px 0;
    border-left:1px solid var(--sp-line);
}

.pillar-item:first-child{
    border-left:none;
    padding-left:0;
}

.pillar-item:not(:first-child){
    padding-left:34px;
}

.pillar-num{
    display:block;
    font-family:var(--font-display);
    font-size:15px;
    font-weight:600;
    color:var(--sp-bronze);
    margin-bottom:18px;
}

.pillar-item h3{
    font-size:23px;
    letter-spacing:-.3px;
    margin-bottom:12px;
}

.pillar-item p{
    color:var(--sp-muted);
    font-size:15px;
    margin-bottom:16px;
}

@media(max-width:850px){
    .pillar-grid{grid-template-columns:1fr; border-top:none;}
    .pillar-item{
        border-left:none !important;
        padding-left:0 !important;
        padding-right:0;
        padding-top:30px;
        border-top:1px solid var(--sp-line);
    }
    .pillar-item:first-child{border-top:none; padding-top:0;}
}

/* =========================
   BUILT TO MATCH THE WORK
========================= */
.match-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:50px;
    margin-top:28px;
}

.match-item{
    border-top:2px solid var(--sp-bronze);
    padding-top:24px;
}

.match-item .pillar-num{
    color:var(--sp-bronze-light);
}

.match-item h3{
    font-size:25px;
    color:#fff;
    margin:12px 0 10px;
}

.match-item p{
    color:#C7C1B3;
    font-size:15px;
}

@media(max-width:850px){
    .match-grid{grid-template-columns:1fr; gap:34px;}
}

/* =========================
   GOVERNMENT CONTRACTING (home teaser)
========================= */
.mini-list-card{
    border:1px solid var(--sp-line);
    padding:6px 28px;
}

.mini-list-row{
    display:flex;
    align-items:baseline;
    gap:16px;
    padding:18px 0;
    border-bottom:1px solid var(--sp-line);
}

.mini-list-row:last-child{
    border-bottom:none;
}

.mini-list-row .mini-num{
    font-family:var(--font-display);
    font-size:14px;
    color:var(--sp-bronze);
    flex-shrink:0;
}

.mini-list-row .mini-title{
    font-size:15px;
    font-weight:600;
    letter-spacing:-.1px;
}

/* =========================
   INDUSTRIES (division list)
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
    .division-arrow{grid-column:2; }
}

/* =========================
   LIVE JOBS (inside Opportunities section)
========================= */
.home-job-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
}

.home-job-card{
    border:1px solid var(--sp-line);
    background:#ffffff;
    padding:28px;
    display:flex;
    flex-direction:column;
    gap:12px;
}

.home-job-tag{
    display:inline-block;
    align-self:flex-start;
    font-size:10px;
    font-weight:800;
    letter-spacing:1px;
    text-transform:uppercase;
    color:var(--sp-bronze-dark);
    background:#ffffff;
    border:1px solid var(--sp-ink);
    padding:4px 9px;
}

.home-job-card h3{
    font-size:18px;
}

.home-job-card h3 a{
    color:var(--sp-ink);
    text-decoration:none;
}

.home-job-card h3 a:hover{
    color:var(--sp-bronze-dark);
}

.home-job-meta{
    font-size:12px;
    color:var(--sp-muted-2);
}

.home-job-desc{
    font-size:13px;
    color:var(--sp-muted);
    flex-grow:1;
}

.home-job-link{
    font-size:13px;
    font-weight:700;
    color:var(--sp-burgundy);
    text-decoration:none;
}

.home-empty{
    border:1px dashed var(--sp-line-dark);
    padding:50px 30px;
    text-align:center;
}

.home-empty h3{
    font-family:var(--font-display);
    font-size:21px;
    margin-bottom:10px;
    color:inherit;
}

.home-empty p{
    color:var(--sp-muted);
    max-width:480px;
    margin:0 auto 22px;
}

.dark .home-empty{
    border-color:var(--sp-line-dark);
}

.dark .home-empty h3{
    color:#fff;
}

.dark .home-empty p{
    color:#C7C1B3;
}

@media(max-width:900px){
    .home-job-grid{grid-template-columns:1fr 1fr;}
}
@media(max-width:600px){
    .home-job-grid{grid-template-columns:1fr;}
}

/* =========================
   FINAL DUAL CTA
========================= */
.cta-shell{
    padding:100px 0;
}

.cta-split{
    display:grid;
    grid-template-columns:1fr 1fr;
    position:relative;
}

.cta-half{
    padding:0 60px;
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
    .cta-shell{padding:70px 0;}
    .cta-split{grid-template-columns:1fr; gap:50px;}
    .cta-half:first-child{border-right:none; border-bottom:1px solid var(--sp-line-dark); padding-bottom:50px;}
    .cta-half{padding-left:20px; padding-right:20px;}
}
"""

PILLARS3 = [
    ("01", "Talent &amp; Workforce",
     "Staffing, recruiting, and workforce solutions built around what an organization actually needs &mdash; temporary, temp-to-hire, direct hire, and contract.",
     "/services/staffing-recruiting/"),
    ("02", "Professional Services",
     "Flexible professional resources &mdash; administrative, operations, program, project, and technical support &mdash; for organizations that need additional capacity.",
     "/services/professional-services/"),
    ("03", "Government Contracting",
     "Public-sector opportunities Southern Point pursues directly, coordinating qualified partners where a requirement calls for it.",
     "/government-contracting/"),
]

MATCH_STEPS = [
    ("01", "Identify", "We start by understanding the actual requirement &mdash; the role, the scope, the timeline &mdash; not a generic template applied regardless of fit."),
    ("02", "Assemble", "We assemble the right people, resources, or partners for that specific requirement, coordinating sourcing, screening, and logistics."),
    ("03", "Deliver", "We stay engaged through delivery and beyond, adjusting the approach as the requirement evolves."),
]

INDUSTRIES = [
    ("01", "Technology", "technology", "Technology Talent, Ready to Contribute.",
     "Technical support, systems, and technology-enabled business roles for organizations that depend on technology-driven operations."),
    ("02", "Healthcare", "healthcare", "Reliable Support for Healthcare Operations.",
     "Administrative and operational staffing that keeps healthcare organizations running — not clinical placement."),
    ("03", "Sales", "sales", "Sales Talent That Moves the Needle.",
     "Sales professionals who can build pipeline, manage accounts, and contribute to revenue goals from day one."),
    ("04", "Operations", "operations", "Operational Support You Can Count On.",
     "Coordination, process management, and the behind-the-scenes work that keeps a business running day to day."),
    ("05", "Administrative", "administrative", "Administrative Support, Done Right.",
     "Front-office coverage and ongoing administrative team support to keep day-to-day business operations smooth."),
]

GC_MINI = [
    ("Contract Pursuit"),
    ("Contract Support"),
    ("Strategic Partnerships"),
    ("Supplier &amp; Subcontractor Network"),
]

PILLARS = [
    ("01", "Staffing &amp; Recruiting", "The right people for the work that matters.",
     "Southern Point connects organizations with qualified talent through flexible staffing and recruiting solutions — temporary, temp-to-hire, direct hire, and contract.",
     "/services/staffing-recruiting/"),
    ("02", "Professional Services", "Support that keeps organizations moving.",
     "Flexible professional resources for organizations that need additional capacity, support, or expertise — administrative, operations, program, project, customer, and technical support.",
     "/services/professional-services/"),
    ("03", "Workforce Solutions", "Flexible resources for changing requirements.",
     "Organizations do not always need the same people, skills, or capacity. Southern Point helps build workforce solutions around actual organizational requirements.",
     "/services/workforce-solutions/"),
    ("04", "Specialized Solutions", "Flexible resources for specialized requirements.",
     "Some requirements call for specialized professionals, local resources, vendors, or external service providers that extend beyond an organization's existing capacity.",
     "/services/specialized-solutions/"),
]


def hero_pillar_rows():
    out = []
    for num, name, desc, href in PILLARS3:
        out.append(f"""
<div class="hero-pillar-row">
<div class="hero-pillar-num">{num}</div>
<div class="hero-pillar-title">{name}</div>
</div>""")
    return "\n".join(out)


def pillar3_items():
    out = []
    for num, name, desc, href in PILLARS3:
        out.append(f"""
<div class="pillar-item">
<span class="pillar-num">{num}</span>
<h3>{name}</h3>
<p>{desc}</p>
<a class="row-link" href="{href}">Learn More &rarr;</a>
</div>""")
    return "\n".join(out)


def match_items():
    out = []
    for num, title, body in MATCH_STEPS:
        out.append(f"""
<div class="match-item">
<span class="pillar-num">{num}</span>
<h3>{title}</h3>
<p>{body}</p>
</div>""")
    return "\n".join(out)


def division_rows():
    out = []
    for num, name, slug, tagline, desc in INDUSTRIES:
        out.append(f"""
<a class="division-row" href="/industries/{slug}/">
<div class="division-num">{num}</div>
<div class="division-body">
<h3>{name}</h3>
<p>{desc}</p>
</div>
<div class="division-arrow">Explore {name} Staffing &rarr;</div>
</a>""")
    return "\n".join(out)


def gc_mini_rows():
    out = []
    for i, title in enumerate(GC_MINI, start=1):
        out.append(f"""
<div class="mini-list-row">
<div class="mini-num">0{i}</div>
<div class="mini-title">{title}</div>
</div>""")
    return "\n".join(out)


def pillar_rows():
    out = []
    for num, name, headline, copy, href in PILLARS:
        out.append(f"""
<a class="editorial-row" href="{href}" style="text-decoration:none; color:inherit;">
<div class="row-num">{num}</div>
<div>
<h3>{name} &mdash; {headline}</h3>
<p>{copy}</p>
<span class="row-link">Explore {name} &rarr;</span>
</div>
</a>""")
    return "\n".join(out)


body = f"""
<section class="hero-shell">
<div class="hero-grid">

<div class="hero-copy">
<div class="eyebrow-line">WORKFORCE &middot; PROFESSIONAL SERVICES &middot; GOVERNMENT CONTRACTING</div>
<h1>The People, Support, and Resources to Move Your Organization Forward.</h1>
<p class="hero-text">Southern Point connects organizations with qualified talent, professional services, and coordinated support &mdash; including public-sector opportunities &mdash; built around the requirement, not a fixed model.</p>
<div class="btn-row">
<a class="btn btn-red" href="/request-talent/">Find Talent</a>
<a class="btn btn-outline-white" href="/services/">Explore Services</a>
</div>
</div>

<div class="hero-visual">
<div class="hero-pillar-card">
<div class="eyebrow eyebrow-light">WHAT WE DO</div>
{hero_pillar_rows()}
</div>
</div>

</div>

<div class="container hero-stat-strip">
<div class="stat"><strong>Houston, TX</strong><span>Headquartered &amp; founded here</span></div>
<div class="stat"><strong>Nationwide</strong><span>Service reach for organizations &amp; candidates</span></div>
<div class="stat"><strong>Five Industries</strong><span>Plus government contracting</span></div>
</div>
</section>

<section id="what-we-do">
<div class="container">
<div class="section-label">WHAT WE DO</div>
<h2 class="section-title" style="max-width:760px;">Three ways Southern Point puts people and resources to work.</h2>
<p class="section-intro">From workforce and staffing to professional services and government contracting &mdash; each is built around the actual requirement, not a fixed model.</p>
<div class="pillar-grid">
{pillar3_items()}
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">HOW WE WORK</div>
<h2 class="section-title" style="color:#fff; max-width:760px;">Built to match the work &mdash; not a fixed process forced onto it.</h2>
<div class="match-grid">
{match_items()}
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-label">SERVICES</div>
<h2 class="section-title">The detail behind what we do.</h2>
<p class="section-intro">Southern Point is built to grow with what your organization needs &mdash; starting with these four areas today.</p>
<div class="editorial-list" style="margin-top:30px;">
{pillar_rows()}
</div>
<div style="margin-top:34px;">
<a class="btn btn-outline" href="/services/">View All Services</a>
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">INDUSTRIES WE SERVE</div>
<h2 class="section-title" style="color:#fff;">Focused expertise, not everything at once.</h2>
<p class="section-intro" style="color:#C7C1B3;">Southern Point staffs deliberately across five industries &mdash; deep focus instead of shallow reach.</p>
<div class="division-list">
{division_rows()}
</div>
<div style="margin-top:34px;">
<a class="btn btn-outline-white" href="/industries/">View All Industries</a>
</div>
</div>
</section>

<section id="government-contracting">
<div class="container">
<div class="split-wide">
<div>
<div class="section-label">GOVERNMENT CONTRACTING</div>
<h2 class="section-title">Public-sector opportunities, pursued deliberately.</h2>
<p class="section-intro">Southern Point pursues public-sector opportunities aligned with its capabilities and, where a requirement calls for it, coordinates qualified contractors, vendors, subcontractors, and specialized partners to support delivery.</p>
<a class="btn btn-outline" href="/government-contracting/" style="margin-top:22px;">Explore Government Contracting</a>
</div>
<div class="mini-list-card">
{gc_mini_rows()}
</div>
</div>
</div>
</section>

<section class="dark" id="opportunities">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">OPPORTUNITIES</div>
<h2 class="section-title" style="color:#fff; max-width:780px;">Government pursuits, workforce openings, and partnerships &mdash; one place to start.</h2>
<p class="section-intro" style="color:#C7C1B3;">A single entry point across the ways organizations and professionals work with Southern Point.</p>

<div id="homeJobGrid" class="home-job-grid" style="margin-top:34px;"></div>
<div id="homeJobEmpty" class="home-empty" style="display:none;">
<h3>No open positions posted right now</h3>
<p>Southern Point doesn't list placeholder openings. Check the full opportunities page, browse the jobs board, or submit your resume so we can reach out when a fit comes up.</p>
<div class="btn-row" style="justify-content:center;">
<a class="btn btn-red" href="/jobs.html">View Jobs Board</a>
<a class="btn btn-outline-white" href="/submit-resume/">Submit Resume</a>
</div>
</div>

<div style="text-align:center; margin-top:34px;">
<a class="btn btn-outline-white" href="/opportunities/">View All Opportunities</a>
</div>
</div>
</section>

<section class="dark cta-shell">
<div class="container">
<div class="cta-split">
<div class="cta-half">
<div class="section-label" style="justify-content:center; color:var(--sp-bronze-light);">FOR ORGANIZATIONS</div>
<h3>Need people, support, or resources?</h3>
<p>Tell Southern Point what you're looking for and we'll follow up to discuss next steps.</p>
<a class="btn btn-red" href="/request-talent/">Find Talent</a>
</div>
<div class="cta-half">
<div class="section-label" style="justify-content:center; color:var(--sp-bronze-light);">FOR CANDIDATES</div>
<h3>Looking for your next opportunity?</h3>
<p>Search current openings or submit your resume for future consideration.</p>
<a class="btn btn-outline-white" href="/jobs.html">Find Jobs</a>
</div>
</div>
</div>
</section>

<script>
(function(){{
    function escapeHTML(value){{
        return String(value === undefined || value === null ? "" : value)
            .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
    }}
    function relativeDate(dateStr){{
        const posted = new Date(dateStr);
        if(!dateStr || isNaN(posted.getTime())){{ return "Recently listed"; }}
        const days = Math.floor((Date.now() - posted.getTime()) / 86400000);
        if(days <= 0) return "Posted today";
        if(days === 1) return "Posted 1 day ago";
        if(days < 30) return "Posted " + days + " days ago";
        return "Posted " + posted.toLocaleDateString("en-US", {{ month: "short", day: "numeric", year: "numeric" }});
    }}
    function cardHTML(job){{
        return '<div class="home-job-card">' +
            '<span class="home-job-tag">' + escapeHTML(job.employmentType || job.category || "Opening") + '</span>' +
            '<h3><a href="/jobs.html?job=' + encodeURIComponent(job.id) + '">' + escapeHTML(job.title) + '</a></h3>' +
            '<div class="home-job-meta">' + escapeHTML(job.location || "") + '</div>' +
            '<p class="home-job-desc">' + escapeHTML(job.description || "") + '</p>' +
            '<div class="home-job-meta">' + relativeDate(job.postedDate) + '</div>' +
            '<a class="home-job-link" href="/jobs.html?job=' + encodeURIComponent(job.id) + '">View Details &rarr;</a>' +
        '</div>';
    }}
    fetch("/data/jobs.json", {{ cache: "no-store" }})
        .then(function(res){{ return res.ok ? res.json() : []; }})
        .then(function(data){{
            const jobs = (Array.isArray(data) ? data : []).filter(function(j){{ return j && j.status === "active"; }}).slice(0, 3);
            const grid = document.getElementById("homeJobGrid");
            const empty = document.getElementById("homeJobEmpty");
            if(!jobs.length){{
                grid.style.display = "none";
                empty.style.display = "block";
                return;
            }}
            grid.innerHTML = jobs.map(cardHTML).join("");
        }})
        .catch(function(err){{
            console.error("Southern Point homepage: could not load data/jobs.json —", err);
            document.getElementById("homeJobGrid").style.display = "none";
            document.getElementById("homeJobEmpty").style.display = "block";
        }});
}})();
</script>
"""

html = build(
    title="Southern Point | Workforce, Professional Services & Government Contracting",
    description="Southern Point helps organizations access the people, support, and resources they need to move forward — staffing and recruiting, professional services, workforce solutions, and government contracting.",
    extra_style=STYLE,
    body_html=body,
    section="home",
    canonical="https://southernpointllc.com/",
)

with open(f"{BASE}/index.html", "w") as f:
    f.write(html)

print("wrote index.html")
