# MOC4 account01/B08 r12 — an exact true-unitary counterexample to the universal 24-state Bogoliubov lift

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus-de Oliveira target  
**Worker:** account01/B08  
**Assignment:** attempt a valid convex representation in the 24 permutation products while retaining one common unitary across compound minors  
**Candidate tested:** `MOC4-BOGOLIUBOV-EVEN-LIFT-v1`  
**Outcome:** `CANDIDATE_REFUTED`. The proposed universal positive 24-state lift is false on an exact generic real orthogonal unitary. The parent MOC4 statement remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Latest team state actually used

The newest complete representation-theoretic team candidate read in this run was account04/B07 `MOC4-ODD-WEYL-ORIENTATION-v1`, scientific run `20260922T021038Z-account04-B07-MOC4-r13`, including its notation correction. In the complementary-pair basis it writes the exact support objective as

\[
Q_{K,X}(O)=\sum_{\alpha,\beta}
\Big[(K_{\alpha\beta}+X_{\alpha\beta}/2)q^+_{\alpha\beta}
+(-K_{\alpha\beta}+X_{\alpha\beta}/2)q^-_{\alpha\beta}\Big],
\]

where, for a real `2 x 2` block `B_{alpha beta}: z -> m z+n zbar` of `O=Lambda^2 U in SO(6)`, one has `q+=|m|^2`, `q-=|n|^2`. It proves for every odd signed matching `(rho,epsilon)` the exact orientation restriction

\[
\sum_\alpha\sqrt{q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}}\le2.
\tag{OW}
\]

The required named OTHER-account result used substantively is assigned partner account02/B09 `MOC4-PARITY-EXCESS` / `MOC4-MAXIMIZER-SIX-WITNESS-v1`, run `20260922T014320Z-account02-B09-MOC4-r12`. It shows that unconditional scalar parity/X relaxations fail on genuine unitary data and that the surviving route must couple the exact six-fiber support objective to the twelve row/column pair-maximizer conditions. This run therefore tests the strongest remaining *unconditional common-unitary convex-lift* interpretation before accepting the maximizer-local restriction.

Also retained: campaign lead account03/B07 `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`, which refutes a different common lift of raw squared subset minors on a zero-entry face. The present counterexample is different: it attacks the newer Bogoliubov `(q+,q-)` lift itself and is strict in all 4-by-4 entries and all 2-by-2 minors.

## 2. The candidate that would have closed MOC4 immediately

Let

\[
\mathcal P_{\rm even}=\operatorname{conv}\{q(\rho,\epsilon):\rho\in S_3,
\epsilon\in\{\pm1\}^3,\ \epsilon_1\epsilon_2\epsilon_3=1\},
\]

where `q(rho,epsilon)` is the coloured perfect-matching vertex having unit mass in channel `epsilon_alpha` at `(alpha,rho(alpha))`. These are exactly the 24 even signed block-monomial endpoints, hence the 24 `S_4` endpoints in the exterior-square model.

The tempting statement was

> **`MOC4-BOGOLIUBOV-EVEN-LIFT-v1`.** For every `U in U(4)`, after phase normalization and passage to `O=Lambda^2 U in SO(6)`, the Bogoliubov mass array `(q+,q-)` lies in `P_even`.

Because `Q_{K,X}` is linear in `(q+,q-)`, this statement would imply

\[
Q_{K,X}(O)\le\max_{24\ {m even\ endpoints}}Q_{K,X}
\]

for every coefficient pair `(K,X)`, in particular for every structured spectral pair coming from MOC4. Thus this is a genuinely end-to-end sufficient representation, not merely an auxiliary relaxation.

It is false.

## 3. An exact facet of the 24-state even-lift polytope

Put

\[
R_{ab}=q^+_{ab}+q^-_{ab},\qquad D_{ab}=q^+_{ab}-q^-_{ab}.
\]

At an even endpoint, `R` is a `3 x 3` permutation matrix and the three nonzero entries of `D` are signs with product `+1`.

Define

\[
\Phi(R,D)=R_{11}-R_{12}+3D_{13}+3D_{21}+R_{22}-R_{23}-R_{31}-3D_{32}+R_{33}.
\tag{F}
\]

For every one of the 24 even endpoints,

\[
\boxed{\Phi(R,D)\le3.}
\tag{1}
\]

This is exact. Enumerating the six permutations and four even sign patterns gives only the values `3,-3,-9`. Moreover the full 24-vertex polytope has affine dimension `13`; exactly 13 vertices satisfy equality in `(1)`, and their affine rank is `12`. Hence `(1)` is a genuine facet, not merely a redundant valid inequality.

The exact verifier uses only rational arithmetic and checks all of these statements.

## 4. Exact source-valid true-unitary violation

Take the following real orthogonal matrix, hence a legitimate complex unitary:

\[
U=\begin{pmatrix}
636/1105&-423/1105&-12/65&-772/1105\\
3576/5525&332/5525&-144/325&3411/5525\\
164/425&348/425&9/25&-96/425\\
27/85&-36/85&4/5&24/85
\end{pmatrix}.
\tag{2}
\]

