# T102 work log

Task received: 2026-11-14, approximately 21:59 Asia/Tbilisi (17:59 UTC).
Owner's task: “push this problem forward by one checkable piece.”

## 1. Orientation and literature search (started 17:59 UTC)

Read PROMPT.md and the startup memory. A brain recall for “two dimensional
incipient infinite cluster resistance exponent spectral dimension” returned no
useful on-topic result. No subagents, git, or external writes are authorized.
The folder-only instruction takes precedence over global checklist/mesh/memory
writes; those shared stores will not be updated.

Commands: `rg --files -g 'AGENTS.md' -g '*.md' -g '*.py' -g '*.json' .`,
`sed -n '1,90p' PROMPT.md`, and read-only startup/compute-state inspection.
Initially only PROMPT.md was present. Compute governor reported `warn`,
`owner_away_open`, 99.5% CPU, roughly 70% free memory. No heavy compute planned.
The requested `OMP_NUM_THREADS=1 nice -n 15 python3 ... brain.py recall ...`
printed `nice: setpriority: Operation not permitted` but finished. `ps` was
also denied by the sandbox. Priority inheritance must be checked before any
further program; no claim of successful nice adjustment is made.

Web-search queries so far:

- `"2604.14122"`
- `"incipient infinite cluster" "resistance exponent" 2026`
- `"Dankovic" "Markering" "Miller" "Yuan" spectral`
- `"percolation" "resistance exponent" "2026" "Alexander"`
- `"spectral dimension" "two-dimensional" "2026" percolation`
- `"2604.14122" resistance bounds`

Opened https://arxiv.org/abs/2604.14122 and
https://arxiv.org/html/2604.14122v1. Searches currently point back to the paper
in the brief; no later solution located. This is a bounded search, not a proof
of absence. Exact theorem statements and version history remain to inspect.

## 2. Concrete piece chosen, before doing it

Derive an exact deterministic gluing formula for electrical resistance across
an interface, separating the two separately wired resistances from the energy
needed to match their optimal boundary currents. Include an explicit planar,
unit-resistance example showing that the omitted matching term can be
arbitrarily large. Then state precisely what annular matching estimate would
suffice to transfer an annular resistance exponent to the rooted exponent.

Why this piece: the unknown resistance exponent is the bottleneck in T102.
Scalar resistances of separately wired annuli offer tempting finite-scale
quantities, but identifying their composition requires a justified matching
step. An exact formula and a checked obstruction give a concrete test for
that route. This does not promise a new exponent or an IIC bound, and no
novelty claim is made for the underlying network identities.

## 3. Literature check completed within ten minutes

Additional queries: `"Alexander–Orbach" "2026" "two" resistance`,
`"incipient" "resistance" "2026" "91/96"`,
`"2604.14122" "spectral" "November"`, and
`"percolation" "resistance exponent" after:2026-04-16`.
No post-brief solution or substantial advance located. The opened arXiv page
lists only v1, submitted 15 April 2026. Corollary 1.3 gives almost-sure rooted
resistance growth; Corollary 1.4 gives the two random-walk exponents in terms
of the unidentified resistance exponent. The authors on the opened paper are
Irina Đanković, Maarten Markering, Jason Miller, Yizheng Yuan. Reference:
https://arxiv.org/abs/2604.14122 ; full text:
https://arxiv.org/html/2604.14122v1 . No SOLVED_ELSEWHERE.md is warranted.

Priority check command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B -c 'import os; print("effective_nice=", os.getpriority(os.PRIO_PROCESS, 0)); print("OMP_NUM_THREADS=", os.environ["OMP_NUM_THREADS"])'`

Output: `nice: setpriority: Operation not permitted`, `effective_nice= 20`,
`OMP_NUM_THREADS= 1`. Thus programs inherit nice 20 (lower priority than 15);
the relative nice command cannot increase it further on this Mac. Subsequent
small computations will retain nice 20, single-thread environment settings,
and use only the Python standard library.

## 4. Derivation and first independent check

Wrote PROOF.md: minimum-energy orthogonality, exact two-piece correction,
its matrix form, the subdivided-cycle obstruction, and a version for many
layers that allows disconnected pieces. The proposed IIC application is
explicitly conditional on a simultaneous annular current-matching estimate.

Wrote check_gluing.py using exact fractions and independently solving the
full-network Kirchhoff equations. First command:

`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_gluing.py`

First output: the known nice warning, followed by
`ValueError: current limit exceeds maximum limit` at `setrlimit(RLIMIT_AS,...)`.
The program stopped before doing any network computation or writing data.
Investigating the platform's resource limits before rerunning. The mathematical
claim has not yet passed the computational audit.

## 5. Resource fix and successful exact verification

The analogous DATA-limit call was rejected too, before any network calculation.
Read-only diagnostic command:
`OMP_NUM_THREADS=1 nice -n 15 python3 -B -c 'import resource; print("AS",resource.getrlimit(resource.RLIMIT_AS)); print("DATA",resource.getrlimit(resource.RLIMIT_DATA)); print("RSS",resource.getrlimit(resource.RLIMIT_RSS)); print("peak",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)'`
Output: all three limits were `(9223372036854775807, 9223372036854775807)`;
initial peak RSS was 11845632 bytes. Removed the unsupported memory-limit
calls. The largest matrix has 66 rows; the successful run explicitly checked
its actual peak RSS against 1 GB. CPU limit 90 seconds and wall alarm 120
seconds remain active. Only the Python standard library is imported.

Successful command (same as above):
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_gluing.py`

