# T133 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, 11:03 Asia/Tbilisi (07:03 UTC).

## Orientation and literature check

Read the original, round 3, round 4 and round 5 reports, logs, proofs and
scripts. The original directory has no PROOF.md or scripts. Earlier
directories remain read-only. The task-specific restriction to this
directory excludes the global brain, checklist and mesh commands, which
write outside it. Startup memory was read directly from the project memory
index (the first attempted ~/.claude/MEMORY.md path did not exist). Read the
compute governor: warn, owner_away_open, CPU saturated. No subagents, git,
external writes or long workloads.

The literature check took less than five minutes. Queries:

- `six vertex arctic curve proof Bufetov 2609.20576`
- `six vertex domain wall arctic curve disordered regime proof 2026`

Opened https://arxiv.org/abs/2609.20576 and
https://arxiv.org/html/2609.20576v1. Alexey Bufetov, *Limit shape for
domain-wall six-vertex model*, still has only v1 in the submission history.
The abstract calls it an announcement. Theorem 3.2 covers
-1 < Delta <= 1/2; Remark 3.3 excludes 1/2 < Delta < 1. This matches
the earlier literature finding. No changed status or full solution was
found in this bounded check; no broader absence claim is made.

## Earlier-result audit, before extending

Recheck the exact gamma=pi/4 curvature certificate with the earlier
standard-library integer verifier, copied here so its output stays here.
This is independent of the earlier SymPy derivation. Also compare the
new endpoint calculations against derivatives of the original trigonometric
coefficients, rather than relying only on their rational representation.

Planned extension, to begin after the recheck passes: compute and match
all four joining-point limits at gamma=pi/4 for arbitrary 0<u<3pi/4.
Use the already proved strict curvature on the open arcs to decide whether
the completed candidate curve is simple, smooth and convex. Joining the
Fredholm critical-branch coordinates is a separate question: their
interior expansions need not be uniform at the joins.

## Exact recheck passed; extension selected

Copied `audit_certificate.py` and `certificate.json` byte for byte from
round 5, then ran (all output paths resolve to this directory):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_certificate.py
```

Output: PASS integer numerator identity and all coefficient signs;
1211 numerator monomials; 324 positive coefficients; minimum 63;
maximum 692394213766656; sum 17765219441341512. Runtime 0.024 s,
peak RSS 15.66 MiB, effective nice 20. The earlier curvature theorem
holds on this exact recheck. The inherited nice 20 explains the shell's
warning when it tries to set nice 15; the program runs at lower priority.

Selected extension: joining-point completion and global convexity of the
candidate curve at Delta=1/sqrt(2), for every positive weight ratio. The
open-arc certificate alone does not settle the pole cancellations or
matching across the joins, so this is a distinct missing geometry step.

First analytic reduction: writing h=4/3, delta=3pi/4, T=delta-u,
the southwest endpoints are expected to be (0,kappa(u)) and
(kappa(u),0), where
`kappa(u)=sin(u)sin(T)/sin(delta) * [cot(T)-h cot(hT)]`.
The identity h(u+T)=pi gives kappa(u)+kappa(T)=1. Next check the
nonzero endpoint speed and compare the graph curvature from both sides.

## Endpoint jets computed exactly

Wrote `derive_joins.py`: divide the tangent equation by its singular
coefficient b, then differentiate the regular rational coefficients.
Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B derive_joins.py
```

Exit 0, 24.21 s, peak RSS 77.94 MiB, nice 20. Full expressions are in
`endpoint_formulas.json`. The endpoint has y=y'=0. The contact formula
satisfies kappa(z)+kappa((1-z)/(1+z))=1, exactly, and the two endpoint
graph curvatures agree under the same substitution. Here z=tan(T/3).
The speed is a positive prefactor times -P(z), with an explicit degree-8
polynomial P. Its sign and an independent trigonometric derivation are
the remaining checks before claiming smooth completion.

The candidate boundary can have a geometric normal collar without proving
that the Fredholm critical-parameter charts extend across joins. The latter
has not been established by these endpoint calculations.

## Independent endpoint and sign audits passed

Wrote `verify_joins.py`, independent of the SymPy derivation. It uses
truncated power series with exact Fraction coefficients at 29 rational
values of z. It reconstructs the envelope from the regular coefficients,
checking contact, first and second jets, complement matching and graph
curvature. A separate standard-library polynomial calculation verifies
the entire endpoint-speed rational identity, coefficient by coefficient.
The sign certificate is

