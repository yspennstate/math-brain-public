# Prime perturbations and the exact price of a summary

All physical inputs are independent uniform bits. A Boolean function takes values in {-1,+1}; H is the entropy in bits of its complete squared normalized Fourier spectrum, and I is the sum of its physical influences. Input Shannon entropy of a summary is a separate quantity.

## Independent reconstruction of A080 and A071

For any seed g on n>=1 bits, add k>=2 fresh bits, put N=n+k and set F(x,z)=g(x)b_N(x,z), where b_N is -1 precisely when the total Hamming weight is at most one. A physical block admits one Boolean summary precisely when its truth matrix has at most two different rows. Necessity follows because assignments with the same summary have the same row; sufficiency labels the two rows.

Every proper block A with |A|>=2 has at least three rows. Write B for its nonempty complement. If A contains two fresh bits, vary only these two bits to weights 0,1,2. The same seed row is multiplied by three different rows on B: a radius-one defect, a point defect, and the constant row. These are distinct even for |B|=1. If B contains two fresh bits, choose A assignments of weights 0,1,2 and restrict B to those fresh bits. The same three multiplier patterns are pairwise distinct even up to sign on a cube of dimension at least two; arbitrary seed signs cannot merge them. Otherwise k=2 with one fresh bit on either side, and A contains an original bit. Restrict to that original bit and the two fresh bits. The four rows, after naming their seed signs s,t, are s(--),s(-+),t(-+),t(++). If s=t they include both constant rows and a mixed row; if s=-t they include opposite mixed rows and a constant row. Thus three rows always remain. No seed relevance assumption is used. Every coordinate of F is relevant, since an irrelevant coordinate paired with another would produce a block with at most two rows.

The edit probability is epsilon=(N+1)2^-N. Parseval gives Fourier-vector distance 2sqrt(epsilon), and Cauchy-Schwarz bounds total variation d of the squared laws by 2sqrt(epsilon). A maximal coupling of the finite laws gives |H(F)-H(g)|<=h2(d)+Nd. Direct edges give |I(F)-I(g)|<=2N epsilon. For N>=6, N+1<=2^(N/2), so d<=delta=2^(1-N/4). With N=8(n+m+2), m>=1, delta<=1/2. The bound h2(delta)<=delta log2(1/delta)+2delta follows from -(1-t)ln(1-t)<=t and ln2>=1/2. Monotonicity up to delta bounds either error by 2N delta. A nonconstant seed has I(g)>=2^(1-n)>0, and

    (2N delta)/I(g) <= 2N 2^(n-N/4) <= 2^-m,

because s+2<=2^s for s=n+m>=2. Therefore R(F)>=(R(g)-2^-m)/(1+2^-m). Division uses a nonnegative numerator; a negative numerator is handled by R(F)>=0. Fixed-seed convergence follows directly, with no interchange of an infinite sum. The supremum of ordinary H/I on composition-prime functions equals the unrestricted FEI supremum, also if infinite. For the specific proper-partition bank of A080, all admissible blocks of a prime function are singletons, with H and nonnegative-K stopping hull zero. Its initial price is exactly H(F)+kappa I(F). Singleton partitions exist for every Boolean function, proving the optimized worst-case price C_FEI+kappa. This is initialization, not historical credit.

For the entire fresh block the residual state is r(z)=min(|z|,2). All three states occur for k>=2. Their rows are distinct for every seed by testing x=0 and a weight-one x. Thus two summary bits suffice and one does not. A071's u=1[z=0],v=1[|z|=1] have disjoint events, so Cov(u,v)=-k4^-k. Product-independent biased composition cannot be substituted for this law. The chain code 00,10,11 for the three states is optimal: each edge between different states changes exactly one bit. The state boundary has k+k(k-1)=k^2 undirected edges. Influence is undirected boundary divided by 2^(k-1), giving k^2 2^(1-k). These facts reconstruct the A071 claims without changing their statements.

## Any number of summary bits has the same minimum

Allow ANY deterministic r-bit summary E(z) from which the residual row can be decoded, including summaries that split a row class across different codes. For each physical edge crossing two different residual states, the endpoint codes must differ in at least one bit. Summing their Hamming distances gives

    sum_(j=1)^r I(E_j) >= k^2 2^(1-k).

