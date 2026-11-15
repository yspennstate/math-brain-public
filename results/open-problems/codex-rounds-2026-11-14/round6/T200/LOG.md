# T200 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session began 15 November 2026, about 11:11 Asia/Tbilisi (07:11 UTC).

## 1. Orientation and literature check

Read the startup MEMORY.md, brain navigation index, mesh protocol and compute
state. The task's explicit restriction to writes inside this folder takes
precedence over global mesh/checklist/brain writes, so those mutating commands
are not run. No git, subagents, external messages or writes in earlier folders.
The compute state is `ok`, `owner_away_open`; this work needs only small
standard-library arithmetic. Every numerical command uses
`OMP_NUM_THREADS=1 nice -n 15`, a 60-second CPU limit, and checks actual priority
and measured memory. No simulation is planned.

Literature check finished within five minutes. Web searches:

* `Brownian intersection exponents three dimensions exact xi 2026 2609.18643`
* `"Brownian intersection" "exact" "2026" exponents`
* `"Brownian intersection" "2611"`
* `"Brownian intersection" "2610"`
* `"three-dimensional" "intersection exponents" "exact" November 2026`

Opened these primary sources (author lists read on their arXiv pages):

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

No subsequent exact evaluation was located. The abstract pages show v1 only;
the numerical paper explicitly says no general exact expression is known.
This is a limited negative search, not a proof of absence or priority.
No SOLVED_ELSEWHERE.md is warranted. Literature search is now closed.

## 2. Earlier work and independent re-check

Reading the REPORT.md, LOG.md, PROOF.md and scripts in each of the original,
round 3, round 4 and round 5 folders. The round 5 proof's radial generator
calculation gives `2 sinh(sqrt(2q))/sinh(2sqrt(2q)) = sech(sqrt(2q))`,
with the correct generator `Delta/2`. Reflection gives the factor four in
its Gaussian bound. The weighted-energy formula, unrestricted continuation,
conditional layer iteration and comparison with the second-moment exponent
have the correct signs and scaling. No defect found in the mathematical
argument so far. A newly written numerical audit will check its main bound
before any extension is used.

## 3. One extension chosen before calculation

Vary the Brownian segment endpoint radius `a>1` and the layer spacing `b>a`,
as the round 5 report suggests. Derive a uniform radial short-time estimate
for this family and carry one rational parameter choice through the same
capacity/moment argument. Retain the previous deterministic time measure
and scalar energy estimate. This is one extension of the geometry, not a
new method for identifying exact exponents. The aim is a strictly stronger
certified upper bound on `xi_3(1,1)`; no optimum or best-known-bound claim.

## 4. Baseline audit implementation

Wrote `audit.py` without importing earlier verification code. It checks the
round 5 Gaussian bound by integrated Taylor series, rather than the Mills
approximation used in its main proof; checks the energy, conditional moment,
tail base and final gap by exact fractions; and checks J separately with
the gamma function. Command:
`OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline`.

The first run passed all rational certificates but failed the redundant
Decimal enclosure assertion: 100-digit working precision did not resolve
the width of the 160-term rational logarithm interval. This is a verifier
precision issue, not a failure of a mathematical inequality. Increase
Decimal precision to 130 before repeating. Actual priority was nice 20;
the wrapper warning is its unsuccessful attempt to add 15 to nice 20.

The repeat exited zero (under one second), with output:

```
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
J_independent_gamma=2.622057554292119
round5_gaussian_rational_upper=16311/1000000
round5_moment_rational_upper=13623/100000
round5_tail_base=333313941/1000000000; three_times_numerator=999941823
round5_tail_exponent=1.000052956527928368824764759279119817...
round5_xi_upper=0.997096525592896850419093332804669515...
ROUND 5 RESULT VERIFIED independently
peak_RSS_bytes=14319616
```

The earlier main claim holds. Before proceeding, re-derived the generalized
radial transform as `a sinh(sqrt(2q))/sinh(a sqrt(2q))`. One-dimensional
Brownian motion started at 1 and killed on exiting (0,a) has upper-exit
transform `sinh(sqrt(2q))/sinh(a sqrt(2q))`. Equality of the transforms
therefore identifies the radial exit law with a times the upper-exit
subprobability law. Its short-time CDF is at most
`2a Phi_bar((a-1)/sqrt(t))`, by dropping the lower-barrier restriction and
using reflection. At a=2 this recovers round 5's factor four. A proof will
justify the stopped martingales and uniqueness for these probability laws.

Wrote `explore.py` to propose geometry parameters. It uses this upper bound,
the retained weighted energy, and a scalar bisection to optimize the Laplace
parameter for each geometry/cutoff grid point. Its output is diagnostic only.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B explore.py`.
Exit 0, about 0.87 seconds. Output:

```
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
evaluations: 211795
best (gap,a,b,v,t,s,c,p,g,theta):
(0.0031259031917891824, 1.9, 3.4, 7.3, 0.11095890410958902,
 21.490387977717045, 0.041478000361620165, 0.01310137602087604,
 0.09222728903007638, 0.8913783203111052)
