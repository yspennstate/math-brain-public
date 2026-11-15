# T070 working log

Task received: 14 November 2026, about 20:50 Asia/Tbilisi (16:50 UTC): “push this problem forward by one checkable piece.”

## 1. Orientation and literature search started (16:50 UTC)

Read the workspace listing, startup memory index, brain navigation index, and compute governor state. The folder initially contained PROMPT.md, codex.log, and run.pid. Governor status was `ok`, mode `owner_away_open`. No other workers were launched. The task-specific restriction to writes inside this folder supersedes the usual shared mesh/checklist/memory writes; those commands were not run.

Commands: read-only Python through `OMP_NUM_THREADS=1 nice -n 15 python3`, and web search queries “activated random walk density conjecture 2026 higher dimensions self organized criticality”, “2605.00207 activated random walk”, and “activated random walk stationary critical aggregate density equality 2025 2026”.

The nice wrapper printed `setpriority: Operation not permitted` but the read-only Python completed. Check the inherited process priority before any computation. Initial search returns the known one-dimensional theorem, the earlier density-conjecture paper arXiv:2406.01731, a complete-graph result arXiv:2604.04747, and a September 2026 stationary one-dimensional result. These are search leads, not yet verified citations. Literature check deadline: 17:00 UTC.

## 2. Literature check completed; choice (16:52 UTC)

Opened the arXiv abstract pages and HTML for:

- Christopher Hoffman, Tobias Johnson, Matthew Junge, *The density conjecture for activated random walk*, arXiv:2406.01731v2 (2024).
- Christopher Hoffman, Tobias Johnson, Matthew Junge, Josh Meisel, *Activated random walk exhibits self-organized criticality*, arXiv:2605.00207 (2026), abstract page opened.
- Nicolas Forien, *A new proof of superadditivity and of the density conjecture for Activated Random Walks on the line*, arXiv:2502.02579v2 (2025).
- Matthew Junge, Harley Kaufman, Josh Meisel, *Scaling limit and density conjecture for activated random walk on the complete graph*, arXiv:2604.04747v2 (2026).
- Tobias Johnson, Matthew Junge, Josh Meisel, *Stationary activated random walk: regularity, heavy tails, and remixing*, arXiv:2609.31843 (2026).

Links: https://arxiv.org/abs/2406.01731 ; https://arxiv.org/abs/2605.00207 ; https://arxiv.org/abs/2502.02579 ; https://arxiv.org/abs/2604.04747 ; https://arxiv.org/abs/2609.31843 . No solution or new higher-dimensional density identification was found. The September paper strengthens local regularity in one dimension; the complete-graph paper treats a different graph sequence. Neither resolves the remaining lattice case. All precede the supplied November 2026 status check.

Density-list clarification: the original density conjecture identifies stationary mean density in growing boxes with the infinite-volume fixed-energy threshold. The one-dimensional 2024 theorem also treats the point-source visited aggregate and a cycle stabilization-time threshold. Forien separately formulates the hockey-stick law and the ratio of source mass to visited aggregate size.

Choice, before calculation: test the proposed edge-diversion monotonicity from Forien, Section 2.5, exactly on the 2-by-2 square in Z^2 at sleep rate lambda=1. Each of its eight directed internal edges may independently be redirected to the sink. Exhaust all 256 resulting kernels, checking stochastic order of the final total sleeping population for every further single-edge diversion (1024 comparisons). This directly addresses a suggested route to higher-dimensional superadditivity. Exact rational absorption laws will settle this finite family, or provide a counterexample. An independent dynamics schedule and direct stationary-chain calculation will audit the result on the original square and selected cuts.

Priority audit command: `OMP_NUM_THREADS=1 nice -n 15 python3` with `os.getpriority(os.PRIO_PROCESS,0)` printed `20`. The process already runs at an even lower priority than requested. All calculation scripts will check inherited nice >=15, use one thread, impose memory/time limits, and stay inside this folder. The wrapper warning comes from adding relative nice to the inherited nice-20 priority.

## 3. Exact solver written; first launch guard failed

Wrote `exact_square.py`. Primary method: finite absorbing-chain Dirichlet equations with integer coefficients and exact fraction-free elimination in SymPy. Independent audit: the continuous-time generator with particle-dependent jump rates, Python `Fraction` Gaussian elimination, and invariance under addition at each vertex.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 exact_square.py --limit 1 --audit --output square_preview.json`.
Output: `ValueError: current limit exceeds maximum limit` while installing RLIMIT_AS, before any calculation. The inherited hard resource limit needs to be respected rather than raised. No mathematical output was produced by this failed run.

## 4. Baseline and independent audit passed (16:55 UTC)

Read inherited limits: AS, DATA and RSS all reported 9223372036854775807, yet macOS rejected lowering their soft limits with `ValueError: current limit exceeds maximum limit`. CPU soft limit installation works. Adjusted the script to tolerate unavailable AS enforcement, bound reachable state count (<500), measure peak RSS at each primary solve, and impose 1100 CPU seconds plus a 1150-second wall alarm. These tiny matrices require far below 1 GB.

Repeated exact command: `OMP_NUM_THREADS=1 nice -n 15 python3 exact_square.py --limit 1 --audit --output square_preview.json`.

Output:
```
masks=1 elapsed=0.035s states=128
independent audit mask=0 passed
comparisons 0 failures 0 zero tail gaps 0 min gap None
base law ['4101320/96025977', '61478038/288077931', '109407745/288077931', '190576/665307', '140/1803']
base mean 205775624/96025977
elapsed=2.473s peak_rss_bytes=65093632
```

The independent audit also checked that the full stable-configuration law is unchanged by adding and stabilizing at each of the four individual vertices. This verifies that the absorption law from one active particle per site is stationary, without relying on an unverified identification of two densities.

## 5. Exhaustive primary calculation passed (16:56 UTC)

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 exact_square.py --audit --output square_data.json`.

