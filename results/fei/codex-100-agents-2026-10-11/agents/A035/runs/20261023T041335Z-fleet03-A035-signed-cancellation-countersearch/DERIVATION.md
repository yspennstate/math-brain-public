# Closing a reference cycle across the asymmetric frontier

All entropy, cross entropy and KL units are bits. Physical children are uniform
restrictions of an actual Boolean function. Spectral laws always mean squared
NORMALIZED signed Walsh coefficients. B_i(p)=H(S_i|S_-i). Fair_j(p) denotes the
complete law fair_j(marg_j p), including reference-only labels.

## 1. Supplied source, with no new admission claim

For every integer L>=1, let f_L=2 product_{k=1}^3(1-1_{E_k=0})-1, where
E1={x,a,c}, E2=X2 union {a,b}, E3=X3 union {b,c}, and X2,X3 are disjoint
L-bit blocks. All named core coordinates are distinct. Write

 D=M(f_L)+B_x(f_L)+E_s B_b(f_L|x=s),
 W=17 I_{ {x} union X2 union X3 }(f_L).

A035-TRIANGLE-SECOND-PRESCRIBED-RESET v1 supplies the all-L input

 D+E_{s,t} CE(p_st,Fair_a(p_st)) < W-1/32.             (1)

The four x,b parents each have original reach 1/4. Neither M, the original
owner, the x/b debits nor any terminal liability is renewed or dropped.
The present theorem is conditional on this supplied source theorem. It does
not supply universal initial admission and does not derive FEI from normalization.

## 2. A generic identity that does not require parent symmetry

For a physical query i distinct from a retained marker j, let p_+,p_- be
the actual child spectra. The signed formula a_child(T)=a(T)+/-a(T+i) implies
their mean law equals marg_i p. Put

 J_i=H(marg_i p)-E_u H(p_u),
 J_i^(-j)=H(marg_{i,j}p)-E_u H(marg_j p_u).

Both are Jensen-Shannon divergences of actual child laws, hence nonnegative.
Their definition requires the ACTUAL mixture; arbitrary unrelated child laws
are not admissible. Directly expanding four entropies gives

 B_j(p)-E_u B_j(p_u)
    =-I_p(S_i;S_j|S_-(i,j))+J_i-J_i^(-j).             (2)

Since CE(p,Fair_j(p))=1+H(marg_j p)=1+H(p)-B_j(p),
the full bill increment for recalibrating the SAME marker is

 B_i(p)+E_u CE(p_u,Fair_j(p_u))-CE(p,Fair_j(p))
   =-I_p(S_i;S_j|S_-(i,j))-J_i^(-j) <=0.             (3)

This is a generic entropy identity and inequality. Booleanity supplies the
actual signed restrictions and the already-paid source, not MI nonnegativity.
For an arbitrary finite adaptive physical query tree which never queries j,
multiply (3) by the actual reach of each internal node and telescope. This
gives the full sum of reached B_i plus ALL terminal Fair_j cross entropies,
bounded by the supplied initial Fair_j cross entropy. All complementary
branches stay; different stopping depths are allowed. Query choices may depend
on earlier physical outcomes. This does NOT pay arbitrary intermediate cuts
whose prescribed references have a different marker.

## 3. The prescribed asymmetric fourth reset

In each x,b parent choose y in X2 and z in X3. Query y, prescribe Fair_c in
BOTH children as in A031's third reset, then query z in all EIGHT parents and
prescribe Fair_a in all SIXTEEN terminals. The new target is

 D+E_st B_y(p_st)+E_stu B_z(p_stu)
      +E_stuv CE(p_stuv,Fair_a(p_stuv)) < W-1/32.      (4)

All reaches are original: 1/4,1/8,1/16. Apply (3) twice with marker a in EACH
original x,b parent, then (1). This proves (4) for ALL L without assuming a/c
symmetry after y. The intermediate Fair_c accounts are retained explicitly:
their incoming-reference refunds and their reset conversion costs telescope
when the complete two-query bill is compared to (1). They are not assigned a
new fair-bit credit. The four earlier M/x/b debits and both new erasures remain.

