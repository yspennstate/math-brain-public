# Sharp signed-reference projection and the influence compensator

All information quantities use base two; ln is natural log. Put a=log2(e)=1/ln2<3/2. The last inequality follows from ln2=2 sum_(j>=0)(1/3)^(2j+1)/(2j+1)>2/3. Incoming KL and full terminal entropy remain in the account. This is an additional-reserve theorem, not FEI.

## 1. General projection, with no small-marginal cutoff

Let p be any law on subsets of [m], with actual marginals 0<d_j<1, I=sum_j d_j, product q, and empty masses q0<=p0<1. Supply a normalized reference R supporting p, with arbitrary supporting empty mass r<1 and conditional nonempty law

    Q_lambda(S)=lambda^|S| q(S)/Z_lambda,
    Z_lambda=sum_(T nonempty)lambda^|T|q(T), 0<lambda<=1.

Then TC=KL(p||q) and K=KL(p||R) satisfy

    [TC-K]_+ <= binaryKL(p0||q0) <= a I.                 (1)

Proof: P=p(.|nonempty) has rank mean I/(1-p0). Direct differentiation of finite positive sums gives

    d KL(P||Q_lambda)/d ln(lambda)
        =(E_Qlambda |S|-I/(1-p0))/ln2,
    d E_Qlambda |S|/d ln(lambda)=Var_Qlambda(|S|)>=0.

At lambda1 the reference rank mean is I/(1-q0)<=I/(1-p0). Thus KL(P||Q_lambda)>=KL(P||Q1). The exact conditional KL decompositions are

    K=binaryKL(p0||r)+(1-p0)KL(P||Q_lambda),
    TC=binaryKL(p0||q0)+(1-p0)KL(P||Q1).

Discard only the nonnegative binary term in K. Since p0>=q0, the second summand of binaryKL(p0||q0) is nonpositive. Also p0 log2(p0)<=0. Hence

    binaryKL(p0||q0) <= -p0 log2(q0)
      =sum_j p0[-log2(1-d_j)]
      <=sum_j (1-d_j)[-log2(1-d_j)] <= a sum_j d_j.

The penultimate inequality uses the actual marginal relation p0<=1-d_j; the last uses -(1-x)ln(1-x)<=x, obtained by integrating 1/(1-x). This proves (1). Every normalizer is positive; no infinite-sum or limit exchange is used here. Neither p nor R is assumed to be a product law.

## 2. Exact finite-tree optional stopping and the original owner

At a Boolean restriction node let p be its squared Fourier law, R a normalized supporting inherited reference, and K=KL(p||R). Query coordinate i; erase its spectral indicator to obtain q=p^-i and Rbar=R^-i. On q(T)>0 use the physical kernel k_b(T)=p_child_b(T)/(2q(T)); on source-zero rows choose any normalized kernel and use the SAME choice in the reference. Write pi_b=sum_T Rbar(T)k_b(T) and R_child_b=Rbar*k_b/pi_b. Source support and the nonzero normalized child law imply pi_b>0. The source physical marginal is fair.

The KL of the source/reference joint laws after the common kernel equals KL(q||Rbar). Decomposing by the physical marginal gives exactly

    K_parent=E_i+O_i+mean K_child,
    E_i=K_parent-KL(q||Rbar)>=0,
    O_i=KL(fair||pi)>=0.                               (2)

The inequality for E_i is the conditional KL chain under erasure. The Boolean influence identity is

    I_parent=Inf_i+mean I_child.                       (3)

Indeed ((u+v)^2+(u-v)^2)/2=u^2+v^2 for each restricted Fourier pair; summing the spectator weights gives (3), with the missing queried indicator contributing Inf_i. Thus current influence plus prior queried influences is a martingale.

Assume TC<=K+aI at every node where terminal conversion is permitted. Set P=K+aI. Equations (2)-(3) imply

    P_parent-mean P_child=E_i+O_i+a Inf_i.              (4)

Stopping without conversion has terminal target T=K. Terminal conversion ONCE to the actual marginal product has target T=TC. Both targets are <=P. Summing (4) over a finite adaptively queried tree, with actual physical reaches, yields

    E T_terminal + E sum_before_stop O_i
       + a E sum_before_stop Inf_i <= K_initial+a I_initial. (5)

Retaining E_i on the left also gives a valid stronger inequality. Adding E H(p_terminal) to BOTH sides retains the complete terminal cross entropy. This entropy is not paid by the additional reserve.

Subtracting (2) from the Bellman inequality that also pays O_i gives the exact least pending additional reserve

    B=max(0, TC-K if conversion admitted,
                  max_i(mean B_child-E_i)).            (6)

For a fixed subtree restrict the maximization accordingly. Backward induction proves B<=aI: conversion uses (1), continuation uses mean B_child-E_i<=a mean I_child<=aI. Formula (6) does not spend O_i twice. The owner is ONE original aI_initial, or the larger rational cap 3I_initial/2. Influence already charged at ancestors stays spent. Pending theta for a nested subclass may be topped up only by cap-theta, with 0<=theta<=cap; unrelated spent omega cannot be relabeled theta. Original owner availability and separately booked K_initial are hypotheses. No fresh descendant prior supplies money.

## 3. Randomization and the distinct unbounded-depth extension

