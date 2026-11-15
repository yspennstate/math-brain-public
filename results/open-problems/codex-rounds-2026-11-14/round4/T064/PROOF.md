# A bound using the local type of a crossing threshold

Let f be the variance-one random plane wave with covariance J_0(|x-y|).
Let Q=[0,L]x[0,H], where L,H>0, A=LH and P=2(L+H). Let p_Q(t)
be the probability of a left-to-right crossing of {f>=t} in Q, with
endpoints allowed on the closed vertical sides. All lengths use
wavenumber one. Write

    phi(t) = exp(-t^2/2)/sqrt(2 pi),
    B(t) = exp(-t^2)/(2 sqrt(pi)) + t erf(t)/2,
    beta(t) = phi(t) B(t)/sqrt(pi),
    s(t) = phi(t) exp(-t^2)/(4 pi).

The function beta is the edge-critical height intensity in the
preceding report. Define

    D_Q(t) = A s(t) + P beta(t)/4
             + (H-L) t phi(t)/(4 sqrt(pi)) + phi(t).        (1)

## Proposition

For every finite a<b,

    0 <= p_Q(a)-p_Q(b) <= integral_a^b D_Q(t) dt.           (2)

In particular p_Q is absolutely continuous, with
0<=-p_Q'(t)<=D_Q(t) for almost every t. Although (1) has a signed
summand, D_Q is nonnegative: its edge part is a sum of nonnegative
one-sided Gaussian expectations, as shown below.

Here is a closed form for comparison with level zero. For d>=0 put

    S(d) = erf(sqrt(3/2) d)/(8 pi sqrt(3)),
    J(d) = sqrt(3) erf(sqrt(3/2) d)/(4 pi)
           - phi(d) erf(d)/(2 sqrt(pi)),
    K(d) = erf(d/sqrt(2))/2.

For u!=0 and d=|u|, (2) gives

    |p_Q(u)-p_Q(0)|
      <= A S(d) + P J(d)/4 + K(d)
         + sign(u)(H-L)[phi(0)-phi(d)]/(4 sqrt(pi)).        (3)

At u=0 the bound is zero. For a square this simplifies to

    |p_[0,R]^2(u)-1/2| <= R^2 S(|u|)+R J(|u|)+K(|u|).     (4)

Its small-level expansion is

    phi(0) [R^2/(4 pi) + R/(2 pi) + 1] |u|
      + O((R^2+R+1)|u|^3).                               (5)

The preceding bound has R/(2 pi) and 1 replaced by 2R/pi and 4.
The area coefficient at zero is unchanged. In particular (4) still
gives convergence to 1/2 only under the sufficient condition
|u_R| R^2 ->0; no improvement of that level scale follows here.

## 1. Generic thresholds and strict crossing paths

Stratify Q into its interior, four open edges and four corners.
Almost surely f has nondegenerate critical points on each stratum,
nonzero normal derivative at an edge-critical point, nonzero derivatives
in both edge directions at each corner, and distinct stratified
critical values. These generic properties for the RPW follow from
Lemma 2.9 of [1]. Definition 2.7 there identifies a unique stratified
critical point at the crossing threshold. The ordinary superlevel
threshold T used here is the negative of that paper's threshold height.

The following additional fact is Lemma B.4 of [1]: at T there is a
crossing path contained in {f>T} together with the single threshold
point x. The path must use x. A crossing entirely in {f>T} is compact,
so its minimum is strictly greater than T, which contradicts the
definition of T. These facts apply to the RPW because it satisfies
the assumptions of [1], as explicitly noted in its Example 1.4.

We use this strict path to classify local types; we do not assume that
every point of the listed types is actually a crossing threshold.

If x is away from the two target sides, take the two path segments
leaving x toward those sides. If their short initial pieces can be
joined in {f>T} in a small neighbourhood of x, replacing the portion
through x produces a crossing entirely in {f>T}, a contradiction.
One may first erase loops from the path, or use its first and last
exit from the neighbourhood to make this replacement.

If x belongs to a target side, keep the subpath from x to the opposite
side. If its initial piece can be joined in {f>T} to another point
of the same target side, moving the endpoint produces the same
contradiction. Neighbourhoods are chosen small enough to avoid every
nonincident side and every other corner. The replacement crossing is
compact, so strict inequality again gives a strictly larger level.

## 2. Interior, edge and corner classification

An interior nondegenerate maximum has no strict superlevel points
near x. An interior nondegenerate minimum has a connected punctured
strict superlevel neighbourhood, so the path can be rerouted. The
Morse lemma therefore forces an interior threshold to be a saddle:

    det Hess f(x) < 0.                                    (6)

At an edge point use a coordinate r>=0 pointing into Q and a tangent
coordinate z. At an edge critical point the boundary Morse normal
form can be taken to be

    f-T = epsilon r + eta z^2,    epsilon,eta in {-1,+1},  (7)

