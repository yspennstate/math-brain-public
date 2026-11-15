# T430 work log

Task: “Open problem T430: Asymptotic independence in the supermarket model with general service times”; received 15 November 2026, approximately 09:22 Asia/Tbilisi (05:22 UTC).

## 1. Orientation and literature check

Read REPORT.md, LOG.md and PROOF.md in the original, round 3 and round 4 folders, and the round 4 script check_bounds.py. The original and round 3 folders contain no computation scripts. Read the startup memory index and compute governor state; the latter reports ok, owner_away_open, 79 percent memory free. Only tiny, single-thread computations are planned. All writes stay in this folder. The task-specific restriction excludes global mesh, checklist and brain writes, including recall commands that log outside this folder. No git or subagents.

Literature search began at 05:22 UTC and ended within five minutes. Web queries covered general-service FIFO supermarket stationary independence in 2025/2026 and global stability of randomized load balancing. Opened the arXiv abstract pages and PDFs of Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, *Convergence properties of many parallel servers under power-of-D load balancing*, https://arxiv.org/abs/1809.05373 and https://arxiv.org/pdf/1809.05373; and Pooja Agarwal and Kavita Ramanan, *Invariant states of hydrodynamic limits of randomized load balancing networks*, https://arxiv.org/abs/2008.08510 and https://arxiv.org/pdf/2008.08510. The former PDF still has internal date November 13, 2021. The latter explicitly leaves stationary-limit identification conjectural, in Section 4.3 of the retrieved PDF (the earlier reports called it Section 4.2). No verified later solution found. This brief search is not an exhaustive certification, and does not justify SOLVED_ELSEWHERE.md.

Commands so far: cat of the files above, rg --files for inventories, and web search/open/find. No numerical program yet.

## 2. Independent audit of the latest main claim

The round 4 bound holds. Independently re-derived its constants by revealing competitor labels sequentially. At draw j, avoiding the tagged label and earlier competitors has probability 1-j/N. Therefore the discrepancy probability is 1-product_{j=1}^{d-1}(1-j/N), at most d(d-1)/(2N). Multiplying by lambda*d gives epsilon_N=lambda*d^2*(d-1)/(2N). The integral representation b(r,nu)=lambda*d*integral_0^1[z*p_r+(1-z)*p_{r+1}]^{d-1} dz gives Lipschitz constant C=lambda*d*(d-1). The independent-reference empirical bound follows by symmetrization and ordering the tail indicators into prefixes, followed by the sign-walk maximal inequality. Thus h'<=C*h+4*C/sqrt(N)+epsilon_N, h(0)=0, integrates to (4/sqrt(N)+d/(2N))*(exp(C*t)-1). The final collision term is at most choose(k,2)/N. This recovers the displayed theorem without using arrival-rate monotonicity or replacing a random initial empirical measure by its mean.

The earlier source-audit identity also holds: conditional on tag inclusion, adding a shorter queue preserves winning only when the d-1 competitors avoid that queue, probability (N+1-d)/N. The empty/busy transient mixture remains a transient obstruction, not a stationary counterexample.

## 3. Chosen extension, recorded before proof work

Prove an O(1/N), fixed-time, conditional full-path product-mixture estimate, improving the round 4 O(1/sqrt(N)) bound. Use an alternative exact proposal representation (independent rate-lambda*d streams at each server, with explicit competitor marks), then explore dependencies backward. Compare with k independent finite branching trees whose leaves have iid initial law equal to the empirical initial measure. On the event that all explored labels are distinct and all initial labels can be coupled without replacement, the complete FIFO paths agree. Derive the collision bound from the first two moments of the branching population. This is a sharper transient estimate within the present sequence; the clan-of-ancestors method already appears in the opened Fittipaldi–Jonckheere–Lopez paper, so no literature novelty claim is made. The stationary directing measure remains random.

## 4. Earlier computation rerun

