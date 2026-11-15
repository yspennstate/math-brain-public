# A finite-scale level-stability bound for RPW crossings

Let f be the centred, variance-one Gaussian field with covariance
E[f(x)f(y)] = J_0(|x-y|). All lengths below use this wavenumber-one
normalisation. For a rectangle Q with side lengths L,H > 0 let C_Q(u)
be the event that {f >= u} has a left-to-right path in Q, including its
boundary. Write p_Q(u) = P(C_Q(u)), A = LH, P = 2(L+H), and
phi(t) = exp(-t^2/2)/sqrt(2*pi).

Define the following nonnegative, even functions:

    alpha(t) = phi(t)/(4*pi) * (t^2 - 1 + 2 exp(-t^2)),
    beta(t)  = phi(t)/(2*pi) * exp(-t^2)
               + t phi(t)/(2 sqrt(pi)) * erf(t).

## Proposition

For every pair of finite real levels a < b,

    0 <= p_Q(a) - p_Q(b)
      <= A integral_a^b alpha(t) dt
         + P integral_a^b beta(t) dt
         + 4 integral_a^b phi(t) dt.                         (1)

In particular p_Q is absolutely continuous. With delta = |u|,

    |p_Q(u) - p_Q(0)| <= A I(delta) + P J(delta) + 4 K(delta), (2)

where

    I(d) = [erf(sqrt(3/2) d)/sqrt(3) - d phi(d)]/(4*pi),
    J(d) = sqrt(3)/(4*pi) erf(sqrt(3/2) d)
           - phi(d) erf(d)/(2 sqrt(pi)),
    K(d) = erf(d/sqrt(2))/2.                                 (3)

For Q = [0,R]^2, p_Q(0) = 1/2. Consequently, whenever R -> infinity
and |u_R| R^2 -> 0,

    p_[0,R]^2(u_R) -> 1/2.                                  (4)

More generally, for a fixed aspect ratio, (2) shows that a level change
u_R = o(R^(-2)) changes a rectangle's crossing probability by o(1),
whether or not its zero-level crossing probability has a limit.

An elementary bound without asymptotic notation is, for 0 <= delta <= 1,

    |p_Q(u)-p_Q(0)|
      <= phi(0) delta [A/(4*pi)
                       + P/(2*pi) (1+delta^2/3) + 4].       (2a)

This is an upper bound on level sensitivity. It asserts no sharpness of
the scale R^(-2) and gives no RSW estimate for nonsquare rectangles.

## 1. Which values can change a crossing?

Stratify Q into its interior, its four open edges and its four corners.
A stratified critical point is an interior zero of grad f, an open-edge
zero of the tangential derivative, or a corner. Count these points with
their values in [a,b], and call the resulting counts N_2, N_1 and N_0.

For a smooth deterministic function g on a neighbourhood of Q, if there
is no stratified critical point with value in [a,b], then {g >= a} and
{g >= b} are related by a homeomorphism of Q preserving each edge and
corner. Here is the required deformation argument.

The compact set Q intersect {a <= g <= b} contains no corners. In its
interior grad g is nonzero. On each open edge meeting this set, the
tangential derivative is nonzero. In an interior neighbourhood choose
the vector field grad g/|grad g|^2. Near an edge choose its unit tangent
tau and the vector field tau/(tau dot grad g). Shrink these edge
neighbourhoods so they avoid the other edges; this field is tangent to
the edge and has dg(V)=1. Use a smooth partition of unity to patch the
fields. Interior patches can be chosen not to meet the boundary. The
patched field is tangent to every edge it meets and still satisfies
dg(V)=1 on a neighbourhood of the level strip.

There is a slightly larger closed level interval about [a,b] with the
same properties: otherwise compactness would give a stratified critical
point with value in [a,b]. For this compactness argument an edge-critical
sequence can accumulate at a corner only if that corner has value in
[a,b], and an interior-critical sequence accumulating at an edge gives
a tangential critical point there. Both possibilities were excluded.

Choose a smooth nonnegative function chi of the value, equal to one on
[a,b] and supported in that slightly larger interval. Multiplying the
patched field by chi(g) and extending it by zero gives a smooth field
on Q tangent to all boundary edges and zero near all corners. Its flow
is defined for positive and negative finite times, preserves every
boundary stratum and satisfies dg/ds = chi(g). The scalar flow in the
value is increasing and carries a to b in time b-a. Thus the time-b-a
homeomorphism carries {g >= a} to {g >= b}. It preserves left-to-right
crossing existence.

