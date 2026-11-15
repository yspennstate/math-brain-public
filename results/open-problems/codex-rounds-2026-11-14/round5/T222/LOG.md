# T222 work log

Task: "take the NEXT checkable step on this problem, building on that work."
Start: 2026-11-15 08:41:50 Asia/Tbilisi (04:41:50 UTC).

## Orientation and reads

All writes are confined to this folder. This task-specific restriction
precludes shared mesh, checklist, recall logging, or brain-memory writes.
No git, subagents, external messages, or heavy computation.
Read the startup memory, memory index, and compute state directly.
Governor reports warn / owner_away_open with CPU saturation.
Shell reads use `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`.
The sandbox prints `nice: setpriority: Operation not permitted`; no
successful priority adjustment is claimed. The first inventory was only
short file reads and did not use that prefix.

Inventoried all three predecessor directories with `rg --files`.
They contain REPORT.md, LOG.md, PROOF.md, AUDIT.md and runner/transcript
files; no mathematical scripts. Read the mathematical documents in
the original, round 3, and round 4 directories. All are read-only.

## Bounded literature check

Used the web search tool for the following queries:

- `"traveling salesman" "variance" "limit" Euclidean Steele 2025 2026`
- `"Steele" "variance" "conjecture" traveling salesman`
- `"Euclidean" "TSP" "variance convergence"`
- `"traveling salesman" "variance" "2026" limit theorem`
- `"travelling salesman" "variance" Steele limit constant`

Opened Sourav Chatterjee, *A general method for lower bounds on
fluctuations of random variables*, arXiv:1706.04290v3,
https://arxiv.org/html/1706.04290v3. Section 3, problem (2), still
states exactly the requested variance-convergence problem. Searches
found no closing theorem. A Dagstuhl report hit concerning points in a
disc was checked before ending this bounded update check. Opening the
30 MB PDF failed with the web tool's content-length error. It is not used
as a reference or evidence. No closing theorem found in this bounded
check; no SOLVED_ELSEWHERE.md is warranted. No further literature search
will be made.

## Independent verification of the earlier main claim

For a deleted (n-1)-point sample S and an independent replacement pair,
half the expected squared tour difference is E Var_X(d(X;S)|S).
The Hoeffding residual identity therefore gives
`E_n = n E Var_X(d(X;S)|S)` with no extra factor two.
The insertion interval is `0 <= d <= 2R`, and moving the inserted vertex
gives 2-Lipschitz continuity. Centering at c/sqrt(n) yields the earlier
endpoint envelope `H_c(r)=max(c^2,(2r-c)^2)`.

Re-derived the round 4 deficit by translation, independently of its
all-pairs integration. Its disks have scaled radius c/8 and centers
5c/8 and 11c/8. Translation moves points by 3c/4, so the Lipschitz
increment is at most 3c/2. On the disks the two deficit factors have
coefficient at least c/2, while the endpoint gap is at least 5c/2.
The pair deficit is thus at least c^2/2; multiplying by disk area
pi c^2/(64n) gives pi c^4/(128n). This is stronger than the stated
pi c^4/(256n), so it validates that conservative constant.
The disjoint supporting disks have radius 3c/(2sqrt(n)). The expected
isolated-point count divided by n tends to exp(-9pi c^2), since there
are n-1 candidate sites and n-2 avoiding points. Thus round 4's main
claim `limsup E_n <= F(c)-(pi*c^4/256)exp(-9*pi*c^2)` holds.
Recomputed F through W=pi Z^2 exponential and truncated first/second
moments, recovering both coefficients 4/pi and -2c erfc(sqrt(pi)c).
No error found in the three earlier results.

## ONE extension chosen before writing its proof

Target the suggested first-order term, including its boundary dependence.
Write `U_n(x)=sqrt(n) E[d(x;S)]` and `mu_n=integral_Q U_n`.
Then `V[n,1]=Var_X U_n(X)` exactly. Prove a boundary-exclusion lemma
and a sharp scalar range bound for this particular projection:

`V[n,1] <= mu_n(1-mu_n)+o(1) <= 1/4+o(1)`.

Reason: Jensen and nearest-distance tails give `0<=U_n<=2sqrt(2)`
everywhere, but `U_n<=1+o(1)` uniformly a shrinking distance away from
the boundary. A boundary strip therefore contributes o(1) to the
normalized first-order variance, without stabilization of optimum tours.
This gives a concrete answer to the boundary part of the prior report's
next target. It does not assert interior homogeneity or V[n,1] convergence.
Combining this one new estimate with the verified energy bound will also
give the automatic consequence `limsup Var(L_n)<=(K+1/4)/2`.

Use explicit strip width `a_n=sqrt(8 log(n)/n)` for sufficiently large n.
Derive all estimates analytically; no simulation or numerical program.

