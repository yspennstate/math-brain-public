# B16 FEI signed transport — local triple-curvature / ordered-parent flag bridge

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact mixed-difference identities, a local distance-four cancellation, and a dimension-free ordered-parent square payment. No novelty or publication-priority claim.

## 0. Fresh entering state and route

This run uses the newest compatible signed-transport handoffs rather than a killed unsigned frame.

* The B16 correlated-noise double-resolvent writes the already-signed odd parity current as a positive sum of clone-pair curvature squares. For an odd mode `(q,k,r)`, `r=(q-k)/2`, the central multiplier is
  \[
  \varepsilon_{q,k}=2\frac{2^{-q}}q\left(\frac{2^{-k}}k-\frac{2^{-q}}q\right).
  \]
* The B16 phase-switch theorem identifies the odd active-syndrome projection with multiplication of the dual phase by the actual Boolean phase `f`, keeps the retained `C_0-D_d` subtraction signed, and proves that its global quadratic term vanishes because `C_0=RM(1,n)^\perp` has distance four.
* Account02/B16 gives the actual positive central parent coefficients after same-syndrome signed aggregation. Account03/B16 identifies those parents with the genuine ordered-min one-subcube flag.
* The fresh account03/B18 signed-flag theorem shows that the correct physical source is the signed derivative curvature, not unsigned support disagreement alone; parity is an exact Boolean obstruction to the latter.

The new move here is to **commute the odd projection through the clone-pair curvature before taking any norm**. This exposes each actual current parent as a *three-phase mixed difference* involving its two physical slice-clones and the actual Boolean phase. The distance-four cancellation then occurs locally, parent by parent. Summing the resulting local quartic squares over the genuine ordered-min parent cells is dimension-free by ordinary cube Poincare and the geometric parent-cell densities.

No R32 coefficient is positive-parted. The terminal code stays in one signed dual weight. R16/moment refunds, negative entropy credits, dual-code multiplicity, Ward boundary terms and the terminal-band payment are not spent here.

---

## 1. Actual current parent = a three-phase mixed difference

At fixed Borel time `s`, write the retained dual potential as
\[
\Psi_s(h)=\Phi_{C_0,s}(h)-\Phi_{D_d,s}(h).
\]
For the fine paired q-flip system, let `g_{j,0},g_{j,1}` be the two slice-clone phase generators of coarse parent `j`. They have disjoint negative sets and
\[
g_{j,0}g_{j,1}=g_j^{\uparrow}.
\tag{1.1}
\]
Let `T_a` denote multiplication of the dual phase by `a`, and put `Delta_a=I-T_a`.

If
\[
F_s(S)=\Psi_s(g_S),
\]
then translation by the all-active syndrome multiplies `g_S` by the actual Boolean phase `f`. Hence the odd/frustrated projection is
\[
F_s^{\rm odd}=\frac12(I-T_f)F_s.
\tag{1.2}
\]
The clone-pair curvature operator is
\[
D_j=(I-T_{g_{j,0}})(I-T_{g_{j,1}}).
\]
Therefore:

### Theorem 1.1 — `P03-B16-LOCAL-TRIPLE-CURVATURE` — PROVED

For every syndrome state `S`,
\[
\boxed{
D_jF_s^{\rm odd}(S)
=\frac12\,\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s(g_S).
}
\tag{1.3}
\]

This is an exact identity, not an estimate. In the relation expansion a coefficient survives (1.3) iff the relation is frustrated by `f` and contains **both** clone coordinates of parent `j`. Thus (1.3) is precisely the doubled-parent sector appearing in the genuine double-resolvent current.

---

## 2. Exact clone-pair cosine factorization

For one residual dual word, split the truth table into the outside of the coarse parent and the two disjoint clone halves. Let the corresponding normalized signed sums be `A,B,C`. Because the two clone negative sets are disjoint,
\[
\boxed{
\Delta_{g_{j,0}}\Delta_{g_{j,1}}\cos(s(A+B+C))
=-4\cos(sA)\sin(sB)\sin(sC).
}
\tag{2.1}
\]

Now split each region by the sign of the actual Boolean phase:
\[
A=A_++A_-,\qquad B=B_++B_-,\qquad C=C_++C_-.
\]
Multiplication by `f` replaces every `+` sum by itself and every `-` sum by its negative. Define
\[
Q_+=\cos s(A_++A_-)\sin s(B_++B_-)\sin s(C_++C_-),
\]
\[
Q_-=\cos s(A_+-A_-)\sin s(B_+-B_-)\sin s(C_+-C_-).
\]
Then the scalar triple difference is `-4(Q_+-Q_-)`, and exact trigonometric expansion gives
\[
\begin{aligned}
Q_+-Q_-=2[&\cos(sA_+)\cos(sA_-)\sin(sB_+)\cos(sB_-)\cos(sC_+)\sin(sC_-)\\
&+\cos(sA_+)\cos(sA_-)\cos(sB_+)\sin(sB_-)\sin(sC_+)\cos(sC_-)\\
&-\sin(sA_+)\sin(sA_-)\sin(sB_+)\cos(sB_-)\sin(sC_+)\cos(sC_-)\\
&-\sin(sA_+)\sin(sA_-)\cos(sB_+)\sin(sB_-)\cos(sC_+)\sin(sC_-)].
\end{aligned}
\tag{2.2}
\]
The apparent quadratic part of the bracket is
\[
s^2(B_+C_-+B_-C_+).
\tag{2.3}
\]

