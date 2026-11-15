# T160 work log

Task: “push this problem forward by one checkable piece.” Session began 2026-11-14 at approximately 22:02 Asia/Tbilisi (18:02 UTC).

## Scope and startup
Read the startup memory index, the priority-related memory card, compute state, and mesh protocol. The task-specific order forbids all writes outside this folder, so shared brain/checklist/mesh commands that write external state were not run. No git and no subagents. Local files are the task record.

Commands so far: read-only `pwd`, `rg --files`, `ls`; subsequently all Python commands launched as `nice -n 15 env OMP_NUM_THREADS=1 python3 ...`. The inherited process priority is already 20: `os.getpriority(os.PRIO_PROCESS,0)` returned `20`. The extra relative nice request prints `nice: setpriority: Operation not permitted`; the child retains priority 20, lower scheduling priority than requested. All work is tiny, single-threaded, and below 1 GB. Compute state: warn/cpu_saturated, owner_away_open, 43% memory free. No heavy computation planned.

## Literature check (first ten minutes only)
Used the web search tool for recent three-dimensional Bernoulli IIC existence, 2026 quasi-multiplicativity, and the supplied arXiv identifiers. Opened Basu–Sapozhnikov arXiv:1603.06884 (abstract and PDF), Chatterjee–Chinmay–Hanson–Sosoe arXiv:2502.10882, Hillairet arXiv:2509.18852, and the metric-graph GFF article https://doi.org/10.1007/s00220-026-05772-5. These distinguish conditional Bernoulli results from proven results in other models. An attempted HTML URL for 2502.10882v2 returned 404; the abstract page opened successfully.

Search also surfaced claims about absence of critical percolation on Z^3; these concern T001 and do not by themselves prove T160. Opened Raphaël Cerf arXiv:2608.23661, which gives a conditional alternative concerning the finite-cluster tail, not existence of an IIC. No verified new solution of T160 found so far. Further final search results to be recorded next.

## Chosen piece (recorded before proof work)
Construct and prove an explicit maximum-degree-three tree with p_c=1/2 and theta(p_c)=0 for which conditioning on connection to the graph-distance sphere does not converge on a fixed edge event. Use two spherically symmetric branches whose sparse nonbranching levels alternate dominance. Derive survival bounds directly by a second moment and a recursion, then check the bounds independently and compute a small exact table of the schedule.

Why: this isolates a genuine obstruction to deriving the IIC merely from bounded degree, compactness, and critical extinction. It does not satisfy lattice transitivity or all the Basu–Sapozhnikov hypotheses, and it does not settle T160. No novelty claim is intended.

### Literature cutoff
Closed the literature check at approximately 22:06 local time, within four minutes of startup. Final searches also covered IIC nonexistence on spherically symmetric trees and possible 2026 IIC announcements. No new three-dimensional Bernoulli IIC theorem was verified. The 2026 GFF publication explicitly still invokes quasi-multiplicativity as an assumption for Bernoulli percolation. Secondary claims about T001 were not validated or used. No SOLVED_ELSEWHERE.md is warranted.

### Construction derived
Use stage endpoints N_0=0, N_k=2^(k^2+10). At the first 2k−1 levels after N_(k−1), suppress branching in A for odd k, B for even k; otherwise both branches are binary. At N_k the cumulative suppressed-level difference is D_A−D_B=(−1)^(k+1)k. Each branch has o(n) suppressed levels, so its critical parameter remains 1/2, while both critical expected generation sizes tend to zero.

Derived two survival estimates, to be written and independently checked: q(n) >= M_n/(n+1) by a second moment; q(N_k) <= 8 M_(N_k)/N_k from the reciprocal survival recursion on the final binary plateau. Thus the weaker/stronger branch survival ratio is at most 16*2^(−k). The fixed root edge opening probability has proposed subsequential limits 1/2 (odd stages) and 1 (even stages). The root attachment shifts the conditioning radius from N_k to N_k+1.

### Proof saved
Wrote PROOF.md: explicit tree, all survival estimates, critical parameter, extinction at every vertex, and the fixed-edge subsequential limits. Added an independent reciprocal-recursion derivation of both bounds. Next: exact finite checks and stage certificates. No external writes.

