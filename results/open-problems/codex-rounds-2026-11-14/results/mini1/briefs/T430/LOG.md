# T430 work log

Task received: 2026-11-14, approximately 22:16 machine local time (18:16 UTC; 22:16 Asia/Tbilisi).

## 1. Orientation and literature search started, 18:16 UTC

Read the supplied problem and local directory. No pre-existing mathematical work was present (PROMPT.md and runner files only). Read the brain memory index and compute governor state. Governor reported `warn`, `owner_away_open`, memory free 60 percent. No numerical simulation is planned.

The instruction specific to this task forbids writes outside this folder. Accordingly, no mesh registration, global checklist update, brain recall with logging, or memory write was run. No git or subagents are used.

Shell reads were invoked with `OMP_NUM_THREADS=1 nice -n 15`; macOS printed `nice: setpriority: Operation not permitted` but executed the reads. This is a resource-control limitation, not a mathematical result. Avoid heavy computation entirely.

Web search queries so far:

- `supermarket model general service times stationary propagation chaos asymptotic independence ansatz solved`
- `Bramson Lu Prabhakar ansatz general service FIFO stationary 2024 2025 2026`
- `"general service" "ansatz" "stationary" supermarket 2024 2025`
- `"FIFO" "asymptotic independence" service times`
- `"supermarket" "invariant" "Aghajani" "Ramanan"`

Search results identify the 2012 Bramson–Lu–Prabhakar paper and its already-known small-arrival-rate/finite-second-moment result, in addition to decreasing hazard rates. This does not settle the stated general case. The literature search is continuing within the ten-minute limit.

## Candidate concrete piece

The initial candidate was a stationary service-age occupation identity and a tightness reduction. It has not been attempted. A more directly relevant issue emerged in the literature search; the final choice below replaces this candidate.

## 2. Literature check and final choice, approximately 18:20 UTC

Search used approximately four minutes, below the ten-minute cap. Additional searches covered invariant states, global stability, FIFO, Coxian distributions, and arXiv:1809.05373. Opened and read the arXiv pages and PDFs of:

- Maury Bramson, Yi Lu, Balaji Prabhakar, *Decay of tails at equilibrium for FIFO join the shortest queue networks*, arXiv:1106.4582v2.
- Reza Aghajani, Kavita Ramanan, *The hydrodynamic limit of a randomized load balancing network*, arXiv:1707.02005v2; its introduction explicitly leaves stationary convergence for future work.
- Pooja Agarwal, Kavita Ramanan, *Invariant states of hydrodynamic limits of randomized load balancing networks*, arXiv:2008.08510v1; Section 4.2 leaves equality with the stationary limit as a conjecture. The publisher page identifies a 2025 publication, DOI 10.1287/moor.2020.0282.
- Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez (arXiv author spelling), *Convergence properties of many parallel servers under power-of-D load balancing*, arXiv:1809.05373. The PDF author line uses initials and López. Proposition 2.1, PDF page 4, explicitly assumes deterministic initial configuration; Proposition 4.1, PDF page 14, claims stationary convergence and invokes uniformity in the initial distribution.

The Stanford PDF of the 2012 Bramson–Lu–Prabhakar paper failed to open after repeated timeouts; it is not used as an opened-paper reference here. Search snippets alone were not treated as proof.

No verified solution of the full stated problem was found. The last paper contains a purported stationary result, but the deterministic-to-random initial-state passage requires a term not supplied by a deterministic-start covariance estimate. This is a mathematical concern to check, not a claim that the paper's conclusion is false. No SOLVED_ELSEWHERE.md is warranted on this evidence.

**Chosen piece, before proof work:** derive an exact stationary variance reduction that retains initial-state randomness, and prove an explicit positive-time counterexample to dropping that randomness within the FIFO supermarket model with deterministic mean-one service times. This addresses the stationary-limit caveat directly and is preferable to reproducing a standard tightness lemma. The example is transient and will not be presented as a counterexample to stationary chaos.

Commands/tools: `web.run` search/open/find calls, as listed in the session transcript; local text reads only. All mathematical output will be in PROOF.md. No numerical program is needed.

