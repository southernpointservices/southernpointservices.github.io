#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
/* =========================
   HERO — large typography, no boxed panel
========================= */
.hero-shell{
    position:relative;
    background:var(--sp-near-black);
    color:#ffffff;
}

.hero-split{
    width:92%;
    max-width:1180px;
    margin:0 auto;
}

.hero-copy{
    display:flex;
    flex-direction:column;
    justify-content:center;
    padding:230px 0 110px;
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
    font-size:clamp(40px,5.6vw,72px);
    line-height:1.03;
    letter-spacing:-2px;
    margin-bottom:28px;
    max-width:640px;
}

.hero-copy .hero-text{
    max-width:520px;
    font-size:18px;
    line-height:1.55;
    color:#D8D3C6;
    margin-bottom:36px;
}

.hero-copy .hero-stack-list{
    margin-top:36px;
    padding-top:26px;
    border-top:1px solid var(--sp-line-dark);
    font-size:13px;
    color:#B8B2A2;
}

.hero-copy .hero-stack-list strong{
    color:#E7E1D2;
    font-weight:600;
}

@media(max-width:980px){
    .hero-split{width:100%; padding:0 24px;}
    .hero-copy{padding:160px 0 50px;}
}

/* =========================
   STATEMENT
========================= */
.statement-block{
    max-width:760px;
    margin:0 auto;
    text-align:center;
}

.statement-block p.lede{
    font-family:var(--font-display);
    font-size:clamp(22px,3.2vw,34px);
    line-height:1.35;
    letter-spacing:-.5px;
    color:var(--sp-ink);
    margin-bottom:18px;
}

.statement-block p.sub{
    color:var(--sp-muted);
    font-size:16px;
}

/* =========================
   DIVISIONS (INDUSTRIES)
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
   LIVE JOBS (HOMEPAGE)
========================= */
.home-job-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
    margin-top:10px;
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
}

.home-empty p{
    color:var(--sp-muted);
    max-width:480px;
    margin:0 auto 22px;
}

@media(max-width:900px){
    .home-job-grid{grid-template-columns:1fr 1fr;}
}
@media(max-width:600px){
    .home-job-grid{grid-template-columns:1fr;}
}

/* =========================
   EDITORIAL WORD GRID (WHY)
========================= */
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
    font-size:clamp(30px,3vw,40px);
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

