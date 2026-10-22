# Contributing

RONGE is still a private draft. Before proposing a public release:

1. Do not add brand names, logos, private screenshots or real user data.
2. Use only synthetic examples in `examples/`.
3. Keep the generic core free of product-specific words; put those in `presets/`.
4. Run `python3 scripts/self_check.py`.
5. Add a changelog entry and bump `VERSION` for behavior changes.

For a new preset, create `presets/<product>.md` with:

- product identity;
- non-negotiable terms;
- rejected directions;
- known user preferences;
- evidence paths and privacy rules.

For a new page recipe, add it to `references/page-recipes.md` with one job, hierarchy, states and
anti-patterns.
