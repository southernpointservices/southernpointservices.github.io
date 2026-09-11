#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/southern-point-site/_partials")
from assemble import build

BASE = "/home/claude/southern-point-site"

STYLE = """
/* SEARCH */
.search-area{
    margin-top:-28px;
    position:relative;
    z-index:5;
}

.search-box{
    background:#ffffff;
    border:1px solid #E2D9C4;
    box-shadow:0 12px 35px rgba(16,24,32,.10);
    padding:25px;
}

.search-grid{
    display:grid;
    grid-template-columns:1.5fr 1fr 1fr auto;
    gap:12px;
}

.search-input,
.search-select{
    width:100%;
    height:50px;
    border:1px solid #E2D9C4;
    background:#ffffff;
    padding:0 15px;
    font-family:inherit;
    font-size:13px;
    color:#1C1A16;
    outline:none;
}

.search-input:focus,
.search-select:focus{
    border-color:#B8863E;
}

.search-button{
    height:50px;
    border:0;
    background:#B8863E;
    color:#ffffff;
    padding:0 25px;
    font-size:11px;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.8px;
    cursor:pointer;
    font-family:inherit;
}

/* MAIN LAYOUT */
.jobs-main{
    padding:60px 0 100px;
}

.jobs-layout{
    display:grid;
    grid-template-columns:240px 1fr;
    gap:35px;
}

/* SIDEBAR */
.filters{
    background:#ffffff;
    border:1px solid #E2D9C4;
    padding:25px;
    height:max-content;
}

.filters h3{
    font-size:15px;
    margin-bottom:22px;
}

.filter-group{
    border-top:1px solid #E2D9C4;
    padding:20px 0;
}

.filter-group:first-of-type{
    border-top:none;
    padding-top:0;
}

.filter-group h4{
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:1px;
    margin-bottom:12px;
}

.filter-option{
    display:block;
    font-size:12px;
    color:#5B5548;
    margin:9px 0;
}

.filter-option input{
    margin-right:7px;
}

/* JOB CONTENT HEADER */
.jobs-header{
    display:flex;
    justify-content:space-between;
    align-items:end;
    gap:20px;
    margin-bottom:20px;
}

.jobs-header h2{
    font-size:27px;
    letter-spacing:-.8px;
}

.jobs-count{
    font-size:12px;
    color:#8C8270;
}

.sort{
    height:40px;
    border:1px solid #E2D9C4;
    background:#ffffff;
    padding:0 12px;
    font-size:12px;
    font-family:inherit;
}

/* JOB CARDS */
.job-list{
    display:flex;
    flex-direction:column;
    gap:14px;
}

.job-card{
    background:#ffffff;
    border:1px solid #E2D9C4;
    padding:27px 29px;
    transition:.2s ease;
}

.job-card:hover{
    border-color:#B8863E;
    transform:translateY(-2px);
    box-shadow:0 7px 22px rgba(16,24,32,.07);
}

.job-top{
    display:flex;
    justify-content:space-between;
    gap:20px;
}

.job-title{
    color:#B8863E;
    font-size:19px;
    font-weight:800;
    margin-bottom:5px;
}

.job-title a{
    color:inherit;
}

.job-title a:hover{
    text-decoration:underline;
}

.job-company{
    font-size:13px;
    font-weight:700;
    color:#3A362E;
}

.job-meta{
    display:flex;
    flex-wrap:wrap;
    gap:8px 18px;
    margin-top:15px;
    color:#5B5548;
    font-size:12px;
}

.job-meta span{
    display:inline-flex;
    align-items:center;
}

.job-tag{
    background:#F0E4C8;
    color:#B8863E;
    padding:5px 9px;
    font-size:9px;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.6px;
    flex-shrink:0;
    height:max-content;
}

.job-tag.fresh{
    background:#edf7f1;
    color:#247548;
}

.job-description{
    color:#5B5548;
    font-size:13px;
    margin-top:17px;
    max-width:850px;
}

.job-bottom{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:14px 20px;
    flex-wrap:wrap;
    margin-top:22px;
    padding-top:18px;
    border-top:1px solid #E2D9C4;
}

.job-posted{
    color:#8C8270;
    font-size:11px;
}

.job-actions{
    display:flex;
    gap:10px;
    align-items:center;
    flex-wrap:wrap;
}

.apply-btn{
    display:inline-block;
    background:#B8863E;
    color:#ffffff;
    padding:11px 17px;
    font-size:10px;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.6px;
    border:0;
    cursor:pointer;
    font-family:inherit;
}

.apply-btn:hover{
    background:#96702F;
}

.detail-link{
    display:inline-block;
    padding:11px 17px;
    font-size:10px;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.6px;
    border:1px solid #E2D9C4;
    color:#3A362E;
}

.detail-link:hover{
    border-color:#B8863E;
    color:#B8863E;
}

/* FEATURED STRIP */
.featured{
    background:#15171E;
    color:#ffffff;
    margin-bottom:35px;
    padding:27px 30px;
}

.featured-label{
    color:#D8B67A;
    font-size:10px;
    font-weight:900;
    letter-spacing:1.7px;
    margin-bottom:8px;
}

.featured h3{
    font-size:21px;
    margin-bottom:5px;
    color:#fff;
}

.featured p{
    color:#CFC9BB;
    font-size:12px;
}

/* EMPTY STATE */
.empty-state{
    background:#ffffff;
    border:1px solid #E2D9C4;
    padding:55px 35px;
    text-align:center;
}

.empty-state h3{
    font-size:21px;
    margin-bottom:12px;
}

.empty-state p{
    color:#5B5548;
    font-size:14px;
    max-width:520px;
    margin:0 auto 26px;
}

.notify-form{
    display:flex;
    gap:10px;
    max-width:420px;
    margin:0 auto;
    flex-wrap:wrap;
    justify-content:center;
}

.notify-input{
    height:48px;
    border:1px solid #E2D9C4;
    padding:0 14px;
    font-size:13px;
    font-family:inherit;
    flex:1;
    min-width:220px;
    outline:none;
}

.notify-input:focus{
    border-color:#B8863E;
}

.notify-form .search-button{
    height:48px;
}

/* EMPLOYER CTA */
.employer-banner{
    margin-top:60px;
    background:#B8863E;
    color:#ffffff;
    padding:45px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:30px;
}

.employer-banner h2{
    font-size:28px;
    line-height:1.15;
    margin-bottom:8px;
    color:#fff;
}

.employer-banner p{
    color:#CFC9BB;
    font-size:13px;
}

.employer-button{
    display:inline-block;
    background:#6E2436;
    color:#ffffff;
    padding:14px 22px;
    font-size:10px;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.7px;
    white-space:nowrap;
}

/* QUICK APPLY MODAL */
.modal-overlay{
    display:none;
    position:fixed;
    inset:0;
    background:rgba(9,14,19,.62);
    align-items:center;
    justify-content:center;
    z-index:2000;
    padding:20px;
}

.modal-overlay.open{
    display:flex;
}

.modal-box{
    background:#ffffff;
    width:100%;
    max-width:480px;
    max-height:90vh;
    overflow-y:auto;
    padding:40px;
    position:relative;
}

.modal-close{
    position:absolute;
    top:16px;
    right:16px;
    background:none;
    border:0;
    font-size:24px;
    line-height:1;
    color:#5B5548;
    cursor:pointer;
}

.modal-eyebrow{
    color:#B8863E;
    font-size:11px;
    font-weight:900;
    letter-spacing:2px;
    margin-bottom:10px;
}

.modal-box h3{
    font-size:22px;
    margin-bottom:6px;
    padding-right:20px;
    color:#1C1A16;
}

.modal-intro{
    color:#5B5548;
    font-size:13px;
    margin-bottom:24px;
}

.modal-label{
    display:block;
    font-size:11px;
    font-weight:800;
    text-transform:uppercase;
    letter-spacing:.5px;
    color:#5B5548;
    margin:16px 0 6px;
}

.modal-label:first-of-type{
    margin-top:0;
}

.modal-input{
    width:100%;
    border:1px solid #E2D9C4;
    padding:12px 13px;
    font-family:inherit;
    font-size:13px;
    color:#1C1A16;
    outline:none;
}

.modal-input:focus{
    border-color:#B8863E;
}

textarea.modal-input{
    resize:vertical;
}

.modal-consent{
    display:flex;
    align-items:flex-start;
    gap:8px;
    font-size:11px;
    color:#5B5548;
    margin:18px 0 22px;
}

.modal-consent input{
    margin-top:3px;
    flex-shrink:0;
}

.modal-submit{
    width:100%;
}

/* JOB DETAIL VIEW */
.job-detail{
    background:#ffffff;
    border:1px solid #E2D9C4;
    padding:40px;
}

.job-detail-top{
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    gap:20px;
    flex-wrap:wrap;
    border-bottom:1px solid #E2D9C4;
    padding-bottom:26px;
    margin-bottom:26px;
}

.job-detail-top h1{
    font-size:30px;
    letter-spacing:-.8px;
    color:#1C1A16;
    margin-bottom:8px;
}

.job-detail-company{
    font-size:14px;
    font-weight:700;
    color:#3A362E;
}

.job-detail-section{
    margin-top:26px;
}

.job-detail-section h3{
    font-size:15px;
    text-transform:uppercase;
    letter-spacing:.6px;
    margin-bottom:12px;
}

.job-detail-section p{
    color:#3A362E;
    font-size:14px;
}

.job-detail-section ul{
    padding-left:20px;
    color:#3A362E;
    font-size:14px;
    line-height:1.9;
}

.job-not-found{
    background:#ffffff;
    border:1px solid #E2D9C4;
    padding:55px 35px;
    text-align:center;
}

.job-not-found h3{
    font-size:21px;
    margin-bottom:12px;
}

.job-not-found p{
    color:#5B5548;
    font-size:14px;
    max-width:480px;
    margin:0 auto 22px;
}

.honey{
    position:absolute;
    left:-9999px;
    width:1px;
    height:1px;
    overflow:hidden;
}

/* MOBILE */
@media(max-width:900px){

    .search-grid{
        grid-template-columns:1fr;
    }

    .jobs-layout{
        grid-template-columns:1fr;
    }

    .filters{
        display:none;
    }

    .job-top{
        flex-direction:column;
    }

    .job-detail-top{
        flex-direction:column;
    }

    .employer-banner{
        flex-direction:column;
        align-items:flex-start;
    }
}
"""

