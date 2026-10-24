# Complete biased-AND sign classification

Let h be binary entropy, psi(x)=h(sin^2 x), extended to all real x (even and period pi/2). All angles below use principal branches. For 0<p,q<1 put

    theta=arcsin(sqrt(p)),
    alpha=atan(sqrt(p/(1-p)) (1-2q)),
    w=1-4p q(1-q)>0.

Then the exact sign identity is

    F(p,q)=J_X-M_X
          =w[psi(theta)-psi(alpha)-psi(theta-alpha)].             (A)

There is a unique s_* in (0,pi/4) satisfying

    2 psi(s_*/2)=psi(s_*),

and put p_*=sin^2(s_*). In particular 0<p_*<1/2. For s in (0,pi/2) define

    G_s(x)=psi(x)+psi(s-x)-psi(s),  0<=x<=s.

The complete scalar classification is:

1. For s>=pi/4, G_s(x)>0 for 0<x<s.
2. For 0<s<s_*, G_s(x)<0 for 0<x<s.
3. For s=s_*, G_s(x)<0 except at x=s/2, where G_s=0.
4. For s_*<s<pi/4 there is a unique a(s) in (0,s/2) such that G_s(a(s))=0. The only interior zeros are a(s),s-a(s). G_s is negative on (0,a) and (s-a,s), and positive on (a,s-a). The two roots are simple; a(s) is smooth on this interval.

## Proof of (A)

Let r=4q(1-q), t=pr. The squared Fourier masses are

    ((1-2pq)^2, 4p(1-p)q^2, p^2 r, p(1-p)r).

Given remaining spectral Y label=1 (mass t), the physical X child is X=1 deterministically, while its spectral X label has mass p. Given remaining label=0 (mass w), the physical X conditional mass and spectral X mass are respectively

    u=p(1-2q)^2/w,
    v=4p(1-p)q^2/w.

Thus J=h(p)-w h(u) and M=w h(v)+t h(p), so F=w[h(p)-h(u)-h(v)]. A unit physical amplitude vector is

    (sqrt(1-p), sqrt(p)(1-2q))/sqrt(w)=(cos alpha,sin alpha).

The orthogonal biased Fourier transform sends it to

    (cos(theta-alpha), -sin(theta-alpha)).

Consequently u=sin^2 alpha and v=sin^2(theta-alpha), proving (A). This proof does not use the universal B09 uncertainty theorem.

## Curvature lemma

On 0<x<pi/2, direct differentiation gives

    (ln 2) psi'=2 sin(2x) ln(cot x),
    (ln 2) psi''=4 cos(2x) ln(cot x)-4,
    (ln 2) psi'''=-8[sin(2x) ln(cot x)+cot(2x)],
    (ln 2) psi''''=16[1+csc^2(2x)-cos(2x) ln(cot x)].          (B)

Put y=cot(2x). Since sin(2x)>0, ln(cot x)=asinh(y) and cos(2x)=y/sqrt(1+y^2). Moreover asinh is odd and |asinh(y)|<=|y|, by integrating its derivative 1/sqrt(1+y^2)<=1. Hence

    0<=cos(2x)ln(cot x)<=y^2,
    1+csc^2(2x)=2+y^2,
    psi''''(x)>=32/ln 2>0.                                 (C)

In particular psi''' is strictly increasing on the whole interval. On (0,pi/4), psi'''<0, so psi'' is strictly decreasing, with limits +infinity at 0 and -4/ln 2 at pi/4. Let tau be its unique zero.

## Complete zero count for G

For 0<x<s/2, (C) yields

    G_s'''(x)=psi'''(x)-psi'''(s-x)<0.

Therefore G_s' is strictly concave on (0,s/2), extends continuously to the endpoints, and

    G_s'(0)=-psi'(s), G_s'(s/2)=0, G_s(0)=0.

If s>=pi/4, psi'(s)<=0. Strict concavity implies G_s'(x)>0 throughout the half-interval. Thus G_s>0 there and, by reflection x->s-x, on the entire interior.

If s<pi/4, G_s'(0)<0. A strictly concave derivative with this negative initial value and zero final value has either no interior zero (it is negative throughout), or exactly one interior zero c, with negative sign before c and positive sign after c. To justify the uniqueness: its superlevel set {G_s'>0} is an interval; if nonempty it reaches the right endpoint in its closure, since concavity with any positive value and the final zero keeps every point to its right positive. Strict concavity excludes an intervening zero plateau. Thus G_s initially decreases and can then increase only once on this half-interval. Since its initial value is zero, the sign and number of its interior roots are determined solely by

    K(s)=G_s(s/2)=2psi(s/2)-psi(s).

If K<0, G is strictly negative on the interior. If K=0, the midpoint is its only interior zero. If K>0, exactly one simple root occurs on (0,s/2), and reflection gives the other root. At the root G_s'>0 on this half-interval, giving simplicity and the implicit function theorem for a(s).

## Unique transition s_*

