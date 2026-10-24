SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T15:22:02Z.
attacking: the true near-coloop survivor by compiling the newest mixed-hub Fresnel theorem into a two-physical-hub invariant and paying the first heavy-leaf branch without conditional projection-density caps.

# Early substantive checkpoint — two-hub Schur/Fresnel invariant

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T152202Z-account03-B16-QFORM-r32`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Full QFORM remains OPEN; global continuity remains OPEN.

## 1. Source actually used

The analytic input is the completed mixed-hub Fresnel theorem (Theorem H) in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`.

That theorem keeps genuine original-coordinate hub variables, uses only the cap-one product laws, and permits arbitrary hub/outside blocks. It does not declare projected coordinates independent.

The B16 predecessor is

`yspennstate/math-open-problems@321c962d54aaeb625a9417dea9842f0910c13714`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T132339Z-account03-B16-QFORM-r29/REPORT.md`.

Its hard exact-rank-three survivor has a physical near-coloop row `r_0=sqrt(c)e`, with `rho=1-c<1/64`, residual rows

`r_j=s_j e+w_j`, `w_j perpendicular e`, `h_j=||w_j||^2<1/64`,

and all physical diagonals `<1/64`, all hub-star atoms `|A_0j|<1/16`.

## 2. General hub-set invariant from Theorem H

Let an exact-rank-three symmetric matrix be partitioned into a physical hub set `H` of size `k=1` or `2` and leaves `L`. Assume the principal hub block `B=A_HH` is invertible. Write

`A = [[B,C],[C^T,A_LL]]`

and the Schur complement

`S=A_LL-C^T B^(-1)C`.

Exact rank three gives `rank S=3-k`. Write

`S=V Lambda V^T`, `V^T V=I_(3-k)`, with `Lambda` invertible. Define three-dimensional deterministic coefficient rows

`b_h=(B_{h,*},0)` for `h in H`,
`b_j=(C_{*,j},V_{j,*})` for `j in L`,

and the coefficient matrix

`M=diag(B^(-1),Lambda)`.

Then exactly

`A=Rtilde M Rtilde^T`,

where the rows of `Rtilde` are the `b_i`. Put

`Gamma=sum_all_i b_i b_i^T`,
`G_L=sum_(j in L)b_j b_j^T`.

If `G_L>0` and every leaf leverage obeys

`d_j=b_j^T G_L^(-1)b_j <=1/2`,

Theorem H (equivalently its Fresnel/BL proof with the `k` physical hubs charged only by their cap-one densities) gives

`|phi_Q(t)| <= (4pi)^(3/2)|t|^(-3/2)[|det M| det G_L]^(-1/2)`.

Therefore

`||p_Q||_infinity <=12[|det M|det G_L]^(-1/3)`,

and the density is continuous and vanishes at infinity.

Now let `P` be the physical orthogonal projector onto `range(A)`. If `U_H` is the matrix of hub rows `b_h`, then

`P_HH=U_H Gamma^(-1) U_H^T`.

The matrix determinant lemma gives

`det G_L = det Gamma * det(I_k-P_HH)`.

If `D` is the product of the three nonzero eigenvalue magnitudes of `A`, then

`D=|det M|det Gamma`.

Hence the exact invariant form is

`boxed: ||p_Q||_infinity <=12[D Delta_H]^(-1/3),`

where

`Delta_H:=det(I_k-P_HH)`.

This is a direct application/compilation of the completed Theorem H, not a new proof of that analytic theorem.

## 3. Two-hub specialization in the B16 near-coloop frame

For the B16 spectral frame, take `H={0,j}`. The range projector is `P=RR^T`, so

`P_00=c`, `P_jj=s_j^2+h_j`, `P_0j=sqrt(c)s_j`.

Thus

`Delta_{0j}
 =det([[rho,-sqrt(c)s_j],[-sqrt(c)s_j,1-s_j^2-h_j]])
 =rho(1-h_j)-s_j^2`.

Define the normalized one-hub leaf leverage

`q_j:=s_j^2/rho+h_j`.

Then the determinant identity simplifies exactly to

`boxed: Delta_{0j}=rho(1-q_j).`

Consequently, whenever the remaining leaves satisfy the two-hub Theorem-H leverage gate,

`boxed: ||p_Q||_infinity <=12[D rho(1-q_j)]^(-1/3).`

In the target exact-rank-three case `D>=1`.

## 4. First quantitative branch newly paid

Suppose

`1/128 <= rho <1/64`,
`1/2 < q_j <=3/4`,

and, after reserving the two physical hubs `{0,j}`, all remaining leaf leverages relative to their exact coefficient Gram are at most `1/2`.

Then

`Delta_{0j}=rho(1-q_j) >=(1/128)(1/4)=1/512`.

The invariant bound above gives the continuous-density estimate

`boxed: ||p_Q||_infinity <=12*512^(1/3)=96.`

This branch is not covered by the one-hub Schur-aligned gate, because `q_j>1/2` is exactly its failure. The second physical hub absorbs that single heavy leaf while retaining the original-coordinate product structure.

Because the inherited B16 survivor has `h_j<1/64`, any one-hub gate failure satisfies

`s_j^2/rho >1/2-h_j >31/64`.

Thus there can be at most two initial gate-failing physical leaves. If in addition `q_j>3/4`, then

`s_j^2/rho >3/4-1/64=47/64`,

so one named physical leaf alone carries more than `47/64` of the entire longitudinal Parseval mass. The remaining unpaid medium-collar obstruction is therefore either this single very-heavy leaf or failure of the second-stage leaf gate after removing a moderate heavy leaf.

This is a real narrowing of the r29 same-bank obstruction, not a claim that the full near-coloop collar is closed.
