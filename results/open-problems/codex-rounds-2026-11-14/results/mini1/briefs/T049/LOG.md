# T049 work log

Task received: 14 November 2026, approximately 20:45 Asia/Tbilisi (16:45 UTC).

## 1. Orientation and literature search (started 16:45 UTC)

Read the startup memory index and compute governor state. The latter reports `status: ok`. The task-specific instruction to write only in this folder overrides the global mesh/checklist/brain commands, which write elsewhere; those commands were not run. No git or subagents were used.

Initial read-only commands: `pwd`; file discovery with `rg --files`; `cat ~/.claude/compute/compute_state.json`; `ls -la`; read the startup `MEMORY.md`. Subsequent commands were prefixed with `env OMP_NUM_THREADS=1 nice -n 15`. The sandbox prints `nice: setpriority: Operation not permitted`; a later `ps` query was also blocked. No computation has been launched, and the inherited priority has not been verified.

Web searches so far: `minimal spanning forest Z d connectivity dimension 8 open problem 2025 2026`; `minimal spanning forest lattice connected dimension three open problem recent`; `"minimal spanning forest" "2026"`; `"minimal spanning forest" "2025" connected lattice`; `"minimal spanning tree" slabs Newman Tassion Wu arxiv`.

Opened https://arxiv.org/abs/math/0412263 and the accepted manuscript https://wrap.warwick.ac.uk/id/eprint/114352/1/WRAP-critical-percolation-minimal-spanning-tree-slabs-Wu-2020.pdf . Found the known slab extension, arXiv:1512.09107 (2015/2017), rather than a resolution on full Z^d. Checking the theorem and looking for later advances before choosing the piece.

## 2. Choice (16:49 UTC; recorded before implementation)

Prove and exactly evaluate a local lower bound on nearest-neighbor connectivity, stronger than the edge-inclusion probability 1/d. For each of the 2(d-1) plaquettes containing a fixed edge e, wire the complement of its four vertices to one vertex, retaining all parallel boundary edges. Calculate the exact probability that the finite wired MST contains the three-edge path around e. Every such path edge is forced into the infinite MSF by a finite cut. Different plaquettes' certificates are disjoint because two such paths would make a cycle. Thus their probabilities can be added to P(e in MSF)=1/d. This is one finite-certificate bound, not a solution or a claim of novelty.

Why this choice: it avoids an uncontrolled extrapolation from finite boxes, gives an exact checkable rational bound in every d>=2, and permits an independent verification by enumerating the 4! orderings of each proposed finite spanning tree versus a partition recursion.

Literature search completed well inside ten minutes. Additional searches were `"minimal spanning forest" "Z" "open" "2024"`, `"minimal spanning forest" "connectivity" "2025"`, and `"minimal spanning forest" "2026" "lattice"`. Opened arXiv:1512.09107, arXiv:2609.11845, and the full Lyons--Peres--Schramm paper at https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf . The 2017 slab theorem (Theorem 2.5 and Remark 2.6) is an older special-case extension omitted from the brief; it does not settle full Z^d. The 2026 paper concerns skewed maximal forests and nonunimodular percolation, with no announced lattice connectivity result. No post-status solution or advance on full Z^d was found; this is a bounded search, not an exhaustive certification.

The startup memory contains a verified scar about relative `nice` stacking at an inherited priority of 20. Read it; will check priority via `os.getpriority` and abort computation if priority is below 15. All numerical work will be tiny, one-threaded, with a hard runtime guard and memory limit.

## 3. First exact-check implementation

Priority check command: `env OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os; print("nice", os.getpriority(os.PRIO_PROCESS, 0))'`. Output: `nice 20` (also the harmless relative-nice warning). Thus the inherited process is already lower priority than requested.

Implemented `verify.py` with two exact methods: Kruskal contraction recursion and integration of the finite MST cycle inequalities over ordered weight simplices. Also included an exhaustive 8! raw-order test at boundary multiplicity m=1, and a grouped symbolic finite-sum formula.

First command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt`. It stopped immediately at `resource.setrlimit(RLIMIT_AS, ...)` with `ValueError: current limit exceeds maximum limit`; no arithmetic or data was produced. Inspecting the existing limits before correcting this platform-specific guard.

The existing AS and RSS limits both print `(9223372036854775807, 9223372036854775807)`. Both attempts to lower these limits were rejected with `ValueError`. Adjusted the guard to record the unavailable limit and measure peak RSS. The computation holds only a few dozen five-vertex partitions and exact fractions; the 8! orders are streamed. It has a 120-second alarm and no large allocation or third-party numerical library.

## 4. Exact calculation completed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt`.
Exit status 0; tool-reported wall time 0.142 seconds. Output is saved verbatim in `verification.txt`; exact fractions, formula factors, and measurements are saved in `data.json`. Peak RSS 15,908,864 bytes; inherited nice level 20; OMP_NUM_THREADS=1; standard library only. AS/RSS hard limits are unavailable in this sandbox, as recorded above; measured usage is well below 1 GB.

