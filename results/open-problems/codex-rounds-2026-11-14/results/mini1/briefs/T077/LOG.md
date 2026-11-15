# T077 work log

Task: “Coexistence in the two-type Richardson model only at equal rates.”
Session began 2026-11-14 21:56 Asia/Tbilisi (17:56 UTC); this is the observed session start, not an independently recorded prompt timestamp.

## 1. Orientation and literature search

Read PROMPT.md, the startup memory index, the brain navigation index, the mesh protocol, and the compute governor state. The governor reported `warn`, `owner_away_open`, about 36% free memory. No substantial computation has run. The task-specific order to write only in this folder overrides the global requests to mutate the mesh, checklist, and brain stores. Those stores will not be changed; no subagents or git commands will be used.

Read-only shell commands: `pwd`, `rg --files`, `cat` of the memory and compute state, `ls -la`, `sed` of PROMPT.md and the mesh protocol. All writes so far are confined to this file.

Literature search began at 17:56 UTC, with a ten-minute maximum. Web queries included `two type Richardson unequal rates coexistence conjecture 2024 2025 2026`, `Richardson model coexistence unequal intensities countably many open problem`, and dated variants. Initial results include the original papers, the equal-rate work, and a general-graph nonmonotonicity paper, but no verified resolution. Dated queries also returned irrelevant biological and algebraic uses of “Richardson”; these are not evidence about T077. Sources will be opened and checked before citation.

Opened sources:

- Thomas Finn and Alexandre Stauffer, *Non-equilibrium multi-scale analysis and coexistence in competing first passage percolation*, J. Eur. Math. Soc. 26 (2024), 1313–1363, DOI 10.4171/JEMS/1309: https://ems.press/content/serial-article-files/47258?nt=1 . Section 1.5 explicitly describes the full-lattice unequal-rate conjecture as open. Its main model is FPP in a hostile environment, not T077.
- Daniel Ahlberg, Maria Deijfen, Christopher Hoffman, *The two-type Richardson model in the half-plane*, arXiv:1808.10796: https://arxiv.org/abs/1808.10796 . This proves the equal-rate criterion on the upper half-plane with seeds on its boundary, not on the full lattice. The advance is from 2018/2020, before the supplied November 2026 status.
- Maria Deijfen and Olle Häggström, *Nonmonotonic coexistence regions for the two-type Richardson model*, arXiv:1509.06972, opened at https://arxiv.org/abs/1509.06972 . This concerns constructed graphs rather than a resolution on the lattice; no new full-lattice theorem is inferred from it.
- Janko Gravner and David Sivakoff, *Competing deterministic growth models in two dimensions*, author-hosted manuscript at https://math.ucdavis.edu/~gravner/papers/EJP-competing-growth-rev.pdf . This is a deterministic cellular-automaton model, not T077.

## 2. Chosen piece (before implementation)

