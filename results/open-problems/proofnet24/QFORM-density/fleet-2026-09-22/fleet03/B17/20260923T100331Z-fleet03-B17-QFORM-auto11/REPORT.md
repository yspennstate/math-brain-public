SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-23T10:03:31Z.
attacking: multiscale fragmented three-bank witnesses beyond the Gaussian ceiling; finite-activity compound-Poisson perturbations of the sharp rotated family.

# Finite-activity fragmented diffuse banks cannot beat the `3 sqrt(2)` obstruction

## Status and scope

This report proves a new supporting sharp-witness theorem.  It does **not** prove the full arbitrary-input QFORM conjecture.  The unrestricted universal density upper bound and the full-target continuity conclusion remain open.


The designated completed partner result actually used is fleet04/B17:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.

It gives the exact rational rotated frame and the weighted local Edgeworth estimate
\[
g_n(x)=\gamma_\sigma(x)\left[1-{1\over20n}H_4(x/\sigma)\right]
 +O(n^{-2})(1+|x|)^{-8},\qquad \sigma^2={1\over12},
\]
together with
\[
p_{Q_n^{(0)}}(0)=3\sqrt2\left(1-{5295\over21952n}+O(n^{-2})\right).
\tag{P}
\]
Thus every universal constant satisfies `C_* >= 3 sqrt(2)`.

A worker-owned dependency used below is the arbitrary-mean Gaussian ceiling

