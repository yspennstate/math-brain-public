# T200 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, 05:01 Asia/Tbilisi (01:01 UTC).

## Orientation and literature check

Read REPORT.md, LOG.md, PROOF.md and all mathematical Python scripts in both
earlier folders (`codex_op_1114/briefs/T200` and `codex_op_1114r3/briefs/T200`).
They remain read-only. Read the startup memory, brain navigation index, and
compute state. The task-specific restriction to writes in this folder takes
precedence over global mesh, checklist, recall-log and memory writes; those
commands are not run. No git, subagents, or external mutations.

The compute state is `warn`, `owner_away_open`, CPU saturated. Only small
standard-library arithmetic is planned, with OMP_NUM_THREADS=1, nice -n 15,
a 60-second CPU limit and measured RSS below 1 GB.

The web-tool literature check finished at 01:02 UTC, within five minutes.
Queries included `"Brownian intersection exponents" "2026" exact`, the two
September arXiv identifiers, and October/November 2026 exact-value searches.
Opened the abstract pages of all four papers below, and the full HTML of
the September papers. The HTML of 2411.14921 timed out; its abstract opened.

* Yifan Gao, Xinyi Li, Yifan Li, Runsheng Liu, and Xiangyi Liu,
  *A boundary Harnack principle and its application to analyticity of 3D
  Brownian intersection exponents*, https://arxiv.org/abs/2411.14921.
* Runsheng Liu, *An explicit lower bound for the growth exponent of
  three-dimensional loop-erased random walk*,
  https://arxiv.org/abs/2609.18643 and https://arxiv.org/html/2609.18643v1.
* Qiyuan Shi, Runsheng Liu, Xinyi Li, Ming Li, and Youjin Deng,
  *Intersection Exponents of Simple Random Walks in Two and Three Dimensions*,
  https://arxiv.org/abs/2609.25968 and https://arxiv.org/html/2609.25968v1.
* Yifan Gao, Ruixuan Li, and Xinyi Li, *Generalized intersection exponents
  and local cut points for three-dimensional Brownian loop soup*,
  https://arxiv.org/abs/2605.17494.

No later exact evaluation was located. The abstract pages show v1 only.
The May paper concerns generalized exponents, not an exact classical value.
This limited search does not certify absence or novelty. No solved-elsewhere
file is warranted.

## Re-check, before extension

