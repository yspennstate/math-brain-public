# fleet03/B18 — one-pivot extension of the diffuse quadratic-density mechanism

Programme: QFORM-DENSITY-3EIG-20260922, control revision 2026-09-22.5.  
Run: `20260922T125414Z-fleet03-B18-qform-r2`.  
Assignment: Literature-to-proof transfer.  
Status: supporting theorem proved; full universal conjecture OPEN.  
Execution: WITHOUT_VERIFIED_BRAIN.

## 1. Exact target and correction state

The active target is: for independent real coordinates `X_i` with probability densities `0 <= f_i <= 1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove

`P(X^T A X in [t,t+h]) <= C h`

for one universal finite `C`, all real `t`, all `h>0`, all dimensions, all permitted laws and all such matrices.

This report does not add moments, log-concavity, Gaussianity, compact support, identical distributions, or independence after rotation. It also does not use the refuted law-uniform pointwise one-dimensional Fresnel bound, the refuted cross-minor-alone claim, the refuted conditional sum/difference density cap, or the refuted assertion that three large eigenvalues force one useful Schur rank-two cross block.

The most recent correction relevant to this report is `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`: the bare spectral hypothesis does not force one physical scalar pivot whose Schur complement has a useful disjoint rank-two cross block. The theorem below is therefore stated as a structural sufficient condition, not as an extraction theorem.

## 2. Primary-source hypothesis audit

### 2.1 Livshyts–Paouris–Pivovarov

Galyna Livshyts, Grigoris Paouris and Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, prove for a product probability density `f(x)=prod_i f_i(x_i)` with each `||f_i||_infinity <= 1` that every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. Their Theorem 3.3 records the normalized geometric Brascamp–Lieb inequality used in the diffuse-frame proof. The hypotheses are exactly product density plus one-dimensional `L^infinity` caps; there is no moment, support, Gaussian, or log-concavity hypothesis.

This source may be applied only while the variables are still original independent coordinates. An eigenvector rotation does not preserve the product law and is not used below.

### 2.2 Beckner

William Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159–182, supplies the sharp Hausdorff–Young inequality. The inequality is for complex-valued functions, so multiplying each original one-dimensional density by an arbitrary modulus-one separable phase does not invalidate it. This is the precise literature point that permits diagonal quadratic and linear perturbations inside the diffuse residual.

### 2.3 Source-valid completed inputs

I use two completed, source-pinned mathematical inputs.

1. `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, complete supporting proof at
   `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb:proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.
   Its exact theorem is: if `U^T U=I_r`, `r>=3`, every row leverage `c_i=||u_i||^2 <= 1/2`, `Lambda` is real symmetric invertible, and `V_i` are arbitrary real measurable coordinate functions, then

   `R=(U^T Y)^T Lambda(U^T Y)+sum_i V_i(Y_i)`

   has a bounded continuous density with

   `M := ||p_R||_infinity <= [r/(r-2)] B(U)^(2/r) |det Lambda|^(-1/r) <= [e r/(r-2)] |det Lambda|^(-1/r)`,

   where `B(U)=prod_{c_i>0}(1-c_i)^(-(1-c_i)/2)`.

2. The required compatible partner result, fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, complete proof at
   `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.
   If `R` has density bounded by `M`, and conditional on `R=r` a variable `V_r` has density bounded by one, with no independence assumption between `R` and `V_R`, then

   `T=R+a V_R^2`, `a!=0`,

   satisfies `||p_T||_infinity <= 2 sqrt(M/|a|)`.

The second input is applied substantively below; it is not merely cited.

## 3. New theorem: QFORM-PIVOT-DIFFUSE-RESIDUAL-v1

### Theorem

Let `Q=X^T A X` with independent original coordinates having densities bounded by one. Choose an original-coordinate principal index set `I={0} union J`, and write its principal matrix after ordering coordinate `0` first as

`B = [[a, b^T],[b,C]]`, with `a != 0`.

Let

`S = C - b b^T/a`

be the physical Schur complement. Assume that, in the original coordinates indexed by `J`,

