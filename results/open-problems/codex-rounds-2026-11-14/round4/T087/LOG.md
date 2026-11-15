# T087 working log

Task: “take the NEXT checkable step on this problem, building on that work.”
Date: 15 November 2026, Asia/Tbilisi. Work stays in this directory.

## Orientation and literature check

Read the startup memory, compute-state file, mesh protocol, and the earlier
REPORT.md, LOG.md, PROOF.md and AUDIT.md in both predecessor folders.
File searches found no predecessor computation scripts. The folder-only rule
overrides shared checklist, mesh and brain writes; those tools were not run.
No git, subagents, external posting or numerical workload is used.

Read commands were prefixed by `OMP_NUM_THREADS=1 nice -n 15`.
The sandbox prints `nice: setpriority: Operation not permitted` and completes
the brief reads. No heavy program will be launched. The compute snapshot was
`warn`, `owner_away_open`, with CPU saturation.

Web searches: `three dimensional percolation critical exponents existence
2026 hyperscaling`; `percolation continuity three dimensions 2026 critical
probability exponents`. Opened primary sources:

- Tom Hutchcroft, *Dimension dependence of critical phenomena in long-range
  percolation*, arXiv:2510.03951,
  https://arxiv.org/abs/2510.03951 . The abstract surveys long-range models;
  it does not announce a solution of the cubic-lattice exponent problem.
- C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform Boundedness of
  Critical Crossing Probabilities Implies Hyperscaling*, MSR-TR-98-26,
  https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .
  Opened the paper and read the introduction and definitions. Annular
  multiplicity and the resulting hyperscaling relations are classical.
- OpenAI, *Critical bond and site percolation on the cubic lattice*,
  September 24, 2026: opened its README at
  https://raw.githubusercontent.com/openai/math/main/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/README.md .
  It supplies bibliographic metadata, not a verified exponent theorem.

The literature pass was closed within five minutes. No verified complete
solution of T087 was found. No new SOLVED_ELSEWHERE.md is warranted.

## Independent verification in progress

The predecessor's main theorem assumes a logarithmic one-arm exponent
`pi(n)=n^{-a+o(1)}`, `0<a<d/2`, and
`P(K_n>n^epsilon)->0` for every positive epsilon. Its conclusions are
`F(t)=t^{-a/(d-a)+o(1)}` and `X(n)=n^{d-2a+o(1)}`.
The recheck will separately reconstruct its buffered-annulus mass bound,
tail interpolation and final subtraction argument before using it.

## 04:48 — independent recheck completed: the earlier result holds

Reconstructed the annulus argument using a uniform vertex S of B_{4m}.
Its chance of reaching the outer boundary is at least pi(20m). On the
bad-count event {J_m>L}, it first has to reach partial B_{7m}. Conditional
on S=x, this inner event has probability at most pi(3m) and is independent
of J_m. Thus the expected number of successful vertices lost to the bad
event is at most V_{4m} pi(3m) P(J_m>L). The covering by centers
m*partial B_12 is valid: their radius-2m boxes lie between norms 10m and
14m, and a crossing path from norm 12m to norm 16m exits one such box.
Different annular components cannot use the same small-box component.
Consequently (P) passes from K_m to J_m by a finite union bound.

At a scale with pi(3m)<=C pi(20m), the lost mass is at most half the
total once P(J_m>L)<=1/(2C). The remaining mass is in at most L
components, so E M_m>=V_{4m}pi(20m)/(2L). This independently reproduces
the predecessor's main lower bound without an expectation of J_m.

For completeness, its scale interpolation also holds: writing
f_j=pi(3*8^j), a run of ratios f_j/f_{j+1}>8^{a+1} throughout
[N,N^{1+zeta}] would telescope to a log drop exceeding
(a+1)zeta log N+O(1). The assumed logarithmic arm law gives only
a zeta log N+o(log N). Hence good scales occur in each such interval.
Largest-cluster mass m^{d-a-o(1)}, sampled with mass/volume weight,
gives F(m^{d-a-o(1)})>=m^{-a-o(1)}. Monotonicity across these intervals
gives the lower tail exponent a/(d-a) at every large t.
The independent upper bound F(t)<=pi(n)+X(n)/t balances at
n=t^{1/(d-a)} and gives the same exponent. Finally, with
t=n^{(1-h)(d-a)}, pi(n)/F(t)=n^{-ha+o(1)} tends to zero, so
X(n)>=t(F(t)-pi(n)) gives exponent at least (1-h)(d-2a).
The endpoint-arm bound gives the matching upper exponent d-2a.
No error was found in the earlier theorem.

