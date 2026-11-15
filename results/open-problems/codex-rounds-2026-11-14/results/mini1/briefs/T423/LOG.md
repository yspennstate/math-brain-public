# T423 work log

Task received: 14 November 2026; session clock at start 22:14 Asia/Tbilisi (18:14 UTC).
Task: “push this problem forward by one checkable piece.”

## 1. Startup and literature check (18:14 UTC)

All writes will remain in this folder. No git, subagents, external posting,
global checklist, mesh registration, or brain updates: those last three would
write outside the folder, contrary to the task-specific restriction.
Read the brain navigation index and mesh protocol; consulted compute state.
Local commands use OMP_NUM_THREADS=1 and nice -n 15 from this point onward;
no numerical workload has been launched. The initial directory listing was
read-only and negligible.

Web search tool queries:
- `"super-Brownian" "pathwise uniqueness" 2025 2026`
- `"stochastic heat equation" "square root" "pathwise uniqueness" open problem`
- `"1008.2126" "1308.5141" uniqueness`

Initial hit: Hao Wang, arXiv:1612.06055, claims uniqueness in its indexed
abstract. This is a lead, not an accepted solution; checking the current
arXiv record and subsequent papers before drawing a conclusion.

The literature-search deadline is 18:24 UTC (ten minutes).

Opened arXiv pages 1008.2126, 1308.5141, and 1612.06055. The last
explicitly says “This paper has been withdrawn by Hao Wang”; it cannot be
used to declare the problem solved. Further queries:
`"super-Brownian" "pathwise uniqueness" "2024"`, the same with `2025`,
and `"1612.06055" withdrawn error`. A 2025 lead is arXiv:2509.10984,
Leonid Mytnik and Johanna Weinberger, about weak uniqueness with drift;
opening the actual paper to check its discussion of pathwise uniqueness.

Compute-state read: status warn, mode owner_away_open, CPU saturated,
62% free memory. No heavy computation is needed. `nice -n 15` emitted
`setpriority: Operation not permitted`; checking the inherited nice value
before any script runs (the parent may already be at the lowest priority).

At 18:15:33 UTC: Python reported inherited nice **20**, OMP_NUM_THREADS=1.
Thus the warning is an attempted priority increase from 20 to 15; the
actual processes are already below the requested priority. `ps` is denied
by the sandbox. No priority change or heavy run is needed.

Opened the full texts of 1008.2126 and 1308.5141, and the HTML and arXiv
record of 2509.10984v3 (12 August 2026). The withdrawn Wang record gives
the reason: a gap in the proof of its main theorem. Search queries also
included `"super-Brownian" "pathwise uniqueness" "2026"`,
`"super-Brownian" "pathwise uniqueness" local time mass difference`, and
`"super-Brownian" "pathwise uniqueness" solved` with secondary aggregators
excluded. No verified solution has appeared in these results.

## 2. Chosen piece (before proof work)

Prove an exact reduction, for a fixed pair of same-white-noise solutions
and deterministic horizon T, from equality of the full fields to equality
of their terminal total masses. Then express the remaining scalar condition
as vanishing expected local time at zero of the mass difference, with an
explicit occupation formula involving the spatial square-root discrepancy.
Include the quantitative bound controlling integrated spatial L1 distance
by the terminal mass difference in L2.

Why this piece: integrating the equation removes the Laplacian, while the
same-white-noise bracket retains the entire spatial discrepancy. The scalar
condition is exact and can be audited using Itô isometry and Tanaka's
formula. It does not assume that the Brownian motions driving the two
Feller mass diffusions are the same. It leaves a specific, genuinely
unproved occupation estimate for the original problem. This is a reduction,
not a claimed solution or a claim of novelty.

Planned attack on the result: check the local-time normalization by a second
smooth convex approximation; check the energy identity by the two-mass
covariance formula; test all putative profile-only bounds on equal-mass
disjoint smooth profiles. In particular Hellinger discrepancy cannot be
bounded by a function of the mass gap which vanishes at zero.

## 3. Literature check closed (18:16:36 UTC; about 2.3 minutes)

No verified resolution of the stated density-SPDE problem was found. This
is a bounded search result, not proof that no resolution exists.
Additional primary sources actually opened:
- Jie Xiong, 1203.4873, full PDF: page 5 explicitly explains that its
  different driving noise prevents transferring its uniqueness result to
  the density equation.
- Lina Ji, Jie Xiong, Xu Yang, 2303.05832, arXiv record and full PDF:
  martingale-problem uniqueness via a corresponding system of SPDEs.
- Jie Xiong, Wen Xu, 2610.41400, arXiv record: catalytic system with
  spatially colored noise and inward mutation/immigration assumptions.
- Yi Han, 2611.07310, arXiv record: weak uniqueness for uniformly
  nondegenerate diffusion, excluding the square-root boundary degeneracy.
Neither of the last two results states the theorem asked for here.
No SOLVED_ELSEWHERE.md will be written.

## 4. Proof draft saved (18:19 UTC)

Wrote PROOF.md. The essential bracket is
`<U-V>_T = integral_0^T integral_R (sqrt(u)-sqrt(v))^2`.
Itô isometry implies that equality of the two terminal masses almost
surely forces equality of the full fields on the entire preceding
interval. The precise scalar obstruction is the expected local time of
the mass gap at zero.

