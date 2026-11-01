# fleet03/B18 — exact fourteen-page five-singular-values audit, pass 7

Run `20260925T075405Z-fleet03-B18-fiveSV-audit-r7`.

Pinned source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`,
`proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/short/short.tex`
(blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`), paired with the exact 14-page PDF
SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.

## Result

Pass 7 is a fresh full source/clause reconstruction with an endpoint/equality, exceptional-set,
and imported-hypothesis lens. All physical source entries 1–676 are represented in the pass ledger.

The immutable literal source is not a clean PASS:
- FALSE: C01, C04, C05.
- GAP: C02, C03, C08, C09, C10, C11, C12.
- UNCHECKED: C07 current-open-status.
- C06 is editorial only.

Every load-bearing local GAP has an explicit zero-constant-loss repair. Under those repairs,
this pass found no unresolved load-bearing defect in the proof of the essentially bounded density
`<=270 K^2/s`. This is mathematical audit evidence, not proof-assistant certification or absolute
certainty. Global continuity is not established by the full proof; the no-pivot Fourier branch is C0.

## Pass-7 hypothesis/import review

Fresh primary-source matching was limited to statements actually cited in the paper. Rudelson–
Vershynin's scalar linear-image theorem has independent bounded-density coordinate hypotheses;
Livshyts–Paouris–Pivovarov gives a joint marginal-density theorem for product measures rather than
independence after projection; BGKS's cited theorem is bilinear-plus-affine and is not used here to
absorb arbitrary same-side quadratic blocks.

C07 remains UNCHECKED: a targeted current search did not find an exact solution to the three-large-
eigenvalue problem, but non-discovery does not certify present open status.

## Peer comparison after independent derivation

Only after the B18 derivation, fleet02/B08 pass 7 was compared. FINISH commit
`8c4c0209480e97787bb0d638505867d40a85e390` independently records 676 physical lines,
zero fatal theorem defects, and C12 at line 224. Checker commit
`d7e0eeb9a1e807a63a24f9908db0b453ca53d01f` gives the explicit witness
`n=2,d=1,U=e1` with uniform coordinates, for which the marginal density can vanish at y=2,
making ordinary `log p(2)` undefined. This is corroboration only, not a premise of B18's result.

## Minimal repairs

C01: open angular chart omitting a null ray.
C02: insert `|E F|^2 <= E|F|^2` before (4.5).
C03: explicitly exclude the critical-level atom.
C04: add “in the absence of a pivot” in the abstract.
C05: “admits an upper envelope,” not “has a singularity.”
C06: editorial pluralization.
C07: safer current-status wording until independently certified.
C08: state square density a.e./off critical value and choose a representative there.
C09: define J(0)=+infinity or use atomlessness before evaluation.
C10: define h(0)=+infinity.
C11: extend log_+(infinity)=infinity or specify the a.e. convention after atomlessness.
C12: if p(y)=0 the projection bound is trivial; take log only when p(y)>0.

Native learned-memory status: `WITHOUT_VERIFIED_BRAIN`.
