# Same-booked-debit transfer at the negative other-owner node

All entropies and amounts below are in bits. The result is a finite physical-history certificate, not a universal FEI inequality.

Let h be negative at the six-bit indices {0,1,2,4,8,16,32,6,17,40}, with zero input bit encoding sign+1. Let J(x)=-h(x xor1), and let g_6 be negative at {0,1,2}. The actual function F=J(g_6^6) has six physically disjoint identical cores and36 physical input bits. Only block0 is queried. Tags are six symbols in original bit order0,...,5, with * meaning free.

## Exact scope and result

Query the zero-spine in physical order [2,0,1,3,4,5], stopping at each nonzero child and continuing through each zero child. There are13 actual states,6 query nodes and7 final terminals. One query, physical coordinate1 after fixing2=0 and0=0, is dummy; it has exactly zero entropy/influence cost, and both uniform children are kept. The final parent is tag00000*.

Use the previously proposed fixed rate K=9/2 for continuation. Preserve the EXACT two initial rate4 bookings of A089's actual root query2 and its nonconstant-child query0; these are not replaced by their smaller rate9/2 values. All subsequent increments use rate9/2, including signed credits.

The checked allocation described below has nonnegative remaining balances at every state and terminal, carries each original booking separately, and at tag00000* performs a selected-to-outer-cost transfer T with

    1/10<T<11/100,
    remaining full owner at00000* >12/25.

The final reach-weighted remaining account, retaining all7 complete terminal entropies, is greater than11/10. This gives an explicit signed transfer at the node requested by A071 without another rate sweep or a reset of A089's incoming debit. It does not extend the two-query rate4 owner to an entire selected-block reveal at rate4, and does not give an all-core or all-history theorem.

## 1. Exact spectra, physical influence and terminal identity

For arbitrary independent actual cores g_l, with p_l=P(g_l=-1), set m_l=1-2p_l and v_l=4p_l(1-p_l). From the actual integer Walsh coefficients a_U of J form the sign-centered coefficients

    c_T=sum_{U containing T} a_U product_{l in U-T} m_l.

Then J(z)=sum_T c_T product_{l in T}(z_l-m_l), and its squared biased masses are c_T^2 product_{l in T}v_l. These formulas are polynomial, so they remain valid when an inner core is constant and v_l=0. Full64-point inverse evaluation verifies the actual sign-valued gate even at those endpoints. Each q_l is computed independently by weighted physical outer edges and reconciled with spectral marginal v_l q_l.

In an occupied physical block, g_l-m_l has exactly the nonempty inner Fourier coefficients. Thus every physical Fourier set has a unique occupied-block pattern, with coefficient c_T times the product of its inner coefficients. The entropy chain rule and exact influence moments give

    H(F)=sum_l q_l H(g_l)+C(p),
    I(F)=sum_l q_l I(g_l),
    C(p)=H_p(J)-sum_l q_l h2(v_l).                   (1)

For a physical query in block0, q0 is fixed and all other q_l are affine in the queried core's mean. Therefore each child has its TRUE conditional reach1/2 and

    Inf_query(F)=q0 Inf_query(g0),
    Delta H(F)=q0 Delta H(g0)+C_parent-average C_child. (2)

Every remaining core and every child entropy is present. Dummy query2-point fibers are checked exactly by edges; their entropy cost is zero by equality of the actual two child functions, not merely a small interval around zero.

## 2. Owner decomposition and why a negative M needs a transfer

Fix K=9/2 and define S_K(g)=K I(g)-H(g). At any tagged state let

    A=q0 S_K(selected core),
    M=sum_{l>0}q_l S_K(g_6)-C,
    S=S_K(full function)=A+M,
    T=max(0,-M), U=A-T, O=max(M,0).

Then S=U+O. The other five original core owners first pay the full outer correction; when their margin M is negative, amount T is transferred from the selected owner to finish that payment. U and O are the amounts available AFTER the complete outer cost, so T is never charged a second time as a physical-query debit.

The13 checked states all have S>0 and U>=0. At tag00000* the exact intervals give M<-1/10 and T=-M in(1/10,11/100). Its O is zero, while U=S is positive. Thus source A071's failure of the inference "other owners suffice, selected owner wholly unused" is independently reproduced, with no denial of its negative-margin witness. The selected owner actually covers that deficit here.

