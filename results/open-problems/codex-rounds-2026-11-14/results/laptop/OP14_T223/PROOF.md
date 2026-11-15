# A one-dimensional invariant-cone case of T223

Let X be a standard normal real random variable, let sigma(z)=max(z,0), and put

    f_rho(x) = integral a sigma(wx) d rho(a,w),
    y(x) = c_+ sigma(x) + c_- sigma(-x),
    R(rho) = (1/2) E[(f_rho(X)-y(X))^2].

The coefficients c_+,c_- are arbitrary real numbers. This includes every
finite bias-free ReLU teacher in dimension one: group its neurons according
to the sign of w and use sigma(wx)=|w| sigma(sign(w)x).

All measures below are probability measures with finite second moment. Sector
integrals are integrals against the original probability measure, without
renormalizing the mass in a sector.

## Statement

Assume rho_0 gives full mass to

    C = {(a,w): |a|<|w|}

and positive mass to each sector C_s={sign(w)=s}, s in {+,-}. Define

    m_s^0 = integral_C_s a |w| d rho_0,
    q_s^0 = integral_C_s (a^2+w^2) d rho_0,
    D_s = sqrt((q_s^0)^2-4(m_s^0)^2),
    Q_s = max{q_s^0, sqrt(D_s^2+4c_s^2)},
    u_s^* = (asinh(2c_s/D_s)-asinh(2m_s^0/D_s))/2.

Then D_s>0. The self-consistent characteristic Wasserstein gradient dynamics
is globally well posed: there is exactly one law obtained by transporting
rho_0 along its own gradient field. It stays in C at every finite time and
is a curve of maximal slope for R in W2, with the energy dissipation identity
proved below. The kink convention is sigma'(0)=0; the law never charges
w=0, so that convention does not affect this solution.

There is an explicitly described probability measure rho_infinity such that

    R(rho_t) <= (1/4) sum_s (m_s^0-c_s)^2 exp(-D_s t),             (1)
    W2(rho_t,rho_infinity)^2
       <= sum_s Q_s (u_s^*)^2 exp(-D_s t).                        (2)

In particular, rho_infinity has finite second moment, realizes y, and
minimizes R globally with value zero. Uniqueness here is for self-consistent
characteristic dynamics; no claim about other definitions of nonsmooth
gradient flow outside the invariant cone is needed.

An explicit unbounded initialization is the law of independent standard
normal A,W conditioned on |A|<|W|. For this law,

    m_+^0=m_-^0=0, q_+^0=q_-^0=D_+=D_-=1.

Consequently,

    R(rho_t) <= (c_+^2+c_-^2) exp(-t)/4,                         (3)
    W2(rho_t,rho_infinity)
      <= (1/2) [sum_s sqrt(1+4c_s^2) asinh(2c_s)^2]^(1/2)
               exp(-t/2).                                      (4)

These are global-in-time bounds for this special case. Conditioning the
Gaussian is an essential restriction of the statement.

## 1. Risk and velocity, including normalization

Write b=|w| in a sector. Because the positive and negative input half-lines
are disjoint,

    f_rho(x)=m_+ sigma(x)+m_- sigma(-x),
    m_s=integral_C_s ab d rho.

Symmetry and E[X^2]=1 give E[X^2 1_{X>0}]=E[X^2 1_{X<0}]=1/2.
The cross term vanishes pointwise. Thus

    R(rho)=(e_+^2+e_-^2)/4,    e_s=m_s-c_s.                     (5)

The first variation at a neuron of sign s is V_rho(a,w)=e_s ab/2.
In coordinates (a,b) its negative Euclidean gradient is

    a'=-e_s b/2,    b'=-e_s a/2.                               (6)

In (a,w) coordinates the second component is w'=-s e_s a/2.
These equations have the Wasserstein continuity equation
partial_t rho + div(rho v_rho)=0 as their law-level form.

For a finite teacher there is also a probability measure realizing y:
use mass 1/2 at (2c_+,1) and mass 1/2 at (2c_-,-1).
Therefore the global infimum of R is zero, independently of the cone.

## 2. Characteristics and the invariant cone

For prescribed continuous e_s(t) on a finite interval, set

    u_s(t)=-(1/2) integral_0^t e_s(r) dr,
    H(u)=[[cosh(u),sinh(u)],[sinh(u),cosh(u)]].

The unique solution of (6) from (a_0,b_0) is

    (a_t,b_t)^T = H(u_s(t)) (a_0,b_0)^T.                        (7)

Indeed differentiating H gives (a',b')=u_s'(b,a). Conversely,
differentiating H(-u_s(t))(a_t,b_t)^T shows it is constant.
In light-cone coordinates,

    b_t+a_t=exp(u_s(t))(b_0+a_0),
    b_t-a_t=exp(-u_s(t))(b_0-a_0).                              (8)

