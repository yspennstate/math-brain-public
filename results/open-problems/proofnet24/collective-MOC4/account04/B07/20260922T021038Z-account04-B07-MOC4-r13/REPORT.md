# MOC4 account04/B07 r13 — odd-Weyl obstruction and an exact SO(6) orientation-overlap inequality

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, the complex-normal 4-by-4 Marcus–de Oliveira target  
**Worker:** account04/B07  
**Assignment:** representation-theoretic / exterior-algebra proof of the shared mixed-minor constraint  
**Candidate:** `MOC4-ODD-WEYL-ORIENTATION-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`. A natural orientation-forgetting Weyl/Birkhoff relaxation is refuted by an exact structured true-unitary datum, and the missing orientation information is replaced by a new exact odd-Weyl overlap inequality for every `SO(6)` exterior-square image. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and current inherited state

The target is: for every pair of complex normal `4 x 4` matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4` counted with multiplicity,

\[
\det(A+B)\in\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\tag{MOC4}
\]

Singular and repeated-spectrum cases are part of the statement. The campaign source/status boundary remains the one in `scheduled_tasks/work/shared/collective-open-problems-2026-09-22/TARGETS.md`: Drury's 2004 result is weakened n=4, while the 2025 survey and 2026 variational paper retain the general problem as open. No literature-search miss is used as a novelty claim here.

This run read the newest complete campaign-lead report available in the canonical archive:

- **account03/B07**, run `20260922T013930Z-account03-B07-MOC4-r11`, `MOC4-ZERO-ENTRY-COMMON-LIFT-v1 = REFUTED`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`. It proves with an exact rational zero-entry orthogonal matrix that even the zero-entry face does **not** restore a common positive `S_4` subset-permutation lift. Its surviving zero-face task is to use the exact support functional directly.

The required named OTHER-account partner result used substantively is:

- **account01/B08**, run `20260922T013942Z-b08-moc4-r11`, report `MOC4 account01/B08 r11 — exact 3x3 roof formula and refutation of the parity-slack gate`. It gives an exact structured generic true-unitary datum on which the scalar parity/convex-roof route fails while the full `X`-dependent MOC4 support inequality has large positive slack. Consequently this run does **not** continue the superseded parity-payment route; it retains the full `X` term and returns to the exterior-square `SO(6)` formulation.

I also use the exact account01/B07 mixed-minor reduction and its newest generic counterexample, because they supply the source-valid structured `(K,X)` used below:

- `MOC4-MIXED-ASSIGNMENT-v1`: exact exterior-power expansion and mixed assignment inequality;
- account01/B07 run `20260922T013731Z-b07-moc4-r11b`: exact generic simple-spectrum, irreducible, strict-compound true-unitary datum for which the parity gate fails but the exact six-fiber inequality succeeds.

No benchmark material, answer key, hidden witness, generation secret, credential, email/Drive content, paid/remote computation, or unrelated private data is used.

## 2. Exact exterior-square coordinates retained from the previous B07 mechanism

For an actual unitary `U`, after multiplying by a scalar phase assume `det U=1`. On

\[
\Lambda^2\mathbb C^4
\]

the operator `Lambda^2 U` preserves both the Hermitian form and the complementary-pair symmetric form. In the real form determined by Hodge-complement conjugation it becomes

\[
O(U)\in SO(6).
\]

Partition the real six-space into the three complementary-pair planes and write

\[
O=(B_{\alpha\beta})_{\alpha,\beta=1}^3,
\qquad B_{\alpha\beta}\in M_2(\mathbb R).
\]

The previous account04/B07 `MOC4-SPIN6-BLOCK-v1` calculation gives exactly

\[
r_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2,
\qquad
d_{\alpha\beta}=\det B_{\alpha\beta},
\tag{1}
\]

and the block orthogonality equations

\[
\sum_\beta B_{\alpha\beta}B_{\gamma\beta}^{T}
=\delta_{\alpha\gamma}I_2,
\qquad
\sum_\alpha B_{\alpha\beta}^{T}B_{\alpha\delta}
=\delta_{\beta\delta}I_2.
\tag{2}
\]

For the structured support coefficients `(K,X)` coming from `(a,b,eta)`, the exact nonconstant support objective is

\[
Q_{K,X}(O)
=\sum_{\alpha,\beta}
\left[
K_{\alpha\beta}\det B_{\alpha\beta}
+\frac14X_{\alpha\beta}\|B_{\alpha\beta}\|_F^2
\right].
\tag{3}
\]

The target support inequality is that `(3)` is at most its maximum on the 24 `S_4` endpoint images in `SO(6)`.

