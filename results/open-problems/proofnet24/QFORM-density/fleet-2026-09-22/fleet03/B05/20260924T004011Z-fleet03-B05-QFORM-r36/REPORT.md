SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-24T00:40:11Z.
attacking: QFORM-DOUBLEZERO-ONE-THIRD-PRODUCT-SMOOTHING-v1 — replace the small-pivot/fresh-square loss at the exact raw double-zero scalar pair by a product one-third kernel matched to the rank-one Schur small-ball exponent, without conditioning the dependent first-bank residual.

# fleet03/B05 r36 — exact raw double-zero ratio packet via one-third product smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea / equivalent interval bound preserving arbitrary product densities  
Owner control at prepublication refresh: revision `2026-09-22.15`, QFORM only  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING PRODUCT-PRESERVING DENSITY THEOREM / EXACT RAW DOUBLE-ZERO PACKET CLOSED / FULL QFORM OPEN**  
Continuity: **not proved by the new theorem**; the conclusion below is absolute continuity plus an essential `L^infinity` bound.

## 1. What this run changes

The preceding B05 line had two endpoint mechanisms that did not meet uniformly:

1. r27 pays every quantitatively nonzero raw scalar diagonal in the ratio packet,
   
   `||p_Q||_infinity <= 128 sqrt(2) (delta_B mu m)^(-1/4)`,
   
   where `delta_B=max(|a|,|d|)`, but this deteriorates as `delta_B->0`;
2. r35 pays scalar-source concentration by exact rank-three crossings, but its pivot currencies can vanish when both scalar source projections become nearly literal.

The exact raw double-zero matrix

`B=[[0,c],[c,0]]`, `c!=0`,

is therefore an important algebraic endpoint. The pair-log theorem covers it but pays a factor which still deteriorates as `c->0` if one uses the generic logarithmic/square-root small-ball splice.

This run uses a different exponent. A product of two independent capped variables has a universal **one-third singular density envelope**. The ratio packet leaves a rank-one Schur remainder with a square-root small-ball estimate. Square-root small-ball implies a finite one-third Riesz potential. At exponent `1/3`, the powers of `c` cancel exactly against

`mu=c^2 |lambda|`.

That cancellation gives a `c`-free density estimate while the full dependent residual coordinate of the first product-projection bank remains inside the same unconditional expectation.

## 2. Sources actually consumed

### 2.1 Ratio packet and predecessor

The active ratio packet comes from

`yspennstate/math-open-problems@b0299facc04ea0c03276dddb1a12c027aed5a946`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B05/20260923T033640Z-fleet01-B05-QFORM-r26/REPORT.md`.

One original-coordinate product bank gives an orthonormal two-dimensional projection

`V=(S,R)=Gamma^T X`, `Gamma^T Gamma=I_2`,

and two disjoint original-coordinate banks give normalized scalar projections `Y,Z`, independent of the first bank and one another, with density caps

`L_Y,L_Z <= sqrt(2)`.

The packet homogeneous matrix is

`H=[[C,P],[P^T,B]]`, `P=(p q)`,

with exact Schur identity

`C-P B^(-1) P^T = lambda m e1 e1^T`,
`mu=|det B| |lambda|`,                                           (2.1)

and the standard packet can be chosen with `m>=3/20`.

The immediate predecessor is

`yspennstate/math-open-problems@3b26570e5ee8a21471acba644e9b20483cbb2118`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T234035Z-fleet03-B05-QFORM-r35/REPORT.md`.

### 2.2 Rank-one affine small-ball theorem

Source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For independent cap-one original coordinates `W`, a unit vector `u`, nonzero `Lambda`, arbitrary affine vector `b` and scalar `d`, it proves

`sup_t P(|Lambda (u dot W)^2+b dot W+d-t|<rho)`
` <= min(1,10 sqrt(rho/|Lambda|)).`                              (2.2)

Crucially the affine vector need not be parallel to `u`.

### 2.3 Product rearrangement input

The product-density source used below is recorded in

`yspennstate/math-open-problems@103fe9295f04e9fae87c2ef9a88ba46a3b1e7fcc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260922T124333Z-fleet01-B04-QFORM-r11/REPORT.md`.

For independent cap-one `U,V`, it gives, for `s!=0`,

`p_(UV)(s) <= 4 log(1+1/(2 sqrt(|s|))).`                         (2.3)

This is a density rearrangement statement, not a pointwise oscillatory-decay statement.

### 2.4 Designated partner fleet04/B05

Canonical source:

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B05/20260923T041255Z-fleet04-B05-dominant-slope-r2/REPORT.md`.

If `m_*` is the largest exact physical-slope mass in the first bank, it proves

`||p_Q||_infinity < 51.6 (mu m_*)^(-1/3).`                       (2.4)

Section 7 applies this to an actual complementary inequality.

## 3. Product one-third kernel

### Lemma 3.1 — `QFORM-PRODUCT-ONE-THIRD-KERNEL-v1`

Let `U,V` be independent real random variables with density caps `L_U,L_V`. Let `kappa!=0` and let `a,b` be arbitrary deterministic shifts. Then `kappa(U+a)(V+b)` has a density satisfying, almost everywhere,

`boxed:
 p_[kappa(U+a)(V+b)](w)
 <= 2^(4/3) (L_U L_V)^(2/3)
    |kappa|^(-2/3) |w|^(-1/3).
