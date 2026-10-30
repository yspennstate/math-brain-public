# A070 independent analytic scope reconstruction

All Shannon quantities below are in bits except the explicitly natural-log heat functional. Fourier coefficients use uniform probability measure. For a normalized real function g write p_S=ghat(S)^2 and E(p)=sum |S|p_S; E agrees with physical total influence only for Boolean signs. Zero atoms contribute zero. Conclusions labelled diagnostic outside the Boolean domain do not refute Boolean theorems.

## 1. Normalized real controls and full Booleanity

For psi_n=n^(-1/2) sum_i x_i, p is uniform on n singleton sets, E=1, H=log2 n. Its fourth moment is [n+6 binom(n,2)]/n^2=3-2/n<=3, so bounded L4 also does not repair a normalized-real FEI claim. Its coefficient support is an inclusion antichain, d(S)=1 and U=0. Consequently a Boolean arithmetic claim H<=2E+2U-(2-log2 e)Var would read log2 n<=log2 e and is false already at n=4. For n=4^m every coefficient is dyadic: dyadic amplitudes alone do not repair the claim.

Booleanity is equivalent to the simultaneous identities sum_S a_S a_(S xor V)=1_{V=empty}, since these are the coefficients of g^2. The singleton control satisfies all singleton-shift identities (indeed every odd-cardinality shift), but has coefficient 2/n at each two-coordinate shift. No choice of phases changes that coefficient to zero: precisely two terms survive with the same product. Thus it has no Boolean phase realization for n>=2. This is an exact impossibility proof, not a failed phase search. It does not establish the distinct historical fixed-arbitrary-order or cyclic-cap-prefix controls.

The near-constant real control sqrt(1-epsilon)+sqrt(epsilon/n)sum_i x_i has E=epsilon and H=h2(epsilon)+epsilon log2 n, while its squared L2 distance to 1 is 2-2sqrt(1-epsilon). Even L2 proximity plus normalization cannot supply a Boolean-only payment. This control is unbounded in L-infinity and makes no assertion about bounded near-Boolean functions.

## 2. Independent review of A066 heat identity

Let q_t(S)=p_S exp(-2t|S|), F(t)=sum q_t ln(1/q_t), E_t=sum |S|q_t, and G=F-2tE_t. Finite-sum differentiation gives G'(t)=-2J(t), where J=sum |S|p_S exp(-2t|S|)ln(1/p_S). Equivalently integrate each nonempty atom using 2|S| integral_0^infinity exp(-2t|S|)dt=1. Hence

    H_nat(p)=p_empty ln(1/p_empty)+2 integral J(t)dt.

This is valid for every probability law p, using NO Booleanity or phase condition. For fixed finite p, 0<=J(t)<=exp(-2t)J(0). The boundary term is at most 1-p_empty<=E(p). For Boolean signs in dimension n>=1 the even integer Walsh numerator gives every positive atom p_S>=2^(2-2n), hence J(0)<=2(n-1)ln(2)I; constants and n=0 have J=0. The missing universal integral payment is exactly FEI-strength on Boolean laws. For the real singleton control J=e^(-2t)ln n, integral J=(ln n)/2, so it cannot be proved from normalization alone.

For the Boolean point defect 1-2 1_{all plus}, put delta=2^-n. Its nonempty amplitudes are -2delta, and I=2n delta. With z=e^(-2t), direct differentiation of (1+z)^n gives

    J(t)/I=(2n-2)ln(2) z [(1+z)/2]^(n-1).

To check the no-integrable-envelope assertion independently, for 0<t<=1/4 take n=ceil(1/t). Then 2n-2>=1/t, z>=e^(-1/2), and (1+e^(-2t))/2=e^(-t)cosh(t)>=e^(-t). Also t(n-1)<1. Thus J/I>=ln(2)e^(-3/2)/t. Countably many dimensions allow the almost-everywhere exceptional sets to be removed simultaneously. Any common measurable pointwise envelope is nonintegrable. Direct substitution u=(1+z)/2 also gives

    (integral J)/I=2(1-1/n)(1-2^-n)ln(2).

Verdict: both A066 v1 claims HOLD at stated scope. This is an independent algebraic review; no repair, contribution or universal integral proof is supplied.

## 3. Independent review of A067 granularity and its precise Boolean step

