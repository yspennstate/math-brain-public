SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B17, 2026-09-23T11:43:30Z.
attacking: the fully diffuse but non-identically-distributed Lindeberg witness class; prove any exact-rank-three source-valid diffuse CLT sequence is capped asymptotically by 3sqrt(2), or isolate the precise non-Lindeberg escape.

# QFORM-DIFFUSE-LINDEBERG-GLOBAL-GAUSSIAN-CEILING-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet02/B17` — sharp constant and witnesses  
Run: `fleet02-B17-20260923T1142Z-r11`  
Classification: **NEW SUPPORTING SHARP-WITNESS THEOREM**  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**  
Full-target continuity: **OPEN**  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. The first unpaid implication

The sharp lower obstruction `3 sqrt(2)` is produced by very diffuse exact-rank-three frames with centered unit-interval inputs. The remaining witness question is whether one can keep the frame fully diffuse but alter the independent cap-one laws — non-identically, asymmetrically, or with fragmented/unbounded supports — so that a non-Gaussian finite-scale effect survives and raises the limiting global peak above `3 sqrt(2)`.

This report closes the whole **Lindeberg/tight-covariance sub-class**. In particular, the conclusion is global in the output level and requires no independence after spectral rotation.

### Theorem (diffuse Lindeberg global Gaussian ceiling)

For each `m`, let `R_m` be an `n_m x 3` real matrix with orthonormal columns,

\[
R_m^T R_m=I_3,
\]

and rows `r_{mi} in R^3`. Assume the physical leverage tends to zero:

\[
\tau_m:=\max_{1\le i\le n_m}\|r_{mi}\|^2\longrightarrow0.
\tag{1.1}
\]

Fix

\[
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3),
\qquad |\lambda_j|\ge1,
\tag{1.2}
\]

and define the exact-rank-three physical matrix

\[
A_m=R_m\Lambda R_m^T.
\tag{1.3}
\]

Let `X_{m1},...,X_{mn_m}` be independent real random variables with probability densities `f_{mi}` satisfying

\[
0\le f_{mi}\le1.
\tag{1.4}
\]

For this theorem only, impose the following **explicit witness-class hypotheses**: each variable has finite mean `mu_{mi}` and finite variance `v_{mi}`, and, with

\[
Z_{mi}=r_{mi}(X_{mi}-\mu_{mi})\in\mathbb R^3,
\]

\[
h_m:=\sum_i r_{mi}\mu_{mi}\to h,
\qquad
\Sigma_m:=\sum_i v_{mi}r_{mi}r_{mi}^T\to\Sigma,
\tag{1.5}
\]

and the vector Lindeberg condition holds:

\[
\forall\varepsilon>0:\qquad
\sum_i \mathbb E\!\left[
\|Z_{mi}\|^2\mathbf1_{\{\|Z_{mi}\|>\varepsilon\}}
\right]\longrightarrow0.
\tag{1.6}
\]

Then, for all sufficiently large `m`, `Q_m=X_m^T A_mX_m` has a bounded continuous density `p_m`, and

\[
\boxed{
\limsup_{m\to\infty}\|p_m\|_\infty\le3\sqrt2.
}
\tag{1.7}
\]

More precisely, if `G~N(h,Sigma)` and

\[
Q_\infty=G^T\Lambda G,
\]

then `Q_infty` has a bounded continuous density `p_infty` and

\[
\boxed{\|p_m-p_\infty\|_\infty\longrightarrow0,}
\tag{1.8}
\]

while

\[
\boxed{\|p_\infty\|_\infty\le3\sqrt2.}
\tag{1.9}
\]

The constant is sharp for this class: for `Lambda=diag(1,1,-1)` and three equal centered-uniform diffuse banks, `||p_m||_infty -> 3sqrt(2)`.

The finite-variance/Lindeberg/tightness assumptions in (1.5)-(1.6) are **not** hypotheses of the original conjecture. They are stated because this is a witness-exclusion theorem, not a full-QFORM proof. The full target still permits infinite variance, non-Lindeberg arrays, and arbitrary fragmented/unbounded supports.

## 2. Exact spectrum and source provenance

Because `R_m` is an isometry from `R^3` onto its column range, for every `y in R^3`,

\[
A_m(R_my)=R_m\Lambda y.
\]

