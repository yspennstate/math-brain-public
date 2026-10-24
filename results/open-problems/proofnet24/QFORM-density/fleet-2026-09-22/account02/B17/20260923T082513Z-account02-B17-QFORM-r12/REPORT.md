SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T08:25:13Z.
attacking: genuinely fragmented/multiscale diffuse-bank witnesses; test whether arbitrary random translations of a cap-one uniform core can beat the `3 sqrt(2)` obstruction.

# QFORM B17 — arbitrary-translation diffuse banks have sharp asymptotic ceiling `3 sqrt(2)`

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING THEOREM**; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution state: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-valid adversarial class

Fix an integer `m>=2`. Let `P_m` be the `3m x 3` block-average frame: in bank `j in {1,2,3}`, its `m` physical rows equal `e_j/sqrt(m)`. Hence

\[
P_m^T P_m=I_3.
\tag{1.1}
\]

Let `B=B^T` be an arbitrary real `3 x 3` matrix with

\[
s_3(B)\ge1,
\tag{1.2}
\]

so every eigenvalue of `B` has modulus at least one, and define the physical target matrix

\[
A_m=P_mBP_m^T.
\tag{1.3}
\]

The nonzero eigenvalues of `A_m` are exactly the three eigenvalues of `B`: indeed `P_m` is an isometry from `R^3` onto its range, and `A_m` restricted to `Ran(P_m)` is unitarily equivalent to `B`. Thus every finite member is an exact source-valid QFORM matrix with at least three eigenvalues of modulus at least one.

For every physical coordinate choose

\[
X_i=U_i+Z_i,
\tag{1.4}
\]

where the `U_i` are iid `Unif[-1/2,1/2]`, the `Z_i` are **arbitrary independent real random variables**, and all `U_i,Z_i` are mutually independent. The laws of the `Z_i` may depend on `m`; they may be discrete, continuous, unbounded, heavy-tailed, multiscale or compound-Poisson. No moment or support assumption is made.

Every physical input nevertheless has a cap-one density. If `mu_i` is the law of `Z_i`, then

\[
f_i(x)=\int 1_{[-1/2,1/2]}(x-z)\,d\mu_i(z)
      =\mu_i([x-1/2,x+1/2])\le1,
\tag{1.5}
\]

and `int f_i=1`. Thus (1.4) is a broad fragmented product class inside the exact target.

Write

\[
S_m=P_m^TU,
\qquad z=P_m^TZ.
\tag{1.6}
\]

The three coordinates of `S_m` are independent normalized sums of `m` centered unit intervals, and after conditioning on all `Z`,

\[
Q_m:=X^TA_mX\mid Z
=(S_m+z)^TB(S_m+z).
\tag{1.7}
\]

The theorem below is uniform over the completely arbitrary translation vector `z`, hence over every law of `Z` above.

## 2. Main theorem

### `QFORM-UNIT-SMOOTHED-FRAGMENTED-DIFFUSE-CEILING-v1`

Let the family be as in (1.1)--(1.7), with a fixed `B` satisfying `s_3(B)>=1`. Then there is a deterministic sequence `delta_m(B)->0`, independent of **all** translation laws of the `Z_i`, such that

\[
\boxed{
\|p_{Q_m}\|_\infty\le3\sqrt2+\delta_m(B),
\qquad m\to\infty.
}
\tag{2.1}
\]

In fact the same estimate holds conditionally and uniformly over every deterministic translation vector:

\[
\boxed{
\sup_{z\in\mathbb R^3}
\|p_{(S_m+z)^TB(S_m+z)}\|_\infty
\le3\sqrt2+\delta_m(B).
}
\tag{2.2}
\]

Every finite `Q_m` in this class has a bounded continuous density.

For the canonical indefinite spectrum, the result is sharp inside this class. If

\[
B=O\,\mathrm{diag}(1,1,-1)\,O^T
\tag{2.3}
\]

for any orthogonal `O`, then

\[
\boxed{
\lim_{m\to\infty}
\sup_{\{\mathcal L(Z_i)\}}
\|p_{Q_m}\|_\infty=3\sqrt2.
}
\tag{2.4}
\]

The supremum is over all independent translation laws in (1.4), including `m`-dependent laws without moments. The lower bound in (2.4) is already achieved asymptotically by `Z_i=0`.

This theorem does **not** prove the full QFORM conjecture, nor does it prove the finite-`m` inequality `<=3 sqrt(2)`. It rules out a specific but broad multiscale mechanism: arbitrary random translations/fragmentation cannot improve the diffuse-bank asymptotic obstruction as long as every physical law retains an independent unit-width uniform smoothing core.

## 3. Required Claude result applied: uniform integrable Fourier envelope

Diagonalize

