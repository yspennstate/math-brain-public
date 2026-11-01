SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T00:35:49Z.
attacking: grouped-square curved-fiber absorption in the rank-two zero-diagonal Schur branch, retaining original-coordinate product structure and locating the exact remaining overlap-entanglement debt.

# fleet01/B06 — grouped square banks and zero-diagonal rank-two Schur geometry

**Run:** `20260923T003549Z-qform-r20-b06`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Target, controls, and source-valid inputs

The target is unchanged: for every dimension, independent real original coordinates with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential supremum, or give a valid counterexample. Continuity is tracked separately and is not proved here.


Two completed fleet02/B06 results are used at displayed inequalities.

1. `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.
   For a unit scalar projection `Y=c^T X` of a cap-one product vector,

   `||p_Y||_infinity <= M(c)
    := product_{j:c_j^2<1} (1-c_j^2)^(-(1-c_j^2)/2)
    <= sqrt(e)`.                                                     (0.1)

2. `QFORM-THIRD-SQUARE-HYPERBOLIC-ABSORPTION-v1`, canonical
   `yspennstate/math-open-problems@168ac7725f62401408f20ce18cbf8ff7055e9013`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T234200Z-e4c1068b3e5d/REPORT.md`.
   Its general scalar-cap estimate is

   `4 sqrt(2) L_Z sqrt(L_U L_V) / sqrt(|a d|)`                       (0.2)

   for a genuine independent square variable plus a product-bank hyperbolic pair. I prove below the exact extension needed here: the square variable may itself be a unit projection of a disjoint original-coordinate bank, and its center may be an arbitrary measurable function of the two hyperbolic banks.

The latest fleet03/B07 overlap-Schur handoff at the source check is
`yspennstate/math-open-problems@391688138f7f481a2c8688c2d27f9508db7af6af` and supplies the exact pair-Schur ledger. The latest fleet03/B08 diffuse handoff at the source check is `@d30dba6db19d1eceabde6222c84a5b57a85506f0` and supplies aggregate third-compound packets. The results below identify a particularly rigid singular-pair endpoint for those ledgers.

## 1. The half-Riesz input

If a real random variable `Y` has density bounded by `L`, then for every `t`,

`E |Y-t|^(-1/2) <= 2 sqrt(2L)`.                                      (1.1)

This is the exact layer-cake estimate used by the partner: split

`int_0^infinity P(|Y-t|<s^(-2)) ds`

at `s=sqrt(2L)` and use `P(|Y-t|<r)<=min(1,2Lr)`.

## 2. Grouped-square extension of the partner theorem

### Theorem 2.1 — `QFORM-GROUPED-SQUARE-HYPERBOLIC-ABSORPTION-v1`

Let `B_0,B_L,B_R` be pairwise disjoint sets of original coordinates. Let

`W=w^T X_{B_0}`,  `U=u^T X_{B_L}`,  `V=v^T X_{B_R}`

with `||w||_2=||u||_2=||v||_2=1`. Suppose their density caps are `L_W,L_U,L_V`. Let `F` be an arbitrary measurable function of `X_{B_L}`, and let `xi` be an arbitrary measurable function of `(X_{B_L},X_{B_R})`. For constants `A,d!=0`, fixed `theta`, and constant `c`, set

`T=A (W+xi(X_{B_L},X_{B_R}))^2
   +F(X_{B_L})+2d(U-theta)V+c`.                                     (2.1)

Then `T` has an essentially bounded density and

`boxed:
 ||p_T||_infinity
 <= 4 sqrt(2) L_W sqrt(L_U L_V) / sqrt(|A d|).`                     (2.2)