after a local change of coordinates preserving r=0 and r>=0.
Here epsilon is the sign of the inward derivative and eta is the
sign of the tangential second derivative. To see (7), first apply
the one-dimensional Morse lemma on r=0; then write f-T=h(r,z)r+eta z^2,
where h(0,0)!=0, and replace r by |h(r,z)|r. The Jacobian of this
last change is nonsingular at zero and preserves the half-plane.

All four possibilities can be checked directly:

| Form | Strict superlevel near the origin |
| --- | --- |
| -r-z^2 | empty |
| r+z^2 | connected, and reaches r=0 at z!=0 |
| r-z^2 | connected, and has no point on r=0 |
| -r+z^2 | two components, each reaching r=0 at z!=0 |

The connectivity statements hold in a sufficiently small adapted
half-neighbourhood, for example |z|<rho and 0<=r<2rho^2 in the
normal-form coordinates. Every positive point sufficiently close
to the origin can be joined within the indicated positive component
to any fixed sufficiently close point of that component.

On a horizontal edge x is not a crossing endpoint. Only the last
row has two positive components; in the middle two rows the path
can be rerouted, and in the first row it cannot approach x. Hence
a horizontal-edge threshold must satisfy

    f_zz(x)>0,     f_in(x)<0.                             (8)

On a vertical edge x can serve as a target endpoint. In the second
and fourth rows each positive component meets the target edge away
from x, so the endpoint can be moved. The first row has no positive
access. Thus a vertical-edge threshold must satisfy

    f_zz(x)<0,     f_in(x)>0.                             (9)

At a corner take r>=0 normal into Q from its vertical target side,
and z>=0 along that target side toward its interior. Put

    a = f_r(x),    b = f_z(x).

Both are nonzero. If both are negative, there is no positive access
near x. If b>0, every positive point sufficiently close to x can
be connected locally to a positive point on r=0, z>0: shrink the
neighbourhood so that both derivative signs are fixed; increase z
and, when a<0, decrease r, or, when a>0, first increase z enough
to stay positive while decreasing r. Such paths stay in an
arbitrarily small neighbourhood when their starting points are
sufficiently close to x. This moves the target endpoint and is
impossible at a threshold. Consequently the only eligible corner
signs are

    a>0,    b<0.                                         (10)

These are necessary local conditions, not sufficient global conditions.

## 3. Conditional Gaussian jets

Differentiating J_0, or averaging the spectral monomials on the unit
circle, gives

    Cov(grad f) = I/2,
    E[f f_11] = E[f f_22] = -1/2,
    Var(f_11) = Var(f_22) = 3/8,
    E[f_11 f_22] = Var(f_12) = 1/8.

Odd derivative covariances vanish. The gradient is independent of
(f,Hess f), and its density at zero is 1/pi. Conditional on f=t,

    Hess f = [ -t/2+X      Y     ]
             [    Y     -t/2-X ],

where X,Y are independent N(0,1/8). Thus Z=X^2+Y^2 has density
4 exp(-4z), z>=0, and det Hess f=t^2/4-Z. With c=t^2/4,

    E[|det Hess f| 1_{det Hess f<0} | f=t,grad f=0]
      = integral_c^infinity (z-c)4 exp(-4z) dz
      = exp(-t^2)/4.                                     (11)

Marked Kac–Rice therefore gives the interior saddle height density
s(t) per unit area. In particular this computation respects the
deterministic Helmholtz trace relation Delta f=-f.

For a straight edge the tangent derivative f_z has density 1/sqrt(pi)
at zero. The inward derivative is an independent N(0,1/2), independent
also of (f,f_z,f_zz). Given f=t and f_z=0,

    V := f_zz has law N(-t/2,1/8),
    E|V| = B(t),    E V = -t/2.

The absolute-normal mean follows by splitting its Gaussian integral
at zero. Splitting into positive and negative parts also gives

    E[(-V)_+] = [B(t)+t/2]/2,
    E[V_+] = [B(t)-t/2]/2.                               (12)

The inward-derivative sign restriction contributes a factor 1/2.
By (8)–(9) the respective eligible densities per unit edge length are

    v(t) = phi(t)[B(t)+t/2]/(4 sqrt(pi))   (vertical),
    h(t) = phi(t)[B(t)-t/2]/(4 sqrt(pi))   (horizontal).    (13)

The total lengths are 2H and 2L. Thus

    2H v(t)+2L h(t)
       = P beta(t)/4 + (H-L)t phi(t)/(4 sqrt(pi)).         (14)

This establishes the nonnegativity of the edge term in (1).

At a corner, f is independent of its two orthogonal gradient
components, which are independent centred normals. Conditional on
f=t, the sign pattern (10) has probability 1/4. Each corner contributes
phi(t)/4; all four together contribute phi(t). Independence of
different corners is neither assumed nor needed.