`                                                                    (3.1)

#### Proof

First take `L_U=L_V=1`, no shifts, and `kappa=1`. By (2.3),

`p_(UV)(s) <=4 log(1+1/(2 sqrt(|s|))).`

For every `x>=0`,

`log(1+x) <= x^(2/3).`                                             (3.2)

Indeed, for `h(x)=x^(2/3)-log(1+x)`,

`h'(x)=2/(3x^(1/3))-1/(1+x)`.

Putting `y=x^(1/3)`, the numerator has the sign of

`2(1+y^3)-3y=2y^3-3y+2`,

whose minimum over `y>=0` is `2-sqrt(2)>0`. Hence `h` increases from zero. Therefore

`p_(UV)(s) <= 2^(4/3)|s|^(-1/3).`                                (3.3)

Separate translations preserve density caps and independence. Scaling the output by `kappa` gives the factor `|kappa|^(-2/3)`. Finally scale `U` by `L_U` and `V` by `L_V`; the two normalized variables have cap one and the coefficient becomes `kappa/(L_U L_V)`. This yields (3.1). QED.

The exponent `1/3` is intentionally weaker than the local logarithmic singularity. Its advantage is exact scale matching with the rank-one Schur remainder below.

## 4. Square-root small-ball implies a one-third Riesz bound

### Lemma 4.1 — `QFORM-SQRT-SMALLBALL-TO-ONE-THIRD-RIESZ-v1`

If a real random variable `T` satisfies

`P(|T-t|<rho) <= min(1,H sqrt(rho))`                              (4.1)

for every `t` and `rho>0`, then

`boxed:
 sup_t E |T-t|^(-1/3) <= 3 H^(2/3).
`                                                                    (4.2)

#### Proof

Layer cake gives

`E |T-t|^(-1/3)
 =(1/3) integral_0^infinity rho^(-4/3)
       P(|T-t|<rho) d rho.`                                       (4.3)

Split at `rho_0=H^(-2)`. On `(0,rho_0)` use `H sqrt(rho)`, and on `(rho_0,infinity)` use one. The two pieces are respectively

`2 H^(2/3)` and `H^(2/3)`.

This proves (4.2). QED.

## 5. Environment version: dependent shifts are harmless

Let `E` be independent of `U,V`. Permit arbitrary measurable shifts `a(E),b(E)` and an arbitrary real `T(E)`. Suppose (4.1) holds for `T(E)`. Conditional on `E`, Lemma 3.1 gives a density for

`Q=T(E)+kappa(U+a(E))(V+b(E))`

bounded at `t` by

`2^(4/3)(L_U L_V)^(2/3)|kappa|^(-2/3)
 |t-T(E)|^(-1/3).`

Averaging and applying Lemma 4.1 proves

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3)(L_U L_V)^(2/3)
    |kappa|^(-2/3) H^(2/3).
`                                                                    (5.1)

No independence between the random shifts and `T(E)` is required. What matters is genuine independence of the two original scalar banks from the environment before conditioning.

This is precisely the product-preserving feature needed in the ratio packet: the dependent first-bank residual may enter both scalar shifts and the Schur remainder.

## 6. Main theorem: exact raw double-zero ratio packet

### Theorem 6.1 — `QFORM-RATIOPACKET-DOUBLEZERO-ONE-THIRD-v1`

Assume the ratio-packet hypotheses (2.1), including arbitrary affine terms generated by conditioning all outside original coordinates. Suppose the raw scalar-pair block is exactly

`B=[[0,c],[c,0]]`, `c!=0`.                                       (6.1)

Then the full packet law has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_DZ (mu m)^(-1/3),
 C_DZ = 3*2^(4/3)*10^(2/3)
      = 35.0882128585... <35.089.
`                                                                    (6.2)

The bound is independent of `c`, of the ratio residual size, and of the condition number of the scalar pair.

#### Proof

After all outside coordinates are fixed, write the affine packet as

`Q=V^T C V+2Y p^T V+2Z q^T V+2cYZ
   +ell_V^T V+ell_Y Y+ell_Z Z+gamma`,                             (6.3)

where `V=(S,R)` is the genuine two-dimensional product projection of the first bank. Set

`alpha(V)=(q^T V+ell_Z/2)/c`,
`beta(V) =(p^T V+ell_Y/2)/c`.                                    (6.4)

Then the scalar pair completes exactly as a product in the two **original independent scalar banks**:

`Q=2c [Y+alpha(V)][Z+beta(V)] + T(V),`                            (6.5)

where

`T(V)=V^T C V+ell_V^T V+gamma-2c alpha(V) beta(V).`               (6.6)

The quadratic matrix of `T` is

