# RONGE UI DESIGN

A screenshot-driven UI method for mobile products.

RONGE makes one screen earn its place: explore three distinct directions, capture real iPhone screens,
get an independent screenshot-only critique, then remove everything that does not help the user decide.

The loop:

```text
3 directions
→ real iPhone screenshots
→ independent screenshot-only critic
→ <9 iterate / <7 restart
→ deletion audit
→ user signoff
```

No web mock as iOS evidence. No fake data, fake charts, or fake buttons.

## Quick start

```bash
cat SKILL.md
cat presets/example-product.md
bash scripts/seed.sh 3
python3 scripts/self_check.py
```

1. Write the brief with `templates/design-brief.md`.
2. Build three genuinely different directions.
3. Capture each on a real iPhone simulator (`references/iphone-preview.md`).
4. Spawn an independent critic that sees screenshots only (`references/design-critic.md`).
5. Iterate below 9/10; at 9+, run `references/audit.md`.
6. Record the screenshot, score and deleted elements in your product memory.
7. User confirms; only then replace production UI.

## What is in this repo

- `SKILL.md` — the entry point.
- `references/` — method, critic, iPhone capture, audit, handoff, accessibility, motion, validation, page recipes, open-source governance.
- `presets/example-product.md` — synthetic example; replace with your own private preset.
- `templates/` — design brief and review report.
- `scripts/` — seed generation, review validation, self-check.
- `examples/` — synthetic walkthrough, no real user or brand data.

## What stays private

Product brand terms, private screenshots, real user data and production presets do not belong in this repo.
See `references/open-source.md`.

## License

Code and text: MIT. See `LICENSE`.
Method credit: see `NOTICE.md`.
