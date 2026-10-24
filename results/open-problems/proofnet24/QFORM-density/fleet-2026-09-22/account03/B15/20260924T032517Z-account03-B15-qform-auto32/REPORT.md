SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T03:25:17Z.
attacking: stability of fixed-instance regularity certificates under nearly singular physical minors; seek an aggregate regularity compiler that avoids reciprocal-minor blow-up.

# account03/B15 — sharp square-root stability of the canonical output density under marginal L1 perturbations

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T032517Z-account03-B15-qform-auto32`  
Status: `SUBMASS-SQRT-C0-PROVED / MARGINAL-L1-TO-OUTPUT-LINF-HOLDER-PROVED / EXPONENT-SHARP / PARTNER-APPLIED / FULL-QFORM-OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact status and contribution

The unrestricted owner target remains OPEN. This run does not claim a matrix-uniform height constant under only `s_3(A)>=1`.

It proves a fixed-matrix regularity theorem which is stronger than qualitative continuity and which is useful for transporting any future smooth-input universal theorem to fully rough cap-one marginals.

Let `A` be a fixed real symmetric matrix with `rank(A)>=3`. Fix an original coordinate `j`. Then there is a finite constant `K(A,j)` such that:

1. every cap-one **subprobability** of mass `m` inserted in coordinate `j`, with arbitrary cap-one probability marginals in the other coordinates, has quadratic pushforward density `r` satisfying

   `r in C_0(R)` and `||r||_infinity <= K(A,j) sqrt(m)`;

2. if two cap-one probability densities `f_j,g_j` are used in coordinate `j`, with every other marginal fixed, then their canonical output densities satisfy

   `||p_f-p_g||_infinity <= sqrt(2) K(A,j) ||f_j-g_j||_1^(1/2)`;

3. for all marginals changed simultaneously, a telescoping sum gives

   `||p_f-p_g||_infinity <= sqrt(2) sum_j K(A,j)||f_j-g_j||_1^(1/2)`;

4. the exponent `1/2` is optimal already for the fixed owner-target matrix with quadratic form `Q=2XY+Z^2`.

Consequently cap-preserving mollification converges **uniformly at the output-density level** for every fixed rank-at-least-three matrix. In particular, if a universal height theorem is proved first for smooth cap-one marginals, then it passes to arbitrary measurable cap-one marginals with the **same universal height constant**. The constants `K(A,j)` used only to justify the per-instance limit and may depend arbitrarily badly on `A`; they are not candidates for the owner universal constant.

The theorem uses the completed physical-pair certificates from account03/B15, the independently scoped-reviewed rank-two affine half-Riesz/rank-three consequence, and the designated partner account04/B15 same-constant `C_0` compiler.

## 2. Absolute continuity remains separate and elementary

For completeness, the qualitative absolute-continuity statement needed by this assignment holds under much weaker hypotheses.

Let `A!=0` and let `X` have any absolutely continuous joint law on `R^n`. Put `q(x)=x^T A x`. Its critical set is

`Crit(q)=ker A`,

which is a proper linear subspace and hence has Lebesgue measure zero. If `N subset R` is Lebesgue-null, define

`E_k=q^(-1)(N) intersect {|grad q|>=1/k}`.

By the coarea formula,

`integral_(E_k) |grad q(x)| dx
 = integral_N H^(n-1)(q^(-1)(t) intersect {|grad q|>=1/k}) dt =0`.

Since `|grad q|>=1/k` on `E_k`, `|E_k|=0`. Thus

`q^(-1)(N) subset ker A union union_k E_k`

is Lebesgue-null. Absolute continuity of the input therefore implies `P(q(X) in N)=0`. Hence every nonconstant quadratic pushforward is absolutely continuous. This proves existence of some density but says nothing quantitative about its height or continuity.

## 3. Source-pinned analytic inputs

The following existing results are used only in their proved scopes.

### 3.1 Physical pair and pair-minor-degenerate triple certificates

From account03/B15 auto27,

