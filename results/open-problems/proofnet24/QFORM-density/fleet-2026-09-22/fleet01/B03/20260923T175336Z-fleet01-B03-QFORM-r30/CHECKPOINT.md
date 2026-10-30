SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T17:53:36Z.
attacking: row-marginal-free rank-two cross-volume L2/collision theorem, then square/fusion receivers for linear small-ball scaling.

# Early substantive calculation

Programme: `QFORM-DENSITY-3EIG-20260922`.
Owner continuation consumed: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.
Brain state: `WITHOUT_VERIFIED_BRAIN`.

Let

`R = F(X_I)+2 X_I^T B X_J+G(X_J)`

for two disjoint original-coordinate product banks, with arbitrary quadratic-plus-affine internal functions `F,G`.  Let `b_i` be the rows of `B` and

`Z_2 = sum_{i<j} |b_i wedge b_j|^2 = e_2(BB^T)>0`.

Define pair-volume row marginals

`alpha_i = Z_2^(-1) sum_{j!=i}|b_i wedge b_j|^2`, so `sum_i alpha_i=2`.

The mechanism is a complete three-case promotion tree.

1. **Diffuse:** if every `alpha_i<=1/2`, Cauchy--Schwarz in the `I` bank and the weighted-subset Fourier lemma with `k=0, ell=2` give

`|phi_R(t)|^2 <= min{1, 8*pi^2*e /(sqrt(Z_2)|t|^2)}`,

hence

`|phi_R(t)| <= min{1, K_2 Z_2^(-1/4)|t|^(-1)}`,

with `K_2=2*pi*sqrt(2e)=14.65015120674476...`.

2. **One heavy row:** if `alpha_i>1/2`, put `m=b_i`, `c_j=b_j(I-P_m)`, `Z_1'=sum_{j!=i}||c_j||^2`.  Then the exact identity

`||m||^2 Z_1' = alpha_i Z_2`

holds.  If every projected one-volume marginal `beta_j=||c_j||^2/Z_1'<=1/2`, apply the completed partner theorem `fleet02/B03@38920ffa423ec07886112206314249deb7294dd4`, Theorem 2.1 / its source grouped-crossing estimate, with `M_H<=1`, `S=||m||`, `F=sqrt(Z_1')`:

`|phi_R(t)| <= min{1, 2*pi*(alpha_i Z_2)^(-1/4)|t|^(-1)}`

`< min{1, 2*pi*2^(1/4) Z_2^(-1/4)|t|^(-1)}`,

strictly better than the diffuse constant.

3. **Two heavy rows:** if some `beta_j>1/2`, then

`|b_i wedge b_j|^2 = ||m||^2||c_j||^2 = alpha_i beta_j Z_2 > Z_2/4`.

Promote the two genuine physical coordinates `i,j` to a 2D hub.  The full hub-to-complement cross matrix has singular-value product `S_H>=|b_i wedge b_j|>sqrt(Z_2)/2`.  The exact-rank-two grouped crossing/Plancherel estimate, with the physical 2D hub density cap `1` and the complementary 2D projection cap `2`, gives

`|phi_R(t)| <= min{1, pi*sqrt(2)*S_H^(-1/2)|t|^(-1)}`

`< min{1, 2*pi Z_2^(-1/4)|t|^(-1)}`.

Therefore the diffuse envelope dominates all cases.  Immediate consequences to complete in the final report:

`||p_R||_2^2 <= 4*sqrt(2e) Z_2^(-1/4)`,

`int |t|^(-1/2)|phi_R(t)|^2 dt <= (16/3)*sqrt(2*pi)*(2e)^(1/4) Z_2^(-1/8)`,

and the one-copy half-Riesz bound

`sup_s E|R-s|^(-1/2) <= 8*(2e)^(1/4) Z_2^(-1/8)`.

Thus one genuine completed physical square `d(Z+h)^2` gives the linear small-ball/density certificate

`||p_Q||_infinity <= 8*(2e)^(1/4)|d|^(-1/2) Z_2^(-1/8)`.

This is a row-marginal-free critical two-volume compiler.  It does not prove the full conjecture; its remaining connection is structural extraction of either this rank-two cross aggregate plus a third smoothing resource, or a previously paid branch.
