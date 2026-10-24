# MOC4 account01/B07 — bi-orientation pair-swap gate for the residual P/R core

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** Marcus–de Oliveira, complex normal `4 x 4` case  
**Worker/run:** account01/B07, `20260922T040155Z-a01-b07-moc4-r12`  
**Assignment:** exact exterior-power/minor expansion and the mixed-minor inequality needed for the shared hull bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Latest compatible team state actually consumed

The latest complete campaign-lead candidate consumed is account03/B07 `MOC4-V4-PAIR-GAP-CEILING-v1`, report commit `dcce2e52aee9c3fb338be4dd56acb02114ebfdde`, blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`. For a fixed support direction, write endpoint supports `H_sigma`,

`M=max H_sigma`, `m=average H_sigma`, `d=M-m`,

let `Q` be the largest `V4`-fiber average, `Delta=M-Q`, let `g_tau` be the six transposition-pair gaps, and `G=sum_tau g_tau`. Every genuine violation `h(U)=M+gamma` satisfies

`0 < gamma <= (3d-Delta-G/2)/4`.

The assigned OTHER-account partner result consumed and applied is account02/B08 `MOC4-CIRCLE-FACE-REDUCTION-v1`, report commit `290ef6e19e8d1bd99decc388191b3dd1fccdb0f8`, blob `5e52a9d9463e30108d1de0c5269d693dfd4e4ef3`. It gives the exact generalized-circle reduction to Fiedler's Hermitian theorem, classifies the generic repeated collinear face, and, together with its preceding boundary theorem, closes repeated-spectrum and proper common-reducing-block cases while isolating explicit transverse/lower-dimensional boundary strata. I use it to keep the present gate focused on the simple-spectrum irreducible residual; the algebra below itself does not require nonsingularity.

I also use account03/B09 `MOC4-ODD-TWIST-MASS-v1` as an essential compatibility dependency: every actual exterior-square point satisfies its 16 orientation-sensitive channel-mass inequalities. The present theorem is different: it couples the `P`-determined oriented channel `D` to the same point's complementary-pair transport `R` at a maximizing representative.

## 2. Exact exterior-power reduction retained

After diagonalizing `A` and writing the relative eigenbasis as `U`, the determinant has the exact Cauchy–Binet expansion

\[
\det(D_a+UD_bU^*)=
\sum_{k=0}^4\ \sum_{|S|=|T|=k}
 a_{S^c}b_T\,|\det U[S,T]|^2.\tag{1}
\]

After grouping the six `k=2` subsets into the three complementary-pair classes, choose the standard real exterior-square basis in which, after an irrelevant scalar phase on `U`,

\[
O=\Lambda^2U\in SO(6)
\]

is a `3 x 3` matrix of real `2 x 2` blocks `B_{alpha beta}`. Put

\[
D_{\alpha\beta}=\det B_{\alpha\beta},\qquad
R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2.\tag{2}
\]

Then `R` is doubly stochastic. With the inherited structured spectral coefficient matrices `(K,X)`, the full nonconstant support is exactly

\[
s(O)=k+x,
\qquad k=\langle D,K\rangle,
\qquad x=\frac12\langle R,X\rangle.\tag{3}
\]

Moreover the oriented middle channel is not free: for `P=|U|^2`,

\[
D=\frac14E^TPE,\tag{4}
\]

where `E` is the `4 x 3` matrix of the three nonconstant Hadamard characters. Thus every inequality below is an exact same-unitary `P/R` constraint, not an arbitrary bistochastic relaxation.

Let

\[
\bar c=\frac16\sum_{\alpha,\beta}X_{\alpha\beta},
\qquad y=x-\bar c.\tag{5}
\]

In the campaign's centered normalization, `h(U)-m=k+y`.

## 3. New theorem — `MOC4-BIORIENTATION-PAIR-GATE-v1`

Let `U` be a **global maximizer** of one fixed support functional, and let `(D,R)` be its exact exterior-square data. For every row-plane pair `alpha<gamma`, define

\[
T^L_{\alpha\gamma}:=
\sum_\beta\bigl(K_{\alpha\beta}D_{\alpha\beta}
+K_{\gamma\beta}D_{\gamma\beta}\bigr)
+\frac12\sum_\beta
(X_{\alpha\beta}-X_{\gamma\beta})
(R_{\alpha\beta}-R_{\gamma\beta}),\tag{6}
\]

\[
C^L_{\alpha\gamma}:=
\sum_\beta
\bigl(K_{\alpha\beta}D_{\gamma\beta}
+K_{\gamma\beta}D_{\alpha\beta}\bigr).\tag{7}
\]

Then

\[
\boxed{T^L_{\alpha\gamma}\ge |C^L_{\alpha\gamma}|}\qquad(\alpha<\gamma).\tag{8}
\]

Likewise, for every column-plane pair `beta<delta`, define

\[
T^R_{\beta\delta}:=
\sum_\alpha\bigl(K_{\alpha\beta}D_{\alpha\beta}
+K_{\alpha\delta}D_{\alpha\delta}\bigr)
+\frac12\sum_\alpha
(X_{\alpha\beta}-X_{\alpha\delta})
(R_{\alpha\beta}-R_{\alpha\delta}),\tag{9}
\]

\[
C^R_{\beta\delta}:=
\sum_\alpha
\bigl(K_{\alpha\beta}D_{\alpha\delta}
+K_{\alpha\delta}D_{\alpha\beta}\bigr).\tag{10}
\]

Then

\[
\boxed{T^R_{\beta\delta}\ge |C^R_{\beta\delta}|}\qquad(\beta<\delta).\tag{11}
\]

These six absolute-value inequalities are exact necessary conditions for a maximizing true unitary. They are singular-safe and require no inverse determinant matrix.

### Proof

Fix `alpha<gamma`. For each `epsilon in {+1,-1}`, choose `Z_epsilon in O(2)` with `det Z_epsilon=epsilon`. Let `W_{alpha gamma,epsilon}` be the real `6 x 6` orthogonal transformation which is the identity on the third complementary-pair plane and acts on the two selected planes by

\[
\begin{pmatrix}
0&Z_\epsilon\\
-Z_\epsilon^T&0
\end{pmatrix}.\tag{12}
\]

Its determinant is `+1`, so `W_{alpha gamma,epsilon} in SO(6)`. By the exact `Spin(6)=SU(4)` exterior-square covering already used in the campaign, `W_{alpha gamma,epsilon}O` is the exterior square of another genuine `4 x 4` unitary. Since `U` is a global support maximizer,

\[
s(O)\ge s(W_{\alpha\gamma,\epsilon}O).\tag{13}
\]

For every block column `beta`, (12) sends

\[
B_{\alpha\beta}\mapsto Z_\epsilon B_{\gamma\beta},
\qquad
B_{\gamma\beta}\mapsto -Z_\epsilon^T B_{\alpha\beta}.\tag{14}
\]

Hence

\[
D_{\alpha\beta}\mapsto\epsilon D_{\gamma\beta},
\quad D_{\gamma\beta}\mapsto\epsilon D_{\alpha\beta},
\quad
R_{\alpha\beta}\leftrightarrow R_{\gamma\beta}.\tag{15}
\]

Substitution in (3) gives the exact difference

\[
s(O)-s(W_{\alpha\gamma,\epsilon}O)
=T^L_{\alpha\gamma}-\epsilon C^L_{\alpha\gamma}.\tag{16}
\]

Both signs in (13) therefore give

`T^L-C^L>=0` and `T^L+C^L>=0`,

which is exactly (8). The column statement follows by the same argument with right block-plane multiplication. `QED`

## 4. Global mixed-minor corollary and relation to the pair Hessian

Summing (6) over the three row pairs gives

\[
\sum_{\alpha<\gamma}T^L_{\alpha\gamma}
=2k+3(x-\bar c).\tag{17}
\]

Indeed every `KD` term occurs twice, while double stochasticity gives

\[
\frac12\sum_{\alpha<\gamma,\beta}
(X_{\alpha\beta}-X_{\gamma\beta})
(R_{\alpha\beta}-R_{\gamma\beta})
=3(x-\bar c).\tag{18}
\]

The same identity holds on the column side. Therefore every global maximizer obeys

\[
\boxed{
2k+3(x-\bar c)
\ge
\max\left\{
\sum_{\alpha<\gamma}|(KD^T+DK^T)_{\alpha\gamma}|,
\sum_{\beta<\delta}|(K^TD+D^TK)_{\beta\delta}|
\right\}.
}\tag{19}
\]

This strictly refines the previously known scalar nonnegativity `2k+3(x-c)>=0`: it keeps the orientation-swapped cross terms which disappear after taking only a Hessian trace.

Using account02/B07's exact singular-safe identity

\[
-\operatorname{Tr}H_{\rm pair}=8\{2k+3(x-\bar c)\},\tag{20}
\]

(19) can equivalently be read as an explicit lower payment in the pair Hessian for the off-diagonal symmetric parts of `KD^T` and `K^TD`.

## 5. Direct progress on the lead's positive-reserve branch

Suppose a genuine global maximizer violates the target by `gamma>0`. Put

\[
\mathcal R:=3d-\Delta-G/2.\tag{21}
\]

The campaign lead proves `0<gamma<=R/4`. Its two exact inequalities are

\[
k\ge\gamma+\Delta,
\qquad
k\le3d-3\gamma-G/2.\tag{22}
\]

Because `k+y=d+gamma`, define

\[
T:=2k+3y=3(d+\gamma)-k.\tag{23}
\]

Then (22) gives the exact sandwich

\[
6\gamma+\frac G2\le T\le3d+2\gamma-\Delta.\tag{24}
\]

The new theorem adds all six pairwise gates (8),(11), and in particular

\[
\mathcal C(D,K):=
\max\left\{
\sum_{\alpha<\gamma}|(KD^T+DK^T)_{\alpha\gamma}|,
\sum_{\beta<\delta}|(K^TD+D^TK)_{\beta\delta}|
\right\}
\le T.\tag{25}
\]

Thus every residual violator must satisfy

\[
\boxed{
\max\left\{\mathcal C(D,K),\ 6\gamma+G/2\right\}
\le T\le3d+2\gamma-\Delta.
}\tag{26}
\]

Since `D=(1/4)E^TPE`, the new term in (26) is an explicit `P`-side restriction coupled to the same point's `R` through the six stronger pairwise inequalities. Eliminating `gamma` with the lead's ceiling gives the gamma-free necessary band

\[
\boxed{
\mathcal C(D(P),K)
\le 3d-\Delta+\frac{\mathcal R}{2}
=\frac92d-\frac32\Delta-\frac14G.
}\tag{27}
\]

Equation (27) is not by itself a proof: it is a new exact filter on the source-valid positive-reserve core. The important gain is that the abstract low-frequency relaxation from the lead cannot be promoted without satisfying these genuine `P/R` orientation-swap constraints.

## 6. Exact negative-control application: the previous generic parity witness is expelled from the maximizer core

Apply (11) to the exact rational true-unitary datum from account01/B07's earlier `MOC4-PARITY-SLACK-v1` refutation. That datum is simple-spectrum, invertible, irreducible, has all 16 unitary entries nonzero and all designated complementary minors nonzero; it refuted only an overstrong proof gate and was **not** an MOC4 counterexample.

For the column complementary-pair planes `12|34` and `14|23`, exact `Fraction` arithmetic gives

\[
T^R=
\frac{24555162551497262400033111}
{156250012500000250000000000},\tag{28}
\]

\[
C^R=
-\frac{27515600499968722687177263}
{156250012500000250000000000}.\tag{29}
\]

Therefore

\[
T^R-|C^R|
=-\frac{370054743558932535893019}
{19531251562500031250000000}<0.\tag{30}
\]

So the orientation-reversing block-plane swap has **strictly larger** support by the exact positive amount

\[
\frac{370054743558932535893019}
{19531251562500031250000000}
\approx0.01894680135447.\tag{31}
\]

This gives an exact finite reason that the earlier hard generic datum cannot be the global maximizer of its support direction. It is consistent with, but stronger and more structural than, the previously observed positive first derivative along one chosen Givens direction.

The source-exact verifier for (28)–(31) is `verify_biorientation_gate.py`; the captured exact output is `VERIFY_OUTPUT.txt` in this run directory. No floating-point arithmetic supports the sign claim.

## 7. Compact conditional end-to-end argument after this run

Assume the following single residual statement:

> **`MOC4-RESIDUAL-PR-BIORIENTATION-v1` (OPEN).** On the simple-spectrum irreducible positive-reserve branch, no genuine exterior-square point `(P,D,R)` can simultaneously be a global support maximizer with positive gap, satisfy `D=(1/4)E^TPE`, the full block-orthogonality relations, account03/B09's 16 odd-twist mass inequalities, and all six bi-orientation gates (8),(11) together with the lead sandwich (26).

Then MOC4 for `n=4` follows. Indeed, if a support direction failed, take a global maximizing true unitary. The account02/B08 boundary/circle machinery removes repeated/common-block/common-circle solved faces and retains the explicit boundary exceptions rather than discarding them. The lead's V4 and pair-specific roofs force the remaining maximizer into the positive-reserve branch. The present theorem adds six exact same-unitary orientation-swap conditions; account03/B09 adds the orientation-sensitive channel-mass constraints. The displayed residual statement excludes the remaining branch, contradiction. Hence every support direction is bounded by the 24 endpoint products, which is equivalent to the target convex-hull inclusion. Singular/repeated cases return through the already source-valid polynomial/boundary reductions, not by inversion or genericity assumptions.

The first essential missing implication is therefore no longer merely “use P/R compatibility”: it is to close the explicitly constrained feasible set in `MOC4-RESIDUAL-PR-BIORIENTATION-v1`, or produce an actual common-unitary/spectral counterexample satisfying all six gates. A witness from an independent-bistochastic, 48-colour, low-frequency, or formal `S4` relaxation does not count.

## 8. Status and nonclaims

- `MOC4-BIORIENTATION-PAIR-GATE-v1`: **proved** for every global true-unitary support maximizer.
- Row and column aggregate gate (19): **proved**.
- Residual sandwich (26) and gamma-free band (27): **proved**, conditional only on the already proved lead inequalities.
- The earlier parity-slack generic datum: **exactly excluded from the global-maximizer core** by one column bi-orientation gate; it remains a valid counterexample only to the older parity-slack proof mechanism.
- `MOC4-RESIDUAL-PR-BIORIENTATION-v1`: **open**.
- Full MOC4: **open**.

No benchmark material, sealed answers, credentials, scheduler identifiers, machine-local paths, unrelated private data, email, Drive, public posting, paid model/API/Codex call, remote workflow, or permission change was used. The only executable check is standard-library exact rational arithmetic on already authorized mathematical data.
