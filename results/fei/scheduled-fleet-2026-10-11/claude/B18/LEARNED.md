# B18 lead - learned (dated)

## 2026-10-11 23:35 UTC
- The affine-support class reduces to juntas: a relevant e_i outside the support's direction space forces B_i=0, so "affine dimension <= d" is "d-junta or free good coordinate". Exhaustive n<=d certificates then transfer to all n inside the class.
- The optimal four-variable good-coordinate constant (3-bit point defect, 2.6725) is beaten at five variables by the lexicographic threshold t=3 (2.6959, exact). Small-n optima are not universal constants; test the next n before treating a small-n extremal as a conjecture.
- A C005 induction with a good-coordinate constant K proves FEI with K+2/ln2, so any known lower bound on the FEI constant is also a lower bound (minus 2/ln2) on every universal good-coordinate constant. Check the literature value before relying on it.
- Exact zero deviations in float checks on small Boolean functions are expected (dyadic Walsh coefficients give identical floating terms); confirm nontriviality and use rational-log rechecks for anything claimed exact.
- The harness refuses REPORT.md writes from a subagent; put the report text in the structured return and record the blocker in PROGRESS.json.
