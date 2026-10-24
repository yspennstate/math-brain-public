# MOC4 account03/B20 — facet-normal reduction for the one-cycle SU(2) payment

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira target  
**Worker:** account03/B20  
**Run:** `20260922T035059Z-account03-B20-moc4-r14`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and completed inputs consumed

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{
 v_\sigma:=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}
\]

for every complex normal 4-by-4 pair, including singular and repeated-spectrum cases.

This run directly uses two completed results.

1. **account03/B08, `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`**, report `proofnet24/collective-MOC4/account03/B08/20260922T031831Z-a03-b08-moc4-r11/REPORT.md`. For the path word
   \(U_0=R_{12}R_{23}R_{34}\) followed by a full closing `SU(2)` gate on columns `1,4`, the determinant image is exactly the filled ellipse
   \[
   E=\left\{\frac{D_0+D_1}{2}+x\frac{D_0-D_1}{2}+yK:x^2+y^2\le1\right\},
   \tag{1}
   \]
   where
   \[
   K=c_1s_1s_2s_3\,(v_{4123}-v_{1423}),
   \tag{2}
   \]
   and both forest endpoints `D0,D1` already have honest 24-vertex probability lifts. In a real-linear direction `L`, if `M=max_sigma L(v_sigma)`, `delta_j=M-L(D_j)` and `C=L(K)`, the whole ellipse is safe in that direction exactly when
   \[
   C^2\le\delta_0\delta_1.\tag{3}
   \]
2. **Assigned partner account04/B09, `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`**, report `proofnet24/collective-MOC4/account04/B09/20260922T022417Z-b09-moc4-r11/REPORT.md`. Haar averaging a genuine row/column pair `SU(2)` orbit gives an exact 24-permutation lift of the complete exterior-minor data. Hence a flat pair orbit cannot be support-violating. This is used below to keep the remaining one-cycle obstruction on the genuine pair-strict branch rather than on an artificial bistochastic relaxation.

The previous B20 run obtained unconditional pair-twirl two-point inequalities and a quantitative pair-curvature collar. The present run changes mechanism: it attacks B08's exact cyclic ellipse directly as a convex-body containment problem.

## 2. New theorem: only target-hull facet directions need be checked

Let

\[
H=\operatorname{conv}\{v_\sigma:\sigma\in S_4\}\subset\mathbb C\cong\mathbb R^2
\]

and assume first that `H` is two-dimensional. Let its exposed edges be `e`. For an edge with endpoints `v_sigma,v_tau`, choose any outward real-linear functional `L_e` such that

\[
M_e=L_e(v_\sigma)=L_e(v_\tau)=\max_\pi L_e(v_\pi).
\]

Put

\[
\delta_{0,e}=M_e-L_e(D_0),\qquad
\delta_{1,e}=M_e-L_e(D_1),\qquad
C_e=L_e(K).
\]

### `MOC4-ONE-CYCLE-FACET-REDUCTION-v1`

For the exact one-cycle ellipse `(1)`,

\[
\boxed{
E\subseteq H
\quad\Longleftrightarrow\quad
C_e^2\le\delta_{0,e}\delta_{1,e}
\text{ for every exposed edge }e\text{ of }H.
}
\tag{4}
\]

In particular, if this one-cycle family ever gives a genuine MOC4 counterexample, then there is already a separating direction in which **at least two permutation products tie for the target maximum**. The continuum of arbitrary support directions is unnecessary: for fixed spectra one checks at most the number of polygon facets, hence at most 24 inequalities.

### Proof

A planar convex polygon is the intersection of its facet halfspaces:

\[
H=\bigcap_e\{z:L_e(z)\le M_e\}.
\tag{5}
\]

The support of the ellipse `(1)` in direction `L_e` is

\[
\max_{z\in E}L_e(z)
=\frac{L_e(D_0)+L_e(D_1)}2
+\sqrt{\left(\frac{L_e(D_0)-L_e(D_1)}2\right)^2+C_e^2}.
\tag{6}
\]

Because `D0,D1` are already in `H`, both `delta_{0,e},delta_{1,e}` are nonnegative. Therefore the halfspace condition `max_E L_e <= M_e` is equivalent to

\[
\frac{\delta_{0,e}+\delta_{1,e}}2
\ge
\sqrt{\left(\frac{\delta_{0,e}-\delta_{1,e}}2\right)^2+C_e^2}.
\]

Both sides are nonnegative, so squaring is lossless and gives precisely

\[
\delta_{0,e}\delta_{1,e}\ge C_e^2.
\]

Combining with `(5)` proves `(4)`. QED.

A strict counterexample on a degenerate spectral hull persists under sufficiently small generic perturbation of the spectra/support data, so for contradiction/search purposes the two-dimensional reduction loses no strict violation. Degenerate segment/point cases can also be checked directly in their affine hull; no degenerate case is being declared solved here merely from genericity.

## 3. Direction-free cross-ratio form on a candidate facet

The tie itself removes the support-direction variable. Let

\[
\Delta_{\sigma\tau}=v_\sigma-v_\tau\ne0.
\]

A normal to the edge is represented, up to a nonzero real scale and orientation, by multiplication with `i/Delta_{sigma tau}`. Consequently `(4)` on that edge is equivalent to

