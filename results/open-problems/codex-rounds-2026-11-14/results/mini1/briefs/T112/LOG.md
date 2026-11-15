# T112 working log

Task: “push this problem forward by one checkable piece.”
Session started 2026-11-14 about 21:16 Asia/Tbilisi (UTC+04).

## Constraints and orientation

All writes remain in this directory. No git or external publication. No subagents.
The later folder-only order precludes the usual mesh/checklist/brain writes;
startup memory and the existing T112 memory were read without invoking logging tools.
The T112 memory describes an enormous finite reduction, not a solution.
The current compute-state file reported warn / owner_away_open, not distress.
Every shell program is invoked with OMP_NUM_THREADS=1 and nice -n 15.
The sandbox prints `nice: setpriority: Operation not permitted`; direct Python
`os.getpriority(os.PRIO_PROCESS, 0)` returned 20, so children already have
lower scheduling priority than requested. No priority increase is attempted.

## Step 1: literature search (under ten minutes)

Web searches: `"1/3–2/3" conjecture Aires Chan Pak Panova`,
`"2609.30888"`, `"1/3-2/3 conjecture" solved 2026`,
`"1/3" "2/3" conjecture "November" "2026" proof`.
Opened the following primary records:

* Max Aires, Swee Hong Chan, Igor Pak, Greta Panova,
  *Breaking the Infinite Barrier in the 1/3–2/3 Conjecture*,
  arXiv:2609.30888v2, 28 October 2026.
  https://arxiv.org/abs/2609.30888
  Full HTML opened: https://arxiv.org/html/2609.30888v2
  Theorem 1.2 is a positive epsilon improvement, not the full conjecture.
* Anish Gupta, *Balance Constants, Majority Cycles, and the Gold Partition
  Conjecture through Fourteen Elements*, arXiv:2607.23926v2.
  https://arxiv.org/abs/2607.23926
  The abstract reports an exhaustive fourteen-element verification.
* Kevin Fathi, *Gold Certificates and Balanced Pairs: Selection, Conditional
  Inequalities, and the One-Third–Two-Thirds Conjecture*, Zenodo
  10.5281/zenodo.23933091, version v22, published 3 November 2026.
  https://zenodo.org/records/23933091
  This primary record claims further bounded-degree results and explicitly
  leaves general width three and the unrestricted conjecture open.
  aiXiv:2611.00391 is an index identifier, NOT an arXiv identifier.
  The linked PDF fetch failed; those claims have not been proof-audited here.

No whole-problem solution found. Continue to a concrete computation.

## Step 2: chosen piece (recorded before implementation)

Perform an exact parameter census of three equal chains of length m, with
one directed joining relation per side of a three-cycle:

    A_a < B_b, B_c < C_d, C_e < A_f,
    1 <= a,b,c,d,e,f <= m.

Take transitive closure and discard cyclic presentations. Target m=1,...,8
(through 24 elements), reducing the upper endpoint if timing requires it.
These are parameter presentations, not isomorphism classes. The class has
width at most three and includes cyclic cover graphs; it is not restricted
to forests. It extends past the reported unrestricted fourteen-element census.
For each valid nonchain presentation compute every pair probability exactly,
record a maximizing pair as a compact certificate, and summarize minimum
balance separately for width-three and ordinal-indecomposable members.

Why this piece: six finite gate coordinates give a complete, reproducible
counterexample search in a narrowly defined class. Linear extensions are
three-dimensional lattice paths, so exact counts need only (m+1)^3 states.
A separate verifier will count extensions after adjoining the certificate
comparison; this uses a different state representation. Small orders will
also be checked by direct permutation enumeration. No claim of a new
infinite-family theorem or an unrestricted order-24 census is intended.

## Step 3a: implementation and first guard check

