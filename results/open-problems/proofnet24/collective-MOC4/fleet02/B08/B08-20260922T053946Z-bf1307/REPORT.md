# MOC4 fleet02/B08 — exact-four 2+2 boundary closure by EVC transversality

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** Marcus–de Oliveira inclusion for complex normal `4 x 4` pairs  
**Worker/run:** fleet02/B08, `B08-20260922T053946Z-bf1307`  
**Assigned scope:** repeated-eigenvalue and proper-common-block boundaries  
**Candidate:** `MOC4-2PLUS2-EVC-TRANSVERSAL-CLOSURE-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Fresh source state actually used

Fresh owner control revision `2026-09-22.2` keeps this slot on MOC4 and stops new installation/benchmark work.

The newest complete campaign-lead report read before this write is fleet03/B07 `20260922T055130Z-fleet03-B07-MOC4-r11`, blob `055492abce4a340ed49b4dbc44787461454c2b71`, candidate `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`. It derives the full genuine-unitary pair Hessian and leaves the flat-pair Gram-rigidity classification as the first boundary-facing implication. In particular a saturated pair sector has weighted traceless-Gram cancellations (its equations (6a)–(7)); the lead asks B08 to classify when that can force a proper block/circle boundary.

The named other-account partner result consumed and applied is fleet03/B09 `20260922T051640Z-fleet03-B09-moc4-external-facets`, blob `51b400736746d39fceb646d41b0566212cb492d8`, candidate `MOC4-SAXL-EXTERNAL-FACET-CLOSURE-v1`. It identifies Drury's `n=4` Saxl cone by the 24 evaluation facets plus 48 external facets and shows how membership closes a support direction for every true unitary. The present argument puts a large generic `2+2` boundary stratum into that cone by an explicit spectral deformation; it therefore pays all 48 external facets there at once rather than checking the two local gate inequalities separately.

The own immediately preceding result is `MOC4-COMMON-BLOCK-EDGE-PAYMENT-v1`. It proves exact one-cross-edge convexity and reduces each disjoint two-edge `2+2` gate to a scalar payment inequality. The current run changes mechanism: it uses the global `n=4` external-vertices theorem plus a local spectral submersion, not another unitary-gate expansion.

External theorem used: S. W. Drury, *The external vertices conjecture in case n=4*, Electron. J. Linear Algebra 11 (2004). Theorem 1.1 proves EVC for `n=4`; Corollary 1.2 gives the homogeneous consequence that when `0` is outside the convex hull of the 24 spectral permutation products, the determinant lies in the convex hull of outward radial multiples of those products. Only this proved `n=4` statement is used below.

## 2. Setup: a support-exposed generic `2+2` common block

Work in eigenbases for `A` and `B`. Let

\[
U_0=\operatorname{diag}(V,W),\qquad V,W\in U(2),
\]

be a proper `2+2` common reducing decomposition. Assume both blocks are nonmonomial, so the two `2 x 2` determinant formulas have coefficients strictly between zero and one. Write

\[
X_0=(a_1+b_1)(a_2+b_2),\qquad
X_1=(a_1+b_2)(a_2+b_1),
\]

\[
Y_0=(a_3+b_3)(a_4+b_4),\qquad
Y_1=(a_3+b_4)(a_4+b_3),
\]

and

\[
Z_{rs}=X_rY_s,\qquad r,s\in\{0,1\}.
\]

If `t,u in (0,1)` are the relevant squared moduli in `V,W`, then the exact block determinant is

\[
D(U_0)=\bigl(tX_0+(1-t)X_1\bigr)
       \bigl(uY_0+(1-u)Y_1\bigr),                         \tag{2.1}
\]

so `D(U_0)` is a convex combination of the four `Z_rs` with all four coefficients positive.

Fix a nonzero real support functional

\[
L(z)=\Re(\eta z),\qquad \eta\ne0,
\]

and let `M` be its maximum on all 24 permutation products. Assume:

1. `L(D(U_0))=M`;
2. the four block-preserving products `Z_rs` are exactly the four maximizing permutation products (the **exact-four face** hypothesis);
3. `a_1\ne a_2`, `b_1\ne b_2`, `a_3\ne a_4`, `b_3\ne b_4`;
4. all eight within-block cross sums `a_i+b_j` are nonzero.

By (2.1) and positivity of its four coefficients,

\[
L(Z_{00})=L(Z_{10})=L(Z_{01})=L(Z_{11})=M.                \tag{2.2}
\]

The other twenty endpoint inequalities are strict.

## 3. Zero-support lemma and the two local real ratios

### Lemma 3.1 — `MOC4-2PLUS2-ZERO-SUPPORT-v1`

Under the hypotheses above,

\[
r:=\frac{X_1}{X_0}\in\mathbb R\setminus\{0,1\},\qquad
s:=\frac{Y_1}{Y_0}\in\mathbb R\setminus\{0,1\},          \tag{3.1}
\]

and necessarily

\[
\boxed{M=0}.                                               \tag{3.2}
\]

#### Proof

The local differences are

\[
X_0-X_1=(a_1-a_2)(b_2-b_1)\ne0,
\]

\[
Y_0-Y_1=(a_3-a_4)(b_4-b_3)\ne0.                          \tag{3.3}
\]

Subtracting the two equalities in (2.2) with fixed first index gives

\[
L\bigl(X_0(Y_0-Y_1)\bigr)=L\bigl(X_1(Y_0-Y_1)\bigr)=0.
\]

Both arguments are nonzero. The kernel of a nonzero real-linear functional on `C` is a one-dimensional real line, hence their ratio `X_1/X_0` is real. Reversing the two blocks gives `Y_1/Y_0 in R`. Nonzero cross sums imply `r,s` are nonzero, and (3.3) implies neither is `1`.

Thus all four `Z_rs` lie on the real line through `Z_00`. At least `Z_00` and `Z_10=rZ_00` are distinct. Since `L` takes the same value on these two distinct points of a one-dimensional real subspace, `L` vanishes on that subspace. Hence their common value is zero, proving (3.2). `QED`

This is the support-form version of the earlier local-circle classification: each local signed quartet has a real cross ratio and therefore lies on a generalized circle. The important extra conclusion here is that an exact-four exposed `2+2` face is a **through-origin zero-support face**.

## 4. The local product map is a complex submersion

For the first block define

\[
\Phi(a_1,a_2,b_1,b_2)=(X_0,X_1)\in\mathbb C^2.            \tag{4.1}
\]

### Lemma 4.1 — `MOC4-LOCAL-PRODUCT-SUBMERSION-v1`

If `a_1\ne a_2` and all four first-block cross sums are nonzero, then the complex Jacobian of `Phi` has rank two.

#### Proof

With `p_ij=a_i+b_j`, two `2 x 2` Jacobian minors are

\[
\det J_{(a_1,b_2)}
=-p_{21}(a_1-a_2+b_1-b_2),                                \tag{4.2}
\]

\[
\det J_{(a_1,b_1)}
= p_{22}(a_1-a_2-b_1+b_2).                                \tag{4.3}
\]

If the rank were below two, both minors would vanish. Since `p_21,p_22` are nonzero, the two parenthesized quantities would both be zero. Adding them gives `2(a_1-a_2)=0`, contradiction. `QED`

The same statement holds for `(Y_0,Y_1)`. By the holomorphic submersion theorem, every sufficiently small independent perturbation of the pair `(X_0,X_1)` (respectively `(Y_0,Y_1)`) is realized by a sufficiently small perturbation of the corresponding four spectral points. This is a spectral, hence source-valid, deformation; no bistochastic or independent-minor surrogate appears.

## 5. Main theorem: three of the four sign chambers are globally support-safe

Call the exact-four face **double-interlacing** when

\[
r<0\quad\text{and}\quad s<0.                            \tag{5.1}
\]

### Theorem 5.1 — `MOC4-2PLUS2-EVC-TRANSVERSAL-CLOSURE-v1`

Under the hypotheses of section 2, if the face is **not** double-interlacing, i.e.

\[
\boxed{r>0\ \text{or}\ s>0},                             \tag{5.2}
\]

then the support inequality is valid for **every** true unitary coupling:

\[
\boxed{
L\!\left(\det(D_a+UD_bU^*)\right)\le M=0
\quad\text{for every }U\in U(4).
}                                                           \tag{5.3}
\]

Thus such an exact-four exposed common-block face cannot be a support direction of an MOC4 counterexample.

#### Proof

Choose `kappa in C\{0}` with

\[
\kappa^4=-\eta
\]

and replace every spectral point by `kappa` times itself. This preserves the real ratios `r,s`. For the normalized permutation products `w_sigma` we now have

\[
\Re w_\sigma=-L(z_\sigma)\ge0.                            \tag{5.4}
\]

The twenty products outside the exact-four face have strictly positive real part, while the four face products have zero real part. Since they are nonzero, write

\[
w_{00}=ic,\qquad c\in\mathbb R\setminus\{0\},
\]

so

\[
w_{10}=irc,\qquad w_{01}=isc,\qquad w_{11}=irsc.         \tag{5.5}
\]

We construct nearby spectra for which **all 24** normalized permutation products have positive real part.

**Case 1: `r>0` and `s>0`.** All four values in (5.5) lie on the same open imaginary ray. Multiply every normalized spectral point by a fourth root of

\[
e^{-i\operatorname{sgn}(c)\varepsilon},
\]

with `epsilon>0` small. Every fourfold permutation product is therefore multiplied by that displayed phase. The four formerly imaginary face products move into the open right half-plane. By continuity the twenty already-strict products remain in the open right half-plane.

**Case 2: `r<0` and `s>0`.** The two products in row `r=0` of (5.5) have one imaginary sign and the two products in row `r=1` have the opposite sign. By Lemma 4.1, for every sufficiently small `epsilon>0` there are nearby first-block spectral points whose local products satisfy

\[
X_0(\varepsilon)=e^{-i\operatorname{sgn}(c)\varepsilon}X_0,
\qquad
X_1(\varepsilon)=e^{+i\operatorname{sgn}(c)\varepsilon}X_1. \tag{5.6}
\]

Keep the second block fixed. Equation (5.6) rotates both products in the first row of (5.5) toward the open right half-plane and both products in the second row toward the open right half-plane. Again the other twenty endpoint real parts stay positive for small enough `epsilon` by strictness and continuity.

**Case 3: `r>0` and `s<0`.** Apply the identical submersion argument to `(Y_0,Y_1)`.

We have therefore obtained normalized spectra `(a^(epsilon),b^(epsilon))` converging to the original normalized spectra such that

\[
\Re\prod_i(a_i^{(\varepsilon)}+b_{\sigma(i)}^{(\varepsilon)})>0
\qquad\text{for all }\sigma\in S_4.                       \tag{5.7}
\]

For each `epsilon`, `0` is outside the convex hull of the 24 products. Drury's proved `n=4` external-vertices theorem (equivalently its Corollary 1.2) gives, for every true unitary `U`,

\[
\Re\det(D_{a^{(\varepsilon)}}+U D_{b^{(\varepsilon)}}U^*)>0. \tag{5.8}
\]

Fix `U` and let `epsilon` tend to zero. Determinants depend continuously on the spectra, so

\[
\Re\bigl((-\eta)\det(D_a+UD_bU^*)\bigr)\ge0,
\]

which is exactly (5.3). `QED`

### Partner-coordinate interpretation

In fleet03/B09's `MOC4-SAXL-EXTERNAL-FACET-CLOSURE-v1` language, (5.7) puts each perturbed spectral endpoint functional in the proved `n=4` EVC/Saxl cone. That cone is the intersection of its 24 evaluation halfspaces and 48 external halfspaces, hence it is closed. The limit endpoint functional therefore lies in the same cone. Consequently **all 48 external-facet payments are automatically satisfied** on the stratum of Theorem 5.1. This is the named partner result applied to the boundary problem, not merely cited.

It also implies both disjoint two-edge payment inequalities from the preceding B08 run on this stratum, because failure of either payment would generate an actual true-unitary local support violation, contradicting (5.3).

## 6. Why the double-interlacing chamber is a genuine residual

The same first-order deformation cannot pay the fourth sign chamber for a structural reason.

Suppose `r<0,s<0`. Then the signs of the four imaginary products in (5.5) are checkerboard. For an arbitrary differentiable spectral deformation with all four local products nonzero, write logarithmic first variations

\[
\frac{X_r'}{X_r}=\alpha_r,\qquad
\frac{Y_s'}{Y_s}=\beta_s.
\]

Then

\[
\frac{Z_{rs}'}{Z_{rs}}=\alpha_r+\beta_s.                 \tag{6.1}
\]

Only the imaginary parts of these logarithmic variations contribute to the first-order real part of a purely imaginary `Z_rs`. After possibly reversing the common sign, strict inward motion of all four checkerboard entries would require real numbers `x_r,y_s` satisfying

\[
x_0+y_0<0,\qquad x_0+y_1>0,
\]

\[
x_1+y_0>0,\qquad x_1+y_1<0.                              \tag{6.2}
\]

But the sum of the two left-column/diagonal expressions in the first and fourth inequalities is the same number

\[
x_0+x_1+y_0+y_1
\]

as the sum of the middle two expressions, so (6.2) is impossible. Hence:

> **No first-order spectral deformation can move all four double-interlacing face products strictly into the same open support half-plane.**

This is not a counterexample to MOC4. A second-order or nonlocal mechanism may still close the chamber. It does show that Theorem 5.1 has reached the first honest obstruction of this deformation method rather than stopping at a bookkeeping boundary.

## 7. Sharpened all-pairs boundary reduction

Combining the earlier B08 boundary theorems with Theorem 5.1 gives the following source-valid reduction for the boundary side of the campaign.

1. Every repeated-spectrum pair is already solved exactly by the B08 fractional-orientation/minimal-lift theorem; singular cases were included there.
2. Every proper common-reducing-block pair is solved exactly by the blockwise `n<=3` representation.
3. Noncollinear support-positive solved faces have an ordinary interior collar.
4. Generic collinear repeated faces are exactly the common-generalized-circle locus and are solved globally by the Möbius-to-Hermitian theorem.
5. A generic support-exposed `2+2` common-block face with exactly its four block-preserving endpoint products tied is now globally support-safe unless **both** local permutation ratios are negative.

Therefore a counterexample sequence approaching a `2+2` common-block boundary can only survive this B08 reduction through one of the following explicit lower-dimensional/structured strata:

- **double-interlacing:** `X_1/X_0<0` and `Y_1/Y_0<0`;
- **enlarged exposed face:** at least one additional off-block permutation product is also support-tied;
- **zero-factor degeneration:** a within-block cross sum vanishes;
- **additional spectral repetition**, which falls back into the already solved repeated-spectrum theorem.

The separate exposed `1+3` common-block line/tangent problem from the earlier circle-face run also remains. Nothing here claims a collar for that branch.

This interfaces directly with the newest lead's flat-pair Gram-rigidity theorem: if a lead flat-pair degeneration lands on a generic exact-four `2+2` common block and is not double-interlacing, Theorem 5.1 closes that support direction outright. The lead's boundary classification can therefore restrict its `2+2` branch to the four residual strata above.

## 8. First next implication

The next named B08 implication is

**`MOC4-2PLUS2-DOUBLE-INTERLACING-v1` (OPEN).** For a true support-exposed `2+2` common-block boundary with simple local spectra, nonzero local cross sums, exactly four tied block-preserving endpoints, and

\[
X_1/X_0<0,\qquad Y_1/Y_0<0,
\]

prove the support inequality for all true unitary couplings, or construct an actual normal `4 x 4` counterexample.

The first-order additive-phase obstruction (6.2) rules out merely repeating the present deformation. A genuinely different next mechanism should use one of: second-order spectral curvature tied to the lead's mixed Hessian gate, or B09's external-facet/spinor identities on this checkerboard face.

## 9. Computation, failures, and status

No numerical or finite computational output is used as evidence for any theorem in this report. The proof is algebraic plus the published `n=4` external-vertices theorem. Exploratory scratch calculations, where performed, were not relied upon and are not promoted to evidence.

A tempting shortcut—`24` pointwise endpoint inequalities alone imply membership in the relevant Saxl cone—is invalid as a general linear statement: the named B09 result exhibits the additional `48` external facets. The present proof avoids that false relaxation by staying in the genuine spectral-product family and using Drury's theorem before taking a closed-cone limit.

**Target status:** full MOC4 remains **OPEN**.  
**Run status:** `ESSENTIAL_STEP_APPLIED`.  
**New proved source-level items:** zero-support lemma; local-product submersion; global support closure of all generic exact-four `2+2` exposed faces outside the double-interlacing chamber; first-order obstruction identifying the honest residual.  
**No full-proof candidate is claimed.**