Both right sides are positive. Thus b_t>|a_t|, b_t>0, and the sign of w
never changes. Also b_t^2-a_t^2=b_0^2-a_0^2>0. This argument needs no
uniform margin from the boundary of C.

For each nonempty initial sector,

    q_s^0+2m_s^0=integral_C_s (b_0+a_0)^2 d rho_0>0,
    q_s^0-2m_s^0=integral_C_s (b_0-a_0)^2 d rho_0>0.

The integrals are finite and strictly positive, so their product D_s^2
is strictly positive.

## 3. Scalar closure, existence, and uniqueness

Multiplying out (7) and integrating gives the functions

    M_s(u)=m_s^0 cosh(2u)+(q_s^0/2) sinh(2u),
    q_s(u)=q_s^0 cosh(2u)+2m_s^0 sinh(2u).                      (9)

They satisfy

    M_s'(u)=q_s(u),
    q_s(u)^2-4M_s(u)^2=D_s^2,
    q_s(u)>0.                                                 (10)

For the positivity assertion, use
q_s(u)=[(q_s^0+2m_s^0)exp(2u)+(q_s^0-2m_s^0)exp(-2u)]/2.
In particular q_s(u)>=D_s. More explicitly,

    M_s(u)=(D_s/2) sinh(2u+asinh(2m_s^0/D_s)).                 (11)

Thus M_s is strictly increasing onto the real line and M_s(u_s^*)=c_s.
Self-consistency is exactly the scalar initial value problem

    u_s'=(c_s-M_s(u_s))/2,    u_s(0)=0.                       (12)

Its right side is smooth. Between 0 and u_s^* it points toward u_s^*.
Uniqueness prevents crossing the equilibrium, so the solution is monotone
and stays in that closed bounded interval. A bounded solution of this
smooth scalar ODE extends for every t>=0: on that compact interval the
right side and its derivative are bounded, so the usual local existence
argument can be restarted with a uniform local time step. This proves
global existence and uniqueness for (12).

Push rho_0 forward by (7), retaining the original sign of w. Since
the operator norm of H(u) is exp(|u|), its second moment is bounded by

    sum_s exp(2|u_s^*|) q_s^0 < infinity.                     (13)

Equations (9) and (12) make the field self-consistent. On each bounded
time interval it has integrable squared speed and satisfies the continuity
equation, by differentiating compactly supported test functions under the
initial-law integral. Domination follows from its linear growth and (13).

For uniqueness in the stated characteristic class, m_s is continuous along
any W2-continuous law, without assuming sector preservation in advance.
Indeed, for any two parameter values,

    |a sigma(sw)-a' sigma(sw')|
       <= |a-a'| |w| + |a'| |w-w'|.

Integration under a coupling and Cauchy-Schwarz prove continuity when the
W2 distance tends to zero, since the second moments remain locally bounded.
Thus the coefficients e_s are continuous and their clocks are finite on
finite time intervals. For each individual initial neuron, apply (7)-(8)
up to its own putative first contact with w=0. Those formulas extend to the
contact time and give b>0 there, a contradiction. This argument does not
assume that the entire population has a common positive first contact time.
Consequently every characteristic keeps its original sector, (7) holds
globally, and self-consistency forces the unique solution of (12).

## 4. Risk decay by a separate moment derivation

Directly from (6),

    (ab)'=-(e_s/2)(a^2+b^2),
    (a^2+b^2)'=-2e_s ab.

Integration is justified by (13), first locally in time. Therefore

    m_s'=-(m_s-c_s)q_s/2,    q_s'=-2(m_s-c_s)m_s.             (14)

Differentiating q_s^2-4m_s^2 gives zero. This independently recovers
(10) along the solution, so q_s>=D_s. Since

    (e_s^2)'=-q_s e_s^2 <= -D_s e_s^2,

integration gives e_s(t)^2<=(m_s^0-c_s)^2 exp(-D_s t).
Combine this with (5) to obtain (1). The same equations give exactly

    -R'(rho_t)=sum_s e_s(t)^2 q_s(t)/4
              =integral |v_rho_t|^2 d rho_t.                 (15)

## 5. The constructed flow is a metric gradient flow

This verification is useful because merely solving an arbitrarily selected
ODE at a kink need not identify a Wasserstein gradient flow.

At a law rho supported in C define G_s(a,w)=a sigma(s w); thus
m_s=integral G_s d rho. Its gradient at w!=0 is (b,s a) in sector s
and zero in the other sector. Let theta=(a,w) belong to C and let
delta=(h,k) be any displacement. The elementary ReLU remainder obeys

    |sigma(s(w+k))-sigma(sw)-s 1_{sw>0}k|
       <= |k| 1_{|w|<=|k|}.

