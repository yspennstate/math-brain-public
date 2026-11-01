# A source-owned pivot reserve beyond one shared bit

All variables are independent uniform signs. Entropies are bits. Both Boolean
branches G(y), H(y) are embedded on the same full data cube, using dummy
coordinates as necessary. Their shared data can be arbitrary. A fresh selector
z gives F=(G+H)/2+z(G-H)/2. B_i is conditional spectral erasure, not a marginal.
Write Phi(p,q)=(p+q)h2(q/(p+q)).

## 1. Exact all-shared collision

For every residual Fourier set T not containing the queried data bit i, put
u=Ghat(T), a=Ghat(T+i), v=Hhat(T), b=Hhat(T+i). Then

B_i(F)=sum_T [Phi((u+v)^2,(a+b)^2)
                     +Phi((u-v)^2,(a-b)^2)]/4,
C_i=[B_i(G)+B_i(H)]/2, D_i=B_i(F)-C_i.                  (1)

This keeps every coherent row, including the empty row, and counts a shared
physical query once. Directly from the physical selector,

Inf_i(F)=[Inf_i(G)+Inf_i(H)]/2.                          (2)

Since each erasure is a binary conditional entropy, 0<=B_i(F)<=1 and
0<=C_i<=1, so |D_i|<=1. This is only useful if a named physical influence
reserve exists; A078's rare-private-query witness shows that it cannot be
silently converted into a constant times arbitrary queried influence.

## 2. Hereditary derivative-gap branch and its owned reserve

Assume every restriction h of H has the following property: each relevant
coordinate has Inf_i(h)>=eta>0. Use the policy:

* While the current H branch is nonconstant, query any coordinate relevant
  to that current H branch. The choice can be adaptive.
* Once the current H branch is constant, query any remaining data coordinates
  of G, stopping at any leaves. The selector stays unqueried.

A run may stop during either phase. At a first-phase node,

|D_i|<=1<=Inf_i(H)/eta; B_i(F)<=2 Inf_i(F)/eta.          (3)

At a second-phase node H=+1 or -1, the A076 stage3 shifted-row proof gives
|D_i|<=Inf_i(G), B_i(F)<=B_i(G)/2+Inf_i(G).              (4)

For any adaptive partial prefix T, let
P_H=sum_first w_v Inf_i(H_v), P_G0=sum_second w_v Inf_i(G_v).
Then the exact inherited and signed ledger and its payment are

B_T(F)=[B_T(G)+B_T(H)]/2+sum_v w_v D_i,
sum_v w_v |D_i| <= P_H/eta+P_G0.                       (5)

Here B_T(G), B_T(H) mean the same physical data tree applied to both branches;
dummy queries are included at zero cost. Influence conservation gives

P_H=I(H)-E I(H_leaf),
P_G0<=I(G)-E I(G_leaf).                                (6)

The first equality holds because no H influence is consumed in the second
phase; this is an exclusive labelled H reserve. More precisely
P_G0=I(G)-E I(G_leaf)-P_G1, where P_G1 is G influence already consumed in
the first phase. Thus neither first-phase G influence nor terminal G influence
is charged again. In particular the correction is <=(2/eta) Pi_I(F) when
eta<=1, but (5) is the stronger source-specific accounting.

## 3. Quadratic and bounded algebraic degree branches

For H=(-1)^P, with P a multilinear polynomial over F2 of degree at most d>=1,
the sign product H(y)H(y flipped at i) is (-1)^(partial_i P), where partial_i
is the F2 derivative. The pivotal probability is Pr[partial_i P=1]. A nonzero
polynomial Q of degree <=r has weight at least
2^-r. Proof by induction on r: a nonzero constant is identically one. For
nonconstant Q, choose a relevant variable j; partial_j Q is nonzero of degree
at most r-1. On every assignment where that derivative is one exactly one
of the two values of Q is one, so Pr[Q=1]>=Pr[partial_j Q=1]/2>=2^-r.
Restrictions do not increase degree. Consequently eta=2^(1-d) is valid.

