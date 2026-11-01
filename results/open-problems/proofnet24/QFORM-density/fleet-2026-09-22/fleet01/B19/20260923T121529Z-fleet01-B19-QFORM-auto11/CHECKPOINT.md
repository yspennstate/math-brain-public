# Substantive checkpoint — STAR leaf-cross paid-or-low-rank classification

Let the r31 balanced STAR cut be `N=B[J,K]`, so `E=||N||_F^2>c0=65025/262144`, and let `x_j=s_j(N)^2`, `T2=sum_{j>=3}x_j`. The r31 D5 exit already pays unless `x1+x2+x3+x4>(63/64)E`.

Set `delta=1/64`. If `x2<delta E`, then the D5 survivor identity gives `x1>(63/64-3/64)E=(15/16)E`, hence `sum_{j>=2}x_j<E/16`: a genuine near-rank-one matrix-level survivor. If `T2<delta E`, then `x1+x2>(63/64)E`: a genuine near-rank-two survivor.

Assume now `x2,T2>=E/64`. If `T2/x3>=225` and the top-two left singular projection has diagonal <=1/2, the completed PEER_TAIL_EXTENSION theorem gives

`||p_Q||inf <=(9sqrt(3)e/2)[x1 x2 T2]^(-1/6) <=36sqrt(3)e E^(-1/2) <340.32`,

using `E>c0`. The same applies after transposing `N`, so the only unpaid high-stable-rank case has a >1/2 top-two leverage coordinate on BOTH sides.

If instead `T2/x3<225`, then `x3>E/(64*225)=E/14400`, hence

`Z3=e3(N^T N)>=x1 x2 x3>E^3/58982400`.

If the three-volume sampling marginals on either side are all <=2/3, orient that side as the constrained side in the completed D' theorem to obtain

`||p_Q||inf <=9sqrt(3e) Z3^(-1/6) <1018.13`.

Thus an unpaid low-tail-stable-rank case has a row marginal `alpha_i>2/3` AND a column marginal `beta_j>2/3`; under the normalized 3-minor volume distribution, the mass of minors containing both `(i,j)` is at least `alpha_i+beta_j-1>1/3`.

This is the new target-level route being completed: after D5, the STAR cut is either universally paid, within Frobenius distance `sqrt(E/16)` of rank one, within distance `sqrt(E/64)` of rank two, or carries one of two explicit double physical anchors (top-two leverage on both sides, or three-volume marginals >2/3 on both sides). No tail is discarded.
