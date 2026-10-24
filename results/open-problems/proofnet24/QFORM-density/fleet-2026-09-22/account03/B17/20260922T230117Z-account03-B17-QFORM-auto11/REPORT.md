# QFORM-B17 rare-fragment first-order barrier

Run: `20260922T230117Z-account03-B17-QFORM-auto11`  
Account/slot: `account03/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control observed before publication: revision `2026-09-22.15`  
Status: `NEW_SUPPORTING_THEOREM`; full conjecture OPEN; full continuity OPEN; `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and purpose

The full target is unchanged: for every dimension, every product law with independent real coordinates whose densities are bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a valid counterexample.

This report tests the next sharp-witness mechanism left open by the preceding B17 work: **vanishing-intensity, mesoscopic fragmented perturbations** of the fully rotated uniform-bank witness. The goal is to decide whether a tiny amount of cap-one mass moved to distance `Theta(sqrt(m))` can reverse the negative local Edgeworth correction and push the zero density above the known obstruction `3 sqrt(2)`.

The answer is negative for an explicit broad triangular-array class: such fragments make the first-order correction strictly *more negative*. The mechanism is an exact noncentral-Gaussian inequality at the cone tip.

## 2. Completed partner input actually used

The designated partner `account04/B17` proved at

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`

that, with

\[
J=\operatorname{diag}(1,1,-1),\qquad
O={1\over7}\begin{pmatrix}6&-2&-3\\-2&3&-6\\-3&-6&-2\end{pmatrix},
\]

and

\[
B=O^TJO={1\over49}\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix},
\]

the three-bank centered-uniform witness satisfies

\[
\boxed{
 p^{\rm unif}_{m}(0)=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right).
}
\tag{2.1}
\]

The partner also proves the weighted local Edgeworth expansion with an integrable polynomially weighted remainder. I use (2.1) as the exact unfragmented first-order term and do not re-prove it.

## 3. Explicit admissible fragmented law

Fix constants `a>0` and `c>0`. Put

\[
\varepsilon_m={c\over m^2}
\]

for all sufficiently large `m` so that `epsilon_m<1`, and let

\[
R_m=
\left[a\sqrt m-\frac{\varepsilon_m}{4},a\sqrt m+\frac{\varepsilon_m}{4}\right]
\cup
\left[-a\sqrt m-\frac{\varepsilon_m}{4},-a\sqrt m+\frac{\varepsilon_m}{4}\right].
\]

The total length of `R_m` is exactly `epsilon_m`. Define

\[
f_m(x)=(1-\varepsilon_m)\mathbf 1_{[-1/2,1/2]}(x)+\mathbf 1_{R_m}(x).
\tag{3.1}
\]

Then `0<=f_m<=1` and

\[
\int f_m=(1-\varepsilon_m)+|R_m|=1.
\]

Thus every `f_m` is an exact admissible density. It is a genuine fragmented law with tiny total remote mass `epsilon_m` placed at distance `a sqrt(m)`.

Take `3m` independent coordinates `X_{jk}` with density `f_m`, form the three independent bank sums

\[
Y_{mj}=m^{-1/2}\sum_{k=1}^mX_{jk},\qquad 1\le j\le3,
\]

and set

\[
Q_m=Y_m^T B Y_m.
\tag{3.2}
\]

Equivalently, if the physical row `O e_j/sqrt(m)` is repeated `m` times, the resulting `3m x 3m` matrix is

\[
A_m=R_m^{\rm frame}J(R_m^{\rm frame})^T,
\]

and its nonzero spectrum is **exactly** `{1,1,-1}` for every finite `m`. Hence (3.2) obeys the full spectral hypothesis exactly.

## 4. Exact Gaussian cone-tip lemma

Let `G~N(h,v I_3)` with `v>0`, and let

\[
S_h=G_1^2+G_2^2-G_3^2.
\]

Write

\[
\alpha={h_1^2+h_2^2\over v},\qquad
\beta={h_3^2\over v}.
\]

Then

\[
{G_1^2+G_2^2\over v}\sim\chi^2_2(\alpha),\qquad
{G_3^2\over v}\sim\chi^2_1(\beta),
\]

independently. Poisson expansion of the two noncentral chi-square laws gives

\[
{p_{S_h}(0)\over p_{S_0}(0)}
=\mathbb E\,r_{K,L},
\tag{4.1}
\]

where

\[
K\sim\mathrm{Pois}(\alpha/2),\qquad
L\sim\mathrm{Pois}(\beta/2)
\]

are independent and

\[
r_{k,l}={\Gamma(k+l+1/2)\over 2^{k+l}k!\,\Gamma(l+1/2)}.
\tag{4.2}
\]

Indeed, conditionally on `(K,L)=(k,l)`, the two central chi-square degrees of freedom are `2+2k` and `1+2l`, and

\[
\int_0^\infty f_{\chi^2_{2+2k}}(u)f_{\chi^2_{1+2l}}(u)\,du
={\Gamma(k+l+1/2)\over 2^{k+l+3/2}k!\Gamma(l+1/2)}.
\]

The central value is

\[
p_{S_0}(0)={1\over2\sqrt2\,v}.
\tag{4.3}
\]

### Lemma 4.1: sharp discrete coefficient bound

\[
r_{0,0}=1,
\qquad
\sup_{(k,l)\ne(0,0)}r_{k,l}={1\over2}.
\tag{4.4}
\]

Proof. Define the negative-binomial probability mass

\[
p_k^{(r)}={ (r)_k\over k!\,2^{k+r}},\qquad k\ge0.
\]

Then `r_{k,l}=sqrt(2) p_k^{(l+1/2)}`.

For `l=0`, the sequence `p_k^(1/2)` strictly decreases after `k=0`, and

\[
r_{k,0}\le r_{1,0}={1\over4}\qquad(k\ge1).
\]

For `l>=1`, the negative-binomial additivity identity gives

\[
p^{(l+1/2)}=p^{(3/2)}*p^{(l-1)}
\]

(with `p^(0)` interpreted as the point mass at zero when `l=1`). Convolution with a probability mass cannot increase the discrete `l^infinity` norm. Since

\[
\sup_k p_k^{(3/2)}=p_0^{(3/2)}=2^{-3/2},
\]

we obtain `r_{k,l}<=1/2` for every `l>=1`. Equality occurs at `(k,l)=(0,1)`. This proves (4.4).  
`□`

Since

\[
\Pr(K=L=0)=e^{-(\alpha+\beta)/2}
=e^{-\|h\|^2/(2v)},
\]

(4.1)-(4.4) yield the quantitative cone-tip inequality

\[
\boxed{
{p_{S_h}(0)\over p_{S_0}(0)}
\le {1+e^{-\|h\|^2/(2v)}\over2}.
}
\tag{4.5}
\]

In particular, every nonzero deterministic Gaussian mean shift strictly lowers the zero density. This statement is orientation-free because any inertia `(2,1)` orthogonal conjugate reduces to `J`.

At the density-one Gaussian variance floor `v=1/12`, a shift of norm `a` obeys

\[
\boxed{
{p_{S_h}(0)\over 3\sqrt2}
\le {1+e^{-6a^2}\over2}.
}
\tag{4.6}
\]

This lemma is the key barrier: a rare mesoscopic fragment becomes a deterministic `O(1)` mean shift in the bank CLT, and such a shift cannot increase the cone-tip density.

## 5. First-order bank expansion for the fragmented law

Let `sigma^2=1/12` and let `gamma_sigma` be the centered Gaussian density with that variance. For one coordinate, after the bank normalization `1/sqrt(m)`, the centered-interval characteristic function is

\[
u_m(t)=\operatorname{sinc}\!\left({t\over2\sqrt m}\right).
\]

Conditioned on the remote component in (3.1), the characteristic function is

\[
r_m(t)=\cos(at)\,
\operatorname{sinc}\!\left({\varepsilon_m t\over4\sqrt m}\right).
\]

Hence the characteristic function of one bank sum is

\[
\Phi_m(t)=\left[(1-\varepsilon_m)u_m(t)+\varepsilon_m r_m(t)\right]^m.
\tag{5.1}
\]

For fixed `a,c`, expansion of `log sinc` and `epsilon_m=c/m^2` gives, uniformly on every fixed compact `t`-interval,

\[
\log\Phi_m(t)
=-{\sigma^2t^2\over2}
-{t^4\over2880m}
+{c\over m}(\cos(at)-1)
+O_{a,c,t}(m^{-2}).
\tag{5.2}
\]

The same three-zone Fourier estimate used in the partner's weighted Edgeworth lemma remains valid here: the core has weight `1-epsilon_m`, while the remote term has total weight `epsilon_m=O(m^-2)`. On `|t|<=m^{1/8}`, Taylor expansion gives (5.2) with derivative bounds. On `m^{1/8}<|t|<=sqrt(m)`, the centered-interval factor gives Gaussian-type damping after the `m`th power. On `|t|>sqrt(m)`, `|sinc x|<=min(1,|x|^-1)` and the `O(m^-2)` remote weight leave an integrable tail after the `m`th power. Applying the same estimates after finitely many derivatives yields the weighted local expansion

\[
\boxed{
\begin{aligned}
g_m(y)=&\,\gamma_\sigma(y)
\left[1-{1\over20m}H_4(y/\sigma)\right]\\
&+{c\over m}
\left[{\gamma_\sigma(y-a)+\gamma_\sigma(y+a)\over2}-\gamma_\sigma(y)\right]
+o_w(m^{-1}),
\end{aligned}}
\tag{5.3}
\]

where `o_w(m^-1)` is small in a polynomially weighted supremum norm strong enough to integrate against the rank-three cone coarea kernel. The coefficient `-1/20` is exactly the partner's uniform Edgeworth coefficient; the new term is the Fourier inverse of

\[
c(\cos(at)-1)e^{-\sigma^2t^2/2}.
\]

The quadratic cone singularity at the origin is integrable in dimension three, so the coarea functional is continuous under the weighted remainder in (5.3).

## 6. First-order density formula and strict fragment penalty

Let

\[
\mathcal C_B(g_1,g_2,g_3)
=\int_{y^TBy=0}{g_1(y_1)g_2(y_2)g_3(y_3)\over|2By|}\,d\mathcal H^2(y).
\]

This is trilinear in the three bank densities. Inserting (5.3), the uniform Edgeworth contribution is exactly the completed partner coefficient from (2.1). The fragment term in bank `j` replaces one centered Gaussian by the symmetric mixture shifted by `+/- a e_j`. Since

\[
y^TBy=(Oy)^TJ(Oy),
\]

this becomes an isotropic Gaussian with spectral mean shift

\[
h_j=\pm a\,Oe_j.
\]

Because `O` is orthogonal, `||h_j||=a`. Define

\[
R_j(a)={p_{N(h_j,\sigma^2I)^T J N(h_j,\sigma^2I)}(0)\over3\sqrt2}.
\]

Then

\[
\boxed{
{p_{Q_m}(0)\over3\sqrt2}
=1-{5295\over21952m}
+{c\over m}\sum_{j=1}^3(R_j(a)-1)
+o(m^{-1}).
}
\tag{6.1}
\]

By (4.6), every `R_j(a)` satisfies

\[
R_j(a)\le {1+e^{-6a^2}\over2}<1.
\]

Therefore

\[
\boxed{
\limsup_{m\to\infty}
 m\left({p_{Q_m}(0)\over3\sqrt2}-1\right)
\le
-{5295\over21952}
-{3c\over2}(1-e^{-6a^2})<0.
}
\tag{6.2}
\]

This is the main result.

### Exact orientation parameters for the partner matrix

For completeness, if

\[
u_j=O_{3j}^2,
\]

then

\[
(u_1,u_2,u_3)=\left({9\over49},{36\over49},{4\over49}\right).
\]

For the shift `h_j=a Oe_j`, the two noncentrality parameters in (4.1) are

\[
\alpha_j=12a^2(1-u_j),\qquad
\beta_j=12a^2u_j,
\]

and `alpha_j+beta_j=12a^2` for all `j`. Thus the exact ratios are

\[
R_j(a)=\mathbb E\,r_{K_j,L_j},
\quad
K_j\sim\mathrm{Pois}(\alpha_j/2),
\quad
L_j\sim\mathrm{Pois}(\beta_j/2).
\tag{6.3}
\]

For the concrete choice `a=c=1`, numerical summation of the absolutely convergent Poisson series gives

\[
(R_1,R_2,R_3)
\approx(0.08230978794,\;0.14920636662,\;0.04389388561),
\]

so the actual first-order deficit coefficient is

\[
{5295\over21952}+\sum_j(1-R_j)
\approx2.96579805020,
\]

far larger than the unfragmented deficit `5295/21952 approximately 0.24120809`. This numerical evaluation is only a check; the rigorous sign and quantitative lower penalty are already supplied by (6.2).

## 7. Generalization of the mechanism

The same first-order argument does not depend on choosing exactly two point-like remote intervals. Suppose in bank `j` the coordinate law is an admissible mixture with rare mass `c_j/m^2`, and conditional on that rare component the normalized displacement `X/sqrt(m)` converges to a compactly supported probability law `nu_j`. Then the fragment contribution in (6.1) is replaced by

\[
{c_j\over m}
\left[
\int {p_{S_{O h}}(0)\over p_{S_0}(0)}\,d\nu_j(h)-1
\right].
\]

By (4.5) it is nonpositive, and strictly negative unless the limiting rare displacement is concentrated at zero. Therefore **any vanishing-intensity `m^{-2}` mesoscopic fragment perturbation of this fixed rotated Gaussian-core witness can only decrease the cone-tip density at first order**.

This does not cover fragment intensities of order `1/m` (which have a nontrivial compound-Poisson limit), growing/nonperiodic frames, multiscale fragment populations without a compact limiting displacement law, or arbitrary finite-leverage full matrices. Those remain distinct mechanisms.

## 8. Consequence for the sharp-constant search

The universal lower bound remains

\[
\boxed{C\ge3\sqrt2.}
\]

No larger lower bound is obtained here. Instead, a previously plausible way to beat `3 sqrt(2)` is eliminated:

* fixed-period centered-uniform rotations already approach `3 sqrt(2)` from below by the completed partner theorem;
* adding cap-one remote fragments of total coordinate mass `Theta(m^-2)` at distance `Theta(sqrt(m))` produces `O(1/m)` rare Gaussian mean shifts;
* every such noncentral Gaussian shift lowers the zero density, with the explicit factor (4.5);
* hence the fragment correction cannot reverse the partner's negative Edgeworth term.

A stronger witness must therefore use a genuinely different scale: e.g. order-`1/m` rare mass with a nontrivial compound-Poisson limit, a multiscale population not reducible to isolated mean shifts, a growing/nonperiodic frame, or a finite/mesoscopic mechanism away from the Gaussian cone-tip perturbative regime.

## 9. Continuity scope

For each fixed sufficiently large `m`, each bank density is an `m`-fold convolution of bounded compactly supported interval densities, hence is continuous (indeed piecewise smooth with increasing regularity as `m` grows). The nonsingular rank-three quadratic cone has locally integrable coarea singularity. The same cone parametrization and dominated-convergence argument used in the partner report therefore gives a continuous density for this explicit witness family.

This says **nothing** about continuity for the full target. The full continuity claim remains open.

## 10. Source/correction discipline

No pointwise law-uniform van-der-Corput decay, arbitrary-joint coarea bound, conditional density-cap substitution, fiber-sup dimension-free bound, one-minor extraction, or histogram extremality assertion is used. The live correction inbox was refreshed before publication. The only peer theorem imported quantitatively is the completed `account04/B17` local Edgeworth/coarea expansion pinned above.

No Monte Carlo evidence is used as proof. The companion checker verifies the exact matrix arithmetic, the orientation parameters, the discrete coefficient maximum on a large finite grid, and the convergent Poisson-series evaluations used only for the concrete numerical illustration.

## 11. Remaining connection to the full theorem

This is a sharp-witness barrier, not a universal upper bound. It narrows the search around the strongest known lower obstruction but does not control arbitrary product densities or arbitrary extra spectrum. The full conjecture remains OPEN.

The next B17 mechanism should leave the vanishing-intensity Gaussian perturbative class: a natural target is the order-`1/m` fragmented regime with a genuine compound-Poisson limit in a **shared-coordinate rotated frame**, or a multiscale construction whose local law is not a convex mixture of noncentral Gaussian cone-tip profiles.
