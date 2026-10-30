# Exposing the retained marker from the same original bank

All statements use uniform normalized Walsh coefficients and entropy in bits.
B_i(p)=H(S_i|S_-i); M is the original oriented erasure sum, not marginal entropy.
Every reference below is a complete normalized law, including reference-only cells.

## 1. Source, exact scope and consumed peer result

For each integer L>=1 use the actual Boolean triangle
f_L=2 product_k(1-1_(input_Ek=0))-1,
E1={x,a,c}, E2=X2 union{a,b}, E3=X3 union{b,c}, with disjoint L-bit blocks.
Set q=2^-L, W=17 I_private(f_L), private={x} union X2 union X3, and

 D=M(f_L)+B_x(f_L)+E_s B_b(f_L|x=s).

The four actual x,b parents p_st have original reach1/4 and supplied references
Fair_a(p_st)=fair_a(marg_a p_st). A035-TRIANGLE-SECOND-PRESCRIBED-RESET v1
supplies D+E_st CE(p_st,Fair_a(p_st))<W-1/32.

A035-CLOSED-REFERENCE-CYCLE-ASYMMETRIC-RESET v1 has ALREADY closed the saved
next asymmetric y/c/z/a cycle. Its proof is consumed unchanged: for any physical
query i distinct from retained marker j,

 B_i(p)+E_u CE(p_u,Fair_j(p_u))-CE(p,Fair_j(p))
   =-I_p(S_i;S_j|others)-J_i^(-j)<=0.                 (1)

Here p_u are the ACTUAL signed restriction laws and
J_i^(-j)=H(marg_(i,j) p)-E H(marg_j p_u)>=0.
This is a generic entropy identity, not Boolean admission. Telescoping (1)
pays all erasure debits and ALL final Fair_a liabilities in any finite complete
adaptive tree avoiding a. A035's local positive fourth charge (>1/10 at L2)
is compatible with endpoint payment. This stage reviews that scope and targets
the marker exposure which (1) does not cover.

## 2. Strengthen the SAME original source, not a child bank

Write C2=D+E_st CE(p_st,Fair_a(p_st)). We prove

                         C2 < W-7/8                 (2)

for ALL L>=1. L1..19 are exact finite certificates; L>=20 follows below.
This strengthens the original source slack while keeping its complete left side.

Let h be the three-variable point defect on {x,a,c}, with other inputs dummy.
Its signed amplitudes are3/4 at empty and-1/4 at each other core label. From the
actual clause formula, Pr(f_L!=h)<=q/2. Under ANY fixed physical history of
at most two coordinates, the conditional disagreement is at most2q. Thus
the signed amplitude difference is at most4q, and the total squared Fourier
mass outside the limiting support of size at most8 is at most8q, by Parseval
applied to the actual difference. This is a comparison between Boolean signs,
not replacement by a nonBoolean approximation.

For any of these root/cofactor laws and ANY spectral marginal used below,
each nonzero limiting mass is at least1/16. At L>=20 a corresponding actual
mass is at least1/64: one limiting amplitude of magnitude>=1/4 retains magnitude
>=1/4-4q>1/8. On [1/64,1], the derivative of -t log2(t) has absolute value<8.

Before marginalization, each of the at most8 core masses changes by at most8q,
since |alpha_f-alpha_h|<=4q and each amplitude has magnitude<=1. Marginalization
can fold at most8q of off-core mass onto the limiting support. Hence the sum
of absolute changes on that support is at most64q+8q=72q. Its entropy changes
by at most576q. The remaining mass t<=8q lies on at most2^(2L+4) labels, so its
entropy is at most t log2(2^(2L+4)/t) <=(24L+8)q. The scalar expression is
increasing on this interval, including t=0 by continuity. Therefore each
needed entropy satisfies

     |H(actual marginal)-H(limiting marginal)|
                   <= E(L)=(24L+584)q.               (3)

For the original oriented M, reuse the checked root perturbation estimate in
A031's stage17 DERIVATION section4 (with the same actual root and same h):

     M(f_L)<=M(h)+(2L^2+4L+350)q, L>=16.             (4)

Its proof bounds the three core row derivatives, keeps off-core reference mass,
and bounds all other coordinate influences by q; it is not FEI as a helper.
In detail, each core probability changes by at most3q. For
F(A,B)=B log2(1+A/B), the partial derivatives on the interpolating core rows
have magnitudes <3/2 and <8, respectively. Four rows per core coordinate cost
at most114q. Off-core rows cost at most their total mass2q, because
t log2(1/t)<1 for0<=t<=1. The three core coordinates therefore cost at most348q
above M(h). Every other coordinate has influence <=q (b has3q/4-q^2/8;
each private coordinate hasq(3-q)/8), and M_i<=B_i<=h2(e_i)<=q(L+3/2).
There are2L+1 such coordinates. Summing gives (4), with the stated350 constant.

Expand the FULL source cost without dropping any term:

 C2=M(f_L)+[H(p)-H(marg_x p)]
      +E_s[H(p_s)-H(marg_b p_s)]
      +1+E_st H(marg_a p_st).

Exactly five entropy errors in (3), with reaches summing to one in each group,
and (4) give

 C2 <= C_infinity + P(L)q,
 P(L)=2L^2+124L+3270,
 C_infinity=M(h)+B_x(h)+3/2
           =39/16+(1/4)log2(10)+(9/16)log2(10/9).     (5)