---

## 3. Local distance-four cancellation — PROVED

Let `E<=C_0` be either retained relation code and `P=E^\perp`. For disjoint truth-table cells `X,Y`, character orthogonality gives
\[
\frac1{|P|}\sum_{r\in P}X_rY_r=0,
\tag{3.1}
\]
because a surviving term would require a weight-two word `e_x+e_y` in `E`, impossible for `E<=C_0` when `x!=y`.

The cells `B_+` and `C_-` are disjoint, as are `B_-` and `C_+`. Hence each code separately satisfies
\[
\boxed{
\sum_{r\in P}(B_{r,+}C_{r,-}+B_{r,-}C_{r,+})=0.
}
\tag{3.2}
\]
Therefore the **retained signed `C_0-D_d` combination also cancels (2.3) exactly before an absolute value is taken**.

This is a local version of the global phase-switch quadratic cancellation: every doubled current parent begins at four-point order after the authentic dual-code average.

---

## 4. Keep the terminal subtraction signed

Write
\[
P_0=C_0^\perp=RM(1,n),\qquad P_1=D_d^\perp,\qquad L=|P_1|,
\]
\[
\rho_d=\frac{2N}{L},\qquad \gamma_d=1-\rho_d,
\]
and combine the retained potential with the signed weights
\[
\alpha_r=\frac1{2N}1_{r\in P_0}-\frac1L1_{r\in P_1}.
\tag{4.1}
\]
For any truth-table cell `X` of density `d_X`, the same distance-four orthogonality gives the exact absolute-weight second moment
\[
\boxed{
\sum_r|\alpha_r|X_r^2=\frac{2\gamma_d}{N}d_X.
}
\tag{4.2}
\]
Indeed each normalized code average contributes `d_X/N`; on `P_0` the positive absolute weight is `1/(2N)-1/L`, while on `P_1\setminus P_0` it is `1/L`.

Thus for any two cells,
\[
\sum_r|\alpha_r||X_rY_r|
\le\frac{2\gamma_d}{N}\sqrt{d_Xd_Y}.
\tag{4.3}
\]
The terminal subtraction is therefore retained in one signed object and contributes exactly through the factor `gamma_d`; it is not paid twice.

---

## 5. A local quartic bound on each genuine ordered parent

Return to the old physical cube before the dummy split. Let `C_j` be the coarse one-subcube parent cell, of density
\[
\delta_j.
\]
In the minimizing-character gauge for `f`, put
\[
u_j^\pm=\Pr[x\in C_j,\ f(x)=\pm1],
\qquad
p_\pm=\Pr[f=\pm1],
\]
\[
a_j^\pm=p_\pm-u_j^\pm.
\tag{5.1}
\]
The two clone halves each contain exactly half of `u_j^+` and half of `u_j^-` in the dummy-extended cube.

Use
\[
|\sin z-z|\le |z|^3/6,
\quad |\sin z|\le|z|,
\quad 1-\cos z\le z^2/2
\]
in (2.2), subtract the exactly cancelled quadratic term (3.2), and apply (4.3). One obtains:

### Theorem 5.1 — `P03-B16-LOCAL-RETAINED-QUARTIC` — PROVED

For every dual phase `h`, every genuine coarse parent `j`, and every real `s`,
\[
\boxed{
\begin{aligned}
&|\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s(h)|\\
&\quad\le16\gamma_d s^4\left[
2\sqrt{u_j^+u_j^-}
\left(\frac{(a_j^+)^2+(a_j^-)^2}{2}
+\frac{(u_j^+)^2+(u_j^-)^2}{6}\right)
+a_j^+a_j^-\delta_j
\right].
\end{aligned}}
\tag{5.2}
\]
In particular,
\[
\boxed{
|\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s(h)|
\le16\gamma_d s^4\left[
\frac43\sqrt{u_j^+u_j^-}+p_+p_-\delta_j
\right].
}
\tag{5.3}
\]

The important feature is not the numerical constant: the right side is expressed in the **actual physical parent cell's sign mixing**, with the signed terminal factor intact.

---

## 6. Ordered-min parent cells have a dimension-free total square bank

