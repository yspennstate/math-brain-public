# Two proportional terminal pairs over an arbitrary weighted core

2 October 2026. Concrete high-fugacity consequence of the general H2
sum-of-squares formula; independently discovered and tested before the general
formula was obtained. This is a partial theorem, not a complete solution of
forest edge negative correlation. Novelty is not certified.

## Graph and coefficient convention

Let H be an arbitrary weighted graph on a core C with s vertices; H may be
disconnected. Add four distinct terminal vertices 0,1,2,3. Apart from the two
marked edges e=01 and f=23 there are no terminal--terminal edges. The spoke
conductances are

\[
 c_{0u}=\alpha a_u,\quad c_{1u}=\beta a_u,\quad
 c_{2u}=\gamma b_u,\quad c_{3u}=\delta b_u,
\]

where \(\alpha,\beta,\gamma,\delta>0\) and every \(a_u,b_u>0\).
Within each pair the spoke profiles need only be proportional. The two
profiles a,b may be different. Marked conductances may be arbitrary positive
numbers. All activities are scaled by \(\lambda\), and marked derivatives
are formed before that specialization.

Set \(n=s+4\). For the forest Rayleigh polynomial write

\[
 R_{ef}(\lambda c)
 =H_0\lambda^{2n-4}+H_1\lambda^{2n-5}
   +H_2\lambda^{2n-6}+O(\lambda^{2n-7}).
\]

The conclusion is \(H_0=H_1=0\), with the explicit strictly positive H2 below
when \(s\ge2\). Hence these marked indicators are strictly negatively
correlated at sufficiently large common fugacity. For \(s=1\) their entire
Rayleigh polynomial is zero.

## Closed formula

Let \(d_a=\sum_u a_u\), \(d_b=\sum_u b_u\), and define core Laplacians

\[
 P_a=\operatorname{diag}(a)-aa^T/d_a,
 \qquad P_b=\operatorname{diag}(b)-bb^T/d_b,
\]

\[
 N=L_H+(\alpha+\beta)P_a+(\gamma+\delta)P_b.
\]

Ground any core vertex r. Put \(T=N_r^{-1}\),
\(\Xi=\det N_r\), with the zero-dimensional conventions \(\Xi=1\) and
empty T when s=1. Every matrix in the trace below is a grounded principal
matrix, on C minus r. Then

\[
 \boxed{
 H_2=\alpha\beta\gamma\delta(\alpha+\beta)(\gamma+\delta)
 d_a^2d_b^2\Xi^2\operatorname{tr}(P_{a,r}T P_{b,r}T).
 }
\]

An equivalent rational sum of squares is obtained by writing
\(b_{uv}=e_u-e_v\) in grounded coordinates (\(e_r=0\)):

\[
 \boxed{
 H_2=\alpha\beta\gamma\delta(\alpha+\beta)(\gamma+\delta)d_ad_b
 \sum_{u<v}\sum_{x<y}a_ua_vb_xb_y
 \left[b_{uv}^T\operatorname{adj}(N_r)b_{xy}\right]^2.
 }
\]

Grounded \(P_{a,r},P_{b,r}\) are positive definite for s>=2: their
pairwise-difference energy vanishes only for a constant vector on all core
vertices, and grounding forces that constant to zero. N is likewise connected
and its grounded inverse is positive definite. Therefore the trace is strictly
positive. The formulas are independent of the chosen root.

## Derivation from the general formula

The forest Rayleigh polynomial is independent of the marked activities:
if \(Z=A+z_eB+z_fC+z_ez_fD\), then \(R_{ef}=BC-AD\). The graph remains
connected after deleting the marked edges, so the general Green formula can
be evaluated at zero marked conductances by continuity. Ground in the core.

The e-unit-current potential then equals
\(v_0=1/(\alpha d_a)\), \(v_1=-1/(\beta d_a)\), and is zero everywhere
else. The f-potential is analogous. Their supports are disjoint and have no
connecting edge, giving H0=H1=0. The common-zero set is precisely the core.

The terminal exit rows are
\(p_0=p_1=a^T/d_a\), \(p_2=p_3=b^T/d_b\), with grounded coordinates
removed. Eliminating terminal diagonals \(\alpha d_a,\beta d_a,\gamma d_b,
\delta d_b\) gives the effective core Laplacian N and spanning-tree weight

\[
 \tau=\alpha\beta\gamma\delta d_a^2d_b^2\Xi.
\]

For a terminal--core spoke, the general cycle response is
\(\eta_{e,0u}=v_0(e_u-a/d_a)\),
\(\eta_{e,1u}=v_1(e_u-a/d_a)\). All other e-responses are zero. Summing
the spoke conductances times their outer products gives

\[
 B_e=\frac{\alpha+\beta}{\alpha\beta d_a^2}P_{a,r},\qquad
 B_f=\frac{\gamma+\delta}{\gamma\delta d_b^2}P_{b,r}.
\]

Substitution in \(H_2=\tau^2\operatorname{tr}(TB_eTB_f)\) yields the first
formula. The identity

\[
 P_a=\frac1{d_a}\sum_{u<v}a_ua_v b_{uv}b_{uv}^T
\]

and \(\Xi T=\operatorname{adj}(N_r)\) yield the displayed sum of squares.
This proof includes unequal pair scalings without additional symmetry.

## Independent checks

`two_twin_pairs_H2_heat.py` computes the full forest Rayleigh coefficients
by direct acyclic subset enumeration and marked-edge insertion tests. Its
formula side independently constructs N and the two profile covariance
matrices with exact Fraction arithmetic. All 21 cases pass, with core sizes
1 through 4, arbitrary/disconnected weighted cores, unequal profiles, every
grounded core root, and the three scaling choices

* (1,1,1,1);
* (2,3,4,5);
* (1/2,2/3,3/4,4/5).

The adjacent JSON records the exact inputs, complete nonzero Rayleigh
coefficients, and exact predicted H2. The broad formula subsumes this family,
but this explicit consequence supplies a useful check of coefficient
normalization and an easily stated strict-positivity class.

## Relation to the earlier four-twin computation

If all four pair scalings equal one and a=b, this recovers the original
four-twin family. If \(M=L_H+4\operatorname{diag}(a)\), \(W=\det M\),
the weighted matrix-tree/rooted-forest identity gives \(\Xi=W/(4d_a)\).
The core covariance projection then makes this trace formula equivalent to
the earlier four-twin adjugate square formula. Unequal profiles and unequal
pair scalings go beyond that first symmetric construction.