`(1+r)^8 H(r/(1+r)) = 21+357r+2191r^2+6930r^3+12688r^4`
`+13860r^5+8764r^6+2856r^7+336r^8`.

Every coefficient is positive. Ten independent high-precision evaluations
of the original trigonometric formulas include u/delta=10^-6 and
1-10^-6. They verify contact limits, nonzero speed, quadratic height at
the join and matching curvature. Fifty interior samples also check the
strict rectangle/chord bounds used for nonintersection.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_joins.py
```

Output: PASS 29 exact series checks; PASS full integer endpoint-speed
identity and positive-coefficient transform; PASS 10 trigonometric checks.
Maximum relative endpoint-limit error 2.6004e-12; runtime below 0.5 s,
peak RSS below 22 MiB, effective nice 20. Data: `join_checks.json`.

Adversarial smoothness check: the equal-weight graph has southwest
one-sided third derivative
`-(4168422 sqrt(2)+494262)/1803649 = -3.542430332118046`.
Reflection changes its sign on the southeast side. Thus C2 is the correct
general smoothness conclusion; analytic or C3 gluing would be false.
The exact value comes from SymPy endpoint jets and is also checked against
the separate series construction. The first series implementation of the
third-derivative audit missed a factor 2 in a chain-rule term; corrected
before using it, then verified equality with the rational jet at all 29
exact test points. No contact, speed or curvature calculation was affected.

## Proof completed and attempted stronger conclusions checked

Wrote PROOF.md. The second graph derivative at a southern contact is
`K=pi*a0^2/d`, where
`8pi*d = (2/3)(h^2-1)-M(T)M(u)` and
`M(t)=cot(t)-h*cot(ht)`.
Both d and a0 are invariant under u<->T; this independently proves the
curvature match. Positivity of d is established by the full polynomial
speed identity and the positive coefficient transform above.

For simplicity, each arc lies strictly below its endpoint chord in its
own reflected coordinate system. Adjacent arcs have disjoint coordinate
ranges; opposite arcs are separated by strict x+y or x-y inequalities.
The tangent angle increases by exactly 2pi. A direct supporting-line
argument in PROOF.md proves strict convexity, without presuming that a
picture of the candidate encloses the model's liquid region. Compactness
and local invertibility of the inward normal map give a uniform positive
geometric collar width for each fixed u.

At equal weights the third derivative has a shorter second derivation:
`v=(41-13sqrt(2))/54`, `a0=(sqrt(2)-1)/(2pi)`,
`x''=v/2`, and the third graph derivative is
`-3(sqrt(2)-1)/(2v^2)`. This agrees exactly with the symbolic expression.
A further derivative calculation from the original trigonometric envelope
at distance 10^-12 from the contact gives absolute error 5.1957e-12.
The final verify_joins.py run took 0.42 s and 19.85 MiB; all checks passed.
The last symbolic derivation run took 25.16 s and 73.83 MiB. Both measured
nice 20 and configure one thread.

The result stops at C2 geometry and its ordinary normal collar. The earlier
small-B Fredholm expansion is only uniform on compact open subarcs, so
claiming its charts glue at these joins would leave an unproved limit
interchange. No such claim is made. REPORT.md records the concrete next
target: joint B/endpoint asymptotics for those charts.

## Final artifact audit

Ran a small Python heredoc under the same environment/nice prefix. Parsed
all three scripts with ast.parse; checked Markdown for control characters;
checked the report verdict, JSON check counts, sign coefficients, endpoint
errors and exact third derivative; and compared both inherited files byte
for byte with round 5. Output:

```text
syntax OK: audit_certificate.py
syntax OK: derive_joins.py
syntax OK: verify_joins.py
inherited file unchanged: audit_certificate.py
inherited file unchanged: certificate.json
PASS final syntax, artifact, copied-source and numerical-summary audit
```

The copied-file SHA256 values are
`6fb9fd605d49fa4aea1dce26c580d54afd747dd51b2c0048507453dc1a9cec8e`
and `49e6de1cbd9ee196945edd4a16616863eafa814213e5f8395501fa0e8b7ae22f`,
respectively. No additional mathematical tests were needed after this audit.
Final result: C2 globally convex completion at Delta=1/sqrt(2), with a
geometric collar; not a limit-shape proof or a Fredholm endpoint theorem.
