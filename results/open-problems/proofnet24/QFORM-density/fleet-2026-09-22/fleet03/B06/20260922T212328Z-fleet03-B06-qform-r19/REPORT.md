SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B06, 2026-09-22T21:23:28Z.
attacking: the strict-higher-rank bicolooop survivor by converting its physical double-incident 2x2-minor bank into either genuine third exterior curvature (which the regularized determinant can spend) or a much sharper rank-one tube for the physical minor matrix.

# fleet03/B06 QFORM r19 — third-curvature payment or physical rank-one incident-minor tube

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T212328Z-fleet03-B06-qform-r19`  
**Assignment:** Curved fiber integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** not proved by the theorem below; the paid branch gives an essentially bounded density after the genuine original-coordinate square.

## 1. Exact scope and fresh source-valid inputs

The target remains the unrestricted theorem for every finite dimension, independent original coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one. No moment, compact-support, Gaussian, log-concave, connected-support, diagonal-basis, or post-rotation-independence hypothesis is introduced.

This run preserves the live corrections: no law-uniform pointwise quadratic-phase decay; no arbitrary-joint rank-three coarea theorem; no positive moment of a worst normalized conditional projection density; no unrestricted fiber supremum; no assumption that a general orthogonal spectral rotation preserves independence; and no reciprocal selection of a single tiny physical minor.

The new mechanism starts from the newest completed bicolooop reduction rather than repeating the previous rank-two tube estimate.

### Input A — fleet03/B08 r20

Canonical source:

`yspennstate/math-open-problems@d5547a484fcc9b62341d80e9ba902cbe2e484284`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T201956Z-fleet03-B08-qform-diffuse-r20/REPORT.md`.

In its only unpaid nonzero-pivot fine-scale branch there are:

* a genuine original-coordinate scalar pivot coefficient `a!=0`;
* a residual original-coordinate cross block `H`;
* a scale `gamma>0`, with `g=gamma/16`;
* the normalized cross matrix

  `Z=H(g^2 I+H^T H)^(-1/2)`;

* a physical row index `j` and physical column index `r` such that the double-incident physical minor bank obeys

  `Delta_jr(Z):=sum_(k!=j)sum_(s!=r) det Z[{j,k},{r,s}]^2 >1067/2000`;       (1.1)

* the exact relation between singular values `h_nu` of `H` and `z_nu` of `Z`,

  `z_nu=h_nu/sqrt(g^2+h_nu^2)`.

The same source proves much more top-two spectral structure, but the argument below only needs (1.1) and the exact normalization relation. Thus the new theorem is genuinely an aggregate physical-minor implication, not another use of a selected spectral pair.

### Input B — regularized graph determinant

Canonical source:

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

For every original-coordinate cross block `H`, retaining arbitrary same-side quadratic phases and outside couplings, the unconditional `q=2` theorem gives

`|phi_R(t)| <= det(I+4t^2 H H^T/(pi^2 e^2))^(-1/8)`.                  (1.2)

No leverage assumption is required at `q=2`.

### Input C — compatible completed fleet04 square result actually used

The designated `fleet04/B06` still had no completed current-QFORM canonical artifact at the source check; no theorem or PASS is fabricated for it. The compatible completed fleet04 theorem actually applied is fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its proof gives, for the genuine physical square completion,

`p_Q(t) <= |a|^(-1/2) int_0^infinity p_R(t-sgn(a)u) u^(-1/2) du`.            (1.3)

For `||p_R||_3<=M`, the optimized split already proved in the B06 chain gives

`||p_Q||_infinity <= C_A |a|^(-1/2) M^(3/4)`,
`C_A=8/3^(3/4)`.                                                            (1.4)

This is the fleet04 result applied below at an actual displayed inequality.

## 2. Exterior-energy notation

For any real matrix `T`, define

`E_k(T)=sum_(|I|=|J|=k) det(T[I,J])^2`.

By Cauchy--Binet, if the singular values are `s_1,s_2,...`,

