# fleet02/B13 independent end-to-end audit — definite pairs / hyperbolic envelope

Run: `20260924T115708Z-fleet02-B13-fixed-mult-audit-r13`

Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Pinned manuscript source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Initial manuscript source commit recorded by the objective: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
Fresh master source used for the complete read: `620e2b9d6d38d697332101394c0199d1a608bc06`; a final refresh at `614cd0abd083dc8e2c06c70b70d1e1a60efd2268` still had the same manuscript blob.
Source SHA-256 recorded by the manuscript package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**Mathematical verdict: PASS, end-to-end for the written 17-eigenvalue candidate.** I read the complete 790-line `manuscript.tex` and independently reconstructed the main analytic and algebraic chains. I found no fatal mathematical gap in the statement

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for independent coordinate densities bounded by `K`.

This is one independent audit, not a self-awarded independently-validated release status. The current objective requires two genuinely separate complete reviews before such a status.

**Package verdict: GAP (reproducibility metadata only).** Current `README.md` and `AUDIT.md` name `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but all four were absent at the pinned/current manuscript root when fetched in this run. I therefore did not rely on the claimed finite checker. The full proof itself is present in `manuscript.tex`, so this does not create a mathematical gap in the argument audited here.

## End-to-end statement/line audit

### Lines 1–83: theorem, quantifiers, normalization, architecture — PASS

The theorem retains arbitrary dimension, signature, remaining spectrum, affine terms, and arbitrary independent rough coordinate laws. The normalization `Y=KX`, `A -> A/s`, followed by `\widetilde Q=(K^2/s)Q`, correctly returns the factor `K^2/s`. No support, moment, log-concavity, or post-rotation independence hypothesis is introduced.

### Lines 84–160: Fourier inversion, power envelope, Riesz half-potential — PASS

The Gaussian normalization is consistent with the stated Fourier convention. Plancherel and inversion are obtained through Gaussian regularization without assuming a priori regularity of the pushforward. The identity

\[
|z|^{-1/2}=\Gamma(1/4)^{-1}\int_0^\infty v^{-3/4}e^{-vz^2}\,dv
\]

and the subsequent Tonelli calculation give exactly the coefficient `1/sqrt(2*pi)` in the Fourier half-potential bound. For the `3/4` envelope the weighted integral is `12 sqrt(u)`, yielding the displayed constant.

### Lines 161–220: singular values, Schur spectral count, diagonal dominance — PASS

The nonsymmetric perturbation inequalities use singular values, not eigenvalues. The Schur count is valid: for invertible `A`, `S^{-1}` is a principal compression of `A^{-1}`; positive and negative interlacing separately imply that the compression cannot have more eigenvalues with absolute value `>1/t`, which is equivalent to `N_S(t)>=N_A(t)-k`. The singular case follows by `A+eps I` and continuity at the weakened threshold. Strict row diagonal dominance is used in its valid nonsymmetric form.

### Lines 221–300: geometric Brascamp–Lieb, projection density, scalar Fourier powers — PASS

For the heat-flow proof, direct differentiation gives

\[
\partial_tF-\Delta F
=F\Big(\sum_i c_i v_i^2-|\sum_i c_i u_i v_i|^2\Big)\ge0
\]

because the frame matrix is a contraction. Compact-support heat tails justify integration by parts, and the large-time Gaussian limit has the correct frame exponent `sum c_i=d`. The projection lemma never declares rotated variables independent: it integrates the original product density over orthogonal fibers and applies the geometric inequality. The scalar Fourier-power estimate is noncircular because `|hat f|^{2m}` is integrable already from Plancherel (`|hat f|<=1`), so inversion at zero is legitimate before invoking the projection density bound.

### Lines 301–400: decoupling, regularized determinant, volume envelopes — PASS

The fourth-power decoupling follows from Cauchy–Schwarz and Jensen, with the difference variables still independent and cap one. In the regularized graph inequality, the frame weights

\[
c_j=\alpha e_j^TH^{-1}e_j,\qquad d_i=a^2m_i^TH^{-1}m_i
\]

sum correctly, and the scalar Fourier factors cancel the `d_i` powers. The entropy estimate contributes `e^{theta/2}`; with `alpha=(2*pi*e)^2` this exactly cancels the remaining scale. Taking fourth roots yields

\[
|\phi_Z(t)|\le\det\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

Cauchy–Binet then gives the `k=5` density envelope `5e Z_5^{-1/10}` and the `k=3` negative-half-moment envelope with the stated constants.

### Lines 401–428: scalar square and definite physical pair — PASS

The scalar-square density is a two-branch change of variables and remains a conditional domination statement, not an independence assertion. For a definite symmetric `2x2` block, completing the square and orthogonally diagonalizing is only a deterministic change of variables in the two-dimensional integral. The joint density cap survives under the Jacobian-one orthogonal map; integrating the elliptic angle with Jacobian `1/(2 sqrt(|det B|))` gives

\[
\|p_q\|_\infty\le \pi M/\sqrt{|\det B|}.
\]

### Lines 429–484: hyperbolic pair — PASS, including the delicate tails

For `B` with eigenvalues `mu_+>0>-mu_-`, the map

\[
w_\epsilon(t)=\epsilon\sqrt{\delta/\mu_+}\cosh t\,e_+
+\sqrt{\delta/|\mu_-|}\sinh t\,e_-
\]

has absolute `(delta,t)` Jacobian `1/(2 sqrt D)`, `D=|det B|`. Writing a branch as `u e^t+w e^{-t}` gives `|u|=|w|=sqrt(delta Lambda)/2`. Some original coordinate obeys `|u_i|>=|u|/sqrt2`; for `t>=(3/4)log2`, the growing term dominates the decaying term by a factor at least two, so the chosen original-coordinate function is one-sign monotone and `|y_i'(t)|>=|y_i(t)|/3`. The cap-one/mass-one condition then gives a tail integral at most `3 log 2`. The negative tail is identical after choosing (possibly a different) original coordinate for `w`; no same-coordinate assumption is needed. The two cutoffs have the displayed logarithmic bound, and `Lambda>=2/sqrt D` yields

