# T200 work log

Task: “push this problem forward by one checkable piece.” Session began 14 November 2026, about 22:05 Asia/Tbilisi (UTC+04).

## 1. Orientation and scope (22:06)

Read the supplied task, the local directory listing, the startup memory index, the compute-state file, and the mesh protocol. The later task-specific instruction permits writes only in this folder; consequently no global checklist, mesh database, recall logs, or brain memories are being changed. No git and no additional agents.

Initial files: PROMPT.md, codex.log, run.pid. No mathematical work products existed.

The compute state reports `warn`, CPU saturation, `owner_away_open`. No simulation is planned. Shell work now uses `OMP_NUM_THREADS=1 nice -n 15 ...`. The first such invocation reported `nice: setpriority: Operation not permitted` but completed. This will be investigated before any computation; no heavy program will run.

The initial web search opened arXiv:2411.14921 and searched:

* `"Brownian intersection exponents" "2026"`
* `"2609.18643"`
* `"2609.25968"`

Results identify the two September papers in the brief, an earlier May loop-soup paper, and no exact evaluation. These are preliminary search results, not a proof that no subsequent work exists. The literature check continues, capped at ten minutes.

## 2. Literature follow-up

Opened the arXiv abstract pages of 2609.18643 and 2609.25968, then their full HTML papers, and the full PDF of 2411.14921 (49 pages). The attempted HTML of 2411.14921 timed out; its PDF succeeded. Additional searches used October/November 2026, `2610`, `2611`, and `solved` with the Brownian intersection terminology. No later exact evaluation or substantial advance beyond the brief was located. This limited search does not certify absence.

Primary sources opened:

* Yifan Gao, Xinyi Li, Yifan Li, Runsheng Liu, and Xiangyi Liu, *A boundary Harnack principle and its application to analyticity of 3D Brownian intersection exponents*, https://arxiv.org/abs/2411.14921 and https://arxiv.org/pdf/2411.14921.
* Runsheng Liu, *An explicit lower bound for the growth exponent of three-dimensional loop-erased random walk*, https://arxiv.org/abs/2609.18643 and https://arxiv.org/html/2609.18643v1.
* Qiyuan Shi, Runsheng Liu, Xinyi Li, Ming Li, and Youjin Deng, *Intersection Exponents of Simple Random Walks in Two and Three Dimensions*, https://arxiv.org/abs/2609.25968 and https://arxiv.org/html/2609.25968v1.

Shell diagnostic `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'ps -o pid,ppid,ni,comm -p $$ -p $PPID; ...'` could not inspect scheduling: `nice: setpriority: Operation not permitted`; `ps` was also denied. Resource limits will be enforced inside any computation, and its actual inherited niceness checked using Python if possible. No heavy work is authorized by this limitation.

## 3. Choice, before doing the mathematics

Choose one piece: sharpen the explicit numerical upper bound on `xi_3(1,1)` by proving and optimizing a parameterized version of the capacity/layer argument in Liu, Sections 2–4. His proof uses several deliberately rounded constants and an elementary union bound. Replace the union bound by a conditional Chernoff bound, allow different annulus ratios and capacity thresholds, and produce one fully certified rational parameter choice. The aim is a modest rigorous bound, not an exact value. If the improvement does not exceed the stronger bound mentioned without proof in his Remark 1.2, state that limitation explicitly.

Why this piece: it reduces to explicit Green-function and Gaussian estimates, a finite parameter calculation, and an elementary exponential-moment argument. It can be checked without Brownian simulation or trusting numerical exponent fits. The literature check has ended within the ten-minute cap. No solved-elsewhere file is warranted.

The first Python scheduling/limit diagnostic was wrapped in `OMP_NUM_THREADS=1 nice -n 15 python3 -B -c ...`. It failed before any computation: setting a 512 MiB `RLIMIT_AS` raised `ValueError: current limit exceeds maximum limit`. This is a portability issue to resolve; the run did no mathematical calculation and produced no data.

## 4. Parameter search setup

