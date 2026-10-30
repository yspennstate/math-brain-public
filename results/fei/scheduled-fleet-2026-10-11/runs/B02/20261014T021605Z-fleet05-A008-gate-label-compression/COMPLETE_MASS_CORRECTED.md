# Complete queue mass for shared labels

Fix the original forests.tex generator, a nonempty covered A, and an eligible assignment tau. Write A_u for the nonempty owned subsets, V for used gates, s_u=|A_u|, g=|V|, and D=product_all_gates(1+lambda_l*pi_l)-1. Fix the original supports, orders, weights and table before sampling A. Define the original subset draw probability

    t_u(A_u) = [1/(s_u(s_u+1))] product_(j in A_u) theta^u_(s_u)(j)/Z^u_(s_u).

Build the original ownership-incidence graph and the polynomial T_tau(x) from A006: edge u->v has weight sum_(j in A_u intersect R_v)x_(u,j); incoming Laplacian; sum of principal minors over exactly one root in each original source SCC, weighted by product_root pi. No extra roots are permitted in this selected run family. This restriction is a legitimate output lower mass, not a characterization of all successful queue runs.

For a monomial x^h put c_u=sum_(j in A_u)h_(u,j). Define the linear operator

    N_s(x^h) = product_(u in V) [ product_(j in A_u) h_(u,j)! /
                     ((c_u+1)(c_u+2) binom(s_u+c_u-1,c_u)) ].

Then the EXACT conditioned probability of all distinct actual partition-forest runs with this assignment and the stated root restriction is

    Q_tau(A) = [product_(u in V) lambda_u*t_u(A_u)] N_s(T_tau) / D.       (1)

The sum Q_part(A)=sum_tau Q_tau(A) is a subprobability on nonempty A and is <=Q_*(A), the original conditioned output reference. Algebraic subset factors are not asserted rational. T and N_s(T) are rational when the pi are rational.

## Proof and complete coding ledger

The determinant identity follows directly by expanding each nonroot row as sum_u w_uv(e_v-e_u). A selected nonroot cycle has dependent rows, hence determinant zero. An acyclic parent choice ends at a root and has determinant one after simultaneous parent-first ordering. Expanding w_uv selects an attachment. Thus T has nonnegative coefficients and records all attached rooted forests without child chronological multiplicity.

For an attached forest, initial roots have conditioned probability product_root(lambda*pi)/D. This includes all absent-root factors and the conditioning, because the unconditioned root law divides by product_all(1+lambda*pi), and Z=D/product_all(1+lambda*pi). Every other visited gate is drawn once as a child, so root and child probabilities together contribute product_used lambda. This communicates each shared gate label once per complete selected set. Every visit contributes its size and subset factor t_u.

At u, the queue draws c_u with probability 1/[(c_u+1)(c_u+2)], and one of binom(s_u+c_u-1,c_u) multisets uniformly. Its occurrence order is fixed. At attachment j there are h_(u,j)! distinct child-label sequences. Multiplying these independent factors gives N_s. No permutation of initial roots or of distinct attachment coordinates is counted. All permutations within repeated attachment groups give distinct draw events, since children have distinct gate IDs.

An actual event recovers tau from the partition subsets, recovers parents and attachments from the appended-child draws, and recovers every chronological choice. BFS order is determined by the initial-root and occurrence orders. Therefore no forest description is counted twice and assignments have disjoint events. Failure and infinite runs remain outside this finite mass. This proves (1) and the subprobability assertion.

Gate table, supports and orders are fixed decoder side information for f. The decoder executes the root and queue record and unions the selected subsets, recovering A. Roots, gate names, attachments, subset choices and child order all have the probabilities just listed; nothing is sent for free. If only A is required, output aggregation is the correct final ambiguity: -log Q_part(A), rather than the cost of an arbitrary representative record. For the posterior eta(r)=q(r)/Q_part(A), E_eta[-log q(r)]-H(eta)=-log Q_part(A). This is a variational/ideal reference statement. It does not subtract entropy from the length of a physically transmitted raw record. A finite output prefix code, if desired, adds its own rounding; no additive bit is charged to I for free.

