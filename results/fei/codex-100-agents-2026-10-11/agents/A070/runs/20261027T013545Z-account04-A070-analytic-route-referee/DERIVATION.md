# Exact shallow Boolean tests do not pay the source

All cubes have uniform measure. Logarithms are base two. For a REAL function g of squared norm one, H(g) is the Shannon entropy of its squared Fourier coefficients and J(g)=sum_S |S| ghat(S)^2. J is squared derivative energy; it is ordinary pivotal influence only for Boolean signs. No statement below refutes Boolean FEI.

## 1. Independent review of A069's near-Boolean theorem

Let m>=2 be even, n=m^2, p=1/(n+1), r=1-2p. Define

    h(y)=Im product_{j=1}^n (m+i y_j)/sqrt(n+1).

Every factor has modulus one, so |h|<=1. Direct expansion gives hhat(S)=(-1)^((s-1)/2) m^(n-s)/(n+1)^(n/2) at odd s=|S| and zero otherwise. These coefficients are rational, since n is even. Summing odd binomial terms and differentiating the finite generating polynomial gives

    A=E h^2=(1-r^n)/2,
    J(h)=np(1+r^(n-1))/2<=1.

All denominators are strictly positive. The binomial theorem gives r^(-n)=(1+2/(n-1))^n >=1+2n/(n-1)>3. Thus A>1/3. Every occupied squared coefficient w_s=p^s(1-p)^(n-s) is at most p.

For a fresh sign x0, 0<epsilon<1, Z=1+epsilon^2 A, set

    g=(x0+epsilon h)/sqrt(Z).

The distinguished Fourier atom {0} is disjoint from the odd y-set atoms. Thus E g^2=1, J(g)=(1+epsilon^2 J(h))/Z, and

    H(g)>=epsilon^2 A log(n+1)/Z,
    H(g)/J(g)>epsilon^2 log(n+1)/(3(1+epsilon^2)).       (1)

The factors Z cancel when taking the ratio; using only J(g)<=1+epsilon^2 would lose that cancellation. All nonzero h-sector probabilities are <=p; all entropy terms, including the distinguished atom, are nonnegative.

Pointwise, sign(g)=x0, |g-x0|<epsilon+epsilon^2/2, and |g^2-1|<=2epsilon+epsilon^2. For the first estimate use 1-Z^(-1/2)<=(Z-1)/2, A<=1, and Z>1. For the square estimate use (1-epsilon)^2/Z<=g^2<=(1+epsilon)^2/Z with 1<=Z<=1+epsilon^2. Averaging preserves the square bound at every physical restriction. Parseval for g^2-1 gives the full squared convolution-residual bound (2epsilon+epsilon^2)^2; its empty coefficient is zero.

Taking epsilon=1/k and n=2^(2k^4), m=2^(k^4), yields the A069 lower bound H/J>2k^2/(3(1+1/k^2)). Every approximation error tends to zero. This reconstructs A069-UNIFORM-NEAR-BOOLEAN-SOURCE-OBSTRUCTION@1 unchanged, including its every-reference/every-complete-tree consequence in Section 4 below. No repair or independent acceptance of our own prerequisite is supplied. The separate A069 acceptance of A070's previous homogeneous-boundary claim is consumed as an external receipt.

## 2. Parity blocks make the shallow tests EXACT

Replace EACH input z_j, j=0,...,n, by the parity of a disjoint block B_j of b>=1 physical coordinates. Write pi_j=product_{i in B_j} x_i and G(x)=g(pi_0,...,pi_n). The parities are independent fair signs. The injective map L(S)=union_{j in S} B_j sends each Fourier coefficient of g to the same coefficient of G. Therefore

    E G^2=1, H(G)=H(g), J(G)=b J(g).                  (2)

It also commutes with symmetric difference, so the signed convolution at L(T) is exactly the original convolution at T, and every convolution outside the image is zero.

The original square g^2=(1+2epsilon x0 h+epsilon^2 h^2)/Z has no nonconstant term of degree one. The cross term x0 h has even total degree at least two. Since h has only odd Fourier degrees, h^2 has only even Fourier degrees, and every nonempty one has degree at least two. After lifting, every nonempty coefficient of G^2 has size at least 2b. Consequently, for EVERY U with 0<|U|<2b,

    sum_S Ghat(S) Ghat(S xor U)=0.                    (3)

For any fixed coordinate set F with |F|<2b and ANY assignment alpha, averaging G^2 over the unfixed coordinates kills every nonconstant coefficient: none can be supported inside F. Hence

    E[G^2 | x_F=alpha]=1.                             (4)

This includes EVERY realized node of EVERY adaptive physical tree of depth at most 2b-1. At a query whose children remain in this range, both children have norm exactly one. The ordinary probability-law entropy restriction formulas are then legitimate there without child renormalization. This is an exact identity, not an error estimate.

The threshold 2b is sharp. Fix all coordinates in B_0 and B_1 positive. In the square, the only surviving nonconstant character is B_0 union B_1 with coefficient

    c=2epsilon m^(n-1)/(Z (n+1)^(n/2))>0.

