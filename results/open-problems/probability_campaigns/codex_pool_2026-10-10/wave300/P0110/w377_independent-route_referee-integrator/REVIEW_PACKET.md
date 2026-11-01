# P0110 referee packet — 2026-10-10

Verdict on parent problem: **GAP**. The primary survey asks for a law exhibiting the relation; Chatterjee's theorem assumes coincident strong upper/lower exponents. Neither peer supplies that coincidence for an iid lattice law. Current 2026 openness remains UNKNOWN after bounded checks; no novelty claim.

## Source and scope

Primary: Auffinger–Damron–Hanson, *50 years of first passage percolation*, Section 4.3, equation (4.19), Question 22 (arXiv:1511.03262). Its literal question is “Find a distribution of passage times where (4.19) holds.” The nearby text says the existence and correct definition of chi and xi are part of the problem. Chatterjee, *Annals of Mathematics* 177 (2013), Theorem 1.1, defines chi_a, chi_b, xi_a, xi_b by A1–A4 and concludes chi=2xi-1 only if chi_a=chi_b and xi_a=xi_b. The upper bounds use uniform exponential moments over all nonzero lattice endpoints; the lower bounds allow a radius cutoff C. Auffinger–Damron, arXiv:1109.0523, Theorem 2.2 removes the nearly-Gamma law condition but retains common-exponent premises; its displayed lower definition (2.2) has an all-nonzero-endpoints infimum, a different quantifier.

## w375 L1: KEEP as finite obstruction

From 0 to k e1, a coordinate-monotone lattice path has exactly k positive e1 steps, hence is unique. The height-one detour has k+2 edges. The two deterministic edge sets are disjoint, so the event that all k axial weights lie in a high interval and all k+2 detour weights lie in a low interval has probability p_high^k p_low^(k+2). On that event k b>(k+2)a makes the detour strictly cheaper. This is a legitimate iid product: no path-selected events are multiplied. It proves a same-environment exact directed reduction fails under w375's two-interval hypothesis. It says nothing about exponents.

## w375 L2: KEEP as bounded-law axial separation

For k satisfying the L1 strict inequality, set S=cost of the k-edge axis, H=cost of its disjoint detour, and delta=E[(S-H)_+]. L1 gives delta>= [k b-(k+2)a] p_high^k p_low^(k+2)>0. A block of k+1 columns uses min(S,H), followed by a single axial connector. Consecutive blocks use disjoint edges: the connector separates the height-one detours by one horizontal column. Their bounded costs Y_j are iid with E Y_j=(k+1)mu-delta. Concatenated block paths are valid paths, so T(0,m(k+1)e1)<=sum_{j<m}Y_j. Strong law yields limsup T(0,n e1)/n<=mu-delta/(k+1); appending at most k edges costs at most kR. The directed axial sum divided by n tends to mu, giving a raw same-environment linear gap at least delta/(k+1). The expectation bound E T(0,n e1)<=n mu-floor(n/(k+1))delta follows from the same path. This is an obstruction to a raw reduction only; it does not rule out recentering, coupling, or common exponents.

Independent exact witness: for iid weights in {1,2} with equal mass, k=3, b=2, a=1. Of the 2^8 assignments to the disjoint three-edge axis and five-edge detour, exactly one has S>H, and then S-H=1. Thus delta=1/256 and the proved linear gap is at least 1/1024. Reproduce with `python -X utf8 ~/brain_workers/w377/review_repro.py`.

## w375 L3: KEEP as diagonal finite obstruction

For endpoints (0,0) to (k,k), the high square edges in w375's event are k(k+1) horizontal plus k^2 vertical edges in columns x<k, totaling 2k^2+k. The low edges are k vertical edges on x=k, k horizontal edges at y=-1, and two external vertical edges, totaling 2k+2; all sets are disjoint. Each coordinate-monotone path stays within [0,k]^2 and uses k high horizontal edges plus k vertical edges each at least ell, so its cost is at least k(b+ell). The exterior detour uses the 2k+2 low edges and costs at most (2k+2)a. The stated k(b+ell-2a)>2a is exactly the strict comparison. For iid {1,2} and k=3, all 20 coordinate-monotone paths have cost at least 9 while the detour costs 8 on the specified event; `review_repro.py` enumerates all 20. The event probability is p_high^(2k^2+k)*p_low^(2k+2). This controls every directed competitor in a diagonal direction, yet remains only a finite obstruction.

