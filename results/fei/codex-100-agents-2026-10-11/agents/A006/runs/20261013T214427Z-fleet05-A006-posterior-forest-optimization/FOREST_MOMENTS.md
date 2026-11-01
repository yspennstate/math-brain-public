# Actual-run determinant and factorial-moment calculation

Fix one nonempty covered set A and a coordinate-to-gate assignment tau. Retain only used gates V. All hypotheses, gate supports, orders, positive feasible lambda and rarity pi are those of forests.tex. Put g=|V|, c=number of source SCCs of the directed graph u->v iff u!=v and A_u intersects R_v, and e=g-c. Base-two costs are used.

Let b_tau be 2 to the negative of the NONROOT terms of eq:forestcost:

    b_tau = product_used [lambda_l M_l^(-s_l) (s_l/kappa_l)^(gamma s_l)]
            * product_(j in A) exp[-gamma F_tau(j)^j(A)].

This is independent of parent, root, attachment and chronological child choices. It is positive, generally algebraic for gamma=6/5; no rationality of b_tau is presumed.

Introduce a variable x_(u,j) for every j in A_u. Set w_uv(x)=sum_(j in A_u intersect R_v) x_(u,j), u!=v. The incoming Laplacian has L_vv=sum_(u!=v)w_uv and L_vu=-w_uv. A root set R is permissible exactly when it selects one vertex in every ORIGINAL source SCC and no others. Define

    T_tau(x)=sum_permissible_R [product_(r in R) pi_r] det L_(V\R,V\R)(x).

The empty determinant is 1. Graph/SCC/root choices are determined using the original positive incidence graph, not a graph obtained by zeroing variables.

## Minor identity, proved directly

Each nonroot row v is sum_u w_uv times the restriction of (e_v-e_u) to nonroot columns. Multilinearity selects one parent u for each nonroot v. If the resulting parent graph contains a nonroot directed cycle, its cycle rows sum to zero and its determinant vanishes. Otherwise every parent chain ends at a root. Ordering nonroots with parents first gives a triangular matrix with diagonal 1 (the simultaneous row/column permutation has no net sign). Thus the minor is exactly the generating polynomial of outgoing rooted spanning forests, with an edge weight w_uv. Expanding each w chooses one attachment j. This proves the identity without an external determinant theorem.

## Actual-run identity

For each attached forest let h_(u,j) be its number of distinct children of u attached at j. The source chooses the attachment MULTISET, then orders occurrences deterministically. Exactly h_(u,j)! distinct sequences of child gate labels can occupy the slots of coordinate j. Choices at different groups are independent, giving multiplicity product h!. No permutation is allowed between distinct attachment coordinates or between initial roots. BFS queue order is then determined. Every resulting event has positive probability, visits each used gate once, and outputs A.

Conversely an actual once-per-gate queue event uniquely recovers tau, root set, parents, attachments, and the child sequence at each repeated coordinate. Thus this construction is injective; different graph descriptions do not become extra runs. If a table itself repeats identical gate functions, gate IDs still describe distinct outcomes of its fixed generator. The theorem needs no repeated gates; the main exact test uses distinct prime gates only.

Let M be the linear map on polynomials taking a monomial product x_(u,j)^h_(u,j) to product h_(u,j)!. Equivalently M(T)=E T(X) for independent rate-one exponential variables, since integral_0^infinity t^h exp(-t)dt=h! by induction/integration by parts. Then

    sum_actual_runs_with_tau 2^(-B(A;r)) = b_tau M(T_tau).

Different tau have disjoint actual run sets, so S(A)=sum_tau b_tau M(T_tau). The already-known finite variational identity yields inf_eta [E B-H(eta)]=-log S(A), attained by eta(r)=2^(-B(r))/S(A). This calculation concerns the surrogate B residual; it is NOT an identity for exact queue probabilities q(r), which contain additional size, count and normalizer factors. The source's universal K_ref I overhead remains.

## Computable determinant bounds

Let T_can=T_tau(1). It uses one canonical child sequence at each repeated attachment. Since h!>=1 and sum h=e, product h!<=e!, so

    T_can <= M(T_tau) <= e! T_can.

For a sharper rational upper bound let D_(u,j) be the number of eligible child gates v!=u containing j. For D>=1 put a_D=(D+1)/2, and put a_0=1. For every integer 0<=h<=D,

    h! <= ((h+1)/2)^h <= a_D^h,

where the first inequality is AM-GM on 1,...,h (h=0 handled separately). More sharply any certified rational a_D >= (D!)^(1/D) works, because (h!)^(1/h) is increasing: multiplying by h+1 increases the geometric mean. Evaluate the same determinant polynomial at x_(u,j)=a_D to obtain T_up. Then

    T_can <= M(T_tau) <= U_tau=min(e! T_can,T_up).

All T quantities are exactly rational for rational pi and rational chosen a_D. Summing b_tau T_can and b_tau U_tau gives lower/upper bounds for S(A) and reversed -log bounds on the optimized cost. Algebraic b_tau and logarithms can be enclosed outward separately; they are not declared rational. One fixed assignment alone gives an attainable upper cost -log(b_tau T_can). The canonical posterior assigns weights proportional to product root pi among these distinct canonical runs. If all D<=1, the lower and upper bounds coincide. No universal O(I) estimate follows from the worst-case log(e!) gap.

The e! factor is sharp within ACTUAL prime tables. For the monotone sunflower OR_i(x0 AND xi), use e+1 gates, A={0,x2,...,x_(e+1)}, tau(0)=1 and tau(xi)=i. The graph is the forced outgoing star from gate 1; all e children attach at 0, giving exactly e! actual child sequences but one canonical sequence. Lambda=1/(e+1), pi=1/4 are feasible. This A has nonzero Fourier mass. The count is independent of those values.

## SCC factorization and its boundary

Topologically order SCCs of the original graph. L is block lower triangular, and deleting one row/column in each source SCC preserves this structure. Non-source diagonal blocks retain all incoming weights from outside their SCC. Consequently

    T_tau(x) = product_(nonsource C) det L_C,C(x)
               * product_(source C) sum_(r in C) pi_r det L_(C\{r},C\{r})(x).

Thus T_can and T_up can be computed in polynomially many exact determinant operations once tau is fixed; root-set enumeration is unnecessary. This does NOT make the sum over assignments polynomial, nor make exact polynomial moment computation polynomial. It is invalid to take separate expectations of the SCC factors: a parent-coordinate variable can feed several different target SCCs. The three-gate star above gives T=pi_1*x_(1,0)^2. Its true moment is 2pi_1, whereas multiplying expectations of its two non-source SCC factors gives pi_1. The deterministic factorization is exact; factorization of its expectation is false.

## Universal boundary

The first unsupported PI-J line remains a dimension-independent bound

    v log[product_l(1+lambda_l pi_l)-1] - E_P log sum_tau b_tau M(T_tau) <= K I(f)

for one globally fixed prime-table reference for each arbitrary Boolean f. The determinant/moment calculation computes the correct forest mass and certifies surrogate optimization bounds; it supplies neither this expectation bound nor a dimension-independent log(e!) bound. NEXT should apply weighted determinant lower masses to A009's off-support error sector with its complete cost ledger, asking whether moment credit reduces the density-sensitive error budget; no rerun of affine-plane FEI is required.
