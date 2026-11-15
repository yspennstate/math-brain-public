# T089 work log

Task received 2026-11-14, approximately 20:54 Asia/Tbilisi (UTC+04):
"push this problem forward by one checkable piece."

## 20:55 — Scope and startup

Read the supplied statement, local directory listing, startup memory index, the
record about inherited macOS nice levels, and the compute governor state. The
directory initially contained PROMPT.md, codex.log, and run.pid. Governor status
was `ok`, mode `owner_away_open`; no heavy computation is planned.

The current task's restriction to writes inside this folder overrides the older
instructions to mutate the shared mesh, checklist, or brain. Those shared state
commands were not run. No git commands or subagents will be used.

Shell commands are launched with `env OMP_NUM_THREADS=1 nice -n 15 ...`.
The sandbox prints `nice: setpriority: Operation not permitted`, but continues
the command. Process inspection with `ps` is also denied. Before any numerical
check, independently inspect the Python process's inherited priority and enforce
a nice level of at least 15 or abort. No large computation is authorized by this
log.

## 20:56 — Literature search started (limit: ten minutes)

Used the web search tool with queries including:

- `Bohigas Giannoni Schmit conjecture proof 2025 2026 billiard GOE`
- `quantum chaos random surfaces GOE spectral statistics 2025 2026 theorem`
- `site.arxiv.org Bohigas Giannoni Schmit 2026 spectral statistics proof`
- `site.arxiv.org "Almost Sure GOE Fluctuations"`

Search hits suggest recent results for smooth statistics of random surfaces and
random perturbations, rather than a fixed billiard's nearest-neighbour law.
Primary pages are being opened before drawing a conclusion.

## 21:00 — Literature check concluded; concrete piece selected

Opened the arXiv abstract pages of the following papers, preserving the author
names exactly as displayed there:

1. Julien Moy, *Smooth spectral statistics of random perturbations of Schrödinger
   operators near Anosov energy levels*, arXiv:2610.09869 (7 October 2026),
   https://arxiv.org/abs/2610.09869 . Also opened the full HTML text. This is
   a substantial related advance for smooth mesoscopic statistics of randomly
   perturbed operators, not a fixed billiard's microscopic spacing theorem.
2. Julien Moy, *Spectral statistics of the Laplacian on random covers of a closed
   negatively curved surface*, arXiv:2408.02808,
   https://arxiv.org/abs/2408.02808 . The abstract specifies smooth counting
   variances and an iterated large-cover/high-energy limit.
3. Zeév Rudnick, Igor Wigman, *Almost sure GOE fluctuations of energy levels for
   hyperbolic surfaces of high genus*, arXiv:2301.05964,
   https://arxiv.org/abs/2301.05964 . Also opened the full HTML text. The limits
   include genus tending to infinity; the statistic is a smooth energy variance.
4. Matic Orel, *Perturbed quantum billiards on the hyperbolic plane*,
   arXiv:2607.03786, https://arxiv.org/abs/2607.03786 . This reports numerical
   spectral and eigenfunction statistics, not a proof of the limit.

No whole-problem resolution found within the under-ten-minute search. No paper
opened supplies the missing fixed-billiard nearest-neighbour limit. The update
is recorded here, not presented as the session's mathematical piece.
SOLVED_ELSEWHERE.md will distinguish the substantial related advance from
the unresolved fixed-system problem, as required by the requested convention.

**Choice, before proof work:** prove a finite-window, quantitative equivalence
between the nearest-neighbour law and the probability that a uniformly shifted
interval is empty. Use the actual leading Weyl unfolding, retain the measured
window density, and bound the artificial cyclic gap and physical window-edge
errors explicitly. This reduces the nearest-neighbour part of T089 to one
scalar empty-interval function, and gives a usable error budget without
claiming any chaotic billiard already satisfies it. Include a finite-grid
criterion and audit it on exact rational spectra.

Reason: the known smooth variance/form-factor statements are not empty-interval
estimates. This reduction identifies a precise missing statistic and avoids
silently differentiating a convergent sequence of functions without a bound.
It is an elementary reduction, not a claimed new universality theorem.

Priority preflight command:

```sh
env OMP_NUM_THREADS=1 nice -n 15 python3 -B -c 'import os; print("inherited_nice=", os.getpriority(os.PRIO_PROCESS, 0)); print("OMP_NUM_THREADS=", os.environ.get("OMP_NUM_THREADS"))'
```