body = """
<section class="page-hero">
<div class="container">
<div class="eyebrow eyebrow-light">SOUTHERN POINT JOBS</div>
<h1>Find Your Next Opportunity.</h1>
<p>Explore current employment opportunities curated by Southern Point. Search by position, location, employment type, and work arrangement.</p>
</div>
</section>

<div class="search-area">
<div class="container">
<div class="search-box">
<form onsubmit="return false;">
<div class="search-grid">

<input class="search-input" id="jobSearch" type="text" placeholder="Search jobs by title or keyword...">

<select class="search-select" id="locationFilter">
<option value="">All Locations</option>
<option value="Remote">Remote</option>
<option value="Houston">Houston</option>
<option value="Dallas">Dallas</option>
<option value="Austin">Austin</option>
<option value="Texas">Texas</option>
<option value="Nationwide">Nationwide</option>
</select>

<select class="search-select" id="typeFilter">
<option value="">All Employment Types</option>
<option value="Full-time">Full-time</option>
<option value="Part-time">Part-time</option>
<option value="Contract">Contract</option>
<option value="Internship">Internship</option>
</select>

<button class="search-button" type="button" onclick="applyFilters()">Search Jobs</button>

</div>
</form>
</div>
</div>
</div>

<section class="jobs-main">
<div class="container">

<!-- LIST VIEW -->
<div id="jobsListView">
<div class="jobs-layout">

<aside class="filters">
<h3>Filter Opportunities</h3>

<div class="filter-group">
<h4>Work Arrangement</h4>
<label class="filter-option"><input type="checkbox" class="filter-arrangement" value="Remote" onchange="applyFilters()"> Remote</label>
<label class="filter-option"><input type="checkbox" class="filter-arrangement" value="Hybrid" onchange="applyFilters()"> Hybrid</label>
<label class="filter-option"><input type="checkbox" class="filter-arrangement" value="On-site" onchange="applyFilters()"> On-site</label>
</div>

<div class="filter-group">
<h4>Categories</h4>
<label class="filter-option"><input type="checkbox" class="filter-category" value="Technology" onchange="applyFilters()"> Technology</label>
<label class="filter-option"><input type="checkbox" class="filter-category" value="Healthcare" onchange="applyFilters()"> Healthcare</label>
<label class="filter-option"><input type="checkbox" class="filter-category" value="Sales" onchange="applyFilters()"> Sales</label>
<label class="filter-option"><input type="checkbox" class="filter-category" value="Operations" onchange="applyFilters()"> Operations</label>
<label class="filter-option"><input type="checkbox" class="filter-category" value="Administrative" onchange="applyFilters()"> Administrative</label>
</div>

<div class="filter-group">
<h4>Opportunity Status</h4>
<label class="filter-option" title="Southern Point only ever lists currently active opportunities.">
<input type="checkbox" checked disabled> Currently Hiring
</label>
</div>
</aside>

<div>
<div class="jobs-header">
<div>
<h2>Latest Opportunities</h2>
<div class="jobs-count" id="jobCount">Loading opportunities&hellip;</div>
</div>
<select class="sort" id="sortSelect" onchange="applyFilters()">
<option value="newest">Newest</option>
<option value="relevance">Relevance</option>
</select>
</div>

<div class="featured">
<div class="featured-label">SOUTHERN POINT FEATURED</div>
<h3>New opportunities added regularly</h3>
<p>Our job listings are sourced from publicly available employer career information and other employment sources. Applicants are directed to the original application source.</p>
</div>

<div class="job-list" id="jobList"></div>

<div class="empty-state" id="emptyState">
<h3>New opportunities are added regularly</h3>
<p>There are no open positions posted at this exact moment, but Southern Point is actively working with clients on new roles. Leave your email and we'll let you know as soon as something opens up.</p>

<form class="notify-form" action="https://formsubmit.co/southernpoint.services@gmail.com" method="POST">
<input type="hidden" name="_subject" value="Job Alert Signup — Southern Point">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://southernpointllc.com/jobs.html?subscribed=1">
<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">
<input class="notify-input" type="email" name="email" required placeholder="you@example.com">
<button class="search-button" type="submit">Notify Me</button>
</form>
</div>

<div class="employer-banner">
<div>
<h2>Looking for qualified talent?</h2>
<p>Southern Point can help organizations identify and connect with qualified candidates.</p>
</div>
<a class="employer-button" href="/services/staffing-recruiting/">Work With Southern Point</a>
</div>

</div>
</div>
</div>

<!-- DETAIL VIEW (shown via ?job=<id>) -->
<div id="jobDetailView" style="display:none;">
<div class="breadcrumb on-light" style="margin-bottom:20px;">
<a href="/">Home</a><span>/</span><a href="/jobs.html">Find Jobs</a><span>/</span><span id="detailBreadcrumb">Job Details</span>
</div>
<div id="jobDetailContent"></div>
</div>

</div>
</section>

<!-- QUICK APPLY MODAL -->
<div class="modal-overlay" id="applyModal">
<div class="modal-box">
<button type="button" class="modal-close" onclick="closeApplyModal()" aria-label="Close">&times;</button>
<div class="modal-eyebrow">QUICK APPLY</div>
<h3 id="applyModalTitle"></h3>
<p class="modal-intro">Submit your information and Southern Point will follow up regarding next steps.</p>

<form id="applyForm" action="https://formsubmit.co/southernpoint.services@gmail.com" method="POST" enctype="multipart/form-data">
<input type="hidden" name="_subject" value="Quick Apply Submission — Southern Point">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://southernpointllc.com/jobs.html?applied=1">
<input type="hidden" name="Position Applied For" id="applyJobTitle" value="">
<input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off">

<label class="modal-label" for="applyName">Full Name</label>
<input class="modal-input" id="applyName" type="text" name="Name" required>

<label class="modal-label" for="applyEmail">Email</label>
<input class="modal-input" id="applyEmail" type="email" name="Email" required>

<label class="modal-label" for="applyPhone">Phone</label>
<input class="modal-input" id="applyPhone" type="tel" name="Phone">

<label class="modal-label" for="applyResume">Resume (PDF or Word)</label>
<input class="modal-input" id="applyResume" type="file" name="Resume" accept=".pdf,.doc,.docx" required>

<label class="modal-label" for="applyNote">Note (optional)</label>
<textarea class="modal-input" id="applyNote" name="Note" rows="3"></textarea>

<label class="modal-consent">
<input type="checkbox" required>
I consent to Southern Point contacting me regarding this and related opportunities.
</label>

<button type="submit" class="apply-btn modal-submit">Submit Application</button>
</form>
</div>
</div>
"""

