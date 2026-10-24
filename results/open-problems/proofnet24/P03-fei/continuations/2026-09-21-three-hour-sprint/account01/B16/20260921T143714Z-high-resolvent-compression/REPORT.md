# B16 FEI signed resolvent — exact spectral compression and a one-third entropy absorption

**Date:** 21 September 2026  
**Scope:** `account01 / B16`, full FEI creative proof search  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Route:** APPROACH 10/13, signed resolvent / noise-transport payment  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Novelty / publication priority:** unverified; no priority claim.

## 0. What moved

The preceding B16 run put the q-flip first-hit covariance into the same resolvent symbol `z/(1+z)` in its spatial and radial variables. The remaining compiler still carries the inherited R16 signed high-resolvent bank

\[
\Delta_{d,>2}=\sum_{r\ge2}\frac{(-1)^r D_{d,r}}{(r-1)2^{r-1}},
\qquad D_{d,r}=C_{0,r}-C_{d,r},
\]

with odd collision orders retained as refunds. At the half-band the old terminal-moment saturation theorem says that this differs from the full initial response by at most `2^{3-2^d}J`.

This run observes that the **full** alternating R16 response has an elementary closed form in the spectral probabilities. That closed form gives two new dimension-free payments:

1. the whole full high-resolvent response is at most `2 ln(3/2) J = 0.8109302162... J` in natural entropy units, leaving a uniform positive amount of the inherited R16 bank unspent;
2. more structurally, the response is at most **one third of the Fourier entropy itself**. Consequently the exact compiler identity can absorb this entire channel into the left-hand side, reducing FEI to a payment for the small-resolvent plus terminal channel with a factor `3/2`.

No collision order is positive-parted and no odd-order refund is discarded.

---

## 1. Entering exact R16 state

Write

\[
p_S=\widehat f(S)^2,
\qquad \sum_Sp_S=1,
\]

and use natural logarithms. The inherited R16 collision reservoir is

\[
C_{0,r}=1-\sum_Sp_S^r,
\qquad r\ge2,
\]

with the folded budget

\[
0\le C_{0,r}\le rJ(f).
\]

The full initial high-resolvent response is

\[
\Delta_{\infty,>2}
:=\sum_{r=2}^{\infty}
\frac{(-1)^rC_{0,r}}{(r-1)2^{r-1}}.
\tag{1.1}
\]

For a completed degree-`d` prefix the carried terminal-moment saturation theorem gives

\[
\boxed{
|\Delta_{\infty,>2}-\Delta_{d,>2}|
\le \varepsilon_dJ,
\qquad
\varepsilon_d:=2^{3-2^d}.
}
\tag{1.2}
\]

At the usual half-band `d=d_h=ceil(n/2)` this error is doubly exponentially small in `d_h`.

The exact compiler synthesis is

\[
H_{\rm nat}(f)
=\kappa_2J-\mathcal B_d+\mathcal Q_{d,<2}+R_d,
\qquad
\mathcal B_d=\kappa_2J-\Delta_{d,>2},
\tag{1.3}
\]

where

\[
\kappa_2=\frac23+\operatorname{artanh}(1/2)=1.2159728110\ldots.
\]

Thus, exactly,

\[
\boxed{H_{\rm nat}(f)=\Delta_{d,>2}+\mathcal Q_{d,<2}+R_d.}
\tag{1.4}
\]

Equation (1.4) is only a rewriting of the inherited signed ledger; it does not spend any existing credit twice.

---

## 2. `B16-HIGH-RESOLVENT-SPECTRAL-COMPRESSION` — PROVED

### Theorem 2.1

For every probability vector `p=(p_S)` arising from a Boolean Fourier spectrum (indeed for every finite probability vector),

\[
\boxed{
\Delta_{\infty,>2}
=\sum_Sp_S\log\frac{3}{2+p_S}.
}
\tag{2.1}
\]

In particular `Delta_{infty,>2}>=0`.

### Proof

Since the Fourier support is finite, interchange of the finite `S`-sum with the absolutely convergent geometric-logarithmic series is immediate. Put `k=r-1`. Then

