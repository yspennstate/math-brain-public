# Exact-target certification addendum

This addendum strengthens the Section 7 witness in `REPORT.md` so that membership in the exact target class is certified by an exact inequality rather than by the displayed floating singular-value check.

Keep the same 5-by-3 Vandermonde matrix

`V_(t,:)=(1,t,t^2)`, `t=0,1,2,3,4`,

but set

`M=10 V`

instead of `M=2V`, and embed it as

`A=[[0,M],[M^T,0]]`.

The determinant-weighted row law is unchanged by this scalar rescaling. Thus

`h=31/35>3/4`, `delta_2=0`, `delta_3=9396/214375`, and `E5(M)=0`.

The target spectral hypothesis now has an elementary exact certificate. Since

`E3(V)=700=(s1(V)s2(V)s3(V))^2`

and

`||V||_F^2=sum_(t=0)^4 (1+t^2+t^4)=389`,

AM--GM gives

`s1(V)s2(V) <= (s1(V)^2+s2(V)^2)/2 <=389/2`.

Therefore

`s3(M)=10s3(V)
 >=10 sqrt(700)/(389/2)
 =20sqrt(700)/389 >1`,

where the final inequality is exact because `280000>389^2=151321`.

The nonzero eigenvalues of the symmetric block matrix `A` are `+/-s_j(M)`, so `A` has at least three (indeed six) eigenvalues of absolute value at least one.

Now

`Z=E3(M)=10^6*700=700000000`.

The three-sample theorem therefore gives, for every independent product input with coordinate densities at most one,

`||p_(X^T A X)||inf
 <=(9sqrt(3)e/2) (delta_3 Z)^(-1/6)
 <1.198`.

Thus the strict-extension example is fully source-valid without relying on numerical eigenvalue certification: D' fails (`h>3/4`), D5 fails (`rank M=3`), the completed partner two-sample compiler fails (`delta_2=0`), while the new three-sample integrated-Fourier compiler succeeds (`delta_3>0`).
