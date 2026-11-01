# One unequal-depth DATA transaction and its constant-cost counterfamily

Author proof, pending independent-person review. All entropies and complete reference costs are in bits. FEI remains OPEN.

## 1. Consume the current synchronized frontier

Use A022-ODDFACE-SURGERY-GAP-LEDGER@8, run20261023T053944Z, PROOF1--4, and its earlier@7 PROOF1--6. Thus t>=2, g is -1 only at000, b=g tensor t, delta=8^-t, and F equals b(x)a(z) at x=v and b(x) elsewhere. The controller a is ANY finite Boolean function on independent physical coordinates. The fixed data order is block-first. At a synchronized data depth d=3r+j<=3floor(t/2)+2, j=0,1,2, A022@8 permits any earlier active-only controller trees and proves the ACTUAL identity

    B_before=Bpure_d+Gamma_old,  Gamma_old>=0,
    B=4 I_remaining_DATA+L-C-U,  0<=U<=t/64.             (1)

C and D=C-H include every complete terminal cost/KL, including inactive siblings and their frozen controller references. L=delta sum_active p_e H(a_e) is the remaining ORIGINAL source-controller earmark; its earlier spend K satisfies K+L=delta H(a_root). No part of K is renewed. The prescribed controller reference is ALWAYS R_delta,a=(1-delta)point_empty+delta P_a, even when conditional activation density differs. Data references q are exactly A022@7's original/one-query/two-query profiles.

Choose ONE active controller leaf e which has experienced at least one controller query. Its actual controller reach p_e=rho<=1/2, current restricted a_e and alpha_e=(1-Ea_e)/2 are retained. Its data cylinder has original reach w=2^-d. Query the next data coordinate ONLY on e. All other frontier leaves remain at depth d. Both new children use the prescribed next data q, and BOTH inherit the SAME current R_delta,a_e, including the new inactive sibling; it is frozen there. This creates a genuinely unequal-depth stopping cut. No child bank or entropy budget is admitted again.

## 2. Exact local capacity loss, all vertex types

Let h=4-(9/8)log2(3), c1=3-(1/2)log2(13), c2=4-log2(15). Let sigma be the original g(v_block)g(v_block xor queried_bit), and J(000)=-(7/4)log2(3), J(u)=(5/4)log2(3) otherwise. The current partial block is the only data-reference factor changed. Parseval preserves controller CE in EXPECTATION and preserves L. Remaining DATA influence decreases by the actual reached query influence. Hence

    B_after=B_before-ell_e,                              (2)
    ell_e=rho [ w ell_base + delta alpha_e T_j ].         (3)

These quantities use ORIGINAL delta and actual rho,w. The complete list is:

* j=0: ell_base=1-h+c1=(9/8)log2(3)-(1/2)log2(13)<0,
  T0=8sigma-4J(v_block)+w1, where w1=0 if the newly queried vertex bit is0 and3log2(13) otherwise.
* j=1: ell_base=c2 if the earlier fixed bit is0, and log2(13)-log2(15) if it is1.
  T1=8sigma-w1+2log2(15), with w1 determined by that earlier fixed vertex bit.
* j=2: let c=1 when both earlier fixed bits are0 (the remaining seed is a character), and c=0 otherwise (a constant). Then ell_base=4c-c2 and T2=8sigma-2log2(15), where sigma=-1 for c=1 and+1 for c=0.

Derivation: the unedited influence and reference drop give ell_base. The point surgery changes physical query influence by2 eta alpha_e sigma, eta=delta/w. The local reference edit corrections before and after are respectively4 eta alpha_e J versus eta alpha_e w1 for j=0; eta alpha_e w1 versus2 eta alpha_e log2(15) for j=1; and2 eta alpha_e log2(15) versus0 for j=2. Multiply by ORIGINAL w rho to obtain(3). All untouched data-reference factors, all controller-reference costs, and every unqueried sibling cancel by exact equality rather than being dropped.

The following bounds are uniform in the controller, history and t:

    j=0: ell_e<=6 delta<=3/32;
    j=1: ell_e<=1/6;
    j=2,r=0: ell_e<=1/2;
    j=2,r>=1: ell_e<=1/16.                              (4)

For j=0 the base is negative because3^9<13^4. The eight vertex types give T0<12: at000 use -8+7log2(3); at a nonzero vertex with queried bit0 use8-5log2(3); at v=e_i use -8-5log2(3)+3log2(13); otherwise use8-5log2(3)+3log2(13)<12, since log2(3)>14/9 and log2(13)<15/4. The latter follow from3^9>2^14 and13^4<2^15. For j=1, c2<1/6, T1<16, w<=1/2, rho<=1/2 and delta<=1/64 give ell<=1/24+8delta<=1/6. For j=2, the character case has T2<0 and ell<4rho w<=2w; w=1/4 when r=0 and w<=1/32 when r>=1. The constant case has negative base and T2<1/3, giving ell<delta/6<=1/384. Here c2<1/6 follows from15^6>2^23. No positive-part replacement of ell is made in the exact account.

## 3. The SAME actual unused source pays the charge