Key output:

```
d  plaquette probability  nearest-neighbor connectivity lower bound
2 47/1485 1673/2970 0.563299663300
3 5521/658350 120767/329175 0.366877800562
4 4217/1261260 113539/420420 0.270060891489
5 168877/102035700 5439539/25508925 0.213240620685
6 1920671/2050647984 180490687/1025323992 0.176032832947
7 199639/343898100 4293664/28658175 0.149823357559
8 3481091/9058076775 9447958967/72464614200 0.130380311429
9 1999367/7476054300 215665643/1869013575 0.115390089128
10 1705463/8812280750 911926409/8812280750 0.103483585563
11 152662663/1056244864752 24768878423/264061216188 0.093799758937
12 766919/6923350980 593818133/6923350980 0.085770335018
Independent cycle-integral checks: 11/11 exact matches
Raw permutation check m=1: 3344 / 40320 = 209/2520
Grouped formula terms: 14 ; multiplicities sum: 96
PASS; data written to data.json
```

The stronger wired-square event replaces the initial sufficient event that the three path edges precede every other incident edge. Its probability is strictly greater in each checked dimension. The strengthening remains within the chosen finite-certificate calculation.

## 5. Adversarial audit

Wrote out `PROOF.md`. Checked the finite-to-infinite step using the actual finite cut opposite the wired root, so an arbitrary exterior completion cannot undo a certified edge. Checked that the spoke multiplicity is per vertex, not per exterior vertex: distinct edges remain independent even when their exterior endpoints coincide. Checked that adding plaquette probabilities uses incompatibility (a six-cycle in F), not independence. Checked the edge-inclusion identity 1/d directly by induced-forest component counts in boxes, with every component reaching the inner boundary.

Added explicit lattice coordinate generation for d=2,...,12 to audit the counts of incident/internal/external edges, the 2(d-1) plaquettes, and the six-cycle formed by every pair of alternate paths. The existing arithmetic audit already compares a partition recursion, ordered-simplex integration of the cycle criterion, all 96 tree-edge orderings grouped in 14 terms, and all 40320 raw orders for m=1. Rerunning is justified by these added geometry checks.

Final verification command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt`. Exit 0, wall time 0.088 seconds, peak RSS 15,499,264 bytes, nice 20. All 11 exact fraction comparisons, all 11 explicit lattice geometry checks, and the 40320-order auxiliary check passed. Final full output is `verification.txt`; exact data are `data.json`. A supplementary leading-coefficient calculation prints `Limit m^3 a_m: 1253/864`; it is not needed for the stated proposition.

Independent hand checks: 1/3+4(5521/658350)=120767/329175. The number of edges internal to a lattice box was counted both by axis positions and by summing vertex degrees and subtracting exiting edges. The 8d-4 incident edges at a plaquette were counted both by four internal edges plus four sets of 2d-2 external edges, and by the degree sum. The proof explicitly covers the possibility that a restricted forest component is isolated, that exterior vertices coincide, and that plaquette events share labels. The d=2 bound is below the known exact connectivity probability 1, and the bounds decrease on the computed range rather than falsely suggesting a dimension-eight transition.

Remaining limitation: this elementary local improvement is not known here to be novel, and it yields no result on the number of infinite components. The slab result found in the literature predates the supplied November 2026 status. No `SOLVED_ELSEWHERE.md` is appropriate for a post-status lattice resolution, because none was found.

## 6. Deliverables

`PROOF.md` contains the full finite-cut and disjointness proof, a finite-sum formula valid for all d>=2, and the independent integral derivation. `verify.py`, `verification.txt`, and `data.json` reproduce and audit the arithmetic for d=2,...,12. `REPORT.md` records the partial verdict and the next possible extension. All authored files remain in this folder. A first attempt to apply the final document patch failed to match a wrapped context line and made no changes; the narrower patch succeeded.

Final read-only audit: `head -1 REPORT.md`; `wc -l LOG.md PROOF.md REPORT.md verify.py verification.txt data.json`; `sed -n '1,155p' PROOF.md`; `sed -n '1,110p' REPORT.md`, all under `env OMP_NUM_THREADS=1 nice -n 15`. Confirmed the required verdict first line, the written cut argument, correct rational values, literature qualifications, reproduction command, and all six deliverables. No further computation was needed.
