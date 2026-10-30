# The first annihilated spike that still needs a positive floor

All logarithms are base two. The functions are Boolean signs on uniform bit cubes. A character includes either sign of any coordinate product, including constants. This certificate concerns a prescribed reference rule. Full FEI remains open.

## 1. Four variables, no tunable circuit parameter

For bits a,x,y,z let chi_T=(-1) raised to the sum of the bits in T. Put

    m(x,y,z) = chi_x if z=0, and chi_y if z=1,
    p(x,y,z) = chi_xyz,
    f(a,x,y,z) = m if a=0, and p if a=1.

The three residual coordinates are essential in BOTH children. All four coordinates are essential in f. Both children and the parent have signed mean zero. Their exact expansions are

    m = (chi_x + chi_y + chi_xz - chi_yz)/2,
    f = (m+p)/2 + chi_a (m-p)/2.

Thus P_f has eight atoms of mass 1/16, indexed by T and aT for T=x,y,xz,yz, and two atoms of mass 1/4, indexed by xyz and axyz. In particular, the parent full atom is occupied. H(f)=3, Inf_a=1/2, I(m)=3/2, I(p)=3, and I(f)=11/4. The complete truth table and signed Walsh numerators are saved in out/CHECK.json, with a the least significant input bit.

For arbitrary 0<alpha<1 supply Q_alpha=(1-alpha)P_f+alpha delta_axyz. This is exactly the matching-empty full-spike reference, since P_f(empty)=0. It is support matched at the parent. Erasing a gives average child spectrum R=(P_m+P_p)/2. At the erased full mask xyz, R=1/2, P_m=0 and P_p=1. The coherent kernel therefore sends the entire spike to outcome a=1. Actual reference outcome probabilities are

    r_0=(1-alpha)/2, r_1=(1+alpha)/2.

After normalization BOTH child references equal their actual spectra: on a=0 only the ordinary mixture survives, and on a=1 both ordinary mass and spike sit at the single parity atom. In A046's language the inherited cap is zero on the multiplexer child. No vacuum calibration, discarded ghost, or sign choice is needed.

Require any new positive tilt 0<gamma<1 at the actual essential residual mask xyz. The multiplexer has no Fourier mass at xyz. Hence

    D(P_m || (1-gamma)P_m+gamma delta_xyz) = -log2(1-gamma)>0.

This includes its new source-zero reference atom. The parity child has zero conversion for every tilt, so the complete paired fresh-minus-inherited price is -log2(1-gamma)/2. All old source, erasure, outcome, terminal and conversion terms remain payable in their respective accounts. This proves the sharp failure of a FREE positive floor at the inherited zero cap, even with balanced children and stable essential masks. It does not contradict A050's fixed-profile iff, whose positive-child-full-mass hypothesis fails here.

## 2. One exact sign comparison

Set alpha=gamma=1/2 solely to obtain a parameter-free certificate. Q_alpha assigns 5/8 to axyz, 1/8 to xyz, and 1/32 to each other occupied parent atom. Therefore

    K_root = D(P_f||Q_alpha)=1-log2(5)/4,
    O_root = D(fair||(1/4,3/4))=1-log2(3)/2,
    D_erase=K_root-O_root=log2(9/5)/4,
    inherited child KLs=0,
    paired fresh child KL=1/2.

Positivity of K_root is exactly 16>5. The strict comparison paired fresh KL>K_root is exactly 5>4. The additional paired conversion is 1/2 bit; it cannot be charged solely by reusing the already consumed root KL. This is not an insolvency certificate for 4I: H(f)+K_root=4-log2(5)/4<4<11=4I(f), so that larger original account has ample slack. The certificate isolates the required additional invoice; it does not refute its possible payment from legitimate original influence surplus.

## 3. Minimality, with the quantifier stated

The exact mechanism is: the parent full Fourier atom is occupied, a physical singleton query annihilates its erased spike on a child, and that child is noncharacter, so a newly imposed positive essential-mask tilt changes its law. Minimum total input dimension for this mechanism is four. This is NOT a minimum among every possible reference-rule failure or every FEI counterexample.

If the parent has at most three variables, the child has at most two. On at most one variable every Boolean sign is a signed character. On two variables, Walsh sums are even integers. The truth-table signs have either an even number of negatives, giving a signed character, or an odd number, giving four Walsh numerators each equal to plus or minus two. In the latter case all four squared coefficients are 1/4, including the full coefficient. Consequently a noncharacter child on at most two variables never has zero full coefficient. Since an occupied parent full atom gives a strictly positive erased full mass, zero spike transmission is equivalent to zero child full mass. This excludes the mechanism below dimension four. The explicit balanced stable-mask example attains four. The checker independently enumerates every table and all singleton outcomes below four, without quotienting by symmetry.