An integer-valued cube polynomial of degree m has coefficients in 2^-m Z: its multilinear coefficients in 0/1 coordinates are integer finite differences, and substitution y=(1-x)/2 proves the assertion. For nonempty S, 2^(|S|-1)D_S f is integer valued because the sum of 2^|S| signs is even. This is the indispensable Boolean input. Its degree is d_f(S)-|S|, so a_S is in 2^(1-d_f(S)) Z, and log2(1/p_S)<=2(d_f(S)-1). Summation plus -p_empty ln p_empty<=1-p_empty gives

    H(f)<=2I+2U-(2-log2 e)Var,
    U=sum_nonempty p_S(d_f(S)-|S|).

The finite-difference integer lemma needs only integer values. The exponent improved by one uses the common odd-integer alphabet of signs; it is not supplied by norm one, fixed XOR prefixes or a probability-law cap.

The normalized singleton law fails that coefficient bound: d=1 would force every positive squared amplitude to be at least one. Thus the proof genuinely uses its Boolean hypothesis. Nevertheless Booleanity does not pay U.

For the dictator point flip x_1-2 1_{all plus} on N bits, delta=2^-N and all coefficients are nonzero. Direct edge counting and Fourier summation give

    I=1+(2N-4)delta,
    Var=1-4delta^2,
    U=N-1-(2N-4)delta-4Ndelta^2.

Therefore U/I diverges although H tends to zero and I tends to one. For Maj3 times the disjoint n-bit point defect, each shifted majority support consists of four distinct sets, at least three nonempty. In every character anchor at least 3/4 of the mass then has a nonempty majority set R_z and has a supported superset (R_z,all defect bits). Its arithmetic-envelope cost is at least 2n times that mass, hence >=3n/2 for every anchor. Meanwhile I=3/2+2n2^-n<=5/2. Verdict: A067 local theorem and both helper no-gos HOLD. The historical source claims are not new A070 candidates.

## 4. General perturbation test reconstructed without an entropy assumption

Fix a Boolean seed f on d bits. Pad to N>=d+2 bits and flip one input x0 to get f_N'. With delta=2^-N,

    a'_S=a_S-2 f(x0)delta chi_S(x0).

