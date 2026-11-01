# Coherent averaging with a variance payment

All logarithms here are natural. For s>0 set psi_s(a)=a^2 ln(s/a^2), with psi_s(0)=0. On [-sqrt(s),sqrt(s)] the function psi_s(a)+3a^2 is convex: away from zero its second derivative is 2 ln(s/a^2)>=0, and its first derivative extends continuously through zero. Jensen therefore gives, for any probability weights pi_r and |a_r|<=sqrt(s),

    psi_s(sum_r pi_r a_r)
      <= sum_r pi_r psi_s(a_r)+3[sum_r pi_r a_r^2-(sum_r pi_r a_r)^2].   (1)

This is a coherent amplitude inequality. It needs no entropy of the slice labels and is independent of their number. The constant 3 suffices for arbitrary signed amplitudes. No claim of optimality for Boolean threshold slices is made.

For an arbitrary Boolean sign F(A,B) on independent product inputs, let f_x(B)=F(x,B). Put v_T=prod_{j in T}4q_j(1-q_j), P(S)=Fhat(S)^2. Every Boolean slice has |fhat_x(T)|<=sqrt(v_T): integrate its normalized mixed difference, whose absolute value is at most one. Let m(B)=E_A F. The coefficient identity is mhat(T)=E_A fhat_x(T), and Parseval on A gives

    E_A fhat_x(T)^2 - mhat(T)^2
       = sum_{U subset A, U nonempty} P(U,T).                           (2)

Applying (1) with s=v_T and summing over |T|>=2 gives the universal block inequality

    E_pureB,ge2(F) <= E_A E_ge2(f_x)
                    +3 sum_{U nonempty, |T|>=2} P(U,T).                (3)

The conditional slices in (3) are physical Boolean restrictions. Their coefficients are averaged coherently; their squared spectra are not substituted for the spectrum of m. This is neither conditional-input total correlation nor good-coordinate spectral erasure.

# Payment for the full two-weight class

Let F=2*1{w sum_{i in A}X_i+sum_{j in B}Y_j>=t}-1, with arbitrary finite groups, arbitrary real w>0,t, and independent interior biases. Define Delta=sum_{S nonempty}(|S|-1)P(S), c=460+80 ln 2, and

    D_B = sum_{U,T: T nonempty} (|T|-1)P(U,T),
    D_A = sum_{U,T: U nonempty} (|U|-1)P(U,T),
    M   = sum_{U nonempty,T nonempty} P(U,T).

All three quantities are nonnegative. Directly, coefficient by coefficient,

    Delta = D_A+D_B+M.                                                (4)

Moreover D_B=E_A Delta(f_x); D_A=E_B Delta(F(A,y)). Both physical slice families are symmetric thresholds, since all weights within their remaining group are equal. The source baseline E(g)<=c Delta(g) at every product bias, and nonnegativity of each corrected entropy summand, give E_ge2(g)<=c Delta(g). Thus (3) and its counterpart with A,B exchanged yield

    E_pure,ge2(F)
      <= c(D_A+D_B)+3 sum_mixed [1{|U|>=2}+1{|T|>=2}]P(U,T)
      <= c(D_A+D_B)+6M
      <= c Delta(F).                                                 (5)

Here E_pure,ge2 includes both sectors supported wholly in one group and having total degree at least two. Equation (4) makes the payment explicit: D_A,D_B,M form a partition of the root deficit. The stronger middle bound in (5) should be retained, rather than treating either D as an additional reserve. Constants, empty groups and deterministic inputs are handled by freezing/removal; real signed weights can be oriented before identifying two positive weight groups.

The singleton corrected entropy of any Boolean sign is at most 4 Delta nats: with signed derivative mean a_i, pivotal probability rho_i, |a_i|<=rho_i, its singleton contribution is 2v_i a_i^2 ln(1/|a_i|)<=2v_i(rho_i-a_i^2); summing I_i-P({i}) costs at most 2Delta. Consequently the full target reduces to a single remaining sector:

    E(F) <= c(D_A+D_B)+6M+4Delta+E_mixed(F),                           (6)
    E_mixed(F)=sum_{U nonempty,T nonempty}P(U,T)ln(v_U v_T/P(U,T)).