## w375 L4: KEEP as exact finite axial threshold

For essential weight bounds 0<r<R<infinity, every nonaxial path from 0 to n e1 has length at least n+2, by parity and uniqueness of the length-n axis. If n(R-r)<=2r, its cost is at least (n+2)r>=nR, so no strict improvement over the axis is possible. At equality, a tie may occur; no uniqueness is claimed. If n(R-r)>2r, put M=n(R-r)-2r and eta=M/(4n+4). Positive-mass neighborhoods [r,r+eta] and [R-eta,R] exist by essential infimum/supremum, and n(R-eta)-(n+2)(r+eta)=M/2>0. L1 supplies a strictly cheaper detour with positive probability. Thus P(T<T_dir)>0 exactly above the threshold. For {1,2}, n=2 is at equality and n=3 gives the first positive-probability gap.

## w376 C001: KEEP as dependency counterexample

For one Bernoulli(1/2) bit B, set A1=A2={B=1} and condition each event on the trivial sigma-field. Each conditional probability is 1/2 but their intersection has probability 1/2, exceeding 1/4. A sequential product bound requires an increasing filtration, measurability of earlier events at the conditioning stage, and an almost-sure bound on P(A_i|F_{i-1}); iterated conditional expectation then proves the product. This is an abstract guard, not a finding of dependency error in w375's proof.

## w376 C002: KEEP as one-index inference obstruction

With a_n=1/4 for even n and 1/3 for odd n, X_n=n^a_n Z for a symmetric sign Z and D_n=n^((1+a_n)/2), sqrt(Var X_n)=D_n^2/n at each n. Odd n controls the least valid uniform upper exponents: chi_a=1/3 and xi_a=2/3. Even n controls the largest tail-uniform lower exponents: chi_b=1/4 and xi_b=5/8. Thus both endpoint identities hold, while the chi and xi gaps are 1/12 and 1/24. The lower-bound condition at exponents below the minimum is satisfied since the ratio is at least 1 for every n>=2. This reproduces the threshold calculation; it is not an iid FPP construction and does not test all lattice directions.

## w376 C003: KEEP with source-specific wording

Chatterjee Theorem 1.1 indeed makes the common-exponent equalities premises. It does not exhibit a law proving them. The exact law hypotheses in that theorem are iid nonnegative nearly-Gamma edge weights with a moment generating function near zero on Z^d, d>=2. Auffinger–Damron later remove the nearly-Gamma premise for their conditional implication. Neither theorem proves P0110 alone.

## Source quantifier correction, independent check

Chatterjee A3–A4 permit an endpoint cutoff |v|>C. Auffinger–Damron equation (2.2) literally takes infimum over all v !=0. For iid Uniform[1,2] weights, the direct edge 0→e1 costs at most 2, while every different self-avoiding path has at least three edges and costs at least 3. Thus D(0,e1)=0 in every environment and the all-endpoint infimum of E D/|v|^r is zero. This blocks that particular law from satisfying the literal (2.2) premise, even though its asymptotic wandering may be nontrivial. The observation is about a stated hypothesis, not a counterexample to either conditional theorem.

## w376 C008: KEEP with raw-scale scope

Let c=delta/(k+1)>0 from w375 L2. The two marginal statements are P(U_n/n>mu-c+epsilon)→0 for unrestricted passage time and P(V_n/n<mu-epsilon)→0 for the directed axial sum. Under any coupling, the union bound makes both inequalities hold jointly with probability tending to one. On that event (V_n-U_n)/n>=c-2epsilon. This rules out a raw o_P(n) same-marginal approximation even after changing the coupling; it says nothing about centered fluctuation laws or universality. No independence of U_n and V_n is used.

## Hardest remaining gap and next audit

The load-bearing open piece is one concrete iid undirected full-lattice law with matching upper/lower fluctuation and wandering exponents under a precise definition, or a new direct relation proof with its own justified definitions. To advance, identify a variance-scale and width-scale stabilization estimate that rules out oscillations without presupposing the desired variance ratio. Any new theorem from this referee must go to w380 before promotion; this packet asserts no new FPP theorem beyond independent checks of the peers' partial lemmas.
