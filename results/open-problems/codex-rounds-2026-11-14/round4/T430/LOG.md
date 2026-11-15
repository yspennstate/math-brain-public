# T430 work log

Task received: 15 November 2026, approximately 06:41 Asia/Tbilisi (02:41 UTC).

## 1. Orientation and literature check

Read REPORT.md, LOG.md and PROOF.md in both prior folders, including the original proof's ending and the round 3 source audit. `rg --files` confirms neither folder contains computation scripts. Read the startup memory and compute state: warn, owner_away_open, CPU saturated, 65 percent memory free. No heavy computation is planned. The present instruction forbids writes outside this folder, so global mesh, checklist, recall logging and brain writes are not run. No git or subagents.

Literature search started at 02:41 UTC and finished within five minutes. Web search queries covered supermarket/general-service/stationary/asymptotic-independence/2025/2026, FIFO/global-stability, and corrections to arXiv:1809.05373. Opened the abstract and PDF of Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, *Convergence properties of many parallel servers under power-of-D load balancing*, https://arxiv.org/abs/1809.05373 and https://arxiv.org/pdf/1809.05373. The retrieved PDF bears 13 November 2021. Opened Pooja Agarwal and Kavita Ramanan, *Invariant states of hydrodynamic limits of randomized load balancing networks*, https://arxiv.org/pdf/2008.08510. Its Section 4.2 still states the relevant identification as a conjecture in this version. No verified later resolution found; this is a brief search, not an exhaustive certification. No SOLVED_ELSEWHERE.md is justified.

Local read commands were `cat` and `sed` for the preceding files and `rg --files` for their inventories. No numerical program has run. Subsequent shell commands will use OMP_NUM_THREADS=1 and nice -n 15.

## 2. Independent recheck

The round 3 main claim holds. Condition on inclusion of the tagged server, of probability d/N. In the N+1 system, conditional on inclusion of the tag, the other d-1 distinct sampled servers avoid the newly appended shorter server with probability (N+1-d)/N. Conditional on avoidance their sample is uniform over the same old N-1 competitors, and all tie probabilities agree. The inclusion factor times the arrival rate is lambda*d in both systems. Thus a_(N+1)=(N+1-d)*a_N/N. This derivation uses conditional competitor sampling rather than the earlier favorable-subset numerator or unconditioned Poisson thinning. With d=2 and periodic prefixes N=3m+2, the conditional winning probability is (m+1+(m/2))/(3m+1), giving a_N=lambda*(3m+2)/(3m+1); the next rate is lambda. The count restrictions hold for m>=d-1. Its positive limiting rate therefore does not imply monotonicity.

The original fair empty/busy mixture also checks: for t<1, E M=p/2 and E M^2=(v+p^2)/2, so Var M=v/2+p^2/4. The no-sampling probability gives p>=exp(-lambda*d*t). This remains a transient obstruction, not a stationary counterexample.

## 3. Choice, recorded before proof work

Prove a quantitative finite-time replacement for the false monotonicity step: for arbitrary exchangeable full-state initial laws, the k-server path law is close to a mixture of k independent nonlinear FIFO queue path laws, conditional on the initial empirical full-state measure. Retain that empirical measure as random. The route is a uniform O(1/N) tagged-rate estimate with no positive class-mass assumption, a full-state graphical coupling, and an elementary empirical-tail estimate for independent, possibly nonidentically distributed reference queues. This directly follows the round 3 recommendation and identifies what randomness survives instead of assuming it disappears.

The proof will separate deterministic initial configurations from their exchangeable randomization. A deterministic empirical initial measure defines the nonlinear reference environment; conditioning on the whole initial configuration gives independent reference queues with possibly different initial states. The average of their laws equals that nonlinear environment. Sampling labels only at the end converts this into the empirical-measure mixture. No stationary limit exchange will be claimed.

## 4. Proof saved

Created PROOF.md. The theorem gives total variation error at most

`k*(4/sqrt(N)+d/(2*N))*(exp(lambda*d*(d-1)*T)-1)+k*(k-1)/(2*N)`

for k full-state paths on [0,T], compared with the product-mixture directed by the nonlinear evolution from the random empirical initial measure. The same bound holds conditionally on that empirical measure. This is finite-time, with an explicit logarithmic-horizon consequence; it does not establish stationary independence.

The route rate is represented without division by a class mass. Independent draws of d-1 competitors differ from the actual competitor sample with probability at most d*(d-1)/(2*N), giving rate error epsilon_N=lambda*d^2*(d-1)/(2*N). The rate functional is C=lambda*d*(d-1) Lipschitz in the supremum queue-tail discrepancy. The empirical-tail bound 4/sqrt(N) is proved for independent nonidentically distributed variables by symmetrization and the maximal inequality for a fair-sign walk. First different candidate acceptances bound disagreement of all full-state coordinates. Gronwall gives epsilon_N/C=d/(2*N).

First audit: independent candidate streams at servers reproduce the true routed transition kernel because a routed arrival changes only one server and its component rate is a_i. This does not assume routed arrival independence. The reference queues become independent only after conditioning on the whole deterministic initial configuration. Their average law is exactly the nonlinear law from its empirical measure. Sampling labels at the end, and only then using exchangeability, is essential. Zero service requirements can cause harmless different acceptances with equal resulting states; counting these as disagreements only enlarges the bound.

## 5. Exact arithmetic audit, first attempt

