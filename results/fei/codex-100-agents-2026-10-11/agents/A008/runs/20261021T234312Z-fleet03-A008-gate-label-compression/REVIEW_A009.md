# A009 private-leaf complete-payment v1: whole independent reconstruction

Verdict: HOLDS at its original whole scope, without a substantive repair. The reviewed statement is A009-ARBITRARY-CORE-PRIVATE-LEAF-COMPLETE-PAYMENT v1, SHA256 cd8869084544f2c5c76e5421dbb16060f797fe3188fc2fcc61f9705b273663a2. This local review does not change a shared registry or presume supervisor adoption.

The source hashes canonical compact sorted JSON of its statement AND hypotheses, not statement text alone (A009 code/finalize.py:16). The initial validator's wrong raw-text convention is preserved in out/HASH_CONVENTION.json; the source digest is retained and checked with its actual convention. This is a validator correction, not a mathematical proof repair.

The original claim quantifies over every finite core on r>=1 named hubs and every vector m_i>=1 of genuine private degree-one leaves. Both endpoint orders, the full edge prime table, its one fixed feasible weighting, actual uniform Boolean spectrum, original queue and ideal nonempty reference cost are retained. It asserts C_PL<843I/80<11I, not a universal graph bound or an output-prefix rounding payment.

## Reconstruct the queue, rather than just its final inequality

Conditioned initial-root probability is product_(root e)(lambda_e/4)/D with D=product_all_edges(1+lambda_e/4)-1. The common denominator includes every core gate's absent-root factor. An isolated singleton root pays subset probability 1/4 and zero-child probability 1/2, hence lambda/32. In a private block with no selected hub, every selected leaf must be such a root. If only the hub is selected, summing over m distinct private root names gives m lambda/32=1/64.

With the hub and t>=1 leaves selected, choose one of the t leaf gates as the pair root. Its pair probability is 1/6. Its c=t-1 children all attach at its hub coordinate. Count probability is 1/[t(t+1)], attachment multiset probability 1/t, and each singleton child has factor lambda/8 before its parent factors. There are (t-1)! different chronological child-label orders for each root choice. Their summed numerator is exactly t! lambda^t/[24*8^(t-1)*t^2*(t+1)]. Root order between blocks is fixed and earns no further permutation factor.

Every gate is visited once, each owned subset is determined at that visit, and distinct root identities or child chronologies are distinct original random events. The decoder follows the queue and unions its owned subsets. Across private blocks the visited supports are disjoint; unused core gates create no arc. Thus their source-SCC forest property is valid and the products of block numerators aggregate actual disjoint events. At the normalized actual-event posterior, subtracting witness entropy gives -log2 Q_PL(A). No latent gate name is counted twice and no final-output ambiguity is discarded.

The elementary bound (c+1)^2(c+2)<=2*6^c is equality at c=0,1 and follows afterwards by consecutive ratios. It gives the claimed U_h(t)>=96^(-h-t)m^(-t), including t=0 and h=0. Consequently C_PL<=v log2 D+(log2 96)I+sum_i I_(leaves i)log2 m_i. This uses only actual Fourier marginals P(i in A)=Inf_i, without a product-spectrum assumption.

## Reconstruct every physical and normalizer charge

Let a_i=Pr(false,hub_i=-1), b_i=Pr(false,hub_i=+1). Genuine privacy makes its leaves fair and independent under the false event with hub_i negative. Flipping the hub positive requires all m_i leaves negative and its core neighbors negative, so b_i<=2^-m_i a_i. Monotonicity gives Inf_hub=2(a_i-b_i)>=a_i and >=2q/3. A private leaf is pivotal exactly on the corresponding positive-hub false state, giving Inf_leaf=2b_i. Thus its label charge is <=2m_i 2^-m_i log2(m_i) Inf_hub <=9Inf_hub/4, because log2 m<=m and m^2 2^-m<=9/8. The latter is checked at m=1,2,3 and decreases thereafter.

Private weights sum to r/2. Each core row uses at most 1/2, so core weights sum to at most r/4. Hence ln D<=sum lambda/4<=3r/16. Since v<=4q and I>=2rq/3, v log2 D<=9I/(8 ln2), including the signed D<1 case. Summing the three charges gives the exact original coefficient. The rational strict comparison is log2 96<33/5, ln2>2/3, and 33/5+9/4+27/16=843/80<11. No step requires a positive lower bound on q independent of dimension; q>0 follows from the all-negative input.

## Independent tests and scope challenges

The new checker imports no author code. It constructs physical truth tables, integer Walsh transforms, exact influence counts, all feasible weight rows, complete block queue probabilities, reference masses and physical payment identities on all 74 labelled cores with r=1,2,3 and m_i in {1,2}. Every nonempty output set is checked, including zero-spectral sets; each whole reference sums to at most one. The pilot covers ten of these cases separately. All decisions use integers or Fraction. Scalar bounds are checked through m=128; their all-m proof is the induction above, not extrapolation.

Privacy cannot be omitted: in K_(r,m), for a named hub b/a=2^(r-1)/(2^m+2^(r-1)-1). At (r,m)=(3,2) this is 4/7, exceeding the proposed private factor 1/4; the exact checker retains four such witnesses. They refute that attempted substitution, not A009's statement. If m_i=0, its chosen hub-only private root is also absent; both coverage and the conditional inequality need replacements.

ROOT_PAYMENT.md is a separate improvement and is not used to repair or accept this original proof. It subsequently substitutes a universally valid root bound into the unchanged accepted reference to obtain C_PL<399I/40<10I. A008 contributes to that new deduction and cannot serve as its independent referee.