### Verification script saved
Created audit.py. It compares exact forward generation distributions to backward survival recursions for every one/two-child pattern through six levels at p=1/3,1/2,2/3; checks the second-moment and reciprocal identities; exhaustively enumerates two-branch depth-three trees; and writes exact rational stage certificates for k<=32. It has a 120-second alarm and uses only the Python standard library. Run command next: `nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py`.

### Exact verification run
Command: `nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1`
Exit status: 0. Output:

```text
nice: setpriority: Operation not permitted
PASS: 378 exact forward-distribution/backward-recursion comparisons
PASS: 378 exact second-moment identities and survival lower bounds
PASS: 126 reciprocal identities, critical bounds, and available plateau bounds
PASS: 16 fixed-edge formulas by exhaustive enumeration of 33856 configurations
PASS: 32 stage counts, final-plateau inequalities, and exact ratio certificates
Certificates are bounds from the proof, not simulated survival probabilities.
k  D_A  D_B  weaker  certified interval for P(e_A open | reach N_k+1)
 1    1    0      A  [0.500000000000, 0.999756216480]
 2    1    3      B  [0.714288205343, 1.000000000000]
 8   28   36      B  [0.996093630802, 1.000000000000]
 9   45   36      A  [0.500000000000, 0.501953139901]
16  120  136      B  [0.999984741211, 1.000000000000]
17  153  136      A  [0.500000000000, 0.500007629395]
32  496  528      B  [0.999999999767, 1.000000000000]
Priority: 20; OMP_NUM_THREADS=1
Elapsed seconds: 0.270
Peak RSS bytes (macOS): 15663104
PASS: all exact checks
```

Data saved as stage_certificates.csv. Values in this CSV are certified bounds from the analytic lemmas, not numerical estimates of the infinite-tree survival probability.

### Adversarial audit
- Re-derived the lower bound from the reciprocal survival recursion independently of the forward second moment. Re-derived the upper bound by the same reciprocal recursion independently of the binary-plateau union bound. Exact finite checks agree with both.
- Recomputed stage counts two ways: adding every suppressed level and evaluating the alternating-sum closed formula. All 32 stages agree. The sum of suppressed levels is k^2 and the signed difference has magnitude k, not k^2; this distinction controls the survival ratio.
- Checked the attachment offset: branch level n corresponds to radius n+1 from o. Every claimed subsequence uses N_k+1.
- Checked the cylinder event carefully. An edge in the unsuccessful branch can still be open. The limiting edge probabilities are 1/2 and 1, rather than 0 and 1. Exhaustive full edge-configuration enumeration verifies equation (11).
- Checked the percolation parameter rather than merely calling 1/2 critical. Below and at 1/2 all descendant means vanish; above 1/2 the second-moment series is finite, giving positive survival. Critical extinction holds at every vertex, not just o.
- Checked that sparse suppression does not disappear: D_s(n)/n tends to zero but D_s(n) tends to infinity. These serve different parts of the proof.
- Checked the final binary plateau and the k=1 endpoint separately. The plateau covers at least half the depth at every selected stage.
- Tested the missing hypotheses. For each p in (1/2,1), close the parent edges of two surviving descendant subtrees: this has positive probability and gives distinct infinite clusters. Thus the tree does not satisfy the supercritical uniqueness assumption in the Basu–Sapozhnikov theorem. Its exponential growth also precludes a nearest-neighbor embedding into Z^3. Neither the theorem nor T160 is contradicted.
- No load-bearing quantity is estimated by floating point. The displayed decimal table is only a rendering of exact rational certificates in stage_certificates.csv. No critical exponent is inferred.
- No proof that the analogous survival-ratio oscillation can occur on a transitive lattice was obtained. No claim that the obstruction is new in the literature is made.

### Final files
PROOF.md contains the proposition and its proof. audit.py reproduces all finite checks and stage_certificates.csv; audit_output.txt is the exact output. REPORT.md records the limited verdict and next step. All mutations stayed inside the task directory; no git, accounts, messages, or external publication.

### Completion check
Verified the required REPORT.md verdict line, all six nonempty deliverable files, the saved all-checks-passed output, 32 CSV rows, and the final counts D_A=496, D_B=528. No substantive changes to the verified computation after its successful run. T160 itself remains unresolved.
