#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
.rt-layout{
    display:grid;
    grid-template-columns:1fr 1.3fr;
    gap:60px;
    align-items:start;
}

.rt-side h3{
    font-size:18px;
    margin:26px 0 8px;
}

.rt-side p{
    color:#5B5548;
    font-size:14px;
}

.rt-side .step{
    margin-bottom:0;
}

#durationField,
#deadlineField{
    display:none;
}

@media(max-width:900px){
    .rt-layout{
        grid-template-columns:1fr;
    }
}
"""

body = """
<section class="page-hero">
<div class="container">
<div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/services/staffing-recruiting/">For Employers</a><span>/</span>Request Talent</div>
<div class="eyebrow eyebrow-light">FOR EMPLOYERS</div>
<h1>Tell Us Who You Need.</h1>
<p>Share your hiring need below and Southern Point will follow up to discuss the role, timeline, and next steps — usually within one business day.</p>
</div>
</section>

<section>
<div class="container rt-layout">

<div class="rt-side">
<div class="section-label">WHAT HAPPENS NEXT</div>
<div class="process-grid" style="grid-template-columns:1fr;">
<div class="step">
<div class="step-number">01</div>
<h3>We Review Your Request</h3>
<p>Southern Point reviews the details you submit — no automated matching, an actual review.</p>
</div>
<div class="step">
<div class="step-number">02</div>
<h3>We Follow Up</h3>
<p>We reach out to confirm details and answer any questions before sourcing begins.</p>
</div>
<div class="step">
<div class="step-number">03</div>
<h3>We Get to Work</h3>
<p>Sourcing and screening begins against your specific requirements.</p>
</div>
</div>

<div style="margin-top:36px; padding-top:28px; border-top:1px solid var(--sp-line-dark);">
<div class="section-label">NOT READY FOR A FORM?</div>
<p>Email us directly and we'll get back to you the same way.</p>
<a href="mailto:contact@southernpointllc.com?subject=Recruiting%20Support%20Inquiry" style="display:inline-block; margin-top:12px; font-weight:800; color:#B8863E;">contact@southernpointllc.com</a>
</div>
</div>

<div class="form-card">

<form
id="requestTalentForm"
action="https://formsubmit.co/contact@southernpointllc.com"
method="POST">

<input type="hidden" name="_subject" value="Request Talent Submission — Southern Point">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://southernpointllc.com/request-talent/?submitted=1">
<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">

<div class="section-label">CONTACT INFORMATION</div>

<div class="form-row">
<div>
<label class="form-label first">Full Name</label>
<input class="form-input" type="text" name="Contact Name" required>
</div>
<div>
<label class="form-label first">Email</label>
<input class="form-input" type="email" name="Email" required>
</div>
</div>

<div class="form-row">
<div>
<label class="form-label">Phone</label>
<input class="form-input" type="tel" name="Phone">
</div>
<div>
<label class="form-label">Company Name</label>
<input class="form-input" type="text" name="Company" required>
</div>
</div>

<div class="section-label" style="margin-top:34px;">HIRING NEED</div>

<label class="form-label first">Industry</label>
<select class="form-select" name="Industry" required>
<option value="">Select an industry</option>
<option>Technology</option>
<option>Healthcare</option>
<option>Sales</option>
<option>Operations</option>
<option>Administrative</option>
<option>Not sure / other</option>
</select>

<label class="form-label">Position(s) Needed</label>
<input class="form-input" type="text" name="Positions Needed" placeholder="e.g. Administrative Assistant, Help Desk Analyst" required>

<div class="form-row">
<div>
<label class="form-label">Number of Openings</label>
<input class="form-input" type="number" min="1" name="Number of Openings" required>
</div>
<div>
<label class="form-label">Location</label>
<input class="form-input" type="text" name="Location" placeholder="City, State or Remote" required>
</div>
</div>

<label class="form-label">Employment Type</label>
<select class="form-select" id="employmentType" name="Employment Type" required>
<option value="">Select an engagement type</option>
<option>Temporary Staffing</option>
<option>Temp-to-Hire</option>
<option>Direct Hire</option>
<option>Contract Staffing</option>
<option>High-Volume Staffing</option>
<option>Not sure</option>
</select>

<div id="durationField">
<label class="form-label">Expected Duration</label>
<input class="form-input" type="text" name="Expected Duration" placeholder="e.g. 3 months, through end of year">
</div>

<label class="form-label">Timeline to Fill</label>
<select class="form-select" id="timeline" name="Timeline" required>
<option value="">Select a timeline</option>
<option>Immediately</option>
<option>Within 2 weeks</option>
<option>Within 30 days</option>
<option>Flexible / planning ahead</option>
</select>

<div id="deadlineField">
<label class="form-label">Target Start Date</label>
<input class="form-input" type="date" name="Target Start Date">
</div>

<label class="form-label">Additional Requirements</label>
<textarea class="form-textarea" name="Additional Requirements" rows="4" placeholder="Certifications, software, shift/schedule, or anything else Southern Point should know."></textarea>

<label class="form-consent">
<input type="checkbox" required>
I consent to Southern Point contacting me regarding this request.
</label>

<button type="submit" class="btn btn-block">Submit Request</button>

<p class="form-note">Southern Point typically responds within one business day. Submitting this form does not create any obligation to hire.</p>

</form>

</div>

</div>
</section>
"""

SCRIPT = """
<script>
(function(){
    var employmentType = document.getElementById("employmentType");
    var durationField = document.getElementById("durationField");
    var timeline = document.getElementById("timeline");
    var deadlineField = document.getElementById("deadlineField");

    function syncDuration(){
        var show = employmentType.value === "Temporary Staffing" || employmentType.value === "Contract Staffing";
        durationField.style.display = show ? "block" : "none";
    }

    function syncDeadline(){
        var show = timeline.value === "Flexible / planning ahead";
        deadlineField.style.display = show ? "block" : "none";
    }

    if(employmentType){
        employmentType.addEventListener("change", syncDuration);
        syncDuration();
    }

    if(timeline){
        timeline.addEventListener("change", syncDeadline);
        syncDeadline();
    }
})();
</script>
"""

html = build(
    title="Request Talent | Southern Point Staffing",
    description="Tell Southern Point about your hiring need — position, timeline, and requirements — and we'll follow up to discuss next steps.",
    extra_style=STYLE,
    body_html=body + SCRIPT,
    section="employers",
    canonical="https://southernpointllc.com/request-talent/",
)

with open(f"{BASE}/request-talent/index.html", "w") as f:
    f.write(html)

print("wrote request-talent/index.html")
