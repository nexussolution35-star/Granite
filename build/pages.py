# -*- coding: utf-8 -*-
from build import *

# ============================================================ HOMEPAGE
def build_index():
    # SECTION 2 — HERO
    hero = f"""
<section class="hero" id="hero">
  <div class="hero-bg"><img src="assets/img/p094.jpg" alt="Luxury granite kitchen with stone island"></div>
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow on-dark">{CITY}'s stone countertop specialists</span>
      <h1>Granite worktops,<br>fabricated &amp; fitted for<br><span class="roll" id="roll" data-words='["your kitchen.","your island.","your home.","real life."]'><span class="w">your kitchen.</span></span></h1>
      <p class="sub">We template, cut and install natural and engineered stone — one accountable team, a fixed price, and an install we never sub out.</p>
      <div class="hero-badges">
        <div class="review-badge">
          <span class="rb-ic">{GOOGLE_ICON}</span>
          <span class="rb-txt"><span class="rb-top"><b>{RATING}</b> <span class="stars">★★★★★</span> <span class="rb-n">({REVIEWS})</span></span><span class="rb-lbl">Google Reviews</span></span>
        </div>
        <div class="review-badge">
          <span class="rb-ic">{FB_ICON}</span>
          <span class="rb-txt"><span class="rb-top"><b>{FB_RATING}</b> <span class="stars">★★★★★</span> <span class="rb-n">({FB_REVIEWS})</span></span><span class="rb-lbl">Facebook Reviews</span></span>
        </div>
      </div>
      <ul class="hero-trust">
        <li><span class="ck">✓</span> Laser-templated for invisible seams &amp; perfect cut-outs</li>
        <li><span class="ck">✓</span> Free in-home measure &amp; physical slab samples</li>
        <li><span class="ck">✓</span> Fixed written price — no surprise extras</li>
      </ul>
    </div>
    <div class="reveal">{lead_form(ident='hero-form')}</div>
  </div>
</section>"""

    # SECTION 3 — REVIEWS
    revcards = "".join(f"""
      <div class="rev-card reveal">
        <div class="stars">★★★★★</div>
        <p>“{t}”</p>
        <div class="rev-who"><div class="rev-ava">{who[0]}</div><div><b>{who}</b><small>{loc}</small></div></div>
      </div>""" for t,who,loc in TESTIMONIALS)
    reviews = f"""
<section class="sec bg-paper" id="reviews">
  <div class="wrap">
    <div class="rev-top reveal">
      <div>
        <span class="eyebrow">What homeowners say</span>
        <h2 class="h-xl">Trusted across <span class="thin" style="color:var(--gold-deep)">{REVIEWS} kitchens</span></h2>
      </div>
      <div class="rev-score">
        <span class="big">{RATING}</span>
        <div><div class="stars">★★★★★</div><small class="muted">Verified Google &amp; Houzz reviews</small></div>
      </div>
    </div>
    <div class="rev-grid">{revcards}</div>
  </div>
</section>"""

    # SECTION 4 — ABOUT
    about = f"""
<section class="sec" id="about">
  <div class="wrap about-grid">
    <div class="about-media reveal">
      <img src="assets/img/workshop.jpg" alt="GraniteFactory team lifting a granite slab with a gantry crane at the workshop">
      <div class="badge"><span class="n">15</span><small>Years of stone</small></div>
    </div>
    <div class="reveal">
      <span class="eyebrow">Meet the workshop</span>
      <h2 class="h-xl">Owner-led. Local.<br>One team, start to finish.</h2>
      <div class="rule short"><span class="dot"></span></div>
      <p class="lead">GraniteFactory is the fabricator your neighbours recommend by name. We select the slab with you, template it with a laser, cut it in our own workshop, and our own crew fits it — no middlemen, no sub-contractors, no surprises.</p>
      <p class="muted">Granite, quartz, marble and quartzite for kitchens, islands, vanities and outdoor bars across {REGION}. One warranty, one point of contact, and a finish we put our name on.</p>
      <div class="sign">
        <div class="av">GF</div>
        <div><b>The {CO} workshop</b><small>Templating · Fabrication · Installation</small></div>
      </div>
      <p style="margin-top:1.6rem"><a href="about.html" class="txtlink">Learn more about us →</a></p>
    </div>
  </div>
</section>"""

    # SECTION 5 — SERVICES (marquee + grid + collections rings)
    marq_items = "".join(f"<span>{t}</span>" for _,t,_,_ in SERVICES)
    svc_cards = "".join(f"""
      <a class="svc-card reveal" href="services/{s}.html">
        <span class="num">{i:02d}</span>
        <img src="assets/img/{img}.jpg" alt="{t}">
        <div class="body">
          <h3>{t}</h3>
          <p>{d}</p>
          <span class="go">Explore <span>→</span></span>
        </div>
      </a>""" for i,(s,t,d,img) in enumerate(SERVICES,1))
    coll = "".join(f"""
      <div class="coll reveal">
        <div class="ring" style="--p:{p}%"><span>{lab}</span></div>
        <small>{b}</small>
      </div>""" for lab,p,b in COLLECTIONS)
    services = f"""
<div class="marquee"><div class="marquee-track">{marq_items}{marq_items}</div></div>
<section class="sec" id="services">
  <div class="wrap">
    <div class="sec-head center reveal" style="text-align:center">
      <span class="eyebrow">What we do</span>
      <h2 class="h-xl">Stone surfaces, one accountable team</h2>
      <p class="lead" style="margin-inline:auto">From the first slab to the final seal — every surface in your home, fabricated and fitted under one roof and one warranty.</p>
    </div>
    <div class="svc-grid">{svc_cards}</div>

    <div class="sec-head center reveal" style="text-align:center;margin-top:5rem">
      <span class="eyebrow">The materials</span>
      <h2 class="h-lg thin">Four collections, endless slabs</h2>
    </div>
    <div class="collections">{coll}</div>
  </div>
</section>"""

    # SECTION 6 — WHY
    WHY = [
        ("Own workshop &amp; crews","We fabricate and install in-house — never sub-contracted."),
        ("Laser templating","Digital precision means invisible seams and flawless cut-outs."),
        ("Fixed written price","The quote is the price. No extras for edges or removal."),
        ("Physical slab matching","We bring real samples to your home and your light."),
        ("Dust-controlled installs","Vacuum-assisted cutting and a spotless hand-over."),
        ("Lifetime sealing guidance","Sealed on install, with a care plan that keeps it perfect."),
    ]
    why_items = "".join(f"""
      <div class="why-item"><div class="ic">✓</div><div><b>{t}</b><p>{d}</p></div></div>""" for t,d in WHY)
    why = f"""
<section class="sec bg-ink why" id="why">
  <div class="wrap why-grid">
    <div class="reveal">
      <span class="eyebrow on-dark">Why homeowners pick us</span>
      <h2 class="h-xl">Built for the<br>way you live.</h2>
      <p class="lead">Fifteen years of stone in {CITY} homes. We live here, we fabricate here, and your warranty is good with a team that is not going anywhere.</p>
      <a href="contact.html" class="btn btn-gold" style="margin-top:1rem">Book a free measure <span class="arr">→</span></a>
    </div>
    <div class="why-list reveal">{why_items}</div>
  </div>
</section>"""

    # SECTION 7 — GALLERY
    gitems = "".join(f"""
      <div class="gal-item {mod} reveal" data-lb="assets/img/{img}.jpg">
        <img src="assets/img/{img}.jpg" alt="{cap}">
        <span class="tag">{cap}</span>
      </div>""" for img,cap,mod in GALLERY)
    gallery = f"""
<section class="sec bg-paper" id="gallery">
  <div class="wrap">
    <div class="rev-top reveal">
      <div><span class="eyebrow">Our work</span><h2 class="h-xl">Stone we have fitted</h2></div>
      <a href="gallery.html" class="txtlink">View full gallery →</a>
    </div>
    <div class="gal-grid">{gitems}</div>
  </div>
</section>"""

    # SECTION 8 — PROCESS
    STEPS = [
        ("Design &amp; sample","We visit, measure, and bring physical slabs to match your cabinetry, light and lifestyle."),
        ("Laser template","Once the slab is approved we laser-template your cabinetry for a precise digital model."),
        ("Workshop fabrication","Your stone is cut, edged and polished in our own workshop — seams planned, cut-outs perfect."),
        ("Install &amp; seal","Our crew fits, seals and hands over a spotless kitchen — usually inside a single day."),
    ]
    steps = "".join(f"""
      <div class="proc-step reveal"><span class="n">{i}</span><h3>{t}</h3><p>{d}</p></div>""" for i,(t,d) in enumerate(STEPS,1))
    process = f"""
<section class="sec" id="process">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">How it works</span>
      <h2 class="h-xl">Four steps, no surprises</h2>
      <p class="lead">Every stage is scheduled, photographed and explained. You approve the slab and the price before we cut a thing.</p>
      <div class="proc-pill"><span class="dot"></span> You are in control — walk away at any step, no pressure.</div>
    </div>
    <div class="proc-grid">{steps}</div>
  </div>
</section>"""

    # SECTION 9 — FINANCING / OFFERS
    financing = f"""
<section class="sec bg-ink" id="financing">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow on-dark">Offers &amp; financing</span>
      <h2 class="h-xl">Free measures, fair finance</h2>
      <p class="lead">Every quote is free, in-home and fixed in writing. When you are ready to proceed, flexible finance keeps the dream kitchen within reach.</p>
    </div>
    <div class="offer-grid">
      <div class="offer-card reveal">
        <div class="ic">◇</div>
        <h3>0% &amp; low-rate finance</h3>
        <p>Spread your worktop investment over 12–60 months through our third-party lending partners. Quick decisions, no early-settlement penalties, and we apply the rate before the written quote.</p>
      </div>
      <div class="offer-card reveal">
        <div class="ic">✦</div>
        <h3>Trade, military &amp; multi-room</h3>
        <p>Builders, designers and repeat clients get preferred pricing, and we discount every additional room — vanities, laundries, bars — quoted alongside your kitchen. Mention it before the quote and we build it in.</p>
      </div>
    </div>
    <p class="muted" style="color:var(--cool);margin-top:2rem">No obligation. No pressure. Honest answers, every visit. <a href="financing.html" class="txtlink" style="color:var(--gold-lt)">See financing options →</a></p>
  </div>
</section>"""

    # SECTION 10 — BLOG
    feat = BLOG_POSTS[0]
    others = BLOG_POSTS[1:4]
    other_cards = "".join(f"""
      <a class="post-card reveal" href="blog/{p['slug']}.html">
        <div class="media"><img src="assets/img/{p['img']}.jpg" alt="{p['title']}"></div>
        <div class="body"><span class="meta">{p['date']} · {p['cat']}</span><h3>{p['title']}</h3>
          <p>{p['excerpt']}</p><span class="go txtlink">Read more →</span></div>
      </a>""" for p in others)
    blog = f"""
<section class="sec bg-paper" id="blog">
  <div class="wrap">
    <div class="rev-top reveal">
      <div><span class="eyebrow">Journal</span><h2 class="h-xl">Stone, explained</h2></div>
      <a href="blog.html" class="txtlink">All articles →</a>
    </div>
    <a class="blog-feature reveal" href="blog/{feat['slug']}.html">
      <div class="media"><img src="assets/img/{feat['img']}.jpg" alt="{feat['title']}"></div>
      <div class="body"><span class="meta">{feat['date']} · {feat['cat']}</span>
        <h2 class="h-lg" style="margin:.4rem 0 .6rem">{feat['title']}</h2>
        <p class="muted">{feat['excerpt']}</p>
        <p style="margin-top:1rem"><span class="txtlink">Read the article →</span></p>
      </div>
    </a>
    <div class="blog-grid">{other_cards}</div>
  </div>
</section>"""

    # SECTION 11 — FAQ
    faqs = "".join(f"""
      <div class="faq-item reveal"><button class="faq-q">{q}<span class="pm">+</span></button>
        <div class="faq-a"><p>{a}</p></div></div>""" for q,a in FAQS)
    faq = f"""
<section class="sec" id="faq">
  <div class="wrap">
    <div class="sec-head center reveal" style="text-align:center">
      <span class="eyebrow">Questions</span><h2 class="h-xl">Frequently asked</h2>
    </div>
    <div class="faq-wrap">{faqs}</div>
  </div>
</section>"""

    # SECTION 12 — SERVICE AREA
    chips = "".join(f'<a href="service-areas.html" class="chip">{a}</a>' for a in AREAS)
    area = f"""
<section class="sec bg-paper" id="service-area">
  <div class="wrap area-grid">
    <div class="reveal">
      <span class="eyebrow">Where we work</span>
      <h2 class="h-xl">Serving {REGION}</h2>
      <p class="lead">Local crews across the metro. We template, fabricate and fit close to home — and we are still here when you need us years later.</p>
      <div class="chips">{chips}</div>
    </div>
    <div class="area-map reveal"><img src="assets/img/p030.jpg" alt="Service area"></div>
  </div>
</section>"""

    # SECTION 13 — CTA FORM
    cta = f"""
<section class="cta sec" id="cta-form">
  <div class="cta-bg"><img src="assets/img/p088.jpg" alt=""></div>
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow on-dark">Ready to start?</span>
      <h2 class="display" style="color:#fff">Get your free<br>stone quote today.</h2>
      <p class="lead" style="color:var(--cool);max-width:42ch">Tell us about your kitchen. We measure it, match the slab, and give you a fixed written price — usually the same week.</p>
      <ul class="hero-trust" style="margin-top:1.6rem">
        <li><span class="ck">✓</span> Free in-home measure &amp; physical samples</li>
        <li><span class="ck">✓</span> Fixed price, no surprise extras</li>
        <li><span class="ck">✓</span> Own workshop, own crews, one warranty</li>
      </ul>
    </div>
    <div class="reveal">{lead_form(ident='cta-form-el')}</div>
  </div>
</section>"""

    # PARTNERS — trusted suppliers strip (right after hero)
    PARTNERS = [
        ("pg-bison","PG Bison"),("wood4u","Wood 4U"),("eeziquartz","EeziQuartz"),
        ("sonae-arauco","Sonae Arauco"),("fhd","FHD — Fittings & Handle Distributors"),
        ("national-edging","National Edging"),
    ]
    plogos = "".join(
        f'<div class="partner reveal"><img src="assets/partners/{slug}.svg" alt="{nm}" loading="lazy"></div>'
        for slug,nm in PARTNERS)
    partners = f"""
<section class="sec-tight partners-sec" id="partners">
  <div class="wrap">
    <div class="sec-head center reveal" style="text-align:center">
      <span class="eyebrow">Our partners</span>
      <h2 class="h-lg thin">Built on the best stone, board &amp; hardware suppliers</h2>
      <p class="muted" style="max-width:60ch;margin-inline:auto">We fabricate with materials from the brands South African kitchens trust — so your worktop is backed by a supply chain as accountable as we are.</p>
    </div>
    <div class="partners-grid">{plogos}</div>
  </div>
</section>"""

    page = (head(f"{CO} | Granite &amp; Kitchen Countertop Installation in {CITY}",
                 f"Owner-led granite, quartz and marble countertop fabrication and installation across {REGION}. {RATING}/5 from {REVIEWS} reviews. Free in-home quotes — call {PHONE}.",
                 "home")
            + nav("home")
            + hero + partners + reviews + about + services + why + gallery
            + process + financing + blog + faq + area + cta
            + footer())
    write("index.html", page)

