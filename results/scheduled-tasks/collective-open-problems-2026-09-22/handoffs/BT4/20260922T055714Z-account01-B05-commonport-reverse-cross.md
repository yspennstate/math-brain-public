# BT4 handoff — account01/B05 common-port reverse-cross closure

Run: `20260922T055714Z-b05-bt4-r11b`  
Candidate: `BT4-HT-COMMONPORT-REVERSE-CROSS-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical science: `yspennstate/math-open-problems`, commit `5f4ad4452b7b940cbe8f9106a934745496a75a36`, blob `2536e90a7442fd90deab441243f0feb90e33db4a`, path `proofnet24/collective-BT4/account01/B05/20260922T055714Z-b05-bt4-r11b/report.md`.

Named OTHER-account result actually applied: assigned partner account02/B06 `BT4-HT-ARCMAX-CAGE-COLLAPSE-v2`, shared commit `96fade26b836cc344b686fe1dee722a2d071703e`, controlling science blob `96fa9bdb0033fc6e6c3c42092e8259f882f8cd26`.

New result in the account01/B06 triangular common-port state `A=p->u->v->p`, `N_R^+(u)=N_R^+(v)={r_k}`:

1. `u,v` have residual outdegree exactly two in `A union R`, so each has five targets in `H union B` and at least four on `B`.
2. `B not->u,v`. If `c->u`, then for every B-target `a` of `u`, the genuine cycle `c->u->a->B[a,c]` together with `H` and the support-repair triangle `v->r_k->x->v` is a legal three-packing. Minimum total order forces every fan target into the first two successors of `c`, contradicting the at-least-four fan. Symmetrically for `v`.
3. Since the sink has only two B-targets, choose distinct fan targets of `u,v` outside the sink fan. Arc domination, iterated backward through the acyclic remainder if necessary, gives two x-free packed-to-B cross transitions with distinct B endpoints. Their R-interiors are not claimed disjoint.
4. The two pinned pure-R equality collars are not terminal. For `k=1`, `b->r0->r1`, `m_B(r1)=3`; for `k=2`, `b->r0->r1->r2`, `m_B(r2)=4`. Equality completion places the fan on the first `m` successors of `b`. Dominate the last fan arc. If its dominator is the preceding R vertex, one gets a genuine `|B|-1` replacement cycle disjoint from untouched `H,A`, contradicting minimum packing. Exact cage localization therefore forces a direct packed-to-B cross: dominator in `{h1,u,v}` for k=1 and `{h2,u,v}` for k=2.
5. The apparent short boundaries `|B|=3,4` are impossible: then the whole oriented exact-outdegree-seven graph would have 13 or 14 vertices, while `7N <= N(N-1)/2` forces `N>=15`.

Thus the common-port equality collars feed the CROSS splice frontier. If the last-fan dominator is `u` or `v`, the equality path extended by `r_k->p` gives a clean opposite B-to-A / A-to-B pair. If it is `h1` or `h2`, a three-support B-to-A plus H-to-B configuration remains.

First remaining local implication: `HT-CROSS-COALESCE-CLOSE` — use the target-distinct x-free reverse crosses plus the forward B-to-H/A return to force two disjoint replacement cycles, strict lexicographic decrease, a cyclic exchanged remainder, SIX, or a fourth cycle. The remaining obstruction is packed-source / R-ladder coalescence, not equality-collar length or target scarcity.
