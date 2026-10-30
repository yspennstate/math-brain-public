# Exact joint posterior/weight optimization along one gate

Fix ANY finite original forests.tex reference and a fixed finite family of distinct actual partition-forest events that visits every used gate once, with positive output mass on every nonempty positive-spectral A. The table, covers, event family and rarities pi are fixed once from f. Keep every weight except gate e fixed, positive and feasible. Let its varying weight be beta in (0,L], where L is the smallest residual incidence capacity over coordinates in R_e. Assume L>0. The true Boolean spectrum P is fixed from f, not replaced by a model law. All costs are bits unless natural units are explicitly used. The graph maximal-matching star family with both endpoint orders and pi=1/4 is the fully rational certified application below; arbitrary support width and overlap are allowed in the analytic theorem.

Because each DISTINCT actual run visits every used gate once, its unnormalized complete probability is k_r product_used lambda, with k_r containing every size/subset/count/multiset/root-rarity factor. For each nonempty positive-spectral A write

    W_A(beta)=a_A+b_A beta,

where a sums events not visiting e and b sums their coefficient for events visiting e. These coefficients are nonnegative; a+b beta>0 for beta>0 by the star-completion coverage proof. Coincident occupations contribute their full summed coefficients, never one description per occupation. The exact complete mass is Q_A=W_A/D. Hence the conditional posterior is genuinely allowed to CHANGE with beta; this is not A009's frozen-posterior objective.

For at least two gates, put d=product_(g!=e)(1+lambda_g*pi_g)-1>0, j=pi_e*(1+d), and D(beta)=d+j beta. Define the normalized initial-root marginal

    r=j beta/(d+j beta),  R=j L/(d+j L)<1,
    beta=d r/[j(1-r)].

The same complete output mass becomes the positive affine function

    Q_A(r)=q0_A+(q1_A-q0_A)r,
    q0_A=a_A/d, q1_A=b_A/j.                              (1)

This algebra pays the entire signed root normalizer, instead of leaving it as a second nonlinear term. Do NOT call q1 a probability reference or a separate generative mixture component: beta beyond L can violate packing, and q1 need not sum to <=1. Only Q(r) for 0<r<=R is known to be an actual output subprobability. The change of coordinate is certificate arithmetic, not a sampled-set-dependent reference or a free selector.

## Full conditional continuum and boundaries

Let v=sum_nonempty P(A). The complete spectral cost after optimal actual posterior aggregation is

    C(r)=-sum_nonempty P(A) log2 Q_A(r).                 (2)

In natural units define G(r)=-sum P log Q, z_A=q1_A-q0_A. Then

    G'(r)=-sum_A P(A) z_A/Q_A(r),
    G''(r)=sum_A P(A) z_A^2/Q_A(r)^2 >=0.                (3)

It is STRICTLY convex unless every z_A=0 on positive spectrum. Thus the entire feasible one-edge JOINT posterior/weight problem is settled by exact derivative signs: if all z=0, every beta has the same cost. Otherwise, if G'(R)<=0 the unique minimum is beta=L. If all q0_A>0 and G'(0)>=0, the infimum is at beta->0; beta=0 is excluded by strict positive weights, so there is no attained positive minimum on this slice. In every other case with G'(R)>0, there is exactly one interior zero of G', giving the unique attained minimum. If some q0=0 on positive P, G(r)->infinity and G'(r)->minus infinity as r->0, so the interior/upper cases cover that boundary. The one-gate table has d=0 and its conditioned output mass is independent of beta, a separate constant case.

In particular, the positive attainment proved for A009's FROZEN posterior cannot simply be reused for this joint problem. A frozen-law global gap is not a gap for arbitrary changing posterior, and a coordinate minimum is not a global all-weight or all-posterior optimum.

## Computable exact certificates, retaining witness entropy

For rational complete event coefficients (as in the two-order width-two graph reference), rational fixed weights and the uniform Boolean cube, P,a,b,d,j,R and every rational derivative sign are exact rational numbers. General original subset factors can be algebraic; they are not declared rational, and would require certified coefficient/sign enclosures or exact algebraic comparisons. Multiplying the denominators of G' produces a polynomial of degree at most the number of positive-spectral sets minus one; all denominators are positive inside the feasible interval. Exact bisection of the monotone derivative therefore isolates the unique interior optimum without a numerical sign. Boundary behavior is classified analytically, not silently discarded.

For a rational test point t in (0,R], let

    mu=sum_A P(A) z_A^2 / max(q0_A,Q_A(R))^2.

If the slice is nonconstant, mu>0 and G''>=mu throughout the feasible interval. Strong convexity gives

    G(t)-inf G <= G'(t)^2/(2mu).

Since ln2>1/2, its BIT gap is at most G'(t)^2/mu, entirely rational. The ordinary supporting-line certificate also gives a bit gap at most

    2*max(G'(t)*t, -G'(t)*(R-t), 0).                  (4)

Use the smaller certificate. This handles a strictly positive approximant to a zero-boundary infimum, where (4) tends to zero whereas the squared-gradient bound may not. A certified sign bracket plus these rational gap bounds provides a concrete continuum certificate. No floating-point optimizer, root-subset independence, or log approximation is needed for the GAP; certified logarithms are needed only if reporting the value of C itself.

At beta0 the old event posterior eta0_A(r) is normalized by W_A(beta0). At beta1 the frozen-law cost exceeds the new optimized output cost by the EXACT expected KL of eta0 to eta1. This existing variational identity is not presented as new; it explains why the new certificate applies to the joint slice and why A009's frozen-law lower bound need not. On one edge, the KL reduces to the binary membership variable 'run visits e': within either membership class, the normalized event law does not change with beta. Its probability is beta*b/(a+beta*b). This credits genuine distinct events, not occupation descriptions, and includes the deterministic one-membership cases by limits.

## Universal bridge and first unsupported line

This solves EVERY one-gate conditional weight continuum with its posterior reoptimized, for any such finite actual partition reference and any fixed positive remainder, including arbitrary support width. It supplies exact rational certificates on graph references with overlapping scales, including a coordinate connected to several matching occupations. Repeated coordinate minimization can improve an actual globally fixed reference, but the simultaneous multi-gate objective need not be convex and a collection of coordinate gaps is not a global gap. The first unsupported PI-J line is still a dimension-independent bound on the complete expected occupation cost for one globally chosen feasible weight vector on arbitrary Boolean spectra. NEXT should couple exact membership refunds and the occupation factorial bill across two incident weight coordinates, or give its first exact joint nonconvexity obstruction, while preserving the same actual output mass and signed normalizer. No new universal constant or FEI theorem follows from this slice theorem.