These full-function S values are independently computed finite certificates. Their positivity is not inferred from the generic owner algebra and is not assumed available for arbitrary unknown cores.

## 3. Preserve the two original K4 bookings

At the root query coordinate2, the selected core's bit1 child is constant-positive, while its bit0 child is the five-bit non-flat negative set{0,1,2}. Let e1 be the FULL rate4 excess Delta H(F)-4Inf_query(F)>0. The constant-core branch receives selected debit0 at unconditional reach1/2, retaining the full nonconstant composed terminal from the other five cores. The nonconstant branch receives D0=2e1.

At its query of surviving original coordinate0, let e2 be the FULL rate4 excess and let A4_b=q0 S4(g_child_b). The checked other-owner K4 margins are positive in both children. Set B4=(A4_0+A4_1)/2. Both original labels are preserved by

    d1_b=D0*A4_b/B4,
    d2_b=e2*A4_b/B4.                                (3)

Their conditional means are exactly D0 and e2, respectively. The independent interval calculation reproduces the source incoming D0 and D0+e2 after converting its192-bit units; it also certifies D0+e2<(3/5)B4. No source executable code is imported. The four pertinent K4 child other-owner margins are independently checked, including the constant child.

Both grandchild bookings in(3) are kept exactly. The bit1 grandchild stops with reach1/4. The bit0 grandchild, tag0*0***, continues. Its two old labels are carried separately through all later queries. The source's whole-eight sharpness assertion is not reviewed or needed here.

## 4. Signed continuation rule and per-owner booking

Suppose a subsequent tagged parent has total incoming booked amount d, and its full rate9/2 query excess is e. Let S0,S1 be the full positive child slacks and B=(S0+S1)/2. Equations(1)-(2) give EXACTLY

    B=S_parent+e.                                   (4)

For each incoming debit label a, assign a_b=a*S_b/B to child b. Introduce the new query label e_b=e*S_b/B. Thus each old label keeps precisely its conditional expectation a, while the new label has conditional mean e. Signed credits remain signed; they do not erase old labels. The child's total booking is d_b=(d+e)S_b/B. If d<S_parent, then

    S_b-d_b=S_b*(S_parent-d)/B>0.                    (5)

This is an exact conditional allocation identity. It is NOT a proof that arbitrary full child slacks are positive; those are separately certified here.

Within child b, book selected liability d_b U_b/S_b and other-owner liability d_b O_b/S_b. Their sum is d_b, and their respective remaining balances are U_b(1-d_b/S_b) and O_b(1-d_b/S_b). At the negative-M target, O_b=0, so all carried liability belongs to the selected remainder AFTER its transfer T. The exact certificate leaves more than12/25 there. Elsewhere liability can move to the original other-owner remainder; that is a source-and-destination transfer of booked liability, not a newly created owner.

The unused original other-core bank is not renewed. Every q_l for l>0 is affine under each query, so its reach-weighted sum across the7 final terminals equals its original root q_l exactly. The rational equalities are recorded for all five other cores in out/SOURCE_AND_LABEL_AUDIT.json. Hence the weighted raw capacity sum_{l>0}q_l S_K(g_6) is conserved before its signed outer-cost deductions. Equations(4)-(5) account for the selected core's inherited excess exactly once as well.

At the dummy coordinate1 query, both child functions and all capacities agree, e=0 exactly, and each old label is unchanged. Both branches still have true reach1/2; the nonzero branch stops, retaining its terminal entropy and old debit.

## 5. One root account, explicit conservative-prefix cost

Let Pi_prefix be the true reach-weighted removed influence of the first two source queries:

    Pi_prefix=d_root+(1/2)d_second.

The preserved rate4 bookings exceed the corresponding rate9/2 excesses by precisely

    tax=(K-4)Pi_prefix=(1/2)Pi_prefix.

This conservative cost is explicitly charged, rather than hidden by using the larger rate. Source queries occur only on the stated branches, so no descendant or conditional weight is reset. All later increments use the same fixed K and the same old labels.

Telescope S_parent=average S_child-e along the actual tree, while every later allocation conserves all incoming labels conditionally. Across the7 final terminals,

    sum_leaf reach_leaf [S_K(full terminal)-all booked labels]
       =S_K(full root)-tax >11/10.                  (6)

