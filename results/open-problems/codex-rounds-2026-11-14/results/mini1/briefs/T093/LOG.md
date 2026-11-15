# T093 work log

Task: “push this problem forward by one checkable piece.” Session started 2026-11-14 at approximately 21:15 +04 (Asia/Tbilisi).

## 21:16 +04 — orientation and literature search started

Read the startup memory index and compute state without changing them. The current task's folder-only rule excludes brain/checklist/mesh writes outside this folder. No subagents, git, or external writes will be used.

Commands were prefixed with `OMP_NUM_THREADS=1 nice -n 15`. macOS printed `nice: setpriority: Operation not permitted` but ran the commands; inherited priority will be checked before any computation. Compute state reported `status: ok`, `mode: owner_away_open`. Only small, single-thread computations are planned.

Initial web searches:

- `random graph colourability threshold convergence 2025 2026 3 coloring 4.69`
- `random graph coloring threshold 2024 2025 existence limit fixed q`
- `"Existence of the q-Colorability Threshold" Aronow Lopatto`
- `"3-colorability" "4.697" random graphs upper bound`

Found a recent Hexagon preprint, P. M. Aronow and Patrick Lopatto, *Existence of the q-Colorability Threshold for Sparse Random Graphs*, identifier hexagon:2610.00608v1. Search results describe convergence, but not identification with the cavity prediction. The primary page and paper still need to be opened before drawing conclusions. Also found an older upper bound of 4.697 that needs its primary reference checked. A search result alone is not verification.

## Literature check and choice (before computation)

Opened the primary Hexagon page and 105-page PDF: https://hexagonmath.org/2610.00608v1 and https://hexagonmath.org/pdf/2610.00608v1. Theorem 1.1 claims existence of the limiting threshold for every fixed q >= 3; p. 4 explicitly says its value is not determined. This is an unrefereed claim, not a proof audited here. Thus the whole problem is not settled by this source. Opened arXiv:1305.0177, arXiv:1304.1063, and arXiv:1812.09691 as well. The literature search is now ending within its ten-minute budget; details go in SOLVED_ELSEWHERE.md.

Choice: derive the first correction to the small-obstruction explanation of non-3-colourability in G(n,c/n) for fixed 0 < c < 1. Specifically, classify all K4-free obstructions of excess e-v <= 4, and use that classification to compute the leading probability of non-3-colourability with no K4 present. This gives an exact rate in a special case, rather than an unsupported claim about c near 4.69. A finite exhaustive classification on at most eight vertices will be checked with an independent graph generator and colouring test. The asymptotic tail needs a written proof, not simulation.

Priority diagnostic command:

`OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os, resource; print("nice", os.getpriority(os.PRIO_PROCESS, 0)); print("OMP_NUM_THREADS", os.environ.get("OMP_NUM_THREADS")); print("memory_limit", resource.getrlimit(resource.RLIMIT_AS))'`

Output: `nice 20`, `OMP_NUM_THREADS 1`. The nice warning comes from attempting to add 15 to inherited nice 20; the actual process already has lower priority than requested. Scripts will enforce a 768 MiB address-space limit and a 19-minute CPU limit.

## First implementation and platform correction

Wrote `enumerate_obstructions.py`, an exhaustive labelled graph generator with degree and edge-count pruning, a three-colouring backtracker, and permutation-orbit checks. First command:

`OMP_NUM_THREADS=1 nice -n 15 python3 enumerate_obstructions.py > enumeration.txt`

It stopped before enumeration: macOS rejected lowering `RLIMIT_AS` to 768 MiB with `ValueError: current limit exceeds maximum limit`. Replaced that unsupported address-space restriction with `RLIMIT_DATA` at 768 MiB and retained the 19-minute CPU and 1100-second wall limits. Actual peak RSS is recorded in the data. This computation uses only tiny graphs and stores at most the small obstruction orbits.

Setting both soft and hard DATA limits failed the same way. Updated the script to retain the inherited hard limit, lower only the soft limit if supported, and explicitly check peak RSS at every recursion entry. Both unsuccessful launches stopped before enumeration. This is a platform restriction, not a mathematical failure.

## Exhaustive census completed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 enumerate_obstructions.py > enumeration.txt`

Output (`n, m, all minimum-degree-3 graphs, K4-free, K4-free non-3-colourable`):

```
4  6      1      0    0
5  8     15     15    0
5  9     10      0    0
6  9     70     70    0
6 10    537    537   72
7 11   5670   5670  630
8 12  19355  19320    0
```

