SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-23T10:28:39Z.
attacking: the ultra-near heavy-null overlap endpoint — prune large-slope mixed leaves without losing the third active direction, then expose the exact linear-shear product factorization that must replace false conditional independence.

# fleet01/B05 r30 — cube-root overlap pruning and the exact linear-shear endpoint interface

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / interval bound, preserving arbitrary product densities  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_REDUCTION_PROVED / PRECISE_MISSING_FACTOR_SHARPENED / FULL_QFORM_OPEN`  
**Continuity:** not proved by the new reduction; the partner Fresnel collar quoted below has a bounded continuous density, but full-target continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

## 1. Scope and the first unpaid implication

The current B05 survivor is the exact-rank-three indefinite heavy-null branch.  Write

\[
A=RBR^\top,\qquad R^\top R=I_3,\qquad s_{\min}(B)\ge1,
\]

choose a physical heavy row `h`, and rotate only the deterministic three-dimensional active coefficient space so that

\[
r_h=\sqrt c\,e_1,\qquad c>127/128,
\]

and, in the physical-null subbranch,

\[
r_h^\top B r_h=0.
\]

As in the completed B05 normal forms, a transverse rotation gives

\[
B=\begin{pmatrix}
0&\beta&0\\
\beta&\alpha&\delta_0\\
0&\delta_0&\gamma
\end{pmatrix},
\qquad |\beta|\ge1,
\]

with the remaining rows written

\[
r_j=(u_j,w_j,z_j),\qquad j\ne h.
\]

Put

\[
\rho:=1-c<1/128.
\]

Parseval gives the exact identities

\[
\sum_{j\ne h}u_j^2=\rho,\quad
\sum_{j\ne h}\binom{w_j}{z_j}(w_j,z_j)=I_2,\quad
\sum_{j\ne h}u_j(w_j,z_j)=0. \tag{1.1}
\]

No probabilistic assumption beyond the original independent cap-one coordinates is used below.

The preceding fleet01/B05 r29 paid the whole collar `rho>=1/128` in the normalized spread branch and left precisely the punctured endpoint `rho downarrow0`.  The purpose of this run is to determine how much of the same-coordinate overlap can be conditioned away *without paying a reciprocal tiny determinant*, and to write the surviving dependence in a form that retains the original product provenance exactly.

## 2. Latest fleet02/B05 result applied to the current branch

The newest completed fleet02/B05 report available at refresh is

`yspennstate/math-open-problems`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T092247Z-fleet02-B05-QFORM-r19/REPORT.md`,

theorem `QFORM-EXACTRANK3-LEAVEONEOUT-FRESNEL-v1`.

For the heavy row `h`, its leave-one-out Gram is exactly

\[
H_h=I-r_hr_h^\top=\operatorname{diag}(\rho,1,1),\qquad \det H_h=\rho. \tag{2.1}
\]

Hence its normalized leaf leverage is

\[
\ell_j^{(-h)}=r_j^\top H_h^{-1}r_j
=\frac{u_j^2}{\rho}+w_j^2+z_j^2. \tag{2.2}
\]

The current r29 normalized-light survivor assumes exactly

\[
\ell_j^{(-h)}\le\frac12\qquad(j\ne h). \tag{2.3}
\]

Therefore fleet02/B05 r19 applies with no change of variables or probabilistic relaxation and gives the actual inequality

\[
\boxed{
\|p_Q\|_\infty
\le 12\,[|\det B|\rho]^{-1/3}
\le 12\rho^{-1/3}.}
\tag{2.4}
\]

This branch has a bounded continuous density because the partner proof produces an `L^1` characteristic function.  At `rho=1/128`, (2.4) is `<60.477`; it worsens as `rho downarrow0`, so it is a correct control rather than the desired endpoint stability.

This is the required equation-level use of a completed fleet02/B05 result.

## 3. Cube-root overlap pruning

The next lemma does not require the spread condition (2.3).

### Lemma 3.1 — `QFORM-CUBEROOT-OVERLAP-PRUNING-v1`

Let `0<rho<1`, and suppose the residual rows satisfy (1.1).  Set

\[
\eta:=\rho^{1/3}
\]

and define the large-slope original-coordinate set

\[
H_\eta:=\left\{j\ne h:\ |u_j|>\eta\sqrt{w_j^2+z_j^2}\right\}. \tag{3.1}
\]

Let

\[
K_\eta:=\sum_{j\in H_\eta}r_jr_j^\top.
\]

Then

\[
\boxed{\|K_\eta\|_{\rm op}\le\operatorname{tr}K_\eta\le\eta+\eta^3.} \tag{3.2}
\]

Consequently, after conditioning the original coordinates in `H_eta`, the surviving active Gram matrix

\[
G_\eta:=I_3-K_\eta
\]

satisfies

\[
\boxed{G_\eta\succeq(1-\eta-\eta^3)I_3,} \tag{3.3}
\]

while every surviving mixed row obeys the pointwise graph estimate

\[
\boxed{|u_j|\le\eta\sqrt{w_j^2+z_j^2}.} \tag{3.4}
\]

