# HARD8-07 — scale-optimization strengthening

**STATUS: OPEN / APPEND-ONLY STRENGTHENING OF THE 09:36:51Z CHECKPOINT**

This file strengthens, but does not overwrite, the report

`hard8_2026-09-16/HARD8-07/runs/2026-09-16/2026-09-16T09-36-51Z__report.md`

creation commit `84fd0a717386f3d81090797a75ba8bbcb6d192fc`.

The first report retained the previous Matala canonical scale \(B_{m+1}\asymp D_n^{2/3}\), which led to a growing signed-portal box \(R=o(D_n^{1/9})\). After publication I re-optimized the argument and found that the modular signed-portal method does **not** need the Matala \(2/3\) scale. Matching the \(\alpha\)-denominator directly to \(D_n\) improves the admissible box to \(R=o(D_n^{1/3})\).

## 1. Free-scale inequality

Keep the bounded-type hard core and notation of the main report. Let \(m,n\) now be arbitrary indices, put
\[
M=B_{m+1},
\]
and for a signed portal
\[
q=Q_n(z,v)=|zD_n+vD_{n+1}|,
\qquad |z|,|v|\le R,
\]
define the exact modular coordinate
\[
\rho_{m,n}(z,v)
=
\left\|
\frac{qA_{m+1}}{B_{m+1}}
\right\|.
\]
Exactly as in equations (6.1)–(6.4) of the main report, choose the centered coefficient \(x\) in
\[
q=xB_m+yB_{m+1}.
\]
Then
\[
\frac{|x|}{M}=\rho_{m,n}(z,v)
\]
and
\[
\|q\alpha\|
\le
2\rho_{m,n}(z,v)+\frac{q}{M^2}.
\]
The signed-portal \(\beta\)-bound remains
\[
q\|q\beta\|\le2(A_\beta+2)R^2,
\]
while
\[
q\le(A_\beta+2)RD_n.
\]
Therefore, for **every** pair of indices \(m,n\),
\[
\boxed{
q\|q\alpha\|\|q\beta\|
\le
4(A_\beta+2)R^2\rho_{m,n}(z,v)
+2(A_\beta+2)^2\frac{R^3D_n}{B_{m+1}^2}.
}
\tag{1.1}
\]
This is the actual scale-free form of the new method.

## 2. Matched-scale choice

Choose \(m=m_*(n)\) by
\[
\boxed{
B_{m+1}\le D_n<B_{m+2}.
}
\tag{2.1}
\]
Because \(\alpha\) is badly approximable with partial quotients at most \(A_\alpha\),
\[
B_{m+2}\le(A_\alpha+1)B_{m+1},
\]
so
\[
\boxed{
\frac{D_n}{A_\alpha+1}<M_n^*:=B_{m_*(n)+1}\le D_n.
}
\tag{2.2}
\]
Define
\[
\rho_n^*(z,v)
=
\left\|
\frac{Q_n(z,v)A_{m_*(n)+1}}{M_n^*}
\right\|.
\]
Substituting (2.2) into (1.1) gives
\[
\boxed{
Q_n(z,v)\|Q_n(z,v)\alpha\|\|Q_n(z,v)\beta\|
\le
4(A_\beta+2)R^2\rho_n^*(z,v)
+C_*\frac{R^3}{D_n},
}
\tag{2.3}
\]
where
\[
C_*=2(A_\beta+2)^2(A_\alpha+1)^2.
\tag{2.4}
\]

## 3. Stronger growing-box criterion

### Theorem 3.1

Let \(R_n\to\infty\) satisfy
\[
\boxed{R_n=o(D_n^{1/3}).}
\tag{3.1}
\]
If infinitely often there are nonzero integers \((z_n,v_n)\) with
\[
|z_n|,|v_n|\le R_n
\]
and
\[
\boxed{
R_n^2\rho_n^*(z_n,v_n)\to0,
}
\tag{3.2}
\]
then the classical Littlewood conjecture holds for \((\alpha,\beta)\).

