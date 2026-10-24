# All-activity matching-edge negativity with heterogeneous terminal spokes over a weighted three-vertex core

Research continuation, 2 October 2026. Complete analytic derivation; an
independent adversarial audit is requested. Historical novelty is unverified.
This extends the separate common-spoke theorem and does not alter it.

## Theorem and exact scope

Let the core have three vertices with arbitrary edge activities p,q,r>=0.
Let m>=4 further terminal vertices have no edges between them initially.
Terminal j is joined to each of the three core vertices with one common
activity a_j>=0, with no requirement that different terminals have the same
activity. Add marked edges e between terminals 1,2 and f between terminals
3,4, with arbitrary positive marked activities. Suppose a_1,a_2,a_3,a_4>0.

Then the two marked indicators have strictly negative covariance under
the weighted unrooted forest measure, at every positive choice of the
marked activities. Equivalently their Rayleigh difference is strictly
positive. Other terminal activities can be zero. Missing core edges are
allowed. Parallel core edges can be aggregated by summing their activities.

Only this matching/matching pair is claimed. The theorem does not assert
the inequality for arbitrary spoke or core pairs, arbitrary three-by-m
edge weights, or a core of unrestricted size.

## 1. Complete three-port forest partition

Write

\[
 X=p+q+r,\quad t=pq+pr+qr,\quad
 S=1+X+t,\quad L=3+2X.
\]

For a terminal of spoke activity x, define

\[
 d(x)=1+3x,\qquad
 \alpha(x)=\frac{x^2}{1+3x},\qquad
 \gamma(x)=\frac{x^3}{(1+3x)^2}.
\]

The five-state transfer on partitions of the three core vertices is

\[
 T(x)=d(x)I+x^2P+x^3Q,
 \qquad P^2=6Q,\quad PQ=QP=Q^2=0.                   \tag{1}
\]

Here P chooses two core vertices in distinct existing blocks and merges
them; Q chooses all three vertices, possible only from the singleton
partition. The factor six comes from three first pair choices and two
second choices joining the remaining core vertex. This is the exact
acyclicity test for the three spokes of the new terminal.

Since `gamma+3alpha^2=x^3/d`, the normalized transfer has the exact
finite-dimensional exponential expression

\[
 T(x)=d(x)\exp[\alpha(x)P+\gamma(x)Q].               \tag{2}
\]

All these transfers commute, as polynomials in the same P,Q. For any
terminal list a_1,...,a_m, set

\[
 D=\prod_{j=1}^m d(a_j),\qquad
 U=\sum_{j=1}^m\alpha(a_j),\qquad
 \Gamma=\sum_{j=1}^m\gamma(a_j).
\]

The initial core-forest row v obeys `v1=S`, `vP1=L`, `vQ1=1`. Multiplying
(2) over all terminals gives the full partition with the two marks absent:

\[
 A=D\mathcal F(U,\Gamma),\qquad
 \mathcal F(U,\Gamma)=S+LU+\Gamma+3U^2.              \tag{3}
\]

One can also derive (3) by classifying zero, one, or two terminal bridges
between the initial core components. Two bridges supply the coefficient
six; three bridges are impossible with only three core vertices. Thus (3)
counts all forests, for arbitrarily many terminals and arbitrary finite
activities. There is no small-activity expansion.

## 2. Disjoint marked contractions

The forest polynomial is multiaffine in the two marked activities:

\[
 Z=A+z_e B_e+z_f B_f+z_ez_f C,
 \qquad R_{ef}=B_eB_f-AC.                           \tag{4}
\]

For each marked pair i=(a,b), contraction replaces its two terminals by
one terminal of activity a+b. Indeed, the two spokes to each core vertex
become parallel; a forest can select at most one, and their activity sum
is exact. The two marked pairs are disjoint, so their contractions commute.

Define the positive scalar and response increments

