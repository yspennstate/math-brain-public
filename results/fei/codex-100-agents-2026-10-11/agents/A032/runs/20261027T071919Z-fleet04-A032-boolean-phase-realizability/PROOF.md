# A source coefficient does not survive physical restrictions

All entropies and divergences are in bits. Full FEI remains open. There are two separate results: independent acceptance of A079's fixed-source theorem, and an actual Boolean obstruction to carrying a bounded source contraction through arbitrary physical restrictions.

## 1. Independent review of A079

The reviewed source is A079-DEFECT-CORE-LATENT-CAPACITY@1, statement hash0600eabe30c6bb4cc705595885de8bb5fcd43e6fbba1ef65f76cf0997cf0cbd4, PROOF.md hashd955dcd8217a22628d73b1601d42a0ab803032e9ab39520770e12303299d1663. Verdict: HOLDS at the stated fixed-source, complete-reference scope, without repair. The degree84 certificate is reconstructed from multinomial coefficients and a Horner shift, without importing author code. Both ordered-cone coefficient arrays are nonnegative. They prove

16(3u^7+v^7)^12 >= [8u^12+(u^4+v^4)^3]^7 (u,v>=0).

Homogeneity covers u>=v by (u,v)=(v+w,v), and v>=u by (u,v)=(u,u+w). Axes and origin are included. Taking nonnegative roots, setting x=u^4,y=v^4, and using the two-term Holder inequality with exponents3 gives, for P=(9,1,1,1,1,1,1,1)/16 and its marginal mu=(3/4,1/4),

E_P product_i f_i <= product_i (E_mu f_i^(7/4))^(4/7).

The factor16 is accounted for: the cube-root product of three scalar numerators divided by16 gives exactly the three marginal norms. There is no omitted product normalization. This inequality tensorizes over independent blocks. For any law R on3r bits choose f_i=(R_i/mu)^(4/7). The right side is1; the product is positive on supp R and its expectation is positive, since P_r has full support. KL against its normalized tilt proves

sum_i D(R_i||mu) <= (7/4)D(R||P_r).

Zero marginal masses cause no occupied zero. The r0 case is trivial. Averaging over an arbitrary auxiliary posterior gives sum_i I(X_i;J)<=(7/4)I(X;J). For a complete normalized product mixture Q=sum_j w_j product_i q_ji, define the exact posterior joint L(x,j)=P_r(x)w_j product_i q_ji(x_i)/Q(x). For finite divergence the posterior normalizers are positive on occupied atoms. Direct expansion gives

D(P_r||Q)=TC_L(X|J)+D(L_J||w)+sum_j L_J(j) sum_i D(L_{X_i|j}||q_ji),
TC_L(X|J)=r*tau-sum_i I(X_i;J)+I(X;J),
tau=2-(9/8)log2(3).

Therefore D(P_r||Q)+(3/4)I_L(X;J)>=r*tau, and D>=max(0,r*tau-(3/4)log2 M) for M positive-weight components. Infinite divergence is a trivial case; it does not require an undefined posterior. Redundant independent labels do not alter the mutual information. The information is posterior information, not a free prior capacity. Four complete rational posterior fixtures independently check both identities by prime-log vectors.

The strict5/3 exclusion also holds. With x1000,y1331 and A=8x^3+(x+y)^3, A^5-4(3*10^5+11^5)^9>0 exactly. The explicit tilted law R(s)=P(s)x^(3-|s|)y^|s|/(A/16) has sum marginal KL>(5/3)full KL, checked independently by outward rational atanh bounds. This R is a probability-law witness, not a claimed Boolean squared spectrum. P itself is Boolean-realized; direct Walsh and edge sums verify P_r for r1,2.

The complementary controller and three character tags preserve both full children, each with complete core bill beta D(P_r||Q), beta3/8. This follows from disjoint vacuum/tag Fourier sectors and their common factors, with no terminal deletion. Thus A079's complete physical scope remains valid: influence23/8+9r/32, conditional auxiliary entropy c_aux+(3/8)H(g_r), physical auxiliary influence(3/8)(3+3r/4), and all original-account debits retained. These identities are inherited from the already reviewed complete-handoff theorem and reconstructed algebraically; this stage does not claim a new exhaustive controller test.

## 2. A flat Boolean parent with arbitrarily bad inherited contraction

Use physical bit coordinates x,y in{0,1}^m, m>=1. Set

F_m(x,y)=(-1)^(sum_{j=1}^m x_j*y_j+y_1*sum_{j=2}^m y_j).

This is an explicit truth-table formula taking only signs. Write h(y)=(-1)^(y_1 sum_{j>=2}y_j). For frequency labels a,b, summing first over x gives

Fhat_m(a,b)=2^(-m)(-1)^(a dot b)h(a).

