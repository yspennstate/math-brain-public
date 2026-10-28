# The physical-query term is part of the original account

A094's accounting objection holds at its stated scope. It refutes an identification in A011 v5 equation (6), not the numerical terminal-functional inequality or FEI. All costs below are in bits.

For a fixed Boolean target on a finite physical query tree, write P_v for its true spectrum, Q_v for its current finite-cost covering subprobability reference, and w_v for the actual reach. Define D(P||Q)=CE(P,Q)-H(P), including the reference mass penalty. If a query inherits Q_vb^inh and then resets to R_vb, set

    delta_v = w_v [D(P_v||Q_v)-mean_b D(P_vb||Q_vb^inh)],
    e_vb = (w_v/2)[CE(P_vb,R_vb)-CE(P_vb,Q_vb^inh)].

Resetting the same target changes CE and D by the same amount. Substitution and finite telescoping of D, with w_child=w_parent/2, give

    CE_root + sum e_vb = H_root + sum delta_v + sum_leaf w_v D(P_v||R_v).

This includes both children at every branch. It requires no entropy monotonicity or exchange of limits. It remains valid for nonconstant stopping leaves and subprobabilities. A target-changing edit is a separate transaction; this identity never identifies it with a same-target reset.

For the actual mass-preserving inheritance in A011, let m=M_i P, r=M_i Q and s=sum Q>0. On occupied fibers raw_b=r P_b/m; on true-zero fibers raw_b=r. Then mean raw=r and mean Z=s, where Z_b=sum raw_b. Each Z_b>0 follows from finite CE and normalized P_b. Inherit Q_b=s raw_b/Z_b. Direct expansion gives

    mean D(P_b||Q_b)=D(m||r)+mean log2(Z_b/s).

Consequently delta_v/w_v equals the conditional KL loss D(P||Q)-D(m||r), plus -mean log2(Z_b/s). The first is nonnegative by the normalized KL chain rule (the same mass s cancels); the second is nonnegative by log concavity and mean Z=s. There is no cancellation of an unknown-sign entropy decrement. Z_b may individually exceed s; only its average is fixed.

In A011's allowed M=1, a=1, b>=12, r_1=1 construction take g(x)=(-1)^x with exact source reference P_g, c=C0=0. Put epsilon=2^(-1-b), with one new fair control w. Flip g only at x=padding=w=0. For the data frequency with original coefficient A, the full parent has coefficients A-epsilon and -epsilon on its two w labels. Thus its data marginal is q(A)=(A-epsilon)^2+epsilon^2. The first prescribed data floor is R(A)=(A^2+3epsilon^2)/(1+3epsilon), lifted by the true w kernel: beta=6*(epsilon/2)=3epsilon. There is one A=1 frequency and 1/epsilon-1 A=0 frequencies. Exposing w gives the clean child A^2 and edited child (A-2epsilon)^2.

The clean normalizer is exactly

    Zc=(1+3epsilon^2)/[(1+3epsilon)(1-2epsilon+2epsilon^2)], Ze=2-Zc.

The positive denominator minus the numerator is epsilon(1-epsilon)(1-6epsilon)>0 throughout 0<epsilon<=2^-13. Hence 0<Zc<1, Ze>0, and 1-Zc*Ze=(1-Zc)^2>0. The conditional KL loss is zero because the parent reference uses the true selector kernel. Therefore the omitted term is exactly -log2(Zc*Ze)/2>0. This is an actual allowed Boolean witness, including nonconstant source, sufficient padding, finite original reference and both inherited children. At the terminals the prescribed clean model P_g and edited model (P_g+6epsilon Uniform)/(1+6epsilon) are retained. Their actual signed charges satisfy the full identity and cannot remove the discrepancy by redefining a reset.

Checks that could fail: wrong 3epsilon/6epsilon first floor, wrong physical selector reach, discarded true-zero fibers, conditioning a subprobability without its penalty, missing nonconstant terminals, confusing a target edit with a reset, and silently assuming individual normalizers <=1. The checker addresses these by complete finite laws, mass-one and half-mass references, actual Boolean spectra, both children, arbitrary signed resets, constants, matched zero-contraction controls, and a separate literal truth-table implementation of the in-family witness. The rational normalizer product certifies the strict sign without floating entropy subtraction. Finite algebra and the displayed factorization give the all-tree and all-b scopes; the finite checks do not stand in for those arguments.

The original A094 statement and hypotheses are unchanged. No substantive repair is supplied. Its first unsupported universal step remains an upper bound on accumulated physical-query contractions from the SAME unused original bank under every claimed compatible policy, or an explicit restriction to the terminal functional. A positive omitted term alone does not show that A011's numerical reserve fails. Initial influence-priced references and full FEI remain open. This is an analytic reconstruction with exact finite certificates; formal status is separately recorded in out/LEAN_RECEIPT.json and cannot be inferred from the checker passing.
