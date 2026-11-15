# T075 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: 2026-11-15 00:37:30 UTC = 04:37:30 +04:00.

## Scope and orientation

All deliverables stay in this folder. No git, subagents, external messages,
shared checklist, mesh, or memory writes are authorized by this task's narrower
scope. Read the startup memory and recalled the Bernoulli-convolution area.
The recalled work distinguishes convolution powers from the original measure;
it is not evidence of absolute continuity of the original measure.
Compute state: warn / owner_away_open, CPU saturated; only small one-thread
computations are planned. Python commands use OMP_NUM_THREADS=1 and nice -n 15.
The inherited priority is already 20, explaining nice's setpriority warning.
The initial recall reported a failed automatic detached index-refresh
attempt. No further brain commands were run; orientation subsequently used
read-only files.

## Read earlier work

Read REPORT.md, LOG.md, and SOLVED_ELSEWHERE.md in the first folder (which has
no PROOF.md or scripts). Read REPORT.md, LOG.md, PROOF.md and the entire
prefix_concentration.py in the round-3 folder. Neither folder is edited.

## Literature check in progress

Web queries:

- Bernoulli convolutions transcendental absolute continuity November 2026 Kittle Kogler 2611.17277
- "Bernoulli" "transcendental" "absolute continuity" 2026

Opened Samuel Kittle and Constantin Kogler,
*On L^p density of self similar measures and Bernoulli Convolutions*,
https://arxiv.org/abs/2611.17277 and
https://arxiv.org/html/2611.17277v1.
Theorem 1.1 assumes absolute continuity. It does not solve T075.
A search also surfaced an October 2026 arithmetic-classification preprint;
its source is being checked within the five-minute literature budget.

The opened source of *An arithmetic criterion for the measure type* in the
October classification preprint gives an infinite algebraic-approximation
criterion for singularity. It does not assert that transcendental parameters
avoid that criterion. No solution of T075 was located. No theorem from this
source is used below. Literature checking ends here, within five minutes.
Source opened:
https://github.com/openai/math/blob/main/preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/build/classification.tex

## Earlier result independently rechecked

Re-derived the qualitative criterion as follows. The absolutely continuous and
singular parts of an invariant probability are separately invariant, because
the two similarities preserve Lebesgue type. Uniqueness of the invariant
probability implies pure type. If the limit measure is singular, a compact
null set carrying mass arbitrarily close to one has an open neighborhood of
arbitrarily small length. Weak convergence puts asymptotically that mass in
the neighborhood, so A_n(delta) tends to one. If the limit is absolutely
continuous, condition on each prefix: a uniform kernel of radius 2r_n,
convolved with the actual measure, is at least f_n/2. Integrating over an
arbitrary set gives A_n(delta) <= 2 omega_nu(delta). This verifies both
directions without assuming strong convergence of f_n.

Re-derived the geometric constant independently: choose cylinder length
D lambda^k <= r < D lambda^(k-1). Then lambda^k > lambda r/D,
so a preimage of E has length at most (2D/lambda)|E|/|B|.
Cylinders meeting B lie in 2B. Hence epsilon=delta lambda/(4D)
is valid after obtaining omega_nu(delta/2)<=theta.
The opened Lemma 2.1 has C=18 in dimension one; substitution reproduces
the earlier exponent with denominator log(72D/(delta lambda)).
The earlier result holds.

Reran the original script read-only:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T075/prefix_concentration.py > earlier_recheck.txt 2>&1
```

Full output is saved locally in earlier_recheck.txt. The independent
midpoint/dual tests and the disjoint/tiled exact-formula tests are the
original script's internal independent computations; the analytical
re-derivation above is independent of the script.

## Choice before extension

Choose one sharper-constant extension: replace the one-dimensional covering
step behind the conditional L^p result. Finite intervals admit a subcover
of multiplicity at most two, avoiding the dilation by three in the earlier
analytic lemma. Derive an explicit recurrence with a tunable level c>1,
then apply the already rechecked localization. The intended gain is a
conditional threshold theta<1/4 instead of theta<1/18, with explicit
exponents. This does not establish the infinite-subsequence hypothesis.
The proof will be self-contained, including the covering argument and
integrability step. Check the constants by exact rational arithmetic and
direct interval examples, and recover the earlier exponent as a control.

## Recheck output and proof saved

Original script exited 0: 72 midpoint/dual comparisons and 112 disjoint/tiled
formula comparisons passed. All twelve displayed caps reproduced exactly.
Elapsed time 1.350 s, peak RSS 36,716,544 bytes, actual priority 20,
OMP_NUM_THREADS=1. Output: earlier_recheck.txt.

Wrote PROOF.md. The new analytic recurrence is

    F((c/epsilon)t) <= [4c eta/(c-1)] F(t),
    F(t) = integral over {h>t} of h,

for large t, whenever the local small-set implication holds with eta.
The factors are: dilation by two, overlap multiplicity two, and c/(c-1)
from splitting h at height t. There is no claim that the dilated intervals
have bounded overlap. Their averages, rather than their multiplicity,
control their integrals. The original intervals have multiplicity two.
For eta<1/4 choose c>1/(1-4eta); then the recurrence contracts.
Layer-cake integration proves all p with

    [4c eta/(c-1)] (c/epsilon)^(p-1) < 1.

This is a conditional improvement in constants and in the admissible
concentration threshold. It supplies no concentration estimate at a new
parameter. No assertion at the endpoint exponent is made.

Wrote check_constants.py and started:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 check_constants.py > computation.txt 2>&1
```

