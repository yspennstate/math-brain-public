# fleet02/B06 early mathematical checkpoint

Run `b06-20260923T083202Z-7358ab1fe71c`. Full QFORM remains open.

## Weighted max-reciprocal receiver

Let `X,Y` be independent real variables with densities at most one, jointly independent of a background `Omega`. Let `U=U(Omega), V=V(Omega), R=R(Omega)`. Assume `(U,V)` has a joint density bounded by `K<infinity`. Then

`T = 2 X U + 2 Y V + R`

has an essentially bounded density and

`||p_T||_infinity <= 2 sqrt(K)`.

Indeed, condition on `Omega`. For `(u,v) != (0,0)`, convolution/Young gives the conditional density cap

`||p_(2uX+2vY)||_infinity <= 1/[2 max(|u|,|v|)]`.

The joint density assumption makes `(U,V)=(0,0)` null. Hence

`||p_T||_infinity <= (1/2) E 1/max(|U|,|V|)`.

By layer cake and the square sublevel set of the max norm,

`E 1/max(|U|,|V|)
 <= int_0^infinity min(1,4K/s^2) ds
 = 4 sqrt(K)`.

Thus the claimed bound follows. This retains the actual two-dimensional coefficient weight and never takes a singular fiber supremum.

If `U=a.Z+u0`, `V=b.Z+v0` are two non-collinear affine forms of independent cap-one coordinates and `Delta=sqrt(||a||^2||b||^2-(a.b)^2)`, the previously completed product-fiber Brascamp--Lieb projection theorem gives `||p_(U,V)||_infinity <= e/Delta`, so

`||p_T||_infinity <= 2 sqrt(e/Delta)`.

## Near-collinear spectral budget

For a double-null physical pair write

`A = [[0,0,a^T],[0,0,b^T],[a,b,C]]`, `b=lambda a+epsilon`, `epsilon perp a`.

Let `H` be the symmetric star obtained by setting `b=lambda a` and `C=0`. Its rank is at most two. Since the target hypothesis gives the third singular value `s_3(A)>=1`, Eckart--Young yields

`1 <= s_3(A) <= ||A-H||op <= ||epsilon|| + ||C||op`.

Therefore

`||epsilon|| + ||C||op >= 1`.

In particular, if `||epsilon||<=1/2`, the background block has an eigenvalue of modulus at least `1/2`; if `||epsilon||>=1/2`, the residual transverse star itself has operator norm at least `1/2`. This is the first deterministic third-direction currency in the near-collinear branch, but converting arbitrary `C` into a product-preserving curved payment remains unpaid.
