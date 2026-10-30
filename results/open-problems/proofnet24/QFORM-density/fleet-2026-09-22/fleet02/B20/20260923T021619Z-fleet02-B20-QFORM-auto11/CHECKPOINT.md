# Early substantive checkpoint — fleet02/B20 QFORM

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T021619Z-fleet02-B20-QFORM-auto11
Status: substantive calculation in progress; full target open.

The newest completed designated partner fleet03/B20 r22 reduces its robust exact-rank-three `2+1` O3 chamber to disjoint original-coordinate banks `H_a` and `G`. Its exact identities give

- `L_a=[sqrt(lambda_a)v_a,W]`, `W W^T=S_G`,
- `L_a L_a^T=I-lambda_b v_bv_b^T`,
- `delta:=det(L_a)^2=1-lambda_b>1/6`,
- `D:=|det M|>=1`,
- `a_a=lambda_a v_a^T M v_a`, and `lambda_a |a_a| D<1/4096`.

Aggregate the rank-one companion physically:

`Z=lambda_a^(-1/2) sum_(i in H_a) c_i X_i`, where `u_i=c_i v_a` and `sum c_i^2=lambda_a`.

Then `Z` is independent of the entire original-coordinate bank `G`, and its density cap is at most `sqrt(e)` by the one-dimensional product-projection bound. Factor the rank-two `G` frame as `R_G=V W^T`, `V^T V=I_2`, and put `Y=V^T X_G`. The required newest Claude source supplies the source-valid two-dimensional product-projection cap `||p_Y||_infty<=2`; no independence between the two coordinates of `Y` is asserted.

Conditioning on `H_b` and all outside original coordinates leaves arbitrary affine terms only. In variables `(Z,Y)`, the active matrix is

`H=L_a^T M L_a`.

Hence

`D_H:=|det H|=delta D`,
`s_min(H)>=delta`,
`H_00=a_a`.

The near-null partner inequality and `lambda_a>1/6` imply

`|H_00|<3/2048`,
`|H_00|/delta<9/1024`.

For the scalar/pair splitting of `H`, let `P=|b^T adj(C)b|` be the cross-transverse resource from the completed projection-product theorem. Since `s_min(H)>=delta`, the receiver block satisfies `|det C|<=D_H/delta` whenever invertible; the singular case gives `P=D_H`. Thus in all cases

`P>=D_H-|H_00||det C|>(1-9/1024)D_H=(1015/1024)D_H`.

The cross-transverse theorem rescales to a scalar density cap `M_1` and pair density cap `M_2` as

`||p_Q||_infty <= C_CT (M_1 M_2)^(2/3) (D_H P)^(-1/6)`,
`C_CT=103680^(1/3)`.

Using `M_1<=sqrt(e)`, `M_2<=2`, `D_H>1/6`, and the displayed lower bound on `P` gives

`||p_Q||_infty < C_CT * 2^(2/3) e^(1/3) * (1024/1015)^(1/6) * 6^(1/3) <190`.

This appears to pay the entire partner r22 robust `2+1` O3 chamber before the physical-star subcase is needed. The remaining task is to write the complete proof with the scalar-cap rescaling and scope checks, refresh live corrections, and identify the first global N3 packet still unpaid.
