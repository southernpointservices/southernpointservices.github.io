#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

# ---------------------------------------------------------------------------
# /contact/
# ---------------------------------------------------------------------------
CONTACT_STYLE = """
.contact-info{
    display:flex;
    flex-wrap:wrap;
    gap:30px;
    margin-top:20px;
}

.contact-info-item{
    font-size:14px;
    color:#3A362E;
}

.contact-info-item strong{
    display:block;
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:.6px;
    color:#8C8270;
    margin-bottom:4px;
}

.contact-info-item a{
    color:#B8863E;
    font-weight:700;
}

/* =========================
   "WHAT CAN WE HELP WITH" SELECTOR
========================= */
.help-options{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:16px;
    margin-top:26px;
}

.help-option{
    display:block;
    width:100%;
    text-align:left;
    border:1px solid var(--sp-line);
    background:#ffffff;
    padding:24px 22px;
    font-family:inherit;
    cursor:pointer;
    transition:border-color .2s ease, background-color .2s ease;
}

.help-option:hover{
    border-color:var(--sp-bronze);
}

.help-option strong{
    display:block;
    font-family:var(--font-display);
    font-size:16px;
    letter-spacing:-.2px;
    color:var(--sp-ink);
    margin-bottom:8px;
}

.help-option span{
    display:block;
    font-size:13px;
    color:var(--sp-muted);
    line-height:1.5;
}

.help-option.active{
    border-color:var(--sp-bronze-dark);
    background:var(--sp-cream-2);
}

/* =========================
   SUBTLE SUPPORTING PHOTOGRAPHY
========================= */
.contact-photo{
    margin-top:30px;
    max-width:320px;
}

.help-option.active strong{
    color:var(--sp-bronze-dark);
}

@media(prefers-reduced-motion: reduce){
    .help-option:hover{ transform:none; }
}

@media(max-width:980px){
    .help-options{grid-template-columns:1fr 1fr;}
}
@media(max-width:560px){
    .help-options{grid-template-columns:1fr;}
}

/* =========================
   DYNAMIC FORM FIELD GROUPS
========================= */
.contact-field-group{
    display:none;
}

.contact-field-group.is-visible{
    display:block;
    animation:fieldFadeIn .35s ease;
}

@keyframes fieldFadeIn{
    from{ opacity:0; transform:translateY(6px); }
    to{ opacity:1; transform:translateY(0); }
}

@media(prefers-reduced-motion: reduce){
    .contact-field-group.is-visible{ animation:none; }
}

#panel-job h3{
    font-size:20px;
    margin-bottom:10px;
}

#panel-job p{
    color:var(--sp-muted);
    font-size:14px;
    margin-bottom:20px;
}

#panel-job .btn-row{
    flex-direction:column;
    align-items:stretch;
}
"""

INSTITUTIONAL_TYPES = [
    "Government / Public Sector", "Prime Contractor", "Healthcare Organization",
    "Technology Organization", "Commercial / Enterprise", "Other Institutional Organization",
]

institutional_options = "\n".join(f"<option>{t}</option>" for t in INSTITUTIONAL_TYPES)

