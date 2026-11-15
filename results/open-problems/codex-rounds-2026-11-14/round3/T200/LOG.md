# T200 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session: 15 November 2026, about 01:38 Asia/Tbilisi (UTC+04).

## 1. Orientation and literature check (01:38–01:40)

Read the earlier REPORT.md, PROOF.md, LOG.md, optimize_layers.py, and
verify_certificate.py from `~/codex_op_1114/briefs/T200`.
That directory remains read-only. Read the startup memory index and brain
navigation index. The task-specific restriction to writes in this folder
supersedes global checklist, mesh, and memory writes; none of those tools is
being run. No git or subagents. Initial local work product: PROMPT.md only.

Compute-state read: `warn`, `owner_away_open`, CPU saturation; no substantial
compute is needed. All numerical scripts will be standard-library, one thread,
under `OMP_NUM_THREADS=1 nice -n 15`, with a 60-second CPU limit and measured RSS.

Web searches, completed within five minutes, included `"Brownian intersection
exponents" "2026" exact Liu`, `"2609.18643" "Remark 1.2"`, `"Brownian
intersection" "2611"`, and searches for October/November 2026. Opened:

* Runsheng Liu, *An explicit lower bound for the growth exponent of
  three-dimensional loop-erased random walk*,
  https://arxiv.org/abs/2609.18643 and
  https://arxiv.org/html/2609.18643v1.
* Qiyuan Shi, Runsheng Liu, Xinyi Li, Ming Li, and Youjin Deng,
  *Intersection Exponents of Simple Random Walks in Two and Three Dimensions*,
  https://arxiv.org/abs/2609.25968.
* Yifan Gao, Xinyi Li, Yifan Li, Runsheng Liu, and Xiangyi Liu,
  *A boundary Harnack principle and its application to analyticity of 3D
  Brownian intersection exponents*, https://arxiv.org/abs/2411.14921.

No later exact evaluation was located. All three abstract pages still show
only v1. Liu's full paper, Remark 1.2, states a bound below 0.999 but omits its
proof; the detailed argument requested by the previous worker is not there.
This limited search cannot establish that no other result exists.
No SOLVED_ELSEWHERE.md is warranted.

## 2. Re-check of the earlier result

Independently reconstructed the Green lower bound as
`1/3 - 3/11 = 2/33`. The radial Gaussian integral is
`sqrt(2/pi)/sqrt(|u-v|)`; integrating the lag gives `(8/3)*sqrt(2/pi)/sqrt(t)`.
At `t=r^2/18` this is `16/(r sqrt(pi))`. The exponential-submartingale exit
bound is `6 sqrt(6) exp(-15/2)`. These reproduce the previous proof's capacity
estimate. Its layer variables are measurable before the next layer begins;
iterated conditioning suffices, and no independence is assumed. The test path
may return inward without invalidating its first-hitting-time decomposition.
The exponent comparison has the correct sign. No mathematical defect found.
An independently written rational/Decimal audit will check the numbers before
using this result as a baseline.

## 3. Choice of one extension, recorded before calculation

Prove a conditional exponential-moment estimate for normalized Brownian-segment
capacity, replacing the good/bad indicators. This is the previous report's
named next lemma. For the unrestricted time occupation energy `I`, the
variational definition gives `C >= 1/(r I)` on the event that the segment lasts
at least `t`. The elementary inequality `exp(-s/y) <= y/(e s)` for `y>0`
then bounds `E exp(-s C)` by the short-segment probability plus
`E(r I)/(e s)`. This keeps more capacity information than the binary threshold.

Candidate simple parameters: retain radii `r,2r,3r`, time `r^2/18`, take
Laplace parameter `s=30`, and aim for `E exp(-30 C) < 3/25`. A Chernoff bound
at average capacity `1/30` would give a lower-tail decay faster than `3^-N`.
If verified, the old hitting lemma would then yield
`xi_3(1,1) <= 1 - 1/(495 log 3)`. These are candidates until the audit and
full probability argument are completed.

## 4. Independent baseline computation (01:45 approximately)