```

The grid supplies candidates only; its optimizing boundary tail exponent is
exactly one and cannot be used for the proof. Test the nearby rational
choice a=19/10, b=17/5, t=81/730, s=43/2, threshold c=5/121, which leaves
a positive exceptional-tail margin while targeting xi_3(1,1)<0.9969.

The search with two fixed candidates appended exited zero (0.92 seconds):

```
candidate a,b,v,s,c: 1.9 3.4 7.3 21.5 0.04132231404958678
t,p_mills,energy_hi,moment_hi,tail_base,1/b,xi_upper:
0.11095890410958902 0.013107367357900199 6.287649001104543
0.12069326506992425 0.29344260887545476 0.29411764705882354
0.9968858297831725
candidate a,b,v,s,c: 2.0 3.5 7.0 20.0 0.043478260869565216
t,p_mills,energy_hi,moment_hi,tail_base,1/b,xi_upper:
0.14285714285714285 0.016310482107367786 5.541385822408738
0.11823857809052178 0.2821022655230262 0.2857142857142857
0.9969556231878416
```

Choose the first candidate. The second is simpler but has a weaker bound.
For the first, propose the roundings p=1311/100000, A=629/100,
e_lower=1359/500, m=151/1250, exp(sc)<304/125. They imply
beta=22952/78125 and b beta=390184/390625<1. The generalized Green constant
is 1800/19517; multiplying by c=5/121 gives 9000/2361557. These will now
be certified exactly in `audit.py geometry`, with a second Gaussian-tail
certificate and separate radial heat-equation diagnostics.

## 5. Exact geometry certificate

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py geometry`.
Exit zero, under one second. Output:

```
niceness=20; OMP_NUM_THREADS=1; CPU_limit=60s
a=19/10; b=17/5; v=73/10; time=81/730; s=43/2; c=5/121
certified_exit_upper=1311/100000; certified_energy_upper=629/100
moment_rational_upper_before_rounding=705610907/5843700000
rounded_moment_upper=151/1250; exp_sc_upper=304/125
tail_base=22952/78125; b_times_tail_base=390184/390625
tail_margin_integer=441
tail_exponent=1.0009230433347472227067772249108457859...
green_constant=1800/19517; gap_numerator=9000/2361557
coarse_gap_lower=360000/115716293 > 31/10000
gap_interval=[0.00311417021682751033910705882786648991514812355049357...,
              0.00311417021682751033910705882786648991514812355049357...]
xi_upper=0.99688582978317248966089294117213351008...
gap_ratio_to_round5=1.072566787297627977508429970516518782...
ALL GEOMETRY CERTIFICATE CHECKS PASSED
peak_RSS_bytes=15646720
```

Exact fractions certify every scalar bound; the displayed decimals are
diagnostics. The independent integrated Taylor Gaussian certificate also
passed. Rational logarithm intervals, Decimal logarithms and libm agree on
the gap. The gap is about 7.26% larger than round 5's, not a 7.26% change in
the exponent. The probability proof still needs to be saved in full.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py diagnostics`.
Exit zero, under one second. Output:

```
radial_CDF a=1.9; t=0.110958904109589;
  spectral=0.0131013760208758; images=0.01310137602087605;
  upper=0.01310137602087605
radial_CDF a=1.9; t=0.25;
  spectral=0.1365352000292832; images=0.1365352000292834;
  upper=0.1365352126291182
radial_CDF a=1.9; t=0.5;
  spectral=0.3857963104851398; images=0.3857963104851401;
  upper=0.3858743963966191
radial_CDF a=1.9; t=1;
  spectral=0.6923433288049519; images=0.692343328804952;
  upper=0.6994284763176862
