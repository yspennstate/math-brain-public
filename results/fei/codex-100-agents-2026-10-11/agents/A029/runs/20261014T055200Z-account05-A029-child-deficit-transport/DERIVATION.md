# Sharp two-block compression with all child deficits retained

Use the exact stage4 interface, independently accepted by A023 stage5 REVIEW_A029.md, and the A023@3 whole-point-block theorem previously reviewed by A029. For arbitrary shared-data cores g0,g1,g2, disjoint fresh point blocks with a=2^-r,b=2^-s,r,s>=1, set h=g1+B(g2-g1), f=g0+A(h-g0). Terminal weights pi=(1-a,a(1-b),ab); I_C=I_A+aI_B. Both outer children and both inner children have their actual original weights. Put Iij=I(gi gj).

    R_star=2 sum_{i<j}pi_i pi_j Iij,
    R_data=2a(1-a)[(1-b)I01+bI02]+2ab(1-b)I12,
    R_controls=2a(1-a)I_B.

The sharp DATA conversion, uniform over every core dimension and core triple, is

    R_data<=kappa(a,b) R_star,
    kappa(a,b)=(2-a-b)/(1-ab), 4/3<=kappa<2.

Proof: On any data edge, let r_j be the Boolean indicator that gj is pivotal there. A product edge pivots iff r_i XOR r_j. If all three agree, both reserves are zero. Otherwise exactly one label differs. Ratios for the exceptional labels0,1,2 respectively are

    1, (1-a+b)/(1-a+ab), (2-a-b)/(1-ab).

The last dominates the middle because the cross-multiplied difference is (1-a)^2(1-2b)>=0. It also dominates1. Summing the nonnegative edge contributions proves the inequality. The range follows a,b<=1/2 and positivity; the lower bound is equivalent to2-3a-3b+4ab>=0, minimized at a=b=1/2 on this square, and kappa<2 follows a+b>2ab. Sharpness holds even with three DISTINCT NONCONSTANT cores: g0=x,g1=-x,g2=xy on two shared bits. The x edge pivots in every branch and contributes zero; only the y edge has exceptional label2, so equality holds. This certifies the conversion factor, not sharpness of actual entropy payment.

Therefore the prior signed sufficient condition improves to the order-free one-owner form, for EVERY real K,

    D_K(f)>=sum_j pi_j D_K(gj)+(K-11/2)I_C
             -kappa R_star-2a(1-a)I_B.

This is a sufficient upper-price argument. Neither negative child is clipped. The future B-control debit remains explicit. In particular supplied terminal rates Cj give

    H(f)<=max(11/2+2(1-a), max_j[Cj+2kappa(1-pi_j)]) I(f).

Only one root R_star is marked at multiplier kappa; the mark is not recreated at descendants. This is a finite two-block all-dimensional consequence of the reviewed source, not a depth-independent nested FEI theorem. A023's stronger finite rate4 with multiplier1 is not contradicted.

# Multi-state boundary bank through physical mixed histories

Let L(y) be ANY deterministic finite-valued controller map on fresh fair physical controls, and let gj(x) be ANY finite list of Boolean cores on a common independent uniform data cube. Output F(x,y)=g_{L(y)}(x). After each actual adaptive physical history, pi_j=P(L=j | fixed controller bits); restrict ALL cores on fixed data bits. Remaining control and data bits are still independent uniform cubes. Labels with pi_j=0 are harmless. Define

    R=2 sum_{j<k}pi_j pi_k I(gj gk).

This is an extension of A028@5's binary carried boundary bank, NOT a new proof of its baseline influence telescope. On each remaining data direction i and data point x, let r_j(i,x) be the Boolean core pivot indicator, q_i(x)=sum_j pi_j r_j(i,x). Product pivotal XOR gives the exact representation

    R=2 sum_i E_x[q_i(x)(1-q_i(x))].

It follows R<=2 I_data(F), and more precisely the terminal owner cap is sum_j2(1-pi_j)pi_j I(gj). For a CONTROLLER query producing pi^0,pi^1, q=(q0+q1)/2, the exact release is

    R(parent)-[R(child0)+R(child1)]/2
      =(1/2) sum_i E_x[(q_i^0-q_i^1)^2]>=0.

For a DATA query i, probabilities pi stay fixed and ordinary product influence conservation gives

    release=2 sum_{j<k}pi_j pi_k Inf_i(gj gk)
           =2 E_x[q_i(1-q_i)]<=2d_i(1-d_i)<=2d_i,

where d_i=Inf_i(F)=E q_i. The sharper local release cap is Jensen for the concave t(1-t). If data space shrinks, the remaining directions' capacities telescope with both physical children. This proves exact nonnegative supermartingale conservation for any mixed stopped tree:

    R(root)=sum_v physical_reach(v) release(v)+E_terminal R.

At resolved-controller leaves R=0, though the actual core entropy/influence may remain. A selected child may have larger R; only the original physical sibling average supports the release identity. A FIXED root multiplier kappa contracts with the same bank. Changing multiplier after restriction requires an additional priced term and is NOT licensed.

# Boundary of the repair

The once-carried bank is a resource, not an entropy drift theorem. A028's exact AND2 guard has Hroot=2, both data-child entropies0, branch entropy drops0, data influence1/2 and bank release1/2. Release-only entropy payment fails by3/2 and needs an added local data price at least3. This guard survives as a two-label subcase of the multi-state construction. No universal controller-influence bound on controller release is asserted.

The new sharp factor covers the TWO-BLOCK inherited data surcharge using one priced root bank, but can approach2; it does not establish multiplier1 actual entropy payment for arbitrary three cores. The old constant-failure chain has split data/root bank ratio d/[2(1-2^-d)] on d one-bit controls, unbounded, so no fixed conversion factor pays every repeated block's sufficient reserve. Grouping those controls was already handled in stage4 and is not re-proved here.

FIRST UNSUPPORTED LINE: at the next genuinely non-flat mixed query, pay the signed entropy/reference residual with the released fixed-price multi-state bank, actual queried influence, and one unused inherited child surplus, keeping both complete terminal debts. Conservation and two-block compression alone do not justify that line. Full FEI remains OPEN.
