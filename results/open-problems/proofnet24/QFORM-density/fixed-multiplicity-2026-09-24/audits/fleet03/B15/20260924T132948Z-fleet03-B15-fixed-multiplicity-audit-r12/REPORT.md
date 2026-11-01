# fleet03/B15 r12 — full fixed-multiplicity audit and regularity synthesis

Run: `20260924T132948Z-fleet03-B15-fixed-multiplicity-audit-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Owner-pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Baseline SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## Verdict

**PASS RECONFIRMED for the written 17-eigenvalue theorem.** I reread the complete 790-line pinned manuscript in this invocation and found no fatal mathematical defect in the claim

\[
s_{17}(A)\ge s>0
\Longrightarrow
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary dimension, arbitrary real symmetric signature and remaining spectrum, arbitrary deterministic affine terms, and arbitrary independent coordinate densities bounded by `K`.

This remains an independent worker audit, not formal verification or a release certificate. The unrestricted three-eigenvalue conjecture remains **OPEN**.

The previously reported repository-package gap is now **resolved**: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are present on current master. `checks.json` records PASS for the new scoped reproducibility suite (534 exact interpolation seeds, 18 volume-sampling cases, 240 numerical Schur threshold cases, and 30 graph-weight cases). Those finite checks do not replace the analytic proof.

One nonfatal wording issue remains in the product-projection lemma. After rows with `b_i=0` are dropped, the displayed equality `sum_i(1-b_i)=d` is unambiguous only if the sum is understood over **all** original indices. If it is read over retained `b_i>0` indices, it should be `<=d`. The required upper bound `p(y)<=e^{d/2}` and every downstream constant are unchanged.

## Full line-range audit ledger

- **Lines 1–90 — PASS.** Statement, all quantifiers, normalization plan, pivot/no-pivot architecture, and the distinction between essential boundedness and continuity are consistent.
- **Lines 91–160 — PASS.** Gaussian regularization, Plancherel normalization, inversion, power-envelope integration, and the Riesz half-potential constant were independently recomputed. In particular
  \[
  \mathbb E|Z-a|^{-1/2}
  \le(2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|dt.
  \]
- **Lines 162–220 — PASS.** Singular-value perturbation/rank inequalities, principal-pivot Schur spectral count (including the singular limiting argument), and strict diagonal dominance are correct.
- **Lines 221–255 — PASS.** The geometric rank-one Brascamp–Lieb heat-flow proof has the correct sign, frame normalization, large-time Gaussian limit, and monotone-convergence closure.
- **Lines 256–309 — PASS WITH WORDING ISSUE ABOVE.** Product projection and integrated scalar Fourier powers retain original-coordinate product structure. No post-rotation independence is asserted.
- **Lines 310–400 — PASS.** Decoupling powers two/four, graph weights, regularizer `alpha=(2*pi*e)^2`, determinant exponent `-1/8`, Cauchy–Binet crossing volumes, and the `k/4` Fourier exponent all check.
- **Lines 401–527 — PASS.** Scalar square domination, definite pair, hyperbolic pair, and quarter-power concentration are valid as measure-domination/test-function arguments for rough laws. Exceptional fibers are not used pointwise.
- **Lines 528–620 — PASS.** Ordered disjoint-minor sampling, nonsymmetric interpolation, `rank R<=3r`, restricted `rank R[L,L]<=r`, zero diagonal error, and the diagonal-dominance contradiction are consistent. The `4r+1` count is used correctly.
- **Lines 621–651 — PASS.** Random cut gives `4^{-k}` exactly. For `k=3`, `Z_3^{-1/6}<=160` yields `12 sqrt(80e)<200`; for `k=5`, `Z_5^{-1/10}<=160` yields `800e<2400`.
- **Lines 652–715 — PASS.** Singular kernels, truncated half-potential bookkeeping, and all scalar/definite/indefinite pivot alternatives are consistent. The manuscript does not confuse truncated and full half potentials.
- **Lines 716–790 — PASS.** The nine-eigenvalue full half-potential step, all final branches, scale restoration `Y=KX`, and theorem limitations are correct. The largest displayed final branch remains `6010<10^4`.

## B15 regularity conclusion beyond the baseline manuscript

The baseline source deliberately states only an essentially bounded density globally. Completed fleet work gives a stronger **fleet-level corollary** without changing the height constant.

A previously completed fleet03/B15 theorem (`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260924T092642Z-fleet03-B15-qform-auto11/REPORT.md`) proves that for every fixed symmetric `A` with `rank(A)>=3`, arbitrary affine `b,c`, and arbitrary cap-one product inputs, the affine quadratic output has a canonical density in `C_0(R) cap L^infinity(R)`. Since `s_17(A)>=s>0` implies `rank(A)>=17`, combine that fixed-instance continuity theorem with the manuscript's interval domination. Continuity then turns the almost-everywhere height bound into the same pointwise bound:

\[
\boxed{
 p_Q\in C_0(\mathbb R),\qquad
 \|p_Q\|_\infty\le10^4K^2/s.
}
\]

Thus the current 17-eigenvalue candidate can be strengthened at fleet level to a **continuous density with no loss in the universal constant**. This is not yet a self-contained amendment of the 790-line manuscript unless the fixed-instance affine `C_0` theorem is imported or reproved there.

### Designated partner applied to an actual inequality

The completed fleet04/B15 same-constant compiler (`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260923T221909Z-fleet04-B15-ruled-trace-c0-r8/REPORT.md`, Theorem 6.1) says: for a fixed rank-at-least-three homogeneous quadratic target, any separately paid interval estimate `P(Q in I)<=M|I|` upgrades to its canonical `C_0` representative with the **same** height `M`.

Apply it to the actual homogeneous specialization of the audited theorem. In normalized variables `Y=KX`, `A'=A/s`, the manuscript gives

