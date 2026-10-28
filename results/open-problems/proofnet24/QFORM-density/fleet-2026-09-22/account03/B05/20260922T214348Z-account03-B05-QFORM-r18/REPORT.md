SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-22T21:43:48Z.
attacking: aggregate coarea curvature before reciprocal local-core inversion, with emphasis on the newest physical incident-minor rank-one tube and the dependent cross-leakage it leaves.

# account03/B05 r18 — two-arm coarea smoothing and the incident-minor tube dichotomy

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** not proved by the new coarea theorem below; only an essentially bounded density is asserted.

## 1. Source-valid inputs and corrections

The exact owner target is unchanged: independent original-coordinate real inputs with probability densities at most one, and a real symmetric matrix with at least three eigenvalues of modulus at least one. No moments, compact support, connected support, Gaussianity, log-concavity, diagonal-basis independence, or post-rotation independence is used here.

Binding corrections retained include the failure of law-uniform pointwise quadratic-phase decay, the dimension loss of naive fiber suprema, the failure of arbitrary-joint rank-three coarea, the failure of positive moments of normalized conditional projection-density suprema, and this slot's own `QFORM-SIGNED-LEAKAGE-FREE-TRIBANK-EXTRACTION-FALSE-v1`. In particular, the theorem below never replaces the product law by an arbitrary bounded joint density and never discards a quadratic term that depends on the same bank being used for smoothing.

Three completed inputs are used at their proved scopes.

1. **One-dimensional product marginal cap.** The completed account03/B09 report `QFORM-RANK2-BILINEAR-DIRECT-v1`, canonical `yspennstate/math-open-problems@55b475aece02e3bd181935ff66a26b8988100a0c:proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T114536Z-account03-B09-qform-r11/REPORT.md`, records the Livshyts--Paouris--Pivovarov marginal theorem in the form

   `||p_(b dot Y)||_infinity <= sqrt(2)/||b||_2`                         (1.1)

   for every nonzero coefficient vector `b` and every original-coordinate product bank `Y` with cap-one marginals.

