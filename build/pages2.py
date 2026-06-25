# -*- coding: utf-8 -*-
from build import *
from pages import BLOG_POSTS, build_index

def page_hero(title, sub, img, crumbs, depth=0):
    pre = "../"*depth
    return f"""
<section class="pagehero">
  <div class="pageimg"><img src="{pre}assets/img/{img}.jpg" alt=""></div>
  <div class="wrap">
    <div class="crumbs"><a href="{pre}index.html">Home</a> &nbsp;/&nbsp; {crumbs}</div>
    <h1 class="display" style="color:#fff;max-width:18ch">{title}</h1>
    <p class="lead" style="color:var(--cool);max-width:52ch;margin-top:1rem">{sub}</p>
  </div>
</section>"""

def mini_cta(depth=0):
    pre="../"*depth
    return f"""
<section class="cta sec" id="cta-form">
  <div class="cta-bg"><img src="{pre}assets/img/p088.jpg" alt=""></div>
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow on-dark">Ready to start?</span>
      <h2 class="h-xl" style="color:#fff">Free in-home quote,<br>fixed in writing.</h2>
      <p class="lead" style="color:var(--cool);max-width:42ch">Tell us about your project and we will measure, match the slab and price it — usually the same week.</p>
    </div>
    <div class="reveal">{lead_form(ident='cta-'+str(depth))}</div>
  </div>
</section>"""

# ---------------------------------------------------------------- ABOUT
def build_about():
    WHY = [("Own workshop, own crews","Templating, fabrication and installation all in-house — never sub-contracted."),
           ("Fixed written pricing","Your quote is the price. No surprise charges for edges, cut-outs or removal."),
           ("15 years of stone","Granite, quartz, marble and quartzite — thousands of metres fitted across the metro."),
           ("One point of contact","One person owns your project from first slab to final seal.")]
    items="".join(f'<div class="why-item"><div class="ic" style="color:var(--gold-deep);border-color:var(--line)">✓</div><div><b style="color:var(--ink)">{t}</b><p style="color:var(--stone)">{d}</p></div></div>' for t,d in WHY)
    body = page_hero("The workshop behind your worktop","Owner-led stone fabrication and installation, built on slabs we are proud to put our name on.","p109","About") + f"""
<section class="sec"><div class="wrap about-grid">
  <div class="reveal"><span class="eyebrow">Our story</span>
    <h2 class="h-xl">Stone is all we do —<br>and we do all of it.</h2>
    <div class="rule short"><span class="dot"></span></div>
    <p class="lead">{CO} began in a single workshop unit with one belief: that a countertop is only as good as the people who template, cut and fit it. Fifteen years on, that has not changed. We still select every slab with the homeowner, still template with a laser, and still send our own crews to install.</p>
    <p class="muted">No sales floor middlemen. No anonymous sub-contractors arriving in an unmarked van. Just one accountable team, one warranty, and a finish we sign our name to — across kitchens, islands, vanities and outdoor bars in the {CITY}.</p>
    <a href="contact.html" class="btn btn-gold" style="margin-top:1rem">Book a free measure <span class="arr">→</span></a>
  </div>
  <div class="about-media reveal"><img src="assets/img/p049.jpg" alt="GraniteFactory kitchen"><div class="badge"><span class="n">{REVIEWS}</span><small>Kitchens fitted</small></div></div>
</div></section>
<section class="sec bg-paper"><div class="wrap">
  <div class="sec-head center reveal" style="text-align:center"><span class="eyebrow">What we stand for</span><h2 class="h-xl">No middlemen. No surprises.</h2></div>
  <div class="why-list reveal" style="grid-template-columns:1fr 1fr;max-width:900px;margin:3rem auto 0">{items}</div>
</div></section>
""" + mini_cta()
    write("about.html", head(f"About | {CO}", "Owner-led granite and stone countertop fabrication and installation. 15 years, one accountable team.","about")+nav("about")+body+footer())

