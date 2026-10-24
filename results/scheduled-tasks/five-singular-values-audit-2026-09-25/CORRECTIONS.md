# Prior assistant review and corrections to challenge independently

Source: the immediately preceding interactive assistant review of the owner's 14-page `five_singular_values_full_proof.pdf`, dated 25 September 2026. Exact original PDF SHA-256: `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`. See README for pinned PDF and accompanying LaTeX. This note preserves the substantive corrections and conclusions of that review; it is not a new independent audit, formal proof, or guarantee.

## Prior review's conclusion, not an assumption

The previous assistant reported that it had checked all 14 pages and the 26 numbered proof-bearing results, found no fatal error in the bound 270 K^2/s, and considered the central argument mathematically sound subject to the corrections below. Every part of that judgment must be independently tested. A previous PASS must not supply a missing proof step, justify skipping a line, or count as an independent review of a later patch.

## C01 — Lemma 5.2, page 9: incorrect global diffeomorphism wording

The source calls the elliptic polar map from `(0,infinity) x [0,2pi)` onto the punctured plane a diffeomorphism. With the ordinary topology on that half-open interval, the inverse angle is discontinuous across the seam.

Proposed replacement: "On (0,infinity) x (0,2pi), this map is a diffeomorphism onto the plane with the ray w_0 + {r e_1 : r >= 0} removed. The omitted ray is Lebesgue null, and the absolute Jacobian is 1/(2 sqrt(det B))."

Then the angular integral gives `p_{q(W)}(v+delta) <= (2 sqrt(det B))^{-1} integral_0^{2pi} L dtheta = pi L/sqrt(det B)`. Verify the coordinate domain, null critical point, both signs of definiteness, measurable change of variables, and the constant independently. Prior classification: literal presentation error with a straightforward local repair, not a refutation of the lemma.

## C02 — Lemma 4.3, page 7, passage to (4.5): display Jensen

After the conditional Cauchy–Schwarz/Plancherel bound, explicitly write

`|E_{X_{I'}} F(X_{I'})|^2 <= E_{X_{I'}} |F(X_{I'})|^2`.

This supplies the step described as "averaging over X_{I'}". Recheck that the conditional complex measure is well defined, its density satisfies `|nu_x| <= p_Y`, and the scaled Plancherel coefficient is `(pi/|t|)^k`. Prior classification: omitted explicit justification, not a discovered inequality reversal.

## C03 — Lemma 5.3, pages 9–10: exclude an atom at the critical value

Add: "The remaining level set {w:q(w)=v} is the union of two affine lines and therefore has probability zero, since W has a joint density."

The two hyperbolic changes of variables cover values strictly above and below v. Check this null-set argument and all positive/negative branch Jacobians independently. The negative tail must use its own suitable original coordinate i', not assume the positive-tail coordinate also works.

## C04 — Abstract, page 1: qualify random-sign conversion

The conversion from 2m−1 large eigenvalues to m large crossing singular values requires the small-entry/no-pivot hypothesis. Without it, A=I_5 has five large eigenvalues but all crossing blocks A_{I,J} are zero.

Proposed description: "...a random-sign argument which, in the absence of a pivot, turns 2m−1 large eigenvalues into m large singular values of an off-diagonal block, for m in {1,2,3}..."

Proposition 6.4 includes the required hypothesis. Verify the exact hypothesis rather than treating the abstract as the theorem.

## C05 — Outline, page 1: singularity versus upper envelope

Replace the assertion that the conditional polynomial "has a square-root or logarithmic singularity" with the assertion that its density "admits a square-root or logarithmic upper envelope". In the definite two-coordinate case the density is bounded. An upper bound does not establish that the bounded object attains or has that singularity.

## C06 — Lemma 2.5, page 3: minor wording

"Both follow" introduces three assertions. Use "These assertions follow". Check all three singular-value assertions independently, including zero padding, dimensions and rank indexing.

## C07 — Introduction, page 1: unverified current-open-status claim

The previous interactive review did not establish by a complete current primary-source search that the three-large-eigenvalue bounded-density question is still open. Until independently documented, use: "The present argument does not settle whether three eigenvalues of modulus at least s always suffice for a bound CK^2/s."

Checking this particular literature statement belongs to the audit. Trying to solve the three- or four-eigenvalue problem does NOT: the owner's new instruction is audit only.

## Scope cautions preserved from the prior review

- The main conclusion is an essentially bounded density, not necessarily a continuous density. The integrable-Fourier branch establishes continuity; do not transfer it without proof to every conditioning branch.
- Remark 7.4 is a limitation of the order-three-crossing method at four eigenvalues, not a counterexample to a four-eigenvalue density theorem.
- No independence after a general rotation may be assumed. A projected joint density bound is not itself independence.
- A numerical diagnostic is not a universal proof. Existing Lean files for the longer manuscript are neither a formalization of every line of this PDF nor permission to skip claimed formalized parts. Verify exact statements, dependencies, axioms and actual build evidence before giving formal credit.

## Numerical values reported by the previous review, to recompute

| Expression | Previously reported value |
|---|---:|
| C3 | 14.81833766 |
| C2 | 12.09507257 |
| gamma1 | 0.3846763770 |
| gamma2 | 0.2373624642 |
| gamma3 | 0.09004855147 |
| Gaussian small-ball coefficient | 18.25531920 |
| L0=2+2 log19 | 7.888877958 |
| C3/gamma3 | 164.5594229 |
| C2/sqrt(gamma2) | 24.82575456 |
| 1+sqrt12*(pi+4 log2+2L0) | 76.14307501 |
| sqrt12*77 | 266.7358244 |
| 16*(8+4 log2+2 log19)+1/e | 266.9513463 |

These entries preserve earlier output only. Independently derive the exact expressions and verify rigorous inequalities; rounded decimal agreement is not a proof certificate.

## Prior proof-by-proof coverage claims to revisit

The prior reviewer labeled Lemmas 2.1–2.7, Theorem 3.1, Lemmas 3.2–3.3, Lemmas 4.2–4.3, Theorem 4.1, Corollary 4.4, Lemmas 5.1–5.6, Lemmas 6.2–6.3, Proposition 6.4, Propositions 7.1–7.2 and Theorem 1.1 valid, with the local qualifications above, and Remarks 7.3–7.4 valid. It especially checked Schur-complement loss k rather than 2k; heat-flow approximation; the complex-measure and mollified L2 step; volume-weighted Hölder and entropy; hyperbolic tails in original coordinates; ordered-pair factors in the Rademacher moment; all pivot branches; and final scaling. This list is a map of the previous review's claims, not new coverage for any scheduled worker. Every worker must build its own line-level evidence and report UNCHECKED portions honestly.

Keep the literal-source verdict separate from the repaired argument. A repair is proposed until independently reproduced; it does not retroactively make the original sentence correct. Preserve disagreements and downstream consequences, including any evidence contradicting the earlier favorable verdict.