The 72 six-vertex graphs form one permutation orbit with automorphism group of size 10; the 630 seven-vertex graphs form one orbit with automorphism group of size 8. All are vertex-critical. Representatives and complete counts are in `obstructions.json`; readable output is in `enumeration.txt`. Runtime 1.082 s, peak RSS 15,122,432 bytes, nice 20. Soft CPU limit succeeded; DATA limit is unsupported, and RSS was checked at each recursive step.

The predicted K4-free failure coefficient is therefore c^10/10 + c^11/8 at order n^-4. This is provisional until independently checked. The remaining analytical step is an O_c(n^-5) bound on other critical obstructions, using exponential component tails for c < 1. A full failure expansion through n^-4 is also available if K4 overlaps are accounted for.

## Independent census check

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 run_independent.py > independent.txt`

The runner compiles `independent_check.cpp` with `clang++ -O2 -std=c++17 independent_check.cpp -o independent_check` and runs it. This checker enumerates fixed-size edge subsets, rather than neighbour sets, and tests containment in complete tripartite graphs from all 3^v assignments, rather than using the Python colouring backtracker.

Output: all seven rows above matched exactly. Final lines:

```
PASS: independent edge-subset enumeration finished
PASS: all independent counts match obstructions.json
peak_child_rss_bytes 122617856
seconds 1.827
```

Data: `independent_counts.csv`. The runner now points compiler temporary files into this folder for future reruns.

## Probability derivation and overlap audit

Wrote `PROOF.md`. The main estimate is

`P(non-3-colourable and K4-free) = (c^10/10 + c^11/8)n^-4 + O_c(n^-5)`

for each fixed 0 < c < 1. Its tail proof uses a direct exploration bound with rho=c*exp(1-c)<1; components larger than O_c(log n) have probability O(n^-6), and a minimum-degree first moment handles smaller high-excess witnesses. No simulation or unproved branching-process limit is used.

Accounting for K4 pairs gives the full expansion

`P(non-3-colourable) = c^6/(24n^2) - c^6/(4n^3) + [11c^6/24-c^9/12+c^10/10+c^11/8-c^12/1152]/n^4 + O_c(n^-5)`.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 check_coefficients.py > coefficient_checks.txt`

Output:

```
overlap vertices [6,6]: 13317 cases, minimum union excess 6
overlap vertices [6,7]: 37633 cases, minimum union excess 6
overlap vertices [7,7]: 130914 cases, minimum union excess 5
overlap vertices [4,6]: 1045 cases, minimum union excess 5
overlap vertices [4,7]: 1961 cases, minimum union excess 5
PASS: K4 pair counts by direct enumeration for n=4,...,10
PASS: all K4 triple intersection types, minimum excess 5
PASS: falling-factorial coefficients [1, -6, 11, -6, 0]
PASS: coefficient and overlap checks
seconds 0.386
peak_rss_bytes 14827520
```

Data: `coefficient_checks.json`. The factors 10 and 8 were also re-derived from the wheel's dihedral symmetries and the two diamonds' flips/exchange; the factor 11 in (n)_4 was checked both by polynomial multiplication and elementary pair sums. Pair counts were checked by directly forming pairs on n=4,...,10 vertices. All possible overlap injections between the two obstruction types, and between each and K4, were checked. K4 triples were checked over every intersection type.

## Attempt to break the argument

- A leading K4 term alone misses the two K4-free classes; both appear at n^-4, so neither can be discarded from that coefficient.
- The n^-4 K4 correction requires both disjoint pairs and pairs sharing three vertices. Overlap one or two contributes only to the next order. Third-order inclusion-exclusion has excess at least five, verified analytically and by exhaustive intersection types.
- The bound for small dense sets cannot just replace all sizes by O(log n), which would lose logarithmic factors. Differentiating the logarithm of the bound gives a geometric decrease and preserves the O(n^-5) remainder.
- A minimal non-colourable witness is connected and has minimum degree three; this is why the component-size bound applies. The argument would not justify excluding a large disconnected union solely by its total vertex count.
- Neither the component tail nor its constants extend uniformly to c=1. No statement at c=1, in the critical window, or near c=4.69 is claimed.
- No novelty claim is made. This is an exact special-case rate and a reproducible obstruction census, not a determination of the colourability threshold.

## 21:26 +04 — final artifact audit

Created `REPORT.md` with the required verdict line. A final read-only Python check loaded both JSON files, checked the total of 25,658 census graphs, independently recomputed 6!/10 and 7!/8, checked every recorded overlap lower bound, verified the report's first line, and verified that the proof, logs, literature update, outputs, and CSV data exist. Output: `PASS: final artifact integrity; 25,658 census graphs; symmetry factors and overlap bounds consistent`.

Completed the authorized piece. The limiting colourability threshold and cavity identification are not claimed proved by this work.
