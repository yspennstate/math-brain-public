# Complete-graph prime DNF: matching mass and global fixed-posterior optimum

Let n>=4 and f_n be the OR of all positive two-variable conjunctions, one per edge of K_n. These are exactly its prime implicants. Thus f_n=1 iff at least two input bits are positive. There are N=n(n-1)/2 gates, read n-1, rarity pi=1/4. Each gate has BOTH endpoint orders in its fixed ordered cover (M=2). The original generator then has theta_s=1 at both endpoints for s=1,2. Its exact size/subset probabilities are t(singleton)=1/4 and t(pair)=1/6. Set lambda=1/(n-1) globally and D=(1+1/[4(n-1)])^N-1. All costs below are bits.

## Actual events and exact mass

For a nonempty spectral set A of size a, define a selected actual-run family as follows. For even a, use every perfect matching of A, select each matched pair at its edge gate, and make all gates roots with zero children. For odd a<n, choose one singleton j in A, one k outside A, and a perfect matching of A minus j. Select {j} at gate {j,k}; use all gates as roots, with zero children. For odd a=n, choose singleton j, a perfect matching of A minus j, and one k in A minus j. Gate {j,k} owns {j}; its parent is the matching gate owning k. All matching gates are roots, and this parent draws exactly one child at attachment k; every other gate has zero children. Use the fixed original root and attachment orders.

These are source-SCC partition forests: in the first two cases used supports are disjoint, and in the last case the only incidence between used gates points from the unique parent to the singleton gate. Every event uniquely recovers its owned subsets, matching, singleton, and attachment. Consequently the counts below are distinct actual queue events, not description multiplicities. They are a subfamily of A008 Q_part. No permutations of root order or distinct attachment slots are counted.

Put L=48(n-1), J=32(n-1), m=floor(a/2), and use (-1)!!=1. One pair-root/zero-child contributes lambda*pi*(1/6)*(1/2)=1/L. One singleton-root/zero-child contributes 1/J. For the odd full-set case, replacing a parent zero-child count by count-one and its one-of-two attachment costs (1/6)/(1/2)/2=1/6. A singleton child contributes lambda*(1/4)*(1/2)=lambda/8. Their product is lambda/48=1/L. Hence the exact conditioned output mass of the selected family is W_a/D, where

    a even:       W_a=(a-1)!! / L^(a/2),
    a odd, a<n:   W_a=a(n-a)(a-2)!! / (J L^((a-1)/2)),
    a=n odd:      W_a=n(n-1)(n-2)!! / L^((n+1)/2).

This is an explicit lower bound for the complete determinant mass, with all sizes, subsets, child counts, attachments, root rarities, labels and output ambiguity retained. In particular it is not a surrogate factorial moment. Every selected event has the same probability for fixed A, so its exact conditional posterior eta_A is uniform. Thus E_eta[-log q]-H(eta)=-log(W_a/D).

## All-dimensional influence payment

For all cases W_a>=m!/L^(m+1), since (2m-1)!!>=m!, J<=L and the additional integer multiplicities are >=1. At m=0 interpret m log(L e/m)=0. The elementary factorial estimate m!>=(m/e)^m gives

    -log(W_a/D) <= log D + m log(48e(n-1)/m) + log(48(n-1)).

Here log D<=n/(8 ln2)<n/4, m<=n/2, log(48e)<10, m log((n-1)/m)<=n/ln2<2n, and log(48(n-1))<=2n for n>=4. The latter follows from 48(n-1)<=4^n at n=4 and induction. Therefore every nonempty set costs <=37n/4 bits. This deliberately coarse bound includes the signed normalizer even when D<1.

With r=(n+1)2^-n, the actual Boolean spectrum is

    P(A)=4^(1-n)(n+1-2|A|)^2  (A nonempty),
    v=4r(1-r),  I=n(n-1)2^(1-n).