#### Proof

The finite bounded-type denominator lemma from the main report gives uniformly
\[
Q_n(z_n,v_n)\ge\frac{D_n}{(A_\beta+2)R_n}\to\infty
\]
because \(R_n=o(D_n)\). The first term of (2.3) tends to zero by (3.2), and the second tends to zero by (3.1). QED.

Thus the \(1/9\) exponent in the first report is **not intrinsic**. It came only from retaining the earlier Matala \(B_{m+1}\asymp D_n^{2/3}\) scale. The optimized signed-portal argument reaches the natural \(R=o(D_n^{1/3})\) range at matched denominator scale.

## 4. Stronger counterexample obstruction

Define the matched-scale torus point
\[
\Theta_n^*
=
\left(
\frac{D_nA_{m_*+1}}{M_n^*},
\frac{D_{n+1}A_{m_*+1}}{M_n^*}
\right)
\pmod1
\]
and
\[
\mu_n^*(R)
=
R^2
\min_{\substack{(z,v)\in\mathbb Z^2\setminus\{0\}\\|z|,|v|\le R}}
\|z\Theta_{n,1}^*+v\Theta_{n,2}^*\|.
\]
As before, two-dimensional Dirichlet gives
\[
\mu_n^*(R)\le1.
\]

If
\[
\Lambda=\liminf_{q\to\infty}q\|q\alpha\|\|q\beta\|>0,
\]
then for **every** integer scale
\[
R_n\to\infty,
\qquad
R_n=o(D_n^{1/3}),
\]
the same argument applied to (2.3) gives, eventually,
\[
\boxed{
\mu_n^*(R_n)
\ge
\frac{\Lambda}{16(A_\beta+2)}.
}
\tag{4.1}
\]
So a counterexample must constant-factor saturate the two-variable Dirichlet bound throughout every growing character box below \(D_n^{1/3-o(1)}\), not merely below \(D_n^{1/9-o(1)}\).

## 5. Why the exponent \(1/3\) appears here

At matched scale \(M\asymp D_n\), a signed portal with coefficient radius \(R\) has
\[
q=O(RD_n).
\]
The exact \(\alpha\)-frame decomposition contributes the deterministic remainder
\[
\frac{q}{M^2}=O(R/D_n).
\]
The \(\beta\)-side costs \(O(R^2)\), so this term contributes
\[
O(R^3/D_n)
\]
to the Littlewood product. Hence \(R=o(D_n^{1/3})\) is the natural range for this particular matched-scale estimate.

The separate modular term is still critical:
\[
R^2\rho_n^*.
\]
Generic Dirichlet gives only \(O(1)\), not \(o(1)\). Thus scale optimization enlarges the range substantially but does **not** remove the central constant-factor obstruction.

## 6. A still more general observation

Equation (1.1) permits choosing \(B_{m+1}\) larger than \(D_n\), which can make the deterministic term \(R^3D_n/B_{m+1}^2\) arbitrarily small. However one must keep \(R=o(D_n)\) (or otherwise separately exclude the exact zero relation \((z,v)=(D_{n+1},-D_n)\)) so that signed portals are genuine positive denominators tending to infinity. Enlarging \(m\) therefore does not by itself solve the problem: the modular term remains at the sharp Dirichlet scale \(R^2\rho\).

This identifies the genuine bottleneck more cleanly than the original \(2/3\)-scale formulation.

## 7. Updated next attack

The next iteration should work with the scale-free inequality (1.1), not the older canonical \(2/3\) scale. The most promising concrete target is an **anisotropic short-character theorem** that simultaneously controls
\[
\rho_{m,n}(z,v)
\quad\text{and}\quad
|v-z\eta_n|,
\]
because the crude \(O(R^2)\) bound for \(q\|q\beta\|\) throws away the possibility that the short modular relation is also close to the continued-fraction tail direction. A pure cardinality/volume argument is expected to remain critical, so any gain must exploit the recurrence structure of the two continued fractions.

The full classical Littlewood conjecture remains open.