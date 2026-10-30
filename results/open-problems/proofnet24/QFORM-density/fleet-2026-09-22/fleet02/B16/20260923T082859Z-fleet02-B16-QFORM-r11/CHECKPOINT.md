# fleet02/B16 substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T082859Z-fleet02-B16-QFORM-r11
Status: supporting lemma; full target open.

## First unpaid implication

Designated partner fleet03/B16 r26 reduces its exact-rank-three analysis to a genuine near-coloop chamber `c>63/64`. The still-unpaid B16 implication is a product-preserving transition through the overlapping weak-leakage/transverse bank. The present calculation closes a semi-aligned source-separated-square subclass; it does not close the generic near-coloop chamber or arbitrary higher rank.

## New calculation

Let `(H,U)` be an arbitrary possibly dependent pair. Let `X,V` be independent of one another and independent of `(H,U)`. Assume density caps

`||p_X||_inf <= L_X`, `||p_U||_inf <= L_U`, `||p_V||_inf <= L_V`.

For nonzero `beta,gamma`, set

`Q = 2 U (gamma X + H) + beta V^2`.

Then

`||p_Q||_inf <= 4 L_V sqrt(L_X L_U) / sqrt(|beta gamma|)`.

Proof skeleton: after reflection take beta>0. The square `beta V^2` has density at most `L_V/(sqrt(beta y)) 1_{y>0}`. Conditional on `(H,U)=(h,u)`, the remaining half-Riesz kernel is integrated against the *original independent scalar* X. The cap-L_X bathtub bound gives

`int f_X(x) (r-2 gamma u x)_+^{-1/2} dx <= sqrt(2 L_X/(|gamma u|))`.

No conditioning or independence is imposed on H and U. Finally the cap-L_U bathtub bound gives

`E |U|^{-1/2} <= 2 sqrt(2 L_U)`.

Multiplying yields the displayed constant. This retains the source scalar until the curved kernel is paid and therefore avoids the conditional-projection-cap failure.

## Target-class application

For even m and c in (0,1), put a=1-c and balanced signs eps_j. With arbitrary independent cap-one inputs define

`T=m^{-1/2} sum X_j`, `U=m^{-1/2} sum eps_j X_j`, `V=m^{-1/2} sum Z_j`,

`Q=2( sqrt(c) X_0 + sqrt(a) T ) U + V^2`.

The physical frame rows are `r_0=(sqrt(c),0,0)`, `r_j=(sqrt(a)/sqrt(m),eps_j/sqrt(m),0)`, `r_{m+j}=(0,0,1/sqrt(m))`, and spectral matrix `Lambda=[[0,1,0],[1,0,0],[0,0,1]]`. Thus `R^T R=I_3` and the nonzero spectrum is exactly `{1,-1,1}`. Ball-Rogozin gives `||p_U||_inf,||p_V||_inf <= sqrt(2)` while T and U may remain dependent. Hence

`||p_Q||_inf <= 2^(11/4) c^(-1/4)`.

For the partner residual `c>63/64`, this is `<6.754`.

The pinned completed ruled-hyperboloid theorem (Theorem C in `COUNTEREXAMPLE_SEARCH.md` at commit e5f71d79eff325201dd0274053d20268ce65b837) also gives the sharper one-sheet estimate `p_Q(s)<=pi sqrt(2)` for `s>=0`, because the spectral signature is `(1,1,-1)`. This use is source-valid: its line integrals are two-dimensional marginals of the original product law, not an independence assertion about spectral coordinates.

Remaining gap: in the generic near-coloop frame the smoothing square V need not live on a source bank disjoint from the same-bank leakage/transverse pair. The next transducer must preserve that overlap or extract a bounded number of source-separated receivers.
