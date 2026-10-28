# Explicit GU transfer and its remaining singleton leak

Candidate frozen before GU computation: for EVERY t>=2, vertex v and
independent finite Boolean controller a, with the actual F of PROOF.md,

 G(F)<=delta G(a)+6delta I(a)+256 I_DATA(F), delta=8^-t.    (G1)

Prior stages supplied complete H/CE histories, not this GU assertion.
The current private GU order was retrieved AFTER those earlier stage10
computations; their relevance gate was missed. This file supplies a new
explicit GU candidate, derivation and separately frozen actual-GU checks.
The older handoff is auxiliary, not mislabelled as a GU theorem.

All U,G here are the private focus contract's upper-set quantities, in bits:
pi(S)=sum_(T containing S) fhat(T)^2,
U=sum p(S)log2(pi(S)/p(S)), G=sum_i[U(f)-average U(f|i)].
No different spectral entropy is substituted for U.

## 1. Exact decomposition: the rare controller U survives once

Write k=3t, s=Ea, h_S=bhat(S), c_S=b(v)chi_S(v),
A_S(s)=h_S+delta c_S(s-1), p_S=A_S^2, and
z_S=sum_(R containing S)[p_R+delta^2(1-s^2)].
Then define E_b(s)=sum_S p_S log2(z_S/p_S), omitting zero p.
Every nonempty controller Fourier row is EXACTLY delta^2 P_a(T)
at each DATA label. Its upward probability is
delta^2*2^(k-|S|)*pi_a(T). Summing over DATA labels yields

 U(F)=delta U(a)+Q_b(s),
 Q_b(s)=E_b(s)-delta phi(s^2)+(delta k/2)(1-s^2),           (G2)
 phi(x)=-x log2 x.

This keeps the mean/vacuum atom, the signed phase of A_S, and the full
upper-set tail. In particular Q_b>=-delta, since E>=0 and phi<=1.
For a CONTROL coordinate j with d_j=ahat({j}), child means are s+d_j
and s-d_j. Thus its EXACT increment is delta Delta_j U(a) plus
Q_b(s)-average Q_b(s+/-d_j). At a DATA coordinate the delta U(a)
term cancels between the parent and its unique active child of density
2delta. No controller U is supplied twice.

## 2. Root curvature with the vacuum singularity kept separately

For b=g tensor t, min|h_S|=4^-t and delta/min|h_S|=2^-t.
Thus |A_S/h_S-1|<=2^(1-t)<=1/2, p_S>=h_S^2/4.
The COMPLETE DATA marginal p_S+delta^2(1-s^2) is affine in s.
Therefore every z_S is affine, z_S''=0. With c=1/ln2<3/2,

 E_b''=sum_S 2delta^2 log2(z_S/p_S)-2c delta
       -c sum_S [p'_S/sqrt(p_S)-sqrt(p_S) z'_S/z_S]^2.

For each DATA marginal m_S, |m'_S|/m_S<=10delta/|h_S|<=10/2^t;
the same ratio bound holds for its upward sums z_S. Also
sum p'^2/p=4delta and sum p<=1. The square inequality gives

 E_b''>=-c(10delta+200*4^-t)>=-20, for ALL t>=2.          (G3)

The nonsingular R_b=E_b+(delta k/2)(1-s^2) has R_b''>=-21,
because k delta<=3/32. Its Jensen gap is at most(21/2)d_j^2.
Summing over ALL controller coordinates uses sum d_j^2<=Var(a)<=1,
not the number of controller bits.

Keep phi(s^2) separately. Its derivative is continuous at0 and has
absolute value at most(4/e+2)c<6. Therefore its positive gap is at most
6|d_j|. Boolean physical edges give |ahat({j})|<=Inf_j(a), hence

 G_CONTROL(F)<=delta G(a)+6delta I(a)+21/2.              (G4)

No bound on a separately clipped KL term or sum of entropy decrements
is used. The still-unamortized6delta I(a) is explicitly retained.

## 3. DATA increments: uniform root and first-child error bounds

For the root seed and each FIRST physical DATA child, write theta for
its point density (delta or2delta), c0 for its unedited restricted seed,
and Q_(c0,theta) for(G2). We prove

             |Q_(c0,theta)(s)-U(c0)|<=20.               (G5)

This elementary bound is independent of t and controller dimension.
Here are full estimates, including the child's possible zero spectrum.
Put tau=(5/16)^t. At root, theta*sum|chat|=tau. At a first child
the partial block is either the two-bit point defect (L1 spectrum2)
or a constant (L1 spectrum1), so theta*sum|chat|<2tau.
Every NONZERO seed amplitude is at least2*4^-t for a first child;
the same relative perturbation bound1/2 still holds.

