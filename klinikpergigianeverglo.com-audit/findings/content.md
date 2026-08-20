# Content Quality & E-E-A-T — 62/100

## Strengths (genuine)

- Original Malay copy addressing real anxieties: *"takut sakit, takut kena judge, risau kos rawatan"*
- **Named practitioners**: Dr. Farah Fatah (Pengarah & Doktor Gigi, ~10 yrs), Dr. Najmina
- 26 verbatim Google reviews with names and recency
- 9 real pre-visit FAQs, present in raw HTML inside `<details>`
- Correct medical hedging: *"Cadangan rawatan bergantung kepada pemeriksaan doktor."*

## Gaps

### High — YMYL page, no credentials
No qualification (BDS/DDS) and, critically for Malaysia, **no MDC registration number** for
either doctor. No bio pages, no `Person` schema, no "medically reviewed by". This is the
largest content-side gap on a health page.

### High — no visible NAP
- Address: only inside a **collapsed FAQ answer**
- Phone: only inside the WhatsApp widget's JSON config (`601162649191`) — never as text
- Hours: only inside JSON-LD
- No map embed, no directions link

### Medium — testimonials are screenshots
8 × `Testimoni*.png` + the 10-image `#evgDeck` are images of text → unindexable.

### Medium — treatments are one sentence each
e.g. Braces: *"Untuk bantu susunan gigi yang tidak teratur."* No process, duration,
aftercare or indicative pricing — the actual search questions.

### Low — promo offers unreadable
Four "Promo Bulan Ini" images carry `alt=""`, so offer, price and validity are invisible.