`E_k(T)=e_k(s_1^2,s_2^2,...)`.                                        (2.1)

In particular `E_2` is the total squared 2x2-minor mass and `E_3` is the total squared 3x3-minor mass.

Fix the heavy physical row `j` and column `r` from Input A. Delete them from the index sets and define the **intersection-minor matrix**

`M=(M_ks)_(k!=j,s!=r)`,

`M_ks = det Z[{j,k},{r,s}]`.                                          (2.2)

Then exactly

`||M||_F^2 = Delta_jr(Z) >1067/2000`.                                (2.3)

This packages the complete physical double-incident bank before any reciprocal operation.

## 3. New algebraic lemma: second curvature of the incident-minor matrix is third curvature of the cross block

### Lemma 3.1 — `QFORM-INCIDENT-MINOR-E2-THIRD-CURVATURE-v1`

For every real matrix `Z` and physical row/column `j,r`, let `alpha=Z_jr` and let `M` be (2.2). Then

`E_2(M) = alpha^2 * sum_(k<l, k,l!=j) sum_(s<t, s,t!=r)
                    det Z[{j,k,l},{r,s,t}]^2`.                         (3.1)

Consequently

`E_2(M) <= alpha^2 E_3(Z)`.                                            (3.2)

If `||Z||_op<=1`, then `|alpha|<=1` and therefore

`boxed( E_3(Z) >= E_2(M). )`                                           (3.3)

The statement includes `alpha=0`; in that case (3.1) forces `E_2(M)=0`.

### Proof

After permuting the selected row and column to the first position, write the relevant entries as

`Z = [[alpha, b^T],[c,D]]`.

Then

`M=alpha D-c b^T`.                                                       (3.4)

For any two remaining rows `k,l` and columns `s,t`, the elementary 3x3 Sylvester identity gives

`det M[{k,l},{s,t}]
 = alpha * det Z[{j,k,l},{r,s,t}]`.                                    (3.5)

This identity is polynomial and does not require `alpha!=0`. Squaring (3.5) and summing over all pairs gives (3.1). Equation (3.2) follows because the selected 3x3 minors are only a subcollection of all 3x3 minors. If `||Z||_op<=1`, every entry has modulus at most one, giving (3.3). QED.

### Why this matters

The previous hard state says the **sum of many physical 2x2 minors** is large. Lemma 3.1 identifies the exact obstruction to spending that bank directly: if the matrix of those minors itself has genuine rank-two exterior mass, then the original cross block necessarily has genuine third exterior curvature. That curvature can be spent by the already source-valid regularized determinant without selecting one physical minor.

## 4. Third exterior curvature gives an L3 residual density

### Lemma 4.1 — `QFORM-E3-CROSS-L3-v1`

Let `R` be any residual quadratic form on original-coordinate product inputs whose cross block across some original-coordinate cut is `H`. Arbitrary same-side quadratic/affine terms and outside conditioning/couplings are allowed. Put

`F=E_3(H)`.

If `F>0`, then `R` has an `L^3` density and

`boxed(
 ||p_R||_3 <= (9e/2)^(2/3) F^(-1/9).
)`                                                                          (4.1)

### Proof

From (1.2), with

`c=4/(pi^2 e^2)`,

`|phi_R(t)| <= det(I+c t^2 H H^T)^(-1/8)`.                         (4.2)

The determinant expansion has nonnegative elementary-symmetric coefficients, hence

`det(I+c t^2 H H^T) >=1+c^3 F t^6`.                                (4.3)

Therefore

`|phi_R(t)|^(3/2) <=(1+c^3 F t^6)^(-3/16)`.                         (4.4)

Set `B=c^3F` and `T=B^(-1/6)`. On `|t|<=T`, use the trivial bound one, contributing at most `2T`. On `|t|>=T`,

`(1+B t^6)^(-3/16) <= B^(-3/16)|t|^(-9/8)`,

and