Each nonzero seed coefficient is a multiple of 2^(1-d), while the update magnitude is 2^(1-N), strictly smaller. A previously zero coefficient becomes nonzero. Thus the entire N-bit Fourier spectrum has full support and d_(f_N')(S)=N for every S.

The coefficient L2 distance is 2sqrt(delta). Cauchy-Schwarz applied to (a'-a)(a'+a) gives spectral total variation tau<=2sqrt(delta). A maximal coupling and the entropy chain rule give |H(p')-H(p)|<=h2(tau)+tau log2(2^N-1) (use the actual variation, or its upper bound when small). This tends to zero. Each physical coordinate influence changes by at most 2delta, since only x0 and its neighbor can have a changed pivot indicator. Hence |I(f_N')-I(f)|<=2Ndelta->0. In contrast

    U(f_N')=N Var(f_N')-I(f_N'),

which grows linearly when f is nonconstant. This independently reconstructs the lead's perturbation neutralization, without treating exact-support fragility as an FEI counterexample. Nonconstant Boolean f has positive variance and influence.

For fixed t and fixed seed, J for the perturbations also converges: the finitely many old atoms converge, and the new equal-probability tail contributes at most O(N^2 2^-N) to J(0). Integrated J converges by its entropy identity. Thus the heat functional passes this stability diagnostic, but has no new payment as a result.

## 5. Hybrid arithmetic and code bound: precise domain and payment

Let p be any probability law on a finite atom set. Suppose a_s>=log2(1/p_s) on every positive atom and l_s>=0 satisfies sum_s 2^-l_s<=1. Let A be the atoms where a_s<=l_s, B its complement, and m=p(B). On A bound entropy directly by p_s a_s. On B use the conditional probability law p_s/m and the restricted Kraft reference; Gibbs gives

    sum_B p_s log2(1/p_s)<=sum_B p_s l_s+m log2(1/m).

Consequently

    H(p)<=sum_s p_s min(a_s,l_s)+m log2(1/m)
         <=sum_s p_s min(a_s,l_s)+h2(m).

This proves the lead's hybrid statement with the branch K explicitly identified. The empty atom must also be handled: set its arithmetic cost to infinity and include it in the code, or keep its exact entropy contribution outside the nonempty sum. Applying 2(d-1) to the empty atom is unsupported. This is a specification guard, not a finding that the lead intended that convention.

Gibbs/Kraft and the branch-entropy charge require NO Booleanity. Booleanity enters only in the validity of a_s=2(d_f(s)-1) on nonempty atoms. The singleton control gives a_s=0, which is invalid, so it is outside the hybrid's arithmetic hypothesis. Pure code bounds remain valid and pay at least log2 n on that control.

The influence code l_s=log2 e+sum_(i in s)log2(I/I_i), with positive I, is Kraft-valid on ALL subsets: writing w_i=I_i/I gives sum_s 2^-l_s=e^-1 prod_i(1+w_i)<=1. Coordinates with zero I_i have infinite cost on containing sets. Here this works for any probability law with E>0 and spectral marginals I_i; it supplies no universal payment. Conditional nonempty code conventions require their own empty/variance accounting.

A level code l_s=-log2 r_|s|+log2 binom(N,|s|) is normalized for any probability distribution r on levels. A fixed prior mixture of complete code laws is valid, with selection penalties log2(1/w_j). Minima of unpenalized independent code lengths need not themselves be Kraft-valid. For the actual mixture, l_mix=-log2 sum_j w_j 2^-l_j obeys l_mix>=min_j l_j when sum w_j<=1. Arithmetic envelopes are not automatically Kraft references; they enter through the partition proof above.

## 6. Exact-scope obstruction to the three-reference hybrid

This independently verifies the lead's stated {granularity, level, influence} failure; it does not refute an additional paid queue reference. Let Addr_a have a address bits and 2^a private data bits. Its 4^a atoms have magnitude 2^-a, supports {data_u} union T, and I_0=1+a/2. Pad to N=a+2^a+2 bits and flip the all-plus vertex, producing F_a. Put epsilon=2^(1-N).

The old atom magnitudes after surgery are >=2^-a-epsilon>=2^(-a-1), so each has mass at least 4^-a/4. All atoms become nonzero, so every arithmetic cost equals 2(N-1). For a>=8, Bin(a,1/2) and Chebyshev give at least half the old atoms with |T|>=a/4. Their new total mass is >=1/8.

Influence changes per coordinate are <=epsilon. For address bits I_i<=1. Total I>=I_0-Nepsilon>=a/2 and I<=a+2; Nepsilon<=1 holds for these N. Therefore on those old atoms

    l_influence >= |T|log2(a/2) >= (a/4)log2(a/2).

For any normalized level prior, with k=|T|+1<=a+1,

    l_level>=log2 binom(N,k)>=k log2(N/k)
           >=(a/4)[a-log2(a+1)] >=(a/4)log2(a/2).

The last inequality follows from a(a+1)<=2^(a+1) for a>=8, verified at 8 and preserved by induction since (a+2)/a<=2. The arithmetic cost is also at least this bound: log2(a/2)<=a and 2(N-1)>=a^2/4 for a>=8. Consequently for either the minimum of these three costs or the arithmetic minimum with a fixed-prior mixture of the two code laws,

    sum_S p_S min(costs) >= (a/32)log2(a/2),
    [sum_S p_S min(costs)]/I(F_a) >= log2(a/2)/40 -> infinity.

The overhead h2(m) is nonnegative and cannot repair this lower bound. In contrast H(F_a)=2a+o(1) and I(F_a)=1+a/2+o(1), uniformly along this growing-seed sequence: spectral variation <=2^(1-N/2), whose product with N tends to zero, and influence error <=Nepsilon. Thus H/I->4. No Boolean FEI disproof occurs. A queue code that pays address labels once may defeat this obstruction, but its completed cost, full support on new tail atoms and fixed prior must be proved; no such universal payment is assumed here.

## 7. Other B14 domains: A068 and A069

A068's explicit packet identity Fhat(S,T)=hhat(S) ahat_S(T), and its entropy/influence chain rules, also work for a normalized real h. Thus these identities alone fail on the singleton control. The regular-base theorem requires a Boolean monotone/desirability base: pivotal derivatives are ternary and their fibers are antichains, enabling the rank expectation. Its extra quadratic phase assumption gives a Boolean autocorrelation supported on the polar kernel, hence a uniform affine spectrum of rank r and H=r<=2I. No conditional entropy is dropped. Arbitrary controls already contain full FEI at a dictator base. A generic point flip need not preserve quadratic-control/private-data form. The restricted theorem is not refuted by that loss of admission, and no universal or hereditary claim follows. This is a scope inspection, not acceptance of its entire baseline proof chain.

A069's prefix code L_T(S)=1+sum_(v internal) b_v 1{S intersects C_v} covers all subsets. Kraft and H<=Gamma_T=E L_T use no Booleanity and remain valid for normalized singleton laws, on which Gamma_T>=log2 n. The influence payment requires the specific paid occupancy hypothesis. It is not a universal consequence of decoding, spatial arms, or matching first moments of spectral and pivotal sets.

For a fixed all-set code with Lmax finite and coefficient perturbation delta_a, weighted Euclidean triangle gives

    |sqrt(Gamma_T(f'))-sqrt(Gamma_T(f))|<=sqrt(sum_S delta_a(S)^2 L_T(S)).

For one point flip delta_a(S)^2=4*2^(-2N), hence the right side is at most sqrt(4*2^-N Lmax). For a tree on N singleton leaves with branching 2..3, Lmax<=1+3(N-1), so it tends to zero. Percolation's original refinement decoder describes occupied cells; it does not determine spectral samples from pivotal sets. A069 correctly distinguishes the two.

An independent reconstruction of ALL A069 family constants is short and closes its review. Each nonempty child mask is represented by a fixed b-bit block after the root empty/nonempty bit. Preorder parsing terminates when all known occupied cells have reached singleton leaves, proving prefix freedom. A tree has at most N-1 internal vertices, so Lmax<=3N-2. If f,g differ on fraction rho then coefficient squared distance is 4rho; squared weighted triangle gives Gamma(f)<=2Gamma(g)+8rho(3N-2). Independently, changed pivotal events imply |I(f)-I(g)|<=2N rho.

For depth-d complete ternary majority the gate expansion has four masks of squared mass 1/4, each child marginal 1/2. Since children are balanced and on disjoint physical cubes, each full set has a unique child-mask decomposition and the coefficient law factors. Thus I(g_d)=(3/2)^d and the expected internal occupancy sum is sum_(j=0)^(d-1)(3/2)^j=2(I(g_d)-1). With three-bit internal masks, Gamma(g_d)=6I(g_d)-5 without padding and 6I(g_d)-3 with padding, using a new binary root. The preceding bounds give

    Gamma(f)<=12I(f)-6+48N rho-16rho.

If N rho<=1/8 this is <=12I(f). For a single point rho=2^-N and N>=3, N rho<=3/8, so Gamma<=12I+12. Balance gives Var(f)=1-4*2^(-2N)>=15/16, and I>=Var, so Gamma<=(124/5)I<25I. For N>=6, N2^-N<=1/8 and the constant 12 applies. For fixed d, padded Gamma(g_d) is constant; weighted triangle with Lmax=O(N) proves Gamma(f)-Gamma(g_d)->0. Every line of A069-STABLE-HIERARCHY-EDIT-PAYMENT v1 is therefore independently accepted at its stated scope. No repair or new contribution to that version was supplied.

## 8. Cyclic-law source boundary and remaining universal line

The campaign plan (lines 273, 302-308) records a non-Boolean cyclic-label signed-lifetime obstruction and a separate fixed atom-cap-prefix obstruction, referring to Brain51/Addendum 11.51. No complete original law appears in the packaged twelve source notes; the recall query is logged separately. We do not fabricate its formula or claim independent cyclic-certificate replay. All generic identities/codes above apply to any such probability law, so those steps add no admission condition excluding it. The decisive Boolean arithmetic step would require a genuine sign-valued inverse Walsh transform. Fixed atom caps and a cyclic marginal cannot replace that requirement, and the separate conditional-entropy remainder must remain paid.

First unsupported universal line after all reviews: every Boolean source has a perturbation-stable complete code/arithmetic partition whose TOTAL expectation (branch/prior normalizers, labels and terminal entropy included) is <=K I with one finite dimension-independent K. Neither the heat identity nor the two diagnosed generic codes establish this. The next concrete action is to reconstruct a full-support queue reference on point-flipped addressing with the tail and fixed prior included, before asserting that the enlarged hybrid evades the obstruction.
