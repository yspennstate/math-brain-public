# Closing marker exposure by the complete terminal-KL budget

Uniform normalized Walsh coefficients are used throughout. H, CE and KL are
in bits; B_i(p)=H(S_i|S_-i). Every tree is finite and complete: a physical query
retains BOTH outcomes, each with its true conditional reach 1/2. No queried
coordinate is queried again on its path. Intermediate costs use signed reset
conversions and actual conditional-KL refunds, not their positive parts alone.

## 1. The reviewed original source

For every integer L>=1, f_L=2 product_k(1-1_{E_k=0})-1, where
E1={x,a,c}, E2=X2 union {a,b}, E3=X3 union {b,c}, and X2,X3 are disjoint
L-bit blocks. All four core coordinates are distinct. Define the ORIGINAL

 W=17 I_private(f_L), private={x} union X2 union X3,
 D=M(f_L)+B_x(f_L)+E_s B_b(f_L|x=s),
 C2=D+E_st CE(p_st,Fair_a(p_st)).

Here p_st are the four actual x,b restriction spectra, each of original reach
1/4, M is original oriented erasure, and Fair_i(p)=fair_i(marg_i p). The supplied
version A031-RETAINED-MARKER-EXPOSURE-SAME-ORIGINAL-BANK v1 proves

                         C2 < W-7/8.                 (1)

This is the SAME complete source account used in the preceding stages, with a
new, stronger lower bound on its reserve. We independently review its source
estimate below; no new child influence reserve is introduced. The actual x=b=1
parent is constant, so B_a(p_11)=0. Since B_a<=1 at every other parent,

                         E_st B_a(p_st)<=3/4.        (2)

All constant and dummy branches still have complete Fair_i CE equal to ONE.

## 2. The exact generic whole-history identity

At a node with signed parent amplitudes alpha, physical child amplitudes are
alpha(T)+/-alpha(T+i). The mean CHILD law therefore equals marg_i p. Hence

 H(p)-E_u H(p_u)=B_i(p)+J_i(p),
 J_i(p)=H(marg_i p)-E_u H(p_u)>=0.                    (3)

J_i is the Jensen-Shannon divergence of the two actual child laws. Multiplying
by actual reaches and telescoping over any finite complete adaptive tree T gives

 sum_internal reach(v) B_i(p_v)+E_leaf H(p_leaf)
       =H(p_root)-sum_internal reach(v) J_i(p_v).    (4)

Now give every terminal a complete normalized Q_leaf with actual support included.
Let d_leaf=D(p_leaf||Q_leaf). Since CE=H+d, (4) yields the EXACT identity

 sum_v reach(v) B_i(p_v)+E_leaf CE(p_leaf,Q_leaf)
       =H(p_root)-J_T+E_leaf d_leaf,                 (5)
 J_T=sum_v reach(v) J_i(p_v)>=0.

This is generic transfer using actual physical mixtures, not Boolean source
admission. Reference-normalization and support conditions are essential. All
past reference conversions and conditional refunds telescope to these complete
endpoint bills. Equation (5) does NOT bound cumulative positive parts of reset
turnover if negative credits are discarded.

## 3. Arbitrary marker exposure and prescribed private reset are paid

From EACH original x,b parent allow ANY finite complete adaptive physical query
tree, with no prohibition on exposing a or c. Supply terminal references whose
FULL KL divergence is at most 1+delta, for some fixed 0<=delta<1/8. They may be
different at different leaves, and stopping depths and query choices may depend
on the actual history. Define the full bill

 F=D+E_st[sum_v reach(v|st) B_i(p_v)+E_leaf CE(p_leaf,Q_leaf)].

CE(p_st,Fair_a(p_st))=H(p_st)+1-B_a(p_st). Subtract C2 from (5) and average:

 F-C2=E_st B_a(p_st)-E_st J_T+E_all_leaves d_leaf-1
      <=3/4+delta.                                  (6)

Combining (1),(6) proves

                  F < W-(1/8-delta).               (7)

