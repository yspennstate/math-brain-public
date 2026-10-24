SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T11:00:08Z.
attacking: the r52 bounded-heavy captured packet — replace the contaminated bordered-minor compiler by a joint top-two principal/boundary row-carrier cut, retaining the full operator tails and aggregate volume.

# Early checkpoint — joint rank-four row carrier

Full QFORM remains OPEN. All coordinates below are original physical coordinates; no post-rotation independence, moments, support, log-concavity, or single-good-minor inference is used.

Latest completed designated partner consumed: account03/B07 r52, `math-open-problems@4f5ee2dc112f258cb5dad4c9be03a9ae3573be6b`, which gives a bounded physical packet `K`, `|K|<=895`, and, on the captured branch, `a_K=lambda_min(U_K^T U_K)>=1/4`; unless already paid, `s_3(B)<1/64` for `B=A[K,K]`. Its physical boundary is `D=A[K,K^c]`.

## First unpaid implication attacked

`QFORM-R52-CAPTURED-JOINT-R4-CARRIER-HEAVYROW-RECEIVER-v1`.

The partner's mixed `1+2` and `2+1` determinant packets cannot safely be sent through one bordered Schur pivot: an earlier exact target family shows the Schur correction can cancel an order-one `E_2` bank completely. Instead, truncate both `B` and `D` to their top two modes and balance the common physical row carrier before any pivot/minor selection.

Let `eps=1/64`. If `s_3(D)>=eps`, the completed marginal-free physical-`E_3` receiver already pays the full ambient law by

`||p_Q||_infinity <= C3/eps = 64 C3 = 675.2108051945456...`,

`C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`.

Hence consider `s_3(D)<eps`. Let `B_2` be the best rank-two spectral truncation of the symmetric matrix `B`, and `D_2` the best rank-two SVD truncation of `D`. Put

`C_0=B_2^2+D_2D_2^T`.

Because `A^2[K,K]=B^2+DD^T>=U_KU_K^T`, while the discarded squared tails are PSD with operator norms below `eps^2`, Weyl gives

`lambda_3(C_0) >= 1/4-2 eps^2 = 511/2048 =: gamma`.

Thus the joint row carrier `range(C_0)` has rank `r_0` equal to 3 or 4. Let `R` be an orthonormal `|K| x r_0` frame for that range and `delta=max_h ||R_{h,*}||_2^2`.

If `delta<=1/(4r_0)`, the B07 balanced-cut lemma gives a physical partition `K=I disjoint_union J` with

`R_I^T R_I, R_J^T R_J >= g I`,
`g=(1-sqrt(r_0 delta))/2 >=1/4`.

Put all of `K^c` on the `J` side and define the rank-at-most-four base crossing

`M_0=[ B_2[I,J] , D_2[I,:] ]`.

Since `range(B_2)` is a subspace of `range(C_0)`, the same lower Gram bound on `J` implies

`B_2[I,J]B_2[I,J]^T >= g (B_2^2)[I,I]`.

The `D_2` block is not cut on its column side, so

`M_0M_0^T >= g C_0[I,I]`.

Also `C_0=R Theta R^T` with `Theta>0` on the carrier and `R_I^TR_I>=gI`, hence

`lambda_3(C_0[I,I])>=g lambda_3(C_0)>=g gamma`.

Therefore

`s_3(M_0)>=g sqrt(gamma)>= (1/4)sqrt(511/2048)`.

The actual physical crossing is

`M=A[I,J union K^c]=M_0+E`.

Its two discarded pieces are horizontally concatenated, so

`||E||_op <= sqrt( ||(B-B_2)[I,J]||_op^2 + ||(D-D_2)[I,:]||_op^2 ) < sqrt(2)/64`.

Thus

`boxed: s_3(M) >= mu_0 := (1/4)sqrt(511/2048)-sqrt(2)/64
                     =0.1027807831124968... .`

The completed physical-`E_3` receiver then gives the full ambient continuous density bound

`boxed: ||p_Q||_infinity <= C3/mu_0
                              =102.64728981114382... .`

No same-bank curvature, outside coupling, or nonzero tail has been deleted. No individual determinant is selected.

Consequently the entire captured r52 packet is now paid unless the rank-3/4 joint row carrier is physically heavy:

`delta>1/(4r_0)>=1/16`.

This is a strictly sharper residual than the partner's two separate bordered-compilation debts. The surviving new structural debt is a heavy physical row of the common principal-plus-boundary top-two carrier (plus the partner's separate spectral-escape branch `a_K<1/4`, T-side three-curvature branch, and earlier same-bank-star branch).

## Mandatory pinned e5 result applied to a real live obstruction

From `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, the proved `D_k` + fractional-potential argument with `q=2` gives, for any physical crossing with `Z_2=e_2(MM^T)>0`,

`H_(1/4)(Q):=sup_s E|Q-s|^(-1/4) <= 3.929132 Z_2^(-1/16)`

with no two-volume marginal gate and with arbitrary same-side curvature/affine terms retained.

On the partner's live mixed `1 principal + 2 boundary` branch, `Z_2(D)>=1/64`, so the actual physical boundary cut obeys

`boxed: H_(1/4)(Q) <= 3.929132 * 64^(1/16)
                         =5.09545379304503... .`

This is useful fractional currency but is deliberately NOT promoted to a density bound or pushed through a single pair peel: the exact earlier B07 cancellation family has order-one edge-times-`E_2` input while the pair Schur correction annihilates one rank-one component and leaves `E_2=0`. The new joint-carrier construction above avoids that invalid transfer completely.