## 3. New Bogoliubov form: the two oriented minor channels are the complex-linear and anti-linear masses

Identify every real complementary-pair plane with `C`. A real `2 x 2` block has a unique form

\[
z\longmapsto m_{\alpha\beta}z+n_{\alpha\beta}\bar z.
\tag{4}
\]

In real coordinates this is

\[
B_{\alpha\beta}=
\begin{pmatrix}
\operatorname{Re}(m+n)&-\operatorname{Im}(m-n)\\
\operatorname{Im}(m+n)&\operatorname{Re}(m-n)
\end{pmatrix}.
\tag{5}
\]

Consequently

\[
\frac12\|B_{\alpha\beta}\|_F^2=|m_{\alpha\beta}|^2+|n_{\alpha\beta}|^2,
\qquad
\det B_{\alpha\beta}=|m_{\alpha\beta}|^2-|n_{\alpha\beta}|^2.
\tag{6}
\]

Thus, with

\[
q^+_{\alpha\beta}:=\frac{r_{\alpha\beta}+d_{\alpha\beta}}2=|m_{\alpha\beta}|^2,
\qquad
q^-_{\alpha\beta}:=\frac{r_{\alpha\beta}-d_{\alpha\beta}}2=|n_{\alpha\beta}|^2,
\tag{7}
\]

the exact support objective becomes

\[
\boxed{
Q_{K,X}(O)=
\sum_{\alpha,\beta}
\left[
\left(K_{\alpha\beta}+\frac12X_{\alpha\beta}\right)q^+_{\alpha\beta}
+
\left(-K_{\alpha\beta}+\frac12X_{\alpha\beta}\right)q^-_{\alpha\beta}
\right].}
\tag{8}
\]

These are not invented variables: `q^+` and `q^-` are exactly the two squared complementary `2 x 2` minors paired in the exterior-square reduction.

Orthogonality implies

\[
\sum_\beta(q^+_{\alpha\beta}+q^-_{\alpha\beta})=1,
\qquad
\sum_\alpha(q^+_{\alpha\beta}+q^-_{\alpha\beta})=1.
\tag{9}
\]

Therefore `(q^+,q^-)` is a two-colour fractional perfect matching on `K_{3,3}`. By integrality of the bipartite perfect-matching polytope with parallel coloured edges, every array satisfying only nonnegativity and `(9)` is a convex combination of the 48 coloured matchings

\[
(\rho,\epsilon),\qquad
\rho\in S_3,\quad \epsilon\in\{+,-\}^3.
\tag{10}
\]

Exactly 24 of these have an even number of minus signs. They are the true `S_4` endpoint images: permuting three real 2-planes has determinant `+1`, so the determinant of the block-monomial endpoint is the product of the three block orientation signs. The other 24 have odd minus parity and lie in the `det=-1` component of `O(6)`.

This identifies, without any positivity conjecture, the exact obstruction in the naive representation relaxation: forgetting the connected/orientation component enlarges the endpoint set from the `D_3` Weyl group (`24`, isomorphic to `S_4`) to the full signed-pair matching set (`48`).

## 4. Exact source-valid counterexample to the orientation-forgetting 48-state relaxation

Take the exact structured coefficient pair from account01/B07 run `20260922T013731Z-b07-moc4-r11b`, equations (16)-(17):

\[
K=\begin{pmatrix}
245983/5120000&5030591/5120000&-39077/1024000\\
-5113569/5120000&56671/5120000&19643/1024000\\
-8539/1024000&-35819/1024000&5009153/5120000
\end{pmatrix},
\tag{11}
\]

\[
X=\begin{pmatrix}
-3609633/1280000&111173/51200&2385071/1280000\\
-917133/1280000&1431961/1280000&525623/256000\\
-1352967/1280000&1061147/1280000&948017/1280000
\end{pmatrix}.
\tag{12}
\]

The cited source report verifies that these coefficients come from an exact rational true-unitary, simple-spectrum, irreducible, strict-compound MOC4 datum. It also verifies that the exact 24-endpoint support maximum is

\[
M_{\rm even}=\frac{13195057}{5120000}
=2.5771595703125.
\tag{13}
\]

Using `(8)`, enumerate all `3! 2^3=48` coloured matching scores exactly. The maximum over the **even** patterns is `(13)`, attained at

\[
\rho=(2,3,1),\qquad \epsilon=(+,+,+)
\tag{14}
\]

in one-based notation. But the maximum over the **odd** patterns is

\[
M_{\rm odd}=\frac{20773731}{5120000}
=4.0573693359375,
\tag{15}
\]

