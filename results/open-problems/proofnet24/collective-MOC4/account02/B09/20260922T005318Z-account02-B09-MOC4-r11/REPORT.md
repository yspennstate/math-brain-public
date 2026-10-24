# MOC4 account02/B09 r11 — exact two-coordinate polarization ellipses

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira target  
**Assignment:** a different geometric/polarization mechanism for the same support function, retaining complex phases and one genuine unitary.  
**Outcome:** `ESSENTIAL_STEP_APPLIED` with one subsidiary `CANDIDATE_REFUTED`. The parent MOC4 target remains open.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source state and peer result actually used

The target is: for every complex normal 4-by-4 pair, after diagonalizing

\[
A=\operatorname{diag}(a_1,\dots,a_4),\qquad B=U\operatorname{diag}(b_1,\dots,b_4)U^*,
\]
prove

\[
D_U:=\det(A+B)\in\operatorname{conv}\{v_\sigma:=\prod_i(a_i+b_{\sigma(i)}):\sigma\in S_4\}.
\]

The canonical archive had no completed `account03/B07` directory in the snapshot read for this run, so I do not pretend to have consumed a nonexistent lead version. I instead applied the completed OTHER-account result **account03/B08, `MOC4-PERMUTATION-TANGENT-v1`**: at a uniquely exposed permutation vertex, every nontrivial true-unitary tangent direction has strictly negative quadratic support variation, and a single 2-by-2 mixing from a permutation unitary traces an exact hull edge. Its first remaining obligation is a finite-mixing obstruction away from monomial unitaries.

I also consumed the later **account01/B08, `MOC4-UPPER-DRURY-FACET-FAN-v1`** handoff: the same-unitary signed coefficients reproduce all compound-minor marginals, and Drury's n=4 cone reduces a full support proof to the upper-facet inequality `(UF)`. That route is complementary to the unitary-side geometric route below; I do not assume `(UF)`.

## 2. Conditional end-to-end route and first missing implication

Fix a support direction `eta` and maximize

\[
F_\eta(U)=\Re(\eta D_U)
\]
over the compact group `U(4)`. If every global maximizer satisfies

\[
F_\eta(U)\le \max_\sigma\Re(\eta v_\sigma),
\]
then support-function separation gives MOC4. Account03/B08 rules out escape from a uniquely exposed permutation vertex by an infinitesimal perturbation. The first essential missing implication on this geometric route is therefore:

> **`MOC4-BIPAIR-MAX-v1`.** Show that a finite-mixing global maximizer which is simultaneously optimal under every two-row and every two-column `U(2)` polarization already satisfies the permutation support bound.

The theorem below derives the exact finite `U(2)` optimization, with no bistochastic surrogate and no loss of phase information. Thus `MOC4-BIPAIR-MAX-v1` is now an explicit algebraic compatibility problem rather than an unspecified finite-mixing condition.

## 3. Exact row-pair polarization theorem

Fix a true unitary `U`, a row pair `I={i,j}`, and let `J=I^c`. Put

\[
C=U\operatorname{diag}(b)U^*,\qquad
m=\frac{a_i+a_j}{2},\qquad \delta=\frac{a_i-a_j}{2}.
\]

Let `N` be obtained from `C+diag(a)` by replacing the two diagonal entries `a_i,a_j` by `m,m`. Equivalently,

\[
N=C+\operatorname{diag}(a_1,\ldots,m,\ldots,m,\ldots,a_4).
\]

For `G in U(2)` embedded on the coordinates `I`, define

\[
H_G=G^*\begin{pmatrix}1&0\\0&-1\end{pmatrix}G.
\]

Every such `H_G` is a traceless Hermitian involution, hence uniquely

\[
H_G=n_x\sigma_x+n_y\sigma_y+n_z\sigma_z,
\qquad n=(n_x,n_y,n_z)\in S^2,
\]
and every `n in S^2` occurs.

### Theorem — the determinant of a full pair orbit is an affine Bloch sphere

For all complex spectra, including singular and repeated cases,

\[
\boxed{
D_{GU}=d_0+\delta\,(q_xn_x+q_yn_y+q_zn_z),
}
\tag{1}
\]
where

\[
d_0=\det N-\delta^2\det N[J,J],
\qquad
q_r=\operatorname{tr}(\operatorname{adj}N\,\widetilde\sigma_r).
\tag{2}
\]
Here `tilde sigma_r` denotes the Pauli matrix embedded in the `I x I` block.

**Proof.** Conjugating the determinant by the same embedded `G`,

\[
D_{GU}=\det(G^*\operatorname{diag}(a)G+C)
      =\det(N+\delta\widetilde H_G).
\]
Because the perturbation is supported on only two rows and columns, the determinant is a polynomial of degree at most two in `delta`. Its constant term is `det N`; its linear term is

