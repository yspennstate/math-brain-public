VERDICT: COMPUTED circuit mismatch costs in 120 finite conditioned triangular-percolation configurations

The values of d_s and d_w remain unidentified. The bounded literature check
found no later solution. The opened paper by Irina Đanković, Maarten Markering,
Jason Miller, Yizheng Yuan, *The scaling limit of random walk and the intrinsic
metric on planar critical percolation*,
[arXiv:2604.14122](https://arxiv.org/abs/2604.14122), still lists only v1.
Corollaries 1.3–1.4 give d_w=91/48+beta_res and
d_s=2(91/48)/(91/48+beta_res), with beta_res unidentified. Nothing here
decides whether beta_res=91/96, equivalently d_s=4/3.

The round-4 result holds. A fresh exact rational solver checked all 3,600
square-interface cases (656 equality cases, 240 zero corrections), all 1,222
weighted circuit demands, and five obstruction-family values. The main
claim was also re-derived: local wired optima vanish on circuit edges;
disjoint circuit repairs therefore have energy exactly A+C and give
0<=R_full-A<=C. Earlier folders were read without alteration.

New beyond round 4: the proposed quantities have now been computed in the
same actual finite percolation configurations, with saved open sites, ordered
circuits and reproducible selection. At each radius R=12,24,48, accept 40
critical triangular-lattice site configurations conditioned on connection
from the open origin to the hexagonal radius-R boundary. All open components
are retained; a measured layer can have as many as 207 components. Selection
uses planar face walks and no electrical data. The full resistance, local
wired sum A, repair cost C, circuit lengths, mismatch total variations and
cumulative-current variances are saved separately.

The first search in two narrower annuli found zero circuits in all 120
configurations. Its outputs are preserved as thin_*. The following table
uses a disclosed exploratory revision: replay the same configurations with
annuli [1,floor(R/4)] and [floor(R/4)+1,R-1]. No extra rejection is imposed.

| R | Accepted samples | Samples with one circuit | With two | Median C/A, given a circuit | Maximum C/A |
|---|---:|---:|---:|---:|---:|
| 12 | 40 | 3 | 0 | 0.1240 | 0.2935 |
| 24 | 40 | 8 | 0 | 0.1111 | 0.5660 |
| 48 | 40 | 11 | 0 | 0.1208 | 0.6665 |

Thus there are 22 nontrivial one-interface measurements, no sampled
two-interface decomposition. Circuit lengths range from 6 to 73. Across
these circuits, the coarse bound length*TV^2/4 exceeds actual repair energy
by factors 1.81–6.87, median 2.79. These are descriptive finite observations,
with small circuit-containing subsets; they provide no exponent estimate.

The numerical checks use a potential-based resistance lower bound and an
explicit feasible flow for an upper bound, obtained by routing the Kirchhoff
residual on a spanning tree. The repaired global flow is checked separately
for conservation and energy A+C. Floating bound differences reach machine
roundoff and are not rigorous outward-rounded interval certificates.
Independent exact rational solves recompute R, A, profiles and C for all
three nontrivial radius-12 samples, agreeing within 1e-9 and verifying
0<=R-A<=C exactly. For example, sample 12-017 gives
R=2.07159909745, A=1.85409026082, C=0.544263769093.

The independent audit reproduces every random bit and rejected proposal,
checks all 480 thin/wide annulus outcomes by closed-site radial crossings,
checks every sampled circuit split by flooding the triangular-face dual,
and compares the selector with explicit simple-cycle enumeration on 256
small random annuli. All pass. CSV-based counts, extrema and medians are
recalculated independently. Exact sample fractions are in sample_audit.json.

Commands, from this folder, each with
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1`
prefixed:

```sh
nice -n 15 python3 -B recheck_previous.py
nice -n 15 python3 -B sample_percolation.py --replay thin_configurations.jsonl
nice -n 15 python3 -B audit_samples.py
```

To generate the final ensemble anew from its fixed seed, run
`sample_percolation.py` without --replay under the same environment. To
reproduce the initial narrower search, use --thin; its default-named outputs
must be preserved before rerunning, as recorded in LOG.md.

All successful runs use one process and the Python standard library.
Inherited nice 20 was checked despite the nice command's setpriority warning.
The sampling replay took 94.94 seconds and peaked at 41.22 MB RSS; the
independent audit took 7.52 seconds and peaked at 92.93 MB. CPU/wall caps
are 1100/1180 seconds. Nothing approached 1 GB or 20 minutes.

What failed: the first annulus choice produced no useful gluing data. The
second still produced no two-circuit sample. An initial independent geometry
checker omitted boundary triangles whose anchors lie outside the ball; its
anchor range was corrected, and the complete audit then passed. This did
not change sampling or measured values. No electrical or mathematical
assertion failed after that checker repair.

What remains uncertain: no large-scale behavior of C/A, no IIC-law tail
estimate, no accumulation control across several interfaces, and no exponent
for A. The wider inner search is not at fixed annular aspect ratio, and
finite conditioning at these radii cannot be substituted for the infinite
IIC. Small observed C/A values do not establish a subpolynomial bound.

Next worker: first specify a circuit rule allowing several interfaces,
then obtain a finite conditioned ensemble with a substantial number of
two-or-more-circuit realizations. Keep the zero/one-circuit cases in its
record. The present face-walk selector is complete for existence within its
annulus, so circuit frequency, rather than undetected circuits, is the
identified limitation at these scales. One option is to expose all enclosing
face-walk cycles in B_(R-1), then select a disjoint nested subsequence by a
fixed geometric rule; document its scale distribution before comparing C/A.
Use the saved configurations for a pilot and retain the exact small-sample
audit. The eventual target remains C<=R^{o(1)}A jointly with an identified
exponent for A; no evidence here establishes that target.

Task: “take the NEXT checkable step on this problem, building on that work” —
15 November 2026, 08:21 Asia/Tbilisi.