\[
 c_i=\frac{d(a+b)}{d(a)d(b)},\qquad
 \delta_i=\alpha(a+b)-\alpha(a)-\alpha(b),\qquad
 \epsilon_i=\gamma(a+b)-\gamma(a)-\gamma(b).          \tag{5}
\]

For e use a_1,a_2; for f use a_3,a_4. The exact four coefficients are

\[
 \begin{aligned}
 A&=D\mathcal F(U,\Gamma),\\
 B_e&=Dc_e\mathcal F(U+\delta_e,\Gamma+\epsilon_e),\\
 B_f&=Dc_f\mathcal F(U+\delta_f,\Gamma+\epsilon_f),\\
 C&=Dc_ec_f\mathcal F(U+\delta_e+\delta_f,
                      \Gamma+\epsilon_e+\epsilon_f).
 \end{aligned}                                     \tag{6}
\]

The scalar normalizations must be retained. They satisfy exactly
`D_e D_f=D D_ef=D^2 c_e c_f`, so the same positive scalar multiplies both
terms in (4).

Let F=mathcal F(U,Gamma) and write

\[
 J_i=\delta_i(L+6U)+\epsilon_i+3\delta_i^2.
\]

The single contraction changes F to F+J_i; the double contraction changes
it to `F+J_e+J_f+6delta_e delta_f`. Hence the full finite-activity Rayleigh
difference is exactly

\[
 \boxed{R_{ef}=D^2c_ec_f
       [J_eJ_f-6\delta_e\delta_f F].}                \tag{7}
\]

## 3. The sign inequalities

For x>0,

\[
 \frac{\alpha(x)}x=\frac{x}{1+3x},\qquad
 \frac{\gamma(x)}x=\left(\frac{x}{1+3x}\right)^2
\]

are strictly increasing. If a,b>0, evaluate these ratios at a+b and
multiply respectively by a and b to obtain
`alpha(a+b)>alpha(a)+alpha(b)` and
`gamma(a+b)>gamma(a)+gamma(b)`. Thus the four endpoint assumptions give
delta_e,delta_f>0 and epsilon_e,epsilon_f>0. The explicit first increment,
if desired, is

\[
 \delta_i=\frac{ab[2+3(a+b)]}{d(a)d(b)d(a+b)}>0.
\]

Each terminal also obeys

\[
 0\le\gamma(x)<\alpha(x)/3\quad(x>0),
 \qquad \alpha(x)/3-\gamma(x)=\frac{x^2}{3(1+3x)^2}.
                                                               \tag{8}
\]

At zero both sides vanish, so summation gives Gamma<=U/3. From (7),
discarding only the nonnegative extra terms inside each J_i gives

\[
 \begin{aligned}
 \frac{R_{ef}}{D^2c_ec_f}
 &\ge\delta_e\delta_f[(L+6U)^2-6F]\\
 &=\delta_e\delta_f[L^2-6S+6LU+18U^2-6\Gamma]\\
 &\ge\delta_e\delta_f[L^2-6S+(6L-2)U+18U^2]>0.       \tag{9}
 \end{aligned}
\]

The last strict inequality follows because L>=3, U>=0, and

\[
 L^2-6S=3+6X+4(p^2+q^2+r^2)+2(pq+pr+qr)>0.          \tag{10}
\]

This proves the theorem. Multiaffinity makes R independent of z_e,z_f;
the corresponding covariance is `-z_e z_f R/Z^2`, strictly negative for
positive marked activities.

## Verification and limits

The accompanying `forest_twin_matching_heterogeneous_core3_exact.py`
independently enumerates subsets of the original uncontracted graph at
heterogeneous parameter choices, rather than computing the coefficients
by the response formula. Independent audit files will be added separately.

The argument proves only the stated unbounded weighted family. It does not
prove the general forest conjecture, arbitrary separator positivity, or
negative association. Known two-sum and series-parallel results should be
credited, and historical novelty of this precise family remains unverified.
