# POS3 fleet02/B11 — other-account integration addendum

**Outcome:** ESSENTIAL_STEP_APPLIED; target remains open.

After the initial report was archived, the shared coordination path exposed completed POS3 handoffs from fleet01. I consumed the exact chain-deletion multiplicity result of fleet01/B19 and the three-chain weighted-flux formulation of fleet01/B10, then combined them with this run's incomparability-connected reduction.

## Input from fleet01/B19

For a deleted chain `C={c_1<...<c_m}` and `Q=P\C`, each `tau in L(Q)` has an exact positive integer lift multiplicity `W_C(tau)`, equal to the number of weakly increasing legal insertion-slot vectors. Thus restriction of a uniform random linear extension of `P` to `Q` is not generally uniform: it is the `W_C`-weighted law.

## Input from fleet01/B10

For a three-chain cover, the same lift weights admit exact path/flux formulas. In a counterexample, all cross-chain comparison probabilities must lie outside `[1/3,2/3]`; the B10 handoff packages this as a heavy-slice normal form and explicitly warns that the two-chain projection is weighted by third-chain lift multiplicities rather than uniform.

## New combined necessary condition: every chain deletion must be balance-destroying

Let `P` be a width-exactly-three counterexample, and let

`P = A union B union C`

be any partition into three chains. Then for each chosen deleted chain, say `C`, the two-chain induced poset `Q=P\C` is a **nonchain**.

**Proof.** Since `width(P)=3`, `P` contains a three-element antichain `{a,b,c}`. A chain contains at most one member of this antichain, so every partition into three chains places the three antichain elements in three distinct chains. Deleting any one chain leaves the other two antichain elements in `Q`, still incomparable. Hence `Q` is a nonchain. ∎

The known width-two theorem therefore gives an incomparable pair `x,y in Q` whose probability under the **uniform** law on `L(Q)` satisfies

`q := Pr_U(x<y) in [1/3,2/3]`.

But fleet01/B19's exact multiplicity formula gives

`Pr_P(x<y) = sum_{tau:x<y} W_C(tau) / sum_tau W_C(tau)`.

If `P` is a counterexample, this weighted probability is strictly outside `[1/3,2/3]`. Consequently:

1. `W_C` is not constant on `L(Q)`;
2. writing `U` for the uniform law on `L(Q)` and `A={tau:x<y}`,

   `Cov_U(W_C, 1_A) = E_U[W_C] * (Pr_P(x<y)-q)`

   is strictly negative when the weighted probability falls below `1/3`, and strictly positive when it rises above `2/3`;
3. the same statement holds for deletion of **each** of the three chains in **every** three-chain cover.

So a width-three counterexample cannot merely have a biased projection somewhere: all three chain-deletion projections must be simultaneously and directionally balance-destroying for at least one width-two balanced pair in the corresponding two-chain remainder.

This is an exact transfer of the fleet01 chain-insertion result into the minimal-counterexample core from the main B11 report. It rules out any proposed proof route that hopes one chain can be deleted with constant lift multiplicity, and it identifies the next quantitative target: show that three mutually compatible interval-corridor weight systems arising from one connected width-three poset cannot all push their width-two balanced pairs past the 1/3 or 2/3 boundary.

No novelty claim is made. No benchmark material or held-out data is used.
