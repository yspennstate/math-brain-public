# B05 / A023 — positive point-defect retained credit

## Outcome

**AUTHOR-PROVED ALL-RANK PROPER-CLASS THEOREM; INDEPENDENT REVIEW PENDING.**

This run strengthens the new B01 variable-rank point-defect endpoint and turns
it into a complete A023 retained-credit statement.  Let `Q_r` be `+1` except
at one point of the `r`-cube, let `r_k>=2` vary arbitrarily, and on fresh
disjoint blocks define

\[
F_1=A(wP),\qquad F_k=A(Q_{r_k}F_{k-1}).
\]

For every Boolean base `P`,

\[
 U(P)\le {8\over3}I(P)
 \quad\Longrightarrow\quad
 \boxed{U(F_d)\le {8\over3}I(F_d)\quad(d\ge1).}
\]

This improves the preceding B01 constant from `5` to `8/3` while retaining
uniformity in dimension, depth, every rank, and activation probabilities
`2^{-r_k}` tending to zero.

For every finite adaptive/pruned physical restriction tree and every common
disjoint Boolean terminal core `h`,

\[
\boxed{
U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)
\le {8\over3}I(F_d).
}
\]

Each branch is charged only through the signed telescope; the common terminal
entropy cancels exactly once, and no descendant reuses a rarity credit.  The
standard bridge gives `H(F_d)<=22 I(F_d)/3`.

## New scalar mechanism

The B01 proof used `R(t)<(5/2)(1-t)`.  Here the exact derivatives give

\[
R'(t)>-\frac43\quad(0<t<1),
\]

hence

\[
\boxed{R(t)\le\frac43(1-t)\quad(0\le t\le1).}
\]

The derivative minimum is isolated without numerical assumptions.  Since
`R'''(t)>0`, it occurs at the unique zero of `R''`.  Exact rational/exponential
bounds put that zero in `(49/100,51/100)`, give `|R''|<1` there, and give

\[
R'(1/2)>\frac{99}{160}-\frac74-\frac{81}{448}.
\]

Therefore the global minimum is greater than
`-14807/11200>-4/3`.  This pays the selector rare logarithm with a uniform
coefficient even when `E Q_r=1-2^{1-r}` tends to one.

The point-defect block itself satisfies the sharper estimate

\[
U(Q_r)\le2I(Q_r)\qquad(r\ge2),
\]

so the scalar term, not the block spectrum, sets the displayed constant.

## Exact recurrence and payment

Writing `t=(E Q_r)(E F_{k-1})`, disjointness and the cap identity give

\[
\begin{aligned}
U(F_k)&=\tfrac12U(F_{k-1})+\tfrac12U(Q_r)+R(t),\\
I(F_k)&=\tfrac12I(F_{k-1})+\tfrac12I(Q_r)+\tfrac12(1-t).
\end{aligned}
\]

The two sharpened estimates close `U<=(8/3)I` at every level.  The first
balanced level closes for every constant at least one.  For a finite tree,
the complete signed node charge telescopes to root `U` minus the nonnegative
leaf average; tensor additivity cancels a common disjoint terminal core.

## Precise class extension

- **Previous B05:** fixed mean `-1/2` balancers, retained constant `c>=48/35`.
- **Previous B01 positive-defect family:** arbitrary point-defect ranks and
  vanishing activation probabilities, endpoint constant `5`.
- **New:** the positive point-defect family has endpoint and complete-tree
  retained constant `8/3`, uniformly for arbitrary rank sequences and depth.
- **Still required:** fresh disjoint balancer blocks and fair outer selectors.
- **Still unpaid:** biased selectors, variable reuse, negative near-constant
  balancers, and changing/overlapping coherent cores.

This is an expanding all-parameter proper class, not a universal upper-set
payment.  Full FEI remains **OPEN**.

## Verification

`CHECK.py` independently reconstructs Walsh spectra, point-defect blocks,
variable-rank towers, the exact recurrences, and randomly pruned physical
trees.  It also checks common-terminal-core cancellation by direct tensor
construction.  The finite computation is corroborative; `PROOF.md` contains
the all-rank proof.

## Status and next unpaid step

Claims `B05_A023_POSITIVE_DEFECT_ENDPOINT_v1` and
`B05_A023_POSITIVE_DEFECT_RETAINED_v1` are author-proved pending independent
A087/A094 review.  A023 is not complete.

The next mechanism should test a biased outer selector or a sign-flipped
point-defect block.  In either case the present positive mean floor can fail,
so a new global credit is needed rather than another optimization of this
scalar constant.

## Source pins

- owner control `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- B05 fixed-bias retained theorem, final commit
  `748f7eb102bb43b98f8b184729594601beb22c7c`;
- independent acceptance of that fixed-bias theorem, final commit
  `aba1124116091e2ed86071528197a8bf5c3540c8`;
- B01 variable-rank point-defect theorem, final commit
  `3da104b41a42deee0b62498ec811fba835bcb72a`.

No external novelty claim is made.
