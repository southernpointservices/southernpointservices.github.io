#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

INDUSTRIES = [
    {
        "slug": "technology",
        "name": "Technology",
        "hero": "Technology Talent, Ready to Contribute.",
        "overview": "Southern Point supports organizations that depend on technology-driven operations, connecting them with professionals who can step into technical support, systems, and technology-enabled business roles without a long ramp-up period.",
        "positions": [
            "Technical Support Specialist",
            "Help Desk Analyst",
            "IT Coordinator",
            "Systems &amp; Network Support",
            "Technical Project Coordinator",
            "Application Support Specialist",
        ],
        "challenges": [
            ("Fast-moving needs", "Technical support gaps can slow down an entire organization, and openings often need to be filled quickly rather than over several months."),
            ("Skills vs. resume claims", "It can be difficult to tell genuine hands-on technical ability apart from a well-written resume without a structured screening process."),
            ("Short-term project surges", "Rollouts, migrations, and system changes often create a temporary need for extra technical support beyond the core team."),
        ],
        "help": "Southern Point sources and screens candidates against the specific technical environment and tools an organization actually uses, rather than presenting a generic pool of applicants. Engagements can be structured as temporary, temp-to-hire, or direct hire depending on how the need is expected to evolve.",
        "why": [
            "A screening process built around the specific systems and tools a role requires, not just keyword matching.",
            "Flexible engagement models so short-term technical support doesn't require a full-time commitment.",
            "Direct, responsive communication throughout the search rather than a slow, opaque process.",
        ],
        "candidate_copy": "Southern Point works with technical professionals — from help desk and technical support to systems and application support — looking for contract, temp-to-hire, or direct-hire opportunities with organizations that need their skills right now.",
    },
    {
        "slug": "healthcare",
        "name": "Healthcare",
        "hero": "Reliable Support for Healthcare Operations.",
        "overview": "Southern Point provides staffing support for the administrative and operational functions that keep healthcare organizations running — the scheduling, records, billing support, and front-office work that allows clinical teams to focus on patient care. This is administrative and operational staffing, not clinical placement.",
        "positions": [
            "Medical Office Administrator",
            "Patient Services Coordinator",
            "Health Information &amp; Records Support",
            "Medical Billing Support",
            "Front Office &amp; Scheduling Coordinator",
            "Healthcare Administrative Assistant",
        ],
        "challenges": [
            ("Administrative backlog", "When front-office and administrative roles go unfilled, it shows up quickly in patient experience and staff workload."),
            ("Confidentiality &amp; compliance awareness", "Healthcare administrative work requires a level of attention to detail and discretion that not every candidate is prepared for."),
            ("Coverage gaps", "Leave coverage and seasonal patient volume changes both create short-term staffing needs that are hard to plan for."),
        ],
        "help": "Southern Point sources candidates with genuine healthcare administrative experience and screens for the attention to detail and discretion the work requires. Coverage can be arranged on a temporary basis for leave and volume spikes, or as temp-to-hire and direct hire for ongoing roles.",
        "why": [
            "Candidates screened specifically for administrative and operational healthcare experience — not a generic office-support pool.",
            "Flexible coverage options for leave, turnover, and seasonal volume changes.",
            "A straightforward, responsive process instead of a long procurement cycle.",
        ],
        "candidate_copy": "Southern Point works with administrative and operational professionals interested in healthcare settings — front office, scheduling, records, and billing support roles — including candidates building a career in healthcare administration without a clinical background.",
    },
    {
        "slug": "sales",
        "name": "Sales",
        "hero": "Sales Talent That Moves the Needle.",
        "overview": "Southern Point connects organizations with sales professionals who can build pipeline, manage accounts, and contribute to revenue goals from day one, across industries and sales models.",
        "positions": [
            "Sales Development Representative",
            "Inside Sales Representative",
            "Business Development Representative",
            "Account Coordinator",
            "Sales Support Coordinator",
            "Customer Success Coordinator",
        ],
        "challenges": [
            ("Turnover", "Sales roles see higher turnover than most functions, which makes a reliable, repeatable sourcing process especially valuable."),
            ("Ramp time", "A new sales hire who takes too long to become productive can cost more than the role's salary in lost pipeline."),
            ("Verifying real sales ability", "Sales candidates are often skilled at selling themselves in an interview — a structured screening process matters more here, not less."),
        ],
        "help": "Southern Point sources candidates for sales aptitude and relevant experience, not just interview polish, and can staff sales teams on a temporary, contract, or direct-hire basis to match hiring cycles and seasonal demand.",
        "why": [
            "A screening process built to separate genuine sales experience from interview performance.",
            "Flexible staffing models for scaling a sales team up or down with demand.",
            "Responsive, direct communication throughout the search.",
        ],
        "candidate_copy": "Southern Point works with sales professionals — from entry-level development reps to experienced account managers — looking for their next opportunity across industries, including contract and direct-hire roles.",
    },
    {
        "slug": "operations",
        "name": "Operations",
        "hero": "Operational Support You Can Count On.",
        "overview": "Southern Point provides staffing support for the operational functions that keep an organization running day to day — coordination, process management, scheduling, and the behind-the-scenes work that often goes unnoticed until it isn't done well.",
        "positions": [
            "Operations Coordinator",
            "Logistics &amp; Operations Support",
            "Process &amp; Documentation Coordinator",
            "Scheduling Coordinator",
            "Operations Administrative Support",
            "Project Support Specialist",
        ],
        "challenges": [
            ("Growth outpacing process", "Fast-growing organizations often outgrow their operational support before they realize it, creating backlogs and dropped details."),
            ("Peak-period coverage", "Seasonal or cyclical peak periods create short-term operational staffing needs that don't justify a permanent hire."),
            ("Attention to detail at scale", "Operations work depends on consistency and follow-through, which is harder to screen for than technical skill alone."),
        ],
        "help": "Southern Point sources candidates with real operational and process experience, and can staff for short-term peak-period coverage or build toward a permanent operations hire through a temp-to-hire arrangement.",
        "why": [
            "Candidates screened for reliability and follow-through, not just a list of past job titles.",
            "Flexible coverage for peak periods without a permanent commitment.",
            "A practical, responsive process from first conversation to placement.",
        ],
        "candidate_copy": "Southern Point works with operations-minded professionals — coordinators, schedulers, and process support specialists — looking for temporary, temp-to-hire, or direct-hire opportunities across industries.",
    },
    {
        "slug": "administrative",
        "name": "Administrative",
        "hero": "Administrative Support, Done Right.",
        "overview": "Southern Point provides administrative staffing support to help organizations keep day-to-day business operations running smoothly, from front-office coverage to ongoing administrative team support.",
        "positions": [
            "Administrative Assistant",
            "Office Coordinator",
            "Administrative Coordinator",
            "Data Entry &amp; Administrative Support",
            "Receptionist &amp; Front Office Support",
            "Executive Support (coordinator level)",
        ],
        "challenges": [
            ("Turnover and leave gaps", "Administrative gaps are felt immediately — calls go unanswered, documents pile up, and other staff absorb the overflow."),
            ("Fast onboarding needs", "Administrative roles often need someone who can contribute in days, not weeks."),
            ("Matching software and process fit", "Two administrative roles can look identical on paper but require very different tools and workflows."),
        ],
        "help": "Southern Point sources administrative candidates matched to the specific software, workflow, and pace of an organization, and can staff a role on a temporary, temp-to-hire, or direct-hire basis depending on the need.",
        "why": [
            "Candidates screened for reliability, professionalism, and fit with the actual day-to-day workflow.",
            "Fast turnaround for time-sensitive administrative gaps.",
            "Flexible engagement models, from short-term coverage to permanent placement.",
        ],
        "candidate_copy": "Southern Point works with administrative professionals at every level looking for temporary, temp-to-hire, or direct-hire opportunities, including candidates who want the flexibility of assignment-based work.",
    },
]


