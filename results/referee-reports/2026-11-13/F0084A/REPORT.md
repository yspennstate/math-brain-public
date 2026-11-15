RESOLVED_IN_LITERATURE

# F0084: a power-law upper bound was published in 2009

For the unique stable allocation of Lebesgue measure to a unit-intensity Poisson process in R^d with appetite 1, let X be the distance from the origin to its allocated centre. For every d >= 2 there are constants C(d) < infinity and s(d) > 0 such that

\[
\boxed{\mathbb P(X>r)\le C(d)r^{-s(d)}\quad(r>0).}
\]

In particular, the published exponent in dimension two is

\[
s(2)=0.496318438868985\ldots .
\]

This resolves the requested “any quantitative upper bound” question. It does not determine the sharp tail asymptotic. This report attributes the result to its authors; it claims no new resolution or new theorem. As instructed, work stopped at the literature resolution, without torus simulations.

## Exact reference and locations

A. E. Holroyd, R. Pemantle, Y. Peres and O. Schramm, **Poisson matching**, *Annales de l’Institut Henri Poincaré, Probabilités et Statistiques* **45**(1) (2009), 266–287. DOI: [10.1214/08-AIHP170](https://doi.org/10.1214/08-AIHP170). Preprint: [arXiv:0712.1867](https://arxiv.org/abs/0712.1867).

The allocation application is explicit in print, rather than an inference from a result about matching two discrete processes:

| Location in the published paper | Content |
|---|---|
| Theorem 6(ii), p. 269 (PDF p. 4) | Power-law upper bound for two-colour stable matching, with positive dimension-dependent exponent. |
| “Extensions to other processes,” item (ii), p. 270 (PDF p. 5) | Explicitly extends Theorem 6 to fair allocations of Lebesgue measure to Poisson points, with X defined as the origin-to-centre distance; identifies the improvement over the earlier allocation bounds. |
| Theorem 19, p. 283 (PDF p. 18), equations (20)–(21) | Gives the exponent as the unique root of an explicit integral equation. |
| Proof of Theorem 19, pp. 283–286 | Establishes the tail inequality. |
| First “Remarks” paragraph after the proof, p. 286 (PDF p. 21) | Specifies the changes from counting points to measuring territories that prove the stable Poisson–Lebesgue allocation version. |

Primary published text: [Numdam PDF](https://www.numdam.org/article/AIHPB_2009__45_1_266_0.pdf). Only the extracted plain text is retained here, in [sources/HPPS2009_published.txt](sources/HPPS2009_published.txt). The arXiv text is separately saved as [sources/HPPS2009.txt](sources/HPPS2009.txt). In that version the corresponding locations are pp. 6–8, Theorem 19 on p. 29, and the allocation proof remark on p. 34.

There is an independent later cross-check: Markó–Timár, *A Poisson allocation of optimal tail*, *Ann. Probab.* **44**(2) (2016), 1285–1307, DOI [10.1214/15-AOP1001](https://doi.org/10.1214/15-AOP1001), arXiv:1103.5259v3, reprint PDF p. 5, explicitly identifies the r^(-0.496...) bound as achieved by the stable allocation and cites *Poisson matching*. See [sources/MT2016.txt](sources/MT2016.txt).

## Model and the different distance variables

An allocation is a measurable map psi from R^d to the centres, an unclaimed symbol, and an exceptional symbol allowed on a Lebesgue-null set. Each centre receives volume at most its appetite. A site desires a different centre when that centre is closer, or when the site is unclaimed. A centre covets a site when it is unsated, or when some currently allocated site is farther from the centre. Stability excludes any site–centre pair satisfying both conditions.

Hoffman–Holroyd–Peres (2006), Theorem 3, gives almost-sure uniqueness up to a null set for the Poisson process. Thus the site-optimal and centre-optimal Gale–Shapley constructions yield the same allocation almost everywhere here. Theorem 4(ii) says that at intensity = appetite = 1 every centre has territory volume 1 and almost every site is claimed. In particular X is finite almost surely.

A typical centre is described by the Palm process, which for Poisson is obtained by adding a centre at 0. If X* means distance from this centre to a site sampled uniformly by volume in its unit-volume territory, mass transport gives

\[
\mathbb P^*(X^*>r)
=\mathbb E^*\mathcal L\{x\in\psi^{-1}(0):|x|>r\}
=\mathbb P(X>r).
\]

This sampled distance is different from the territory radius R*, the essential supremum of distances over the Palm centre's territory. The HHP papers use R* for that radius; it is not X*. A bound for the volume-averaged distance does not by itself bound R*.

The original downloaded source is arXiv:math/0505668v4, the 2006 electronic reprint. Its Section 1 contains Theorems 3, 4 and 7; Sections 5–7 are “Phases,” “Monotonicity,” and “Geometry of territories.” Its tail lower bounds are in Section 9, and “Open problems” is unnumbered on PDF p. 31, rather than Section 12. Those sections and the open problem were read directly. Theorem 7 on PDF p. 6 states E[X^(d/2)] = infinity for d = 1,2 and E[X^d] = infinity for d >= 3. Theorem 32 on PDF p. 30 proves E[X^d] = infinity for ergodic insertion-tolerant critical processes in every dimension. These moment statements are compatible with the upper bound above; moment divergence alone is not a pointwise tail lower bound.

For comparison, HHP, *Tail bounds for the stable marriage of Poisson and Lebesgue*, *Canad. J. Math.* **61**(6) (2009), 1279–1299, Theorem 1.2, p. 1281, gives E*[(R*)^(1/18)] < infinity only in dimension one. Lemma 1.5 on that page transfers this to X. That article's noncritical bounds are Theorem 1.3. Its introduction does not incorporate the later improvement from *Poisson matching*, despite the same publication year.

## Proof of the allocation bound

The following supplies the details of the allocation adaptation prescribed on p. 286 of *Poisson matching*. It uses the same argument and exponent as that paper. Existence, uniqueness, saturation and equivariance of the allocation are the HHP results just stated.

Write v_k for the volume of the unit ball in R^k and omega_d = d v_d for the surface area of the unit sphere in R^d. In particular v_(d-1) = omega_(d-1)/(d-1). Define

\[
F(r)=\mathbb P(X>r).
\]

This function is nonincreasing and at most one. The exponent s = s(d) is the unique solution in (0,1) of HPPS equation (21):

\[
2\omega_d\int_1^2(t-1)^{d-1}t^{-s}\,dt
=v_{d-1}\int_0^2(1-t^2/4)^{(d-1)/2}t^{-s}\,dt. \tag{1}
\]

### 1. Stability and the discrepancy estimate

Fix a ball B = B(0,R), with volume V = v_d R^d and centre count N. Define four nonnegative quantities:

- A: volume of sites x in B with |x-psi(x)| > R+|x|.
- H: summed volume, over centres xi in B, of sites in xi's territory with |x-xi| > R+|xi|.
- Q_s: volume of sites in B allocated to centres outside B.
- Q_c: volume of sites outside B allocated to centres in B.

Every site counted in A is assigned outside B, so A <= Q_s. Likewise H <= Q_c. Also A and H cannot both be positive: a site x counted in A and a centre xi contributing to H satisfy

\[
|x-\xi|<R+|x|<|x-\psi(x)|.
\]

The centre has a territory site farther than R+|xi|, while |x-xi| < R+|xi|. Thus x desires xi and xi covets x, contradicting stability.

Since the territories have volume 1 and sites are claimed almost everywhere, conservation inside B gives Q_s-Q_c = V-N. Consequently

\[
A+H\le Q_c+(V-N)^+.
\]

Mass transport identifies the distribution of displacement from a typical site with that from a Palm centre to a volume-uniform territory site. Applying this identity with the location-dependent threshold R+|x| gives E A = E H. Since N is Poisson(V),

\[
2\mathbb E A\le\mathbb E Q_c+\mathbb E(V-N)^+
\le\mathbb E Q_c+\tfrac12\sqrt V. \tag{2}
\]

The last step uses E(V-N)=0, so E(V-N)^+ = E|V-N|/2, followed by Cauchy–Schwarz and Var(N)=V. This proves directly the allocation analogue of HPPS equation (23).

### 2. Express both terms using the same tail F

Stationarity and polar coordinates give

\[
\mathbb E A
=\int_B F(R+|x|)\,dx
=\omega_d\int_R^{2R}F(t)(t-R)^{d-1}\,dt. \tag{3}
\]

For E Q_c, the expected displacement measure from a Palm centre is a probability measure, because its territory has volume 1. Its radial tail is F by mass transport, and it is rotation invariant by equivariance of the allocation and isotropy of Poisson. Thus its direction is uniform conditional on its length.

For x in B and a unit direction u, let q(x,u) be the distance to leave B along the ray in direction u. A displacement along u leaves B exactly when its length exceeds q(x,u), apart from null boundaries. Campbell's formula therefore gives

\[
\mathbb E Q_c
=\frac1{\omega_d}\int_{S^{d-1}}\int_B F(q(x,u))\,dx\,du
=\int_B F(q(x,u_0))\,dx \tag{4}
\]

for any fixed direction u_0. Slicing B along lines parallel to u_0, write x=(z,a), |z|<R, and h(z)=sqrt(R^2-|z|^2). Then q=h(z)-a and da=-dq. For a fixed q=t, admissible z satisfy |z|<sqrt(R^2-t^2/4). Hence

\[
\mathbb E Q_c
=v_{d-1}\int_0^{2R}(R^2-t^2/4)^{(d-1)/2}F(t)\,dt. \tag{5}
\]

Define the bounded kernel, zero outside [0,2],

\[
g(t)=2\omega_d\mathbf1_{[1,2]}(t)(t-1)^{d-1}
-v_{d-1}\mathbf1_{[0,2]}(t)(1-t^2/4)^{(d-1)/2}.
\]

Substitution into (2), followed by division by R^(d-1), yields

\[
\int_0^\infty g(t/R)F(t)\,dt
\le c_d R^{1-d/2},\qquad c_d=\tfrac12\sqrt{v_d}. \tag{6}
\]

Also the same integral is at most 2R ||g||_infinity, simply because 0 <= F <= 1 and g is bounded and supported on [0,2].

### 3. The exponent and a nonnegative integrated kernel

On [0,2], g is continuous and strictly increasing when d >= 2, with g(0)<0<g(2). It has a unique zero t_0. Moreover

\[
\int_0^2g(t)\,dt=v_d>0.
\]

Indeed the integral of the first term is 2v_d, whereas the second is v_d by the same ball-slicing formula as (5), with F identically one. As s increases to 1, the integral of g(t)t^(-s) tends to minus infinity due to g(0)<0. It therefore has a zero in (0,1). This zero is unique: increasing s weights t<t_0 relatively more than t>t_0, and g has opposite signs in those two intervals. More explicitly, for s_2>s_1, the product

\[
g(t)\{t^{-s_2}-t_0^{s_1-s_2}t^{-s_1}\}
\]

is negative except at t_0. If the weighted integral at s_1 is nonpositive, the one at s_2 is strictly negative. This also verifies uniqueness and (1).

For this root s, define

\[
G_R(t)=\int_0^R g(t/\rho)\rho^{s-2}\,d\rho.
\]

The substitution u=t/rho and equation (1) show that the same integral over rho in (0,infinity) is zero. If t/R >= t_0, every nonzero integrand in G_R is nonnegative. If t/R < t_0, use instead

\[
G_R(t)=-\int_R^\infty g(t/\rho)\rho^{s-2}\,d\rho\ge0.
\]

These sign arguments are strict for 0<t<2R. Continuity on compact subintervals and scaling imply that

\[
c_0:=\min_{1/2\le u\le1}G_1(u)>0,
\qquad G_R(t)=R^{s-1}G_1(t/R).
\]

Therefore monotonicity of F gives

\[
\int_0^\infty G_R(t)F(t)\,dt
\ge \frac{c_0}{2}R^sF(R). \tag{7}
\]

### 4. Finish the bound

For finite R, absolute Fubini is valid since

\[
\int_0^R\rho^{s-2}\int_0^\infty|g(t/\rho)|F(t)\,dt\,d\rho
\le2\|g\|_\infty\int_0^R\rho^{s-1}\,d\rho<\infty.
\]

For R >= 1, integrate (6) with weight rho^(s-2), using the trivial bound below rho=1. This gives

\[
\begin{aligned}
\int_0^\infty G_R(t)F(t)\,dt
&\le 2\|g\|_\infty\int_0^1\rho^{s-1}\,d\rho
+c_d\int_1^R\rho^{s-1-d/2}\,d\rho\\
&\le \frac{2\|g\|_\infty}{s}+\frac{c_d}{d/2-s}=:K_d<\infty.
\end{aligned}
\]

Here s<1<=d/2 is exactly what makes the last integral finite. Combining this with (7) proves

\[
F(R)\le\frac{2K_d}{c_0}R^{-s},\qquad R\ge1.
\]

Enlarging the constant to at least 1 handles 0<R<1. All constants depend only on d; this proves the stated critical allocation bound. In particular E[X^p] is finite for every 0<p<s(d), by integrating the tail. No finite p=s(d) moment is asserted by this upper bound.

## Checks, scope and retained files

The published paper was checked against the arXiv text, including both allocation extension passages and the entire proof of Theorem 19. The allocation conservation identity, stability exclusion, Palm/site mass transport, ball-section formula, kernel signs and final integrability were checked in the model with Lebesgue sites, rather than assumed from the discrete matching statement. The later Markó–Timár text independently confirms that the bound concerns the stable allocation itself.

The exponent equation was checked two ways: 40-digit beta-function evaluation with mpmath, and independently transformed direct quadrature with SciPy. Dimension two was also checked against the gamma-function identity printed beneath HPPS equation (21):

\[
\sqrt\pi\,(2^s-2s)\Gamma((2-s)/2)=\Gamma((3-s)/2).
\]

| d | s(d), numerical value | Difference between the two numerical methods |
|---|---:|---:|
| 2 | 0.496318438869 | 2.2e-16 |
| 3 | 0.448696000412 | 1.1e-13 |
| 10 | 0.339356979825 | 1.5e-12 |
| 100 | 0.223860022251 | 4.8e-12 |

These numerical checks are consistency checks, not interval-certified proofs. The rigorous exponent is defined by (1), whose existence and positivity were proved above. Code is in [code/check_exponents.py](code/check_exponents.py), and results are in [data/exponent_checks.json](data/exponent_checks.json). The computation used one thread, inherited nice 10, and no large arrays or simulations.

All downloaded paper files are plain text. [sources/manifest.jsonl](sources/manifest.jsonl) records original URLs, fetch times, PDF hashes computed in memory, and extracted-text hashes. No PDFs, page images or scans were saved. Searches and several relevant later texts were saved before the decisive passage was found. The requested broader literature survey was not continued after the stopping condition was met; no exhaustive claim about all work through 2026 or the sharp tail is made. No publication, push, external message or subagent was used.

Task: “Open problem F0084 … Critical tail behavior” — 2026-11-13 07:42 Asia/Tbilisi (first local clock reading 07:42:33).
