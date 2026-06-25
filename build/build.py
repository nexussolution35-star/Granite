# -*- coding: utf-8 -*-
"""GraniteFactory static site generator.
Conversion architecture = Website A (Cloud Nine). Visual language = Website B (Twelve).
Emits a multi-page site into OUT."""
import os, html

OUT = "/home/user/Granite"

# ---------------------------------------------------------------- brand
CO      = "GraniteFactory"
PHONE   = "074 216 7873"
TEL     = "+27742167873"
EMAIL   = "designm37@gmail.com"
ADDRESS = "2 Transnet Avenue, Eloff Estate, Capital Park"
CITY    = "Pretoria"
REGION  = "the Greater Pretoria area"
POSTAL  = "Pretoria, South Africa, 0018"
HOURS   = "Mon–Fri 8:00–5:00 · Sat 8:00–1:00"
RATING  = "4.9"
REVIEWS = "168"

SERVICES = [
    ("kitchen-granite-countertops", "Kitchen Granite Countertops",
     "Hand-selected granite slabs cut, polished, and installed for the heart of your home.", "p020"),
    ("quartz-engineered-stone", "Quartz &amp; Engineered Stone",
     "Caesarstone, Silestone and engineered quartz — non-porous, consistent, and built for daily life.", "p100"),
    ("bathroom-vanity-tops", "Bathroom Vanity Tops",
     "Coordinated stone vanities and surrounds that carry the kitchen language through the home.", "p013"),
    ("waterfall-islands", "Waterfall Islands &amp; Edges",
     "Mitred waterfall islands and sculpted edge profiles that make the slab the centrepiece.", "p065"),
    ("outdoor-kitchens", "Outdoor Kitchens &amp; BBQ Tops",
     "Heat- and weather-resistant stone surfaces engineered for patios, braais and outdoor bars.", "p096"),
    ("stone-fabrication", "Custom Fabrication &amp; Edges",
     "Our own templating and CNC fabrication — seamless joins, precise cut-outs, perfect edges.", "p085"),
    ("templating-installation", "Templating &amp; Installation",
     "Laser-templated, dust-controlled installs by our own crews. We never sub out the install.", "p036"),
]

COLLECTIONS = [  # (label, percent, blurb)
    ("Granite", 72, "Natural igneous stone — every slab one of a kind, sealed for life."),
    ("Quartz", 58, "Engineered consistency, non-porous and virtually maintenance-free."),
    ("Marble", 66, "Timeless veining for statement islands and feature surrounds."),
    ("Quartzite", 81, "Natural stone with the durability of granite and the look of marble."),
]

AREAS = ["Capital Park", "Villieria", "Gezina", "Queenswood",
         "Waverley", "Brooklyn", "Menlo Park", "Centurion"]

GALLERY = [  # (img, caption, css-modifier)
    ("p004", "Charcoal island · honed granite", "tall"),
    ("p022", "Statement waterfall · Calacatta quartz", "wide"),
    ("p021", "Bright kitchen · polished marble", ""),
    ("p023", "Open-plan · full-height splashback", ""),
    ("p055", "Bespoke pantry · matte stone", "tall"),
    ("p011", "Family kitchen · warm granite", ""),
    ("p070", "Slab detail · book-matched veining", ""),
    ("p118", "Minimal island · seamless join", "wide"),
    ("p024", "Entertainer's kitchen · waterfall ends", ""),
    ("p029", "Dark scheme · brushed quartzite", "tall"),
    ("p033", "Scandi-luxe · pale engineered stone", ""),
    ("p039", "Galley kitchen · mitred edge", ""),
    ("p119", "Showroom build · feature lighting", ""),
    ("p123", "Compact luxe · integrated sink", ""),
]

TESTIMONIALS = [
    ("The template-to-install timeline was exactly what they promised. Seam placement on our island is invisible — you have to be told where it is.", "The Harveys", "Granite kitchen · Waterkloof"),
    ("We priced three fabricators. GraniteFactory were the only ones who templated with a laser and walked us through the slab in person before cutting.", "Priya & Sam", "Quartz island · Brooklyn"),
    ("Old laminate gone in a morning, stone in by afternoon, and they vacuumed the place spotless. The crew clearly does this every single day.", "M. Okonkwo", "Vanity + kitchen · Capital Park"),
]

FAQS = [
    ("How long does a granite kitchen take from quote to install?",
     "Most kitchens are templated within a week of slab approval and installed 7–10 working days after templating. We give you the exact dates in writing before any deposit, and a single point of contact for the whole project."),
    ("Do you fabricate the stone yourselves or sub it out?",
     "Everything is fabricated in our own workshop and installed by our own crews — we never sub out the cut or the install. That is why we can stand behind the seams, the edges and the timeline."),
    ("Granite, quartz or quartzite — which should I choose?",
     "It depends on how you cook and live. Granite and quartzite are natural and heat-tolerant; quartz is non-porous and ultra-consistent. We bring physical samples to your home and match them to your cabinetry and light before you commit."),
    ("Do you template digitally?",
     "Yes. We laser-template every job for a precise digital model of your cabinetry, so cut-outs for sinks, hobs and outlets land exactly right and joins disappear."),
    ("Is the quote really fixed?",
     "Your written quote is the price you pay. We measure on site, confirm the slab, and lock the number — no surprise extras for edges, cut-outs or removal of the old top."),
]