An absolute bound E_mixed<=K Delta would give corrected FEI+ with (c+4+K)/ln2. This is a sufficient reduction, not an assertion that it is proved. Adding the two bounds makes the coefficient c+4+K explicit; it does not create a second independent root deficit.

# A mass-only mixed payment is false on actual unequal-weight gates

For each m>=1 use |A|=|B|=m, w=2, t=3m and all biases 1/2. The gate is the conjunction sign: only the all-one input meets the threshold. Put N=2m. Every nonempty Fourier coefficient has magnitude 2^(1-N), hence P=4^(1-N) and v_S=1. Therefore

    M=(2^m-1)^2 4^(1-2m),
    E_mixed/M=2(2m-1)ln2.                                            (7)

This diverges, so no arity-independent inequality E_mixed<=K M can complete (5). It refutes that proposed replacement only, not FEI+. The actual mixed deficit is

    Delta_mixed/M=2m*2^(m-1)/(2^m-1)-1,

so E_mixed/Delta_mixed tends to 4 ln2. A viable mixed-set reference must charge degree or exploit coherent slice structure, rather than pricing each mixed atom with one fixed mass credit. Conjunction is already a closed class; (7) is a route obstruction, not a new class target.

# Extension to every partition into equal-weight groups

The pure-sector payment is not restricted to two weights. Partition any weighted threshold into its k nonzero positive equal-weight groups G_j. For a nonempty Fourier set S let r(S) be the number of occupied groups and a_j(S)=|S intersect G_j|. Put

    D_j=sum_{S:a_j>0}(a_j-1)P(S),
    R=sum_{S nonempty}(r(S)-1)P(S).

Then Delta=sum_j D_j+R exactly. Every restriction to one G_j is a symmetric threshold at its actual product bias. Applying (3) to each group pays the sum of all pure-group higher-degree entropies by

    c sum_j D_j +3 sum_{S:r(S)>=2} #{j:a_j(S)>=2} P(S).

For r>=2, #{j:a_j>=2}<=r<=2(r-1). The last term is at most 6R, so the whole expression is at most c Delta. Thus (5) extends to all finite real-weight thresholds, with no dependence on k, arity or weight ratios. Equal weights need not imply equal biases. If all weights are distinct these pure higher-degree sectors are empty, so this extension alone pays none of the genuinely mixed higher-degree cost; this limit prevents overclaiming the progress toward arbitrary weights.

# Exact first unsupported line

For two groups with M>0, define mixed marginals p_A(U)=sum_{T nonempty}P(U,T), p_B(T)=sum_{U nonempty}P(U,T). The product reference Q(U,T)=[p_A(U)/M][p_B(T)/M] is normalized on the two nonempty-set spaces. Put E_A^m=sum_U p_A(U)ln(v_U/p_A(U)) and likewise E_B^m. A direct logarithmic expansion gives

    E_mixed = E_A^m+E_B^m+M ln M-M TC_spec,                            (8)
    TC_spec = sum_{U,T}(P(U,T)/M)ln[(P(U,T)/M)/Q(U,T)] >=0.

Thus a bound on E_A^m+E_B^m+M ln M would suffice, but is not proved here. Retaining the negative spectral TC term may be essential. This TC is dependence between the two portions of a Fourier set conditioned on being mixed; it is not the physical input law conditioned on the threshold event. Equation (8) is an exact normalized-reference identity, not a payment theorem or an erasure bound. When M=0 the mixed entropy and the reference obligation are zero, and no conditional distribution is formed.

For arbitrary two-weight thresholds it remains unproved that E_mixed(F)<=K Delta(F) for one absolute K, with a normalized reference describing both occupied groups. The disjoint-boundary Gram matrix pays energy, not the logarithm of a complete mixed Fourier set. Neither (1) nor applying the scalar lemma separately in each heavy coordinate controls the internal A-spectrum of fhat_x(T). The next step is one reference for that coefficient process, retaining the degree-weighted mixed deficit and the signed/coherent nature of every slice coefficient. The original coefficient-one pivotal-credit failure remains at its original scope; nothing here disproves a larger-constant pivotal estimate or replaces spectral erasure with conditional-input TC.
