# T088 work log

Task received: 14 November 2026, approximately 21:57 +04 (first shell clock).

## 21:57–22:03 +04: orientation and literature check

Read PROMPT.md, the startup memory, the brain topic index, and the compute state, without editing outside this directory. The current task's restriction to this directory takes precedence over the earlier instructions to update the shared checklist and mesh. No agents were started.

Web queries included `"2604.14122" chemical distance`, `percolation shortest path exponent d_min universality 2026 proof`, `"chemical distance" "2026" percolation exponent universality`, `"shortest crossing" percolation "2026"`, `"percolation" "chemical distance exponent" "November" "2026"`, and `"percolation" "chemical distance" "universality" "2026" "square"`.

Opened the arXiv abstract and full HTML of Irina Đanković, Maarten Markering, Jason Miller, and Yizheng Yuan, *The scaling limit of random walk and the intrinsic metric on planar critical percolation*, arXiv:2604.14122:

- https://arxiv.org/abs/2604.14122
- https://arxiv.org/html/2604.14122v1

The abstract and introduction establish existence of the exponent, not its value or universality for square-lattice bonds. No later solution or substantial advance beyond the supplied status was found in this bounded search. This is a search result, not proof of absence. The HTML uses triangular coordinates, so its box is a parallelogram (Introduction, Section 1.3).

Resource check: the governor reported `status: warn`, `mode: owner_away_open`, with CPU saturation. A harmless test command, `env OMP_NUM_THREADS=1 nice -n 15 /bin/date '+%Y-%m-%d %H:%M:%S %Z'`, printed `nice: setpriority: Operation not permitted`. A second harmless shell probe produced the same diagnostic. The sandbox does not permit the requested priority adjustment. No numerical search, simulation, compiler, or substantive computation will be run. The deliverable will be a proof.

## Choice, recorded before work

Solve one special case exactly: independent bond percolation with p=1/2 on the two-row square-lattice ladder, conditioned on a left-right crossing. Derive the generating function of the shortest crossing length and the limiting conditional mean per horizontal step. This isolates the optimization over paths in an exactly tractable geometry and provides a finite-width benchmark. It will not determine the planar exponent or provide a new planar bound.

The intended mechanism is that every simple left-right ladder crossing is horizontally monotone: each vertical cut has only two edges and a simple crossing uses an odd number of them. Horizontal cuts with exactly one open edge then force a sequence of rail choices. The number of changes in those choices is the minimal number of rungs, provided every forced change has an available rung between its two constraints. This permits a renewal generating function.

## Derivation completed

Wrote PROOF.md. For the ladder with vertices `(i,h)`, `0 <= i <= n`, `h in {0,1}`, let H_n be an open crossing, S_n its shortest edge length, and T_n=S_n-n. The marked crossing generating function obtained by summing horizontal cut types and independent rung events is

```
sum_n E[1_{H_n} t^{T_n}] z^n
  = (1-(1+t)z/8) / ((1-z/4)(1-(5+t)z/8+z^2/16)).
```

Consequences proved in the same file:

- Crossing probability `(lambda^(n+1)-mu^(n+1))/(lambda-mu)`, with `lambda=(3+sqrt(5))/8`, `mu=(3-sqrt(5))/8`.
- Conditional mean `E[S_n|H_n]=(1+1/(2sqrt(5)))n+O(1)`.
- Conditional variance `Var(S_n|H_n)=7n/(20sqrt(5))+O(1)`.
- Conditional convergence in probability of `S_n/n` and convergence of every fixed interior quantile to `1+1/(2sqrt(5))`.

No program was run to obtain these formulas. PROOF.md gives the formal-series sum, the partial fractions, and all derivative steps. Added finite_checks.csv with exact counts derived by hand for n=1,2,3, including all random boundary rungs. These data are certificates of the displayed finite polynomials, not simulation output.

## Initial audit

Re-derived the crossing probability with a separate two-state connectivity transfer matrix `[[1/2,1/4],[1/4,1/4]]`. Its trace `3/4` and determinant `1/16` give the same roots and recurrence as the generating function. Re-derived the mean and variance coefficients by implicit differentiation of the leading-root quadratic, separately from differentiation of its radical expression.

Directly classified all nonempty horizontal cut types for n=1,2,3. This gives `P_1(t)=3/4`, `P_2(t)=(7+t)/16`, and `P_3(t)=(30+11t+t^2)/128`. Thus `P(H_2)=1/2`, `E[S_2|H_2]=17/8`, `P(H_3)=21/64`, and `E[S_3|H_3]=139/42`. The full graph has `3n+1` random edges, so these probabilities give integer counts with denominators 16,128,1024; those counts are recorded in finite_checks.csv.

The main limitation is deliberate: p=1/2 is the critical probability of the ambient planar square lattice, but the fixed-width ladder itself has critical probability 1. Its conditioned crossing probability decays exponentially, unlike the box crossing in T088. This is an exact strip benchmark, not evidence for a planar exponent estimate.

## Final adversarial audit

Checked the cases with no single cuts, a single single cut, an empty horizontal cut, all interior rungs closed, multiple available rungs in one forced-change interval, and random boundary rungs. The interval decomposition counts every horizontal cut sequence once; required rung intervals are disjoint; unused rung states sum to probability one. Shortest paths are simple, so the parity argument for two-edge cuts applies without a hidden assumption about path choice.

Added an explicit failure at three rows: the path `(0,0),(1,0),(2,0),(2,1),(1,1),(1,2),(2,2),(3,2)`, with only its seven edges open, is the unique crossing and backtracks horizontally. This blocks extending the width-two renewal argument to wider strips without more state.

Expanded the denominator in (1) as `1-(7+t)z/8+(7+t)z^2/32-z^3/64`, then extracted its first three coefficients to check the direct finite counts independently. At n=3, the counts sum as `688+240+88+8=1024`; the crossing count is `336`, and the length sum is `3*240+4*88+5*8=1112`, giving conditional mean `1112/336=139/42`. At n=2, `64+56+8=128`, and the conditional mean is `(2*56+3*8)/64=17/8`. These are exact hand calculations.

The asymptotic proof uses a simple dominant root with analytic nonzero coefficient. Its two competitors have bases `1/4` and `(3-sqrt(5))/8`, strictly below `(3+sqrt(5))/8`; differentiating their relative contributions twice gives at most a polynomial factor times exponential decay. Thus the mean and variance statements do not rest on an unjustified differentiation of a pointwise asymptotic.

## Saved-file review

Read REPORT.md and PROOF.md back from disk using `env OMP_NUM_THREADS=1 nice -n 15 /bin/cat REPORT.md` and the analogous command for PROOF.md; checked file lengths with `wc -l`. The same priority diagnostic appeared on these read-only commands. Corrected inline mathematical delimiters and escaped symbols in the saved proof. A final in-memory text check found no unexpected control characters and matching display-math delimiters. REPORT.md has the required verdict as its first line. The completed result, its failed extension, exact finite checks, and next steps are all saved in this folder.
