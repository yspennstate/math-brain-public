# Rigor check — B15 r14 strong-cross collar reduction

This file independently rechecks the new algebra in `REPORT.md`. It is not a second-worker review.

## A. Combinatorial identities

For each two-set `H`, put

`w_H(U)=det(A[H,U])^2` for two-sets `U` disjoint from `H`, and `G_H=sum_U w_H(U)`.

1. By Cauchy--Binet applied to `C_H=A[H,H^c]`,

   `det(C_H C_H^T)=sum_U det(C_H[:,U])^2=G_H`.

2. The manuscript's `V_2` is the sum over ordered disjoint row/column two-sets. Grouping by the row set gives exactly

   `V_2=sum_H G_H`.

3. By symmetry, `det(A[S,H])^2=w_H(S)`. Hence the B04 collar currency grouped by its middle set is

   `Xi_H=sum_{S,T disjoint from H and from each other} w_H(S)w_H(T)`.

   All terms are nonnegative, so allowing `S=T` and allowing overlaps can only increase the sum:

   `Xi_H <= (sum_S w_H(S))^2=G_H^2`.

4. Therefore

   `Xi_2=sum_H Xi_H <= sum_H G_H^2
        <= (max_H G_H)sum_H G_H
        =(max_H G_H)V_2`.

   Since the terminal collar has `V_2>=kappa^2>0`, division is legitimate. Combining with the source theorem's stronger ratio statement `Xi_2 >= (delta_*^2/2)V_2` gives

   `max_H G_H >= delta_*^2/2`.

No factor depending on `n`, the number of two-sets, or a local-minor count enters.

## B. Numerical constants

Use

`delta_*=0.85433514019113377100...`.

Then

`delta_*^2/2 = 0.36494426588270207...`,

`sqrt(delta_*^2/2)=delta_*/sqrt(2)=0.6041061710351104...`.

In the no-pivot chamber, `eta=0.01` and

`|A_12| < sqrt(eta^2+eta)=sqrt(0.0101)=0.1004987562112089...`.

For a symmetric two-by-two block the operator norm is at most its maximum absolute row sum, so

`||A[H,H]||_op < 0.01+0.1004987562112089
                 =0.1104987562112089`.

For the exact-zero receiver, substituting `det(CC^T)>=delta_*^2/2` yields

`e sqrt(2 pi)(delta_*^2/2)^(-1/4)
 =8.766531143873209... <8.766532`.

The projected affine coefficient density cap becomes

`e/sqrt(delta_*^2/2)=e sqrt(2)/delta_*
 =4.499675651055482...`,

and the receiver's inverse-radius split gives

`2 sqrt(2 pi M)=10.63433983616953...`.

These calculations use only positive quantities, so no sign branch is hidden.

## C. Scope checks

- `s_8(A)>=1` implies `n>=8` and `rank(A)>=8`, so all two-column Cauchy--Binet sums and the partner rank-at-least-three compiler are applicable.
- The strong-cross extraction uses only symmetry and the already-proved collar ratio; it makes no rotation of random coordinates.
- The exact-zero receiver conditions on literal original coordinates and explicitly allows arbitrary outside quadratic curvature and affine terms.
- The fleet04/B15 `C_0` compiler is applied only to the homogeneous specialization, exactly matching its stated scope. The affine `C_0` statement is sourced separately from the completed affine fixed-instance theorem.
- No continuity is inferred merely from `L^infinity` boundedness.
- The result does not claim the nonzero weak-self chamber is solved; in particular no perturbative continuity in `A[H,H]` is assumed.

Verdict on the new lemma and exact-zero application: **PASS (self-check)**. Multiplicity eight: **OPEN**.