Created census.cpp and run_limited.py. Compile command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py /usr/bin/clang++ -std=c++17 -O2 -Wall -Wextra census.cpp -o census
```

The guard stopped before compilation: setting RLIMIT_DATA to 512 MiB raised
`ValueError: current limit exceeds maximum limit`. Inspecting inherited limits
and adapting the guard before retrying. No census has run yet.

The sandbox also rejects RLIMIT_RSS and soft-only memory-limit changes.
The guard retains CPU/wall limits, reports peak RSS, and relies on the
explicitly small, bounded program arrays for memory. The successful compile
used 126.562 MiB peak RSS and 0.857 seconds wall time.

Pilot command:
```sh
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py ./census 4 > pilot.out
```
Output:
```text
priority=20; OMP_NUM_THREADS=1; cpu_limit=1100s; wall_limit=1140s; memory bounded by program construction; DATA limit unavailable: current limit exceeds maximum limit
m,presentations,cyclic,chains,nonchains,width3,width3_indecomp,min_all,min_width3,min_width3_indecomp,min_width3_indecomp_attainers,gate_a,gate_b,gate_c,gate_d,gate_e,gate_f
1,1,1,0,0,0,0,NA,NA,NA,0,0,0,0,0,0,0
exit=-6; wall_seconds=0.374; child_peak_rss_mib=1.219
```

Pilot audit caught a reversed inequality in the independent cycle criterion.
The correct cycle condition is f<=a AND b<=c AND d<=e: follow
A_a -> B_b <= B_c -> C_d <= C_e -> A_f <= A_a.
The lattice-path transition code was unchanged. Recompiled and reran the
same pilot command successfully. Corrected output:
```text
priority=20; OMP_NUM_THREADS=1; cpu_limit=1100s; wall_limit=1140s; memory bounded by program construction; DATA limit unavailable: current limit exceeds maximum limit
m,presentations,cyclic,chains,nonchains,width3,width3_indecomp,min_all,min_width3,min_width3_indecomp,min_width3_indecomp_attainers,gate_a,gate_b,gate_c,gate_d,gate_e,gate_f
1,1,1,0,0,0,0,NA,NA,NA,0,0,0,0,0,0,0
2,64,27,3,34,13,7,5/13,11/24,11/24,6,1,1,1,2,1,2
3,729,216,6,507,360,252,1/3,137/344,137/344,3,1,1,3,3,1,3
4,4096,1000,9,3087,2592,2052,1/3,36/85,3/7,6,1,2,4,2,1,3
exit=0; wall_seconds=0.542; child_peak_rss_mib=1.484
```

## Step 3b: full target census launched

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py ./census 8 > census.out
```

The pilot needed 0.542 seconds and 1.484 MiB peak RSS.
The full run writes certificates.csv and summary.csv incrementally.

## Step 3c: census completed

Full output of the command recorded above:
```text
priority=20; OMP_NUM_THREADS=1; cpu_limit=1100s; wall_limit=1140s; memory bounded by program construction; DATA limit unavailable: current limit exceeds maximum limit
m,presentations,cyclic,chains,nonchains,width3,width3_indecomp,min_all,min_width3,min_width3_indecomp,min_width3_indecomp_attainers,gate_a,gate_b,gate_c,gate_d,gate_e,gate_f
1,1,1,0,0,0,0,NA,NA,NA,0,0,0,0,0,0,0
2,64,27,3,34,13,7,5/13,11/24,11/24,6,1,1,1,2,1,2
3,729,216,6,507,360,252,1/3,137/344,137/344,3,1,1,3,3,1,3
4,4096,1000,9,3087,2592,2052,1/3,36/85,3/7,6,1,2,4,2,1,3
5,15625,3375,12,12238,11020,9340,1/3,17/40,7599/17770,3,2,2,2,4,4,4
6,46656,9261,15,37380,34875,30825,1/3,313/715,13082/29735,6,2,4,3,3,5,3
7,117649,21952,18,95679,91098,82782,1/3,3/7,32763/74260,3,2,5,6,2,3,6
8,262144,46656,21,215467,207760,192472,1/3,125/286,22205/49566,6,1,7,2,5,7,1
exit=0; wall_seconds=2.514; child_peak_rss_mib=1.969
```
The full search used 2.514 seconds wall time and 1.969 MiB peak RSS.

## Step 4a: independent verifier

Created verify.cpp, which reconstructs every tuple and computes transitive
closure for rejection/classification. It independently counts extensions
using predecessor bitmasks and a memoized recurrence on remaining subsets.
For every saved row it counts both P and P+(x<y), thereby verifying E and
the certificate probability. It also checks every pair of one attaining
example for each reported minimum. Commands:
```sh
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py /usr/bin/clang++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py ./verify 8 > verify.out
```
Compilation succeeded, 0.886 seconds and 132.703 MiB peak RSS.

## Step 4b: independent verification completed

Full verifier output:
```text
priority=20; OMP_NUM_THREADS=1; cpu_limit=1100s; wall_limit=1140s; memory bounded by program construction; DATA limit unavailable: current limit exceeds maximum limit
m=1 cyclic=1 chains=0 nonchains=0 width3=0 width3_indecomp=0
m=2 cyclic=27 chains=3 nonchains=34 width3=13 width3_indecomp=7 minima=5/13,11/24,11/24 core_attainers=6
m=3 cyclic=216 chains=6 nonchains=507 width3=360 width3_indecomp=252 minima=1/3,137/344,137/344 core_attainers=3
m=4 cyclic=1000 chains=9 nonchains=3087 width3=2592 width3_indecomp=2052 minima=1/3,36/85,3/7 core_attainers=6
m=5 cyclic=3375 chains=12 nonchains=12238 width3=11020 width3_indecomp=9340 minima=1/3,17/40,7599/17770 core_attainers=3
m=6 cyclic=9261 chains=15 nonchains=37380 width3=34875 width3_indecomp=30825 minima=1/3,313/715,13082/29735 core_attainers=6
m=7 cyclic=21952 chains=18 nonchains=95679 width3=91098 width3_indecomp=82782 minima=1/3,3/7,32763/74260 core_attainers=3
m=8 cyclic=46656 chains=21 nonchains=215467 width3=207760 width3_indecomp=192472 minima=1/3,125/286,22205/49566 core_attainers=6
VERIFIED certificates=364392 unbalanced_certificates=0 fully_checked_extrema=19 extremal_pair_counts=2532
exit=0; wall_seconds=11.035; child_peak_rss_mib=2.828
```
All 364,392 certificates passed. The verifier also computed all 2,532
pair counts of 19 distinct extremal presentations. It rederived every
reported minimum as a global certificate lower bound plus an attaining
example upper bound.

