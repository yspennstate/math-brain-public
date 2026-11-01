# fleet02/B09 — full fixed-multiplicity audit

Run: `20260924T144107Z-fleet02-B09-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
B09 lens: spectral rank perturbation, diagonal-dominance contradiction, adversarial finite symmetric examples.

## Source pin and package coverage

Pinned mathematical baseline:

- repository: `yspennstate/math-open-problems`
- baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- source size: 47,883 bytes, 790 lines.

Fresh master was resolved before the audit and the manuscript blob was unchanged. I read `README.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and the README-required `DELIVERY_STATUS.md`. The support package is now present. `checks.json` reports PASS for the newly supplied finite suite, but I treat those checks only as diagnostics, not proof.

## Overall mathematical verdict

**PASS for the stated 17-eigenvalue theorem, with two local nonfatal statement/wording GAPs repaired below.** I found no FALSE mathematical assertion used by the proof and no theorem-breaking GAP. No mathematical source range remains UNCHECKED in this review.

The audited statement is exactly: if the independent real coordinate densities are bounded by `K`, `A=A^T`, `s_17(A)>=s>0`, and `b,c` are arbitrary, then `X^TAX+b^TX+c` has an essentially bounded density with

`||p||_infinity <= 10000 K^2/s`.

This audit does **not** prove or claim the unrestricted three-eigenvalue conjecture.

## Line-by-line ledger

