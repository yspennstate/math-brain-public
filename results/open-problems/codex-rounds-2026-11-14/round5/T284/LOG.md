# T284 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 09:03 +04 (Asia/Tbilisi).

## Orientation and bounded settlement check

Read the three earlier REPORT.md, LOG.md, PROOF.md and Python verifiers, with focused rereads after combined output was too long. Read the startup memory index, brain index and compute state (status ok, mode owner_away_open). The task's restriction to this folder overrides external mesh, checklist and brain writes; recall commands that log outside this folder were not run. No git, subagents or external messages. All program launches use OMP_NUM_THREADS=1 and nice -n 15. The sandbox rejects raising the inherited nice value from 20 to 15; priority remains 20.

The initial web settlement check took less than five minutes. Queries included `random independent set sparse graph polynomial algorithm log d overlap gap 2026 hardness`, `2411.01836`, and `1907.05401`. Opened:

- David Gamarnik, *The Overlap Gap Property: a Geometric Barrier to Optimizing over Random Structures*, arXiv:2109.14409, https://arxiv.org/abs/2109.14409 .
- Shuangping Li and Tselil Schramm, *Some easy optimization problems have the overlap-gap property*, arXiv:2411.01836, https://arxiv.org/abs/2411.01836 . The page still gives the June 2025 revision and concerns shortest paths.
- Alexander S. Wein, *Optimal low-degree hardness of maximum independent set*, https://ems.press/journals/msl/articles/4180358 . The abstract establishes a restriction for low-degree algorithms.
- Omid Etesami, Saeed Mahloujifar and Mohammad Mahmoody, *Computational Concentration of Measure: Optimal Bounds, Reductions, and More*, arXiv:1907.05401, https://arxiv.org/pdf/1907.05401 . Checked Theorem 1.1, Theorem 3.2 and Remark 3.3.

No settlement found; this bounded check is not exhaustive. Later literature reading concerns only the selected extension.

## Independent recheck of round 4

If G and H differ in the blocks whose owners form D, every changed edge has its smaller endpoint in D. Thus G and H agree on the complement of D, and deleting I intersect D repairs any independent set I of H, even for adaptively chosen H. This independently re-derives the deterministic step.

There are n-1 disjoint edge-row blocks and one padded solver-tape block. The product dimension controlling distance is n; total representation length is binom(n,2)+r(n). The opened source explicitly distinguishes these quantities. Its stated theorem bounds distance by O(sqrt(n log(1/(epsilon delta)))); applying epsilon=1/(2n^S) and delta=1/(2n^ell) gives the round-4 radius. Dyadic rounding with w=(S+ell+6)ceil(log_2 n) changes the initial law by at most binom(n,2)2^-w. Coupling the complete randomized computation transfers the guarantee once, including adaptive queries. The round-4 claim holds conditional on the published concentration theorem, with its previously recorded source-parameter caveat. A verifier rerun follows.

## Extension choice, before proof and computation

Determine whether the O(sqrt(n log n)) loss in a general amplification theorem can be improved to o(sqrt(n log n)) when final failure must be n^-L. Examine an obstruction from actual independent-set feasibility, rather than arbitrary product events.

For every fixed d>0, there are linearly many isolated four-vertex tree components. Conditional on their vertex sets and the remaining graph, each is a uniform labelled tree: twelve paths have independence number two and four stars have independence number three. Consequently alpha(G) is conditionally a fixed shift of Bin(t,1/4), where t is linear in n. A binomial change of measure should give a lower bound exp(-O_d(r^2/n)) on infeasibility at target k-r whenever infeasibility at k has constant probability. For a concrete polynomial-time solvable example, use d=1/2, a central-limit target, and a solver that exhaustively handles components only up to logarithmic size. This would show that the round-4 loss has optimal order in its general class; it would not settle the large-d overlap barrier.

The four-vertex-component smoothing argument is already present in Tom Bohman and Jakob Hofstad, *Two-Point Concentration of the Independence Number of the Random Graph*, https://doi.org/10.1017/fms.2024.6 (opened). No novelty claim is made for that mechanism. A search located Boris Pittel's subcritical central limit theorem, which must be opened and checked before use. The intended new deliverable is its quantitative consequence for the loss required by amplification.