Literature search closed after opening the July 2026 paper by Daniel Ahlberg, Maria Deijfen, Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589 (https://arxiv.org/abs/2607.07589 and https://arxiv.org/pdf/2607.07589). Its introduction explicitly says the unequal-rate “only if” direction remains open. Its theorem concerns equal passage-time distributions and an infinite cone of initial infection, so it does not settle the finite-seed unequal-rate problem. No resolution or later substantial advance of T077 itself was found in this bounded search. The known half-plane result is recorded above as an omitted related special case, not as a solution of the stated full-lattice problem. No SOLVED_ELSEWHERE.md is warranted.

Compute exact rational upper bounds for coexistence in Z² from two adjacent singleton seeds, using the event that one infection never leaves its initial site. Prove the comparison to the infinite model. Use the 3-by-3 box with the trapped seed removed (an eight-cycle), then a larger 5-by-3 punctured box to improve the bound. Compute the local trapping probability by a finite-state exponential-race recurrence, and check it independently by forward probability propagation. For the eight-cycle, also enumerate the two advancing fronts and derive the large-rate coefficient from independent gamma passage times.

Why this piece: it gives certified bounds for the actual infinite model, involves no statistical or finite-size extrapolation, and fits comfortably within the resource limits. It does not prove noncoexistence at any unequal ratio, and no claim of a new literature-best bound is intended. Merely deleting exterior edges in a two-type process is unsafe; the proof will instead suppress all growth of the tested infection and compare only the other, one-type process on a punctured graph.

## 3. Implementation and first run

Wrote `trapping_bounds.py` using only the Python standard library. It implements a backward bit-mask recurrence and a forward set-state mass propagation separately, an independent enumeration of all 128 left/right sequences on the eight-cycle, and first/second moments of the integrated number of exposed seed neighbors.

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 trapping_bounds.py > trapping_output.txt`

First run stopped before enumeration: `nice: setpriority: Operation not permitted`, followed by `ValueError: current limit exceeds maximum limit` at `resource.setrlimit(RLIMIT_AS, ...)`. The memory index had warned that a process already at nice 20 cannot add another 15 on macOS. Added an explicit `getpriority` check requiring nice >=15. Removed the rejected address-space limit, replacing it with a 14-vertex hard enumeration bound and a 512 MiB peak-RSS guard checked at every probability state. CPU time is capped at 600 seconds and wall time at 900 seconds. No attempt is made to raise scheduling priority or obtain more permissions. Rerun uses the same command and verifies the inherited priority.

The rerun finished in 0.301 seconds and explicitly printed `Process nice level: 20`. Its output is saved verbatim in `trapping_output.txt`, and all rational values are in `trapping_data.json`. There were 29 eight-cycle states and 981 larger-box states. The forward/backward values agreed at all 13 distinct tested rates, the cycle front enumeration agreed, the cycle first moment agreed with the gamma-integral calculation, and the cycle second moment agreed between the front enumeration and the moment recurrence. Selected output:

```text
3x3: area mean=27/4; area second moment=431/8
  r=2: upper=0.927897988920
  exact upper at r=2: 1466583599/1580544000
5x3: area mean=1240529051/194400000
  area second moment=36966833651/777600000
  r=2: upper=0.921859253275
  exact upper at r=2: 1183866617620303957642961/1284216233024601676800000
All exact independent checks passed.
```

## 4. Strengthening the same certificate

Before writing the next implementation: allow the tested infection to occupy K = {(0,0),(-1,0),(0,1),(0,-1)}, rather than just its starting site. Stop unsuccessfully as soon as it tries to leave K. Competitor growth remains restricted to a finite induced graph. Add a short outer detour around each extremal neighbor so that deleting any connected two-site tested cluster leaves the graph connected. This avoids a failed construction: the mere neighbor closure of K has leaves such as (0,2), which the competitor could never capture after (0,1) turns tested. Such a graph loses at the first tested birth and cannot yield a quadratic large-rate certificate.

The new 16-vertex graph has at most 3^3 * 2^11 = 55296 states before reachability restrictions: only three initially healthy vertices may acquire the tested type. Thus this is still a small, bounded enumeration, within the same local-extinction-bound task. Exact backward and forward algorithms will be implemented separately; no inferred large-rate exponent will be reported without proof.

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 cluster_bounds.py > cluster_output.txt`

Output: 2735 reached states, 1.417 seconds, all 13 exact forward/backward comparisons passed. Selected coexistence upper bounds: r=2 gives 0.879513957510; r=10 gives 0.233499308634; r=100 gives 0.003975074607. The exact coefficients of the restricted failure probability in epsilon=1/r are (0,0,33393164656111/806215680000). This coefficient is not yet used as a global inequality. The script also prints the crude independently provable bound 1638/r²: 14 choose 2 possible positions of the first two tested births, with conditional hazard bounds 3/r and 6/r. Connectivity after zero or one tested births was checked explicitly.

Audit extension, before implementation: compute a sharper global quadratic constant by integrating the opportunities for two tested births along pure-competitor growth, discarding the probability of surviving each intervening tested hazard. Positive integral weights then upper-bound the actual two-birth probability for every r. Recompute that constant by forward occupation-weight propagation. Recompute the large-rate coefficient independently by checking whether the competitor can still reach every exterior vertex after the second tested birth. This checks both the numerical coefficient and the argument's possible missing disconnected component.

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 audit_bounds.py > audit_output.txt`

Output: the global coefficient is B=2977401937361/53747712000, approximately 55.39588247702525. The independently recalculated leading coefficient is L=33393164656111/806215680000, approximately 41.41964177143144. Both values agree between backward and forward positive insertion integrals; L also agrees with the separate rational-series recurrence. All stored rate values satisfy the global quadratic bound. The audit reached 2479 states in 0.095 seconds.

## 5. Proof and adversarial review

Wrote `PROOF.md`, including the arrow coupling, disjointness of actual extinction events, finite-state recurrence, connectivity checks, the all-r quadratic bound, and the distinction between the certificate's asymptotics and the actual coexistence probability. The proof also gives the independent singleton cycle and gamma checks.

Cases specifically checked: a disconnected unseeded competitor component after a second tested birth; success while other healthy sites still remain; missing exterior arrows from a tested site; a final cycle vertex with two active edges but only one target; reciprocal rates and reflected seed locations; the equal-rate case; dimensions and seed placements beyond the claim. All tested neighbors must lie in G, which is checked in code. For coefficient L, an unseeded component matters exactly when it contains a vertex outside K; counting all such second births as harmless would give a wrong coefficient.

Presentation audit found that nearest-rounded decimals from raw output cannot safely be printed as literal upper bounds. Added integer-based upward decimal rounding to all table outputs and a peak-RSS report. One attempted multi-file patch failed validation and changed no files; the corrected patch was then applied. Final reruns and a check against the prose table follow below.

## 6. Final commands and complete output

All four final commands exited zero. The common stderr warning was `nice: setpriority: Operation not permitted`; each process independently verified its inherited nice level of 20. On this Mac the reported peak-RSS units are bytes. The largest recorded peak was 22872064 bytes, below 23 MB. No calculation ran longer than two seconds.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 trapping_bounds.py > trapping_output.txt
```

Complete stdout:

```text
Process nice level: 20
Exact trapping bounds; r = competitor rate / tested-seed rate
3x3: vertices=8, evaluated states=29
  area mean=27/4; area second moment=431/8
  r=   1: upper_ceil=0.976666666667; q(r)=0.011666666667; q(1/r)=0.011666666667
  r= 3/2: upper_ceil=0.960532842530; q(r)=0.036544921875; q(1/r)=0.002922235596
  r=   2: upper_ceil=0.927897988921; q(r)=0.071152575316; q(1/r)=0.000949435764
  r=   3: upper_ceil=0.848826324713; q(r)=0.151011297376; q(1/r)=0.000162377911
  r=   5: upper_ceil=0.701279443726; q(r)=0.298706932436; q(1/r)=0.000013623838
  r=  10: upper_ceil=0.471012197202; q(r)=0.528987461740; q(1/r)=0.000000341059
  r= 100: upper_ceil=0.064887129192; q(r)=0.935112870808; q(1/r)=0.000000000001
  exact upper at r=2: 1466583599/1580544000
5x3: vertices=14, evaluated states=981
  area mean=1240529051/194400000; area second moment=36966833651/777600000
  r=   1: upper_ceil=0.974527018158; q(r)=0.012736490921; q(1/r)=0.012736490921
  r= 3/2: upper_ceil=0.956997327842; q(r)=0.039834959595; q(1/r)=0.003167712564
  r=   2: upper_ceil=0.921859253276; q(r)=0.077121333562; q(1/r)=0.001019413163
  r=   3: upper_ceil=0.838116459535; q(r)=0.161712141031; q(1/r)=0.000171399434
  r=   5: upper_ceil=0.685668861205; q(r)=0.314317061969; q(1/r)=0.000014076826
  r=  10: upper_ceil=0.454688016078; q(r)=0.545311638425; q(1/r)=0.000000345498
  r= 100: upper_ceil=0.061502276556; q(r)=0.938497723444; q(1/r)=0.000000000001
  exact upper at r=2: 1183866617620303957642961/1284216233024601676800000
All exact independent checks passed.
Peak RSS: 17743872 platform units
Elapsed seconds: 0.316
Data: trapping_data.json
```

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 cluster_bounds.py > cluster_output.txt
```

Complete stdout:

```text
Process nice level: 20
Cluster confinement: tested region K has 4 vertices; graph G has 16
r=   1: upper_ceil=0.963212367649; q(r)=0.018393816176; q(1/r)=0.018393816176
r= 3/2: upper_ceil=0.935503608356; q(r)=0.060161832327; q(1/r)=0.004334559317
r=   2: upper_ceil=0.879513957511; q(r)=0.119147717112; q(1/r)=0.001338325378
r=   3: upper_ceil=0.746557074658; q(r)=0.253231052167; q(1/r)=0.000211873175
r=   5: upper_ceil=0.517827898619; q(r)=0.482155921417; q(1/r)=0.000016179965
r=  10: upper_ceil=0.233499308635; q(r)=0.766500323312; q(1/r)=0.000000368054
r= 100: upper_ceil=0.003975074607; q(r)=0.996024925393; q(1/r)=0.000000000001
Evaluated states: 2735
Failure coefficients in epsilon=1/r: (Fraction(0, 1), Fraction(0, 1), Fraction(33393164656111, 806215680000))
Elementary bound: P(coexistence) <= 1638/r^2
All exact forward/backward and connectivity checks passed.
Peak RSS: 22872064 platform units
Elapsed seconds: 1.239
```

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 audit_bounds.py > audit_output.txt
```

Complete stdout:

```text
Process nice level: 20
Global quadratic constant B = 2977401937361/53747712000 = 55.395882477025
Certified upper decimal for B: 55.395882477026
Leading failure coefficient L = 33393164656111/806215680000 = 41.419641771431
B and L independently agree between backward and forward insertion integrals.
L also agrees with the separate exact rational-series recurrence.
All stored rate values satisfy failure <= B/r^2.
Backward insertion states: 2479
Elapsed seconds: 0.091
Peak RSS: 19447808 platform units
```

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 verify_artifacts.py > verification_output.txt
```

Complete stdout:

```text
Process nice level: 20
Seven proof-table upper decimals agree with independent Decimal ceilings.
All exact bounds, reciprocal data, and 13-rate monotonicity checks passed.
Counts: 16 graph vertices, 4 allowed vertices, 2735 reached states.
State ceiling 55296 and elementary constant 1638 agree independently.
```

## 7. Completion

REPORT.md records the computed verdict, exact constants, scope, literature status, commands, failed constructions, uncertainty about novelty, and the next mathematical obstacle. PROOF.md and every exact-data artifact exist and are nonempty. The prose table passed independent Decimal ceiling verification. All requested writes are inside T077. No git, subagents, external messages, or brain/checklist/mesh mutations were used.

Task: “push this problem forward by one checkable piece” — T077, 2026-11-14 21:56 Asia/Tbilisi, observed session start.
