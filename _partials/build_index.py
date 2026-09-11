#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
/* =========================
   CINEMATIC HERO
========================= */
.cinematic-hero{
    position:relative;
    background:var(--sp-near-black);
    color:#ffffff;
    padding:118px 0 70px;
    overflow:hidden;
}

.cinematic-hero::before{
    content:"";
    position:absolute;
    inset:-30% -10% auto auto;
    width:60%;
    aspect-ratio:1;
    border-radius:50%;
    background:radial-gradient(circle at 30% 30%, rgba(184,134,62,.20), transparent 65%);
}

.cinematic-hero::after{
    content:"";
    position:absolute;
    left:-15%;
    bottom:-35%;
    width:55%;
    aspect-ratio:1;
    border-radius:50%;
    background:radial-gradient(circle at 70% 70%, rgba(110,36,54,.28), transparent 65%);
}

.hero-grid-2{
    position:relative;
    display:grid;
    grid-template-columns:1.15fr .85fr;
    gap:70px;
    align-items:center;
}

.hero-kicker{
    display:inline-flex;
    align-items:center;
    gap:10px;
    font-size:11px;
    font-weight:800;
    letter-spacing:2px;
    text-transform:uppercase;
    color:var(--sp-bronze-light);
    margin-bottom:22px;
}

.hero-kicker::before{
    content:"";
    width:34px;
    height:2px;
    background:var(--sp-bronze-light);
}

.cinematic-hero h1{
    font-size:clamp(38px,5.4vw,66px);
    line-height:1.05;
    letter-spacing:-2px;
    margin-bottom:26px;
    max-width:820px;
}

.cinematic-hero .hero-text{
    max-width:600px;
    font-size:18px;
    color:#D8D3C6;
    margin-bottom:14px;
}

.cinematic-hero .hero-text.secondary{
    font-size:15px;
    color:#B8B2A2;
    margin-bottom:32px;
}

.hero-trust-row{
    display:flex;
    flex-wrap:wrap;
    gap:26px;
    margin-top:38px;
    padding-top:24px;
    border-top:1px solid var(--sp-line-dark);
}

.hero-trust-row div{
    font-size:12px;
    color:#B8B2A2;
}

.hero-trust-row strong{
    display:block;
    font-family:var(--font-display);
    font-size:15px;
    color:#ffffff;
    font-weight:600;
}

.hero-panel-v2{
    position:relative;
    background:var(--sp-midnight-2);
    border:1px solid rgba(255,255,255,.09);
    border-top:2px solid var(--sp-bronze);
    box-shadow:0 40px 80px -20px rgba(0,0,0,.55);
    padding:44px 40px;
}

.hero-panel-v2 .panel-label{
    color:var(--sp-bronze-light);
    font-size:11px;
    font-weight:800;
    letter-spacing:2px;
}

.hero-panel-v2 h2{
    font-size:23px;
    line-height:1.28;
    margin:14px 0 26px;
    color:#fff;
}

.hero-panel-v2 ul{
    list-style:none;
}

.hero-panel-v2 li{
    padding:12px 0;
    border-top:1px solid var(--sp-line-dark);
    font-size:14px;
    color:#E2D9C4;
}

@media(max-width:980px){
    .hero-grid-2{grid-template-columns:1fr; gap:46px;}
    .cinematic-hero{padding:90px 0 60px;}
    .hero-trust-row{gap:20px;}
}

/* =========================
   POSITIONING STATEMENT
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
   WHAT WE DO — SERVICE PILLARS
========================= */
.home-pillars{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:24px;
    margin-top:24px;
}

.pillar-block{
    padding:36px;
    border:1px solid var(--sp-line);
    background:#ffffff;
    display:flex;
    flex-direction:column;
}

.pillar-block .pillar-num{
    font-family:var(--font-display);
    font-size:26px;
    color:var(--sp-bronze);
    margin-bottom:14px;
}

.pillar-block .eyebrow{
    margin-bottom:10px;
}

.pillar-block h3{
    font-size:22px;
    margin-bottom:10px;
    letter-spacing:-.3px;
}

.pillar-block p{
    color:var(--sp-muted);
    font-size:14px;
    margin-bottom:18px;
}

