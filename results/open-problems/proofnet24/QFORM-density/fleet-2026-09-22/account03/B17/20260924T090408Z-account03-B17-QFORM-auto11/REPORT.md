# account03/B17 — full Gaussian comparator barrier for QFORM witnesses

Run: `20260924T090408Z-account03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL QFORM OPEN`

## 1. Scope and exact target

The unrestricted target remains open: independent original variables with arbitrary probability densities bounded by one, no moment/log-concavity/support/diagonal assumptions, and a real symmetric matrix with at least three eigenvalues of absolute value at least one.

This report proves a comparator theorem for **Gaussian limits only**. It is not a Gaussian reduction of the original problem. Its use is to rule out a large class of proposed sharp-witness mechanisms: any argument whose source-valid finite product construction genuinely Gaussianizes in the active spectral variables cannot obtain a limiting density peak above `3 sqrt(2)` at the density-cap-one variance floor.

The current corrections are respected: no post-rotation independence of the original product law is used, no arbitrary-joint coarea bound is assumed, and no law-uniform pointwise van-der-Corput estimate is used.

## 2. Main theorem

### Theorem (QFORM-GAUSSIAN-FULLTARGET-COMPARATOR-v1)

Let `G ~ N(mu,Sigma)` in `R^n`, with `Sigma >= v I` in Loewner order for some `v>0`. Let `A=A^T` have at least three eigenvalues of absolute value at least `s>0`. Then `Q=G^T A G` has a bounded continuous density and

\[
\boxed{\|p_Q\|_\infty\le {1\over 2\sqrt2\,v s}.}
\tag{2.1}
\]

In particular, at the minimum-variance scale forced by a density cap one,

\[
v={1\over 12},\qquad s=1,
\]

one gets

\[
\boxed{\|p_Q\|_\infty\le 3\sqrt2.}
\tag{2.2}
\]

The constant in (2.1) is sharp within the Gaussian comparator class: equality occurs for the centered three-dimensional signature `(1,1,-1)` with covariance `v I`.

## 3. Spectral threshold survives covariance congruence

Write

\[
M=\Sigma^{1/2}A\Sigma^{1/2}.
\]

Suppose `A` has `r_+` eigenvalues at least `s`. Let `E_+` be their spectral subspace and put `F_+=Sigma^{-1/2}E_+`. For `y in F_+`, writing `x=Sigma^{1/2}y in E_+`,

\[
y^TMy=x^TAx\ge s\|x\|^2
=s\|\Sigma^{1/2}y\|^2\ge sv\|y\|^2.
\]

By min-max, `M` has at least `r_+` eigenvalues at least `sv`. The same argument applied to `-A` shows that every large negative spectral count is preserved at threshold `sv`. Consequently `M` has at least three eigenvalues of absolute value at least

\[
m_0:=sv.
\tag{3.1}
\]

## 4. Centered case reduces to three independent Gaussian squares

For `mu=0`, orthogonally diagonalize `M`. Rotational invariance of a standard Gaussian gives

\[
Q\stackrel d=\sum_{j=1}^n \lambda_j Z_j^2,
\]

with independent standard normals `Z_j`. Select any three indices with `|lambda_j|>=m_0`. The remaining sum is independent, so convolution cannot increase an `L^infinity` norm. It is enough to control exactly three terms.

There are two sign cases.

## 5. Indefinite three-term Gaussian: exact global tip and sharp bound

After an overall sign change write

\[
Q_3=aZ_1^2+bZ_2^2-cZ_3^2,
\qquad a,b,c\ge m_0,
\]

and assume `a<=b`.

Let `U=aZ_1^2+bZ_2^2` and `V=cZ_3^2`. The density of `U` is

\[
f_U(u)={1\over 2\sqrt{ab}}
\exp\!\left[-{a+b\over4ab}u\right]
I_0\!\left({b-a\over4ab}u\right),\quad u>0.
\]

Because `I_1/I_0<1`, its logarithmic derivative is strictly negative. The density of `V` is also decreasing. Hence, for `q>=0`,

\[
p(q)=\int_0^\infty f_U(q+v)f_V(v)\,dv\le p(0),
\]

and for `q=-r<0`,

\[
p(-r)=\int_0^\infty f_U(u)f_V(u+r)\,du\le p(0).
\]

Thus zero is the global mode.

A direct cone/elliptic-integral computation gives

