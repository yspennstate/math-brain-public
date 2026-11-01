## Catalog chapter 4: Codex campaign (Probability_1000_20h_20260906), P0451-P0488

This chapter covers rows P0451 through P0488 of the Codex 20-hour probability campaign ledger (problems.jsonl, attempts.jsonl, sources.jsonl in ~/Downloads/Probability_1000_20h_20260906). P0488 is the last P-row in problems.jsonl; the ledger's own STATUS.json records 451 admitted/attempted problems as of the resumed thread's last checkpoint (2026-09-07T09:32:34Z), and this shard is entirely post-checkpoint intake (recorded_at 2026-09-07T07:49:20Z through 09:27:15Z). All 38 ids in the range are present in problems.jsonl with no duplicate problem_id rows. 28 of 38 are marked admitted and 10 are not admitted (each not-admitted row carries a reason or resolution record in the ledger: a source's own later theorem already resolves the leading-order question, a later independent paper resolves or refutes the historical open question, or the proposal needs a precise formulation before it counts as a distinct attempted problem). Result_status counts across the 38 rows: candidate_partial_counterexample: 2, held: 4, known_result_not_original: 1, literature_resolved: 3, not_attempted_as_precise_problem: 2, unsolved: 26. 28 of 38 rows have a recorded attempt in attempts.jsonl (the 10 rows without one are the not-admitted rows that were held or resolved without an original attempt); 2 rows carry a proof_file or proof_path reference (P0458 and P0459, both proofs/Bilateral_degree_fluctuations_partial.md). No CORRECTIONS.md file exists in the source directory; no record in this directory revises a status for a row in this range beyond what is already recorded on the row itself, in its own resolution_source_id / resolution_evidence / resolution_locator / exclusion_reason fields. As stated in the campaign's own README.md and STATUS.json, zero results in this ledger are independently reviewed; every verification level reported below is author_checked or weaker, and nothing in this chapter is a claim of publishable novelty.

### P0451. Unimodularity and reversibility of the Erlang branching spine

**Source.** Moharrami, Subramanian, Liu and Sundaresan: The Erlang Weighted Tree, A New Branching Process (v5, 27 May 2023) (erlang_weighted_tree_2023), Section4, question2; PDF16.

**Statement.** Characterize the relationship between unimodularity of the marked branching tree and reversibility of its source-defined continuous-state spine kernel. Ledger caveat: The reversibility of this particular kernel is already established in the source. The open target is the general relationship and correct change of root, not another proof of detailed balance.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches for EWT, La-Kabkab and bilateral preference degree results; 2025 connectivity theorem credited. No current-open or novelty certification. Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact conditioning, spectral integral estimate, deterministic graph comparison or order-statistic asymptotics. Result: For the displayed kernel p(x,y)=min(x,y)*g2(y)*f0(y)/(beta0*f0(x)), the measure with density pi(x)=g2(x)*f0(x)^2 has symmetric pair flow pi(x)p(x,y)=min(x,y)*g2(x)*g2(y)*f0(x)*f0(y)/beta0. This recovers the credited reversibility by inspection. The obstacle to identifying it with ordinary unimodular rerooting is the reproductive f0 bias: unimodularity is a mass-transport identity for the root law, while the spine favors descendants through the right eigenfunction. One must construct and normalize a two-sided marked spine with the appropriate Radon-Nikodym factor before claiming an equivalence. Obstruction: No general equivalence, converse, or root-bias formula beyond this explicit kernel calculation is proved. Verification: author_checked_partial. No proof file recorded.

### P0452. Giant-component density from Erlang weighted-tree survival

**Source.** Moharrami, Subramanian, Liu and Sundaresan: The Erlang Weighted Tree, A New Branching Process (v5, 27 May 2023) (erlang_weighted_tree_2023), Section4, question3; PDF16; Corollary2.2.

**Statement.** Prove the lower bound matching the known upper bound: the largest La-Kabkab component has asymptotic vertex fraction equal to EWT survival probability. Ledger caveat: The later logarithmic connectivity theorem concerns growing preference budgets and does not supply the fixed-distribution giant lower bound.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches for EWT, La-Kabkab and bilateral preference degree results; 2025 connectivity theorem credited. No current-open or novelty certification. Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact conditioning, spectral integral estimate, deterministic graph comparison or order-statistic asymptotics. Result: The local-limit argument controls the fraction of vertices in components above a fixed size; it does not put those vertices in one component. To break that inference, compare one cycle of size n with a disjoint union of cycles of length floor(sqrt(n)), adjusting a negligible remainder. Both local weak limits are the bi-infinite path, which is infinite with probability one. The largest component fractions instead tend to one and zero. Thus the missing step for La-Kabkab is a genuine uniqueness/coalescence or sprinkling argument controlling dependencies among mutually preferred edges; local convergence alone cannot provide it. Obstruction: This is a counterexample to a proposed proof implication on general graph sequences, not a counterexample within the La-Kabkab model. Verification: author_checked_partial. No proof file recorded.

### P0453. Weaker degree-tail hypotheses for Erlang weighted-tree growth

**Source.** Moharrami, Subramanian, Liu and Sundaresan: The Erlang Weighted Tree, A New Branching Process (v5, 27 May 2023) (erlang_weighted_tree_2023), Section4, question4; PDF16; Section5.4.

**Statement.** Relax the exponential-moment hypothesis in the EWT growth, spectral and extinction conclusions, with the conditions for each conclusion stated separately. Ledger caveat: The question groups related conclusions. A compact mean operator alone is not an extinction or branching-martingale convergence theorem.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches for EWT, La-Kabkab and bilateral preference degree results; 2025 connectivity theorem credited. No current-open or novelty certification. Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact conditioning, spectral integral estimate, deterministic graph comparison or order-statistic asymptotics. Result: One spectral step only needs finite mean. Put g2(x)=exp(-x)*sum_(j>=2)P(j)*x^(j-2)/(j-2)!, and consider Kf(x)=integral min(x,y)*f(y)*g2(y)dy on L2(g2 dx). Tonelli gives integral x*g2(x)dx=sum_(j>=2)(j-1)P(j)=E[K_degree]-1. Since min(x,y)^2<=x*y, the squared Hilbert-Schmidt norm is at most (E[K_degree]-1)^2. Thus finite mean already makes this symmetric integral operator compact. The kernel is also positive semidefinite because min(x,y)=integral_0^infinity 1_(t<x)*1_(t<y)dt. This removes an exponential moment from the compactness step, while leaving the stronger population conclusions untouched. Obstruction: No assertion that every source growth/extinction theorem survives under finite mean. Identifying the branching eigenfunctions, integrability of the spine, and uniform integrability of martingales still require proof. Verification: author_checked_partial. No proof file recorded.

### P0454. Iterated budget-filling bilateral graph limits

**Source.** Moharrami, Subramanian, Liu and Sundaresan: The Erlang Weighted Tree, A New Branching Process (v5, 27 May 2023) (erlang_weighted_tree_2023), Section4 question5; PDF17.

**Statement.** Iterated budget-filling bilateral graph limits

**Status.** Historical status: source_says_open. Current-literature status: intake_needs_precise_formulation. Status search: none recorded in the ledger. Admission: not admitted; result_status: not_attempted_as_precise_problem.

**Our work.** Not admitted (result_status: not_attempted_as_precise_problem). Reason: The proposal requires an exact round/update protocol. Retain as an intake lead until that model is fixed; no extra admission for an arbitrary invented protocol. No attempt is recorded for this row in attempts.jsonl.

### P0455. A general spectral method for uncountable-type branching

**Source.** Moharrami, Subramanian, Liu and Sundaresan: The Erlang Weighted Tree, A New Branching Process (v5, 27 May 2023) (erlang_weighted_tree_2023), Section4 question6; PDF17.

**Statement.** A general spectral method for uncountable-type branching

**Status.** Historical status: source_says_open. Current-literature status: intake_needs_precise_formulation. Status search: none recorded in the ledger. Admission: not admitted; result_status: not_attempted_as_precise_problem.

**Our work.** Not admitted (result_status: not_attempted_as_precise_problem). Reason: Methodological research direction without a sharp general target; hold rather than count a broad extension request as another precise problem. No attempt is recorded for this row in attempts.jsonl.

### P0456. The fine connectivity window for bilateral preference graphs

**Source.** Dabirian and Subramanian: Connectivity of a family of bilateral preference random graphs (bilateral_connectivity_2025), Open Problems; PDF2-3.

**Statement.** Locate the sharp connectivity window and limiting connectivity probability of LK(n,k) inside the source remaining band around log(n). Ledger caveat: The source already settles the leading log(n) threshold. The unresolved band has width of order sqrt(log(n))*log(log(n)).

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches for EWT, La-Kabkab and bilateral preference degree results; 2025 connectivity theorem credited. No current-open or novelty certification. Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact conditioning, spectral integral estimate, deterministic graph comparison or order-statistic asymptotics. Result: At k=log(n)+a*sqrt(log(n)), the known mean-degree expansion gives E[D]=log(n)+(a-1/sqrt(pi))*sqrt(log(n))+lower-order terms. Matching this mean to log(n) therefore suggests an apparent positive shift, but it does not derive a connectivity threshold: isolated-vertex probabilities depend on the far lower tail of D, not its mean. Even the candidate central fluctuation law in the separate packet probes deficits of order sqrt(k); isolation requires deficit k, a moving far-tail event outside that limit. An actual sharp-window proof must analyze the relevant order-statistic large deviation and then exclude nontrivial small components. Obstruction: No connectivity shift, window width or limiting probability is established; the mean-matching calculation is explicitly a failed inference to test. Verification: author_checked_partial. No proof file recorded.

### P0457. Diameter near the newly established bilateral connectivity threshold

**Source.** Dabirian and Subramanian: Connectivity of a family of bilateral preference random graphs (bilateral_connectivity_2025), Open Problems; PDF3.

**Statement.** Characterize LK(n,k) diameter in the additional near-logarithmic range where the source proves connectivity. Ledger caveat: The old diameter result follows from a coarser embedded graph and does not automatically extend through the improved connectivity range.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches for EWT, La-Kabkab and bilateral preference degree results; 2025 connectivity theorem credited. No current-open or novelty certification. Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact conditioning, spectral integral estimate, deterministic graph comparison or order-statistic asymptotics. Result: Any connected graph with maximum degree k>=3 has at most 1+k*((k-1)^r-1)/(k-2) vertices within radius r. Hence its diameter d satisfies n<=1+k*((k-1)^d-1)/(k-2), giving a deterministic lower bound of logarithmic order log(n)/log(k). For LK this uses its exact degree cap and requires no independence. A matching upper bound needs expansion of balls grown through mutual rankings; the Erdős-Rényi subgraph used by a coarse coupling may itself be disconnected in the newly covered range and then offers no diameter bound. Obstruction: No matching upper bound or limiting constant is proved. The tree-volume inequality is classical and credited as a diagnostic. Verification: author_checked_partial. No proof file recorded.

### P0458. The standardized degree law in growing bilateral preference graphs

**Source.** Dabirian and Subramanian: Connectivity of a family of bilateral preference random graphs (bilateral_connectivity_2025), Open Problems; PDF3 first additional question.

**Statement.** Determine the limiting law of (D-E[D])/sqrt(Var(D)) for a typical LK(n,k) degree as the preference budget grows. Ledger caveat: A private packet covers k->infinity with k=o(n^(2/5)), including the source mean-asymptotic regime k=o(n^(1/3)). Other growth regimes and novelty are not settled.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches for EWT, La-Kabkab and bilateral preference degree results; 2025 connectivity theorem credited. No current-open or novelty certification. Admission: admitted; result_status: candidate_partial_counterexample.

**Our work.** Method: Exact conditioning, spectral integral estimate, deterministic graph comparison or order-statistic asymptotics. Result: The packet uses the exact root (k+1)st order statistic X~Beta(k+1,n-k-1). Ignoring internal edges among the root preferred neighbors gives D0|X~Bin(k,1-q(X)), where q(X)=E[(X-T)+]/X and T~Beta(k,n-2k). The actual error satisfies E[(D0-D)^2/k]=O(k^2/n+k^5/n^2). Beta central limits and explicit moment controls then give (k-D)/sqrt(k)->g(Z), g(z)=phi(z)+z*Phi(z), with convergence of its first two moments. The variance constant is v=1/3+(sqrt(3)-2)/(2*pi), and the standardized degree limit is (1/sqrt(pi)-g(Z))/sqrt(v), which is non-Gaussian. Obstruction: Author-only partial candidate for the broader source question. No independent review, current-openness or novelty certificate, and no assertion for every k regime. Verification: author_checked_partial. Proof/memo file: proofs/Bilateral_degree_fluctuations_partial.md.

### P0459. Simultaneous concentration of bilateral preference degrees

**Source.** Dabirian and Subramanian: Connectivity of a family of bilateral preference random graphs (bilateral_connectivity_2025), Open Problems; PDF3 second additional question.

**Statement.** Find growth conditions and quantitative bounds for LK(n,k) degrees to concentrate simultaneously around their mean. Ledger caveat: The source asks for concentration conditions. The private packet supplies a sufficient superlogarithmic regime using the source existing ER-sandwich method, with no optimality or novelty claim.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches for EWT, La-Kabkab and bilateral preference degree results; 2025 connectivity theorem credited. No current-open or novelty certification. Admission: admitted; result_status: candidate_partial_counterexample.

**Our work.** Method: Exact conditioning, spectral integral estimate, deterministic graph comparison or order-statistic asymptotics. Result: Put delta=sqrt(6*k*log(n)) and assume k>2*delta. Threshold edge weights at t=(k-delta)/(n-1). Each threshold degree B_v is binomial with mean k-delta. Chernoff and a union bound give k-2*delta<=B_v<=k for all vertices with probability at least 1-2/n^2. On that event every threshold edge is preferred at both endpoints, so k-2*delta<=D_v<=k simultaneously. Thus k/log(n)->infinity suffices for relative concentration. The argument uses independence of the underlying edge weights, and never independence of vertex degrees. Obstruction: A sufficient-condition partial only. Sharp tails and the logarithmic boundary are not determined; below connectivity isolated vertices rule out concentration of every degree near k. Verification: author_checked_partial. Proof/memo file: proofs/Bilateral_degree_fluctuations_partial.md.

### P0460. Leading logarithmic connectivity threshold of bilateral preference graphs

**Source.** Dabirian and Subramanian: Connectivity of a family of bilateral preference random graphs (bilateral_connectivity_2025), Introduction; Theorem1.1 and Theorems4.1,5.3.

**Statement.** Determine the leading k=t*log(n) connectivity threshold originally conjectured by La and Kabkab.

**Status.** Historical status: source_recalls_earlier_conjecture. Current-literature status: resolved_in_literature. Status search: none recorded in the ledger. Admission: not admitted; result_status: known_result_not_original. Resolution record: The archived v3 paper proves disconnectedness below log(n)-0.5*sqrt(log(n))*log(log(n)) and connectivity above the corresponding upper band, with strict inequalities in the coefficient. It settles the leading threshold; P0456 retains only the fine unresolved window (source: Dabirian and Subramanian: Connectivity of a family of bilateral preference random graphs, bilateral_connectivity_2025).

**Our work.** Not admitted (result_status: known_result_not_original). Reason: no reason recorded on the row No attempt is recorded for this row in attempts.jsonl.

### P0461. Entropy concavity for determinantal kernels

**Source.** Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (lyons_determinantal_2014), Conjectures2.6 and5.3; PDF5,22.

**Statement.** Prove or disprove concavity of finite determinantal Shannon entropy in a positive-contraction kernel. Include the source-related stationary-symbol entropy conjecture as a grouped consequence. Ledger caveat: Finite-kernel concavity implies the stationary version by restriction to finite boxes and entropy-rate limits. They are not asserted equivalent. Diagonal means diagonal in the coordinate basis defining the point process, not merely simultaneously diagonalizable.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches on entropy concavity, union coupling, block factors, Fuglede-Kadison domination and the linear distance bound. Known rank-one coupling and degree-one block-factor cases credited. No current-openness certificate. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact special-case argument and failure analysis after checking the incoming source. Result: The coordinate-diagonal case is a sum of binary entropies, whose second derivatives are -1/[q(1-q)]. There is also an explicit non-diagonal line: for Q(c)=[[1/2,c],[c,1/2]], |c|<1/2, the empty and doubleton probabilities are a=1/4-c^2 and the two singleton probabilities are b=1/4+c^2. Hence H(c)=-2*a*log(a)-2*b*log(b), and Hsecond(c)=4*log(a/b)-8*c^2*(1/a+1/b)<=0. Continuity includes c=+-1/2. This verifies concavity on this affine kernel line. In general the determinant probabilities depend nonlinearly on Q, so concavity of Shannon entropy in a probability vector cannot be applied directly to an arithmetic kernel midpoint. Obstruction: No joint concavity proof, no extension to arbitrary off-diagonal or noncommuting kernels, and no numerical trials treated as certification. Verification: author_checked_restricted_argument. No proof file recorded.

### P0462. Disjoint coupling of orthogonal projection processes

**Source.** Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (lyons_determinantal_2014), Question2.8; PDF6.

**Statement.** For H=H1 orthogonal-direct-sum H2 in l2(E), construct or rule out a coupling of their projection determinantal processes whose union has the projection law of H. Ledger caveat: Finite-rank cardinalities force disjointness. The rank-one argument below is a credited consequence of stochastic domination, already present in Lyons2003; it is not a new solution.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches on entropy concavity, union coupling, block factors, Fuglede-Kadison domination and the linear distance bound. Known rank-one coupling and degree-one block-factor cases credited. No current-openness certificate. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact special-case argument and failure analysis after checking the incoming source. Result: If H2 is spanned by a unit vector u and H1 has finite rank, monotone-couple A with law P_H1 inside C with law P_H. Their deterministic sizes differ by one, so C minus A is a singleton B. At any coordinate e, P(B={e})=P(e in C)-P(e in A)=(P_H)ee-(P_H1)ee=|u(e)|^2. Thus B has precisely P_H2 and (A,B) gives the required coupling in this special case. For higher rank, the same subtraction determines only one-point intensities of C minus A; its higher inclusion probabilities are not fixed. The finite problem can be written as nonnegative weights w(A,B) on disjoint pairs with the three required marginals, but setting up this transportation problem does not prove it feasible. Obstruction: No general coupling construction. Earlier floating-point LP claims are retained only in the frozen incoming record, not counted as exact certificates. Verification: author_checked_restricted_argument. No proof file recorded.

### P0463. Block factors for finite-range determinantal symbols

**Source.** Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (lyons_determinantal_2014), Question5.4; PDF22.

**Statement.** For a trigonometric polynomial f:T->[0,1] of degree m, is its stationary determinantal process an (m+1)-block factor of iid variables? Ledger caveat: The source credits Broman2005 for degree one. A sublattice reduction proves new cases only when the lower-degree process already has a suitable block-factor construction; it is not an induction proving every even degree.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches on entropy concavity, union coupling, block factors, Fuglede-Kadison domination and the linear distance bound. Known rank-one coupling and degree-one block-factor cases credited. No current-openness certificate. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact special-case argument and failure analysis after checking the incoming source. Result: Let f(theta)=g(k*theta). Its Fourier coefficients vanish at lags not divisible by k, so the determinantal kernel is block diagonal on the k residue classes. Determinant factorization proves that these restrictions are independent copies of P_g. If P_g can be represented as F(U_j,...,U_(j+r)) with iid U, define Y_i=F(U_i,U_(i+k),...,U_(i+r*k)). This is a shift-equivariant function of the window U_i,...,U_(i+r*k), so is an (r*k+1)-block factor. The residue-class families use disjoint iid coordinates and have the correct laws. In particular any single-harmonic symbol a+b*cos(k*theta)+c*sin(k*theta) with range in [0,1] inherits the known degree-one construction and is a (k+1)-block factor. Obstruction: General mixed-harmonic symbols remain untreated. Finite dependence by itself does not imply a block-factor representation. Verification: author_checked_restricted_argument. No proof file recorded.

### P0464. Geometric-mean product bounds for equivariant determinantal laws

**Source.** Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (lyons_determinantal_2014), Conjecture5.7; PDF23.

**Statement.** For a Gamma-equivariant positive contraction Q on l2(Gamma), establish or refute the optimal stochastic product bounds with lower density FK(Q)=exp(tr log Q) and upper density 1-FK(I-Q). Ledger caveat: The following classical conditioning argument gives weaker harmonic-mean bounds for finite groups and 0<Q<I. It is an author-checked supporting calculation, not a novelty claim or a solution of the geometric-mean conjecture.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches on entropy concavity, union coupling, block factors, Fuglede-Kadison domination and the linear distance bound. Known rank-one coupling and degree-one block-factor cases credited. No current-openness certificate. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact special-case argument and failure analysis after checking the incoming source. Result: Put J=Q(I-Q)^(-1). Given the occupied set B outside e, the conditional odds of presence are s_B=J_ee-J_eB*(J_BB)^(-1)*J_Be. Schur-complement minimization makes s_B decrease as B increases. Its minimum is s_all=1/(J^(-1))ee=1/[(Q^(-1))ee-1]. The conditional probability, however, is s_all/(1+s_all)=1/(Q^(-1))ee. Equivariance makes (Q^(-1))ee=tr(Q^(-1)), with normalized trace, so this probability is the harmonic mean h of all eigenvalues counted with multiplicity. Sequential sampling with common independent uniforms couples the process above iid Bernoulli(h), since every conditional probability given a partial reveal is also at least h. Applying the same argument to the complement gives the upper density 1-HM(I-Q). AM-GM applied to the reciprocals gives HM(Q)<=FK(Q), exposing the exact remaining gap. Obstruction: No geometric-mean domination theorem or sharpness certificate. Numerical coupling feasibility is not exact proof, and the infinite-group extension of this particular calculation is not asserted. Verification: author_checked_restricted_argument. No proof file recorded.

### P0465. Linear coupling distance for noncommuting equivariant kernels

**Source.** Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (lyons_determinantal_2014), Section5.2 afterTheorem5.6; PDF23.

**Statement.** For sofic-group equivariant positive contractions Q,Qprime, does the invariant normalized Hamming coupling distance satisfy dbar(P_Q,P_Qprime)<=||Q-Qprime||_1 without a commutativity assumption? Ledger caveat: The source states the linear bound for commuting pairs and a weaker power bound in general. We examine why the natural common-upper-kernel proof fails; the example is not a counterexample to the actual coupling inequality.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: 2026-09-07 bounded primary searches on entropy concavity, union coupling, block factors, Fuglede-Kadison domination and the linear distance bound. Known rank-one coupling and degree-one block-factor cases credited. No current-openness certificate. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact special-case argument and failure analysis after checking the incoming source. Result: Write D=Q-Qprime. A tempting common upper kernel is R=Qprime+Dplus=(Q+Qprime+|D|)/2. It dominates both in operator order, but need not be a contraction. In dimension two take Q=diag(1,0) and Qprime=(1/2)*[[1,1],[1,1]]. Then D^2=I/2 and |D|=I/sqrt(2). The largest eigenvalue of Q+Qprime is 1+1/sqrt(2), giving lambda_max(R)=1/2+1/sqrt(2)>1. Thus R is not an admissible determinantal kernel and one cannot apply monotone-coupling bounds through it. This same obstruction can be placed in the two-dimensional irreducible block of the right group algebra of S3, with zeros on the other blocks; the resulting operators commute with left translations but not with one another. Obstruction: Failure of a common-upper-kernel construction does not refute the desired distance inequality. No claim of having executed a nonabelian coupling LP. Verification: author_checked_restricted_argument. No proof file recorded.

### P0466. Joint intermediate level-set limits from one continuum field

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Problem16.1; PDF220.

**Statement.** Find a joint limit of normalized two-dimensional DGFF intermediate level-set measures for all lambda in (0,1), with the limiting chaos measures constructed from the same continuum GFF. Ledger caveat: Marginal convergence, countable joint tightness and identification of one common-field coupling are different claims.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: For any countable sequence lambda_j, marginal tightness already gives tightness in the countable product: choose compact K_j carrying probability at least 1-epsilon*2^(-j) uniformly in N, and apply a union bound and compactness of the product. A diagonal subsequence therefore yields a joint law at those levels. This does not identify that law as the chaos family of a common CGFF. For uncountably many levels a topology and stochastic continuity or another separability argument are still needed. The known marginal laws allow many couplings, just as (X,X) and (X,Y) with independent equal-law coordinates have identical individual marginals. Obstruction: No identification of cross-level dependencies or all-lambda convergence; no subcritical use of the critical Seneta-Heyde normalization. Verification: author_checked_restricted_argument. No proof file recorded.

### P0467. Fluctuations and deviation scales of intermediate DGFF counts

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Problem16.2; PDF220.

**Statement.** Determine rates, fluctuation laws and deviation estimates around the known random-measure limits of DGFF intermediate level sets. Ledger caveat: The normalized count has a random chaos limit; it is not expected to concentrate around a deterministic mean.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: For an interior bulk region A and a threshold 2*sqrt(g)*lambda*log(N), the diagonal variance expansion is g*log(N)+c0+g*log(r_D(x))+o(1). The Gaussian Mills ratio gives the exceedance probability asymptotic N^(-2*lambda^2)*exp(2*lambda^2*c0/g)*r_D(x)^(2*lambda^2)/(2*lambda*sqrt(2*pi*log(N))). Summing over a regular bulk region produces a mean proportional to N^(2-2*lambda^2)/sqrt(log(N)), with the displayed conformal-radius integral as its coefficient. This recovers the indispensable square-root logarithmic divisor. It only fixes the first-moment scale: correlated two-point events and the random limiting mass prevent an iid variance or deterministic-centered CLT inference. Obstruction: No fluctuation law, convergence rate or sharp deviation theorem. The incoming claim omitting sqrt(log(N)) is discarded. Verification: author_checked_restricted_argument. No proof file recorded.

### P0468. Recovering the critical chaos tail from Gibbs-Markov axioms

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Conjecture16.3; PDF220-221; Theorem10.15 PDF134.

**Statement.** Does every nontrivial family of random measures satisfying properties1-4 of Theorem10.15 also obey its logarithmic Laplace-tail property5, up to a positive normalization constant? Ledger caveat: The four premises include null-set behavior, fourth-power scaling, independent additivity on disjoint domains and the Gaussian Gibbs-Markov multiplicative decomposition.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: Partitioning a domain gives independent fine measures multiplied by an independent, spatially varying Gaussian binding field. On each compact subdomain, the weighted mass lies between exp(alpha*inf(Phi)) times its fine total mass and exp(alpha*sup(Phi)) times that mass. These inequalities explain a possible smoothing-transform route, but the weights are functions of position rather than single scalar multipliers of identically distributed masses. Replacing each field by one value creates an oscillation error that must be controlled on the critical tail scale. Multiplying the entire family by a deterministic c>0 preserves the four premises, so the best possible conclusion must allow its tail constant to change by c. Obstruction: No scalar smoothing-transform theorem has been applied without checking these errors. No finite-mean or moment-threshold consequence is asserted from the four axioms alone. Verification: author_checked_restricted_argument. No proof file recorded.

### P0469. Explicit law of the position and height of the DGFF maximum

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Problem16.4; PDF221; equation12.86 PDF180.

**Statement.** Find an explicit expression or a uniquely characterizing PDE for the limiting joint density rho_D(x,t) of the scaled location and centered height of the DGFF maximum. Ledger caveat: rho_D is the joint density from the local limit theorem, not the normalized expectation of the critical chaos measure.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: Conditional on Z, the extremal leaders form a Poisson process with intensity Z(dx)*exp(-alpha*h)dh. Thus the probability that all heights are at most t is exp(-Z(D)*exp(-alpha*t)/alpha), and the joint maximum density measure is exp(-alpha*t)*E[Z(dx)*exp(-Z(D)*exp(-alpha*t)/alpha)]dt, matching equation12.86. Integrating over t gives the position marginal E[Z(dx)/Z(D)]. This is well-defined although E[Z(D)] is infinite under the source critical-tail law. Consequently a ratio of expectations is unavailable. More generally, a random total mass alone does not forbid equality of such ratios: Z=W*nu for a fixed probability measure nu and integrable positive W is a counterexample to that proposed obstruction. Obstruction: The exact Cox-process representation is credited to the source. It is not an explicit solution for rho_D or a closed PDE. Verification: author_checked_restricted_argument. No proof file recorded.

### P0470. The size of deep DGFF extremal level sets

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Conjecture16.5; PDF221.

**Statement.** Prove the iterated N-then-t limit of the DGFF count above m_N-t, divided by t*exp(alpha*t), as a positive constant times the critical chaos mass, jointly for finitely many spatial regions. Ledger caveat: An expectation asymptotic for a cluster is not equivalent by itself to this distributional statement.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: In the limiting decorated Poisson process, restrict leader heights to [-t,H] and let F_s be the number of sites in one cluster within depth s. Conditional on Z, Campbell's formula gives expected truncated count Z(A)*exp(alpha*t)*integral_0^(t+H) exp(-alpha*s)*E[F_s] ds. If E[F_s] is asymptotic to c*exp(alpha*s), this is asymptotic to c*Z(A)*t*exp(alpha*t) when H=o(t), explaining the conjectured t factor. The conditional variance, when finite, is Z(A)*exp(alpha*t)*integral_0^(t+H) exp(-alpha*s)*E[F_s^2] ds. Its negligibility after division by t^2*exp(2*alpha*t), and control of high leaders and finite-N approximation, are additional requirements, not consequences of the first-moment formula. Obstruction: No second-moment, Laplace remainder or uniform-integrability bound sufficient for the full target has been proved. The incoming claimed equivalence with Conjecture16.6 is discarded. Verification: author_checked_restricted_argument. No proof file recorded.

### P0471. The mean number of sites deep in an extremal DGFF cluster

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Conjecture16.6; PDF222.

**Statement.** Show that exp(-alpha*h)*E_nu[F_h] has a finite strictly positive limit, where F_h=sum_z 1{phi_z<=h} under the source extremal cluster law. Ledger caveat: The source asks about a cumulative depth count. No unsupported identification of relevant spatial scales with log(h) is used.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: Tonelli yields E[F_h]=sum_z P(phi_z<=h). For beta>alpha it also gives G(beta):=sum_z E[exp(-beta*phi_z)]=beta*integral_0^infinity exp(-beta*h)*E[F_h] dh, allowing infinite values. If the desired limit is c, the Abelian implication is (beta-alpha)*G(beta)->alpha*c as beta decreases to alpha. The converse needs more information: the increasing function f(h)=exp(alpha*h)*(1+epsilon*sin(h)), with 0<epsilon<alpha/sqrt(alpha^2+1), has the same leading Laplace pole but exp(-alpha*h)*f(h) has no limit. Thus proving a pole alone would not settle the pointwise cluster asymptotic. Obstruction: No asymptotic for the actual cluster transform or a valid Tauberian remainder is established. The oscillatory function diagnoses an implication, not the DGFF conjecture. Verification: author_checked_restricted_argument. No proof file recorded.

### P0472. Profile of near-extremal level sets of the 2D DGFF

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Chapter16 target16.7.

**Statement.** The measure eta^D_N = (1/log N) sum_x e^{alpha(h_x - m_N)} delta_{x/N} x delta_{(m_N - h_x)/sqrt(log N)} converges in law to c Z^D(dx) x 1_{[0,infty)}(h) h e^{-h^2/2g} dh.

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature. Status search: Primary later theorem read directly; exclude from open-problem count. Admission: not admitted; result_status: literature_resolved. Resolution record: Biskup-Gufler-Louidor, Near-maxima of the two-dimensional DGFF, arXiv2010.13939v3 and AIHP2024, Theorem2.3 PDF4 proves the near-maximum profile. Remark2.4 specifies full-closure canonical-domain versus compact-interior general-approximation scope (source: Biskup, Gufler, Louidor: Near-maxima of the two-dimensional DGFF, dgff_near_maxima_2024, Theorem2.3 and Remark2.4; PDF4).

**Our work.** Not admitted (result_status: literature_resolved). Reason: Biskup-Gufler-Louidor, Near-maxima of the two-dimensional DGFF, arXiv2010.13939v3 and AIHP2024, Theorem2.3 PDF4 proves the near-maximum profile. Remark2.4 specifies full-closure canonical-domain versus compact-interior general-approximation scope. No attempt is recorded for this row in attempts.jsonl.

### P0473. Universality of two-dimensional log-correlated level-set processes

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Problem16.8; PDF222-223.

**Statement.** Under the source continuum Green-kernel limit and uniform microscopic covariance-increment limit, prove analogues of the DGFF intermediate and full extremal process limits. Ledger caveat: The complete covariance hypotheses matter; a bounded covariance difference alone is weaker than the source premises.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: To test a naive bounded-perturbation argument, add one independent Gaussian W to every DGFF site. The covariance changes by the bounded constant Var(W), yet the centered maximum changes exactly by W. Intermediate threshold counts are also shifted in height, giving a random multiplicative change of their limiting spatial intensity rather than an identical limit. This does not refute the stated conjecture: the added constant changes the macroscopic covariance and so violates its prescribed continuum Green limit. It does show why comparison inequalities using only a uniform covariance error cannot identify the same extremal law. Microscopic perturbations can likewise change cluster decorations even when macroscopic behavior agrees. Obstruction: No general comparison theorem proving the full source process convergence; the restricted rapidly decaying Gaussian perturbation case is already discussed in the source. Verification: author_checked_restricted_argument. No proof file recorded.

### P0474. Intermediate level-set limits for uniformly convex gradient fields

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Problem16.9; PDF223-224.

**Statement.** Prove the scaling limit of intermediate level-set measures for two-dimensional gradient models with even uniformly strictly convex potentials and zero boundary values. Ledger caveat: The field convergence as a distribution and leading maximum asymptotics are not the desired rare-level measure theorem.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: For a quadratic potential equal to kappa times the DGFF quadratic potential, the full field is exactly kappa^(-1/2) times the reference DGFF. Thus its logarithmic variance constant is g/kappa and the intermediate level 2*sqrt(g/kappa)*lambda*log(N) reduces exactly to the known DGFF level after multiplication by sqrt(kappa). This checks the necessary stiffness normalization. For general uniformly convex potentials, Gaussian exponential-moment comparison can give upper tails on the logarithmic scale, but does not automatically recover the Mills prefactor or the mixed high-point moments that determine the chaos limit. A field-level central limit statement cannot be inserted into an N-dependent indicator of a rare logarithmic-height event. Obstruction: No extension from quadratic to general uniformly convex potentials. No moment convergence at moving rare-event thresholds is assumed. Verification: author_checked_restricted_argument. No proof file recorded.

### P0475. DGFF over an ergodic uniformly elliptic random conductance model: level sets and extremal process

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Chapter16 target16.10.

**Statement.** For uniformly elliptic conductances with a shift-invariant ergodic law, prove for almost every realisation the analogues of Theorems 2.7 and 9.3 for the associated DGFF. Ledger caveat: Held direction; incoming claims are not promoted or counted as substantive main-campaign attempts.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: none recorded in the ledger. Admission: not admitted; result_status: held. Resolution record: Later2025 random-conductance field/Green convergence must be compared to the exact microscopic covariance and rare-level target before admission.

**Our work.** Not admitted (result_status: held). Reason: Later2025 random-conductance field/Green convergence must be compared to the exact microscopic covariance and rare-level target before admission. No attempt is recorded for this row in attempts.jsonl.

### P0476. Scaling limit of local-time level sets of planar random walk in the full range of eta

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Chapter16 target16.11.

**Statement.** Show that a suitably normalised level set (16.19) of the local time of simple random walk on D_N (run to a multiple theta of the cover time), or the associated point measure, admits a scaling limit for all 0 < eta < 1 + (1/2) sqrt theta. Ledger caveat: Held direction; incoming claims are not promoted or counted as substantive main-campaign attempts.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: none recorded in the ledger. Admission: not admitted; result_status: held. Resolution record: Later wired-boundary local-time results do not directly match the torus and inverse-origin-local-time target; exact current status remains unchecked.

**Our work.** Not admitted (result_status: held). Reason: Later wired-boundary local-time results do not directly match the torus and inverse-origin-local-time target; exact current status remains unchecked. No attempt is recorded for this row in attempts.jsonl.

### P0477. A typical-displacement upper bound in a DGFF landscape

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Problem16.12; PDF225; exponent13.9 PDF183.

**Statement.** Prove the proposed quenched high-probability upper bound on displacement at time T, with exponent theta(beta) from equation13.9 and the stated subpolynomial correction. Ledger caveat: The source writes psi in16.20 while13.9 calls the exponent theta; the intended exponent is theta. Expected exit-time bounds alone do not give this probability upper bound.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: A commute-time identity controls the sum of opposite hitting times, not a lower bound of comparable size for each direction. A unit-conductance star with n vertices gives a concrete check: from a leaf a to its center b the hitting time is1, while the reverse mean is2*n-3; their sum is2*n-2=2*|E|*R(a,b). Thus a large commute time cannot be assigned to the outward hitting time. Even a genuine large expectation need not give a lower-tail bound: a nonnegative variable equal to n^2 with probability1/n and zero otherwise has mean n but is zero with probability tending to one. A displacement upper bound therefore needs a genuine lower-tail control on exit times or a suitable heat-kernel estimate, beyond these expectation identities. Obstruction: No claim that exit-time concentration fails in the DGFF model. The examples invalidate proposed proof implications, not the requested estimate. Verification: author_checked_restricted_argument. No proof file recorded.

### P0478. A joint continuum limit for Liouville Langevin motion

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Problem16.13; PDF226-227.

**Statement.** Find suitable time scalings so that the regularized diffusion dX=beta*grad(h_epsilon)(X)dt+sqrt(2)dB converges jointly with its field to a nonconstant continuous process coupled to the CGFF. Ledger caveat: This is the drifted diffusion in the source. Its Dirichlet energy differs from that of a pure time change of Brownian motion.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: For smooth h, L=Delta+beta*grad(h) dot grad equals exp(-beta*h)*div(exp(beta*h)*grad). Integration by parts on compactly supported smooth functions gives E_h(f,g)=integral grad(f) dot grad(g)*exp(beta*h)dx on L2(exp(beta*h)dx). The random weight therefore enters both the speed measure and the energy. Weak convergence of the speed measures alone does not determine the limiting form. As a one-dimensional diagnostic, rapidly alternating conductivities1 and2 have arithmetic-mean speed density3/2 but harmonic-mean effective energy coefficient4/3; a constant conductivity3/2 has the same speed density and energy coefficient3/2. The two resulting effective generators differ. Thus a chaos-measure limit cannot by itself identify the Langevin path limit. Obstruction: No joint tightness, form convergence or renormalized drift construction is proved. The incoming field-independent energy and consequent Brownian-time-change identification are discarded. Verification: author_checked_restricted_argument. No proof file recorded.

### P0479. Scaling law of effective resistance in DGFF conductances

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Problem16.14; PDF227.

**Statement.** Characterize the joint limiting distribution of (log(N))^(-1/2)*log(R_eff(floor(N*x),D_N complement)) for the source DGFF conductance network. Ledger caveat: Keep the field pinning and boundary normalization fixed. Bounds involving only global field extrema are too coarse to identify this law.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded primary-source search2026-09-07 distinguished later near-maximum and wired-domain local-time progress. No current-openness certificate for these eleven historical-source targets. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted calculation or proof-obstruction analysis after primary-source comparison. Result: For conductances c_xy=exp(beta*(h_x+h_y)), adding a constant a to the field multiplies every conductance by exp(2*beta*a) and every effective resistance by exp(-2*beta*a). This gives an exact normalization check. If m<=h_x<=M on the finite network, Rayleigh monotonicity gives exp(-2*beta*M)*R_unit<=R_h<=exp(-2*beta*m)*R_unit. Since the DGFF extrema are of logarithmic order, these elementary bounds leave a window of order log(N) in log resistance, far larger than the proposed sqrt(log(N)) scale. They cannot justify a Brownian maximum/minimum sandwich or a CGFF limit. The missing work is control of multiscale flows and cutsets that exploits cancellation and typical field structure. Obstruction: No tightness or limiting resistance field is identified; the incoming asserted Brownian-functional bounds are not retained. Verification: author_checked_restricted_argument. No proof file recorded.

### P0480. Scaling limit of the current-minimising path in the DGFF network

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Chapter16 target16.15.

**Statement.** Prove that the joint law of the DGFF and the random path P minimising the effective-resistance energy between two boundary points admits a non-degenerate scaling limit. Ledger caveat: Held direction; incoming claims are not promoted or counted as substantive main-campaign attempts.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: none recorded in the ledger. Admission: not admitted; result_status: held. Resolution record: A measurable path-selection/decomposition rule and continuum topology must be fixed before counting this direction as a distinct attempted problem.

**Our work.** Not admitted (result_status: held). Reason: A measurable path-selection/decomposition rule and continuum topology must be fixed before counting this direction as a distinct attempted problem. No attempt is recorded for this row in attempts.jsonl.

### P0481. Hausdorff dimension of the continuum DGFF current path and of the energy support

**Source.** Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (biskup_dgff_extrema_2020), Chapter16 target16.16.

**Statement.** What is the Hausdorff dimension of the continuum random path of Problem 16.15, and, for the electric current between opposite sides of a square, what is the dimension of the support of the energy? Ledger caveat: Held direction; incoming claims are not promoted or counted as substantive main-campaign attempts.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: none recorded in the ledger. Admission: not admitted; result_status: held. Resolution record: The proposed continuum geometric object and its dimension statement require a precise definition before admission.

**Our work.** Not admitted (result_status: held). Reason: The proposed continuum geometric object and its dimension statement require a precise definition before admission. No attempt is recorded for this row in attempts.jsonl.

### P0482. Ballisticity and an absolutely continuous stationary environment law

**Source.** Drewitz and Ramirez: Selected topics in random walks in random environment (drewitz_ramirez_rwre_2014), Open question2.19 PDF24; Corollary2.15 PDF20-21.

**Statement.** Under stationary ergodicity and ellipticity, does directional ballisticity imply an invariant probability law for the environment viewed from the particle that is absolutely continuous with respect to the environment law? Ledger caveat: The opposite implication, assuming directional transience, is already Corollary2.15 of the source. Its stationary-increment recurrence argument supplies strict positive speed; this is not an unresolved part of the target.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded2026-09-07 primary searches and archived later theorems checked. No current-openness certificate; known stationary/non-nestling/homogeneous cases credited. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted argument and corrected proof-obstruction analysis. Result: Let R be the environment transition kernel. Every P*R^i is absolutely continuous with respect to the translation-invariant P. Its density is the finite sum f_i(omega)=sum_x P_(-x),omega[X_i=0], obtained by changing variables under a spatial shift in the annealed endpoint formula. Set g_n=(1/n)*sum_(i=0)^(n-1) f_i. If these densities are uniformly integrable in L1(P), Dunford-Pettis gives a weak-L1 convergent subsequence g_n to g, with g>=0 and integral g=1. For bounded measurable h, integral(Rh-h)*g_n dP=((P*R^n)h-P h)/n tends to zero. Weak-L1 convergence passes both bounded test functions, so g dP is invariant. A uniform Lp bound for some p>1 would suffice, since integral_(g_n>K) g_n<=K^(1-p)*integral g_n^p. This isolates an explicit missing estimate: positive speed must supply enough control of these occupation densities, not merely weak compactness of the environment space. Obstruction: No density-uniform-integrability estimate follows here from ballisticity. The invariant-law-to-positive-speed direction is credited to the source; no unsupported assertion that iid regeneration alone always gives a full-space absolutely continuous invariant law. Verification: author_checked_restricted_argument. No proof file recorded.

### P0483. Directional transience versus positive speed under uniform ellipticity

**Source.** Drewitz and Ramirez: Selected topics in random walks in random environment (drewitz_ramirez_rwre_2014), Open question2.20 PDF24; renewal identities PDF47-49.

**Statement.** For nearest-neighbor iid uniformly elliptic RWRE on Z^d, d>=2, does transience in direction ell imply positive limiting speed in that direction? Ledger caveat: Equivalence of conditions(T) and(Tprime), proved by Guerra-Ramirez, does not answer this question.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded2026-09-07 primary searches and archived later theorems checked. No current-openness certificate; known stationary/non-nestling/homogeneous cases credited. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted argument and corrected proof-obstruction analysis. Result: Uniform ellipticity gives a precise finite-trap bound. Suppose every site of a finite set A has a nearest-neighbor path of at most m steps leading outside A, and every transition probability is at least kappa. At each block of m steps before exit, the conditional probability of leaving is at least kappa^m. The strong Markov property yields P_x,omega[tau_A>j*m]<=(1-kappa^m)^j and E_x,omega[tau_A]<=m*kappa^(-m). For A=[-R,R]^d intersect Z^d, m=2R+1 works by moving along one coordinate. Thus no fixed-size trap has an arbitrarily large quenched mean under uniform ellipticity. But the bound grows exponentially with R; it cannot be summed over the random spatial extent explored before regeneration without a further tail estimate. For coordinate directions, the source renewal formula gives positive speed exactly when the conditional mean regeneration time is finite; almost-sure finite regeneration times alone do not supply it. Obstruction: No estimate on the distribution of the size or shape of a regeneration excursion, and no proof that transience implies an integrable regeneration time. Verification: author_checked_restricted_argument. No proof file recorded.

### P0484. Ballisticity under the ellipticity moment condition

**Source.** Drewitz and Ramirez: Selected topics in random walks in random environment (drewitz_ramirez_rwre_2014), Open question 2.22, p. 25.

**Statement.** For d >= 2, is every RWRE satisfying (E), (IID) and max_e E[1/(1 - omega(0,e) omega(0,-e))] < infinity which is transient in direction l ballistic in direction l? (Known for Dirichlet environments in d >= 3 by Sabot.)

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature. Status search: none recorded in the ledger. Admission: not admitted; result_status: literature_resolved. Resolution record: Literal source moment is automatic since omega(0,e)*omega(0,-e)<=1/4. The intended edge product uses omega(e,-e). Even that corrected sufficiency claim is false: Fribergh-Kious Proposition4.4 constructs elliptic iid directionally transient zero-speed walks in dimension D=d+1>=3 with at least two outgoing edges per vertex of probability>=c=1/(4(d+1)). Any single transition is thus<=1-c, so every corrected edge product is<=(1-c)^2 and its reciprocal escape denominator is uniformly bounded. Larger hypercube traps cause zero speed. No new counterexample claimed (source: Fribergh and Kious: Local trapping for elliptic random walks in random environments, fribergh_kious_trapping_2015, Proposition4.4 PDF24-25; construction PDF22-24).

**Our work.** Not admitted (result_status: literature_resolved). Reason: Literal source moment is automatic since omega(0,e)*omega(0,-e)<=1/4. The intended edge product uses omega(e,-e). Even that corrected sufficiency claim is false: Fribergh-Kious Proposition4.4 constructs elliptic iid directionally transient zero-speed walks in dimension D=d+1>=3 with at least two outgoing edges per vertex of probability>=c=1/(4(d+1)). Any single transition is thus<=1-c, so every corrected edge product is<=(1-c)^2 and its reciprocal escape denominator is uniformly bounded. Larger hypercube traps cause zero speed. No new counterexample claimed. No attempt is recorded for this row in attempts.jsonl.

### P0485. Transience of elliptic iid environments in dimension at least three

**Source.** Drewitz and Ramirez: Selected topics in random walks in random environment (drewitz_ramirez_rwre_2014), Open question2.23 PDF25.

**Statement.** Is every nearest-neighbor elliptic iid random walk in random environment on Z^d transient when d>=3? Ledger caveat: Transience means finitely many visits to each site, not transience in a specified direction. The following homogeneous calculation is a classical special case.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded2026-09-07 primary searches and archived later theorems checked. No current-openness certificate; known stationary/non-nestling/homogeneous cases credited. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted argument and corrected proof-obstruction analysis. Result: For a deterministic homogeneous elliptic environment, the increments are iid. Nonzero mean gives transience by the strong law. If the mean is zero, nearest-neighbor steps force p(e_i)=p(-e_i)>0 for every i. The characteristic function is phi(t)=2*sum_i p(e_i)*cos(t_i). Its absolute value equals1 only at the two torus points with all coordinates0 or all coordinates pi. Taylor expansion at each gives |phi(t)|<=1-c*dist(t,S)^2 locally, while compactness bounds it strictly below1 elsewhere. Fourier inversion therefore bounds the return probability by C*n^(-d/2). The sum over n is finite for d>=3, proving transience through the expected visit count. For a spatially varying environment the quenched increments are no longer iid and there is no one fixed characteristic function whose nth power gives the transition law. Obstruction: No heat-kernel estimate for general iid elliptic environments. A central limit theorem by itself is not a local return-probability bound. Verification: author_checked_restricted_argument. No proof file recorded.

### P0486. Directional zero-one law beyond the plane

**Source.** Drewitz and Ramirez: Selected topics in random walks in random environment (drewitz_ramirez_rwre_2014), Open question3.2 PDF42.

**Statement.** For elliptic iid nearest-neighbor RWRE on Z^d, d>=3, prove or disprove P_0[A_ell] in{0,1} for every direction ell. Ledger caveat: A_ell and A_minusell are disjoint by definition. Showing their intersection is empty proves no zero-one law. The source credits the dimension-two theorem to Zerner-Merkl.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded2026-09-07 primary searches and archived later theorems checked. No current-openness certificate; known stationary/non-nestling/homogeneous cases credited. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted argument and corrected proof-obstruction analysis. Result: There is a useful stationary-measure special case. Suppose additionally that the environment process has an invariant probability Q absolutely continuous with respect to P. Kozlov gives Q equivalent to P. Put q(omega)=P_0,omega[A_ell]. By the Markov property and invariance of A_ell under deleting finitely many steps, q(eta_n)=E[1_Aell|omega,X_0,...,X_n] is a bounded martingale and tends to1_Aell. Under initial law Q the variables q(eta_n) all have the same distribution, so q(eta_0) itself must take values only0 and1. The harmonic identity q(omega)=sum_e omega(0,e)*q(t_e omega), together with ellipticity, then forces every neighboring shift to have the same value on a common full-measure set. Spatial ergodicity of P makes q constant, establishing the directional zero-one law in this restricted class. The absent invariant law is the obstruction to applying this stationary argument to all iid environments. Obstruction: No existence proof for Q in a general elliptic iid environment. The argument is a credited stationary special-case rederivation, not a solution of the higher-dimensional question. Verification: author_checked_restricted_argument. No proof file recorded.

### P0487. Does positive velocity force a quantitative ballisticity condition?

**Source.** Drewitz and Ramirez: Selected topics in random walks in random environment (drewitz_ramirez_rwre_2014), Open question3.20 PDF52; Theorem3.17 PDF51.

**Statement.** Under iid uniform ellipticity, does positive velocity in direction ell imply the polynomial ballisticity condition(P)_M for M>15d+5? Ledger caveat: The source links stretched-exponential slab conditions to exponential moments of the spatial regeneration radius, not to an asserted equivalence with arbitrary time moments.

**Status.** Historical status: source_says_open. Current-literature status: unverified. Status search: Bounded2026-09-07 primary searches and archived later theorems checked. No current-openness certificate; known stationary/non-nestling/homogeneous cases credited. Admission: admitted; result_status: unsolved.

**Our work.** Method: Integrator-authored exact restricted argument and corrected proof-obstruction analysis. Result: For the known non-nestling subcase with local projected drift at least delta>0 everywhere, let xi be a one-step displacement in direction ell. Since |xi|<=1, E[exp(-a*xi)|past]<=1-a*delta+a^2*exp(a)/2. Choosing0<a<=min(1,delta/exp(1)) makes exp(-a*X_n dot ell) a nonnegative supermartingale. Stopping at a backward level-bL gives probability at most exp(-a*bL) of ever reaching it. Nearby directions retain a positive drift lower bound, giving the slab decay needed for(T), and hence the known polynomial condition. Positive limiting velocity alone supplies no such uniform local drift. Even at the level of abstract regeneration times, finite first moment gives only n*P[T>n]->0: the valid tail P[T>n]=1/((n+1)*log(n+exp(1))^2), n>=0, has finite mean and no moment1+epsilon. This is an implication counterdiagnostic, not a RWRE construction or a claimed equivalence between slab exits and time moments. Obstruction: No self-improvement from positive velocity to the required exit bound in the nestling case, and no counterexample satisfying iid uniform ellipticity. Verification: author_checked_restricted_argument. No proof file recorded.

### P0488. Equivalence of the ballisticity conditions (T) and (T')

**Source.** Drewitz and Ramirez: Selected topics in random walks in random environment (drewitz_ramirez_rwre_2014), Open question 3.28, p. 55.

**Statement.** Is Sznitman's condition (T') equivalent to condition (T) for RWRE in uniformly elliptic i.i.d. environments?

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature. Status search: none recorded in the ledger. Admission: not admitted; result_status: literature_resolved. Resolution record: Guerra-Ramirez Theorem2.1 proves(Tprime) implies(T) under iid uniform ellipticity in d>=2. The reverse implication follows directly from the definitions, resolving the historical question (source: Guerra and Ramirez: A proof of Sznitman conjecture about ballistic RWRE, guerra_ramirez_ballistic_2018, Theorem2.1 PDF3).

**Our work.** Not admitted (result_status: literature_resolved). Reason: Guerra-Ramirez Theorem2.1 proves(Tprime) implies(T) under iid uniform ellipticity in d>=2. The reverse implication follows directly from the definitions, resolving the historical question. No attempt is recorded for this row in attempts.jsonl.
