# Same-source x exposure and paid canonical terminal resets

All entropy and KL are in bits, on independent uniform inputs. This refines A038-BALANCED-CANONICAL-ADMISSION@1 on its stated character-point-defect family; it is not a universal source-admission theorem. Let d_m(y)=1-2*1[y=0], h_m(z,y)=chi_z d_m(y), m>=3, and F=chi_a on x=0, h_m on x=b=1, and +1 otherwise. M is the ORIGINAL completed canonical occupancy reference of F. A=D(P_F||M)=(15/16)K_occ. The definition is the source-exact nonempty matched-marginal maximum-entropy projection, not an ordinary full-product substitution.

Query b first. Retain b=0 untouched. In b=1 permit any finite adaptive tree of fresh data coordinates and x, with x exposed on every terminal path and a never queried. Data may precede or follow x, with different choices in the two x outcomes. Stop after this physical tree. Then prescribe a fresh completed canonical occupancy reference at EVERY b=1 terminal; retain the inherited reference on b=0. The conclusion charges these actual resets, including the full old inherited terminal bills. No further physical query or second reset is covered.

Write H0=H(F), I0=I(F), Hf=E H(leaf), If=E I(leaf), S=4If-Hf, Sroot=4I0-H0, D=H0-Hf and R=I0-If. The original source liability is L=A+[D-4R]_+. For each terminal l receiving a reset, let Knew_l be its divergence to the prescribed canonical reference and Kold_l its divergence to the normalized inherited reference. Use the original physical reach probabilities p_l, not reference likelihoods. Define B=sum_reset p_l Knew_l, and actual positive reset conversion C=sum_reset p_l [Knew_l-Kold_l]_+. Any prior genuine conservative booking 0<=omega<=11/32 is retained.

Here omega includes EVERY genuinely booked earlier conservative charge beyond the displayed final whole liability L. The numerical bound on omega is a hypothesis, not automatic permission to retire old positive bookings. In the specific intended transition from ANY already paid data-only frontier, append x immediately to every b1 leaf and then reset; do no further physical query between that frontier and reset. X neutrality proves that L is EXACTLY its already booked value at that frontier. Thus this direct post-prefix application preserves the old L itself, without a refund, as well as the old omega. The broader interleaved-history eligibility theorem uses the same explicit all-bookings hypothesis.

THEOREM. Every stated m and history satisfy

    A<39/32,  S>=2,  Sroot>=2,  0<=C<=B<=7/32,
    S - (L+omega+B) > 7/32.

Thus the SAME actual final surplus pays the complete original source liability, old booking, and the full prescribed new terminal KLs. Since C<=B, this also pays the actual positive reference conversion. Neither original source credit nor query allowance is renewed. Retaining old terminal KL AND paying full new KL is deliberately conservative; they are counted as two different already-specified reference bills, not as independent releases from one source.

## 1. Exact source and physical account

For completeness, r_i=Inf_i(F)/v, v=1-P_F(empty)=15/16. If sum r_i>1, the canonical law on nonempty sets is Bernoulli(c r_i) conditioned nonempty, where 1-c=product_i(1-c r_i). M(empty)=1-v. Its normalization and matching marginals follow from this equation. A positive unique c follows by strict monotonicity of [1-product(1-c r_i)]/c on (0,1), with endpoints above/below 1. On nonempty atoms log M is affine in set membership. Matching these moments and empty mass proves CE(P_F,M)=H(M), so A=H(M)-H0.

Disjoint root Fourier sectors give H0=3+H(h_m)/4 and I0=(5+I(h_m))/4; control marginals are 1/2,1/2,1/4 and data marginals Inf_j(h_m)/4. Ordinary entropy subadditivity of M, not a reference replacement, gives

    A <= G_m-1-H(h_m)/4,
    G_m=2 h2(1/4)+m h2(2^(-m-1)).                 (1)

The same actual coherent kernel transports the full M. For row amplitudes u=fhat(T), w=fhat(T+i), erase i and use k_s(T)=(u+(-1)^s w)^2/[2(u^2+w^2)]; if the denominator is zero use k_s=1/2 for BOTH source and reference. Keep reference-only rows, normalize each reference child by its OWN output probability, and retain both physical outcomes with probability1/2. The finite KL chain rule is incoming KL = erasure loss + outcome KL + mean inherited child KL. Iterating gives A equal to all weighted erasure/outcome releases plus all terminal inherited KLs. This is a common stochastic channel, not an independence assumption. It applies in either order of data/x exposure and includes b=0.

Pure algebra yields

    S-L=min(S-A,Sroot-A),                       (2)

because D-4R=S-Sroot. No second root bank is introduced by (2).

## 2. Why arbitrary stated x/data histories retain S>=2

