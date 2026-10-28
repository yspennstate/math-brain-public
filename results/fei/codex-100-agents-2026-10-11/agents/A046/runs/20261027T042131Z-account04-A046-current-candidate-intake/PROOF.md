# Exact spike-floor admission, including prepaid vacuum mismatch

All entropies and relative entropies use base two. Full FEI remains OPEN.

## 1. Frozen target and retired repairs

The live continuation is the supplied-reference C024/C019 potential, not the October 11 tax-free biased uncertainty helper. Current BOARD, A046 stage11, A049 stage21 and A050 stage11 take precedence over the unchanged B10 lead's original review request, which A046 stage2 already completed at its declared scope. Freeze a REQUIRED spike-parameter floor ell, not a required atom mass or a profile-preserving two-cell class. A097's projection does not automatically price this class: changing a spike parameter also changes its within-cell profiles when the spike is occupied.

Retired at their original quantifiers: tax-free J<=M; O(p) singleton tax (AND at q=1/4 needs coefficient at least 1/2); fixed Renyi order below one; raw-L; fixed positive whole-mask reset at every query; larger finite local multiplier for that reset; and treating a bound on entry KL as a bound on complete entry cross entropy. A046 stage10 and A047 stable-mask examples obstruct fixed resets, while A048's cumulative example obstructs mandatory repetition. None disproves FEI. The new computation tests an exact price formula, not a smaller fixed tilt or a larger local constant.

## 2. Exact price on an arbitrary finite incoming law

Let p be a finite probability law, partitioned into a vacuum sector V and a nonempty sector N, with pi=p(N)>0. Let q be normalized and positive wherever p is positive; put rho=q(N)>0. Suppose

    q(.|N)=(1-beta)p(.|N)+beta delta_M,  0<=beta<1,

where M is an atom of N, possibly source-zero. Let E be a declared target atom of N, also possibly source-zero. For 0<=gamma<1 define R_gamma to copy p on V and have conditional nonempty profile

    R_gamma(.|N)=(1-gamma)p(.|N)+gamma delta_E.

Write t_M=p(M)/pi, t_E=p(E)/pi, and

    d_t(u)=(1-t)log(1/(1-u))+t log(t/(t+u(1-t))).

Use 0 log 0=0; explicitly d_0(u)=-log(1-u), d_1(u)=0. Define the COMPLETE vacuum/sector credit

    L = sum_{s in V} p(s)log(p(s)/q(s)) + pi log(pi/rho).

This equals the KL of the coarse law retaining each vacuum atom and merging N; hence L>=0, including pi=1. Direct atomwise expansion proves

    D(p||q)=L+pi*d_tM(beta),
    sigma(gamma)=CE(p,R_gamma)-CE(p,q)
                =pi*(d_tE(gamma)-d_tM(beta))-L.                 (1)

No ghost mass or reference normalizer is discarded. For an activation lift pi=Var(g)/2, V consists of BOTH controller vacuum atoms, and this is exactly the four-scalar interface from A046 stage11. If an old mask strictly contains the new essential mask, t_M=0; E need not be source-zero.

For 0<t<1, differentiation gives

    d'_t(u)=u(1-t)/(ln(2)*(1-u)*(t+u(1-t))).

It is positive for 0<u<1. The t=0 derivative is 1/((1-u)ln(2)); t=1 is constant. All denominators used here are strictly positive on their stated domains. Therefore for the DECLARED class gamma>=ell, 0<=ell<1, the sharp minimum signed price is sigma(ell). It is unique in gamma when t_E<1. At t_E=1 all candidate laws agree. This proves continuum quantifiers, rather than inferring them from a grid.

The exact free-floor criterion is

    d_tE(ell)<=d_tM(beta)+L/pi.                               (2)

When t_E<1 there is a unique maximal free gamma in [0,1), determined by equality, since d_t is continuous, starts at zero and diverges at one. For t_E=0 it is explicit:

    gamma_max=1-2^(-d_tM(beta)-L/pi).

If M=E and t_E=0 this becomes 1-(1-beta)*2^(-L/pi). For the same mask, gamma<=beta is sufficient. It is also sufficient in the actual essential-mask retarget case t_M=0, since d_tE(u)<=d_0(u). It need not suffice for an arbitrary unrelated target E. Even for the same mask, the cap is not sharp when unpaid vacuum calibration credit is already present. For example p=(1/4,3/4,0), V={0}, M=E=2, q=(1/2,1/2,0), beta=0 has L=(1/4)log(1/2)+(3/4)log(3/2)>0. The positive floor ell=1/9 still has sigma<0: 2^(4 sigma)=27/32<1. With matched q=p instead, the same floor has sigma=(3/4)log(9/8)>0. This explicitly checks why the incoming reference matters.

