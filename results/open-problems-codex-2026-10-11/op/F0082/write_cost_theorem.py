from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write(r'''

## A. Classification of continuous universal uncrossing costs

**Definition.** A continuous function f:(0,infinity)->R has the universal weak uncrossing property if, for every four distinct planar points in general position whose red-blue segments [r1,b1] and [r2,b2] cross properly,

f(|r1-b2|)+f(|r2-b1|) <= f(|r1-b1|)+f(|r2-b2|).

The strict property replaces <= by <. These are statements about every crossing configuration, not merely configurations typical of a particular infinite matching.

**Theorem.** Such a continuous f has the weak property if and only if f(t)=At+B with A>=0. It has the strict property if and only if it has this form with A>0.

**Proof of necessity.** Fix arbitrary positive a,b,c,d. Put u=(1,0), v_theta=(cos(theta),sin(theta)), for 0<theta<pi, and set

r1=-a u, b1=b u, r2=-c v_theta, b2=d v_theta.

The two old segments intersect properly at the origin, which is in their interiors. The supporting lines are distinct; the four endpoints are distinct, and no three endpoints are collinear: a line containing the two endpoints on one supporting line cannot contain a nonzero endpoint on the other. This remains true even when some arm lengths coincide. Old lengths are a+b and c+d. Swapped lengths are

sqrt(a^2+d^2+2ad cos(theta)),
sqrt(c^2+b^2+2cb cos(theta)).

As theta decreases to zero, these approach a+d and c+b respectively. Applying the weak property for every positive theta and using continuity gives

f(a+d)+f(c+b) <= f(a+b)+f(c+d).                         (A1)

Apply exactly the same argument with b and d interchanged to obtain the reverse inequality. Hence

f(a+d)+f(c+b) = f(a+b)+f(c+d)                         (A2)

for all positive a,b,c,d.

Given x,y>0, take a=b=x/2 and c=d=y/2. Then (A2) yields

2 f((x+y)/2)=f(x)+f(y).                              (A3)

To prove that continuity and (A3) imply affinity without omitting the functional-equation step, fix any 0<x<y. Repeated midpoint subdivision proves, by induction on n, that

f((1-k/2^n)x+(k/2^n)y)=(1-k/2^n)f(x)+(k/2^n)f(y)

for integers 0<=k<=2^n. The base n=0 consists of the endpoints. At level n+1, even k reduce to the preceding level and odd k are the midpoint of their adjacent even neighbours; (A3) gives the formula. Every t in [0,1] is a limit of these dyadic fractions. Continuity therefore gives the formula for all t. Thus f is linear on every compact interval in (0,infinity).

Fix two distinct positive base points x0<y0 and define A=(f(y0)-f(x0))/(y0-x0), B=f(x0)-Ax0. For any z>0, choose a compact positive interval containing x0,y0,z. On that interval the preceding interpolation identity implies that all its secant slopes agree; using the two base points identifies the slope and intercept as A,B. Hence f(z)=Az+B for all positive z.

For a proper crossing, the strict Euclidean length improvement from ATTEMPT.md Section 1 says that the old total length exceeds the swapped total length. If A<0, the cost comparison is reversed, contradicting the weak property. Thus A>=0. For the strict property A=0 also fails since all comparisons are equal, leaving A>0.

**Sufficiency.** When f(t)=At+B, each two-edge comparison cancels the 2B term. The strict Euclidean improvement multiplied by A is weakly positive if A>=0 and strictly positive if A>0. This proves both converses and the theorem.

**Consequence for the missing tightness.** Every continuous radial cost that strictly improves all crossings is exactly linear in length up to a positive scale and an additive constant. Theorem 2 of the original Poisson Matching paper says that every invariant perfect two-colour planar matching has infinite mean edge length. Therefore its expected f-cost is infinite too. In particular the proposed route of combining this universal local uncrossing property with a uniformly bounded expected coercive f-cost cannot work for an almost-perfect family: if such a family existed, Markov's inequality would give uniform displacement tightness, ATTEMPT.md Section 3 would give a perfect limit, and the same expectation bound would force finite mean length, contradicting the source theorem. A detailed direct bound is recorded below after checking it.

This is a no-go theorem for an optimization strategy, not a nonexistence theorem for non-crossing Poisson matching. It does not classify position-dependent costs, objectives involving more than additive edge costs, crossing constraints imposed explicitly, discontinuous costs, or improvements restricted to selected configurations.
''')
