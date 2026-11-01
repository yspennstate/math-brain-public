# Addendum — fractional mixed-order Brascamp--Lieb closes all non-heavy P2 pair-volume states

This file strengthens the same run's `REPORT.md`. It does not alter that immutable file. Full QFORM remains **OPEN**.

## A. Fractional mixed-order theorem

Let `M` be an actual physical cross block between disjoint original-coordinate banks in the full ambient quadratic form. Let `Omega` be any probability law on nonzero square physical minors `(S,T)` of possibly varying orders. Write

`alpha_i=P_Omega(i in S)`, `beta_j=P_Omega(j in T)`,
`kbar=E_Omega |S|=sum_i alpha_i=sum_j beta_j`,

and

`K(Omega)=exp(E_Omega log det(M_ST)^2+H(Omega)).`                    (A.1)

Fix `rho in (0,1)`. Assume

`rho alpha_i <=1/2` for every physical row i,                       (A.2)

and

`rho kbar>2`.                                                        (A.3)

Then the full ambient quadratic form, with arbitrary same-side blocks, outside coordinates/couplings and induced affine terms retained, has a bounded continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= [2 rho kbar sqrt(e)/(rho kbar-2)]
    K_rho^(-1/(2 rho kbar))
    K(Omega)^(-1/(2 kbar)),
`                                                                        (A.4)

where

`K_rho=rho^(-rho)(1-rho)^(-(1-rho)).`                               (A.5)

This is `QFORM-FRACTIONAL-MIXED-VOLUME-BL-v1`.

### Proof

Start from the same source-valid original-coordinate decoupling integral used in the completed fleet01/B01 mixed-order theorem. In Lieb's Gaussian Brascamp--Lieb formula choose

`c_i=rho alpha_i`, `d_j=1-rho beta_j`.                               (A.6)

The scaling identity holds:

`sum_i c_i+sum_j d_j=rho kbar+|J|-rho kbar=|J|`.                    (A.7)

For positive Gaussian parameters `u_i,v_j`, set

`P0=prod_j(d_jv_j)`                                                  (A.8)

for the pure diagonal term in the positive Cauchy--Binet expansion. The sum of the expansion terms indexed by the support of `Omega` is, by weighted AM--GM,

`P1 >= K(Omega)
       prod_i(c_i u_i)^(alpha_i)
       prod_j(d_j v_j)^(1-beta_j).`                                  (A.9)

The complete determinant is at least `P0+P1`. The elementary weighted inequality

`x+y >= K_rho x^(1-rho)y^rho`                                       (A.10)

therefore gives

`det(D+M^T D_I M)
 >=K_rho K(Omega)^rho
   prod_i(c_i u_i)^(rho alpha_i)
   prod_j(d_jv_j)^((1-rho)+rho(1-beta_j))`
` =K_rho K(Omega)^rho
   prod_i(c_i u_i)^(c_i)
   prod_j(d_jv_j)^(d_j).`                                           (A.11)

Hence the Gaussian BL constant is at most

`[K_rho K(Omega)^rho]^(-1/2)
 prod_i c_i^(-c_i/2) prod_j d_j^(-d_j/2).`                          (A.12)

By (A.2), `1/c_i>=2`, so the same characteristic-function `L^p` lemma used in the completed B01 theorem applies and, after the `2t` scaling, gives

`||h_i^(1/c_i)||_1^(c_i)
 <=(2pi/|t|)^(c_i)c_i^(c_i/2).`                                    (A.13)

These factors cancel the row factors in (A.12). For the physical input densities on the receiver coordinates, `0<=g_j<=1` and `int g_j=1`, while

`prod_j d_j^(-d_j/2)
 <=exp[(1/2)sum_j rho beta_j]
 =exp(rho kbar/2).`                                                  (A.14)

Thus the decoupled characteristic function obeys

`|phi_Q(t)|
 <=min{1,
  [K_rho K(Omega)^rho]^(-1/4)
  exp(rho kbar/4)(2pi)^(rho kbar/2)|t|^(-rho kbar/2)}.`              (A.15)

Put `a=rho kbar/2>1`. Integrating `min(1,B|t|^-a)` exactly and applying Fourier inversion gives

`||p_Q||_infinity
 <=2 rho kbar sqrt(e)/(rho kbar-2)
   K_rho^(-1/(2rho kbar))K(Omega)^(-1/(2kbar)),`                    (A.16)

which is (A.4). The right side of (A.15) lies in `L^1`, so the density is continuous and vanishes at infinity. No random-coordinate rotation occurs. QED.

The case `rho=1` recovers the completed B01 mixed-order theorem. The gain for `rho<1` is that the physical row-occupancy gate expands from `alpha_i<=1/2` to `alpha_i<=1/(2rho)`, while the determinant-order exponent remains integrable precisely when `rho kbar>2`.

## B. Apply it to the completed fleet02/B20 P2 inequalities

Use the partner packet from the main report:

`Z>1/768`, `E2(D)>1/48`.                                             (B.1)

Let `w3` be the natural anchored third-minor law and `v2` the natural residual pair-volume law. Set

`lambda=1/32`,
`Omega=lambda w3+(1-lambda)v2`,
`rho=493/500`.                                                       (B.2)

Then

`kbar=3lambda+2(1-lambda)=65/32`,                                   (B.3)

and

`rho kbar=32045/16000=2.0028125>2`.                                 (B.4)

The fixed outer anchor row has `Omega`-marginal `1/32`, so it automatically satisfies (A.2). For a residual physical row `j`, with anchored-three marginal `a_j` and natural pair-volume marginal `q_j`,

`alpha_j=(a_j+31q_j)/32`.                                           (B.5)

The entropy-determinant currency is

`K(Omega)
 =lambda^(-lambda)(1-lambda)^(-(1-lambda)) Z^lambda E2^(1-lambda)`  (B.6)

and the actual partner lower bounds imply

`K(Omega)
 > [2^(1/32)(32/31)^(31/32)]/48
 =0.0219544898803... .`                                              (B.7)

Also

`K_rho=(493/500)^(-493/500)(7/500)^(-7/500)
      =1.07644431722... .`                                           (B.8)

Substitution into (A.4) yields the explicit universal payment

`boxed: ||p_Q||_infinity <5902`                                     (B.9)

whenever

`boxed:
 (493/500)(a_j+31q_j)/32 <=1/2
 for every residual physical row j.