max_radial_CDF_discrepancy=3.331e-16
grid_Green_minimum=0.09222728903007638; formula=0.09222728903007638
unrounded_gaussian_upper=0.01310137602087605;
actual_mean_energy=6.280600976031794
unrounded_moment_bound=0.120566677289871;
unrounded_tail_base=0.2931348348798714
GEOMETRY DIAGNOSTICS PASSED (not a proof certificate)
peak_RSS_bytes=15532032
```

These compare the radial sine-series solution with an image expansion at
four radii and four times. The new Gaussian bound has the right factor and
scaling. A 21-by-21-by-21 Green grid includes the opposite boundary points
where the claimed lower bound is attained. These checks are diagnostics;
the continuous minima and exit bound have analytic proofs in PROOF.md.

## 6. Complete proof saved

Saved PROOF.md with the normalized radial exit/upper-exit identity, the
general two-geometry-parameter capacity lemma, the rational parameter choice,
and the full exponent deduction. It includes the retained time-energy
identity and all finite scalar certificates. An initial combined patch was
rejected atomically because its LOG.md context did not match; PROOF.md was
then added in a separate successful patch. No computation or constant changed.

Added two exact audit checks: the Mills polynomial identity at eleven
distinct integers (its degree is at most ten), and the factored expression
for the Green constant. These independently check the algebra, and warrant
one final run of the geometry certificate.

## 7. Attempt to break the proof

Re-derived the radial identity in two descriptions. The Laplace ODE has
generator Delta/2 and the smooth origin value a sqrt(2q)/sinh(a sqrt(2q)).
The killed one-dimensional process has the same transform after multiplying
its upper-exit subprobability by a. The factor a is required: the probability
of upper exit is 1/a, so omitting it fails total-mass normalization. At a=2,
the transform and the short-time Gaussian factor agree with round 5. The
independent radial heat equation (sine expansion) matches the transform/image
calculation at a=1.2,1.9,2,3 and four times, with error below 3.4e-16.

The image formula's paired CDF differences are nonnegative; their densities
need not be. Its written justification uses Tonelli on the CDFs and their
Laplace transforms, not on signed density differences. This distinction
does not affect the main exit bound, which follows directly from the killed
one-dimensional exit law and reflection. Neither numerical series is used
as a probability bound in the theorem.

The generalized Green minimum has two independent expressions: the d,D
kernel estimate and the opposite radial image points. Its factored value
(b-1)(b-a)/((1+a)(b^2+a)) is positive precisely in the relevant geometry.
Both endpoint extrema can occur simultaneously. For the selected parameters,
the rational arithmetic and the 9261-point grid agree on 1800/19517.
The zero-capacity, initial-hit and coincident-point cases are covered.

The energy still scales as t^(-1/2), with dimensionless mean r I_t.
Its probability time measure has integrable endpoint singularities and no
atoms. Finite expected energy handles spatial self-intersections without
assuming injectivity. On long segments it lies in the obstacle; on short
segments only exp(-s C)<=1 is used. No independence of that event and the
energy is assumed. The energy constant has the retained beta certificate
and an independent gamma-function diagnostic. The Gaussian probability is
certified both by the Mills bound and integrated Taylor series; all squaring
steps compare positive quantities.

Earlier capacities are measurable before each next segment starts, since
a<b. The final segment ends before R. Conditional iteration does not
require independent layers. With the obstacle fixed, the test path is still
independent Brownian motion. Its first-hitting-time decomposition permits
inward returns and an initial point already in K. Every factor 1-g C is
nonnegative, since g a<a/(1+a)<1. The capacity threshold cN is real.

The exceptional-tail exponent is strictly greater than the exact
second-moment exponent one: b beta=390184/390625<1, with integer margin
441. Decimal logarithms check its value 1.0009230433... independently.
The second-moment comparison rearranges to a lower bound on E Q_R, hence
an upper bound on xi, with the right sign. Monotonic bracketing transfers
the defining limit to (17/5)^N; no estimate up to multiplicative constants
is assumed. The final gap is independently checked by rational logarithm
bounds, Decimal and libm. It exceeds the round 5 gap by direct comparison
of rational intervals, avoiding subtraction of two nearly equal xi bounds.

The final audit found two written short certificates that the script had
previously checked through stronger variants: the eight-term Machin bound
and the J bound using 178/125 rather than the exact eight-term beta sum.
Added the exact shorter comparisons too, so the written proof and script
now match. No mathematical constant changed. No unresolved defect found.

## 8. Final verification and report

Final commands after those certificate additions:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py geometry
```

Both exited zero in under one second. The baseline printed
`ROUND 5 RESULT VERIFIED independently`, the same upper bound
0.9970965255928968504..., and peak_RSS_bytes=14778368.
The geometry mode printed `ALL GEOMETRY CERTIFICATE CHECKS PASSED`,
the unchanged moment bound 705610907/5843700000<151/1250,
tail base 22952/78125, b times tail base 390184/390625,
tail exponent 1.0009230433347472227..., Green constant 1800/19517,
gap numerator 9000/2361557, upper bound 0.99688582978317248966...,
gap ratio 1.0725667872976279775..., and peak_RSS_bytes=14745600.
The diagnostics had already passed and its code was unchanged.

Observed clock reading after final numerical verification: 07:24:59 UTC,
11:24:59 Asia/Tbilisi. Saved REPORT.md with the required PARTIAL verdict,
the new geometry lemma and bound, reproduction commands, audit results,
failed checks, limitations and a concrete next step. The problem's exact
values remain open. No solved-elsewhere file is warranted. All requested
predecessor reports, logs, proofs and mathematical scripts have been read;
none was executed in a mode that could write there, and none was edited.

Final readback confirmed the verdict prefix and all five work products.
Cross-referenced the scalar constants between REPORT.md, PROOF.md and
audit.py. Corrected a stray plus sign in this log; no mathematics or code
changed after the successful final certificates.