Apply the contrapositive to a sample of f. Since C_Q(b) is a subset of
C_Q(a),

    1_{C_Q(a) minus C_Q(b)} <= N_2 + N_1 + N_0.              (5)

Counting all critical points is sufficient; no assertion that each is
pivotal is used. This also explains why boundary critical points and
corners cannot be dropped.

## 2. The one-point jet

The expansion

    J_0(|x|) = 1 - (x_1^2+x_2^2)/4
                 + (x_1^2+x_2^2)^2/64 + O(|x|^6)

and differentiation of the covariance give

    Var(f) = 1,
    Cov(grad f) = (1/2) Id,
    E[f f_11] = E[f f_22] = -1/2,
    Var(f_11) = Var(f_22) = 3/8,
    E[f_11 f_22] = Var(f_12) = 1/8.

All covariances involving one derivative and either f or two
derivatives vanish, as do E[f f_12], E[f_11 f_12] and E[f_22 f_12].
These are jointly Gaussian variables, so grad f is independent of
(f, Hess f). The density of grad f at zero is 1/pi.

Conditional on f=t, the Hessian therefore has the distribution

    [ -t/2 + X      Y       ]
    [    Y      -t/2 - X    ],                              (6)

where X,Y are independent N(0,1/8) variables. The deterministic trace
in (6) is consistent with the Helmholtz identity Delta f = -f; it must
not be replaced by an independent Gaussian trace.

Put Z=X^2+Y^2. Then Z has density 4 exp(-4z), z >= 0. For a=t^2/4,

    E|det Hess f| conditional on f=t
      = E|a-Z|
      = a - 1/4 + 2 E[(Z-a)_+]
      = a - 1/4 + (1/2) exp(-4a)
      = (t^2 - 1 + 2 exp(-t^2))/4.                         (7)

The third equality follows by directly integrating
integral_a^infinity (z-a) 4 exp(-4z) dz = exp(-4a)/4.

## 3. Counting interior critical values

The one-point Kac–Rice formula for the zero set of grad f, marked by
f in [a,b], reads

    E N_2 = A p_grad f(0)
              integral_a^b phi(t)
                E[|det Hess f| given f=t, grad f=0] dt.

Its hypotheses hold: f is smooth, grad f is nondegenerate, its
derivative has finite Gaussian moments, and conditional on grad f=0
the Hessian determinant is nonzero almost surely. The latter also
follows from (6) and the continuous distributions of f,X,Y. The
formula with a bounded height mark follows either in its marked form
or by approximating interval indicators. The resulting integrals are
finite. Degeneracy of the joint vector (f,Hess f) from the Helmholtz
identity does not invalidate Kac–Rice for grad f.

Substituting (7) gives

    E N_2 = A integral_a^b alpha(t) dt.                      (8)

As an additional check, the analogous density restricted to saddles
is phi(t) exp(-t^2)/(4*pi), since a saddle has Z>a and
E[(Z-a)_+] = exp(-t^2)/4. This observation is only an audit; (8)
counts all interior critical points.

## 4. Counting edge and corner values

Restrict f to a straight edge and use arclength s. Its derivative f_s
has variance 1/2 and density 1/sqrt(pi) at zero. It is independent of
(f,f_ss). Conditional on f=t,

    f_ss has distribution N(-t/2, 1/8).

Integration of the absolute value of this normal variable gives

    E[|f_ss| given f=t]
      = exp(-t^2)/(2 sqrt(pi)) + (t/2) erf(t).               (9)

For example, (9) follows by splitting the normal integral at zero;
it is even in t, and its derivative for t>0 is erf(t)/2.

The one-dimensional marked Kac–Rice formula for zeros of f_s, using
(9), gives

    E N_1 = P integral_a^b beta(t) dt.                      (10)

Each corner is standard normal, so linearity of expectation, with no
independence assumption between corners, gives

    E N_0 = 4 integral_a^b phi(t) dt.                       (11)

The endpoints have zero expected critical count because the densities
in (8)–(11) have no atoms. Thus all endpoint conventions agree almost
surely. Equations (5), (8), (10), (11) prove (1). In fact the law of
the superlevel crossing threshold is dominated by the finite measure
with density A alpha + P beta + 4 phi: apply (1) to disjoint intervals
and then to open sets. This also proves the claimed absolute continuity.

## 5. Integrals, constants and the square

The functions alpha and beta are even. To integrate alpha, use

    (t phi(t))' = (1-t^2) phi(t),
    integral_0^d phi(t) exp(-t^2) dt
       = erf(sqrt(3/2) d)/(2 sqrt(3)).

