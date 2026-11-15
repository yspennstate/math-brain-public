# T200 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session began 15 November 2026, about 08:35 Asia/Tbilisi (UTC+04).

## Orientation and bounded literature check

Read REPORT.md, LOG.md, PROOF.md and all mathematical Python scripts in
the three predecessor folders: codex_op_1114, codex_op_1114r3 and
codex_op_1114r4, each under briefs/T200. They remain read-only. Read the
startup memory index, brain navigation index and compute state. The latter
reports status ok, mode owner_away_open. The task-specific prohibition on
writes outside this folder takes precedence over global mesh, checklist,
recall-log and memory writes; those commands are not run. No git or agents.

The web check ended by 08:36, within five minutes. Queries included
`"Brownian intersection exponents" "2026" exact three dimensional`, the
two September arXiv IDs, and exact-value searches with November 2026 and
xi_3. No later exact evaluation was located. This limited search establishes
neither absence nor priority. No SOLVED_ELSEWHERE.md is warranted.

Primary sources actually opened:

* Yifan Gao, Xinyi Li, Yifan Li, Runsheng Liu, and Xiangyi Liu,
  *A boundary Harnack principle and its application to analyticity of 3D
  Brownian intersection exponents*, https://arxiv.org/abs/2411.14921.
  Its attempted HTML timed out; the abstract page opened.
* Runsheng Liu, *An explicit lower bound for the growth exponent of
  three-dimensional loop-erased random walk*,
  https://arxiv.org/abs/2609.18643 and
  https://arxiv.org/html/2609.18643v1. Remark 1.2 still omits the proof of
  its stronger 0.999 bound.
* Qiyuan Shi, Runsheng Liu, Xinyi Li, Ming Li, and Youjin Deng,
  *Intersection Exponents of Simple Random Walks in Two and Three Dimensions*,
  https://arxiv.org/abs/2609.25968 and
  https://arxiv.org/html/2609.25968v1. Its introduction states that no
  general exact expression is known and describes its estimates as numerical.

## Re-derivation of round 4, before extending it

The beta/binomial calculation gives
L(x)=B(3/4,1/2)/4 times integral_0^x [z(1-z)]^(-3/4) dz.
Reflection makes L(x)+L(1-x) constant, with endpoint value pi sqrt(2).
The signed-energy argument is valid: finite absolute energy justifies the
mixture of positive exponential kernels, and the competitor's mixed energy
with the candidate is the same constant. Infinite-energy competitors cause
no exception. Thus J=pi sqrt(2)/B(3/4,3/4) is the minimum time energy.

Independently re-derived the Brownian mean energy as
sqrt(2/pi) J/sqrt(t), and the Green minimum as
1/(1+2)-3/(9+2)=2/33. The occupation support, conditional layer iteration,
and second-moment comparison have no apparent defect. A separate local
script will now certify the scalar inequalities and directly integrate the
candidate's potential, before selecting the extension.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline`.
Exit 0, under one second. Output:

```
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
independent_potential_mesh=1024; max_error=5.401e-09
independent_potential_mesh=2048; max_error=3.321e-10
J_independent_beta_series=2.62205755429211981046483958989111941368275495143162316281633
round4_rational_laplace_upper=324643/2669160
round4_unrounded_laplace=0.120725448617180082585826868556666529492338627539644094226196
round4_tail_exponent=1.00243054677562008992623944932105376659949563992587748955696
round4_xi_upper=0.998097723664311729584923218044438647856608911061117634807260
ROUND 4 RESULT VERIFIED independently
peak_RSS_bytes=14876672
```

The shell's nice warning reflects inherited nice 20, checked through libc.
The numerical potential test uses a sine substitution different from round
4's rational substitution. It is diagnostic only. Exact fractions certify
the probability comparisons. Round 4's main claim holds; no defect found.

## One extension chosen, before calculation

Replace the displacement-maximal estimate for a short r-to-2r segment by
a radial exit-time estimate, the next step explicitly proposed by round 4.
Retain the optimal deterministic time weight and factor-three layers; choose
a longer time cutoff if the radial bound permits it. Prove the radial
identity or bound and carry a certified constant through the same capacity
moment and exponent argument. No simulation and no change to the Green
hitting estimate are planned.

Reason: at initial radius exactly half the killing radius, the radial
Laplace equation appears to simplify to sech(sqrt(2q)). This is also the
Laplace transform of the first exit time of a one-dimensional Brownian
motion from (-1,1), started at zero. If verified, reflection and a Gaussian
tail estimate will give a much smaller short-time probability. This is a
candidate derivation until checked below.

## Radial identity and cutoff exploration

