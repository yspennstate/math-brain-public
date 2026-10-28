# Positive posterior credits fail on a rare-query, same-support Boolean family

All logarithms are base2; inputs are uniform physical bits, equivalent to uniform signs. Full FEI remains OPEN. This stage consumes A047's already proved finite nonpoint obstruction; it does not repeat the cancelled three-bit census. The new feature is an all-dimensional, exponentially diverging actual reset/influence ratio with an explicitly paid ORIGINAL source transaction.

## 1. Actual Boolean family and complete references

For r>=3 put d=2^-r and let a=e0+e1 in the r-bit private cube. On bits (j,z,w), define

    v_r(j,z,w)=(-1)^z [1-2*1{w=0 OR (j=1 AND w=a)}].

Thus v_0 is a character times a single rare point defect, and v_1 is the same character times a two-point defect at0,a. The two private points have the SAME parity. Both child means, and the parent mean, are zero. Direct physical edges give

    Inf_j(v_r)=d, Inf_z(v_r)=1,
    Inf_wk(v_r)=3d for every k,
    I(v_r)=1+(3r+1)d;
    I(v_0)=1+2rd, I(v_1)=1+4rd.                         (1)

Let G_epsilon(x,j,z,w)=epsilon at x0 and v_r at x1. Its j influence is d/2, H(G)=2+H(v_r)/2, and I(G)=1+(3r+1)d/2. Both signs have the same spectral masses and influence values, but both physical signs/outcomes are retained when embedded below.

For any balanced core p use the SAME-alpha full-block spike

    q_alpha=(1-alpha)p+alpha delta_full, 0<alpha<1.

Lift it into G by copying the two actual zero-data controller masses and putting q_alpha(T)/4 on each of the two nonempty-data control copies. Every parent and child full coefficient is NONZERO, so these references have exactly the source supports. Constants/characters use exact laws, although no such endpoint occurs here for r>=3. No positive reference-only row is removed.

We query the rare physical j bit. Reference transport always erases j, applies the actual common physical kernel, and normalizes by the reference's OWN outcome probability. Fresh children use the SAME alpha and their remaining-full spike; this is not a declared profile change.

## 2. Spectrum, normalized outcomes and exact reset cost

At private full frequency the child amplitudes are -2d,-4d; hence the parent non-j and j amplitudes are -3d,+d. Their paired erased mass is10d^2 and the physical outcome kernel there is(1/5,4/5). All of the spike alpha is in the parent j-containing full coefficient. Other reference mass follows the actual source, while the controller-only half stays exact and splits fairly. Therefore the ACTUAL reference outcomes are exactly

    r_0=1/2-3alpha/20, r_1=1/2+3alpha/20,
    kappa_alpha=D(fair||r)=-log2(1-9alpha^2/100)/2>0.     (2)

Write beta=1-alpha and

    f_alpha(m)=(1-m)log2(1/beta)
                 +m log2(m/(alpha+beta*m)).

This is D(p||(1-alpha)p+alpha delta_full) whenever the actual full mass is m. The three needed full masses are4d^2,16d^2 in the children and10d^2 in the erased source. All selectors have zero core mean. The full compensated KL identity, with its OWN outcome normalizers, gives the exact physical mean fresh-minus-inherited reset bill

    sigma_r = kappa_alpha
                +[f_alpha(4d^2)+f_alpha(16d^2)-2f_alpha(10d^2)]/4.   (3)

The second derivative is f_alpha''(m)=alpha^2/[m(alpha+beta*m)^2 ln2]>0. Since10=(4+16)/2, the second term is strictly positive. Thus sigma_r>kappa_alpha for ALL r>=3 and ALL0<alpha<1, under exactly matching old/fresh source support. At alpha1/6, the outcomes are19/40,21/40 and

    kappa=log2(400/399)/2>1/600,
    sigma_r/Inf_j(G)>2^r/300.                           (4)

The strict rational sign is400^300>2*399^300. No dimension-independent K can make sigma_i<=K Inf_i for this actual full-spike hereditary rule. This does NOT refute A036's point-factor theorem: v_r is not a signed point factor.

