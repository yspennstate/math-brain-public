# Same-profile coherent factor refresh is nonpositive

All Fourier entropy and KL units are bits. Full FEI remains OPEN. This is a proof draft pending independent review, with exact checks recorded separately. It does not price an arbitrary-core initial supplier.

## Local statement
Let G(x,z)=epsilon for x=0 and v(z_V)u(z_U) for x=1, epsilon in {+1,-1}. The factors have disjoint coordinates. v is a signed width-w point defect, w>=2, and u is any Boolean spectator. Put mu=E u (absorbing the sign of v into u) and d=2^-w. Let p_v,p_u be their squared spectra. Fix 0<alpha<1. The queried factor reference is q_v(0)=p_v(0), and q_v(T)=(1-alpha)p_v(T)+alpha Var(v)1_full(T) for nonempty T. Let q_u be ANY normalized reference with the SAME support as p_u and q_u(0)=p_u(0). The outer reference R copies the actual two zero-data control masses and puts q_v(T)q_u(U)/4 at both control copies when combined data are nonempty. It is normalized. Characters/constants use matching laws.

Query one bit of v. Transport R by the actual coherent kernel, fair on source-zero rows, and normalize by its OWN outcome probabilities r_y. After EACH physical child reset the queried factor to the SAME alpha full-spike reference on the remaining point factor, exact on constant/character children; keep q_u unchanged and rebuild the outer lift with actual child control masses. Then the physical mean signed reset sigma=mean_y[D(P_y||R_y^new)-D(P_y||R_y^old)] is nonpositive. For w>=3 it is strictly negative, uniformly in mu, epsilon and q_u. No outcome normalizer, erasure term or terminal is omitted.

## Exact compensated identity and spectator cancellation
Write l(T)=q_v(T)/p_v(T), s(U)=q_u(U)/p_u(U), with value1 on zero/zero rows. Then R=P_G l s, including zero data, where both ratios are1. Put B=P_G l and let bars denote erasure of the queried frequency bit. B is normalized, since the target marginal of P_G is (delta_0+p_v)/2 and l(0)=1. The inherited normalized child is P_y s (Bbar/Pbar)/(2r_y); the fresh child is P_y s l_y. Pointwise cancellation gives EXACTLY

    sigma = (1/2) mean_y D(p_vy||q_vy) - D(Pbar||Bbar) + D(fair||r).  (1)

The reference outcome r is also the outcome of Bbar through the coherent kernel. Indeed for U!=0 the kernel depends only on target frequency and child, independent of U and controller sign; summing s(U)p_u(U) gives sum q_u(U)=1-mu^2, the same source total. For U=0, s=1. This argument requires the stated matching-empty hypothesis. Forced-character spectators have p_u(0)=0; the controller-only atoms still use ratio1. Formula(1) is A039's compensated identity specialized to equal old/new alpha, independently reconstructed here.

## Coarsening the erased divergence
Assume w>=3, n=2^(w-1), beta=1-alpha, E=1-4d+8d^2, A=(1+E)/2. Erase controller and spectator frequencies from Pbar and Bbar. Their resulting target-frequency laws are

    target zero: A versus A-2alpha d^2;
    target remaining-full: 4d^2 versus beta*4d^2+alpha*2d(1-d);
    each other nonzero target (n-2 atoms): 4d^2 versus beta*4d^2.

Both laws sum to1. Log-sum gives D(Pbar||Bbar)>=D_coarse. Only the active child has fresh factor KL, so the first term of(1) is one quarter the width-(w-1) factor KL. Its nonfull terms cancel EXACTLY against D_coarse. The difference is

    V = A log2(1-2alpha d^2/A)
        +4d^2 log2(1+alpha d/[alpha+(2-4alpha)d]).             (2)

All denominators are positive, since alpha+(2-4alpha)d=alpha(1-4d)+2d>0. Using ln(1-z)<=-z and ln(1+z)<=z,

    (ln2)V <= -2alpha d^2 +4alpha d^3/[alpha+(2-4alpha)d]
             <= -4alpha^2 d^2/(1+2alpha)
             <= -(4/3)alpha^2 d^2.                         (3)

For the middle inequality, 4d/[alpha+(2-4alpha)d] increases in d, derivative4alpha divided by the positive squared denominator, and at d=1/8 equals2/(1+2alpha). The final inequality uses alpha<1.

## The actual outcome normalizer is smaller than the gap
Let child0 be the inactive constant factor. Its source law is supported only at remaining-target zero. At each such row Bbar=Pbar-alpha d^2 p_u(U), for each controller sign. Thus r_0=(1-eta)/2, r_1=(1+eta)/2, where

    eta = alpha d^2 sum_(c,U) p_u(U) P_0(c,0,U)/Pbar(c,0,U),

