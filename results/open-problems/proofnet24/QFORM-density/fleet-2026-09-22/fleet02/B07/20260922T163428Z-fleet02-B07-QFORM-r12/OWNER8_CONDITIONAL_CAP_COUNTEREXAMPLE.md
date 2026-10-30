# Revision 2026-09-22.8 correction: the proposed uniform conditional 3-D projection-density cap is false

**Status:** `CANDIDATE_REFUTED` for one intermediate bridge only; the full QFORM conjecture remains OPEN.

The later owner revision 2026-09-22.8 proposes the following route: choose three large spectral coordinates `(Y1,Y2,Y3)`, condition on the remaining spectral coordinates, use a rank-three coarea estimate, and prove a universal bound on the conditional three-dimensional density of `(Y1,Y2,Y3)` given the rest. The rank-three coarea idea may still be useful, but the stated **uniform conditional projection-density bound is false under the exact target hypotheses**, already in dimension four with uniform product inputs.

## Exact target-valid construction

Let `X1,X2,X3,X4` be independent `Uniform[0,1]` random variables. Their densities are exactly one on `[0,1]`.

Use the orthonormal spectral basis

`r1=(e1+e4)/sqrt(2)`,
`r2=e2`,
`r3=e3`,
`r4=(e1-e4)/sqrt(2)`,

and eigenvalues

`lambda1=lambda2=lambda3=1`, `lambda4=0`.

Thus

`A = r1 r1^T+r2 r2^T+r3 r3^T`

`  = [[1/2,0,0,1/2],
      [0,1,0,0],
      [0,0,1,0],
      [1/2,0,0,1/2]]`,

so `spec(A)={1,1,1,0}` and the exact three-large-eigenvalue hypothesis holds. The spectral variables are

`Y1=(X1+X4)/sqrt(2)`,
`Y2=X2`,
`Y3=X3`,
`Y4=(X1-X4)/sqrt(2)`,

and

`Q=Y1^2+Y2^2+Y3^2`.

## Conditional density calculation

The map `(X1,X4) -> (Y1,Y4)` is orthogonal, so its Jacobian has absolute value one. Hence `(Y1,Y4)` has joint density one on the rotated unit square. Fix

`v in (-1/sqrt(2),1/sqrt(2))`.

The inverse transform is

`X1=(Y1+v)/sqrt(2)`,
`X4=(Y1-v)/sqrt(2)`.

The constraints `0<=X1,X4<=1` are equivalent to

`Y1 in [-v,sqrt(2)-v] intersect [v,sqrt(2)+v]`

`    = [|v|, sqrt(2)-|v|]`.

This interval has length

`ell(v)=sqrt(2)-2|v|`.

Therefore

`p_{Y4}(v)=ell(v)`

and the exact regular conditional density is

`p_{Y1 | Y4=v}(y)
 = ell(v)^(-1) 1_{[|v|,sqrt(2)-|v|]}(y)`.

Because `(Y2,Y3)` is independent of `(Y1,Y4)` and has unit density on `[0,1]^2`,

`||p_{(Y1,Y2,Y3) | Y4=v}||_infinity
 = 1/(sqrt(2)-2|v|).`

As `|v| -> 1/sqrt(2)`, this tends to infinity. More strongly, for every finite `M`, the set of conditioning values satisfying

`1/(sqrt(2)-2|v|)>M`

has positive `Y4` probability. Hence there is no universal finite essential bound on the conditional three-dimensional spectral projection density.

This is not a pathology from a vanishing-density input, a moment assumption, or a rotated-independence error. The source law is the simplest cap-one product uniform law, the spectral map is orthogonal, and the matrix satisfies the exact target eigenvalue condition.

## Why this does not refute QFORM

The failure is only in the proposed intermediate cap. In this example, conditional on `Y4=v`, the variables `Y2=X2` and `Y3=X3` remain independent unit-density uniforms, and

`Y2^2+Y3^2`

has bounded density (indeed its two-square Beta bound is at most `pi/4` for `Uniform[0,1]`). Convolution with the independent conditional variable `Y1^2` cannot increase that `L^infinity` bound. Thus the conditional **output** density can stay uniformly bounded even while the conditional **three-dimensional input** density cap diverges.

The repair is therefore not to bound `||p_{(Y1,Y2,Y3)|rest}||_infinity` pointwise in the rest. A successful rank-three coarea route must retain more of the original product structure along the conditioned affine fiber, or directly bound the conditional quadratic output by a weighted-fiber / Brascamp--Lieb / grouped-coordinate argument before normalizing by a potentially tiny slice mass.

This counterexample is consistent with the earlier live corrections that conditional density caps and unrestricted fiber-supremum arguments can blow up after linear conditioning.

**Conclusion:** the full QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`; the revision-2026-09-22.8 proposed universal conditional 3-D projection-density bridge is `REFUTED` as stated.
