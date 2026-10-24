# MOC4 account02/B08 — Möbius circle reduction, repeated-face classification, and an exposed 2+2 boundary witness

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Worker:** account02/B08  
**Run:** `B08-20260922T033842Z-c41e2a`  
**Candidate:** `MOC4-CIRCLE-FACE-REDUCTION-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact inherited state

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for every complex normal `4 x 4` pair `A,B`, including singular and repeated-spectrum cases.

Fresh owner control is revision `2026-09-22.2`; it stops installation/benchmark work and keeps account02/B08 on the repeated-eigenvalue/common-block MOC4 boundary.

The exact completed dependencies used here are:

1. **Campaign lead account03/B07**, latest complete run available at the source snapshot: `20260922T013930Z-account03-B07-MOC4-r11`, `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`. It gives a genuine orthogonal zero-entry counterexample to the proposed common second-compound permutation lift. Therefore nothing below assumes such a lift.
2. **Named partner account03/B09**, latest complete run available at the source snapshot: `20260922T024834Z-account03-B09-moc4-r11`, report blob `aae26d4d72c3ca5b06d5ef06cff44b3c6ebd9a7d`, result `MOC4-ODD-TWIST-MASS-v1`. It proves 16 true-unitary `SO(6)` odd-twist mass inequalities and an exact rational dual certificate on a hard generic structured support datum.
3. **This worker's preceding result**, `MOC4-BOUNDARY-SUPPORT-FACE-REDUCTION-v3`, report blob `34af548e5db7f7437624a04f8a725ad0bd916ff9`. It proves: every repeated-spectrum pair has an exact fractional-orientation representation; the exact support is determined by Hall-tight cuts; every proper common reducing decomposition has a support-positive exact blockwise representation; and noncollinear supported boundary faces have an ordinary interior collar.
4. **Hermitian base case.** The 2025 survey by Bebiano–da Providência states Fiedler's theorem for Hermitian `A,B`; Drury's 2004 paper still records unrestricted `n=4` as open. A bounded current-status search also found no source-matching full `n=4` resolution; this is a status check, not a novelty claim.

The previous first unpaid boundary implication was `MOC4-COLLINEAR-BOUNDARY-v1`. This run attacks that implication directly.

## 2. Compact conditional all-pairs reduction after this run

The surviving chain is now sharper.

1. Repeated-spectrum pairs are solved exactly by the preceding minimal lift. Proper common-reducing-block pairs are solved exactly by the preceding blockwise representation.
2. If the positive supported boundary vertices are not collinear, the determinant is an ordinary interior point of the full permutation hull and continuity gives a genuine open collar.
3. If the support is collinear, section 3 below first replaces the crude condition "collinear" by an **exposed-face** condition: a boundary point can matter only when all positively supported vertices lie on one exposed line of the full 24-vertex hull.
4. On a fully supported generic repeated face `a_1=a_2`, section 5 proves that collinearity is **equivalent** to one spectral condition: all seven signed spectral points
   \[
   -a_1=-a_2,\ -a_3,\ -a_4,\ b_1,b_2,b_3,b_4
   \]
   lie on one generalized circle. Section 4 proves MOC exactly for *every* normal pair, in every dimension, whose signed spectra lie on one generalized circle, by a Möbius reduction to Fiedler's Hermitian theorem.
5. Thus a counterexample sequence can approach a Hall-interior repeated face only through one of the explicit lower-dimensional strata: a unitary support degeneration (tight Hall cut or vanished designated pair minor), an additional spectral/cross-sum degeneration, or a **transverse departure from the common-circle spectral locus**. The vague collinear branch is gone on the generic repeated stratum.
6. For a generic `2+2` common block, section 6 classifies collinearity by two local generalized circles. If the two circles coincide, section 4 closes the whole pair. However section 7 gives an exact true-unitary example where the circles are different and the block-preserving line is genuinely exposed in the full 24-vertex hull. Hence the stronger attempted implication "exposed `2+2` line forces one global circle" is false.
7. After the opposite-scalar gauge, any residual counterexample may still be taken simple-spectrum, individually invertible and irreducible. On that generic core the named partner's `MOC4-ODD-TWIST-MASS-v1` inequalities are valid true-unitary constraints and must be imposed before any relaxation; the boundary work here removes only escape routes into solved faces and does not replace that generic mechanism.

The next boundary-specific implication is therefore narrower and genuinely tangent-level: control perturbations **transverse to the common-circle repeated face**, together with exposed mismatched-circle `2+2` and the remaining exposed `1+3` block lines.

## 3. General exposed-face lemma for any support-positive boundary representation

Let `H=conv{v_sigma:sigma in S_4}` and suppose a solved boundary mechanism gives

\[
x=\sum_{\sigma\in\Omega}\mu_\sigma v_\sigma,
\qquad \mu_\sigma>0,\quad \sum\mu_\sigma=1.\tag{1}
\]

If `x` lies on the boundary of `H`, choose a nonzero real support functional `L(z)=Re(eta z)` with

\[
L(x)=\max_{y\in H}L(y)=h.
\]

Every `v_sigma` satisfies `L(v_sigma)<=h`; averaging in (1) gives equality. Because every coefficient in (1) is strictly positive,

\[
\boxed{L(v_\sigma)=h\quad\text{for every }\sigma\in\Omega.}\tag{2}
\]

Therefore a collinear supported set is harmless whenever its line is not a supporting line of the **full** permutation hull: in that case `x` is an ordinary interior point and the previous continuity collar applies. Only an exposed supported line can remain boundary-critical.

This observation is elementary but removes many false collinear alarms and is used below.

## 4. New exact lemma: common generalized-circle spectra reduce to Hermitian MOC

Write

\[
X=-A,\qquad Y=B,
\]

so that the target is `det(Y-X)` and the permutation vertices are

\[
\prod_i(y_{\sigma(i)}-x_i).
\]

### Theorem 1 — `MOC-COMMON-CIRCLE-v1`

Let `X,Y` be normal `n x n` matrices. If the finite set

\[
\sigma(X)\cup\sigma(Y)
\]

lies on one generalized circle (a Euclidean circle or line in the Riemann sphere), then

\[
\det(Y-X)\in\operatorname{conv}\left\{\prod_i(y_{\sigma(i)}-x_i):\sigma\in S_n\right\}.
\tag{3}
\]

Thus the Marcus–de Oliveira inclusion holds for `(A,B)` whenever `sigma(-A) union sigma(B)` lies on one generalized circle.

### Proof

Choose a Möbius map

\[
\phi(z)=\frac{\alpha z+\beta}{\gamma z+\delta},
\qquad \Delta=\alpha\delta-\beta\gamma\ne0,
\]

that maps the generalized circle to the extended real line and whose pole is not one of the finitely many spectral points. Then `gamma X+delta I` and `gamma Y+delta I` are invertible, and normal functional calculus gives Hermitian matrices

\[
X'=\phi(X),\qquad Y'=\phi(Y),
\]

because all their eigenvalues are real.

A direct noncommutative calculation gives

\[
(\gamma Y+\delta I)(Y'-X')(\gamma X+\delta I)
=\Delta(Y-X).\tag{4}
\]

Indeed, after multiplying out the two rational expressions, the `YX` terms cancel without assuming that `X` and `Y` commute. Taking determinants yields

\[
\det(Y-X)=K\det(Y'-X'),\tag{5}
\]

where

\[
K=\frac{\det(\gamma Y+\delta I)\det(\gamma X+\delta I)}{\Delta^n}\ne0.
\tag{6}
\]

For scalar spectral points the same Möbius difference identity gives

\[
y_j-x_i
=\frac{(\gamma y_j+\delta)(\gamma x_i+\delta)}{\Delta}
\bigl(\phi(y_j)-\phi(x_i)\bigr).
\]

Hence for every permutation `sigma`, because each `y_j` occurs exactly once,

\[
\prod_i(y_{\sigma(i)}-x_i)
=K\prod_i\bigl(\phi(y_{\sigma(i)})-\phi(x_i)\bigr).
\tag{7}
\]

Apply Fiedler's Hermitian case to the Hermitian pair `Y'` and `-X'`:

\[
\det(Y'-X')\in
\operatorname{conv}\left\{\prod_i(\phi(y_{\sigma(i)})-\phi(x_i))\right\}.
\]

Multiplication by the fixed nonzero complex number `K` maps this convex hull exactly to the original one by (7), and (5) maps the determinant to the same scale. This proves (3). `QED`

No nonsingularity of `Y-X` is required. The only chosen pole is outside a finite spectral set.

## 5. Generic repeated face: collinearity if and only if the signed spectra are concyclic

Assume

\[
a_1=a_2=\alpha,
\qquad a_3=c,
\qquad a_4=d,
\]

with `c,d` distinct from `alpha`, `b_1,...,b_4` distinct, and no cross-sum

\[
\alpha+b_j,\quad c+b_j,\quad d+b_j
\]

vanishing. Assume also that the repeated-face orientation is on its full-support stratum: all designated weights `r_{jk}>0` and no Hall cut is tight. By the preceding B08 theorem every directed edge is then admissible, so the determinant has a representation positive on all 24 permutations (12 distinct vertex values because rows 1 and 2 have equal eigenvalue).

For ordered `j != k`, let `{l,m}` be the complementary pair and define the corresponding distinct vertex value

\[
V_{jk}=(\alpha+b_l)(\alpha+b_m)(c+b_j)(d+b_k).\tag{8}
\]

Put

\[
q_j=\alpha+b_j,\qquad
s=c-\alpha,\qquad t=d-\alpha,\qquad
Q=\prod_{r=1}^4q_r,
\]

and

\[
R_j=1+\frac{s}{q_j}=\frac{c+b_j}{\alpha+b_j},
\qquad
S_j=1+\frac{t}{q_j}=\frac{d+b_j}{\alpha+b_j}.
\]

Then

\[
\boxed{V_{jk}=Q R_jS_k.}\tag{9}
\]

### Theorem 2 — `MOC4-REPEATED-CIRCLE-CLASSIFICATION-v1`

Under the generic hypotheses above, the following are equivalent:

1. the 12 values `V_{jk}`, `j != k`, are collinear in `C`;
2. they lie on a real line through the origin;
3. the seven distinct signed spectral points
   \[
   -\alpha,-c,-d,b_1,b_2,b_3,b_4
   \]
   lie on one generalized circle.

### Proof: (1) implies (2) and (3)

If the values are collinear, there are `eta != 0` and a real constant `h` with

\[
\operatorname{Re}(\eta Q R_jS_k)=h\qquad(j\ne k).\tag{10}
\]

Fix distinct `k,k'`. There are exactly two indices `r,s` outside `{k,k'}`. Subtracting (10) for `k` and `k'` gives

