# T059 work log

Task received 14 November 2026, approximately 20:48 Asia/Tbilisi: “push this problem forward by one checkable piece.”

Scope: all writes stay in this folder; no git, external messages, or subagents. The task-specific folder-only rule supersedes global instructions to mutate the brain/checklist/mesh. A startup brain recall was attempted, but no further global-state commands will be run. Compute state was `ok`, `owner_away_open`.

## Step 1: literature check (started 20:49)

Searching the web for a solution or substantial advance beyond the supplied status, and opening primary sources. No mathematical claim is adopted from search snippets alone.

Execution caveat: `OMP_NUM_THREADS=1 nice -n 15 python3 ...` emitted `nice: setpriority: Operation not permitted`; checking inherited scheduling priority before any computation. Research runs will be small, single-threaded, and memory-bounded.

Scheduling check: `OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os; print("priority", os.getpriority(os.PRIO_PROCESS,0))'` printed `priority 20`. The inherited priority is already lower than the requested 15; the sandbox refuses changing it. Keep that inherited priority. No heavy compute is needed.

Opened primary arXiv pages: Alexander Goldenshluger and Yaakov Malinovsky, arXiv:2610.33701; Léonard Brice, F. Thomas Bruss, Anirban Majumdar, Jean-François Raskin, arXiv:2608.27419; Martin Meier and Leopold Sögner, arXiv:1606.03348. Also opened the 19-page Goldenshluger–Malinovsky paper PDF via its indexed mirror. Searches for later solutions and November 2026 developments found no later primary result. The finite-n characterization in the October paper is already part of the supplied status, not a reason to declare solved elsewhere.

## Step 2: chosen piece (20:57)

Choice: prove an explicit quadratic certificate converting uniform errors in continuation values into expected-rank regret of the induced policy. The current relative-rank term must be evaluated exactly. The key is that the stop-minus-continue advantage grows at least linearly with the current observation, even though it has jumps at historical values. A one-sided continuation error should halve the certificate. Derive a concrete corollary for rounding histories upward, and check the discontinuity and terminal cases with exact rational examples.

Why: this gives a checkable reduction from numerical continuation approximations to a policy guarantee, rather than another unvalidated decimal approximation to V. It does not determine the asymptotic constant, and priority is not claimed. The opened 2026 papers establish Bellman recursions and discuss numerical errors; the proposed certificate concerns the induced policy's regret.

Literature search ended within ten minutes. No SOLVED_ELSEWHERE.md is warranted.

## Step 3: proof drafted

Wrote PROOF.md: history monotonicity by coupling a fixed future stopping functional; a slope bound for the stop-minus-continue advantage; a measure argument that allows jumps; an exact recursive decomposition of policy regret; and the rounding corollary. The special last-two slope is 2, rather than the generic r-1=1, and is retained in all constants. No new value for V_n or V is claimed.

The literature comparison is limited: the opened papers provide the finite-horizon Bellman framework, while the certificate here is proved independently. It may be a standard consequence of margin bounds in optimal stopping; novelty has not been established.

## Step 4: independent exact checks, first run

Created verify_certificate.py, using only Python's standard library and exact fractions. The script integrates actual policy costs and separately integrates local residuals on exact affine cells; checks third-to-last advantages from independently evaluated W_2; and compares the rounding coefficient's stage sum with its closed form.

Command:
```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_certificate.py > audit_stdout.txt 2> audit_stderr.txt
```
First run exited before doing mathematics: `resource.setrlimit(RLIMIT_DATA, (512 MiB,512 MiB))` raised `ValueError: current limit exceeds maximum limit`. Inspecting inherited limits and adapting the cap to them. This is an execution-limit issue, not evidence about the theorem.

Second run: removed the unsupported RLIMIT_DATA call; the script still sets a 90-second CPU limit, and records/checks peak resident memory. Reran exactly the command above. Exit status 0; runtime about 0.25 seconds. Standard output:
```
arithmetic: fractions.Fraction throughout; no floating-point tests
penultimate_histories: 126
penultimate_policy_checks: 2016
third_to_last_slope_checks: 2016
stage_sum_vs_closed_form_checks: 29
sharp_two_sided_epsilon_1_over_4: 1/32
sharp_one_sided_epsilon_1_over_4: 1/64
pinned_threshold_regret_delta_1_over_100: 51/10000
n5_rounding_coefficient: 31/4
n5_M100_regret_certificate: 31/40000
priority: 20
peak_rss_bytes_macos: 16171008
all_checks_passed: True
```
Standard error contains only the previously explained `nice: setpriority: Operation not permitted`. The process inherits priority 20. Peak memory was about 16.2 MB, well below 1 GB.

Data saved: penultimate_audit.csv (2016 exact-rational test records); audit_results.json (summary and all 29 coefficients); audit_stdout.txt and audit_stderr.txt.

## Adversarial audit

- Re-derived the sharp two-choice constants from separate antiderivatives of S=1+x and C=2-x, rather than from the advantage integral. Results: 1/32 and 1/64 at epsilon=1/4.
- For 126 histories, including duplicates, endpoints, and jumps, checked all 4 epsilon choices and 4 error patterns. Actual chosen-cost minus optimal-cost integration equals independent residual integration exactly; all 2016 certificates pass.
- Checked 2016 adjacent rational comparisons for third-to-last advantages, evaluating W_2 by exact integration and verifying its asserted lower slope.
- Re-derived A_n by summing stages and by its polynomial closed form, agreeing for n=2,...,30. In particular A_5=31/4 and the M=100 oracle rounding certificate is 31/40000.
- Deliberately tried a shortcut that bounds loss only by threshold displacement. It FAILS at h=(1/2), r=2: a displacement delta=1/100 costs 51/10000, i.e. delta/2+delta^2. This failure is recorded in PROOF.md and is why the exact relative-rank condition is explicit.
- Checked the telescoping argument a second way: at each reached decision, the selected action's optimal-continuation cost minus the local Bellman value is a nonnegative residual. Summing expectations telescopes the successive Bellman values; the final compulsory decision has zero residual. This recovers equation (12)'s bound and confirms that there is no extra penalty per continued step.
- Terminal case n=1 is excluded from harmonic-number notation and has zero regret. n=2's improved slope is applied only where it is exactly available. Approximation monotonicity is optional in the main theorem; it is used only for the halved constant with two-sided error.

No attempt was made to infer a certified numerical V_5 from the October paper's decimal table. Its approximation errors have not been bounded here. The rounding corollary is an oracle reduction, not a completed finite-state solver, and it uses exact past comparisons.

## Completion audit

REPORT.md starts with the required `VERDICT: PROVED` line and includes the mathematical result, exact command, checks, failed approach, uncertainty about novelty, and next step. A final read-only artifact check confirmed that all deliverables exist and that the CSV row count agrees with the JSON summary (2016). The general proof, finite checks, and the oracle limitation are stated separately. No git or external write was performed.
