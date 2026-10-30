# Tail-certified extremality and a SAME-K escape obstruction

All spectra are normalized real Walsh spectra on a uniform finite cube,
embedded in the countable product cube when a limit is discussed. Entropy
is in bits. Write D_K=H-KI, K>=0. No infinite-dimensional optimizer is
assumed, and no counterexample to universal FEI is claimed.

## 1. Explicit finite Boolean approximation

Let f be a Boolean sign on the countable uniform product (a finite cube
is included), with finite Fourier entropy and influence. For m>=1 put

 delta_m=sum_{S not subset [m]} fhat(S)^2,
 T_H(m)=sum_{S not subset [m]} -fhat(S)^2 log2(fhat(S)^2),
 T_I(m)=sum_{S not subset [m]} |S| fhat(S)^2.

Let z=E[f|X_1,...,X_m] and let g=sign(z), assigning sign(0)=+1.
This is an actual m-bit Boolean table, not a fractional conditional mean.
With e=P(f!=g), conditional on the first m coordinates its error is
(1-|z|)/2 <= (1-z^2)/2. Parseval therefore gives e<=delta_m/2.
For each j<=m, disagreement of the two edge indicators requires an error
at one endpoint, so |Inf_j(f)-Inf_j(g)|<=2e. Consequently

 |I(f)-I(g)| <= m delta_m + T_I(m).                         (1)

For completeness, the omitted-coordinate influence is at most T_I;
the latter also charges internal coordinates of every escaping label.
The Fourier coefficient vectors have l2 distance 2 sqrt(e). Cauchy--
Schwarz applied to (ahat-bhat)(ahat+bhat) shows the total variation
distance between their squared spectra is <=2 sqrt(e)<=sqrt(2delta_m).
Collapse every label not contained in [m] into one extra atom. The new
alphabet has 2^m+1 atoms. Its entropy differs from H(f) by

 T_H(m)+delta_m log2(delta_m),

which lies in [0,T_H(m)]. The spectrum of g has zero mass at the extra
atom. If delta_m<=1/8, set eta=sqrt(2delta_m)<=1/2. The finite-alphabet
continuity inequality (proved by coupling the mismatch indicator and
bounding the conditional choice by 2^m possibilities) yields

 |H(f)-H(g)| <= T_H(m)+h2(eta)+m eta.                     (2)

Here 0 log 0=0. The coupling proof gives h2(v)+v log2(M-1) at actual
variation v; it is increasing for v<=1/2 and M>=2, licensing eta.
There is no continuity assertion on an unbounded alphabet without T_H.
Combining (1),(2),

 |D_K(f)-D_K(g)| <= E_m(K)
 :=T_H(m)+h2(eta)+m eta+K[T_I(m)+m delta_m].              (3)

Compress g to essential variables and minimize I over its finite affine
spectral orbit, as in A051's finite minimum-basis theorem. The resulting
Boolean g* has dimension <=m, the same H, and D_K(g*)>=D_K(g).
Thus D_K(f)>E_m(K) certifies a FINITE actual K-counterexample. In
particular, if T_H,T_I->0 and m sqrt(delta_m)->0, every positive deficit
of such an infinite Boolean limit has a finite witness. This is an
explicit, sufficient approximation hypothesis, not a consequence of
bounded influence or ordinary L2 convergence. For a finite table the
choice m=n has zero error, recovering the finite selector without an
optimizer over unbounded dimensions.

For near-extremality, the inequality D_K(g*)>=D_K(f)-E_m(K) is the
admissible transfer rule. Any claimed epsilon budget must include E_m;
dimension-dependent stationarity costs from prior stages still apply.

## 2. An actual Boolean escape family retaining an arbitrary seed ratio

Fix a nonconstant d-bit Boolean g whose spectrum has full affine span
and which minimizes I in its full invertible affine spectral orbit.
Write H0=H(g), I0=I(g)>0, mu=Eg with |mu|<1. These are finite objects.
For k>=2 set p=2^-k, t=2^k, let h_k be the product of t disjoint copies
of g, and let A_k be the event that the FIRST k control bits are zero.
Use the subsequent dt coordinates for h_k and define

 F_k=1-A_k+A_k h_k.                                      (4)

Then H(h_k)=t H0, I(h_k)=t I0, nu=E h_k=mu^t, and

 I(F_k)=I0+kp(1-nu),                                     (5)
 ||F_k-1||_2^2=2p(1-nu)<=4p.                            (6)

For reference let q(x)=-x^2 log2(x^2), q(0)=0. Direct summation of the
actual Fourier coefficients gives the complete scalar profile

 H(F_k)=p t H0+q(1-p(1-nu))-p q(nu)
       +p(1-p)q(1-nu)
       +2kp[(1-nu^2)+(1-p)(1-nu)^2].                    (7)

At each nonzero data label s every control label has coefficient
p hhat_k(s). At data label zero, the nonempty control coefficients
are -p(1-nu), and the empty coefficient is 1-p(1-nu).
These signed coefficients prove (7); nothing is discarded at zero.
The estimates 0<=q(x)<=1 for |x|<=1, |q(x)|<=8 for |x|<=2,
and q(1-pb)<=2pb/ln2<=6p for 0<=b<=2, p<=1/4, imply

 |H(F_k)-H0| <= p(10k+15).                               (8)