In particular every quadratic branch, including arbitrary cross terms and
linear terms, has eta=1/2. Its full first-phase correction costs at most
2 I(H), and each first-phase node has B_i(F)<=4 Inf_i(F). No Fourier l1
assumption on the shared mean profile is used. This includes the two-bit
nonlinear slice left open by A077/A058, and the arbitrarily multishared
quadratic branch in A078's actual adverse fixture.

## 4. Terminal functions are retained exactly

At every leaf, write g_S,h_S for the two full-cube branch coefficients.
Their exact selector potential is

R(G,H)=sum_S [phi((g_S+h_S)^2/4)+phi((g_S-h_S)^2/4)
                            -phi(g_S^2)/2-phi(h_S^2)/2].

Thus
H(F)=[H(G)+H(H)]/2+R(G,H),
E H(F_leaf)=E[H(G_leaf)+H(H_leaf)]/2+E R(G_leaf,H_leaf). (7)

This is an exact accounting identity, not a free leaf certificate. If z is
queried at a leaf, its decrement is R and its remaining entropy is the
half-sum of branch entropies. Keeping z unqueried at intermediate stops
retains the full actual terminal function. Equations (5)-(7) pay only the
collision correction; neither inherited erasure nor terminal core entropy
has been erased from the universal obligation.

## 5. Mandatory A078 adverse fixture: an actually paid complete policy

Let G=1-2*1{s=0,x=0} and H=(-1)^(s1*s2+...+s(k-1)*sk), k even.
A078 already proves that the rare x query has D_x/Inf_x>=k-4, while a paid
selector exists and H(F)<4I(F). Those facts are credited, not rediscovered.
Apply the policy in section 2, skipping any quadratic partner made irrelevant
by a zero answer. Every first-phase data query has B<=4 Inf.

Once H is constant, G is constant or a point defect on the remaining data
bits (dummy variables can be ignored). For an r-bit point defect let
delta=2^(1-r)=Inf_i(G). For r=1 its queried erasure is zero. For r>=2 its
erasure is exactly

Phi((1-delta)^2,delta^2)+2delta(1-delta).

Its ratio to delta is at most
2(1-delta)+delta[2(r-1)+log2(e)]<=3.                    (8)

For r=2, use log2(e)<2 to get the last bound directly; for r=3 also use
log2(e)<2; for r>=4, with l=r-1, 2l/2^l<=3/4 and
(log2(e)-2)/2^l<0, giving a value below 3. The preceding envelope follows
from Phi(p,q)<=q log2(e(p+q)/q), p+q<=1. Constant cases are zero.
Combining (4) and (8) gives B_i(F)<=5 Inf_i(F) at second-phase nodes.
After all data are revealed F is constant or a character in z and has
entropy zero; a final z query has B=JS=0. Therefore the complete physical
policy, hereditarily at all its reached nodes, has

B_T(F)<=5 I(F), Q_T(F)<=5 I(F).                         (9)

The general JS bound JS_i<=2 Inf_i/ln2, obtained from the scalar
[(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2), supplies the optional entropy
consequence H(F)<8 I(F). This is weaker than A078's existing H<4I, and is
not advertised as a class-bound improvement: the new result is the paid
data-only adaptive policy and its exclusive collision reserve.

## 6. Honest universal frontier

The derivative-gap hypothesis has eta exponentially small in algebraic degree;
arbitrary Boolean H has no dimension-independent eta. Thus (3) cannot serve
as a universal C018 pivot theorem. Arbitrary inherited erasure and terminal
entropy in (5),(7) are still unpaid. This stage consumes A078's obstruction
by giving a complete policy and a reusable ownership lemma beyond bounded
shared Fourier l1, rather than claiming that the bad rare query became cheap.
The next shortest target is an adaptive branch-switch policy when BOTH
branches lack a derivative gap: can the first rare/rare collision be paid by
one signed terminal slack instead of spending eta^-1? This is the first
unsupported line separating the present reserve from a universal C019 rule.