# ---------------------------------------------------------------- SERVICES HUB
def build_services():
    cards="".join(f"""<a class="svc-card reveal" href="services/{s}.html" style="min-height:360px">
      <span class="num">{i:02d}</span><img src="assets/img/{img}.jpg" alt="{t}">
      <div class="body"><h3>{t}</h3><p>{d}</p><span class="go">Explore <span>→</span></span></div></a>""" for i,(s,t,d,img) in enumerate(SERVICES,1))
    body = page_hero("Stone surfaces, one accountable team","From kitchen worktops to outdoor bars — every surface fabricated and fitted under one roof.","p004","Services") + f"""
<div class="marquee"><div class="marquee-track">{''.join(f'<span>{t}</span>' for _,t,_,_ in SERVICES)*2}</div></div>
<section class="sec"><div class="wrap">
  <div class="sec-head center reveal" style="text-align:center"><span class="eyebrow">What we do</span><h2 class="h-xl">Seven services, one warranty</h2>
    <p class="lead" style="margin-inline:auto">Choose a surface to see how we template, fabricate and install it — and what makes the finish ours.</p></div>
  <div class="svc-grid" style="margin-top:3rem">{cards}</div>
</div></section>""" + mini_cta()
    write("services.html", head(f"Services | {CO}","Granite, quartz, marble and quartzite countertops, islands, vanities and outdoor kitchens — fabricated and installed.","services")+nav("services")+body+footer())

# ---------------------------------------------------------------- SERVICE DETAIL
SVC_LONG = {
 "kitchen-granite-countertops": ("Granite Kitchen Countertops",
    "The worktop is the hardest-working surface in your home — and the one everyone sees. We fabricate and fit natural granite that shrugs off heat, knives and daily life while anchoring the whole room.",
    ["Hand-select your slab — we mark the cut so the best veining lands where it matters","Laser template for invisible seams and millimetre-perfect cut-outs","Your choice of edge profile, from crisp pencil-round to bold mitre","Sealed on install with a simple lifetime care routine"]),
 "quartz-engineered-stone": ("Quartz &amp; Engineered Stone",
    "Engineered quartz gives you near-total consistency, a non-porous surface and almost no maintenance — ideal for busy family kitchens that still want a flawless finish.",
    ["Caesarstone, Silestone &amp; premium engineered quartz","Non-porous — no sealing, highly stain resistant","Consistent colour and pattern across every piece","Seamless joins and integrated drainer grooves available"]),
 "bathroom-vanity-tops": ("Bathroom Vanity Tops",
    "Carry the language of your kitchen through the home with coordinated stone vanities, surrounds and shelving — cut from the same slabs for a considered, whole-home finish.",
    ["Undermount or vessel basin cut-outs, precisely templated","Matching splashbacks, window sills and niche shelves","Granite, quartz, marble and quartzite options","Compact and floating-vanity friendly"]),
 "waterfall-islands": ("Waterfall Islands &amp; Edges",
    "A mitred waterfall island turns a slab into sculpture. We plan the vein-match around the corner so the stone appears to pour from the top to the floor in one continuous run.",
    ["45° mitred corners with vein-matched continuity","Statement edge profiles and book-matched fronts","Integrated seating overhangs and supports","Works with granite, quartz, marble and quartzite"]),
 "outdoor-kitchens": ("Outdoor Kitchens &amp; BBQ Tops",
    "Outdoor surfaces face sun, rain and serious heat. We specify and fit stone engineered to stay beautiful outside — for braais, bars, pizza ovens and alfresco prep.",
    ["UV-stable, freeze-thaw and heat-tolerant stone","Cut-outs for built-in grills, burners and sinks","Drip edges and overhangs detailed for the weather","Sealed and finished for low-maintenance outdoor life"]),
 "stone-fabrication": ("Custom Fabrication &amp; Edges",
    "Our own workshop is where the craft happens. CNC cutting and hand finishing let us deliver seamless joins, precise cut-outs and edge profiles other fabricators sub out.",
    ["In-house CNC and hand fabrication — never sub-contracted","Full range of edge profiles, from minimal to ornate","Drainer grooves, hot rods, and tap &amp; soap cut-outs","Trade fabrication for designers and builders"]),
 "templating-installation": ("Templating &amp; Installation",
    "Precision starts before we cut. We laser-template your cabinetry for a digital model, then our own crews install — dust-controlled, on-schedule, and spotless on hand-over.",
    ["Laser templating for a precise digital model","Our own installation crews — we never sub out the fit","Vacuum-assisted, dust-controlled on-site work","Usually fitted, sealed and cleaned within a single day"]),
}
def build_service_pages():
    imgmap = {s:img for s,_,_,img in SERVICES}
    for i,(s,t,d,img) in enumerate(SERVICES):
        title, intro, bullets = SVC_LONG[s]
        bl="".join(f"<li>{b}</li>" for b in bullets)
        # related
        rel=[x for x in SERVICES if x[0]!=s][:3]
        relc="".join(f'<a class="post-card reveal" href="{rs}.html"><div class="media"><img src="../assets/img/{ri}.jpg" alt="{rt}"></div><div class="body"><h3 style="font-size:1.05rem">{rt}</h3><span class="go txtlink">View service →</span></div></a>' for rs,rt,rd,ri in rel)
        body = page_hero(title, d, img, f'<a href="../services.html">Services</a> / {title}', depth=1) + f"""
<section class="sec"><div class="wrap about-grid">
  <div class="reveal"><span class="eyebrow">{title}</span><h2 class="h-xl">{intro[:48]}…</h2>
    <div class="rule short"><span class="dot"></span></div>
    <p class="lead">{intro}</p>
    <ul class="hero-trust" style="margin-top:1.4rem">{''.join(f'<li><span class="ck" style="color:var(--gold-deep)">✓</span> {b}</li>' for b in bullets)}</ul>
    <a href="../contact.html" class="btn btn-gold" style="margin-top:1.6rem">Get a free quote <span class="arr">→</span></a>
  </div>
  <div class="about-media reveal"><img src="../assets/img/{img}.jpg" alt="{title}"></div>
</div></section>
<section class="sec bg-paper"><div class="wrap">
  <div class="rev-top reveal"><div><span class="eyebrow">Related</span><h2 class="h-lg">Other surfaces we fabricate</h2></div><a href="../services.html" class="txtlink">All services →</a></div>
  <div class="blog-grid" style="margin-top:2rem">{relc}</div>
</div></section>""" + mini_cta(depth=1)
        write(f"services/{s}.html", head(f"{title} | {CO}", d.replace('&amp;','and'), "services", depth=1)+nav("services",depth=1)+body+footer(depth=1))