For the first estimate, -u ln u<=1/e and ln2>2/3 suffice. In the
second, the range 1<=|x|<=2 has |q(x)|<=8. For the third use
-ln x<=(1-x)/x and b=1-nu. The bracket in (7) is at most5.
Equations (5),(8) imply I(F_k)->I0, H(F_k)->H0 and
D_K(F_k)->D_K(g) for EVERY fixed K>=0. In particular H/I tends
to the SAME seed ratio, and any fixed positive seed deficit survives
eventually. More explicitly,

 |D_K(F_k)-D_K(g)| <= 2^-k[(10+2K)k+15].                 (9)

For a certified positive seed gap, any k>=2 making the rational right
side smaller than that gap is a finite, executable witness parameter;
no passage from a formal limit to an unidentified Boolean family is
needed. This last implication is conditional on an actual violating
seed; it does not manufacture one at an unknown universal K.

## 3. The escape survives the affine-minimal/full-span reduction

For a spectral parity v let w(v)=P(v dot S=1) and m(v)=min(w,1-w).
A051's criterion for affine minimality is p_j<=1/2 and
m(v)>=max_{j:v_j=1}p_j. For disjoint tensor factors,

 |1-2w_h(v)|=product_l |1-2w_g(v_l)|,

so m_h(v)>=m_g(v_l) for each nonzero component. Tensor products
therefore preserve the criterion and full affine span.
An activated parity supported only on data has cost p w_h(v). Any
parity with a nonzero control part has cost p(1-nu). Every such cost
is <=2p<=1/2; no hidden majority centering is needed. A data-only cost
dominates all used data marginals by the tensor criterion. For a mixed
parity use the elementary Boolean bound w_h(e_j)<=1-|nu|<=1-nu.
Thus every F_k is affine-influence minimal. Since nonconstant full-span
h_k has a nonzero data coefficient, its replicated control labels span
all controls, while data differences span the full data space. F_k has
full affine spectral span k+dt.

Equation (6) gives convergence to the constant1 in L2 and almost surely:
outside the null event that every control bit is zero, eventually A_k=0.
Yet H(F_k)->H0>0 and I(F_k)->I0>0. Moreover sup I(F_k)<=I0+1.
For ANY finite collection of spectral labels, when k exceeds their
largest coordinate, each nonempty label is control-only and has mass
p^2(1-nu)^2<=4p^2; the empty mass tends1. The entropy and influence
contributed by that finite collection tend0. Hence for every fixed m,

 T_H^{F_k}(m)->H0, T_I^{F_k}(m)->I0, delta_m^{F_k}->0.

This is a concrete failure of uniform spectral entropy AND influence
tail control inside the reduced class. L2 compactness plus bounded I,
even with full affine span/minimality, cannot justify entropy continuity
or existence of an entropy-influence optimizer. For a named unconditional
fixture take the two-bit bent sign (-1)^(xy), H0=2,I0=1,mu=1/2.
Its canonical activated family tends to constant1 while H tends2,I to1.
At k=10,t=1024 this is an explicitly specified 2058-bit Boolean table
(defined by its formula, not enumerated), and (6),(9) certify
||F_10-1||_2^2<=1/256 and D_1(F_10)>=889/1024>0. This is a
finite rational guard against deficit continuity at constant1, not a
counterexample to an unspecified absolute FEI constant.
It also tests the necessity of the explicit tail terms INSIDE the small-
delta regime. For m=1, the conditional activation probability is at most
2p, so the conditional mean is at least1-4p>0 and g_round is constant1.
Here delta_1<=Var(F_10)<=4p=1/256, eta<=1/8, and (8) gives
H(F_10)>=1933/1024>9/8. If T_H were omitted from (2), its right side
would be at most h2(eta)+eta<=1+1/8=9/8, a contradiction. If T_I
were omitted from (1), it would assert I(F_10)<=delta_1<=1/256,
whereas (5) gives I(F_10)>=1. Both missing-tail negative arms are
therefore exact finite Boolean counterexamples to those stronger
approximation claims, with no truth-table enumeration or float sign.
No brute-force construction at growing dimension is required for this
all-k proof.

## 4. Relation to the critical bank; first unsupported line

The family (4) can carry an arbitrary canonical seed ratio and loses
the signed terminal eligibility required in A051/A052's critical bank.
It is not asserted to be a genuine least-dimensional K-witness.
The finite maximal-deficit/minimal-dimension selector remains valid and
needs no compactness. One cannot replace it by an unqualified infinite
optimizer or infer the tail hypotheses of Section1 from bounded I.

FIRST UNSUPPORTED UNIVERSAL LINE: force adequate independent cheap-
parity rank, or an equivalent paid selection, at an ORIGINAL proper
pair of a genuine finite critical witness using the SAME unused child
reserve, mixed interaction refund and every complete terminal. Neither
the escape guard nor the sufficient finite approximation bound pays
that pair. Universal FEI remains OPEN.