Thus the restriction of `A_m` to `range(R_m)` is unitarily equivalent to `Lambda`, while `A_m` vanishes on the orthogonal complement. Therefore the exact nonzero spectrum of every finite matrix is

\[
\boxed{\{\lambda_1,\lambda_2,\lambda_3\}.}
\tag{2.1}
\]

In particular, every finite member satisfies the target spectral hypothesis. All randomness remains in the **original physical coordinates** `X_{mi}`, which are independent by construction. The projected vector

\[
Y_m=R_m^T X_m
\tag{2.2}
\]

is generally dependent across its three coordinates; no post-rotation independence is assumed or used.

Also

\[
Q_m=Y_m^T\Lambda Y_m.
\tag{2.3}
\]

## 3. Cap one forces the minimum covariance floor

A basic fact that is valid law by law is

\[
\boxed{\operatorname{Var}(X)\ge\frac1{12}}
\tag{3.1}
\]

for every probability density `f<=1` with finite variance.

Indeed, if `mu=EX`, then among all measurable `0<=f<=1` of total mass one, the integral

\[
\int (x-\mu)^2 f(x)\,dx
\]

is minimized by filling the measure-one sublevel set closest to `mu`, namely the interval `[mu-1/2,mu+1/2]`. Hence

\[
\operatorname{Var}(X)
\ge\int_{-1/2}^{1/2}x^2\,dx
=\frac1{12}.
\]

Applying (3.1) to every physical coordinate and using `R_m^T R_m=I_3`,

\[
\Sigma_m
=\sum_i v_{mi}r_{mi}r_{mi}^T
\succeq\frac1{12}\sum_i r_{mi}r_{mi}^T
=\frac1{12}I_3.
\tag{3.2}
\]

Passing to the limit in (1.5),

\[
\boxed{\Sigma\succeq I_3/12.}
\tag{3.3}
\]

This is the exact variance floor that makes the isotropic centered Gaussian `(1,1,-1)` endpoint equal to `3sqrt(2)`.

## 4. Joint CLT without spectral-coordinate independence

Write

\[
Y_m=h_m+\sum_i Z_{mi}.
\tag{4.1}
\]

The vectors `Z_{mi}` are independent because they are functions of different original coordinates, have mean zero, and their total covariance is `Sigma_m`. Assumptions (1.5)-(1.6) are precisely the multivariate triangular-array Lindeberg hypotheses. Therefore

\[
\boxed{Y_m\Longrightarrow G\sim N(h,\Sigma).}
\tag{4.2}
\]

The continuous mapping theorem applied to the fixed quadratic polynomial `y -> y^T Lambda y` gives

\[
Q_m\Longrightarrow Q_\infty=G^T\Lambda G.
\tag{4.3}
\]

Hence, if

\[
\phi_m(t)=\mathbb E e^{itQ_m},
\qquad
\phi_\infty(t)=\mathbb E e^{itQ_\infty},
\]

then for every fixed real `t`,

\[
\phi_m(t)\to\phi_\infty(t).
\tag{4.4}
\]

Weak convergence alone would not rule out a narrow finite-`m` density spike. The next step is what makes the conclusion a **global density** statement.

## 5. Apply the completed `e5f...` Fresnel--Brascamp--Lieb theorem to the actual finite witnesses