`S = D + U Lambda U^T`,

where

- `D` is an arbitrary real diagonal matrix;
- `U^T U=I_r` with `r>=3`;
- every row leverage `c_i=||u_i||^2` is at most `1/2`;
- `Lambda` is real symmetric and invertible.

All entries of the ambient matrix `A` outside this selected principal block, including all couplings to outside coordinates, are arbitrary.

Then `Q` is absolutely continuous and

`||p_Q||_infinity <= 2 sqrt(r/(r-2)) B(U)^(1/r) |a|^(-1/2) |det Lambda|^(-1/(2r))`

and therefore

`boxed( ||p_Q||_infinity <= 2 sqrt(e r/(r-2)) |a|^(-1/2) |det Lambda|^(-1/(2r)) ).`

Equivalently, the same constant pays every interval small ball:

`P(Q in [t,t+h]) <= 2 sqrt(e r/(r-2)) |a|^(-1/2) |det Lambda|^(-1/(2r)) h`.

For `r=3`, `|a|>=1`, `|det Lambda|>=1`, this gives the explicit universal branch constant

`2 sqrt(3e) = 5.7113380167...`.

This theorem proves bounded density, not continuity of the final density. The residual density is continuous, but the dependent square-smoothing step presently yields only an `L^infinity` density.

### Proof

Condition on every original coordinate outside `I`. Since the original coordinates are independent, the selected coordinates retain their original independent laws and their one-dimensional density caps. Outside variables create only deterministic linear and constant terms. Suppress the fixed outside value from notation and write the selected scalar variable as `Z` and the remaining selected variables as `Y`.

The conditioned polynomial has the form

`Q_w(Z,Y) = a Z^2 + 2 Z b^T Y + Y^T C Y + ell_0 Z + 2 ell^T Y + c`.

Completing the square only in the physical coordinate `Z` gives

`Q_w(Z,Y) = a (Z + m_w(Y))^2 + R_w(Y)`,

where `m_w` is affine in `Y` and

`R_w(Y) = Y^T S Y + 2 tilde_ell_w^T Y + tilde_c_w`.

By the assumed decomposition `S=D+U Lambda U^T`, this residual is exactly

`R_w(Y)=(U^T Y)^T Lambda(U^T Y)+sum_{i in J} [D_ii Y_i^2 + 2 tilde_ell_{w,i}Y_i] + tilde_c_w`.

The bracketed terms are coordinate-separable phases. `QFORM-DIFFUSE-SEPARABLE-PHASE-v1` therefore gives, uniformly in the outside conditioning value,

`||p_{R_w}||_infinity <= M := [r/(r-2)] B(U)^(2/r) |det Lambda|^(-1/r)`.

Now disintegrate the law of `Y` over `R_w(Y)=r`. Before this disintegration, `Z` is independent of `Y`. Hence for almost every `r`, the conditional law of

`V_r := Z + m_w(Y)`

given `R_w(Y)=r` is a mixture of translations of the original density of `Z`. More explicitly, for a regular conditional law `mu_r(dy)` of `Y` given `R_w=r`,

`h_r(v)=integral f_Z(v-m_w(y)) mu_r(dy) <= 1`.

Thus the exact hypothesis of fleet04/B18's dependent square-smoothing lemma is satisfied, despite the fact that `V_r` and `R_w` are generally dependent. Applying it yields

`||p_{Q_w}||_infinity <= 2 sqrt(M/|a|)`.

Substituting `M` gives the first displayed bound. The inequality `B(U)<=exp(r/2)` gives the simpler second bound.

The constant is uniform in the conditioned outside coordinates. Averaging the conditional densities therefore preserves the same `L^infinity` bound for the full `Q=X^TAX`. QED.

## 4. Why this is a genuine mechanism change

The preceding B18 run used Banks's bilinear density theorem on a physical bipartite block, and its remaining gap was extraction/aggregation of a strong physical cross block. The new theorem does not ask for a bipartite zero-within-side block or for a rank-two Schur cross minor. It instead pays a diffuse curved Schur residual and then reincorporates one fully nonseparable physical pivot through a dependent square. This survives the new correction showing that a useful single Schur rank-two cross block need not exist.

