# B07 improvement attempt: exact counting/rank sharpness and the 17-to-16 barrier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`

Pinned source: manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **complete obstruction to three tempting bookkeeping reductions; no unconditional multiplicity reduction claimed.**

The baseline order-five no-pivot proof uses a sampled order-r interpolation with

`rank R <= 3r`, `rank R[L,L] <= r`, `D=0` on the 2r seed coordinates,

and a child-minor counting factor `(r+1)^2`. Exact finite examples show all three pieces are genuinely needed at the strength stated.

## Sharp child multiplicity

For `m=r+1`, let `C_ij=1/(i+j+1)` and form the symmetric bipartite no-pivot matrix `A=[[0,C/100],[C^T/100,0]]`. For the child consisting of all m left and all m right coordinates, every row/column deletion is an invertible Cauchy r-minor. Hence that one ordered child has exactly `(r+1)^2` nonsingular parents for r=1,2,3,4. Sorting signs vary, but squaring removes them exactly. Therefore no symmetry convention permits replacing `(r+1)^2` by a smaller universal parent-count factor in this argument.

## Sharp existential seed quantifier

For

```
A = (1/1000) * [[-6, 5, 3,-2],
                [ 5, 4, 1, 4],
                [ 3, 1, 4, 3],
                [-2, 4, 3,-2]],
```

the matrix is no-pivot and at r=1 the sampling threshold is `4V2/V1=247/8000000`. The seed `(S,T)=({1},{2})` has `||F||_F^2=149/12500000` below threshold, whereas `({2},{3})` has `||F||_F^2=97/200000`, more than fifteen times the threshold. Thus the weighted-expectation proof supports exactly an existential good seed, not a universal good seed.

## Simultaneous sharpness of global and restricted rank

For one scaled block

```
A=(1/250)*[[-2,-2,-2],[-2,-2,-1],[-2,-1,-2]],
S={1}, T={2}, L={3},
```

the canonical completion has `E=0`, global `rank R=3`, and restricted `rank R[L,L]=1`, while the block is no-pivot. Direct sums of r copies give, simultaneously for every r=1,2,3,4,

`rank R=3r`, `rank R[L,L]=r`.

So neither symmetry nor the no-pivot assumption yields a universal `rank R<=2r` repair for this completion.

## Consequence

For the density-producing order-five branch, r=4 can be the small-ratio index. With sixteen unit-scale singular values, the existing global rank loss can force only `16-12=4` large diagonal directions, while the restricted block may genuinely have rank four. The strict-diagonal-dominance contradiction needs five. Therefore this exact architecture cannot be lowered from 17 to 16 by improving only the ordered-minor multiplicity, choosing a different arbitrary seed, or replacing `3r` by `2r`.

Using order four instead does not close the analytic side either: the current leverage-free determinant estimate gives characteristic-function decay only at the `|t|^{-1}` endpoint, not an L1 envelope. A complete lower-threshold theorem therefore needs a genuinely stronger analytic endpoint/cancellation statement or a new structural decomposition preserving arbitrary rough product laws, signs, affine terms and the full spectrum.

This is a method barrier, not an optimality theorem for 17 and not a counterexample to any lower-multiplicity density theorem.