Created check_bounds.py to audit routing constants by exact fractions and independent subset enumeration, and to check the fair-sign maximal inequality on all walks through length 12. Command: `OMP_NUM_THREADS=1 nice -n 15 python3 check_bounds.py`. This first run stopped before any arithmetic audit: macOS rejected RLIMIT_AS with `ValueError: current limit exceeds maximum limit`. The shell also printed `nice: setpriority: Operation not permitted`. Changed the script to certify inherited priority using os.getpriority before proceeding and to cap RLIMIT_DATA at 128 MiB rather than the unsupported address-space cap; CPU limit is 30 seconds. The computation is streamed and tiny. The failed first run is not evidence for any mathematical bound.

Second attempt, same command: `priority=20; OMP_NUM_THREADS=1`, certifying the inherited priority already exceeds the requested niceness. RLIMIT_DATA was also rejected with the same ValueError before the audit. Removed the unsupported memory-limit setter; the fixed small loops store only one tuple and a few fractions at a time, and RSS is checked/reported directly. The first two failures concern platform resource-limit setters, not the mathematics. No large program or allocation was attempted.

Third attempt, same command, passed. Output:

```text
priority=20; OMP_NUM_THREADS=1
CPU limit = 30 seconds
routing rate bound: 4770 exact count cases passed (2<=N<=16, 2<=d<=7)
independent subset enumeration: 378 cases passed (N<=7)
largest observed error / stated bound = 1/2
sign-walk maximal second-moment bound: 8190 walks passed (1<=N<=12)
prior append-shorter witness: 36 exact cases passed
peak RSS = 14057472 bytes (macOS)
All checks passed. Finite enumeration supplements the symbolic proof.
```

The shell's same nice warning appeared, but os.getpriority independently certifies priority 20. Run completed in less than one second, single thread, approximately 13.4 MiB peak RSS. Enumeration supports the constants and earlier result; the proof, not finite enumeration, establishes all N and d.

## 6. Second derivations and attempted break cases

Added a self-audit section to PROOF.md. Re-derived the competitor error from the exact good-event probability product over j=1,...,d-1 of (1-j/N), instead of the collision union bound. Re-derived C from telescoping the d degree-(d-1) monomials, independently of the integral formula. Re-derived the sign-walk maximum bound by reflection, independently of the stopping-time L2 inequality. Checked the scalar bound by its differential equation and integrating factor. Checked the label collision constant by the exact falling-factorial probability. These checks establish the numerical factors symbolically beyond the finite enumeration.

Boundary audits covered T=0, N=d, all equal queue lengths, singleton classes, G=delta_1, G with an atom at zero, and unbounded support without second moments. Found and corrected one overbroad sentence in the first proof draft: zero-size jobs can depart exactly at a candidate arrival. The final version treats those departures as part of the candidate update and invokes noncoincidence only for previously scheduled positive-residual completions. No theorem or constant changed.

Checked the conditional mixture carefully: conditioning on the whole initial configuration gives independent but nonidentically distributed reference queues; conditioning on its empirical measure gives a uniform initial permutation, which is used only after sampling distinct labels. Reference paths on repeated labels must use fresh independent randomness. The proof includes this, so it never asserts independence of duplicated coordinates.

The stationary covariance error is at most three times the two-path TV bound: one joint-test error plus two marginal errors. The comparison covariance itself equals Var(mu_t^(L_N(0)) f). This is the exact randomness the earlier work warned not to discard.

Restored inline mathematics delimiters and parenthesized equation references with two tiny Python formatting commands, both under OMP_NUM_THREADS=1 nice -n 15. The first reported 143 restored inline delimiters. Read back the entire proof with OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md and added an explicit conditional-law version of the theorem. One attempted combined tool wrapper had a JavaScript parsing error and performed no action; the corrected call then ran.

## 7. Report saved

Created REPORT.md with the required PARTIAL verdict, the explicit finite-time bound, conditional empirical-mixture scope, stationary covariance consequence, commands/output, failed resource-limit setters, zero-service draft correction, and a precise next target. No SOLVED_ELSEWHERE.md was created. The second formatting command reported 40 restored parenthesized equation references and corrected the interval delimiter. All writes remain in this folder; no global state was mutated.

## 8. Final audit

Expanded the nonlinear path-kernel measurability argument and the independent-candidate realization of the true Poisson arrival/routing law. These additions justify existing steps and do not change the theorem or constants. Re-read the round 3 REPORT.md and the original proof's quantitative criterion and transient construction with short read-only commands under OMP_NUM_THREADS=1 nice -n 15.

Final static command used OMP_NUM_THREADS=1 nice -n 15 python3 with a short heredoc reading the four deliverables, parsing check_bounds.py with ast.parse, checking the report verdict, balanced display/inline mathematics delimiters, equation tags 1 through 18, and absence of control characters. Output:

```text
VERDICT: PARTIAL quantitative full-state finite-time product-mixture bound retaining the random initial empirical measure
Proof checks: 29 matched display blocks; 183 matched inline math pairs; equation tags 1 through 18.
Script syntax, verdict, and text control-character checks passed.
LOG.md: 73 lines, 10780 bytes
PROOF.md: 276 lines, 19260 bytes
REPORT.md: 32 lines, 4613 bytes
check_bounds.py: 92 lines, 3960 bytes
```

This final entry increases only LOG.md. Arithmetic checks were not repeated after passing because later edits only expanded explanations and formatting. Final deliverables: REPORT.md, PROOF.md, LOG.md, check_bounds.py. The full stationary product-limit problem is left unresolved, with the nonlinear empirical conditional-mean variance as the next explicit target.
