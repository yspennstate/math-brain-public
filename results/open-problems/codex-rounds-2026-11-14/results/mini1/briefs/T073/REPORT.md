VERDICT: PARTIAL explicit high-noise uniqueness criterion for the stated process

For the continuous-time four-neighbor process with fair random ties, proved
uniqueness of the stationary measure whenever

\[
(2-4\varepsilon)(1-\varepsilon^3/2)<1,
\qquad 0\le\varepsilon\le1/2.
\]

Equivalently, uniqueness holds for epsilon > epsilon_*, where epsilon_* is
the unique root in [0,1/2] of
`2*epsilon^4 - epsilon^3 - 4*epsilon + 1 = 0`.
Exact rational bounds put this root between
0.248076921333012290 and 0.248076921333012735. In particular, the whole
interval [0.2481, 0.5] is covered. This slightly extends the elementary
single-neighbor influence criterion epsilon > 1/4. It does not settle the
requested low-noise coexistence statement.

The proof is in [PROOF.md](PROOF.md). In a stationary ordered coupling, a
disagreeing neighbor loses its influence if the other three neighbors have
been forced to a common spin. Decomposing according to the disagreeing
site's last update gives a lower bound `(epsilon^3/2)*d` for this event
weighted by disagreement, where d is the stationary disagreement density.
The resulting contraction forces d=0. Extremal stationary measures then
coincide, and all stationary measures coincide with them.

Reproduce the finite audit with:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py
```

The command exits 0 and writes [audit_output.json](audit_output.json). It
checks all 81 ordered neighbor pairs and all 24 telescoping orders for each,
reconstructs the update rule independently using random three-neighbor
majorities, checks the clock integral three ways, and verifies the endpoint
and root bracket by exact rational arithmetic. At epsilon=0.2481 the
contraction factor is exactly
`4999531215835321/5000000000000000 = 0.9999062431670642`.
The successful run took below one second, used approximately 15.6 MB peak
resident memory, and ran at inherited nice 20 with one thread. On this
worker `nice -n 15` prints `setpriority: Operation not permitted` because
priority is already 20; the script verifies priority >= 15 before running.

The literature search, bounded to under ten minutes, located no solution
or substantial new rigorous advance for the exact process in the task.
This does not establish that none exists. The rule caveat matters:

- Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority vote
  process on trees*, [arXiv:2501.16202](https://arxiv.org/html/2501.16202v1),
  Section 1.1, use synchronous updates, retained ties, and fair-resampling
  noise. These are different dynamics from the task.
- Damiano De Gaspari, *Fredrickson Andersen Model and Noisy Majority Vote
  Process on Nonamenable Graphs*,
  [arXiv:2508.06935](https://arxiv.org/pdf/2508.06935), page 2 and Definition
  2.3, likewise uses a synchronous retained-tie rule and requires expansion;
  it describes the Euclidean-lattice equilibrium question as open.
- Damiano De Gaspari's 2026 thesis, *Out-of-equilibrium systems: stationary
  measures and superdiffusivity*, has an opened
  [catalog entry and abstract](https://repositum.tuwien.at/handle/20.500.12708/231354)
  placing its majority-vote results on nonamenable graphs.

Failures and limits: an initial audit run had an incorrect root-bracket
bookkeeping assertion; correcting the bracket produced the saved successful
run. A macOS address-space limit diagnostic failed; the actual audit remained
far below the memory budget. A potentially relevant Minnesota thesis PDF was
blocked with HTTP 403, so its contents were not used. The proof explicitly
checks the dependence issue in the last-ring calculation, constructs a
stationary joint coupling rather than assuming joint convergence, and covers
nontranslation-invariant stationary measures by extremal squeezing.

No result is obtained at epsilon=epsilon_*, at positive low noise, or for
the retained-tie rule. No monotonicity of the coexistence set in epsilon is
proved. The bound's novelty and its relation to the strongest published
high-noise criteria have not been established.

The next worker should first check whether this elementary last-update
bound is already subsumed by a published uniqueness criterion for this exact
rule. For a further mathematical improvement, sharpen the local bound (4)
by also using its unused slack when three or four neighbors disagree, and
seek a justified lower bound on those events from shared update histories.
Such a bound would still concern uniqueness; low-noise coexistence needs
an additional argument controlling large error clusters on Z^2.

Task: “push this problem forward by one checkable piece” — 2026-11-14,
approximately 20:51 +04 (Asia/Tbilisi).