`yspennstate/math-open-problems@dcf8885d5153370cacfa246ad1e29fb06d971769`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T070310Z-fleet03-B17-QFORM-r25/REPORT.md`.

It proves that if `G~N(h,I_3/12)` and `J=diag(1,1,-1)`, then
\[
\|p_{G^TJG}\|_\infty\le3\sqrt2
\tag{G}
\]
for every `h`, and at the cone tip
\[
p_{G^TJG}(0)\le3\sqrt2\,{1+e^{-6\|h\|^2}\over2}.
\tag{GT}
\]

## 1. Compact end-to-end argument

Take the exact partner rotation
\[
O={1\over7}\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix},\qquad J=\operatorname{diag}(1,1,-1),
\]
so
\[
B=O^TJO={1\over49}\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix}.
\]
For each physical bank `j=1,2,3`, replace the centered unit interval law by a cap-one law with probability `lambda_j/m` placed in a remote interval at distance `a_j sqrt(m)`.  The normalized bank sum then converges locally, with polynomial weight, to
\[
Y_j=G_j+a_jN_j,
\qquad G_j\sim N(0,1/12),\quad N_j\sim\operatorname{Poisson}(\lambda_j),
\]
independently.  Hence the spectral vector converges to
\[
OY=G+H,\qquad G\sim N(0,I_3/12),\quad H=O(a_1N_1,a_2N_2,a_3N_3)^T,
\]
with `G` independent of `H`.  Conditional on `H=h`, (G) gives density at most `3 sqrt(2)`.  Averaging in `H` therefore gives
\[
\|p_{(G+H)^TJ(G+H)}\|_\infty\le3\sqrt2.
\tag{1}
\]

The partner weighted Edgeworth estimate implies a polynomially weighted local limit theorem for the fragmented bank sums.  A direct cylindrical formula for the `(2,1)` quadratic pushforward then upgrades the bank local limit to **uniform convergence of the entire output density**.  Consequently the exact finite cap-one fragmented family satisfies
\[
\boxed{\limsup_{m\to\infty}\|p_{Q_m}\|_\infty\le3\sqrt2.}
\tag{2}
\]
Combining (2) with the partner saturation (P),
\[
\boxed{
\limsup_m\|p_{Q_m^{\rm frag}}\|_\infty
\le3\sqrt2
=\lim_m p_{Q_m^{(0)}}(0)
\le C_* .
}
\tag{3}
\]
Thus finite-activity `1/m` fragmentation at the critical remote distance `sqrt(m)` cannot yield an asymptotic witness above the current sharp obstruction.

The rest of the report proves each step.

## 2. Exact source-valid fragmented family

Fix `lambda_j>=0` and nonzero real `a_j`.  For all sufficiently large `m` with `lambda_j<m`, put
\[
I=[-1/2,1/2],
\]
and let
\[
R_{j,m}=\left[a_j\sqrt m-{\lambda_j\over2m},
                    a_j\sqrt m+{\lambda_j\over2m}\right],
\]
chosen disjoint from `I`.  Define the physical one-coordinate density
\[
f_{j,m}(x)=\left(1-{\lambda_j\over m}\right){\bf1}_I(x)
            +{\bf1}_{R_{j,m}}(x).
\tag{4}
\]
Then
\[
0\le f_{j,m}\le1,
\qquad \int f_{j,m}=1.
\]
No moment, log-concavity, connected-support, or Gaussian hypothesis is being imposed; the support is deliberately fragmented and its diameter grows like `sqrt(m)`.

Let the `3m` inputs `X_{jk}^{(m)}` be independent with density (4), and define
\[
Y_{j,m}={1\over\sqrt m}\sum_{k=1}^mX_{jk}^{(m)}.
\]
Use the same repeated physical rows as the partner: repeat `Oe_j/sqrt(m)` for bank `j`.  If `R_m` is that `3m x 3` row matrix, set
\[
A_m=R_mJR_m^T,
\qquad Q_m=X^TA_mX=Y_m^TBY_m.
\tag{5}
\]
Exactly as in the partner construction,
\[
R_m^TR_m=I_3,
\]
so the exact nonzero spectrum of every finite `A_m` is
\[
\boxed{\{1,1,-1\}.}
\tag{6}
\]
All nine entries of `B` are nonzero, hence this is a genuinely rotated three-bank form rather than a diagonal control.

## 3. One-bank Gaussian-plus-Poisson local limit

The law (4) has the exact selector representation
\[
X=(1-\xi)U+\xi(a\sqrt m+V_m),
\]
where
\[
\xi\sim\operatorname{Bernoulli}(\lambda/m),\quad
U\sim\operatorname{Unif}[-1/2,1/2],\quad
V_m\sim\operatorname{Unif}[-\lambda/(2m),\lambda/(2m)],
\]
independently.  If
\[
N_m=\sum_{k=1}^m\xi_k\sim\operatorname{Bin}(m,\lambda/m),
\]
then conditional on `N_m=k`,
\[
Y_m=ak+T_{m,k}+E_{m,k},
\tag{7}
\]
where
\[
T_{m,k}={1\over\sqrt m}\sum_{r=1}^{m-k}U_r,
\qquad
|E_{m,k}|\le {k\lambda\over2m^{3/2}}.
\]

Let `g_m` denote the density of `Y_m`, and let
\[
g(x)=e^{-\lambda}\sum_{k=0}^\infty{\lambda^k\over k!}
      \gamma_\sigma(x-ak),\qquad \sigma^2=1/12.
\tag{8}
\]
This is the density of `G+aN`, where `G~N(0,1/12)` and `N~Pois(lambda)` are independent.

### Lemma 1 (weighted local convergence)

For every fixed `lambda,a`,
\[
\boxed{
\sup_x(1+|x|)^4|g_m(x)-g(x)|\longrightarrow0.
}
\tag{9}
\]
Moreover
\[
\sup_m\sup_x(1+|x|)^4g_m(x)<\infty.
\tag{10}
\]

### Proof

Fix `k<=m/2` and write `n=m-k`.  Then
\[
T_{m,k}=\sqrt{n/m}\,Z_n,
\qquad
Z_n=n^{-1/2}\sum_{r=1}^nU_r.
\]
The partner weighted Edgeworth theorem applied to `Z_n`, followed by the scaling factor `sqrt(n/m) in [1/sqrt(2),1]`, gives uniformly for `k<=m/2`
\[
h_{m,k}(x)\le C(1+|x|)^{-8},
\tag{11}
\]
where `h_{m,k}` is the density of `T_{m,k}`.  The same Fourier-derivative bounds used in the partner proof give a uniform first-derivative envelope.  Convolution with the `E_{m,k}` law, whose support radius is at most `lambda/(4sqrt(m))` when `k<=m/2`, preserves (11) and tends to the identity.  For each fixed `K`, uniformly over `0<=k<=K`, the conditional centered density in (7) therefore converges in polynomially weighted sup norm to `gamma_sigma`.

The binomial weights converge termwise to the Poisson weights.  For `K<k<=m/2`, the shift inequality
\[
1+|x|\le (1+|a|k)(1+|x-ak|)
\]
and (11) show that the weighted contribution is bounded by
\[
C\,\mathbb E[(1+N_m)^4{\bf1}_{\{N_m>K\}}].
\]
All factorial moments of `Bin(m,lambda/m)` are bounded by the corresponding powers of `lambda`, so these fourth moments are uniformly integrable and the displayed quantity tends to zero as `K->infinity`, uniformly in `m`.

For `k>m/2`, the conditional density is at most `C m^{3/2}` (one scaled remote interval already has that cap, and convolution cannot raise a sup norm), while its support has polynomial size in `m`; meanwhile a Chernoff bound for `Bin(m,lambda/m)` gives superexponentially small probability of `N_m>m/2`.  Hence that tail contributes `o(1)` even after multiplication by `(1+|x|)^4`.

Taking `m->infinity` for fixed `K` and then `K->infinity` proves (9); the same estimates give (10).  `square`

Applying Lemma 1 separately in the three banks yields independent limits
\[
Y_{j,m}\Longrightarrow Y_j=G_j+a_jN_j,
\tag{12}
\]
with the stronger weighted density convergence (9).

## 4. Uniform local limit for the quadratic output

Let
\[
\rho_m^Y(y)=\prod_{j=1}^3g_{j,m}(y_j),
\qquad
\rho^Y(y)=\prod_{j=1}^3g_j(y_j).
\]
Put
\[
\rho_m^Z(z)=\rho_m^Y(O^Tz),
\qquad
\rho^Z(z)=\rho^Y(O^Tz).
\]
Because `O` is orthogonal, `|O^Tz|=|z|`.  Telescoping the product, using (9)-(10), and observing that at least one coordinate of `O^Tz` has magnitude at least `|z|/sqrt(3)`, gives numbers `epsilon_m->0` such that
\[
\boxed{
|\rho_m^Z(z)-\rho^Z(z)|
\le\epsilon_m(1+|z|)^{-4}
\quad\text{for all }z\in\mathbb R^3.
}
\tag{13}
\]

Now set
\[
q(z)=z_1^2+z_2^2-z_3^2.
\]
For any continuous density `rho` with the decay in (13), cylindrical coordinates in `(z_1,z_2)` give the exact pushforward formula
\[
p_\rho(s)
={1\over2}\int_{z^2+s\ge0}\int_0^{2\pi}
\rho\left(\sqrt{z^2+s}\cos\theta,
          \sqrt{z^2+s}\sin\theta,z\right)
\,d\theta\,dz.
\tag{14}
\]
There is no singular factor: the radial Jacobian `r` cancels the derivative `2r` of the quadratic constraint.

Applying (14) to (13), uniformly in the level `s`,
\[
\begin{aligned}
|p_m(s)-p_\infty(s)|
&\le \pi\epsilon_m\int_{\mathbb R}(1+|z|)^{-4}dz\\
&={2\pi\over3}\epsilon_m.
\end{aligned}
\]
Therefore
\[
\boxed{
\|p_m-p_\infty\|_\infty\longrightarrow0.
}
\tag{15}
\]
This is stronger than weak convergence and prevents an unseen narrow finite-`m` spike from surviving asymptotically.

For large `m`, each bank density is a convolution of at least two `L^1` densities and is continuous; formula (14) plus the polynomial envelope gives a continuous density for `Q_m`.  The limiting compound-Poisson/Gaussian mixture below is also continuous.  These continuity statements are only for this family, not the full conjecture.

## 5. The limiting law is a mixture of affine Gaussians

By (12),
\[
Y=(G_1+a_1N_1,G_2+a_2N_2,G_3+a_3N_3)^T,
\]
where the `G_j~N(0,1/12)` and `N_j~Pois(lambda_j)` are mutually independent.  Since `O` is orthogonal,
\[
OY=G+H,
\qquad G\sim N(0,I_3/12),
\qquad H=O(a_1N_1,a_2N_2,a_3N_3)^T,
\]
with `G` independent of `H`.  Hence
\[
Q_\infty=(G+H)^TJ(G+H).
\]
Condition on `H=h`.  The arbitrary-mean Gaussian ceiling (G) gives
\[
\|p_{Q_\infty\mid H=h}\|_\infty\le3\sqrt2.
\]
Averaging the conditional densities proves
\[
\boxed{\|p_{Q_\infty}\|_\infty\le3\sqrt2.}
\tag{16}
\]
Combining (15) and (16) proves (2).

This argument actually shows a broader statement: **adding any independent random vector `H` to the minimum-variance isotropic Gaussian cannot raise the `(2,1)` quadratic density above `3 sqrt(2)`**, because conditional on `H` one is simply in the arbitrary-mean Gaussian theorem.  The finite-activity fragmented arrays above converge precisely to such a Gaussian-plus-independent-jump law.

## 6. Explicit strict cone-tip penalty

The quantitative cone-tip inequality (GT) gives more.  Since orthogonal `O` preserves norm,
\[
\|H\|^2=a_1^2N_1^2+a_2^2N_2^2+a_3^2N_3^2.
\]
Therefore
\[
p_{Q_\infty}(0)
\le {3\sqrt2\over2}
\left(1+\mathbb E e^{-6\|H\|^2}\right)
\]
and independence yields
\[
\boxed{
p_{Q_\infty}(0)
\le {3\sqrt2\over2}\left(1+\prod_{j=1}^3F(\lambda_j,a_j)\right),
}
\tag{17}
\]
where
\[
F(\lambda,a)
=e^{-\lambda}\sum_{k=0}^\infty{\lambda^k\over k!}e^{-6a^2k^2}.
\tag{18}
\]
For every `lambda>0` and `a!=0`, `F(lambda,a)<1`; hence any nontrivial one-sided rare-fragment perturbation in at least one bank gives a strict limiting loss at the cone tip.

For the symmetric numerical stress `lambda_1=lambda_2=lambda_3=1` and `a_1=a_2=a_3=1`,
\[
F(1,1)=0.3687913231439408\ldots,
\]
so (17) gives
\[
p_{Q_\infty}(0)\le2.22772198808356\ldots,
\]
far below
\[
3\sqrt2=4.242640687119286\ldots.
\]
The computation is only a diagnostic; the strict inequality is analytic.

The same proof extends to finitely many remote intervals per bank (multinomial rare categories).  The limit is `G+H` with `H` an arbitrary finite-activity compound-Poisson vector built from those jump types, and the global ceiling (16) is unchanged.  Symmetric `+/-` fragments and exact jump cancellations are therefore included in the global statement; only the simple product formula (17) changes.

## 7. Designated partner result applied to the sharp-constant inequality

The completed fleet04/B17 theorem (P) is not merely cited: it supplies the actual lower side of the sharp-constant comparison.  Its unfragmented exact cap-one sequence satisfies
\[
p_{Q_m^{(0)}}(0)
=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right),
\]
so
\[
3\sqrt2\le C_*.
\]
The new fragmented sequence has the **same exact matrices**, the same exact nonzero spectrum `{1,1,-1}`, and still has independent cap-one physical inputs, but (15)-(16) give
\[
\limsup_m\|p_{Q_m^{\rm frag}}\|_\infty\le3\sqrt2.
\]
Hence
\[
\boxed{
\limsup_m\|p_{Q_m^{\rm frag}}\|_\infty
\le3\sqrt2
=\lim_m p_{Q_m^{(0)}}(0)
\le C_*.
}
\]
This closes the finite-activity critical-fragment route as a way to obtain a stronger asymptotic lower bound.

## 8. What this constrains, and what remains open

1. **Critical `1/m` remote fragments at distance `sqrt(m)` are exhausted.**  They survive the bank limit as compound-Poisson jumps, but those jumps are only an independent random affine shift of the minimum-variance Gaussian core, and the arbitrary-mean Gaussian ceiling kills any gain.

2. **The result is global in the output level asymptotically.**  Equation (15) gives uniform convergence of the full output density, not only the value at zero.

3. **Finite-dimensional overshoot is not ruled out uniformly in `m`.**  The theorem proves an asymptotic ceiling; it does not assert `||p_{Q_m}||_infinity<=3sqrt(2)` for every finite `m` in the fragmented family.

4. **The full QFORM theorem is still open.**  This family has exact rank three and a particular repeated-row architecture.  Arbitrary finite leverage, arbitrary additional spectrum, and arbitrary product laws are not reduced to it.

5. **Next genuinely different B17 mechanism.**  A candidate witness above `3sqrt(2)` must avoid a limit of the form `minimum-variance Gaussian + independent shift`.  Natural next tests are infinite-activity triangular arrays (jump rate tending to infinity while jump size tends to zero on a non-CLT scale), several mesoscopic shared rows whose surviving residual is dependent on the Gaussian core, or finite-leverage constructions where the non-Gaussian component enters the quadratic form non-additively.

No Monte Carlo histogram or interval-extremality assumption is used.

Status: `SUPPORTING_SHARP_WITNESS_EXCLUSION`; full QFORM `OPEN / NOT PROVED`; full-target continuity `OPEN`; repository use genuine, native brain ingestion not verified (`WITHOUT_VERIFIED_BRAIN`).
