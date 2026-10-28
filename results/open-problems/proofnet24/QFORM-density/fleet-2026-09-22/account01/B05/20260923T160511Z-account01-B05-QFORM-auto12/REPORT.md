SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T16:05:11Z.
attacking: the near-null nonzero-pivot bridge after the paid heavy-null endpoint; first eliminate every support-disjoint longitudinal coordinate exactly, then isolate the genuinely same-coordinate mixed shear.

# account01/B05 auto12 — arbitrary-pivot mixed-support absorption and exact partial-Fourier shear

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea / equivalent interval bound, preserving arbitrary product densities  
**Run:** `20260923T160511Z-account01-B05-QFORM-auto12`  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / PARTNER_RESULTS_APPLIED / PRECISE_REMAINING_FACTOR_SHARPENED / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the leave-one-out Fresnel branch below; not claimed on the exact-coloop branch by this report; unrestricted continuity remains open.

The full conjecture remains OPEN / NOT PROVED / NOT DISPROVED. The theorem below concerns the exact-rank-three heavy-row reduction and does not silently extend to arbitrary higher-rank Schur remainders. No moments, support bounds, log-concavity, iid assumption, post-rotation independence, conditional-density cap, or pointwise law-uniform van-der-Corput estimate is used.

## 1. Fresh source state and first unpaid implication


The preceding B05 auto11 proved the exact nonzero-pivot Schur identity

\[
B=\begin{pmatrix}d&g^T\\g&C\end{pmatrix},\qquad
S=C-d^{-1}gg^T,
\]
\[
q(s,y)=d(s+d^{-1}g^Ty)^2+y^TSy,
\qquad \det B=d\det S,
\]
so under the three-large-eigenvalue condition `|det S| >= |d|^{-1}`. It also showed that a square-root slice estimate alone does not close a quadratic hub: determinant/Schur curvature has to be retained.

The freshest completed designated partner account02/B05 result available at the start was

