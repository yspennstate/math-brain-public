SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-23T22:16:26Z.
attacking: the positive-leakage near-null/near-coloop endpoint; expose the exact scalar-Schur discriminant that stays nondegenerate as the hub pivot tends to zero, and test whether the existing mixed-basis receiver has a genuine structural collision obstruction.

# Early substantive checkpoint

Continue from account03/B10 r26. In the surviving exact-rank-three state write

`A=R M R^T`, `R^T R=I_3`, `D=|det M|>=1`,

with physical hub row `u_0=sqrt(c)e`, `c>63/64`, `rho=1-c<1/64`, normalized Rayleigh coefficient `alpha=e^T M e`, `0<|alpha|<1/16`, and leaves

`u_j=t_j e+x_j v+y_j q`,

where `(e,v,q)` is orthonormal, `v` points along the transverse component of `Me`, and every surviving leaf satisfies `x_j^2+y_j^2<1/61`. Put

`M=[[alpha,s,0],[s,b,k],[0,k,d]]`.

Since `sigma_min(M)>=1`, `s^2+alpha^2=||Me||^2>=1`, hence `s^2>255/256`. Parseval gives

`sum t_j^2=rho`, `sum x_j^2=sum y_j^2=1`, and all three cross sums `sum t_j x_j=sum t_j y_j=sum x_j y_j=0`.

Define

`z_j=x_j+(alpha/s)t_j`.

Then the physical hub cross row is

`g_j=A_0j=sqrt(c)s z_j`,

and exactly

`sum z_j^2=1+(alpha^2/s^2)rho`.

For the nonzero physical pivot `a_0=A_00=c alpha`, scalar completion has leaf Schur remainder

`S=A_LL-g g^T/a_0=P K P^T`,

where `P` has rows `p_j=(x_j,y_j)` and

`K=[[b-s^2/alpha,k],[k,d]]`.

The two key exact identities are

`det K=det M/alpha`,

and therefore, for every two leaves `j,k`,

`det S_{ {j,k} }=(det M/alpha) det(p_j,p_k)^2`.

Thus the Schur curvature diverges exactly at the reciprocal rate of the scalar pivot. Applying the designated partner account04/B10 theorem `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1` to the current full leaf bank gives disjoint original-coordinate banks `S0,Y,Z` with `M(G_Y,G_Z)>=2/81`. Consequently

`sum_{j in Y,k in Z} |det S_{ {j,k} }| >= 2D/(81|alpha|)`,

and multiplication by the actual scalar pivot yields the endpoint-stable aggregate inequality

`|A_00| sum_{j in Y,k in Z}|det S_{ {j,k} }|
 >= 2cD/81 > 7/288`.

This is a genuine partner splice at an actual inequality. It shows that the near-zero scalar pivot does not destroy aggregate Schur curvature; reciprocal single-pivot bounds lose the cancellation by paying the two factors separately.

A second exact normal form, before scalar completion, is also useful. With

`kappa=-alpha+b alpha^2/s^2`, `eta=-k alpha/s`,

one can shear only the leaf algebra to obtain a two-channel residual matrix

`N=[[kappa,eta],[eta,d]]`

on the projections `(t.X_L,y.X_L)`, and

`det N=alpha det M/s^2`.

Since `gamma^2=||g||^2=c s^2[1+(alpha^2/s^2)rho]`, this gives the scale-free discriminant identity

`(|det N| gamma^2)/|A_00|
 =D[1+(alpha^2/s^2)rho] >=D>=1`.

So the surviving endpoint already carries a universal algebraic discriminant. The remaining question is analytic/product-theoretic: preserve this joint currency before a fiber supremum, scalar square peel, or reciprocal local-minor selection separates it.

Execution remains `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not being counted as native learned-memory ingestion. Full exact rank three and full QFORM remain OPEN.