`                                                                        (B.10)

The same statement applies after transposition.

In particular, because `a_j<=1`, if every natural residual pair-volume row marginal satisfies

`q_j<=49/100`,                                                       (B.11)

then

`alpha_j <=1/32+(31/32)(49/100)=1619/3200`,

and

`(493/500)alpha_j=798167/1600000<1/2`.                              (B.12)

Therefore **every P2 state with `max_j q_j<=0.49` is already paid by `<5902`**, regardless of the anchored-third-volume marginals. The identical column statement follows by transposition.

## C. Strong residual dichotomy: true >1/2 pair-wedge hub or doubly nested anchors

Assume the P2 state is still unpaid after applying (B.10) in both orientations. Then some residual row `j` violates (B.10), so

`a_j+31q_j>16/rho=8000/493`.                                        (C.1)

Likewise some residual column `p` violates the transposed condition.

If either selected pair-volume marginal exceeds `1/2`, we have the genuine physical heavy-wedge-hub exit

`boxed: q_j>1/2`                                                     (C.2)

or its column analogue.

Otherwise `q_j<=1/2`; then (C.1) gives the exact anchored-third marginal lower bound

`a_j>8000/493-31/2=717/986.`                                        (C.3)

The same bound holds for the failing column's anchored-third marginal. Under the **same anchored physical third-minor law** `w3`, the two events therefore satisfy

`P_w3(j selected and p selected)
 >2(717/986)-1
 =224/493.`                                                          (C.4)

Multiplying by the actual anchored mass `Z>1/768` gives

`boxed:
 sum_{k != j, q != p}
 det B[{i,j,k},{a,p,q}]^2
 > (224/493)(1/768)
 =7/11832.
}`                                                                      (C.5)

Thus the P2 branch of the newest completed fleet02/B20 packet is now reduced to the sharper exhaustive alternative:

1. **paid fractional mixed-volume state:** `||p_Q||_infinity<5902`, with a continuous density;
2. **true pair-wedge hub:** a physical residual row or column has natural `E2` marginal `>1/2`;
3. **doubly nested physical anchor packet:** fixed residual row and column anchors carry common anchored-third-minor mass `>7/11832`.

This strictly strengthens the `5/12` hub / `1/1536` nested alternative in the main report. In particular, the high-dimensional spike/dust family cannot remain in an amorphous low-`E3` class: either its residual pair-volume is diffuse enough for the fractional mixed Fourier payment, or more than half of the pair-wedge currency is captured by one physical row/column, or the original anchored third-volume localizes simultaneously on a second physical row and column with a dimension-free mass floor.

## D. First remaining implication

The earliest P2 debt is now

`QFORM-P2-TRUE-HUB-OR-DOUBLE-NESTED-PAYMENT-v2`:

- pay a physical natural-pair-volume row/column hub of marginal `>1/2`; or
- pay the doubly nested anchored `3x3` minor packet (C.5),

while retaining arbitrary same-side quadratic blocks and all ambient couplings.

The partner's zero-edge doubly-transverse and double-star packets remain separate debts. No claim is made that the full target is solved.