Wrote `audit.py` independently of the earlier scripts. Its baseline mode uses
an inscribed regular 48-gon to certify the needed lower bound on pi (different
from the previous Machin certificate), exact fractions for the probability
rounding, the integer Chernoff comparison, and a direct power series for
`-log(1-h)`. Decimal arithmetic with a separately calculated Machin pi checks
the resulting constants.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline`

Output:
```
nice: setpriority: Operation not permitted
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
old_failure_upper=0.12548008032735818538811938659966944146615701662843169254167555136
old_tail_exponent=1.0035659415129856921602178536728326981342316053916120313827874227
old_gap_interval=[0.00016142418987595458293403859103411681765706063692248333460390165726, 0.00016142418987595458293403859103411681765706063692248333460390174493]
old_xi_upper=0.99983857581012404541706596140896588318234293936307751666539609826
EARLIER RESULT VERIFIED independently
peak_RSS_bytes=14925824
```

Result: the earlier claim holds. The `nice` warning comes from an inherited
nice 20; the script checks the actual priority through libc before computing.
That priority is lower than requested. Runtime was below one second and RSS
below 15 MiB. No earlier script was executed, so no output files could be
written in the earlier directory.

## 5. Capacity-moment certificate

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py moment`

Output:
```
nice: setpriority: Operation not permitted
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
polygon_pi_lower=1962/625
e_interval=(65/24, 1631/600)
rational_laplace_upper=68779/573480
rational_margin_below_3_over_25=193/2867400
unrounded_laplace_bound=0.11882397959491679859365706052605204104230302704513846859297204064
certified_tail_base=33/100
certified_tail_exponent=1.0091482099346311275441546293108735776720744883949158736097976672
delta_interval=[0.0018388671244986614012408892237093070719447193075862863529824284107, 0.0018388671244986614012408892237093070719447193075862863529824284176]
xi_upper=0.99816113287550133859875911077629069292805528069241371364701757159
coarse_xi_upper=1087/1089 < 99817/100000
ALL CAPACITY-MOMENT CERTIFICATE CHECKS PASSED
peak_RSS_bytes=15106048
```

The new conditional estimate is `E[exp(-30 cap(K(r))/r) | F_sigma_r] < 3/25`.
For `T_N=sum_j cap(K(3^j))/3^j`, it implies
`P(T_N < N/30) <= (33/100)^N`. The tail exponent is above one, as required
when comparing with the exact second-moment exponent. The proposed exponent
gap is about 0.001838867. Decimal logarithms and a separate libm evaluation
agree with an exact rational logarithm interval. All certification assertions
use rational/integer arithmetic. Runtime below one second; RSS below 15 MiB.

The key inequality was checked in two forms: with `x=s/y`, it is
`x exp(-x) <= 1/e`, whose derivative has its unique maximum at `x=1`;
equivalently `exp(-s/y)/y` is maximized at `y=s`. On the short-segment event
only the bound by one is used. On its complement, the unrestricted occupation
measure lies in the stopped segment. No independence between its energy and
the exit event is used, and the energy may involve future increments beyond
the segment on the short-segment event, where it is not needed.

## 6. Resumption and final audit (03:31–03:35)

Resumed the interrupted work from the local LOG.md, PROOF.md, and audit.py;
no REPORT.md had yet been written. Re-read all requested earlier files and
the current proof and script. The startup memory and current compute state
were read without writes outside this folder. Compute state remains `warn`,
`owner_away_open`; only subsecond standard-library arithmetic is planned.

The fresh literature check took under five minutes. Opened the full HTML
papers 2609.18643v1 and 2609.25968v1 and the abstract page of 2411.14921.
Searches used `"Brownian intersection" "2026" exact three dimensional exponent`,
`"2609.18643" "2609.25968"`, and
`"three-dimensional" "intersection exponents" "2611"`.
No subsequent exact evaluation was found. This is a limited negative search.
The source author lists agree with those recorded above. Continue the same
chosen extension, the conditional capacity exponential moment; no second
extension is being substituted. An initial append patch found no matching
context and made no change; the corrected patch succeeded.

