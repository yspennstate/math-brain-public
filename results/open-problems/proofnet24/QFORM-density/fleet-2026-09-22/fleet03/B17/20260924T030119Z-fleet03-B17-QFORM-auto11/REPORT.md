SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-24T03:01:19Z.
attacking: centered-Gaussian cone-tip rigidity and quantitative strict-spectral-slack penalties for exact rank-three witnesses.

# QFORM centered-Gaussian global-tip rigidity and fragmented strict-slack tradeoff

Run: `20260924T030119Z-fleet03-B17-QFORM-auto11`  
Status: `PROVED_SUPPORTING_SHARP_WITNESS_THEOREM`; full QFORM remains OPEN / NOT PROVED.  
Programme: `QFORM-DENSITY-3EIG-20260922`.


No post-rotation independence for the original inputs is used below. The Gaussian theorem is explicitly a theorem about centered Gaussian rank-three comparators/limits, not a Gaussian assumption on the full conjecture. No pointwise van-der-Corput estimate, arbitrary-joint coarea bound, conditional projection-density moment, compact-support reduction, connected-support assumption, or Monte Carlo argument is used.

## 1. Exact centered Gaussian theorem

Let `G ~ N(0,Sigma)` in `R^3`, with `Sigma` positive definite, and let `A` be a real symmetric nonsingular indefinite `3 x 3` matrix. Put

`M = Sigma^(1/2) A Sigma^(1/2)`.

After replacing the form by its negative if necessary, write the eigenvalues of `M` as

`a, b, -c`, with `0 < a <= b` and `c > 0`.

Then `Q = G^T A G` has a continuous density, its global density maximum occurs at zero, and

\[
\boxed{
\|p_Q\|_\infty=p_Q(0)=
\frac{K(k)}{\pi\sqrt{b(a+c)}},\qquad
k^2=\frac{(b-a)c}{b(a+c)},
}
\tag{1.1}
\]
where

\[
K(k)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-k^2\sin^2\theta}}
\]
is the complete elliptic integral of the first kind.

Moreover,

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{1}{2\,[ab(a+c)(b+c)]^{1/4}}.
}
\tag{1.2}
\]

### Proof that the global maximum is at zero

Whitening and orthogonal diagonalization reduce to independent standard normals `Z_1,Z_2,Z_3` and

\[
Q=aZ_1^2+bZ_2^2-cZ_3^2=U-V,
\qquad
U=aZ_1^2+bZ_2^2,\quad V=cZ_3^2.
\]

The density of `V` is decreasing on `(0,infinity)`. The density of `U` admits the exact polar representation

\[
f_U(u)=\frac{1}{4\pi\sqrt{ab}}
\int_0^{2\pi}
\exp\!\left[-\frac u2\left(\frac{\cos^2\theta}{a}+\frac{\sin^2\theta}{b}\right)\right]d\theta,
\qquad u>0,
\]
so `f_U` is also decreasing. Therefore, for `q>=0`,

\[
p_Q(q)=\int_0^\infty f_U(q+v)f_V(v)\,dv\le p_Q(0),
\]
and for `r>=0`,

\[
p_Q(-r)=\int_0^\infty f_U(u)f_V(u+r)\,du\le p_Q(0).
\]
Thus `||p_Q||_infty=p_Q(0)`. Since `p_Q` is the convolution of two `L^1` densities (one reflected), it is continuous and vanishes at infinity.

### Exact cone-tip formula

For a standard Gaussian write `Z=RU`, where `U` is uniform on `S^2`, `R` is independent of `U`, and `E[R^{-2}]=1` in dimension three. Hence the density at zero of `aZ_1^2+bZ_2^2-cZ_3^2` equals the density at zero of `aU_1^2+bU_2^2-cU_3^2`.

The squared coordinates `(u,v,w)=(U_1^2,U_2^2,U_3^2)` have the Dirichlet `(1/2,1/2,1/2)` density