`2 int_T^infinity B^(-3/16)t^(-9/8)dt
 =16 B^(-1/6)`.                                                       (4.5)

Thus

`J:=int_R |phi_R(t)|^(3/2)dt
 <=18 B^(-1/6)
 =18 c^(-1/2)F^(-1/6)
 =9 pi e F^(-1/6)`.                                                   (4.6)

Inverse Hausdorff--Young in the Fourier convention of the source gives

`||p_R||_3 <=(2pi)^(-2/3)J^(2/3)
            <=(9e/2)^(2/3)F^(-1/9)`,

which is (4.1). QED.

This is an integrated Fourier estimate, not the refuted pointwise one-dimensional van-der-Corput claim.

## 5. Transfer from normalized third curvature back to the actual cross block

The singular values of `Z` and `H` satisfy

`z_nu=h_nu/sqrt(g^2+h_nu^2)`,

hence

`h_nu^2 = g^2 z_nu^2/(1-z_nu^2) >= g^2 z_nu^2`.                       (5.1)

Therefore, term by term in the elementary symmetric sum,

`boxed( E_3(H) >= g^6 E_3(Z). )`                                      (5.2)

This transfer uses only the exact spectral functional relation between `H` and `Z`; it does not claim the rotated input coordinates are independent.

## 6. Main live-branch theorem: pay third curvature or force a 3-percent physical rank-one minor tube

Fix

`kappa=1/4096`.                                                        (6.1)

### Theorem 6.1 — `QFORM-BICOLOOP-E3-OR-RANK1-MINOR-TUBE-v1`

In the fleet03/B08 r20 surviving nonzero-pivot branch, form the physical intersection-minor matrix `M` from (2.2). Exactly one of the following source-valid conclusions holds.

#### Branch A — genuine third-curvature payment

If

`E_2(M)>=1/4096`,                                                       (6.2)

