# Minimum-influence endpoint: a dimension-cutoff scope certificate

All entropies are in bits. Let N>=1, f be a nonconstant Boolean sign, A its smaller sign class, a=|A|<=2^(N-1), and b its number of physical boundary edges. Then I(f)=b/2^(N-1).

For X uniform on A, each conditional binary fiber is a singleton or a pair, so H(X_i|X_-i)=2 E_i(A)/a, where E_i is the internal undirected edge count. By the entropy chain rule and conditioning, sum_i H(X_i|X_-i)<=H(X)=log2 a. Thus 2E(A)<=a log2 a and b=aN-2E(A)>=a(N-log2 a).

If a=1, b=N. If N>=3 and 2<=a<=2^(N-1), the concave function t(N-log2 t) has its minimum on that interval at an endpoint. These endpoints are 2(N-1) and 2^(N-1), both strictly larger than N. Consequently I(f)>=N 2^(1-N), with equality precisely at one-point defects and their output complements for N>=3. For N=1 the two nonconstant signs attain the bound. For N=2 a singleton attains it, and a two-point set attains it precisely when its vertices are adjacent; the latter signs are signed dictators. Opposite pairs have b=4 and do not attain it. These exhaust the exceptions.

Define the finite, nonnegative cutoff s_*(N)=N-1-log2 N. Its influence threshold is 2^-s_*(N)=N 2^(1-N). The admissible class 0<I(f)<=2^-s_*(N) is exactly the equality class above. A cutoff strictly larger than s_* at every N admits no nonconstant function. In particular s(N)=N has empty domain. Constants are excluded before any normalization or ratio.

For a point defect f=1-2 1_{x=x0}, put p=2^-N and t=4p^2. Its empty Fourier mass is (1-2p)^2 and every nonempty mass is t. Fix ell>=2. In R_geell=sum_i sum_{T subset [N]\{i}, |T|>=ell} phi(p_T,p_(T+i)), every retained pair has two equal masses t; phi(t,t)=2t. There are sum_(r=ell..N-1) binom(N-1,r) such pairs for each i. Therefore

R_geell/I = 4*2^-N sum_(r=ell..N-1) binom(N-1,r)
             = 2-4*2^-N sum_(r=0..ell-1) binom(N-1,r),

where binom(N-1,r)=0 for r>N-1 and the first sum is zero if ell>N-1. This is nonnegative and strictly below 2 for every finite N; it tends to 2 for every fixed ell because the omitted sum is bounded by a fixed polynomial in N. The N=2 dictator exceptions have no retained edges and R_geell=0. Hence, for every fixed ell>=2, the supremum over all dimensions at cutoff s_* is exactly 2. Every finite value is below the supremum; no maximizing finite dimension is asserted.

The oriented retained quantity M_geell=sum_i sum_|T|>=ell p_(T+i) log2((p_T+p_(T+i))/p_(T+i)) has half of each equal-mass edge contribution. At this same endpoint its optimal ratio is exactly 1, with the same exceptions and limiting interpretation. This is only an endpoint calculation, not an upper bound for arbitrary Boolean signs.

The unrestricted oriented constant K_M is also strictly larger than its endpoint value 1. For each spectral edge x,y, its complementary entropy term satisfies x log2(1+y/x)<=y/ln 2; sum of all upper masses is I, so M>=B-I/ln 2. The positive atanh series gives ln 2>2/3, hence 1/ln 2<3/2. The same five-bit witness below has M/I>107/40-3/2=47/40>1. Thus the analogous arbitrary-cutoff extension of A096's oriented completeness statement also fails; its stated sublinear theorem is unaffected.

By contrast the unrestricted erasure constant K_E is strictly greater than 107/40, hence greater than 2: the actual five-bit negative set {5,12,13} has every relevant coordinate erasure ratio at least K5=16/3-(3/8)log2 3-(169/24)log2 13+(89/24)log2 89>107/40, independently accepted in A085's prior stage. The current checker independently recertifies this strict inequality on its exact Fourier masses. Thus extending A090's optimal-tail-constant equality from finite nonnegative sublinear s(N)=o(N) to all nonnegative cutoffs is false, even for the largest pointwise cutoff with a nonempty class in every dimension. No such extension is asserted by A090@1: its explicit o(N) hypothesis is essential, and the source theorem survives.

For completeness, the source sublinear-cutoff construction is dimension-safe. Fix a nonconstant seed with n variables and J=I(f)>0. Set eta_m=sup_{N>=mn} s(N)/N. Because s(N)/N tends to zero, eta_m is finite and tends to zero, even without monotonicity. For sufficiently large m set k_m=ceil(4(n+1)m sqrt(eta_m)+2sqrt(m)); k_m=o(m), N_m=mn+ell+k_m, and I(F_m)=2^-k_m(mJ+ell+k_m). Since J<=n and eventually eta_m<=1 and k_m<=m, s(N_m)<=eta_m[(n+1)m+ell], whereas k_m dominates this term plus log2(mJ+ell+k_m). Hence I(F_m)<=2^-s(N_m) eventually. The nonnegative pure-control tail term and retained qm B(f) imply liminf R_geell(F_m)/I(F_m)>=B(f)/I(f); R_geell<=B gives the reverse optimal-supremum bound. Fixed ell, nonconstant seed, eventual m, and sublinear s are all used. The endpoint s_* has s_*(N)/N tending to 1 and cannot be inserted in this argument.

The first unsupported universal line remains a finite dimension-independent bound on K_E (or the equivalent retained terminal-core KL payment). Neither the endpoint classification nor the source cutoff transport pays it. The endpoint result is a scope guard for proposed numerical-to-universal reductions, not a counterexample to FEI, A090@1 or A096@1.