\[
\frac{1}{2\pi}(uvw)^{-1/2},\qquad u,v,w>0,\quad u+v+w=1.
\]
Eliminating `w` and then the delta constraint gives

\[
p_Q(0)=\frac1{2\pi}
\int_0^{c/(a+c)}
\frac{du}{\sqrt{u\,[c-(a+c)u]\,[b-(b-a)u]}}.
\]
With `u=c t/(a+c)` and then `t=sin^2(theta)`, this becomes (1.1).

### Elementary elliptic bound

Cauchy-Schwarz gives

\[
K(k)^2
\le\frac\pi2\int_0^{\pi/2}\frac{d\theta}{1-k^2\sin^2\theta}
=\frac{\pi^2}{4\sqrt{1-k^2}}.
\]
Since

\[
1-k^2=\frac{a(b+c)}{b(a+c)},
\]
substitution into (1.1) yields (1.2).

## 2. Sharp covariance-stable consequence

Suppose now that

\[
\Sigma\succeq v_0 I_3,
\qquad
\min_j|\lambda_j(A)|\ge s>0.
\]
Then

\[
\sigma_{\min}(M)
\ge\sigma_{\min}(\Sigma^{1/2})^2\sigma_{\min}(A)
\ge v_0s.
\]
Thus `a,b,c >= m_0:=v_0s`, and (1.2) immediately gives

\[
\boxed{
\|p_{G^T A G}\|_\infty\le\frac{1}{2\sqrt2\,v_0s}.
}
\tag{2.1}
\]

The constant is sharp in this centered-Gaussian class. Equality forces `a=b=c=v_0s`; using

\[
|\det M|=\det\Sigma\,|\det A|\ge(v_0s)^3
\]
then forces `Sigma=v_0 I_3` and all three eigenvalue magnitudes of `A` to equal `s`.

For the cap-one variance floor `v_0=1/12` and spectral threshold `s=1`,

\[
\boxed{
\|p_{G^T A G}\|_\infty\le3\sqrt2,
}
\tag{2.2}
\]
with equality exactly at the isotropic covariance / equal spectral-magnitude configuration (up to signs and orthogonal rotation).

## 3. Quantitative strict-spectral-slack penalty

There is a useful stable strengthening. Assume additionally

\[
|\det A|\ge s^3(1+\delta),\qquad 0\le\delta\le1.
\]
Then

\[
abc=|\det M|
\ge(v_0s)^3(1+\delta).
\]
Scale `m_0=v_0s` out and write `x=a/m_0`, `y=b/m_0`, `z=c/m_0`, all at least one. Let `P=xyz>=1+delta` and `r=sqrt(xy)>=1`. By AM-GM,

\[
xy(x+z)(y+z)
\ge \left(r^2+\frac{P}{r}\right)^2.
\]
If `r^2>=1+delta`, the bracket is at least `r^2+r>2+delta`. If `r^2<1+delta`, then

\[
r^2+\frac{P}{r}\ge r^2+\frac{1+\delta}{r},
\]
and the right side is increasing for `r>=1` because `delta<=1`; hence it is at least `2+delta`. Therefore

\[
ab(a+c)(b+c)\ge(v_0s)^4(2+\delta)^2,
\]
and (1.2) gives

\[
\boxed{
\|p_{G^T A G}\|_\infty
\le\frac{1}{2v_0s\sqrt{2+\delta}}
<\frac{1}{2\sqrt2\,v_0s}
\quad(\delta>0).
}
\tag{3.1}
\]

For two positive coefficients equal to `v_0s` and minority negative magnitude `v_0s(1+delta)`, equality holds in (3.1). Thus the strict-slack penalty is sharp.

## 4. Why `v_0=1/12` is forced by cap-one product laws

If a real random variable `X` has density `0<=f<=1`, mass one, and finite variance, then