then the complete post-pivot quadratic form has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity < 99 / sqrt(|a| gamma).
)`                                                                      (6.3)

No rank assumption on `H`, no self-block restriction, and no physical-minor selection is made.

#### Branch B — sharply factorized physical incident bank

If

`E_2(M)<1/4096`,                                                        (6.4)

then `M` is within squared Frobenius distance

`boxed(
 inf_(rank N<=1) ||M-N||_F^2
 <125/136576
 <0.000916.
)`                                                                      (6.5)

Equivalently, the best rank-one error has Frobenius norm `<0.030253`. Moreover the leading singular value satisfies

`sigma_1(M)^2 >9092287/17072000 >0.532584`,                            (6.6)

and hence

`boxed(
 ||M-M_1||_F / sigma_1(M) <0.041455,
)`                                                                      (6.7)

where `M_1` is the best rank-one approximation.

Thus failure of the analytic payment leaves a **physical double-incident minor bank that is factorized to within 4.15 percent relative Frobenius error**, substantially sharper than the previously known global exterior-mode tube.

### Proof of Branch A

The normalized matrix `Z` is a strict contraction because its singular values are `h/sqrt(g^2+h^2)<1`, so Lemma 3.1 and (6.2) give

`E_3(Z)>=1/4096`.                                                       (6.8)

By (5.2),

`F=E_3(H)>=g^6/4096`.                                                  (6.9)

Lemma 4.1 gives

`||p_R||_3
 <=(9e/2)^(2/3) g^(-2/3) 4096^(1/9)`.                               (6.10)

Now apply the completed fleet04/B18 square theorem at the actual inequality (1.4):

`||p_Q||_infinity
 <= C_A |a|^(-1/2)||p_R||_3^(3/4)`
` <= [24/3^(3/4)] sqrt(e/2)
      |a|^(-1/2) g^(-1/2) 4096^(1/12)`.                              (6.11)

Since `4096^(1/12)=2` and `g=gamma/16`, the numerical coefficient is

`4 * 2 * [24/3^(3/4)]sqrt(e/2)
 =98.1957136523... <99`.                                               (6.12)

This proves (6.3).

### Proof of Branch B

Let the squared singular values of `M` be

`rho_1>=rho_2>=...>=0`,

put

`C=sum_i rho_i=||M||_F^2`,
`R=sum_(i>=2)rho_i`.                                                    (6.13)

By the B08 bank (2.3),

`C>1067/2000`.                                                         (6.14)

Because every `rho_i<=rho_1`,

`sum_i rho_i^2 <=rho_1 C`.

Therefore

`E_2(M)
 =(C^2-sum_i rho_i^2)/2
 >=C(C-rho_1)/2
 =CR/2`.                                                               (6.15)

Under (6.4),

`R < 2(1/4096)/(1067/2000)
   =125/136576`.                                                        (6.16)

Eckart--Young identifies `R` with the squared Frobenius error of the best rank-one approximation, proving (6.5). Also

`rho_1=C-R
 >1067/2000-125/136576
 =9092287/17072000`,                                                   (6.17)

which is (6.6). Dividing (6.16) by (6.17) and taking square roots gives the numerical bound (6.7). QED.

## 7. Interpretation: the unpaid implication is now narrower

Before this run, the strict-higher-rank bicolooop branch was described as a small spectral tail around a strong rank-two cross block. That is useful but still spectral: a small coefficient tail cannot simply be dropped under arbitrary fragmented product laws.

Theorem 6.1 converts the same survivor into a **physical aggregate dichotomy**:

1. if the incident 2x2-minor bank has even `2^-12` units of its own second exterior curvature, the regularized determinant sees a true third cross direction and the branch is paid with `<99/sqrt(|a|gamma)`;
2. otherwise the entire matrix of double-incident physical minors is within `0.030253` in Frobenius norm of one rank-one factor, with relative error below `4.15%`.

This is stronger information than merely saying that the top two singular values dominate. The remaining hard state says that essentially **all physical determinant currency incident to the heavy row and heavy column factorizes as one left vector times one right vector**. That is the exact structure needed for a grouped two-coordinate transducer; a diffuse third-curvature remainder is no longer present at meaningful scale.

The next exact obligation is therefore

`QFORM-FACTORISED-INCIDENT-BANK-TAIL-TRANSDUCER-v1`:

> starting from the live branch with `||M-M_1||_F/sigma_1(M)<0.041455`, use the rank-one factorization of the complete physical incident-minor matrix before any reciprocal selection to construct either (i) a dependence-safe grouped rank-two `L^3`/half-Riesz payment for the actual cross form, or (ii) an already-paid original-coordinate pair/ridge/three-curvature exit. The proof must retain arbitrary same-bank curvature and the nonzero residual tail rather than discarding it by moments or support truncation.

This is a strictly narrower mechanism than generic near-rank-two stability.

## 8. Computation and integrity checks

`CHECK.py` beside this report verifies:

* `125/136576=0.0009152413308...`;
* the rank-one error norm `<0.030253`;
* the leading singular-square lower bound `9092287/17072000`;
* the relative tail bound `<0.041455`;
* the paid-branch constant `98.1957136523...<99`;
* 1000 random integer instances of the exact Sylvester identity (3.5).

The recorded output terminates `STATUS=PASS`. The computation is only arithmetic/regression evidence; the proof is the algebra and inequalities above.

## 9. Status

**Proved in this run:** `QFORM-INCIDENT-MINOR-E2-THIRD-CURVATURE-v1`, `QFORM-E3-CROSS-L3-v1`, and the live-branch dichotomy `QFORM-BICOLOOP-E3-OR-RANK1-MINOR-TUBE-v1`.

**Not proved:** the full QFORM conjecture. The zero/near-zero physical-pivot branch, the global exhaustive structural bridge, and the new factorized-minor-bank tail transducer remain separate debts. Continuity is not established by this branch.

No scheduler, task, notification, email, Drive, public-release, paid-API, Codex, or cross-account action is part of this mathematics. Repository transport is not native brain ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
