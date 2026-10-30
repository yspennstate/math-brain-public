# fleet01/B05 full source audit — fixed multiplicity

Run: `20260924T145314Z-fixed-multiplicity-audit-r11`  
Owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Source theorem under audit: candidate 17-eigenvalue theorem only; no claim about the unrestricted three-eigenvalue conjecture and no owner-level independent-validation flag.

## Source pin and package read

I read fresh `math-research-brain/main/AGENTS.md` and `scheduled_tasks/CURRENT_OBJECTIVE.md` before the mathematics and created only my own actual sign-in.

The audited manuscript is pinned to

- repository: `yspennstate/math-open-problems`;
- source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`;
- source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- package-recorded SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- source size recorded by package: 47,883 bytes / 790 lines.

I read the entire 790-line `manuscript.tex`, plus `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md` as present on `master`. The latest-commit query for `manuscript.tex` still pointed to the source commit above; peer audit/improvement additions on master did not alter the manuscript source.

## Urgent defects first

**No theorem-breaking FALSE or GAP was found in the pinned 17-eigenvalue manuscript.** My mathematical verdict on the candidate theorem is **PASS**.

The theorem I checked is exactly:

> For arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent real coordinates with probability densities bounded by `K`, if `s_17(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density with `||p_Q||_infinity <= 10000 K^2/s`.

I found no step that assumes iid inputs, moments, compact support, connected support, Gaussianity, log-concavity, or independence after an orthogonal rotation.

### Items deliberately not upgraded to PASS

- **UNCHECKED (bibliographic/priority only):** historical priority/completeness of literature metadata and any claim external to the mathematical proof.
- **UNCHECKED (hash recomputation):** I verified the source blob and the package-recorded SHA-256 agree across the manifest/status files, but did not independently recompute the SHA-256 from raw bytes in this invocation.
- **UNCHECKED (script execution in this invocation):** I read `verify.py` and `checks.json`; I did not rerun the checker here. The saved package output reports PASS on 534 exact interpolation seeds, 18 exact volume checks, 240 floating Schur checks, and 30 graph-integral checks. These finite checks are support, not substitutes for the proof.

## Complete line ledger

Every source line 1--790 is assigned below; there is no omitted source interval.

| Source range | Status | Audit result |
|---|---|---|
| 1--46 | PASS | Title/abstract/scope/notation accurately separate the fixed-multiplicity result from the three-eigenvalue conjecture. Mathematical scaling and singular-value notation are consistent. External priority is separately UNCHECKED above. |
| 47--57 (`thm:main`) | PASS | Quantifiers match the owner target: arbitrary symmetric matrix, arbitrary affine terms, independent cap-`K` densities, `s_17>=s`, essential density bound `10000K^2/s`. |
| 58--90 | PASS | Road map and reductions do not introduce hidden input assumptions. |
| 91--120 (`lem:fourier`) | PASS | Gaussian smoothing, Fourier inversion and Plancherel constants are consistent with `hat f(t)=int e^{itx}f(x)dx`. The singular Fourier kernel is used distributionally/through nonnegative regularization, not by assuming a pointwise density version. |
| 121--130 (`lem:envelope`) | PASS | Power-envelope integration and the `q>1` threshold are correct. |
| 131--160 (`lem:riesz`) | PASS | Half-Riesz representation and regularization are valid for rough laws; Tonelli is used on nonnegative kernels. |
| 161--168 | PASS | Singular-value conventions and block notation are consistent. |
| 169--181 (`lem:rank`) | PASS | Rank perturbation is stated for arbitrary matrices and singular values, exactly what is later needed for nonsymmetric interpolation matrices. |
| 182--208 (`lem:schur`) | PASS | Schur complement loss is by pivot size, with perturbation covering singular/near-singular limiting blocks. Affine terms remain arbitrary. |
| 209--220 (`lem:dd` and transition) | PASS | Strict diagonal dominance is invoked only on the square restricted block and gives invertibility as used. |
| 221--257 (`lem:bl`) | PASS | Rank-one Brascamp--Lieb/heat-flow proof is self-contained enough for the stated use; zero weights are handled by omission/limits. |
| 258--283 (`lem:projection`) | PASS | **B05 lens checked carefully.** The orthogonal completion is a deterministic change of variables in the full integral. The proof never claims the rotated coordinates are independent. It bounds the *joint marginal density* of an orthogonal projection, not conditional densities of rotated coordinates. |
| 284--309 (`lem:scalar-fourier` plus setup) | PASS | Scalar Fourier-power estimate follows from the projection density and Plancherel/interpolation with correct scaling. |
| 310--325 (`lem:decouple`) | PASS | Independent-copy decoupling is performed on literal original-coordinate product banks. Same-bank phases are discarded only by modulus where explicitly allowed. |
| 326--385 (`lem:determinant`) | PASS | Regularized determinant/graph compiler keeps physical product variables until after the independent-copy step. Endpoint determinants and exponents are consistent. |
| 386--403 (`eq:vol`/volume definitions) | PASS | Exterior-volume definitions and Cauchy--Binet identities match subsequent sampling. |
| 404--422 (`lem:square`) | PASS | Scalar square conditional pushforward is an a.e. statement; exceptional critical slice is harmless under Tonelli. No global pointwise density representative is silently assumed. |
| 423--436 (`lem:definite`) | PASS | Two-coordinate definite pair bound uses a deterministic linear/orthogonal integral change, not rotated random independence. Uniformity in induced affine translations is valid. |
| 437--484 (`lem:hyperbola`) | PASS | Indefinite pair change of variables and logarithmic envelope are valid as Borel/a.e. density bounds. Later averaging uses nonnegative envelopes, so exceptional density versions do not depend adversarially on the conditioned complement. |
| 485--527 (`lem:quarter`) | PASS | Quarter-power small-ball bound correctly splits scalar-diagonal/off-diagonal branches and uses regularized Fourier estimates; it does not assume pointwise van-der-Corput decay for rough one-variable laws. |
| 528--544 (pivot/volume setup) | PASS | Pivot alternatives are exhaustive and the small-entry consequences follow from the definitions. |
| 545--565 (`lem:sampling`) | PASS | Determinant-squared sampling is only over nonsingular seeds; Cauchy--Binet counting is correct. |
| 566--581 (`lem:completion`) | PASS | **Critical nonsymmetric interpolation check:** `R` need not be symmetric; the support decomposition yields global `rank R<=3r`, restricted `rank R[L,L]<=r`, `D=0` on the seed, and the stated Frobenius control of off-diagonal `E`. |
| 582--620 (`prop:volume`) | PASS | Rank bookkeeping is valid with singular values of the possibly nonsymmetric `A-E`. From `m=4k-3` and `r<=k-1`, `m>=4r+1`, giving at least `r+1` large diagonal entries of `D` outside the seed. Diagonal dominance then contradicts the restricted rank. |
| 621--631 (`lem:cut`) | PASS | Fair physical cut keeps expectation `4^{-k}` of each disjoint squared minor; no spectral-coordinate independence is invoked. |
| 632--653 (`prop:nopivot`) | PASS | `k=5` needs exactly `s_17>=1`; Fourier exponent `5/4>1` is integrable and constants stay below the declared budget. |
| 654--675 (`lem:kernels`) | PASS | Truncated singular-integral bounds are sufficient for later pivot estimates. |
| 676--715 (`prop:pivot-H`) | PASS | Scalar, definite-pair and indefinite-pair pivots are all covered. Conditional density envelopes are averaged via Tonelli; random critical values are controlled by the quarter-power logarithmic potential, not by a uniform conditional-density fiction. |
| 716--725 (`lem:nine`) | PASS | The bookkeeping that nine surviving directions suffice for the pivot half-potential branch is correct. |
| 726--749 (proof of `thm:main`) | PASS | Normalized no-pivot/pivot branches close under `s_17>=1`, and the rescaling `Y=KX`, `A/s` yields exactly `K^2/s`. |
| 750--790 | PASS | Closing remarks/appendix-style bookkeeping are consistent with the theorem and do not promote the unrestricted three-eigenvalue conjecture. External literature-priority assertions remain covered by the separate UNCHECKED item. |

## B05 lens: product projections, rotations, density versions, exceptional slices

### 1. Orthogonal changes in integrals are not claims of random independence

The projection lemma writes the density of a deterministic orthogonal projection as an integral over the orthogonal complement and applies Brascamp--Lieb to that integral. This is legitimate even though a general orthogonal rotation of the input destroys coordinate independence. The proof never factorizes the rotated law.

The same distinction survives later: normalized coefficient rows are used to calculate Jacobians or joint projected density caps. Whenever product factorization is needed, the variables are still literal original-coordinate banks or independent copies thereof.

### 2. Marginal projected density is not a conditional projected density

Nothing in the manuscript requires a statement of the form `||p_{Z|Y=y}||_infinity <= C` for rotated/projected coordinates. Such a statement is false in general even for a square with uniform product density. The manuscript instead uses either a joint projected density bound before conditioning, or conditions on literal source banks and then applies a source-valid one-dimensional/two-dimensional change of variables.

### 3. Density versions do not create a hidden common exceptional-set problem

The scalar-square, definite-pair and hyperbolic lemmas produce a.e. density bounds. In every later conditional use, the proof can be stated as domination of conditional measures against nonnegative test functions, followed by Tonelli. Thus no single pointwise representative has to work simultaneously for uncountably many conditioned parameters. The Fourier branches can likewise be justified first after Gaussian/mollifier regularization and then passed to the rough law.

## Verdict on the pinned 17-eigenvalue source

**PASS.** I found no mathematical GAP or FALSE line in the 790-line source. This is my worker-level audit verdict only; it is not an owner-level validation/publication/release action and says nothing about the unrestricted three-eigenvalue conjecture.

## Lowering the multiplicity: current mathematical status after this audit

I also independently checked the now-complete grouped product-Fourier replacement mechanism at multiplicity nine. The source-valid mechanism keeps every promotion on literal physical coordinates, mollifies the complex projected law before its `L^2` expansion, and uses only joint product-projection density bounds after deterministic coefficient changes. I find the nine-eigenvalue theorem mathematically sound.

A newer parameter retuning gives the sharper candidate

`||p_Q||_infinity <= 400 K^2/s` under `s_9(A)>=s`.

I checked its grouped compiler, the improved quarter-power constant, the full two-coordinate half-potential, the retuned no-pivot interpolation inequalities, all pivot alternatives, scaling, and numerical constants. My verdict on that **constant-400 multiplicity-nine candidate is PASS in this review**, but I do **not** mark it owner-validated: the file explicitly requested independent reviews, and this run supplies only one such review of that sharpened version.

Multiplicity eight remains **GAP/open**, not FALSE. The precise unresolved issue is analytic shared-anchor dependence: the terminal `s_8` geometry has dimension-free overlap-one determinant mass, but the shared physical coordinate cannot be assigned to two independent source banks, and collapsing the structure to the critical `|phi(t)|=O(1/|t|)` endpoint yields only all finite `L^r`, not `L^infinity`.

See the sibling improvement file from this run for a new exact frequency-Jacobian identity that translates every overlap-one minor directly into the determinant of the three physical frequencies appearing in the retained-copy formula.
