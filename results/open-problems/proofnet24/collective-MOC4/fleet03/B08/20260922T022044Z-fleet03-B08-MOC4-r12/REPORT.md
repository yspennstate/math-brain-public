# MOC4 fleet03/B08 r12 — exact one-cycle chord reduction and a 90%-margin true-unitary adversary

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus-de Oliveira determinant hull  
**Worker:** fleet03/B08  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and peer state consumed

The target is: for every pair of complex normal `4 x 4` matrices with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\{v_\sigma(a,b):\sigma\in S_4\},\qquad
v_\sigma=\prod_{i=1}^4(a_i+b_{\sigma(i)}).
\]

This run executes the assigned true-unitary/spectrum adversary role. Its named assigned other-account input is **fleet04/B09 `MOC4-PR-JOINT-LIFT-v1` / structured-coefficient result**, whose exact rational orthogonal witness shows that unitary-derived `(P,R)` need not admit a common permutation lift, while its Vandermonde/Bezout identities show why arbitrary bistochastic separation is still not a target counterexample. I therefore do not search over arbitrary bistochastic arrays or infer target failure from negative formal coefficients.

I also consume the newer fleet02/B09 exact six-fiber compression: with `T=|K|+X/2`, parity penalties `m_rho`, assignment values `c_rho`, orientation slack `S`, and parity excess `E=<R,T>-max_rho(c_rho-2m_rho)`, the exact support gap is `S-E`. That result and the fleet01/B07/B08 counterexamples rule out decoupling the true-unitary orientation and structured-X mechanisms. The present run changes mechanism: instead of another six-fiber scalar gate, it analyzes the first genuinely cyclic Givens family directly in determinant coordinates.

## 2. The first cyclic Givens family

For real numbers `c_j,s_j` with `c_j^2+s_j^2=1`, let `R_ij(c,s)` be the identity except for the `(i,j)` block

\[
\begin{pmatrix}c&-s\\s&c\end{pmatrix}.
\]

Consider the true orthogonal (hence unitary) coupling

\[
U=R_{12}(c_1,s_1)R_{23}(c_2,s_2)R_{34}(c_3,s_3)R_{14}(c_4,s_4).
\tag{2.1}
\]

The first three support edges form the path `12-23-34`; the final `14` edge closes the first cycle. Put

\[
U_0=R_{12}R_{23}R_{34},\qquad
U_1=U_0R_{14}(0,1),
\]

and write

\[
D(U)=\det(D_a+UD_bU^T),\quad D_0=D(U_0),\quad D_1=D(U_1).
\]

By the preceding B08 forest-Givens theorem, `D_0` and `D_1` are honest convex combinations of the 24 permutation products for every complex spectra. The question is exactly what the one new cycle contributes.

## 3. New theorem: `MOC4-ONE-CYCLE-CHORD-v1`

### Theorem

For the family `(2.1)`, for all complex spectra `a,b`,

\[
\boxed{
D(U)=c_4^2D_0+s_4^2D_1
+2c_4s_4c_1s_1s_2s_3\bigl(v_{4123}-v_{1423}\bigr).
}
\tag{3.1}
\]

Moreover

\[
\boxed{
v_{4123}-v_{1423}
=(a_1-a_2)(a_3+b_2)(a_4+b_3)(b_1-b_4).}
\tag{3.2}
\]

Thus the entire first-cycle interference, although its raw determinant quasidistribution has many signed coefficients, collapses in the actual spectral image to **one explicit chord between two allowed permutation vertices**.

### Proof

Use the determinantal quasidistribution expansion

\[
D(U)=\sum_{\sigma\in S_4}\mu_\sigma(U)v_\sigma,
\qquad
\mu_\sigma(U)=\operatorname{sgn}(\sigma)\prod_i u_{i,\sigma(i)},
\tag{3.3}
\]