For exit from the radius-2 ball at initial radius 1, solve (1/2) Delta f=qf
with boundary value 1: f_q(x)=2 sinh(a|x|)/(|x| sinh(2a)), a=sqrt(2q),
with its removable value at zero. Optional stopping gives the Laplace
transform f_q(1)=1/cosh(a). The one-dimensional exit from (-1,1), started
at zero, has the same transform, from cosh(ax)/cosh(a). Thus the two exit
times have the same law. Reflection plus a union bound gives short-time
probability at most 4 times the standard normal upper tail at 1/sqrt(t).
Both the optional-stopping justification and transform uniqueness will be
written out in PROOF.md.

Saved and ran `OMP_NUM_THREADS=1 nice -n 15 python3 -B explore.py`.
Exit 0, under one second. A 302,151-point diagnostic grid over cutoff and
Laplace parameter suggested t=0.1408, s=16.8, average capacity threshold
about 0.0527153 (tail boundary). No grid result is a proof certificate.
At the old t=1/18, reflection gives p<=0.0000441809940, versus the old
0.00812864695. At t=1/7, the reflection bound is 0.0163019431870 and the
mean energy constant is 5.53517430739. The simple Mills bound is 0.0182134
there and loses some of the gain. A sharper certified Gaussian tail and
the rational candidate s=17, threshold 1/19 will now be checked.

Two small one-thread Python heredocs, using the local resource guard,
checked candidate roundings. With the elementary third Mills convergent
and J<21/8, the candidate fails: tail base 0.3335023>1/3. The fifth
convergent succeeds: tail base about 0.33330277<1/3. Its rational factor
at x=sqrt(7) is 60/67. The exact derivative identity for
U(x)=(x^4+9x^2+8)/(x^5+10x^3+15x) is
U'-xU+1=-120/(x^5+10x^3+15x)^2, proving it bounds the Mills ratio above.

Proposed clean certificate: t=1/7, s=17, threshold 1/19; exit upper
p=16311/1000000; energy upper A=27707/5000; e>67957/25000;
exp(17/19)<24467/10000. Then
m=p+A/(17 e_lower)=157378592659/1155269000000<13623/100000.
The resulting tail base is at most 333313941/1000000000<1/3.
Each scalar comparison in the heredoc passed using exact fractions.
No theorem relies on the exploratory decimal grid. The full local radial
audit, including a second Gaussian-tail certificate, will now be run.

An initial patch adding this audit matched the wrong wrapped log line and
was rejected atomically. Inspection confirmed no partial edit; a corrected
patch was then applied. No computation failed and no constants changed.

First `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py radial` exited 1
in the redundant Decimal-versus-rational gap cross-check. All preceding
exact certificate assertions passed. The 100-term log interval is narrower
than the current 60-digit Decimal context, so its two endpoints rounded to
the same number. Increased the Decimal context to 80 digits; no proof
constant or exact comparison changed.

The second radial run exited 0 in under one second, peak RSS 15138816 bytes:

```
exit_CDF t=1/18: radial_spectral=0.00004418099399716713, reflection=0.00004418099399717088
exit_CDF t=1/7: radial_spectral=0.01630194318700118, reflection=0.01630194318700126
exit_CDF t=1/2: radial_spectral=0.3145542331096479, reflection=0.3145542331096481
exit_CDF t=1: radial_spectral=0.6292225702004761, reflection=0.6292225702004761
Mills_polynomial_remainder=-120 verified
Gaussian_reflection_bound=0.0163019431870054006259585206558590854858336161950753...
Mills_upper_at_t_1_over_7=0.0163104821073677851969027926637708803022409829239874...
certified_exit_upper=16311/1000000 (two independent rational certificates)
weighted_energy_constant=5.53517430738822107996933072580562819510964569690838...
certified_energy_upper=27707/5000
certified_e_lower=67957/25000; certified_exp_17_over_19_upper=24467/10000
rational_moment_upper=157378592659/1155269000000
rounded_moment_upper=13623/100000
unrounded_reflection_moment_bound=0.136082933245152699130550616338285777238244392849322...
certified_tail_base=333313941/1000000000
tail_margin_below_1_over_3=58177/3000000000
certified_tail_exponent=1.00005295652792836882476475927911981704690061524362...
xi_upper=0.997096525592896850419093332804669515149560969514337...
gap_ratio_to_round4=29/19
ALL RADIAL-EXIT CERTIFICATE CHECKS PASSED
```

The full output includes an exact rational-series interval for the gap.
The displayed long decimals are diagnostics, not certified precision claims
for all their digits. The exact proof depends on rational comparisons only.
The tail exponent's margin above 1 is small but strictly positive. The
spectral check uses the radial heat equation and is independent of the
Laplace-transform argument; its maximum discrepancy is below 2e-16.