These identities give I in (3). For beta, integration by parts gives

    integral_0^d t phi(t) erf(t) dt
      = -phi(d) erf(d)
        + (2/sqrt(pi)) integral_0^d phi(t) exp(-t^2) dt.

Substitution yields J in (3), and integration of phi gives K. This
proves (2) and (3).

For (2a), if 0<=t<=1, the convex function
s -> s-1+2 exp(-s) on [0,1] is at most the larger of its two endpoint
values, namely 1. Thus alpha(t)<=phi(0)/(4*pi). If B(t) denotes the
conditional expectation in (9), then B(0)=1/(2 sqrt(pi)) and
B'(t)=erf(t)/2<=t/sqrt(pi). Consequently
B(t)<=(1+t^2)/(2 sqrt(pi)), giving
beta(t)<=phi(0)(1+t^2)/(2*pi). Finally phi(t)<=phi(0).
Integrating these three inequalities over [0,delta] proves (2a).

In particular, as d decreases to zero,

    I(d) = phi(0) d/(4*pi) + O(d^3),
    J(d) = phi(0) d/(2*pi) + O(d^3),
    K(d) = phi(0) d + O(d^3).                               (12)

The implied constants in (12) are fixed constants, independent of Q.
For a square, (2) and (12) become

    |p_[0,R]^2(u) - p_[0,R]^2(0)|
      <= phi(0) [R^2/(4*pi) + 2R/pi + 4] |u|
         + O((R^2+R+1)|u|^3).                              (13)

Here (13) means that the right side of (2) has the displayed
expansion; (2) is the exact nonnegative bound for every u.

At level zero, planar crossing duality says that exactly one of a
left-to-right crossing in {f>=0} and a top-to-bottom crossing in
{f<0} occurs. The regular level is transverse to all edges and avoids
corners almost surely by (8)–(11) at the singleton {0}. Thus changing
{f<0} to {f<=0} does not affect the crossing event: the level-strip
deformation moves a nonpositive crossing into a strictly negative
crossing at a sufficiently close negative level. Rotation invariance and f equal
in law to -f identify the two probabilities. Each is 1/2. This is also
the square duality statement used in Section 2.4 and Lemma C.1 of [1].
Now |u_R| R^2 -> 0 makes (13) tend to zero and proves (4).

## 6. Independent normalization checks

The derivative covariances in Section 2 can instead be recovered from
the uniform spectral angle theta: the second moments are
E cos^2(theta)=1/2, E cos^4(theta)=3/8 and
E[cos^2(theta) sin^2(theta)]=1/8. This checks the covariance
normalisation without the Taylor expansion.

Integrating alpha over the whole real line gives

    integral_R alpha(t) dt
      = (1/(4*pi)) E[T^2-1+2 exp(-T^2)]
      = 1/(2*pi*sqrt(3)),                                  (14)

where T is standard normal. The saddle density integrates to
1/(4*pi*sqrt(3)); the extrema account for the other half. Independently,
the unconditioned Hessian entries have variances 3/8,3/8,1/8 as above;
the total critical intensity in (14) agrees with Proposition 1.1 of [2].

For an edge, the unmarked zero density of f_s is

    (1/pi) sqrt(Var(f_ss)/Var(f_s)) = sqrt(3)/(2*pi).

The formula for J gives 2J(infinity)=sqrt(3)/(2*pi), checking (9)–(10)
without conditioning on the height. At height zero the three densities
are

    alpha(0) = 1/(4*pi*sqrt(2*pi)),
    beta(0)  = 1/(2*pi*sqrt(2*pi)),
    phi(0)   = 1/sqrt(2*pi).                                (15)

The factors A, P and 4 in (1) reflect different-dimensional strata;
neither edge length nor corner count is multiplied by area.

## Scope and references

The new statement here is the explicit crossing-stability bound
(1)–(4), derived from standard one-point Kac–Rice and level-set
deformation. No claim of priority over the literature is made. It
extends the previous report by allowing a specified vanishing level
change, but cannot remove sprinkling at an unspecified o(1) rate.
Obtaining a useful bound at substantially larger levels requires
controlling which critical points are pivotal for a macroscopic
crossing, not merely counting them.

[1] Stephen Muirhead, Alejandro Rivera and Hugo Vanneuville, with an
appendix by Laurin Köhler-Schindler, *The phase transition for planar
Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3).
Definition 2.7 and Appendix B supply an alternative stratified-Morse
formulation of the critical-value argument.

[2] Dmitry Beliaev, Valentina Cammarota and Igor Wigman, *Two point
function for critical points of a random plane wave*,
[arXiv:1704.04943](https://arxiv.org/abs/1704.04943).