A restriction process in n fixed coordinates has at most n real reveals. Condition on independent policy randomness; each resulting eligible finite tree satisfies (5). Integrating proves randomized stopping. If initial data also depend on that randomness, assume the initial nonnegative account is integrable and integrate it as well. No UI or unbounded-depth assertion is needed for this actual finite-cube theorem.

Separately, suppose a countable locally finite tree has finite nonnegative P, nonnegative edge/node costs c_i=O_i+aInf_i, and mean P_child+c_i<=P_parent at each continuation. Suppose tau is almost surely finite, its nonnegative terminal target satisfies T_tau<=P_tau, and E P_initial<infinity. Apply finite stopping to tau wedge N, retaining P_N on paths not yet stopped. The resulting nonnegative random variable Y_N is accumulated costs through tau wedge N plus T_tau on stopped paths or P_N otherwise, and E Y_N<=E P_initial. On every path with tau finite, Y_N eventually equals sum_(i<tau)c_i+T_tau. Fatou proves the same bound at tau. No UI, exchange of expectation and limit, or across-dimension reference convergence is asserted. If tau=infinity with positive probability, an explicit liminf terminal domination is required; this case is not silently admitted. This extension is conditional on the stated tree data, not a construction of such data for FEI.

## 4. Actual invariant at all dimensions: point defects

For g_n=1-2*1[x=0], n>=2, put d_n=2^(1-n). Direct Fourier expansion gives

    p_n(empty)=(1-d_n)^2, p_n(S)=d_n^2 for S nonempty,
    Inf_j=d_n, I=n d_n.

Supply ONE original reference with arbitrary empty mass in (0,1) and conditional nonempty Bernoulli(delta)^n law, conditioned nonempty, with 0<delta<=d_n. Transport it by (2), without intermediate resets.

At an active node with remaining m>=2, d=d_m, its reference has shape

    R(empty)=r,
    R(S nonempty)=c delta^|S|(1-delta)^(m-|S|),
    c=(1-r)/(1-(1-delta)^m)>0.

For a nonempty erased spectator T the two source amplitudes are -d,-d, so the active physical child has kernel probability1 there and the constant child0. At empty spectator the active kernel probability is

    alpha=(1-2d)^2/[2((1-d)^2+d^2)].

The erased reference empty mass is R0=r+c delta(1-delta)^(m-1); nonempty coefficients keep delta. Predicted active reach pi=1-(1-alpha)R0 is positive, as is the constant reach. Normalization gives r_child=alpha R0/pi and c_child=c/pi. Therefore delta stays fixed on every active history. The other child is constant with reference concentrated at empty and K=TC=I=0. At m2, alpha0 gives a dictator child with zero empty source and reference mass. At m1 both children are constants. No zero source mass is divided away; no nonconstant point node has reference-only erased zero-source rows. Constant nodes stop.

At active m>=3, p0=(1-d_m)^2>=q0=(1-d_m)^m and the nonempty reference has common attenuation

    lambda=[delta/(1-delta)]/[d_m/(1-d_m)]<=1.

Thus (1) applies. At m<=2, TC=0 directly. Permutation invariance on remaining coordinates covers every adaptive query choice, not only a fixed order. Consequently (5)-(6), with B<=aI, hold for every n, eligible original reference, adaptive randomized stopping policy and either terminal choice. No tensor reference transport assertion is used. Dimensions0,1 may be included directly as zero-TC endpoints.

## 5. Sharp coefficient, with the limit justified

At a root choose delta=d_n and r=p0=(1-d_n)^2. The conditional laws agree at lambda1, and the discarded binary empty-tilt KL vanishes, so TC-K=binaryKL(p0||q0), q0=(1-d_n)^n. Put d=d_n and mu=2d-d^2. The first binary term divided by I=n d is

    ((n-2)/n)(1-d)^2[-log2(1-d)/d],

which tends to a, since a<=-log2(1-d)/d<=a/(1-d). The other term is mu log2(mu/(1-q0))/(n d). For n>=2, mu<=1-q0, mu>=d and 1-q0<=n d. Hence this term lies in [-2log2(n)/n,0] and tends to zero. Thus (TC-K)/I tends to a. Since B>=TC-K and B<=aI, B/I also tends to a. No smaller universal coefficient is possible for this eligible additional-reserve theorem. This is a finite-parameter squeeze, not a stopping-limit exchange.

## 6. Essential hypothesis and first universal unpaid line

If R=p_n, K=0, but its conditional nonempty shape has delta=1/2>d_n at n>=3. Immediate product conversion costs TC and TC/I diverges. Specifically M/I>=n-1, while H<(4n-1)d follows from the exact point spectrum, -ln(1-d)<=d/(1-d) and a<3/2. Thus TC/I>n-5+1/n, exceeding3/2 already at n8. This disproves an unconditional additional-reset cap, not FEI. Validation includes the exact atom identity R=p8 and a rigorous positive TC-3I/2 bound.

The general lemma covers unequal marginals and nonuniform laws; it does not claim a mixed physical query preserves p0>=q0 or common attenuation. Unequal-width products of point cores and parity shifts below are root fixtures, not an all-history theorem. At an eligible product root K_initial=TC may itself greatly exceed I. Initial reference admission, complete terminal entropy, repeated conversions, and eligibility lost after mixed queries remain unpaid. The next target keeps one original reference and every ancestor debit across one unequal-row query and asks whether the eligibility defect is paid by that same unused owner. A descendant reference renewal is not licensed.
