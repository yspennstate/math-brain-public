# T284 work log

Task received: 14 November 2026, approximately 21:27 +04 (Asia/Tbilisi).
Task: “push this problem forward by one checkable piece.”

## 21:27–21:30: orientation and literature

Read the compute governor: status ok, mode owner_away_open. All substantive programs in this session use OMP_NUM_THREADS=1 and nice -n 15; no large computation is planned. Read the startup-memory index, startup card, and the prior T284 memory `t284_ogp_chain_and_estimator_stability_meet_at_log_n_2026_11_01.md`. That memory concerns shortest-path stability scales, not a solution of the independent-set question.

The current task's restriction to writes in this folder overrides the earlier global requests to mutate the mesh, checklist, and brain. Those external write commands are not run. No git or subagents.

Web search queries included:
- independent set overlap 2026 algorithm random sparse
- independent set 2025 polynomial log d barrier
- arxiv 2411.01836
- independent set sparse random graph all polynomial algorithms hardness 2026 planted clique
- independent sets random graphs success amplification reverse hypercontractivity

Opened primary sources:
- Shuangping Li and Tselil Schramm, *Some easy optimization problems have the overlap-gap property*, arXiv:2411.01836v3, https://arxiv.org/abs/2411.01836 . Shortest paths give a counterexample to a generic OGP-hardness principle; this does not settle T284.
- Abhishek Dhawan, Eren C. Kızıldağ, Neeladri Maitra, Cheng Mao, Timothy L. H. Wee, *Half-Optimal Induced Matchings in Random Graphs: Online and Low-Degree Algorithms*, arXiv:2610.40369, https://arxiv.org/abs/2610.40369 . Its abstract concerns induced matchings and online/low-degree lower bounds.
- Abhishek Dhawan, Nhi U. Dinh, Eren C. Kızıldağ, Neeladri Maitra, Bayram A. Şahin, *Algorithmic Phase Transition for Large Independent Sets in Dense Hypergraphs*, APPROX/RANDOM 2026, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.68 . Its abstract concerns dense hypergraphs and online algorithms.

No whole-problem settlement found. Search results alone are not treated as evidence of a theorem.

## Choice, recorded before proof work

Prove a success-amplification reduction applying to arbitrary randomized polynomial-time algorithms: constant-probability search at density a in G(n,d/n) implies high-probability search at any strictly smaller density b<a, with d fixed. Use independent edge refreshes, reverse hypercontractive small-set expansion to reach the solver's good instances, and deletion of endpoints of edges reintroduced into the proposed independent set. This targets a quantifier in the all-algorithm problem without assuming algorithmic stability. It would make constant-success hardness sufficient for the high-probability question, up to arbitrarily small density slack. Need verify a dimension-free reverse hypercontractive inequality for biased products and quantify the repair loss. No claim of an original general amplification principle or a solution to the main barrier.

## 21:30: analytic input verified

Literature check ended within four minutes of starting (shell clock 21:30 +04). Added the opened survey David Gamarnik, *The Overlap Gap Property: a Geometric Barrier to Optimizing over Random Structures*, arXiv:2109.14409, https://arxiv.org/abs/2109.14409 . No settlement found in this bounded search; this is not an exhaustive assertion about all papers.

Opened Elchanan Mossel, Krzysztof Oleszkiewicz, Arnab Sen, *On reverse hypercontractivity*, arXiv:1108.1210v5, https://arxiv.org/abs/1108.1210 and https://arxiv.org/pdf/1108.1210 . Corollary 1.11 on PDF page 5 states the dimension-free bound for tensor products of arbitrary simple semigroups: ||T_t f||_q >= ||f||_p when q<p<1 and t >= log((1-q)/(1-p)). This includes negative q and biased Bernoulli factors with bias d/n. This is the only non-elementary analytic input planned for the proof.

The argument actually permits inverse-polynomial starting success n^(-s), not merely constant success. For refresh probability delta and r=delta/2, setting p=r and q=-r in Corollary 1.11 gives E[(T_t f)^(-r)] <= 1/E[f] for f in [0,1]. Hence P(T_t f < n^(-h)) <= n^(s-hr). This should yield polynomial overhead with arbitrarily prescribed polynomial failure rate, while a union bound controls every trial's repair failure. This is a strengthened version of the recorded choice, with the same scope.

