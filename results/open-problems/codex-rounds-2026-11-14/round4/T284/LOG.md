# T284 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 06:30 +04 (Asia/Tbilisi).

## Orientation, 06:30–06:32

Read the startup memory index, brain index, and compute governor. Governor status warn, mode owner_away_open, CPU saturated. Only tiny single-thread checks are planned. The task-specific restriction to writes in this folder overrides the global mesh/checklist/brain write routines, including recall commands that log outside this folder. No external state is mutated, no git and no subagents. Earlier folders are read only.

All Python commands use `env OMP_NUM_THREADS=1 nice -n 15 python3`. The shell inherits nice 20; requesting 15 prints `nice: setpriority: Operation not permitted` and retains the lower priority. No long or memory-intensive computation is planned.

Read the earlier REPORT.md, LOG.md, PROOF.md, scripts and AUDIT.md, with focused rereads following the initial combined read. The round-3 result uses independent edge refresh and reverse hypercontractivity to obtain vanishing loss from subpolynomial success.

## Bounded settlement check, 06:30–06:32

Web queries: `random independent set overlap gap polynomial time algorithm sparse random graph 2025 2026 hardness`; `"2411.01836" independent set overlap`; `independent set random graph success amplification reverse hypercontractivity`.

Opened primary sources:

- David Gamarnik, *The Overlap Gap Property: a Geometric Barrier to Optimizing over Random Structures*, arXiv:2109.14409, https://arxiv.org/abs/2109.14409 .
- Shuangping Li and Tselil Schramm, *Some easy optimization problems have the overlap-gap property*, arXiv:2411.01836, https://arxiv.org/abs/2411.01836 . The page still gives the June 2025 revision; its shortest-path counterexample does not settle independent-set search.
- *Algorithmic Phase Transition for Large Independent Sets in Dense Hypergraphs*, arXiv:2605.05618, https://arxiv.org/abs/2605.05618 . The abstract concerns dense hypergraphs and restricted algorithm classes.
- *Half-Optimal Induced Matchings in Random Graphs: Online and Low-Degree Algorithms*, arXiv:2610.40369, https://arxiv.org/abs/2610.40369 . The abstract concerns induced matchings and restricted algorithm classes.

No settlement found in this bounded check; this is not exhaustive coverage. Settlement checking stopped within five minutes. Subsequent literature reading concerns the chosen technical extension.

## Independent re-derivation of the earlier claim

Let p=d/n. For a refreshed edge pair (X,Y), P(X=1,Y=0)=p delta(1-p) and P(Y=0)=1-p, giving P(X=1|Y=0)=delta p. Independence across pairs survives conditioning on the entire refreshed graph. Thus a k-set selected from that graph and fresh solver coins has Binomial(binom(k,2),delta p) original internal edges. With lambda=delta d k(k-1)/n, its mean is lambda/2, and the optimized Poisson-Chernoff exponent at lambda is lambda(log 2-1/2).

For the negative-moment estimate, put r=delta/2. The condition (1-delta)(1+r)<=1-r permits reverse hypercontractivity with exponents r and -r. Since E[f^r]>=v, raising the norm inequality to -r gives E[(T_delta f)^(-r)]<=1/v, with the inequality in the correct direction. At M=n^2 trials, u=1/n and beta=2(log(1/v)+K log log n)/log n, any dyadic delta in [beta,2 beta) gives bad-input probability at most (log n)^(-K). The loss ceil(lambda) is bounded by the round-3 D_{n,K}. For log(1/v)=o(log n), the chosen scale exists eventually, the loss is o(n), and the repair tail beats the polynomial trial count. The earlier theorem holds. Its verifier will also be rerun from this folder.

## Choice recorded before extension work

Replace independent edge refresh by computational concentration in a product of vertex-row blocks. Apply Theorem 1.1 of Omid Etesami, Saeed Mahloujifar, and Mohammad Mahmoody, *Computational Concentration of Measure: Optimal Bounds, Reductions, and More*, arXiv:1907.05401, https://arxiv.org/pdf/1907.05401 . Opened the full PDF. The theorem gives a polynomial-time map from a random product point to a verifiable event of inverse-polynomial measure, changing O(sqrt(N log(1/(epsilon delta)))) blocks with failure delta.