\[
p(0)={K(k)\over \pi\sqrt{b(a+c)}},
\qquad
k^2={(b-a)c\over b(a+c)}.
\tag{5.1}
\]

Cauchy-Schwarz on the complete elliptic integral gives

\[
K(k)\le {\pi\over 2(1-k^2)^{1/4}}.
\]

Since

\[
1-k^2={a(b+c)\over b(a+c)},
\]

(5.1) yields

\[
\|p\|_\infty
\le {1\over 2[ab(a+c)(b+c)]^{1/4}}
\le {1\over2\sqrt2\,m_0}.
\tag{5.2}
\]

The last inequality uses `ab>=m_0^2`, `a+c>=2m_0`, `b+c>=2m_0`. Equality requires `a=b=c=m_0`.

## 6. Definite three-term Gaussian is strictly below the indefinite barrier

Now let

\[
Q_3=aZ_1^2+bZ_2^2+cZ_3^2,
\qquad a,b,c\ge m_0.
\]

For `omega in S^2`, write

\[
h(\omega)=a\omega_1^2+b\omega_2^2+c\omega_3^2\ge m_0.
\]

Polar coordinates give, for `q>0`,

\[
p(q)={\sqrt q\over2(2\pi)^{3/2}}
\int_{S^2}h(\omega)^{-3/2}
\exp\!\left[-{q\over2h(\omega)}\right]d\omega.
\tag{6.1}
\]

If `0<q<=3m_0`, then with `y=q/(2h)` one has `0<y<=3/2`, and `y^{3/2}e^{-y}` is increasing. Therefore

\[
h^{-3/2}e^{-q/(2h)}
\le m_0^{-3/2}e^{-q/(2m_0)}.
\]

The resulting isotropic envelope has maximum at `q=m_0`, giving

\[
p(q)\le {e^{-1/2}\over\sqrt{2\pi}\,m_0}.
\tag{6.2}
\]

If `q>=3m_0`, the pointwise maximum over `h>=m_0` occurs at `h=q/3`, so

\[
p(q)\le {\sqrt6\,e^{-3/2}\over2\sqrt\pi\,m_0}
< {e^{-1/2}\over\sqrt{2\pi}\,m_0}.
\tag{6.3}
\]

Finally `e^{-1/2}/sqrt(2 pi) < 1/(2 sqrt(2))` because `pi e>4`. Hence the definite branch is strictly below (5.2).

Together, Sections 3--6 prove (2.1) for centered Gaussians.

## 7. Arbitrary Gaussian translations cannot raise the norm

For general `mu`, after whitening,

\[
Q=Z^TMZ+2\ell^TZ+\text{constant},
\qquad
\ell=\Sigma^{1/2}A\mu=M\Sigma^{-1/2}\mu\in\operatorname{ran}M.
\]

After diagonalizing `M`, every linear term lies in a nonzero spectral coordinate and can be completed into a square. Thus, up to an additive constant,

\[
Q=\sum_j \lambda_j(Z_j+\delta_j)^2.
\]

For each coordinate, `chi^2_1(delta_j^2)` is a Poisson mixture of `chi^2_{1+2k}`, and

\[
\chi^2_{1+2k}\stackrel d=\chi^2_1+\chi^2_{2k}
\]

with independent summands. Conditional on all Poisson indices, the noncentral quadratic form is the centered form plus an independent random variable. Hence its density is a mixture of convolutions/translates of the centered density, and Young's inequality gives

\[
\|p_{Q,\mu}\|_\infty\le\|p_{Q,0}\|_\infty.
\tag{7.1}
\]

This proves the full theorem.

Continuity follows independently from the characteristic function: three nonzero Gaussian-square factors already give `O(|t|^{-3/2})`, which is integrable; noncentrality only multiplies by a factor of modulus at most one after the standard formula.

## 8. Density-cap-one variance floor and the sharp-witness consequence

For any real probability density `f<=1` with finite variance, translation to its mean and the one-dimensional bathtub principle give

\[
\operatorname{Var}(X)\ge {1\over12},
\tag{8.1}
\]

with equality for a unit interval density.

Therefore every genuine Gaussian limit of independent cap-one coordinates whose covariance records their limiting second moments has covariance at least `I/12`. Theorem (2.1) then gives the sharp Gaussian barrier

\[
\boxed{\text{Gaussianized witness peak}\le3\sqrt2.}
\tag{8.2}
\]