`yspennstate/math-open-problems@2f36eb6204ac8598eaf63faed15f9fa7fddffd0c`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T222614Z-account03-B15-qform-auto27/REPORT.md`,

if an ORIGINAL-coordinate physical pair `D` is invertible indefinite, with

`Delta=|det D|`, `kappa=sigma_min(D)`,

and nonzero physical Schur remainder `S`, then

`||p_Q||_infinity <= 2^(13/4)(Delta*kappa*eta(S))^(-1/4)`,       (3.1)

where `eta(S)` is the maximum absolute diagonal coefficient if one exists, and otherwise the maximum absolute off-diagonal coefficient. The same theorem is uniform in arbitrary affine terms produced by conditioning. If `D` is definite, the corresponding uniform bound is

`||p_Q||_infinity <= pi/sqrt(|det D|)`.                         (3.2)

From account03/B15 auto31,

`yspennstate/math-open-problems@bea3c88b8ba5df9f7fbed3bf0676709971a1e9da`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260924T023146Z-account03-B15-qform-auto31/REPORT.md`,

if a physical invertible `3x3` block `B` has every physical `2x2` principal determinant equal to zero, then, uniformly in arbitrary affine terms,

`||p_Q||_infinity <=4(|det B| max_i|B_ii|)^(-1/4)`.             (3.3)

The same report proves that (3.1)--(3.3) furnish a finite explicit affine-uniform certificate for every **fixed** symmetric matrix of rank at least three.

### 3.2 Rank-three principal-block consequence

The source-pinned rank-two fusion theorem is

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

Its rank-three consequence says: if an ORIGINAL-coordinate principal block has exact rank three and representation `V M V^T`, `V^T V=I_3`, then for a row `i` of leverage `c_i` with nonzero physical diagonal `a`, the full ambient form has

`||p_Q||_infinity <=128[c_i |a| |det M|]^(-1/4)`.               (3.4)

For an invertible physical `3x3` block `B`, take `V=I_3`, `M=B`, so `c_i=1` and

`||p_Q||_infinity <=128(|B_ii| |det B|)^(-1/4)`                 (3.5)

for every nonzero chosen `B_ii`. The source theorem allows arbitrary outside coefficients and couplings. It received a scoped independent PASS at

`yspennstate/math-open-problems@3bec1a01afe9cf433d3f4e14a46fe21b5dcbfc64`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T164017Z-account03-B16-QFORM-r13/INDEPENDENT_REVIEW_RANK2_FUSION.md`.

### 3.3 Designated partner: same-constant C0 compiler

The completed designated partner result is account04/B15 r8,

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`.

Its Theorem 6.1 states: for a fixed cap-one product instance with `rank(A)>=3`, any separately proved interval domination

`P(Q in I)<=M|I|`                                                  (3.6)

upgrades to a canonical representative `p_Q in C_0(R)` with the **same** pointwise height `||p_Q||_infinity<=M`. No class-uniform modulus of continuity is asserted.

## 4. Scaled-coordinate certificate

### Theorem 4.1 — `QFORM-SCALED-COORDINATE-CERTIFICATE-v1`

Fix a real symmetric `A` with `rank(A)>=3` and an original coordinate `j`. For `0<m<=1`, put

`T_m=diag(1,...,1,m,1,...,1)`

with `m` in coordinate `j`, and

`A_m=T_m A T_m`.

There exists a finite `K(A,j)` such that for every independent cap-one probability vector `Y`,

`P(Y^T A_m Y in I) <= K(A,j)m^(-1/2)|I|`                        (4.1)

for every interval `I`.

The proof is by the exact rank of the principal complement

`C=A_[j^c,j^c]`.

### Case 1: `rank C>=3`

The complete fixed-matrix physical certificate in auto31 applies to `C` itself and is uniform in arbitrary affine terms. Let `K_C<infinity` be the explicit constant obtained from its pair/triple dichotomy. Conditioning on `Y_j=y`,

`Y^T A_m Y
 =Y_(j^c)^T C Y_(j^c)
 +2my A_(j,j^c)Y_(j^c)+m^2 A_jj y^2`.

The last two terms are an arbitrary affine perturbation plus a constant in the `j^c` variables. Hence every conditional law has height at most `K_C`, uniformly in `m,y`. Averaging gives

`P(Y^T A_mY in I)<=K_C|I|<=K_C m^(-1/2)|I|`.                  (4.2)

### Case 2: `rank C=2`