For a nonzero seed label S put P=chat(S)^2 and Pi=its seed upward tail.
The local partial-block tail obeys Nsup/Pi<=4; every intact three-bit
block obeys Nsup/Pi<=16. Hence at a first child
theta^2 Nsup/Pi<=4^-t<=1/16. Upward contributions from zero seed
labels plus the controller rows give

 1/4<=z/Pi<=9/4+5/16<4,  1/4<=p/P<=9/4.

Thus both relevant log ratios have absolute value<=2. For positive seed
labels sum|p-P|<=8tau+8delta, and log2(Pi/P)<=4t. Expanding
p log(z/p)-P log(Pi/P) gives absolute total at most

       32t(tau+delta)+4<=45/4.

The last bound uses t tau<=25/128 and t delta<=1/32, both decreasing
for t>=2. Zero seed labels contribute nonnegative E and at most
N*phi(4theta^2)<=8theta log2(1/theta)<=48t delta<=3/2;
phi is increasing on the required interval. Finally theta phi(s^2)<=theta
and theta(k-1)/2<=3t delta. These estimates give(G5) with room to spare.
At root there are no zero seed labels and the analogous bound is smaller:
16t(tau+delta)+4 plus the same bounded mean terms. Nothing omits a
zero seed row, a physical child, or the perturbation's upward tail.

U tensorizes exactly because pi tensorizes. Thus G(b)=tG(g)<=9t:
G(g)<=3U(g)<=3H(g)<=9. In each DATA increment the only changed
child is the active child, so(G2),(G5) give

                  G_DATA(F)<=G(b)+30k<=99t.             (G6)

Actual boundary counting gives I_DATA(F)>=3t/4-6t delta>=21t/32.
Combine(G4),(G6): 99t+21/2<=256 I_DATA(F) for t>=2. This proves(G1)
analytically for ALL t and ALL controller dimensions, not by finite testing.

## 4. Original U implication; its leak is repaired below

If the controller obeys G(a)<=A I(a)+B U(a), A finite,0<=B<1,
then(G1),(G2), Q>=-delta and delta<=I_DATA give

 G(F)<=max(A+6,257) I(F)+B U(F).                          (G7)

This is a concrete GU transfer; B does not approach1 with t or bias.
It does NOT establish ONE universal A under arbitrary nesting: A+6
can grow by6 at every stage. Nor does it remove the independent-controller
or special near-tensor-seed hypotheses. The exact missing payment is the
aggregate of the mean-atom gaps from -delta phi(s^2) in(G2).

The next section closes precisely this A->A+6 leak by retaining the
nonempty upper-set potential. It does not pretend(G7) alone is stable.

## 5. Nonempty upper-set potential removes the recursive coefficient leak

For EVERY Boolean function define V(f)=U(f)-phi(fhat(empty)^2),
the sum of its NONEMPTY upper-set terms; V>=0 and V(constants)=0.
Write G_V=sum_i[V(f)-average V(f|i)]. This V is distinct from the
activation variance denoted V in older campaign entropy ledgers.

Removing the global empty label in(G2) yields the EXACT identity

 V(F)=delta V(a)+T_b(s),
 T_b(s)=sum_(S_DATA nonempty) p_S log2(z_S/p_S)
                  +(delta k/2)(1-s^2)>=0.                (V1)

The empty DATA term of E_b is exactly phi(mean(F)^2), since z_empty=1.
This cancels the ONLY problematic vacuum term; no singleton or entropy
supplier is regranted. The same proof as(G3), restricting the nonnegative
log terms and squared sums to S nonempty, gives T_b''>=-21. Consequently

 G_V,CONTROL(F)<=delta G_V(a)+21/2.                       (V2)

For each root/first-child pair in Section3, subtract its empty atom:
T-Q=theta phi(s^2)-phi(mean(F_child)^2), while
V(seed)=U(seed)-phi(mean(seed)^2). Since each phi<=1, (G5) implies
|T-V(seed)|<=24, including child zero spectra. Further,
|G_phi(f)|<=6I(f) for EVERY Boolean f: child means differ from the
parent mean by +/-fhat({i}); use the Lipschitz bound of Section2 and
|fhat({i})|<=Inf_i(f). Thus

 G_V(b)<=G_U(b)+6I(b)<=27t/2,
 G_V,DATA(F)<=27t/2+36k=243t/2.

Together with(V2) and I_DATA>=21t/32,

          G_V(F)<=delta G_V(a)+256 I_DATA(F).             (V3)

Indeed243t/2+21/2<=168t=256*(21t/32) for t>=2.
This is an ALL-t, ALL-controller analytic inequality, not a finite-table
extrapolation. Also(V1), the root error<=24 and V(b)<=H(b)<=3t give

 delta V(a)<=V(F)<=delta V(a)+24 I_DATA(F),               (V4)

since3t+24<=24*(21t/32) for t>=2. Both endpoints remain explicit.

Hence the EXACT stable conditional implication is

 [G_V(a)<=A I(a)+B V(a)]
   => G_V(F)<=max(A,256)I(F)+B V(F), 0<=B<1.             (V5)