Re-derived the Green minimum as 1/3-3/11=2/33. The inverse-distance Gaussian
mean is sqrt(2/pi)/sqrt(|u-v|), and the uniform time-energy integral is
2 integral_0^1 (1-v)/sqrt(v) dv=8/3. At t=r^2/18 this gives
E[r I_t]=16/sqrt(pi). The Gaussian maximal bound is
6 sqrt(6) exp(-15/2). On a long segment, capacity/r >=1/(r I_t);
on a short segment only exp(-s capacity/r)<=1 is used. The unrestricted
continuation causes no support problem. The successive capacity variables
are measurable before the next first hitting time, so conditional iteration
is valid. The exponent comparison discards a tail with exponent strictly
greater than the known second-moment exponent 1. An independent numerical
certificate will be run before choosing the extension.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline`.
Output (exit 0, under one second):

```
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
baseline_laplace_bound=0.11882397959491679859365706052605204104230302753817962651701661198
baseline_rational_laplace_upper=68779/573480
baseline_tail_exponent=1.0091482099346311275441546293108735776720744883949158736097976672
baseline_xi_upper=0.99816113287550133859875911077629069292805528069241371364701757159
ROUND 3 RESULT VERIFIED independently
peak_RSS_bytes=14499840
```

The shell warned `nice: setpriority: Operation not permitted`; actual nice
20 was independently checked through libc and is lower priority than nice
15. No unresolved defect was found in the earlier result.

## Choice of one extension, before its calculation

Choose the next step proposed by round 3: replace uniform time occupation by
a deterministic weighted measure and solve the expected-energy minimization
for the kernel |u-v|^(-1/2) on [0,1]. Carry one certified improved energy
constant through the same conditional capacity-moment and exponent argument.
Keep r-to-2r segments, factor-three layers, and time r^2/18 fixed, so the
change can be attributed to the weight. The candidate density is proportional
to [u(1-u)]^(-1/4). Its constant-potential identity and global minimizing
property need proofs, including endpoint and singular-energy issues.
This is an explicit analytic lemma; no path simulation is needed.

## Weighted energy calculation and first certificate attempt

The candidate's unnormalized potential splits into L(x)+L(1-x).
A positive binomial expansion gives
L(x)=(B(3/4,1/2)/4) integral_0^x [z(1-z)]^(-3/4) dz.
Reflection therefore makes the sum constant, equal at x=0 to
B(1/4,3/4)=pi sqrt(2). The normalized energy is
J=pi sqrt(2)/B(3/4,3/4). Positivity of the kernel on signed measures will
give the global minimizing property.

For certification, the positive half-interval series gives
B(3/4,3/4)=2^(1/4) S, with rational partial sums for S. The first 24 terms
already certify J<21/8 by fourth powers. This replaces 16/sqrt(pi) by
63/(4 sqrt(pi)) in the earlier energy bound. At Laplace parameter 29,
the rational bound is below 11/90. Since e<68/25, the tail base is
374/1125<1/3. The proposed new gap is 2/(957 log 3).

First command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py weighted`.
It exited 1 in a redundant numerical cross-check: the Machin pi interval
used only 30 terms, insufficient for the requested 1e-45 agreement with a
160-term independent beta series. Every preceding rational certificate
comparison passed. Increase the pi precision; no proof constant changes.

With 40 Machin terms the same command exited 0 in under one second:

```
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
beta_series_terms=24; beta_series_width=1.2203745169254616648814034024012246185021647971634773842776088383E-10
optimal_time_energy_J=2.6220575542921198104648395898911194136827549514316225522763489606
certified_J_upper=21/8
weighted_expected_energy_times_r=8.8760253575659166769324640731831586994246945881739455252057401959
uniform_expected_energy_times_r=9.0270333367641005911692712249723613735048100692639817095056888522
energy_reduction_fraction=0.01672841714045507107568515379083021986896689321314154289636913979
weighted_laplace29_bound=0.12072544861718008258582686855666652949233862753889114548443520832
uniform_laplace29_bound=0.12264106003096824414161355017608732716063780433193634922314386994
critical_laplace_for_threshold_1_over_29=0.12262648039048077386517459005382028914860371034392261150261226723
rational_laplace_upper=324643/2669160
rational_laplace_margin=4763/8007480
rounded_laplace_upper=11/90
certified_tail_base=374/1125
tail_margin_below_1_over_3=1/1125
certified_tail_exponent=1.0024305467756200899262394493210537665994956399258774895569486215
gap=0.0019022763356882704150767819555613521433910889388823651927404431836
xi_upper=0.99809772366431172958492321804443864785660891106111763480725955682
gap_ratio_to_round3=30/29
ALL WEIGHTED-ENERGY CERTIFICATE CHECKS PASSED
peak_RSS_bytes=14909440
```

The weighted expected energy is about 1.67% smaller. At threshold 1/29,
the uniform measure's unrounded estimate narrowly fails the required tail
test, whereas the weighted measure passes. The new certified exponent gap
is 30/29 times the round 3 gap. These are bounds, not exponent evaluations.

## Proof and simpler second certificate

Saved PROOF.md with the constant-potential identity, a nonnegative signed
energy proof using an integral of squared exponential kernels, and the full
capacity/layer deduction. This proves global minimality among all
deterministic probability time measures, not only a finite family of weights.
Endpoint potentials are finite; atomic time measures have infinite energy.