Output:
```
masks=1 elapsed=0.035s states=128
masks=32 elapsed=0.313s states=39
masks=64 elapsed=0.465s states=31
masks=96 elapsed=0.592s states=27
masks=128 elapsed=0.687s states=23
masks=160 elapsed=0.915s states=31
masks=192 elapsed=1.027s states=23
masks=224 elapsed=1.082s states=19
masks=256 elapsed=1.132s states=15
independent audit mask=0 passed
independent audit mask=1 passed
independent audit mask=3 passed
independent audit mask=15 passed
independent audit mask=63 passed
independent audit mask=85 passed
independent audit mask=127 passed
independent audit mask=255 passed
comparisons 1024 failures 0 zero tail gaps 1792 min gap 0
base law ['4101320/96025977', '61478038/288077931', '109407745/288077931', '190576/665307', '140/1803']
base mean 205775624/96025977
elapsed=6.912s peak_rss_bytes=70549504
```

All 4096 exact tail inequalities are nonnegative. Some are equalities, so strict domination would be a false conclusion. The fully cut case is exactly Binomial(4,1/2), checked against its elementary law. To rederive every comparison independently, expanded the audit from eight representative kernels to all 256 kernels; the next command uses actual continuous-time clocks and Python rational Gaussian elimination for every law, with four addition-stationarity checks per kernel.

## 6. Every law independently rederived; data-only audit passed (17:00 UTC)

Commands:
```
OMP_NUM_THREADS=1 nice -n 15 python3 exact_square.py --audit-all --output square_data.json > square_run.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 verify_square_data.py > square_verify.txt 2>&1
```

The complete first output is saved in `square_run.txt`. Its final lines are:
```
independent audits=256 last_mask=255 passed
comparisons 1024 failures 0 zero tail gaps 1792 min gap 0
base law ['4101320/96025977', '61478038/288077931', '109407745/288077931', '190576/665307', '140/1803']
base mean 205775624/96025977
elapsed=119.715s peak_rss_bytes=71401472
```

The data-only verifier's complete mathematical output is:
```
256 laws agree with independent clock/Fraction calculations
1024 comparisons; 4096 tail inequalities; 1792 zero gaps; 2304 positive gaps
minimum positive gap and (uncut mask, cut mask, threshold): (Fraction(15, 65296), 102, 103, 4)
dihedral symmetry checks: 2048
two-site law: ['99/427', '216/427', '16/61']
two independent rows (mask 90): ['9801/182329', '42768/182329', '68832/182329', '6912/26047', '256/3721']
square versus two rows tail gaps: ['193361026297/17508320360433', '1691370841397/52524961081299', '518688964/17329251429', '59372/6708963']
baseline stationary density: 51443906/96025977
PASS
```

Both output files also contain the already diagnosed `nice: setpriority: Operation not permitted` warning: the inherited priority is 20 and no priority increase was attempted. Measured RAM was 71,401,472 bytes, comfortably below 1 GB; the longest run was 119.715 seconds, one interpreter and no worker threads.

Wrote `PROOF.md` with the finite model, absorption and uniqueness arguments, exact equation construction, two independent solvers, stationarity verification, and a hand derivation of the two-site law (99,216,112)/427. The row-splitting case is a finite superadditivity comparison without a separator: the original square dominates the independent sum of its two isolated rows. The verifier explicitly checks strict positivity of these four particular tail gaps.

What was tried to break the result: asymmetric one-way cuts and every subsequent cut were included, not just undirected deletions; both endpoints (no deletions and all deletions) were included; all four tail thresholds were tested; all vertex-addition stationary identities were tested; geometric relabelings were checked; the all-sink law and two-independent-row law were derived separately. General strictness fails because 1792 tail differences vanish. No counterexample to non-strict edge-diversion monotonicity was found in this finite family.

## 7. Deliverables and final audit

Finished `REPORT.md` with verdict COMPUTED, exact scope, reproduction commands, limitations, literature clarification, and the proposed symbolic-lambda next step. Reran `OMP_NUM_THREADS=1 nice -n 15 python3 verify_square_data.py > square_verify.txt 2>&1` after adding an explicit assertion for strictness of the row-splitting case; it passed.

Final read-only Python audit parsed both scripts with `ast.parse`, checked the report verdict, checked all 256 independent audit entries and absence of failures, and verified that saved verifier output ends in PASS. Output:
```
Python 3.13.2 SymPy 1.13.1
nice 20
two script syntax checks, 256 independent laws, report, and saved PASS checked
data bytes 332679
```

All created artifacts are in this folder. No git commands, external posts, messages, accounts, subagents, or shared-state writes were used. The higher-dimensional density conjecture remains unresolved by this work.

Task completed: “push this problem forward by one checkable piece” — received 14 November 2026, about 20:50 Asia/Tbilisi.