\[
B=O\Lambda O^T,
\qquad
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3).
\tag{3.1}
\]

The physical rank-three eigenframe is `R=P_mO`. Its rows have leverage

\[
\|R_{i,*}\|^2=1/m,
\tag{3.2}
\]

and

\[
G:=\sum_i R_{i,*}R_{i,*}^T=I_3.
\tag{3.3}
\]

Conditioning on `Z` converts (1.7) into a quadratic form in the independent physical uniforms `U_i`, with quadratic part `P_mBP_m^T` and an arbitrary linear term. For `m>=2`, every leverage is at most `1/2`.

Apply the completed Fresnel--Brascamp--Lieb **Theorem F** from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,  
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

(and independently audited in `FOURIER_ROUTE_REPORT.md` in the same source directory). The theorem explicitly allows arbitrary linear terms. With `I` equal to all `3m` coordinates and zero residual block, it gives, uniformly in `z`,

\[
|\phi_{m,z}(t)|
\le
\min\left\{1,
(4\pi)^{3/2}|\det B|^{-1/2}|t|^{-3/2}
\right\}.
\tag{3.4}
\]

In particular,

\[
\|p_{m,z}\|_\infty\le12|\det B|^{-1/3}\le12.
\tag{3.5}
\]

Equation (3.4), rather than the coarse constant (3.5), is the decisive input: it is an integrable characteristic-function envelope uniform over **every** translation vector, including translations whose size grows with `m`.

This is a genuine application of the required newest-Claude result to the still-unpaid witness class. No law-uniform one-dimensional pointwise stationary-phase estimate is asserted; (3.4) is the proved joint three-direction estimate under this exact low-leverage frame.

## 4. Uniform-bank local limit in total variation

Let `h_m` be the density of one coordinate of `S_m`, i.e.

\[
S_{m,1}=m^{-1/2}\sum_{k=1}^mU_k,
\qquad U_k\sim\mathrm{Unif}[-1/2,1/2],
\tag{4.1}
\]

and let

\[
\gamma(x)=\sqrt{\frac6\pi}\,e^{-6x^2}
\tag{4.2}
\]

be the `N(0,1/12)` density. Then

\[
\boxed{\|h_m-\gamma\|_1\longrightarrow0.}
\tag{4.3}
\]

For completeness, this needs no moment hypothesis beyond the explicit uniform summands. The characteristic function is

\[
\widehat h_m(\xi)
=\operatorname{sinc}\!\left(\frac{\xi}{2\sqrt m}\right)^m
\to e^{-\xi^2/24}.
\tag{4.4}
\]

On any fixed compact interval convergence is dominated. For `|u|` in a fixed neighbourhood of zero, `|sinc u|<=e^{-c u^2}` for an absolute `c>0`; after the substitution `u=xi/(2sqrt(m))` this gives a Gaussian majorant on the growing central region. Away from zero but in a fixed bounded `u`-region, `|sinc u|<=q<1`; in the far region `|sinc u|<=|u|^{-1}`. Splitting the Fourier integral into those three regions shows

\[
\int_{\mathbb R}
\left|\widehat h_m(\xi)-e^{-\xi^2/24}\right|d\xi\to0.
\tag{4.5}
\]

Fourier inversion therefore gives uniform convergence `h_m->gamma`; since both are nonnegative probability densities, Scheffe's lemma gives (4.3).

For the product densities

\[
H_m=h_m^{\otimes3},\qquad \Gamma=\gamma^{\otimes3},
\tag{4.6}
\]

telescoping yields

\[
\eta_m:=\|H_m-\Gamma\|_1
\le3\|h_m-\gamma\|_1\to0.
\tag{4.7}
\]

## 5. Uniform-in-translation local limit for the quadratic output

Let `G~N(0,I_3/12)` and define

\[
Q_{\infty,z}=(G+z)^TB(G+z).
\tag{5.1}
\]

For every `t` and every `z`, the modulus-one test function in the characteristic function gives directly from (4.7)

\[
|\phi_{m,z}(t)-\phi_{\infty,z}(t)|
\le\eta_m.
\tag{5.2}
\]

The Gaussian characteristic function has a second translation-uniform integrable envelope. In the diagonal coordinates of (3.1), the standard noncentral-square formula gives

\[
|\phi_{\infty,z}(t)|
\le
\prod_{j=1}^3
\left(1+\frac{t^2\lambda_j^2}{36}\right)^{-1/4}
\le
\left(1+\frac{t^2}{36}\right)^{-3/4}.
\tag{5.3}
\]

The noncentral exponential factor has modulus at most one, which is why (5.3) is uniform in `z`.

Combining (3.4), (5.2) and (5.3),

