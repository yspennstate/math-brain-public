# Theory proposal review

## Recommendation

`proposal.tex` is a self-contained, approximately 720-word optional subsection for the end of `sections/03_dynamics.tex`, following the current single-warning net-value identity. It can replace the current final paragraph's trivial example in which a correct baseline blindly follows one incorrect retrieved statement. It should not be added as a new empirical result or a novelty claim. No existing manuscript files or remote files were edited.

The useful extension is **interaction among individually useful warnings**. A correct warning can still produce a false-positive application; warnings that have already detected most invalid proofs leave less opportunity for further true detections. The exact marginal identity handles dependence. A homogeneous conditional-independence model then has an explicit optimal warning count under equal-card token capacity. This makes selective delivery mathematically concrete without presupposing memory displacement or false stored mathematics.

## Assumptions and interpretation

- The task is binary proof auditing, with a known prior mixture of valid and invalid proofs. Correct rejections count as successful audit outputs, so `A` is correctness, not the probability of accepting the submitted proof.
- The auditor follows an OR decision rule: any alert rejects; no alert accepts. This describes a stipulated response policy, not optimal inference and not a claim about the inspected implementation.
- The candidate alert events are jointly defined on a common probability space and do not change with the selected context. Real context interactions can violate that assumption.
- The first identity needs no independence. The optimal-count specialization requires mutual independence conditional on validity and mutual independence conditional on invalidity, homogeneous diagnostic quality, and equal fully serialized token lengths.
- The available capacity is `k = min(N, floor(b/tau))`; card wrappers and metadata are part of `tau`. This is a capacity model, not a billing model.
- Higher accuracy plus lower positive mean cost implies a lower cost/accuracy ratio only on the same task population and quality criterion. The proposal makes no empirical claim that a larger packet actually costs more end to end; measurement remains necessary.

## Mathematical checks

For an existing set `S`, only cases where all existing alerts are silent and the new alert fires can change their verdict. The exact change is therefore

`(1-pi) P(all S silent and i alerts | invalid) - pi P(all S silent and i alerts | valid)`.

Under conditional independence and identical rates,

`A_n = pi (1-f)^n + (1-pi)[1-(1-d)^n]`

and

`A_(n+1)-A_n = (1-pi)d(1-d)^n - pi f(1-f)^n`.

The ratio of the positive detection term to the positive false-alarm term is strictly decreasing because `0 < f < d < 1`. Consequently the sign of the increments crosses at most once. With

`t = log(((1-pi)d)/(pi f)) / log((1-f)/(1-d))`,

increments are positive at integer indices `n < t`, zero at `n = t`, and negative at `n > t`. The smallest feasible maximizer is `min(k, max(0, ceil(t)))`. If `t` is a nonnegative integer and `t+1 <= k`, both `t` and `t+1` maximize accuracy. This includes the `t=0` boundary. If `k=0`, the formula gives zero. The assumptions exclude logarithms at zero and division by zero.

Exact example (`pi=4/5`, `d=4/5`, `f=1/20`):

| Warnings | Exact correctness | Decimal |
|---|---:|---:|
| 0 | 4/5 | 0.8000 |
| 1 | 23/25 | 0.9200 |
| 2 | 457/500 | 0.9140 |
| 3 | 8843/10000 | 0.8843 |

The second card lowers correctness by `3/500 = 0.006`. Each card alone improves correctness by `3/25 = 0.12`. The ratio for the zeroth increment is 4, and its geometric multiplier is `4/19`; after one card the ratio is `16/19 < 1`, so the optimum is one card whenever at least one card fits.

The numerical values were recomputed with exact rational arithmetic. A deterministic numerical check of 5,000 parameter combinations and feasible counts agreed with the maximizer formula; the displayed proof, including its exact tie treatment, is the mathematical justification.

## Relationship to existing text

1. The existing coverage model remains sound for its stated nonnegative maximum-coverage objective. It is explicitly monotone, so its greedy guarantee cannot justify maximizing this nonmonotone audit objective.
2. The single-warning value identity remains useful but does not show how the marginal usefulness changes after previous warnings. The general identity in this proposal supplies that missing dependence.
3. The contraction proposition in the existing text has an appropriate row-substochastic and gain-below-one assumption and correctly disclaims applicability to every inspected hook. No amendment is recommended on the basis of this review.
4. The cost-per-accepted-result accounting remains valid under the stated law-of-large-numbers conditions, with no need for independence between an attempt's cost and its success; both empirical averages simply need to converge and success probability must be positive. No amendment is needed.

## Novelty and references

No novel optimization or inference theorem is claimed. All displayed results are elementary consequences of event subtraction, conditional independence, and the sign of a geometric sequence; full proofs are provided. The proposal does not borrow or assert the optimality of a named existing test. It consequently adds no external citation to the manuscript.

For background only, classic decision-fusion literature includes Z. Chair and P. K. Varshney, *Optimal Data Fusion in Multiple Sensor Detection Systems*, IEEE Transactions on Aerospace and Electronic Systems AES-22(1), 98–101 (1986), DOI [10.1109/TAES.1986.310699](https://doi.org/10.1109/TAES.1986.310699). Bibliographic metadata were located, but the publisher's full text was blocked by a JavaScript verification page in this session. The proposal does not attribute its formulas or assumptions to that unread article. Adding a ceremonial citation to a different optimal-rule result could obscure the fixed-policy nature of the example and is not recommended without reviewing the source.

## Empirical restraint

The proposal does **not** claim that full brain was worse than diet brain, that AB30 is finished, that its card-level events satisfy conditional independence, or that any observed difference has this mechanism. Even a completed arm-level score cannot identify these parameters. The text offers a measurable mechanism and a counterexample to monotonic memory utility, not a fitted explanatory model.