\[
\boxed{
\operatorname{Im}\!\left(\frac{v_\sigma-D_0}{\Delta_{\sigma\tau}}\right)
\operatorname{Im}\!\left(\frac{v_\sigma-D_1}{\Delta_{\sigma\tau}}\right)
\ge
\operatorname{Im}\!\left(\frac{K}{\Delta_{\sigma\tau}}\right)^2,
}
\tag{7}
\]

with the edge orientation chosen so the two left factors have the same nonnegative facet-deficit sign. The product and square are invariant under reversing the normal.

Thus `MOC4-ONE-CYCLE-PAYMENT-v2` can be attacked as finitely many algebraic edge-pair inequalities rather than an arbitrary-angle optimization. This is the first unpaid universal step produced by this run.

## 4. Exact full-ellipse certificate for B08's near-saturation datum

Apply `(4)` to B08's exact near-saturation data

\[
a=(10-13i,-18+17i,-20+5i,-20+11i),
\]
\[
b=(17-18i,-22+3i,-19-7i,2+7i),
\]

with

\[
(c_1,s_1)=(3/5,4/5),\qquad
(c_2,s_2)=(c_3,s_3)=(7/25,24/25).
\]

Exact integer/Fraction arithmetic gives a nine-vertex target hull, in counterclockwise order,

\[
4213,\ 2143,\ 2134,\ 2431,\ 2413,\ 1423,\ 1432,\ 1234,\ 1243.
\tag{8}
\]

All nine facet-payment inequalities `(4)` are **strictly positive**. Therefore, for these spectra and the first three Givens gates,

\[
\boxed{E\subset H}
\]

for the **entire closing SU(2) gate**, including every complex closing phase and every mixing angle. This is stronger than checking only the previously selected support direction or one rational final rotation.

The closest facet is the edge `4213--2143`. One exact outward normal is

\[
n=(110388,-311628).
\]

For that facet,

\[
\delta_0=rac{1415020501782005184}{9765625},\qquad
\delta_1=rac{2204750924271689664}{9765625},
\]
\[
C=rac{562286043316224}{3125},
\]

and the exact payment margin is

\[
\boxed{
\delta_0\delta_1-C^2
=
\frac{32213125297983477483140165687218176}{95367431640625}>0.
}
\tag{9}
\]

Equivalently,

\[
\frac{C^2}{\delta_0\delta_1}
=
\frac{27918426593870104014720000000000}
{28209705576960955771475824704203}
\approx0.9896745117634712.
\tag{10}
\]

So the source-valid example is even closer to failure on an actual hull facet than in B08's original unique-vertex direction, but it still has a fully exact all-phase/all-angle containment certificate.

## 5. Application of the assigned partner result

`MOC4-FLAT-PAIR-TWIRL-LIFT-v1` eliminates the flat-pair branch exactly. Combining it with `(4)` gives a sharper search/proof target for this one-cycle mechanism:

- a true violation need only be sought at an exposed **target-hull facet normal**, hence at a two-vertex tie;
- at the violating point the closing pair orbit must be **strict**, because a flat pair orbit is already in the permutation hull after the partner's exact Haar twirl;
- arbitrary bistochastic or common-minor proxy data are irrelevant: every quantity in `(4)` and `(7)` comes from the actual spectral vertices and the actual true-unitary one-cycle ellipse.

This reduces both nuisance dimensions that were previously present: arbitrary support angle and pair-flat degeneracy.

## 6. Updated conditional chain and next exact obligation

The one-cycle branch now has the following complete conditional chain.

1. The two forest endpoints `D0,D1` have exact 24-vertex lifts.
2. B08 gives the exact genuine-unitary ellipse `(1)` for the closing `SU(2)` gate.
3. This run reduces ellipse containment to the finite set of target-hull facet inequalities `(4)`, equivalently the direction-free edge formulas `(7)`.
4. Assigned partner account04/B09 removes the flat-pair possibility, so only strict edge-normal payment failure could produce a counterexample.

The first unpaid implication is therefore:

> **`MOC4-ONE-CYCLE-FACET-PAYMENT-v1`.** For every complex spectra and every real first-three Givens parameters, prove `(7)` for every pair of permutation products that forms an exposed edge of the spectral hull.

A strict failure of `(7)` on a genuine exposed edge would immediately give a true-unitary MOC4 counterexample through B08's ellipse theorem. A proof for every exposed edge would close the entire one-use four-cycle `SU(2)` family. The next algebraic attack should exploit the tie relation `Re(eta(v_sigma-v_tau))=0` and classify the relative permutation type of exposed pairs, rather than returning to unrestricted direction sweeps or the already-refuted parity/common-lift gates.

Full MOC4 remains **OPEN**.

## 7. Verification and non-claims

`verify_one_cycle_facets.py` reconstructs the 24 exact Gaussian-integer vertices, the two exact forest lifts, `D0,D1,K`, computes the exact convex hull, derives all outward facet normals, and verifies every payment inequality using `fractions.Fraction`. It exits with `PASS MOC4-ONE-CYCLE-FACET-CERTIFICATE-v1`.

This run does not claim worldwide novelty or a full MOC4 proof. No arbitrary bistochastic surrogate, floating tolerance, benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API/Codex call, remote workflow, or permission bypass is used.