## 4. Independent review of A050: inherited witnesses and the original KL account

Reviewed source: A050-FIXED-PROFILE-ZERO-COST-REPAIR@1, statement hash 740215f9dc8b09fe147531f1d0ad038fd47beb84b1d6c7508d7361948790f8c4, in A050 run 20261023T132645Z-fleet03-A050-repair-with-scope. Verdict: HOLDS at its printed hypotheses, without repair.

First reconstruct its hereditary part directly from the full joint law. Write Q=bP+sum_j c_j delta_Wj with b>0, nonnegative coefficients summing to one, and positive witness atoms in supp(P). Under erasure E and source coherent kernel K_t(U)=P_t(U)/(2EP(U)), EQ transported to outcome t is b P_t/2+sum_j c_j K_t(EW_j)delta_EW_j. Its mass r_t is at least b/2; division gives b_t=b/(2r_t), c_tj=c_j K_t(EW_j)/r_t. The coefficients sum to one and any positive child witness is in supp(P_t). A zero-weight witness can be omitted; its kernel never needs evaluation. This is the exact side condition that exposed the first checker bug, rather than an error in A050's theorem.

The source joint law has fair physical outcome. Relative entropy of source versus reference joint law is both D(EP||EQ) (same conditional kernel) and O+(D(P_0||Q_0)+D(P_1||Q_1))/2. Data processing gives D(P||Q)-D(EP||EQ)>=0. Combining proves A050's one-node identity; finite-tree weighted telescoping proves its complete sum of reached erasure KL, outcome KL and full terminal KL equals the ORIGINAL root KL. Nonnegativity follows from Gibbs/log-sum. No optional-stopping limit is used. The coefficient envelope follows from Q>=bP and the average identity log(1/b_child)=log(1/b)-O. It is an EXPECTED, reach-weighted account, not pathwise fresh capital. This resolves the prior A049 next step for the altered inherited interface, conditional on its initial supplier.

For the fixed-profile equal-mean part, let E=(t0+t1)/2, c=alpha(1-mu^2)>0 and beta=1-alpha>0. Direct full-row comparison gives r_t=1/2+(c/2)(t_t/E-1) and sigma=O+(F(t0)+F(t1))/2-F(E), F(t)=t log2(t/(beta*t+c)). Differentiating twice gives F''=c^2/(ln(2)*t*(beta*t+c)^2)>0 on positive child full masses. The denominators are nonzero on the entire stated range. Strict convexity and O>=0 show sigma<=0 iff t0=t1; substitution then gives fair r and equality of inherited/fresh laws atom by atom. The activation halves the Jensen term and has its own r, as A050 states. The translation example has opposite full coefficients and equal squares, so it satisfies the occupied-parent condition; a generic isospectral pair need not.

Finally the printed signed reserve formula is elementary but exact: M0=4I0-H0-A0 and e=H0-EH-4(I0-EI) imply A0+e=S-M0, S=E(4I-H). Thus S-[A0+e]_+=min(S,M0). A previously supplied conversion sum subtracts from M0 and an old booking subtracts from both alternatives. No terminal surplus or original cross-entropy bound is inferred from reference transport.

## 5. Validation and remaining line

Frozen specification precedes execution. The corrected checker uses direct integer Walsh sums and Fraction arithmetic; KL identities are exact prime-log coefficient equalities, not floating-point cancellation. The critical witness also has a separate FWHT spectrum check. Complete smaller-dimensional census and all eligible coordinate-order trees pass. An arbitrary adaptive policy is covered by the node identity and finite induction, not by claiming the fixed-order census enumerates every adaptive tree. Half-tilt signs reduce to exact integer comparisons. The first run's zero-weight-witness KeyError is preserved in out/FIRST_CHECK_FAILURE.json. It is fixed before the passing run. Lean admission is HELD below its 5500 MB availability floor: no compiler ran, so the rung is analytic proof plus exact finite certificates, independently reconstructed for A050, and externally unreviewed for the new extraction.

The first unsupported universal line remains an influence-priced ORIGINAL arbitrary-core complete source and a useful physical stopping policy with sufficient complete terminal surplus. A mandatory profile must first be justified; its actual additional floor invoice can then be compared with the SAME remaining original surplus. This four-variable certificate tells that comparison exactly what it must retain.