## Choice, recorded before proving the extension

Prove the reverse transfer left open in the round 3 report:

    (P) and X(n)=n^{s+o(1)}, 0<s<d
      => pi(n)=n^{-(d-s)/2+o(1)}.

This is one extension: it restores the original equivalence under the
weaker count hypothesis. Together with the verified round 3 theorem it
also supplies its volume-tail conclusion starting from X alone.

Reason: keeping squared component masses, rather than only their maximum,
appears to give an all-scale finite inequality

    pi(20m) <= pi(3m) P(J_m>L)
                  + sqrt(L X(8m)/V_{4m}).

Its error has the desired power whenever X has an exponent. Since
P(J_m>ceil(m^epsilon))->0, the recurrence on scales 8^j has arbitrarily
small contraction eventually. It may replace good-arm-ratio selection
entirely in the reverse argument. This choice does not presume the
recurrence is correct; the proof and audit below will check it.

## Proof saved

Saved PROOF.md with the finite bound

    pi(20m) <= pi(3m) P(J_m>L) + sqrt(L X(8m)/V_{4m}).

Its key improvement over the largest-mass argument is to retain
Q_m=sum s_i^2 for core masses of crossing B_{16m} components.
On {J_m<=L}, W_m^2<=L Q_m, and E Q_m<=V_{4m}X(8m).
The same independent buffered inner count bounds the bad-event part.

If X(n)=n^{s+o(1)}, set a=(d-s)/2 and L=ceil(m^h), 0<h<a.
The error is at most A m^{-a+h}. On m=8^j this gives
f_{j+1}<=q_j f_j+A r^j, r=8^{-(a-h)}, q_j->0.
Taking q_j<=r/2 eventually proves f_j<=C r^j by induction with
C>=2A/r. This supplies the previously missing upper bound on pi.
The opposite bound follows by subtracting X(3n) from X(N) with
N=ceil((3n)^{1/t}), t<1, and using separated endpoint arms.

The resulting reverse transfer is established without any bound on
E K_n or any assumption that pi has an exponent. The volume-tail
corollary then uses the independently checked predecessor theorem.
All writes used the patch tool in this directory. No computation
script or numerical percolation data is involved.

## 04:49–04:51 — audit and full proof reread

Command:

    OMP_NUM_THREADS=1 nice -n 15 sed -n '1,360p' PROOF.md

Output: the entire saved proof, reread; exit code 0, with the same
`nice: setpriority: Operation not permitted` warning. The clock command
`OMP_NUM_THREADS=1 nice -n 15 date '+%Y-%m-%d %H:%M:%S %Z'`
returned `2026-11-15 04:49:38 +04`.

Saved AUDIT.md. The quadratic estimate was independently reconstructed
using two uniformly sampled core vertices and
R sum s_i^2-(sum s_i)^2=sum_{i<k}(s_i-s_k)^2. Normalizing the pair
sum by V_{4m}^2 confirms the error sqrt(L X(8m)/V_{4m}).
Unrolling the recurrence as a geometric convolution independently
confirms f_j=O(r^j) and the factor 2A/r. Rechecked every radius,
the monotonicity pi(24m)<=pi(20m), all integer scales, and the exact
covering count in d=3 by two counts, both giving 3458.

The error exponent was re-derived both before and after taking square
roots: h+s+h-d=s-d+2h, hence -a+h. The volume-tail substitution was
also re-derived by solving s=d(delta-1)/(delta+1). Attempts to break
the argument covered component splitting and merging, repeated core
visits, nonmonotone bad events, rare huge counts, slow convergence
of their probabilities, nonregular arm ratios, endpoint s values,
and the order of limits. No invalid step was found.

## Report saved

Saved REPORT.md with first line `VERDICT: PARTIAL reverse exponent-existence
transfer under crossing-count control in probability`. It states the
new reverse theorem, its dependence on (P), and the volume-tail
corollary obtained from the verified predecessor theorem. It records
that no Z^3 input or exact value was proved, gives the text-verification
command and priority warning, and identifies the remaining geometric
target. No SOLVED_ELSEWHERE.md was created because no complete solution
was verified.

Final consistency command:

    OMP_NUM_THREADS=1 nice -n 15 rg -n '^(VERDICT:|## |Task:)|pi\(20m\)|f_\{j\+1\}|delta=' REPORT.md PROOF.md AUDIT.md LOG.md

Output confirmed REPORT.md line 1 has the required verdict, the finite
inequality agrees across the four files, and the volume-tail formulas
and task attribution are present. Exit code 0; the same priority warning
appeared. No mathematical claim changed during the final check.
