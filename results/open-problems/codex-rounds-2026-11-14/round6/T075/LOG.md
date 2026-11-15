# T075 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session date 2026-11-15; first exact tool clock
06:29:54 UTC = 10:29:54 +04:00.

## Scope and orientation

All writes stay here. No git, subagents, external messages, or shared
mesh/checklist/brain writes: the task-specific restriction takes precedence.
Read the startup MEMORY.md and compute_state.json. Compute is warn /
owner_away_open, CPU saturated. Only short standard-library calculations
under nice -n 15, OMP_NUM_THREADS=1 are planned. Brain recall is not run:
the preceding log records that it attempts an out-of-folder index refresh.

Read all four earlier REPORT.md and LOG.md files, all three existing
PROOF.md files, and all three scripts. The first folder has no PROOF.md
or scripts. Earlier folders remain read only.

## Bounded literature check

Used the web search tool for:

- Bernoulli convolutions transcendental absolute continuity November 2026 Kittle Kogler 2611.17277
- Bernoulli convolution absolute continuity transcendental Erdős problem solved 2026

Opened Samuel Kittle and Constantin Kogler, *On L^p density of self-similar
measures and Bernoulli convolutions*, arXiv:2611.17277v1,
https://arxiv.org/html/2611.17277v1 . Theorem 1.1 assumes absolute continuity.
Opened their *The Exact Overlaps Conjecture for Self-Similar Measures on
the Real Line*, https://arxiv.org/abs/2610.10511 : the conclusion is dimension.
Also opened the October arithmetic-classification source already checked
in round 4:
https://github.com/openai/math/blob/main/preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/build/classification.tex
Its criterion is an infinite algebraic-approximation/crowding condition;
it does not exclude transcendental parameters from the singular set.
No result from that source is used. No solution of T075 was found.
Literature checking ends within five minutes; this is a bounded search.

## Independent recheck of round 5

The branch densities have heights (1-lambda)/(4lambda) on the outer
region and (1-lambda)/(2lambda) on the overlap. The outer region has
total length 4. Integrating its deficit against uniform[-R,R] gives
4[(1-lambda)/2-(1-lambda)/(4lambda)]
=(2lambda-1)(1-lambda)/lambda. The central surplus gives the same
answer, so the TV normalization is correct. Contractivity gives
e_(n+1)<=e_n+d, hence e_n<=nd and the reported cap inequality.
At the multinacci root, 2lambda-1=lambda^(k+1); the earlier upper
root bracket and Pisot proof supply singularity and 2lambda-1<2^-k.
The proof does not interchange the finite-horizon and parameter quantifiers.
The earlier mathematical claim holds.