`math-open-problems@75df8a812c96735205ee8370363808fd734e2d12`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T130427Z-account02-B05-QFORM-auto11/REPORT.md`.

It closes the entire exact-rank-three heavy **physical-null** endpoint in the residual-diffuse branch by slicing a transverse projection and applying a product-Fourier/Fresnel--Brascamp--Lieb estimate, with bound `<55.776`; its first successor is the nonzero near-null pivot bridge.

The first question in this run is more basic than estimating that bridge: which part of the longitudinal residual projection is actually relevant? The answer is exact and independent of the pivot.

## 2. Setup: arbitrary physical pivot

Let

\[
A=RBR^T,\qquad R^TR=I_3,
\]

be exact rank three with real symmetric invertible `B` and

\[
s_{\min}(B)\ge1.
\]

Choose an ORIGINAL physical coordinate `h` with leverage

\[
c=\|r_h\|^2>1/2.
\]

Rotate only the deterministic three-dimensional active coefficient basis so that

\[
r_h=\sqrt c\,e_1.
\]

No random variable is rotated. Write every other row as

\[
r_j=(u_j,t_j),\qquad t_j\in\mathbb R^2.
\]

Parseval gives

\[
\sum_{j\ne h}u_j^2=1-c,\qquad
\sum_{j\ne h}t_jt_j^T=I_2,\qquad
\sum_{j\ne h}u_jt_j=0. \tag{2.1}
\]

No assumption on the physical pivot

\[
d=e_1^TBe_1
\]

is made. In particular `d` may be zero, small nonzero, or large.

Define the support-disjoint and mixed-support sets

\[
D=\{j\ne h:t_j=0\},\qquad M=\{j\ne h:t_j\ne0\}, \tag{2.2}
\]

and longitudinal masses

\[
\rho_D=\sum_{j\in D}u_j^2,\qquad
\rho_M=\sum_{j\in M}u_j^2. \tag{2.3}
\]

Then

\[
c+\rho_D+\rho_M=1. \tag{2.4}
\]

## 3. Main theorem: arbitrary-pivot pure-longitudinal absorption

### Theorem 3.1 — `QFORM-ARBITRARY-PIVOT-MIXED-SUPPORT-ABSORPTION-v1`

Under Section 2, the law of `X^TAX` is exactly the law of an exact-rank-three quadratic form of independent cap-one inputs consisting of one synthetic scalar and the original coordinates indexed by `M`. Its orthonormal coefficient frame has a synthetic heavy row of leverage

\[
\boxed{c_*={c\over c+\rho_M}}, \tag{3.1}
\]

and hence residual leakage

\[
\boxed{1-c_*={\rho_M\over c+\rho_M}.} \tag{3.2}
\]

Writing

\[
g=c+\rho_M,
\]

the normalized active matrix is

\[
\boxed{B_*=G^{1/2}BG^{1/2},\qquad G=\operatorname{diag}(g,1,1),} \tag{3.3}
\]

and satisfies

\[
\boxed{s_{\min}(B_*)\ge g\,s_{\min}(B)\ge g\ge c,} \tag{3.4}
\]

\[
\boxed{\det B_*=g\det B.} \tag{3.5}
\]

The physical quadratic coefficient of the synthetic heavy input is exactly unchanged:

\[
\boxed{r_*^TB_*r_*=c\,e_1^TBe_1=cd.} \tag{3.6}
\]

Thus every longitudinal coefficient supported on a coordinate carrying no transverse coefficient is exactly harmless, for **every** scalar pivot. Only the longitudinal mass on coordinates simultaneously carrying transverse coefficients remains a genuine endpoint parameter.

### Proof

Put

\[
U_D=\sum_{j\in D}u_jX_j,
\]

and define

\[
S=X_h+{U_D\over\sqrt c}. \tag{3.7}
\]

The random variable `S` is independent of every `X_j`, `j in M`, because it uses only the disjoint bank `{h} union D`. If `f_h<=1` is the density of `X_h`, then, without requiring a density for `U_D`,

\[
p_S(s)=\mathbb E f_h\!\left(s-{U_D\over\sqrt c}\right), \tag{3.8}
\]

so

\[
0\le p_S\le1,\qquad \int p_S=1. \tag{3.9}
\]

The active spectral vector becomes exactly

\[
R^TX=\sqrt c\,S e_1+\sum_{j\in M}r_jX_j. \tag{3.10}
\]

The coefficient Gram of the new independent source is

\[
G=c e_1e_1^T+\sum_{j\in M}r_jr_j^T. \tag{3.11}
\]

Using (2.1), the mixed bank has first-coordinate mass `rho_M`, transverse Gram `I_2`, and zero longitudinal-transverse cross Gram. Hence

\[
G=\operatorname{diag}(c+\rho_M,1,1)=\operatorname{diag}(g,1,1). \tag{3.12}
\]

Normalize the rows by `G^{-1/2}` and move the congruence into the active matrix. The synthetic row is

\[
r_*=(\sqrt{c/g},0,0), \tag{3.13}
\]

which proves (3.1)-(3.3). Since `s_min(G^{1/2})=sqrt(g)`,

\[
s_{\min}(G^{1/2}BG^{1/2})
\ge g\,s_{\min}(B),
\]

proving (3.4). Equation (3.5) is `det B_*=(det G)det B=g det B`. Finally

\[
r_*^TB_*r_*
={c\over g}(g d)=cd,
\]

which is (3.6). QED.

## 4. Exact leave-one-out geometry and determinant cancellation

Assume `rho_M>0`. The normalized mixed rows are

\[
r_j^*=\left({u_j\over\sqrt g},t_j\right),\qquad j\in M. \tag{4.1}
\]

Deleting the synthetic hub from the normalized frame leaves the exact Gram

\[
H_*=I-r_*r_*^T
=\operatorname{diag}\left({\rho_M\over g},1,1\right). \tag{4.2}
\]

Therefore every mixed leaf has leave-one-out leverage

\[
\boxed{
\ell_j^{(-*)}=(r_j^*)^TH_*^{-1}r_j^*
={u_j^2\over\rho_M}+\|t_j\|^2.
} \tag{4.3}
\]

Also

\[
\sum_{j\in M}\ell_j^{(-*)}=3, \tag{4.4}
\]

so at most five mixed leaves can violate the strict gate `ell_j^{(-*)}>1/2`.

Most importantly,

\[
\boxed{
|\det B_*|\det H_*
=(g|\det B|){\rho_M\over g}
=|\det B|\rho_M.
} \tag{4.5}
\]

The absorption renormalization introduces no hidden factor: the determinant gain and the leave-one-out Gram loss cancel exactly.

## 5. Designated partner applied: diffuse mixed-support branch

Use account02/B05 r19, theorem `QFORM-EXACTRANK3-LEAVEONEOUT-FRESNEL-v1`, canonical mathematics

`math-open-problems@96b63ddb9eb6835e92a5ad56e3fd91f5b220f9e2`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T092247Z-account02-B05-QFORM-r19/REPORT.md`.

