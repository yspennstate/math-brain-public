# B01 / A003 — variable-rank rare-defect balancer tower

## Outcome

**AUTHOR-PROVED ALL-RANK PROPER-CLASS THEOREM; INDEPENDENT REVIEW PENDING.**

The previous B01 theorem handled one fixed nonzero balancer mean `-1/2`. This
run removes that fixed-bias dependence for the entire restriction-closed family
of positive point-defect balancers.

Let `Q_r` be `+1` except at one vertex of the `r`-cube, and let

\[
F_1=A(wP),\qquad F_k=A(Q_{r_k}F_{k-1}),
\]

where `w` is fresh and balanced, every block is physically disjoint, and the
ranks `r_k>=2` may vary arbitrarily. Since
`E Q_r=1-2^{1-r}`, the permitted biases approach `+1` and the activation event
can be arbitrarily rare. Nevertheless, for every depth,

\[
\boxed{G(F_d)\le2^{-d}G(P)+24.}
\]

Thus every base GU' inequality

\[
G(P)\le aI(P)+bU(P),\qquad 0\le b<1,
\]

transfers as

\[
\boxed{G(F_d)\le(a+24)I(F_d)+bU(F_d),}
\]

with `b` preserved exactly and no dependence on dimension, depth, rank, or
activation probability.

The same towers satisfy the endpoint implication

\[
U(P)\le5I(P)
\Longrightarrow
\boxed{U(F_d)\le5I(F_d),\qquad H(F_d)\le12I(F_d).}
\]

## Why the parameter dependence disappears

The scalar activation identity contains the logarithmic cusp of `R''` at zero.
For point-defect bias `beta_r`, one might therefore expect a constant growing
like `log(1/(1-beta_r))`. That loss is spurious.

After one rare activation, every inherited restricted mean is at least `1/4`.
All later scalar arguments are therefore at least `1/8`, where

\[
R''(t)>-4.
\]

The aggregate inherited charge is then at most `2W_1<=2`, uniformly in rank.
Only the original balancing character and selector can touch the cusp, so they
pay one fixed global charge. The `r` point-defect coordinates together cost at
most `9/2`; for `r>=3` their sharper cost is at most `3/8`.

This yields the same recurrence as in the fixed-bias theorem,

\[
G(F_k)\le\frac12G(F_{k-1})+12,
\]

and hence the same constant `24`.

## Precise class extension

- **Previous:** fixed two-bit AND balancer, mean `-1/2`, at every positive
  level.
- **New:** arbitrary rank sequence of point-defect balancers with means
  `1-2^{1-r}`, uniformly through the limit `beta->1`.
- **Controlled uniformly:** base dimension, rank, bias, tower depth, terminal
  rarity, and rank variation between levels.
- **Still required:** fresh disjoint physical blocks and fair outer selectors.
- **Still unpaid:** negative near-constant bias, arbitrary Boolean balancers,
  biased selectors, variable reuse, and changing overlapping coherent cores.

The balancer family itself is restriction-closed (`Q_r` restricts to `Q_{r-1}`
or `1`), but the activated tower class is not. This is meaningful movement
toward the universal GU' lemma, not its proof.

## Verification

`CHECK.py` independently reconstructs small truth-table towers and evaluates
the exact state recurrence for long nonstationary rank sequences. It passed:

- 1,421,020 scalar and balancer checks through rank 256;
- 834 direct truth-table towers over all Boolean bases through three variables;
- 3,336 exact state-recurrence checks;
- 12,354 GU' transfer and 12,354 endpoint checks; and
- 24,168,424 restriction-mean floor checks in long variable-rank towers.

Maximum recurrence error was `1.776e-15`. The largest observed additive GU
cost was `3.58483`, versus the proved `24`. The largest endpoint increment
ratio was `2.11767`, versus the proved `5`. Finite checks are corroborative;
the all-rank result is analytic in `PROOF.md`.

## Status and next step

Claims `B01_A003_POINT_DEFECT_BALANCER_GU_TRANSFER_v1` and
`B01_A003_POINT_DEFECT_BALANCER_ENDPOINT_v1` are author-proved pending an
independent A086/A094 review. Full FEI remains **OPEN**.

The next unpaid step is to determine whether the positive restriction-mean
floor can be recovered for sign-flipped point defects (bias approaching `-1`)
or for biased outer selectors. Without such a floor, many inherited
coordinates can revisit the scalar cusp and the present proof does not give a
dimension-independent charge.

## Source pins

- owner control revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- preceding fixed-bias package commit
  `bdd18f98e73739debb566afac8a55356af5ff370`;
- preceding parity-tower finalized commit
  `51ef0d5565bbb807ba99e38815cbda4c2e32fe73`.

No external priority claim is made.