The checker proves positive remaining balances at every terminal, and independently evaluates both sides of(6) with exact rational outward intervals. Every first-query label has final reach-weighted total e1; every second-query label has final total e2/2. All seven reaches sum exactly to1. These checks prevent a discarded constant branch or relabeled old charge from fabricating a remaining bank.

The two final selected-core constants still produce nonconstant30-bit full functions on the other five cores. Their full H,I,C and remaining liabilities are explicitly saved, together with every stopped nonconstant sibling. This is a finite continuation through the requested endpoint, not a selected-only full-reveal theorem; nonzero siblings are stopped with their full unresolved core spectra.

## 6. Exact validation and first unsupported universal line

SPEC.json freezes the entire13-state path, original debit rule, existing rate9/2 and all structural fixtures. The main checker validates every inner integer Walsh spectrum by Parseval, inverse signs, direct character sums and direct edges; every outer rational spectrum by Parseval, all64 inverse signs and independent weighted pivotal edges; and all6 physical query influences by an independent fiber sum. These precede entropy comparisons. Its small actual12-/11-bit truth tables additionally verify16384 signed physical coefficients and68 physical coordinate edge counts, including both constant-core signs. Logarithm intervals are proved48-term atanh bounds with outward rounding; no float decides a sign or a transfer amount.

All label equalities are algebraic formulas(3)-(6); enclosing zero in an interval is a diagnostic, not the justification of equality. Strict positivity, the transfer bracket and rational lower margins follow from saved exact interval endpoints. Source comparisons are explicitly scoped; no acceptance of the full729-state census or all A089 alternatives is claimed.

**First unsupported universal line:** extend this eligibility to arbitrary retained cores or arbitrary weak/non-flat physical continuations from an already supplied root bank, without obtaining nonnegative full S_K at every descendant by directly computing the entire unknown entropy. In this finite example, full S_K positivity is checked; asserting it universally would already contain FEI. The generic proportional-allocation identity does not discharge that premise.

## 7. Alternative next query in a different non-flat core, both children nonconstant

After the preceding certificate was saved, HETEROGENEOUS_SPEC.json froze exactly one additional alternative continuation. At tag00000*, retain the original block0 balanced one-bit core and ALL its incoming labels, but query original block1's physical coordinate0 INSTEAD OF querying block0's final bit. No rate, core dimension or initial booking is changed. This replaces the last two terminals of the first tree, rather than charging both alternative queries to one account.

The original block1 core is g_6. Its two children are actual five-bit functions negative on{0,1} and{0}, with biases1/16 and1/32, respectively. Both are nonconstant. The original block0 owner remains distinguished, even though the newly queried block is1. All six child q_l are separately recomputed; q1 stays fixed while every other q_l, including q0, averages to its parent value. Direct weighted physical edges independently verify the new removed influence.

The FULL rate9/2 query excess is strictly positive. The new two complete30-bit child functions have positive S_K and U balances, checked by their integer inner spectra and exact64-entry outer law. Apply the same labeled allocation rule of Section4, adding just one new query label and preserving each old label's conditional expectation. In each child the original-owner-to-outer transfer is paid before the carried liabilities are split. Both complete child remainders are strictly positive. The newly queried block1's mean core-slack change is included in this FULL query excess; it is not treated as an unchanged raw other-core reserve. The untouched original block0 capacity instead has conserved mean q0 times its fixed one-bit-core slack.

The five earlier stopped siblings remain EXACTLY unchanged, with their old debit labels, true reaches and full terminal spectra. Together with these two new children they again have total reach1. Their mean remaining account still equals S_K(root)-tax>11/10. No earlier debit or signed credit is removed, and no additional initial bank is introduced. out/heterogeneous.json records the complete parent, both children, independent edge influence, positive new excess, old/new label allocations and all7 final terminal balances.

This closes the concrete cross-core next-exposure test with both new queried-core children nonconstant. What remains universal is a NONCIRCULAR eligibility criterion deriving the needed child capacity from inherited signed component constraints, rather than checking full S_K entropy from scratch. The finite successful transfer and the conditional algebra alone cannot provide that criterion.