with zero-row contributions defined0. Since P_0/Pbar<=2 and sum_(c,U)p_u(U)=2,

    0<=eta<=4alpha d^2.

No estimate on the spectator bias is used. Therefore

    (ln2)D(fair||r) = -(1/2)ln(1-eta^2)
        <= eta^2/[2(1-eta^2)]
        <= 8alpha^2 d^4/(1-16alpha^2 d^4)
        <= (32/255)alpha^2 d^2,                             (4)

using d<=1/8, alpha<1, and 1-16d^4>=255/256. Equations(1)-(4) give the quantitative normalized payment

    sigma <= -(308/255)alpha^2 d^2/ln2 <0,  w>=3.             (5)

This deliberately conservative bound retains the NORMALIZED outcome divergence. It is not a raw-L payment or a product-kernel assertion at coherent rows.

## Width two and endpoints
When w=2 both factor children are constant/character and their fresh factor KL is0. The coherent outcome is an actual channel of (Pbar,Bbar), so data processing gives D(fair||r)<=D(Pbar||Bbar). Equation(1) gives sigma<=0. Width1 characters have matching target law, l=1, and zero signed refresh; constants have no essential bit. At alpha=0 the exact law gives sigma=0 (outside the strict theorem but a checked endpoint). Alpha=1 is excluded because domination can fail. Spectator signs, zero bias and constant spectators do not change the argument. References with extra source-zero support are outside the local theorem, not silently deleted.

## Arbitrary finite actual post-a refresh histories and original account
Start with the SAME original Q0, first ACTUAL strong reset sigma1, and omega<=1/4 of A036-PAID-CORRELATED-MIXED-RESET@1: h is a tensor of m width-r>=2 point defects, Q0 factor alpha0=1/8, root margin M0>1+2t+3m*d0/10, and first reset alpha=1/6 at selected complete a-pairs after b and any allowed adaptive data prefix, sigma1<11m*d0/40. Retain untouched b0 and all complementary terminals. In any already reset a child, execute arbitrary finite adaptive data queries, refreshing ONLY the queried factor after BOTH children at the SAME alpha1/6. All other paid factor references are unchanged. Each step restores the outer-lift invariant. Formula(5) and the width-two argument imply the cumulative physically weighted sigma_later<=0; this remains true with different stopping policies in the two a signs. The analogous post-x invariant is A047's existing theorem, independently separated from this new coherent extension.

Every remaining point-tensor restriction has H<=4I. For J_epsilon(g), 4I-H>=-2epsilon E g+(4I(g)-H(g))/2. Within each complete finite sign-conditioned physical data partition E(Eg_leaf)=Eg_initial. Averaging the BOTH retained a signs cancels the signed bias, even under divergent query/stopping policies. The b0 terminal contributes1 globally, so the full terminal surplus S=E(4I-H)>=1. No claim of nonnegative individual activation surplus is used.

With ALL terminal references, e=H0-Hf-4(I0-If), and A0=D(P0||Q0), the exact signed recovery is

    S-[A0+e+sigma1+sigma_later]_+
       =min(S,M0-sigma1-sigma_later)>=1.

Subtract the SAME booked omega once: at least3/4 remains. The first actual reset, original source and every later outcome/erasure/terminal KL remain booked. No child account, variance reserve or query credit is renewed. This closes arbitrary finite ACTUAL same-profile factor-refresh histories after a exposure, extending the one-query mixed-reset payment. It does not prove a no-intermediate-reset terminal refresh has the same sign, nor allow changed alpha or simultaneous arbitrary factor replacement for free.

## First unsupported line
An influence-priced complete correlated reference for arbitrary Boolean cores remains unavailable. Also unproved here is nonpositive full-profile terminal refresh after an unrefreshed multi-query gap or a change of profile alpha; these cannot be inferred from the invariant under actual intermediate resets. General Boolean hereditary reference construction and its cumulative payment remain the universal bridge. The universal FEI constant improves by zero.

## Adversarial boundary control
For an actual width3 point target times one character spectator, epsilon=+1, alpha=1/6, change ONLY the old spike from full to the queried singleton. The active core inherited law is(11/36,25/108,25/108,25/108) and the fresh remaining-full law is(1/4,5/24,5/24,1/3). The core active reset is log2(6875/6561)/4. The activation outcomes, however, are21/40 and19/40; therefore its actual paired reset is

    sigma_control=(1/16)log2[(6875/6561)*(99/100)^4*(400/399)^8]>0.

Strict positivity is the rational inequality that the bracket exceeds1. This breaks the prescribed OLD full-spike hypothesis, and is not a counterexample to the theorem or FEI. Our initial control predicted half of the core paired reset without its changed outcome divergence; its exact-expression comparison failed. CONTROL_INITIAL_FAILURE records that error and the corrected expression before replay. The main proof already retained this outcome term throughout.