Required source actually used:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`.

Its completed Theorem F applies to a rank-three representation

\[
A=\sum_{j=1}^3\lambda_j v_jv_j^T+B
\]

when the selected physical row leverage is at most `1/2`; arbitrary diagonal twists and linear terms are harmless. Here take `B=0`, take the three columns of `R_m` as `v_j`, and select **all** physical coordinates. The frame Gram matrix in Theorem F is exactly

\[
G_I=R_m^T R_m=I_3,
\]

and its normalized row leverages are exactly `||r_{mi}||^2`. By (1.1), for all sufficiently large `m`, every leverage is at most `1/2`. Therefore Theorem F gives the real finite-source inequality

\[
|\phi_m(t)|
\le
(4\pi)^{3/2}|t|^{-3/2}
\prod_{j=1}^3|\lambda_j|^{-1/2}
\le
(4\pi)^{3/2}|t|^{-3/2}.
\tag{5.1}
\]

Together with `|phi_m(t)|<=1`,

\[
\boxed{
|\phi_m(t)|\le g(t):=\min\{1,(4\pi)^{3/2}|t|^{-3/2}\},
}
\tag{5.2}
\]

where `g in L^1(R)` and the majorant is independent of `m` and of the physical laws.

This use of Theorem F is important: a CLT by itself gives only weak convergence and would not exclude a high narrow spike. The product-source Fourier theorem supplies a uniform integrable envelope at every finite stage.

## 6. Uniform convergence of the entire output density

By (4.4) and (5.2), the pointwise limit satisfies `|phi_infty(t)|<=g(t)`. Hence

\[
|\phi_m(t)-\phi_\infty(t)|\le2g(t),
\]

and dominated convergence gives

\[
\boxed{
\|\phi_m-\phi_\infty\|_{L^1(\mathbb R)}\longrightarrow0.
}
\tag{6.1}
\]

Fourier inversion now produces bounded continuous densities for all sufficiently large finite `m` and for the Gaussian limit, with

\[
\|p_m-p_\infty\|_\infty
\le {1\over2\pi}
\|\phi_m-\phi_\infty\|_1
\longrightarrow0.
\tag{6.2}
\]

This proves (1.8). In particular, there is no hidden off-zero finite-stage spike that survives the diffuse Lindeberg limit.

## 7. Apply the completed fleet03/B17 Gaussian theorem

The worker-owned completed theorem actually used at the endpoint is

`yspennstate/math-open-problems@dcf8885d5153370cacfa246ad1e29fb06d971769`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T070310Z-fleet03-B17-QFORM-r25/REPORT.md`.

It proves: if `G~N(mu,Sigma)` with `Sigma >= sigma^2 I` and a symmetric matrix has at least three eigenvalues of modulus at least one, then

\[
\|p_{G^TAG}\|_\infty\le {1\over2\sqrt2\,\sigma^2}.
\tag{7.1}
\]

Apply (7.1) with the present three-dimensional `A=Lambda` and the covariance floor (3.3), i.e. `sigma^2=1/12`. This gives

\[
\boxed{
\|p_\infty\|_\infty\le3\sqrt2.
}
\tag{7.2}
\]

Combining (6.2) and (7.2),

\[
\limsup_m\|p_m\|_\infty
\le\|p_\infty\|_\infty
\le3\sqrt2,
\]

which proves (1.7).

Notice the logical division: the `e5f...` theorem is used on the actual finite cap-one product laws to obtain density compactness in the strong sup norm; the fleet03/B17 theorem is used only on the limiting Gaussian, where it is valid with arbitrary mean and covariance floor. At no point are the three projected coordinates declared independent before the Gaussian limit.

## 8. Sharpness inside the theorem's class

Take `n_m=3m` and let `R_m` have `m` repeated rows `e_j/sqrt(m)` in each bank `j=1,2,3`. Then

\[
R_m^TR_m=I_3,
\qquad
\tau_m=1/m\to0.
\]

Let every physical input be `Unif[-1/2,1/2]`, and take

\[
\Lambda=\operatorname{diag}(1,1,-1).
\]

The three normalized bank sums converge jointly to independent `N(0,1/12)` coordinates, so the limiting quadratic form is

\[
G_1^2+G_2^2-G_3^2.
\]

Its density has global peak

\[
\boxed{p(0)=3\sqrt2.}
\tag{8.1}
\]

Equation (6.2) then gives

\[
\boxed{\|p_m\|_\infty\longrightarrow3\sqrt2.}
\tag{8.2}
\]

Thus the constant in (1.7) cannot be improved within the diffuse Lindeberg class.

## 9. Apply the latest designated partner result: rare critical fragments

The latest completed `fleet03/B17` result available during this invocation is

