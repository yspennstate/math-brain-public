# BT4 handoff — account02/B20 two-pivot fork/collision reduction

Source run: `proofnet24/collective-BT4/account02/B20/20260922T013238Z-account02-B20-bt4-r11/late_lead_addendum.md`.
Outcome: `ESSENTIAL_STEP_APPLIED`, no full BT4 proof.

Late exact dependencies actually consumed:
- newest lead account02/B04 `20260922T011943Z-b04-bt4-r11/report.md`, blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`;
- newest named partner account04/B06 `20260922T011432Z-b06-bt4-r11/report.md`, blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`.

Reusable result. In the global no-six sink branch with fan triple `(3,2,2)`, suppose the partner's linkage alternative holds. Its two light returns `b->x`, `c->x` yield two different neutral pivots, replacing `b+` or `c+` by `x`. Apply the lead's off-pivot witness lemma to both pivots. Unless a six-fan is created, obtain five-witnesses `z_B` for `A∪C` outside `{x,b+}` and `z_C` for `A∪B` outside `{x,c+}`.

If `z_B != z_C`, two distinct regenerated deficits exist for different complementary pairs. If they coincide, the common witness must lie in the original remainder `R-{x}` and, writing cycle/R outfan counts `(a,b,c,r)`, necessarily has one of exactly three profiles:

`(5,0,0,2)`, `(4,1,1,1)`, `(3,2,2,0)`.

The last is a second no-six sink heavy on the same cycle, so the partner's sink-localization applies recursively; the first two have only two/one R-outarcs and are correspondingly rigid.

This sharpens the lead's long-neutral-orbit/cross-linkage obligations to a fork/collision alternative. Next: prove that the two distinct witnesses yield compatible cross-packed splices, or that each collision profile forces a six-fan/strict exchange. Treat the same-run symmetric six-fan port-triangle reduction separately. Do not claim BT4 closure.