The3/2 retains the full limiting CE: two x=0 branches cost2 each, and two
x=1 constant branches cost1 each, all with reach1/4. The ORIGINAL source
I_private>=e_x>=1/4-q/4 gives W>=17/4-17q/4. Since

 2P(L)-P(L+1)=2L^2+120L+3144>0,

and q decreases, the tail lower bound for W-C2 is minimized at L20. The exact
rational logarithm certificate checks

 17/4-C_infinity-(6550+17/4)/2^20 >7/8.              (6)

Equations (3)-(6), plus the finiteL1..19 certificates, prove (2). No finite
extrapolation supplies the all-L quantifier. The measured old reserve is not
being silently renamed: >1/32 was an earlier weaker certified lower bound;
>7/8 is a new lower bound for the SAME C2 account, proved here.

## 3. Arbitrary adaptive PRIVATE frontier followed by the retained marker

From EACH original x,b parent, allow ANY finite complete adaptive physical tree
on remaining PRIVATE coordinates in X2 union X3. It may stop immediately or at
different depths, choose the next coordinate from earlier outcomes, and expose
all private coordinates. Neither a nor c is queried before its leaves. Keep ALL
leaves, their original reaches, and full Fair_a references. Equation (1) yields

 D+E[sum of all reached private B_i]+E_leaf CE(p_leaf,Fair_a(p_leaf))
                                                   <=C2.  (7)

Now in EVERY reached leaf query physical a and prescribe Fair_c in BOTH actual
children. For this MARKER query the incoming a bit is indeed fair; this is a
different query from the earlier nonfair private queries. Its exact conditional
refund rho=1-B_a is used once. With Qbar=marg_a p,

 Delta=E_u[CE(p_u,Fair_c(p_u))-CE(p_u,Qbar)],
 N=B_a+E_u CE(p_u,Fair_c(p_u))-CE(p,Fair_a(p))
   =Delta-rho=B_a-J_a-E_u B_c(p_u) <= B_a <=1.       (8)

This formula DOES NOT assert N<=0: the retained-marker exposure has a genuine
possible positive cost. Every terminal keeps the full fresh-reference CE.

In the original x=b=1 branch the actual function is constant, and stays constant
under every private history. There B_a=0 and N=0, while BOTH fresh Fair_c child
references still cost1. The other THREE original parents contribute at most1
each to (8), at original reach1/4. Regardless of adaptive stopping depths,

                       E_leaf N <=3/4.               (9)

Consequently (2),(7),(9) prove, for ALL L>=1 and ALL the stated adaptive trees,

 D+E[all reached private B_i]+E_leaf B_a
       +E_(all marker children) CE(p_child,Fair_c(p_child))
                                                   <W-1/8. (10)

The original M/x/b debits stay booked; no source or fair-bit credit is renewed.
All private siblings and all marker children remain. The concrete y,z,a
continuation has32 final terminals at reach1/32, including constants. Arbitrary
untouched spectator g keeps M(g)+CE(p_g,Q_g) with coefficient ONE on BOTH sides,
with every reference tensored by Q_g. The triangle pays none of this spectator debt.

## 4. Signs, Boolean admission, countercontrol and honest remaining line

For U_J the union of selected clauses, the entire original amplitude is

 alpha_S=2 sum_(J subset{1,2,3})(-1)^|J|2^-|U_J|1_(S subset U_J)
              -1_(S=empty).

All eight signed terms are combined BEFORE squaring. Restrictions give
alpha_child(T)=alpha_parent(T)+/-alpha_parent(T+i), so their mean squared law
is the actual spectral marginal. Booleanity supplies ALL convolution identities
sum_S alpha_S alpha_(S triangle U)=1_(U=empty), not a truncated prefix. The
source comparison and exact finite certificates use this actual Boolean family.
The generic transfer (1),(8) is distinguished from its paid source application.

Normalized nonBoolean control: take N=2^18 equal singleton amplitudes on private
coordinates that are not queried (choose sufficiently large L), with x,a,b,c and
the concrete y,z dummy. All mentioned physical restrictions have norm1. M and
queried B vanish, private spectral energy is1, and fresh Fair_c CE=log2 N+1=19>17.
The paid inequality fails, while nonempty convolution at two occupied singleton
labels is2/N>0. No large truth table is allocated. Thus probability normalization
and the generic entropy identities alone do not admit this source.

Checkpoint correction: an early scratch bound suggested I_a<=q/2 in the x=1,b=0
parent. The actual value is q(1-q/2), not that bound. No claim uses it: (9) only
uses B_a<=1 and the structurally constant fourth branch, so the proof is unaffected.

Querying the final marker c and using each child's ACTUAL spectrum as reference
is already free: its full net charge is B_c-1-J_c<=0. Such an exit and carried
no-reset continuations are not an unpaid gap or a new admission theorem.

First unsupported paid-reference line: retain a private j through a chosen
frontier, then expose c and prescribe Fair_j in BOTH children, with the original
M/x/b/private/a debits, all old terminals, and SAME unused source. The generic
bound B_c does not fit the proved >1/8 leftover by itself. Price this specific
nonempty-profile change with the actual incoming kernel; do not relabel the
free actual-spectrum exit as that reset. Arbitrary signed-core initial source
admission also remains open, so this triangle theorem does not settle full FEI.
