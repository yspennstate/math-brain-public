# Rigorous improvement and threshold analysis

Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This note assumes the singular-Schur repair in the sibling `SCHUR_REPAIR.md`.

## 1. The written argument already proves a smaller universal constant

In the normalized case `K=s=1`, the scalar-pivot truncated half-potential estimate can be kept at its exact displayed value rather than rounded to 600:

`C_H = 10(20+12 log 16)`.

The other alternatives used in Proposition `prop:pivot-H` are smaller:

- definite pair: `<=40 pi`;
- indefinite pair: `<=10(32+4 log16)+4/e`;
- no-pivot nine-direction full half potential: `<200`.

Thus the nine-direction proposition may be strengthened to

`sup_a E |Q-a|^{-1/2} <= C_H+1`.

At the scalar pivot of the main theorem, `|A_ii|>=1/100`, so

`||p_Q||_infty <= 10(C_H+1) = 2010+1200 log16`.

All other normalized branches are smaller (`<2400` in the no-pivot branch, `<40` in the definite-pair main branch, and `<251` in the indefinite-pair branch as presently estimated). Therefore the same proof yields the sharpened theorem

`||p_Q||_infty <= (2010+1200 log16) K^2/s`.

Numerically this constant is approximately `5337.106466687737`. The exact expression, not the decimal, is the proof statement.

No matrix/law/affine hypothesis changes.

## 2. Why the present architecture does not rigorously lower 17

The no-pivot route requires a crossing volume of order five because the determinant theorem gives the characteristic-function envelope

`|phi_Q(t)| <= min(1,(u_k/|t|)^(k/4))`.

Direct Fourier inversion requires exponent `k/4>1`, hence `k>=5`. At `k=4` the available estimate is the endpoint `O(1/|t|)`, whose integral diverges logarithmically; no uniform `L^infty` density follows from this estimate alone.

For order `k`, Proposition `prop:volume` selects a bad ratio index `r<=k-1`. The completion has

`rank R <=3r`, `rank R_LL<=r`, and `D=0` on the `2r` seed coordinates.

To contradict the restricted rank, one must force `r+1` large diagonal entries of `D`. From `s_m(A)>=1`, the global-rank estimate gives only `m-3r` such entries. Therefore the present argument requires

`m-3r >= r+1`, i.e. `m>=4r+1`.

For `k=5`, the worst possible selected ratio is `r=4`, so this mechanism requires `m>=17`. With `m=16` it forces only four large entries, which is compatible with `rank R_LL<=4`; the diagonal-dominance contradiction no longer follows.

Hence 17 is the lowest multiplicity justified by the **current determinant-plus-interpolation proof architecture**. This is not a lower-bound theorem for the underlying problem. A genuine reduction below 17 needs at least one new ingredient, for example:

- a bounded-density endpoint theorem at fourth crossing volume despite only `|t|^{-1}` Fourier decay;
- a completion with a stronger global/restricted rank tradeoff while retaining source provenance; or
- a new structural branch that handles the `r=4` survivor.

No such full-hypothesis ingredient was proved in this run, so I do not claim a threshold reduction.