.pillar-tags{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    list-style:none;
    margin-bottom:22px;
}

.pillar-tags li{
    font-size:11px;
    font-weight:700;
    color:var(--sp-bronze-dark);
    background:var(--sp-cream-2);
    padding:6px 10px;
}

.pillar-link{
    font-size:12px;
    font-weight:800;
    letter-spacing:.3px;
    color:var(--sp-burgundy);
    margin-top:auto;
}

@media(max-width:850px){
    .home-pillars{grid-template-columns:1fr;}
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
    background:var(--sp-cream-2);
    padding:5px 10px;
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
    margin-bottom:14px;
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
    ("01", "STAFFING &amp; RECRUITING", "The right people for the work that matters.",
     "Southern Point connects organizations with qualified talent through flexible staffing and recruiting solutions.",
     ["Temporary Staffing", "Temp-to-Hire", "Direct Hire", "Contract Staffing", "Recruiting"],
     "Explore Staffing &amp; Recruiting", "/services/staffing-recruiting/"),
    ("02", "PROFESSIONAL SERVICES", "Support that keeps organizations moving.",
     "Southern Point provides flexible professional resources for organizations that need additional capacity, support, or expertise.",
     ["Administrative Support", "Operations Support", "Program Support", "Project Support", "Customer Support", "Technical Support"],
     "Explore Professional Services", "/services/professional-services/"),
    ("03", "WORKFORCE SOLUTIONS", "Flexible resources for changing requirements.",
     "Organizations do not always need the same people, skills, or capacity. Southern Point helps build workforce solutions around actual organizational requirements.",
     ["Workforce Planning", "Talent Acquisition", "Workforce Augmentation", "Contract Resources"],
     "Explore Workforce Solutions", "/services/workforce-solutions/"),
    ("04", "SPECIALIZED SOLUTIONS", "Flexible resources for specialized requirements.",
     "Some requirements call for specialized professionals, local resources, vendors, or external service providers. Southern Point can coordinate appropriate resources when a requirement extends beyond an organization's existing capacity.",
     ["Specialized Professionals", "Local Resources", "Vendors &amp; External Providers"],
     "Explore Specialized Solutions", "/services/specialized-solutions/"),
]

WHY = [
    ("Responsive", "Clear communication and timely follow-through."),
    ("Flexible", "Solutions designed around actual organizational requirements."),
    ("Resourceful", "Access to qualified talent and specialized resources."),
    ("Accountable", "Engaged from initial requirement through delivery."),
]

