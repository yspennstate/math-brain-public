# account03/B02 r54 — multiplicity-seven weighted-Fourier bridge

Run: \`20260924T182540Z-account03-B02-fixedmult-r54\`  
Objective: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`  
Status: **PROVED SUPPORTING LEMMAS / MULTIPLICITY 7 OPEN / UNRESTRICTED 3 OPEN**.

Full proof and source ledger are in the canonical run report:
\`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T182540Z-account03-B02-fixedmult-r54/REPORT.md\`.

## New result 1: weighted rough scalar-square Fourier estimate

If \(Y\) has arbitrary probability density \(0\le f\le1\), \(a\ne0\), and
\[
\Psi(t)=\mathbb E e^{it(aY^2+bY+c)},
\]
then
\[
\int_{|t|\ge |a|^{-1}}\frac{|\Psi(t)|}{|t|}\,dt
\le\frac4{1-2^{-1/4}}<26.
\]

The proof uses only the exact conditional length bound
\[
\mathbb P(|Z^2-(Z')^2|\le r)\le\min(1,2\sqrt{2r})
\]
for independent cap-one \(Z,Z'\), which yields
\[
\int_0^U|\mathbb E e^{isZ^2}|^2ds\le4\sqrt2\,U^{1/2}\quad(U\ge1),
\]
followed by dyadic Cauchy--Schwarz. This bypasses the false uniform pointwise quadratic-phase-decay premise.

## New result 2: separated rank-two plus scalar-square Fourier \(L^1\)

For disjoint original-coordinate blocks \(U,V,H,Z\), with \(U,V\in\mathbb R^2\), if conditional on \(Z=z\)
\[
Q=F_z(U)+G_z(V)+2U^TBV+aH^2+b_zH+c_z,
\]
where \(B\) is fixed invertible and \(a\ne0\), then
\[
\int|\phi_Q(t)|dt
\le\frac2{|a|}
+\frac{4\pi}{1-2^{-1/4}}|\det B|^{-1/2}
<\frac2{|a|}+26\pi|\det B|^{-1/2}.
\]
Hence \(Q\) has a continuous \(C_0\) density with
\[
\|p_Q\|_\infty
<\frac1{\pi|a|}+13|\det B|^{-1/2}.
\]
The rank-two factor is the original-coordinate Plancherel estimate
\[
\left|\mathbb E e^{it(F(U)+G(V)+2U^TBV)}\right|
\le\frac{\pi}{|t|\sqrt{|\det B|}}.
\]

## New result 3: exact \(s_7\) same-seed shared-anchor collar

Set \(\eta=1/100,\ \kappa=1/6400\). In the no-\(\eta\)-pivot chamber with \(s_7(A)\ge1\), either
\[
V_3(A)\ge\kappa^3,
\]
which is already paid by the order-three physical receiver with a \(C_0\) density and bound \(<2400\), or there are disjoint physical two-sets \(S,T\), \(h\notin S\cup T\), and the same order-two interpolation seed \(B=A[S,T]\) such that
\[
\|E\|_F<3/80,\qquad
|D_{hh}|>77/80,\qquad
|P_{hh}|>381/400,
\]
and
\[
|\det A[S\cup\{h\},T\cup\{h\}]|
>\frac{77}{80}|\det A[S,T]|.
\]

The equation-level partner input is the completed account04/B02 same-seed estimate
\[
\|E\|_F^2\le9V_3/V_2
\]
from
\`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account04/B02/20260924T161206Z-account04-B02-nine400-overlap-audit-r1/REPORT.md\`.
At \(s_7\), the global interpolation rank is at most six, so
\[
s_1(D)\ge s_7(D+R)\ge1-\|E\|,
\]
which supplies the displayed physical shared anchor. The preliminary volume argument gives \(V_2\ge\kappa^2\), so failure of the paid \(V_3\) branch means \(V_3/V_2<\kappa\).

## Exact remaining gap

The shared coordinate \(h\) occurs on both sides of the bordered minor. The large interpolation defect is coefficient algebra, not a product-preserving random-variable separation. The separated Fourier theorem above therefore cannot yet be applied. An amplitude-agnostic extension is impossible: an arbitrary modulus-one amplitude \(G_t(h)=e^{-it(ah^2+bh+c)}\) cancels the scalar oscillation.

The next required implication is a **structure-sensitive shared-anchor weighted-Fourier receiver** for the displayed same-seed collar, or a direct small-ball/coarea substitute on the same branch.

Current status:
- \(s_8\): complete candidate \(<2400K^2/s\); two separate complete PASS reviews are now present (account03/B08 and account01/B03).
- \(s_7\): OPEN, reduced to the same-seed shared-anchor collar above.
- \(s_3\): OPEN.
- global continuity: OPEN.