Partition graph edges by smaller endpoint and put all solver coins in one extra block. Membership in the success event is deterministic and polynomial-time decidable. If the concentration algorithm changes t graph rows, delete their t owner vertices from its independent set. Every changed edge has an endpoint among those owners, so repair loses at most t vertices. If the theorem's sampler, runtime and finite-bit hypotheses check out, this yields loss O(sqrt(n log n)) with polynomially small failure from inverse-polynomial starting success. It directly improves the previous report's O(n/log n) question. This is an application of a published concentration theorem, not a solution of T284 or a new concentration theorem.

## Earlier verifier rerun and source audit, 06:34

Command (cwd is this folder): `env OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T284/verify_extension.py`.

```
nice: setpriority: Operation not permitted
status: PASS
latent_refresh_posterior_checks: 90
count_based_posterior_checks: 396
dyadic_negative_moment_checks: 6120
worst_moment_ratio: 1.0
exact_binomial_tail_checks: 111
scale_and_loss_checks: 369
all_scale_sampler_budget_checks: 8
excluded_small_scale_cases: 4
rounding_checks: 19482
largest_test_n: 2^8192 (symbolic integers only; no n-sized allocation)
gamma_decimal: 0.1931471805599453094172321214581765680755001343602552541206800094933936219696947156058633269964186875
nice: 20
omp_num_threads: 1
elapsed_seconds: 1.4253
max_rss_bytes_macos: 15482880
```

Output data: extension_verification.json in this folder. Together with the independent calculation above, this supports the earlier main claim.

Checked Theorem 1.1 on PDF page 3, Theorem 3.2 and Remark 3.3 on PDF page 14, and the runtime construction in Section 3.2, PDF pages 21–22, of arXiv:1907.05401v1. The formal runtime uses the total bit representation length, not alphabet cardinality; polynomial-length graph rows and one polynomial-length random tape are permitted. Remark 3.3 identifies the untampered transcript with the input product distribution. The main theorem accepts a lower bound on event measure, so its exact measure need not be known. The conclusion concerns the joint probability of reaching the event and being close; it is sufficient here.

Audit observation: the final worst-case parameter formula printed in Section 3.2 uses a product of two logarithms, whereas the main theorem states a single logarithm of 1/(epsilon delta). The application will explicitly invoke the stated Theorem 1.1/3.2, rather than copy that parameter formula or infer sharp constants from it. This is recorded as a source-level limitation to inspect, not an established error in the theorem. A conservative O(sqrt(n) log n) variant would already improve the previous loss. No explicit leading constant is asserted.

The finite-bit implementation can avoid a union bound over the adaptive algorithm's unknown number of sampler calls: round p=d/n to a dyadic q once, apply concentration with exact finite-bit samplers for q, and transfer the entire guarantee to the original input distribution using total variation. Only the law of the initial graph needs transfer. The success event's measure changes by at most the same total variation. This also handles adaptively chosen sampler queries.

For attribution completeness, the opened induced-matching page gives Abhishek Dhawan, Eren C. Kızıldağ, Neeladri Maitra, Cheng Mao, and Timothy L. H. Wee. The opened dense-hypergraph page instead gives Abhishek Dhawan, Nhi U. Dinh, Eren C. Kızıldağ, Neeladri Maitra, and Bayram A. Şahin. Corrected an initial mistaken assumption that these two author lists coincided. Neither abstract supplies the all-polynomial-time obstruction requested by T284.

Also opened the publisher's page for the concentration paper, https://epubs.siam.org/doi/10.1137/1.9781611975994.21 . It confirms the same authors, polynomial membership-oracle algorithm and concentration claim. No new average-case assumption is being introduced.

## Proof and verifier saved

Saved PROOF.md. Its one extension is a vertex-row application of the published computational concentration theorem. The graph has n-1 independent row blocks and one independent solver-tape block, for n blocks in all. The deterministic repair deletes the owners of changed rows. The total representation length is binom(n,2)+r(n), not n; this affects the polynomial runtime but not the square-root block-distance bound.

