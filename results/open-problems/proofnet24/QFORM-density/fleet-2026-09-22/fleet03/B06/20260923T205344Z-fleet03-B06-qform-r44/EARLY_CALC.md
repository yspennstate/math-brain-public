SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T20:53:44Z.
attacking: the near-rank-one two-hub collar; separate the definite curved ellipse from the indefinite hyperbola, prove a weighted arcsine-maximal receiver for the definite side, and identify the exact anchored third-curvature matrix needed on the indefinite side.

# Early substantive calculation — r44

Let X,Y be independent original coordinates with densities at most one, let Z be an independent original-coordinate product bank, let

H = [[a,b],[b,d]],  A(Z)=alpha dot Z+a0,  B(Z)=beta dot Z+b0,

and retain an arbitrary measurable same-bank remainder R(Z). Consider

Q = a X^2+2bXY+dY^2+2A(Z)X+2B(Z)Y+R(Z).

## Definite hub: a curved arcsine average, not a fiber supremum

Assume det H>0. After a global sign change and possibly swapping X,Y, take a>0 and put

delta=d-b^2/a=det(H)/a>0,
C(Z)=B(Z)-(b/a)A(Z).

Exact completion gives

Q=a[X+(bY+A)/a]^2 + delta[Y+C/delta]^2 + S(Z),
S=R-A^2/a-C^2/delta.

Conditioning first on (Y,Z), the translated X keeps density cap one. Hence for a.e. t,

p_Q(t) <= a^(-1/2) E [t-S-delta(Y+C/delta)^2]_+^(-1/2).

For a probability density f<=1 define the centered arcsine maximal operator

Af(v)=sup_{r>0} integral_{|y-v|<r} f(y)/sqrt(r^2-(y-v)^2) dy.

For the centered Hardy-Littlewood maximal function Mf(v),

Af(v) <= 4 sqrt(Mf(v)).

Indeed, split (v-r,v+r) into halves. If m_- is the f-mass of the left half, then

integral_left f(y)/sqrt(r^2-(y-v)^2)dy
 <= r^(-1/2) integral_left f(y)/sqrt(y-(v-r))dy
 <= 2 r^(-1/2) sqrt(m_-),

by the bathtub bound for 0<=f<=1; the right half is identical. Since m_-+m_+ <= 2r Mf(v), Cauchy gives the claim.

Using the safe centered weak-(1,1) estimate |{Mf>s}|<=3/s,

|{Af>lambda}| <= 48/lambda^2.

Also Af<=pi because f<=1 and the full arcsine kernel has mass pi. Thus if V has density cap K,

E Af(V) <= integral_0^pi min(1,48K/lambda^2) dlambda <= 8 sqrt(3K).

Here V=-C/delta. If ||p_C||_infinity<=M, then ||p_V||_infinity<=delta M, so

||p_Q||_infinity <= 8 sqrt(3) a^(-1/2) sqrt(M).

For C=(beta-(b/a)alpha) dot Z+const, the source-valid one-dimensional product projection bound gives

M <= sqrt(2)/||beta-(b/a)alpha||_2.

Writing Gamma=a beta-b alpha,

||p_Q||_infinity <= 8*2^(1/4)*sqrt(3) ||Gamma||_2^(-1/2)
 =16.4781371513... ||Gamma||_2^(-1/2).

This is uniform as det H downarrow 0 from the DEFINITE side and retains arbitrary R(Z).

## Why the indefinite side cannot use the same arbitrary-remainder interface

For 0<epsilon<=1 let independent X,Y,C be Uniform[-1/2,1/2] and set

Q_epsilon=X^2-epsilon Y^2+2CY-C^2/epsilon
         =X^2-epsilon(Y-C/epsilon)^2.

The physical hub is diag(1,-epsilon), and the slope innovation is Gamma=1. For |c|<=epsilon/4, the shifted Y-variable contains [-1/4,1/4]. Hence for 0<t<3/16,

p_(Q_epsilon|C=c)(t)
 >= integral_{-1/4}^{1/4} du/sqrt(t+epsilon u^2)
 = (2/sqrt(epsilon)) asinh(sqrt(epsilon)/(4 sqrt(t))).

Averaging over c in [-epsilon/4,epsilon/4] yields

p_(Q_epsilon)(t)
 >= sqrt(epsilon) asinh(sqrt(epsilon)/(4 sqrt(t))) -> infinity.

Its matrix in (X,Y,C) is

[[1,0,0],[0,-epsilon,1],[0,1,-1/epsilon]],

with spectrum {1,-(epsilon+epsilon^(-1)),0}. Therefore this is NOT a QFORM counterexample; it proves that on an indefinite near-null hub, even robust slope innovation does not control an arbitrary completed remainder. The genuine target third curvature must be spent.

## Exact third-curvature object

For a full block matrix

M=[[H,E],[E^T,Cenv]],

define

K_H = det(H) Cenv - E^T adj(H) E.

For every environment indices j,k,

(K_H)_{jk}=det M[{hub1,hub2,j},{hub1,hub2,k}].

For invertible H this is the 2x2 Schur determinant identity, and the singular cases follow polynomially. Thus K_H is exactly the complete anchored third-minor bank, not an error term. At rank one H=lambda uu^T with unit null vector n,

adj(H)=lambda nn^T,
K_H=-lambda (n^T E)^T(n^T E),
||K_H||_F=|lambda| ||n^T E||_2^2,
||adj(H)E||_F=|lambda| ||n^T E||_2,

so

||K_H||_F = ||adj(H)E||_F^2/|lambda|.

This supplies the exact currency to carry into the remaining indefinite near-null branch.