For 0<s<=tau, psi is strictly convex on [0,s] with psi(0)=0, hence K(s)<0. For tau<=s<pi/4,

    K''(s)=(1/2)psi''(s/2)-psi''(s)>0,

because psi''(s/2)>psi''(s) and psi''(s)<=0. At pi/4, the already proved s>=pi/4 case gives K(pi/4)>0. Continuity gives a zero between tau and pi/4; strict convexity and K(tau)<0 imply exactly one zero there (after a crossing its derivative is positive and increasing). This is s_*. These facts prove all four scalar cases. Also K'(s_*)>0 by the positive secant slope from tau to s_*. At s_* the midpoint is a strict local maximum of G: if G_s''(s/2)>=0, G_s'' would be positive throughout the half-interval and G_s would strictly decrease to a negative midpoint, a contradiction. Thus G_s''(s_*/2)<0.

## Exact full sign map in the original biases

The formulas below include all real interior biases, without any grid hypothesis. F>0 means tax-free J<=M fails. Equality and F<0 are distinguished explicitly.

**Always:** q=1/2 is a zero line. For p>1/2 there is also the exact zero q_0=1/(2p). These are disjoint in the open square.

**q<1/2:**

- If p>=1/2, F<0.
- If 0<p<p_*, F>0 throughout this q half-interval.
- If p=p_*, F>0 except at q_m=1/[2(1+sqrt(1-p))], where F=0.
- If p_*<p<1/2, take s=theta and a=a(s), and define

      q_L=(1-cot(theta)tan(s-a))/2,
      q_R=(1-cot(theta)tan(a))/2.

  Then 0<q_L<q_R<1/2. F<0 on (q_L,q_R), F=0 at q_L,q_R, and F>0 elsewhere in (0,1/2).

These statements follow from F=-w G_theta(alpha), with alpha decreasing from theta to 0 as q increases from 0 to 1/2.

**q>1/2, p<=1/2:** F<0 everywhere. Indeed, let b=-alpha in (0,theta), s=pi/2-theta>=pi/4. Entropy reflection psi(x)=psi(pi/2-x) gives

    psi(b)+psi(theta+b)-psi(theta)=G_s(b)>0,

where b<s (also when p=1/2, b<theta=s). Thus F<0.

**q>1/2, p>1/2:** Put s=pi/2-theta in (0,pi/4), and b=-alpha. As q runs from 1/2 to q_0, b increases from 0 to s and

    F=-w G_s(b).

Consequently:

- If 1-p<p_* (equivalently p>1-p_*), F>0 throughout (1/2,q_0).
- If p=1-p_*, F>0 there except at q_m=1/(2sqrt(p)), where F=0.
- If 1/2<p<1-p_*, take a=a(s), and define

      q_L=(1+cot(theta)tan(a))/2,
      q_R=(1+cot(theta)tan(s-a))/2.

  Then 1/2<q_L<q_R<q_0. F<0 on (q_L,q_R), zero at q_L,q_R, and positive in the two remaining intervals.

For every p>1/2 and q>q_0, F<0. To prove this final case set c=b-s>0. Since b<theta, c<theta-s<theta, and

    psi(b)+psi(theta+b)-psi(theta)
      =psi(s+c)+psi(c)-psi(s)
      =G_theta(c)>0.

In the second equality use theta+s=pi/2 and evenness/periodicity; in the third use reflection. Thus this region is also covered exactly.

## Number of distinct interior q zeros, for each fixed p

    0<p<p_*:                 1
    p=p_*:                   2
    p_*<p<1/2:               3
    p=1/2:                   1
    1/2<p<1-p_*:             4
    p=1-p_*:                 3
    1-p_*<p<1:               2

The extra two-root branches in each half are smooth away from their coalescence threshold. Uniqueness ensures there are no unlisted zero curves. At either threshold there is one midpoint tangency instead of two simple roots. Together with q=1/2 and the hyperbola q_0 these statements give a complete implicit analytic description of the zero set and exact strict-sign regions. No elementary closed form for a(s) is asserted or needed.

## Outer boundaries

The continuous extension has F(0,q)=F(1,q)=F(p,0)=0, F(p,1)=-h(4p(1-p)). These follow by direct substitution of the four masses. The stage-1 pointwise edge asymptotics remain valid. The present classification removes their prior nonuniform corner gap: every interior point, even one approaching a corner on an arbitrary path, is classified by the formulas above.

## Consequence for actual coordinate selection

For every pair 0<p,q<p_*, both physical singletons A={X} and A={Y} have J_A>M_A. For X use the q<1/2,p<p_* classification; for Y exchange the names and biases of the independent input bits. Thus an existential coordinate selector cannot make the tax-free biased inequality J_A<=M_A hold universally, even for this fixed two-input gate. This is an actual Boolean continuum family, and the conclusion concerns both relevant coordinates rather than a single prescribed bad split. It does not refute an endpoint-tax payment, corrected FEI+, or uniform-cube C018/C019.
