# account02 / B19 — five-singular-values line audit r13

## Pin and scope

Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`. Audit only; no lower-threshold or unrelated research.

Exact source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`.

- `short.tex`: blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`, 58,136 bytes, 676 lines, independently recomputed SHA-256 `f4a4f4c6db7f0ad4feffbe04041af3cf1a759fb4cb51f4979b6fd884eba26037`.
- `short.pdf`: blob `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`, 484,310 bytes, 14 page objects, independently recomputed SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.

Two complete current-run passes were performed: P3 fresh forward reconstruction with an adversarial falsification lens, then P4 reverse dependency/repair regression. P3/P4 each account for all 676 physical source lines. Clause-level multi-assertion records are in `CLAUSE_AUDIT.jsonl`; proof-unit hypotheses/dependencies and reproducible derivations are in `PROOF_UNITS.json`.

## Verdict

Literal-source verdict: **GAP/FALSE at local clauses; no fatal theorem counterexample found.**

Repaired theorem verdict: **PASS_AFTER_LOCAL_REPAIRS**. The reconstructed proof supports
[
s_5(A)ge s>0quadLongrightarrowquad |p_{X^TAX+b^TX+c}|_{infty,mathrm{ess}}le 270,K^2/s,
]
for independent real coordinates with densities bounded by (K), arbitrary real symmetric (A), arbitrary (b,c), arbitrary dimension/signature/remaining spectrum.

The auxiliary result also reconstructs:
[
s_3(A)ge s>0quadLongrightarrowquad sup_amathbb E|Q-a|^{-1/2}le77,K/sqrt s.
]
This is a negative-half-moment theorem only; no three-eigenvalue density theorem is claimed.

## Local source issues revalidated independently

- **L41 / PDF p1 — FALSE (C04, exposition only).** The abstract's random-sign conversion omits the no-pivot/small-entry hypothesis. (A=I_5) refutes the unqualified sentence. Section 6 itself has the correct hypothesis; add “in the no-pivot regime”.
- **L62 / p1 — UNCHECKED (C07, non-proof).** The examples showing one/two directions insufficient are correct. The current-literature assertion that the three-direction density case remains open was targeted in a fresh web search but not authoritatively resolved; it remains UNCHECKED.
- **L65 / p1 — FALSE wording (C05).** A definite pair need not have a singular density; the proof only needs the stated square-root/log upper-envelope alternatives. Rewrite the outline accordingly.
- **L148 / p3 — PASS with grammar repair (C06).** Three claims, not two; “Both” should be “All three”.
- **L222 / p5 — FALSE (B19-N01).** “Factors with (eta_i=0) are at most one” is false. Counterexample: (n=4,d=2), (U=[e_1,e_2]), (W=[e_3,e_4]), so (eta_1=eta_2=0). Repair: drop **all** zero-(eta) factors. They are independent of the integration variable and at most one; positive-(eta) rows retain (sumeta_i v_i v_i^T=I), and the entropy step still uses (0log0=0). No constant changes.
- **L319–321 / p7 — GAP (C02).** Insert Jensen/Cauchy (|mathbb EF|^2lemathbb E|F|^2) before averaging the conditional squared estimate. No constant changes.
- **L412 / p9 — FALSE presentation (C01).** The half-open polar chart is not literally a global diffeomorphism because of the angular seam. Delete one null ray or state an a.e. change of variables. The Jacobian and density constant are unchanged.
- **L431–437 / pp9–10 — PASS.** The pinned short source already uses separate positive-tail and negative-tail coordinates (i,i'); the historical selector defect is repaired here.
- **L441 / p10 — GAP (C03).** The proof treats (z>v) and (z<v) but must explicitly exclude an atom at (z=v). For a nondegenerate indefinite quadratic, (q=v) is the union of two affine lines, null under the joint density. This closes absolute continuity with no constant change.
- **L74 and bibliography / pp2,14 — UNCHECKED external metadata.** No proof dependency.

No additional mathematical defect was found in r13 beyond these independently revalidated items.

## End-to-end reconstruction highlights

Sections 2–5 were rebuilt directly from the pinned source. Fourier normalization, Gaussian inversion, the negative-half-moment transform, conditional measure domination, approximation-number/Weyl facts, singular Schur count, Gram/Cauchy–Binet identities, heat-flow Brascamp–Lieb, product projection densities, scalar Fourier powers, the grouped physical-hub compiler, mollified complex-measure (L^2), weighted Hölder/entropy, and the crossing-volume receivers all checked after the local L222 and L319–321 repairs. No rotated-coordinate independence is used.

Section 5's one- and two-coordinate estimates were reconstructed including rough densities and affine terms. The definite-pair chart needs only the L412 seam repair. The indefinite hyperbolic estimate correctly uses original-coordinate caps and separate tail selectors; L441 needs the null critical-level sentence. The concentration/log-moment and pair half-potential constants then follow.

Per the current owner instruction, Section 6's machine-checked spectral facts were treated as completed. Its textual interfaces were nevertheless checked: no-pivot gives (|a_{ii}|<1/12), (|a_{ij}|<5/48); (A-DAD=2C); the sign-chaos second moment has the stated pairing; compression leaves the margin (gamma_m=(44-5sqrt2(2m-1))/96); and the block dilation duplicates (s_m(A_{I,J})).

Section 7 was reverse-audited from the conclusion. The independently recomputed normalized branch values are:
[
C_3/gamma_3=164.559422908ldots<167,qquad
C_2/sqrt{gamma_2}=24.825754563ldots<26,
]
[
sqrt{12},(pi+4log2+2L_0)=75.143075010ldots<76,quad
sqrt{12}cdot77=266.735824366ldots<267,
]
[
16pi=50.265482457ldots<51,qquad
16(8+4log2+2log19)+e^{-1}=266.951346330ldots<269.
]
The cases are exhaustive, and the final (Y=KX) scaling gives exactly (K^2/s).

## PDF representation status

Exact PDF bytes, blob, hash and 14-page count were independently verified in this invocation. Direct rendered-page inspection remains **UNCHECKED/BLOCKED**: the required web PDF open route returned `DisabledError`, so no screenshot surface was available. Page references in the ledgers use B19's previously decoded page/source map for the same exact PDF blob, after current-run byte/hash/page-count revalidation. I do not claim a fresh visual render comparison.

## Package and formal evidence

The pinned package `README.md`, `AUDIT.md`, `MANIFEST.txt`, numerical check scripts/logs and relevant Lean run logs were read. Numerical/Monte-Carlo outputs were treated as diagnostics only. Section 6 formal results were accepted as completed per the owner instruction; recorded logs have `rc=0` and report only `propext`, `Classical.choice`, and `Quot.sound` under `#print axioms`. No fresh Lean build is claimed.

B20 has a current healthy account02 audit run, so B19 performed no fallback keeper or scheduler mutation. No email, notifications, permission, public release, cross-account authorization, lower-threshold research, or unrelated work was performed.

First remaining unchecked proof-independent clause: L62 literature-status statement. First remaining representation obligation: direct visual comparison of all 14 PDF pages when a render/screenshot path is available. There is no unresolved essential proof dependency after the stated local repairs.