Every original M/x/b debit, every reached private/core erasure, every old signed
reference conversion, and EVERY full terminal CE remains in this account. There
is no assumption of post-query a/c symmetry and no new local fair-bit refund.

In particular, retain ANY private j along the chosen history, expose a and then
c, and prescribe Fair_j(p_child) in BOTH children of c. Since

 D(p||Fair_j(p))=1-B_j(p)<=1,                         (8)

(7) with delta=0 proves the explicit A031 NEXT for ALL L and ALL such adaptive
histories, with SAME original rate17 and more than1/8 spare. A retained private
j may depend on the terminal history if it is actually still unqueried there.
All intermediate marker changes are allowed at complete cuts satisfying the
same full-KL cap. If no coordinates remain, the actual-spectrum reference is
also allowed and has KL zero. No fixed-marker stopping restriction remains.

This is strictly a paid-source application of a generic identity. It neither
proves uniform original admission nor adds a universal Booleanity inequality.

## 4. One controlled arbitrary reference-profile change also fits

Equation (7) with delta=1/16 leaves more than1/16. A complete explicit class of
such reference changes is, at any terminal retaining j,

 Q'=(31/32) Fair_j(p)+(1/32) R,

where R is ANY complete normalized reference on the SAME remaining spectral
space. The full law is normalized and dominates (31/32)Fair_j(p). Therefore

 D(p||Q') <= D(p||Fair_j(p))+log2(32/31)
           <=1+log2(32/31)<17/16,                   (9)

where the strict scalar bound follows from the exact rational inequality
(32/31)^16<2. Thus a genuine arbitrary reference-profile mixture can be paid
after the marker exposure from this SAME original bank, with all terminal costs
and more than1/16 reserve. This statement concerns the full final law, not a
fresh allowance to add 1/32 repeatedly without checking the current full KL.
It is a corollary of (7); no new source supplier is asserted.

## 5. Local positive price and exact checks

At a parent p immediately before exposing c, incoming Q=Fair_c(p). Put
Qbar=marg_c Q=marg_c p, and prescribe Qnew_u=Fair_j(p_u). The exact local refund
and conversion are

 rho=1-B_c(p), Delta=E_u[CE(p_u,Qnew_u)-CE(p_u,Qbar)],
 N=Delta-rho=B_c(p)-J_c(p)-E_u B_j(p_u).              (10)

N can be POSITIVE. The main frozen certificates and independent truth-table
reconstruction record genuine positive examples at L3. Their positivity is
not an obstruction to (7): the complete account retains earlier releases and
the original source reserve. Assuming N<=0 at every node would be a false
local strengthening. No positivity at untested L is extrapolated.

The compressed checker treats x,a,b,c, queried private y,z and retained j as
explicit coordinates. Only the remaining coordinates of each private block
are grouped by empty/nonempty spectral hit, with exact multiplicities. Signed
inclusion-exclusion amplitudes are summed BEFORE squaring. Independent code
uses actual truth tables and integer FWHT, without importing the compressed
checker, plus distinct rational log enclosures. It checks all root convolution
shifts at L1 and all canonical signed collapses at L1,2,3.

An independent exact Bellman interval envelope at L1,2 checks ALL adaptive
physical query/stop policies retaining one private j, including a/c exposure
in arbitrary orders. At each of the 1080 physical partial-history states it
compares immediate Fair_j stopping with every available physical query. Maxima
of interval upper endpoints bound all policy values; no guessed optimal policy
or floating-point sign is used. This is finite validation; (3)-(7), not the
finite census, establish the all-L/all-tree quantifiers.

## 6. Independent review of A031's strengthened source

The limiting function h is the three-bit point defect on x,a,c. Actual Boolean
disagreement Pr(f_L!=h)<=q/2, q=2^-L. After at most two fixed physical inputs,
the disagreement is <=2q, amplitude error<=4q, and off-limiting-support squared
mass<=8q by Parseval. There are at most8 limiting atoms. Their total absolute
mass change after a spectral marginal is <=8*8q+8q=72q. For L>=20 each positive
limiting atom, originally at least1/16, stays at least1/64. Entropy has derivative
magnitude<8 there. Its supported entropy error is therefore <=576q. The remaining
mass t<=8q on at most2^(2L+4) labels has entropy <=(24L+8)q. Thus every used entropy
error is <=(24L+584)q. This argument also covers dummy/constant cofactor marginals.

For original M, three core coordinates have four limiting rows each; each core
probability error<=3q. For F(A,B)=B log2(1+A/B), |partial_A F|<3/2 and
|partial_B F|<8 along those rows. This contributes <=342q. Off-core rows contribute
at most their total row mass, <=2q per core coordinate, hence <=6q. The other
2L+1 coordinates each have influence<=q, and M_i<=B_i<=h2(q)<=q(L+3/2).
Summing yields M(f_L)<=M(h)+(2L^2+4L+350)q. No unknown FEI bound occurs here.

Expanding C2 uses exactly FIVE entropy errors, so

 C2<=C_infinity+(2L^2+124L+3270)q,
 C_infinity=39/16+(1/4)log2(10)+(9/16)log2(10/9).

Our independent limiting-row reconstruction checks this constant rather than
copying it as an opaque input. I_private>=1/4-q/4. At L20 a rational logarithm
certificate proves

 17/4-C_infinity-(6550+17/4)/2^20 >7/8.

The positive coefficient polynomial
2P(L)-P(L+1)=2L^2+120L+3144 proves monotonicity for the tail. Exact independent
finite-source computations cover L1..19. This reconstructs the critical source
argument and endpoint without repairing the reviewed statement. The original
marker-exposure extension then follows from fixed-marker closure and the
constant fourth parent, as A031 states. Its scoped claim HOLDS; full FEI does
not follow. Our new theorem depends only on its strengthened source substatement,
not on a circular acceptance of the new endpoint theorem.

## 7. Boolean admission, spectators, and the first unpaid line

There is also an ACTUAL BOOLEAN obstruction to removing the terminal-cost cap.
Take this same triangle at L=64. Retain any fixed FIVE private inputs J in X2;
after x,b physically query every other remaining input, retaining all outcomes.
At every terminal prescribe the COMPLETE uniform law on the 2^5 frequencies of
J. Its CE is exactly5 for every normalized actual child, INCLUDING constants.
All original and reached erasure debits are nonnegative, so the full bill is at
least5. On the other hand the exact original private influence is

 I_private=(2-2q+q^2)/8+2L*q*(3-q)/8, q=2^-L,

and at L64 rational arithmetic verifies 17 I_private<5. Therefore an unrestricted
version allowing these five-bit references is FALSE on an actual Boolean function.
No huge tree or truth table is allocated: the reference's uniformity proves every
terminal cost symbolically. This is a reference-payment obstruction, not an FEI
counterexample and not a claim that the chosen conversion is necessary. The five
ghost bits at constant terminals cannot be erased from the bill. No sharp maximal
admissible terminal-KL threshold between our sufficient bound and this obstruction
is claimed.

Normalization alone still fails the source: choose N=2^18 equal singleton
amplitudes on unqueried private coordinates, disjoint from all designated dummy
queries. All mentioned restrictions have norm one, original private spectral
energy is1, and queried erasures and M are zero; a dummy retained Fair_j costs
log2 N+1=19>17. Nonempty convolution at two occupied singleton labels is2/N>0.
The generic identity remains valid but supplies no paid initial account.

For an untouched independent Boolean spectator with supplied finite-cost Q_g,
retain M(g)+CE(p_g,Q_g) with coefficient ONE on both sides, tensoring every
triangle reference with Q_g. Apply the KL cap only to the triangle component;
its owner pays none of the spectator debt.

The first unpaid universal line is an influence-priced initial complete source
for an arbitrary signed Boolean core, or a NECESSARY actual reference conversion
whose FULL terminal KL exceeds the available inherited budget. Merely exposing
another single marker or repeating a fixed bounded-KL cycle is now covered.
The theorem does not bound arbitrary positive-part reset turnover, arbitrary
reference laws, or uniform source CE by influence. Full FEI remains OPEN.
