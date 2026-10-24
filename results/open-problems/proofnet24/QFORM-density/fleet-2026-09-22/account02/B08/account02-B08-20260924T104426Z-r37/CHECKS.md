# account02/B08 r37 deterministic checks

Marker: `QFORM_B08_R37_CHECK_PASS`.

These are exact arithmetic/algebra regression checks for the report; they are not benchmarks, simulations, or evidence beyond the displayed identities.

## Constants

Let

`a = sqrt(31)/24`,
`s = sqrt(9/20)`,
`eps0 = 0.005848650958799406`,
`c = a*s-eps0`,
`m0 = sqrt(47/48)`,
`d = 6.328856436640812e-6`.

Direct evaluation gives

- `a = 0.23199018178458422`,
- `s = 0.6708203932499369`,
- `c = 0.14977509401605973`,
- `16*c^2 = 0.35892126060031254`,
- `(m0*c)/sqrt(2)-1/4096 = 0.10455383978519894`,
- `d/4 = 1.582214109160203e-6`,
- `d/sqrt(8) = 2.2375886517524236e-6`.

Thus the eight-bank mismatch lower bound and thirteen-cross-block constant in the report are numerically consistent.

## Eight-bank greedy packet

Normalize atom masses by `a_i=|q_i|^2/||delta||^2`. From `max_i ||V_i||^2<=1/16`, every `a_i<=1/16`, and `sum_i a_i=1`.

For a greedy bank stopped at the first time its mass reaches `1/16`, the previous partial mass is `<1/16` and the final atom is `<=1/16`; hence every completed bank has mass in `[1/16,1/8)`. After seven banks the used mass is `<7/8`, so unused mass is `>1/8`, enough to complete an eighth bank. Taking square roots yields

`||delta||/4 <= ||q_B|| < ||delta||/sqrt(8)`.

## Sixteen-bank exact-frame packet

For every inherited bank `J_r`,

`||b_Jr|| > a ||z|| >= a*s ||b||`,
`||b-Pb|| < eps0 ||b||`.

Therefore

`|| (Pb)_Jr || > (a*s-eps0)||b|| = c||b||`.

Since `||Pb||<=||b||`, the normalized exact-frame vector `u=Pb/||Pb||` satisfies `||u_Jr||>c` on all sixteen banks.

## Thirteen literal cross blocks

For disjoint banks `J_r`, with `G_r=V_Jr^T V_Jr`,

`sum_r tr(G_r)<=tr(V^T V)=2`.

If four banks had trace `>1/2`, the sum would exceed `2`; hence at least thirteen satisfy `tr(G_r)<=1/2`, thus `G_r<=I/2` and `V_Jr^c^T V_Jr^c>=I/2`.

For such a bank, `w=u_Jr/||u_Jr||` gives `||V^T w||>=||u_Jr||>c`, so the rank-two spectral part has complement norm at least `m0*c*L/sqrt(2)`. Subtracting the exact spectral tail `||E||op<L/4096` yields the checked constant `0.10455383978519894 L`.

## Walsh stress family

For

`A_eps = [[0,(sqrt(2)L u)^T],[sqrt(2)L u, L uu^T+L vv^T+eps L ww^T]]`

with orthonormal Walsh `u,v,w`, restriction to `(e0,u,v,w)` is

`L[[0,sqrt(2),0,0],[sqrt(2),1,0,0],[0,0,1,0],[0,0,0,eps]]`.

The `2x2` hub/u block has characteristic polynomial `lambda^2-lambda-2=(lambda-2)(lambda+1)`, so the nonzero eigenvalues are exactly `{2L,-L,L,eps L}`.

For `m>=32768`, hub-light least singular value is bounded by the off-diagonal magnitude

`sqrt(2)L/sqrt(m) <= L/128 < L/64`.

Any light-light `2x2` block has every entry bounded by `(2+eps)L/m`, hence operator norm at most `2(2+eps)L/m < L/64` for `eps<1/4096`.

On a half of the flat star, `||b_T||=||b||/sqrt(2)`. Partitioning that half into sixteen equal banks gives `||b_Jr||/||b_T||=1/4`, and `1/4 > sqrt(31)/24`.

## Pinned-source Theorem F payment

For the light rank-three frame `(u,v,w)`, `G_I=I_3`, row leverage is `3/m<=1/2`, and coefficient product is `eps L^3`. Theorem F therefore gives

`||p||_infinity <= 12(eps L^3)^(-1/3)=12 eps^(-1/3)/L`.

At `eps=2^-16`, this equals

`12*2^(16/3)/L = 483.8096831596312/L`.

All displayed checks are consistent. `QFORM_B08_R37_CHECK_PASS`.