\[
\sup_z|\phi_{m,z}(t)-\phi_{\infty,z}(t)|
\to0
\quad\text{for every fixed }t,
\tag{5.4}
\]

and it is dominated by the integrable function

\[
\min\{1,(4\pi)^{3/2}|\det B|^{-1/2}|t|^{-3/2}\}
+
(1+t^2/36)^{-3/4}.
\tag{5.5}
\]

Dominated convergence therefore gives

\[
\delta_m(B):=rac1{2\pi}
\int_{\mathbb R}
\sup_z|\phi_{m,z}(t)-\phi_{\infty,z}(t)|dt
\longrightarrow0.
\tag{5.6}
\]

Both characteristic functions lie in `L^1`, so Fourier inversion gives the **uniform local limit**

\[
\boxed{
\sup_{z\in\mathbb R^3}\sup_{s\in\mathbb R}
|p_{m,z}(s)-p_{\infty,z}(s)|
\le\delta_m(B)\to0.
}
\tag{5.7}
\]

This is the essential strengthening over a weak CLT: the approximation is uniform over arbitrary translations, so no tightness or moment assumption on the translation laws is needed.

## 6. Designated partner applied: affine Gaussian ceiling

The completed designated partner `account03/B17` result is

`yspennstate/math-open-problems@dcf8885d5153370cacfa246ad1e29fb06d971769`,  
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T070310Z-account03-B17-QFORM-r25/REPORT.md`.

It proves that for every Gaussian `Y~N(mu,Sigma)` with `Sigma >= sigma^2 I` and every symmetric `B` with `s_3(B)>=1`,

\[
\|p_{Y^TBY}\|_\infty
\le\frac1{2\sqrt2\,\sigma^2}.
\tag{6.1}
\]

Apply (6.1) to `Y=G+z`, whose covariance is exactly `I_3/12`. Uniformly in `z`,

\[
\boxed{\|p_{\infty,z}\|_\infty\le3\sqrt2.}
\tag{6.2}
\]

Combining (5.7) and (6.2) proves the conditional estimate (2.2).

Finally, condition on all `Z`. The unconditional output law is the mixture of the conditional densities:

\[
p_{Q_m}(s)=\mathbb E_Z\,p_{m,P_m^TZ}(s).
\tag{6.3}
\]

Thus

\[
\|p_{Q_m}\|_\infty
\le\sup_z\|p_{m,z}\|_\infty
\le3\sqrt2+\delta_m(B),
\tag{6.4}
\]

which proves (2.1), uniformly over all translation laws.

Moreover the averaged characteristic function is dominated by (3.4), hence belongs to `L^1`; Fourier inversion shows that the unconditional `Q_m` also has a bounded continuous density for every `m>=2`.

## 7. Sharpness in the canonical indefinite class

Let `B=O diag(1,1,-1)O^T` and take every `Z_i=0`. Then `z=0`, while the Gaussian endpoint satisfies

\[
p_{\infty,0}(0)=3\sqrt2.
\tag{7.1}
\]

The uniform density convergence (5.7) yields

\[
p_{m,0}(0)\to3\sqrt2.
\tag{7.2}
\]

Therefore

\[
\liminf_m\sup_{\{\mathcal L(Z_i)\}}\|p_{Q_m}\|_\infty
\ge3\sqrt2.
\tag{7.3}
\]

The upper bound (6.4) gives the matching `limsup`, proving (2.4).

This is a sharp source-valid witness statement: every finite physical matrix has exact nonzero spectrum `{1,1,-1}`, and all physical input densities obey the original cap one.

## 8. What this rules out — and what it does not

The preceding `account03/B17` result showed that a fixed affine Gaussian mean cannot improve `3 sqrt(2)`. The present theorem closes a substantially stronger loophole: even **arbitrary random**, unbounded, `m`-dependent translations of every physical interval cannot create an asymptotic overshoot, because the low-leverage three-bank smoothing admits a translation-uniform `L^1` Fourier envelope.

Consequently a counterexample to the candidate sharp constant `3 sqrt(2)` cannot be obtained, in this diffuse three-bank geometry, merely by replacing each centered interval by a probability mixture of translated unit intervals—even a multiscale or compound-Poisson mixture. A sharper witness must break at least one ingredient, for example by using cap-one fragments whose intrinsic smoothing widths shrink with scale, macroscopic/shared-coordinate rows that survive outside the diffuse Gaussian core, or a different finite/mesoscopic geometry.

Failure of the auxiliary finite bound `12` to reach `3 sqrt(2)` is only a proof-constant limitation. Likewise, any future finite-`m` value above `3 sqrt(2)` in some other family would refute that **candidate sharp constant**, not the existence of a larger universal QFORM constant.

The full arbitrary-law, arbitrary-matrix conjecture remains OPEN.
