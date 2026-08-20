# AI Search Readiness (GEO) — 55/100

## Strengths

- `Dentist` schema with a rich natural-language `description` — highly extractable
- `alternateName` covers misspellings ("Everglow Dental", "Everglo Dental Clinic") → helps
  entity resolution when a user asks an LLM by an approximate name
- 9 FAQs in **raw HTML** — directly citable Q&A passages
- Explicit services, `areaServed`, `paymentAccepted` (Atome, Grab PayLater, panel insurance),
  `knowsLanguage` — exactly the attributes needed to answer *"dentist near Bangi that takes
  Atome?"*

## High — the review corpus is invisible to non-rendering crawlers

The 26 Google reviews live in a JS array and are injected into `#tc` only when an
`IntersectionObserver` fires (`rootMargin: '600px 0px'`). The 10-image testimonial deck
(`#evgDeck`) is built the same way.

GPTBot, PerplexityBot, ClaudeBot and similar retrieval crawlers generally **do not execute
JavaScript**. To them, the page's richest citable content is an empty `<div>`.

These are static strings — there is no reason for them to be JS-injected. Server-render
them and keep the observer purely for the fan-out animation.

## Medium — missing extraction markup

- `FAQPage` — highest-value GEO addition (see `schema.md` for the rich-results caveat)
- `Review` objects for the reviews actually displayed
- `Person` for Dr. Farah Fatah and Dr. Najmina
- `sameAs` — without it, no reliable link to the clinic's TikTok / Facebook / Instagram /
  Google Maps entities

## Not assessed

`llms.txt` presence · AI crawler rules in robots.txt (GPTBot / CCBot / PerplexityBot) ·
actual citation rates in ChatGPT / Perplexity — all require network access.