# ---------------------------------------------------------------- GALLERY
GAL_ALL = ["p004","p011","p013","p020","p021","p022","p023","p024","p029","p033",
           "p036","p039","p049","p055","p065","p070","p096","p100","p109","p118","p119","p123","p030","p094"]
def build_gallery():
    items="".join(f'<div class="gal-item reveal" data-lb="assets/img/{im}.jpg"><img src="assets/img/{im}.jpg" alt="Project {n+1}"><span class="tag">Project · {im}</span></div>' for n,im in enumerate(GAL_ALL))
    body = page_hero("Stone we have fitted","A sample of recent kitchens, islands, vanities and outdoor surfaces across the metro. Click any image to enlarge.","p022","Gallery") + f"""
<section class="sec"><div class="wrap">
  <div class="gal-grid" style="grid-auto-rows:230px">{items}</div>
</div></section>""" + mini_cta()
    write("gallery.html", head(f"Gallery | {CO}","Recent granite, quartz and marble installations across the metro.","gallery")+nav("gallery")+body+footer())

# ---------------------------------------------------------------- FINANCING
def build_financing():
    FAQF=[("Is the in-home measure really free?","Yes — every measure and quote is free, in your home, and with no obligation. We bring physical samples and leave you a fixed written price."),
          ("How does the finance application work?","We pass you to our third-party lending partner for a quick, soft-check decision. There is no cost to apply and no early-settlement penalty."),
          ("Can I finance more than the kitchen?","Absolutely. Vanities, laundries, outdoor bars and splashbacks can all be bundled into one quote and one finance plan."),]
    faqs="".join(f'<div class="faq-item reveal"><button class="faq-q">{q}<span class="pm">+</span></button><div class="faq-a"><p>{a}</p></div></div>' for q,a in FAQF)
    body = page_hero("Free measures, fair finance","An honest fixed price up front, and flexible ways to spread the cost when you are ready to proceed.","p100","Financing") + f"""
<section class="sec bg-ink"><div class="wrap">
  <div class="offer-grid">
    <div class="offer-card reveal"><div class="ic">◇</div><h3>0% &amp; low-rate finance</h3><p>Spread your investment over 12–60 months through our lending partners. Soft-check decisions, no early-settlement penalties, and the rate is applied before your written quote.</p></div>
    <div class="offer-card reveal"><div class="ic">✦</div><h3>Trade, military &amp; multi-room</h3><p>Designers, builders and repeat clients get preferred pricing, and every additional room quoted alongside your kitchen is discounted. Mention it before the quote and we build it in.</p></div>
  </div>
  <p class="muted" style="color:var(--cool);margin-top:2rem">No obligation. No pressure. Honest answers, every visit.</p>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head center reveal" style="text-align:center"><span class="eyebrow">Good to know</span><h2 class="h-xl">Financing questions</h2></div>
  <div class="faq-wrap">{faqs}</div>
</div></section>""" + mini_cta()
    write("financing.html", head(f"Financing | {CO}","Free in-home quotes and flexible 0% and low-rate finance on granite and quartz countertops.","financing")+nav("financing")+body+footer())