## 3. Proof written

Created PROOF.md using `apply_patch`. Its contents are one connected reduction, with an example that tests its essential term:

1. Exact conditional-variance decomposition (1), with the stationary specialization (3).
2. Equivalence of full-state chaos and empirical concentration, assuming convergence of the first marginal; proof includes the sampling-collision error k(k-1)/(2N).
3. An admissible exchangeable mixture for deterministic FIFO services that has Var(M(t)) ≥ exp(-2λdt)/4 for every t<1, and nonvanishing tagged emptiness covariance.
4. A separate direct two-server derivation giving covariance at least 1/8 at t*=min(1/2,1/(8λd)), for every N≥max(d,2).

No service-age occupation identity or tightness theorem is claimed. No simulation or numerical evidence is used. The formulae are exact inequalities with symbolic parameters.

## 4. First self-audit

- Re-derived the nonzero covariance directly from joint empty events, independently of the conditional-variance/sum-of-covariances argument.
- Re-derived the union-sampling rate bound by both inclusion-exclusion and a union bound. Checked N=d and sampling with replacement.
- Checked t=0 exactly: both the variance and covariance are 1/4, matching the principal bounds.
- Checked the restriction t<1: initial jobs in the occupied branch cannot depart before then. No claim is made beyond that time.
- Re-derived the collision constant by counting unordered pairs among k sampled positions. Products take values in [0,1], so the error is the collision probability, without an extra factor two.
- Checked full-state scope: the reduction uses a full Markov descriptor throughout; the example uses a measurable, continuous projection to emptiness. Queue lengths alone are never used as a general-service Markov state.
- Checked the crucial limitation: the example is not stationary and does not disprove the target ansatz. A deterministic-start bound remains valid in the presence of this example; the invalid extension is to arbitrary dependent random initial laws.

## 5. Quantitative continuation criterion and report

Added (14)–(15) to PROOF.md: conditional-mean forgetting on a set of stationary probability at least 1-η_N bounds empirical variance by ε_N+δ_N²+η_N. This is a sufficient condition, explicitly left unproved for the supermarket system. The times t_N may depend on N; there is no unjustified interchange of limits.

Created REPORT.md with a PARTIAL verdict. The report distinguishes an unverified published claim from a proved solution and describes exactly what remains to be checked. No claim of a new solution or of a stationary counterexample is made.

A local audit command was:

```sh
OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'ps -o pid=,ni=,comm= -p $$; wc -l PROOF.md LOG.md; cat ~/.claude/projects/-Users-user/memory/macos_os_nice_raises_at_nice_20_stacked_relative_nice_2026_11_10.md'
```

Relevant output at that point:

```text
nice: setpriority: Operation not permitted
/bin/sh: /bin/ps: Operation not permitted
     242 PROOF.md
      63 LOG.md
     305 total
```

The memory read explains that relative nice increments can fail when inherited priority is already at the macOS limit. The sandbox prevented an independent priority read with ps, so priority was not certified. These were short read-only commands, not numerical runs. The mathematical argument needs no program, no data file, and no estimated constants.

Second audit of (15): Var(H)≤E(H-c_N)²; the good set contributes at most δ_N² and its complement at most η_N since H,c_N∈[0,1]. Add the nonnegative conditional variance from (3). Checked that no uniform integrability, service second moment, invariant-state uniqueness, or stationarity of the counterexample has been introduced silently.

## 6. Final file check, 18:24 UTC

Executed:

```sh
OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'head -1 REPORT.md; wc -l PROOF.md LOG.md REPORT.md; rg -n "Proposition|tag\{|not stationary|not.*proved|No such" PROOF.md'
```

Output confirmed the required first-line verdict, three propositions, all displayed equation tags, the explicit transient limitation, and the unproved status of the sufficient forgetting estimate. At the time of the check the files had 268, 89, and 26 lines respectively; this final log entry increases only LOG.md. The same priority warning appeared. No numerical program was run. Final deliverables: PROOF.md, REPORT.md, LOG.md.