Priority audit command:
`env OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os; print("OMP_NUM_THREADS=" + os.environ["OMP_NUM_THREADS"]); print("nice=" + str(os.getpriority(os.PRIO_PROCESS, 0)))'`
Output:
```
nice: setpriority: Operation not permitted
OMP_NUM_THREADS=1
nice=20
```
The sandbox denies changing priority; the inherited priority is already 20, lower than the requested 15. Keep the requested launcher and inherited priority 20. No heavy program has run.

## Proof draft saved

Created PROOF.md with the inverse-polynomial-to-high-probability amplification theorem, its finite-n failure bound, the application at the log(d)/d scale, and the exact scope of the success quantifiers. The explicit repair analysis uses delta <= (a-b)/(4 d a^2), r=delta/2, and kappa=(2 log 2-1)/4. The proof imports only Corollary 1.11 from Mossel–Oleszkiewicz–Sen; the remaining argument is written out.

The trial-selection issue is handled by bounding the unconditional repair failure of each predetermined trial and taking a union bound over all trials. No posterior law is asserted after choosing the first successful trial. Next: exact finite enumeration of the refresh posterior, numerical tests of the moment bound, independent algebra checks, and adversarial cases.

## Verifier first launch

Created verify.py. Exact command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify.py`.
The first launch stopped immediately at an attempted 768 MiB address-space cap:
```
ValueError: current limit exceeds maximum limit
```
No verification loop ran. The macOS resource-limit interface rejected the cap. The inputs are explicitly bounded (at most 64 graph states and a 64-by-64 matrix of rational numbers); replace the unsupported cap with recorded limits and measured peak resident memory, retaining the fixed small inputs.

## Exact and numerical verification passed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify.py`
Output:
```
nice: setpriority: Operation not permitted
status: PASS
exact_bayes_identities: 4096
exact_conditional_binomial_cases: 225
conditional_cases_by_set_size: {'2': 192, '3': 32, '4': 1}
boolean_negative_moment_checks: 3060
randomized_negative_moment_checks: 80
ceiling_and_mean_checks: 12933
kappa_decimal: 0.09657359027997265470861606072908828403775006718012762706034
nice: 20
omp_num_threads: 1
elapsed_seconds: 0.2713
max_rss_bytes_macos: 15253504
```
Full data: verification.json. Exact rational enumeration checks Bayes reversal for all 4096 ordered graph pairs on four vertices, then the full conditional binomial distribution for all 225 pairs (H,I) with 2<=|I|<=4 and I independent in H. No numerical approximation is used for these identities. Moment tests cover all nonempty events on three coordinates at twelve parameter choices and 80 nonzero non-Boolean functions on two coordinates. These moment tests are numerical sanity checks, not a substitute for Corollary 1.11. Rounding and mean checks cover 12933 allowed parameter cases.

The repair constant was evaluated independently by Decimal.log and an exact-rational atanh series for log(2); the Chernoff calculation with the optimized Poisson exponent independently returns the same kappa. A second derivation of P(G_e=1 | H_e=0)=delta p uses stationarity and Cov(G_e,H_e)=(1-delta)p(1-p).

## Final adversarial audit and report

Saved AUDIT.md, including two derivations of the refresh posterior; sign checks for negative moments; an optimized Chernoff re-derivation of the repair exponent; and checks for trial selection, rounding, output validation, sampling precision, rational parameters, rare success, and fixed-versus-growing parameters. Corrected the finite-bit budget in PROOF.md to an explicitly integer expression. No change to the mathematical theorem or verifier was required after its passing run.

Saved REPORT.md with verdict PARTIAL. The full T284 barrier is unresolved. This session's completed piece is the reduction from eventual inverse-polynomial success to high-probability success at any strictly smaller fixed density, with a verified finite-n bound. No SOLVED_ELSEWHERE.md is warranted by the bounded search.

Final readback at 21:37 +04 confirmed the report's required first-line verdict, the saved verification data, the finite-bit coupling bound, and the scope of the overlap-scale corollary. Renamed the bit-count variable to w to distinguish it from algorithm B. All six deliverables are present in this folder. No additional computation or external write was performed.