For `rho<=1/128`,

\[
\eta\le0.198425132,\qquad
1-\eta-\eta^3\ge0.793762368. \tag{3.5}
\]

#### Proof

By definition of `H_eta`,

\[
w_j^2+z_j^2<\eta^{-2}u_j^2\qquad(j\in H_\eta).
\]

Therefore

\[
\sum_{j\in H_\eta}(w_j^2+z_j^2)
\le \eta^{-2}\sum_{j\in H_\eta}u_j^2
\le \eta^{-2}\rho
=\eta.
\]

Also `sum_{H_eta}u_j^2<=rho=eta^3`.  Since `K_eta` is positive semidefinite,

\[
\|K_\eta\|_{\rm op}\le\operatorname{tr}K_\eta
=\sum_{j\in H_\eta}(u_j^2+w_j^2+z_j^2)
\le\eta^3+\eta.
\]

This proves (3.2), hence (3.3).  Equation (3.4) is simply the complement of (3.1).  QED.

### Why the cube-root scale is useful

The more general deterministic tradeoff is

\[
H_\tau:=\{j:|u_j|>\tau\|(w_j,z_j)\|\}
\quad\Longrightarrow\quad
\|K_\tau\|_{\rm op}\le \rho+\rho/\tau^2. \tag{3.6}
\]

Choosing `tau=rho^(1/3)` balances the retained pointwise overlap `tau` against the active-Gram loss `rho/tau^2`; both tend to zero at the same cube-root scale.  Thus the ultra-near-coloop branch can be reduced, by conditioning only original independent coordinates, to a *pointwise vanishing graph perturbation* of the source-separated endpoint while losing only `O(rho^(1/3))` of the active Gram.

## 4. Whitening preserves three-dimensional curvature and the null heavy row

Let `S` denote the heavy row together with the leaves not conditioned in `H_eta`, and let `R_S` be their row matrix.  Then

\[
R_S^\top R_S=G_\eta.
\]

Set

\[
\widetilde R=R_SG_\eta^{-1/2},\qquad
\widetilde B=G_\eta^{1/2}BG_\eta^{1/2}. \tag{4.1}
\]

Then `widetilde R^T widetilde R=I_3` and the conditioned homogeneous quadratic matrix is exactly

\[
R_SBR_S^\top=\widetilde R\widetilde B\widetilde R^\top. \tag{4.2}
\]

Because singular values are submultiplicative under congruence,

\[
\boxed{s_{\min}(\widetilde B)
\ge\lambda_{\min}(G_\eta)s_{\min}(B)
\ge1-\eta-\eta^3.} \tag{4.3}
\]

The heavy physical pivot remains exactly zero:

\[
\widetilde r_h^\top\widetilde B\widetilde r_h
=r_h^\top Br_h=0. \tag{4.4}
\]

Its whitened leverage is

\[
\widetilde c
=\|r_hG_\eta^{-1/2}\|^2
=c\,e_1^\top G_\eta^{-1}e_1
\ge c, \tag{4.5}
\]

because `G_eta<=I`.  Since `widetilde R` is an orthonormal-column frame, `widetilde c<=1`.  Hence the residual leakage after whitening satisfies

\[
\boxed{1-\widetilde c\le1-c=\rho.} \tag{4.6}
\]

So the pruning operation does not trade the ultra-near heavy row for a poorly conditioned three-dimensional core: it preserves all three active directions at a universal scale and can only make the heavy leverage closer to one.

Conditioning generates affine terms, but the quadratic statements (4.2)--(4.6) are exact and the existing B05 receivers allow arbitrary affine terms at their stated scopes.

## 5. Endpoint control supplied by the completed partner theorem

The pruning lemma also gives a quantitative consistency check against the completed source-separated endpoint.  Suppose that after conditioning `H_eta` the surviving rows have **zero** longitudinal overlap, `u_j=0` for every surviving leaf.  Then the conditioned homogeneous form is source-separated: one physical heavy scalar versus a transverse product pair.

The completed fleet02/B05 support-separated theorem (`QFORM-HEAVY-ROW-SUPPORT-SEPARATED-CLOSURE-v1`) gives `<248` when the active spectral scale is at least one.  By scaling and (4.3), here it yields uniformly in the conditioned values

\[
\boxed{
\|p_{Q\mid X_{H_\eta}}\|_\infty
<\frac{248}{1-\eta-\eta^3}.}
\tag{5.1}
\]

Averaging the conditioning preserves the same bound.  For `rho<=1/128`,

\[
\frac{248}{1-\eta-\eta^3}<312.44. \tag{5.2}
\]

Thus the exact graph endpoint is already uniformly paid even after the pruning operation.  What remains is stability for nonzero graph slope tending to zero, not recovery of lost third curvature.

## 6. Exact triangular shear: the dependence is linear, not arbitrary

The homogeneous heavy-null form before pruning is

\[
Q
=2\beta\sqrt c\,X_hL
+2\beta UL
+\alpha L^2+2\delta_0LV+\gamma V^2, \tag{6.1}
\]