A rank-two symmetric matrix has a nonsingular physical `2x2` principal block `D`: otherwise all physical pair minors vanish, and the sign-matrix argument in auto31 forces rank at most one or at least three, never exactly two. Choose such `D` entirely inside `j^c`.

If `D` is definite, (3.2) gives a constant independent of `m`, so (4.1) follows immediately.

Suppose `D` is indefinite. Partition the full matrix by this pair and write its Schur complement as `S`. Since `rank A>=3` and `D` is invertible, `S!=0`. In the scaled matrix `A_m`, the pair `D` is unchanged, while the remainder scaling is a diagonal matrix `E_m` with one entry `m`; its Schur complement is exactly

`S_m=E_m S E_m`.                                                 (4.3)

If `S` has a nonzero diagonal, each diagonal coefficient is multiplied by either `1` or `m^2`, and therefore

`eta(S_m)>=m^2 eta(S)`.

If every diagonal vanishes, each off-diagonal coefficient is multiplied by either `1` or `m`, hence again

`eta(S_m)>=m^2 eta(S)`                                           (4.4)

because `0<m<=1`. Apply (3.1):

`||p_(A_m)||_infinity
 <=2^(13/4)(|det D| sigma_min(D) eta(S_m))^(-1/4)
 <=K_2 m^(-1/2)`,                                                (4.5)

where

`K_2=2^(13/4)(|det D| sigma_min(D) eta(S))^(-1/4)<infinity`.

This proves (4.1) in rank two.

### Case 3: `rank C<=1`

Bordering a matrix by one row and column increases rank by at most two, so

`rank A<=rank C+2`.

Because `rank A>=3`, this case forces

`rank C=1`, `rank A=3`.                                         (4.6)

Write

`A=[[a,b^T],[b,C]]`, `C=sigma v v^T`, `sigma in {+1,-1}`, `v!=0`.

If `b` were proportional to `v`, the full matrix would have rank at most two. Thus `b` and `v` are not proportional, so there are `k,l in j^c` with

`d:=v_k b_l-v_l b_k !=0`.                                       (4.7)

The physical principal triple on `{j,k,l}` is

`B=[[a,b_k,b_l],
    [b_k,sigma v_k^2,sigma v_k v_l],
    [b_l,sigma v_k v_l,sigma v_l^2]]`.

A direct determinant calculation gives

`det B=-sigma (b_k v_l-b_l v_k)^2 !=0`.                          (4.8)

At least one of `v_k,v_l` is nonzero. Choose `i in {k,l}` with `v_i!=0`; then

`B_ii=sigma v_i^2 !=0`.

Under the coordinate scaling, the corresponding triple becomes

`B_m=diag(m,1,1) B diag(m,1,1)`,

so

`det B_m=m^2 det B`, `B_(m,ii)=B_ii`.                            (4.9)

Apply the independently reviewed rank-three consequence (3.5):

`||p_(A_m)||_infinity
 <=128(|B_ii||det B_m|)^(-1/4)
 =K_3 m^(-1/2)`,                                                 (4.10)

with

`K_3=128(|B_ii||det B|)^(-1/4)<infinity`.

This completes all cases and proves Theorem 4.1. Notice that the theorem is purely fixed-matrix: `K(A,j)` may diverge along diffuse target families. The useful point is the **universal exponent** `m^(-1/2)`.

## 5. Positive submass theorem

### Theorem 5.1 — `QFORM-SUBMASS-SQRT-C0-v1`

Fix `A` and `j` as in Theorem 4.1. Let the coordinates `i!=j` have arbitrary independent probability densities `f_i<=1`. Let `g` be a measurable subdensity in coordinate `j` satisfying

`0<=g<=1`, `integral g=m<=1`.

Define the pushforward subprobability measure

`nu_g(E)=integral 1_{x^T A x in E} g(x_j) prod_(i!=j) f_i(x_i) dx`.

Then `nu_g` has a density `r_g in C_0(R)` and

`boxed( ||r_g||_infinity <=K(A,j) sqrt(m). )`                    (5.1)

For `m=0` this is trivial. Assume `m>0`. Normalize the `j`-th source density to `h=g/m`, whose cap is at most `1/m`. If `X_j` has density `h` and

`Y_j=X_j/m`,

then the density of `Y_j` is

`m h(my)=g(my)<=1`,

