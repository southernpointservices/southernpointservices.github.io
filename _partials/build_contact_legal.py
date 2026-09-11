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
.contact-paths{
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    gap:20px;
    margin-top:15px;
}

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

@media(max-width:850px){
    .contact-paths{grid-template-columns:1fr;}
}
"""

INSTITUTIONAL_TYPES = [
    "Government / Public Sector", "Prime Contractor", "Healthcare Organization",
    "Technology Organization", "Commercial / Enterprise", "Other Institutional Organization",
]

institutional_options = "\n".join(f"<option>{t}</option>" for t in INSTITUTIONAL_TYPES)

contact_body = """
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">CONTACT</div>
<h1>Let's Start The Conversation.</h1>
<p>Whether you're hiring or looking for your next role, here's the fastest way to reach Southern Point.</p>
</div>
</section>

<section>
<div class="container">
<div class="section-label">CHOOSE YOUR PATH</div>
<h2 class="section-title">Get where you need to go faster.</h2>
<div class="contact-paths">

<div class="card">
<div class="card-number">01</div>
<h3>I'm Hiring</h3>
<p>Tell Southern Point about an open role and we'll follow up to discuss timeline, requirements, and next steps.</p>
<a class="btn btn-outline" href="/request-talent/" style="margin-top:14px;">Request Talent</a>
</div>

<div class="card">
<div class="card-number">02</div>
<h3>I'm Job Searching</h3>
<p>Browse current openings or submit your resume for general consideration — there's no cost to candidates.</p>
<div class="btn-row" style="margin-top:14px;">
<a class="btn btn-outline" href="/jobs.html">Find Jobs</a>
<a class="btn btn-outline" href="/submit-resume/">Submit Resume</a>
</div>
</div>

<div class="card">
<div class="card-number">03</div>
<h3>I Represent an Organization</h3>
<p>Inquiring on behalf of a commercial, healthcare, technology, institutional, or government-related organization? Share some detail below.</p>
<a class="btn btn-outline" href="#institutional" style="margin-top:14px;">Institutional Inquiry</a>
</div>

</div>
</div>
</section>

<section class="tint">
<div class="container split">

<div>
<div class="section-label">GENERAL INQUIRIES</div>
<h2 class="section-title">Send us a message.</h2>
<p style="color:#5B5548; margin-bottom:10px;">For anything that doesn't fit the paths above — questions, partnership inquiries, or anything else — use the form and Southern Point will respond directly.</p>

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
</div>

<div class="form-card">
<form
id="contactForm"
action="https://formsubmit.co/southernpoint.services@gmail.com"
method="POST">

<input type="hidden" name="_subject" value="Contact Form Submission — Southern Point">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://southernpointllc.com/contact/?contacted=1">
<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">

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

<label class="form-label">I am a...</label>
<select class="form-select" name="I Am A" required>
<option value="">Select one</option>
<option>Employer</option>
<option>Job Seeker</option>
<option>Other</option>
</select>

<label class="form-label">Message</label>
<textarea class="form-textarea" name="Message" rows="5" required></textarea>

<button type="submit" class="btn btn-block">Send Message</button>

<p class="form-note">Southern Point typically responds within one business day.</p>

</form>
</div>

</div>
</section>

<section id="institutional">
<div class="container split">

<div>
<div class="section-label">INSTITUTIONAL &amp; ORGANIZATIONAL INQUIRIES</div>
<h2 class="section-title">Inquiring on behalf of an organization?</h2>
<p style="color:#5B5548; margin-bottom:10px;">Southern Point supports organizations with workforce, professional, administrative, operational, and project-related requirements — commercial businesses, healthcare and technology organizations, prime contractors, and other institutional or government-related organizations alike.</p>
<p style="color:#5B5548;">Share some detail below and a member of our team will review your inquiry and follow up directly.</p>
</div>

<div class="form-card">
<form
id="institutionalForm"
action="https://formsubmit.co/southernpoint.services@gmail.com"
method="POST">

<input type="hidden" name="_subject" value="Institutional Inquiry — Southern Point">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://southernpointllc.com/contact/?institutional=1">
<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">

<div class="form-row">
<div>
<label class="form-label first">Organization Name</label>
<input class="form-input" type="text" name="Organization Name" required>
</div>
<div>
<label class="form-label first">Your Title</label>
<input class="form-input" type="text" name="Title" required>
</div>
</div>

<div class="form-row">
<div>
<label class="form-label">Business Email</label>
<input class="form-input" type="email" name="Business Email" required>
</div>
<div>
<label class="form-label">Phone</label>
<input class="form-input" type="tel" name="Phone" required>
</div>
</div>

<label class="form-label">Organization Type</label>
<select class="form-select" name="Organization Type" required>
<option value="">Select one</option>
{institutional_options}
</select>

<label class="form-label">Services Needed</label>
<textarea class="form-textarea" name="Services Needed" rows="3" placeholder="Staffing, professional services, workforce solutions, specialized resources, etc."></textarea>

<label class="form-label">Message</label>
<textarea class="form-textarea" name="Message" rows="4" required></textarea>

<button type="submit" class="btn btn-block">Submit Inquiry</button>

<p class="form-note">Inquiries are reviewed individually by our team — nothing is sent automatically in response to this form.</p>

</form>
</div>

</div>
</section>
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
