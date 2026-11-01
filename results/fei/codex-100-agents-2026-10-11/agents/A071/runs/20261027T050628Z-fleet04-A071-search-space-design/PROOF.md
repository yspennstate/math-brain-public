# A cheap two-output summary retains the arbitrary seed

All inputs are independent uniform bits. Fourier entropy H is in bits of the COMPLETE squared normalized Fourier spectrum. I counts every physical coordinate. Full FEI remains open.

## 1. Reconstructing the reviewed reduction

Let g be any Boolean sign function on n>=1 coordinates, k>=2, N=n+k. Put F(x,z)=g(x)b_N(x,z), where b_N is negative exactly when |x|+|z|<=1. A block has a one-output Boolean summary exactly when its truth matrix has at most two distinct rows: equal summary outputs force equal rows; conversely label the at most two row classes by signs.

Here is an independent cut-based reconstruction of A080-COMPOSITION-PRIME-APPROXIMATION@1. For a proper block A with |A|>=2, write B=A^c. If A has two fresh coordinates, use only these coordinates to give its assignments weights0,1,2. The seed row is fixed. The multiplier rows on B are negative on |B|<=1, on B=0, and nowhere. Since B is nonempty, these give three different rows. If B has two fresh coordinates, use A assignments of weights0,1,2 and restrict B to those fresh coordinates. The three multiplier rows are respectively a radius-one ball, a point defect, and a constant. On at least two bits they are distinct even up to sign; arbitrary seed signs cannot identify them. If neither side has two fresh coordinates, k=2 and each side has one. A must have an original coordinate. Vary it and the fresh A coordinate, restrict B to its fresh coordinate, and obtain four rows s(--),s(-+),t(-+),t(++). If s=t, the first, second, fourth differ; if s=-t, the first, second, third differ. Hence all proper nonsingleton blocks have at least three rows. Constants and dummy seed coordinates are allowed. Every physical coordinate of F is relevant, since an irrelevant coordinate paired with any other would give a two-row block.

For two N-bit signs differing on probability epsilon, their Fourier vectors a,b satisfy ||a-b||_2=2sqrt(epsilon) by Parseval. The squared laws have total variation d <= ||a-b||_2 ||a+b||_2/2 <=2sqrt(epsilon). Coupling their common masses gives |H(a^2)-H(b^2)|<=h2(d)+d log2(2^N-1). A physical edge can change disagreement only if either endpoint is edited, so each influence changes by at most2epsilon. Here epsilon=(N+1)2^-N, and the padded seed has exactly H(g),I(g).

The source's quantitative schedule checks as follows. N>=6 implies N+1<=2^(N/2) (base6; successive ratio at most8/7<sqrt2). Thus d<=delta=2^(1-N/4). At N=8(n+m+2), m>=1, delta<=1/2. Since ln2>=1/2, h2(delta)<=delta log2(1/delta)+2delta. Monotonicity on [0,1/2] bounds the entropy error by2Ndelta=4N2^(-N/4). The same quantity bounds influence error because epsilon<=delta. A nonconstant n-bit sign has at least one disagreeing undirected edge, so I(g)>=2^(1-n)>0. With s=n+m>=2, division gives relative error at most

    2N 2^(n-N/4)=16(s+2)2^(-n-2m-4)<=2^-m,

using s+2<=2^s. Thus H(F)/I(F)>=(H(g)/I(g)-2^-m)/(1+2^-m). The denominator is positive. If the numerator is negative, use H(F)>=0 rather than reversing division inequalities. For a fixed seed both errors tend to zero, proving ratio convergence. No limit is exchanged with a dimension-dependent sum.

For the source's bank corollary, a prime function has only singleton proper disjoint scalar partitions. A singleton's complete entropy and true nonnegative-K stopping deficit hull are zero, including constant restrictions. Its bank is therefore exactly H(F)+kappa I(F). Arbitrary functions always have a singleton partition with that price. Taking suprema, using approximation of every fixed seed, proves the source's exact identity C_FEI+kappa, also when the supremum is infinite. No initial payment follows from this identity. Verdict: source statement HOLDS unchanged, with digest pinned in REVIEW.json. A071's antecedent row criterion is disclosed; this stage supplies a separate reconstruction of A080's arbitrary-seed argument, not an independent review of A071's own antecedent theorem.

## 2. Exact three-state summary

