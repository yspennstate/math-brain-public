# Deterministic checks

Run `20260923T190214Z-account02-B20-QFORM-auto11`.

## Exact block-minor check

For invertible `2 x 2` `A`, arbitrary `2 x 2` `B,C,D`, and

`T=[[A,C],[D,B]]`,

fix bottom row `q` and right-block column `j`.  The minor using both top rows, bottom row `q`, both left columns, and right column `j` is

`det [[A,c_j],[d_q^T,B_qj]]
 = det(A)(B_qj-d_q^T A^{-1}c_j)`.

Thus with `S=B-D A^{-1}C`, the sum of the four squared selected minors is exactly

`det(A)^2 ||S||_F^2`.

Since `e_3(TT^T)` is the sum of squares of all `3 x 3` minors, the selected-minor lower bound used in the report is exact.

## Compression check

For orthogonal row/column compressions `T=P^T M Q`, exterior powers give

`wedge^3 T=(wedge^3 P^T)(wedge^3 M)(wedge^3 Q)`.

The outer factors are contractions, so

`||wedge^3 T||_HS <= ||wedge^3 M||_HS`.

Therefore `e_3(TT^T)<=e_3(MM^T)`.

## Constants

Partner diffuse constant:

`a_D=0.002408434254376076`.

Hence

`delta_0=a_D^2=5.800555557652045e-6`.

The Schur-volume gate `||S||_F>=delta_0` gives

`Z_3>a_D^4 delta_0^2=a_D^8=1.1320832461591675e-21`.

With `C_3=10.5501688311648`,

`C_3 Z_3^(-1/6)=C_3 a_D^(-4/3)=32679.82200032744<32679.823`.

The pinned D5 gate at `Z_5>=1/1024` gives

`5 sqrt(2e) (1024)^(1/10)=10 sqrt(2e)=23.316439815971243<23.317`.

Finally `delta_0<a_D`, so if `s_2(B)>a_D` and `||B-R||_op<delta_0`, then `R` cannot have rank at most one by Eckart--Young.  Applied to `R=D A^{-1}C`, this proves invertibility of both `C` and `D` in the unpaid `2 x 2` collar.