Fix a physical coordinate order `pi`. For pivot `i`, let `m_i` be the number of coordinates later than `i`. The inherited ordered-min parent cell fixes the pivot and every later coordinate, so
\[
\delta_i=2^{-(m_i+1)}.
\tag{6.1}
\]
As the ordered-min displacement varies, the `2^{m_i}` parent cells for fixed pivot are disjoint and partition one pivot half-cube.

Inside one such cell, only earlier coordinates are free. Conditional cube Poincare gives
\[
4\frac{u_j^+u_j^-}{\delta_i^2}
\le I(f\mid C_j).
\tag{6.2}
\]
After multiplying by the cell probability and summing the partition for fixed pivot, then summing pivots,
\[
\boxed{
\sum_j u_j^+u_j^-\le\frac14J(f).
}
\tag{6.3}
\]
Here `f` is in the same minimizing-character gauge as the phase-switch continuation, so `I(f)=J(f)`.

Also, since the values `m_i` are exactly `0,1,...,n-1`,
\[
\boxed{
\sum_j\delta_j^2
=\sum_{m=0}^{n-1}2^m2^{-2m-2}
<\frac12.
}
\tag{6.4}
\]
Finally cube Poincare on the whole folded function gives
\[
p_+p_-\le J(f)/4,
\]
and `p_+p_-<=1/4`, hence
\[
(p_+p_-)^2\sum_j\delta_j^2\le J(f)/32.
\tag{6.5}
\]

Combining (1.3), (5.3), and Cauchy across the actual parent family gives the new square bank:

### Theorem 6.1 — `P03-B16-ORDERED-PARENT-TRIPLE-SQUARE` — PROVED

Let `F_s^{odd}` be the authentic retained odd syndrome field. Then pointwise in the syndrome state, and hence also after syndrome averaging,
\[
\boxed{
\sum_j |D_jF_s^{odd}|^2
\le
64\left(\frac23+\frac1{4\sqrt2}\right)^2
\gamma_d^2 s^8 J(f).
}
\tag{6.6}
\]
The numerical coefficient is
\[
45.529389109757\ldots.
\]

This is a dimension-free **original-coordinate** payment for the complete local doubled-parent square bank. It did not require an unsigned q-flip support frame, and therefore avoids the exact parity obstruction found by account03/B18.

---

## 7. Consequence for the central double-resolvent current

For one odd mode `(q,k,r)`, summing `||D_jF^{odd}||_2^2` over its `r` doubled parents gives `16r b_R^2`. Since
\[
\frac{\varepsilon_{q,k}}{16r}\le\frac{11}{4608},
\tag{7.1}
\]
with equality at `(q,k,r)=(3,1,1)`, the exact central current satisfies
\[
\boxed{
\mathcal E_{cen}(s)
\le\frac{11}{4608}\sum_j\|D_jF_s^{odd}\|_2^2.
}
\tag{7.2}
\]
Therefore:
\[
\boxed{
\mathcal E_{cen}(s)
\le
\frac{11}{72}
\left(\frac23+\frac1{4\sqrt2}\right)^2
\gamma_d^2 s^8J(f).
}
\tag{7.3}
\]
The coefficient is
\[
0.108685607684\ldots.
\]

This is **not numerically stronger** than the previously proved global phase-switch quartic estimate at small `s`. Its value is structural: it localizes the authentic current to the actual ordered-min physical parent cells while preserving the phase/orientation information that an unsigned support pushforward loses.

---

## 8. What this kills and what remains open

### PROVED here

1. Every doubled-parent odd current is exactly half of a retained three-phase mixed difference `Delta_clone0 Delta_clone1 Delta_f`.
2. The apparent local quadratic term cancels codewise by the same distance-four mechanism as the global phase-switch cancellation.
3. The signed terminal subtraction remains inside one exact weight and yields the factor `1-rho_d`.
4. The resulting local quartic square bank sums over **all ordered-min parents** with a dimension-free `J(f)` bound.
5. The central current is consequently bounded by the local parent bank through the exact `11/4608` mode ratio.

### KILLED / not revived

* No domination of signed additive curvature by unsigned support disagreement is used; parity refutes that interface.
* No unit-weight arbitrary-q-flip frame, one-resolvent shortcut, generic endpoint `L2`, basiswise `L_v=O(n)`, or positive-part R32 relation sum is used.
* The terminal, R16/moment, negative-credit and resolvent-boundary ledgers are not re-spent.

### OPEN

The large-Borel corridor is still open. The new local theorem says the correct object to transport is the **three-phase mixed parent curvature**, not a sign-free q-flip indicator. The next calculation should keep the exact sine/cosine expression (2.2), insert the random ordered-flag Hardy kernel on the physical parent cells, and seek a large-`s` contraction into the signed derivative Hardy bank proved by account03/B18. If that contraction fails on authentic R32 coefficients, preserve the Boolean packet and identify the orthogonal component.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