Command (read-only outside this folder; bytecode disabled):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T430/check_bounds.py
```

Output:

```text
nice: setpriority: Operation not permitted
priority=20; OMP_NUM_THREADS=1
CPU limit = 30 seconds
routing rate bound: 4770 exact count cases passed (2<=N<=16, 2<=d<=7)
independent subset enumeration: 378 cases passed (N<=7)
largest observed error / stated bound = 1/2
sign-walk maximal second-moment bound: 8190 walks passed (1<=N<=12)
prior append-shorter witness: 36 exact cases passed
peak RSS = 13877248 bytes (macOS)
All checks passed. Finite enumeration supplements the symbolic proof.
```

Runtime was below one second. The shell's relative nice increment fails because the inherited priority is already 20; Python independently verifies priority 20, satisfying the requested low priority. This rerun supplements the independent symbolic audit in Section 2.

## 5. Proof saved

Created PROOF.md. The new path error is capped at one and otherwise equals

```text
[k*(k+d-1)*exp(2*C*T)-k*d*exp(C*T)]/(2*N), C=lambda*d*(d-1).
```

The branching forest has jump size a=d-1, rate beta*M with beta=lambda*d, and starts with k histories. Its terminal size is the total number of independently labelled histories. Its factorial second moment is k*(k+a)*exp(2*C*T)-k*(a+1)*exp(C*T). Dividing by 2*N bounds all label collisions, including the k initial labels. On the collision-free event the exact proposal representation and independent nonlinear queue trees reconstruct identical complete paths. The independent second derivation uses the negative-binomial generating function z^k*[p/(1-(1-p)*z^a)]^(k/a), p=exp(-C*T).

Corollaries retain the stationary mixture variance with error delta_2+2*delta_1, and give conditional empirical squared error <=1/N+(N-1)*delta_2/N for any bounded full-state test in [0,1]. This makes approximate invariance of the stationary directing law quantitative, without assuming a topology or concentration. The new bound improves fixed-time order, but does not enlarge the previous logarithmic time window or solve stationary independence.

Self-audit so far: local competitor rejection excludes only the parent and tuple repeats, never previously exposed competitors; meeting a previously exposed label is counted as coupling failure. Otherwise one would change the finite-system marginal. Different forest histories remain independent even if their auxiliary labels repeat; only the finite-system construction identifies a label with a single server. Zero-size departures are part of candidate state updates. All initial-state randomness survives conditioning on its empirical measure.

## 6. Independent finite arithmetic audit

Created check_collision_bound.py and ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_collision_bound.py
```

Output:

```text
nice: setpriority: Operation not permitted
priority=20; OMP_NUM_THREADS=1
CPU limit = 30 seconds
exact proposal representation: 1035 configurations/choice counts, 4797 tagged rates passed
birthday bound: 40 cases, 458959 explicit label tuples passed
branching moments: 480 exact PGF expansions and 96 initial generator derivatives passed
centered-product oscillation: 101 exact cases passed
peak RSS = 13828096 bytes (macOS); elapsed = 0.097 seconds
All checks passed. Enumeration supplements the all-parameter proof.
```

The proposal audit independently enumerates original d-subsets and per-tag competitor subsets for every length vector in {0,1,2}^N, 2<=N<=5, 2<=d<=min(N,4); their rate vectors agree and sum to N when lambda=1. The label audit enumerates all iid tuples for 2<=N<=6, 0<=m<=7, including m>N. The PGF audit expands (15) at z=1 to second order with exact rational arithmetic, for a=1,...,8, k=1,...,12 and five rational values of p; it agrees with the separately integrated moment ODE. Initial derivatives also agree with one-jump generator calculations. No simulation or fitted constants.

Second symbolic checks: at T=0 the bound is choose(k,2)/N; its time derivative is C*k*(2*k+d-2)/2 before division by N, agreeing with the proposal-rate times the increment of choose(M,2). Forests larger than N are necessarily bad, not omitted. The conditional centered-product test has oscillation max(m,1-m)<=1, checked algebraically and at 101 exact rational values, so total variation introduces no missing factor two. Mean-one, finite second moment, and service-density assumptions do not enter the collision proof. Sampling without replacement is the theorem's stated convention, inherited from round 4.

What was not obtained: no attraction, strict dissipation, stationary empirical concentration, or unique stationary marginal limit. The new O(1/N) bound has e^(2*C*T) growth, so the allowable coefficient of log N stays below 1/(2*C). No extension of that time window is claimed. The literature citation's Section 4.2/4.3 discrepancy is a numbering correction, not a failure of the earlier mathematical result.

## 7. Final artifact audit

Created REPORT.md with the required PARTIAL first line, exact new bound, commands, limits, and continuation target. Ran a short inline Python read-only audit under `OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 -`, with priority >=15 independently asserted. It checked the report verdict, equation tags 1–15 in order, matched display/inline math delimiters, absence of text control characters, and the computation script's syntax via ast.parse. Output:

```text
nice: setpriority: Operation not permitted
PROOF.md: 225 lines, 20820 bytes
REPORT.md: 33 lines, 4896 bytes
LOG.md: 88 lines, 9309 bytes
check_collision_bound.py: 106 lines, 4837 bytes
Verdict, equation tags 1–15, math delimiters, control characters, and script syntax passed.
The mathematical boundary cases and independent constant derivations are in PROOF.md Section 6.
```

After this check, removed comparisons with earlier sessions from the proof's prose; all equations, mathematical arguments and code stayed unchanged. REPORT.md retains the required comparison. This final entry increases LOG.md. No further arithmetic run is needed because no mathematical constant or code changed. Deliverables: REPORT.md, PROOF.md, LOG.md, check_collision_bound.py. The full stationary independence problem remains unresolved.