\[
\sum_{r=2}^{\infty}
\frac{(-1)^r}{(r-1)2^{r-1}}
=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k2^k}
=\log\frac32,
\tag{2.2}
\]

while for `0<=x<=1`,

\[
\sum_{r=2}^{\infty}
\frac{(-1)^rx^r}{(r-1)2^{r-1}}
=x\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}k\left(\frac x2\right)^k
=x\log\left(1+\frac x2\right).
\tag{2.3}
\]

Insert `C_{0,r}=1-sum_Sp_S^r` into (1.1):

\[
\Delta_{\infty,>2}
=\log\frac32-
\sum_Sp_S\log\left(1+\frac{p_S}{2}\right).
\]

Because `sum_Sp_S=1`, this is exactly (2.1). Each logarithm in (2.1) is nonnegative because `p_S<=1`. `square`

### Resolvent interpretation

The same formula follows directly from the inherited resolvent identity

\[
\Delta_{\infty,>2}
=\int_2^\infty
\left[
\sum_S\frac{p_S}{p_S+t}-\frac1{1+t}
\right]dt,
\]

but (2.1) makes the pointwise spectral payment transparent.

---

## 3. `B16-R16-INFLUENCE-FLOOR` — PROVED

Define

\[
g(x)=\log\frac3{2+x},\qquad 0\le x\le1.
\]

Then `g''(x)=1/(2+x)^2>0`, `g(0)=ln(3/2)`, and `g(1)=0`. Convexity therefore places `g` below its endpoint chord:

\[
\boxed{
g(x)\le(1-x)\log\frac32.}
\tag{3.1}
\]

Multiplying by `p_S` and summing gives

\[
\Delta_{\infty,>2}
\le\log\frac32\sum_Sp_S(1-p_S)
=\log\frac32\,C_{0,2}.
\tag{3.2}
\]

The inherited R16 budget `C_{0,2}<=2J` now gives the genuinely dimension-free bound

\[
\boxed{
\Delta_{\infty,>2}
\le2\log\frac32\,J
=0.8109302162163288\ldots\,J.
}
\tag{3.3}
\]

Combining with (1.2),

\[
\boxed{
\Delta_{d,>2}
\le\left(2\log\frac32+\varepsilon_d\right)J.
}
\tag{3.4}
\]

Therefore the inherited signed R16 bank has the explicit floor

\[
\boxed{
\mathcal B_d
\ge
\left[
\kappa_2-2\log\frac32-\varepsilon_d
\right]J.
}
\tag{3.5}
\]

The limiting coefficient is

\[
\kappa_2-2\log\frac32
=0.4050425947843928\ldots.
\tag{3.6}
\]

At `d_h>=3` (hence `n>=5`), `epsilon_d<=1/32`, so (3.5) already reserves at least

\[
0.3737925947843928\ldots\,J
\]

of signed R16 bank after the whole full high-resolvent channel is accounted for. This is a lower bound on the **aggregate signed bank**, not a license to reuse individual odd-order credits elsewhere.

### Sparse folded regime

After the minimizing-character gauge, the spectral sample has mean size `J`. If `J<=1`, Markov gives

\[
p_\varnothing\ge1-J.
\]

Hence

\[
C_{0,2}=1-\sum_Sp_S^2
\le1-p_\varnothing^2
\le2J-J^2.
\]

Thus the sharper small-`J` form is

\[
\boxed{
\Delta_{\infty,>2}
\le\log\frac32\,(2J-J^2),
\qquad 0\le J\le1.
}
\tag{3.7}
\]

This adds a positive `ln(3/2) J^2` reserve to (3.5) in the sparse folded regime.

---

## 4. `B16-ONE-THIRD-ENTROPY-ABSORPTION` — PROVED

### Theorem 4.1

For every `0<x<=1`,

\[
\boxed{
\log\frac3{2+x}
\le\frac13\log\frac1x.
}
\tag{4.1}
\]

The constant `1/3` is sharp as `x->1`.

### Proof

Exponentiating three times, (4.1) is equivalent to