## Proof saved

Saved PROOF.md with the exact first-projection identity, the uniform
bound U_n<=2sqrt(2), an explicit interior error delta_n(a), and
boundary-exclusion inequalities. The main new conclusions are

`V[n,1] <= mu_n(1-mu_n)+O(sqrt(log(n)/n))`,
`limsup V[n,1] <= 1/4`, and
`|V[n,1]-Var(U_n(X) | X in [a,1-a]^2)| <= 8(4a-4a^2)`.

The centered squared first-projection contribution on the excluded strip
also has upper bound 8(4a-4a^2). The normalization sqrt(n) has already
been absorbed into U_n; no missing factor n belongs on these errors.
The strip result holds for every shrinking strip, independently of
the extra condition needed to bound the interior range by 1+o(1).

The nonnegative spectral identity gives
`2 Var(L_n) <= E_n+V[n,1]`, hence
`limsup Var(L_n) <= (K+1/4)/2` with the previously verified K.
This is strictly smaller than K: the averaged two-endpoint square gives
F(c)>=2/pi-1/4, and t^2 exp(-t)<=4/e^2 gives
eta(c)<=1/(5184*pi*e^2). Therefore K>1/4 by rational inequalities.
All constants were derived analytically. No claim about optimal published
upper bounds, variance convergence, or a limiting variance value.

Next audit: derive the first-projection bound directly through replacement
pairs and through pointwise nearest-distance moment convergence. Check
the boundary comparison with arbitrary different conditional means,
the small-n restriction on a_n, and the spectral factor two. Construct
an oscillating profile example to test the scope of the conclusion.

## Sharper error during the audit

The same first-projection argument permits an integrated boundary estimate,
so sharpened the main error from O(sqrt(log(n)/n)) to O(n^{-1/2}).
This remains the one chosen extension. With s(x)=dist(x,boundary Q), set
`D_n(x)=2 sqrt(n) integral_[s(x),infinity) exp(-(n-1)r^2/2) dr`.
The split-tail bound gives U_n<=sqrt(n/(n-1))+D_n. Tonelli and
`|{s(x)<=r}|<=4r` yield `integral D_n <=8 sqrt(n)/(n-1)`.
Since `U_n^2-U_n <=2sqrt(2)(U_n-1)_+`, the improved explicit error is

`epsilon_n=2sqrt(2)(sqrt(n/(n-1))-1+8sqrt(n)/(n-1))`.

Saved this strengthening as (5a) in PROOF.md. The strip comparison remains
available for every shrinking width, while no strip choice is needed
for the O(n^{-1/2}) first-projection bound. The earlier strip calculation
is retained as an explicit uniform-interior estimate and cross-check.

## Audit complete and final artifact check, 08:49 Asia/Tbilisi

Saved AUDIT.md and REPORT.md. The independent pointwise tail argument
confirms limsup V[n,1]<=1/4 without the shrinking-strip estimates.
Replacement pairs confirm the projection normalization. Homothety gauge
order statistics confirm the global bound 2sqrt(2). Total variance with
two distinct conditional means confirms the boundary comparison. Summing
the four sides independently confirms the integrated coefficient 8.
The n=2 case, overlaps at corners, signs, n-1 factors, and rate all pass.
Exact spectral subtraction confirms `2 Var <=E+V1` and the rational
comparison verifies K>1/4. No mathematical error was found.

Artificial square-symmetric continuous profiles q and q/2 have variances
2/45 and 1/90, respectively, despite satisfying the derived range and
boundary controls. This checks that no convergence claim follows from
those controls alone. They are explicitly not TSP insertion fields.
An oscillating O(n^{-1/2}) perturbation of beta sqrt(n) independently
shows why the normalized expected-length increment cannot be deduced
from a first-order asymptotic alone. These are analytic counterchecks,
not simulations or claims about actual tour lengths.

Final read-back command (shell body used semicolons between short reads):

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
cat ~/codex_op_1114r4/briefs/T222/REPORT.md
sed -n "240,400p" ~/codex_op_1114/briefs/T222/PROOF.md
cat AUDIT.md REPORT.md
rg -n "epsilon|varepsilon|1/4|n-1|O\\(" PROOF.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
date "+%Y-%m-%d %H:%M:%S %Z"
'
```

Exit 0, again with the setpriority denial. Output time:
2026-11-15 08:49:19 +04. Before this append, counts were LOG.md 137,
PROOF.md 403, AUDIT.md 261, REPORT.md 108. The report begins with the
required verdict and states the stronger final O(n^{-1/2}) error.
No predecessor files were edited. Only the four documents here were
created. The chosen first-projection extension and its analytic audit
are complete; the variance-limit conjecture remains unresolved.