Command (completed, exit 0):

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/T075/check_obstruction.py > earlier_recheck.txt 2>&1
```

## Choice before extension

Choose one extension: prove explicit stability of the finite-prefix cap
under changes of parameter, then use it to transfer the round-5 delayed
concentration to open intervals containing transcendental parameters.
The earlier obstruction only used algebraic singular parameters. The
extension will show that merely restricting the parameter to be
transcendental does not give a uniform all-depth cap bound from finitely
many small initial caps. It will not claim a singular transcendental
parameter or disprove an absolute-continuity criterion on that class.

Aim for an explicit TV Lipschitz constant on [a,b] subset (0,1), derived
from the moving endpoints of the uniform-tail intervals. Check it by
exact rational interval integration independently of the endpoint bound.
Use continuity and the known eventual concentration at a multinacci
control for the theorem; no computable upper time of that concentration
is assumed. Keep the choice of late depth and parameter interval explicit
about which quantities are existential.

## Proof saved and first computation attempt

Saved PROOF.md and check_stability.py. The proof gives
C_n(a,b)=(1-a)/[(1-b)^2 a^n]. Each prefix interval endpoint has
derivative bounded by (1-b)^-2, because the finite-prefix derivative
and the derivative of its uniform-tail radius sum to the derivative
of the entire geometric series. Uniform-interval TV is computed from
the length of intersection divided by the larger interval length.
Mixing over words and taking cap suprema gives the result without any
assumption about distinct endpoints or sums.

The extension transfers a late cap near one from a singular multinacci
control to an open interval. Transcendental parameters remain after
removing the countably many algebraic numbers. A further subinterval
can avoid any prescribed finite list of polynomial roots, with a
positive rational separation bound selected by the construction.

First command:

~~~sh
OMP_NUM_THREADS=1 nice -n 15 python3 check_stability.py > computation.txt 2>&1
~~~

It exited 1 before computation: macOS rejected setrlimit(RLIMIT_AS,
(900000000,900000000)) with ValueError: current limit exceeds maximum
limit. Restricted this optional address-space cap to non-macOS platforms;
the script's finite word counts, 120-second alarm and measured RSS check
remain. At most 512 words are enumerated for each parameter in the grid.
Also corrected an independently recomputed example denominator before
rerunning: 159201*6561=1044517761, rather than the mistyped 1044546321.
This display-target correction does not alter the derived bound.

The first patch attempt for these corrections had an unmatched LOG.md
context and changed no files. A subsequent tool expression had unescaped
Markdown backticks and failed to parse before making any tool calls.
The corrected patch succeeded.

## Successful computation

Reran the same command. Exit 0; computation.txt records:

~~~text
priority 20
OMP_NUM_THREADS 1
uniform-interval formula and endpoint-bound checks 225
exact parameter-pair/depth TV checks 81
individual-word endpoint and TV checks 4599
cap-difference checks 324 independent midpoint/dual caps 360
largest TV / Lipschitz bound in grid 249001/250000
finite-polynomial exclusion checks 80
round-5 depth and margin rechecked 25031 1/9437184
example a 3/5 b 601/1000 n 8 C_n 156250000000/1044517761 bound for parameter change 1e-6 156250/1044517761
WARNING: no late depth m or singular transcendental parameter computed
elapsed_seconds 0.908
peak_rss_bytes 19185664
~~~

The mixture TV was integrated by signed endpoint events, separately
checking equality of its positive and negative integrals. Wordwise
interval TV was independently obtained from overlaps of directly
enumerated sign words. Affine-iteration generation reverses the order
of the word but gives the same full mixture; multiplicities are kept.
Caps were checked both by sorting density segments and by direct
midpoint coverage plus the convex-dual minimum over density thresholds.
The grid includes parameters on both sides of 1/2, near 1, and across
the first multinacci overlap at approximately 0.618.

Repaired inline math delimiters lost during the initial tool-string
serialization. An inline Python command replaced the outer parenthesis
pairs in prose by dollar delimiters, retaining nested function arguments,
equation references, displayed formulas and the Markdown link. Restored
the initial lambda commands and the escaped finite coefficient set.
No mathematical claim or script changed in this formatting correction.

Two delimiter-repair attempts stopped on a dollar-count assertion before
writing. The successful repair generated dollar delimiters with chr(36)
and checked each line before saving 114 inline math spans.

## Failure-case audit

1. Uniform-interval TV is 1-intersection_length/max(lengths), not a
   denominator using the shorter interval. Direct integration of the
   absolute density difference independently checked all 225 pairs,
   including nesting, disjointness and equal endpoints.
2. The endpoint bound sums the prefix derivative and the radius
   derivative. Their positive series partition the full geometric
   derivative, including n=0. Independently, the script checked
   sum_(1<=j<n) j b^(j-1)
   + n b^(n-1)/(1-b) + b^n/(1-b)^2 = (1-b)^-2.
3. Mixture TV can be smaller than the average of wordwise TV.
   Only the required inequality is used. Coincident words retain
   multiplicity; no parameter transversality or algebraicity is assumed.
4. Cap sets may be disconnected, and the maximizing set need not be
   attained. The difference of suprema follows by bounding each eligible
   set individually. The midpoint/dual checks independently verify the
   finite cap calculations.
5. The example constant was re-derived as
   2*5^7*10^6/(399^2*3^8)
   =156250000000/(159201*6561)
   =156250000000/1044517761. The test's parameter change is 10^-6,
   inside [3/5,601/1000]. Its TV upper bound is
   156250/1044517761; this is not a computed late cap.
6. Test counts were separately recovered:
   15^2=225 interval pairs; 9*9=81 parameter/depth pairs;
   9*(2^9-1)=4599 word pairs; 81*4=324 cap differences;
   9*5*4*2=360 dual comparisons;
   2*(1+3+9+27)=80 nonzero-leading coefficient polynomials.
7. The early interval has b=1/2+(theta-delta_0/4)/(2N)<1.
   The parameter remains strictly below b, so even n=N has
   a strict cap inequality. The n=0 case uses delta_0/4<theta
   directly. The multinacci root lies strictly inside this interval.
8. The late-depth choice is made before shrinking the parameter
   interval. The TV constant grows exponentially with that depth,
   but the radius in equation (10) stays positive for every finite m.
   This proves existence, with no uniform lower interval width or
   effective upper m claimed.
9. Removing finitely many polynomial roots leaves a subinterval.
   The derivative bound H_i=sum j|c_ij| supplies a rational margin
   there. Constant nonzero polynomials are included. The margin is
   selected after the interval; no prescribed Diophantine bound is
   proved. Differences of sign prefixes are twice {-1,0,1}-polynomials,
   which accounts for the factor 2 in their separation.
10. The supremum in equation (11) takes parameters outside the depth
    limit. The parameter changes with the desired concentration scale.
    Reversing these quantifiers would be an unsupported singular
    transcendental construction. Finite high caps are compatible with
    a density, even a density in some L^p; no AC criterion on
    transcendental inputs is disproved by this result.

Saved REPORT.md with VERDICT: PARTIAL. T075 remains open in the bounded
literature check. No solution-elsewhere file is warranted.

## Final verification

An inline read-only command under OMP_NUM_THREADS=1 nice -n 15 python3
parsed the script, checked the six deliverables and the report verdict,
balanced all display delimiters and all 114 inline math spans, checked
for control characters, and independently recovered the example
coefficient, old margin and every reported verification count.
It also checked the n=0 TV formula h/(1-a) against the bound at three
parameter pairs. Output:

~~~text
Final audit passed: syntax, delimiters, quantifiers, independent constants, counts, n=0.
Actual priority 20
~~~

Exit 0. No further script changes followed the successful computation.
The first final-log append had an unmatched context and made no change.
Final exact clock: 2026-11-15 06:39:01 UTC = 10:39:01 +04:00.