# ---------------------------------------------------------------- BLOG INDEX
def build_blog():
    feat=BLOG_POSTS[0]; rest=BLOG_POSTS[1:]
    cards="".join(f'<a class="post-card reveal" href="blog/{p["slug"]}.html"><div class="media"><img src="assets/img/{p["img"]}.jpg" alt="{p["title"]}"></div><div class="body"><span class="meta">{p["date"]} · {p["cat"]}</span><h3>{p["title"]}</h3><p>{p["excerpt"]}</p><span class="go txtlink">Read more →</span></div></a>' for p in rest)
    body = page_hero("The Journal","Plain-spoken guidance on stone — from people who template, cut and fit it every week.","p052","Journal") + f"""
<section class="sec"><div class="wrap">
  <a class="blog-feature reveal" href="blog/{feat['slug']}.html"><div class="media"><img src="assets/img/{feat['img']}.jpg" alt="{feat['title']}"></div>
    <div class="body"><span class="meta">{feat['date']} · {feat['cat']}</span><h2 class="h-lg" style="margin:.4rem 0 .6rem">{feat['title']}</h2><p class="muted">{feat['excerpt']}</p><p style="margin-top:1rem"><span class="txtlink">Read the article →</span></p></div></a>
  <div class="blog-grid" style="margin-top:1.3rem">{cards}</div>
</div></section>""" + mini_cta()
    write("blog.html", head(f"Journal | {CO}","Granite and quartz buying guides, care tips and design ideas.","blog")+nav("blog")+body+footer())