In expanding G_s(theta+delta), the remainder is the last expression
multiplied by a, plus h[sigma(s(w+k))-sigma(sw)]. Because |a|<|w|,
its absolute value is at most k^2+|hk|, and hence at most
(3/2)(h^2+k^2). This bound holds even for displacements crossing w=0.

For a coupling pi of rho and another finite-second-moment law eta, put
d_pi^2=integral |delta|^2 d pi. Integrating the remainder and applying
Cauchy-Schwarz to the linear term gives

    m_s(eta)-m_s(rho)=integral grad G_s(theta) dot delta d pi
                     + O(d_pi^2).

The linear term has absolute value at most sqrt(integral(a^2+w^2)d rho)
times d_pi. Expanding the quadratic expression (5), for d_pi<=1, yields

    R(eta)-R(rho)=integral grad V_rho(theta) dot delta d pi
                 + O(d_pi^2).                               (16)

The constants are finite and depend only on the current second moment and
residuals, not on eta or pi. Taking an optimal W2 coupling in (16) proves
that the descending local metric slope satisfies

    |partial R|(rho) <= ||grad V_rho||_{L2(rho)}.

For the reverse inequality, take eta=(Id-epsilon grad V_rho)_#rho.
Equation (16) gives an energy drop epsilon ||grad V_rho||^2+O(epsilon^2),
while W2(rho,eta)<=epsilon ||grad V_rho||. Let epsilon decrease to zero.
If this norm is zero the previous upper bound already gives equality.
Thus in all cases

    |partial R|(rho)^2=integral |v_rho|^2 d rho.               (17)

The characteristic coupling gives the metric speed bound
|rho_t'|<=||v_rho_t||_{L2(rho_t)} for almost every t. To see this directly,
couple theta_t and theta_{t+h} using the same initial neuron and apply
the integral triangle inequality to their velocity integral, then use
Lebesgue differentiation in t.

Conversely, the definition of local descending slope, applied to eta=rho_{t+h},
implies -R'(rho_t)<=|partial R|(rho_t)|rho_t'| at times where both
derivatives exist. Equations (15) and (17) give the reverse speed inequality
when the norm is nonzero. If it is zero the upper speed bound is enough.
Consequently, for every T>=0,

    R(rho_T)+(1/2) integral_0^T
       (|rho_t'|^2+|partial R|(rho_t)^2) dt = R(rho_0).         (18)

This is the metric energy dissipation identity, and proves the claimed
curve-of-maximal-slope property along this solution.

## 6. Convergence of the parameter law

Let delta_s(t)=u_s(t)-u_s^*. Using (12) and the mean value theorem,

    (delta_s^2)'=-delta_s [M_s(u_s)-M_s(u_s^*)]
                 <= -D_s delta_s^2.

Therefore

    |u_s(t)-u_s^*| <= |u_s^*| exp(-D_s t/2).                  (19)

Define rho_infinity by (7) with u_s^* in place of u_s(t). Bound (13)
also proves its finite second moment. It has m_s=M_s(u_s^*)=c_s.

Couple the two laws by using the same initial neuron. For any u between
0 and u_s^*, the vector-valued derivative of H(u)(a_0,b_0)^T is
(b(u),a(u)). Its squared L2 norm over the initial sector is q_s(u).
M_s(u) lies between m_s^0 and c_s, so (10) gives q_s(u)<=Q_s.
The integral triangle inequality in L2 now gives

    integral_C_s |H(u_s(t))theta_0-H(u_s^*)theta_0|^2 d rho_0
       <= Q_s |u_s(t)-u_s^*|^2.

Changing b back to w preserves Euclidean distances within a sector.
Summing this coupling cost and using (19) proves (2). This proves W2
convergence directly, with no inference from risk convergence alone.

## 7. Conditioned Gaussian constants

For independent standard normal A,W, polar coordinates give (A,W)=
(r sin(theta),r cos(theta)), with theta uniform modulo 2pi and independent
of r. The event |A|<|W| has probability 1/2 and depends only on theta.
The radial expectation E[r^2]=E[A^2+W^2]=2 is unchanged by conditioning.
The two signs of W have equal conditional probability 1/2 and the same
radial distribution. Hence q_s^0=2 times (1/2)=1.
Reflection A -> -A preserves the event and each sector and reverses
A|W|, so m_s^0=0. This proves all the stated constants, and substituting
them into (1)-(2) proves (3)-(4).

## Limits of the result

The initialization is an unbounded cone-conditioned Gaussian, not a full
Gaussian. For a full independent Gaussian, positive mass has |a|>|w|;
such neurons can reach w=0 and invalidate sector preservation and the
closed moments (14). In higher input dimensions the half-line decoupling
also fails. The general T223 statement, and uniqueness claims for arbitrary
nonsmooth metric-flow conventions outside this cone, are not proved here.
No novelty claim relative to all one-dimensional literature is made.
