SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T17:21:19Z.
attacking: QFORM-MIXED-OFFDIAGONAL-TRANSVERSE-COAREA-v1 — after the chi and Psi exits fail, isolate and spend the exact off-diagonal transverse curvature U before reciprocal coarea inversion.

# account03/B05 r29 — currency compensation inside the mixed-transverse cancellation chamber

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea bound.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `NEW SUPPORTING DETERMINISTIC THEOREM / FRACTIONAL-TRACE CONSEQUENCE / FULL QFORM OPEN`.  
**Regularity:** no new full density or continuity theorem is claimed here.

The predecessor r28 is source-pinned at

`yspennstate/math-open-problems@175ac74eb73ef3444ec1a6d998b78a02e72104f2:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T164014Z-account03-B05-QFORM-r28/`.

Its final source refresh already removed the broad punctured-null gap by applying account02/B05 `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1`. The actual survivor is the simultaneous mixed-transverse cancellation chamber. This run proves that the two previously identified currencies cannot both disappear without forcing a large determinant in the same original product-projection bank.

## 1. Packet notation and already-paid exits

Use the live exact ratio packet

\[
H=\begin{pmatrix}C&P\\P^T&B\end{pmatrix},\qquad
B=\begin{pmatrix}a&c\\c&d\end{pmatrix},\qquad
P=\begin{pmatrix}\alpha&\beta\\r&s\end{pmatrix},
\]
with `B` invertible and indefinite and
\[
C-PB^{-1}P^T=\begin{pmatrix}L&0\\0&0\end{pmatrix},
\qquad L=\lambda m,
\qquad \mu=|\det B|\,|\lambda|.
\]
Here `(S,R)` is an orthonormal two-dimensional projection of one original-coordinate product bank; `Y,Z` are normalized scalar projections of two disjoint product banks, independent of each other and of the first bank. The packet construction gives `m>=3/20`.

Put
\[
\Delta=\det B<0,\qquad q=(r,s)^T,\qquad z=B^{-1}q=(z_1,z_2)^T,
\]
and
\[
\tau=\det P=\alpha s-\beta r.
\]
The r28 exact determinant identities are
\[
|\det H_Y|=\mu m z_2^2,\qquad |\det H_Z|=\mu m z_1^2. \tag{1.1}
\]
Its fresh-square currency is
\[
\chi:=\max\{|d|z_1^2,|a|z_2^2\}. \tag{1.2}
\]
The final source refresh defines
\[
T_Y=Lr^2+\frac{a}{\Delta}\tau^2,\qquad
T_Z=Ls^2+\frac{d}{\Delta}\tau^2, \tag{1.3}
\]
\[
\Psi:=\max\{|T_Y|z_2^2,|T_Z|z_1^2\}. \tag{1.4}
\]
The paid exits are
\[
\|p_Q\|_\infty\le128\sqrt2\,(\mu m\chi)^{-1/4} \tag{1.5}
\]
when `chi>0`, and
\[
\|p_Q\|_\infty\le76.074\,(\mu m\Psi)^{-1/6} \tag{1.6}
\]
when `Psi>0` in the source theorem's nonzero factors. The issue is not that (1.5)-(1.6) are false; it is that either displayed bound deteriorates as its own currency tends to zero.

## 2. New exact block-determinant identity

For a symmetric `2 x 2` matrix `C` and a vector `h`,
\[
h^T\operatorname{adj}(C)h=(Jh)^TC(Jh),\qquad J(x_1,x_2)=(-x_2,x_1). \tag{2.1}
\]
Therefore the scalar-plus-pair determinant formula gives
\[
\det\begin{pmatrix}\gamma&h^T\\h&C\end{pmatrix}
=\gamma\det C-(Jh)^TC(Jh). \tag{2.2}
\]
Apply (2.2) to the two retained conditional matrices. Their scalar-to-pair cross vectors are
\[
h_Y=(\alpha,r)^T,\qquad h_Z=(\beta,s)^T.
\]
By (1.3), `(Jh_Y)^TC(Jh_Y)=T_Y` and `(Jh_Z)^TC(Jh_Z)=T_Z`. Hence
\[
\boxed{\det H_Y=a\det C-T_Y,\qquad \det H_Z=d\det C-T_Z.} \tag{2.3}
\]
Combining with (1.1) gives two exact currency identities:
\[
\boxed{|a\det C-T_Y|=\mu m z_2^2,} \tag{2.4}
\]
\[
\boxed{|d\det C-T_Z|=\mu m z_1^2.} \tag{2.5}
\]
No probability argument is used here.

## 3. Main theorem — `QFORM-RATIOPACKET-CURRENCY-COMPENSATION-v1`

Let
\[
\theta^2:=z_1^2+z_2^2.
\]
Then
\[
\boxed{\chi\,|\det C|+\Psi\ge \frac14\,\mu m\,\theta^4.} \tag{3.1}
\]

### Proof

Let
\[
w:=\max(z_1^2,z_2^2)\ge\theta^2/2. \tag{3.2}
\]
Suppose first `w=z_2^2`. Multiply (2.4) by `w` and use the triangle inequality:
\[
\mu m w^2
\le |a|w\,|\det C|+|T_Y|w
\le \chi|\det C|+\Psi. \tag{3.3}
\]
Since `w^2>=theta^4/4`, (3.1) follows. If `w=z_1^2`, use (2.5) instead. QED.

### Consequence 3.2 — failure of both density exits forces large pair determinant