2. **Dependent square smoothing.** The completed compatible account04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`, states that if `R` has density cap `M`, `V_R` has conditional density cap one for almost every residual value, and `a!=0`, then

   `||p_(R+a V_R^2)||_infinity <= 2 sqrt(M/|a|)`.                       (1.2)

   This theorem is applied at an actual displayed inequality in Section 4.

3. **Newest incident-minor tube.** account03/B06 r19, canonical `yspennstate/math-open-problems@f82fe367b06909082f94eda2b98f4a2fd2a5bb7c:proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T212328Z-account03-B06-qform-r19/REPORT.md`, reaches a normalized original-coordinate cross block `C` with `||C||_op<1`, a physical row `j`, a physical column `r`, and the intersection-minor matrix

   `N_ks=det C[{j,k},{r,s}]`.

   In its unpaid branch it proves

   `||N-N_1||_F^2 < 125/136576`,                                      (1.3)

   for the best rank-one approximation `N_1`, and

   `sigma_1(N)^2 > 9092287/17072000`.                                 (1.4)

   The complementary branch `E_2(N)>=1/4096` is already paid there by third exterior curvature plus square smoothing.

The exact designated partner `account04/B05` had no completed current-QFORM canonical handoff at the fresh lookup. No theorem is fabricated for it. The compatible completed account04/B18 theorem above is therefore the account04 mathematics actually applied in this run.

## 2. A reciprocal-max lemma for two independent physical pivots

### Lemma 2.1 — `QFORM-TWO-PIVOT-RECIPROCAL-MAX-v1`

Let `X,Y` be independent real random variables with probability densities bounded by one. For every `A,B>0` and every translations `x_0,y_0`,

`E [ 1 / max( A|X-x_0|, B|Y-y_0| ) ] <= 4/sqrt(A B).`                 (2.1)

The integrand is interpreted arbitrarily on the probability-zero event where both denominators vanish.

### Proof

Translations preserve the density caps, so write `x_0=y_0=0` and

`M=max(A|X|,B|Y|)`.

For every `r>0`, independence and the one-dimensional cap give

`P(M<r)
 =P(|X|<r/A) P(|Y|<r/B)
 <=min(1,2r/A) min(1,2r/B)
 <=min(1,4r^2/(AB)).`                                                  (2.2)

The last inequality is immediate below both saturation radii; if exactly one factor has saturated, say `2r/B>=1`, then `4r^2/(AB)>=(2r/A)`; if both have saturated the right side is replaced by one.

Layer cake gives

`E M^(-1)=int_0^infinity P(M<1/t) dt`.

With `t_0=2/sqrt(AB)`, use probability at most one on `[0,t_0]` and (2.2) afterwards:

`E M^(-1)
 <= t_0 + int_(t_0)^infinity 4/(AB t^2) dt
 = 2/sqrt(AB)+2/sqrt(AB)
 =4/sqrt(AB).`                                                         (2.3)

This proves (2.1). QED.

The key point is that the reciprocal singularity is integrable only after the two genuinely independent physical pivots are retained together. Taking a worst fiber in either pivot separately would recreate a logarithmic divergence.

## 3. New direct coarea theorem: two independent arms

### Theorem 3.1 — `QFORM-DOUBLE-STAR-DIRECT-COAREA-v1`

Let `X,Y,Z,W` be mutually independent real random variables with probability densities bounded by one. Let `beta,gamma` be nonzero reals, let `x_0,y_0` be arbitrary constants, and let `H,m,n:R^2->R` be arbitrary Borel functions. Define

`R = H(X,Y)
   + 2 beta (X-x_0) [Z+m(X,Y)]
   + 2 gamma (Y-y_0) [W+n(X,Y)].`                                     (3.1)

Then `R` is absolutely continuous and

`boxed( ||p_R||_infinity <= 2 / sqrt(|beta gamma|). )`                  (3.2)

No support, moment, sign, or regularity condition is imposed on the four input laws. The functions `H,m,n` may be arbitrarily large and irregular.

### Proof

Condition on `(X,Y)=(x,y)`. The two bracketed variables in (3.1) are independent translations of `Z` and `W`; hence their densities remain bounded by one. Except on a null set of `(x,y)`, the two scaled summands have density caps

`1/[2|beta| |x-x_0|]`, `1/[2|gamma| |y-y_0|]`.                         (3.3)

The density of a convolution of two probability laws is bounded by the smaller of the two individual `L^infinity` caps. The conditional additive term `H(x,y)` only translates the output. Thus

`||p_(R|X=x,Y=y)||_infinity
 <= 1 / [2 max(|beta||x-x_0|, |gamma||y-y_0|)].`                       (3.4)

Average the conditional densities and apply Lemma 2.1 with `A=|beta|`, `B=|gamma|`:

`||p_R||_infinity
 <= (1/2) E[1/max(|beta||X-x_0|,|gamma||Y-y_0|)]
 <=2/sqrt(|beta gamma|).`                                               (3.5)

Tonelli gives an integrable density representative, so absolute continuity follows as well. QED.

This is a direct product-coarea estimate. It is not an arbitrary-joint coarea theorem: the proof spends the two original independent pivot laws *before* taking a reciprocal Jacobian.

## 4. Square lifting, with the account04 theorem applied at the actual inequality

### Corollary 4.1 — `QFORM-DOUBLE-STAR-SQUARE-COAREA-v1`

Under the hypotheses of Theorem 3.1, let `S` be one further independent cap-one real variable, let `psi=psi(X,Y,Z,W)` be arbitrary Borel, and let `a!=0`. Then

`Q = R + a [S+psi(X,Y,Z,W)]^2`                                       (4.1)

has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(2) |a|^(-1/2) |beta gamma|^(-1/4).
)`                                                                    (4.2)

### Proof

Theorem 3.1 gives the base density cap

`M=2/sqrt(|beta gamma|).`                                             (4.3)

Condition on the value `R=r`. Because `S` is independent of `(X,Y,Z,W)`, the conditional law of

`V_r=S+psi(X,Y,Z,W)`                                                  (4.4)

is a mixture of translations of the fixed density of `S`, and therefore has density cap at most one. This is exactly the hypothesis of the completed account04/B18 dependent-square theorem (1.2). Applying it to the actual value (4.3) yields

`||p_Q||_infinity
 <=2 sqrt(M/|a|)
 =2 sqrt(2) |a|^(-1/2)|beta gamma|^(-1/4),`                           (4.5)

which is (4.2). QED.

Thus a true square plus two independent aggregate arms is a fully paid coarea architecture even when the square translation depends arbitrarily on all four arm variables.

