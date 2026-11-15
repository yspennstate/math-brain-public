# T222 work log

Task received: 2026-11-14, approximately 21:20 Asia/Tbilisi (17:20 UTC).
Request: "push this problem forward by one checkable piece" for Steele's
unscaled planar Euclidean TSP variance-limit conjecture.

## 2026-11-14 17:20–17:25 UTC: orientation and literature check

Read PROMPT.md, the compute governor state, the brain navigation index, and
the mesh protocol. The task-specific instruction confines every write to this
folder. Therefore no shared brain, checklist, mesh database, git, or external
application was mutated. No subagents were started.

Governor: status `warn`, mode `owner_away_open`, CPU saturated. No simulations
or heavy computation are planned. Shell reads were requested through
`env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c ...`; the sandbox printed
`nice: setpriority: Operation not permitted`. Process inspection was also
denied. This limitation must not be mistaken for a verified priority setting.

Web searches (web search tool, not a shell downloader):

- `Euclidean traveling salesman variance convergence Steele conjecture 2025 2026`
- `"traveling salesman" "variance" "limit" Steele Chatterjee`
- `"1706.04290" traveling salesman variance`
- `"traveling salesman" "variance convergence"`
- `"Euclidean" "TSP" "fluctuations" "2026"`
- `"Steele" "variance" "conjecture" salesman`
- `"traveling salesman" "Hoeffding" variance`
- `"travelling salesman" "noise stability"`
- `"Euclidean traveling salesman" "central limit theorem" 2025 2026 variance`

Opened primary sources:

- Sourav Chatterjee, *A general method for lower bounds on fluctuations of
  random variables*, arXiv:1706.04290, abstract and v3 HTML:
  https://arxiv.org/abs/1706.04290 and
  https://arxiv.org/html/1706.04290v3.
- Zhuolun Dong and Junyu Cao, *New Bounds for the Euclidean TSP Constant*,
  arXiv:2610.02809, abstract: https://arxiv.org/abs/2610.02809.
- Julia Gaudio and Charlie K. Guan, *An Improved Upper Bound for the
  Euclidean TSP Constant Using Band Crossovers*, arXiv:2602.11250,
  abstract: https://arxiv.org/abs/2602.11250.

The recent two papers concern the first-order constant, not convergence of
the unscaled optimal-tour variance. An attempted SSRN open returned 403;
that paper is not used as evidence. No closing theorem was found. The search
was bounded to less than ten minutes; absence from these searches is not a
proof of absence from the literature.

## Choice, recorded before carrying out the proof

Prove a quantitative reduction to the fixed-order Hoeffding interaction
energies of the *exact* Euclidean TSP length. The intended claim is a uniform
bound on the first moment of the interaction order, implying an explicit
tail bound for variance in orders greater than m. Consequently, convergence
of each fixed-order energy would imply variance convergence, with an
explicit truncation error. Also express the same reduction through covariance
under independent point resampling.

Why this piece: nearest-neighbor insertion bounds control one-coordinate
replacement without assuming that optimal tours stabilize. Combined with an
orthogonal product-space decomposition, this should isolate a precise
remaining convergence question and rule out variance escaping to interaction
orders that grow with n. It does not assume a CLT or confuse the optimal tour
with an approximation. The product-space ingredients are standard; no claim
of a new general decomposition is intended.

Initial target constant: 8, obtained from the candidate estimates
E[R^2] <= 2/n, insertion cost <= 2R, and the resampling energy identity.
These estimates and all factors of two remain to be checked in PROOF.md.

## Literature check closed; proof development

The Chatterjee v3 HTML was opened at the exact conjecture (Section 3,
problem (2)) and at its TSP discussion (Section 2.1). It explicitly asks for
the unscaled variance limit. The opened 2026 arXiv abstracts have the authors
listed above and concern first-order bounds. No further literature search
will be used this session. Search elapsed time was under ten minutes.

The geometric estimate has a short boundary-safe proof: for any x in the
unit square Q and 0 <= r <= sqrt(2), the homothetic square
`x + (r/sqrt(2))(Q-x)` lies in both Q and B(x,r), and has area r^2/2.
Thus the nearest-neighbor squared-distance tail is bounded by
`(1-u/2)^(n-1)` for 0 <= u <= 2; its integral is exactly 2/n.

Replacement of a point is the difference of two nonnegative insertion
costs. Each insertion cost is at most twice its nearest-neighbor distance.
The inequality `(a-b)^2 <= a^2+b^2` gives expected squared replacement
cost at most 16/n, hence total resampling energy at most 8.

Independent audit planned in the proof: derive 2/n using the order
statistics of the homothety gauge instead of the distance-tail integral;
derive 8 directly through conditional variance and deletion instead of
replacement. These are analytic checks and require no simulation.

## Proof saved and first audit completed