## Probability representation of the exact operator

Independently for each used gate u, let Y_u be rate-one exponential, B_u have density 2(1-b) on [0,1], and Z_u be uniform on the probability simplex of dimension s_u-1; for s_u=1 set Z=1. Use independent triples at different gates, and put X_(u,j)=B_u Y_u Z_(u,j). The elementary beta integrals give

    E B_u^c = 2/[(c+1)(c+2)],   E Y_u^c=c!,
    E product_j Z_(u,j)^h_j = (s_u-1)! product_j h_j!/(s_u+c-1)!.

The simplex moment follows by iterated beta integration (for integers a,b, integral_0^1 z^a(1-z)^b dz=a!b!/(a+b+1)!, proved by integration by parts). Hence

    N_s(T_tau) = 2^(-g) E T_tau(X).                                  (2)

This representation is analytical, not a proposed randomized numerical certificate. Dependence inside each gate matters. SCC factors can share X and their expectations cannot generally be multiplied.

## Exact comparison with the surrogate moment

Let a=|A| and e=g-number_of_source_SCCs. Every monomial in T has total degree e. The elementary inequalities (c+1)(c+2)<=2*3^c and binom(s+c-1,c)<=2^(s+c) give, coefficient by coefficient,

    2^(-(a+g+e))*3^(-e) M(T) <= N_s(T) <= 2^(-g) M(T).             (4)

The upper inequality uses the denominator >=2 at each visit. Thus all child-count/attachment corrections cost at most a+g+e+e*log2(3) bits relative to the surrogate moment, hence at most (3+log2(3))*a. They are fully chargeable to that constant times I when averaged over the true spectral law. Size and subset factors t_u, labels lambda, root pi and D remain explicit in (1); (4) does not pay them. This independently recovers precisely the type of count/attachment overhead used in the source theorem and shows that (3) is a missing-factor diagnosis, not a divergence obstruction after averaging. No additive constant is used.

## Exact sharp separation from surrogate factorial credit

On the prime table of the monotone sunflower OR_i(x0 AND xi), choose e+1 gates, A={x0,x2,...,x_(e+1)}, tau(x0)=1 and tau(xi)=i. The attached forest is a forced star, T=pi_1*x_(1,0)^e. Its surrogate factorial moment is pi_1*e!. Here every s_u=1, the parent has c=e, and all e leaves have c=0. Therefore

    N_s(T) = pi_1*e! / [(e+1)(e+2)2^e].                             (3)

In (1), the full singleton t_u includes the conditional subset draw. For common-first width-two orders put a=2^(-6/5): t_common=1/[2(1+a)] and t_private=a/[2(1+a)], with product t=a^e/[2^(e+1)(1+a)^(e+1)]. With both endpoint orders each singleton t=1/4, with product t=4^(-(e+1)). Any feasible positive lambda works, for example lambda_i=1/(e+1), pi_i=1/4. See ERRATUM.md for the original error and its downstream scope. Equation (3) proves that transplanting surrogate factorial credit into actual probabilities without count/multiset factors is false by the exact factor (e+1)(e+2)2^e. It is not an FEI counterexample. These A have positive Fourier mass: directly expanding the sunflower gives every such nontrivial set coefficient of magnitude 2^(-(e+1)).

## Universal boundary

No dimension-independent influence payment is proved. The first unsupported complete-reference line is

    sum_(A nonempty) P_f(A) log2(1/Q_part(A)) <= K I(f)

for every Boolean f under one fixed feasible prime-table reference, with absolute K. The h2(v) term is separately paid by the source estimate <=2I. In particular, (2) does not make the assignment sum or a polynomial expectation efficiently computable in general. It supplies the exact cost to insert into A009's full-transfer error sector, while preventing the unpaid-factor shortcut.