SCRIPT = """
<script>

let ALL_JOBS = [];

async function loadJobs(){
    try{
        const res = await fetch("/data/jobs.json", { cache: "no-store" });
        if(!res.ok){ throw new Error("Failed to load job data (" + res.status + ")"); }
        const data = await res.json();
        ALL_JOBS = Array.isArray(data) ? data : [];
    }catch(err){
        console.error("Southern Point jobs: could not load data/jobs.json —", err);
        ALL_JOBS = [];
    }

    const jobId = new URLSearchParams(window.location.search).get("job");
    if(jobId){
        showJobDetail(jobId);
    }else{
        applyFilters();
    }
}

function escapeHTML(value){
    return String(value === undefined || value === null ? "" : value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function isFresh(dateStr){
    if(!dateStr) return false;
    const posted = new Date(dateStr);
    if(isNaN(posted.getTime())) return false;
    const days = (Date.now() - posted.getTime()) / (1000 * 60 * 60 * 24);
    return days >= 0 && days <= 7;
}

function relativeDate(dateStr){
    const posted = new Date(dateStr);
    if(!dateStr || isNaN(posted.getTime())){ return "Recently listed"; }
    const days = Math.floor((Date.now() - posted.getTime()) / (1000 * 60 * 60 * 24));
    if(days <= 0) return "Posted today";
    if(days === 1) return "Posted 1 day ago";
    if(days < 30) return "Posted " + days + " days ago";
    return "Posted " + posted.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
}

function matchesLocationFilter(job, filterValue){
    if(!filterValue) return true;
    const loc = (job.location || "").toLowerCase();
    const arrangement = (job.workArrangement || "").toLowerCase();
    const value = filterValue.toLowerCase();
    if(value === "remote"){ return arrangement === "remote" || loc.includes("remote"); }
    if(value === "nationwide"){ return loc.includes("nationwide") || arrangement === "remote"; }
    if(value === "texas"){
        return loc.includes("tx") || loc.includes("texas") ||
            ["houston", "dallas", "austin"].some(function(city){ return loc.includes(city); });
    }
    return loc.includes(value);
}

function jobCardHTML(job){
    const fresh = isFresh(job.postedDate);
    const tagClass = fresh ? "job-tag fresh" : "job-tag";
    const tagLabel = fresh ? "Fresh" : (job.employmentType || "");
    const companyLabel = job.companyLabel || job.category || "";

    const applyControl = job.applyType === "external"
        ? '<a class="apply-btn" href="' + escapeHTML(job.applyUrl || "#") + '" target="_blank" rel="noopener noreferrer">Apply on Company Site</a>'
        : '<button type="button" class="apply-btn" data-apply-id="' + escapeHTML(job.id) + '">Apply Now</button>';

    return (
        '<article class="job-card" ' +
            'data-title="' + escapeHTML(job.title) + '" ' +
            'data-location="' + escapeHTML(job.location) + '" ' +
            'data-type="' + escapeHTML(job.employmentType) + '" ' +
            'data-arrangement="' + escapeHTML(job.workArrangement) + '" ' +
            'data-category="' + escapeHTML(job.category) + '">' +

            '<div class="job-top">' +
                '<div>' +
                    '<div class="job-title"><a href="/jobs.html?job=' + encodeURIComponent(job.id) + '">' + escapeHTML(job.title) + '</a></div>' +
                    '<div class="job-company">' + escapeHTML(companyLabel) + '</div>' +
                '</div>' +
                '<span class="' + tagClass + '">' + escapeHTML(tagLabel) + '</span>' +
            '</div>' +

            '<div class="job-meta">' +
                '<span>' + escapeHTML(job.location) + '</span>' +
                '<span>' + escapeHTML(job.employmentType) + '</span>' +
                '<span>' + escapeHTML(job.workArrangement) + '</span>' +
            '</div>' +

            '<p class="job-description">' + escapeHTML(job.description) + '</p>' +

            '<div class="job-bottom">' +
                '<span class="job-posted">' + relativeDate(job.postedDate) + '</span>' +
                '<div class="job-actions">' +
                    '<a class="detail-link" href="/jobs.html?job=' + encodeURIComponent(job.id) + '">View Details</a>' +
                    applyControl +
                '</div>' +
            '</div>' +

        '</article>'
    );
}

function renderJobs(jobs){
    const list = document.getElementById("jobList");
    const empty = document.getElementById("emptyState");
    const count = document.getElementById("jobCount");
    const activeJobs = ALL_JOBS.filter(function(job){ return job && job.status === "active"; });

    if(!jobs.length){
        list.innerHTML = "";
        empty.style.display = "block";
        count.textContent = activeJobs.length
            ? "Showing 0 opportunities — try broadening your search"
            : "No open positions posted right now";
        return;
    }

    empty.style.display = "none";
    list.innerHTML = jobs.map(jobCardHTML).join("");
    count.textContent = "Showing " + jobs.length + " opportunit" + (jobs.length === 1 ? "y" : "ies");
}

function applyFilters(){
    const search = document.getElementById("jobSearch").value.toLowerCase().trim();
    const location = document.getElementById("locationFilter").value;
    const type = document.getElementById("typeFilter").value.toLowerCase();
    const sort = document.getElementById("sortSelect").value;

    const arrangements = Array.from(document.querySelectorAll(".filter-arrangement:checked"))
        .map(function(box){ return box.value.toLowerCase(); });
    const categories = Array.from(document.querySelectorAll(".filter-category:checked"))
        .map(function(box){ return box.value.toLowerCase(); });

    const activeJobs = ALL_JOBS.filter(function(job){ return job && job.status === "active"; });

    let filtered = activeJobs.filter(function(job){
        const title = (job.title || "").toLowerCase();
        const description = (job.description || "").toLowerCase();
        const jobType = (job.employmentType || "").toLowerCase();
        const jobArrangement = (job.workArrangement || "").toLowerCase();
        const jobCategory = (job.category || "").toLowerCase();

        const matchesSearch = !search || title.includes(search) || description.includes(search);
        const matchesLocation = matchesLocationFilter(job, location);
        const matchesType = !type || jobType === type;
        const matchesArrangement = !arrangements.length || arrangements.includes(jobArrangement);
        const matchesCategory = !categories.length || categories.includes(jobCategory);

        return matchesSearch && matchesLocation && matchesType && matchesArrangement && matchesCategory;
    });

    if(sort === "newest"){
        filtered = filtered.slice().sort(function(a, b){
            return new Date(b.postedDate || 0) - new Date(a.postedDate || 0);
        });
    }

    renderJobs(filtered);
}

function openApplyModal(job){
    document.getElementById("applyModalTitle").textContent = job.title || "";
    document.getElementById("applyJobTitle").value = job.title || "";
    document.getElementById("applyModal").classList.add("open");
    document.body.style.overflow = "hidden";
}

function closeApplyModal(){
    document.getElementById("applyModal").classList.remove("open");
    document.body.style.overflow = "";
}

/* ===== JOB DETAIL VIEW ===== */

function listHTML(items){
    if(!items || !items.length) return "";
    return "<ul>" + items.map(function(item){ return "<li>" + escapeHTML(item) + "</li>"; }).join("") + "</ul>";
}

function jobDetailHTML(job){
    const companyLabel = job.companyLabel || job.category || "";
    const applyControl = job.applyType === "external"
        ? '<a class="apply-btn" href="' + escapeHTML(job.applyUrl || "#") + '" target="_blank" rel="noopener noreferrer">Apply on Company Site</a>'
        : '<button type="button" class="apply-btn" data-apply-id="' + escapeHTML(job.id) + '">Apply Now</button>';

    let sections = "";

    if(job.responsibilities && job.responsibilities.length){
        sections += '<div class="job-detail-section"><h3>Responsibilities</h3>' + listHTML(job.responsibilities) + '</div>';
    }
    if(job.requirements && job.requirements.length){
        sections += '<div class="job-detail-section"><h3>Requirements</h3>' + listHTML(job.requirements) + '</div>';
    }
    if(job.benefits && job.benefits.length){
        sections += '<div class="job-detail-section"><h3>Benefits</h3>' + listHTML(job.benefits) + '</div>';
    }

    return (
        '<div class="job-detail">' +
            '<div class="job-detail-top">' +
                '<div>' +
                    '<h1>' + escapeHTML(job.title) + '</h1>' +
                    '<div class="job-detail-company">' + escapeHTML(companyLabel) + '</div>' +
                    '<div class="job-meta" style="margin-top:14px;">' +
                        '<span>' + escapeHTML(job.location) + '</span>' +
                        '<span>' + escapeHTML(job.employmentType) + '</span>' +
                        '<span>' + escapeHTML(job.workArrangement) + '</span>' +
                    '</div>' +
                '</div>' +
                applyControl +
            '</div>' +
            '<div class="job-detail-section"><h3>About This Role</h3><p>' + escapeHTML(job.description) + '</p></div>' +
            sections +
            '<div class="job-detail-section"><span class="job-posted">' + relativeDate(job.postedDate) + '</span></div>' +
        '</div>'
    );
}

function jobNotFoundHTML(){
    return (
        '<div class="job-not-found">' +
            '<h3>This position is no longer available</h3>' +
            '<p>The role you\\'re looking for may have been filled or is no longer posted. Browse current openings below instead.</p>' +
            '<a class="btn btn-red" href="/jobs.html">View All Jobs</a>' +
        '</div>'
    );
}

function showJobDetail(jobId){
    const job = ALL_JOBS.find(function(j){ return j && j.id === jobId && j.status === "active"; });

    document.getElementById("jobsListView").style.display = "none";
    const detailView = document.getElementById("jobDetailView");
    detailView.style.display = "block";

    if(job){
        document.getElementById("detailBreadcrumb").textContent = job.title;
        document.title = job.title + " | Southern Point Jobs";
        document.getElementById("jobDetailContent").innerHTML = jobDetailHTML(job);
    }else{
        document.getElementById("detailBreadcrumb").textContent = "Job Not Found";
        document.getElementById("jobDetailContent").innerHTML = jobNotFoundHTML();
    }
}

function showConfirmationBanner(){
    const params = new URLSearchParams(window.location.search);
    let message = "";

    if(params.get("applied") === "1"){
        message = "Thanks — your application was submitted. Southern Point will follow up if there's a fit.";
    }else if(params.get("subscribed") === "1"){
        message = "You're on the list — we'll email you when new opportunities open up.";
    }

    if(!message) return;

    const banner = document.createElement("div");
    banner.className = "confirm-banner";
    banner.textContent = message;
    document.getElementById("bannerSlot").appendChild(banner);
}

document.getElementById("jobSearch").addEventListener("input", applyFilters);
document.getElementById("locationFilter").addEventListener("change", applyFilters);
document.getElementById("typeFilter").addEventListener("change", applyFilters);

document.addEventListener("click", function(event){
    const button = event.target.closest("[data-apply-id]");
    if(!button) return;
    const job = ALL_JOBS.find(function(j){ return j.id === button.dataset.applyId; });
    if(job) openApplyModal(job);
});

document.getElementById("applyModal").addEventListener("click", function(event){
    if(event.target === this) closeApplyModal();
});

document.addEventListener("keydown", function(event){
    if(event.key === "Escape") closeApplyModal();
});

document.addEventListener("DOMContentLoaded", function(){
    showConfirmationBanner();
    loadJobs();
});

</script>
"""

html = build(
    title="Find Jobs | Southern Point Staffing",
    description="Search current employment opportunities through Southern Point. Explore jobs by keyword, location, category, employment type, and work arrangement.",
    extra_style=STYLE,
    body_html=body + SCRIPT,
    section="job-seekers",
    canonical="https://southernpointllc.com/jobs.html",
)

with open(f"{BASE}/jobs.html", "w") as f:
    f.write(html)

print("wrote jobs.html")