\[
\operatorname{Re}\!\left(\eta Q R_r\,t\left(\frac1{q_k}-\frac1{q_{k'}}\right)\right)=0
\]

and the same equation with `R_s`. The factor

\[
t\left(\frac1{q_k}-\frac1{q_{k'}}\right)
\]

is nonzero because `t != 0` and the `b_j` are distinct. The real kernel of `z -> Re(z w)` for a fixed nonzero complex `w` is a one-dimensional real line. Hence `R_r/R_s` is real. Since every pair `{r,s}` arises as the complement of some `{k,k'}`, all ratios

\[
R_j/R_k\in\mathbb R.\tag{11}
\]

The nonvanishing cross-sum hypothesis makes every `R_j` nonzero. By the same argument with the roles of `j` and `k` exchanged,

\[
S_j/S_k\in\mathbb R.\tag{12}
\]

Thus all `R_j` share one complex phase and all `S_k` share another; (9) shows all `V_{jk}` lie on one line through zero. This proves (2).

Moreover (11) says

\[
\frac{(c+b_j)(\alpha+b_k)}{(\alpha+b_j)(c+b_k)}\in\mathbb R.\tag{13}
\]

The left-hand side is the cross ratio of `-c,-alpha,b_j,b_k` up to the standard harmless ordering convention. Therefore `-c,-alpha,b_j,b_k` lie on one generalized circle. Varying `j,k` shows that `-c,-alpha,b_1,...,b_4` lie on a common generalized circle. Equation (12) similarly places `-d,-alpha,b_1,...,b_4` on a generalized circle. Two distinct generalized circles cannot share the four distinct points `b_1,...,b_4`, so they are the same circle. This proves (3).

### Proof: (3) implies (2)

If all seven points lie on one generalized circle, each cross ratio in (13) is real, so all `R_j` share one phase. The analogous cross ratios for `d` show all `S_j` share one phase. Equation (9) then places all `V_{jk}` on one line through zero. `QED`

### Boundary consequence

On the Hall-full repeated stratum the previous residual "supported products are collinear" is therefore **exactly** the common-generalized-circle spectral locus, apart from the explicitly excluded lower-dimensional cross-sum/additional-repeat strata. Theorem 1 solves that exact locus. What remains for an all-pairs collar is only perturbation **transverse** to it, not an unidentified collinear geometry.

The generalized-circle **line** subcase reduces, after the same opposite shift/scaling, to the known Hermitian case. The proper-circle subcase is handled by Theorem 1's Möbius determinant identity, not by pretending the matrices are Hermitian in their original coordinates.

## 6. Generic `2+2` common block: exact local-circle classification

Suppose the signed spectra are partitioned compatibly into two `2 x 2` common blocks. Write the two local permutation products as

\[
X_0=(a_1+b_1)(a_2+b_2),\qquad
X_1=(a_1+b_2)(a_2+b_1),
\]

\[
Y_0=(a_3+b_3)(a_4+b_4),\qquad
Y_1=(a_3+b_4)(a_4+b_3).
\]

Assume these four local numbers are nonzero and `X_0 != X_1`, `Y_0 != Y_1`; equalities are the expected local repeat degeneracies. The block-preserving global vertices are

\[
X_0Y_0,\ X_0Y_1,\ X_1Y_0,\ X_1Y_1.\tag{14}
\]

### Lemma 3 — product-grid collinearity

The four values in (14) are collinear if and only if

\[
X_1/X_0\in\mathbb R,
\qquad
Y_1/Y_0\in\mathbb R.\tag{15}
\]

Indeed scale (14) by `1/(X_0Y_0)` and put `r=X_1/X_0`, `s=Y_1/Y_0`. The points are `1,r,s,rs`. If they are collinear, then

\[
\frac{r-1}{s-1}\in\mathbb R,
\qquad
\frac{rs-1}{s-1}=r+\frac{r-1}{s-1}\in\mathbb R.
\]

Since `r != 1`, `s != 1`, this forces first `r` and then `s` to be real. The converse is immediate.

Each condition in (15) is again a cross-ratio condition. Hence generic collinearity of a `2+2` support is equivalent to:

- `-a_1,-a_2,b_1,b_2` lie on one generalized circle `C_1`;
- `-a_3,-a_4,b_3,b_4` lie on one generalized circle `C_2`.

If `C_1=C_2`, Theorem 1 solves the entire pair by one global Möbius transform. It was tempting to conjecture that an **exposed** block-preserving line forces `C_1=C_2`. Section 7 refutes that stronger shortcut by an exact true-unitary witness.

## 7. Exact source-valid witness: exposed `2+2` line with two different circles

Let the signed `A` spectrum `x_i=-a_i` and the `B` spectrum be

\[
x=(-3,-2,1-3i,1-2i),
\qquad
b=(-1,0,1,1+i).
\tag{16}
\]

Equivalently,

\[
a=(3,2,-1+3i,-1+2i).
\]

The first local quartet `{-3,-2,-1,0}` lies on the real line; the second `{1-3i,1-2i,1,1+i}` lies on the vertical line `Re z=1`. These generalized circles are distinct. In particular the eight signed spectral points are not on one generalized circle, because a generalized circle through four distinct real points must be the real line.

Take the genuine unitary

\[
U_0=\operatorname{diag}(H,H),
\qquad
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\]

and `B=U_0 diag(b) U_0^*`. Then `A` and `B` are normal and have a genuine `2+2` common reducing decomposition.

The four block-preserving permutation products are exactly

\[
-36,-32,-27,-24.
\tag{17}
\]

All twenty off-block permutation products have **strictly negative imaginary part**. Thus the real axis is an exposed support line of the full 24-vertex hull, not merely of the block sub-hull.

Each `2 x 2` Hadamard block gives the equal Birkhoff law on its two permutations, so

\[
\det(A+B)
=\frac{4+3}{2}\cdot\frac{-9-8}{2}
=-\frac{119}{4},\tag{18}
\]

which lies in the relative interior of the exposed real segment but on the boundary of the full planar hull.

Therefore the following stronger candidates are false:

- "a collinear support-positive common-block representation is always rescued into the interior by off-block vertices";
- "an exposed generic `2+2` support line forces the two local generalized circles to coincide".

This witness is **not** an MOC counterexample: (18) is inside the hull exactly.

### Exact integer verifier used

`verify_circle_face.py` enumerates all 24 products as Gaussian-integer pairs. Its exact output begins

```text
support = [((0, 1, 2, 3), (-36, 0)), ((0, 1, 3, 2), (-32, 0)), ((1, 0, 2, 3), (-27, 0)), ((1, 0, 3, 2), (-24, 0))]
off_imag_unique = [-112, -108, -100, -96, -72, -64, -60, -54, -48, -44, -30, -24, -18, -16, -14, -12]
all_off_imag_negative = True
support_sum = (-119, 0)
```

so the support-line claim and determinant average are exact integer/rational statements.

## 8. Second-order check on the exposed witness: every off-block unitary tangent points inward

The same exact witness gives a useful tangent diagnostic rather than a target failure.

Let

\[
B_0=U_0\operatorname{diag}(b)U_0^*,
\]

and perturb only away from the common-block subgroup by

\[
K(C)=\begin{pmatrix}0&C\\-C^*&0\end{pmatrix},
\qquad
B(t)=e^{tK(C)}B_0e^{-tK(C)}.
\]

Set

\[
D(t)=\det(A+B(t)).
\]

Because `A+B_0` is block diagonal while `[K,B_0]` is block off-diagonal,

\[
D'(0)=0.
\]

For `N=(A+B_0)^{-1}`, the standard determinant derivative gives

\[
D''(0)=D(0)\left(
\operatorname{tr}(N[K,[K,B_0]])
-\operatorname{tr}((N[K,B_0])^2)
\right).\tag{19}
\]

Write

\[
C=\begin{pmatrix}
u_0+i u_1&u_2+i u_3\\u_4+i u_5&u_6+i u_7\end{pmatrix}.
\]

(Here `nu_0` is the variable called `u0` in the verifier.) Exact symbolic expansion yields

\[
\operatorname{Im}D''(0)
=q(u_0,u_2,u_4,u_6)+q(u_1,u_3,u_5,u_7),\tag{20}
\]

where `q(v)=v^T Mv` and

\[
M=\begin{pmatrix}
-59&1&33&-3\\
1&-79&-3&45\\
33&-3&-75&-3\\
-3&45&-3&-99
\end{pmatrix}.\tag{21}
\]

The leading principal minors of `-M` are

\[
59,\quad4660,\quad263136,\quad19107648,
\]

all strictly positive. Sylvester's criterion therefore makes `-M` positive definite, so

\[
\boxed{\operatorname{Im}D''(0)<0\quad\text{for every nonzero off-block }C.}\tag{22}
\]

This is a rigorous local fact for the witness: although the determinant sits on the exposed top edge at `t=0`, every nontrivial infinitesimal off-block mixing moves it strictly into the allowed half-plane to second order. It does **not** prove a full neighborhood theorem when the spectra themselves also move, but it confirms that the remaining obstruction is genuinely a coupled spectral/tangent problem rather than an immediate unitary-mixing escape.

The exact verifier prints the quadratic form and checks negative definiteness:

```text
D0 = -119/4
one_copy_matrix = [[-59, 1, 33, -3], [1, -79, -3, 45], [33, -3, -75, -3], [-3, 45, -3, -99]]
negative_definite_check_principal_minors_of_minus_M = [59, 4660, 263136, 19107648]
```

The full exact polynomial is preserved in `VERIFY_OUTPUT.txt`.

## 9. Application of the named partner result

The account03/B09 result `MOC4-ODD-TWIST-MASS-v1` is not a boundary representation and is not replaced here. It supplies 16 inequalities satisfied by every genuine `SO(6)` exterior-square image and an exact support duality mechanism on the generic structured coefficient problem.

The boundary reduction above applies it as follows: after excluding repeated/common-block exact cases, opposite-shifting away individual singularities, and removing nonexposed/noncollinear boundary approaches, any remaining counterexample must lie in the simple-spectrum irreducible core and simultaneously satisfy the partner's 16 odd-twist mass inequalities. In particular one must **not** enlarge to the unrestricted 48-state colored matching relaxation already known to overshoot. The new common-circle theorem and repeated-face classification remove a spectral boundary escape; the partner inequalities continue to constrain the surviving interior support problem.

## 10. Status and next implication

**Established this run:**

- `MOC-COMMON-CIRCLE-v1`: exact Möbius reduction of common-generalized-circle signed spectra to Fiedler's Hermitian theorem, valid in every dimension.
- `MOC4-REPEATED-CIRCLE-CLASSIFICATION-v1`: on the generic Hall-full repeated face, collinearity of all 12 distinct repeated-face vertices is equivalent to common generalized-circle signed spectra.
- exact generic `2+2` local-circle classification.
- an exact true-unitary exposed `2+2` witness with distinct local circles, refuting an overstrong global-circle shortcut.
- an exact negative-definite second variation for every off-block unitary tangent at that witness.

**Not established:** full MOC4; an open collar through every collinear repeated/common-block boundary; any generic common second-compound permutation lift; any claim that a search miss proves novelty.

**First boundary-specific missing implication:** a tangent/support theorem for perturbations transverse to the common-circle repeated locus, and then the analogous exposed mismatched-circle `2+2` / exposed `1+3` common-block faces. A productive next formulation is to compare the normal derivative (or, when the first derivative vanishes, the second variation) of `det(A+B)` with the active permutation-vertex support derivatives, preserving the genuine unitary constraints. The exact witness above shows that second-order inwardness can hold even when ordinary interior-margin arguments fail.

MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.
