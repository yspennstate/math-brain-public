# B01 / A003 — sign-flipped rare-defect GU' transfer

## Outcome

**AUTHOR-PROVED ALL-RANK PROPER-CLASS THEOREM; INDEPENDENT REVIEW PENDING.**

The preceding B01 theorem controlled arbitrary positive point-defect biases
approaching `+1`.  This run proves a uniform counterpart for the previously
unpaid negative near-constant regime.

Let `Q_r` be `+1` except at one point, `N_r=-Q_r`, and

\[
F_1=A(wP),\qquad F_k=A(N_{r_k}F_{k-1}),\qquad r_k\ge2,
\]

on fresh disjoint blocks with fair selectors.  Then, for every finite depth
and arbitrary rank sequence,

\[
\boxed{G(F_d)\le2^{-d}G(P)+34.}
\]

Hence every base inequality

\[
G(P)\le aI(P)+bU(P),\qquad 0\le b<1,
\]

transfers as

\[
\boxed{G(F_d)\le(a+34)I(F_d)+bU(F_d),}
\]

with the same contraction coefficient `b`.  The constant is independent of
base dimension, tower depth, every rank, and the rare activation
probabilities `2^{-r_k}`.

The same class has the sharper endpoint transfer

\[
U(P)\le\frac{56}{27}I(P)
\Longrightarrow
\boxed{U(F_d)\le\frac{56}{27}I(F_d),\qquad
H(F_d)\le\frac{166}{27}I(F_d).}
\]

## Mechanism and class extension

The negative bias destroys the positive mean floor used in the previous
proof, but the damage lasts for only two generations.  Every fresh selector
creates one exceptional restriction-mean pair.  After two subsequent
negative activations that pair enters `[1/8,1/2]`; all point-defect coordinates
are born inside that interval.  Thus at most three physical coordinates are
exceptional at any level.

For every other coordinate the scalar arguments lie in
`[-1/2,-1/16]`, where `R''>-6`.  Their complete aggregate mismatch is at most
`3W_1<=3`; the exceptional coordinates pay a fixed global charge.  This gives
the depth-uniform recurrence

\[
G(F_k)\le\frac12G(F_{k-1})+17
\]

and the constant `34`.

The endpoint improvement uses a new reflection inequality

\[
R(-t)\le R(t),\qquad 0\le t\le1,
\]

together with the independently reviewed bound `R(t)<=4(1-t)/3`.

## Verification

`CHECK.py` uses exact rational Walsh transforms and influences for small
truth tables and an independent mean-pair recurrence for long nonstationary
towers.  It passed:

- 1,465,767 scalar checks;
- 834 direct truth-table towers and 3,336 reconstructed state quantities;
- 16,756 GU' and 16,756 endpoint checks;
- 39,301,864 pair-classification checks through rank 233 and depth 91.

The maximum recurrence error was `2.220e-15`.  The largest observed additive
GU cost was `4.02520` versus the proved `34`; the largest observed `G/I` was
`1.89436`.  The analytic proof, not the finite experiment, establishes the
all-rank theorem.

## Exact scope and remaining gap

- Previous class: arbitrary positive point-defect biases approaching `+1`.
- New class: arbitrary negative point-defect biases approaching `-1`.
- Uniform parameters: dimension, depth, rank sequence, bias, and activation
  probability.
- Still required: fresh disjoint blocks and fair outer selectors.
- Still open: arbitrary sign mixtures, biased selectors, variable reuse,
  changing or overlapping coherent cores, and the universal aggregate
  upper-set asymmetry mismatch.

The activated tower family is not restriction-closed.  This is a strict
proper-class extension, not the universal GU' inequality.  Full FEI remains
**OPEN**.

## Source pins

- owner control revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- positive point-defect GU' source commit
  `3da104b41a42deee0b62498ec811fba835bcb72a`;
- independently reviewed positive point-defect scalar/endpoint proof,
  canonical commit `f9e5ba18eb5860b3c985ca2a1e983ddc851e29d0`;
- exact current repository head inspected before this run:
  `ed48e79876a2da66ddc63701e701271db11226c2`.

No novelty or literature-priority claim is made.

## Next action

Freeze alternating sign sequences.  Track whether a positive-to-negative
switch can create more than a single generation of near-zero restriction
means, and seek a finite-state age potential that pays the scalar cusp without
reusing singleton energy.  Route this theorem to A005, A023, A086/A094, B05,
B18, and B20.