# ---------------------------------------------------------------- BLOG POSTS
POST_BODY = {
 "granite-vs-quartz-which-countertop": """
<p>It is the first question almost every client asks: granite or quartz? Both are excellent. The right answer depends less on which is "better" and more on how you cook, clean and live.</p>
<h2>Granite — natural, characterful, heat-proof</h2>
<p>Granite is quarried natural stone. Every slab is unique, which is the whole appeal — you are choosing a one-of-a-kind surface, not a print. It laughs at hot pans and is extremely hard-wearing. Because it is natural, it is sealed on installation and benefits from a quick re-seal every year or two.</p>
<blockquote>Choose granite if you want genuine natural stone and a worktop you can put a hot pot straight onto.</blockquote>
<h2>Quartz — engineered, consistent, low-maintenance</h2>
<p>Engineered quartz mixes natural quartz with resins and pigments. The result is non-porous (no sealing), highly stain resistant, and beautifully consistent slab to slab — ideal if you want a precise, uniform look or a colour nature does not offer.</p>
<ul><li><b>Heat:</b> Granite wins — quartz can scorch, so use a trivet.</li><li><b>Maintenance:</b> Quartz wins — no sealing, ever.</li><li><b>Uniqueness:</b> Granite wins — no two slabs alike.</li><li><b>Consistency:</b> Quartz wins — perfect repeatability.</li></ul>
<h2>So which should you pick?</h2>
<p>We bring physical samples of both to your home and lay them against your cabinetry and light. Nine times out of ten the decision makes itself the moment the right slab is on the counter.</p>""",
 "how-stone-countertops-are-fabricated": """
<p>Between choosing your slab and the day it lands in your kitchen, a lot of precise work happens. Here is the journey, start to finish.</p>
<h2>1 · Templating</h2>
<p>Once your cabinets are fitted, we laser-template the room. This builds a millimetre-accurate digital model — every wall that is not quite square, every overhang, every cut-out for a sink, hob or tap.</p>
<h2>2 · Slab layout &amp; cutting</h2>
<p>We lay the template over a digital photo of your actual slab so you can see exactly where the veining will fall — then CNC machines cut the pieces. Planning seams here is what makes them disappear later.</p>
<h2>3 · Edging &amp; polishing</h2>
<p>The cut edges are profiled to your chosen style and polished to a consistent sheen. This is slow, skilled work, and it is the difference between a worktop that feels bespoke and one that feels cut-price.</p>
<h2>4 · Install &amp; seal</h2>
<p>Our crew dry-fits, bonds and seams the stone on site, seals natural stone, and cleans up completely. Most kitchens are done in a day.</p>""",
 "caring-for-granite-countertops": """
<p>Good news: a stone worktop is one of the lowest-maintenance surfaces in your home. Here is everything you actually need to do.</p>
<h2>The daily two minutes</h2>
<p>Warm water, a drop of pH-neutral soap, a soft cloth. That is it. Skip anything acidic (vinegar, lemon, harsh de-scalers) — over time acids dull natural stone.</p>
<h2>Sealing — the myth and the reality</h2>
<p>Quartz never needs sealing. Granite and quartzite are sealed on installation; a simple water-drop test tells you when a refresh is due — if water beads, you are fine; if it darkens the stone, it is time for a re-seal (a 15-minute job).</p>
<ul><li>Wipe spills promptly — especially wine, oil and citrus on natural stone.</li><li>Use a board for chopping; stone will blunt your knives, not the other way round.</li><li>Use a trivet under very hot pans on quartz.</li></ul>
<blockquote>Done weekly, this routine keeps a worktop looking exactly like the day it was installed — for decades.</blockquote>""",
 "waterfall-island-worth-it": """
<p>The waterfall island — where the stone runs over the edge and down to the floor — is the signature move of the modern kitchen. Is it worth the extra cost? Usually, but not always.</p>
<h2>What makes it special</h2>
<p>A mitred waterfall joins two slabs at a 45° angle so the veining appears to pour around the corner in one continuous run. Done well, it turns a worktop into a sculpture.</p>
<h2>What it costs</h2>
<p>You are buying more stone and far more fabrication time — the mitre and vein-match are skilled work. Budget for roughly one and a half to two times a standard island top.</p>
<h2>When to do it — and when not to</h2>
<ul><li><b>Do it</b> if the island is a focal point and you have chosen a slab with beautiful movement.</li><li><b>Maybe skip it</b> on a very plain stone, where the drama is lost, or where a power point in the end panel forces an awkward break.</li></ul>
<p>We will tell you honestly whether your slab and layout will reward the investment.</p>""",
}
def build_posts():
    for idx,p in enumerate(BLOG_POSTS):
        body_html = POST_BODY[p["slug"]]
        rel=[x for x in BLOG_POSTS if x["slug"]!=p["slug"]][:3]
        relc="".join(f'<a class="post-card reveal" href="{r["slug"]}.html"><div class="media"><img src="../assets/img/{r["img"]}.jpg" alt="{r["title"]}"></div><div class="body"><span class="meta">{r["cat"]}</span><h3 style="font-size:1.02rem">{r["title"]}</h3><span class="go txtlink">Read →</span></div></a>' for r in rel)
        page = head(f"{p['title']} | {CO}", p["excerpt"], "blog", depth=1) + nav("blog",depth=1) + f"""
<section class="pagehero"><div class="pageimg"><img src="../assets/img/{p['img']}.jpg" alt=""></div>
  <div class="wrap"><div class="crumbs"><a href="../index.html">Home</a> / <a href="../blog.html">Journal</a> / {p['cat']}</div>
  <h1 class="h-xl" style="color:#fff;max-width:22ch">{p['title']}</h1>
  <p class="lead" style="color:var(--cool);margin-top:.8rem">{p['date']} · {p['cat']}</p></div></section>
<section class="sec"><div class="wrap"><div class="article reveal">{body_html}
  <div class="rule"><span class="dot"></span></div>
  <p><a href="../contact.html" class="txtlink">Get a free quote for your project →</a></p>
</div></div></section>
<section class="sec bg-paper"><div class="wrap"><div class="rev-top reveal"><div><span class="eyebrow">Keep reading</span><h2 class="h-lg">More from the journal</h2></div><a href="../blog.html" class="txtlink">All articles →</a></div>
  <div class="blog-grid" style="margin-top:2rem">{relc}</div></div></section>""" + mini_cta(depth=1) + footer(depth=1)
        write(f"blog/{p['slug']}.html", page)