| Source lines | Item | Status | Independent reasoning / repair | Impact / next obligation |
|---|---|---|---|---|
| 1–46 | packages, notation, abstract | PASS | Definitions are consistent with later use; abstract states exactly the fixed-multiplicity result. | none |
| 47–90 | theorem, corollary, normalization, architecture | PASS | Quantifiers preserve arbitrary signs, remaining spectrum, affine terms and rough product laws. Scaling is correctly deferred to the end. | none |
| 91–160 | Fourier identities, power envelope, Riesz half-potential | PASS | Recomputed the `2*pi` Plancherel and `1/(2*pi)` inversion conventions. The Gaussian identity yields the stated `1/sqrt(2*pi)` Riesz constant; the `3/4` envelope gives weighted integral `12 sqrt(u)`. | none |
| 161–181 | `lem:rank` | PASS | Approximation numbers give both inequalities for arbitrary, possibly nonsymmetric matrices. No symmetry is used in the rank-shift step. | none |
| 183–207 | `lem:schur` | PASS | For invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`; positive and negative compression counts give `N_S(t)>=N_A(t)-k`. The `A+eps I` moving-threshold limit is valid for singular `A`. | none |
| 209–217 | strict diagonal dominance | PASS | Standard maximum-coordinate proof works without symmetry. | none |
| 221–255 | geometric rank-one Brascamp–Lieb | PASS | Heat-flow derivative has the right sign from the Parseval-frame contraction; Gaussian tails justify integration by parts; large-time normalization and small-time Fatou/monotone truncation are sound. | none |
| 258–282 | product projections | **GAP, nonfatal wording** | After rows with `b_i=0` are dropped, the text writes the entropy sum as if equality with `d` still held. The exact repair is `sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`; equivalently reinsert the omitted nonnegative zero-`b_i` terms before taking equality. The stated `e^(d/2)` bound is unchanged. | editorial repair only; no downstream constant changes |
| 284–301 | integrated scalar Fourier powers | PASS | `|fhat|^(2m)` is integrable by Plancherel and `|fhat|<=1`; inversion at zero is legitimate. The signed coefficient vector has norm `sqrt(2m)`, giving the displayed constant. | none |
| 303–324 | cross-block decoupling | PASS | Only the designated bank is copied. Pure phases cancel or are discarded by modulus; the coordinate differences remain independent with cap-one densities. | none |
| 326–373 | regularized crossing determinant | PASS | Rebuilt the graph frame and Jacobian. With `alpha=(2*pi*e)^2`, the `c_j` entropy factor and scalar Fourier powers cancel exactly; fourth-root accounting gives exponent `-1/8`. | none |
| 374–400 | Cauchy–Binet crossing volumes and envelopes | PASS | `Z_k=e_k(M^TM)` and the retained order-`k` determinant term give exponent `k/4`; order five is integrable, order three is used only with the Riesz weight. Constants check. | none |
| 404–422 | square profile and scalar conditioning | PASS | Inverse branches and interval-preimage length are correct; conditional domination is Tonelli-based and does not assert independence of the completed square from the remainder. | none |
| 423–434 | definite pair | PASS | Deterministic orthogonal diagonalization of the integral is legitimate; no rotated-coordinate independence is asserted. Jacobian is `1/(2 sqrt(det B))`. | none |
| 437–482 | hyperbolic pair | PASS | Recomputed the two hyperbola branches and Jacobian `1/(2 sqrt D)`. The original-coordinate tail spend, middle length, and AM–GM step `Lambda>=2/sqrt D` give the claimed logarithmic envelope. | none |
| 485–525 | quarter-power concentration | **GAP, nonfatal statement hypothesis** | The proof uses that `X` has independent coordinates with densities bounded by one, but the lemma statement itself does not restate this hypothesis. Add exactly that sentence to the statement. Every downstream invocation already occurs under those hypotheses, so the proof and theorem remain valid. The sign-cut gives `||M||>=||S||/4`; the Gaussian-smoothed Fourier calculation and layer cake constants check. | make lemma self-contained; no theorem change |
| 528–544 | pivot/volume definition and no-pivot entry bound | PASS | From `|a_ii|<eta` and `|a_ii a_jj-a_ij^2|<eta`, one gets `|a_ij|^2<eta^2+eta<2eta`, hence `|a_ij|<1/7`. | none |
| 545–564 | volume-sampled interpolation | PASS | Bordered determinant identity is exact up to sorting signs, removed by squaring. Singular seeds carry zero sampling weight, so the global extension count is an inequality. `P` interpolates rows `S` and columns `T` exactly. | none |
| 566–580 | nonsymmetric completion | PASS | `E_LL=off(A_LL-P_LL)`, `D` is diagonal and zero on `S union T`, and `R_LL=P_LL`. Support of `R-P` in rows `T` or columns `S` gives global `rank R<=3r`; restricted rank is exactly bounded by `r`. | none |
| 582–619 | no-pivot spectral-to-volume proposition | PASS | Rebuilt below in detail. The singular-value perturbation is applied to nonsymmetric `A-E`, which is valid. Global rank `3r` and restricted rank `r` are used in distinct places. Exact diagonal-dominance slack is `297/2800>0`. | baseline `4k-3` implication valid |
| 621–630 | random coordinate cut | PASS | Each ordered disjoint `(S,T)` survives a fair cut with probability `4^(-k)`. | none |
| 632–645 | no-pivot analytic consequences | PASS | The cut yields `Z_k^(-1/(2k))<=160`; constants `12 sqrt(80e)<200` and `800e<2400` are correct. | none |
| 646–674 | truncated potential and singular kernels | PASS | The `J(d)` split and logarithmic-kernel rearrangement are valid; the latter is maximized by centered interval overlap. | none |
| 676–714 | pivot controls truncated half potentials | PASS under standing product-law context | Scalar pivot uses one surviving Schur direction plus the repaired quarter-power lemma; definite and indefinite pair alternatives have the displayed constants. The proposition would be more self-contained if it repeated the standing product-law hypothesis, but all uses satisfy it. | optional exposition repair only |
| 716–724 | nine-eigenvalue half-potential bound | PASS | Pivot branch gives truncated `<=600`; adding the outside-unit tail costs at most one. No-pivot branch already controls the full half potential. | none |
| 726–749 | main theorem proof and scaling | PASS | No-pivot branch `<2400`; scalar pivot leaves 16 directions and gives `6010`; definite pair `<40`; indefinite pair leaves 15 directions and gives `<251`. For `Y=KX`, `Q=(s/K^2) Qtilde`, giving `10000 K^2/s`. | theorem closes |
| 750–790 | threshold accounting, limitations, bibliography | PASS | Correctly distinguishes global `3r` and restricted `r` ranks and does not claim continuity in pivot branches or the unrestricted `s_3` theorem. | none |

## B09 reconstruction of the spectral/rank contradiction

Let a bad volume ratio occur at seed order `1<=r<=4`. The completion gives

`A=D+R+E`, `rank R<=3r`, `rank R[L,L]<=r`, `D=0` on the `2r` seed coordinates, and

`eps:=||E|| <= ||E||_F <= (r+1)/80 <=1/16`.

Put `m=4k-3`, with `r<=k-1`. Since `s_m(A)>=1`, Weyl's singular-value perturbation gives

`s_m(D+R)=s_m(A-E)>=1-eps`.

The nonsymmetric rank-shift inequality gives

`s_(m-3r)(D)>=s_m(D+R)>=1-eps`.

Because

`m-3r = 4k-3-3r >= r+1`,

there are at least `r+1` diagonal entries of `D` with modulus at least `1-eps`; they all lie in `L` because `D` vanishes on the seed. Choose `H` of size `r+1`. Since `E_ii=0` and there is no pivot,

`|R_ii| >= 1-eps-eta >= 371/400`.

For `i!=j` in `H`,

`|R_ij| <= |A_ij|+|E_ij| < 1/7+1/16 = 23/112`.

As `r<=4`, each off-diagonal row sum is strictly less than

`4*(23/112)=23/28`.

The exact margin is

`371/400 - 23/28 = 297/2800 > 0`.

Thus `R[H,H]` is strictly row-diagonally dominant and invertible, so its rank is `r+1`; but `H subset L` and `rank R[L,L]<=r`, contradiction. This validates the manuscript's count and also shows exactly where `4r+1` enters.

## Counterexample/stress work

### 1. Both completion-rank constants are genuinely sharp

Consider the finite symmetric matrix

`C = [[0,3,3],[3,0,3],[3,3,3]]`.

Its eigenvalues are `-3`, `3-3sqrt(2)`, `3+3sqrt(2)`, all of modulus greater than one. Choose the disjoint one-coordinate seed `S={1}`, `T={2}`. The seed entry is `B=3`. Exact completion gives `D=0`, `E=0`, `P` of rank one, while

`rank R=3`, `rank R[L,L]=1`.

Thus for `r=1` both `rank R<=3r` and `rank R[L,L]<=r` are equalities. Direct sums of `r` copies give exact equality `rank R=3r`, `rank R[L,L]=r` for every `r`. Therefore the baseline proof cannot lower its count merely by replacing the global rank by `2r` or the restricted rank by `r-1`.

A no-pivot diffuse version is obtained by replacing each coordinate of `C` by a flat bank of size `m` and replacing each scalar entry `C_ab` by the constant `m x m` block `C_ab/m`. The three nonzero eigenvalues are unchanged. For `m>=301`, every physical diagonal is `<1/100`, and every principal two-by-two determinant has modulus at most `18/m^2<1/100`, so this is a genuine no-pivot large-spectrum family. A seed formed by one physical coordinate from bank 1 and one from bank 2 still has global completion rank three and restricted rank one. Hence symmetry, the no-pivot condition, and unit-scale spectrum do not by themselves improve either rank constant.

### 2. Sixteen directions do not follow from the two abstract rank bounds alone

For `r=4`, split a 16-dimensional coordinate space into a seed `U` of size eight and two outside sets `H,G` of size four each. Let

- `D` be diagonal, equal to one on `H` and zero elsewhere;
- `R` be diagonal, equal to one on `U union G` and zero on `H`.

Then `D=0` on the seed, `rank R=12=3r`, `rank R[L,L]=4=r`, and

`D+R=I_16`.

So `D+R` has sixteen singular values equal to one, but `D` has only `r=4` large diagonal entries, not `r+1=5`. This is a finite symmetric counterexample to the attempted inference

`4r large singular values + global rank 3r + restricted rank r + seed-zero D => r+1 large D entries`.

It is **not** a counterexample to an `s_16` density theorem: this abstract packet has large physical diagonals and does not use the no-pivot small-entry structure. Its role is precise: reducing 17 to 16 requires additional structure beyond the two rank bounds and seed-zero property.

### 3. Independent numerical stress of the spectral lemmas

As diagnostics only, I generated nonsymmetric random `D,R` with `rank R<=q` in dimensions 2 through 10 and checked 2,499 admissible index instances of

`s_(j+q)(D+R)<=s_j(D)`;

there were zero violations. Separately I generated random symmetric matrices, with half the samples forced singular, and checked 7,000 threshold instances of the principal-Schur count for one- and two-coordinate pivots; there were zero violations. These calculations support but do not replace the proofs above.

## Threshold improvement status

After the baseline audit I independently reconstructed the later complete `QFORM-FIXED-MULTIPLICITY-9-v1` replacement proof (source artifact blob `054facef834d29927713c5d42a1f09a541c5644b`). My reconstruction of its grouped product-Fourier compiler, weighted-subset entropy cancellation, heavy-row promotion identities, order-three density receiver, order-two full half-potential receiver, and complete pivot/no-pivot assembly is recorded separately under this run's `improvements/fleet02/B09/...` artifact.

**Result of that reconstruction: PASS.** It proves the stronger fixed-multiplicity statement

`s_9(A)>=s > 0  =>  ||p_(X^T A X+b^T X+c)||_infinity <= 6010 K^2/s`,

with arbitrary dimension, signs, remaining spectrum, affine terms and rough independent coordinate laws. It does not prove the unrestricted three-eigenvalue conjecture.

I did not find a complete multiplicity-eight replacement proof. Current exact work localizes the `s_8` debt to a no-pivot overlap-one/two-sided near-singular collar; the analytic receiver uniform through the near-singular self-pair remains unpaid. Therefore **nine is the lowest complete threshold established in this B09 run**.

## Final classifications

- Baseline `s_17`: **PASS** mathematically.
- Product-projection summation wording: **GAP, repaired locally, nonfatal**.
- Quarter-power lemma missing product-law hypothesis in its statement: **GAP, repaired locally, nonfatal**.
- Any source line mathematically unreviewed in this run: **none**.
- Any FALSE theorem claim found: **none**.
- Complete lower threshold established/reconstructed here: **9**, constant `6010 K^2/s`.
- Multiplicity 8: **OPEN** in this run.
- Unrestricted three-eigenvalue QFORM: **OPEN**.
