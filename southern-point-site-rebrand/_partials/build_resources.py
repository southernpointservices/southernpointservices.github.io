#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

# ---------------------------------------------------------------------------
# Article data
# ---------------------------------------------------------------------------
ARTICLES = [
    {
        "slug": "reducing-time-to-fill",
        "category": "hiring",
        "category_label": "Hiring Advice",
        "title": "Reducing Time-to-Fill Without Lowering Your Standards",
        "description": "Practical ways employers can shorten the hiring process without cutting corners on candidate quality.",
        "intro": "A slow hiring process costs more than it looks like on paper. Strong candidates accept other offers, hiring managers lose momentum, and the role stays a drag on the team long after it should have been filled. None of that means rushing the process or lowering the bar — it means removing the delays that don't actually improve the decision.",
        "sections": [
            ("Start with a specific request, not a general one", "\"We need a strong administrative assistant\" is harder to act on than \"we need someone who can manage scheduling for a 12-person team and has used our specific software before.\" The more specific the request, the faster a recruiter can identify a real match instead of a plausible one."),
            ("Compress the scheduling gap, not the evaluation", "Most delay in hiring happens between steps, not during them — the days it takes to get a panel on the calendar, or the week a resume sits unreviewed. Shortening those gaps doesn't reduce how carefully a candidate is evaluated; it just removes dead time."),
            ("Decide what's actually required versus preferred", "Requiring every \"nice to have\" as a hard requirement shrinks the candidate pool for no real benefit. Separating true requirements from preferences up front keeps the search focused without excluding qualified people over a minor gap."),
            ("Give feedback quickly, even when the answer is no", "Candidates who don't hear back for weeks often accept something else before your team makes a final decision. A fast, honest response — even a rejection — keeps the process moving and protects the employer's reputation with candidates who might be a fit for a future role."),
        ],
        "closing": "None of this is about moving fast for its own sake. It's about spending time where it actually improves the hiring decision, and cutting the time that doesn't. Southern Point structures its search process around exactly that distinction, on every engagement.",
        "cta": "employer",
    },
    {
        "slug": "choosing-the-right-engagement-model",
        "category": "hiring",
        "category_label": "Hiring Advice",
        "title": "Temporary, Temp-to-Hire, or Direct Hire: Choosing the Right Model",
        "description": "A practical breakdown of when to use temporary staffing, temp-to-hire, or direct hire for a given role.",
        "intro": "Employers often default to whichever staffing model they used last time, even when the situation has changed. The right engagement type depends on the specific need — how certain the requirement is, how long it's expected to last, and how much risk the organization wants to take on up front.",
        "sections": [
            ("Temporary staffing fits a defined, short-term need", "Coverage for a leave, a seasonal spike, or a short project all point toward temporary staffing. The commitment is limited to the actual window of need, which makes it the lowest-risk option when the timeline is clear."),
            ("Temp-to-hire works when you need to confirm fit first", "If the role is likely permanent but the organization wants to see the person's work firsthand before committing, temp-to-hire bridges the two. It costs more flexibility than a straight temporary placement, but removes much of the guesswork from a permanent hiring decision."),
            ("Direct hire makes sense for a confirmed, ongoing role", "When the need is clearly permanent and the organization is ready to hire directly, going straight to direct hire avoids the extra step of a temporary period. It requires more confidence in the requirement up front, since there's no trial window."),
            ("Contract staffing suits project-based and fixed-scope work", "When a project has a defined scope and end date — a system migration, a specific initiative — contract staffing matches the engagement to the actual duration of the work instead of treating it like a permanent hire."),
        ],
        "closing": "There's no universally \"better\" model — only the one that matches the actual situation. Southern Point walks through this with every employer before recommending an approach, rather than defaulting to a single staffing model across every request.",
        "cta": "employer",
    },
    {
        "slug": "resume-first-scan",
        "category": "careers",
        "category_label": "Career Advice",
        "title": "How to Make Your Resume Pass the First Ten-Second Scan",
        "description": "What actually gets noticed in the first quick pass of a resume, and how to make sure your strongest points aren't missed.",
        "intro": "Most resumes get a fast first pass before anyone reads them closely. That first scan isn't unfair — it's just how people manage a stack of applications. The goal isn't to trick that scan; it's to make sure the things that matter most are impossible to miss during it.",
        "sections": [
            ("Put your strongest, most relevant line first", "Whatever makes you a genuinely strong fit for this specific role should be visible without scrolling — not buried under an objective statement that could apply to any job."),
            ("Lead each bullet with what changed, not just what you did", "\"Managed the scheduling system\" says less than \"Managed scheduling for a 12-person team, cutting last-minute conflicts.\" You don't need invented numbers — a clear, honest description of scope and outcome does the same job."),
            ("Match the language of the role you're applying for", "If the posting says \"customer success\" and your resume says \"client relations,\" a fast scan may miss the connection. Mirror the real terms from the posting wherever they honestly describe your experience."),
            ("Cut anything that doesn't support this specific application", "A resume trying to say everything says nothing clearly. Trim older or unrelated experience so the most relevant parts aren't competing for attention."),
        ],
        "closing": "A resume's job is to earn a real conversation, not to tell your entire career story. Southern Point's recruiters read past a rough resume when the underlying experience is strong — but a clear one gets you that conversation faster.",
        "cta": "candidate",
    },
    {
        "slug": "tell-me-about-yourself",
        "category": "careers",
        "category_label": "Career Advice",
        "title": "How to Answer \"Tell Me About Yourself\" Without Rambling",
        "description": "A simple structure for answering the most common opening interview question with confidence.",
        "intro": "\"Tell me about yourself\" is usually the first question in an interview, which makes it easy to either freeze or ramble through an entire career history. The interviewer isn't asking for your life story — they're asking for a quick, relevant frame for the conversation that follows.",
        "sections": [
            ("Start with where you are now, briefly", "One sentence on your current or most recent role is enough context to start — no need to walk through every job you've ever had."),
            ("Connect your background to the role you're interviewing for", "Pick the one or two experiences most relevant to this specific job, and explain briefly why they matter here. This is the part that actually earns attention."),
            ("End by explaining why you're interested in this role", "Closing with a genuine, specific reason you want this particular position (not just \"a job\") gives the interviewer a natural next question to ask."),
            ("Keep it under about ninety seconds", "If you're still talking two minutes in, you've likely drifted from a frame into a full history. Practice saying it out loud once or twice beforehand — it's the easiest interview answer to over-prepare and still ramble through if you skip that step."),
        ],
        "closing": "This question isn't a test of memory — it's a chance to set the tone for the rest of the conversation. A short, relevant answer does that better than a comprehensive one.",
        "cta": "candidate",
    },
    {
        "slug": "hiring-administrative-talent",
        "category": "industry-insights",
        "category_label": "Industry Insights",
        "title": "What Employers Should Know About Hiring Administrative Talent",
        "description": "Why strong administrative hires are harder to evaluate from a resume alone, and what actually predicts success in the role.",
        "intro": "Administrative roles are often treated as easy to fill and hard to differentiate — but the difference between an adequate hire and a genuinely strong one shows up constantly in day-to-day operations. The skills that matter most rarely show up clearly on a resume.",
        "sections": [
            ("Judgment matters more than task lists", "Almost every administrative resume lists scheduling, correspondence, and office coordination. What's harder to see — and far more valuable — is how someone prioritizes when three urgent things land at once."),
            ("Software fluency is necessary but not sufficient", "Familiarity with the specific tools your office uses matters, but it's a baseline, not a differentiator. The stronger signal is how quickly someone picks up a new system when the ones they know don't match yours."),
            ("Ask about a time something went wrong, not just what they're good at", "How a candidate describes handling a scheduling conflict or a miscommunication tells you more about their actual day-to-day fit than a list of responsibilities from a past job."),
            ("Consider the team they'll actually support", "An administrative hire who thrives supporting one executive may struggle supporting a distributed team of ten, and vice versa. The structure of the role should shape who you're looking for, not just the title."),
        ],
        "closing": "Southern Point staffs administrative roles by screening for exactly this kind of judgment and adaptability — not just a list of software names on a resume.",
        "cta": "employer",
    },
    {
        "slug": "staffing-growing-technology-teams",
        "category": "industry-insights",
        "category_label": "Industry Insights",
        "title": "Staffing Considerations for Growing Technology Teams",
        "description": "What to think through before adding your next technology hire, whether it's a permanent role or temporary support.",
        "intro": "Technology teams often grow in bursts — a new project, a system migration, an unexpected gap — which makes the staffing decision as important as the hiring decision itself. Getting the engagement type right matters as much as getting the right candidate.",
        "sections": [
            ("Separate a permanent need from a temporary spike", "A new ongoing product area calls for a different hiring approach than a six-month migration project. Treating a temporary spike like a permanent hire (or the reverse) usually costs more than getting the distinction right up front."),
            ("Be specific about which skills are truly non-negotiable", "Technology roles often list every tool the team has ever touched as a requirement. Narrowing that list to what the role genuinely requires on day one opens up a much stronger, faster-moving candidate pool."),
            ("Screen for how someone learns, not just what they already know", "In fast-moving technology environments, the tools in use today may not be the tools in use next year. Evaluating how a candidate has picked up new systems in the past is often a better predictor than their current tool list."),
            ("Plan for onboarding time, not just start date", "A technical hire's start date isn't the same as their productive date. Factoring in a realistic ramp-up period avoids the false impression that a slow first month means a bad hire."),
        ],
        "closing": "Southern Point staffs technology roles across both permanent and project-based needs, matching the engagement type to the actual shape of the work rather than defaulting to one hiring model.",
        "cta": "employer",
    },
]

