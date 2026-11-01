# Kosygina–Zerner Problem 5.3 — source-scoped proof package

Status on 2026-09-18: **candidate mathematically complete / operationally PARTIAL**. Do not label this package `PROVED`, `KNOWN`, novel, or publishable until the independent-audit and prior-art requirements below are completed.

## Exact source scope

Source: Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895v2 (2012), journal version *Bull. Inst. Math. Acad. Sin. (N.S.)* 8 (2013), 105–157.

Locator: **Problem 5.3**, immediately after Theorem 5.2, printed p. 20 in the author copy.

Problem 5.3 asks whether the bounded-cookie assumption `(BD)` in Theorem 5.2 can be replaced by `(POS1)`. In the positive one-dimensional branch, retaining `(IID)+(WEL)+(POS1)`, the source-level statement is

\[
\delta\le2\Longrightarrow v=0,
\qquad
\delta>2\Longrightarrow v>0,
\]

where

\[
\delta=\mathbb E\sum_{i\ge1}(2\omega(0,+1,i)-1)\in[0,\infty].
\]

The source's exact `(WEL)` condition is that for each direction `e`, there is positive environment probability that **all** cookie transition probabilities in direction `e` are positive. Deterministic-right cookies are therefore permitted provided there is positive probability of a site stack with positive left probabilities at every depth.

## What the package proves

`main.tex` gives a source-scoped argument with three pieces.

1. **Supercritical clause.** If `delta>2`, finite-depth truncation has drift `delta_M>2` for some `M`; the published bounded theorem gives positive speed for the truncation, and monotonicity gives positive speed for the original walk.
2. **Critical clause.** At `delta=2`, Bernoulliization and front-loading reduce the problem to the random-emigration chain
   \[
   Z_{n+1}=\sum_{j=1}^{(Z_n+1-N_n)_+}\xi_{n,j},
   \qquad EN=2,\quad P(N=0)>0,
   \]
   with mean-one geometric offspring. For every such `N`, an explicit three-point law
   \[
   P(N_*=0)=a,\quad P(N_*=2)=1-3a,\quad P(N_*=3)=2a,
   \quad a=\min\{P(N=0)/2,1/6\},
   \]
   satisfies `N_* <=cx N`. The branching kernel converts this into finite-time increasing-convex domination of the arbitrary chain by the bounded critical comparator. The comparator is a source-valid bounded cookie environment with `delta=2`; its stationary first moment is infinite by the published bounded theorem and the standard backward-BLP speed identity. Therefore the arbitrary critical chain also has infinite invariant mean and speed zero.
3. **Subcritical-positive clause.** If `delta<2`, strengthen finitely many cookie coordinates to a source-valid critical environment. Speed monotonicity and the critical result give `0<=v<=0`.

Thus the mathematical claim of `main.tex` is exactly the positive `(POS1)` version requested by Problem 5.3, not a change of quantifiers and not a restricted finite-depth statement.

## Main proof provenance inside this repository

- Admission: `research7_2026-09-17/R7-02/admissions/2026-09-18T165900Z__C0134_admission.md`.
- First mathematical artifact (supercritical clause and transition asymptotics): `research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T170300Z__C0134_truncation_and_unbounded_stack_transition_lemma.md`.
- Second artifact (front-loading / RE(2) reduction): `research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T173258Z__C0134_frontloading_reduction_and_geometric_emigration.md` @ `73e81758400e788e06a1787a153458b38d0ac384`.
- Closing convex-order artifact: `research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T183000Z__C0134_convex_order_critical_closure.md` @ `ddc080447b69ba38d9dcf05f740de83b29a67f14`.

## Prior-art status as of 2026-09-18

A bounded search has **not** found a later paper explicitly claiming the no-tail-assumption solution of Problem 5.3, but that negative search is not a novelty certificate.

Important nearby work requiring full comparison before any novelty claim:

- Omar Chakhtoun, 2019 doctoral dissertation, *One-Dimensional Excited Random Walk with Unboundedly Many Excitations Per Site*. Its public abstract explicitly says it imposes a tail-decay estimate on the number of excitations per site and obtains ballisticity/zero-speed criteria under that wider class.
- Tuan-Minh Nguyen, 2022, *Speed of Excited Random Walks with Long Backward Steps*, which treats a critical multi-type branching process with deterministic emigration in a different ERW model.
- Patrick Carper, arXiv:2609.06311, submitted 2026-09-05, *A Branching Process with Geometric Emigration and the “Have Your Cookie and Eat It” Random Walk*, which treats geometric emigration rather than arbitrary integrable emigration.
- Classical critical branching-with-emigration/migration work of Vatutin, Kaverin, Nagaev–Khan, and Yanev–Mitov. Their exact hypotheses must be inspected against the random-emigration theorem before novelty is asserted.

## Closure obligations still outstanding

The owner protocol requires all of the following before canonical closure:

- full dated prior-art reconciliation, including the sources above;
- an actual independent P26 full-proof audit;
- a second independent audit from a distinct OTHER track;
- audit of every imported source theorem/hypothesis and of the Bernoulliization/front-loading reduction.

There is no finite computational core in the closing argument, so no exact-arithmetic certificate is naturally applicable. The core is theorem-sized and is written in full in `main.tex` and the closing Markdown artifact.

Shared `RESULTS.md`, `QUEUE.md`, and `POSTED.md` are coordinator-owned and are intentionally not edited by R7-02.
