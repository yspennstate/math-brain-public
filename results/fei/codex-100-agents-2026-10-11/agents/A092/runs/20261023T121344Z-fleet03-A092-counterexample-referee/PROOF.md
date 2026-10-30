# Independent audit of the literal envelope obstruction and empty-term payment

All entropies, deficits and cross entropies below use bits. Both physical
children are retained at their fair reaches. Full FEI is OPEN.

## 1. Actual circuit and independent reconstruction

Let g_m be -1 only at the allzero m-bit vertex and +1 elsewhere. Let h
be +1 exactly when all three of its input signs are +1. On disjoint
blocks of sizes3,2,2 set F=h(g3,g2,g2). In particular F(x)=+1 exactly
when all three blocks are nonzero. This defines all128 truth values.

Query original physical bit0 in the first block. At outcome0 its child
is h(g2,g2,g2) on the six remaining physical coordinates. At outcome1
it is h(+1,g2,g2), still on SIX physical coordinates; the two leftover
first-block coordinates are retained as dummies, not deleted terminals.

For a disjoint AND gate, q_j=product_(ell!=j) Pr(g_ell=+1), by direct
physical pivotality. Define the FULL correction

    C(f)=H(f)-sum_j q_j H(g_j).

No occupied-set product assumption is needed: the checker derives H(f)
from direct integer character sums on the actual full truth table. It
independently checks an integer butterfly transform and physical edge
influences. From those exact spectra it obtains

    C_parent=57/8-(1431/1024)log2(3)-(3087/2048)log2(7),
    C_0=53/8-(1701/512)log2(3)-(25/512)log2(5),
    C_1=3-(27/16)log2(3).

All three C are strictly positive. Clearing the symbolic-log rational
denominators gives three positive integer comparisons, respectively

    2^14592 > 3^2862*7^3087,
    2^3392 > 3^1701*5^25,
    2^48 > 3^27.

Thus taking positive parts changes none of these three values.

## 2. Exact all-real-K scope and sign

For m=0,1,2,3, every restriction of g_m is a smaller point core or a
constant. H(g1)=0,I(g1)=1; H(g2)=2,I(g2)=1; and
H(g3)=4-(9/8)log2(3), I(g3)=3/4. The inequality H(g3)<3I(g3)
is equivalent to 3^9>2^14. Constants have zero entropy/influence.
Induction through every possible inner stopping tree therefore gives
rho_K(g_m)=0 for EVERY real K>=3, not just tested integer rates.

The proposed U_K=C_+ +sum_j q_j rho_K(g_j) equals C at the parent and
both complete children. Its drift is consequently

    G=(C_0+C_1)/2-C_parent
     =-37/16-(567/512)log2(3)-(25/1024)log2(5)
                         +(3087/2048)log2(7).

The exact sign certificate is

    7^3087 > 2^4736*3^2268*5^50.

This is a comparison of arbitrary-precision integers reconstructed by
clearing denominators in the truth-table-derived log expression. It is
independent of floating evaluation. Rigorous rational log intervals also
give 0.107184<G<0.107185. Parent and full-child influences are
111/64,27/16,3/2; the queried coordinate has influence9/64 by BOTH the
physical edges and I_parent-mean I_child.

The modified candidate U_K+lambda I is superharmonic on this row only
if lambda>=(64/9)G, where 0.762198<(64/9)G<0.762199. This is a NECESSARY
local coefficient, not a sufficient universal repair. Any conditional
credit allocation with mean conserved and initial stock exactly U_K(parent)
cannot dominate both prescribed child requirements: their mean exceeds
it by G. Old owner names and sibling rerouting do not create this mean
stock. The source's conditional rerouting theorem is not refuted.

## 3. The full empty Fourier term is payable in every dimension

Put phi(t)=-t^2 log2(t^2), phi(0)=0. Its derivative extends continuously
at0 and equals -(2t/ln2)(2ln|t|+1). For0<=t<=1,
|t(2ln t+1)|<=1: where 2ln t+1>=0 both factors are at most1;
on the negative branch the maximum is2exp(-3/2)<1, by differentiation.
Evenness handles t<0. Hence phi is globally2/ln2-Lipschitz.
The first positive term of the atanh series at1/3 gives ln2>2/3,
so the Lipschitz constant is strictly less than3.

For ANY Boolean f and ANY physical coordinate j, let its two full
child means be mu0,mu1 and d=Inf_j(f). Direct physical coupling gives
|mu0-mu1|<=2d, while mu=(mu0+mu1)/2. Therefore

    mean phi(mu_b)-phi(mu) <= (2/ln2)d <=3d.

The exact physical identity I(f)=d+mean I(f_b) proves that

    V(f)=phi(Ef)+3I(f) >= mean V(f_b)

under every query. The elementary inequality -u ln u<=1-u gives
phi(Ef)<=Var(f)/ln2. Parseval gives Var(f)<=I(f), hence

    0<=V(f)<=9I(f)/2.

This is an ALL-DIMENSION proof of the EMPTY entropy component only.
It does not majorize full H or establish a whole FEI-deficit envelope.
When inserted in an existing ledger, its influence payer must be actual
unused original stock; the same I cannot be reissued after earlier debits.

## 4. Separation on the literal witness

The empty squared coefficients of the full parent and children are
1/4096,25/1024,1/64. Their entropy drift is

    G_empty=85/512-(25/1024)log2(5).

The remaining drift is

    G_nonempty=G-G_empty
      =-1269/512-(567/512)log2(3)+(3087/2048)log2(7)<0,

certified by 7^3087<2^5076*3^2268. Thus the complete empty-term bill
explains this example's positive drift. It may be paid by the universal
component lemma if its original payer is available. The nonempty
correction being favorable on ONE witness does not prove universal
coherence, especially near cancellations of nonempty coefficients.

## 5. Actual stopping hull versus proposed overprotection

Here the stopping-deficit hull uses the source's terminal-deficit convention:
rho_K(v)=max{(H(v)-K I(v))_+, max_j mean rho_K(v_{j=b})}, with constants
having hull0. It does not assert a new bound for separately added erasure
charges or a different ledger. This explicit recursion is what the
supplemental finite certificate closes.

The supplemental checker freezes and enumerates all3^7=2187 labelled
physical restrictions of THIS original circuit and all5103 outgoing
physical query rows. It uses direct full truth tables, exact symbolic
entropy forms and integer signs. It verifies H<=3I at every state.
Backward induction then proves the TRUE full stopping deficit hull is
identically0 for this circuit at K=3 and consequently every K>=3.
The result is saved only after that exhaustive check passes. It does
not extrapolate to unrestricted circuits or larger block sizes.

This makes the distinction precise: the proposed U_K asks for positive
stock and has a positive drift even though this witness's actual deficit
requires zero stopping stock at those rates. The refutation is of that
candidate envelope, not an unavoidable FEI liability. No restriction
table is dropped by symmetry; memoization reuses byte-identical tables.

## 6. Exact remaining universal line

Construct an initially influence-priced superharmonic envelope for the
NONEMPTY signed correction plus inherited inner stopping hulls, retaining
the paid empty component, full children, old owner labels and already
spent donor. The local coefficient bound above is necessary only on its
one row. Neither adding new influence stock without an unused owner nor
discarding the empty entropy term repairs the universal ledger. The
source claims are accepted only at their explicitly stated scopes.
