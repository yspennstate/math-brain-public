SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-24T04:07:02.722961Z.
attacking: almost-sure fragmented sharp witnesses — can a product law have diverging support gaps and probability tending one of visiting satellite components while the cone-tip density still tends to 3 sqrt(2)?

# QFORM-ALMOST-SURE-SATELLITE-DIVERGING-GAP-SHARP-WITNESS-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet03/B17`  
Run: `20260924T040702Z-fleet03-B17-QFORM-r11`  
Status: **PROVED SUPPORTING SHARP-WITNESS THEOREM / FULL TARGET OPEN**  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report constructs an exact rotated target family for which (i) all three nonzero eigenvalues have modulus at least one, (ii) the physical matrix is entrywise dense, (iii) every one-dimensional input density is disconnected with a support gap tending to infinity, (iv) the probability that at least one of the `3m` coordinates lands in a satellite component tends to one, yet (v) the output density at the cone tip converges to the sharp known obstruction `3 sqrt(2)`. Thus neither a globally overwhelming amount of fragmented-support usage nor diverging support diameter can by itself force a density improvement below the sharp obstruction.

No Gaussian assumption is imposed on the finite inputs. No post-rotation independence is used. No arbitrary-joint coarea inequality, conditional-density supremum, Monte Carlo histogram, centered-interval extremality claim, or law-uniform pointwise van-der-Corput estimate is used.

## 1. Exact target matrices (completed partner result applied)

Use the completed designated-partner `fleet04/B17` construction

`QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1`, scientific commit
`4be63022324b82f254f1d7a4353a3e883f08d10a`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260924T011922Z-fleet04-B17-QFORM-r6/REPORT.md`.

It fixes

\[
n={1\over\sqrt{14}}(1,2,3)^T,\qquad
B_m=I_3-\left(2+{1\over m}\right)nn^T,
\]

and the `3m x 3` bank synthesis matrix `R_m` with `m` copies of `e_j/sqrt(m)` in bank `j`. Since `R_m^T R_m=I_3`,

\[
A_m=R_m B_m R_m^T
\]

has exact nonzero spectrum

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-(1+1/m)\}.}\tag{1.1}
\]

Every entry of `B_m`, hence every physical entry of `A_m`, is nonzero. Therefore every finite member is an entrywise-dense exact instance of the owner's target, with strict negative spectral slack.

The partner theorem also proves for its two-interval marginal with main length `1-theta/m` the exact mixture inequality

\[
\|p_{Q_m}\|_\infty\ge
(1-\theta/m)^{3m-2}\|p_{Q_m^0}\|_\infty,\tag{1.2}
\]

and, after applying the completed diffuse-bank limit, the actual target-level inequality

\[
\liminf_m\|p_{Q_m}\|_\infty\ge 3\sqrt2 e^{-3\theta}.\tag{1.3}
\]

Below I specialize the partner matrix and support geometry to a slower satellite displacement, prove that the satellite cells omitted by (1.2) asymptotically restore the **entire** `3 sqrt(2)` cone-tip height, and then push the satellite intensity so far that the all-main event has probability tending zero.

## 2. New almost-sure-satellite input family

For `m>=16`, set

\[
\varepsilon_m=m^{-3/4},\qquad
\ell_m=1-\varepsilon_m,\qquad
R_m^\star=m^{1/8}.
\tag{2.1}
\]

Every one of the `3m` original coordinates is independent with density

\[
\boxed{
f_m(x)=
\mathbf 1_{[-\ell_m/2,\ell_m/2]}(x)
+\mathbf 1_{[R_m^\star,R_m^\star+\varepsilon_m]}(x).
}\tag{2.2}
\]

This is an exactly normalized probability density with `0<=f_m<=1`, since the two component lengths sum to one. The support is disconnected and

\[
\operatorname{gap}(\operatorname{supp}f_m)
\ge R_m^\star-1/2\longrightarrow\infty.\tag{2.3}
\]

Let `S_m` be the event that at least one of the `3m` coordinates falls in its satellite interval. Then

\[
\mathbb P(S_m)=1-(1-\varepsilon_m)^{3m}.
\]

Because `m epsilon_m=m^{1/4}->infinity`,

\[
\boxed{\mathbb P(S_m)\longrightarrow1.}\tag{2.4}
\]

Thus the all-main product cell has probability tending **zero**, not merely a fixed number below one.

## 3. Bank sums still converge locally to the minimum-variance Gaussian

Let `X_m` have density (2.2), let `X_{m,1},...,X_{m,m}` be iid copies, and define one bank sum

\[
Y_m={1\over\sqrt m}\sum_{k=1}^mX_{m,k}.
\tag{3.1}
\]

The three spectral banks in `R_m^T X` are independent copies of `Y_m` because they use disjoint original coordinates.

### 3.1 Exact first two moments

The one-coordinate mean is

\[
\mu_m=R_m^\star\varepsilon_m+{\varepsilon_m^2\over2},\tag{3.2}
\]

so

\[
\sqrt m\,\mu_m
=m^{-1/8}+{1\over2}m^{-1}\longrightarrow0.\tag{3.3}
\]

The raw second moment is

\[
\mathbb EX_m^2={\ell_m^3\over12}
+(R_m^\star)^2\varepsilon_m
+R_m^\star\varepsilon_m^2
+{\varepsilon_m^3\over3}.
\tag{3.4}
\]

Hence, writing `sigma_m^2=Var(X_m)`, direct expansion gives

\[
\sigma_m^2={1\over12}
+\big((R_m^\star)^2-1/4\big)\varepsilon_m
+\big(R_m^\star+1/4-(R_m^\star)^2\big)\varepsilon_m^2
+\big(1/4-R_m^\star\big)\varepsilon_m^3
-{\varepsilon_m^4\over4}.
\tag{3.5}
\]

Since `(R_m^star)^2 epsilon_m=m^{-1/2}`,

\[
\boxed{\sigma_m^2\longrightarrow {1\over12}.}\tag{3.6}
\]

The satellite contribution to the third absolute moment is at most

\[
\varepsilon_m(R_m^\star+1)^3=O(m^{-3/8}),\tag{3.7}
\]

so the centered standardized third absolute moments remain uniformly bounded.

### 3.2 Self-contained triangular local CLT

Let

\[
W_m={X_m-\mu_m\over\sigma_m},
\qquad \chi_m(s)=\mathbb E e^{isW_m}.
\]

The preceding uniform third-moment bound and `sigma_m -> 1/sqrt(12)>0` give, uniformly for small `|s|`,

\[
\chi_m(s)=1-{s^2\over2}+O(|s|^3),\qquad
|\chi_m(s)|\le e^{-c s^2}.\tag{3.8}
\]

For every fixed `0<delta<K`, `f_m -> 1_{[-1/2,1/2]}` in `L^1` with distance `2 epsilon_m`, while the centering and variance parameters converge. Therefore

\[
\sup_{\delta\le |s|\le K}|\chi_m(s)|\le\rho_{\delta,K}<1
\tag{3.9}
\]

for all sufficiently large `m`.

For high frequencies, the exact two-interval form gives a location-independent bound. For an interval `I` of length `L`,

\[
\left|\int_I e^{itx}\,dx\right|\le\min(L,2/|t|).
\]

Consequently, after the harmless fixed variance rescaling,

\[
|\chi_m(s)|\le {C\over |s|}+\varepsilon_m.\tag{3.10}
\]

Choose fixed `K` so that `C/K<1/4`. On `K<=|s|<=C'/epsilon_m`, (3.10) is at most a fixed number below one; for `|s|>=C'/epsilon_m`, both interval integrals are bounded by `C''/|s|`. Since `epsilon_m=m^{-3/4}` is only polynomially small,

\[
\sqrt m\int_{|s|\ge\delta}|\chi_m(s)|^m ds\longrightarrow0.\tag{3.11}
\]

Combining (3.8)--(3.11) with the change of variables `t=s sqrt(m)` gives

\[
\int_{\mathbb R}
\left|\chi_m(t/\sqrt m)^m-e^{-t^2/2}\right|dt\longrightarrow0.\tag{3.12}
\]

Fourier inversion therefore yields the uniform local CLT

\[
\boxed{
\|g_m-\gamma_{1/12}\|_\infty\longrightarrow0,
}\tag{3.13}
\]

where `g_m` is the density of `Y_m` and

\[
\gamma_{1/12}(y)=\sqrt{6/\pi}\,e^{-6y^2}.
\]

The same proof also gives one constant `C_0` such that

\[
\sup_m\|g_m\|_\infty\le C_0\tag{3.14}
\]

for all sufficiently large `m`.

This is a local CLT for the actual disconnected cap-one triangular array; it does not assume Gaussian finite inputs.

## 4. Exact cone-tip formula for the rotated strict-slack matrix

Write

\[
q_m(y)=y^T B_m y,
\qquad \alpha_m=2+1/m,
\qquad \beta_m=1+1/m.
\]

Fix an orthonormal basis `e_1,e_2` of `n^perp`, put

\[
v(\theta)=\cos\theta\,e_1+\sin\theta\,e_2,
\]

and define the two null circles on `S^2` by

\[
\omega_m^\pm(\theta)=
\pm {n\over\sqrt{\alpha_m}}
+\sqrt{\beta_m\over\alpha_m}\,v(\theta).
\tag{4.1}
\]

Indeed `q_m(omega_m^pm)=0`. On these circles

\[
|\partial_\theta\omega_m^\pm|=\sqrt{\beta_m/\alpha_m},
\qquad
|\nabla_{S^2}q_m|=2\sqrt{\beta_m}.
\tag{4.2}
\]

Let

\[
\rho_m(y)=g_m(y_1)g_m(y_2)g_m(y_3).
\]

Spherical coarea for the homogeneous quadratic form therefore gives the exact cone-tip density

\[
\boxed{
p_m(0)=
{1\over2\sqrt{\alpha_m}}
\sum_{\pm}\int_0^{2\pi}\int_0^\infty
\rho_m(r\omega_m^\pm(\theta))\,dr\,d\theta.
}\tag{4.3}
\]

No symmetry of `g_m` is assumed; both null sheets are retained separately.

The ray integrals are uniformly tight. Since every unit vector has some coordinate of magnitude at least `1/sqrt(3)`, (3.14) gives

\[
\rho_m(r\omega)\le C_0^2 g_m(r\omega_j)
\]

for some `j=j(omega)`. Therefore

\[
\int_M^\infty\rho_m(r\omega)\,dr
\le C_0^2\sqrt3\,
\mathbb P\{|Y_m|\ge M/\sqrt3\}.
\tag{4.4}
\]

The means of `Y_m` tend to zero and their variances stay bounded, so Chebyshev yields

\[
\sup_{m,\omega}\int_M^\infty\rho_m(r\omega)dr
\le {C_1\over M^2}\longrightarrow0.
\tag{4.5}
\]

On every finite `0<=r<=M`, (3.13) and `omega_m^pm -> omega_infty^pm` give uniform convergence of the integrand in (4.3). The tail estimate (4.5) therefore permits passage to the limit.

## 5. Sharp cone-tip limit survives almost-sure fragmentation

For the limit covariance `v=1/12`, the latent Gaussian density is radial,

\[
\rho_\infty(y)=(2\pi v)^{-3/2}e^{-|y|^2/(2v)}.
\]

Since `alpha_m->2`, (4.3) gives

\[
\begin{aligned}
\lim_{m\to\infty}p_m(0)
&={1\over\sqrt2}(2\pi)(2\pi v)^{-3/2}
\int_0^\infty e^{-r^2/(2v)}dr\\
&={1\over2\sqrt2\,v}
=3\sqrt2.
\end{aligned}
\tag{5.1}
\]

Thus the new exact target family satisfies simultaneously

\[
\boxed{
\operatorname{spec}_{\ne0}(A_m)=\{1,1,-(1+1/m)\},
}\tag{5.2}
\]

\[
\boxed{
\operatorname{gap}(\operatorname{supp}f_m)\to\infty,
\qquad
\mathbb P(S_m)\to1,
}\tag{5.3}
\]

and

\[
\boxed{
p_{X^TA_mX}(0)\longrightarrow3\sqrt2.}\tag{5.4}
\]

In particular,

\[
\boxed{C_*\ge3\sqrt2}\tag{5.5}
\]

is witnessed by a family in which **almost every product sample uses at least one remote support component**.

This is stronger than the fixed-`theta` main-cell estimate (1.3): the sharp cone-tip obstruction does not require a positive-probability all-main cell at all.

## 6. Direct strengthening of the designated partner inequality

Return briefly to the partner's exact law with

\[
\varepsilon_m=\theta/m,
\qquad \ell_m=1-\theta/m,
\]

but specialize its freely chosen satellite location to

\[
R_m^\star=m^{1/8}.
\]

The completed partner inequality (1.3) gives

\[
\liminf_m\|p_{Q_m}\|_\infty\ge3\sqrt2 e^{-3\theta}.
\tag{6.1}
\]

For this slow-gap specialization, the same local-CLT/coarea argument above has

\[
\sqrt m\,\mu_m=O(m^{-3/8}),
\qquad
\sigma_m^2=1/12+O(m^{-3/4}),
\qquad
\varepsilon_m(R_m^\star)^3=O(m^{-5/8}),
\]

and therefore proves the strictly stronger actual inequality

\[
\boxed{
p_{Q_m}(0)\to3\sqrt2,
\qquad
\|p_{Q_m}\|_\infty\ge p_{Q_m}(0)=3\sqrt2-o(1).
}\tag{6.2}
\]

Meanwhile

\[
\mathbb P(S_m)\to1-e^{-3\theta}.
\]

So, in this valid specialization, the positive mixture pieces omitted by the partner's all-main lower bound asymptotically recover exactly the factor `e^{3 theta}` that (6.1) loses. This is an explicit application and sharpening of a completed partner result, not a parallel restatement.

## 7. Continuity scope

For each fixed sufficiently large `m`, the bank density `g_m` is an `m`-fold convolution of finite unions of interval indicators and is therefore compactly supported and `C^2` once `m` is large enough. Since `B_m` is nonsingular, standard stationary phase for the three-dimensional nondegenerate quadratic phase gives an integrable `O(|t|^{-3/2})` characteristic-function tail. Hence each constructed finite output has a continuous `C_0` density.

This continuity statement is **only for the constructed family**. Full-target continuity for arbitrary cap-one inputs remains open.

## 8. What this rules out and what remains

A universal proof cannot argue that fragmented supports are harmless merely because one can isolate a dominant all-main product cell. In the family above the all-main probability tends zero, the support gap tends infinity, yet the sharp known concentration obstruction remains.

The mechanism is transparent: each coordinate has satellite mass `m^{-3/4}`, so there are `m^{1/4}` satellite hits on average across a bank, but their normalized aggregate displacement is only

\[
{m^{1/4}m^{1/8}\over\sqrt m}=m^{-1/8}\to0.
\]

At the same time the satellite contribution to the variance is `m^{-1/2}` and to the third absolute moment is `m^{-3/8}`. Thus product-level fragmentation can be overwhelming while spectral-bank-level contamination vanishes.

The unrestricted theorem remains open. A witness strictly above `3 sqrt(2)`, if one exists, must exploit a mechanism not captured by this asymptotically minimum-variance three-bank regime: e.g. a surviving non-Gaussian macroscopic component, negative two-sheet off-tip concentration, several interacting macroscopic shared rows, or additional active spectrum.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.  
Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**.
