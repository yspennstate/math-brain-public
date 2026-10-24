# B18 addendum — a dimension-free L2 phase-imbalance bank paid by scalar-frontier slack

**Status:** **PROVED auxiliary theorem / full FEI OPEN.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Dependencies:** sibling `REPORT.md` and `PHASE_HANDOFF.md` only.

The pointwise phase handoff leaves a square-root bad-posterior tail. Coordinate-by-coordinate that tail costs `sqrt(M_i)`, which is too weak for a linear selector. However, the current signed-transport routes naturally use **squares**. After squaring and summing over coordinates, the square-root loss disappears completely.

Retain the notation of `PHASE_HANDOFF.md`. For coordinate `i`, let

\[
Z_i=Y_{i,+}-Y_{i,-},
\]

where `Y_{i,+}` and `Y_{i,-}` are the upper Fourier masses on good endpoint edges `|q_{i,T}-tau|<eta` with positive and negative signed Fourier edge product respectively. Let

\[
V_i=\sum_Tp_{T+i}(q_{i,T}-\tau)^2,
\]

\[
M_i=\sum_{T:\,|q_{i,T}-\tau|\ge\eta}p_{T+i},
\]

and let

\[
R_i=\sum_{T:\,|q_{i,T}-\tau|\ge\eta}\sqrt{p_Tp_{T+i}}.
\]

The preceding proposition gives

\[
|Z_i|\le C_{\tau,\eta}\sqrt{p_iV_i}+\sqrt\theta\,R_i,
\tag{1}
\]

with `theta=tau/(1-tau)`.

## Theorem — L2 sign imbalance is linearly paid

For a restriction-maximal hard core at ratio `r>4`, let

\[
D_r=B-b(r)I,
\]

and let `c_r>0` be the tangent-defect stability constant proved in `REPORT.md`. Then

\[
\boxed{
\sum_i Z_i^2
\le
{2D_r\over c_r}
\left(
C_{\tau,\eta}^2+{\theta\over\eta^2}
\right).
}
\tag{2}
\]

Equivalently,

\[
\boxed{
D_r\ge
{c_r\over2(C_{\tau,\eta}^2+\theta/\eta^2)}
\sum_iZ_i^2.
}
\tag{3}
\]

Thus the scalar-frontier slack itself contains a dimension-free quadratic payment for phase imbalance of the near-endpoint Fourier edges.

### Proof

From Cauchy on the bad edges,

\[
R_i^2
\le
\left(\sum_{bad}p_T\right)
\left(\sum_{bad}p_{T+i}\right)
\le M_i,
\tag{4}
\]

because `sum_Tp_T=1-p_i<=1`. Squaring (1) with `(a+b)^2<=2a^2+2b^2` gives

\[
Z_i^2
\le2C_{\tau,\eta}^2p_iV_i+2\theta R_i^2.
\]

Since `p_i<=1`, summing and using the scalar stability estimates

\[
\sum_iV_i\le D_r/c_r,
\qquad
\sum_iM_i\le D_r/(c_r\eta^2)
\]

gives (2). QED.

## Corollary — L2 half-half phase law

Because

\[
Y_{i,+}+Y_{i,-}=p_i-M_i,
\]

we have

\[
Y_{i,+}-{p_i\over2}={Z_i-M_i\over2},
\qquad
Y_{i,-}-{p_i\over2}={-Z_i-M_i\over2}.
\]

Therefore

\[
\sum_i\left[
\left(Y_{i,+}-{p_i\over2}\right)^2
+\left(Y_{i,-}-{p_i\over2}\right)^2
\right]
={1\over2}\sum_i(Z_i^2+M_i^2).
\]

Since `0<=M_i<=1`, `M_i^2<=M_i`, so

\[
\boxed{
\sum_i\left[
\left(Y_{i,+}-{p_i\over2}\right)^2
+\left(Y_{i,-}-{p_i\over2}\right)^2
\right]
\le
{D_r\over c_r}
\left(
C_{\tau,\eta}^2+{\theta+1/2\over\eta^2}
\right).
}
\tag{5}
\]

This robustly extends the exact endpoint sign law `Y_{i,+}=Y_{i,-}=p_i/2`.

## Integration significance

The bad low-posterior edges can indeed carry signed convolution mass of order `sqrt(y)` and therefore defeat a **coordinatewise linear** payment. But they cannot defeat the squared global bank: their contribution satisfies

\[
\sum_iR_i^2\le\sum_iM_i\le D_r/(c_r\eta^2).
\]

This is the first phase-sensitive dimension-free payment extracted directly from the new scalar stability theorem. Its geometry matches the squared-divergence form appearing in the current B16 Hardy/Ward interface, although no identification between `Z_i` and B16's plaquette divergence is claimed here.

The next integration question is now narrower: either (a) show that a restriction-critical core with large `r` must generate a nontrivial L2 phase-imbalance bank `sum Z_i^2`, which (3) immediately charges, or (b) classify the nearly half-half signed endpoint regime and feed its residual square/cycle constraints into the B16 signed transport or block-collision machinery. This avoids the refuted attempt to pay every unsigned pairwise term separately.