contact_body = f"""
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">CONTACT</div>
<h1>Let's Start a Conversation.</h1>
<p>Tell Southern Point what you need, and we'll follow up directly — usually within one business day.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">GET STARTED</div>
<h2 class="section-title">What can we help you with?</h2>
<p class="section-intro">Choose what best describes why you're reaching out, and the form below will adjust to match.</p>

<div class="help-options" role="group" aria-label="What can we help you with?">
<button type="button" class="help-option active" data-target="talent">
<strong>I'm looking for talent</strong>
<span>Staffing &amp; recruiting for an open role at your organization</span>
</button>
<button type="button" class="help-option" data-target="professional">
<strong>I need professional services</strong>
<span>Workforce, operational, or specialized resource support</span>
</button>
<button type="button" class="help-option" data-target="job">
<strong>I'm looking for a job</strong>
<span>Search openings, submit your resume, or set up alerts</span>
</button>
<button type="button" class="help-option" data-target="other">
<strong>Something else</strong>
<span>General questions or anything not listed above</span>
</button>
</div>

</div>
</section>

<section class="tint">
<div class="container split">

<div>
<div class="section-label">REACH US DIRECTLY</div>
<h2 class="section-title">Southern Point Professional Services</h2>
<p style="color:#5B5548; margin-bottom:10px;">Southern Point supports employers and job seekers across Technology, Healthcare, Sales, Operations, and Administrative roles nationwide — through staffing and recruiting, professional services, workforce solutions, and specialized resource coordination.</p>

<div class="contact-info">
<div class="contact-info-item">
<strong>Email</strong>
<a href="mailto:southernpoint.services@gmail.com">southernpoint.services@gmail.com</a>
</div>
<div class="contact-info-item">
<strong>Location</strong>
Houston, Texas &middot; Serving organizations nationwide
</div>
</div>

<div class="photo-frame ratio-portrait contact-photo">
<img class="photo" src="/assets/images/contact-subtle.jpg" alt="A quiet Southern Point workspace detail">
</div>
</div>

<div class="form-card">

<div id="panel-job" class="contact-field-group">
<h3>Looking for your next opportunity?</h3>
<p>There's never a cost to candidates. Search current openings, submit your resume for general consideration, or sign up for alerts so we reach out when a fit comes up.</p>
<div class="btn-row">
<a class="btn btn-red" href="/jobs.html">Find Jobs</a>
<a class="btn btn-outline" href="/submit-resume/">Submit Resume</a>
<a class="btn btn-outline" href="/job-alerts/">Job Alerts</a>
</div>
</div>

<form
id="contactForm"
action="https://formsubmit.co/southernpoint.services@gmail.com"
method="POST">

<input type="hidden" name="_subject" id="contactSubject" value="Talent Request — Southern Point Contact Form">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://southernpointllc.com/contact/?contacted=1">
<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">
<input type="hidden" name="Inquiry Type" id="inquiryTypeField" value="I'm looking for talent">

<div class="form-row">
<div>
<label class="form-label first">Full Name</label>
<input class="form-input" type="text" name="Name" required>
</div>
<div>
<label class="form-label first">Email</label>
<input class="form-input" type="email" name="Email" required>
</div>
</div>

<div id="group-orgfields" class="contact-field-group is-visible">
<div class="form-row">
<div>
<label class="form-label">Organization Name</label>
<input class="form-input" type="text" name="Organization Name">
</div>
<div>
<label class="form-label">Phone</label>
<input class="form-input" type="tel" name="Phone">
</div>
</div>
</div>

<div id="group-orgtype" class="contact-field-group">
<label class="form-label">Organization Type</label>
<select class="form-select" name="Organization Type">
<option value="">Select one</option>
{institutional_options}
</select>
</div>

<label class="form-label" id="contactMessageLabel">Message</label>
<textarea class="form-textarea" id="contactMessage" name="Message" rows="5" required placeholder="Tell us about the role you're hiring for, timeline, and any details that would help."></textarea>

<button type="submit" class="btn btn-block">Send Message</button>

<p class="form-note">Southern Point typically responds within one business day.</p>

</form>

</div>

</div>
</section>

<script>
(function(){{
    var options = document.querySelectorAll(".help-option");
    var form = document.getElementById("contactForm");
    var panelJob = document.getElementById("panel-job");
    var groupOrgFields = document.getElementById("group-orgfields");
    var groupOrgType = document.getElementById("group-orgtype");
    var subjectField = document.getElementById("contactSubject");
    var inquiryTypeField = document.getElementById("inquiryTypeField");
    var messageField = document.getElementById("contactMessage");

    var CONFIG = {{
        talent: {{
            label: "I'm looking for talent",
            subject: "Talent Request — Southern Point Contact Form",
            placeholder: "Tell us about the role you're hiring for, timeline, and any details that would help.",
            showOrgFields: true,
            showOrgType: false
        }},
        professional: {{
            label: "I need professional services",
            subject: "Professional Services Inquiry — Southern Point Contact Form",
            placeholder: "Tell us what kind of support your organization needs — workforce, operational, or specialized resources.",
            showOrgFields: true,
            showOrgType: true
        }},
        other: {{
            label: "Something else",
            subject: "General Inquiry — Southern Point Contact Form",
            placeholder: "How can we help?",
            showOrgFields: false,
            showOrgType: false
        }}
    }};

    function setGroupVisible(el, visible){{
        if(!el) return;
        if(visible){{
            el.style.display = "block";
            el.classList.add("is-visible");
        }}else{{
            el.style.display = "none";
            el.classList.remove("is-visible");
        }}
    }}

    function select(target){{
        options.forEach(function(opt){{
            opt.classList.toggle("active", opt.getAttribute("data-target") === target);
        }});

        if(target === "job"){{
            setGroupVisible(panelJob, true);
            if(form) form.style.display = "none";
            return;
        }}

        setGroupVisible(panelJob, false);
        if(form) form.style.display = "block";

        var cfg = CONFIG[target] || CONFIG.other;
        setGroupVisible(groupOrgFields, cfg.showOrgFields);
        setGroupVisible(groupOrgType, cfg.showOrgType);
        if(subjectField) subjectField.value = cfg.subject;
        if(inquiryTypeField) inquiryTypeField.value = cfg.label;
        if(messageField) messageField.placeholder = cfg.placeholder;
    }}

    options.forEach(function(opt){{
        opt.addEventListener("click", function(){{
            select(opt.getAttribute("data-target"));
        }});
    }});
}})();
</script>
"""