Output (after the sandbox's `nice` warning):

```text
inherited_nice= 20
OMP_NUM_THREADS= 1
```

Thus computation already inherits a priority lower than the requested nice 15.

## Proof written — quantitative reduction and its sharpness

Created PROOF.md. The main finite-window bound, for N levels on a circle of
length W, density rho=N/W, target spacing CDF F, target integrated survival E,
and empty-function error delta on [0,S+h], is

```text
sup_[0,S] |F_internal-F| <= 1/N + (2*delta/h + omega_F(h) + |rho-1|)/rho.
```

The proof uses secants of a convex empty function, including a separate check
at s<h; it never interchanges a limit with a derivative. A finite mesh adds at
most its largest mesh width to delta. Nonwrapping and cyclic empty functions
differ by at most s/W. Weyl's law supplies rho -> 1 for the correct symmetry
sector coefficient.

An exact family relative to the uniform mean-one law on [0,2] has N even and
gaps (2j-1)/N, with the central 2k gaps collapsed to 1. Its gap CDF error is
k/N and empty-function error is (k/N)^2. This shows the square-root exponent
is optimal in this general class. It does not claim optimality specifically
for GOE, or that these artificial spectra come from chaotic billiards.

Next audit: exact rational arithmetic with a second geometric construction of
empty probabilities, direct CDF integration, exhaustive small configurations
including multiplicities, and the sharpness family. The proof is the result;
the computation will check finite identities and constants.

## First audit launch — platform limit failure, before any cases ran

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_reduction.py > audit_output.txt 2>&1
```

Exit status 1, before numerical work: macOS sandbox rejected
`resource.setrlimit(RLIMIT_AS, (768 MiB, 768 MiB))` with
`ValueError: current limit exceeds maximum limit`. A separate tiny diagnostic
reported inherited AS/DATA/CPU limits all equal to 9223372036854775807;
attempting to lower RLIMIT_DATA to 256 MiB was also rejected with the same
error. This is a platform resource-control failure, not a failed identity.

Replaced hard-limit calls with measured peak-RSS and elapsed-time guards
between fixed small cases (256 MiB and 120 seconds). The largest gap array has
128 entries, small cases stream one configuration at a time, and no numerical
library or worker thread is used. The report will state the actual RSS and
time rather than claiming an OS-enforced cap. The exact launch command above
will be rerun, writing its final output to audit_output.txt.

## First successful audit and a coverage gap found

The rerun completed with exit status 0. It checked 455 exact rational
configurations, including repeated levels; 11,375 geometric empty-probability
identities, 11,375 integrated-CDF identities, 11,375 right-derivative identities,
10,920 physical window-edge bounds, 11,375 cyclic-gap CDF bounds, 12,285 sampled
theorem inequalities, and 1,365 grid certificates. Both edge constants were
attained. All 17 sharpness cases gave `CDF_error^2 = empty_error` exactly.
Runtime was 1.298 seconds; measured peak RSS was 15,171,584 bytes; nice was 20.

Self-review found that the exhaustive configurations only had density below
one, and many of their theorem bounds were larger than one. Added a separate
audit with densities on both sides of one and with small errors giving
nonvacuous bounds. It checks the full CDF supremum at every jump and both
one-sided limits, rather than just test thresholds. This addition warrants
one final rerun of the same exact command.

## 21:04 — Final mathematical audit passed

Final command (exit status 0):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_reduction.py > audit_output.txt 2>&1
```

Exact captured output:

```text
nice: setpriority: Operation not permitted
All exact rational checks passed.
{"counts": {"configurations": 455, "cyclic_gap_cdf": 11375, "edge_bound": 10920, "grid_certificate": 1365, "integral_identity": 11375, "right_derivative": 11375, "theorem_bound": 12285, "void_geometry": 11375}, "max_cyclic_gap_bound_ratio": "1", "max_edge_bound_ratio": "1"}
Sharpness cases: 17; all D^2 = delta exactly.
{"cases": 120, "cdf_supremum_checked_at_all_jumps_and_both_limits": true, "density_above_one_cases": 48, "density_below_one_cases": 48, "internal_bound_less_than_one": 45}
{"large_cyclic_gap_checked": true, "one_over_N_boundary_constant_attained": true, "wrong_density_detected": true, "zero_gaps_checked": true}
{"OMP_NUM_THREADS": "1", "elapsed_guard_seconds": 120, "elapsed_seconds": 2.628, "nice": 20, "os_hard_memory_cap": false, "peak_rss_bytes_macos": 15974400, "rss_guard_bytes": 268435456}
```

Independent derivations and attempted breaks:

- Empty lengths were computed both as sums of gap hinges and by partitioning
  the starting-position domain at geometric events and integrating occupancy.
- The same empty function was recomputed by integrating the empirical survival
  CDF. Its right derivative was checked with exact one-sided difference
  quotients, including at jumps and at zero.
- Small-configuration counts are independently 21+56+126+252=455, using
  combinations with repetition. Multiplying by 25, 24, 27, and 3 gives
  11,375, 10,920, 12,285, and 1,365 respectively. The extended design has
  3*2*5*4=120 cases, including 48 on each side of density one.
- Sharpness errors were computed by exact extremization on every hinge-free
  interval. Independently, the removed positive odd gaps sum to
  (1+3+...+(2k-1))/N^2=k^2/N^2 at s=1. For N=128,k=1 the errors are exactly
  1/128 and 1/16384. This refutes a proposed linear-in-delta error rate.
- Explicitly included coincident levels, zero gaps, a huge cyclic gap, physical
  endpoints, and a wrong unfolding density. Density and endpoint terms cannot
  simply be omitted. No bound on the maximal physical gap was assumed.
- Checked the density term's sign algebraically for rho above and below one;
  the initial below-one-only coverage was repaired in the extended audit.
- Checked the h-neighbourhood of zero separately: a centered secant is not
  available there. F(0)=0 and the one-sided secant supply the bound.
- The sharpness example concerns a uniform target; it does not prove sharpness
  for GOE. The reduction concerns a spacing marginal, not all local spectral
  correlations. No fixed chaotic spectrum was computed or proved universal.

Created SOLVED_ELSEWHERE.md for the related literature advance and REPORT.md
with the partial verdict and remaining spectral task. No external writes,
git operations, publication, large computation, or subagents were used.

## Final artifact check

A separate `env OMP_NUM_THREADS=1 nice -n 15 python3 -B -` read-only check
loaded audit_data.json, recomputed the configuration count as
`sum(comb(5+n,n) for n in range(2,6))`, and independently verified
`Fraction(cdf_error)**2 == Fraction(empty_error)` in all 17 saved rows. It
checked that the seven deliverable files exist and are nonempty and that
REPORT.md starts with `VERDICT: PARTIAL `. Output:

```text
Final artifact and independent count checks passed.
```

Exit status 0. The exact numerical audit's reproducible command and complete
output are above; this final check made no numerical or proof changes.