Indeed the normalized x sum vanishes unless y=a, when it equals1. Thus the parent squared spectrum is the full uniform law on2m bits. It is a coordinate product with optimal marginal-KL contraction coefficient1. Every physical influence is1/2: flipping x_j changes the exponent by y_j; flipping y_j changes it by x_j plus a function of y, and the fresh uniform x_j makes it balanced. Hence H(F_m)=2m and I(F_m)=m.

Restrict precisely x_2,...,x_m to an arbitrary t in{0,1}^(m-1). Every one of the2^(m-1) terminals remains. In the residual order x_1,y_1,y_2,...,y_m the terminal is

G_t=(-1)^[y_1(x_1+sum_{j=2}^m y_j)+sum_{j=2}^m t_j y_j].

Its Fourier support has four atoms of mass1/4, parameterized by two independent fair bits A,B:

S_{x_1}=A, S_{y_1}=B, S_{y_j}=A xor t_j (j>=2).

To derive this, sum over x_1 and over each y_j,j>=2. Nonzero coefficients require y_1=S_{x_1}=A and S_{y_j}=A xor t_j. The remaining sum over y_1 fixes this value and leaves a coefficient of magnitude1/2, for either S_{y_1}=B. This proves the actual Boolean realization, not just normalization of the four-atom vector. All remaining physical influences equal1/2 (each leaf derivative contains the free bit x_1 or y_1), so H(G_t)=2 and I(G_t)=(m+1)/2.

Let P_t denote this terminal squared spectrum. For any law R supported on its four atoms, identify R with the corresponding law of(A,B), with uniform reference U_2. There are m copies of A up to fixed complements, and one B. Consequently

sum_i D(R_i||(P_t)_i)=m D(R_A||U_1)+D(R_B||U_1)
 <=m[D(R_A||U_1)+D(R_B||U_1)] <=m D(R||P_t).

The last step is the exact identity D(R||U_2)=D(R_A||U_1)+D(R_B||U_1)+I_R(A;B). It uses m>=1. Singular targets are handled by restricting to the four-atom support; laws outside that support have infinite full divergence.

Equality is attained by R=P_t conditioned on A=1, with B still fair. Then D(R||P_t)=1, m copied marginals each contribute1, and B contributes0. The optimal terminal coefficient is therefore exactly m. For m2 this is already2>7/4 after a single physical query of a4-bit flat parent. For arbitrary m the entire terminal frontier has coefficient m, at total reach1; no rare branch has been selected and no complementary terminal discarded.

The original influence account is explicit. Every queried x_j has influence1/2 at every earlier restriction; a still free y_j makes its derivative balanced. Therefore total reach-weighted query influence is(m-1)/2 and expected terminal influence is(m+1)/2, whose sum is the original m. At query depth k the remaining quadratic form has rank2(m-k), since the unrestricted x_j still pair with their y_j and the other rows are dependent on y_1. Eliminating the paired rows removes all the extra edges, which proves the rank assertion. Thus each intermediate spectrum is flat on rank2(m-k) support and entropy is2(m-k): total entropy loss is2(m-1), and terminal entropy2 is retained. In particular this family satisfies H<=2I throughout; it is not an FEI counterexample. Arbitrary choice of another policy is not refuted.

The source-capacity consequence is equally explicit. Each terminal has total correlation TC(P_t)=m-1. Splitting on the single latent bit A gives an EXACT two-component coordinate-product mixture Q=P_t, so D(P_t||Q)=0 and posterior I(S;A)=1. Thus a universal inequality D(P_t||Q)+a I(S;A)>=TC(P_t) would need a>=m-1 on these actual inherited laws. This matches c-1 for the sharp coefficient c=m above; it is not a contradiction to A079's fixed-source a3/4. For m>=2 one component is impossible because the copied marginals are fair but deterministically related, hence the exact mixture count is2. At m1 the source is already a product and the minimum count is1. No exponential latent alphabet is needed. The resulting TC(m-1) equals TWICE the original query influence(m-1)/2, so this witness also shows why unbounded contraction alone does not exclude a correctly amortized O(I) account.

## 3. Universal boundary and next step

No dimension-independent KL marginal-contraction coefficient can be guaranteed merely because the original actual Boolean spectrum is a coordinate product and descendants are actual physical restrictions. Spectral marginalization alone would preserve a product law; the signed Fourier recombination at a physical query is different. This theorem supplies an explicit phase-compatible obstruction to dropping that distinction. It does not refute A079, whose source is the specified P_r, and does not show that every selected restriction strategy fails.

The first unsupported universal line remains an ORIGINAL O(I) source for arbitrary Boolean cores, or a necessary compatible continuation paid from the SAME genuinely unused source while retaining all old bills and full terminals. A fixed contraction budget inherited from a flat root cannot supply it. The next action is to price the actual signed source change, or to select and justify a policy with its full inherited source coefficient charged to original influence. Reapplying the7/4 defect theorem to a descendant just because the ancestor has a cheap reference is invalid.
