# Deterministic checks — rank-two rough-curvature receiver

Run `20260923T224543Z-fleet02-B04-QFORM-auto11`.

## 1. Rank-two zero-diagonal classification

Let `E=E^T`, `diag(E)=0`, `rank(E)=2`, `E!=0`. Since `tr E=0`, its two nonzero eigenvalues are `lambda,-lambda`, `lambda>0`. Write

`E=lambda(rr^T-ss^T)`, `||r||=||s||=1`, `r perp s`.

The diagonal identities give `r_i^2=s_i^2`. On active coordinates write `s_i=epsilon_i r_i`, `epsilon_i in {+1,-1}`. Orthogonality gives

`sum_{epsilon_i=+1} r_i^2=sum_{epsilon_i=-1}r_i^2=1/2`.

With `P={epsilon=+1}`, `Q={epsilon=-1}`, `a=sqrt(2) r_P`, `c=sqrt(2) r_Q`, one has `||a||=||c||=1` and

`E_PP=E_QQ=0`, `E_PQ=lambda a c^T`.

Thus `||E||op=lambda` and the only nonzero curvature is a rank-one crossing between two physical coordinate subbanks.

## 2. Exterior-product lower bound

In the fleet03/B04 r41 zero-anchor factorization, assume the residual `E_ZZ` has rank two and use the partition above. Put curved bank `X=(Y_N,Y_Q)` and clean bank `Y=(X_h,Y_P)`. Its physical crossing matrix is

`M=[[b,E_NP],[0,lambda c a^T]]`.

For the orthonormal coefficient-domain vectors `e_h` and `(0,a)`,

`M e_h=(b,0)`,
`M(0,a)=(E_NP a,lambda c)`.

Hence their image-area squared is

`||b||^2 lambda^2 + ||b||^2 ||E_NP a||^2 - <b,E_NP a>^2 >= ||b||^2 lambda^2`.

Because `s1(M)s2(M)=||wedge^2 M||op`, this proves

`s1(M)s2(M)>=||b|| lambda`.

Combining with the already proved clean-bank top-two rearrangement theorem gives

`||p||inf <=2 sqrt(pi) (||b|| lambda)^(-1/2)`.

## 3. Stress family

For `m>=2`, take original-coordinate groups

`N={n1,n2}`, `P={p1,...,pm}`, `Q={q1,...,qm}`, `R={r1,r2}`, `S={s1,s2}`, plus an anchor `h`.

Set

`b=(sqrt(2),sqrt(2))`,
`u=v=m^(-1/2) 1_m`,
`a=c=2^(-1/2)(1,1)`.

On the natural physical cut

`I=N union Q union R`, `J={h} union P union S`,

define the crossing

`M_epsilon=diag_block(b, 2 v u^T, epsilon a c^T)`.

The singular values are exactly `2,2,epsilon`; therefore the symmetric bipartite matrix

`A_epsilon=[[0,M_epsilon],[M_epsilon^T,0]]`

has nonzero spectrum

`{2,2,epsilon,-epsilon,-2,-2}`

and `2m+1` zero eigenvalues. Thus it has four eigenvalues of modulus two for every `epsilon>0`.

The first two components form the r41 core: relative to `h`, the strong `P-Q` residual curvature is zero-diagonal rank two with operator norm two, while `||b||=2`. The new receiver gives the core density bound `sqrt(pi)`. The weak `R-S` component is independent of the core, so convolution preserves this bound for the full output.

## 4. Exact third-volume optimization on the same physical cut

Every nonzero physical `3x3` minor selects one row from each of `N,Q,R` and one column from each of `{h},P,S`. There are

`2*m*2 * 1*m*2 = 8 m^2`

supported minors. Each has squared determinant

`(sqrt(2) * (2/m) * (epsilon/2))^2 = 2 epsilon^2/m^2`.

Therefore

`Z=E3(M_epsilon)=16 epsilon^2`.

The canonical squared-minor law is uniform. Its constrained-side row marginals are

- `1/2` on each row of `N`,
- `1/m` on each row of `Q`,
- `1/2` on each row of `R`.

For any supported probability weight `w`, because all supported determinant squares equal the same `a0=2 epsilon^2/m^2`,

`G(w)=a0 exp(H(w)) <= a0*(8m^2)=16 epsilon^2`,

with equality only for the uniform law. Also every supported minor contains exactly one `N` row, so the two `N` marginals sum to one; no row-marginal threshold below `1/2` is feasible. The same holds for the two `R` rows. Consequently the uniform law at `h=1/2` is the exact global optimum over every supported weight and every proved D/D' threshold.

The pinned e5 Theorem D therefore gives exactly

`B_e5=6 sqrt(e) 2^(-2/3) epsilon^(-1/3)=6.231775903093545... epsilon^(-1/3)`.

The latest fleet03/B04 r42 marginal-free E3 theorem gives

`B_r42=C_* 2^(-2/3) epsilon^(-1/3)=5.325069688625554... epsilon^(-1/3)`,

where `C_*=8.453021225528176...`; using its matrix-specific diffuse branch at the known threshold `h=1/2` sharpens this to

`3e 2^(-2/3) epsilon^(-1/3)=5.137230742833414... epsilon^(-1/3)`.

Its incident-row receiver, with `J_i=Z/2=8 epsilon^2` for any `N` or `R` row, gives

`3*2^(5/6) epsilon^(-1/3)=5.345392308842036... epsilon^(-1/3)`.

## 5. Direct-ridge comparison on the same physical cut

Let `g=gamma^2`,

`k=4/(4+g)`, `h_e=epsilon^2/(epsilon^2+g)`.

Then `theta=2k+h_e`. Physical ridge leverages are `k/2` on `N`, `k/m` on `Q`, and `h_e/2` on `R`, so the completed `q=1` leverage gate is automatically satisfied for every `gamma>0`.

Whenever the trace gate `theta>2` holds,

`theta-2=h_e-2(1-k)<=h_e`,

and the completed simplified ridge certificate

`R=sqrt(e)/(sqrt(2)gamma) * theta/(theta-2)`

obeys

`R >= sqrt(2e)/(gamma h_e)
   = sqrt(2e)(epsilon^2+gamma^2)/(gamma epsilon^2)
   >= 2 sqrt(2e) epsilon^(-1)`.

Thus every certificate in this completed q=1 simplified ridge family costs at least

`4.663287963194248... epsilon^(-1)`.

Choosing `gamma=sqrt(3/2) epsilon` yields

`R=(2 sqrt(3e)+o(1)) epsilon^(-1)
  =5.711338016744285... epsilon^(-1)(1+o(1))`.

At `epsilon=10^(-6)`, the grouped rough-curvature receiver remains `sqrt(pi)=1.772453850905516...`, while the r42 diffuse E3 certificate is about `513.7231`, pinned e5 is about `623.1776`, and the q=1 ridge certificate is at least `4.6633*10^6`.