\[
p_q(z)\le D^{-1/2}\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right).
\]

The proof is valid for rough densities because the coarea/change-of-variables statement is used against nonnegative test functions; exceptional critical levels are not selected after conditioning.

### Lines 485–530: quarter-power concentration and logarithmic potential — PASS

If no large diagonal exists, random sign splitting produces a physical cross block with norm at least `||S||/4`. Keeping one singular factor in the already-proved determinant theorem gives the `|t|^{-1/4}` envelope. Gaussian smoothing with `v=1/8` has coefficient

\[
2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)<16,
\]

so the small-ball bound is valid. Layer cake then gives `4+4 log 16`. This supplies exactly the logarithmic integrability needed by the indefinite-pair branch.

### Lines 531–584: ordered disjoint-minor sampling and nonsymmetric completion — PASS

The sampling identity is correctly an inequality: singular seeds can have nonsingular extensions, so each `(r+1)` extension is counted at most `(r+1)^2` times. `P=A[:,T]B^{-1}A[S,:]` may be nonsymmetric, but agrees on rows `S` and columns `T`. In the completion, `R-P` is supported in rows `T` or columns `S`, giving the global `rank R<=3r`, while `R[L,L]=P[L,L]` gives the sharper restricted rank `<=r`. `D` vanishes on the seed exactly.

### Lines 585–652: spectral-to-volume conversion, cut, no-pivot consequences — PASS

For a bad ratio, `||E||_F<=(r+1)/80<=1/16`. Singular-value perturbation and global rank force `r+1` diagonal entries of `D` of modulus at least `1-epsilon`, all in the seed complement. On that set,

\[
|R_{ii}|\ge371/400,\qquad
\sum_{j\ne i}|R_{ij}|<23/28,
\]

so the restricted block is invertible of rank `r+1`, contradicting `rank R[L,L]<=r`. The fair cut retains each ordered disjoint pair with probability `4^{-k}`. The resulting `k=3` and `k=5` constants are arithmetically correct.

### Lines 653–726: singular kernels, pivot half-potential, nine-direction receiver — PASS

The kernel `J(d)` split produces the claimed constant and logarithm. In the scalar-pivot branch, the Schur remainder has one surviving unit-scale eigenvalue, so the quarter-power lemma excludes an atom and controls the logarithmic expectation. Definite and indefinite pair pivots are averaged through the previously checked conditional envelopes. The distinction between truncated and full half potentials is handled explicitly: outside `|Q-a|<=1`, the kernel is at most one, so `H<=600` becomes the full bound `<=601`.

### Lines 727–790: main theorem, scaling, limitations — PASS

The no-pivot, scalar-pivot, definite-pair, and indefinite-pair cases exhaust the proof. A scalar pivot from `s_17>=1` leaves at least sixteen unit-scale Schur eigenvalues, more than the nine needed. An indefinite pair leaves at least fifteen, and only one is used for logarithmic averaging. The normalized largest branch is `6010<10000`. The final scaling is correct. The manuscript accurately does not claim the three-eigenvalue theorem or continuity in branches where only measure domination was proved.

## B13 adversarial stress test: the logarithm is genuinely necessary

Status: **PASS / SHARPNESS OBSTRUCTION**, not a QFORM counterexample.

Let `X,Y` be independent uniform variables on `[-1/2,1/2]` and

\[
Q=X^2-Y^2=(X-Y)(X+Y).
\]

With `U=X-Y`, `V=X+Y`, the joint density of `(U,V)` is `1/2` on the diamond `|U|+|V|<=1`. Therefore, for `0<|z|<1/4`,

\[
 p_Q(z)
 =\log\frac{1+\sqrt{1-4|z|}}{1-\sqrt{1-4|z|}}.
\]

Indeed, for `z>0`, the product-density formula gives

\[
p_Q(z)=\int_{u_-}^{u_+}\frac{du}{u},\qquad
u_\pm=\frac{1\pm\sqrt{1-4z}}2,
\]