The libc diagnostic returned `getpriority 20 errno 0`, and `OMP_NUM_THREADS 1`. Thus the inherited process already has lower scheduling priority than nice 15. The wrapper's attempt to add another 15 fails, but the launched process retains nice 20. No attempt is made to raise its priority.

Wrote `optimize_layers.py`, a deterministic 187,264-point search of an explicit five-parameter bound. Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B optimize_layers.py`. Its first run stopped in the resource guard, before the search: preserving the reported INT64_MAX hard-limit sentinel while lowering the soft limit was rejected. Revised the guard to lower both CPU and RSS limits to finite values (60 seconds and 256 MiB). No mathematical output from the failed run is used.

## 5. Search completed

The second guard attempt also stopped before searching: the macOS RSS limit cannot be set here. Kept the working 60-second CPU limit, checked inherited nice 20, and report measured peak RSS. The actual program uses constant working memory and no numerical libraries or worker threads.

Successful command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B optimize_layers.py`.

Output that matters (full parameter data in `layer_search.json`):

```
niceness=20; OMP_NUM_THREADS=1; CPU limit=60s
evaluations=187264
best: a=2, b=3, t=1/18, c=13/1000, q=9/40
p=0.1254800803273582
exit_bound=0.008128646949424879
green_min=2/33=0.06060606060606061
hit_bound=13/16500=0.0007878787878787878
tail_exponent=1.0063610384887713
delta=0.00016142418987595455
original_published_delta=0.00010021499569435554
peak_RSS_bytes=15204352
```

Runtime reported by the shell tool: about 0.035 seconds. The wrapper again warned that it cannot add 15 to the inherited niceness; the script independently verified nice 20. The RSS hard-limit warning is retained in the output. The observed memory is under 16 MiB.

The search suggests the rational parameters above. The exact proof will replace the floating-point failure probability by `p < 63/500` and certify the tail exponent by integer arithmetic. This gives a slightly sharper proved constant than Liu's displayed theorem, but is weaker than the `xi < 0.999` mentioned without proof in his Remark 1.2. It must not be described as a new best bound.

## 6. Proof and exact certificate

Saved `PROOF.md` with the full capacity/layer argument for the rational parameter choice. It works directly with the starting points in the task, so no equivalence with uniform starting distributions is required. It uses existence of the moment limits and `xi_3(1,2)=1`; no analyticity or asymptotics up to multiplicative constants are used.