The spectrum follows by expanding the indicator of zero or one positive bit; I follows by counting pivotal inputs with exactly one other positive bit. Thus nv/I=2(n+1)(1-r)/(n-1)<=10/3 for n>=4. The complete nonempty spectral cross-entropy C_match is <=185 I/6<31 I. In particular its off-support part (sets not contained in any edge, equivalently |A|>=3) obeys the same bound. This replaces the raw indicator-sum error charge by a complete mass certificate at all densities N/4, which diverge with n. This is a coding result for an already-known threshold family, not a novel FEI class or a universal theorem.

## Global weight optimum for this frozen posterior

Freeze the just defined eta_A at uniform lambda; thereafter vary only one global positive feasible weight vector. Write c_l=sum_A P(A) Pr_eta(l used). Each run has g(A)=ceil(|A|/2) used gates. The complete probability factors as q(r;lambda)=k_r product_used lambda_l/D(lambda), where k_r is independent of lambda. Therefore the frozen-posterior natural-log objective is a constant plus

    F(t)=v ln D(exp t)-sum_l c_l t_l,
    sum_(l incident j) exp(t_l)<=1.

This is convex: D is a positive sum of nonempty root-set monomials, so ln D(exp t) is log-sum-exp. Symmetry of the TWO-order reference and selected run family gives c_l=c0=(1/N)sum_a binom(n,a)P_a ceil(a/2). Put p=1/(4n-3), Z=1-(1-p)^N and rho=p/Z. These are rational and are the marginal probabilities for the normalized nonempty root-subset law. The gradient at uniform weights is v rho-c0.

It is strictly negative. Indeed sum c_l/v>=I/(2v)=n(n-1)/[4(n+1)(1-r)], while N rho=Np/Z<=1+Np<1+n/8. For n>=12, n(n-1)/[4(n+1)]>=1+n/8 follows from n^2-11n-8>=0. For each n=4,...,11, substitution into the finite rational c0 and rho formulas verifies c0-v rho>0; these eight certificates are saved. The bound Np/Z<=1+Np follows from (1-p)^(-N)>=(1+p)^N>=1+Np.

Choose the same rational coordinate price y_j=(n-1)(c0-v rho)/2>0. Each edge meets two coordinates, so its log-incidence derivative is lambda*(y_j+y_k)=c0-v rho. Thus gradient plus incidence-price derivative is zero at every gate. Every incidence constraint is tight. Convexity and these exact KKT identities prove uniform lambda is a global minimizer for the frozen posterior, over all positive feasible vectors.

The c0 formula, v, rho and prices are rational for each n. No floating optimization is needed. This is not a global optimum when the posterior is allowed to change with weights, nor a certificate for the coordinatewise outer-pressure objective.

## Exact remaining line

For an arbitrary simple graph G of maximum degree Delta>=1, the same globally fixed two-order edge reference and lambda=1/Delta give an exact matching-sector lower mass. Write pm(B) for the number of perfect matchings of the induced graph G[B], with pm(empty)=1. Put L=48 Delta, J=32 Delta and D=(1+1/(4 Delta))^|E|-1. For even a the unnormalized mass is pm(A)/L^(a/2). For odd a=2m+1 it is

    sum_(j in A) deg_(outside A)(j) pm(A minus j)/(J L^m)
      + sum_(j in A) deg_(inside A)(j) pm(A minus j)/L^(m+1).

The two terms use exactly the external-singleton-root and internal-singleton-child events proved above; they are disjoint and every internal neighbor k has a unique matching parent. Dividing by D gives a complete output subprobability and a lower bound on A008 Q_part. This is valid for every graph, including unbounded read, but can be zero on positive spectral mass. On the prime star edges {0,1},{0,2},{0,3}, A={1,2,3} has P(A)=1/64 and matching-sector mass zero. This refutes only the attempted all-graph positivity extension: general whole-set forests still have positive mass. The raw approximation G=2 sum_edge b_edge-1 also has zero coefficient at that A, so this is genuinely an off-support error sector.

For arbitrary Boolean prime tables the matching count and symmetric spectrum are absent. The first unsupported extension is an influence-paid expectation of -log Q_part(A) for one globally fixed feasible table and weights. Even the dense equal-width linear-hypergraph extension lacks an analogue of W_a large enough on the true off-support spectrum. No bound on the raw indicator-sum approximation at arbitrary density is asserted.
