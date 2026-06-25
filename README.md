# GraniteFactory — Countertops & Installation

A static marketing site for **GraniteFactory**, a granite & kitchen-granite
installation business.

It was built to a brief:

- **Conversion architecture** is replicated from **Website A** (the Cloud Nine
  contractor framework) — every section, every form, every trust component, in
  the exact same sequence.
- **Visual language** is taken from **Website B** (the *Twelve* minimalist-luxury
  kitchen site) — thin Jost/Inter typography, generous whitespace, full-bleed
  moody stone imagery, the circular "collection ring" motif, overlay gallery
  captions, hairline dividers, and a dark charcoal footer.
- **Brand palette** is derived from the GraniteFactory logo: charcoal
  `#1b1b1d` ("Granite") + bronze/gold `#c0892d` ("Factory") on white.
- **Imagery** uses the stone/kitchen photography from Website B (downloaded and
  self-hosted in `assets/img/`, so the site makes no third-party image calls).

## Homepage section sequence (matches Website A exactly)

1. `#hero` — rotating headline, review badges, trust bullets, **lead-capture form**
2. `#reviews` — aggregate rating + testimonial cards
3. `#about` — owner-led story + stat badge
4. `#services` — brand marquee, 7-service image grid, **collection rings**
5. `#why` — "built for the way you live" trust grid
6. `#gallery` — masonry project grid with **lightbox**
7. `#process` — four-step, no-surprises timeline
8. `#financing` — free-measure + finance / trade & military offers
9. `#blog` — featured article + 3-post grid
10. `#faq` — accordion
11. `#service-area` — city chips + map
12. `#cta-form` — final lead-capture form
13. footer + sticky mobile call bar

## Pages

```
index.html              Home (all 13 conversion sections)
about.html              Story + values
services.html           Services hub
services/*.html         7 service detail pages
gallery.html            Full lightbox gallery
financing.html          Offers + finance FAQ
blog.html               Journal index
blog/*.html             4 articles
contact.html            Lead form + NAP + map
service-areas.html      Coverage + area cards
assets/styles.css       Full design system
assets/img/*.jpg        Self-hosted stone photography
```

## Before you go live — edit these placeholders

All business details live at the top of `build/build.py` (and are baked into the
HTML). Search-and-replace or re-run the generator after editing:

| Placeholder            | Value to replace                         |
|------------------------|------------------------------------------|
| `(212) 555-0148`       | real phone                               |
| `hello@granitefactory.com` | real email                           |
| `1420 Stoneworks Avenue…` | real address                          |
| `Riverside Metro` + area names | real service region              |
| Reviews / rating       | real numbers                             |
| Map image              | swap `assets/img/p030.jpg` for an embedded Google Map |

The contact/quote forms are front-end only — wire them to your CRM or an email
handler (Formspree, Netlify Forms, etc.) to receive submissions.

## Develop / regenerate

The HTML is generated for consistency. To rebuild after editing content:

```bash
cd build && python3 pages2.py
```

No build step is required to *serve* it — it is plain static HTML/CSS/JS. To
preview locally:

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```