All marked Kac–Rice uses here are one-point formulas for either
grad f or an edge tangent derivative; their Gaussian zero densities
are nonsingular, all required moments are finite, and the relevant
critical points are almost surely nondegenerate. The sign marks can
equivalently be obtained as limits of bounded continuous marks;
their equality boundaries have zero conditional probability.

## 4. Probability domination

For a<b, if crossing holds at a but fails at b, its unique threshold
T lies in [a,b]. By Section 2 it is one of the eligible points
counted above. Therefore the indicator of this event is bounded by
the number of eligible stratified critical points with values in
[a,b]. Their expected number, by (11)–(14) and the corner computation,
is integral_a^b D_Q(t)dt. This proves (2).

There is no endpoint atom: for every fixed t, the expected number of
all stratified critical points of value exactly t is zero by the
same height-marked formulas, including the unmarked corner heights.
Domination on intervals extends to open sets by disjoint intervals
and then to Borel sets by outer regularity. The threshold law is
therefore dominated by D_Q(t)dt, which proves absolute continuity
and the derivative assertion.

Direct integration gives

    integral_0^d s(t) dt = S(d),
    integral_0^d beta(t) dt = J(d),
    integral_0^d phi(t) dt = K(d),
    integral_0^d t phi(t) dt = phi(0)-phi(d).

The first identity follows from phi(t)exp(-t^2)=
exp(-3t^2/2)/sqrt(2 pi). For the second, integrate the t phi(t)erf(t)
part by parts using phi'=-t phi and erf'=2exp(-t^2)/sqrt(pi).
The other two are immediate Gaussian integrals. The first three
integrands are even and the fourth is odd, yielding (3).
Square duality and sign/rotation invariance give p_[0,R]^2(0)=1/2
(also Lemma C.1 of [1]), hence (4). Taylor expansion at zero gives
S(d)=phi(0)d/(4 pi)+O(d^3), J(d)=phi(0)d/(2 pi)+O(d^3), and
K(d)=phi(0)d+O(d^3), proving (5).

## 5. Comparison, orientation and sharpness of the corner coefficient

The preceding report counts all interior critical points with density

    alpha(t)=phi(t)[t^2-1+2exp(-t^2)]/(4 pi).

Subtracting (11) gives

    alpha(t)-s(t)
      = phi(t)[t^2-1+exp(-t^2)]/(4 pi) >=0,               (15)

because e^(-q)>=1-q for q>=0. Its integral over [0,d] is

    phi(0)d^5/(40 pi)+O(d^7).

Each v,h in (13) is at most beta: it counts a subset of edge critical
points. The corner intensity is reduced from 4phi to phi. Thus (2)
is never weaker than the preceding all-critical-point bound.
It is strictly stronger on every nonempty finite interval for L,H>0.

Rotating Q by pi/2 and replacing f by -f interchanges primal and dual
crossings. The density respects this operation exactly:

    D_{L,H}(t) = D_{H,L}(-t),

since B, beta and s are even. In particular the signed term in (1)
cannot generally be omitted on a nonsquare at a nonzero level.

For an independent check on corner signs, take the affine deterministic
function g(x,y)=a x+b y, with a,b nonzero. Every crossing meets every
vertical slice, so its threshold is at most

    min_{0<=x<=L} max_{0<=y<=H} g(x,y)
       = min(0,aL)+max(0,bH).

The horizontal segment on the maximizing top or bottom side attains
this value, so equality holds. Its threshold location is precisely
the corner with positive derivative normal in from the target side
and negative derivative along that side into Q, in agreement with
(10), for all four choices of signs of a,b.

Finally the corner coefficient 1 is optimal among bounds of this
form with fixed locally integrable area and perimeter densities.
Fix a rectangle shape Q_0 with a corner at zero and shrink Q=epsilon Q_0.
By continuity, sup_Q |f-f(0)| ->0 almost surely. The maximin crossing
threshold lies between min_Q f and max_Q f, so T_Q -> f(0) almost surely.
Consequently p_Q(a)-p_Q(b) -> integral_a^b phi(t)dt for every a<b.
The area and perimeter terms in an interval bound tend to zero.
Replacing the corner density phi by c phi with c<1 would give the
false inequality integral_a^b phi <=c integral_a^b phi in this limit.
Thus the improvement from four corner contributions to one reaches
the best possible constant in this class of bounds.

## Scope

The result imposes only necessary local conditions for crossing
pivotality. It gives no conditional macroscopic arm estimate, zero-level
RSW for nonsquares, conformal limit, or new critical exponent. The
small-rectangle sharpness concerns the corner term, not large-scale
critical behavior. No claim of literature priority is made.

[1] Stephen Muirhead, Alejandro Rivera and Hugo Vanneuville, with an
appendix by Laurin Köhler-Schindler, *The phase transition for planar
Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3).
Used for genericity and the strict threshold path, not for the explicit
Gaussian densities or constants above.