If
\[
\Psi\le\frac18\mu m\theta^4, \tag{3.4}
\]
then (3.1) gives
\[
\boxed{\chi|\det C|\ge\frac18\mu m\theta^4.} \tag{3.5}
\]
Thus whenever `chi>0`,
\[
\boxed{|\det C|\ge \frac{\mu m\theta^4}{8\chi}.} \tag{3.6}
\]
In particular, along any survivor with quantitative `mu*m*theta^4` and `chi->0`, the determinant of the quadratic form carried by the **same original product-projection bank `(S,R)`** must diverge like at least `chi^{-1}`. The curvature does not disappear; it is transferred into the pair block.

If `chi=0` while (3.4) holds and `theta>0`, (3.1) is impossible. Hence a true low-`Psi`, active-shear survivor cannot sit at `chi=0`; it must be punctured with a nonzero raw diagonal and compensating large `|det C|`.

## 4. Apply the completed rank-two affine half-Riesz theorem

The completed orientation-free theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` states that for an orthonormal two-dimensional product projection `U^TX`, invertible symmetric `2 x 2` matrix `Lambda`, and an arbitrary original-coordinate affine term,
\[
\sup_t E\,|(U^TX)^T\Lambda(U^TX)+b^TX-t|^{-1/2}
\le128|\det\Lambda|^{-1/4}. \tag{4.1}
\]
Condition on the independent scalar banks `Y,Z`. Their values create only an arbitrary affine term on the first original-coordinate bank; the quadratic matrix on `(S,R)` is exactly `C`. Thus, whenever (3.4) holds,
\[
\sup_t E\left[|Q-t|^{-1/2}\mid Y,Z\right]
\le128|\det C|^{-1/4}. \tag{4.2}
\]
Average over `Y,Z` and use (3.6):
\[
\boxed{
\sup_t E|Q-t|^{-1/2}
\le128\left(\frac{8\chi}{\mu m\theta^4}\right)^{1/4}.
} \tag{4.3}
\]
This is a genuine product-preserving fractional-trace estimate. It becomes **stronger**, not weaker, as the fresh-square currency `chi` tends to zero inside the low-`Psi` active-shear chamber.

Equation (4.3) is not a bounded-density theorem: a uniform half-Riesz potential does not by itself control `||p_Q||_infinity`. Its value is that it eliminates the possibility that the remaining singularity is caused by loss of pair curvature. The unpaid half-order of smoothing must come from coupling this increasingly strong pair trace to the two independent scalar banks before absolute values/conditioning destroy the needed cancellation.

## 5. Exact mixed off-diagonal location of the transferred curvature

For completeness, the r28 addendum proved the following further identity. Let
\[
u=(-r,\alpha)^T,\qquad v=(-s,\beta)^T,
\]
and
\[
U:=u^TCv.
\]
Then
\[
\boxed{U=Lrs+\frac{c}{\Delta}\tau^2,} \tag{5.1}
\]
\[
\boxed{T_YT_Z-U^2=\tau^2\det C,} \tag{5.2}
\]
with
\[
\det C=\frac{\tau^2}{\Delta}+Lq^TB^{-1}q. \tag{5.3}
\]
Hence if `|T_YT_Z| <= (1/2)|tau|^2|det C|`,
\[
\boxed{|U|\ge2^{-1/2}|\tau|\sqrt{|\det C|}.} \tag{5.4}
\]
Combining (3.6) and (5.4), on that subbranch
\[
\boxed{
|U|\ge 2^{-1/2}|\tau|
\left(\frac{\mu m\theta^4}{8\chi}\right)^{1/2}.
} \tag{5.5}
\]
So when both diagonal transverse currencies are genuinely canceled, the forced large determinant from Theorem 3.1 appears concretely as an off-diagonal transverse curvature unless the cross-block area `|tau|` itself collapses.

This gives an exact deterministic trichotomy for the active-shear chamber:

1. `Psi` quantitative: paid by the account02/B05 near-null scalar/dependent-pair theorem;
2. `Psi` small but `|tau|^2|det C|` quantitative relative to `|T_YT_Z|`: the missing curvature is forced into `U`, and the full pair half-Riesz budget improves as `chi->0`;
3. `Psi` small and the mixed determinant product `tau^2 det C` also small: the scalar-to-pair cross block is collapsing in two-volume or the pair determinant is not the active resource, so a separate structural escaped-curvature argument is required.

## 6. Designated account04/B05 result applied

The completed designated partner theorem

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

proves
\[
\|p_Q\|_\infty<51.6(\mu m_*)^{-1/3}. \tag{6.1}
\]
Thus on the actual branch
\[
\mu\ge1,\qquad m_*\ge1/8,
\]
we obtain
\[
\boxed{\|p_Q\|_\infty<103.2.} \tag{6.2}
\]
For the r28 odd-`N` trigonometric stress frame, `1/N<=m_*<=2/N`, so the partner displayed RHS is `Theta(N^(1/3))`; this confirms that (3.1)-(5.5) address a genuinely different diffuse/cancellation mechanism rather than rephrasing the exact-slope exit.

## 7. First remaining implication

The exact next B05 analytic step is now narrower:

`QFORM-MIXED-OFFDIAGONAL-HALFRIESZ-TO-DENSITY-v1`:

> In the active-shear ratio packet, assume the low-`Psi` branch so that the same-bank rank-two half-Riesz bound (4.3) is strong, and in the balanced mixed subbranch retain the quantitative off-diagonal currency `U` from (5.5). Combine this fractional trace with the two genuinely independent scalar product banks to obtain an `O(epsilon)` interval bound, without conditioning the residual projection coordinate, without rotating it into falsely independent coordinates, and without taking a fiber supremum before aggregation.

If `tau^2 det C` collapses instead, transfer to the structural escaped-curvature branch; do not spend another run merely reparametrizing `T_Y,T_Z`.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains OPEN. No Gaussianity, log-concavity, moments, compact support, connected support, post-rotation independence, arbitrary-joint coarea, positive conditional projection-density moment, or law-uniform pointwise quadratic Fourier decay is used.