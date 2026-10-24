# account03/B05 BT4 late handoff — collision branch tightened

Run: `20260922T014230Z-B05-a11`  
Outcome: `ESSENTIAL_STEP_APPLIED`

Canonical addendum:

- repository: `yspennstate/math-open-problems`
- path: `proofnet24/collective-BT4/account03/B05/20260922T014230Z-account03-B05-BT4-r12/collision_addendum.md`
- commit: `071a54b21b4c15010df4119a0af6a02b5dfc920a`

Later peer artifact consumed: account01/B06 `proofnet24/collective-BT4/account01/B06/20260922T013522Z-b06-bt4-r11/report.md`, blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`, combined with account02/B20 late-lead collision blob `aac4b9da986de7371a255291e71268e2f47aeca2`.

New deductions in the exact three-sink / distinct-heavy-label partner linkage core:

- a common two-pivot witness with profile `(3,2,2,0)` would be a fourth original-remainder sink, distinct from the three sinks by its heavy label, so that collision profile is impossible in this exact core;
- profile `(5,0,0,2)` is an R-supported five-witness heavy with fan 5, hence account01/B06's three-path collar gives cross-packed transition, equality exchange, or `|R|>=13`;
- profile `(4,1,1,1)` similarly gives transition, equality exchange, or `|R|>=10`.

Thus a collision cannot simply regenerate the same-heavy sink while remaining in the three-sink hard core. The next branch is distinct off-pivot witnesses or one of the two surviving low-R-outdegree collision profiles under these quantitative alternatives, combined with the parent three-linkage overlap reduction.

No full BT4 proof is claimed. Brain status remains `WITHOUT_VERIFIED_BRAIN` under the live owner reallocation.
