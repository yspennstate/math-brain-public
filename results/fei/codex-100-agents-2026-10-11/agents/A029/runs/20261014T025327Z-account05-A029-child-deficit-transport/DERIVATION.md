# Two physical children and one nested reserve

All bits uniform, signs Boolean, entropy bits. Independently review ONLY the additional whole-block clause of A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER@3; older overlap/separator clauses and its unconditional activation family are excluded. No source repair is needed for the reviewed clause.

Let A,B be independent fresh point blocks of widths r,s, probabilities a=2^-r,b=2^-s. Three arbitrary cores g0,g1,g2 share the same data cube. Put h=g1+B(g2-g1), f=g0+A(h-g0). Query A to resolution, then B on success. Stop at actual cores. Terminal weights pi=(1-a,a(1-b),ab); terminal entropy and influence are their weighted sums. I_B=2s b P(g1!=g2), I_A=2r a[(1-b)P(g0!=g1)+bP(g0!=g2)]. Removed influence is I_A+a I_B.

Write Iij=I(gi gj), ordinary influence on data only. The marked reserves from the TWO applications of the source theorem are exactly

    R_data=2a(1-a)[(1-b)I01+b I02]+2ab(1-b)I12,
    R_controls=2a(1-a) I_B.

Reason: I(g0 h) on data is (1-b)I01+b I02, and on B controls is I_B because g0 is independent of B. The inner reserve is weighted a. These are actual physical derivative counts, including edges destroyed by a core change. No disjoint-core assumption occurs.

At price K the source bound gives the sufficient, signed condition

    D_K(f) >= sum pi_j D_K(gj)+(K-11/2)(I_A+a I_B)
              -R_data-2a(1-a) I_B.

The right side retains both outer physical children and both inner physical children, with their ORIGINAL reach weights. Its nonnegativity is sufficient for D_K(f)>=0; it is not necessary. Neither child deficit is clipped or discarded. A source entropy upper bound is used, not an equality for the actual decrement.

For EACH data coordinate the reserve cap is the terminal influence capacity multiplied by:

    core0: 2a; core1: 2(1-a+b); core2: 2(2-a-b).

Thus any independently certified terminal prices Cj give the finite two-block rate

    max(11/2+2(1-a), C0+2a, C1+2(1-a+b), C2+2(2-a-b)).

This is a diagnostic consequence of the reviewed source, not a universal induction. In particular the same core2 capacity can receive more than TWO rate units after only two blocks. Data-edge product influence is exactly the XOR of the two branches' pivotal indicators; bounding XOR by their sum gives these coordinate owners.

# What would need a refund

Define the order-free data functional R_star=2 sum_{i<j} pi_i pi_j Iij. Direct expansion gives

    R_data=R_star+2a(1-a)b(1-b)I12.

R_star<=sum_j 2(1-pi_j)pi_j I(gj)<=2 I_terminal. The added term is a strictly positive possible order/grouping surcharge. This algebra DOES NOT prove that R_star pays actual entropy decrements. Removing the surcharge without another inequality is the FIRST UNSUPPORTED LINE of an order-free universal reserve proposal. It also does not pay R_controls for free.

# Sharp grouping diagnostic

For any Boolean core g, let f=1+A_1...A_d(g-1) for disjoint point blocks of positive widths t_j; a_j=2^-t_j, p=product a_j. Apply the source at each separate block. The cumulative reserve on original DATA coordinates is exactly

    R_split,data=2p I(g) sum_j(1-a_j).

Each depth contributes 2p(1-a_j)I(g): its remaining child has data influence product_{k>j}a_k I(g), and its physical reach is product_{k<j}a_k. Treating the union of all controls as ONE point block instead gives R_fold,data=2p(1-p)I(g). Their difference is exactly

    2p I(g)[sum_j(1-a_j)-(1-p)]>=0.

For two blocks this is 2p(1-a1)(1-a2)I(g). For d fair one-bit blocks the split reserve is d p I(g), against terminal capacity p I(g); the folded ratio is 2(1-p). The unbounded ratio diagnoses THIS SUFFICIENT RESERVE, not actual entropy or FEI failure. A025's older repeated-face no-go is not reproved as a new claim; the new use is the exact grouping refund for A023's distinct whole-block capacities. Folding is valid only because every failed branch is the same constant. Three genuinely distinct shared cores lack that simplification.

The original control-coordinate part cannot be discarded either. If e=1-Eg and T_j=sum_{k>j}t_k, its exact split reserve is R_split,control=2p e sum_j(1-a_j)T_j, whereas the folded source reserve has NO control part. For d one-bit blocks this equals p e d(d-1)/2. This is a debit to already-queried future controls, not terminal data slack. The true removed influence is p e sum t_j, the complete terminal accounts are pH(g),pI(g), and folding pays H(f)-pH(g)<=(11/2)p e sum t_j+2p(1-p)I(g). The exact refund contains BOTH the data redundancy and all of R_split,control. Hence grouping repairs this sufficient ledger without erasing the actual terminal entropy or modifying any physical tree. Width grouping is a proof-account change on the SAME leaf partition.

# Independent source reconstruction

For one point block alpha=2^-s, gamma=P(G!=H), the empty residual-control row has derivative mass rho^2 gamma and total row mass<=1. Binary entropy remainder plus log-sum bounds its erasure by rho^2 gamma[log2(1/(rho^2 gamma))+c], c=1/ln2. Other rows contribute exactly2(1-rho)rho gamma. Physical weight times rho gamma equals2alpha gamma. The sums sum rho=2(1-alpha), sum l rho=2[1-(s+1)alpha] give E_B<=2(1-2alpha)I_S+4alpha gamma(1-alpha)[log2(1/gamma)+c]. Edge isoperimetry converts gamma log2(1/gamma) to I(GH)/2, yielding R=2alpha(1-alpha)I(GH). JS<=2c I_S supplies A_s=2(1-2alpha)+2c+2c(1-alpha)/s<11/2. Without JS b_s<5/2; minority J<=B, mu<=d supplies full rate<7. Rational c<81/56, finite s<=5 and elementary tails establish all widths. Product pivotal XOR proves per-coordinate owner fractions. This independently reconstructs the arbitrary-shared-data whole-block erasure/entropy/minority payment and certified-child-rate clauses. The proof uses no prior FEI certificate on an arbitrary core.
