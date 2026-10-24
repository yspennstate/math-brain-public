SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T04:00:49Z.
attacking: strengthen the fixed-three-column result to an all-cross-minor entropy compiler and identify the exact finite-hub residue when disjoint determinant mass is small.

# r19 stronger addendum

Canonical mathematics now extends through `yspennstate/math-open-problems@601f3b5a79ffc72be9e2ef68b8d23c679eebdf50`, run folder `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T040049Z-account03-B02-qform-r19/`.

## Stronger theorem: QFORM-BALANCED-CROSSMINOR-ENTROPY-L1-v1

For an arbitrary original-coordinate cross block `B=A[I,J]` with `rank(B)>=3`, define

`W3(B)=sum_(|R|=|S|=3) det(B_[R,S])^2=e3(B^T B)`

and the canonical minor law `w_(R,S)=det(B_[R,S])^2/W3(B)`. If a probability law `mu<<w` has row inclusion marginals `p_i=P(i in R)<=1/2` and entropy `D=D(mu||w)`, then arbitrary within-bank self-curvature and arbitrary outside spectrum/couplings are allowed and

`|phi_Q(t)| <= min(1, pi^(3/2)e^(3/2)2^(-3/4) exp(D/4) W3(B)^(-1/4)|t|^(-3/2))`,

so

`||phi_Q||1 <=(6pi e/sqrt(2)) exp(D/6)W3(B)^(-1/6)`,

`||p_Q||inf <=(3e/sqrt(2)) exp(D/6)W3(B)^(-1/6)`.

The density is continuous on this branch. The proof is one physical-bank Cauchy--Schwarz followed by a determinant-expansion/entropy rank-one Brascamp--Lieb estimate on the graph integral. The exact determinant identity used is

`det(D_y+a^2B^T D_z B)=sum_(r,R,S) a^(2r)det(B_[R,S])^2 prod_(j notin S)y_j prod_(i in R)z_i`.

The scalar factors are controlled by the already source-valid sharp Young/Hausdorff--Young estimates. No conditional cap, post-rotation independence, or scalar law-uniform Fresnel decay enters.

## Automatic balanced law

For iid canonical minors `(R,S),(R',S')`, let `delta_row=P(R cap R'=empty)`. Conditioning on row-disjointness gives a balanced `mu` with `D<=log(1/delta_row)`, hence

`||p_Q||inf <=(3e/sqrt(2)) delta_row^(-1/6)W3(B)^(-1/6)`.

The transpose version uses `delta_col=P(S cap S'=empty)`.

## Exact small-disjointness residue

If `delta_row` is small, there exists a fixed physical row triple `H` with

`W3(B_[I\H,J])<=delta_row W3(B)`.

Similarly small `delta_col` produces a column triple `L` with

`W3(B_[I,J\L])<=delta_col W3(B)`.

If both are small, at least `1-delta_row-delta_col` of the determinant-weighted three-minor mass touches both a fixed row triple `H` and fixed column triple `L`. Thus failure of the new Fourier certificate localizes the third compound mass to a six-original-coordinate hub rather than an unspecified high-dimensional obstruction.

## Global cut identity

For the full symmetric `A`, let

`T3(A)=sum_(R,S)det(A_[R,S])^2=e3(A^2)>=1`

under the three-large-eigenvalue hypothesis, and split by `h=|R cap S|`. If `T^(0)` is the disjoint-triple part, a random physical bipartition satisfies exactly

`E W3(A[I,J])=T^(0)/64`.

Hence the all-disjoint spectral-volume branch reduces to the new Fourier theorem unless it yields the six-coordinate compound hub. If `T^(0)` is small, a universal fraction of `T3` lies in overlap-one/two/principal-triple geometries. The remaining global debt is therefore `QFORM-COMPOUND-HUB-OR-OVERLAP-COMPILER-v1`: aggregate those finite-overlap classes into the already-paid pivot/Schur, pair/hub, principal/zero-diagonal, grouped-star, ridge, or diffuse exits without selecting a tiny local minor.

The completed designated partner account04/B02 was already applied in the main r19 report to a genuine low-frequency L2 / high-frequency L1-tail hybrid inequality. Full QFORM and the full target-wide L1 criterion remain OPEN. Execution remains `WITHOUT_VERIFIED_BRAIN`; no scheduler/task/notification/email/Drive/workflow/public-release/paid-model/API/Codex/cross-account state was changed.