The former max(A+6,257) becomes max(A,256): no depth growth. Fresh
iterated one-point surgeries starting from constants satisfy G_V<=256I
at EVERY finite depth. This is a scoped grammar, not every Boolean
function, and no closure under arbitrary restrictions is asserted.
Endpoint(V4) separately gives V<=24I on that grammar by direct induction;
the earlier H<=4I grammar theorem is stronger for H and is NOT rediscovered
or improved by these coarse constants. The new result is stable signed
upper-set drift with its vacuum endpoint, not a better class FEI constant.

## 6. Complete universal implication and the precise remaining hypothesis

Here is the sufficient alternative criterion, with all signs retained:

 for EVERY Boolean f, G_V(f)<=A I(f)+B V(f), A finite,0<=B<1.  (VC)

Let K=A/(1-B). Induct on physical dimension, constants having V=I=0.
For nonconstant f, averaging the signed increments over relevant
coordinates supplies i with Delta_i V<=(A+B V/I)Inf_i.
The induction bound on BOTH actual children and influence partition gives
V-KI<=B(V-KI)*Inf_i/I, hence V<=KI, since1-B*Inf_i/I>0.
No positivity assumption on individual Delta_i V is used.

The original reviewed Theorem G, including its empty term, states
H<=2(I-Var)+2U-phi(mean^2). Thus with U=V+phi(mean^2) and
phi(mean^2)<=log2(e)Var<2Var, one has H<=2I+2V. Therefore

                     (VC) => H<=[2+2A/(1-B)]I.          (V6)

This is the complete sufficient implication required by the current GU
focus, using originals NOTES Section5 and REFEREE Sections2.1,2.2,2.6.
Also G_U=G_V+G_phi<=G_V+6I, so(VC) implies original GU with(A+6,B)
directly. These are universal implications; (V5) alone does NOT establish
(VC) outside the explicitly fresh one-point grammar.

First unsupported universal line: preserve(V3)'s single original owner
when the next changed core has TWO adjacent controlled edits with dependent
controllers on the SAME control block. The signed nonempty rows interfere;
they are not disjoint copies of(V1). NEXT derive their exact upper-set
interference remainder and either pay it once from the retained data/vacuum
account at the same256 rate or give an actual Boolean obstruction. This
removes the one-point/disjoint-row hypothesis rather than extending depth
or optimizing constants. A021/A025 reconstruct; A028/A087/A094 review.
Universal GU/VC and FEI remain OPEN; external review and formal checking
are not claimed. The earlier numerical same-bank handoff remains auxiliary.

## 7. Exact adjacent-edit interface for the next unpaid bound

This is an identity, not a claimed adjacent GU inequality. Let w=v xor e_i,
epsilon=b(v)b(w), and use arbitrary DEPENDENT controllers a,c on the same
control cube, independently of DATA. At v replace b(v) by b(v)a(z), at w
replace b(w) by b(w)c(z). For any NONEMPTY controller frequency T,

 fhat(S,T)=delta b(v)chi_S(v)[ahat(T)+epsilon(-1)^(1[i in S]) chat(T)].

Write qplus(T)=(ahat(T)+epsilon chat(T))^2 and
qminus(T)=(ahat(T)-epsilon chat(T))^2, with upward tails Pi_q.
Then the ACTUAL complete upward probability is

 pi_F(S,T)=delta^2 2^(k-|S|) *
    [pi_a(T)+pi_c(T)-2epsilon 1[i in S] sum_(R superset T)ahat(R)chat(R)].

The cross term vanishes only when the upward DATA set still allows BOTH
values of frequency bit i. Dropping it for i in S is false in general.

There is an exact shared-selector description. Let h(y,z)=a(z) for y=0
and epsilon c(z) for y=1, an ACTUAL Boolean mux on the reused coordinate.
Its frequency-y rows are qplus/4 and qminus/4. Put
J_y(h)=P_h({y}) log2(pi_h({y})/P_h({y})), with zero convention.
The part of V(F) carried by NONEMPTY original controller T is exactly

 U_CONTROL!=empty(F)
   =delta*(k-1)/2 *[Var(a)+Var(c)] +2delta[V(h)-J_y(h)]
   =delta*(k-1)/2 *[Var(a)+Var(c)]
      +delta[V(a)+V(c)+2Delta_y V(h)-2J_y(h)].            (ADJ)

For each of the other k-1 DATA frequency bits the conditional law is fair,
giving(k-1)/2. The remaining two rows are the ACTUAL h spectrum, so(ADJ)
follows by summing log upper probabilities; it makes no independence
assumption between a and c. The singleton J_y and the signed physical
selector increment must both stay. It is this shared-selector remainder,
and its changes at other coordinates, that NEXT must price jointly with
the DATA rows. Replacing it with two fresh source owners would skip the
first unsupported line. The frozen adjacent check verifies both spectra
and upward tails, including exact destructive cancellation, not an
unproved sign for the remaining GU aggregate.
