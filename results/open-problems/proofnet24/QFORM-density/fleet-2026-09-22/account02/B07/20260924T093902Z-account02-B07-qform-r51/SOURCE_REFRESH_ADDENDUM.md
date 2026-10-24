# Final source-refresh addendum — account02/B07 r51

After REPORT.md was committed, the designated partner account03/B07 published a newer completed r51 proof:

`yspennstate/math-open-problems@87ddc6e4974103cb1f992bab5cfeccadee810ddb`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T093712Z-account03-B07-qform-r51/REPORT.md`.

It proves `QFORM-FINITERANK-DIFFUSE-CARRIER-E3-v1` and, crucially for the present coordinate-selection run, source-pins the completed account02/B03 theorem

`QFORM-Z3-CROSSING-MARGINAL-FREE-v1`

at `math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`. For every literal physical cut M=A[I,J] with `Z3=e_3(MM^T)>0`, that theorem gives

`||p_Q||_infinity <= C3 Z3^(-1/6)`,
`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`,

with arbitrary same-side blocks, affine terms, outside coordinates, signs and additional spectrum retained; the density is continuous on that branch.

This newer receiver strengthens, but does not invalidate, the pinned-e5 Theorem-D application already proved in REPORT.md. The e5 route remains an actual completed-source application at equation (3.6), and Lemma 4.1 remains a dimension-free stability theorem for the actual volume-sampling marginals. For the live r50/r51 coefficient state, however, the marginal-free E3 theorem removes the need to impose the stricter `H(tau)<=1/2` gate.

## Marginal-free upgrade of the balanced-cut theorem

Under Corollary 4.2 of REPORT.md, let

`A[L,L]=R+E_L`, `rank R=r>=3`, `||E_L||op<=eta`,
`R=U Lambda U^T`, `sigma=s3(R)`,
`delta=max_i ||U(i,:)||^2`, `rho=sqrt(r delta)<1`,
`a=(1-rho)/2`.

Lemma 3.1 supplies a literal physical partition `L=I union J` for which the base crossing satisfies

`s3(R[I,J])>=a sigma`.

The retained tail gives, for the ACTUAL crossing `M=A[I,J]`,

`s3(M)>=a sigma-eta =: mu`.

Therefore whenever `mu>0`,

`Z3=e_3(MM^T)>=s3(M)^6>=mu^6`,

and the completed marginal-free physical-E3 theorem yields the full ambient inequality

`boxed: ||p_Q||_infinity <= C3/(a sigma-eta).`

No single minor is selected; the Cauchy-Binet three-volume of the actual physical crossing is the analytic currency.

In the convenient diffuse regime `delta<=1/(4r)`, `a>=1/4`, so

`boxed: sigma>4 eta  =>  ||p_Q||_infinity <= C3/(sigma/4-eta).`

This is `QFORM-BALANCED-CUT-MARGINALFREE-UPGRADE-v1`.

## Direct live H62-rank4 consequence

For the account02 r50 localized-exception state,

`eta=0.001631502080283948`, `|H|<=62`, `L=S\H`,
`dist_op(A[L,L],rank<=4)<eta`.

If a rank-four approximant R has

`max_i ||U(i,:)||^2<=1/16`

and

`s3(R)>4 eta = 0.006526008321135792`,

then the full ambient law is already paid by

`boxed: ||p_Q||_infinity <= 10.5501688311648/(s3(R)/4-0.001631502080283948).`

For example, if `s3(R)>=8 eta`, then `s3(M)>=eta` and the branch has

`||p_Q||_infinity < 6466.1`.

Thus the earlier sufficient scale `s3(R)>=260 eta` from the pinned-D marginal gate is not the final live threshold; after the partner r51 refresh, the diffuse rank-four local branch is paid as soon as its third approximant singular value exceeds `4 eta`.

## Combined final survivor with the newer partner

The partner r51 global routing says that for the r50 decomposition

`A=diag(C,0_S)+P_54+G`, `rank P_54<=54`, `||G||op<0.001646760870`,

one of the following occurs:

1. `s3(C)>1/64` — the physical T-side three-curvature/affine branch remains unpaid;
2. `s3(C)<=1/64` and the resulting rank<=56 carrier has maximum physical leverage <=1/16 — paid by a literal E3 crossing with continuous density `<161.751`;
3. otherwise there is a literal heavy set `K`, `|K|<=895`; if `s3(A[K,K])>=1/64` the physical-core receiver pays `<16625.398`, while the residual has weak principal third singular value on K.

Combining that routing with the present balanced-cut upgrade, every still-unpaid moderate-energy state must ALSO avoid the local diffuse rank-four exit on `L=S\H`. In particular, no rank-four approximant to `A[L,L]` may simultaneously have

`max physical range leverage <=1/16`

and

`s3(R)>0.006526008321135792`.

So the first unpaid state is now genuinely concentrated/weak on both descriptions: either the T-side has three-curvature with arbitrary affine terms, or the near-rank-two-T branch contains a bounded heavy packet `|K|<=895` with weak principal third singular value, while the complementary H62 local approximant is rank<=3, has weak s3 at the displayed scale, or has physical range leverage >1/16. The separate `E_star>1` branch remains unpaid.

Full unrestricted QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN; continuity holds on the paid physical-E3 branches above.