## Earlier verifier rerun

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T284/verify_rows.py` (cwd is this folder).

Output: PASS; 4165 graph pairs, 35256 repairs, 8330 graph-and-tape distances, 225 product masses, 18 exact total-variation checks, 54 event transfers, 153 error budgets, 48 fair-bit sampler checks. Runtime 0.0367 seconds; peak RSS 16056320 bytes; OMP_NUM_THREADS=1; nice=20. The earlier script writes row_verification.json in the current folder; its source and earlier folder were unchanged.

## Source check and proof saved

Opened the full Section 5 of Bohman--Hofstad, including Theorem 12, Lemma 13 and the shifted-binomial representation. It gives mu_d=(2/3)d^3 exp(-4d), four stars and twelve paths, and a conditional Bin(t,1/4). These parts were independently re-derived by counting component constraints.

Opened Boris Pittel, *On tree census and the giant component in sparse random graphs*, Random Structures & Algorithms 1 (1990), 311--342, https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.3240010306 . The publisher abstract states the subcritical Gaussian limit for alpha with mean n(beta+beta^2/2)/d and variance n[(beta+beta^2/2)/d-(d+1)beta^2/d^2], beta exp(beta)=d. Direct DOI opening failed; the PDF URL redirected to this abstract. The full proof was not accessible, and no theorem number or tail rate is claimed.

Saved PROOF.md. Its main quantitative statement is: if P(alpha<k_n)>=1/3, then for r_n=o(n), P(alpha<k_n-r_n)>=exp(-320)/16 times exp(-40 r_n^2/(mu_d n)), eventually. A tilted-binomial window proves the estimate without any moderate-deviation theorem. Selecting a constant mass of suitable histories before estimating the tiny tail avoids subtracting an O(1/n) exceptional probability from it.

At d=1/2, Pittel's central limit theorem supplies a polynomial-time computable central target k_n. Exhaustive search on components of size at most 64 ceil(log_2 n) is a polynomial worst-case-time solver and is optimal with probability tending to one. Its success at k_n tends to 1/2. Every algorithm with failure n^-L at target k_n-r_n must lose Omega(sqrt(n log n)) vertices. Thus the round-4 radius has optimal order as a general theorem over all its degrees and targets. This does not establish optimality at the large-d overlap density.

## New bounded verifier passed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify_loss.py`.

```
nice: setpriority: Operation not permitted
status: PASS
labelled_four_vertex_trees: 16
independence_number_counts: {3: 4, 2: 12}
prufer_tree_set_agrees: True
exhaustive_graph_checks: 33867
conditional_shape_fibres_checked: 36
exact_component_moment_checks: 18
exact_disjoint_component_checks: 12
forest_shape_checks: 4368
exact_threshold_checks: 5935
exact_binomial_tails_checked: 24
likelihood_identity_checks: 48
rational_constant_checks: 24
minimum_log_tail_margin: 305.198390264462686677691182119107154432965269151693385255438359246029639091366606510140071
beta_at_d_one_half: 0.351733711249195826024909300929951065171464215517111804046643846109960610720338710896832304
limiting_independence_density: 0.827184026127524318418820615277153872386516271612083220402366883463268723113570104256108814
variance_coefficient: 0.084884404352728320204808534773643420124989228144925546547891736003183713076214009481443581
target_rounding_checks: 5
component_cutoff_exponent: -16.8337586915531709644824102079394516023473294671044501076656189782045049862020774436631480
largest_exhaustive_graph_n: 6
largest_binomial_t: 16384
omp_num_threads: 1
nice: 20
elapsed_seconds: 0.949
max_rss_bytes_macos: 157810688
limitations: Finite checks support the elementary application; they do not verify Pittel's CLT or the imported concentration theorem, and do not solve T284.
```

Full data: loss_verification.json. All 33867 labelled graphs up to six vertices were checked. Exact component moments agree with independent formulas. Conditional fibres agree with the shape law; separate forests include up to three four-vertex components. Exact integer binomial sums, followed by 90-digit logarithmic comparisons, check the tail bound through t=16384. The 48 likelihood checks compare direct point-mass ratios with the relative-entropy formula. A rational bisection bracket and an independent Decimal Newton iteration agree on beta; two variance formulas agree. These checks do not replace the proofs or establish a central limit theorem experimentally.

## Adversarial audit and report saved

Saved AUDIT.md. Recounted the labelled trees by paths/stars and by Prüfer codes; re-derived the isolated-component mean and joint-event exponent by distinct constraint counts; checked the full conditional fibre rather than assuming its independence. Re-derived the entropy bound by both log u<=u-1 and its second derivative, and the likelihood identity by direct point masses. Independently checked the constants, integer thresholds, uniformity over conditional histories, positive CLT variance, target computation, and exploration domination for the cutoff solver.

Saved REPORT.md with verdict PARTIAL. The new result is sharpness in order of the earlier amplification theorem in its full generality. The original large-d overlap-barrier problem remains unresolved. No SOLVED_ELSEWHERE.md is warranted. There was no failed mathematical assertion or verifier check. The inaccessible source proof, unchanged concentration-source caveat, restricted role of the subcritical example, and the hypothesis of constant infeasibility are explicit.

Final inline readback command: `env OMP_NUM_THREADS=1 nice -n 15 python3 -` with assertions for both JSON PASS statuses, required report verdict, all seven deliverables, and independent enumeration-count formulas. Output: `artifact and independent count audit: PASS`. Counts were independently obtained as sum_(n=1)^6 2^binom(n,2)=33867, sum_(t=1)^3 16^t=4368, and 1+binom(5,4)+2binom(6,4)=36 conditional fibres. All files stayed in this folder; earlier folders were read only. No proof or verifier changes followed the passing runs.
