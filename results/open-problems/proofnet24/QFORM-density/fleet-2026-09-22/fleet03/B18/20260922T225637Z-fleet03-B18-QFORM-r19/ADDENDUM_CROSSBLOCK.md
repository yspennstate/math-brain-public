# r19 addendum — arbitrary self-curvature across a rank>=3 physical cross block

This addendum strengthens `REPORT.md`. It was derived after the first report commit and is stored separately rather than rewriting that immutable file.

## Theorem D (`QFORM-CROSSBLOCK-RANKGE3-FRESNEL-v1`)

Let `X=(X_i)_{i in I}` and `Y=(X_j)_{j in J}` be two disjoint blocks of the original independent cap-one coordinates, with `I union J` all active coordinates. Let

`Q = F(X)+G(Y)+2 X^T B Y`,

where `F` and `G` are arbitrary real measurable functions and `B` is a real `|I| x |J|` matrix of rank `r>=3`. Let its nonzero singular values be

`sigma_1>=...>=sigma_r>0`.

Then `Q` has a continuous density and

`||p_Q||_infinity <= [2r/(r-2)] (prod_{ell=1}^r sigma_ell)^(-1/r).`  (D.1)

In particular, if `rank(B)=3`,

`||p_Q||_infinity <= 6 (sigma_1 sigma_2 sigma_3)^(-1/3).`  (D.2)

This applies directly to a completely general quadratic form under a physical bipartition:

`F(X)=X^T A_II X`, `G(Y)=Y^T A_JJ Y`, `B=A_IJ`.

Thus **arbitrary quadratic self-curvature on both sides is allowed**. The only structural payment is the full nonzero singular-volume of the physical cross block and the requirement `rank(B)>=3`.

### Proof

Take a thin SVD

`B=P Sigma R^T`,

where `P` and `R` have orthonormal columns in their respective original-coordinate blocks and `Sigma=diag(sigma_1,...,sigma_r)`. Put

`U=P^T X`, `V=R^T Y`.

Because `X` and `Y` live on disjoint original-coordinate sets, they are genuinely independent, hence `U` and `V` are independent. Livshyts–Paouris–Pivovarov Theorem 1.1 gives

`||p_U||_infinity <= 2^(r/2)`, `||p_V||_infinity <=2^(r/2)`  (D.3)

for proper marginals. If a block has exactly `r` coordinates, the corresponding orthogonal map preserves the product-density cap and gives the even better bound one; (D.3) still holds.

For each real frequency `t`, disintegrate the two original product laws over `U` and `V` and define the complex amplitudes

`a_t(u)=p_U(u) E[exp(i t F(X)) | U=u]`,

`b_t(v)=p_V(v) E[exp(i t G(Y)) | V=v]`.

Regular conditional expectations exist in these Euclidean spaces, and

`|a_t(u)|<=p_U(u)`, `|b_t(v)|<=p_V(v)`.

Consequently

`||a_t||_2 <=2^(r/4)`, `||b_t||_2 <=2^(r/4)`.  (D.4)

The characteristic function is exactly

`phi_Q(t)=int int exp(2 i t u^T Sigma v) a_t(u)b_t(v) du dv`.

With Fourier convention `hat b(xi)=int exp(i xi.v)b(v)dv`, the inner integral is `hat b_t(2t Sigma^T u)`. Cauchy–Schwarz, the change of variables `xi=2t Sigma^T u`, and Plancherel give for `t!=0`

`|phi_Q(t)|
 <= ||a_t||_2 (2|t|)^(-r/2) |det Sigma|^(-1/2) ||hat b_t||_2`

`= pi^(r/2) |t|^(-r/2) |det Sigma|^(-1/2) ||a_t||_2||b_t||_2`

`<= pi^(r/2) 2^(r/2) |t|^(-r/2) (prod sigma_ell)^(-1/2).`  (D.5)

Equivalently set

`D=pi^(r/2) 2^(r/2)(prod sigma_ell)^(-1/2)`.

Together with `|phi_Q(t)|<=1`,

