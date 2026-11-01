# Quantifier clarification for BT4-HT-HALL-SOURCE-COLLAPSE-v1

This immutable clarification accompanies the report of run `20260922T055931Z-fleet02-B20-bt4-r15`.

In the theorem statement, the phrase “exactly one of the following source-level alternatives applies” should be read as follows.

- `s_i != s_j` versus `s_i=s_j` is an exclusive split.
- In the common-source / positive-R-exit case, **fix one** directed continuation starting with a chosen arc `q->r_1` and extending inside the acyclic remainder until its first packed contact `t`. For that fixed continuation, exactly one of the three endpoint categories occurs: `t in H union A`, `t in B\{q}`, or `t=q`.
- Different choices of the initial R-exit or continuation may realize more than one endpoint category in the same digraph. The theorem only needs the existential routing conclusion: at least one of CROSS, taxed same-support BYPASS, or short-support return is available whenever the common source has an R-exit.

No other proof line changes. In particular the exact-six zero-R-exit branch and the distinct-source full path-disjointness lemma are unchanged.
