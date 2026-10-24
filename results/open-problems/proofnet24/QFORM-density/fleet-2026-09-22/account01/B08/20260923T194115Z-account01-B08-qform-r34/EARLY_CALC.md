# Early calculation — heavy three-frame row forces literal physical currency

Run `20260923T194115Z-account01-B08-qform-r34`.

Let `C` be a real symmetric child block with an actual unit eigenvector `r`, `Cr=lambda r`, `|lambda|>=cL`. Let `B` be the literal cross block, let `U` be its top-two left singular frame, and assume `s2(B)>=beta L`. Put

`d=dist(r,range U)>0`, `q=(I-UU^T)r/d`, `W=[q,U]`.

For every physical row `i`, write `u_i=||U^T e_i||`, `h_i=q_i^2+u_i^2`, and `m_i=max(|r_i|,u_i)`. Since `r=Ua+dq` with `||a||<=1`,

`|q_i| <= (|r_i|+u_i)/d <= 2m_i/d`,

hence

`h_i <= m_i^2(1+4/d^2)` and therefore

`m_i >= [d/sqrt(d^2+4)] sqrt(h_i)`.

If `u_i=m_i`, then by the exact SVD identity

`||B^T e_i||^2=sum_j s_j(B)^2 |<e_i,u_j>|^2 >= s2(B)^2 u_i^2`,

so

`||B^T e_i|| >= beta L [d/sqrt(d^2+4)] sqrt(h_i)`.

If `|r_i|=m_i`, then Cauchy applied to the eigen-equation gives

`||e_i^T C|| >= |(Cr)_i| = |lambda r_i| >= cL [d/sqrt(d^2+4)] sqrt(h_i)`.

Consequently either the child diagonal or the child off-diagonal row star is at least `1/sqrt(2)` times that amount.

At the partner-r28 transverse gate `d>=1/2`, a row with `h_i>1/48` therefore forces either

`||B^T e_i|| > beta L/sqrt(816)`

or

`max(|C_ii|,||C_{i,-i}||_2) > c L/sqrt(1632)`.

With the stronger r30 physical cross scale `beta=3/sqrt(40)` and `c=sqrt(3/20)`, these are respectively

`0.0166052791038768 L` and `0.00958706236059213 L`.

This is a deterministic coefficient statement. It uses no moments, no support regularity, no random-variable rotation, no probabilistic perturbation, and no pointwise oscillatory estimate.