More generally the same bank bounds any finite complete adaptive continuation
from each x,b parent avoiding physical a, provided every final reference is
Fair_a. The prescribed y/c/z/a cycle is one concrete such endpoint theorem.
This extension has no dependence on equal-width symmetry beyond source (1).

## 4. A genuinely positive LOCAL net charge

Fix an asymmetric y child p. Incoming Q=Fair_c(p). Query z and let Qbar=marg_z Q.
The actual available refund is

 rho=sum_T pbar(T) KL(p(S_z|T)||Q(S_z|T))
     =I_p(S_z;S_c|S_-(z,c)).

For fresh Qnew_u=Fair_a(p_u), define
 Delta=E_u[CE(p_u,Qnew_u)-CE(p_u,Qbar)].
The FULL fourth-reset increment, including the queried erasure, is

 N=Delta-rho=B_c(p)-J_z-E_u B_a(p_u).                 (5)

No sign is available merely by assuming B_c=B_a; that symmetry was lost at y.
At L=2 with x=1,b=0,y=1, the actual Boolean witness satisfies N>1/10 bit.
The certificate POSITIVE_WITNESS.json contains its signed parent coefficients,
normalized incoming complete reference and exact outward rational bounds for
N,Delta,rho. Two implementations (compressed signed inclusion-exclusion and
independent truth-table integer FWHT) certify this strict rational inequality.
Thus the proposed nodewise assertion Delta<=rho is FALSE at this frontier.
It is not a failure of (4): earlier same-owner release pays the positive local
charge. In particular the stage's counterexample separates a false local
payment rule from an obstruction to the full inherited-bank target.

At x=b=1 every actual descendant is constant, but Fair_a costs exactly ONE
bit in all four y,z outcomes. These full terminal costs are explicitly kept.
All ghost/reference-only labels remain normalized, even in dummy branches.

## 5. Review of A031's nonfair third reset

A031-NONFAIR-PRIVATE-QUERY-THIRD-RESET v1 correctly uses rho=I(S_y;S_a|rest),
not 1-B_y, for incoming Fair_a. Its net identity is
B_a-J_y-E B_c. In the original x,b parents the actual permutation
(a,X2)<->(c,X3) gives B_a=B_c, so (2) makes that net
-I(S_y;S_c|rest)-J_y^(-c)<=0. Symmetry is invoked before y only. Its kernel
formula 2v^2/(u^2+3v^2), u=1-2q+q^2/2,v=-q+q^2/2, gives 49/218 at L2;
at L1 it is 9/14, and at L>=2 u^2-v^2=(1-q)(1-3q+q^2)>0.
The all-L scoped inherited extension therefore HOLDS. Independent FWHT
reconstruction overlaps its full third bill at L1,2,3. This is a review of
the new extension, not a second independent reconstruction of its whole
inherited source chain. No repair was supplied to the reviewed version.

## 6. Admission and the first unsupported line

The generic cycle identity cannot replace Boolean source admission: take N=2^18
equal singleton amplitudes on private dummy-unqueried coordinates, with all
queried core coordinates dummy. Its spectral private energy is 1, all queried
B and oriented M are zero, and final Fair_a CE is log2 N+1=19>17.
Every mentioned restriction still has norm one, but nonempty convolution is
2/N>0. This normalized nonBoolean control fails the original bank.

Any untouched independent Boolean spectator g with finite-cost Q_g retains
M(g)+CE(p_g,Q_g) with coefficient one on BOTH sides. All references tensor
with Q_g and every terminal retains that same debt; the triangle pays none.

First unsupported universal line: pay a complete cut whose retained marker a
is itself physically queried, or whose final marker changes without closing
the reference cycle, from the SAME original unused ancestor reserve. Identity
(3) does not apply at i=j. Generic tree closure avoiding a and another finite
class census do not settle this step. Arbitrary signed Boolean source admission
and full FEI remain OPEN. No all-L positivity of the local fourth charge is
claimed from the finite positive examples.