The piecewise quadratic convex approximation gives a stronger finite-width
statement: the occupation expression differs from `E|U_T-V_T|` by at most
`epsilon/2`. Checked the local-time factor separately with
`sqrt(z^2+delta^2)-delta`. A covariance expansion independently reproduces
the energy identity and the `2*m*T` upper bound.

Read back the saved proof with
`OMP_NUM_THREADS=1 nice -n 15 zsh -c 'sed -n "1,145p" PROOF.md; tail -80 PROOF.md; wc -l PROOF.md LOG.md'`.
The readback caught missing escape characters on some inline math
delimiters; repairing those before final audit. One attempted patch call
failed to parse because of JavaScript template quoting; it executed no
tools and changed no files. The next call corrected the quoting.

## 5. Adversarial audit

Checked the following independently on paper and included the derivations
in PROOF.md:

- Energy: direct white-noise isometry versus expansion of E(U_T-V_T)^2
  using both marginal second moments and the cross moment. Both give
  `2*m*T - 2*E integral C`.
- Local time: Tanaka with symmetric normalization versus Itô applied to
  the piecewise quadratic F_epsilon. A separate smooth approximation
  `sqrt(z*z+delta*delta)-delta` has a second-derivative kernel of total
  integral one after the Itô factor 1/2. No exchange of a singular limit
  and expectation is used.
- Finite-width error: outside the central interval it is epsilon/2;
  inside it is r-r*r/(2*epsilon), maximized at r=epsilon. This gives the
  independent two-sided occupation bound with error epsilon squared.
- Spatial bound: two Cauchy--Schwarz applications give the factor
  `2*sqrt(m*T)`; proportional profiles show that the underlying algebraic
  factor 2 cannot be decreased uniformly. This does not establish
  optimality over actual SPDE pairs.
- Mass zero and S=0: both are explicitly covered by nonnegativity.
  No inverse mass is used in the main proof.
- Fixed terminal time: equality is an almost-sure property of the pair,
  not an implication restricted to an event where the two terminal masses
  happen to coincide. Added this limitation explicitly.
- Full time interval: space-time almost-everywhere equality upgrades by
  joint continuity, including the endpoint T. Countably many integer
  horizons suffice for indistinguishability for all time.
- Extinction: optional stopping at an unbounded extinction time is not
  justified by the finite-horizon L2 estimates. It is not used.
- Marginal versus coupled law: only marginal mass continuity and first
  moments are imported from known weak uniqueness; the martingale and
  cross-bracket in the actual joint filtration are derived from W.

Failed closing argument: any bound of A by a mass-gap modulus vanishing
at zero is false for arbitrary smooth profiles. Disjoint translates and
equal-mass nearby mixtures give the exact values in (25)--(26). They do
not construct SPDE nonuniqueness. The general occupation estimate is
O(epsilon); the necessary little-o improvement is still unproved.

## 6. Final verification and handoff

Added an independent marginal normalization check: Itô formula for
`exp(-q_s*U_s)`, with `q_s=lambda/(1+(T-s)*lambda/2)`, yields
`E exp(-lambda*U_T)=exp(-m*lambda/(1+T*lambda/2))`.
Its first two Taylor coefficients give m and m*m+m*T, agreeing with
the separate mass-martingale isometry calculation.

Final readback/format check command (no numerical experiment):

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY'
from pathlib import Path
import re
proof = Path('PROOF.md').read_text()
report = Path('REPORT.md').read_text()
for opening, closing in [(r'\[', r'\]'), (r'\(', r'\)')]:
    count_open, count_close = proof.count(opening), proof.count(closing)
    print(f'delimiters {opening} {closing}: {count_open} {count_close}')
    assert count_open == count_close
labels = re.findall(r'\\tag\{([^}]+)\}', proof)
assert len(labels) == len(set(labels))
assert set(labels) == set(map(str, range(1, 28))) | {'24a'}
print('equation labels: 1 through 27 and 24a; all unique')
assert report.splitlines()[0].startswith('VERDICT: PARTIAL ')
print(report.splitlines()[0])
for name in ['LOG.md', 'PROOF.md', 'REPORT.md']:
    body = Path(name).read_text()
    print(f'{name}: {len(body.splitlines())} lines, {len(body.encode())} bytes')
assert not Path('SOLVED_ELSEWHERE.md').exists()
print('SOLVED_ELSEWHERE.md absent: no external solution claimed')
PY
```

Output before this final log append and a wording-only sign clarification:

```text
nice: setpriority: Operation not permitted
delimiters \[ \]: 34 34
delimiters \( \): 103 103
equation labels: 1 through 27 and 24a; all unique
VERDICT: PARTIAL exact reduction to terminal-mass equality and a scalar occupation estimate
LOG.md: 154 lines, 8377 bytes
PROOF.md: 453 lines, 14083 bytes
REPORT.md: 95 lines, 4493 bytes
SOLVED_ELSEWHERE.md absent: no external solution claimed
```

The analytic audit is in sections 2--5 of PROOF.md; the formatting check
does not verify mathematics. REPORT.md records the partial verdict and
the precise open estimate. No script, simulation, or data-driven result
is claimed. The next worker should seek an estimate using spatial
cancellation specific to actual coupled solutions, rather than an
inequality for arbitrary profiles. All intended artifacts are saved.