## 5. Original-coordinate bank corollary: no strongest leaf is paid

Let `U=(U_1,...,U_m)` and `V=(V_1,...,V_k)` be disjoint original-coordinate banks, independent of one another and of independent original coordinates `X,Y,S`. All scalar marginals have density cap one. Let `c in R^m`, `b in R^k` be nonzero and write

`K=c dot U`, `L=b dot V`, `s=||c||_2`, `r=||b||_2`.

By (1.1), the normalized aggregates

`W=(sqrt(2)/s)K`, `Z=(sqrt(2)/r)L`                                   (5.1)

have one-dimensional density caps at most one. The two are independent because their physical banks are disjoint. Therefore every form

`Q = H(X,Y)+2 X L+2 Y K + a[S+psi(X,Y,U,V)]^2`                       (5.2)

with arbitrary Borel `H,psi` and `a!=0` satisfies, by Corollary 4.1 with

`beta=r/sqrt(2)`, `gamma=s/sqrt(2)`,

`boxed(
 ||p_Q||_infinity
 <= 2^(7/4) |a|^(-1/2) (rs)^(-1/4).
)`                                                                    (5.3)

The payment depends on the **whole Euclidean arm masses** `r,s`; it never selects one leaf coefficient. In particular, completely diffuse arms `b_j~r/sqrt(k)` and `c_i~s/sqrt(m)` cost exactly the same as concentrated arms of the same norms.

An arbitrary independent direct-sum random remainder may be added before the square without increasing the base density cap. Equation (5.3), however, does **not** permit extra quadratic terms depending on the same `U,V` banks except through the two displayed aggregates and the square translation. That distinction is the central point of Section 7.

## 6. New deterministic bridge from the B06 incident-minor tube

Write the normalized cross matrix from account03/B06 r19, after moving its distinguished physical row and column first, as

`C = [[alpha, b^T],[c,D]]`, `||C||_op<1`.                             (6.1)

Its intersection-minor matrix is exactly

`N=alpha D-cb^T`.                                                     (6.2)

Let

`epsilon_0=sqrt(125/136576)<0.030253`,
`sigma_0=sqrt(9092287/17072000)>0.729784`.                            (6.3)

The B06 unpaid branch gives a rank-one `N_1` with

`||N-N_1||_F<epsilon_0`, `sigma_1(N)>sigma_0`.                        (6.4)

### Lemma 6.1 — `QFORM-INCIDENT-RANK1-TUBE-ARM-OR-RANK2-v1`

Under (6.1)--(6.4), exactly the following quantitative dichotomy is available at the fixed threshold `1/4`.

**Small central entry.** If `|alpha|<1/4`, then

`boxed( ||b||_2 ||c||_2 > sigma_0-1/4 >0.479784. )`                    (6.5)

**Non-small central entry.** If `|alpha|>=1/4`, there exists a matrix `C_2` of rank at most two such that

`boxed( ||C-C_2||_F <4 epsilon_0 <0.121012. )`                         (6.6)

### Proof

Every submatrix of a contraction is a contraction, so `||D||_op<=1`. From (6.2),

`cb^T=alpha D-N`.

Therefore in the small-central-entry branch,

`||b|| ||c||=||cb^T||_op
 >=||N||_op-|alpha| ||D||_op
 >sigma_0-1/4`,                                                       (6.7)

which gives (6.5).

Now assume `alpha!=0`. Define

`D_2=(N_1+cb^T)/alpha`,
`C_2=[[alpha,b^T],[c,D_2]].`                                          (6.8)

The Schur complement of the scalar block `alpha` in `C_2` is

`D_2-cb^T/alpha=N_1/alpha`,                                          (6.9)

which has rank at most one. Hence

`rank(C_2)=1+rank(N_1/alpha)<=2`.                                    (6.10)

Also

`C-C_2=[[0,0],[0,(N-N_1)/alpha]]`,                                  (6.11)

so if `|alpha|>=1/4`,

`||C-C_2||_F=||N-N_1||_F/|alpha|<4 epsilon_0`,                       (6.12)

proving (6.6). QED.

This is stronger geometric information than the bare statement that the incident-minor matrix is close to rank one: either the distinguished crossing has two dimension-free aggregate arms, or the *whole normalized cross block* lies in a `0.121012` Frobenius tube around rank at most two.