For fixed alpha, expansion of f_alpha(m)=log2(1/beta)+m log2(beta*m/alpha)+O_alpha(m^2) in (3) gives

    sigma_r=kappa_alpha+c*4^-r+O_alpha(16^-r),
    c=18-5log2(10)>0.                                  (5)

The m log d terms cancel exactly. The remaining log(1+beta*m/alpha) has remainder bounded by a constant times m^2, e.g. ln(1+t)<=t; thus (5) is an analytic asymptotic, not a floating fit.

## 3. Every declared posterior credit is positive and asymptotically insufficient

Here 'declared credits' means the following FIVE specified KL-type quantities. We do not assert that EVERY imaginable reference KL is small: the outcome KL in (2) is a nonvanishing COST and is explicitly retained.

Let E_r be the conditional ERASURE KL lost when j is erased from the actual G law/reference, J_r the spectral Jensen-Shannon divergence of the two physical child spectra, P_r=I(S_j;S_rest) the posterior mutual information in G's actual squared spectrum, Gamma_r the sum of Bernoulli-marginal Jensen-Shannon credits for the OTHER influences, and TC_r=D(P_G||product of actual spectral marginals). All five are strictly positive for every r>=3. Their exact leading orders, with d=2^-r, are

    E_r = 9r d^2+O(d^2),
    J_r = (1+c)d/2+O(d^2),
    P_r = rd/2+O(d),
    Gamma_r = g*rd+O(rd^2), g=1-(3/2)log2(3/2)>0,
    TC_r = (3/2)r^2 d+O(rd).                           (6)

Consequently division by sigma_r tends to zero with the exact leading coefficients9/kappa, (1+c)/(2kappa),1/(2kappa),g/kappa,3/(2kappa) respectively. Division by retained entropy H(G)->2 also tends to zero, with the same numerators divided by2 instead of kappa. Thus positivity of all five credits supplies no fixed multiple that pays either this retained entropy or this actual reset bill. This is a quantitative insufficiency statement, not KL nonnegativity.

Here are explicit formulas and derivations for (6). Put phi(t)=-t log2 t, n=2^(r-1). The parent has one principal mass(1-3d)^2, n-1 masses9d^2 and3n masses d^2. The children have principal masses(1-2d)^2,(1-4d)^2 and respectively2^r-1 masses4d^2,n-1 masses16d^2. The erased law has principal mass1-6d+10d^2, n-1 masses10d^2 and n masses2d^2. All listed masses are on frequencies containing z; zero coefficients stay zero.

E_r=[f_alpha(d^2)-f_alpha(10d^2)]/2, proving its first expansion; f_alpha is strictly decreasing, so E_r>0. J_r=[H(erased)-[H(v_0)+H(v_1)]/2]/2. The even nonprincipal classes contribute c*d/2+O(d^2), odd classes contribute d/2, and the principal class is O(d^2). Distinct child distributions give J_r>0.

The actual erasure entropy is B_r=[H(v_r)-H(erased)]/2=O(d). Hence P_r=h2(d/2)-B_r=rd/2+O(d). Conditional j probabilities include1/2 on odd classes and1/10 on even classes, distinct from the unconditional d/2, so P_r>0. The x,z influence marginals are the same in both children; each private marginal is d versus2d. Therefore Gamma_r=r*[h2(3d/2)-(h2(d)+h2(2d))/2], proving its expansion and strict positivity by strict concavity. Finally

    TC_r=h2(d/2)+r*h2(3d/2)-H(v_r)/2.

The parent entropy is12rd+O(d), giving its leading term. TC_r>0 because the actual joint spectrum is not the product: it has source-zero atoms while all actual marginal influences are strictly between0 and1. Entropy expansions use phi(1-t)=t log2(e)+O(t^2) and the exact finite mass classes; all claims in (6) follow with explicit O bounds from the convergent log(1-t) series.

The direct edges and masses imply H(v_r)=O(rd), I(v_r)->1, so

    H(G_epsilon)/I(G_epsilon)->2.                      (7)

This is a reference-payment counterfamily, not an FEI counterexample.

## 4. The SAME original admitted nonpoint source pays the actual positive bill

