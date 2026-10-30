# fleet02/B09 five-singular-value audit — pass 01 (mollification first)

Run: `20260925T004344Z-fleet02-B09-five-singular-audit-a11`

Pinned source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`; `short/short.tex` blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`; PDF blob `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`; PDF SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.

## Scope and verdict

The full 676-line source was read. This invocation performed clause-level audit of the B09 starting lens and its immediate dependencies: lines 208–241, 260–391, plus correction hotspots at lines 41, 62, 65, 407–442. The rest remains **UNCHECKED in this pass**; this is not a complete-manuscript PASS.

Main B09 result: the mollification/measurability/DCT chain at lines 323–334 is **PASS**. The conditional complex measures are L2, the mollified norms are measurable, the approximate identity converges in L2, the uniform bound needed for DCT is valid, and integrating the original-coordinate bank first gives the stated characteristic-function product.

## Defects reproduced or found

1. **FALSE, line 222:** “Factors with beta_i=0 are at most one.” Exact counterexample: n=3,d=2, U=(e1,e2), W=e3 gives beta1=beta2=0. Safe repair: delete the count claim and drop *all* zero-beta factors, each bounded by one. No constant changes. This defect is not in CORRECTIONS.md.
2. **GAP, lines 319–322 (C02):** the passage to (4.5) needs the explicit Jensen step |E F|^2 <= E|F|^2. One line repairs it with no constant change.
3. **GAP, line 412 (C01):** the polar map on the half-open angular interval is not a global diffeomorphism. Delete one angular seam (a null ray) and use the same Jacobian.
4. **GAP, lines 415–442 (C03):** the proof must exclude an atom at the critical value v. The level set is two affine lines and has zero probability under the joint density. The short source already uses separate positive/negative tail coordinates i and i'.
5. **FALSE expository clauses:** line 41 omits the no-pivot condition from the abstract’s random-sign conversion; A=I_5 is an exact counterexample. Line 65 says the conditional polynomial “has” a singularity where the proof establishes only an upper envelope.
6. **UNCHECKED, line 62:** current literature/open-status claim was not independently surveyed this run.

No theorem-level counterexample was found in the reviewed mathematical range. After the local line-222 deletion and C01/C02/C03 repairs, Theorem 4.1 and Corollary 4.4 reconstruct with the displayed constants.

## Cross-check after independent derivation

After deriving the Section 4 calculations, I compared with fleet01/B06 and fleet01/B08. B06 independently records the same C02 Jensen omission and passes the mollification/Holder/entropy steps. B08 independently flags line 222 with the same n=3,d=2 counterexample and safe deletion repair. These peer reports were comparison evidence only, not premises for the derivations above.

## Remaining coverage

Earliest source line not clause-audited in this pass: line 1. Large unchecked ranges remain 1–207 (except 41,62,65), 242–259, and 392–676 (except 407–442). PDF render/source equivalence was not independently inspected visually because the connected repository interface exposes the PDF identity/blob/size but not a page-rendering surface in this run; page labels above use the shared package’s mapping where stated and are marked when unverified.