This does **not** say arbitrary cap-one inputs are Gaussian, and it does not control a non-Gaussian sequence without a valid local-limit passage. It says that a witness above `3 sqrt(2)`, if one exists, must retain a genuinely non-Gaussian/non-infinitesimal mechanism (or evade a covariance-floor Gaussian local limit).

## 9. Exact source-valid isometric lifts

The obstruction is directly relevant to exact finite target matrices. Let `B=B^T` be any fixed `d x d` matrix and let `R_m` be the `dm x d` isometry whose `(j,k)` row is `e_j/sqrt(m)`. Then

\[
R_m^TR_m=I_d,
\qquad
A_m=R_mBR_m^T
\]

has exactly the same nonzero spectrum as `B`.

With independent physical inputs `U_{jk}~Unif[-1/2,1/2]` (each density exactly one),

\[
Y_{j,m}=m^{-1/2}\sum_{k=1}^mU_{jk},
\qquad
U^TA_mU=Y_m^TBY_m.
\]

Thus every finite `A_m` is source-valid and the active variables Gaussianize to iid `N(0,1/12)`. Any use of a genuine local density limit for this construction is therefore capped by (8.2); weak convergence alone is not being promoted to a density-norm statement.

## 10. Completed partner result applied to an actual inequality

The designated completed partner theorem is account04/B17 r7, `QFORM-SHARED-FOLD-LOGRECEIVER-UNIFORM-v1`, canonical source

`yspennstate/math-open-problems@d2795ffa95ffde81e63da02b677fdc3c0ea950a1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260924T061346Z-account04-B17-QFORM-r7/REPORT.md`.

For

\[
A_\theta=
\begin{pmatrix}
\theta&0&1&0\\
0&0&0&1\\
1&0&\theta^{-1}&0\\
0&1&0&0
\end{pmatrix},\qquad0<\theta\le1,
\]

it proves for four independent unit-interval inputs

\[
\|p_{Q_\theta}^{\rm unif}\|_\infty\le2\sqrt6.
\tag{10.1}
\]

Its nonzero spectral magnitudes are

\[
L=\theta+\theta^{-1}\ge2,\qquad1,\qquad1.
\]

For a Gaussian comparator with covariance at least `v I`, the rank is exactly three. Singular-value monotonicity under congruence gives nonzero magnitudes `a,b,c>=v` with

\[
abc\ge L v^3\ge2v^3.
\]

In the indefinite case, the bound (5.2) can be sharpened. Normalize `a,b,c` by `v`; put `r=sqrt(ab)>=1`. Since `abc>=2v^3`, after normalization `c>=max(1,2/r^2)`, and

\[
ab(a+c)(b+c)
\ge r^2(r+c)^2\ge9.
\]

Indeed, for `1<=r<=sqrt2`, `r(r+c)>=r^2+2/r>=3`, while for `r>=sqrt2`, `r(r+c)>=r^2+r>3`. Therefore

\[
\boxed{\|p_{G^TA_\theta G}\|_\infty\le {1\over2\sqrt3\,v}.}
\tag{10.2}
\]

At `v=1/12`,

\[
\boxed{\|p_{G^TA_\theta G}\|_\infty\le2\sqrt3
={1\over\sqrt2}(2\sqrt6).}
\tag{10.3}
\]

Thus Gaussianizing the exact partner stress matrix loses at least a factor `sqrt(2)` relative to the partner's distribution-free uniform-law ceiling. In particular it cannot exploit the near-singular fold to approach the present `3 sqrt(2)` lower obstruction.

## 11. What is and is not resolved

Proved here:

- arbitrary dimension Gaussian comparator, arbitrary covariance `Sigma>=vI`, arbitrary mean, all sign patterns, at least three spectral magnitudes `>=s`;
- sharp universal Gaussian ceiling `1/(2 sqrt(2) v s)`;
- continuity in the Gaussian comparator class;
- exact isometric source-valid bank lifts preserve the target spectrum;
- a strict `2 sqrt(3)` Gaussian ceiling for the completed account04/B17 fold family at the cap-one variance floor.

Not proved here:

- the original arbitrary-law QFORM conjecture;
- a uniform local-limit theorem for every possible source-valid triangular array;
- that `3 sqrt(2)` is the sharp universal constant outside Gaussian limits;
- full-target continuity.

The witness frontier is therefore pushed toward surviving non-Gaussian macroscopic rows, off-tip/two-sheet effects that do not Gaussianize, or additional active spectrum coupled to non-infinitesimal product structure.
