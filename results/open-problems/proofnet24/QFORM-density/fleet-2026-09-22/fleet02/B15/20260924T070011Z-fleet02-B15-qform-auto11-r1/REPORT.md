SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-24T07:00:11Z.
attacking: dimension-free majority-sheet regularity versus diffuse leverage; sharpen submass stability and independently audit the ruled rough-input bridge.

# fleet02/B15 — leverage-sensitive ruled regularity

Status: `NEW_RULED_LEVERAGE_STABILITY_PROVED / ROUGH_BRIDGE_RECHECKED / SOURCE_RESULT_APPLIED / FULL_QFORM_OPEN`.

Control refresh before publication: `math-research-brain@426c030d3bb9f01efa27556c8a0b6cedb613f798`, owner revision `2026-09-22.15`; no fleet02/B15 stop or pause. Execution remains `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication

The full theorem remains OPEN. This run removes a regularity loss on the already-completed majority/one-sheet rank-three chamber: in a diffuse spectral frame, rough product-law perturbations are now **Lipschitz in aggregate marginal L1**, with a dimension-free constant. For the isotropic rank-three majority sheet, arbitrary leverage is dimension-free Holder in the aggregate marginal L1 distance, and all square-root instability is confined to at most three high-leverage original coordinates.

The first unpaid B15 implication is therefore still the complementary convex/two-sheet and higher-rank aggregate receiver in the no-good-physical-triple branch. A generic X-ray bound is unavailable (`QFORM-TWOSHEET-XRAY-ONLY-FALSE`); product provenance must be retained until the third smoothing resource is paid. Continuity is not the missing universal-height step.

## 1. New anisotropic submass theorem

Let `R in R^{n x 3}` have orthonormal columns `r_1,r_2,r_3`, let `rho_j` be the j-th row of R, and set

\[
a_j=|\rho_j|^2,\qquad \sum_j a_j=3.
\]

For

\[
q(X)=\lambda_1\langle r_1,X\rangle^2+\lambda_2\langle r_2,X\rangle^2-\mu\langle r_3,X\rangle^2,
\qquad \lambda_1,\lambda_2,\mu>0,
\]

define the completed source coefficient

\[
C_+=
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
{d\theta\over
\sqrt{\sin^2\theta/\lambda_1+
\cos^2\theta/\lambda_2+1/\mu}}.
\tag{1}
\]

Replace one original-coordinate probability factor, coordinate j, by an arbitrary cap-one subdensity of mass `m<=1`, and let `nu_{j,m}^+` be the output submeasure on `q>=0`. Then, whenever `a_j<1`,

\[
\boxed{
H(\nu_{j,m}^+)
\le C_+\min\left(1,{m\over\sqrt{1-a_j}}\right).
}
\tag{2}
\]

Here `H(nu)=sup_I nu(I)/|I|`, so (2) is an essential-height statement without assuming a density representative in advance.

**Proof.** Undo the source's spectral scaling. The ruling direction is

\[
v_\theta=
\left(-{\sin\theta\over\sqrt{\lambda_1}},
{\cos\theta\over\sqrt{\lambda_2}},
{1\over\sqrt\mu}\right).
\]

Let `U_theta` be an orthonormal 2-frame spanning `v_theta^perp`. The projected coefficients of the original product law have total Gram matrix `I_2`. Removing coordinate j leaves Gram determinant

\[
d_j(\theta)
=\det(I_2-(U_\theta\rho_j)(U_\theta\rho_j)^T)
=1-|U_\theta\rho_j|^2
\ge1-a_j.
\tag{3}
\]

The two-dimensional trace density seen by the ruling satisfies two bounds:

\[
h_\theta\le2,
\qquad
h_\theta\le {2m\over\sqrt{d_j(\theta)}}.
\tag{4}
\]

The first completes the subdensity to a cap-one probability and uses the same two-dimensional product-projection theorem as the source. The second conditions on the selected original coordinate and applies that theorem to the remaining 2-frame, whose Gram determinant is `d_j(theta)`, then integrates the selected factor of mass m.

The source coarea factor is exactly `1/2`; the ruling parameter is not arclength, so the line integral carries the reciprocal speed `1/|v_theta|`. Consequently

\[
H(\nu_{j,m}^+)
\le
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
{\min(1,m/\sqrt{d_j(\theta)})\over|v_\theta|}\,d\theta,
\]

and (3) gives (2). When all three curvatures are at least one, the completed source theorem gives `C_+<=pi sqrt(2)`.

## 2. Diffuse frames are Lipschitz in rough product laws

Take two cap-one product laws `f=(f_i)` and `g=(g_i)`, and put

\[
\delta_j=\|f_j-g_j\|_1,
\qquad
\Delta=\sum_j\delta_j.
\]

Telescope the product difference in the original coordinates. The positive and negative parts of `f_j-g_j` are cap-one subdensities of mass `delta_j/2`. Applying (2) to both signs yields

\[
\|T_j^+\|_\infty
\le {C_+\delta_j\over\sqrt{1-a_j}}.
\tag{5}
\]

Hence, if the rank-three frame is diffuse in the exact source sense

\[
\max_j a_j\le {1\over2},
\]

then for `lambda_1,lambda_2,mu>=1`,

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le\sqrt2 C_+\Delta
\le2\pi\Delta.
}
\tag{6}
\]

This is dimension-free, orientation-free within the rank-three spectral frame, and anisotropic in the curvatures. No continuity is used to obtain (6).

## 3. Arbitrary leverage in the isotropic chamber

The preceding B15 result at
`math-open-problems@45779cb1dca5f453ac620431b380ad015a052e70`
proved, for the isotropic `(1,1,-1)` majority sheet, the orientation-uniform submass estimate

\[
H(\nu_{j,m}^+)\le20\sqrt2\sqrt m.
\tag{7}
\]

Combining (2) and (7), the j-th signed telescoping contribution obeys

\[
\|T_j^+\|_\infty
\le
\min\left(40\sqrt{\delta_j},
{\sqrt2\pi\delta_j\over\sqrt{1-a_j}}
\right).
\tag{8}
\]

Let `H={j:a_j>3/4}`. Since `sum a_j=3`, at most three coordinates lie in H. On the complement use the linear branch of (8), and on H use the square-root branch plus Cauchy-Schwarz. This gives the new aggregate estimate

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le2\sqrt2\pi\Delta+40\sqrt{3\Delta}.
}
\tag{9}
\]

For `Delta<=1`, in particular,

\[
\|r_f^+-r_g^+\|_\infty<79\sqrt\Delta.
\tag{10}
\]

Thus the previous `40 sum_j sqrt(delta_j)` loss is replaced by a dimension-free function of the aggregate marginal error. More structurally: all square-root instability is confined to at most three high-leverage original coordinates. In the fully diffuse chamber, even that loss disappears and (6) is Lipschitz.

The earlier sharpness example `Q=2XY+Z^2` has row leverages equal to one and exhibits a genuine `sqrt(delta)` lower bound on the same positive sheet. Therefore the improvement is not in conflict with the known optimal one-coordinate exponent: the sharp square-root behavior sits precisely in the high-leverage chamber excluded by (6).

## 4. Continuity is downstream

The source theorem first gives the majority interval height. For compact-smooth cap-one product inputs, the ruled integral gives a `C_0` positive-sheet density. Approximate arbitrary cap-one marginals in original-coordinate L1 by compact-smooth cap-preserving probabilities, arranging aggregate error `Delta_k->0`. Equation (6) makes the positive-sheet densities uniformly Cauchy when `max a_j<=1/2`; equation (9) does the same in the isotropic arbitrary-leverage case. Product L1 convergence identifies the uniform limit with the rough output submeasure.

Therefore in the diffuse anisotropic ruled chamber there is a canonical

\[
r_f^+\in C_0([0,\infty)),
\qquad
0\le r_f^+\le C_+\le\pi\sqrt2,
\tag{11}
\]

but the logical order is crucial: the essential height is proved by the interval/ruling argument first; continuity follows only afterward from uniform approximation. It is not used to smuggle in the bound.

## 5. Required completed-source application to a real target family

Apply the completed ruled theorem from
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
to three disjoint banks of size `m>=2`:

\[
Y_k={1\over\sqrt m}\sum_{j=1}^m X_{k,j},
\qquad
Q_m=Y_1^2+Y_2^2-Y_3^2.
\tag{12}
\]

The matrix has spectrum

\[
\{1,1,-1,0,\ldots,0\},
\]

so it lies exactly in the owner target. Every row leverage is `1/m<=1/2`. The completed source theorem gives the actual majority inequality

\[
\boxed{
\Pr(Q_m\in I,Q_m\ge0)
\le\pi\sqrt2\,|I|
}
\tag{13}
\]

for every interval I and arbitrary rough cap-one input laws. At the owner's triangular-kernel scale,

\[
\boxed{
\mathbb E[(\varepsilon-|Q_m-y|)_+\mathbf1_{\{Q_m\ge0\}}]
\le\pi\sqrt2\,\varepsilon^2.
}
\tag{14}
\]

The new stability theorem simultaneously gives, for two input-law arrays,

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le2\pi\sum_{k,j}\|f_{k,j}-g_{k,j}\|_1,
}
\tag{15}
\]

and therefore the difference of the two triangular-kernel quantities in (14) is at most

\[
2\pi\varepsilon^2
\sum_{k,j}\|f_{k,j}-g_{k,j}\|_1.
\tag{16}
\]

This is a genuine target-level rough-law inequality, not a continuity consequence.

## 6. Explicit source-valid obstruction to single-physical-triple payment

The same family (12) makes the remaining aggregate-before-inversion issue concrete. The one-dimensional product-projection theorem gives

\[
\|p_{Y_k}\|_\infty\le\sqrt2.
\]

Hence

\[
p_{Y_k^2}(s)\le{\sqrt2\over\sqrt s},\qquad s>0,
\]

and the beta convolution yields

\[
\|p_{Y_1^2+Y_2^2}\|_\infty\le2\pi.
\]

Convolution with the independent law of `-Y_3^2` cannot raise `L^infty`, so

\[
\boxed{\|p_{Q_m}\|_\infty\le2\pi\quad\text{uniformly in }m.}
\tag{17}
\]

Yet every invertible physical `3x3` principal block chooses one coordinate from each bank and equals, up to ordering,

\[
\operatorname{diag}(1/m,1/m,-1/m).
\]

Thus the best physical-triple scale is exactly `1/m`. The newest designated partner fleet03/B15 theorem
`math-open-problems@40b108ab5984542e26b8c8ff2cd059e13446bea8`
would give only

\[
\|p_{Q_m}\|_\infty<153m
\tag{18}
\]

if one insists on paying a single physical triple first. Equations (13) and (17) remain universal. This is consistent with the live `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` correction: reciprocal local-minor payment is a proof artifact on diffuse banks, not evidence of output blow-up.

This is an obstruction to a proof interface, not a counterexample to QFORM.

## 7. Independent audit of the ruled/rough-input bridge

For the source's standard cone

\[
q_0(z)=z_1^2+z_2^2-z_3^2,
\qquad
F(\theta,t)=\sqrt s\,e_\theta+t(e_\theta^\perp+e_3),
\]

one checks exactly

\[
F_\theta\times F_t={1\over2}\nabla q_0(F),
\qquad
{d\sigma\over|\nabla q_0|}={1\over2}\,d\theta\,dt.
\tag{19}
\]

After anisotropic scaling the ruling direction is `v_theta` above. Since t is not arclength, the line trace contributes `1/|v_theta|`; the two-dimensional product-projection cap `2` cancels the coarea `1/2`. This reproduces (1), including both delicate factors.

For arbitrary rough active marginals, mollify only the original independent coordinates. A nonnegative probability approximate identity preserves cap one and mass, while

\[
\left\|\prod_i f_i^{(\eta)}-\prod_i f_i\right\|_1
\le\sum_i\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{20}
\]

For an ambient invertible original-coordinate active block B, outside conditioning gives

\[
Q_w(x)=x^TBx+2d(w)^Tx+c_0(w)
=(x+B^{-1}d(w))^TB(x+B^{-1}d(w))+c(w).
\tag{21}
\]

Thus the later correction requiring the affine term to lie in the quadratic range is automatic in this scope, and square completion is only an original-coordinate translation. Restriction to the fixed conditional majority event and deterministic quadratic pushforward contract total variation. Therefore the smooth interval estimate passes to arbitrary rough inputs with the **identical** coefficient, and averaging the outside coordinates loses nothing.

No pointwise trace of a rough density, no output continuity, and no post-rotation independence is used.

## 8. Regularity ledger

Qualitative absolute continuity remains a separate coarea fact for a nonconstant quadratic-affine pushforward of an absolutely continuous joint law; it has no universal-height content. Essential boundedness in this report is paid by interval domination and the source's ruled projection geometry. Continuity is then obtained downstream in the explicitly stated chambers by uniform approximation. The complementary two-sheet/convex side remains governed by the live X-ray obstruction and is not claimed here.

## Sources consumed

- Fresh owner/control and QFORM state through `math-research-brain@426c030d3bb9f01efa27556c8a0b6cedb613f798`, owner revision `2026-09-22.15`.
- Required source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md` in `20260922T211500Z-decoupling-brascamp-lieb/`.
- Later compatible continuation: `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md`, including the correction that Theorem C's affine term must lie in the quadratic range.
- Prior fleet02/B15 submass theorem: `math-open-problems@45779cb1dca5f453ac620431b380ad015a052e70`.
- Latest designated partner fleet03/B15 localized physical-triple theorem: `math-open-problems@40b108ab5984542e26b8c8ff2cd059e13446bea8`.

No full-solution claim is made.