We need more information than the loose guarantee Bpure>=13t/576. Re-evaluate the SAME exact source, with no changed reference or booking. Let n=t-r-1[j>0] be the number of untouched full blocks. Their unedited bank beta=3-h>3/4. The partial-block bank b_j=2-c1 or1-c2 is>5/6. The exact signed surgery costs obey X<=118/9 per untouched block and Y_j<=16 per partial block (A022@7 PROOF3,5). Also

    G_delta(s)=H(R_delta,a)-delta H(a)<=h2(delta)
                <=delta(3t+log2(e))<delta(3t+3/2).        (5)

The first inequality is entropy of a mixture with its mixture label retained; equivalently use the explicit G formula and its maximum at s=0. The last uses ln2>2/3. Thus the SAME actual source has the stronger lower estimate

 Bpure_d >=(3/4)n+(5/6)1[j>0]
           -delta[(118/9)n+16*1[j>0]+3t+3/2]-t/64.       (6)

This is unused existing balance, not an extra source allowance. Relax only delta<=1/64, n>=t/2 for j=0, n>=t/2-1 for j>0, and n=t-1 for r=0,j=2. Rational simplification gives

    j=0: Bpure >=121t/576-3/128;
    j>0: Bpure >=121t/576+17/1152;
    r=0,j=2: Bpure >=139t/288+17/1152.                   (7)

Subtracting (4), each bound exceeds13t/576 for EVERY t>=2. The exact excess lower bounds are respectively

    j=0: 3t/16-15/128;
    j=1: 3t/16-175/1152;
    j=2,r>=1: 3t/16-55/1152;
    j=2,r=0: 265t/576-559/1152.                          (8)

Each affine expression is increasing and positive already at t=2. Combining(1),(2),(7),(8) proves

    B_after >=13t/576+Gamma_old.                        (9)

In fact these estimates retain an additional t/10, but(9) is the only admission used. The old Jensen credits are explicitly retained; the actual charge ell_e is debited once from unused original source surplus. A later step must keep ell_e, not readmit Bpure as a new bank. The proof is all-dimensional in t and controller dimension; finite enumeration is a check, not this passage.

## 4. Both complete terminal debts and actual phase conversion

The source entropy earmark L does not change at this DATA query. The physical reach of the parent is w rho. With its actual physical data influence Inf_i and conditional output entropy decrement DeltaH_F, add exactly w rho(4Inf_i-DeltaH_F) to the previous signed history E. Since D=C-H,

    B_after+D_after+E_after=B_before+D_before+E_before.   (10)

Both new children remain, as do ALL untouched terminals at depth d. If comparing target references with actual phase inheritance, pair parent amplitudes x,y and send either member to (b,pair) with probability (x+(-1)^b y)^2/[2(x^2+y^2)], using1/2 when x=y=0. Propagate every reference atom; normalize by its actual positive branch mass. KL chain rule gives D_parent=erasure+outcome+average D_inherited. Therefore the raw signed conversion kappa satisfies

 kappa-erasure-outcome=average D_target-D_parent.        (11)

The net expression is retained in(10), not separately clipped. The old controller query used its original delta p entropy spend and has not been recomputed or erased.

## 5. A parameterized rare-event obstruction with constant local charge

For EVERY integer t>=2, take the actual Boolean function

 F_t(x,z)=b_t(x)(1-2*1[x=0^(3t)]*z), z in{0,1}, delta=8^-t.

Reveal the first two DATA bits in block1 (all four physical data children remain). Query z ONLY in the active00 cylinder, retaining both outcomes and original controller references. On the z=0 child, query the third DATA bit ONLY there. The selected leaf is the unedited remaining character of block1, tensor the untouched remaining blocks. Thus rho=1/2,w=1/4,alpha_e=0,c=1, and(3) gives EXACTLY

    ell_e=log2(15)/8>0, independently of t.              (12)

Consequently NO fixed finite K pays every such selective DATA capacity loss by K*t*delta: ell/(t*8^-t) tends to infinity. This refutes ONLY the all-coordinate LOCAL charge rule using rare-edit-only t delta payment at admitted histories. It does not refute a constant in FEI, an influence-based query price, or the universal stopping-tree route. The actual unused source pays this charge by(9).

Indeed this counterfamily satisfies H(F_t)<5 I(F_t). Physical edges give EXACTLY I(F_t)=3t/4-3t delta+delta. Since delta<=1/64, I>=45t/64, while the dimension bound gives H<=3t+1<=7t/2. Hence H/I<=224/45<5. Its Boolean nature and bounded entropy/influence ratio distinguish a local charge obstruction from an FEI disproof.

## First unsupported universal line

After this unequal-depth operation, a second data query on an already changed branch must retain the FIRST actual ell_e, changed data reach, current q/R, old Gamma, U, original source entropy spend and all complete terminal KLs. Equations(1) and(7) cannot be readmitted as fresh source credit. Arbitrary unequal-depth mixed frontiers and an influence-priced arbitrary source-controller entropy supplier remain unproved. This single transaction is not a universal induction.
