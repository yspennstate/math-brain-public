# account04/B08 MOC4 report — sharp exterior-blockrow energy and mixed-Schur boundary splitting

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T091158Z-account04-B08-MOC4-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`; `full_brain_connected=false`.

## 1. Exact target and source-bound state

For every complex normal `4 x 4` pair `A,B`, with spectra `a_i,b_i` counted with multiplicity, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_i(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

No arbitrary bistochastic replacement, independently selected compound-minor array, or non-source unitary surrogate is used below.

The latest complete campaign-lead report actually consumed is

- `proofnet24/collective-MOC4/account03/B07/20260922T074824Z-account03-B07-MOC4-r13/REPORT.md`, blob `7724d19f793eb934c5fcc2b469bb9d0a108da4eb`, theorem `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`.

It reduces a strict generic support counterexample to a true-unitary global maximizer with gap `gamma>0` and two branches: a mixed-Schur pair-Hessian boundary (`MSQR`) or the all-pair-negative-definite branch (`NDI`). On `MSQR`, the pair kernel is a full-Hessian kernel and the exact fourth-order necessary condition is

\[
q+3R_{\rm pair}+3R_{\rm cross}\le0. \tag{1}
\]

The assigned OTHER-account partner actually consumed is **account01/B09**:

- `proofnet24/collective-MOC4/account01/B09/20260922T074619Z-b09-moc4-r11/REPORT.md`, blob `09d12f95bbf37648773afe6ee08acf65343f149a`, theorem `MOC4-MIXED-SCHUR-GAP-CONDITIONING-CEILING-v1`.

For a generic mixed-Schur row edge `e={alpha,gamma}`, let

\[
h_e=\frac{\lambda_\alpha\lambda_\gamma}{\lambda_\alpha+\lambda_\gamma}>0
\]

be its exact spectral-covariance conditioning parameter, let `E_alpha,E_gamma` be the two exterior block-row nonconformality energies, and put

\[
Q=T^2-C^2=4(\gamma+r_\tau)(\gamma+r_{\tau^c}). \tag{2}
\]

The partner proves

\[
E_\alpha+E_\gamma\ge 4Qh_e. \tag{3}
\]

Its published ceiling used only the crude separate bounds `E_alpha,E_gamma<=1`, hence `8 h_e(gamma+r_tau)(gamma+r_{tau^c})<=1`.

I also consume the newest compatible account03/B20 result

- `proofnet24/collective-MOC4/account03/B20/20260922T084401Z-account03-B20-MOC4-r11/REPORT.md`, blob `197308f44d9e273a0d73ba89f691d3e85b4c23aa`, theorem `MOC4-MSQR-ORTHOGONAL-ROOT-FLOOR-v1`.

Writing `Lambda=-(q+3R_pair)>=0`, every explicit adjacent-root cubic residual matrix `R` obeys

\[
3N_\epsilon(R)\le2\Lambda(T-\epsilon C),\qquad \epsilon=\pm1, \tag{4}
\]
where
\[
N_+(R)=\|R\|_F^2+2\det R,\qquad N_-(R)=\|R\|_F^2-2\det R. \tag{5}
\]

Finally, for the `C=0` exceptional cross-root algebraic stratum I use account01/B07

- `proofnet24/collective-MOC4/account01/B07/20260922T080631Z-account01-B07-MOC4-r13/REPORT.md`, blob `721ef994504083caf2a130649bdd4a03c4d9263f`, equation
\[
\operatorname{cof}(Z_*)P+Z_*Q=0. \tag{6}
\]

## 2. Compact conditional end-to-end deduction

Assume a strict MOC4 support counterexample. By the campaign genericization/maximization state, take a genuine global maximizer with support gap `gamma>0`. Scalar Spin(4) saturation is already excluded, so the generic proof tree is:

1. `MSQR`: at least one genuine pair Hessian block is singular at mixed-Schur equality;
2. `NDI`: all six pair Hessian blocks are negative definite.

For `MSQR`, (1), the explicit cross-root gates, and the partner covariance payment (3) must all hold simultaneously. This run sharpens the previously unpaid `MSQR` inequalities in two independent exact ways:

- it proves the optimal universal bound `E_alpha<=1/2`, improving the partner gap-conditioning ceiling by a factor two in the product;
- it removes the weak `C=0 => det Q=0` replacement and gives the full rank-one splitting of the cross-root annihilator.

Thus a full proof follows once the remaining positive-gap survivor is excluded under these sharper gates (and the separate `NDI` branch is closed).

## 3. New theorem: sharp block-row nonconformality bound

### `MOC4-EXTERIOR-BLOCKROW-HALF-ENERGY-v1`

Let `O in SO(6)` be any genuine exterior-square matrix, partitioned into a `3 x 3` array of real `2 x 2` blocks `B_{alpha beta}`. For one block row `alpha`, put

\[
R_\beta=\frac12\|B_{\alpha\beta}\|_F^2,\qquad D_\beta=\det B_{\alpha\beta},
\]
and
\[
E_\alpha=\sum_{\beta=1}^3(R_\beta^2-D_\beta^2).
\]

Then

\[
\boxed{0\le E_\alpha\le\frac12.} \tag{7}
\]

Moreover equality `E_alpha=1/2` holds **if and only if**, after no change of the matrix itself but merely describing the two-dimensional row plane in a suitable orthonormal basis, exactly two block Gramians are complementary rank-one projections and the third is zero:

\[
B_{\alpha\beta_1}B_{\alpha\beta_1}^T=xx^T,\qquad B_{\alpha\beta_2}B_{\alpha\beta_2}^T=x_\perp x_\perp^T,\qquad B_{\alpha\beta_3}=0. \tag{8}
\]

#### Proof

Set
\[
S_\beta=B_{\alpha\beta}B_{\alpha\beta}^T\succeq0.
\]
Row orthogonality of `O` gives
\[
\sum_\beta S_\beta=I_2. \tag{9}
\]
Write
\[
S_\beta=r_\beta I_2+\begin{pmatrix}x_\beta&y_\beta\\y_\beta&-x_\beta\end{pmatrix},\qquad w_\beta=(x_\beta,y_\beta).
\]
Then
\[
r_\beta=\frac12\operatorname{tr}S_\beta=R_\beta,\quad D_\beta^2=\det S_\beta=r_\beta^2-|w_\beta|^2,
\]
so
\[
E_\alpha=\sum_\beta |w_\beta|^2. \tag{10}
\]
Equation (9) gives
\[
\sum_\beta r_\beta=1,\qquad \sum_\beta w_\beta=0. \tag{11}
\]
Positivity gives `|w_beta|<=r_beta`.

Let
\[
s=\sum_\beta|w_\beta|,\qquad m=\max_\beta|w_\beta|.
\]
Because the vectors sum to zero, a largest one is the negative sum of the others, hence
\[
m\le s-m,\qquad m\le s/2. \tag{12}
\]
Also
\[
s\le\sum_\beta r_\beta=1. \tag{13}
\]
Therefore
\[
E_\alpha=\sum_\beta|w_\beta|^2\le ms\le\frac{s^2}{2}\le\frac12,
\]
proving (7).

Equality forces equality in every displayed inequality: `s=1`, `m=1/2`, every nonzero `|w_beta|` equals `m`, and `r_beta=|w_beta|` on every active block. Hence exactly two `w_beta` are nonzero, each has norm `1/2`, and they are opposite. The two active `S_beta` therefore have eigenvalues `(1,0)` and are complementary rank-one projections; the third vanishes. Conversely (8) gives two contributions `1/4`, hence `E_alpha=1/2`. QED.

The constant `1/2` is sharp. A signed `6 x 6` permutation in `SO(6)` that sends the two scalar axes of one block row into two different block columns has `E_alpha=1/2`.

## 4. Application to the assigned partner: factor-two stronger MSQR conditioning ceiling

Combining the partner lower bound (3) with (7) on both participating block rows gives

\[
1\ge E_\alpha+E_\gamma\ge4Qh_e.
\]

Hence every generic positive-gap mixed-Schur survivor satisfies

\[
\boxed{4Qh_e\le1.} \tag{14}
\]

Using (2),

\[
\boxed{16h_e(\gamma+r_\tau)(\gamma+r_{\tau^c})\le1.} \tag{15}
\]

In particular,

\[
\boxed{\gamma\le\frac1{4\sqrt{h_e}}.} \tag{16}
\]

This is a strict factor-two improvement in the product inequality over the assigned partner's published bound `8 h_e(...)<=1` (equivalently a factor `sqrt(2)` improvement in the gap ceiling).

### Equality stratum

If equality holds in (14), then necessarily

\[
E_\alpha=E_\gamma=\frac12, \tag{17}
\]

and both rows have the exact two-rank-one-block structure (8), while the covariance lower bound (3) is also saturated. Therefore saturation of the sharpened conditioning ceiling is not a generic interior event: it lies on an explicitly characterized exterior-minor boundary.

I call (14)--(17) **`MOC4-MSQR-SHARP-GAP-CONDITIONING-CEILING-v1`**.

## 5. New residual anisotropy gate from the B20 cross reserve

Multiply the two B20 inequalities (4):

\[
9N_+(R)N_-(R)\le4\Lambda^2(T^2-C^2)=4\Lambda^2Q.
\]

By (14), `Q<=1/(4h_e)`, hence

\[
\boxed{N_+(R)N_-(R)\le\frac{\Lambda^2}{9h_e}.} \tag{18}
\]

For singular values `s_1(R)>=s_2(R)>=0`,
\[
N_+(R)N_-(R)=\|R\|_F^4-4(\det R)^2=(s_1(R)^2-s_2(R)^2)^2.
\]
Therefore every explicit adjacent-root residual at a positive-gap mixed-Schur survivor satisfies

\[
\boxed{|s_1(R)^2-s_2(R)^2|\le\frac{\Lambda}{3\sqrt{h_e}}.} \tag{19}
\]

This is **`MOC4-MSQR-RESIDUAL-ANISOTROPY-GATE-v1`**. It is denominator-free and couples the lead/B20 quartic reserve directly to the partner's exact spectral conditioning. In particular, when the available quartic budget is small, every surviving cross cubic residual must be nearly conformal; when `Lambda=0`, B20's stronger orientation equations already force `R=0`.

## 6. Degenerate `C=0` mixed-Schur boundary: full rank-one cross split

The account01/B07 cross-root gate (6) treated `C=0` by multiplying with `Z_*^T`, obtaining only `det Q=0`. The rank-one geometry yields more.

### `MOC4-C0-CROSS-ROOT-RANKONE-SPLIT-v1`

On the strict scalar-sector mixed-Schur boundary, if `C=0`, then
\[
\det Z_*=2C=0,\qquad \|Z_*\|_F^2=4T>0,
\]
so `Z_*` has rank one. Write
\[
Z_*=\rho x y^T,\qquad \operatorname{cof}(Z_*)=\pm\rho x_\perp y_\perp^T,
\]
with unit vectors `x,y` and perpendicular unit vectors `x_perp,y_perp`.
Then (6) becomes
\[
x_\perp(y_\perp^TP)\pm x(y^TQ)=0.
\]
Because `x` and `x_perp` are linearly independent, both row coefficients vanish:

\[
\boxed{y_\perp^TP=0,\qquad y^TQ=0.} \tag{20}
\]

Equivalently, there are row vectors `p^T,q^T` such that
\[
\boxed{P=y\,p^T,\qquad Q=y_\perp\,q^T.} \tag{21}
\]

Thus
\[
\boxed{\operatorname{rank}P\le1,\quad \operatorname{rank}Q\le1,\quad \operatorname{col}(P)\perp\operatorname{col}(Q).} \tag{22}
\]

In particular both `det P=0` and `det Q=0`; the previous exceptional gate `det Q=0` is only half of the exact rank-one splitting condition. The analogous equation from the other endpoint of the singular pair supplies the corresponding second adjacent-root split.

This is an exact characterization of a genuine degenerate MSQR stratum, not a claim that every stationary or nonmonomial point is a counterexample.

## 7. Exact verification

The analytic proofs above do not depend on computation. A standard-library exact verifier was run only as an independent transcription/sharpness check.

It verifies:

1. the sharp signed-permutation witness with block-row energies `(1/2,1/2,0)`;
2. over all `720` unsigned scalar permutations, no block-row energy exceeds `1/2`;
3. a dense rational `SO(6)` matrix built from rational Givens rotations has all three exact energies below `1/2`;
4. for all `2401` integer `2 x 2` residual matrices with entries in `[-3,3]`,
   \[
   N_+=(a+d)^2+(c-b)^2,\quad N_-=(a-d)^2+(b+c)^2,
   \]
   and
   \[
   N_+N_-=\|R\|_F^4-4(\det R)^2.
   \]

The terminal marker is `PASS MOC4-B08-BLOCKROW-HALF-ENERGY-v1`.

## 8. First essential missing implication

The `MSQR` branch is now narrower. A positive-gap survivor must simultaneously satisfy:

- the lead full-Hessian kernel and quartic reserve (1);
- the B20 four explicit cross-root payment inequalities;
- the sharpened conditioning ceiling (15);
- the residual anisotropy gate (19);
- the exact rank-splitting equations (20)--(22) on any `C=0` boundary;
- same-unitary exterior/minor compatibility, stationarity, cofactor-annulus and subgroup roofs.

The first unpaid implication is therefore

**`MOC4-MSQR-SHARP-RESIDUAL-BOUNDARY-CLOSURE-v1`**:

> Prove that no positive-gap true-unitary mixed-Schur maximizer can satisfy all of the preceding gates; in the equality/near-equality conditioning regime, exploit the two-rank-one-block boundary structure (8), while away from that boundary use the quantitative slack in (14) together with (18)--(19). Alternatively produce a genuine spectra/unitary target-level counterexample satisfying all gates.

After `MSQR` is closed, the campaign lead's separate `NDI` branch remains.

## 9. Verdict

`ESSENTIAL_STEP_APPLIED`.

The partner's mixed-Schur conditioning obstruction is strengthened by the optimal exterior block-row energy constant, its equality locus is completely characterized, the latest B20 cross-reserve acquires a new denominator-free singular-value anisotropy gate, and the exceptional `C=0` cross-root boundary is upgraded from one determinant equation to a full orthogonal rank-one split. Full MOC4 remains OPEN.