Thus the conditional norm is exactly 1+c. Changing one of the two block parities gives 1-c. This explicitly identifies a missing Boolean equation and a nonunit deeper child. In particular, the family is genuinely non-Boolean.

## 3. A growing exact prefix still has unbounded H/J

Take k>=2, b=k, epsilon=1/k, n=2^(2k^4). Equations (1)-(2) give

    H(G_k)/J(G_k)>2k/(3(1+1/k^2)) -> infinity.         (5)

Meanwhile G_k is uniformly within 1/k+1/(2k^2) of the actual Boolean parity pi_0; its square is uniformly within 2/k+1/k^2 of one. All convolution equations of degrees 1 through 2k-1 hold EXACTLY, and ALL restrictions fixing at most 2k-1 physical bits have squared norm EXACTLY one. For any prescribed finite depth/order and any positive uniform tolerance, an entire tail of the sequence satisfies those hypotheses with unbounded H/J. The rounded Boolean family is pi_0 with H=0 and I=k. No Boolean counterfamily is produced.

This combines A069's uniform approximation guard with an exact, growing shallow-normalization guard. It does not establish a new all-Boolean consequence, and no novelty is asserted relative to previously known fixed-prefix obstructions. It prevents using a finite collection of exact local norms to close the original source-payment gap.

## 4. Full terminals keep the obstruction on stopped trees

Let R be any normalized reference dominating the actual root Fourier support. Use homogeneous child masses and marginalize R in the queried frequency; never renew or independently normalize the child reference. Put C(g,R)=sum ghat(S)^2 log(1/R(S)). Pairing coefficients a,b in a queried fiber gives

    D_i=C_parent-average C_child
       =sum_T [a^2 log((R_T+R_Ti)/R_T)
                +b^2 log((R_T+R_Ti)/R_Ti)]>=0.

Zero actual masses are omitted; a positive mass has a positive corresponding reference atom. These conditions remain true after restriction. The energy identity is J_parent=j_i+average J_child. On ANY finite adaptive stopping tree, with original physical reach weights w,

    sum_nodes w D_i + E C_leaf = C_root,
    sum_nodes w j_i + E J_leaf = J_root.

Since (D_i-4j_i)_+>=D_i-4j_i,

    sum_nodes w(D_i-4j_i)_+ + E C_leaf
       >= C_root-4(J_root-E J_leaf)
       >= H_root-4J_root.                             (6)

The final step uses J_leaf>=0 and Gibbs C_root>=H_root for the root probability law. Thus (5) obstructs the complete terminal-inclusive source bill for EVERY stopping rule, not just complete exposure. Independently chosen initial random seeds are handled by conditioning on the seed and averaging its original law. Both full child costs and constant-output continuations remain present. For complete trees C_leaf=0, recovering A069's exact scope.

For a tree stopped at depth <=2k-1, all spectra at nodes are probability laws by (4). There is also a reference-free statement: entropy telescoping and the same energy identity imply

    sum_nodes w(Delta_i H-4j_i)_+ + E H_leaf >= H_root-4J_root.

So exact shallow child normalization does not make the unpaid terminal entropy disappear. This conclusion does not depend on a chosen reference or on accepting an abstract subset law as Boolean.

## 5. Checks that could fail and their outcome

The review must catch an incorrect norm factor, entropy atom bound, parity-lift energy factor, convolution cutoff, missing constant term, changed physical measure, or omitted terminal. The independent checker constructs the Gaussian product by integer real/imaginary multiplication, computes Walsh transforms from its actual values, independently computes every convolution, lifts the physical table, and Walsh-transforms the squared lifted table. It checks every shallow fixed mask/assignment and directly averages the first failing restriction. The fixture n=4 has A=272/625 and hhat({j})=8/25; b=1,2,3 and epsilon=1/2,1/4 cover the minimum block width, negative/positive input signs, all shallow prefixes, and the exact boundary 2b. The larger base binomial checks are n=16,64, without allocating their cubes. The infinite-family limit is symbolic, never extrapolated from finite tests.

All new expressions are finite sums. No integral or limit is interchanged with a sum. Normalizers Z>1, n-1>0, b>=1, and J(G)>0 are verified analytically where used. The normalized degree-one control still fails Booleanity at degree two; the new family postpones that failure to degree 2b. Historical cyclic-law companion certificates remain unavailable in the packaged sources and are not replayed or used as proof dependencies. Their stated distinction between non-Boolean law failures and Boolean FEI is preserved.

The proof rung is an explicit finite Fourier proof with exact finite certificates, pending independent review of Sections 2-4. Any Lean result concerns only its named algebraic sublemma and does not certify the Fourier argument or the full conjecture.

## 6. First unpaid Boolean step

For arbitrary actual Boolean cores, construct a once-owned ORIGINAL influence-priced source or selected Bellman supersolution using a full signed Boolean consequence that excludes this family. Exact finite-depth norm/convolution constraints and uniformly small defects cannot supply that line with a dimension-independent constant. No old debit is refunded, no source is reset, and both full terminals must remain. Full FEI is OPEN.