# ---------------------------------------------------------------- helpers
def head(title, desc, active, depth=0, page_css=""):
    pre = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@200;300;400;500;600&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/styles.css">
<link rel="icon" type="image/svg+xml" href="{pre}assets/logo-emblem.svg">
<script>document.documentElement.className+=' js';</script>
{page_css}</head>
<body>
"""

def nav(active, depth=0):
    pre = "../" * depth
    def cls(name): return ' class="active"' if name == active else ''
    svc_links = "".join(
        f'<a href="{pre}services/{s}.html">{t}</a>' for s,t,_,_ in SERVICES
    )
    links = [
        ("home", f"{pre}index.html", "Home"),
        ("about", f"{pre}about.html", "About"),
        ("services", f"{pre}services.html", "Services"),
        ("gallery", f"{pre}gallery.html", "Gallery"),
        ("areas", f"{pre}service-areas.html", "Service Areas"),
        ("financing", f"{pre}financing.html", "Financing"),
        ("blog", f"{pre}blog.html", "Journal"),
        ("contact", f"{pre}contact.html", "Contact"),
    ]
    mob = "".join(f'<a href="{u}">{t}</a>' for _,u,t in links)
    nav_li = ""
    for key,u,t in links:
        if key == "services":
            nav_li += (f'<li class="has-drop"><a href="{u}"{cls("services")}>{t} ▾</a>'
                       f'<div class="drop">{svc_links}<a href="{pre}services.html">All Services →</a></div></li>')
        else:
            nav_li += f'<li><a href="{u}"{cls(key)}>{t}</a></li>'
    brand = f"""<a href="{pre}index.html" class="brand" aria-label="{CO} — Countertops & Installation">
      <img class="brand-mark" src="{pre}assets/logo-emblem.svg" alt="" width="46" height="46">
      <span class="brand-txt">
        <span class="brand-word"><span class="b1">Granite</span><span class="b2">Factory</span></span>
        <span class="brand-sub">Countertops &amp; Installation</span>
      </span>
    </a>"""
    return f"""<div class="topbar"><div class="wrap">
  <div class="tb-l"><span class="star">★</span> {RATING} / 5 · {REVIEWS} verified reviews</div>
  <div class="tb-r">
    <span class="tb-hide">{HOURS}</span>
    <a href="mailto:{EMAIL}" class="tb-hide">{EMAIL}</a>
    <a href="tel:{TEL}"><b>{PHONE}</b></a>
  </div>
</div></div>
<header class="site-head" id="head">
  <div class="wrap nav">
    {brand}
    <nav><ul class="nav-links">{nav_li}</ul></nav>
    <div class="nav-cta">
      <span class="avail"><i class="pulse"></i> We're Available Now</span>
      <a href="tel:{TEL}" class="nav-phone"><span>{PHONE}</span></a>
      <a href="{pre}contact.html" class="btn btn-gold est">Get My Free Estimate</a>
    </div>
    <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
  <div class="mobile-menu" id="mobile">{mob}<a href="tel:{TEL}">Call {PHONE}</a></div>
</header>
"""

def footer(depth=0):
    pre = "../" * depth
    svc = "".join(f'<a href="{pre}services/{s}.html">{t}</a>' for s,t,_,_ in SERVICES)
    areas = "".join(f'<a href="{pre}service-areas.html">{a}</a>' for a in AREAS[:6])
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a href="{pre}index.html" class="brand foot-brand">
          <img class="brand-mark" src="{pre}assets/logo-emblem.svg" alt="" width="44" height="44">
          <span class="brand-txt"><span class="brand-word"><span class="b1">Granite</span><span class="b2">Factory</span></span>
          <span class="brand-sub">Countertops &amp; Installation</span></span>
        </a>
        <p>Countertops &amp; installation, done by one accountable team. We template, fabricate and fit natural and engineered stone across {REGION} — and we never sub out the install.</p>
        <div class="soc">
          <a href="#" aria-label="Facebook">f</a>
          <a href="#" aria-label="Instagram">◎</a>
          <a href="#" aria-label="Pinterest">P</a>
          <a href="#" aria-label="Houzz">h</a>
        </div>
      </div>
      <div><h4>Services</h4>{svc}</div>
      <div><h4>Service Areas</h4>{areas}<a href="{pre}service-areas.html">All areas →</a></div>
      <div>
        <h4>Visit / Contact</h4>
        <a href="https://maps.google.com/?q={ADDRESS.replace(' ','+')}+Pretoria" target="_blank" rel="noopener">{ADDRESS}<br>{POSTAL}</a>
        <a href="tel:{TEL}">{PHONE}</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <p style="margin-top:.8rem">{HOURS}</p>
      </div>
    </div>
    <div class="foot-bot">
      <span>© 2026 {CO}. All rights reserved.</span>
      <span>Templating · Fabrication · Installation · Free in-home quotes</span>
    </div>
  </div>
</footer>
<div class="callbar"><a href="tel:{TEL}">Call Now</a><a href="{pre}contact.html">Free Quote</a></div>
<div class="lb" id="lb"><span class="x" id="lbx">×</span><span class="nav-a prev" id="lbp">‹</span><img id="lbi" alt=""><span class="nav-a next" id="lbn">›</span></div>
{scripts()}
</body></html>"""