\[
\operatorname{Var}(X)\ge\frac1{12}.
\]
Indeed, with `m=EX`, the bathtub principle for the increasing reward `(x-m)^2` gives

\[
\int (x-m)^2f(x)dx
\ge\int_{-1/2}^{1/2}t^2dt=\frac1{12}.
\]

Hence for independent cap-one inputs with diagonal covariance `D`, one has `D>=I/12`. For any three orthonormal linear forms with synthesis matrix `R`, `R^T R=I_3`, their centered covariance is

\[
R^TDR\succeq I_3/12.
\]
Consequently **every centered Gaussian rank-three comparator or Gaussian limit that genuinely arises from such finite-variance product inputs** obeys the global ceiling `3sqrt(2)` in (2.2). This is a statement about the Gaussian comparator/limit only; it does not silently replace arbitrary input laws by Gaussians and it does not cover noncentered limits, surviving non-Gaussian components, extra active spectrum, or the full QFORM target.

## 5. Actual application of the completed fleet04/B17 partner result

Completed designated-partner source:

- `yspennstate/math-open-problems@4be63022324b82f254f1d7a4353a3e883f08d10a`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260924T011922Z-fleet04-B17-QFORM-r6/REPORT.md`;
- theorem `QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1`.

Their exact matrices have nonzero spectrum

\[
\{1,1,-(1+1/m)\}.
\]
For the centered isotropic Gaussian comparator with covariance `I/12`, (3.1) is exact and gives the **global** density norm

\[
\boxed{
\|p_{G,m}\|_\infty
=\frac{6}{\sqrt{2+1/m}}
=3\sqrt2\left(1-\frac1{4m}+\frac{3}{32m^2}+O(m^{-3})\right)
<3\sqrt2.
}
\tag{5.1}
\]
Thus strict spectral slack itself pushes the centered Gaussian witness downward; approaching `3sqrt(2)` requires the slack to vanish.

The partner theorem is source-valid at finite dimension and uses independent normalized cap-one two-component densities. For every

\[
0<\theta<\frac13\log\left(\frac{3\sqrt2}{4}\right)
\]
it proves

\[
\liminf_m\|p_{Q_m}\|_\infty\ge3\sqrt2e^{-3\theta}>4,
\]
while the probability of at least one satellite support component tends to `1-e^{-3theta}`. Reparameterizing by

\[
\alpha=1-e^{-3\theta}
\]
gives the concrete target-level lower-bound tradeoff

\[
\boxed{
C_*\ge3\sqrt2(1-\alpha)>4,
\qquad
0<\alpha<1-\frac4{3\sqrt2},
}
\tag{5.2}
\]
for exact entrywise-dense strict-slack matrices with limiting satellite probability `alpha`.

At `theta=0.01`, this is

\[
C_*\ge4.117251705266084\ldots,
\qquad
\alpha=0.0295544664514918\ldots.
\]
This application is an actual inequality for the full target class, not a Gaussian surrogate. It does not improve the already established lower obstruction `C_*>=3sqrt(2)`, but it shows that strict spectral inequality, disconnected support, arbitrarily remote support, and a nonvanishing satellite probability do not force a large gap below the sharp diffuse obstruction.

## 6. Consequences for witness search

The centered-Gaussian rank-three mechanism is now completely pinned at its global density maximum: under the variance floor forced by cap-one product inputs it cannot exceed `3sqrt(2)`, and quantitative determinant slack makes it strictly smaller by (3.1). Therefore any genuine witness above `3sqrt(2)`, if one exists, must use a mechanism absent from this centered Gaussian rank-three class: a surviving non-Gaussian component, noncentral/off-center structure, interacting extra active spectrum, or another product-preserving effect. The partner fragmented family remains a sharp stress test because its finite laws are genuinely non-Gaussian and disconnected, but its proved lower curve still approaches `3sqrt(2)` from below.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**. Continuity is proved here only for the centered Gaussian rank-three theorem.