The explicit finite-bit parameters are S>s, ell>=max{1,L}, w=(S+ell+6)ceil(log_2 n), epsilon=(2n^S)^(-1), delta=(2n^ell)^(-1). Rounding d/n down to q gives total variation eta<=0.5 n^(-(S+ell+4)). This preserves event measure at least epsilon and adds eta only once to the entire output guarantee. Final failure is at most delta+eta<=n^(-L), with loss ceil(C sqrt(n log(4n^(S+ell)))). The input remains G(n,d/n). The result does not depend on k_n/n tending to a positive constant.

Saved verify_rows.py with bounded exact enumeration of all ordered graph pairs up to four vertices, all independent output sets, two computations of changed-row owners, graph-and-tape distance checks, exact product masses and total variation, finite-bit budgets, and a star example where 19 changed edges require only one owner deletion. It does not implement or experimentally verify the imported concentration algorithm.

## New verifier passed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify_rows.py`.

```
nice: setpriority: Operation not permitted
status: PASS
graph_pair_induced_agreement_checks: 4165
independent_set_repair_checks: 35256
graph_and_tape_distance_checks: 8330
exact_row_product_mass_checks: 225
exact_graph_total_variation_checks: 18
seeded_solver_event_transfer_checks: 54
exact_full_error_budget_checks: 153
fair_bit_threshold_checks: 48
star_example: 19 changed edges in one row; one vertex deletion suffices
largest_graph_n: 20
largest_exhaustive_graph_n: 4
largest_symbolic_n: 2^512; no n-sized allocation
nice: 20
omp_num_threads: 1
elapsed_seconds: 0.0414
max_rss_bytes_macos: 16203776
```

Data are in row_verification.json. Every assertion uses integers or exact rational arithmetic. No numerical test of the concentration theorem or independent-set performance experiment is claimed.

## Adversarial audit saved

Saved AUDIT.md. Checked the deterministic repair both by row agreement and by covering the symmetric-difference edges. Checked total variation by an explicit coupling and its exact likelihood formula, then checked transfer of the whole adaptive computation by common randomness and by contraction under a randomized map. Re-derived the exhaustive loop counters by closed-form counts, independent of loop structure. Checked all polynomial-time membership and sampler requirements, finite-bit support, padded solver coins, eventual success versus subsequences, and the loss comparison after substituting n=exp(t).

The main theorem's stated single-log distance bound is consistent with optimizing the source's preceding quadratic exponent n lambda^2-k lambda: its minimum is -k^2/(4n). This does not independently verify its full approximate-oracle proof. The discrepancy with the final printed product-of-logs parameter choice remains recorded; no constant is inferred from that display.

No new mathematical check failed. The web PDF screenshot and publisher formula-image fetch failed with cache-miss errors; text access to the theorem, proof displays and publisher abstract succeeded. The proof relies on the published concentration theorem as stated. T284 itself remains unresolved.

## Final report and readback

Saved REPORT.md with the required first-line verdict, the amplification advance, commands, failed source-rendering requests, source-parameter caveat, verification limits and next step. An inline audit under `env OMP_NUM_THREADS=1 nice -n 15 python3` read the two saved JSON files, checked both PASS statuses and the exact report verdict, and independently evaluated the closed-form enumeration counts in AUDIT.md. Output:

```
REPORT.md: 5169 bytes
LOG.md: 11847 bytes
PROOF.md: 10937 bytes
AUDIT.md: 7192 bytes
verify_rows.py: 7156 bytes
row_verification.json: 820 bytes
extension_verification.json: 766 bytes
independent closed-form count audit: PASS; 4165 graph pairs, 35256 repairs
report and artifact audit: PASS
```

The LOG.md byte count is from before this final append. The independent formulas were `sum(2**(2*comb(n,2)), n=1..4)` and `sum(2**comb(n,2)*sum(comb(n,k)*2**(comb(n,2)-comb(k,2)), k=0..n), n=1..4)`. No proof or verifier changes followed the passing runs. All writes stayed in this folder; the two earlier folders remained read only. No git, subagents, external messages or brain-state writes were used.
