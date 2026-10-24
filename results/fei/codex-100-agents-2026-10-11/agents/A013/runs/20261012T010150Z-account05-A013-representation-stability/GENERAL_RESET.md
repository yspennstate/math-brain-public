# Universal exact update for the inherited full-minterm cover

All entropies are in bits. Let f be any Boolean function on n>=1 coordinates, P(S)=fhat(S)^2, K=|S|, and Z=1{i in S}. Use the positive truth-table minterm cover, a common coordinate order with ranks r_j, and the canonical fixed first-gate tie. Every gate has width n and probability 2^-n. Every candidate gate has the same G_j(S), so all coordinates of a nonempty S are assigned to one gate. Consequently S_subset=0, L=Pr(K>0) log2 N (N is the number of positive inputs), and

T=(6/5)[sum_j Inf_j log2 r_j - E log2(K!)],
Q=E[n K 1{120K<11n}], R=T+Q.

If N=0, the function is constant and all nonempty costs are zero. Empty-dimensional terminal children also have zero nonempty costs. Restrict coordinate i, preserve the order of the remaining coordinates, and take the uniform average over the two actual signed children. Writing a_U=fhat(U), b_U=fhat(U+i), their coefficients are a_U+b_U and a_U-b_U. Thus their averaged squared spectrum is a_U^2+b_U^2, exactly the residual-set marginal of P. This identity does not assert that either physical child's spectrum is the marginal.

The exact rank reset is

avg T(child)-T(parent)=(6/5)[ E Z log2 K - Inf_i log2 r_i + sum_{j:r_j>r_i} Inf_j log2((r_j-1)/r_j) ].

Indeed, occupied later ranks decrease by one, the queried rank disappears, and log2(K!)-log2((K-Z)!)=Z log2 K. The exact rarity reset is

avg Q(child)-Q(parent)=E[(n-1)(K-Z)1{120(K-Z)<11(n-1)}-nK1{120K<11n}].

The label term contracts on average. Child counts N_+,N_- sum to N, and each is at most N. Their averaged nonempty spectral mass is Pr(K>0)-P({i}). Therefore avg L(child)<=log2 N [Pr(K>0)-P({i})]<=L(parent). Children of count zero are constant and contribute zero. This proof covers constant parent and N=1 without logarithms of zero.

For N>0 the original root odds are 2^-n/N, root probability 2^-n/(N+2^-n), and normalization cost Lambda_n(N)=N log2(1+2^-n/N). The vacuum-weighted term is Pr(K>0)Lambda_n(N). Each child uses its actual count and n-1; the exact average is the half sum of its own nonempty mass times Lambda_(n-1)(N_child), with zero for constant children. No count or root normalization is reset for free.

This is an all-dimensional transport identity, not a universal influence payment. DERIVATION.md exhibits an actual Boolean family for which the combined nonempty reset divided by queried influence is unbounded, and pays its positive rank, rarity, and normalization increments from one retained-core reserve. The first unsupported line is a corresponding single-use reserve for arbitrary covers and physical descendants, with terminal entropy retained.
