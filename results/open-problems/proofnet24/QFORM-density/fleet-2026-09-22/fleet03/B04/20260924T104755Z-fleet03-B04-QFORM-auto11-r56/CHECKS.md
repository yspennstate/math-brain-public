# Deterministic verification notes

Marker: `QFORM_B04_R56_ZEROPIVOT_RANKR_CHECK_PASS`.

No Monte Carlo evidence was used.

## Rank-two zero-pivot stress matrix

For residual indices `i=1,...,6`, use `a_i=i^2`, `v_i=1`, `w_i=i`, and `R=2I+vv^T+ww^T`. Then the augmented row vectors are `z_i=(i^2,1,i)`.

For every triple `P={i,j,k}`, exact integer elimination gives

`det(z_i,z_j,z_k)^2 = [(j-i)(k-i)(k-j)]^2`.

For every ordered pair of disjoint triples `(P,Q)` (necessarily complementary for six residual indices), exact determinant evaluation verifies

`det A[{h} union P,{h} union Q]^2 = c_P c_Q`.

The ordered disjoint packet sums to

`J_2=331904`.

The theorem constant is `4 sqrt(2)=5.656854249492381...`, hence

`4 sqrt(2) * 331904^(-1/8)=1.154644864670688...`.

The residual off-diagonal rank-one tetrad test fails exactly:

`(1+1*2)(1+3*4)=39`, while `(1+1*3)(1+2*4)=36`.

Thus the residual cannot be made diagonal plus rank one by changing only its diagonal.

## Designated fleet04/B04 r2 partner block

For

`M=[[5,3,3,4],[3,5,5,3],[1,2,4,5],[1,2,1,4],[5,4,5,5],[3,4,1,2]]`,

exact `4x4` determinant enumeration gives

`E_4=165775`, `H_2=137045`, `rho_2=27409/33155`.

The largest anchored conditional row marginal is

`beta_*=90786/137045<2/3`,

so `q=181572/137045`. The carrier row has squared norm `68`. The partner entropy theorem therefore gives

`[3e/((3-2q)sqrt(q))] (137045/68)^(-1/6)=5.692467732262831...`.

Finally, the leading principal minors of `M^T M-I_4` are

`69, 681, 8451, 107715`,

all positive. Sylvester therefore certifies that every singular value of `M` exceeds one, so the pure-cross symmetric matrix `[[0,M],[M^T,0]]` is strictly inside the owner spectral target.
