# T119 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session opened 15 November 2026, approximately 01:31 Asia/Tbilisi; first shell
clock 01:31:47 +04.

## 1. Orientation and bounded literature check

Read the earlier REPORT.md, LOG.md, SOLVED_ELSEWHERE.md and directory listing
at `~/codex_op_1114/briefs/T119`. There is no PROOF.md and
there are no mathematical scripts in that directory. No earlier files edited.
Read the compute state: status `warn`, mode `owner_away_open`. Only tiny,
single-thread computations are planned. All writes stay in this directory;
shared checklist, mesh and brain tools that write elsewhere are excluded by
the task's explicit scope. Read the brain navigation/startup memory directly.

Commands use `OMP_NUM_THREADS=1 nice -n 15`. Although `nice` prints
`setpriority: Operation not permitted`, an independent
`python3 -c 'import os; print(os.getpriority(os.PRIO_PROCESS,0))'` reports
**20**. The inherited process priority is already lower than nice 15; the
denied operation attempts to raise it. No priority escalation is needed.

Web search (within the first five minutes):

- `random cubic graph independence ratio Harangi upper bound 0.450 2025 2026`
- `"2204.01353" independence bound cubic`

Opened and read these primary sources:

- Viktor Harangi, *Improved replica bounds for the independence ratio of
  random regular graphs*, arXiv:2204.01353v4,
  https://arxiv.org/abs/2204.01353 and
  https://arxiv.org/html/2204.01353 . Equation (3), Section 1.2, Tables 1–2.
- Balázs Gerencsér and Viktor Harangi, *Boosted second moment method in
  random regular graphs*, arXiv:2510.12600v3 (12 March 2026),
  https://arxiv.org/abs/2510.12600 and
  https://arxiv.org/html/2510.12600v3 . Abstract and introduction: new
  lower bounds beat previous results for degrees at least 10, while the
  small-degree constant is still unresolved.
- Harangi's accompanying examples page,
  https://www.renyi.hu/~harangi/rsb.htm . It lists the cubic 5-RSB value
  0.450785209433452, consistent with the earlier report's rounded bound.

No solution of the cubic problem found. This is a short search, not an
exhaustive literature claim. The earlier report's interpretation of the
early-stop rule as applying to any improvement is too broad: the current
instruction says stop if the problem was solved elsewhere. Continue.

Next: independently evaluate the four-atom expression, before selecting
the extension. Its exact parameters, from Section 1.2, are
lambda=19.3, m=.557, p=(.2493,.2778,.2880,.1849),
q=(.1184,.5947,.8876,.9827).

Initial `recheck.py` launch failed before arithmetic: setting RLIMIT_AS to
768 MiB raises `ValueError: current limit exceeds maximum limit` on this
Mac. Investigating the platform limits; this is a resource-guard failure,
not a failed bound. The expression has only 80 terms and needs negligible
working memory.

## 2. Independent recheck of earlier claim

Command:
```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck.py
```
Output (exit 0):
```
nice = 20
ordered star terms = 64; ordered edge terms = 16
V = 1.3378720687134031
E = 0.73974606806929843
B = 0.45078995170969816
0.450789952 - B = 2.90301838124e-10
peak RSS bytes = 12615680
```
The earlier explicit four-atom claim holds in this independent ordinary
floating-point substitution. Its margin is only 2.9e-10, so this is not yet
a rigorous numerical certificate. The stronger 5-RSB number was checked
against the primary sources but has not been independently computed here.
The resource guard was changed to report and check actual peak RSS; the
failed address-space guard was removed. The workload is fixed at 80 terms.

## 3. One selected extension

**Choice:** certify the explicit four-atom witness by exact rational
interval arithmetic, including all fractional powers and logarithms.
This is the earlier report's named next step. It turns a documentary
claim into a reproducible numerical proof without an optimization search
or reliance on an interval library's transcendental rounding.