def positions_html(items):
    return "\n".join(f'<li>{item}</li>' for item in items)


def editorial_rows(items, start=1):
    """Shared numbered-row list — no cards, no boxes, just rules and type."""
    rows = []
    for i, (title, body) in enumerate(items, start=start):
        rows.append(f"""
<div class="editorial-row">
<div class="row-num">{i:02d}</div>
<div class="row-body">
<h3>{title}</h3>
<p>{body}</p>
</div>
</div>""")
    return f'<div class="editorial-list">{"".join(rows)}</div>'


def why_html(items):
    return "\n".join(f'<li>{item}</li>' for item in items)


def industry_split(label, title, body_html, positions):
    """Copy + role-list section used for each industry's overview."""
    return f"""
<section>
<div class="container">
<div class="section-label">{label}</div>
<h2 class="section-title" style="max-width:760px;">{title}</h2>
{body_html}
<h3 style="margin-top:34px; font-size:18px;">Positions Southern Point commonly staffs</h3>
<ul class="role-list">
{positions_html(positions)}
</ul>
</div>
</section>"""


PAGE_STYLE = """
.role-list{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:12px 30px;
    margin-top:10px;
    max-width:900px;
}

.role-list li{
    padding:14px 0 14px 26px;
    border-bottom:1px solid #E2D9C4;
    position:relative;
    font-weight:700;
    font-size:14px;
}

.role-list li::before{
    content:"";
    position:absolute;
    left:0;
    top:20px;
    width:8px;
    height:8px;
    background:#B8863E;
}

.why-list{
    margin-top:8px;
}

.why-list li{
    padding:14px 0 14px 30px;
    border-top:1px solid #33323A;
    position:relative;
    font-size:14px;
    color:#CFC9BB;
}

.why-list li:last-child{
    border-bottom:1px solid #33323A;
}

.why-list li::before{
    content:"\\2713";
    position:absolute;
    left:0;
    top:14px;
    color:#D8B67A;
    font-weight:900;
}

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
    font-size:clamp(22px,2.4vw,28px);
    margin-bottom:16px;
    color:#fff;
}

.cta-half p{
    color:#C7C1B3;
    max-width:380px;
    margin:0 auto 24px;
}

@media(max-width:900px){
    .role-list{
        grid-template-columns:repeat(2,1fr);
    }
}
@media(max-width:560px){
    .role-list{
        grid-template-columns:1fr;
    }
}

@media(max-width:850px){
    .cta-split{grid-template-columns:1fr;}
    .cta-half:first-child{border-right:none; border-bottom:1px solid var(--sp-line-dark);}
    .cta-half{padding:50px 30px;}
}
"""


