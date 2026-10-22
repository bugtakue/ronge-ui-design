# Open-source governance

This repository is the public, generic core. Product presets, brand terms, real screenshots and
user data stay private.

## What is public

- the three-phase method: Discover / Define / Deliver;
- seed strings and specific-reference prompts;
- the screenshot-only critic prompt and scorecard;
- real iPhone capture, states and accessibility checks;
- deletion audit and anti-patterns;
- the 100-point card and 9/10 gate.

## What stays private

- product names, logos and non-negotiable terms;
- real user quotes and screenshots;
- production API keys, internal paths, App Store IDs;
- private presets and page inventories.

## Contributor checklist

- [ ] No brand names, logos, private screenshots or real user data.
- [ ] Examples use synthetic data only.
- [ ] Generic core contains no product-specific words.
- [ ] Images/fonts/icons have clear licenses.
- [ ] `python3 scripts/self_check.py` passes.
- [ ] `CHANGELOG.md` and `VERSION` updated for behavior changes.

## Licensing

This repository uses MIT for code and text. If you add third-party images or fonts, record their
licenses separately; do not relicense them as MIT.

## Release checklist

- [ ] README quickstart works for a new user;
- [ ] synthetic walkthrough is complete;
- [ ] no private paths or internal commands;
- [ ] CI self-check green;
- [ ] tag `vX.Y.Z` and update CHANGELOG.