It gives, after conditioning one original independent coordinate and provided every remaining normalized leaf leverage is at most `1/2`,

\[
\|p_Q\|_\infty
\le12\,[|\det B_*|\det H_*]^{-1/3}. \tag{5.1}
\]

Strictly, `s_min(B_*)` may be `c<1`; apply the partner theorem to `B_*/c` and then scale the output back. The factor `c` cancels, leaving exactly (5.1). Substituting (4.5),

\[
\boxed{
\|p_Q\|_\infty
\le12\,(|\det B|\rho_M)^{-1/3}.
} \tag{5.2}
\]

For the owner target `|det B|>=1`,

\[
\boxed{
\|p_Q\|_\infty\le12\rho_M^{-1/3}.
} \tag{5.3}
\]

This branch has a bounded continuous representative because the partner proof produces an `L^1` characteristic function. In particular, if

\[
\rho_M\ge1/128,
\]

then

\[
\boxed{\|p_Q\|_\infty<60.477.} \tag{5.4}
\]

This is an actual equation-level application of a completed account02/B05 theorem to the arbitrary-pivot absorbed state.

## 6. Designated partner applied: exact mixed-support endpoint `rho_M=0`

If

\[
\rho_M=0, \tag{6.1}
\]

then after absorption the normalized frame has a leverage-one synthetic original input: `c_*=1`. The remaining transverse variables use a disjoint original-coordinate bank. This is exactly an **exact-coloop** state, for arbitrary physical pivot.

Use the completed account02/B05 r22 theorem `QFORM-EXACT-COLOOP-CLOSURE-v1`, canonical proof

`math-open-problems@e175c1cd46ed7803bdd10a9fe7f8bb30f22c72fd`.

That theorem gives `||p||_infinity<=256` when the active three eigenvalues have magnitude at least one. Here `s_min(B_*)>=c`, so apply it to `B_*/c` and scale back. This gives

\[
\boxed{
\|p_Q\|_\infty\le{256\over c}<512
\qquad(c>1/2).
} \tag{6.2}
\]

For the ultra-heavy collar `c>127/128` used in preceding B05 endpoint reductions,

\[
\boxed{
\|p_Q\|_\infty
<{256\cdot128\over127}
<258.016.
} \tag{6.3}
\]

Thus the endpoint `rho_M=0` is paid uniformly for **all** scalar pivots, including the nonzero near-null bridge. Pure-longitudinal leakage does not create that bridge.

## 7. Mixed-only cube-root pruning works for arbitrary pivot

The remaining small parameter is now only `rho_M`. Put

\[
\widehat\rho={\rho_M\over g}=1-c_*,\qquad
\eta=\widehat\rho^{1/3}. \tag{7.1}
\]

For the normalized mixed rows (4.1), define the large-slope set

\[
J_\eta=\left\{j\in M:
{|u_j|\over\sqrt g}>\eta\|t_j\|
\right\}. \tag{7.2}
\]

Let

\[
K_\eta=\sum_{j\in J_\eta}r_j^*(r_j^*)^T.
\]

Then exactly as in the B05 cube-root calculation,

\[
\sum_{j\in J_\eta}{u_j^2\over g}
\le\widehat\rho=\eta^3, \tag{7.3}
\]

and the defining inequality gives

\[
\sum_{j\in J_\eta}\|t_j\|^2
\le\eta^{-2}\widehat\rho=\eta. \tag{7.4}
\]

Hence

\[
\boxed{\|K_\eta\|_{op}\le\operatorname{tr}K_\eta\le\eta+\eta^3.} \tag{7.5}
\]

After conditioning only the ORIGINAL independent coordinates in `J_eta`, the surviving active Gram obeys

\[
G_\eta=I-K_\eta\succeq(1-\eta-\eta^3)I. \tag{7.6}
\]

Whitening the surviving frame therefore leaves all three active directions at scale at least

\[
\boxed{
s_{\min}(B_{\rm surv})
\ge g(1-\eta-\eta^3).
} \tag{7.7}
\]

Every unconditioned mixed row satisfies the pointwise graph estimate

\[
\boxed{
{|u_j|\over\sqrt g}\le\eta\|t_j\|.
} \tag{7.8}
\]

No use was made of `d=0`: this reduction is stable for arbitrary pivot. Therefore the punctured endpoint can be reduced to a pointwise-vanishing same-coordinate graph shear while preserving all three curvatures at a universal scale.

## 8. Exact triangular shear and partial-Fourier product factorization

