# Addendum — near-rankdrop sharpens to a double-coloop

This is a compatible late strengthening of `REPORT.md`; full QFORM remains open.

### `QFORM-RANK2-CROSS-SOURCE-WELLCONDITIONED-v1`

Retain the exact-rank-three setup of the report and account03/B19 r27:

`A=RMR^T`, `R^TR=I_3`, all `|eig M|>=1`, original partition `I union J`, `P=R_I`, `S=R_J`, `G=P^TP`, `H=S^TS=I-G`, `rank(P)=3`, `rank(A_IJ)=2`, and `rho=s1(A_IJ)s2(A_IJ)>=rho0=sqrt(29/3072)`.

Let `W=(ker H)^perp`. If

`lambda_min(G|_W)>=a>0`,

then the source self block `B=A_II=PMP^T` has smallest nonzero singular value at least `a`, hence for the transverse unit vector `r` in account01/B19's receiver,

`R_perp=||Br||>=a`.

Indeed, `Q=P G^(-1/2)` has orthonormal columns, and on `range(P)` the self block is orthogonally represented by

`G^(1/2) M G^(1/2)`.

Therefore

`s_min^+(B) >= lambda_min(G) s_min(M) >= a`.

Applying the product-safe receiver

`||p_Q||inf <= C_* R_perp^(-1/4) rho^(-3/8)`, `C_*=2^(15/4)3^(-3/8)`,

gives

`||p_Q||inf <= C_* a^(-1/4) rho0^(-3/8)`.

At `a=1/64`,

`boxed: ||p_Q||inf <60.420 <61`.

Consequently the near-rankdrop alternative from the main report can be sharpened. Let `0<h1<=h2<1` be the eigenvalues of `H|W`; then the eigenvalues of `G|W` are `1-h1,1-h2`. If `h1<1/64` but `1-h2>=1/64`, this addendum pays the branch by `<61`. Hence every still-unpaid near-rankdrop survivor must satisfy simultaneously

`h1<1/64`,
`h2>63/64`.

It is a genuine **double-coloop / complementary-line-bank** state: one spectral-frame direction has almost all of its physical mass on the I side and the other has almost all of its mass on the J side. This conclusion is exact and uses no perturbative deletion.

Combining with `QFORM-RANK2-CROSS-DIFFUSE-J-REPARTITION-v1`, the first exact-rank-three rank-two-cross debt is now only:

1. a double-coloop state `h1<1/64<h2` with in fact `h2>63/64`; or
2. when `lambda_min(H|W)>=1/64`, a normalized-heavy J core `{j: ell_j>1/16}` of cardinality at most 31.

Call this narrower gate `QFORM-RANK2-CROSS-DOUBLECOLOOP-OR-HEAVYCORE-v1`.