# ---------------------------------------------------------------------------
# Legal pages — shared prose style
# ---------------------------------------------------------------------------
LEGAL_STYLE = """
.legal-body{
    max-width:800px;
}

.legal-updated{
    color:#8C8270;
    font-size:12px;
    margin-bottom:30px;
}

.legal-body h2{
    font-size:19px;
    margin:30px 0 10px;
}

.legal-body p{
    color:#3A362E;
    font-size:14px;
    margin-bottom:10px;
}

.legal-body ul{
    padding-left:20px;
    color:#3A362E;
    font-size:14px;
    line-height:1.8;
    margin-bottom:10px;
}

.legal-body a{
    color:#B8863E;
    font-weight:700;
}
"""

PRIVACY_BODY = """
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span>Privacy Policy</div>
<div class="eyebrow eyebrow-light">LEGAL</div>
<h1>Privacy Policy.</h1>
</div>
</section>

<section>
<div class="container">
<div class="legal-body">
<p class="legal-updated">Effective date: September 2026</p>

<p>This Privacy Policy explains how Southern Point Professional Services ("Southern Point," "we," "us") collects, uses, and handles information through southernpointllc.com (the "Site"). Southern Point is a trade name used by DeJaun Henry Jr., Sole Proprietor.</p>

<h2>Information We Collect</h2>
<p>Southern Point collects information you choose to provide directly through forms on the Site, including:</p>
<ul>
<li>Contact information such as your name, email address, and phone number.</li>
<li>Employment-related information such as a resume, job title, industry of interest, and any details you include in an application, resume submission, or staffing request.</li>
<li>The content of any message you send through a contact or inquiry form.</li>
</ul>
<p>The Site does not require you to create an account, and does not collect payment information from job seekers — there is never a cost to candidates to use Southern Point's services.</p>

<h2>How We Use Information</h2>
<p>Information submitted through the Site is used to:</p>
<ul>
<li>Respond to inquiries from employers and job seekers.</li>
<li>Evaluate candidates for current and future job opportunities.</li>
<li>Follow up regarding a staffing request, job application, or general inquiry.</li>
</ul>
<p>Southern Point does not sell personal information to third parties.</p>

<h2>How Forms Are Processed</h2>
<p>Forms on this Site are processed using FormSubmit, a third-party form-processing service, which delivers form submissions by email to Southern Point. Submitting a form on this Site means your information is transmitted through that third-party service in order to reach Southern Point. Southern Point does not maintain a separate database of website form submissions beyond the email records generated this way.</p>

<h2>Cookies and Tracking</h2>
<p>This Site does not currently use advertising cookies or third-party tracking for marketing purposes. If that changes in the future, this Privacy Policy will be updated to reflect it.</p>

<h2>Data Retention</h2>
<p>Resumes and application information may be retained by Southern Point for consideration against current and future opportunities. If you would like your information removed, contact Southern Point using the information below and we will honor reasonable requests.</p>

<h2>Children's Privacy</h2>
<p>This Site is intended for individuals who are at least 18 years old and is not directed to children. Southern Point does not knowingly collect information from children.</p>

<h2>Changes to This Policy</h2>
<p>Southern Point may update this Privacy Policy from time to time. The effective date above reflects the most recent update.</p>

<h2>Contact</h2>
<p>Questions about this Privacy Policy can be sent to <a href="mailto:southernpoint.services@gmail.com">southernpoint.services@gmail.com</a>.</p>
</div>
</div>
</section>
"""