and it has total mass one. Thus the normalized subprobability law is exactly the cap-one product law for the scaled matrix `A_m`:

`X^T A X = Y^T A_m Y`.                                           (5.2)

By Theorem 4.1,

`P(Y^T A_mY in I)<=K(A,j)m^(-1/2)|I|`.                           (5.3)

Now apply the designated completed account04/B15 Theorem 6.1 to the **actual inequality (5.3)**. Since `rank A_m=rank A>=3`, the normalized output law has a canonical density `p_m in C_0(R)` with

`||p_m||_infinity<=K(A,j)m^(-1/2)`.

The original subprobability is `nu_g=m Law(Y^T A_mY)`, hence

`r_g=m p_m in C_0(R)`

and (5.1) follows. This is the required current-run application of the designated partner result; continuity is added after the interval height is paid, with zero constant loss.

## 6. Sharp marginal L1 -> output Linfinity stability

### Theorem 6.1 — `QFORM-MARGINAL-HOLDER-STABILITY-v1`

Fix every marginal except coordinate `j`. Let `f_j` and `g_j` be probability densities with `0<=f_j,g_j<=1`. Let `p_f,p_g` denote the canonical `C_0` densities of the two rank-at-least-three quadratic outputs. Put

`delta=||f_j-g_j||_1`.

Then

`boxed( ||p_f-p_g||_infinity
 <=sqrt(2) K(A,j) delta^(1/2). )`                                (6.1)

Indeed, write

`f_j-g_j=h_+-h_-`.

Because both densities have total mass one,

`integral h_+=integral h_-=delta/2`,

and `0<=h_+<=f_j<=1`, `0<=h_-<=g_j<=1`. Their two quadratic pushforward submeasures have `C_0` densities `r_+,r_-` satisfying Theorem 5.1:

`||r_+||_infinity, ||r_-||_infinity
 <=K(A,j) sqrt(delta/2)`.

The signed output-measure identity gives

`p_f-p_g=r_+-r_-`

almost everywhere. Both sides are continuous, hence the equality is pointwise. Therefore

`||p_f-p_g||_infinity
 <=2K(A,j)sqrt(delta/2)
 =sqrt(2)K(A,j)sqrt(delta)`.

### Simultaneous change of all marginals

For two cap-one product families `(f_1,...,f_n)` and `(g_1,...,g_n)`, replace coordinates one at a time and telescope. Since `K(A,j)` is uniform over the other cap-one marginals,

`boxed(
 ||p_f-p_g||_infinity
 <=sqrt(2) sum_(j=1)^n K(A,j)||f_j-g_j||_1^(1/2).
)`                                                                  (6.2)

This is a genuine quantitative regularity statement for the quadratic pushforward map at every fixed rank-at-least-three matrix.

## 7. Same-constant reduction from smooth to rough laws

Let `rho_epsilon` be a standard nonnegative approximate identity and put

`f_(j,epsilon)=f_j*rho_epsilon`.

Then

`0<=f_(j,epsilon)<=1`, `integral f_(j,epsilon)=1`,

and

`||f_(j,epsilon)-f_j||_1 ->0`.

By (6.2), for fixed `A,n`,

`||p_epsilon-p||_infinity
 <=sqrt(2) sum_j K(A,j)
     ||f_(j,epsilon)-f_j||_1^(1/2)
 ->0`.                                                            (7.1)

Thus cap-preserving smoothing of every input marginal produces **uniform convergence of the canonical output densities**.

This has an important target-level implication. Suppose a future argument proves, for every target matrix `s_3(A)>=1`, the bound

`||p_Q||_infinity<=C`                                             (7.2)

for all smooth cap-one marginals, with one `C` independent of `n,A` and the smooth laws. Fix an arbitrary rough target instance and mollify its marginals. Each approximating output has height at most `C`, while (7.1) converges uniformly to the rough output. Therefore the rough output also has

`||p_Q||_infinity<=C`                                             (7.3)

with the **same universal constant**. Account04/B15 supplies `C_0` representatives throughout, so the same limit also preserves continuity.

The matrix-dependent constants `K(A,j)` do not contaminate `C`: they only prove convergence for each fixed target instance. This sharply separates rough-input regularity from the still-open matrix-uniform height problem.

## 8. The square-root exponent is optimal