valid here because `U` is real orthogonal with determinant one. Right multiplication by the final `R_14(c_4,s_4)` changes only columns 1 and 4, so each `mu_sigma` is homogeneous quadratic in `(c_4,s_4)`. Its `c_4^2` and `s_4^2` parts are exactly the quasidistributions of `U_0` and `U_1`. Hence only the mixed `c_4s_4` coefficient needs evaluation.

Factoring out `c_1s_1s_2s_3`, the mixed term groups into

\[
 c_2^2c_3^2 A+c_2^2s_3^2 B+s_2^2c_3^2 C+s_2^2s_3^2 D+D,
\tag{3.4}
\]

where

\[
\begin{aligned}
A={}&-v_{1234}+v_{2134}-v_{2314}+v_{2341}-v_{2431}+v_{3214}-v_{3241}+v_{4231},\\
B={}&-v_{1243}+v_{2143}-v_{2413}+v_{4213},\\
C={}&-v_{1324}+v_{3124}-v_{3421}+v_{4321},\\
D={}&-v_{1423}+v_{4123}.
\end{aligned}
\tag{3.5}
\]

Direct two-row/two-column swap factorization gives, in every line,

\[
A=B=C=D
=(a_1-a_2)(a_3+b_2)(a_4+b_3)(b_1-b_4)
=v_{4123}-v_{1423}.
\tag{3.6}
\]

For example the final equality is the ordinary two-row swap identity; the other three are the same identity after grouping the displayed alternating terms. Therefore the bracket multiplying the common chord is

\[
(c_2^2+s_2^2)(c_3^2+s_3^2)+1=2.
\]

Multiplying back by `c_4s_4c_1s_1s_2s_3` proves `(3.1)`, and `(3.2)` is the direct factorization of `D`. QED.

## 4. Exact support-form adversary gate

Fix one common real support functional

\[
L(z)=\operatorname{Re}(\eta z),\qquad
M=\max_{\sigma\in S_4}L(v_\sigma).
\]

Define the two nonnegative tree-endpoint deficits

\[
\delta_0=M-L(D_0)\ge0,\qquad
\delta_1=M-L(D_1)\ge0.
\]

Applying `L` to `(3.1)` gives the exact target gap

\[
\boxed{
M-L(D(U))
=c_4^2\delta_0+s_4^2\delta_1
-2c_4s_4c_1s_1s_2s_3\bigl(L(v_{4123})-L(v_{1423})\bigr).
}
\tag{4.1}
\]

Therefore a genuine MOC4 violation in this first cyclic family occurs in a direction exactly when the one explicit chord payment exceeds the two already-certified forest endpoint deficits. This is a target-level common-direction test: `M` is the maximum over **all 24 spectral vertices in the same direction**, not a formal-coefficient or bistochastic surrogate.

Equation `(4.1)` is the main progress of this run. It replaces a 24-term signed cyclic quasidistribution by one scalar competition with two safe endpoint margins. It also gives a clean finite-mixing subproblem for the next run: prove the chord payment can never exceed those endpoint deficits for structured permutation products, or construct spectra/direction where it does, which by `(4.1)` would be a genuine MOC4 counterexample in this family.

## 5. Exact true-unitary near-adversary: the cycle consumes 90.0176% of the endpoint margin

Set every rotation to

\[
c_j=3/5,\qquad s_j=4/5,
\]

and use the simple nonzero Gaussian-integer spectra

\[
a=(-4+5i,\ 3-8i,\ -3,\ 3-5i),
\]

\[
b=(-1+8i,\ 7-3i,\ 5-6i,\ 6-4i).
\]

Take the common support direction

\[
L(z)=\operatorname{Re}((-1-i)z).
\]

Exact enumeration shows that all 24 complex permutation products are distinct and the support maximizer is unique, at permutation `3142`, with

\[
M=8,
\]

while the next three support values are `0,-36,-80`.

The exact cyclic determinant is

\[
D(U)=\frac{292022244}{390625}
+i\frac{49307748}{390625},
\]

so

\[
\boxed{M-L(D(U))=\frac{245839496}{390625}>0.}
\tag{5.1}
\]