Define 0/1 outputs u(z)=1[z=0], v(z)=1[|z|=1]. For every physical input,

    F(x,z)=g(x){1-2[1[|x|<=1]u(z)+1[x=0]v(z)]}.

Only pairs (u,v)=(1,0),(0,1),(0,0) occur. Their probabilities are 2^-k,k2^-k,1-(k+1)2^-k. All three are positive for k>=2. Fixing x=0 and an original weight-one assignment shows the three residual rows are distinct for EVERY g. Thus exactly three rows occur on the full fresh block, and two Boolean outputs are necessary and sufficient (one is impossible by pigeonhole). The unused fourth output pair has no physical meaning. In particular u,v are not independent: their product is always zero and Cov(u,v)=-k4^-k<0. A product-biased composition formula cannot be applied without a new coupling argument.

Let U=1-2u,V=1-2v be Boolean signs. The point event has k boundary edges. The weight-one event has k edges to zero and k(k-1) edges to weight two. Dividing undirected boundary counts by2^(k-1) gives

    I(U)=k2^(1-k), I(V)=k^2 2^(1-k).

Their sum tends to zero. Their individual Fourier entropies also tend to zero: for an event of density p the nonempty Fourier mass of its sign is w=4p(1-p), so H<=h2(w)+kw. For p=2^-k and p=k2^-k, both w and kw tend to zero. The INPUT Shannon entropy of the pair is separately h2(q)+q h2(1/(k+1)), q=(k+1)2^-k, and also tends to zero. These are three different quantities; none is substituted for the complete physical H(F).

Each fresh physical coordinate of F is pivotal precisely when all other N-1 coordinates have weight one. The seed is unchanged along that edge and has square one. Therefore

    I_fresh(F)=k(N-1)2^(1-N).

If one instead sums the two summary-output influences weighted by their outside activities, the price is

    W=(n+1)2^-n I(U)+2^-n I(V)=k(N+1)2^(1-N).
    W-I_fresh(F)=2k2^(1-N)>0.

The excess is exact, not a rounding error. At x=0, an edge from z=0 to a weight-one z flips BOTH summary outputs while F keeps the same sign. At original weight one only u is active, so there is no such cancellation. This accounts for every extra edge. No overlap or output fee is charged twice as physical influence in the displayed exact I_fresh.

The optimal TWO-output encoding has an even smaller exact total influence. Put a(z)=1[|z|>=1], c(z)=1[|z|>=2]. The three row states have codes00,10,11. Each edge between different row classes changes exactly one output; all other edges change none. There are k edges from weight0 to weight1 and k(k-1) edges from weight1 to weight2. Hence the sum of output influences is k^2 2^(1-k). Every valid two-output summary, even one that splits a row class across several codes, MUST assign different codes to different row classes. Each of those same edges therefore changes at least one output. This proves the matching lower bound without assuming row-constant coding. Thus k^2 2^(1-k) is the exact optimal sum. The earlier u,v encoding is a convenient algebraic representation, not the optimal influence encoding. The two formulas refer to different encodings and their difference is k2^(1-k).

## 3. Universal scope and the target falsifier

For every delta>0 and nonconstant seed g, sufficiently many fresh bits make H(U)+H(V)+I(U)+I(V)+H_input(u,v)<delta and |H(F)/I(F)-H(g)/I(g)|<delta. This follows from the limits above and I(g)>0, with g fixed. Thus the supremum of ordinary H/I over composition-prime functions admitting an arbitrarily cheap three-state fresh-block summary is STILL exactly C_FEI. Subclass inclusion proves one direction; approximation of each fixed seed proves the other, including infinity. No divergent seed is supplied.

The bounded family therefore falsifies the proposed extension 'composition-prime implies no proper two-output compression': n=1,k=2 and ANY seed already have a three-row fresh block. This proposal is a strategy-level test, NOT a claim attributed to A080, whose source explicitly excludes multiple-output summaries. More usefully, the all-dimensional construction shows that merely obtaining a cheap bounded-output summary does not remove the arbitrary seed from the outer function: at state(0,0) the outer function is exactly g. A paid outer entropy/reference theorem would still be needed. The exact frozen domain tests the geometry and cost accounting; it cannot certify a universal payment.

First unsupported full-FEI line: a noncircular ORIGINAL O(I) source for the arbitrary retained outer seed, closed under whatever histories/correlated summaries the rule requires, with old debits and BOTH full terminals retained. The proof above establishes a reduction and a false-route diagnostic, not such a source.
