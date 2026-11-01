# C0032 — complete-Bernstein radius map and a fixed-contour all-radius inverse

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), arXiv:1109.3343v4, heavy-tailed limiting law `mu_alpha`; underlying scalar characterization: Charles Bordenave, Pietro Caputo and Djalil Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011), arXiv:1006.1713v5.

Status of this artifact: theorem-sized **PARTIAL / OPEN** progress. It proves that a natural power of the physical radius map is a complete Bernstein function, which gives an exact global slit-plane root count. It then replaces the remaining positive-real inverse by a fixed family of argument-principle contour integrals whose contours do not depend on the unknown root. This is a candidate source-matching explicit transform representation, but this artifact does **not** promote C0032 to PROVED: the source word “explicit” is informal, no independent P26 + distinct OTHER-track audits exist for this representation, and no source-closure paper package is claimed.

Methods executed in this recovery cycle: **B15 / B8 / B25**.

## 1. Cumulative starting point

Fix

\[
0<\alpha<2,\qquad \beta=\alpha/2\in(0,1),
\]

and write

\[
c_\beta=\Gamma(1-\beta),\qquad
C_\beta=\Gamma(1-\beta)\Gamma(1+\beta)=c_\beta\Gamma(1+\beta).
\]

Let `S,S'` be independent positive beta-stable random variables in the BCC normalization

\[
\mathbb E e^{-tS}=e^{-c_\beta t^\beta}.
\]

Earlier verified R7-06 work eliminated the BCC fixed-point unknown and proved that, for

\[
T=SS',\qquad
q_\beta(a)=\mathbb E\frac{T}{a+T},
\tag{1.1}
\]

the squared physical radius is parameterized by

\[
R_\beta(a)
=a\left(\frac{q_\beta(a)}{C_\beta}\right)^{1/\beta},
\qquad a>0,
\tag{1.2}
\]

where `R_beta:(0,infinity)->(0,infinity)` is a smooth strictly increasing bijection. If

\[
M_\beta(r)=\mu_{2\beta}\{|z|^2\le r\},
\qquad Q_\beta(r)=1-M_\beta(r),
\]

then

\[
Q_\beta(R_\beta(a))=q_\beta(a)
\tag{1.3}
\]

and

\[
g_{2\beta}(\sqrt{R_\beta(a)})
=-\frac{q_\beta'(a)}{\pi R_\beta'(a)}.
\tag{1.4}
\]

The previous STUCK2 diagnosis isolated the only remaining strict-form obstruction as the inverse `R_beta^{-1}` and precommitted this run to complex inversion.

The exact Mellin transform already proved for `q_beta` is

\[
\widehat q_\beta(s)
=c_\beta^{2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)},
\qquad 0<\Re s<\beta.
\tag{1.5}
\]

Thus, with the principal logarithm on the slit plane, for every fixed `sigma in (0,beta)`,

\[
q_\beta(z)
=\frac1{2\pi i}
\int_{\sigma-i\infty}^{\sigma+i\infty}
 c_\beta^{2s/\beta}
 \frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)}
 z^{-s}\,ds.
\tag{1.6}
\]

Stirling's formula gives exponential decay `exp(-pi |Im s|/beta)` before the factor `z^{-s}`; because `|arg z|<pi<pi/beta`, (1.6) converges locally uniformly on

\[
\Omega:=\mathbb C\setminus(-\infty,0],
\]

so it supplies the holomorphic slit-plane continuation used below.

## 2. B15 — complexify the radius map: the correct object is complete Bernstein

The key move is not to complexify `R_beta` directly, whose `1/beta` power makes branch bookkeeping awkward. Instead take the beta-th power

\[
\boxed{
H_\beta(a):=R_\beta(a)^\beta
=\frac{a^\beta q_\beta(a)}{C_\beta}.
}
\tag{2.1}
\]

The physical inversion `R_beta(a)=r` is equivalent to the **single-valued** equation

\[
H_\beta(a)=r^\beta.
\tag{2.2}
\]

### Theorem 2.1 — `H_beta` is a complete Bernstein function

For every `0<beta<1`, `H_beta` is a nonconstant complete Bernstein function on `(0,infinity)`. Consequently it extends holomorphically to `Omega` and satisfies