The script checks interval covers with exact endpoints, reproduces the
earlier caps in integer coordinates, and compares the exponent arithmetic
using binary logarithms and independently 60-digit Decimal logarithms.

## Computation output

Exit code 0. Full output is in computation.txt:

```text
priority 20
OMP_NUM_THREADS 1
exact open-interval covering families 4943 passed
integer-coordinate prefix cap comparisons 12 passed
tunable recurrence/exponent checks 18 passed
example epsilon 1/2304 H 4608 Gamma 2/9
earlier p 1.065189685675672
new p, formula (5) 1.130236012180298
fixed-c endpoint, excluded 1.178302249289551
new p, formula (4) 1.094082508877522
exponent improvement grid 1000 passed
WARNING: no infinite-subsequence concentration bound was checked
elapsed_seconds 0.125
peak_rss_bytes 21069824
```

The exact covering checks enumerate every nonempty family of up to five
open intervals with endpoints among 0,...,5. Endpoints and intervening
cells are both checked. These are finite checks of the elementary lemma,
not a substitute for its proof. The integer-coordinate computation uses
the same proven overlap-sorting formula as the previous script, but
independent integer endpoints and direct binary-word enumeration.

## Attempts to break the proof

1. Covering: if three retained intervals meet at a point, absence of
containment puts both their left and right endpoints in the same strict
order. The middle interval lies in the union of the outer two. This
contradicts irredundancy. Equal endpoints and nested intervals are
removed before this argument. Open endpoints cause no gap because the
outer intervals overlap at the common point. The selection covers the
entire original union, so it still covers the compact set.
2. The intervals 2B_i may have arbitrarily large multiplicity. The proof
never bounds that multiplicity; it bounds each doubled-interval integral
by its own average at the maximal radius. Only the undoubled B_i are
used for the multiplicity-two bound.
3. Independently normalize t=1 in the recurrence calculation. A selected
interval of length L has mass cL, so its mass above level one is at
least (c-1)L. Multiplicity two gives total length at most 2F(1)/(c-1).
The local hypothesis contributes at most 2c eta times that length.
The product is 4c eta/(c-1), agreeing with the direct derivation.
4. Algebraically, 4c eta/(c-1)<1 iff c(1-4eta)>1. Thus eta<1/4 and
c>1/(1-4eta) suffice. This does not establish optimality or show the
endpoint eta=1/4 is impossible by other methods.
5. A largest average-critical radius exists: averages are continuous for
positive radii, exceed ct at sufficiently small radii at the chosen
Lebesgue point, and are at most ||h||_1/(2r) at large radii. Maximality
therefore bounds every dilated average. The radius of B_i, not 2B_i,
needs to be below one in the local hypothesis.
6. The strong-L^p endpoint is deliberately excluded. The argument requires
Gamma A^(p-1)<1. Formula (4) has product sqrt(Gamma)<1, and formula (5)
has product exactly 2/3. These are inside the proved range.
7. Sample arithmetic re-derived directly from c=2 and epsilon=1/2304:
A=4608 and Gamma=8/36=2/9. Independently, 8D/(delta lambda)=4608.
The gain log(3)/log(4608) makes A^(p-1)=3, so the multiplier is 2/3.
The old denominator is nine times the new one: 41472=9*4608.
Decimal logarithms at 60-digit precision agree with binary logarithms.
8. The zero-length preimage inequality remains non-strict. Cylinders
meeting an open B lie wholly in open 2B even when their diameter equals
r, since the point of intersection is strictly inside B.
9. The singular control lambda=1/3 has A_4(1/64)=27/1024<1/36, yet
A_14(1/64)=1. It therefore also defeats using the stronger finite-depth
threshold proposed here as an unconditional test. This example lies
outside the interval of T075 and tests the all-parameter conditional
theorem only.

What did not advance: no propagation bound on A_n(delta) was obtained.
No new parameter is certified absolutely continuous. The extension is a
sharper conditional theorem, and its method may overlap existing sharper
one-dimensional reverse-Hölder estimates. No priority claim is made.

## Final audit and report

Saved REPORT.md with VERDICT: PARTIAL and the exact conditional claim.
No SOLVED_ELSEWHERE.md is created because no solution was located.

Final read-only command: `OMP_NUM_THREADS=1 nice -n 15 python3 -` with
an inline audit checking all six deliverables, parsing check_constants.py,
balancing the proof's math delimiters, checking the verdict and strict
endpoint, and independently verifying the exact example constants.
In particular c=9/4 in formula (4) gives H=5184 and Gamma=1/5;
c=2 in formula (5) gives H=4608 and Gamma=2/9, with multiplier 2/3.

Output:

```text
Final audit passed: deliverables, script syntax, delimiters, strict endpoint, and exact constants.
Local deliverable bytes 33355
```

Exit code 0. The first attempt to append this final audit used an unmatched
patch context and made no change; the corrected append succeeded.
Final recorded clock: 2026-11-15 00:46:03 UTC (04:46:03 +04:00).
No tests or proof changes remain pending.