Plan: replace ordered tuples by nondecreasing tuples with exact multinomial
weights (20 star terms and 10 edge terms). For x>0, m=557/1000 and a fixed
integer grid S, enclose x^m between a/S and (a+1)/S using only integer
power comparisons. Enclose logarithms by range reduction to [1,2] and
the positive atanh series with an explicit rational remainder. Propagate
lower and upper endpoints through the quotient. Independently audit tuple
counts, weight normalization, degenerate measures and endpoint inequalities.
No improvement of Harangi's upper bound or solution of T119 is claimed.

First exact certificate run:
```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 certify.py
```
Exit 0, 0.512 seconds, peak RSS 17,268,736 bytes, nice 20.
```
V in [1.33787206871340330777, 1.33787206871340330878]
E in [0.73974606806929845498, 0.73974606806929845599]
B in [0.45078995170969821614, 0.45078995170969821783]
0.450789952 - B in [0.0000000002903017821710, 0.0000000002903017838543]
CERTIFIED: alpha_3 <= B < 0.450789952
exact power brackets checked = 30
```
All displayed endpoints are rounded outward. The ordinary floating result
differs by about 6e-17, as expected; it was not used in the certificate.
Next: audit the certificate with identities and degeneracies, and evaluate
the original ordered sums independently at 70 and 110 Decimal digits.

## 4. Attempts to break the certificate

Commands (all programs one thread; inherited nice 20):
```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 certify.py --audit
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 certify.py --digits 24 --series-terms 64 --audit
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_decimal.py
```
All exit 0. Default certificate plus audits: 0.621 seconds, peak RSS
17,301,504 bytes. Refined certificate plus audits: 1.072 seconds, peak RSS
17,154,048 bytes. Decimal audit peak RSS: 17,645,568 bytes.

Refined certificate output:
```
V in [1.33787206871340330831, 1.33787206871340330832]
E in [0.73974606806929845553, 0.73974606806929845554]
B in [0.45078995170969821695, 0.45078995170969821696]
0.450789952 - B in [0.0000000002903017830494, 0.0000000002903017830495]
CERTIFIED: alpha_3 <= B < 0.450789952
exact power brackets checked = 30
audit: grouped/ordered weights, 2/3-fold counts, integer root boundaries,
       power inequalities, log identities, degenerate measures, 1-RSB PASS
```
The refinement addresses possible sensitivity to the root grid or the
logarithm tail truncation. Every root is checked by direct integer
cross-multiplication against the original rational base, not just the
integer-root routine's intermediate target. The grouped sum is compared
with an independent ordered enumeration as a dictionary of exact rational
bases and weights. Degenerate measures q=0 and q=1 give respectively 1 and
3/2; a single interior atom agrees with the rational-log 1-RSB expression
after cancellation of m. The logarithm identities at 1, 1/2, 2 and 4 check
the sign change under negative range-reduction exponents.

Independent Decimal values (110-digit working precision; abbreviated here):
```
V = 1.3378720687134033083163606606006400324890363276915404419207418513402855451167478068770747303930492937455356145
E = 0.73974606806929845553310935967953078982249911206358215429073117432020037137913921548005945344413509769462072814
B = 0.45078995170969821695059434974724250867957127380982733517769400686301992262547894290821405060466397653504097154
Decimal values inside exact intervals: grid 10^-18, N=48 PASS
Decimal values inside exact intervals: grid 10^-24, N=64 PASS
70/110-digit agreement within 1e-67 PASS
```
The Decimal audit uses all 64 star and 16 edge terms, evaluated via exp(m log x).
The certificate uses 20 and 10 grouped terms and integer root brackets.
Decimal transcendental routines are only a cross-check, not part of the proof.

The numerical claim survived these checks. PROOF.md will give the exact
input, the inequality being applied, the interval construction and the
error propagation. Limitations: no optimization, no independent
reproduction of the stronger 5-RSB witness, no lower-bound audit, and
no determination of alpha_3.

## 5. Written result

Saved PROOF.md with all numerical enclosure steps and REPORT.md with
verdict COMPUTED. The certificate reproduces a published four-atom bound;
it is new verification beyond the earlier report, not a new extremal
bound. The exact value of alpha_3 remains unresolved. Recommended next
step: certify the strongest 5-RSB witness using the author's example 11.