`|phi_Q(t)|<=min(1,D|t|^(-r/2))`.

For `r>2`,

`int_R min(1,D|t|^(-r/2))dt
=2 [r/(r-2)] D^(2/r)`.

Therefore `phi_Q in L^1`. Fourier inversion gives a continuous density and

`||p_Q||_infinity
 <= [1/(2pi)] 2[r/(r-2)]D^(2/r)`

`= [r/(r-2)] * 2 * (prod sigma_ell)^(-1/r)`,

which is (D.1).

### General cap version

The same proof shows that if the aggregate densities satisfy `||p_U||_infinity<=M`, `||p_V||_infinity<=N`, then

`||p_Q||_infinity <= [r/(r-2)](MN)^(1/r)|det Sigma|^(-1/r).`  (D.6)

The theorem in `REPORT.md` is a special case of this general amplitude argument.

## Exact hypothesis comparison with Banks–Garza-Vargas–Kulkarni–Srivastava

Banks et al., arXiv:2005.08930, Theorem 2.1 and Corollary 2.4, study bilinear-plus-affine expressions in two arrays of genuinely independent bounded-density entries. In the scalar case their Corollary 2.4 has content already from two bilinear singular directions and can select the geometric mean of the top `j` singular values. It does **not** include arbitrary same-side nonlinear or quadratic terms `F(X)+G(Y)`.

Theorem D is complementary: it requires cross rank at least three and pays the geometric mean of **all nonzero cross singular values**, but in exchange arbitrary measurable self-phases `F(X)` and `G(Y)` survive exactly because they have modulus one inside the `L^2` amplitudes. Hence applying Banks directly after adding `X^T A_II X+Y^T A_JJ Y` would be a source-hypothesis error; Theorem D is the proved replacement for that branch.

## Partner application with fleet04/B18 r1

Use the completed dependence-safe square smoother from

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`:

if a residual `R` has density cap `M` and the shifted physical scalar pivot has conditional density cap one given `R`, then

`||p_{R+aV^2}||_infinity <=2 sqrt(M/|a|)`.

Suppose a physical scalar pivot `a!=0` has Schur residual `S`, and some bipartition `I union J` of all residual original coordinates has cross block `S_IJ` of rank `r>=3` with nonzero singular values `sigma_1,...,sigma_r`. The diagonal residual blocks `S_II,S_JJ` are unrestricted. Theorem D gives

`M <= [2r/(r-2)] (prod sigma_ell)^(-1/r)`.

Completing the pivot square and applying fleet04/B18 r1 therefore gives the actual inequality

`||p_{X^TAX}||_infinity
 <=2 sqrt{ [2r/(r-2)] / ( |a| (prod sigma_ell)^(1/r) ) }.`  (D.7)

For rank exactly three this is

`||p_Q||_infinity <=2 sqrt( 6 / (|a| (sigma_1 sigma_2 sigma_3)^(1/3)) ).`  (D.8)

This partner splice allows arbitrary same-side quadratic curvature in the Schur residual. The dependence induced by completing the scalar square is paid by the partner theorem; no post-completion independence is asserted. I record essential boundedness, not continuity, for this wrapper because the partner handoff does not assert continuity for its dependent-square conclusion.

## Relation to current corrections and the full target

The rank-two threshold is essential to the architecture: when `r=2`, the time majorant is `|t|^-1` and the `L^1` integral diverges logarithmically, exactly matching the known two-direction obstruction. Thus Theorem D does not contradict `QFORM-CROSSMINOR-ALONE-FALSE`, whose problematic mechanisms are rank two / insufficient cross curvature.

Nor does the theorem assert that `s_3(A)>=1` forces a good rank-three physical cross cut. The current correction family `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)` has all physical cuts of cross rank at most two. Therefore the remaining structural gap is an exhaustive dichotomy: either find a rank>=3 cross cut with a payable singular volume, or route the matrix into one of the already completed rank<=2 aggregate, scalar-pivot, ridge, or diagonal branches.

**Full QFORM remains OPEN.**