\[
\delta\operatorname{tr}(\operatorname{adj}N\,\widetilde H_G);
\]
and the quadratic term is the complementary principal minor times the 2-by-2 determinant,

\[
\delta^2\det(H_G)\det N[J,J]
=-\delta^2\det N[J,J],
\]
since `det H_G=-1`. Expanding `H_G` in the Pauli basis gives (1)-(2). No inverse or nonvanishing assumption is used, so the identity already includes singular and repeated-spectrum cases. ∎

### Geometric consequence

The image of `S^2` under (1), viewed in the complex plane, is a filled ellipse (degenerating to a segment or a point). For a fixed support direction define the real vector

\[
r_\eta=(\Re(\eta\delta q_x),\Re(\eta\delta q_y),\Re(\eta\delta q_z)).
\]
Then the entire pair-orbit support optimization is exact:

\[
\boxed{
\max_{G\in U(2)}F_\eta(GU)=\Re(\eta d_0)+\|r_\eta\|_2.
}
\tag{3}
\]

At the current point `G=I`, `n=e_z`. Therefore `U` is already maximal on this whole row-pair orbit iff

\[
\boxed{r_{\eta,x}=r_{\eta,y}=0,\qquad r_{\eta,z}\ge0.}
\tag{4}
\]

This is a finite-orbit statement, not merely a first- or second-variation test. Applying the same argument to `UG` after conjugating by `U^*` gives the identical theorem for every **column** pair, with the roles of `a` and `b` interchanged. Hence every global support maximizer must satisfy twelve exact pair-polarization conditions: six row pairs and six column pairs.

When the relevant pair is a common reducing block, the transverse coefficients vanish and the ellipse degenerates to the segment between the two swap endpoints. This recovers the edge behavior seen in account03/B08, but (1) also describes the genuinely interacting finite-mixing case where the orbit bulges away from that segment.

## 4. A tempting stronger lemma is false on a genuine unitary

A natural attempted completion would say that, on every pair orbit, the support is bounded by the better of the two endpoints `G=I` and the coordinate swap. That would permit a pairwise descent toward permutation matrices. It is false even for a real orthogonal 4-by-4 unitary with simple spectra and no zero `a_i+b_j`.

Take the normalized Hadamard matrix

\[
U_0=\frac12\begin{pmatrix}
1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1
\end{pmatrix},
\]

\[
a=(-2,7,2,8),\qquad b=(-1,5,3,1),\qquad \eta=1,
\]
and rotate rows 1,2 by

\[
G=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\]

The exact verifier gives

\[
F(U_0)=-175,\qquad F(G_{\rm swap}U_0)=-391,
\]
while

\[
\boxed{F(GU_0)=1457/25},
\]
so the interior rational rotation exceeds the better endpoint by

\[
\boxed{5832/25>0.}
\]

For this orbit the exact ellipse data are

\[
c=-283,\qquad r=(-387,0,108),\qquad \|r\|^2=161433.
\]
Thus the transverse coefficient is genuinely nonzero; endpoint convexification loses essential common-unitary phase geometry. This is `CANDIDATE_REFUTED` for the endpoint-only pair descent, not a counterexample to MOC4: the full 24-vertex support maximum here is `840`, far above the entire pair-orbit maximum `-283+\sqrt{161433}`.

The standard-library exact verifier and its output are saved beside this report.

## 5. What this changes in the shared proof state

The account03/B08 tangent result says a violation cannot be born infinitesimally from a uniquely exposed permutation unitary. The present theorem upgrades the finite two-coordinate part: every row/column `U(2)` orbit is completely solvable as one ellipse, so a hypothetical counterexample maximizer must sit at the north pole of **all twelve** corresponding support ellipses. No arbitrary doubly stochastic object is introduced; every point is produced by one actual unitary, and all complex phases are retained.

The exact next obligation is therefore not to repeat local Hessian tests and not to force pair endpoints. It is:

> **`MOC4-BIPAIR-MAX-v1` (remaining).** Combine the twelve conditions (4), for one common unitary and one common support direction, with the account01/B07 `(P,R)` compatibility identities or the account01/B08 Drury upper-facet reduction, and prove the permutation support bound; alternatively construct a true-unitary simple-spectrum point satisfying all twelve pair-optimality conditions with a positive global support gap.

This is the first unpaid implication after the present result. No full proof, target counterexample, or novelty claim is made.

## 6. Provenance

Source/status dependencies were taken from the campaign `TARGETS.md`: Drury (2004), Bebiano--da Providencia (2025), and Mulero-Martinez (2026). Exact peer inputs used were account03/B08 `MOC4-PERMUTATION-TANGENT-v1`, account01/B07 `MOC4-MIXED-ASSIGNMENT-v1`, and account01/B08 `MOC4-UPPER-DRURY-FACET-FAN-v1`. The missing canonical account03/B07 lead artifact was recorded as missing rather than reconstructed as if it had been read.