## 7. Actual coarea payment and the precise surviving factor

In the small-`alpha` branch, (6.5) says the aggregate arm product is dimension-free. If the residual quadratic form had no additional term depending quadratically on the two arm banks beyond the two aggregate arms, the bank form (5.2) would apply with

`rs=||b|| ||c|| >sigma_0-1/4`.

For the genuine physical square coefficient `a` of the B06 Schur state this gives the concrete inequality

`||p_Q||_infinity
 < 2^(7/4) (sigma_0-1/4)^(-1/4) |a|^(-1/2)
 < 4.042 |a|^(-1/2).`                                                (7.1)

Equation (7.1) is not asserted for the full B06 state, because that state may contain the same-bank/cross-bank residual quadratic leakage that (5.2) explicitly excludes. The calculation instead isolates the exact unpaid factor:

> **`QFORM-DOUBLE-STAR-DEPENDENT-BANK-LEAKAGE-v1`.** Retain the two strong aggregate arms certified by (6.5), but also allow the same two original-coordinate banks to carry an arbitrary residual bilinear block `U^T D V` and/or within-bank quadratic phases. Prove a dimension-free coarea/small-ball estimate without replacing those product-linear banks by arbitrary joint densities and without paying a worst leaf coefficient.

The large-`alpha` alternative (6.6) gives a second formulation of the same debt: robustify the already-paid rank-two-cross-plus-third-curvature mechanisms under a `0.121012` normalized Frobenius tail. Because the inputs may be unbounded, a small coefficient matrix cannot simply be discarded as a small value perturbation; it must be consumed by an integrated Fourier, ridge, or joint coarea estimate.

Thus the newest B06 `4.15%` incident-minor tube is converted into a concrete B05 coarea dichotomy rather than merely being restated.

## 8. Scoped review of the pair-log theorem

The current research state requests an independent mathematical check of the pair-log theorem. I read the complete source `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md` and checked the steps relevant to B05.

- The far-region inverse-derivative payment gives `2 sqrt(2)/r` after the two original-coordinate choices are summed.
- In the near region, the orthogonal diagonalization is used only on Lebesgue measure; no rotated independence is claimed. The change `u=z_1+z_2`, `v=z_1-z_2` has Jacobian `1/2` and gives exactly the logarithmic trace `D^(-1/2) log(L^2/|t|)`.
- The layer-cake identity

  `E log_+(A/|t-R|)=int_0^infinity P(|t-R|<A e^(-v)) dv`

  combined with `P(|R-t|<rho)<=H sqrt(rho)` yields `<=2H sqrt(A)` with the correct exponent.
- Optimizing the resulting `A/r+B r` expression gives exactly

  `4 sqrt(2H)(D kappa)^(-1/4)`.
- In the exact-rank-three Schur step, the remaining coefficient is the scalar Schur complement `lambda`; `1/lambda` is a diagonal entry of `M^(-1)`, so `|lambda|>=sigma_min(M)>=s`. This gives the stated `8 sqrt(5)(D kappa s)^(-1/4)` after the source-valid rank-one affine small-ball estimate.

**Scoped review result: PASS for the displayed pair-log/coarea chain and its exact-rank-three Schur application.** This is not an end-to-end review of the full QFORM conjecture and does not enlarge the theorem's scope to arbitrary higher-rank Schur remainders.

## 9. Status and next implication

New proved supporting statements in this run:

- `QFORM-TWO-PIVOT-RECIPROCAL-MAX-v1`, (2.1);
- `QFORM-DOUBLE-STAR-DIRECT-COAREA-v1`, (3.2);
- `QFORM-DOUBLE-STAR-SQUARE-COAREA-v1`, (4.2), using completed account04/B18 at the actual inequality;
- original-coordinate diffuse-arm corollary (5.3);
- `QFORM-INCIDENT-RANK1-TUBE-ARM-OR-RANK2-v1`, (6.5)--(6.6);
- scoped pair-log review: PASS at its stated scope.

The full conjecture remains OPEN. The first B05 implication is now the dependent-bank leakage problem stated in Section 7: spend `U^T D V` / same-bank quadratic leakage jointly with the two aggregate arms before any conditional supremum or reciprocal local-minor payment. Full continuity is also still open; no continuity claim is made for Theorems 3.1 or 4.1.
