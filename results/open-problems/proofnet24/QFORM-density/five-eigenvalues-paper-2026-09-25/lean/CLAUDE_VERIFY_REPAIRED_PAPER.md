# Claude Lean verification directive — repaired five-singular-value paper

Owner directive, 25 September 2026.

The owner has explicitly instructed Claude to **verify the results and proofs of the repaired five-singular-value paper in Lean**.

## Owner follow-up: acknowledge this message in GitHub when you read it

The owner has now explicitly asked Claude to confirm in GitHub, once it reads this message, whether it is carrying out the verification below.

**Claude: on your next actual read of this message, post your own acknowledgement in this repository. Confirm that you have read the owner's instruction and identify whether you have started verifying the results and proofs of the exact repaired paper below in Lean. Do not wait for the complete formalization before acknowledging.**

Create a new, uniquely named acknowledgement at:

`proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/lean/acknowledgements/claude/<actual-UTC-run-id>.md`

Include:

1. Your actual acknowledgement time in UTC and the revision of this directive that you read.
2. The manuscript path, pinned commit `4e530247ec0ef4101a6e5ecf621bd35a969c42aa`, and source blob `98e45d53d106db9a205051a4dd4917fc39dc2e3a`, confirming that this repaired paper is the verification target.
3. Your truthful current status: `VERIFYING`, `RECEIVED_NOT_STARTED`, or `BLOCKED`. Confirm that you are working on it only if that is actually true; otherwise explain what has not started or the specific blocker.
4. The precise lemma or proof dependency you are currently addressing, or the first one you will address if work has not started.
5. Paths and commit references for any actual Lean source, compiler output, and axiom checks supporting your progress. Distinguish prior reusable results from new work on this repaired source, and explicitly say when no new build has been run.
6. Any unresolved mathematical, formalization, access, or tool blockers.

Read back your committed acknowledgement and report its actual commit. Preserve earlier acknowledgements rather than overwriting their history. Do not expose credentials or private runtime identifiers.

**Only the actual Claude worker should author this acknowledgement. Other agents must not manufacture a confirmation on Claude's behalf. This posted request is not evidence that Claude has read it, started verification, or completed a proof.**

## Exact target

Repository: `yspennstate/math-open-problems`

Repaired manuscript commit: `4e530247ec0ef4101a6e5ecf621bd35a969c42aa`

Target source:
`proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/repaired-2026-09-25/paper.tex`

Pinned source blob: `98e45d53d106db9a205051a4dd4917fc39dc2e3a`

Target theorem:
[
s_5(A)\ge s>0
\Longrightarrow
\|p_{X^TAX+b^TX+c}\|_\infty\le 270 K^2/s
]
for real symmetric (A), arbitrary affine terms, and independent real coordinates with densities bounded by (K).

## Required Lean work

Claude should formalize and verify the **proofs of this paper**, not merely the numerical constants. Existing QFORM Lean files may be reused, but their scope must be stated exactly.

Priority proof dependencies include:

1. Fourier/regularization and conditional-density lemmas used in the paper.
2. Singular-value approximation, compression, perturbation, and signed Schur-complement count.
3. Geometric Brascamp–Lieb/product-projection bounds.
4. The grouped crossing-volume Fourier decay theorem, including the conditional-to-unconditional Jensen step.
5. The scalar, definite-pair, indefinite-pair, concentration, logarithmic-kernel, and negative-half-moment estimates.
6. The random-sign extraction and Proposition 6.4.
7. The no-pivot, scalar-pivot, definite-pair, and indefinite-pair branches.
8. Final normalization/scaling to (270K^2/s).

The formalization must not introduce moment, support, smoothness, iid, Gaussian, sign, or post-rotation-independence assumptions absent from the manuscript.

Every Lean theorem used for the final chain should be compiled and accompanied by `#print axioms`; no `sorry`, `admit`, or `sorryAx` is acceptable for a claimed verified dependency.

The final status must distinguish:
- fully kernel-verified;
- partially formalized;
- unformalized dependencies;
- failed or blocked statements.

The repaired manuscript above is the exact paper the owner instructed Claude to verify. Claude should verify the results and proofs in this paper in Lean. It supersedes the older immutable audit target for future formal verification.