For a simpler written certificate, additionally certify pi>314159/100000
by the short Machin sums and exp(7/2)>662309/20000 by its degree-24 positive
Taylor sum. These coarse rationals already certify both the Gaussian
Mills bound and the energy upper 27707/5000. Added these exact checks;
the proof constants are unchanged. Next: save the complete proof, then
audit the stopping-time and Gaussian-bound steps for missing cases.

## Complete proof saved; attempt to break it

Saved PROOF.md with the radial Laplace identity, its transform uniqueness
argument, the Gaussian rational bound, the weighted time-energy identity,
all conditional iteration steps and the passage to exponents. It is
self-contained apart from the standard equilibrium-potential identity
already used and sourced in Liu, Section 2, and the two exponent inputs
explicitly supplied in the task. The round 4 optimality theorem is not
needed anew: the proof re-derives the candidate's energy and its bound.

Audit of possible failures:

* The radial function sinh(a|x|)/|x| is smooth at zero by its even power
  series. The stopped Itô integrals have bounded coefficients on the ball.
  Exit times are finite, as shown separately by the squared-distance
  martingales. No unbounded optional-stopping step is hidden in (3).
* Laplace transforms match with generator (1/2) Delta; using Delta instead
  would change the time by a factor two. Polynomial approximation for
  exp(-tau) explicitly supplies uniqueness. The dimension three and initial
  radius one-half of the killing radius are essential to the simplification.
* Independently derived the radial heat equation by multiplying radial
  survival probability by the radius. Its sine expansion gives (23), which
  matches the one-dimensional reflection expansion in four diagnostics.
* The reflection union is an upper bound, not an exact CDF. At t=1/7 the
  difference from the exact CDF is about 4e-15; it is retained as a bound.
  Both barriers and the factor four are accounted for. The Mills rational
  upper-bound sign follows by integrating its negative derivative remainder
  backwards from infinity; a sign error would reverse the argument.
* Rechecked the Gaussian scalar bound independently by an integrated
  Taylor series, using exact fractions and squaring positive quantities.
  Both rational certificates pass. Decimal evaluations give the same scale.
* Brownian scaling gives r I_t mean sqrt(14/pi) J at t=r^2/7. At t=r^2/18,
  it recovers round 4's 6J/sqrt(pi). No energy is conditioned on segment
  survival. The weighted measure is supported on the segment only on the
  long-segment event, which is precisely where capacity is invoked.
* The time weight has integrable endpoint singularities and no atoms.
  Finiteness of expected energy addresses possible spatial self-intersection
  singularities. The proof does not assume that unequal times give distinct
  locations on every path.
* The earlier layer capacities are measurable before the next layer starts.
  The test motion is conditioned only on its past; inward returns, initial
  hits, zero capacity, coincident Green points and the final layer all satisfy
  the same bounds. There is no independence assertion about the layers.
* The threshold N/19 is real, with no integrality requirement. The tail
  condition is exactly beta<1/3; its integer margin is 58177 after
  multiplication by 3 and 10^9. The small size of b-1 affects how large a
  radius is needed, but does not invalidate the asymptotic comparison.
* Rechecked exponent signs by rearranging (19): the result is a lower bound
  on E Q_R and hence an upper bound on xi_3(1,1). Monotonic bracketing of
  coupled paths transfers integer log-radii to 3^N.
* Independently evaluated 2/(627 log 3) with rational atanh-series bounds,
  Decimal logarithms and libm. The gap increases by 29/19, has the expected
  positive sign, and remains far from the numerical exponent near 0.58.

The run after simplifying the pi/exponential certificate also exited 0,
peak RSS 15138816 bytes; its values agree with the output above. No
unresolved mathematical defect was found. No claim of an optimal or best
known exponent bound is supported by this work.

## Final checks and report

After the common Decimal precision change, reran
`OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline`.
Exit 0, peak RSS 15384576 bytes, under one second. The round 4 upper bound,
Laplace certificate and potential errors agree with the first baseline
run; `ROUND 4 RESULT VERIFIED independently` printed. No new mathematical
constant changed after the successful radial audit.

At the observed clock reading 08:46:41 UTC+04, checked file sizes and
cross-referenced every proof constant using rg. Corrected the prose phrase
introducing the second-moment asymptotic; no equation changed. Saved
REPORT.md with a PARTIAL verdict, the improved upper bound, reproduction
commands, failures, limitations and a next step allowing general segment
and layer radii. All work products and writes are inside this folder.
No exact value is claimed and no solved-elsewhere file is warranted.
