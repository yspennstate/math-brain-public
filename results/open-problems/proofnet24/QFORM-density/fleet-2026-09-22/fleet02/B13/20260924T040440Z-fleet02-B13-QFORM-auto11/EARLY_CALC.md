SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-24T04:04:40.602812Z.
attacking: center-free two-strip diagonal-bank receiver: force a product-preserving payment from distributed diagonal curvature, otherwise isolate the exact remaining rough strip obstruction and apply pinned D5 to the general crossing.

# Early calculation — hard-rank-two physical pivot shrinks quadratically

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T040440Z-fleet02-B13-QFORM-auto11`  
Status: supporting theorem; full QFORM remains OPEN and continuity remains separate.

Fresh compatible designated-partner input is fleet03/B13 r42, canonical report commit `8118c1b30c07d8775ad0e93f0c9581f24a3cb700`. In its hard diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`,

there is an ORIGINAL physical pivot `k` with

`|d_k|>=1`,

and

`|det Lambda| > H0 rho^(-2)`,

where

`H0=sqrt(1536 e^2)=16 sqrt(6) e=106.534455308869...`.

The partner also proves the ten-center/two-line structural alternatives, but the calculation below uses only the displayed hard-branch inequalities and the diffuse leverage bound.

The required pinned Fourier source is `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. Its Theorem F plus the half-potential/square-peel Corollary 4.4(i) says: if an ORIGINAL physical scalar pivot `a=A_kk` is nonzero and its Schur complement has the exact form

`S=D'+W N W^T`, `W^T W=I_2`,

with every row leverage `||w_i||^2<=1/2`, then

`||p_(X^T A X)||_inf <= 8 sqrt(2) |a|^(-1/2) |det N|^(-1/4)`.

Arbitrary diagonal twists and affine terms are retained. No product-coordinate rotation is used.

## Theorem — `QFORM-HARD-R2-PHYSICAL-PIVOT-QUADRATIC-SHRINK-v1`

In the hard branch above, every slab witness

`rho=P{X^T A X in J}/|J|`

satisfies

`boxed: |A_kk| <= (256 sqrt(6)/e) rho^(-2) < 230.686 rho^(-2).`

If `A_kk !=0`, the normalized rank-two Schur coefficient matrix additionally satisfies

`boxed: |det N| > e^2/24.`

### Proof

Put

`u=u_k`, `c=||u||^2<=1/3`, `d=d_k`, `a=A_kk=d+u^T Lambda u`.

If `a=0`, the first assertion is immediate. Assume `a!=0`. Since `|d|>=1`, also `d!=0`. The exact scalar Schur remainder is

`S=D_-+U_- M U_-^T`,

`M=Lambda-a^(-1) Lambda u u^T Lambda`.

Let

`G=U_-^T U_-=I_2-u u^T`,
`W=U_- G^(-1/2)`,
`N=G^(1/2) M G^(1/2)`.

Then `W^T W=I_2`. For every remaining physical row,

`||w_i||^2 = u_i^T G^(-1) u_i
            <= ||u_i||^2/(1-c)
            <= (1/3)/(2/3)=1/2`.

The determinant transport is exact:

`det N=(1-c)d det(Lambda)/a`.

Apply the pinned square-peel/Fresnel rank-two theorem to this actual physical pivot:

`rho <= 8 sqrt(2) |a|^(-1/2)|det N|^(-1/4)`

`     = 8 sqrt(2) [(1-c)|a d det Lambda|]^(-1/4)`.

Raising to the fourth power gives

`|a| <= 16384 / ((1-c)|d det Lambda| rho^4)`.

Use `1-c>=2/3`, `|d|>=1`, and `|det Lambda|>H0 rho^-2`:

`|a| < 24576/H0 * rho^-2`

`     = (256 sqrt(6)/e) rho^-2`

`     = 230.685930938945... rho^-2`.

Finally, for `a!=0`,

`|det N|=(1-c)|d det Lambda|/|a|`

` > [(2/3)H0]/[256 sqrt(6)/e]`

` = e^2/24`.

This proves the theorem.

## Corollary — a genuine physical star survives

The same pivot has order-one ORIGINAL-coordinate cross energy. Put

`q=u^T Lambda u=a-d`,
`r=A[-k,k]=U_- Lambda u`.

Then

`||r||_2^2 = u^T Lambda(I-u u^T)Lambda u
            =u^T Lambda^2 u-q^2`.

Cauchy gives `q^2<=c u^T Lambda^2 u`, hence

`||r||_2^2 >= (1/c-1)q^2 >=2q^2`.

Therefore

`boxed:
 sum_(i!=k) A_ik^2
 >=2(1-(256 sqrt(6)/e)rho^-2)_+^2.}`

So the hard high-density survivor is not merely a near-null physical diagonal: its low-rank term must cancel the physical diagonal to accuracy `O(rho^-2)` while leaving an order-one physical star coupling to the remaining coordinates.

This is a real narrowing of the partner r42 endpoint and an equation-level use of the required pinned Fourier package. It does not finish the rough-law receiver: a near-null hub with distributed star mass can still evade a single robust physical pair, and no coefficient-small quadratic remainder may be discarded under arbitrary fragmented/unbounded product laws.