where

\[
U=\sum_{j\ne h}u_jX_j,\quad
L=\sum_{j\ne h}w_jX_j,\quad
V=\sum_{j\ne h}z_jX_j. \tag{6.2}
\]

Define the triangularly sheared hub variable

\[
Y_h:=X_h+\frac{U}{\sqrt c}. \tag{6.3}
\]

Then, **exactly**,

\[
\boxed{
Q
=2\beta\sqrt c\,Y_hL
+\alpha L^2+2\delta_0LV+\gamma V^2.}
\tag{6.4}
\]

The Jacobian of `(x_h,x') -> (y_h,x')` is one.  Therefore the joint density in the new coordinates is

\[
g(y_h,x')
=f_h\!\left(y_h-\frac{U(x')}{\sqrt c}\right)
\prod_{j\ne h}f_j(x_j). \tag{6.5}
\]

This is not a product density and must **not** be replaced by a conditional-cap independence assertion.  However it has a stronger exact structure that the live arbitrary-joint counterexamples do not possess.

Taking the Fourier transform only in the sheared hub variable gives

\[
\boxed{
\int_{\mathbb R}e^{isy_h}g(y_h,x')\,dy_h
=\widehat f_h(s)
\prod_{j\ne h}
\left[f_j(x_j)e^{is u_jx_j/\sqrt c}\right].}
\tag{6.6}
\]

Thus the entire overlap is converted into **coordinatewise linear phases** on the original product factors.  Product factorization is restored after this one partial Fourier transform.  The same statement holds after conditioning `H_eta`: the conditioned coordinates contribute only a deterministic unimodular factor, while the unconditioned original-coordinate factors still split exactly as in (6.6).

The shear vector has Euclidean size

\[
\left\|\frac{u}{\sqrt c}\right\|_2
=\sqrt{\frac{\rho}{c}}, \tag{6.7}
\]

which tends to zero at the endpoint.  Nevertheless no total-variation or moment perturbation argument is available: admissible densities can be arbitrarily fragmented, and an arbitrarily small translation need not be uniformly small in `L^1` over this class.  Equation (6.6), rather than a small-random-error estimate, is the product-sensitive resource that has to be spent.

## 7. What the new reduction rules out

The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` and the strengthened B05 r27 construction show that a generic residual variable may cancel the square through a reciprocal nonlinear shear such as

\[
T\approx-\frac{Z^2}{2Y}+\hbox{free variable},
\]

producing a logarithmically unbounded output even with bounded one-, two-, and three-dimensional densities.  The present survivor is narrower: its hub dependence is the **linear** shear (6.5), and its partial Fourier transform factorizes exactly as (6.6).  Therefore those counterexamples correctly forbid a generic conditional-cap proof but do not falsify the new linear-shear endpoint interface.

Likewise, treating `2 beta U L` as a small quadratic perturbation is invalid without support or moment assumptions.  The pruning lemma avoids that mistake: it changes no random variable and discards no term; it only conditions a controlled set of original coordinates and records the exact remaining graph geometry.

## 8. First unpaid implication after r30

Define

`QFORM-LINEAR-SHEAR-SUPPORT-STABILITY-v1`:

> In the heavy-null exact-rank-three core, after the cube-root pruning above, prove a universal interval/density bound uniform as `eta=rho^(1/3)->0` for the product-linear shear (6.5), using the exact factorization (6.6), while retaining arbitrary fragmented cap-one input laws and arbitrary affine terms.

A sufficient normalized version may assume

\[
s_{\min}(B)\ge s_0>0,\qquad
\sum u_j^2\le\eta^3,\qquad
|u_j|\le\eta\sqrt{w_j^2+z_j^2}, \tag{8.1}
\]

with the surviving active Gram bounded below by a fixed constant.  The endpoint `eta=0` is paid by (5.1).  A proof must be nonperturbative in the random variables; the natural analytic currency is the coordinatewise phase factorization (6.6), or an equivalent direct interval/coarea estimate that keeps it intact.

This is strictly sharper than saying merely "tiny leakage remains": the geometric part can be made a vanishing graph perturbation with vanishing Gram loss, and the exact stochastic defect from independence is a triangular **linear** shear whose partial Fourier transform still factorizes over original coordinates.

## 9. Status

- Full QFORM conjecture: `OPEN_NOT_PROVED_NOT_DISPROVED`.
- New result: `QFORM-CUBEROOT-OVERLAP-PRUNING-v1`, proved.
- New exact identity/interface: `QFORM-LINEAR-SHEAR-PARTIAL-FOURIER-FACTORIZATION-v1`, proved.
- Latest fleet02/B05 theorem applied to the actual current spread branch: (2.4).
- Completed fleet02/B05 support-separated theorem applied after pruning at the exact graph endpoint: (5.1).
- Continuity: available on the partner Fresnel collar (2.4); not established by the new endpoint reduction and not established for the full target.
- No Gaussian, log-concavity, moment, compact-support, connected-support, rotated-coordinate independence, or generic bounded-joint coarea assumption is introduced.