attained at

\[
\rho=(2,1,3),\qquad \epsilon=(+,-,+).
\tag{16}
\]

The exact excess is

\[
\boxed{
M_{\rm odd}-M_{\rm even}
=\frac{3789337}{2560000}
=1.480209765625>0.}
\tag{17}
\]

The standard-library verifier `verify_odd_weyl.py` enumerates the 48 cases using `fractions.Fraction`; `VERIFICATION.txt` records exactly:

```text
even_max = 13195057/5120000 2.5771595703125
even_argmax rho,bits = (1, 2, 0) (0, 0, 0)
odd_max = 20773731/5120000 4.0573693359375
odd_argmax rho,bits = (1, 0, 2) (0, 1, 0)
odd_minus_even = 3789337/2560000 1.480209765625
PASS: exact 48-state colored-matching enumeration
```

Hence the following tempting mechanism is **refuted on an actual structured MOC4 coefficient pair**:

> “Apply coloured Birkhoff to `(q^+,q^-)`, maximize over all 48 signed pair matchings, and expect the structured spectral coefficients to make an even `S_4` endpoint dominate every odd matching.”

They do not. This is a counterexample to that stronger representation-theoretic relaxation, not to MOC4. The cited true-unitary datum itself has a positive exact MOC4 support slack; the forbidden high-scoring point `(16)` is orientation reversing and is not an exterior-square image of an `SU(4)` unitary.

## 5. New exact theorem: odd-Weyl overlap is at most two

The previous section shows that orientation cannot be dropped. The following theorem supplies a quantitative orientation constraint that is absent from the coloured Birkhoff relaxation.

### Theorem — `MOC4-ODD-WEYL-OVERLAP-v1`

Let `O in SO(6)` be partitioned into `2 x 2` blocks as above. Fix a permutation `rho in S_3` and signs `epsilon_alpha in {+,-}` with an **odd** number of minus signs. Then

\[
\boxed{
\sum_{\alpha=1}^3
\sqrt{q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}}\le2.}
\tag{18}
\]

In particular,

\[
\boxed{
\sum_{\alpha=1}^3
q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}\le2.}
\tag{19}
\]

### Proof

For a real `2 x 2` matrix `B`, let `V_+` be the two-dimensional subspace of orientation-preserving conformal blocks

\[
\begin{pmatrix}a&-b\\ b&a\end{pmatrix},
\]

and `V_-` the orientation-reversing conformal blocks

\[
\begin{pmatrix}a&b\\ b&-a\end{pmatrix}
\]

(up to the harmless equivalent sign convention from `(5)`). Equation `(5)` says that the orthogonal projection of `B_{\alpha\beta}` to `V_+` has Frobenius norm `sqrt(2)|m_{\alpha\beta}|`, and the projection to `V_-` has norm `sqrt(2)|n_{\alpha\beta}|`.

Therefore, for each selected block `B_{\alpha,\rho(\alpha)}`, choose a matrix

\[
J_\alpha\in O(2),\qquad
\det J_\alpha=
\begin{cases}+1,&\epsilon_\alpha=+,\\-1,&\epsilon_\alpha=-,
\end{cases}
\]

whose phase maximizes its Frobenius pairing with the corresponding conformal component. Then exactly

\[
\langle J_\alpha,B_{\alpha,\rho(\alpha)}\rangle_F
=2\sqrt{q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}}.
\tag{20}
\]

Assemble the three `J_alpha` into the block-monomial real orthogonal matrix `J` with block permutation `rho`. Swapping two 2-dimensional planes has determinant `(+1)`, so

\[
\det J=\prod_\alpha\det J_\alpha=-1
\tag{21}
\]

because the sign pattern is odd. Since `O in SO(6)`,

\[
J^TO\in O(6),\qquad \det(J^TO)=-1.
\]

Any real `6 x 6` orthogonal matrix of determinant `-1` has trace at most `4`: its nonreal eigenvalues occur in conjugate pairs on the unit circle, and the real eigenvalues are `+/-1`; determinant `-1` forces at least one `-1`, so the largest possible real trace is `5-1=4`.

Thus

\[
4\ge\operatorname{tr}(J^TO)
=\sum_\alpha
\langle J_\alpha,B_{\alpha,\rho(\alpha)}\rangle_F
=2\sum_\alpha
\sqrt{q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}}.
\]

Dividing by two proves `(18)`. Since every `q` lies in `[0,1]`, `q<=sqrt(q)` termwise, so `(19)` follows. QED.

### Interpretation

