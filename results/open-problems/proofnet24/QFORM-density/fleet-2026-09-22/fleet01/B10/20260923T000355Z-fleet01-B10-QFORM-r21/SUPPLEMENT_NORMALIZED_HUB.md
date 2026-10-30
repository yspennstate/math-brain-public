# Supplement: deterministic re-whitening of the designated partner's isolatable hub

This supplement makes explicit one normalization step used in `REPORT.md`.

In fleet02/B10 `20260922T225540Z-fleet02-B10-QFORM-auto11`, before isolating the hub the normalized frame has rows `v_i` with `sum_i v_i v_i^T=I_3`, a hub `v=v_h` of leverage `L_0=||v||^2>511/512`, a fixed-hub packet

`T_h^0=sum_(j in B2,k in B3)det(v,v_j,v_k)^2>1/512`,

and active sub-Gram after conditioning `B1\{h}`

`K=vv^T+sum_(j in B2)v_jv_j^T+sum_(k in B3)v_kv_k^T`.

The partner proves `0<K<=I_3`, `det K>=T_h^0>=1/512`, and for `N_h=K^(1/2) N K^(1/2)`,

`|det N_h|, sigma_min(N_h) >=2^-18`.

Now re-whiten only the deterministic active coefficient geometry by setting

`r_i=K^(-1/2)v_i`.

Then

`sum_(i active)r_i r_i^T=I_3`.

The same physical active matrix is represented as

`A_active=R N_h R^T`,

so no random coordinate rotation and no new independence assertion is involved.

The new hub leverage is

`L=v^T K^(-1)v`.

Because `K<=I_3`, `K^(-1)>=I_3`, hence

`L>=L_0>511/512`.

Because the re-whitened rows form a Parseval frame, also `L<=1`.

Every active triple determinant transforms by

`det(r_i,r_j,r_k)^2 = det(K)^(-1) det(v_i,v_j,v_k)^2`.

Therefore the re-whitened fixed-hub packet is

`T_h=det(K)^(-1)T_h^0 >=T_h^0>1/512`,

since `det K<=1`.

Thus the normalized state used in the report really has simultaneously

`sum r_i r_i^T=I_3`,
`L>511/512`,
`T_h>1/512`,
`|det N_h|,sigma_min(N_h)>=2^-18`.

This verifies the provenance of the constants entering the bordered-volume inequality

`sum_(j,k)|det A_{hjk}|=|det N_h|T_h>2^-27`.