\[
\Pr\{Y^TA'Y\in I\}\le10^4|I|.
\]

The partner theorem therefore yields

\[
p_{Y^TA'Y}\in C_0,\qquad \|p_{Y^TA'Y}\|_\infty\le10^4.
\]

Scaling back gives exactly

\[
\boxed{
 p_{X^TAX}\in C_0,\qquad
 \|p_{X^TAX}\|_\infty\le10^4K^2/s.
}
\]

The affine conclusion above is supplied separately by the completed affine fixed-instance theorem plus the manuscript's affine interval bound; no unsupported affine extension of the partner theorem is asserted.

## Thirteen-direction endpoint: new B15 quantitative supplement

The current order-four endpoint is not enough for a universal `L^infinity` theorem, but it does give a stronger half-potential estimate than the order-three route in the no-pivot chamber.

Assume normalized cap-one inputs, arbitrary affine terms, no `eta=1/100` pivot, and `s_13(A)>=1`. Proposition `prop:volume` with `k=4` and the random cut supply a physical crossing block `M` such that

\[
Z_4(M)^{-1/8}\le160.
\]

Put

\[
u=\pi e Z_4(M)^{-1/8}\le160\pi e.
\]

The audited determinant theorem gives the critical envelope

\[
|\phi_Q(t)|\le\min(1,u/|t|).
\]

Insert this envelope directly into the audited Riesz inequality. The weighted integral is exact:

\[
\begin{aligned}
\int_{\mathbb R}|t|^{-1/2}|\phi_Q(t)|dt
&\le 2\int_0^u t^{-1/2}dt
  +2u\int_u^\infty t^{-3/2}dt\\
&=8\sqrt u.
\end{aligned}
\]

Hence

\[
\boxed{
\sup_a\mathbb E|Q-a|^{-1/2}
\le8\sqrt{u/(2\pi)}
\le8\sqrt{80e}
=117.9728907915\ldots<118.
}
\]

This is a genuine quantitative improvement over the manuscript's `<200` no-pivot half-potential constant when thirteen directions are available. It does **not** produce a universal density height at thirteen directions: an `O(1/|t|)` Fourier envelope plus finite half-potential can still coexist with logarithmic density singularities.

A fresh fleet03/B01 improvement on current master proves the complementary endpoint statement: under `s_13>=1` every finite `L^q` norm is universally controlled, with the no-pivot bound

\[
\|p_Q\|_q\le(160e\,q)^{1-1/q},\qquad 2\le q<\infty,
\]

and interval concentration `O(|I|\log(1/|I|))`. Combining that result with the completed fixed-matrix affine `C_0` theorem gives the precise regularity picture at thirteen directions:

\[
\boxed{
 p_Q\in C_0(\mathbb R)\cap\bigcap_{2\le q<\infty}L^q(\mathbb R),
}
\]

with universal finite-`q` bounds but only a matrix-dependent `L^infinity` bound currently known. The unresolved `17 -> 13` step is therefore **uniformity at the critical endpoint**, not density existence or qualitative continuity.

## Threshold status

The strongest new route inspected in this invocation is the leverage-interpolated determinant theorem from fleet01/B04. It proves a genuine thirteen-direction `L^infinity` bound whenever the order-four volume-producing cut has maximum physical row leverage `h<1`, with explicit constant blowing up as `h->1`. This isolates the remaining high-leverage chamber. No source currently supplies the missing uniform high-leverage receiver, so I do **not** certify a multiplicity below seventeen.

The full three-eigenvalue conjecture remains **OPEN**.
