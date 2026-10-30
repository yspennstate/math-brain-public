# Exact checks — fleet02/B20 20260923T153203Z

All checks are deterministic coefficient/arithmetic checks. They do not simulate random laws and do not replace any probabilistic hypothesis.

## Partner constants

`E_M > 961/4096`, hence `||M||_F>31/64`.

`ell0^2=749373/2097152` and

`ell0^2-(19/32)^2`
`=749373/2097152-361/1024`
`=10045/2097152>0`,

so `ell0>19/32`.

## Tail fourth-volume inequality

For tail weights `0<=x_i<c=1/4096`, total `T=sum x_i`, the ordered distinct-product sums satisfy

`S_(m+1)=sum_(i1,...,im distinct) x_i1...x_im (T-x_i1-...-x_im)`
`       >=(T-mc)S_m`.

Thus if `T>=1/64`,

`24 e4 = S4 >=T(T-c)(T-2c)(T-3c)`
` >=(1/64)(63/4096)(62/4096)(61/4096)`.

## D5 floor and density constant

Using `s1^2>(19/32)^2=361/1024`,

`Z5=e5(W^T W)`
` > (361/1024)*(1/64)*(63/4096)*(62/4096)*(61/4096)/24`
` =14335671/18014398509481984`
` =7.957896008825571e-10`.

The pinned D5 receiver gives

`5*sqrt(2e)*Z5^(-1/10)=94.74415290245376<94.745`.

## Thin-tail arm constants

If `||R||_F<1/8`, then

`s1||v_Q|| >31/64-1/8 =23/64`.

Since `||R||_op<1/64` and `||L||_op>ell0>19/32`,

`s1||v_K|| >19/32-1/64 =37/64`.

## Rank-two subtraction

`H=[[beta uu^T,s1uv^T],[s1vu^T,gamma vv^T]]` has range contained in
`span{(u,0),(0,v)}`, hence rank at most two.

The target gives `s3(A)>=1`. Since

`A-H=diag(B-beta uu^T,C-gamma vv^T)+[[0,R],[R^T,0]]`

and the second summand has operator norm `||R||_op<1/64`,

`max(||B-beta uu^T||op,||C-gamma vv^T||op)>1-1/64=63/64`.

For the realizing side `S,e`, writing

`D0=S-<e,Se>ee^T=[[0,w^T],[w,Cperp]]`,

we have `||D0||op<=||w||+||Cperp||op`, so one term is `>63/128`.

## Physical internal cross packet

`||D0||op<=2||S||op` implies `||S||op>63/128`.

The N3 physical diagonal cap gives `||diag(S)||op<1/64=2/128`, so

`||S-diag(S)||op>61/128` and therefore its Frobenius norm is also `>61/128`.

For a uniform independent two-colouring of the original coordinates of this bank,

`E ||S[U,V]||F^2 = (1/4)||S-diag(S)||F^2`
` > (1/4)(61/128)^2`
` =3721/65536`
` =0.0567779541015625`.

All displayed strict inequalities are consistent with the strict partner hypotheses.
