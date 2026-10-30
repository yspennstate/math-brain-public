SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-23T19:44:07Z.
attacking: the exact-rank-three hybrid/near-null physical direction; consume the ruled-side theorem, close the true coloop small-hub-square endpoint, and isolate endpoint-stable source-product currency in the positive-leakage collar.

# Early substantive checkpoint — endpoint-stable hub-star x transverse-area packet

Programme: `QFORM-DENSITY-3EIG-20260922`. Full unrestricted QFORM remains OPEN.

## First unpaid implication

After the completed fleet03/B10 r26 transverse payment, the live near-coloop state is

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`, `D=|det M|>=1`,

with one ORIGINAL hub row `u_0=sqrt(c)e`,

`c>63/64`, `rho=1-c in (0,1/64)`, `alpha=e^T M e`,

`|A_00|=c|alpha|<1/64`, `|alpha|<1/16`,

and leaf rows

`u_j=t_j e+p_j`, `p_j perp e`,

satisfying

`sum t_j^2=rho`, `sum t_j p_j=0`, `sum p_j p_j^T=I_2`,

and, after r26's completed physical-pivot/pair exits,

`||p_j||^2<1/61` for every leaf.

The first unpaid implication is still endpoint-stable gluing as `(alpha,rho)->(0,0)`, but the calculation below shows that the geometry itself does NOT lose a factor `rho`: a uniform product-preserving hub-star x transverse-area packet survives all the way to the coloop endpoint. Thus the remaining loss is analytic/source-topological, not lack of aggregate physical currency.

## Theorem — `QFORM-NEARCOLOOP-STAR-AREA-PACKET-v1`

Let

`g_j=A_0j=sqrt(c) e^T M u_j`

be the actual physical hub-to-leaf row. Then there is a partition of the ORIGINAL leaf coordinates `L=I sqcup J` such that, with

`G_I=sum_(i in I) p_i p_i^T`,

one has

`boxed: ||g_J||_2^2 det(G_I) > 240975/1998848 > 0.12055.`

In particular the packet is uniform as `rho->0`; no projected coordinate is declared independent.

### Proof

Put `v=P_(e^perp) M e`. Since `e^TMe=alpha`,

`||v||^2=||Me||^2-alpha^2 >=1-alpha^2`,

using `sigma_min(M)>=1`. By the Parseval ledger,

`g_j=sqrt(c)(alpha t_j+v.p_j)`

and therefore

`sum_j g_j^2
 =c[alpha^2 sum t_j^2+2alpha v.(sum t_jp_j)+v^T(sum p_jp_j^T)v]
 =c(alpha^2 rho+||v||^2)
 =c(||Me||^2-c alpha^2)
 >=c(1-c alpha^2)
 > (63/64)(255/256).`                                      (E1)

For leaf pairs define the transverse Pluecker weights

`a_ik=det(p_i,p_k)^2`, `i<k`.

Two-dimensional Cauchy--Binet gives

`sum_(i<k) a_ik=det(sum p_jp_j^T)=1`.                    (E2)

The weighted degree at a leaf `j` is exactly

`d_j=sum_(k!=j)a_jk=||p_j||^2`,                           (E3)

again because the transverse frame is Parseval. Hence `d_j<1/61` by the partner gate.

Colour every leaf independently into `I` or `J` with probability `1/2`. Expand

`||g_J||^2 det(G_I)
 =sum_j g_j^2 1_{j in J}
   sum_(i<k) a_ik 1_{i,k in I}`.

A term survives precisely when `j` is disjoint from the Pluecker edge `{i,k}`, and then with probability `1/8`. Therefore

`E[||g_J||^2 det(G_I)]
 =(1/8) sum_j g_j^2 (1-d_j)
 >(60/(61*8)) sum_j g_j^2`.                              (E4)

Insert (E1):

`E[||g_J||^2 det(G_I)]
 >(15/122)(63/64)(255/256)
 =240975/1998848
 =0.1205569407... .`                                      (E5)

Some deterministic original-coordinate split attains at least its expectation. QED.

## Immediate source consequence already consumed

The required ruled-level theorem in

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

is used, not reproved: after choosing the global sign so an indefinite exact-rank-three core has signature `(2+,1-)`, every majority-sign level `s>=0` already satisfies

`p_Q(s)<=pi sqrt(2)`.

Thus the punctured near-coloop work may be confined to the minority/two-sheet side `s<0`; the ruled side is no longer an unpaid subproblem.

## Endpoint update from the fresh three-variable coarea theorem

The new complete theorem at

`math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae:proofnet24/QFORM-density/interactive/20260923T191000Z-small-hub-square-coarea/GENERAL_3D_CORE.md`

closes the TRUE spectral-coloop endpoint `rho=0` even when the hub Rayleigh coefficient is nonzero. Indeed, if `c=1`, the leaves lie exactly in `e^perp`; choose an orthonormal transverse basis and let `(L,V)` be the corresponding two orthogonal projections of the original leaf product vector. Their joint density is at most two. The physical hub `X_0` is independent of `(L,V)`. The resulting exact three-variable quadratic core is orthogonally congruent to `M`, hence has smallest singular value at least one, while its hub diagonal is `alpha=A_00` with `|alpha|<1/64`. The cited general three-variable theorem therefore gives

`boxed: ||p_Q||_infinity <65}`                                  (E6)

at `rho=0`, with no condition `alpha=0` and no post-rotation independence assertion.

So both coordinate axes of the corner are paid: `alpha=0` by the completed fleet03/B10 null-hub mixed-Fresnel theorem, and `rho=0` by (E6). The genuine survivor is the punctured corner `alpha rho !=0`.

## Next calculation

The next step is to put the punctured corner into an exact no-division Witt normal form and identify the single residual mode that disappears at `alpha=0`; this must be done before attempting any reciprocal projected-crossing payment. The new packet (E5) is the endpoint-stable aggregate resource that such a receiver should spend.