/* =====================================================================
   SOUTHERN POINT — SHARED SITE BEHAVIOR
   Mobile nav toggle, FAQ accordions, and the confirmation-banner
   helper used by every form on the site (Request Talent, Contact,
   Submit Resume, Quick Apply, Job Alerts). Loaded on every page.
===================================================================== */

document.addEventListener("DOMContentLoaded", function(){

    /* ---------- Mobile nav toggle ---------- */

    var toggle = document.querySelector(".nav-toggle");

    if(toggle){

        toggle.addEventListener("click", function(){
            document.body.classList.toggle("nav-open");
        });

        document.querySelectorAll(".mobile-nav a").forEach(function(link){
            link.addEventListener("click", function(){
                document.body.classList.remove("nav-open");
            });
        });

    }

    /* ---------- FAQ accordions ---------- */

    document.querySelectorAll(".faq-item").forEach(function(item){

        var question = item.querySelector(".faq-question");
        var answer = item.querySelector(".faq-answer");

        if(!question || !answer) return;

        question.addEventListener("click", function(){

            var isOpen = item.classList.contains("open");

            item.parentElement.querySelectorAll(".faq-item.open").forEach(function(open){
                if(open !== item){
                    open.classList.remove("open");
                    open.querySelector(".faq-answer").style.maxHeight = null;
                }
            });

            if(isOpen){
                item.classList.remove("open");
                answer.style.maxHeight = null;
            }else{
                item.classList.add("open");
                answer.style.maxHeight = answer.scrollHeight + "px";
            }

        });

    });

    /* ---------- Confirmation banner from ?submitted=1 style params ---------- */

    var params = new URLSearchParams(window.location.search);
    var bannerSlot = document.getElementById("bannerSlot");
    var message = "";

    if(bannerSlot){

        if(params.get("applied") === "1"){
            message = "Thanks — your application was submitted. Southern Point will follow up if there's a fit.";
        }else if(params.get("subscribed") === "1"){
            message = "You're on the list — we'll email you when new opportunities open up.";
        }else if(params.get("submitted") === "1"){
            message = "Thanks — your request was submitted. Southern Point will be in touch shortly.";
        }else if(params.get("resume") === "1"){
            message = "Thanks — your resume was received. Southern Point may reach out if there's a potential fit.";
        }else if(params.get("contacted") === "1"){
            message = "Thanks — your message was sent. Southern Point will respond soon.";
        }

        if(message){
            var banner = document.createElement("div");
            banner.className = "confirm-banner";
            banner.textContent = message;
            bannerSlot.appendChild(banner);
        }

    }

});