Simplified the bound J<21/8: the first eight terms of S already give
S8=112206509213551/78752847495168>178/125. The exact margin is
7806797553971/9844105936896000. The elementary integral identity
22/7-pi=integral_0^1 x^4(1-x)^4/(1+x^2) dx proves pi<22/7.
Then the integer/rational comparison
2(22/7)^4<(21/8)^4(178/125)^4 suffices. This separately checks the earlier
24-term/Machin certificate for the same bound.

Commands for the simplification used a small `python3 -B -c` calculation,
wrapped in `OMP_NUM_THREADS=1 nice -n 15`, importing only the local guard
and Fraction. Outputs were the fractions above and `True` for both
comparisons. Re-ran `audit.py weighted` after adding the simpler certificate;
it exited zero and printed `J_upper_verified_two_rational_ways=True` and
`ALL WEIGHTED-ENERGY CERTIFICATE CHECKS PASSED`, peak RSS 15384576 bytes.
The remaining constants agree with the preceding output.

## Attempt to break the result

The positive binomial calculation and the signed-kernel positivity proof
give independent roles to the candidate density: the first establishes
constant potential and its value, the second establishes minimality. No
unproved stationarity-to-minimum implication is used. Both endpoints and
infinite-energy competitors are included. The expected-energy identity
scales as t^(-1/2), hence at r^2/18 the factor is 6/sqrt(pi), independently
matching the uniform constant when J is replaced by 8/3.

As a further diagnostic, directly integrate the original potential and beta
normalization after the substitution v=x z^4/(z^4+(1-z)^4). This removes
their endpoint singularities, permitting inexpensive Simpson quadrature at
two mesh sizes. This diagnostic is not a proof certificate; it can expose
an incorrect binomial identity, normalization, or endpoint limit.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py potential`.
Output (exit zero, under one second):

```
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
mesh=1024; direct_beta=1.694426169586988; direct_J=2.622057554293621; max_potential_error=4.79e-12
mesh=2048; direct_beta=1.694426169587897; direct_J=2.622057554292214; max_potential_error=2.98e-13
DIRECT POTENTIAL QUADRATURE DIAGNOSTIC PASSED (not a proof certificate)
peak_RSS_bytes=15089664
```

The nine test points include 0, 0.001, 0.01, 0.125, 0.25, 0.5, 0.9,
0.999, and 1. The error falls by about 16 on doubling the mesh, consistent
with the transformed integrands being smooth. The exact proof, not these
floating-point checks, establishes the result.

Rechecked the support of the occupation measure on long segments and the
bound by one on short segments; conditional iteration at ordered stopping
times; time-zero hits, zero capacity, coincident Green points, inward test
path returns, the last layer, and noninteger thresholds. The Green minimum
also follows from the image formula at opposite radial endpoints:
1/(1+2)-3/(9+2)=2/33. The capacity scale is cap(K)/r, the energy scale is
r I_t. Subtracting the exceptional tail in the second-moment comparison
uses b>1, which has both the exact integer check 1122<1125 and the separate
Decimal value 1.002430546775620... . No unresolved mathematical defect found.

For a sharper rounded display, replaced log(3)<1.1 by log(3)<1.099.
The positive sixth-degree Taylor sum at 1099/1000 exceeds 3. This gives
delta>2000/1051743>19/10000, proving xi_3(1,1)<0.9981. Re-ran
`OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py weighted`: exit zero,
`ALL WEIGHTED-ENERGY CERTIFICATE CHECKS PASSED`, peak RSS 15138816 bytes.
All other output agrees with the preceding successful weighted certificate.
Subsequent script edits correct comments only.

## Final report

Saved REPORT.md with a PARTIAL verdict, the optimal deterministic time-weight
lemma, the improved exponent bound below 0.9981, reproduction commands,
the failed precision check, resource usage, limitations and a concrete next
step using sharper radial exit-time estimates. The exact-value problem and
general moment family remain unresolved. No priority or best-bound claim.
No earlier folder was modified; no git, workers, external writes or large
computations were used.