The exponent `1/2` in (6.1) cannot be improved uniformly even for one fixed owner-target matrix.

Take

`Q=2XY+Z^2`,

so

`A=[[0,1,0],[1,0,0],[0,0,1]]`

has eigenvalues `{1,-1,1}`. Let `Y,Z` be independent `Unif[0,1]`. For `0<m<=1/2`, compare

`f_X=1_[0,1]`

with

`g_X=1_[m,1]+1_[2,2+m]`.

Both are probability densities bounded by one and

`delta=||f_X-g_X||_1=2m`.                                        (8.1)

The positive part of `f_X-g_X` is the subdensity on `[0,m]`; the negative part is the subdensity on `[2,2+m]`.

For the positive subdensity, the density of `W=2XY` is

`r_+(w)=(1/2) log(2m/w)`, `0<w<2m`.                              (8.2)

The density of `Z^2` is

`h(s)=1/(2sqrt(s))`, `0<s<1`.

At `t=2m`, direct convolution gives

`(r_+*h)(2m)
 =(1/4) integral_0^(2m) log(2m/w)(2m-w)^(-1/2) dw
 =sqrt(2m)(1-log 2)`,                                             (8.3)

using

`integral_0^1 log(1/u)(1-u)^(-1/2) du=4(1-log2)`.

For the negative subdensity and every `0<w<2m`,

`r_-(w)=(1/2) integral_2^(2+m) dx/x
       =(1/2)log(1+m/2)`.                                        (8.4)

Therefore

`(r_-*h)(2m)
 =(1/2)log(1+m/2)sqrt(2m)`.                                      (8.5)

Since the common part of the two `X` laws cancels,

`|p_f(2m)-p_g(2m)|
 =sqrt(2m)[1-log2-(1/2)log(1+m/2)]`                              (8.6)

and, using `(1/2)log(1+m/2)<=m/4`,

`boxed(
 ||p_f-p_g||_infinity
 >=sqrt(delta)[1-log2-delta/8].
)`                                                                  (8.7)

As `delta->0`, the right side is asymptotic to

`(1-log2)sqrt(delta)`.

Hence no law-uniform estimate for this fixed target matrix can replace the exponent `1/2` in (6.1) by any exponent `alpha>1/2`. The square-root modulus is genuinely sharp in scale.

## 9. Regularity ledger

The precise hierarchy is now:

1. **Absolute continuity:** every nonzero quadratic pushforward of an absolutely continuous joint law is absolutely continuous; no rank-three hypothesis is needed.
2. **Fixed-matrix bounded density:** every fixed rank-at-least-three matrix has a finite cap-one product-law height certificate, but that constant can degenerate with matrix geometry.
3. **Fixed-matrix continuous density:** account04/B15's completed compiler supplies a canonical `C_0` representative after the interval height is paid.
4. **New quantitative stability:** at fixed rank-at-least-three `A`, the canonical density is `1/2`-Holder from each marginal's `L^1` distance into output `L^infinity`, with an explicit finite matrix-dependent coefficient `K(A,j)`. The exponent is sharp.
5. **Rough-law reduction:** a same-constant universal theorem for smooth cap-one inputs automatically extends to all measurable cap-one inputs.
6. **No universal continuity modulus in the output variable:** the earlier account03/B15 phase-aligned construction still rules out any target-uniform modulus `omega(h)->0` for translations of `p_Q`. There is no contradiction: the new theorem controls perturbation of the **input law at fixed A**, not translation regularity of the output variable uniformly over the target class.
7. **Full universal height theorem:** still OPEN. None of the constants `K(A,j)` is controlled by the bare condition `s_3(A)>=1`.

## 10. Next mathematical step

Regularity is no longer the first unpaid implication. The next useful use of this theorem is to let the proof-assembly workers freely mollify arbitrary fragmented marginals, solve the height problem in the smooth category if that enables differential/coarea/Fourier arguments, and return to the rough category with the same final universal constant.

For B15 itself, the remaining structural regularity question is whether an analogous square-root submass estimate can be made **matrix-uniform after averaging over several coordinates** under `s_3(A)>=1`. A positive result of that stronger type could interact with the grouped-bank/diffuse decomposition. The present theorem intentionally does not claim it.

No counterexample to the owner conjecture was produced in this run.
