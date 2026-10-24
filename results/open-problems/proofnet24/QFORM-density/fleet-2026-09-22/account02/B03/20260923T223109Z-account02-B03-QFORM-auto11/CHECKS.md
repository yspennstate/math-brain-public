# Finite sanity checks for A_m(a,b)

The theorem in `REPORT.md` is analytic for all `m>=2`. As a finite sanity check, the family was instantiated at `a=1.7`, `b=-1.3` and `m=2,3,4`.

Observed nonzero eigenvalues in each case: `[-1.7,-1.3,1.7]`.

Exhaustive enumeration of all disjoint physical cuts for these dimensions gave maximum full cross rank `2`. After Schur-complementing any one `V` coordinate (all such pivots are equivalent by symmetry), exhaustive cut enumeration gave maximum residual cross rank `1`.

These computations are only checks. The all-`m` statements follow exactly from the decomposition into the rank-one star crossing plus the rank-one `J_m` crossing, and from the exact Schur cancellation

`(b/m)J_{m-1} - ((b/m)1)((b/m)1)^T/(b/m)=0`.

`QFORM_B03_GROUPED_LOCAL_SEPARATION_CHECK_PASS`
