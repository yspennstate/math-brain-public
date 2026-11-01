# fleet03/B03 r26 — logarithmic near-alignment weighted-time compiler

Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN / CONTINUITY NOT CLAIMED / WITHOUT_VERIFIED_BRAIN**.

Target remains the universal bounded-density conjecture for `Q=X^T A X` under independent cap-one physical coordinates and at least three eigenvalues of absolute value at least one. Nothing below rotates the independent coordinates or treats `X_i+X_i'` and `X_i-X_i'` as independent.

## Source inputs actually used

1. `QFORM-ARBITRARY-HUB-SQRT-SMALLBALL-v1`, fleet03/B19, canonical `yspennstate/math-open-problems@80403bc0adff2c5e8278848674c81448e9782e44`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T030233Z-fleet03-B19-QFORM-r23/`. For one original physical row with aggregate star norm `S>0`, its residual law obeys

   `sup_z P(|R-z|<=eps) <= H1 eps^(1/2)`, `H1=4*2^(1/4) S^(-1/2)`.

2. `QFORM-TWO-PHYSICAL-GRADIENT-2OVER3-SMALLBALL-v1`, fleet03/B19, canonical `yspennstate/math-open-problems@2c88af5e0ac6a4faf8d923a621c7d7006d544ffe`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T034239Z-fleet03-B19-QFORM-r24/`. For two original physical coordinates and a rank-two original-product cross matrix `M`, with `Delta=sqrt(det(M M^T))>0`, the same residual law obeys

   `sup_z P(|R-z|<=eps) <= H2 eps^(2/3)`, `H2=12(2 Delta)^(-1/3)`.

3. The designated fleet04/B03 handoff is `yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`. Its advertised weighted-L2 compiler is not used because the fleet has already identified the missing time-weight/homogeneity step. Only the elementary valid lemma

   `P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`

   is consumed below.

## 1. General two-exponent layer-cake lemma

Let `R` be any real random variable. Suppose for all `z` and all `eps>0`,

`P(|R-z|<=eps) <= min(1, H1 eps^(1/2), H2 eps^(2/3))`,

where `H1,H2>0`. Then

**Lemma.**

`sup_z E |R-z|^(-1/2) <= H1 [ 4 + 3 log_+( H2 / H1^(4/3) ) ]`.

Equivalently,

`sup_z E |R-z|^(-1/2) <= H1 [ 4 + log_+( H2^3/H1^4 ) ]`.

### Proof

Fix `z` and put `T=|R-z|`. The positive small-ball exponents imply `P(T=0)=0`. Layer cake gives

`E T^(-1/2) = (1/2) int_0^infty r^(-3/2) P(T<=r) dr`.

First suppose `H2 >= H1^(4/3)`. Set

`r0=(H1/H2)^6`, `r1=H1^(-2)`.

Then `r0<=r1`; at `r0` the two power bounds agree, while at `r1` the square-root bound reaches one. Therefore

`E T^(-1/2)`
`<= (H2/2) int_0^r0 r^(-5/6) dr`
` + (H1/2) int_r0^r1 r^(-1) dr`
` + (1/2) int_r1^infty r^(-3/2) dr`
`= 3 H2 r0^(1/6) + (H1/2) log(r1/r0) + r1^(-1/2)`
`= 4 H1 + 3 H1 log(H2/H1^(4/3))`.

If `H2 < H1^(4/3)`, use the `2/3` bound alone until it reaches one. The standard one-exponent calculation gives

`E T^(-1/2) <= 4 H2^(3/4) < 4 H1`,

which is exactly the displayed formula with `log_+=0`. This proves the lemma.

The key point is that the `eps^(2/3)` estimate is used only at the smallest scales, where it kills the logarithmic divergence of the critical `eps^(1/2)` estimate. Consequently the cost of a nearly rank-one second gradient is logarithmic rather than a negative power.

## 2. Physical two-gradient packet

Let `X=(X1,X2)` be two independent original cap-one coordinates, let `Y` be a disjoint bank of original independent cap-one coordinates, and let

`R = X^T B X + X^T(2 M Y + beta) + S0(Y)`,

where `B` is an arbitrary real symmetric `2x2` matrix, `beta` is arbitrary, `S0` is arbitrary measurable, and `M` has rank two. Write its rows as `m1^T,m2^T` and put

`Delta = sqrt(det(M M^T)) > 0`.

For the first physical coordinate, the full aggregate original-coordinate star into the residual variables `(X2,Y)` is

`s1 = (B12, m1)`, `S1=||s1||_2 = sqrt(B12^2+||m1||_2^2)`.

Similarly `S2=sqrt(B12^2+||m2||_2^2)`. Since `rank M=2`, both are positive. Choose either row `j`; below write `S=Sj`.

The arbitrary-hub theorem applies after conditioning on neither a conjugate sum nor a rotated coordinate: the other physical coordinate is simply part of the independent residual product bank. Hence

`H1 = 4*2^(1/4) S^(-1/2) = 2^(9/4) S^(-1/2)`.

The two-gradient theorem applies to the same `R` with

`H2 = 12 (2 Delta)^(-1/3)`.

A useful cancellation is exact:

`H1^(4/3) = 8 S^(-2/3)`,

so

`(H2/H1^(4/3))^3 = 27 S^2/(16 Delta)`.

Combining with the lemma proves the new theorem:

### `QFORM-STAR-AREA-LOG-HALF-RIESZ-v1`

For every real `t`,

`boxed{
 sup_t E |R-t|^(-1/2)
 <= 2^(9/4) S^(-1/2)
    [4 + log_+(27 S^2/(16 Delta))].
}`

One may minimize the right-hand side over `S=S1,S2` if desired.