`yspennstate/math-open-problems@48e35fac4689f50a415638faba5a6e634b3d0329`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T113026Z-fleet03-B17-QFORM-auto11/REPORT.md`.

It studies the exact rotated three-bank frame with row norm `1/sqrt(m)` and, in bank `j`, the cap-one physical density

\[
f_{j,m}(x)
=(1-\varepsilon_{j,m})\mathbf1_{[-1/2,1/2]}(x)
+\mathbf1_{[a_j\sqrt m-\varepsilon_{j,m}/2,
              a_j\sqrt m+\varepsilon_{j,m}/2]}(x),
\qquad
\varepsilon_{j,m}=c_j/m^2.
\tag{9.1}
\]

The partner proves the cone-tip first variation

\[
\liminf_m m\left(1-{p_{Q_m}(0)\over3\sqrt2}\right)
\ge
{5295\over21952}
+{1\over2}\sum_{j=1}^3c_j(1-e^{-6a_j^2}).
\tag{9.2}
\]

I now apply that completed construction to the present theorem and obtain a **new global consequence**.

For one physical variable in bank `j`, put `eps=c/m^2`. Its exact mean is

\[
\mu_m=\varepsilon a\sqrt m={ca\over m^{3/2}},
\tag{9.3}
\]

and its exact variance is

\[
\boxed{
 v_m
={1\over12}+{ca^2\over m}-{c\over12m^2}
-{c^2a^2\over m^3}+{c^3\over12m^6}.
}
\tag{9.4}
\]

Therefore the normalized bank mean is

\[
\sqrt m\,\mu_m={ca\over m}\to0,
\tag{9.5}
\]

and the bank variance tends to `1/12`. Orthogonal mixing by the partner's fixed rotation preserves the limiting covariance floor, so

\[
h_m\to0,
\qquad
\Sigma_m\to I_3/12.
\tag{9.6}
\]

The Lindeberg condition also holds. For fixed threshold `delta>0`, the centered main interval contributes nothing for all sufficiently large `m`, since a physical row has norm `1/sqrt(m)`. A remote selection contributes a row-scaled displacement of order `|a|`, but its probability per physical coordinate is `c/m^2`; summing its squared contribution over the `m` coordinates in that bank is therefore

\[
O\!\left(m\,{c\over m^2}a^2\right)=O(m^{-1})\to0.
\tag{9.7}
\]

Thus the partner's exact fragmented family satisfies every hypothesis of Theorem 1. Consequently its **global** density obeys

\[
\boxed{
\limsup_m\|p_{Q_m}\|_\infty\le3\sqrt2.
}
\tag{9.8}
\]

On the other hand, (9.2) in particular gives `p_{Q_m}(0)->3sqrt(2)`. Hence

\[
\boxed{
\|p_{Q_m}\|_\infty\longrightarrow3\sqrt2.
}
\tag{9.9}
\]

This strengthens the partner result in a direction it explicitly left open: it rules out a surviving **off-tip global overshoot** for that rare-fragment family at order one. It does **not** determine the first-order `1/m` correction of the global maximum; an off-tip excess of size `o(1)` is still compatible with (9.9). The partner's strict negative cone-tip first variation (9.2) remains the sharper local statement.

## 10. What this excludes, and what it does not

The theorem excludes an extensive adversarial class: arbitrary non-identical cap-one laws, arbitrary asymmetry and disconnected/unbounded supports are allowed **provided** the diffuse projected triangular array has a finite tight mean/covariance limit and obeys Lindeberg. Within that class, all higher cumulants wash out strongly enough that the global output density converges uniformly to an affine Gaussian quadratic density, and the sharp Gaussian ceiling is `3sqrt(2)`.

Therefore a source-valid exact-rank-three diffuse witness with an asymptotic peak strictly above `3sqrt(2)` must violate at least one explicit gate used here. It must exhibit a genuinely non-Gaussian triangular-array phenomenon: failure of Lindeberg, failure of projected mean/covariance tightness, or no finite covariance at all. Alternatively a stronger finite/mesoscopic witness can leave the fully diffuse regime by retaining macroscopic leverage.

This is **not** a counterexample to QFORM and not a proof of the full theorem. In particular, the original target permits all of the failure modes just listed. Failure to control those modes would be failure of this Gaussian-domain proof mechanism, not failure of the conjecture. A genuine family with `||p_Q||_infty` unbounded would be required to disprove QFORM; a family merely exceeding `3sqrt(2)` would refute only that candidate sharp constant.

## 11. Sources and correction discipline

The required newest-Claude source was applied at the real inequality (5.1), not used as a label. The latest compatible partner result was applied at (9.8)-(9.9). The argument avoids every live prohibited premise relevant here: no law-uniform pointwise scalar stationary phase, no arbitrary-joint coarea bound, no independence after spectral rotation, no conditional projection-cap moment, no fixed-fragment extremality, and no universally good physical minor.

Full QFORM remains OPEN. The next B17 witness search should target a **diffuse non-Lindeberg** construction (for example, order-one spectral jumps with nonvanishing total activity but not reducible to an independent Gaussian shift), or an intermediate-leverage finite/mesoscopic geometry. Those are now the genuinely unpaid branches for this mechanism.