Repeated the independent commands after resumption:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py moment
```

Both exited zero, in under one second. The baseline again printed
`EARLIER RESULT VERIFIED independently`,
`old_xi_upper=0.99983857581012404541706596140896588318234293936307751666539609826`,
and `peak_RSS_bytes=14893056`. The moment mode again printed
`ALL CAPACITY-MOMENT CERTIFICATE CHECKS PASSED`,
`rational_laplace_upper=68779/573480`,
`rational_margin_below_3_over_25=193/2867400`,
`certified_tail_base=33/100`,
`certified_tail_exponent=1.0091482099346311275441546293108735776720744883949158736097976672`,
`xi_upper=0.99816113287550133859875911077629069292805528069241371364701757159`,
and `peak_RSS_bytes=14761984`. Actual nice was 20 in both runs;
`OMP_NUM_THREADS=1` and the 60-second CPU limit were checked by the scripts.
The shell's `nice` warning does not mean a higher-priority run occurred.

## 7. Attempts to break the proof

Re-derived the Green minimum with the image formula at opposite radial
directions: for normalized radii `u<=1`, `v<=2`, its value is
`1/(u+v)-3/(9+uv)`. Its derivative in either variable is negative:
`9+uv>3(u+v)` and `sqrt(3v)<3` (and the analogous inequality in u).
Thus the minimum is `1/3-3/11=2/33`, agreeing with the distance-and-A proof.
The energy has an independent scaling check: at unit time the lag integral is
`2 integral_0^1 (1-v)/sqrt(v) dv=8/3`; Brownian scaling multiplies it by
`t^(-1/2)`. At `t=r^2/18` this is `16/(r sqrt(pi))`.

Checked the central scalar estimate in two ways: maximizing `z exp(-z)`
gives `1/e`; differentiating `exp(-s/y)/y` gives a unique maximum at `y=s`
with value `1/(e s)`. In particular the direction of the energy-to-capacity
inequality is correct. Multiplying capacity by r, rather than dividing,
would fail Brownian scaling; the proof consistently uses `cap(K)/r` and
`r I_t`. The tail constant has an exact second check: `(33/100)^N` is smaller
than `3^(-N)` since `3*33=99<100`. Its logarithmic exponent is independently
evaluated by Decimal. The gap is `(2/33)*(1/30)/log(3)`, agreeing with both
the rational interval and the separate libm calculation in audit.py.

Checked zero capacity, a test starting position in the obstacle, coincident
Green points, the last layer, inward returns of the test path, and noninteger
thresholds. On a short segment the occupation measure can leave K: the proof
then uses only the bound by one. Elsewhere the measure is supported on K.
No conditional energy expectation given a long segment is substituted.
Likewise, the capacity sum uses successive conditional expectations, not an
independent-layer assumption. Conditioning on the full obstacle path causes
no dependence in X, which is an independent Brownian motion. Increasing R
enlarges both traces in the avoidance event, so the moment interpolation from
integer log-radii is valid. Subtracting the exceptional tail uses b>1 and
the second-moment exponent exactly one; using a tail exponent below one
would invalidate the conclusion. No unresolved mathematical defect was found.

The requested detailed argument behind Liu's Remark 1.2 could not be obtained
from the opened paper: the remark omits it. No claim of priority or a best
known bound is justified by this five-minute search. The current result is
the checked capacity-moment lemma and its explicit consequence beyond the
previous report. No exact exponent is determined.

## 8. Final deliverable

Wrote REPORT.md with `VERDICT: PARTIAL`, the checked bound below 0.99817,
the new conditional exponential-moment lemma, reproduction commands, limits
of the literature check, and a concrete next step using weighted occupation
measures. An attempted log append had a mismatched context and changed
nothing; the corrected append succeeded. Final readback confirmed the exact
verdict prefix and the presence of REPORT.md, PROOF.md, LOG.md, and audit.py.
The earlier directory was read only throughout. There were no git
operations, external writes, agents, simulations, or large computations.
