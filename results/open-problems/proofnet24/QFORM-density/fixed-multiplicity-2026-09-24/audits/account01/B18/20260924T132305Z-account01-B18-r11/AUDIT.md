# account01/B18 full source/prior-art audit — run 20260924T132305Z-account01-B18-r11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and scope

- Requested baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Fresh `master` `manuscript.tex` git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`, exactly the pinned baseline blob.
- Owner-recorded/source-manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- `SOURCE_MANIFEST.json` now exists and records the same commit/blob/SHA-256, 47,883 bytes and 790 lines.
- I read `manuscript.tex` lines 1–790 in full, plus `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` on fresh `master`.
- The support files that were absent during my earlier B18 run are present now. `checks.json` records PASS for the new delivery reproducibility suite: 534 exact interpolation seeds, 18 exact volume-sampling cases, 240 floating Schur-threshold diagnostics and 30 graph-weight diagnostics. I audited the checker logic, but these finite tests are not mathematical proof and I do not count the recorded run as an independent rerun by this B18 invocation.

## Overall verdict

**PASS on the mathematical 17-eigenvalue theorem in this B18 reconstruction, with a prior-art/bibliography GAP-PRESENTATION.** I found no fatal mathematical defect after reconstructing every proof and lemma invocation. The candidate statement remains exactly

\[
s_{17}(A)\ge s>0\implies
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent real coordinate densities bounded by `K`.

This report **corrects my own earlier B18 false-positive GAP** concerning the singular Schur-complement limit. The original moving-threshold argument is valid; the baseline source does not need the fixed-delta replacement I previously proposed. The correction is proved explicitly below. My earlier report is preserved as historical evidence and should not be counted as a separate passing review. This B18 report does not self-award independent-validation status; the release gate remains for the designated synthesis/reconciliation process.

The full three-eigenvalue problem is not claimed solved. No global continuity statement is added.

## Fatal issues first

**No fatal mathematical issue found.**

### CORRECTION of prior B18 GAP — `lem:schur`, lines 183–207: PASS

Let the pivot size be `k`, put `m=N_A(t)-k`, and suppose `m>0` (otherwise the claim is trivial). For a sequence `epsilon -> 0` avoiding the finitely many values at which `A+epsilon I` or `B+epsilon I` is singular, define the Schur complement

\[
S_\epsilon=(D+\epsilon I)-C^T(B+\epsilon I)^{-1}C.
\]

Then `S_epsilon -> S`. For every eigenvalue `lambda` of `A` with `|lambda|>=t`,

\[
|\lambda+\epsilon|\ge t-|\epsilon|,
\]

so

\[
N_{A+\epsilon I}(t-|\epsilon|)\ge N_A(t).
\]

The already-proved invertible case at the threshold `t-|epsilon|` therefore gives

\[
N_{S_\epsilon}(t-|\epsilon|)\ge m.
\]

Because `S_epsilon` is symmetric, this is exactly

\[
s_m(S_\epsilon)\ge t-|\epsilon|.
\]

Singular values are continuous under operator-norm convergence, hence

\[
s_m(S)=\lim_{\epsilon\to0}s_m(S_\epsilon)\ge t.
\]

Thus `N_S(t)>=m=N_A(t)-k`. The moving threshold causes no loss: the proof tracks the **ordered m-th singular value**, not an arbitrarily matched individual eigenvalue. My earlier objection that an eigenvalue near `t` could move at speed larger than `|epsilon|` was inapplicable to this ordered-value inequality. The manuscript's original singular-case paragraph is mathematically sound.

**Downstream impact:** the scalar-pivot truncated-half-potential branch, the scalar-pivot main branch, and the indefinite-pair Schur-survivor branch are valid as written. My earlier `SCHUR_REPAIR.md` is unnecessary for correctness and should be treated only as an alternative proof.

## Complete source ledger: every line covered

`PASS` means reconstructed from the displayed definitions/proofs rather than inherited from the self-audit. `GAP-PRESENTATION` is nonfatal attribution/presentation debt. There are no `UNCHECKED` mathematical ranges in `manuscript.tex` in this run.

| Source lines | Status | Reasoning / dependency check |
|---|---|---|
| 1–35 | PASS | LaTeX definitions, theorem environments, notation macros and metadata; no hidden mathematical assumption. |
| 36–46 | PASS | Abstract matches the theorem and proof architecture. It correctly says seventeenth singular value, arbitrary rough independent laws, arbitrary signature/affine terms, and self-contained specialized inputs. |
| 47–61 | PASS | Main theorem and 33-direction corollary have consistent quantifiers. `s_j(A)` for symmetric `A` is the ordered absolute eigenvalue list. Essential-supremum and interval formulations are compatible. |
| 62–80 | PASS with prior-art GAP-PRESENTATION | Parameters and pivot/no-pivot architecture match later proof. The antecedent sentence citing only BCCT/RV is not false, but omits especially relevant LPP product-marginal work and Banks–Garza Vargas–Kulkarni–Srivastava quadratic-form anticoncentration. See source audit below. |
| 81–120 | PASS | Fourier convention, Gaussian transform, Plancherel `2pi`, inversion `(2pi)^-1`, Gaussian inversion coefficient, approximate-identity limit and weak identification of the density are consistent for rough laws. |
| 121–160 | PASS | Power-envelope integral is exact. Riesz half-potential Gamma representation, Gaussian inversion, Tonelli order and `1/sqrt(2pi)` coefficient reconstruct correctly; the `3/4` envelope gives weighted integral `12 sqrt(u)`. |
| 161–181 | PASS | Singular-value perturbation and rank inequalities use approximation numbers and therefore apply to nonsymmetric auxiliaries exactly as required later. |
| 182–207 | PASS | Invertible Schur proof via complementary compression of `A^-1` is correct. Singular case is valid by the ordered-singular-value moving-threshold argument proved above. |
| 208–217 | PASS | Strict row diagonal dominance proof is valid without symmetry. |
| 218–255 | PASS | Geometric rank-one Brascamp–Lieb heat-flow proof closes: frame contraction gives the sign; compact-time Gaussian tails justify differentiation/integration by parts; large-time scaling uses `sum c_i=d`; Lebesgue points + Fatou give the small-time limit; truncation handles general integrable inputs. |
| 256–282 | PASS | Product-projection density proof uses only deterministic orthogonal coordinates and never rotated independence. Zero `b_i` factors are safely dropped; for the remaining set `sum(1-b_i)<=d`, which suffices for the stated `e^(d/2)` bound. Full-dimensional case is separate. |
| 283–301 | PASS | Integrated Fourier powers: `|fhat|<=1` and `2m>=2` make the even power integrable; inversion at zero is legitimate; the signed projection has coefficient norm `sqrt(2m)`; constants yield `2pi sqrt(2e)/sqrt(p)`. Difference densities remain independent coordinatewise and cap one. |
| 302–324 | PASS | Cross-form decomposition includes arbitrary same-bank measurable phases. Decoupling conditions/integrates only genuine original product banks. Cauchy–Schwarz/Jensen powers 2 and 4 are correct; no moment assumptions enter. |
| 325–373 | PASS | Regularized determinant: exact frame from `H=alpha I+a^2 M^TM`; `c_j,d_i` lie in `[0,1]`; trace identity for `theta`; determinant Jacobian and one-dimensional rescalings are correct; scalar Fourier power uses `p=2/d_i>=2`; `d_i` factors cancel; `alpha=(2pi e)^2` cancels entropy; `a=2t` produces `t^2/(pi^2 e^2)`; fourth root gives exponent `-1/8`. |
| 374–400 | PASS | Cauchy–Binet expansion of crossing volumes is correct. Retaining the order-k term gives exponent `k/4`; `k=5` integrates by the power lemma and `k=3` integrates only after the Riesz weight, with displayed constants. |
| 401–422 | PASS | Scalar square profile and interval preimage length are correct; conditional profile is explicitly a measure domination, not an independence claim. |
| 423–434 | PASS | Definite two-coordinate pushforward: deterministic square completion/rotation and `(delta,theta)` Jacobian `1/(2 sqrt(|det B|))` yield `pi M/sqrt(|det B|)` without rotating the random product law. |
| 435–482 | PASS | Hyperbolic pair: two level-set branches, Jacobian, `ue^t+we^-t` decomposition, original-coordinate tail monotonicity, bathtub bound and middle interval length reproduce the logarithmic envelope. `Lambda>=2/sqrt(D)` has the correct inequality direction. Exceptional critical level is handled in test-function/Tonelli form. |
| 483–525 | PASS | Quarter-power concentration: diagonal case is immediate; fair sign split exposes a physical cross block with norm at least `L/4`; determinant theorem gives the `|t|^-1/4` bound; Gaussian smoothing and Gamma integral have correct exponents; layer cake gives `L0=4+4 log16`; atom exclusion follows. |
| 526–544 | PASS | Pivot-volume definition is precise about ordered disjoint sets. No-pivot principal 2x2 determinant condition implies the off-diagonal entry bound `<1/7` at the chosen `eta`. |
| 545–564 | PASS | Volume-sampled interpolation: bordered determinant identity is exact after sorting signs vanish on squaring; ordered extensions counted at most `(r+1)^2`; singular seeds correctly create an inequality rather than an equality; interpolation rows/columns and rank of `P` check. |
| 565–580 | PASS | Completion `A=D+R+E`: `E` is zero-diagonal and supported on `LxL`; `D` is diagonal and vanishes on `S union T`; `R_LL=P_LL`; support of `R-P` is rows `T` or columns `S`, giving global rank `<=3r`; restricted rank `<=r` is retained separately. |
| 581–619 | PASS | Spectral-to-volume proposition: ratio-drop selection is exhaustive. For `r=0`, operator norm is `<1`. For `1<=r<=4`, `||E||<=1/16`; global rank gives at least `m-3r>=r+1` large diagonal entries of `D`; seed vanishing puts them in `L`; the exact diagonal/off-diagonal bounds give strict dominance and contradict restricted rank. Nonsymmetric auxiliaries are handled by singular values, not eigenvalues. |
| 620–645 | PASS | Random physical cut probability for an ordered disjoint k-minor is exactly `4^-k`; order 3 and 5 consequences give `Z_k^-1/(2k)<=160`, full half potential `<200`, and continuous no-pivot density `<=800e<2400`. |
| 646–674 | PASS | Truncated potential definition is used consistently. Both singular integral estimates are valid; interval-overlap rearrangement for the log kernel is Tonelli-safe. |
| 675–714 | PASS | Pivot truncated-half-potential proposition: scalar pivot uses the valid Schur spectral survivor + quarter log potential; definite pair gives a uniform cap; indefinite pair integrates the hyperbolic log profile and uses `sup D^-1/2 log_+ D=2/e`. The constants are conservative. |
| 715–724 | PASS | `s_9` theorem correctly separates truncated pivot bound from no-pivot full half-potential bound; adding at most one outside `|Q-a|<=1` yields full half potential `<=601`. |
| 725–749 | PASS | Main normalized proof is exhaustive. No pivot `<2400`; scalar pivot leaves at least 16 spectral directions and uses the nine-direction full half potential; definite pair `<40`; indefinite pair leaves at least 15 directions, hence one for the log potential. All induced affine terms are permitted. General `K,s` scaling gives exactly `K^2/s`. |
| 750–779 | PASS | Threshold accounting accurately identifies order-five `5/4>1`, order-three `3/4>1/2` only after Riesz weight, and correctly disclaims `s_3` and optimality. Continuity is claimed only for no-pivot Fourier branch. |
| 780–790 | GAP-PRESENTATION, math PASS | Acknowledgment is nonmathematical. BCCT and RV citations are relevant but bibliography should use published versions and add LPP and Banks et al.; see exact recommendations below. No proof imports those sources, so theorem validity is unaffected. |

## Primary-source / prior-art verification

### 1. Bennett–Carbery–Christ–Tao

The cited arXiv preprint `math/0505065` is real and relevant. The published article is J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp–Lieb inequalities: finiteness, structure and extremals*, Geom. Funct. Anal. 17(5) (2008), 1343–1415, DOI `10.1007/s00039-007-0619-6`. The published abstract explicitly identifies heat-flow monotonicity as a main tool and discusses the rank-one heat-flow method. This is appropriate provenance for manuscript lines 218–255. The manuscript proves the exact geometric rank-one statement itself, so BCCT is attribution rather than a correctness dependency.

### 2. Rudelson–Vershynin

M. Rudelson and R. Vershynin, *Small ball probabilities for linear images of high-dimensional distributions*, International Mathematics Research Notices 2015(19), 9594–9617, DOI `10.1093/imrn/rnu243` (published online 4 Dec 2014). Their bounded-density projection theory is appropriate provenance for manuscript lines 256–301. In particular, their scalar normalized-sum theorem gives the sharper `sqrt(2)K` cap. The manuscript uses a weaker self-contained `sqrt(e)K` scalar constant, so it does not rely on importing the sharp theorem.

### 3. Livshyts–Paouris–Pivovarov — omitted directly relevant prior art

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216(2) (2016), 877–889, DOI `10.1007/s11856-016-1431-5`, arXiv:1507.07949. For a cap-one product density they prove the sharp dimension-k marginal bound `2^{k/2}`. This directly strengthens the manuscript's self-contained `e^{k/2}` projection bound and should be cited in a publication version. It does **not** by itself subsume the quadratic-form theorem.

### 4. Banks–Garza Vargas–Kulkarni–Srivastava — omitted quadratic-form anticoncentration prior art

J. Banks, J. Garza-Vargas, A. Kulkarni, N. Srivastava, *Overlaps, eigenvalue gaps, and pseudospectrum under real Ginibre and absolutely continuous perturbations*, Ann. Inst. H. Poincare Probab. Statist. 60(4) (2024), 2736–2766, DOI `10.1214/23-AIHP1400`, arXiv:2005.08930. Their Section 2 contains Theorem 2.1 explicitly titled “Density of Quadratic Forms.” It treats bilinear-affine matrix-valued forms

\[
X^T ZY+X^T U+V^T Y+W
\]

under independent bounded-density entries; Corollary 2.4 gives a scalar (`k=1`) bound in terms of geometric means of leading singular values. This is directly relevant prior art and should be discussed.

It does **not** directly imply the manuscript's determinant theorem or fixed-multiplicity theorem: after a physical cut the manuscript must retain arbitrary same-bank phases `F(X_I)+G(X_J)` coming from unrestricted within-bank quadratic terms. Those are absent from Theorem 2.1's bilinear-affine scope. Hence this is a bibliography/scope omission, not an exact prior solution.

### 5. Herry–Malicet–Poly — nearby but narrower

R. Herry, D. Malicet, G. Poly, *Regularity of laws via Dirichlet forms — Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488. Their setting assumes iid variables whose common law is representable as a sufficiently smooth function of a Gaussian field, and focuses on strong regularity/CLT regimes. Those assumptions are materially narrower than the present arbitrary non-iid coordinate densities bounded only in `L^infty`; it does not subsume the theorem.

### Literature conclusion

A targeted current primary-literature search did **not** locate a theorem matching all of the manuscript's simultaneous quantifiers: arbitrary non-iid density-capped coordinates, arbitrary real symmetric indefinite matrix and affine terms, and a fixed spectral-multiplicity hypothesis of the present kind. This statement is only a scope audit. **No novelty or priority claim is inferred from the search miss.**

## Threshold reduction: 17 is still the lowest rigorously certified value in this architecture

I found no full-hypothesis proof lowering 17 in this run. The obstruction can be stated exactly.

The determinant theorem gives from order-`k` crossing volume a large-frequency exponent `k/4`. Direct density inversion needs `k/4>1`, so order 5 is the first order this receiver can pay; order 4 is the endpoint `O(|t|^-1)` and is not absolutely integrable.

The algebraic volume proof, for order `k=5`, may select a ratio-drop index as large as `r=4`. The decomposition has global rank at most `3r`, while the final contradiction needs `r+1` large diagonal entries on the complement. Thus it requires

\[
m-3r\ge r+1\quad\Longleftrightarrow\quad m\ge4r+1.
\]

At `r=4`, this is exactly `m>=17`. For `m=16`, the present proof can force only four large diagonal entries after the global rank-12 correction, which is compatible with the restricted rank-four block. Therefore **17 is the exact limit of this proof mechanism**, not a claim of theorem-optimality.

The fresh B20 endpoint lemma further localizes the `s_16` unpaid case to rank-four-near crossing geometry plus a second physical crossing, but it still has an alignment/transversality obligation. I found no primary-source theorem that pays that geometry while retaining arbitrary same-bank quadratic phases. Banks et al. pays the bilinear-affine case but not those arbitrary phases. Thus I do not certify 16.

## Constant improvement already supported by the written proof

Keeping the exact scalar-pivot half-potential constant instead of rounding to 600 gives

\[
H(Q)\le 10(20+12\log16)=200+120\log16
\]

in the worst pivot branch; the definite/indefinite alternatives and no-pivot `s_9` bound are smaller. Hence

\[
\sup_a E|Q-a|^{-1/2}\le201+120\log16.
\]

At the main scalar pivot, multiplication by `eta^-1/2=10` gives

\[
\boxed{\|p_Q\|_\infty\le (2010+1200\log16)K^2/s}
\]

with

\[
2010+1200\log16=5337.106466687737\ldots<5338.
\]

All other final branches are smaller (`800e≈2174.63`, definite pair `<40`, indefinite pair `<251`). This is a rigorous constant tightening with every law/matrix/affine hypothesis unchanged. It was already identified in my earlier B18 run; this run independently rechecked the arithmetic and does not present it as new relative to that earlier artifact.

## Support-file audit

- `proof_map.csv`: PASS as a source-navigation map; listed theorem/proof ranges agree with the 790-line source.
- `SOURCE_MANIFEST.json`: PASS as metadata; source blob/SHA/bytes/line count agree with the current objective and README.
- `verify.py`: PASS as a finite diagnostic script. Its exact tests cover interpolation/rank/support identities and rational diagonal-dominance slack; its Schur/graph tests are explicitly floating diagnostics. It correctly refuses a manuscript whose SHA-256 differs from the pinned source.
- `checks.json`: PASS as an execution receipt for that script, not a proof certificate. Recorded counts match the current `DELIVERY_STATUS.md`.
- Historical `AUDIT.md`: informational only. Its old finite-test counts are explicitly not reproduced by the new suite.

## Validation gate and next obligation

This B18 run is a complete source/prior-art reconstruction and now returns mathematical PASS on the pinned 17-direction theorem. It is not a second independent B18 reviewer; it corrects the same slot's earlier mistaken GAP. A distinct B20 reconstruction also reports PASS, but release/independent-validation status should be assigned only after the designated release gate reconciles all current reports and the presentation/prior-art patch. The next mathematical obligation for a genuine threshold reduction is a self-contained endpoint receiver or transversality lemma that closes the `s_16` rank-four-plus-second-crossing chamber while preserving arbitrary same-bank quadratic phases and all rough-law hypotheses.

Execution: `WITHOUT_VERIFIED_BRAIN`. Model/effort metadata: `UNKNOWN` unless platform-exposed separately. No email/push, task creation/restart, cadence/state change, cross-account authentication, paid call, public release, or permission change was performed.