For ANY restricted data core g independent of a, the selector between chi_a and g by x has H=2+H(g)/2 and I=1+I(g)/2, regardless of bias of g. The two Fourier copies of g are disjoint from the a and ax atoms. Exposing x leaves chi_a and g with weights1/2. Their mean price-four surplus is exactly 2+(4I(g)-H(g))/2, identical to that of the selector before exposure. Thus x itself has H decrement2 and influence decrement1/2, with zero signed price-four deficit.

Every data restriction of h_m is, up to sign, a character times a point defect on independent coordinates, a point defect, a character, or a constant. Each has H<=4I. To check the only nontrivial case d_k, epsilon=2^-k: its squared masses are (1-2epsilon)^2 and 4epsilon^2 repeated 2^k-1 times. Its nonempty entropy is 8(k-1)epsilon(1-epsilon), and the empty entropy is at most 4epsilon(1-epsilon)/ln2. With ln2>1/2, H(d_k)<=8k epsilon=4I(d_k) for k>=2. k=0,1 are constant/character. Tensoring an independent character preserves this certificate.

At the first-x frontier, each reached selector with conditional weight p supplies an x=0 character branch with weight p/2 and surplus4, and an x=1 core branch with supplied surplus>=0 at EVERY later data leaf. Data queries on the character branch are dummy. Since the first-x frontier probabilities sum to1 inside b=1, the total character contribution there is2, regardless of adaptation before x. Thus b=1 contributes mean surplus>=2. The untouched b=0 selector also has surplus2. Consequently S>=2. The root certificate gives Sroot=2+I(h_m)-H(h_m)/4>=2. Individual core terminals need not have surplus2; both x outcomes supply the pair bound.

## 3. Sharper uniform original-source bound

Set e_m=m(m+5/2)/2^(m+1). Since ln2>2/3, h2(u)<=u log2(e/u) implies m h2(2^(-m-1))<e_m. Also h2(1/4)<13/16 is exactly equivalent to 3^12>2^19. The sequence e_m decreases for m>=3, since 2m(m+5/2)-(m+1)(m+7/2)=m^2+m/2-7/2>0.

At m=3, G<85/32 and H(h_3)>=8*2*(1/8)*(7/8)=7/4, so (1) gives A<39/32. At m=4, G<13/8+13/16=39/16 and H(h_4)>=8*3*(1/16)*(15/16)=45/32, giving A<139/128<39/32. At m>=5, G<13/8+75/128=283/128 and H>=0, giving A<155/128<39/32. These are explicit all-dimensional estimates, not an extrapolation.

## 4. Price of the prescribed new occupancy references

For a point defect d_k with k>=2, all nonempty squared masses are equal. Its conditional nonempty law is uniform and its inclusion marginals are all 2^(k-1)/(2^k-1). Thus c=1-2^-k makes c r_i=1/2; the canonical conditional law equals its actual conditional law, so its completed-reference KL is ZERO. Constant and character boundaries also have completed canonical KL zero; zero-variance is interpreted directly as delta_empty.

For chi_z d_k with z still present, the spectrum always contains z and its z marginal is1. Hence the canonical law on the forced support is z forced and the other coordinates independent Bernoulli(2^(1-k)). The completed-source KL is exactly

    T_k = k h2(2^(1-k)) - H(d_k).               (3)

This is a forced-coordinate boundary of the NONEMPTY canonical definition: nonemptiness is automatic. It is not a full-product substitution at the original root. Dummy coordinates are fixed absent. For k=0,1,2, T_k=0 (constant/character or the flat two-bit defect product law). For k>=3, using the lower nonempty entropy and the preceding binary-entropy upper bound,

    T_k < E_k = 2^(1-k)[k^2-7k/2+4+4(k-1)2^-k].

E_3=7/8. E_k-E_(k+1)=2^-k[k^2-11k/2+13/2+(6k-8)2^-k]. The bracket is1/4 at k=3, positive at k=4, and its polynomial part is positive and increasing for k>=4. Thus E_k decreases for k>=3, and ALL possible reset core terminals have Knew<=7/8.

Every terminal on x=0 is a character and costs zero. The total physical weight of b=1,x=1 is1/4, even with adaptation: x was fresh and fair at its first exposure. Hence B<=7/32. Each inherited terminal KL is nonnegative, so [Knew-Kold]_+<=Knew, proving C<=B. No signed refund is needed for this conservative upper bound.

Combining (2) with S,Sroot>=2 and A<39/32 gives S-L>25/32. Subtracting omega<=11/32 and B<=7/32 proves the claimed remaining margin >7/32 from the SAME owner.

## 5. Exact scope boundary

Only one specified canonical reset frontier, after all b=1 paths have exposed x, is paid. Querying a can consume the supporting x=0 character reserve; it is not authorized by the S>=2 proof. Querying b=0 further, a second fresh-reference reset, or a subsequent mixed query requires a new same-account argument retaining the actual first reset debit. Arbitrary Boolean cores do not come with the required source bound or hereditary terminal certificates. Those are the first unsupported universal lines. Full FEI remains OPEN.
