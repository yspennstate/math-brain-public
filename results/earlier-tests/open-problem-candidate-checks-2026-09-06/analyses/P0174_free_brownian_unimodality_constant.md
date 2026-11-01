# Independent analytic review of P0174

Observed candidate SHA-256:
0d2e7cb7c659334ccb366e2ab56b30181c1398f065ce12a1cd65e4ba02431a01. This records analytic
work, not a machine proof or a novelty certificate.

## Moment and normalization reconstruction

For centered X under Q in an interval of diameter D, a=E X^2 and b=E X^4.
An independent copy gives E(X-X')^2=2a and E(X-X')^4=2b+6a^2.
Since |X-X'|<=D, b+3a^2<=D^2 a. Also a<=D^2/4.

Put s=x-u, y=R^2>0 and Z=int(s^2+y)^(-2)dmu. With
dQ=Z^(-1)(s^2+y)^(-2)dmu, stationarity of F=int(s^2+y)^(-1)dmu
gives E_Q s=0. Direct differentiation yields
F''/(2Z)=3-4y E_Q[1/(s^2+y)]. Jensen and F''>=0 force y<=3a;
therefore a>0. Independently, E_Q(s^2+y)=F/Z and
E_Q(s^2+y)^2=1/Z, so 1/F=(b+2ay+y^2)/(a+y).
This verifies the often-dangerous direction of the change-of-measure identity.

## Second upper-bound derivation

Rather than reuse the candidate's polynomial factorization, set
T(y)=a+y+(b-a^2)/(a+y). Because b>=a^2, T is convex for y>=0.
For 0<=y<=3a its maximum occurs at an endpoint:
T(0)=b/a<=D^2-3a, and
T(3a)=(b+15a^2)/(4a)<=(D^2+12a)/4<=D^2.
Thus 1/F<=D^2 by a different algebraic route.

## Equality and topology attacks

The candidate's two nonpositive terms require y=3a and 4a=D^2 at
equality. Maximal variance forces Q to be equally weighted at both endpoints;
their identical reweighting denominators force the same for mu. Put c=D/2.
Direct rational subtraction gives
F(u+s)-1/(4c^2)=-s^4/[4c^2(s^4+4c^2s^2+16c^4)]<0 for s!=0.
The apparent degenerate stationary point is a strict maximum. It cannot
invalidate the t=D^2 endpoint via a flat local minimum.

If a positive level <=1/D^2 had three ordered preimages, a dip below the
level between the outer two would attain an interior local minimum; otherwise
the middle point is itself a local minimum. Both contradict the preceding
strict lower bound at minima. Source Lemma 3.1 applies through the stated
Biane homeomorphism and the positive-density level correspondence.
The homeomorphism need not preserve second derivatives: preserving local order
and strict local minima is sufficient. Atomic or singular initial mu causes
no differentiation issue because R>0. D=0 is the point-mass case; the density
argument is only used for t>0.

## Independent sharpness check

For symmetric Bernoulli on {-c,c}, at u=0 the implicit solution is
v=sqrt(t-c^2), for t>c^2. Symmetry gives v'=0. Differentiating its implicit
profile equation gives v''=(4c^2-t)/(t sqrt(t-c^2)). It is positive for
c^2<t<4c^2. The density consequently has a positive strict interior minimum
and is not unimodal. Since D=2c, constants below 1 fail by taking
max(C,1/4)D^2<t<D^2. Units are variance t and support diameter D throughout.

## Primary-source and literature limits

The ALEA PDF defines S(0,t) with variance t and D_mu as diameter. Printed
page 359 states the symmetric {-1,1} threshold as t=4 and D_mu=2, then
prints 2<=C<=4. The former numbers yield the lower bound 1, not 2. This
is a checked arithmetic inconsistency, not evidence for the new upper bound.

Primary URLs: https://alea.math.cnrs.fr/articles/v15/15-15.pdf and
https://arxiv.org/abs/1710.08240 . Searches on 2026-09-06 for Problem 3.3,
free Brownian unimodality with diameter/optimal/sharp/C=1, and Hasebe/Ueda
followups did not locate a later C=1 solution. Hasebe's publication page
https://www.math.sci.hokudai.ac.jp/~thasebe/index.html was read in full;
absence of an obvious followup title is weak negative evidence only. Ueda's
thesis was a search lead, not fully read. The literature search is incomplete.

No gap was found in the explicit analytic steps and edge cases above.