# Simple geometric line icons — one per service pillar, rendered inside
# .icon-mark. No stock icon set; kept deliberately minimal and consistent.
PILLAR_ICONS = [
    # Staffing & Recruiting — two people
    '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"></circle><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"></path><circle cx="17.5" cy="9" r="2.3"></circle><path d="M15.3 20c.3-2.5 2-4.4 4.2-5"></path></svg>',
    # Professional Services — briefcase
    '<svg viewBox="0 0 24 24"><rect x="3" y="8" width="18" height="12" rx="1"></rect><path d="M8 8V6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><path d="M3 13h18"></path></svg>',
    # Workforce Solutions — flexible modular grid
    '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect></svg>',
    # Specialized Solutions — precision target
    '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="5"></circle><circle cx="12" cy="12" r="1"></circle></svg>',
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

def resource_cards():
    out = []
    for slug, cat, title, desc in RESOURCE_PICKS:
        out.append(f"""
<a class="card" href="/resources/{slug}/" style="text-decoration:none; color:inherit; display:block;">
<span class="insight-cat">{cat}</span>
<h3>{title}</h3>
<p>{desc}</p>
</a>""")
    return "\n".join(out)

def pillar_blocks():
    out = []
    for i, (num, eyebrow, headline, copy, tags, cta_label, cta_href) in enumerate(PILLARS):
        tag_html = "\n".join(f"<li>{t}</li>" for t in tags)
        icon = PILLAR_ICONS[i]
        out.append(f"""
<div class="pillar-block">
<div class="icon-mark">{icon}</div>
<div class="eyebrow">{eyebrow}</div>
<h3>{headline}</h3>
<p>{copy}</p>
<ul class="pillar-tags">
{tag_html}
</ul>
<a class="pillar-link" href="{cta_href}">{cta_label} &rarr;</a>
</div>""")
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
<section class="cinematic-hero">
<div class="container hero-grid-2">

<div>
<div class="hero-kicker">WORKFORCE &middot; PROFESSIONAL SERVICES &middot; SOLUTIONS</div>
<h1>Workforce. Professional Services. Solutions.</h1>
<p class="hero-text">Southern Point helps organizations access the people, support, and resources they need to move forward.</p>
<p class="hero-text secondary">From talent acquisition and workforce support to professional and operational services, we build flexible solutions around the requirements of each organization.</p>

<div class="btn-row">
<a class="btn btn-red" href="/request-talent/">Find Talent</a>
<a class="btn btn-outline-white" href="/services/">Explore Services</a>
</div>

<div class="hero-trust-row">
<div><strong>Houston, TX</strong>Headquartered &amp; founded here</div>
<div><strong>Nationwide</strong>Service reach for organizations &amp; candidates</div>
<div><strong>Five Industries</strong>Technology, Healthcare, Sales, Operations, Administrative</div>
</div>
</div>

<div class="hero-panel-v2">
<div class="panel-label">HOW WE HELP</div>
<h2>Access to the people, support, and resources organizations need to move forward.</h2>
<ul>
<li>Staffing &amp; recruiting</li>
<li>Professional services</li>
<li>Workforce solutions</li>
<li>Specialized resource coordination</li>
</ul>
</div>

</div>
</section>

<section class="tint">
<div class="container">
<div class="statement-block">
<div class="divider-rule center"></div>
<p class="lede">Southern Point combines workforce expertise, professional support, and flexible resource coordination to help organizations solve operational and talent challenges.</p>
<p class="sub">From a single hire to a broader operational need, Southern Point builds the solution around the requirement — not the other way around.</p>
</div>
</div>
</section>

<section id="services">
<div class="container">
<div class="section-label">WHAT WE DO</div>
<h2 class="section-title">Four ways we help organizations move forward.</h2>
<p class="section-intro">Southern Point is built to grow with what your organization needs — starting with these four areas today.</p>
<div class="home-pillars">
{pillar_blocks()}
</div>
</div>
</section>

<section class="dark">
<div class="container">
<div class="section-label" style="color:var(--sp-bronze-light);">INDUSTRIES WE SERVE</div>
<h2 class="section-title" style="color:#fff;">Focused expertise, not everything at once.</h2>
<p class="section-intro" style="color:#C7C1B3;">Southern Point staffs deliberately across five industries — deep focus instead of shallow reach.</p>
<div class="division-list">
{division_rows()}
</div>
</div>
</section>

<section>
<div class="container">
<p class="statement-xl">The right people can change <span class="accent">the trajectory</span> of an organization.</p>
<p class="section-intro" style="margin-top:24px;">Southern Point exists to make that connection &mdash; matching organizations with people who can actually move the work forward, not just fill a seat.</p>
</div>
</section>

<section class="tint">
<div class="container split-wide">
<div class="visual-panel">
<div class="visual-panel-graphic"></div>
</div>
<div>
<div class="section-label">FOR ORGANIZATIONS</div>
<h2 class="section-title">Need people, support, or resources?</h2>
<p style="color:var(--sp-muted); margin-bottom:20px;">Tell Southern Point what you need and we'll follow up to discuss the requirement, timeline, and next steps &mdash; usually within one business day, across staffing, professional services, workforce solutions, or specialized resource coordination.</p>
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
</div>
</section>

<section>
<div class="container split-wide">
<div>
<div class="section-label">FOR JOB SEEKERS</div>
<h2 class="section-title">Looking for your next opportunity?</h2>
<p style="color:var(--sp-muted); margin-bottom:20px;">Search current openings or submit your resume for general consideration &mdash; there's no cost to candidates, ever. Southern Point works across Technology, Healthcare, Sales, Operations, and Administrative roles nationwide.</p>
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
<div class="visual-panel tone-light">
<div class="visual-panel-graphic"></div>
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
<div class="grid-3">
{resource_cards()}
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