The chosen direction therefore does not separate the determinant from the 24 vertices. More strongly, this datum is **exactly inside the full two-dimensional spectral hull**, not merely safe in one tested direction: the verifier checks the Caratheodory certificate

\[
D(U)=\lambda_1v_{1234}+\lambda_2v_{2134}+\lambda_3v_{2314},
\tag{5.2}
\]

with

\[
\lambda_1=\frac{28480049}{10030078125},\qquad
\lambda_2=\frac{572818676}{668671875},\qquad
\lambda_3=\frac{1409317936}{10030078125},
\]

all nonnegative and summing exactly to one.

Nevertheless it is adversarial for the one-cycle mechanism. The exact endpoint deficits are

\[
\delta_0=\frac{23525352}{3125},\qquad
\delta_1=\frac{87756716}{15625}.
\]

The chord support difference is

\[
L(v_{4123}-v_{1423})=19244.
\]

Thus the positive endpoint contribution in `(4.1)` is

\[
B:=c_4^2\delta_0+s_4^2\delta_1
=\frac{2462748296}{390625},
\]

whereas the dangerous cycle chord contributes

\[
C:=2c_4s_4c_1s_1s_2s_3L(v_{4123}-v_{1423})
=\frac{88676352}{15625}.
\]

Exactly

\[
\frac{C}{B}=\frac{277113600}{307843537}
\approx0.9001767674.
\tag{5.3}
\]

So a single true-unitary cycle can erase just over **90.0%** of the margin supplied by its two forest endpoints, even for a datum that still has an exact three-vertex hull representation. This is a much sharper adversarial datum than the previous observation that some formal `mu_sigma` turn negative.

For the same unitary, the raw formal quasidistribution indeed has

\[
\min_\sigma\mu_\sigma=-\frac{186624}{9765625}<0,
\]

but `(5.2)` proves directly why that sign by itself has no target meaning.

## 6. Exact verification

The companion `verify_one_cycle_chord.py` uses only Python standard-library `Fraction` arithmetic. It verifies:

- exact orthogonality of the cyclic true unitary and both tree endpoints;
- 24 distinct spectral vertices and a unique common-direction maximizer `3142`;
- the exact determinant and target support gap `(5.1)`;
- exact endpoint deficits, chord support, and identity `(4.1)` for the adversarial datum;
- the exact ratio `(5.3)`;
- nonnegative normalized determinant quasidistributions for both forest endpoints;
- the negative cyclic formal coefficient, confirming that formal positivity has genuinely failed;
- the exact nonnegative three-vertex hull certificate `(5.2)`.

The theorem `(3.1)` is proved algebraically above; the finite verifier is an independent exact check of the selected source-valid datum, not a substitute for that proof.

## 7. Status and next obligation

- `MOC4-ONE-CYCLE-CHORD-v1`: **PROVED** for the ordered one-cycle family `(12),(23),(34),(14)`.
- Exact true-unitary/simple-spectrum adversarial datum: **INSIDE THE FULL HULL EXACTLY**, by the explicit three-vertex certificate `(5.2)`.
- Previous forest-Givens positivity mechanism: still valid for the two endpoints, but insufficient after the closing cycle.
- Parent MOC4: **OPEN**.

The first next implication is now sharply stated:

> **`MOC4-ONE-CYCLE-PAYMENT-v1`.** For every complex spectra and every support direction, prove the right side of `(4.1)` is nonnegative. Equivalently, prove that the explicit one-cycle chord payment never exceeds the two forest endpoint deficits. An exact negative instance of `(4.1)` would already be a genuine target-level counterexample, because its left side is the actual common-direction gap against the maximum of all 24 permutation vertices.

If the payment remains nonnegative throughout this one-cycle family, that proves MOC4 for this first cyclic mechanism and the next adversarial step should move to repeated-edge or two-cycle words rather than return to the already-refuted X-free/roof gates.

No benchmark gold/keys, FEI proof material, arbitrary bistochastic surrogate, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive/public posting, paid model/API, Codex, remote workflow, or permission changes were used.