and symmetry handles `z<0`. Hence `p_Q(z)=\log(1/|z|)+O(1)` as `z->0`. Thus a determinant-only **bounded conditional density** for an indefinite physical pair is false even for compact interval product laws. The manuscript's logarithmic envelope has the correct singularity order; the subsequent averaging against a surviving Schur direction is essential.

## New target-level implication extracted from the audited pair proof

The pair argument is stronger than its use inside the 17-eigenvalue theorem.

Let the original target hypothesis `s_3(A)>=1` hold and let `B=A[{i,j},{i,j}]` be any invertible physical principal pair with `D=|det B|`. If `B` is definite,

\[
\|p_Q\|_\infty\le \pi D^{-1/2}.
\]

If `B` is indefinite, the two-coordinate Schur complement retains at least one eigenvalue of modulus at least one by the audited Schur-count lemma. Its arbitrary-affine quadratic remainder therefore satisfies the quarter-power logarithmic bound. Averaging the hyperbolic envelope gives

\[
\|p_Q\|_\infty
\le D^{-1/2}\left(6+\log_+(16\sqrt D)+4+4\log16\right).
\]

Using

\[
\log_+(16\sqrt D)\le\log16+\tfrac12\log_+D,
\qquad
\sup_{D>0}D^{-1/2}\log_+D=2/e,
\]

we obtain the uniform determinant-only estimate

\[
\boxed{
\|p_Q\|_\infty
\le C_{\rm pair}D^{-1/2}+e^{-1},
\qquad
C_{\rm pair}=10+5\log16=23.8629436111989\ldots .
}
\]

Consequently every slab witness of ratio `rho>1/e` under the exact three-eigenvalue target satisfies, for **every** physical pair,

\[
\boxed{
|A_{ii}A_{jj}-A_{ij}^2|
\le
\left(\frac{C_{\rm pair}}{\rho-e^{-1}}\right)^2.
}
\]

Singular pairs satisfy this trivially. This is a genuine original-coordinate obstruction: high output density forces all physical principal two-volume to collapse at rate `O(rho^{-2})`. It uses no moments, support bound, log-concavity, rotated independence, or continuity assumption.

## Application to the latest completed designated partner fleet03/B13 r50

Partner r50 (`5ee01246ea47b42ea88c89f54c33e7520883ea21`) starts its non-ultracollapse packet with an **indefinite original-coordinate pair** satisfying

\[
D_B\ge D_0=1001/12544.
\]

The determinant-only receiver above immediately gives

\[
\rho\le
\frac{C_{\rm pair}}{\sqrt{D_0}}+\frac1e
=84.8422567126\ldots .
\]

Thus r50's subsequent heavy-Schur analysis, which is entered only for `rho>209.078`, is not needed in this packet if the audited manuscript pair lemmas are accepted: the physical pair already pays the density before any heavy-row deletion. This is an equation-level use of the newest compatible designated-partner result and a simplification of that branch, not a claim that the unrestricted three-eigenvalue conjecture is solved.

## Required pinned Fourier source applied to a real manuscript inequality

The owner-pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` proves the unconditional fifth-volume receiver

\[
\|p_Q\|_\infty\le5\sqrt{2e}\,Z_5^{-1/10}
\]

for every physical cross block, with no marginal condition. In the manuscript no-pivot `s_17>=1` branch, `V_5>=kappa^5` and the random cut gives `Z_5>=4^{-5}kappa^5`; hence

\[
Z_5^{-1/10}\le2\kappa^{-1/2}=160
\]

and therefore independently

\[
\boxed{
\|p_Q\|_\infty\le800\sqrt{2e}
=1865.31518528\ldots .
}
\]

This is a direct source-pinned cross-check, and slightly improves the manuscript's self-contained no-pivot constant `800e=2174.625...`; it does not change the final `10000` constant because the scalar-pivot branch remains larger.

The same pinned counterexample-search report found no growing tested family, but none of those numerics is used as proof here.

## Threshold reduction status

No complete reduction of the manuscript's global threshold `17` is established here. The B13 pair branch itself needs only the exact target `s_3>=1`, but the current no-pivot order-five branch still invokes `s_17`. Lowering the fixed multiplicity therefore still requires new information in the no-pivot structural route (in particular the terminal order-five bad-ratio chamber), not a change to the pair analysis.

## First unpaid implication

`QFORM-PAIRDET-COLLAPSE-TO-NOPIVOT-RECEIVER-v1`: combine the new all-pairs determinant collapse

\[
\max_{i<j}|A_{ii}A_{jj}-A_{ij}^2|=O(\rho^{-2})
\]

with the no-pivot/minor-sampling structure at the exact `s_3>=1` target, without turning a small coefficient into a small random quadratic perturbation. Either extract a dimension-free physical crossing/aggregation receiver from this quantitative near-rank-one principal geometry, or construct a genuine cap-one product counterexample satisfying the collapse on every physical pair.