This is scale-correct: `S` has one matrix-coefficient unit, `Delta` has two, so `S^2/Delta` is dimensionless and the overall potential scales as coefficient^(-1/2).

Compared with the pure two-gradient receiver

`sup_t E|R-t|^(-1/2) <= 2^(13/4) 3^(3/4) Delta^(-1/4)`

from the `eps^(2/3)` bound alone, the new estimate improves the near-alignment deterioration from `Delta^(-1/4)` to only

`S^(-1/2) log(S^2/Delta)`

when `Delta/S^2 -> 0`.

## 3. Assigned independent-copy weighted-time estimate

Let `R'` be an independent copy of the *whole* random variable `R`. No attempt is made to split any coordinate-pair sum from its difference. Since for `0<alpha<1`,

`int_R |u|^(alpha-1) e^{iux} du = 2 Gamma(alpha) cos(pi alpha/2) |x|^(-alpha)`

in the standard Riesz sense, Tonelli/regularization gives at `alpha=1/2`

`int_R |u|^(-1/2) |phi_R(u)|^2 du`
`= sqrt(2 pi) E |R-R'|^(-1/2)`.

Conditioning on `R'` and applying the translation-uniform estimate above yields

`boxed{
 int_R |u|^(-1/2) |phi_R(u)|^2 du
 <= 2^(11/4) sqrt(pi) S^(-1/2)
    [4 + log_+(27 S^2/(16 Delta))].
}`

Numerically the outside coefficient `2^(11/4)sqrt(pi)` is

`11.92360071543272...`.

This is the requested dependence-safe decoupled-time estimate. The `|phi|^2` identity is used only for the whole independent copy, so all dependence between `Xi-Xi'` and `Xi+Xi'` remains intact.

## 4. Linear small-ball scaling after one genuine original square

Let `Z` be an additional original cap-one coordinate independent of `(X,Y)`, and let `h=h(X,Y)` be arbitrary. For `d!=0`, define

`Q = d [Z+h(X,Y)]^2 + R`.

Conditionally on `(X,Y)`, the pushforward of `Z` under `d(Z+h)^2` has density bounded by

`|d|^(-1/2) |u|^(-1/2)`

at displacement `u` from the conditional shift (the two inverse branches each contribute at most the reciprocal derivative). Therefore

`boxed{
 ||p_Q||_infinity
 <= 2^(9/4) |d|^(-1/2) S^(-1/2)
    [4 + log_+(27 S^2/(16 Delta))].
}`

Thus for every interval `I`,

`P(Q in I) <= 2^(9/4) |d|^(-1/2) S^(-1/2)
 [4 + log_+(27 S^2/(16 Delta))] |I|`.

This proves an essentially bounded density in this packet. **Continuity is not claimed.**

The theorem is particularly useful in a nearly rank-one two-gradient packet: the previous direct receiver paid `Delta^(-1/4)`, whereas this square-pivot compiler pays only a logarithm in the aspect ratio `S^2/Delta`.

## 5. Designated partner applied to an actual new inequality

For the density above, normalization implies

`||p_Q||_2^2 <= ||p_Q||_infinity`.

Apply the valid fleet04/B03 collision lemma to an independent copy `Q'`:

`P(|Q-Q'|<=eps) <= 2 eps ||p_Q||_2^2`.

Hence the actual partner-consumed inequality is

`boxed{
 P(|Q-Q'|<=eps)
 <= 2^(13/4) |d|^(-1/2) S^(-1/2)
    [4 + log_+(27 S^2/(16 Delta))] eps.
}`

The outside coefficient `2^(13/4)` is `9.513656920021768...`.

No part of the fleet04/B03 weighted-L2 compiler is used.

## 6. Strict-N3 control family and comparison

Consider the original-coordinate block matrix corresponding to

`Q_delta = Z^2 + 2 X1 Y1 + 2 delta X2 Y2`, `0<delta<=1`,

with all five inputs independent and density-capped by one. Its symmetric matrix is

`[1] direct_sum [[0,M],[M^T,0]]`, `M=diag(1,delta)`,

so its nonzero eigenvalues are

`1, +1, -1, +delta, -delta`.

It therefore satisfies the exact target hypothesis for every `delta`: at least three eigenvalues have absolute value at least one. Here `d=1`, `S=1`, and `Delta=delta`. The new theorem gives

`||p_(Q_delta)||_infinity <= 2^(9/4)[4+log_+(27/(16 delta))]`.

This is not a universal bound as `delta->0`; it is a mechanism comparison. The earlier pure two-gradient square receiver costs `O(delta^(-1/4))`, while the hybrid estimate costs only `O(log(1/delta))`. The exact `delta=0` endpoint is a separate rank-one packet and cannot be reached by silently deleting the small `delta` term on unbounded input laws.

## 7. What is and is not solved

**Solved in this run:** the critical square-root star estimate and the supercritical two-gradient estimate can be glued before taking the half-Riesz/time norm. This converts the near-rank-one power loss into a logarithmic loss while preserving physical-coordinate product provenance and exact sum/difference dependence.

**Still open:** the bare three-large-eigenvalue hypothesis does not yet force a uniformly bounded aspect ratio or a separate product-preserving endpoint mechanism whose constant is stable as `Delta/S^2 ->0`. Thus the unrestricted QFORM conjecture remains OPEN. Global continuity remains OPEN; the present square-pivot conclusion is only `L^infinity`/linear-small-ball.

A natural next implication is a quantitative `second-gradient OR stable rank-one endpoint` compiler: if the two-row area is tiny, aggregate the almost-collinear packet with the already-paid exact-coloop/rank-one geometry without perturbatively deleting the transverse term.