CATEGORIES = {
    "hiring": {
        "label": "Hiring Advice",
        "path": "resources/hiring",
        "intro": "Practical guidance for employers on hiring decisions, staffing models, and building a process that finds strong candidates without unnecessary delay.",
    },
    "careers": {
        "label": "Career Advice",
        "path": "resources/careers",
        "intro": "Straightforward advice for job seekers on resumes, interviews, and navigating a job search.",
    },
    "industry-insights": {
        "label": "Industry Insights",
        "path": "resources/industry-insights",
        "intro": "A closer look at hiring considerations specific to the industries Southern Point staffs: Technology, Healthcare, Sales, Operations, and Administrative.",
    },
}

ARTICLE_STYLE = """
.article-meta{
    color:#8C8270;
    font-size:12px;
    margin-bottom:6px;
}

.article-body{
    max-width:760px;
}

.article-body .lede{
    font-size:17px;
    color:#3A362E;
    margin-bottom:10px;
}

.article-body h2{
    font-size:21px;
    margin:34px 0 12px;
}

.article-body p{
    color:#3A362E;
    font-size:15px;
    margin-bottom:6px;
}

.article-cta{
    margin-top:44px;
    padding-top:30px;
    border-top:1px solid #E2D9C4;
}
"""

CARD_GRID_STYLE = """
.res-article-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
    margin-top:15px;
}

.res-article-card{
    display:flex;
    flex-direction:column;
    height:100%;
}

.res-article-card .cat-tag{
    color:#B8863E;
    font-size:10px;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.6px;
    margin-bottom:10px;
}

.res-article-card h3{
    font-size:17px;
    margin-bottom:8px;
}

.res-article-card p{
    color:#5B5548;
    font-size:13px;
    flex:1;
}

.res-article-card .read-more{
    margin-top:14px;
    font-size:11px;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.6px;
    color:#B8863E;
}

.cat-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
    margin-top:15px;
}

@media(max-width:850px){
    .res-article-grid{grid-template-columns:1fr 1fr;}
    .cat-grid{grid-template-columns:1fr;}
}

@media(max-width:560px){
    .res-article-grid{grid-template-columns:1fr;}
}
"""