\[
27x\le(2+x)^3.
\]

But

\[
(2+x)^3-27x
=(x-1)^2(x+8)\ge0.
\tag{4.2}
\]

This proves (4.1). The quotient of the two sides tends to `1/3` as `x->1`. `square`

Multiplying (4.1) by `p_S` and summing gives the universal self-payment

\[
\boxed{
\Delta_{\infty,>2}
\le\frac13H_{\rm nat}(f).
}
\tag{4.3}
\]

With the half-band tail,

\[
\boxed{
\Delta_{d,>2}
\le\frac13H_{\rm nat}(f)+\varepsilon_dJ.
}
\tag{4.4}
\]

This is not circular when inserted into the exact compiler identity (1.4): it absorbs the high-resolvent response into the left-hand side.

---

## 5. `B16-SMALL-RESOLVENT-ONLY-REDUCTION` — PROVED

Insert (4.4) into (1.4):

\[
H_{\rm nat}
\le\frac13H_{\rm nat}
+\varepsilon_dJ
+\mathcal Q_{d,<2}+R_d.
\]

Therefore

\[
\boxed{
H_{\rm nat}(f)
\le\frac32
\left[
\mathcal Q_{d,<2}+R_d+\varepsilon_dJ
\right].
}
\tag{5.1}
\]

Independently, (3.4) and (1.4) give

\[
\boxed{
H_{\rm nat}(f)
\le
\mathcal Q_{d,<2}+R_d
+\left(2\log\frac32+\varepsilon_d\right)J.
}
\tag{5.2}
\]

Thus a dimension-free upper bound

\[
\mathcal Q_{d_h,<2}+R_{d_h}\le C J
\tag{5.3}
\]

would imply FEI immediately, with natural-log constant at most

\[
\boxed{
\min\left\{
C+2\log\frac32+\varepsilon_{d_h},
\frac32(C+\varepsilon_{d_h})
\right\}.
}
\tag{5.4}
\]

The point is structural rather than the displayed constant: **the alternating R16 high-resolvent channel no longer needs an independent influence payment in this reduction.** It is either paid by the explicit `0.81093 J` bound or absorbed at one-third of the entropy itself. The live universal obstruction is correspondingly concentrated on the signed small-resolvent selector/R32 channel plus the already-separate terminal response.

This does not prove (5.3). Full FEI remains OPEN.

---

## 6. Relation to the current signed-transport route

The preceding B16 work found the resolvent symbol `z/(1+z)` twice: in the projective spatial q-flip payment and in the radial Hardy first-hit variance. The new identity (2.1) shows that the **inherited R16 collision resolvent itself** also collapses to a bounded scalar spectral response, rather than an opaque infinite alternating series.

This changes the next target. The useful route is not to spend more effort estimating the high-resolvent tail order by order. At the half-band it is already saturated, explicitly bounded by (3.4), and self-absorbing by (4.4). The next account01 B16 attack should therefore stay on `0<t<2`: combine the exact first-hit/radial signed square with the source-selected small-resolvent measure before any absolute value, while reserving the quantitative bank floor (3.5) exactly once.

A particularly concrete target is to show that the fully refunded first-hit radial/plaquette residual costs at most

\[
\mathcal B_{d_h}
+KJ
\]

for a universal `K`, with the `0.4050 J` floor from (3.5) available as an explicit aggregate credit. If the residual representation still needs more than this floor on an admissible Boolean family, that would be a decisive obstruction to this compiler organization and the route should change.

---

## 7. Self-check

The companion `check_high_resolvent_compression.py` checks only the new algebra. It verifies:

- the exact polynomial factorization `(x+2)^3-27x=(x-1)^2(x+8)` by integer coefficient arithmetic;
- the series/closed-form identity (2.1) on deterministic and seeded random probability vectors, truncating after 100 collision orders (the tail is below floating-point resolution in the tested range);
- inequalities (3.2) and (4.3) on the same vectors;
- the constants in (3.3), (3.6), and the `d=3` bank floor.

These numerical checks are falsification evidence only; the proof is the algebra above.
