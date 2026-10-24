# Exact checks for `QFORM-R39-LIGHT-DIAGSPIKE-PAID-OR-NULLHUB-RANK2-COLLAR-v1`

These are finite arithmetic/algebra checks only; the proof is in `REPORT.md`.

1. Partner-to-carrier diagonal:

`3/4-1/8-1/32 = (24-4-1)/32 =19/32`.

2. Light carrier leverage:

If `P_jj=||z||^2<=1/16`, then `||z||<=1/4`; hence
`|K_jj|=|z^T Lambda z|<=||z||||Lambda z||<=||Ke_j||/4`.
Thus `||K[j,j^c]||^2=||Ke_j||^2-|K_jj|^2>15|K_jj|^2`.

3. Strong hub constant:

`h_0=(19 sqrt(15)-1)/32=2.2683338618106537...`.
Moreover `19 sqrt(15)>73` because `19^2*15=5415>5329=73^2`; therefore `h_0>72/32=9/4`.

4. Indefinite pair:

Under `|A_jj|,|A_kk|<1/8` and `|A_jk|>=1/4`,
`det B<1/64-1/16=-3/64`, so `|det B|>3/64`.
Weyl against `[[0,b],[b,0]]` gives `sigma_min(B)>1/8`.
The B09 bound is

`12.181*(3/64)^(-3/7)*(1/8)^(-1/14)=52.45488808854...<52.455`.

5. Diffuse hub atom:

If every `|w_k|<1/4` and `||w||>9/4`, then
`max w_k^2/||w||^2 < (1/16)/(81/16)=1/81`.

6. Five-bank split:

`1/6+1/81=(27+2)/162=29/162` and
`1-4*(29/162)=46/162=23/81>1/6`.
Thus every bank has hub norm `>9/(4 sqrt(6))=0.9185586535...`.

7. Third-resource cut:

The physical star matrix `[[A_jj,w^T],[w,0]]` has rank at most two. Hence `s_3(A)>=1` implies `||A[j^c,j^c]||_op>=1`. If every actual diagonal is `<1/8`, its zero-diagonal part has operator norm `>7/8`, and a random half-cut has expected squared cross Frobenius equal to one quarter of the zero-diagonal squared Frobenius. Therefore some cut has cross Frobenius `>7/16`.

8. E3 currency:

With `S>9/(4 sqrt(2))`, `S^2>81/32`. At `zeta=2^-20`,
`Z_3>(81/32)2^-20`.
The marginal-free E3 bound is

`C_3*[(81/32)2^-20]^(-1/6)=91.0898992435...<91.1`,
where `C_3=3*2^(4/3)*e^(1/3)=10.5501688312...`.

9. Rank-two collar:

If `F=||C_perp||_F>=1/8` and the squared singular values are `y_r`, then `F^2=sum y_r`. If the best-rank-one squared tail `T=sum_{r>=2}y_r` were at least `F^2/2`, then
`e_2>=(F^4)/4>=(1/8)^4/4=2^-14>2^-20`, contradiction.
Hence `y_1>F^2/2` and
`2^-20>e_2>=y_1 T>(F^2/2)T`, so
`T<2*2^-20/F^2<=2^-13`.
Therefore the Frobenius best-rank-one error is `<2^(-13/2)=0.01104854346...`.

10. Scalar-pivot control:

`C_* sqrt(8)=3.9354796432...*10^9`, with `C_*=1+44*(10^-15)^(-1/2)`.