/* =========================
   RESOURCES PREVIEW
========================= */
.insight-cat{
    font-size:11px;
    font-weight:800;
    letter-spacing:1px;
    text-transform:uppercase;
    color:var(--sp-bronze-dark);
    margin-bottom:8px;
    display:block;
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

RESOURCE_PICKS = [
    ("reducing-time-to-fill", "Hiring Advice", "Reducing Time-to-Fill Without Lowering Your Standards",
     "Practical ways employers can shorten the hiring process without cutting corners on candidate quality."),
    ("resume-first-scan", "Career Advice", "How to Make Your Resume Pass the First Ten-Second Scan",
     "What actually gets noticed in the first quick pass of a resume, and how to make sure your strongest points aren't missed."),
    ("staffing-growing-technology-teams", "Industry Insights", "Staffing Considerations for Growing Technology Teams",
     "What to think through before adding your next technology hire, whether it's a permanent role or temporary support."),
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

WHY = [
    ("Responsive", "Clear communication and timely follow-through."),
    ("Flexible", "Solutions designed around actual organizational requirements."),
    ("Resourceful", "Access to qualified talent and specialized resources."),
    ("Accountable", "Engaged from initial requirement through delivery."),
]

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

def resource_rows():
    out = []
    for i, (slug, cat, title, desc) in enumerate(RESOURCE_PICKS, start=1):
        out.append(f"""
<a class="editorial-row" href="/resources/{slug}/" style="text-decoration:none; color:inherit;">
<div class="row-num">0{i}</div>
<div>
<span class="insight-cat">{cat}</span>
<h3>{title}</h3>
<p>{desc}</p>
<span class="row-link">Read More &rarr;</span>
</div>
</a>""")
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
<span class="row-link">Explore {name.replace('&amp;', '&amp;')} &rarr;</span>
</div>
</a>""")
    return "\n".join(out)

def why_items():
    out = []
    for title, body in WHY:
        out.append(f"""
<div class="word-item">
<strong>{title}.</strong>
<p>{body}</p>
</div>""")
    return "\n".join(out)

body = f"""
<section class="hero-shell">
<div class="hero-split">

<div class="hero-copy">
<div class="eyebrow-line">WORKFORCE &middot; PROFESSIONAL SERVICES &middot; SOLUTIONS</div>
<h1>Workforce. Professional Services. Solutions.</h1>
<p class="hero-text">Southern Point helps organizations access the people, support, and resources they need to move forward &mdash; through staffing and recruiting, professional services, workforce solutions, and specialized resource coordination.</p>

<div class="btn-row">
<a class="btn btn-red" href="/request-talent/">Find Talent</a>
<a class="btn btn-outline-white" href="/services/">Explore Services</a>
</div>

<div class="hero-stack-list">
<strong>Houston, TX</strong> &middot; headquartered &amp; founded here &nbsp;&mdash;&nbsp;
<strong>Nationwide</strong> &middot; service reach for organizations &amp; candidates &nbsp;&mdash;&nbsp;
<strong>Five Industries</strong> &middot; Technology, Healthcare, Sales, Operations, Administrative
</div>
</div>

</div>
</section>

<section class="tint">
<div class="container">
<div class="statement-block">
<div class="divider-rule center"></div>
<p class="lede">Southern Point combines workforce expertise, professional support, and flexible resource coordination to help organizations solve operational and talent challenges.</p>
<p class="sub">From a single hire to a broader operational need, Southern Point builds the solution around the requirement &mdash; not the other way around.</p>
</div>
</div>
</section>

<section id="services">
<div class="container">
<div class="section-label">WHAT WE DO</div>
<h2 class="section-title">Four ways we help organizations move forward.</h2>
<p class="section-intro">Southern Point is built to grow with what your organization needs &mdash; starting with these four areas today.</p>
<div class="editorial-list" style="margin-top:30px;">
{pillar_rows()}
</div>
</div>
</section>

<section>
<div class="container">
<p class="statement-xl">The right people can change <span class="accent">the trajectory</span> of an organization.</p>
<p class="section-intro" style="margin-top:24px;">Southern Point exists to make that connection &mdash; matching organizations with people who can actually move the work forward, not just fill a seat.</p>
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
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">FOR ORGANIZATIONS</div>
<h2 class="section-title">Need people, support, or resources?</h2>
<p class="section-intro" style="margin-bottom:20px;">Tell Southern Point what you need and we'll follow up to discuss the requirement, timeline, and next steps &mdash; usually within one business day, across staffing, professional services, workforce solutions, or specialized resource coordination.</p>
<div class="stats">
<div class="stat"><strong>Sourcing</strong><span>Targeted, not generic</span></div>
<div class="stat"><strong>Screening</strong><span>Before you see a resume</span></div>
<div class="stat"><strong>Support</strong><span>Through delivery &amp; beyond</span></div>
</div>
<div class="btn-row" style="margin-top:26px;">
<a class="btn btn-red" href="/request-talent/">Find Talent</a>
<a class="btn btn-outline" href="/services/">Explore Services</a>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-label">FOR JOB SEEKERS</div>
<h2 class="section-title">Looking for your next opportunity?</h2>
<p class="section-intro" style="margin-bottom:20px;">Search current openings or submit your resume for general consideration &mdash; there's no cost to candidates, ever. Southern Point works across Technology, Healthcare, Sales, Operations, and Administrative roles nationwide.</p>
<div class="stats">
<div class="stat"><strong>Search</strong><span>Real, current openings</span></div>
<div class="stat"><strong>Connect</strong><span>With a real recruiter</span></div>
<div class="stat"><strong>No Cost</strong><span>Ever, to candidates</span></div>
</div>
<div class="btn-row" style="margin-top:26px;">
<a class="btn btn-red" href="/jobs.html">Find Jobs</a>
<a class="btn btn-outline" href="/submit-resume/">Submit Resume</a>
</div>
</div>
</section>

<section class="tint" id="jobs">
<div class="container">
<div class="section-label">PART OF STAFFING &amp; RECRUITING</div>
<h2 class="section-title">A few of our current openings.</h2>
<p class="section-intro">Openings are posted here as they come in directly from our data feed &mdash; nothing shown here is placeholder content.</p>

<div id="homeJobGrid" class="home-job-grid"></div>
<div id="homeJobEmpty" class="home-empty" style="display:none;">
<h3>No open positions posted right now</h3>
<p>Southern Point doesn't list placeholder openings. Check back soon, browse the full jobs board, or submit your resume so we can reach out when a fit comes up.</p>
<div class="btn-row" style="justify-content:center;">
<a class="btn btn-red" href="/jobs.html">View Jobs Board</a>
<a class="btn btn-outline" href="/submit-resume/">Submit Resume</a>
</div>
</div>

<div style="text-align:center; margin-top:34px;">
<a class="btn btn-outline" href="/jobs.html">Search All Jobs</a>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-label">HOW WE WORK</div>
<h2 class="section-title">One process, whatever the requirement.</h2>
<div class="process-grid">
<div class="step"><div class="step-number">01</div><h3>Understand</h3><p>We learn what you actually need.</p></div>
<div class="step"><div class="step-number">02</div><h3>Build</h3><p>We identify the people, resources, and approach required.</p></div>
<div class="step"><div class="step-number">03</div><h3>Coordinate</h3><p>We manage communication, scheduling, documentation, and delivery.</p></div>
<div class="step"><div class="step-number">04</div><h3>Deliver</h3><p>We stay engaged through completion and adjust as requirements evolve.</p></div>
</div>
</div>
</section>

<section class="tint" style="text-align:center;">
<div class="container">
<p class="statement-xl" style="max-width:820px; margin-left:auto; margin-right:auto;">Built around <span class="accent">people</span>. Designed for organizations.</p>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">WHY SOUTHERN POINT</div>
<h2 class="section-title" style="color:#fff;">Not a high-volume staffing mill.</h2>
<div class="word-grid">
{why_items()}
</div>
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">FROM THE RESOURCE CENTER</div>
<h2 class="section-title">Guidance for both sides of the table.</h2>
<div class="editorial-list" style="margin-top:30px;">
{resource_rows()}
</div>
<div style="text-align:center; margin-top:34px;">
<a class="btn btn-outline" href="/resources/">Visit the Resource Center</a>
</div>
</div>
</section>

<section class="dark">
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
    title="Southern Point | Workforce, Professional Services & Solutions",
    description="Southern Point helps organizations access the people, support, and resources they need to move forward — staffing and recruiting, professional services, workforce solutions, and specialized resource coordination.",
    extra_style=STYLE,
    body_html=body,
    section="home",
    canonical="https://southernpointllc.com/",
)

with open(f"{BASE}/index.html", "w") as f:
    f.write(html)

print("wrote index.html")