Saved and ran `verify_certificate.py`. Exact command:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_certificate.py
```

Complete output:

```
nice: setpriority: Operation not permitted
niceness=20; OMP_NUM_THREADS=1; CPU limit=60s
{
  "exact_checks": {
    "exp_7.5_partial_sum_gt_1800": true,
    "pi_lower_gt_1.77_squared": true,
    "exp_1.1_partial_sum_gt_3": true,
    "failure_probability_rational_margin": "9/59000",
    "chernoff_integer_lhs": "547010220251476124397111231170616570028274940518068764654445004214067781178609806147505878470838069915771484375",
    "chernoff_integer_rhs": "467670505444162168362384536873007779435313343240984293695715812427369445419728639884309520617031548403737165824",
    "chernoff_integer_difference_positive": true,
    "green_constant_two_ways": "2/33",
    "hit_probability": "13/16500",
    "delta_coarse_lower_bound": "39/242000",
    "delta_coarse_margin_above_1_over_6250": "7/6050000",
    "chernoff_log_series_margin_positive": true
  },
  "decimal_crosscheck": {
    "exit_failure_bound": "0.0081286469494248777029188606750287436105944857279999303181057212510",
    "expected_energy_times_r": "9.0270333367641005911692712249723613857321860930263912198774379623",
    "failure_probability_bound_before_rounding": "0.12548008032735818538811938659966944162511290493734301617651241476",
    "rounded_failure_probability": "0.126",
    "chernoff_tail_exponent_with_rounded_p": "1.0035659415129856921602178536728326981342316053916120313827874227",
    "chernoff_log_margin": "0.0039175871668378330591749634766961063179885038141206719964527996",
    "log_margin_rational_lower": "0.0039175871668378330591747363385907549690370326651617759520783260706",
    "log_margin_rational_upper": "0.0039175871668378330591749664446222043222801773360516657101842709231",
    "delta": "0.00016142418987595458293403859103411681765706063692248333460390174477",
    "delta_rational_interval_lower": "0.00016142418987595458293403859103411681765706063692248333122576783577",
    "delta_rational_interval_upper": "0.00016142418987595458293403859103411681765706063692248416382828072310",
    "xi_upper_bound": "0.99983857581012404541706596140896588318234293936307751666539609826"
  },
  "peak_RSS_bytes": 15843328
}
ALL EXACT CERTIFICATE CHECKS PASSED
```

The verifier's rational comparisons are the proof certificate; the decimal output is an independent audit. The output is also saved as `certificate.json`. The run completed immediately and used under 16 MiB of RAM.

## 7. Attempt to break the argument

* Re-derived the minimum Green kernel both by separate distance/regular-part bounds and by putting the two points in opposite directions and differentiating in their radii. Both give `2/(33r)`; the two extrema in the first argument are simultaneously attainable.
* Re-derived the Gaussian inverse-distance integral from its radial density, and checked the time-energy constant using Brownian scaling and the single lag integral `2 integral_0^1 (1-v)/sqrt(v) dv = 8/3`.
* Checked the rounding of the bad-layer probability by rational exponential and arctangent series, then evaluated it again at high precision. Its actual bound is about 0.12548008, below the certified 0.126.
* Checked the Chernoff threshold two ways: an integer power comparison, and independently bounded logarithm series. The rounded tail exponent is about 1.00356594, still strictly above 1. The smaller margin after rounding, rather than the exploratory value, is used throughout the proof.
* Checked that no independence of good layers is assumed. Earlier bad events are measurable before the next layer starts; iterated conditional exponential-moment bounds are sufficient.
* Checked possible returns to smaller radii by the test path. Only successive first-hitting-time segments are constrained, and full avoidance implies each local event. No annular confinement or unjustified conditioning on future avoidance is used.
* Checked time-zero hits, zero-capacity sets, the last layer, equality at a capacity threshold, and noninteger `qN`. The inequalities cover all of them.
* Checked the passage from integer log-radii in the task to `R=3^N` by monotonic bracketing. The asymptotic comparison uses only the exponent limit; the discarded tail is negligible since its exponent exceeds 1.
* Checked sign and magnitude: the original displayed gap is about 0.000100215; the new certified gap is about 0.000161424. Thus the new upper bound is smaller, and it still does not reach 0.999. No claim of optimality over the continuous parameter space is supported by the finite grid.

## 8. Final audit (clock read: 22:14:48 UTC+04)

Read back the proof and the key claims using `rg`; checked file line counts. Expanded the Gaussian radial integral in the proof so its normalization is explicit. The first edit patch did not match the wrapped sentence and made no changes; a narrower patch succeeded. Intermediate section timestamps were estimates and have been removed; only the observed session clock readings are retained. No mathematical constants changed after verification, so no repeated computation was needed.

Final result: `xi_3(1,1) <= 1 - (9/(40 log 3)) log(16500/16487) < 0.99984`. The exact value and the general moment family remain unresolved. The reproducible artifacts are being summarized in `REPORT.md`.

## 9. Completed report

Saved `REPORT.md` with a PARTIAL verdict, the proved bound, both reproduction commands, the comparison with Liu's Remark 1.2, resource/guard failures, the audit, and a concrete next step. All numerical inequalities used in the proof are covered by the successful verifier run; the probabilistic and potential-theoretic argument is written out in PROOF.md and audited above. The final edits only expand exposition and record the result.

Final read-only command: `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'head -1 REPORT.md; ls -lh LOG.md PROOF.md REPORT.md optimize_layers.py verify_certificate.py layer_search.json certificate.json'`. It confirmed the first line `VERDICT: PARTIAL a fully checked explicit bound xi_3(1,1) < 0.99984` and the existence of all seven artifacts. No further computation or mathematical changes followed.