In particular, applying fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` separately to the three disjoint product banks gives

`boxed:
 ||p_T||_infinity <= 4 sqrt(2) e / sqrt(|A d|).`                    (2.3)

### Proof

Condition on the two hyperbolic banks `X_{B_L},X_{B_R}`. The square variable is a translate of `W`. For either sign of `A`, the density of `A(W+z)^2` obeys the pointwise envelope

`p_{A(W+z)^2}(y) <= L_W/(sqrt(|A|) sqrt(|y|))`                       (2.4)

on its support, uniformly in the shift `z`. Therefore

`p_T(t)
 <= L_W |A|^(-1/2)
    E |t-c-F(X_{B_L})-2d(U-theta)V|^(-1/2)`.                         (2.5)

Now condition on the entire left bank. The random variable

`2d(U-theta)V`

has density cap

`L_V/[2|d| |U-theta|]`.                                              (2.6)

Apply (1.1):

`E_V |s-2d(U-theta)V|^(-1/2)
 <= 2 sqrt( L_V/(|d| |U-theta|) )`.                                 (2.7)

Average over the left bank and use (1.1) again on the scalar projection `U`:

`E |U-theta|^(-1/2) <= 2 sqrt(2L_U)`.                               (2.8)

Combining (2.5)--(2.8) proves (2.2). The partner's exact weighted affine-fiber theorem gives `L_W,L_U,L_V<=sqrt(e)`, so (2.3) follows. No conditional density cap after a rotation is used: each scalar cap is an unconditional projection of its own disjoint original-coordinate product bank. `QED`

The arbitrary bank-dependent center `xi` is important. It disappears at (2.4) before either hyperbolic factor is integrated, so no independence between the center and `U,V` is asserted or needed.

## 3. Exact geometry of a zero-diagonal rank-two Schur complement

Let a physical scalar pivot `i` have

`a=A_ii !=0`,  `h=A_{-i,i}`,  `C=A_{-i,-i}`,

and let

`S=C-hh^T/a`                                                        (3.1)

be its exact Schur complement.

### Lemma 3.1 — rank two plus zero physical diagonal is a disjoint hyperbolic product

Suppose `S` has rank two and `S_jj=0` for every physical coordinate `j`. Then there are unit vectors `u,v` with disjoint physical supports and a number `sigma>0` such that

`S=sigma(uv^T+vu^T)`,
`Y^T S Y=2 sigma (u^T Y)(v^T Y)`.                                   (3.2)

### Proof

`tr S=0`. Since `S` is symmetric of rank two, its two nonzero eigenvalues are therefore `+sigma,-sigma`. Let `p,q` be corresponding orthonormal eigenvectors and define

`u=(p+q)/sqrt(2)`,  `v=(p-q)/sqrt(2)`.

Then `u,v` are orthonormal and

`S=sigma(pp^T-qq^T)=sigma(uv^T+vu^T)`.                              (3.3)

The diagonal equation gives

`0=S_jj=2 sigma u_j v_j`

for every physical `j`, so `u_jv_j=0` coordinatewise. Hence their supports are disjoint. `QED`

The condition has an exact original-matrix interpretation:

`det A[{i,j},{i,j}]=a S_jj`.                                        (3.4)

Thus, when `a!=0`, all physical `2x2` principal pairs through `i` are singular exactly when the Schur diagonal vanishes.

Let

`L=supp(u)`,  `R=supp(v)`,  `K={j:u_j=v_j=0}`.                       (3.5)

Then `L,R,K` are disjoint physical banks and every row/column of `S` indexed by `K` is zero.

## 4. A spectral identity: the effective third square is automatically large enough

The preceding geometry exposes a hidden third square direction. Its size is forced by the third singular value even when the original physical pivot `a` is arbitrarily small.

Let `P_ker` be orthogonal projection onto `ker S`, put

`k=P_ker h`,
`rho^2=a^2+||k||_2^2`,
`gamma=rho^2/|a|`.                                                   (4.1)

### Lemma 4.1 — `QFORM-ZERODIAG-EFFECTIVE-SQUARE-SPECTRAL-v1`

If `A` has exact rank three, then

`boxed: gamma sigma >= s_3(A)^2`,                                   (4.2)

where `s_3(A)` is the smallest nonzero singular value.

### Proof

Square completion gives the matrix identity

`A=(1/a) t t^T + diag(0,S)`,  `t=(a,h)`.                             (4.3)

Write `h=r+k` with `r in ran(S)` and `k in ker(S)`. Let

`w=(a,k)/rho`.                                                       (4.4)

Then `w,u,v` are orthonormal and span `ran(A)`. Write `r=alpha u+beta v`. In the orthonormal basis `(w,u,v)`, the nonzero restriction of `A` is

`B=[[g,b^T],[b,D+b b^T/g]]`,                                        (4.5)

where `g=rho^2/a`, `b=(rho/a)(alpha,beta)^T`, and

`D=[[0,sigma],[sigma,0]]`.                                          (4.6)

Thus the Schur complement of `g` is exactly `D`, so

`|det B|=|g| sigma^2=gamma sigma^2`.                                (4.7)

Choose a unit `x in R^2` with `b^T x=0`. Then

`B(0,x)=(0,Dx)`, hence `||B(0,x)||=sigma`.                           (4.8)

Therefore the largest singular value `s_1(B)>=sigma`. Also `s_2(B)>=s_3(B)`. Since `B` carries exactly the three nonzero singular values of `A`,

`gamma sigma^2
 =s_1(A)s_2(A)s_3(A)
 >=sigma s_3(A)^2`.                                                  (4.9)

Divide by `sigma`. `QED`

This identity is useful because it separates a spectral fact from the product-structure difficulty. Spectrally, there is always enough third-square curvature; the remaining question is how much of that direction lives on a physical bank disjoint from the two hyperbolic factors.

## 5. Main receiver: the physical null-support square bank

The full kernel vector `k` can overlap the physical supports `L,R` even though it is orthogonal to `u,v`. Define the genuinely disjoint part

`rho_0^2=a^2+||h_K||_2^2`,
`kappa=rho_0^2/rho^2 in (0,1]`.                                     (5.1)

Define the unit scalar projection on the disjoint bank `{i} union K`,

`W_0=(aX_i+h_K^T X_K)/rho_0`.                                      (5.2)

Let `U=u^T X_L`, `V=v^T X_R`. The three variables are projections of pairwise disjoint original-coordinate product banks. The exact square completion is

`Q=(rho_0^2/a)
    (W_0+(h_L^T X_L+h_R^T X_R)/rho_0)^2
   +2 sigma U V`.                                                    (5.3)

### Theorem 5.1 — `QFORM-ZERODIAG-SCHUR-DISJOINT-SQUAREBANK-v1`

Under the preceding exact-rank-three hypotheses,

`boxed:
 ||p_Q||_infinity
 <= 4 sqrt(2) e / (s_3(A) sqrt(kappa)).`                             (5.4)

Hence under the target normalization `s_3(A)>=1`,

`boxed:
 ||p_Q||_infinity <= 4 sqrt(2) e kappa^(-1/2).`                     (5.5)

In particular, the entire branch `kappa>=1/3` is paid by the universal numerical constant

`4 sqrt(6) e < 26.634`.                                              (5.6)

### Proof

Apply Theorem 2.1 to (5.3) with

`A_0=rho_0^2/a`,  `d=sigma`,  `theta=0`.                             (5.7)

The named fleet02/B06 weighted affine-fiber theorem gives the actual caps

`L_(W_0)<=M(W_0)<=sqrt(e)`,
`L_U<=M(u)<=sqrt(e)`,
`L_V<=M(v)<=sqrt(e)`.                                                (5.8)

Thus

`||p_Q||_infinity
 <=4sqrt(2)e / sqrt((rho_0^2/|a|) sigma)`.                           (5.9)

But

`(rho_0^2/|a|)sigma
 =kappa (rho^2/|a|)sigma
 =kappa gamma sigma
 >=kappa s_3(A)^2`                                                   (5.10)

by Lemma 4.1. This proves (5.4)--(5.6). `QED`

This is an actual product-weighted curved-fiber payment. It never replaces the hyperbolic surface by its fiber maximum and never asserts that the spectral coordinates are independent.

## 6. What happens when the paid bank is small: an exact Pluecker entanglement identity

The complementary branch `kappa<1/3` is not featureless. It forces a dimension-free amount of the third square direction to overlap the two hyperbolic physical banks in an explicitly aggregate way.

Keep the normalized full effective-square vector `w=(a,k)/rho` from (4.4). On the physical null bank `{i} union K`,

`||w_{ {i} union K }||_2^2=kappa`.                                  (6.1)

Since `w,u,v` are orthonormal, and `u,v` have disjoint supports,

`w_L dot u=0`,  `w_R dot v=0`,
`||w_L||^2+||w_R||^2=1-kappa`.                                      (6.2)

Let `F=[w,u,v]`, an `n x3` orthonormal frame.

### Lemma 6.1 — `QFORM-ZERODIAG-SCHUR-ENTANGLEMENT-PLUECKER-v1`

The structured Pluecker masses satisfy the exact identities

`sum_{j<k in L, ell in R}
 det F[{j,k,ell},:]^2 = ||w_L||_2^2`,                               (6.3)

`sum_{j in L, k<ell in R}
 det F[{j,k,ell},:]^2 = ||w_R||_2^2`.                               (6.4)

Consequently, if `kappa<1/3`, then one of these two disjoint-bank triple classes carries Pluecker mass strictly larger than `1/3`.

### Proof

For `j,k in L` and `ell in R`, the corresponding three frame rows are

`(w_j,u_j,0)`, `(w_k,u_k,0)`, `(w_ell,0,v_ell)`.

Hence

`det F[{j,k,ell},:]
 =v_ell (w_j u_k-w_k u_j)` up to sign.                              (6.5)

Sum squares. Since `||v||=1`, `||u||=1`, and `w_L dot u=0`, Lagrange's identity yields

`sum_{j<k}(w_j u_k-w_k u_j)^2
 =||w_L||^2||u||^2-(w_L dot u)^2
 =||w_L||^2`.                                                       (6.6)

This proves (6.3); (6.4) is symmetric. If `kappa<1/3`, then `||w_L||^2+||w_R||^2>2/3`, so one is `>1/3`. `QED`

This is the exact residual obstruction after Theorem 5.1. It is not a demand to select one triple: the mass can be diffuse over arbitrarily many triples, and current corrections show that localizing before aggregation can lose a power of the bank size. The next receiver must therefore consume (6.3) or (6.4) while the original product banks are still present. This dovetails with the current fleet03/B07/B08 aggregate-compound work.

## 7. A target-valid family where grouped square aggregation removes an arbitrarily bad physical pivot

The new theorem is not cosmetic. For `t>0`, consider four physical coordinates ordered `(i,k,L,R)` and

`A_t=
 [[ t^2/(1+t^2), t/(1+t^2), 0,0],
  [ t/(1+t^2),   1/(1+t^2), 0,0],
  [ 0,0,0,1],
  [ 0,0,1,0 ]].`                                                    (7.1)

The first `2x2` block is rank one with eigenvalues `{1,0}` and the last block has eigenvalues `{1,-1}`. Therefore

`spectrum(A_t)={1,1,-1,0}`                                          (7.2)

for every `t>0`: this is an exact target-valid family.

At the physical pivot `i`,

`a=t^2/(1+t^2)`                                                      (7.3)

can tend to zero. Its Schur complement is exactly the hyperbolic block on `(L,R)` plus a zero row on `k`, so `sigma=1`, `kappa=1`. The grouped square is

`W_0=[t X_i+X_k]/sqrt(1+t^2)`,                                      (7.4)

and

`Q=W_0^2+2X_LX_R`.                                                   (7.5)

Thus the small physical pivot is entirely an artifact of choosing a bad physical coordinate; the product-preserving grouped square has coefficient one.

The partner's exact scalar projection bound gives

`M(W_0)
 =(1-a)^(-(1-a)/2) a^(-a/2)
 =exp(H(a)/2)
 <=sqrt(2)`,                                                        (7.6)

while the physical variables `X_L,X_R` have density caps one. Theorem 2.1 therefore gives the sharper family-specific bound

`boxed: ||p_Q||_infinity <= 4sqrt(2) M(W_0) <= 8`,                  (7.7)

uniformly as `a downarrow0`.

For the exact rational checker value `t=1/8`,

`a=1/65`, `A_ik=8/65`, `A_kk=64/65`,
`M(W_0)=1.0405438421309723`,                                        (7.8)

so

`||p_Q||_infinity <=5.88620485514172`.                              (7.9)

By contrast, retaining only the tiny physical square `aX_i^2` in the same half-Riesz mechanism gives the crude factor `4sqrt(2/a)=4sqrt(130)>45.6`. The grouped bank exactly removes that false small-pivot loss.

## 8. Consequence for the proof graph and first unpaid implication

This run closes the zero-diagonal rank-two Schur branch whenever a fixed fraction of the effective third-square direction lies on physical coordinates disjoint from the two hyperbolic supports. Spectral geometry itself is not the problem: Lemma 4.1 proves `gamma sigma>=s_3(A)^2`. The only remaining loss is the physical overlap fraction `kappa`.

The first unpaid implication is now

`QFORM-ZERODIAG-OVERLAP-PLUECKER-RECEIVER-v1`:

when `kappa<1/3`, consume the `>1/3` structured Pluecker mass in (6.3) or (6.4) **before selecting a physical triple**, using the product structure of the two original-coordinate banks. A valid solution may route this mass into the current finite-bank third-compound compiler / ridge receiver, or prove a direct bank-level curved coarea estimate. It may not replace the aggregate by one reciprocal minor, nor replace the overlapping orthogonal projections by independent variables.

This is also a concrete handoff to the current B07/B08 aggregate-compound work: the zero-diagonal singular-pair endpoint now has a paid disjoint-square branch and an exact dimension-free overlap ledger in the complementary branch.

## 9. Status

The full arbitrary-dimensional QFORM conjecture remains **OPEN**. No target-valid counterexample was produced. The theorem above establishes essential boundedness only in its stated branch. The separate continuous-density conclusion remains **OPEN** here.

No FEI work, installation, public release, email, notification change, new task, cross-account authentication, paid model/API, remote workflow, or permission expansion was performed.