## 3. SAME-owner substitution and accumulated query losses

At any complete finite terminal frontier h let its actual reach be w_h. Suppose the supplied ORIGINAL account already has C=sum_h w_h CE(p_h,q_h), all old bills U, and capacity B, so M_remaining=B-C-U>=0. Changing every terminal to its required floor is payable if and only if

    sum_h w_h sigma_h(ell_h)<=M_remaining.                    (3)

This is exact by cancellation in the same B; no budget is renewed. Negative sigma is prepaid release and cannot also be booked elsewhere. Disjoint controller/seed decompositions introduce their actual seed weights, not the number of terminals. Equation (3) assumes that the previous query costs are already included in C and U; it is not permission to omit them.

For an actual finite coherent physical-query tree, the separate KL telescope is

    K_entry + sum_reached w_v sigma_v
       = sum_reached w_v (erasure_KL_v+outcome_KL_v)
           + sum_leaves w_h K_h.                             (4)

Derive a node by first applying the deterministic erasure to p,q, then their common source coherent kernel. The source outcome law is fair; the reference uses its OWN outcome probabilities. Chain rule gives erased KL=outcome KL+mean child KL. The erased-away difference is nonnegative by log-sum. Add signed reset changes and telescope over a FINITE tree. Source-zero rows use a declared fallback kernel and keep their reference mass. Equation (4) includes the Qloss missing in A011 v5; current A011 v6 explicitly withdraws that transaction reading. No all-policy v6 source envelope is independently accepted here.

## 4. Independent reconstruction of A049's four-bit certificate

Let m(x,y,z)=chi_x on z=0 and chi_y on z=1; let p=chi_xyz. Set f(a,x,y,z)=m on a=0 and p on a=1. Expansion gives m=(chi_x+chi_y+chi_xz-chi_yz)/2. The parent has eight atoms 1/16 and two atoms 1/4; H(f)=3, I(f)=11/4, and Inf_a=1/2. Both children are balanced and have the SAME essential mask xyz. Parent full coefficient squared is 1/4, while child full masses are 0 and 1. These statements are reconstructed from truth tables by the checker, independently of A049's helper.

Supply Q_alpha=(1-alpha)P_f+alpha delta_axyz, 0<alpha<1. The coherent kernel sends all spike mass to parity. Reference outcomes are ((1-alpha)/2,(1+alpha)/2). BOTH normalized inherited child references equal their true spectra. Therefore

    K_alpha=-(3/4)log(1-alpha)-(1/4)log(1+3alpha),
    O_alpha=-(1/2)log(1-alpha^2),
    erasure_KL=K_alpha-O_alpha,
    mean inherited terminal KL=0.

Every required fresh tilt gamma>0 costs F_gamma=-(1/2)log(1-gamma), on the multiplexer half only. Equation (4) consequently gives total query-plus-floor KL bill K_alpha+F_gamma>K_alpha for EVERY alpha,gamma in (0,1). This extends the parameter-free half-tilt comparison to the whole continuum and shows why comparing F_gamma to K_alpha alone is insufficient: all of K_alpha has already been spent on the preceding query.

For reference, the weaker bare comparison F_gamma<=K_alpha is equivalent to (1-gamma)^2>=(1-alpha)^3(1+3alpha). It does not establish payment after the query. At alpha=gamma=1/2 it fails by 5>4, recovering A049 exactly. A supplied remaining reserve M pays the actual extra floor if and only if gamma<=1-2^(-2M); M=0 permits only gamma=0. Full 4I capital is NOT refuted.

Minimality at A049's declared scope also holds: with at most two residual bits a Boolean noncharacter has all four squared coefficients 1/4. Otherwise it is a signed character. Hence a noncharacter child with zero full coefficient requires at least three residual bits, and the four-bit construction attains the bound. The finite census checks every labelled Boolean function through n=3 and every singleton outcome; it proves only this finite classification, not any FEI bound. A049's witness, exact sign and scoped minimality are independently accepted without repair. The new continuum payment consequence and formula (1) await external review.

## 5. First unpaid universal line

No necessary positive floor is supplied by these equations. The required algorithm must name its admissible profile and establish that it suffices for complete terminal entropy payment. It must then provide an ORIGINAL arbitrary-core complete source at O(I) price and the ACTUAL unused surplus for (3), including all query losses in (4). Taking q=p makes entry KL zero while CE remains H(p); free hereditary transport alone does not price full entropy. Full FEI remains open.
