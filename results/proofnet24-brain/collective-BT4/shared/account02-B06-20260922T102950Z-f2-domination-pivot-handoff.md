# BT4 handoff — account02/B06 balanced-F2 domination pivot

Run: `b06-20260922T102950Z-7c94e1ad`  
Outcome: `ESSENTIAL_STEP_APPLIED` with local `CANDIDATE_REFUTED`  
Target: `OPEN_NOT_PROVED`  
Brain: `WITHOUT_VERIFIED_BRAIN`

Source-bound inputs:
- lead account02/B04 `20260922T101701Z-b04-bt4-r11`, `BT4-TRACE-TRANSVERSAL-ESCAPE-v1`, report blob `180efea97f9e427143959c7274a9bd2bba810021`;
- assigned partner account03/B04 `account03-b04-20260922t095155z-r11`, `BT4-R4-HMED-TWOFAN-NEUTRAL-PIVOT-v1`, report blob `06c33bc5ad285dc15cbd80945534ce87c485e93f`;
- compatible account04/B05 gap-signature handoff blob `e699a87b99e0c9c5d7ac272042846d48f977d73d`.

## New applied result: `BT4-R4-HMED-F2-DOMINATION-PIVOT-v1`

In the partner's neutral H-mediated packing `(T0,A,B*)`, let `z=q+` be in the exact balanced residual profile `(2,2,1,2)`. Then the old support arc `q->z` is dominated by some common predecessor `c`. The balanced remainder has no inarc to `z`; old-B chordlessness plus `q->h1` excludes every `B*` vertex as that common predecessor. Hence `c in T0 union A`.

If `C` is the support containing `c`, then `z` has exactly two outneighbors on `C`. Minimum total packed order applied to `c->z->y->C[y,c]` forces both targets to be exactly `{c+,c++}`. Therefore

`C' = c->z->c++->C[c++,c]`

is an equal-size directed replacement cycle and frees `c+`. A cyclic exchanged remainder is already a fourth cycle; otherwise the balanced F2 state necessarily propagates by a genuine neutral pivot. If `C=T0=h0 r0 x h0` and `c=r0`, the pivot frees `x`, and the exchanged remainder contains the saturation triangle `h2->r2->x->h2`, so this subcase is impossible in a counterexample.

First unpaid branch-specific implication: `BT4-HMED-F2-NEUTRAL-ORBIT-CLOSE-v1`. After removing the fatal `c=r0` case, control the forced pivot for `c in A union {h0,x}` and show its neutral orbit must produce SIX/new-heavy, strict packing decrease, cyclic remainder, usable off-trace/rank exit, or the fourth cycle.

## Adversarial repair / different mechanism

`BT4-ARCMAX-DAG-CERTIFICATE-v1`: in an arc-maximal BT4 counterexample, every missing ordered arc `u->v` has a certificate consisting of three disjoint directed cycles plus a disjoint directed return path `v->u`, and the complement of the three cycles is a DAG containing that path. Do not silently combine this normal form with exact-seven bookkeeping: saturation can raise outdegrees/change local packing geometry.

The stronger local shortcut `BT4-ARCMAX-TRIANGLE-CERT-v0` is false. An exact 19-vertex oriented near-tournament in the run checker has min outdegree 7, is 3-vertex-strong and every-arc dominated, but its unique missing pair `{1,17}` has shortest return `17->2->5->1` of length three. Adding `1->17` gives a 4-cycle certificate, not a triangle certificate. The graph is explicitly not a BT4 counterexample.

Reproducibility: report blob `ce3338d186e22081674244a390e0aeeb1511e56b`; checker blob `f94be02ffe08f61f1c69a5dda96fc7eb21af59af`, SHA-256 `8a384ca692c65c58daa8fe662755a388b97cb22353853c6caa8243b13288ad8b`; output blob `5c553b86e88b5eca6f4e2967355447b7ee751c29`, SHA-256 `ae041519ae304a904cc122e468bcf22300059fb6fe8048858d01186d0bd8abfd`, status `PASS`.