# ---------------------------------------------------------------- CONTACT
def build_contact():
    body = page_hero("Let's build the heart of your home","Book a free in-home measure, request a quote, or just ask a question. We answer fast.","p118","Contact") + f"""
<section class="sec"><div class="wrap about-grid" style="align-items:start">
  <div class="reveal">{lead_form(light=True, ident='contact-form')}</div>
  <div class="reveal">
    <span class="eyebrow">Visit the workshop</span>
    <h2 class="h-lg">Talk to a real person.</h2>
    <div class="rule short"><span class="dot"></span></div>
    <p class="lead">Prefer to call? You will reach the team that actually templates and fits your stone — not a call centre.</p>
    <div style="display:grid;gap:1.1rem;margin-top:1.6rem">
      <div><div class="meta">Call</div><a href="tel:{TEL}" style="font-family:Jost;font-size:1.4rem">{PHONE}</a></div>
      <div><div class="meta">Email</div><a href="mailto:{EMAIL}" style="font-family:Jost;font-size:1.2rem">{EMAIL}</a></div>
      <div><div class="meta">Showroom &amp; workshop</div><p style="margin:.2rem 0">{ADDRESS}<br>{CITY}</p></div>
      <div><div class="meta">Hours</div><p style="margin:.2rem 0">{HOURS}</p></div>
    </div>
    <div class="area-map" style="margin-top:1.6rem;aspect-ratio:16/10"><img src="assets/img/p030.jpg" alt="Map"></div>
  </div>
</div></section>"""
    write("contact.html", head(f"Contact | {CO}","Book a free in-home granite countertop quote. Call "+PHONE+".","contact")+nav("contact")+body+footer())

# ---------------------------------------------------------------- SERVICE AREAS
def build_areas():
    chips="".join(f'<div class="chip" style="cursor:default">{a}</div>' for a in AREAS)
    cards="".join(f'<div class="post-card reveal"><div class="media"><img src="assets/img/{im}.jpg" alt="{a}"></div><div class="body"><span class="meta">Service area</span><h3>{a}</h3><p class="muted">Granite, quartz &amp; marble countertops templated, fabricated and fitted in {a}.</p></div></div>' for a,im in zip(AREAS[:6],["p004","p011","p021","p023","p033","p055"]))
    body = page_hero(f"Serving the {CITY}","Local crews, local fabrication. We template, cut and fit close to home — and we are still here years later.","p040","Service Areas") + f"""
<section class="sec"><div class="wrap">
  <div class="area-grid">
    <div class="reveal"><span class="eyebrow">Where we work</span><h2 class="h-xl">Across the whole metro</h2>
      <p class="lead">From the first measure to the final seal, every job is handled by our own team based right here. Find your area below — or call and we will confirm we cover you.</p>
      <div class="chips">{chips}</div>
      <a href="contact.html" class="btn btn-gold" style="margin-top:1.8rem">Book a free measure <span class="arr">→</span></a>
    </div>
    <div class="area-map reveal"><img src="assets/img/p030.jpg" alt="Service map"></div>
  </div>
  <div class="blog-grid" style="margin-top:4rem">{cards}</div>
</div></section>""" + mini_cta()
    write("service-areas.html", head(f"Service Areas | {CO}",f"Granite and quartz countertop installation across the {CITY}.","areas")+nav("areas")+body+footer())

# ---------------------------------------------------------------- RUN
if __name__ == "__main__":
    build_index()
    build_about()
    build_services()
    build_service_pages()
    build_gallery()
    build_financing()
    build_blog()
    build_posts()
    build_contact()
    build_areas()
    print("ALL PAGES BUILT")