Embed v_r in the ORIGINAL priority family F(x,a,b,zdata)=chi_a on x0, v_r on x=b=1, and+1 otherwise. Use the normalized ORIGINAL seven-eighths correlated lift Q0 (alpha0=1/8), copying all six actual controller atoms and assigning q_core(T)/16 to its four nonempty-data copies. This supplies a concrete initial nonpoint reference, not a free conversion from a previously booked Q. Keep one eligible old booking0<=omega<=1/4.

Query b, retain b0, query a in b1 and retain BOTH a signs. ACTUALLY reset both to alpha1/6 coherent lifts, booking the full signed sigma1. Then query rare j in each a-child, retaining both outcomes, and ACTUALLY reset each to SAME-alpha1/6 full-spike law. Let sigma2 be the COMPLETE global second bill. The b/a references have fair own outcome laws and their inherited core reference is exactly the ORIGINAL alpha0 lift, as follows directly from the sector rows. Thus

    A0=f_alpha0(d^2)/4,
    sigma1=[f_alpha1(d^2)-f_alpha0(d^2)]/4>0,
    sigma2=sigma_r/2>kappa/2.                          (8)

The original rare-j influence is d/4, so sigma2/Inf_j(F)>2^r/300 as well. No query allowance is renewed.

For r>=8 we can certify this full transaction analytically. Every parent/child core has its principal spectral mass at least1-8d, with support size at most2^(r+1). Using h2(t)<=t[log2(1/t)+log2(e)] and log2(e)<3/2 gives

    H(v_r), H(v_0), H(v_1)
        <=8d(2r-1/2)<=31/64<1/2.                     (9)

The last expression decreases for integers r>=8; at8 it is31/64. No small-case extrapolation is used. All these cores have influence>=1 by the z bit.

For the original priority root, I0>=3/2, H0<=3+1/8=25/8, and A0<=log2(8/7)/4<1/20 using8^5<2*7^5. Hence original inclusive margin M0=4I0-H0-A0>113/40. Each reset generation's complete positive upper bound is its FRESH full KL: sigma1<=log2(6/5)/4 and sigma2<=log2(6/5)/4. These are UPPER bounds on the signed actual costs in(8), not extra payments. The integer sign6^40<2^11*5^40 gives

    M0-sigma1-sigma2>43/16.

Every final a/j child has I>=1,H<9/4, and so surplus>7/4. The untouched b0 has surplus2 and reach1/2. The COMPLETE final surplus S=E(4I-H)>=15/8. Keeping ALL original/query/outcome/erasure/terminal KL and e=H0-Hf-4(I0-If), exact signed recovery gives

    S-[A0+e+sigma1+sigma2]_+-omega
       =min(S,M0-sigma1-sigma2)-omega >=13/8.          (10)

This proves actual source admission and payment for EVERY r>=8, with the old quarter and BOTH complete terminal subtrees. The local influence payment fails exponentially although the actual ancestor account pays. No arbitrary incoming source, extra old debit or repeated reset series is admitted.

## 5. Source intake and first unsupported universal line

A036's point-specific negative refresh and A037's monotone point-profile ledger already settle the point history mechanism at their stated scope. A047's three-bit same-support obstruction already disproves nonpositive arbitrary-Boolean refresh; its source formulas are reconstructed separately in REVIEW_A047.md. The abandoned initial three-bit census was frozen but NEVER executed. The new family here addresses A048's next sigma<=K_alpha Inf query and A047's SAME-unused-original-source payment requirement with an actual growing-dimensional Boolean construction.

The first unsupported universal line is a hereditary reference-payment bound involving a transferable ORIGINAL source or spectral likelihood potential, rather than the current query influence or these five vanishing local credits. The concrete rare-query transaction has a finite ancestor surplus; unlimited repeated nonsummable conversions do not follow. Nor does this special balanced near-character initial price provide a price for arbitrary Boolean cores. NEXT is to carry one further rare physical query/profile change from its actual diminished original owner, or derive a source-likelihood amortization that can control all such events. This targets C024/C019 ownership rather than another isolated H/I estimate. The universal FEI constant improves by zero.