for ind in INDUSTRIES:
    body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/industries/">Industries</a><span>/</span>{ind['name']}</div>
<div class="eyebrow eyebrow-light">INDUSTRY FOCUS</div>
<h1>{ind['hero']}</h1>
<p>{ind['overview']}</p>
<div class="btn-row" style="margin-top:10px;">
<a class="btn btn-red" href="/request-talent/">Need Talent?</a>
<a class="btn btn-outline-white" href="/jobs.html?category={ind['name']}">Find Opportunities</a>
</div>
</div>
</section>

{industry_split(
    "INDUSTRY OVERVIEW",
    f"Staffing built around {ind['name'].lower()} work.",
    f'<p class="section-intro">{ind["overview"]}</p>',
    ind["positions"],
)}

<section class="tint">
<div class="container">
<div class="section-label">COMMON CHALLENGES</div>
<h2 class="section-title">What makes {ind['name'].lower()} staffing hard to get right.</h2>
{editorial_rows(ind['challenges'])}
</div>
</section>

<section>
<div class="container split">
<div>
<div class="section-label">HOW SOUTHERN POINT HELPS</div>
<h2 class="section-title">A practical approach, not a resume dump.</h2>
<p class="section-intro">{ind['help']}</p>
</div>
<div>
<div class="section-label">HIRING PROCESS</div>
<div class="process-grid" style="grid-template-columns:1fr; gap:0;">
<div class="step" style="border-top:none; border-left:2px solid #B8863E; padding:0 0 18px 20px; margin-bottom:0;">
<div class="step-number">01</div>
<h3>Tell Us What You Need</h3>
<p>Share the role, requirements, timeline, and engagement type you're looking for.</p>
</div>
<div class="step" style="border-top:none; border-left:2px solid #B8863E; padding:18px 0 18px 20px;">
<div class="step-number">02</div>
<h3>We Source &amp; Screen</h3>
<p>Southern Point identifies and screens candidates against the specific need — not a generic pool.</p>
</div>
<div class="step" style="border-top:none; border-left:2px solid #B8863E; padding:18px 0 0 20px;">
<div class="step-number">03</div>
<h3>You Choose, We Support</h3>
<p>You make the final call on who joins your team, and Southern Point stays engaged through onboarding.</p>
</div>
</div>
</div>
</div>
</section>

<section class="dark">
<div class="container split">
<div>
<div class="section-label">WHY EMPLOYERS USE SOUTHERN POINT</div>
<h2 class="section-title">Built for how {ind['name'].lower()} teams actually hire.</h2>
<ul class="why-list">
{why_html(ind['why'])}
</ul>
</div>
<div>
<div class="section-label">CANDIDATE OPPORTUNITIES</div>
<h2 class="section-title">For {ind['name']} professionals</h2>
<p>{ind['candidate_copy']}</p>
<div class="btn-row" style="margin-top:22px;">
<a class="btn btn-outline-white" href="/jobs.html?category={ind['name']}">View {ind['name']} Openings</a>
</div>
</div>
</div>
</section>

<section class="dark">
<div class="cta-split">
<div class="cta-half">
<div class="section-label" style="justify-content:center; color:var(--sp-bronze-light);">FOR EMPLOYERS</div>
<h3>Need {ind['name']} talent?</h3>
<p>Tell Southern Point about your hiring need and we'll follow up to discuss next steps.</p>
<a class="btn btn-red" href="/request-talent/">Request Talent</a>
</div>
<div class="cta-half">
<div class="section-label" style="justify-content:center; color:var(--sp-bronze-light);">FOR JOB SEEKERS</div>
<h3>Looking for {ind['name']} work?</h3>
<p>Explore current openings or submit your resume for consideration on future roles.</p>
<a class="btn btn-outline-white" href="/jobs.html?category={ind['name']}">Find Opportunities</a>
</div>
</div>
</section>
"""

    html = build(
        title=f"{ind['name']} Staffing Services | Southern Point",
        description=f"Southern Point provides {ind['name'].lower()} staffing support — sourcing, screening, and placing candidates for {ind['name'].lower()} roles on a temporary, temp-to-hire, or direct-hire basis.",
        extra_style=PAGE_STYLE,
        body_html=body,
        section="industries",
        canonical=f"https://southernpointllc.com/industries/{ind['slug']}/",
    )

    out_path = f"{BASE}/industries/{ind['slug']}/index.html"
    with open(out_path, "w") as f:
        f.write(html)
    print("wrote", out_path)