\[
\operatorname{sgn}\Im H_\beta(z)=\operatorname{sgn}\Im z
\qquad(z\in\Omega\setminus(0,\infty)),
\tag{2.3}
\]

with strict sign in the open upper and lower half-planes.

#### Proof

The previous elimination used

\[
F_\beta(a)=\mathbb E(S'+a/S)^{-\beta},
\qquad q_\beta(a)=C_\beta F_\beta(a).
\]

Since

\[
S'+a/S=\frac{a+SS'}S,
\]

we have

\[
F_\beta(a)
=\mathbb E\frac{S^\beta}{(a+SS')^\beta}.
\]

Therefore

\[
H_\beta(a)=a^\beta F_\beta(a)
=\mathbb E\left[S^\beta
\left(\frac{a}{a+SS'}\right)^\beta\right].
\tag{2.4}
\]

Define a positive Borel measure on `(0,infinity)` by

\[
\nu_\beta(B)
:=\mathbb E\left[S^\beta\mathbf 1_{\{SS'\in B\}}\right].
\tag{2.5}
\]

Although `nu_beta` has infinite total mass, it is locally finite. Indeed, for every compact interval `[u,v] subset (0,infinity)`,

\[
F_\beta(1)
=\int_0^\infty(1+t)^{-\beta}\nu_\beta(dt)
\ge (1+v)^{-\beta}\nu_\beta([u,v]),
\]

so

\[
\nu_\beta([u,v])\le (1+v)^\beta F_\beta(1)<\infty.
\tag{2.6}
\]

Equation (2.4) becomes the generalized Stieltjes representation

\[
\boxed{
H_\beta(a)
=\int_0^\infty
\left(\frac{a}{a+t}\right)^\beta
\nu_\beta(dt).
}
\tag{2.7}
\]

For fixed `t>0`, set

\[
\phi_t(z)=\left(\frac{z}{z+t}\right)^\beta
\tag{2.8}
\]

with the principal beta-th power. If `Im z>0`, then

\[
\Im\frac{z}{z+t}
=\frac{t\Im z}{|z+t|^2}>0.
\]

Hence `z/(z+t)` lies in the upper half-plane, and its principal beta-th power lies in the sector `0<arg w<beta*pi`, still in the upper half-plane. Also `phi_t(a)>0` for `a>0`. Thus `phi_t` is a complete Bernstein function by the standard Pick/Nevanlinna characterization of complete Bernstein functions.

Let

\[
\nu_{\beta,n}=\nu_\beta|_{[1/n,n]},
\qquad
H_{\beta,n}(z)=\int_{1/n}^{n}\phi_t(z)\nu_\beta(dt).
\tag{2.9}
\]

The measure in (2.9) is finite. The integral is holomorphic on `Omega`, positive on `(0,infinity)`, and maps the upper half-plane into its closure, so each `H_{beta,n}` is complete Bernstein. On the positive axis,

\[
H_{\beta,n}(a)\uparrow H_\beta(a)<\infty.
\]

The class of complete Bernstein functions is closed under finite nonnegative linear combinations and finite pointwise limits, hence under this monotone pointwise limit. Therefore `H_beta` is complete Bernstein.

It is nonconstant because `R_beta` was already proved strictly increasing. Equivalently, differentiating the positive kernel in (2.7) gives a strictly positive derivative on `(0,infinity)`. A nonconstant holomorphic Pick function cannot take an interior point of the upper half-plane to the real boundary: the open mapping theorem upgrades `Im H>=0` to `Im H>0` there. Complex conjugation gives the lower-half-plane statement. QED.

### Corollary 2.2 — exact global root count in the slit plane

For every `x>0`,

\[
\boxed{H_\beta(z)=x}
\tag{2.10}
\]

has exactly one solution in `Omega`, and that solution belongs to `(0,infinity)`.

#### Proof

If `Im z>0`, Theorem 2.1 gives `Im H_beta(z)>0`, so `H_beta(z)` cannot equal the positive real number `x`. The same excludes the lower half-plane. Hence every solution in `Omega` is positive real.

On `(0,infinity)`, `H_beta(a)=R_beta(a)^beta` is strictly increasing. Also

\[
H_\beta(0+)=0.
\]

At infinity, the stable tail implies `E[S^beta;S<=a]` grows logarithmically; restricting (2.4) to `{S<=a,S'<=1}` gives `H_beta(a)>=c log a` for all large `a`. Thus `H_beta(a)->infinity`. There is exactly one positive solution. QED.

This is the relevant complex branch theorem that STUCK2 lacked. It does **not** assert that `H_beta` is globally univalent for arbitrary complex target values. It proves the stronger-for-our-purpose fact that every positive physical target has exactly one preimage in the entire canonical slit domain.

### Special-case check at `alpha=1`

For `beta=1/2`, earlier work proved

\[
H_{1/2}(a)
=\frac\pi2\left[\mathbf H_0\left(\frac\pi{2\sqrt a}\right)
-Y_0\left(\frac\pi{2\sqrt a}\right)\right].
\tag{2.11}
\]

Theorem 2.1 therefore implies, as a new structural statement about this classical Struve/Bessel combination composed with `a^{-1/2}`, that it is a complete Bernstein function of `a`. Its positive inverse is the simplest interior member of the general construction below.

## 3. B8 — finite discretization: the naive model fails, and the CBF model repairs it

STUCK2 proposed finite atomic models to inspect branch topology. The first result is a warning: discretizing the **probability law of `T=SS'` itself** destroys the topology that makes the true radius map invertible.

### Proposition 3.1 — naive finite atoms force a spurious positive critical point

Let

\[
q_N(a)=\sum_{j=1}^N p_j\frac{t_j}{a+t_j},
\qquad p_j>0,\quad t_j>0,\quad\sum_jp_j=1,
\]

and imitate (2.1) by

\[
H_N^{\rm naive}(a)=\frac{a^\beta q_N(a)}{C_\beta}.
\tag{3.1}
\]

Then

\[
H_N^{\rm naive}(0+)=0,
\qquad
H_N^{\rm naive}(a)\sim
\frac{\sum_jp_jt_j}{C_\beta}a^{\beta-1}\to0
\quad(a\to\infty).
\tag{3.2}
\]

Since `H_N^naive(a)>0` in between, it attains a positive interior maximum and hence has at least one positive critical point. In particular, for generic `x` below that maximum the equation `H_N^naive(a)=x` has more than one positive solution.

Thus finite-atom discretization of `T` creates exactly the branch pathology we were trying to diagnose. The reason is conceptual: every finite atomic `T` has finite first moment, whereas the true stable product has the infinite-tail structure responsible for the logarithmic growth `H_beta(a)->infinity`.

### Proposition 3.2 — topology-preserving discretization of the generalized Stieltjes measure

The representation (2.7) identifies the correct object to discretize. For a finite positive atomic measure

\[
\nu_N=\sum_{j=1}^N w_j\delta_{t_j},
\qquad w_j,t_j>0,
\]

define

\[
H_N(a)=\sum_{j=1}^Nw_j
\left(\frac{a}{a+t_j}\right)^\beta.
\tag{3.3}
\]

Then `H_N` is complete Bernstein, strictly increasing from `0` to

\[
W_N:=\sum_{j=1}^Nw_j.
\]

Consequently, for every `0<x<W_N`, `H_N(z)=x` has exactly one solution in `Omega`, positive real.

Moreover, the truncations

\[
\widetilde H_n(a)
=\int_{1/n}^{n}
\left(\frac{a}{a+t}\right)^\beta\nu_\beta(dt)
\tag{3.4}
\]

increase pointwise to `H_beta(a)`. Their total masses tend to infinity: by monotone convergence,

\[
\lim_{a\to\infty}H_\beta(a)=\nu_\beta((0,\infty))=\infty.
\tag{3.5}
\]

For a fixed `x>0`, let `a_*=H_beta^{-1}(x)`. Whenever `n` is large enough that `nu_beta([1/n,n])>x`, let `a_n` be the unique positive solution of `\widetilde H_n(a_n)=x`. Then

\[
\boxed{a_n\downarrow a_* .}
\tag{3.6}
\]

Indeed, `\widetilde H_n<=H_beta` gives `a_n>=a_*`, and monotonicity in `n` makes `a_n` decrease. For every `epsilon>0`,

\[
H_\beta(a_*+\epsilon)>x,
\]

so pointwise monotone convergence gives `\widetilde H_n(a_*+epsilon)>x` eventually; hence `a_n<a_*+epsilon` eventually.

Finally, each finite measure in (3.4) can be approximated by positive atomic quadrature. On real compact `a`-intervals, using nested partitions and right endpoints gives lower sums because `t -> (a/(a+t))^beta` decreases in `t`; refinement converges uniformly away from `a=0`. Every such atomic approximation remains complete Bernstein and therefore preserves the one-root slit-plane topology.

So B8 does not merely supply numerics: it explains which finite models preserve the analytic branch structure and which finite models necessarily create false branches.

## 4. B25 — count the same root twice: a fixed-contour inverse

The complete-Bernstein theorem now makes the argument principle global and canonical for positive physical targets.

Define the conformal map

\[
\chi(w)=\left(\frac{1+w}{1-w}\right)^2,
\qquad |w|<1.
\tag{4.1}
\]

The Möbius map `(1+w)/(1-w)` sends the unit disk conformally onto the right half-plane, and squaring sends the right half-plane conformally onto `Omega`. Hence `chi` is a conformal bijection

\[
\mathbb D\longrightarrow\Omega,
\]

with inverse

\[
\chi^{-1}(a)=\frac{\sqrt a-1}{\sqrt a+1}
\tag{4.2}
\]

for `a>0`.

For `x>0`, set

\[
G_{\beta,x}(w)=H_\beta(\chi(w))-x.
\tag{4.3}
\]

By Corollary 2.2, `G_{beta,x}` has exactly one zero in the unit disk,

\[
w_*=\chi^{-1}(H_\beta^{-1}(x))\in(-1,1).
\tag{4.4}
\]

It is simple because `H_beta'(a_*)>0` and `chi'(w_*)` is nonzero.

For `n>=2`, put `s_n=1-1/n`. Whenever the circle `|w|=s_n` contains no zero, define

\[
I_{\beta,x}(n)
:=\frac1{2\pi i}
\oint_{|w|=s_n}
 w\,\frac{G_{\beta,x}'(w)}{G_{\beta,x}(w)}\,dw.
\tag{4.5}
\]

There can be at most one exceptional `n` for which `s_n=|w_*|`. For every sufficiently large `n`, the circle contains the unique zero `w_*`, and the first-moment form of the argument principle gives

\[
I_{\beta,x}(n)=w_*.
\tag{4.6}
\]

Therefore the following limit is exact and uses a contour family fixed **before** the unknown root is known:

\[
\boxed{
\omega_\beta(x)
:=\lim_{n\to\infty}
\frac1{2\pi i}
\oint_{|w|=1-1/n}
 w\,
\frac{H_\beta'(\chi(w))\chi'(w)}
{H_\beta(\chi(w))-x}
\,dw
= w_*.
}
\tag{4.7}
\]

If one finite contour happens to pass through the zero, omit that single term of the sequence; it does not affect the limit. No unknown radius, root, branch point, or stopping rule appears in the definition.

Hence the positive inverse itself is

\[
\boxed{
H_\beta^{-1}(x)
=\chi(\omega_\beta(x))
=\left(\frac{1+\omega_\beta(x)}{1-\omega_\beta(x)}\right)^2.
}
\tag{4.8}
\]

Combining (1.6) and (2.1), the function in the integrand of (4.7) is itself explicit by a Mellin-Barnes transform:

\[
\boxed{
H_\beta(z)
=\frac{z^\beta}{C_\beta}
\frac1{2\pi i}
\int_{\sigma-i\infty}^{\sigma+i\infty}
 c_\beta^{2s/\beta}
 \frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)}
 z^{-s}\,ds,
\quad 0<\sigma<\beta.
}
\tag{4.9}
\]

Thus (4.7)–(4.9) are a root-free, fixed-contour representation of the exact inverse in terms only of Gamma functions, principal powers, and convergent contour integrals.

### Why this is not the vacuous statement “use a root finder”

The generic residue identity

\[
\frac1{2\pi i}\oint z\frac{f'(z)}{f(z)-x}\,dz
\]

is useful only after the number of enclosed roots and an admissible contour are known. Here Theorem 2.1 and Corollary 2.2 provide the missing global root theorem, while the disk uniformization (4.1) supplies a universal contour exhaustion independent of the root. That is precisely the global complex information absent at STUCK2.

## 5. Direct all-radius CDF and density with no hidden root solve

Let `rho>0` be the physical radius and put

\[
r=\rho^2,\qquad x=r^\beta=\rho^{2\beta}=\rho^\alpha.
\tag{5.1}
\]

Define

\[
w(\rho)=\omega_\beta(\rho^\alpha),
\qquad
a(\rho)=\chi(w(\rho)).
\tag{5.2}
\]

By (4.8), `a(rho)` is exactly the unique parameter satisfying `R_beta(a)=rho^2`, but it is now represented without a root solve.

Since

\[
H_\beta(a)=\frac{a^\beta q_\beta(a)}{C_\beta}=r^\beta,
\]

we get

\[
q_\beta(a)=C_\beta\left(\frac r a\right)^\beta.
\]

Therefore the physical radial tail is

\[
\boxed{
\overline M_\alpha(\rho)
:=1-\mu_\alpha\{|z|\le\rho\}
=C_\beta
\left[
\rho\frac{1-w(\rho)}{1+w(\rho)}
\right]^\alpha.
}
\tag{5.3}
\]

This is an all-`alpha`, all-positive-radius formula whose only non-elementary object is the fixed contour transform (4.7) with explicit Mellin-Barnes kernel (4.9).

For the planar density, differentiate with respect to the squared radius `r`. Let

\[
a=A_\beta(r)=H_\beta^{-1}(r^\beta).
\]

From `H_beta(a)=r^beta`,

\[
a'(r)=\frac{\beta r^{\beta-1}}{H_\beta'(a)}.
\tag{5.4}
\]

Also

\[
Q_\beta(r)=C_\beta r^\beta a^{-\beta}.
\]

Thus

\[
\frac{Q_\beta'(r)}{Q_\beta(r)}
=\frac\beta r-
\frac{\beta^2r^{\beta-1}}{aH_\beta'(a)}.
\]

Since `M_beta'(r)=pi g_{2beta}(sqrt r)=-Q_beta'(r)`, we obtain

\[
\boxed{
 g_\alpha(\rho)
=\frac{\beta\,\overline M_\alpha(\rho)}{\pi\rho^2}
\left[
\frac{\beta\rho^\alpha}
{a(\rho)H_\beta'(a(\rho))}-1
\right],
\qquad \rho>0.
}
\tag{5.5}
\]

Here `a(rho)=chi(omega_beta(rho^alpha))` is the fixed-contour expression (4.7)–(4.8). The derivative `H_beta'` can be obtained by differentiating (4.9), or directly from

\[
H_\beta'(a)
=\beta\int_0^\infty
\frac{t\,a^{\beta-1}}{(a+t)^{\beta+1}}
\nu_\beta(dt)>0.
\tag{5.6}
\]

At `rho=0`, use the already-proved exact origin value from the BCC formula / prior R7-06 work,

\[
\pi g_\alpha(0)=m_1^2m_\beta^{-1/\beta},
\qquad
m_q=\frac{\Gamma(1+q/\beta)}
{\Gamma(1+q)c_\beta^{q/\beta}}.
\tag{5.7}
\]

Equations (4.7), (4.9), (5.3), (5.5), and (5.7) therefore give a complete transform-level representation at every physical radius with the BCC self-consistent unknown and the positive root solve both removed.

## 6. Relation to current inversion literature

Fresh bounded literature checks on 2026-09-19 recovered:

1. Bordenave–Caputo–Chafaï, arXiv:1006.1713 / CMP 307 (2011), as the construction and PWIT/stable implicit-characterization source.
2. Bordenave–Chafaï, arXiv:1109.3343v4 / Probability Surveys 9 (2012), as the survey source carrying the statement that the heavy-tailed limiting law is not known explicitly.
3. James Chen and Sheehan Olver, *Computing inverses of Stieltjes transforms of probability measures*, Mathematics of Computation, published electronically 2026-01-14, DOI 10.1090/mcom/4159, arXiv:2410.16178. Their paper studies multivalued inverse Stieltjes transforms and uses contour/root-count machinery for rigorous inverse computation. It is the closest current methodological analogue located in this run, but the search did not expose the BCC radius map or formulas (4.7)–(5.5) there.
4. The complete-Bernstein/Pick facts used in Theorem 2.1 are standard; see Schilling, Song and Vondraček, *Bernstein Functions: Theory and Applications*, Chapters 6–7. In particular the slit-plane Pick characterization, convex-cone/limit closure, and examples `z/(z+t)` and `z^beta` are prior machinery, not claimed new here.

The search also checked combinations of `Bordenave`, `Chafai`, `mu_alpha`, `explicit density`, `inverse Stieltjes`, `complete Bernstein`, and `inverse function`. No later source-matching all-radius BCC density formula was located. This is **negative evidence only**, not a novelty certificate.

## 7. What moved mathematically and what did not

The frozen campaign metric remains

```text
M_jet = +infinity -> +infinity
```

because every finite origin jet was already explicit before this run. So the official frozen metric shows **NO MOVEMENT**.

Nevertheless the global obstruction did move:

- Before B15: only a positive-real monotone inverse `R_beta^{-1}` was known; complex branch/root geometry was uncontrolled.
- After B15: `H_beta=R_beta^beta` is complete Bernstein and every positive target has exactly one zero in the entire canonical slit plane.
- B8 shows why naive finite-atom stable-product discretization necessarily manufactures false turning points, and gives a topology-preserving CBF discretization that converges to the correct inverse.
- B25 turns the unique inverse into the fixed-contour expression (4.7), and hence gives the all-radius CDF/density formulas (5.3) and (5.5) with no self-consistent unknown and no hidden positive root solve.

The source remains labelled **PARTIAL / OPEN** under the owner's closure protocol because:

1. the source's word “explicit” is informal, so an independent audit should decide whether the transform-level formula is considered source-matching rather than merely a canonical inversion device;
2. the theorem has not received the required independent P26 audit plus a distinct OTHER-track audit;
3. no self-contained source-closure paper package has yet passed those audits;
4. the bounded literature search is not a novelty certificate.

## 8. Exact method outcomes

### B15 — break the positive-real symmetry by complexification

**Outcome: success on the relevant branch problem.** Passing from `R_beta` to `H_beta=R_beta^beta` exposes complete-Bernstein/Pick structure. Positive physical values have exactly one preimage in the whole slit plane. Full univalence for arbitrary complex target values is neither needed nor claimed.

### B8 — discretize

**Outcome: one route refuted, one repaired.** Finite atoms for `T=SS'` force `H_N^naive(infinity)=0` and therefore a spurious positive critical point. Discretizing the generalized measure `nu_beta` in (2.7) instead produces finite complete-Bernstein models with the correct one-root topology and convergent inverses.

### B25 — count the same thing twice

**Outcome: success.** The unique root is counted by the argument principle after disk uniformization. Its first moment gives the exact fixed-contour inverse (4.7), which feeds directly into the radial tail and density.

## 9. Natural next tests, not claims of closure

The most useful next nonrepeating methods are **B10 / B24 / B26**:

- **B10 (derandomize):** eliminate the remaining stable-law notation even from the proof of the CBF measure by deriving an explicit deterministic density or Mellin-Barnes Stieltjes measure for `H_beta`, if possible.
- **B24 (extremal object):** obtain explicit lower bounds for `|H_beta(chi(w))-x|` on the fixed circles and hence quantitative, uniform contour-truncation error estimates rather than only the exact limiting identity.
- **B26 (sporadic cases):** test `beta=1/2` and reciprocal-integer/rational beta against the Struve/Meijer-G representations to confirm the contour formula collapses to the previously derived special-function equations and to detect any branch anomaly before paper packaging.

No shared RESULTS/QUEUE/POSTED file, peer report, historical report, schedule, email, Drive object, or public resource is modified by this artifact.