For every r>=2 equality is achieved by the chain code and r-2 constant outputs. For r=1 no decoding exists. No independence, row-constant encoding or bounded r assumption enters the lower bound. Moreover H_input(E)>=H_input(r), since the state is a deterministic function of E; the chain code attains equality. This statement concerns input entropy only, not the sum of Fourier entropies.

## Exact original physical influence, including cancellation

Define D0=sum_i 1[g(0)!=g(e_i)] and D1=sum_(i!=j) 1[g(e_j)!=g(e_i+e_j)]. D1 counts undirected seed boundary edges from weight one to weight two once (their weight-one endpoint determines j). Then for every seed, including constants,

    I(F)=I(g)+2^(1-N)[N(N-1)-2kD0-2D1].

Proof: along any old coordinate i the seed derivative is unchanged unless the ball multiplier differs at the edge endpoints. This happens precisely when all remaining N-1 bits have weight one. There are k edges with fresh weight one and old weight zero, with derivative d_i(0), and one edge for each other original coordinate j with derivative d_i(e_j). On each such edge, replacing derivative d by 1-d changes its indicator by 1-2d. Each undirected edge has probability weight 2^(1-N). Summing old coordinates gives 2^(1-N)[n(N-1)-2kD0-2D1]. Along each of the k fresh coordinates the seed is constant, and exactly N-1 ball-boundary edges are pivotal, adding k(N-1)2^(1-N). Adding I(g) proves the formula. The old and fresh edge sets are disjoint by their coordinate, so no edge is omitted or duplicated. The formula uses the actual original total-influence owner.

For comparison, summing the convenient two-output u,v influences weighted by their outer activities gives k(N+1)2^(1-N), while actual fresh influence is k(N-1)2^(1-N). Their difference 2k2^(1-N) counts double flips that cancel at x=0. They cannot be booked as additional physical credit.

## A literal counterfamily to paying only the summary

Take the fixed two-bit seed g=-1 only at 00, so H(g)=2, I(g)=1, D0=2 and D1=0. For every integer k>=2 the literal Boolean circuit above satisfies

    I(F_k)=1+(k^2-k+2)2^(-k-1),
    min_E sum_j I(E_j)=k^2 2^(1-k),

where the minimum ranges over any finite number of decodable Boolean summary outputs for the entire fresh block. The entropy perturbation bound implies H(F_k)->2. More explicitly, for k>=32 (N>=34), 2N delta<1: at N=34, (4N)^4<2^N; the fourth-power successive ratio is ((N+1)/N)^4/2<1 because 35^4<2*34^4. Hence H(F_k)>1 for every k>=32. Consequently

    H(F_k) / min_E sum_j I(E_j) > 2^(k-1)/k^2 -> infinity.

This refutes the exact proposed inequality H(F)<=C sum_j I(E_j), with an absolute C for every such function and an optimally chosen decodable fresh-block summary. It refutes only the strategy of paying total entropy from the fresh summary alone. No other agent is asserted to have claimed this inequality. The full physical I(F_k) tends to one and H(F_k)/I(F_k)->2, so the same family does NOT refute FEI. The retained original seed is precisely the unpaid part.

## Checks, hypotheses and the remaining line

The finite audit includes constants, all labelled seeds n<=3, k=2,3, every proper block, direct character sums versus FWHT, and direct edges versus both Fourier influence and the new formula. Every two-bit vertex encoding for k=2,3 is enumerated, including split-class encodings. Missing-fresh-bit source controls show why k>=2 cannot be discarded; they are checked separately. The integer schedule checks cover a fixed 32x32 grid, not an all-dimensional theorem. The proofs above provide the all-dimensional arguments. A finite Lean check of the four-row Boolean alternative is attempted only after fresh compute admission; its status is separate from the analytic proof and no full-theorem formal verification is claimed.

First unsupported universal line: fund the retained arbitrary original core, including its source/reference, correlated residual law, old bookings and both full terminals, by ONE unused dimension-independent total-influence account. Optimizing the number or influence of summary outputs does not supply this payment. Full FEI remains OPEN. The new influence identity and counterfamily corollary have analytic proofs with exact finite validation; independent review is pending.