Exact output, apart from the already-explained nice warning:

```json
{
  "effective_nice": 20,
  "OMP_NUM_THREADS": "1",
  "peak_RSS_bytes_macOS": 18006016,
  "cycle_cases": 7,
  "three_vertex_interface_cases": 255,
  "nonzero_correction_cases": 210,
  "disconnected_layer_R_i": ["1/2", "3/4", "1/2"],
  "disconnected_layer_correction_energies": ["1/32", "1/16", "1/32"],
  "disconnected_layer_R_full": "15/8",
  "AO_beta": "91/96",
  "AO_walk_dimension": "91/32",
  "result": "all exact rational checks passed"
}
```

Elapsed time reported by the tool: 0.163 seconds. Data: cycle_data.csv,
interface_data.csv, validation_summary.json. Rational Kirchhoff solves on
the full network agree exactly with the independently composed local
quadratic forms. All 255 connected assignments among 1323 candidates pass;
210 have a strictly positive correction. The disconnected middle layer also
passes, with total correction 1/8 and full resistance 15/8.

## 6. Attempts to break the result

Mathematical audit:

- Re-derived the correction by two methods: energy orthogonality on edge
  flows, and a quadratic minimization in interface profiles. The matrix
  derivation does not assume the two quadratic-form matrices commute.
- Re-derived every cycle value by ordinary series/parallel reduction,
  then by minimizing the interface-current quadratic. Exact full-network
  Kirchhoff solutions agree for L=1,2,3,4,8,16,32. L=1 checks the zero
  correction case. At L=32, full resistance is 33/2 and the wired sum is
  64/33, so their ratio is 1089/128, consistent with divergence as L grows.
- Checked disconnected pieces explicitly. The two global paths have lengths
  3 and 5, giving resistance 15/8 by a separate parallel-law calculation.
  Their optimal current split is 5/8 and 3/8. Each outside piece has
  correction 2(1/8)^2=1/32; the middle piece has correction
  (1+3)(1/8)^2=1/16; total correction 1/8. This checks componentwise
  constraints which an unrestricted interface-vector formula could miss.
- Re-derived the exhaustive count independently of network solving. A graph
  on the three interface vertices with k edges admits f(k) terminal-neighbor
  subsets that meet every component, where f=(1,3,7,7). Thus the count is
  sum_{a+b<=3} 3!/[a!b!(3-a-b)!] f(a)f(b)=38+126+84+7=255.
  Wired profiles agree exactly when the two terminal-neighbor masks agree.
  Masks of size 1 permit zero assignments, size 2 permit 6 each, and size 3
  permits 27, so there are 3*6+27=45 zero corrections and 255-45=210
  positive corrections. Added these independent assertions to the script.
- Re-derived the AO threshold by cross multiplication and exact fraction
  substitution: beta=91/96 gives d_w=91/32 and d_s=4/3.
- The lower bound sum R_i<=R_full is always valid; the reverse comparison
  needs the correction. No positivity of individual interface currents was
  assumed. A one-vertex interface has a zero-dimensional correction space.
- The exponent corollary requires estimates for all shells of one cluster,
  not marginal estimates for a typical shell. It also requires b>=0 in the
  stated sufficient bound involving 1+D_m. Both qualifications are explicit.

Limits found: the planar cycle example is not a probabilistic counterexample
on the IIC. No estimate on the correction under the IIC law has been proved.
The current-matching identity follows from the usual minimum-energy principle;
there is no claim that it is a new network theorem. This is a checkable
reduction/obstruction, not a determination or sharper bound of the exponent.

## 7. Final rerun and report

Reran the exact command in section 5 after adding the independent counting
assertions. Exit code 0, runtime 0.168 seconds. All mathematical outputs
were unchanged; final peak RSS was 17039360 bytes. The exact final output
is validation_summary.json (the same fields as section 5, with that updated
RSS value). Wrote REPORT.md with verdict PARTIAL, the completed deterministic
piece, failed resource-limit attempts, explicit limits of applicability,
and the next IIC estimate required. No new exponent or bound is claimed.