An odd signed-pair endpoint would have its three selected masses equal to `1`, and hence left side `3` in `(18)`. The theorem says every actual `SO(6)` point stays quantitatively away from every such forbidden odd endpoint: the best possible total selected square-root overlap is `2`.

This is precisely the orientation information erased by the 48-state transport relaxation. It uses the same exterior-square representation as the exact mixed-minor problem and makes no common-lift or coefficientwise-positivity assertion.

## 6. Compact conditional end-to-end argument after this run

The smallest surviving representation-theoretic chain is now:

1. The exact exterior-power identity reduces MOC4 support to the mixed `(P,R)` inequality, equivalently the `SO(6)` block quadratic `(3)` for the structured `(K,X)`.
2. The new Bogoliubov coordinates rewrite this exactly as the two-colour squared-minor objective `(8)`.
3. Nonnegativity plus row/column conservation alone gives the 48 coloured Weyl matchings. The 24 even matchings are exactly the target `S_4` endpoints.
4. The exact source-valid datum `(11)-(17)` proves that **odd** Weyl scores can be strictly larger than every target endpoint. Therefore no proof may replace `SO(6)` by the full 48-state coloured matching polytope.
5. The new theorem `(18)` supplies a universal quantitative exclusion of every odd Weyl vertex from the actual `SO(6)` orbit.
6. The remaining indispensable implication is now an **orientation-aware weighted suppression** statement: combine `(18)` with the full block orthogonality equations `(2)` and the structured spectral form of the weights in `(8)` to prove

\[
Q_{K,X}(O)
\le
\max_{\substack{\rho\in S_3,\epsilon\in\{+,-\}^3\\\#\{\epsilon=-\}\text{ even}}}
\sum_\alpha
\left(K_{\alpha,\rho(\alpha)}+\frac{\epsilon_\alpha}{2}X_{\alpha,\rho(\alpha)}\right)
\quad\text{with the sign convention of `(8)`,}
\tag{22}
\]

for every **structured** support pair `(K,X)` and every `O in SO(6)` arising from one common unitary. Equivalently, one must show that the extra score available to an odd coloured matching is always paid by its compulsory `SO(6)` orientation distance and the off-diagonal block-orthogonality couplings.

Equation `(22)` is not claimed proved here. The advance is that its first false relaxation and its first exact missing orientation inequality are now both identified. A next representation-theoretic worker should attack the weighted payment directly, rather than return to the already-refuted parity roof or a positive common lift.

## 7. Failure accounting and scope

- `MOC4-48-WEYL-DOMINANCE-v1`: **REFUTED** by the exact structured coefficients `(11)-(17)`.
- `MOC4-ODD-WEYL-OVERLAP-v1`: **PROVED** for every real `O in SO(6)`, hence for every exterior-square image of a `4 x 4` unitary after phase normalization.
- This theorem is an exact necessary orientation constraint, not a complete characterization of the `SO(6)` block orbit and not by itself a proof of MOC4.
- The source-valid counterexample refutes only the stronger orientation-forgetting proof mechanism; it is **not** a counterexample to MOC4.
- The partner's parity/roof refutation is preserved and used: the full `X`-dependent support objective remains live throughout.
- The lead's zero-entry common-lift no-go is preserved: the new theorem does not resurrect a positive `S_4` lift on the boundary or in the interior.
- Singular and repeated spectra remain part of the parent target. This run does not make a new boundary theorem; it works on the exact all-unitary mixed-minor constraint and is compatible with inherited boundary reductions.

## 8. Artifacts and exact computation

- `verify_odd_weyl.py`: standard-library exact `Fraction` enumeration of all 48 coloured matching scores for the source-valid structured `(K,X)`.
- `VERIFICATION.txt`: exact deterministic output quoted in Section 4.

No numerical tolerance is used in the new counterexample. The proof of `(18)` is analytic and does not depend on the verifier.

## 9. Source-bound handoff

**To the team lead account03/B07 and partner account01/B08:** the parity-roof route should remain retired. In the exact `SO(6)` exterior-square coordinates, write every block as `z -> mz+n zbar`; the support is the weighted colour transport `(8)`. The full 48-colour Birkhoff relaxation is decisively too large on the account01/B07 exact generic datum: its best odd Weyl score exceeds the target `S_4` maximum by exactly `3789337/2560000`. However every actual `SO(6)` point satisfies the new odd-pattern inequality `sum sqrt(q_selected)<=2`. The next proof step is to make the structured `(K,X)` weights pay for that compulsory orientation distance using the exact off-diagonal block equations `(2)`, not to seek another unrestricted positive lift.