CTA_BLOCK = {
    "employer": (
        "Looking to fill a role?",
        "Tell Southern Point what you need and we'll follow up to discuss next steps.",
        "/request-talent/", "Request Talent",
    ),
    "candidate": (
        "Ready for your next opportunity?",
        "Search current openings or submit your resume for general consideration.",
        "/jobs.html", "Find Jobs",
    ),
}

def article_card(a):
    return f"""
<a href="/resources/{a['slug']}/" class="card res-article-card">
<div class="cat-tag">{a['category_label']}</div>
<h3>{a['title']}</h3>
<p>{a['description']}</p>
<span class="read-more">Read Article &rarr;</span>
</a>"""

# ---------------------------------------------------------------------------
# Resources hub
# ---------------------------------------------------------------------------
def build_hub():
    cat_cards = "\n".join(f"""
<a href="/{c['path']}/" class="card">
<div class="card-number">&rarr;</div>
<h3>{c['label']}</h3>
<p>{c['intro']}</p>
</a>""" for c in CATEGORIES.values())

    featured = "\n".join(article_card(a) for a in ARTICLES)

    body = f"""
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">RESOURCES</div>
<h1>Workforce Insights.</h1>
<p>Practical, original guidance for employers and job seekers — hiring advice, career advice, and industry-specific insights, all in one place.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">EXPLORE BY CATEGORY</div>
<h2 class="section-title">Find guidance built for your side of the table.</h2>
<div class="cat-grid">
{cat_cards}
</div>
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">FEATURED ARTICLES</div>
<h2 class="section-title">Recent guidance from Southern Point.</h2>
<div class="res-article-grid">
{featured}
</div>
</div>
</section>

<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">READY TO TAKE ACTION?</div>
<h2 class="section-title">Whichever side of the table you're on.</h2>
<div class="btn-row" style="justify-content:center; margin-top:10px;">
<a class="btn btn-red" href="/request-talent/">Request Talent</a>
<a class="btn btn-outline-white" href="/jobs.html">Find Jobs</a>
</div>
</div>
</section>
"""

    html = build(
        title="Resources | Southern Point Staffing",
        description="Original hiring advice, career advice, and industry insights from Southern Point, covering staffing models, resumes, interviews, and more.",
        extra_style=CARD_GRID_STYLE,
        body_html=body,
        section="resources",
        canonical="https://southernpointllc.com/resources/",
    )
    os.makedirs(f"{BASE}/resources", exist_ok=True)
    with open(f"{BASE}/resources/index.html", "w") as f:
        f.write(html)
    print("wrote resources/index.html")