Third implementation: direct enumeration of all permutations for every
presentation at m=1,2, plus the standard tight three-element example.
```sh
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py python3 brute_small.py > brute_small.out
```
Output:
```text
priority=20; OMP_NUM_THREADS=1; cpu_limit=1100s; wall_limit=1140s; memory bounded by program construction; DATA limit unavailable: current limit exceeds maximum limit
BRUTE VERIFIED presentations=65 cyclic=28 chains=3 nonchains=34; every pair checked
TIGHT EXAMPLE VERIFIED extensions=3; both incomparable-pair balances=1/3
exit=0; wall_seconds=0.094; child_peak_rss_mib=13.562
```

## Step 4c: arithmetic and boundary audit

A separate Python stream pass counted 364,392 certificate rows and 347,718
width-three rows, checked the integer balance inequality again, and found
that every equality certificate lies in an ordinal-decomposable width-two
member. Equality counts by m: {3: 18, 4: 15, 5: 12, 6: 12, 7: 12, 8: 12}.
The independent unconstrained three-dimensional integer recurrence gave
9,465,511,770, agreeing with 24!/(8!)^3. Counts fit in uint64; fraction
cross-products use uint128. Raw/removed counts also agree:
446,964 - 82,488 - 84 = 364,392.

The finite class does not cover arbitrary width-three orders. Targeted
searches for an existing unicyclic-cover theorem yielded no relevant
primary paper; this is not a claim of novelty.

## Step 4d: direct check of the global width-three minimizer

Extended brute_small.py to enumerate all 1,680 shuffles of three length-3
chains by choosing their occupied positions. This avoids both recurrences.
Same command as before:
```sh
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py python3 brute_small.py > brute_small.out
```
Final output:
```text
priority=20; OMP_NUM_THREADS=1; cpu_limit=1100s; wall_limit=1140s; memory bounded by program construction; DATA limit unavailable: current limit exceeds maximum limit
BRUTE VERIFIED presentations=65 cyclic=28 chains=3 nonchains=34; every pair checked
TIGHT EXAMPLE VERIFIED extensions=3; both incomparable-pair balances=1/3
WIDTH-THREE MINIMIZER VERIFIED shuffles=1680; extensions=344; A3_before_B3=137; maximum_balance=137/344; every pair checked
exit=0; wall_seconds=0.090; child_peak_rss_mib=13.859
```

## Step 4e: saved-data audit and manifest

Created audit_data.py for aggregate arithmetic, streaming certificate
checks, completeness of all saved extremal pair matrices, and file hashes.
It was rerun after the direct minimizer check to refresh the manifest.
```sh
OMP_NUM_THREADS=1 nice -n 15 python3 run_limited.py python3 audit_data.py > audit_data.out
```
Final output:
```text
priority=20; OMP_NUM_THREADS=1; cpu_limit=1100s; wall_limit=1140s; memory bounded by program construction; DATA limit unavailable: current limit exceeds maximum limit
TOTALS {"chains": 84, "cyclic": 82488, "nonchains": 364392, "presentations": 446964, "width3": 347718, "width3_indecomp": 317730}
EQUALITY_COUNTS {"3": 18, "4": 15, "5": 12, "6": 12, "7": 12, "8": 12}
UNCONSTRAINED_COUNT_BY_DP_AND_FACTORIAL 9465511770
EXTREMAL_PRESENTATIONS 19
EXTREMAL_PAIR_COUNTS 2532
GLOBAL_WIDTH_THREE_MINIMUM 137/344
WROTE manifest.json
exit=0; wall_seconds=1.548; child_peak_rss_mib=35.812
```

## Step 5: deliverables

Wrote PROOF.md (finite statement and counting justification), REPORT.md
(verdict, exact scope, reproduction, failures, limits, next step), and
SOLVED_ELSEWHERE.md (no full solution found; bounded literature status).
The linked newer PDF remained inaccessible on retry; its record is only
an unverified lead. All writes, programs and data stayed in this folder.
No git, messages, external publication, model workers or subagents used.

Task: “push this problem forward by one checkable piece” — 2026-11-14 21:16 Asia/Tbilisi.

Final document audit: updated PROOF.md to the final brute/shuffle timing
(0.090 seconds, 13.859 MiB); earlier timing remains recorded above.
REPORT.md starts with the required VERDICT line. The manifest contains
hashes of all computation sources, three data files, and primary outputs.