It is also stricter than merely conditioning away the pivot: the pivot is not independent of the residual after completing the square, and the partner's dependent-smoothing lemma is exactly what pays this dependence.

## 5. Explicit nonseparable target example

Take six residual coordinates and

`U=(I_3;I_3)/sqrt(2)`, `Lambda=diag(2,2,-2)`, `D=(1/10)I_6`.

Then every row leverage is `1/2`, `B(U)=2^(3/2)`, `|det Lambda|=8`, and the diffuse residual theorem gives the sharp branch value

`M = 3`.

Set `a=1`, `b=(1/10)(1,1,1,1,1,1)^T`, and

`C=S+b b^T`, where `S=D+U Lambda U^T`.

The resulting seven-variable physical block

`B=[[1,b^T],[b,C]]`

is genuinely coupled through the pivot. Its Schur complement is exactly `S`, so the new theorem gives

`boxed( ||p_{X^T B X}||_infinity <= 2 sqrt(3) = 3.4641016151... ).`

It also genuinely meets the target's three-large-eigenvalue hypothesis. At `b=0`, `diag(1,S)` has eigenvalues `21/10,21/10,-19/10,1,1/10,1/10,1/10`. The coupling perturbation is

`E=[[0,b^T],[b,b b^T]]`

and

`||E||_op <= 2||b||+||b||^2 = sqrt(6)/5+3/50 < 0.55`.

Weyl's inequality therefore leaves two positive eigenvalues above `21/10-0.55>1` and one negative eigenvalue below `-19/10+0.55<-1`. Thus at least three eigenvalues have modulus greater than one. This example is indefinite, rotated relative to the independent coordinates, and has nonzero pivot-to-residual couplings.

## 6. Literature routes that still do not transfer

The source audit also rules out several tempting shortcuts.

- Gaussian quadratic-form density formulas do not transfer: the permitted inputs have arbitrary bounded densities and no moment assumptions.
- Carbery–Wright-type polynomial small-ball estimates require log-concavity and moreover have the wrong `epsilon^(1/degree)` scaling for a density theorem unless additional structure is supplied.
- Discrete quadratic Littlewood–Offord theorems such as Kwan–Sauermann control atom probabilities for discrete product variables, not the length-linear interval probability required here.
- A fixed restricted-invertibility/minor theorem with an `n`-dependent singular-value loss cannot by itself give a dimension-free density constant. The current correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` gives an even sharper source-valid obstruction to a one-minor-only closure.

## 7. Exact remaining implication

The full conjecture remains OPEN. The new theorem says that one broad structural branch is now closed:

> a physical nonzero scalar pivot whose Schur residual contains a diagonally perturbed diffuse rank-`r>=3` component with leverage at most `1/2` and determinant scale bounded below.

The next universal implication is structural, not analytic inside this branch:

> Starting only from the hypothesis that `A` has at least three eigenvalues of modulus at least one, prove that either (i) some physical block has the pivot-diffuse-residual structure above with dimension-free scales, or (ii) a different aggregate mechanism (for example the high-cardinality hyperbolic-square aggregation seen in the current counterexample to single-Schur extraction) supplies the density bound.

Because a single useful Schur rank-two cross block is now known not to be forced, the successor should aggregate many weak physical interactions or prove a product-preserving heavy/diffuse dichotomy rather than keep searching for one fixed minor.

## 8. Source pins and scope

Primary literature:
- Livshyts, Paouris, Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949; Israel J. Math. 216 (2016).
- W. Beckner, *Inequalities in Fourier analysis*, Ann. Math. 102 (1975), 159–182, DOI 10.2307/1970980.

Internal completed dependencies:
- diffuse separable phase: `773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, exact report path above;
- fleet04/B18 dependent square smoothing: `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, exact report path above.

The current theorem is a conditional structural theorem, not a full solution and not a novelty claim. No external publication, email, remote workflow or paid model/API call is involved.