Saved PROOF.md. The result is a conditional reduction, not a proof of the
conjecture: the Hoeffding energies satisfy
`sum_j j V[n,j] <= 8` and
`sum_(j>m) V[n,j] <= 8/(m+1)` for every n. Fixed-order convergence would
therefore imply the required variance limit. A second version uses the
exact covariance C_n(rho) of optimal tours under independent retention of
each point with probability rho, with
`0 <= Var(L_n)-C_n(rho) <= 8(1-rho)`.

Independent checks already included in Section 5 of PROOF.md:

- Squared homothety gauges are uniform on [0,1]. The expected minimum of
  n-1 such variables is 1/n, giving E[R^2] <= 2/n without the distance-tail
  calculation.
- Conditional mean squared error relative to the deleted tour bounds the
  conditional variance by E[delta^2] <= 8/n. This gives energy <= 8 without
  using the resampling identity's factor of one half.
- A detour-and-shortcut proof checks insertion <= 2R independently of the
  edge-splice proof. A singleton base attains equality.
- Both variance tails in the rate comparison lie in [0,8/(m+1)], so their
  difference costs 8/(m+1), not twice that amount.

All checks so far are exact algebra or geometric arguments. There is no
Monte Carlo estimate, no numerical variance-limit estimate, and no executed
computation whose priority could be misreported after the sandbox denial.

An audit-file patch initially failed because its LOG.md context did not
match. It made no changes and was reapplied with the correct context.

## Refinement found during audit

The averaged nearest-neighbor moment has the exact elementary limit
`n E[R^2] -> 1/pi`. PROOF.md now proves this by an interior/boundary
sandwich; AUDIT.md re-derives it by dominated convergence of the scaled
distance tail. Since the energy estimate before its final simplification
is `sum_j j V[n,j] <= 4 n E[R^2]`, this gives
`limsup_n sum_j j V[n,j] <= 4/pi` and the sharper asymptotic tail bound
`limsup_n sum_(j>m) V[n,j] <= 4/(pi(m+1))`.

For every 0 < epsilon < 1/2 the proof also gives the finite-n certificate
`sum_j j V[n,j] <= min(8, 4/pi + 8(1-epsilon^2/2)^n + 32 epsilon)`.
The constant 4 multiplying the nearest-neighbor moment was checked again
using deletion and conditional variance. No approximation to pi or any
floating-point output is needed.

Exact analytic two-site Euclidean tour calculations in AUDIT.md check the
decomposition, resampling factors, noisy covariance, and binomial inversion
for all n, with explicit checks at n=2,3,4. These are checks of the
identities, not numerical evidence for the uniform-square conjecture.

An oscillating symmetric product-space example has energy at most 4 and
nonconvergent variance; it confirms that bounded energy alone cannot close
the conjecture. Another example shows that convergence of all fixed-order
energies is sufficient but not necessary.

Read-back command at 17:27 UTC:
`env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l LOG.md PROOF.md AUDIT.md; sed -n "1,110p" PROOF.md; sed -n "240,390p" PROOF.md; cat ~/.claude/compute/compute_state.json'`
(The actual shell body used newlines between commands.) At that point the
files had 125, 374, and 143 lines respectively, before this refinement.
The governor reported `ok`, mode `owner_away_open`. The sandbox again
denied setpriority; these were brief file reads, and no numerical program
was run.

## Deliverable and final audit

REPORT.md records `VERDICT: PARTIAL` and distinguishes the proved
quantitative reduction from the unproved fixed-order/noisy covariance
limits. PROOF.md also spells out the subsequential compactness argument
in the space of absolutely summable interaction spectra. This does not
give uniqueness of a limiting spectrum or prove the conjecture.

The analytic audit found no counterexample to the claimed reduction.
It explicitly found counterexamples to the tempting abstract inference
that bounded interaction energy forces variance convergence. The two-site
checks do not claim to simulate the uniform-square distribution.

Files: LOG.md (decisions, sources, commands, outcomes), PROOF.md (complete
argument), AUDIT.md (independent calculations and failure cases), REPORT.md
(verdict and next target). No claimed numerical dataset, no git, no external
writes, and no subagents.

Final read-back, 2026-11-14 17:29:51 UTC (21:29:51 Asia/Tbilisi):

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
sed -n "65,280p" PROOF.md
head -n 2 REPORT.md
rg -n "^##|VERDICT|limsup|4/pi|4\\\\pi" LOG.md REPORT.md AUDIT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
'
```

Output: REPORT.md begins with the required `VERDICT: PARTIAL` line.
Before this final log append, line counts were LOG.md 177, PROOF.md 452,
AUDIT.md 166, REPORT.md 96. Read back the refined geometric inequalities,
all factors in the energy argument, and the convergence passage. No
correction to the mathematical claims was needed. The shell returned zero
and again printed the sandbox setpriority denial. This session completed
the stated reduction and its analytic audit; it did not solve T222.