The absorption theorem gives a particularly clean form of the remaining dependence. Write the active matrix in the deterministic split `e_1 direct_sum e_1^perp` as

\[
B=\begin{pmatrix}d&g_0^T\\g_0&C\end{pmatrix}. \tag{8.1}
\]

On the mixed bank put

\[
U_M=\sum_{j\in M}u_jX_j,
\qquad
T=\sum_{j\in M}t_jX_j\in\mathbb R^2. \tag{8.2}
\]

After the support-disjoint absorption, define the triangularly sheared hub

\[
Y=S+{U_M\over\sqrt c}. \tag{8.3}
\]

Then the quadratic form becomes exactly

\[
\boxed{
Q=cd\,Y^2+2\sqrt c\,Y\,g_0^TT+T^TCT.
} \tag{8.4}
\]

This looks like a scalar plus a projected pair, but `Y` and `T` are **not** independent. The point is that their dependence is not arbitrary. If `F_M(x)=prod_{j in M}f_j(x_j)`, their joint source density before projecting `T` is

\[
G(y,x)=p_S\!\left(y-{U_M(x)\over\sqrt c}\right)F_M(x), \tag{8.5}
\]

with unit Jacobian. Taking Fourier transform only in `y` gives the exact identity

\[
\boxed{
\int_{\mathbb R}e^{isy}G(y,x)\,dy
=\widehat p_S(s)
\prod_{j\in M}
\left[f_j(x_j)e^{is u_jx_j/\sqrt c}\right].
} \tag{8.6}
\]

Thus after one partial Fourier transform the original-coordinate product factorization is restored **exactly**; the whole same-coordinate overlap appears only as coordinatewise linear phases. The shear vector has deterministic squared size

\[
\boxed{
\sum_{j\in M}{u_j^2\over c}={\rho_M\over c}.
} \tag{8.7}
\]

This is precisely the kind of translation/modulation that the current Fresnel--Brascamp--Lieb source handles without changing its one-dimensional `L^p` constants. What is not yet proved is the final endpoint-stable integration of the quadratic hub chirp together with the two-sheet transverse curvature.

For `d!=0`, completing the square in (8.4) gives the same exact Schur curvature from auto11:

\[
S_C=C-d^{-1}g_0g_0^T,
\qquad
\boxed{\det S_C={\det B\over d}.} \tag{8.8}
\]

So the remaining bridge simultaneously contains a vanishing graph shear (8.7) and a diverging Schur determinant (8.8). Any proof that first takes an absolute fiber supremum loses the cancellation between those two resources.

## 9. What is now genuinely unpaid

The first B05 implication is sharpened to

**`QFORM-ARBITRARY-PIVOT-SAME-COORDINATE-MIXED-SHEAR-v1`.** In the exact-rank-three heavy-row state, after absorbing every pure-longitudinal original-coordinate bank as in Theorem 3.1, prove a universal interval/coarea bound in the punctured regime

\[
0<\rho_M\ll1,
\]

uniformly in the physical pivot `d` (especially `d->0`), when one or more normalized mixed leaves violate the leave-one-out `1/2` gate. Equivalently, exploit the exact product factorization (8.6) while jointly spending the quadratic hub chirp and the determinant identity (8.8).

The following states are no longer part of that debt:

- all pure-longitudinal leakage, for any pivot: absorbed exactly;
- `rho_M=0`: exact-coloop partner bound `<=256/c`;
- diffuse mixed leaves: partner Fresnel bound `12(|det B|rho_M)^(-1/3)`;
- large-slope mixed leaves can be conditioned with Gram loss at most `eta+eta^3`, leaving the pointwise graph slope `eta=rhohat^(1/3)`.

The missing factor is therefore not a scalar density cap, a transverse joint-density cap, or a local determinant. It is an **endpoint-stable modulation/Fresnel estimate for the exact partial-Fourier product object (8.6)**. This is narrower than the preceding nonzero-pivot Schur statement and preserves the original product provenance required by all live corrections.

## 10. Source discipline

No arbitrary-joint coarea theorem, conditional-density moment, post-rotation independence, small-random-perturbation argument, or pointwise law-uniform scalar oscillatory decay is used. The only rotations are deterministic changes of the three-dimensional coefficient basis. Every conditioning operation is on original independent coordinates. The synthetic scalar is formed only from a disjoint original-coordinate bank and inherits the cap one by convolution.

Full QFORM remains OPEN. Essential boundedness is proved only in the scoped branches above; continuity is separately proved on the account02/B05 r19 Fresnel branch and is not promoted to the full target.