def scripts():
    return """<script>
(function(){
  // header shadow on scroll
  var h=document.getElementById('head');
  addEventListener('scroll',function(){h.classList.toggle('scrolled',scrollY>10)});
  // mobile menu
  var b=document.getElementById('burger'),m=document.getElementById('mobile');
  if(b)b.addEventListener('click',function(){m.classList.toggle('open')});
  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function(q){
    q.addEventListener('click',function(){
      var it=q.parentElement,a=it.querySelector('.faq-a');
      var open=it.classList.toggle('open');
      a.style.maxHeight=open?a.scrollHeight+'px':0;
    });
  });
  // reveal on scroll
  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}})},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});
  // safety: never leave content hidden if observer misfires
  setTimeout(function(){document.querySelectorAll('.reveal:not(.in)').forEach(function(el){
    if(el.getBoundingClientRect().top<innerHeight)el.classList.add('in');})},2500);
  // hero rolling word
  var roll=document.getElementById('roll');
  if(roll){var words=JSON.parse(roll.dataset.words),i=0;
    setInterval(function(){i=(i+1)%words.length;
      roll.innerHTML='<span class="w">'+words[i]+'</span>';},2200);}
  // lightbox gallery
  var imgs=[].slice.call(document.querySelectorAll('[data-lb]'));
  var lb=document.getElementById('lb'),lbi=document.getElementById('lbi'),idx=0;
  function show(n){idx=(n+imgs.length)%imgs.length;lbi.src=imgs[idx].dataset.lb;lb.classList.add('open');}
  imgs.forEach(function(el,n){el.addEventListener('click',function(){show(n)})});
  function close(){lb.classList.remove('open')}
  var x=document.getElementById('lbx');if(x)x.onclick=close;
  lb.addEventListener('click',function(e){if(e.target===lb)close()});
  var p=document.getElementById('lbp'),nx=document.getElementById('lbn');
  if(p)p.onclick=function(){show(idx-1)};if(nx)nx.onclick=function(){show(idx+1)};
  addEventListener('keydown',function(e){if(!lb.classList.contains('open'))return;
    if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(idx-1);if(e.key==='ArrowRight')show(idx+1);});
  // parallax hero
  var pb=document.querySelector('.hero-bg img');
  if(pb)addEventListener('scroll',function(){pb.style.transform='scale(1.06) translateY('+(scrollY*.12)+'px)'});
  // form stub
  document.querySelectorAll('form').forEach(function(f){f.addEventListener('submit',function(e){
    e.preventDefault();
    f.innerHTML='<div style="padding:2rem 0;text-align:center"><div style="font-family:Jost;font-size:1.6rem;font-weight:300;margin-bottom:.4rem">Thank you.</div><p style="opacity:.8;margin:0">Your request is in. This is a front-end build — connect the form to your CRM or email handler to receive submissions.</p></div>';
  });});
})();
</script>"""

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", path)

# lead form markup (reused in hero + cta)
def lead_form(light=False, ident="lead"):
    cls = "lead-card light" if light else "lead-card"
    opts = "".join(f"<option>{t}</option>" for _,t,_,_ in SERVICES)
    return f"""<form class="{cls}" id="{ident}">
  <div class="lc-top">Free in-home quote</div>
  <h3>We call you back in minutes.</h3>
  <p class="lc-note">No obligation, no pressure — just an honest measure and a fixed price.</p>
  <div class="form-grid">
    <input class="form-input" placeholder="Your name" required>
    <input class="form-input" type="tel" placeholder="Phone number" required>
    <input class="form-input col-2" type="email" placeholder="Email address" required>
    <select class="form-input col-2" required><option value="" selected disabled>How can we help?</option>{opts}<option>Something else</option></select>
    <input class="form-input col-2" placeholder="Property address">
    <textarea class="form-input col-2" rows="2" placeholder="Tell us about your project (optional)"></textarea>
    <button class="btn btn-gold btn-block col-2" type="submit">Get my free quote <span class="arr">→</span></button>
  </div>
  <p class="form-fine">We never send unsolicited spam · Your details stay private</p>
</form>"""
print("module loaded")