`C-(p q^T+q p^T)/c
 = C-P B^(-1)P^T
 = lambda m e1e1^T.`                                              (6.7)

Thus, when rewritten on the original independent coordinates of the first bank,

`T=lambda m S^2+b^T V+gamma'`

is exactly a rank-one quadratic plus an arbitrary affine form. By (2.2),

`P(|T-t|<rho)
 <=min(1,H sqrt(rho)),
 H=10/sqrt(|lambda|m).`                                           (6.8)

Now apply the environment estimate (5.1) with

`kappa=2c`, `L_U=L_Y`, `L_V=L_Z`.

Since `L_Y,L_Z<=sqrt(2)`,

`(L_Y L_Z)^(2/3) <=2^(2/3).`                                     (6.9)

Therefore

`||p_Q||_infinity
 <=3*2^(4/3)*2^(2/3)*(2|c|)^(-2/3)
      *10^(2/3)(|lambda|m)^(-1/3)`
` =3*2^(4/3)*10^(2/3)
      [c^2 |lambda| m]^(-1/3).`                                  (6.10)

But `det B=-c^2`, so by definition

`c^2 |lambda|=mu.`                                                (6.11)

Equations (6.10)-(6.11) prove (6.2). No conditional density of `S|R` is ever used. QED.

For the standard ratio packet `m>=3/20`, (6.2) becomes

`boxed:
 ||p_Q||_infinity
 <66.039 mu^(-1/3).
`                                                                    (6.12)

In particular, when `mu>=1`, the exact raw double-zero packet is bounded by `<66.039` for every admissible product input law.

### Regularity

The proof constructs a density by conditional product pushforward and Tonelli. It proves absolute continuity and the essential bound (6.2). It does **not** establish continuity, so full-target continuity remains open.

## 7. Designated partner applied to an actual complementary inequality

The newest completed `fleet04/B05` theorem (2.4) remains the correct exit when one literal first-bank coordinate carries substantial exact Schur-direction mass. In the ratio packet, if

`q_xi=max_i xi_i^2 >=1/4`,

then `u_i^2=m xi_i^2>=m/4` for some literal original coordinate, hence

`m_*>=m/4`.

Substitution into (2.4) gives the actual full-line inequality

`boxed:
 ||p_Q||_infinity
 <51.6 [4/(mu m)]^(1/3).
`                                                                    (7.1)

With the standard `m>=3/20`,

`boxed:
 ||p_Q||_infinity <154.161 mu^(-1/3).
`                                                                    (7.2)

This partner branch applies for arbitrary raw scalar diagonals. Combining it with Theorem 6.1 means the remaining near-double-zero stability problem may assume `q_xi<1/4`: the exact endpoint `a=d=0` is now paid regardless of `q_xi`, while any heavy exact-slope carrier is already paid before one studies a punctured perturbation.

## 8. Relation to r27 and the precise missing factor

r27 proves, for

`delta_B=max(|a|,|d|)>0`,

`||p_Q||_infinity
 <=128 sqrt(2) (delta_B mu m)^(-1/4).`                            (8.1)

The new theorem proves the **exact endpoint**

`delta_B=0 => ||p_Q||_infinity
 <=35.089 (mu m)^(-1/3).`                                        (8.2)

Thus the raw-double-zero singularity in (8.1) is a proof-interface singularity, not bad behavior of the exact endpoint. The scale-invariant parameter is

`epsilon = delta_B/(mu m)^(1/3).`                                (8.3)

After normalizing `mu m=1`, r27 controls every quantitative `epsilon>0`, while (8.2) controls `epsilon=0`. What is genuinely missing is a **uniform punctured stability theorem** as `epsilon downarrow0`.

The exact next obligation is therefore

`QFORM-NEAR-DOUBLEZERO-ONE-THIRD-STABILITY-v1`:

> extend the one-third product-kernel receiver to
> `B=[[a,c],[c,d]]` with `a,d` nonzero but small on the determinant scale, while preserving the original `Y,Z` product coordinates. The terms `aY^2+dZ^2` cannot be discarded as small random errors because no support or moment bounds are available. A valid proof must either absorb those self-quadratics inside a product-sensitive fractional kernel or route them to a second aggregate currency before taking a reciprocal.

Together with the designated partner, this hard punctured branch may additionally assume `q_xi<1/4`. The r35 scalar-source crossing currencies remain available whenever one scalar bank has enough source tail; they are complementary to, not replaced by, the new raw-pair mechanism.

## 9. Integrity / scope

- Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity remains **OPEN**.
- No Gaussian, log-concave, moment, bounded-support, connected-support, or diagonal-basis assumption is introduced.
- No independence is asserted after rotating the two-dimensional first-bank projection.
- No conditional density cap for `S|R` is used.
- No arbitrary-joint coarea theorem is used.
- No pointwise quadratic-phase decay is used.
- No small coefficient is treated as a small random error.
- The one-third exponent is paid by an integrated density/fractional-potential argument on genuine original product banks.
- Finite numerical checks are diagnostic only; the theorem above is proved analytically.
