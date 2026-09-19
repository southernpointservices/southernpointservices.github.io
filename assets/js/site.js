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
            var isOpen = document.body.classList.toggle("nav-open");
            toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
        });

        document.querySelectorAll(".mobile-nav a").forEach(function(link){
            link.addEventListener("click", function(){
                document.body.classList.remove("nav-open");
                toggle.setAttribute("aria-expanded", "false");
            });
        });

    }

    /* ---------- Header scroll state ----------
       The header is transparent over every page's dark opening hero
       (header + hero read as one composition) and gains a solid fill
       + hairline border once the page scrolls past it. Threshold is
       intentionally small — this only needs to catch "no longer at
       the very top", not track scroll position precisely. */

    var SCROLL_THRESHOLD = 40;

    function updateScrolledState(){
        var scrolled = (window.scrollY || document.documentElement.scrollTop) > SCROLL_THRESHOLD;
        document.body.classList.toggle("scrolled", scrolled);
    }

    updateScrolledState();
    window.addEventListener("scroll", updateScrolledState, { passive: true });

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

    /* ---------- Scroll-reveal animation ----------
       Applies a subtle fade/slide-in to shared component blocks as they
       enter the viewport. Works site-wide off shared CSS classes rather
       than requiring every page to opt in individually. Elements sharing
       a parent (a card grid, a step row) get a small staggered delay so
       they settle in sequence rather than all at once. Fully inert when
       prefers-reduced-motion is set, or if IntersectionObserver isn't
       available — content just renders in its final state. */

    var revealSelectors = [
        ".card",
        ".leader-card",
        ".word-item",
        ".photo-frame",
        ".editorial-row",
        ".statement-xl",
        ".process-grid .step",
        ".stat-big"
    ].join(",");

    var revealEls = Array.prototype.slice.call(document.querySelectorAll(revealSelectors));
    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if(revealEls.length){

        revealEls.forEach(function(el){
            el.classList.add("reveal");
        });

        if(!reduceMotion){

            // Stagger elements that share a parent (grid/row groupings).
            var revealParents = [];
            revealEls.forEach(function(el){
                var parent = el.parentElement;
                if(parent && revealParents.indexOf(parent) === -1){
                    revealParents.push(parent);
                }
            });

            revealParents.forEach(function(parent){
                var siblings = revealEls.filter(function(el){
                    return el.parentElement === parent;
                });
                siblings.forEach(function(el, i){
                    el.style.transitionDelay = (Math.min(i, 5) * 70) + "ms";
                });
            });

        }

        if(reduceMotion || !("IntersectionObserver" in window)){

            revealEls.forEach(function(el){
                el.classList.add("reveal-in");
            });

        }else{

            var revealObserver = new IntersectionObserver(function(entries, observer){
                entries.forEach(function(entry){
                    if(entry.isIntersecting){
                        entry.target.classList.add("reveal-in");
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.12, rootMargin: "0px 0px -60px 0px" });

            revealEls.forEach(function(el){
                revealObserver.observe(el);
            });

            // Safety net: some renderers (headless full-page screenshot
            // tools, certain crawlers, a page opened mid-scroll) never
            // fire a real scroll event, so an element that's technically
            // "below the fold" can end up permanently stuck at opacity:0.
            // Force everything visible shortly after load regardless —
            // real visitors scroll well within this window, so it never
            // shows in normal use, it just guarantees content can't stay
            // invisible.
            window.setTimeout(function(){
                revealEls.forEach(function(el){
                    el.classList.add("reveal-in");
                });
                revealObserver.disconnect();
            }, 900);

        }

    }

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
