VERDICT: COMPUTED circuit mismatch costs in 49 two-interface finite percolation measurements

The values of d_s and d_w remain unidentified. The bounded literature check
found no later solution. The opened paper by Irina Đanković, Maarten
Markering, Jason Miller, Yizheng Yuan, *The scaling limit of random walk
and the intrinsic metric on planar critical percolation*,
[arXiv:2604.14122](https://arxiv.org/abs/2604.14122), still lists only v1.
Corollaries 1.3–1.4 give d_w=91/48+beta_res and
d_s=2(91/48)/(91/48+beta_res), with beta_res unidentified. Nothing here
decides beta_res=91/96 or d_s=4/3.

The earlier result holds. Its independent audit reproduced all 120
configurations, all rejected proposals, 480 thin/wide annulus checks, 22
circuit partitions, 256 small brute-force cycle checks and all three
nontrivial exact R=12 solves. The deterministic bound

    0 <= R_full-A <= C,    C=sum_i Q_Ci(delta_i)

also re-derives from circuit repairs with disjoint supports and zero local
wired current on their edges. Earlier folders were only read.

New beyond round 5: a whole-disk outward peeling rule now gives actual
multi-interface percolation measurements. In the open induced graph of
B_(R-1) excluding the origin, extract enclosing simple cycles by splitting
face walks. Select minimum enclosed area among those candidates, with
canonical lexicographic ties; delete its interior and boundary vertices
from the selection graph, then repeat. This uses no electrical data and
produces vertex-disjoint nested circuits. It need not maximize their number.
All open components remain in the electrical network.

On the SAME 120 saved configurations, peeling finds 38 circuits in 36
realizations, including two realizations with two circuits. The earlier
annular rule found no two-circuit sample. Pilot counts (zero, one, two)
are (34,6,0), (27,12,1), (23,16,1) at R=12,24,48. Maximum pilot C/A is
20.4312. Data and audits have the prefix pilot_.

The new all-case ensemble accepts 200 configurations per radius, seed
202611150652, conditioned only on origin-to-boundary connection. Every
accepted outcome receives an electrical solve:

| R | Samples | Zero circuits | One circuit | Two circuits | Median C/A given a circuit | Maximum C/A |
|---|---:|---:|---:|---:|---:|---:|
| 12 | 200 | 175 | 25 | 0 | 0.7183 | 5.5161 |
| 24 | 200 | 151 | 47 | 2 | 0.6967 | 38.5590 |
| 48 | 200 | 130 | 66 | 4 | 0.8124 | 34.5657 |

This gives six two-interface realizations and 150 circuits. The largest
layer has 279 components; none are dropped. Data have the prefix ensemble_.

Because six cases were few, a separate census fixes 2,000 accepted R=48
configurations with seed 202611150700. It retains EVERY configuration and
its circuit count, including 1,423 zero-circuit and 536 one-circuit cases.
All 41 remaining configurations have two circuits; none has three. Only
these 41 receive electrical solves in this census. Thus its electrical
statistics explicitly condition on k>=2; they do not estimate unconditional
electrical moments. The pilot, all-case ensemble and census remain separate.
The fixed sample size and electrical allocation were recorded before this
census began, and sampling did not stop upon reaching a circuit target.

For these 41 two-interface cases:

| Quantity | Minimum | Median | Maximum |
|---|---:|---:|---:|
| C/A | 0.09399 | 2.41487 | 48.58400 |
| R_full/A | 1.04186 | 1.95322 | 8.99846 |
| (R_full-A)/C | 0.11291 | 0.30899 | 0.52999 |

The maximum-C/A case, survey sample 48-1290, independently recomputes to
R=7.77604833869, A=1.04721479318, C=50.8778788636 by exact rational
arithmetic. Thus substantial circuit repair costs occur in these finite
configurations, and the circuit-only upper bound can exceed the actual
correction considerably. These numbers give no exponent estimate.

Circuit geometry limits their interpretation. In the all-case ensemble,
140 of 150 circuits have minimum radius at most 2. In the census this is
542 of 618 circuits; among its measured two-interface cases it is 62 of
82. Those 82 measured circuits have lengths 6–399 and median maximum
radius 12. The rule imposes nesting but no fixed annular aspect ratio or
scale separation. No sample has three interfaces, so there is no test of
accumulation over a growing circuit sequence.

Independent audits reproduce all random proposals, check cycle existence
and termination by triangular-face dual connectivity, and check every
selected circuit's vertex/edge partition by a separate dual flood. There
are 158, 750 and 2,618 existence/termination checks in the pilot, ensemble
and census. CSV geometry, cumulative-current variance, coarse cost and
reported quantiles are checked separately. A fresh sparse rational
prescribed-current solver agrees with dense unit-voltage solves on ten
small networks. It recomputes selected multi-interface samples, the census
maximum-C/A case, and every per-radius maximum C/A in the pilot and
all-case ensemble. All exact inequalities pass; R,A,C agree with stored
floating values within 1e-9. Fractions are in the *_audit.json files.
Floating bounds on the remaining samples are diagnostic, not rigorous
outward-rounded interval certificates.

Commands, run here with
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1`
exported, are:

```sh
nice -n 15 python3 -B audit_samples.py
nice -n 15 python3 -B peel_circuits.py --replay configurations.jsonl
nice -n 15 python3 -B peel_circuits.py --samples 200 --seed 202611150652 --prefix ensemble
nice -n 15 python3 -B audit_peeling.py pilot
nice -n 15 python3 -B audit_peeling.py ensemble
nice -n 15 python3 -B survey_multiple.py
nice -n 15 python3 -B audit_survey.py
nice -n 15 python3 -B audit_outliers.py
nice -n 15 python3 -B summarize_results.py
```

Complete commands and relevant outputs are in LOG.md and the saved .stdout
files. Census configurations are compressed in survey_configurations.jsonl.gz;
survey_census.csv includes every outcome, while survey_samples.csv and
survey_circuits.csv contain the explicit k>=2 electrical subset. Every run
used one standard-library process. All verified inherited nice 20 despite
the nice command's setpriority warning. Maximum peak RSS was 199.8 MB;
longest run was 412.35 seconds. CPU/wall caps were at most 1100/1180 s.

What failed: 200 samples per radius supplied only six multi-interface
cases, so the separate census was needed. Peeling does not solve circuit
scale selection; many circuits approach the origin. No mathematical or
executed numerical assertion failed. A pre-audit boundary-case review fixed
handling of undefined D/C when C=0 without changing any measurements.

What remains uncertain: no IIC-law tail estimate, no almost-sure
C_R<=R^{o(1)}A_R bound, no identified exponent for A_R, and no comparison
of this finite conditional subset with the infinite IIC. Neither the large
outliers nor the smaller medians establish or refute a subpolynomial bound.

Next worker: use the saved 2,000-configuration census to test a circuit
rule with controlled radial separation before doing more electrical work.
For example, fix annuli [r,4r] and [8r,32r], enumerate the available r with
32r<R, and record all zero/one/two outcomes. Count viable two-interface
cases first, then compare their A,C,R on the same configurations with the
present peeling measurements. Keep the exact outlier audit. The eventual
target remains a justified IIC estimate for C/A jointly with an exponent
for A; more interfaces near the origin alone will not supply it.

Task: “take the NEXT checkable step on this problem, building on that work” —
15 November 2026, 10:52 Asia/Tbilisi.