# blog data shared
BLOG_POSTS = [
    dict(slug="granite-vs-quartz-which-countertop", title="Granite vs Quartz: Which Countertop Is Right for Your Kitchen?",
         cat="Buying Guide", date="June 2026", img="p052",
         excerpt="Natural stone or engineered? We break down durability, maintenance, heat tolerance and cost so you can choose with confidence — not marketing."),
    dict(slug="how-stone-countertops-are-fabricated", title="From Slab to Worktop: How a Stone Countertop Is Actually Made",
         cat="Behind the Scenes", date="June 2026", img="p085",
         excerpt="Templating, cutting, edging, polishing and sealing — a plain-spoken tour of what happens between choosing your slab and the day it lands in your kitchen."),
    dict(slug="caring-for-granite-countertops", title="Caring for Granite & Quartz: A Simple, Lifetime Routine",
         cat="Care & Maintenance", date="May 2026", img="p124",
         excerpt="Sealing myths, what actually stains stone, and the two-minute daily habit that keeps a worktop looking like the day it was installed."),
    dict(slug="waterfall-island-worth-it", title="Is a Waterfall Island Worth It? The Honest Answer",
         cat="Design", date="May 2026", img="p022",
         excerpt="Mitred waterfall ends are the showpiece of the modern kitchen — but they are not for every slab or budget. Here is how to decide."),
]
print("pages module ready")