# ---------------------------------------------------------------------------
# Category pages
# ---------------------------------------------------------------------------
def build_category(key, cat):
    cat_articles = [a for a in ARTICLES if a["category"] == key]
    cards = "\n".join(article_card(a) for a in cat_articles)

    extra = ""
    if key == "industry-insights":
        chips = "\n".join(
            f'<a href="/industries/{slug}/" style="border:1px solid #E2D9C4; padding:16px; text-align:center; font-weight:800; font-size:13px;">{name}</a>'
            for name, slug in [("Technology","technology"),("Healthcare","healthcare"),("Sales","sales"),("Operations","operations"),("Administrative","administrative")]
        )
        extra = f"""
<section class="tint">
<div class="container">
<div class="section-label">BROWSE BY INDUSTRY</div>
<h2 class="section-title">See staffing pages for each focus area.</h2>
<div class="cat-grid" style="margin-top:20px;">
{chips}
</div>
</div>
</section>
"""

    cta_href, cta_label = ("/request-talent/", "Request Talent") if key == "hiring" else ("/jobs.html", "Find Jobs")

    body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span>{cat['label']}</div>
<div class="eyebrow eyebrow-light">RESOURCES</div>
<h1>{cat['label']}.</h1>
<p>{cat['intro']}</p>
</div>
</section>

<section>
<div class="container">
<div class="res-article-grid">
{cards}
</div>
</div>
</section>
{extra}
<section class="dark" style="text-align:center;">
<div class="container">
<div class="section-label" style="justify-content:center;">TAKE THE NEXT STEP</div>
<h2 class="section-title">Put this into action.</h2>
<a class="btn btn-red" href="{cta_href}" style="margin-top:10px;">{cta_label}</a>
</div>
</section>
"""

    html = build(
        title=f"{cat['label']} | Southern Point Resources",
        description=cat["intro"],
        extra_style=CARD_GRID_STYLE,
        body_html=body,
        section="resources",
        canonical=f"https://southernpointllc.com/{cat['path']}/",
    )
    os.makedirs(f"{BASE}/{cat['path']}", exist_ok=True)
    with open(f"{BASE}/{cat['path']}/index.html", "w") as f:
        f.write(html)
    print(f"wrote {cat['path']}/index.html")

# ---------------------------------------------------------------------------
# Article pages
# ---------------------------------------------------------------------------
def build_article(a):
    sections_html = "\n".join(f"<h2>{h}</h2>\n<p>{p}</p>" for h, p in a["sections"])
    cat = CATEGORIES[a["category"]]
    cta_title, cta_body, cta_href, cta_label = CTA_BLOCK[a["cta"]]

    body = f"""
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><a href="/{cat['path']}/">{cat['label']}</a><span>/</span>{a['title']}</div>
<div class="eyebrow eyebrow-light">{a['category_label'].upper()}</div>
<h1>{a['title']}</h1>
</div>
</section>

<section>
<div class="container">
<div class="article-body">
<p class="lede">{a['intro']}</p>
{sections_html}
<p>{a['closing']}</p>

<div class="article-cta">
<div class="section-label">{cta_title.upper()}</div>
<p style="color:#5B5548; margin-bottom:16px;">{cta_body}</p>
<a class="btn btn-red" href="{cta_href}">{cta_label}</a>
</div>
</div>
</div>
</section>

<section class="tint">
<div class="container">
<div class="section-label">MORE FROM {cat['label'].upper()}</div>
<h2 class="section-title">Continue reading.</h2>
<a class="btn btn-outline" href="/{cat['path']}/" style="margin-top:10px;">View All {cat['label']}</a>
</div>
</section>
"""

    html = build(
        title=f"{a['title']} | Southern Point Resources",
        description=a["description"],
        extra_style=ARTICLE_STYLE,
        body_html=body,
        section="resources",
        canonical=f"https://southernpointllc.com/resources/{a['slug']}/",
        og_type="article",
    )
    out_dir = f"{BASE}/resources/{a['slug']}"
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/index.html", "w") as f:
        f.write(html)
    print(f"wrote resources/{a['slug']}/index.html")


if __name__ == "__main__":
    build_hub()
    for key, cat in CATEGORIES.items():
        build_category(key, cat)
    for a in ARTICLES:
        build_article(a)