TERMS_BODY = """
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span>Terms of Use</div>
<div class="eyebrow eyebrow-light">LEGAL</div>
<h1>Terms of Use.</h1>
</div>
</section>

<section>
<div class="container">
<div class="legal-body">
<p class="legal-updated">Effective date: September 2026</p>

<p>These Terms of Use govern your use of southernpointllc.com (the "Site"), operated by Southern Point Professional Services, a trade name used by DeJaun Henry Jr., Sole Proprietor. By using the Site, you agree to these terms.</p>

<h2>Use of the Site</h2>
<p>The Site is provided to share information about Southern Point's staffing and recruiting services, to allow employers to submit staffing requests, and to allow job seekers to browse openings and submit applications or resumes. You agree to use the Site only for these lawful purposes and to provide accurate information in any form you submit.</p>

<h2>No Guarantee of Placement or Employment</h2>
<p>Submitting a staffing request does not guarantee that Southern Point will be able to fill the role, and submitting an application or resume does not guarantee an interview, referral, or job placement. Southern Point evaluates every submission individually and follows up when there is a potential fit.</p>

<h2>Job Listings</h2>
<p>Job listings on the Site reflect current openings Southern Point is aware of at the time they are posted. Listings may be updated, filled, or removed at any time without notice. For roles marked as an external application, you will be directed to the original employer's or job board's application page, which is not operated by Southern Point.</p>

<h2>Third-Party Services and Links</h2>
<p>The Site uses FormSubmit, a third-party service, to process form submissions, and may link to third-party sites (such as an employer's own career page). Southern Point is not responsible for the content, policies, or practices of third-party websites or services.</p>

<h2>Intellectual Property</h2>
<p>The content, design, and branding of the Site are the property of Southern Point Professional Services and may not be copied or reused without permission, except as necessary to use the Site for its intended purpose (such as printing a job listing for your own reference).</p>

<h2>Disclaimer of Warranties</h2>
<p>The Site is provided "as is" without warranties of any kind. Southern Point does not guarantee that the Site will be uninterrupted, error-free, or that any information on it is complete or current at all times.</p>

<h2>Limitation of Liability</h2>
<p>To the fullest extent permitted by law, Southern Point is not liable for any indirect, incidental, or consequential damages arising from your use of the Site.</p>

<h2>Governing Law</h2>
<p>These Terms of Use are governed by the laws of the State of Texas, without regard to conflict-of-law principles.</p>

<h2>Changes to These Terms</h2>
<p>Southern Point may update these Terms of Use from time to time. The effective date above reflects the most recent update.</p>

<h2>Contact</h2>
<p>Questions about these Terms of Use can be sent to <a href="mailto:southernpoint.services@gmail.com">southernpoint.services@gmail.com</a>.</p>
</div>
</div>
</section>
"""

ACCESSIBILITY_BODY = """
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span>Accessibility</div>
<div class="eyebrow eyebrow-light">LEGAL</div>
<h1>Accessibility.</h1>
</div>
</section>

<section>
<div class="container">
<div class="legal-body">
<p class="legal-updated">Effective date: September 2026</p>

<p>Southern Point Professional Services is committed to making southernpointllc.com usable by as many people as possible, including people with disabilities.</p>

<h2>Our Approach</h2>
<p>The Site is built with semantic HTML, keyboard-accessible navigation and forms, and readable color contrast, with WCAG 2.1 Level AA as an ongoing guideline for new and updated pages. Accessibility is an ongoing effort rather than a one-time project, and improvements are made as the Site continues to grow.</p>

<h2>Known Limitations</h2>
<p>As with most websites, some pages or third-party elements (such as embedded forms) may not yet meet every accessibility guideline. If you encounter a barrier using the Site, we want to know about it so we can address it.</p>

<h2>Alternative Access</h2>
<p>If any part of the Site is difficult for you to access or use, you can reach Southern Point directly by email and we will work with you to provide the information or service you need in another way.</p>

<h2>Contact</h2>
<p>Accessibility feedback can be sent to <a href="mailto:southernpoint.services@gmail.com">southernpoint.services@gmail.com</a>. Please describe the issue and the page you were trying to use, and we will follow up.</p>
</div>
</div>
</section>
"""

PAGES = [
    ("contact", contact_body, CONTACT_STYLE,
     "Contact Southern Point | Workforce & Professional Services",
     "Contact Southern Point to find talent, search jobs, submit your resume, or send an organizational or general inquiry.",
     "https://southernpointllc.com/contact/", "contact"),
    ("privacy", PRIVACY_BODY, LEGAL_STYLE,
     "Privacy Policy | Southern Point",
     "How Southern Point Professional Services collects, uses, and handles information submitted through southernpointllc.com.",
     "https://southernpointllc.com/privacy/", "legal"),
    ("terms", TERMS_BODY, LEGAL_STYLE,
     "Terms of Use | Southern Point",
     "Terms governing the use of southernpointllc.com, operated by Southern Point Professional Services.",
     "https://southernpointllc.com/terms/", "legal"),
    ("accessibility", ACCESSIBILITY_BODY, LEGAL_STYLE,
     "Accessibility | Southern Point",
     "Southern Point's ongoing commitment to making southernpointllc.com accessible to all users.",
     "https://southernpointllc.com/accessibility/", "legal"),
]

for path, body_html, style, title, description, canonical, section in PAGES:
    html = build(
        title=title,
        description=description,
        extra_style=style,
        body_html=body_html,
        section=section,
        canonical=canonical,
    )
    out_dir = f"{BASE}/{path}"
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/index.html", "w") as f:
        f.write(html)
    print(f"wrote {path}/index.html")