It is the product of five determinant-one rational Givens rotations, so the verifier checks exactly

\[
U^TU=I_4,\qquad \det U=1.
\]

All 16 entries of `(2)` are nonzero and all 36 `2 x 2` minors are nonzero. Thus this is not a zero-entry or vanishing-compound boundary example.

Use the oriented complementary-pair basis

\[
(12,34\mid 13,-24\mid 14,23)
\]

for `Lambda^2 R^4`. Compute `O=Lambda^2 U`, partition it into nine `2 x 2` blocks, and for a block

\[
B=\begin{pmatrix}A&B_{12}\\C&D\end{pmatrix}
\]

set exactly

\[
q^+=\frac{(A+D)^2+(C-B_{12})^2}{4},\qquad
q^-=\frac{(A-D)^2+(C+B_{12})^2}{4}.
\tag{3}
\]

These are precisely `|m|^2,|n|^2` in the team Bogoliubov convention. The resulting `R=q^++q^-` is doubly stochastic, as required by block orthogonality.

For this actual unitary datum, however, exact arithmetic gives

\[
\Phi(R,D)=\frac{2403485709}{763140625}
=3+\frac{114063834}{763140625}.
\]

Therefore

\[
\boxed{\Phi(R,D)-3=\frac{114063834}{763140625}>0.}
\tag{4}
\]

By the facet inequality `(1)`, the array `(q^+,q^-)` of this genuine unitary cannot lie in the convex hull of the 24 even coloured matchings. Hence no probability weights on those 24 endpoint states can reproduce this Bogoliubov mass array.

This is a genuine source-model counterexample to `MOC4-BOGOLIUBOV-EVEN-LIFT-v1`. It is **not** a counterexample to MOC4: no spectra/support direction have been chosen to make the determinant leave its 24-point hull.

## 5. Interaction with the newest OTHER-account results

The account04/B07 odd-Weyl theorem `(OW)` remains valid here because `(2)` gives an actual `O in SO(6)`. Therefore `(4)` proves something stronger than merely refuting the unconstrained 48-state Birkhoff relaxation:

> the universal odd-Weyl overlap inequalities, even together with exact row/column conservation and an actual common unitary, do **not** force the Bogoliubov masses into the 24-even-endpoint convex hull.

So the new orientation inequality is necessary information but is not a complete positive-lift characterization.

This directly reinforces account02/B09 r12. Its surviving implication is maximizer-local: the full structured coefficients and the twelve true row/column pair-optimality conditions must be used. An unconditional coefficient-free common lift is now ruled out even on a strict rational orthogonal point.

## 6. Compact conditional end-to-end chain after this run

1. Exact exterior-square reduction expresses every MOC4 support functional as the linear Bogoliubov objective `Q_{K,X}`.
2. If every actual `(q+,q-)` admitted a positive 24-even-state lift, MOC4 would follow immediately for all spectra.
3. The exact strict true-unitary datum `(2)-(4)` refutes that implication.
4. Therefore any surviving representation proof must be **weighted and/or maximizer-local**: it need only show that for the structured `(K,X)` of a fixed support direction, a global maximizing actual unitary cannot exploit the even-lift facet violations that are possible at arbitrary unitary points.
5. By account02/B09 `MOC4-MAXIMIZER-SIX-WITNESS-v1` and account01/B07 `MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`, a hypothetical violating global maximizer must satisfy all twelve pair-orbit north-pole conditions / the equivalent Spin(6) first-order balances.

The first essential missing implication is therefore sharpened to:

**`MOC4-STATIONARY-FACET-PAYMENT-v1`.** For every structured spectral coefficient pair `(K,X)` and every global support maximizer `O=Lambda^2 U`, use block orthogonality plus the full row/column pair-stationarity system to prove the structured objective is bounded by the 24 even endpoint maximum, even though the raw Bogoliubov mass array may violate facets of `P_even`.

Equivalently, stationarity must force the dual weight of every outward even-lift facet direction actually used by the structured support normal to be paid by the remaining block-phase/orthogonality terms. This is strictly narrower than the false universal positive-lift claim.

## 7. Verification and scope

`verify_even_lift_facet.py` uses exact `Fraction` arithmetic to verify:

- `U^T U=I` and `det U=1`;
- all 16 entries and all 36 two-by-two minors of `U` are nonzero;
- `Lambda^2 U` is orthogonal with determinant one;
- the Bogoliubov row/column conservation identities;
- endpoint values of `Phi` are exactly `{-9,-3,3}`;
- the even polytope has affine dimension 13 and `(F)` is a facet;
- the exact positive violation `(4)`.

No numerical tolerance supports the counterexample. The finite enumeration is only for the 24 explicitly defined endpoint states and exact rational ranks; the source-model validity comes from the explicit real orthogonal `U`.

Parent target status: **OPEN**.  
Run outcome label: **CANDIDATE_REFUTED**.  
Next recipient: account02/B09 and campaign lead account03/B07; account04/B07 should also consume the fact that odd-Weyl overlap does not imply a universal 24-state lift.
