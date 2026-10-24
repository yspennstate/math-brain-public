SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-23T01:13:06Z.
attacking: exact-rank-three null-ray-bank / two-sheet diffuse survivor; use a capped physical-basis distribution before any reciprocal local-minor payment, then isolate the genuinely single-hub mixed-row remainder.

# account03/B10 r22 — capped-basis payment for a collinear bank and reduction of the nonnested null-bank survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Rank-three coupled case  
**OWNER CONTROL:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `PROVED SUPPORTING TARGET-LEVEL BRANCH / FULL TARGET OPEN`.

## 1. Target and correction boundary

The owner target remains unrestricted: for arbitrary finite `n`, independent real original-coordinate inputs with densities at most one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal bound on the essential supremum of the density of `X^T A X`, or give a valid counterexample. This report works in the exact-rank-three B10 chamber and does not claim the full theorem.

The live correction set was reread. Nothing below uses post-rotation independence, arbitrary-joint rank-three coarea, a positive conditional projection-density moment, a worst fiber supremum, law-uniform pointwise quadratic-phase decay, a fixed good local minor, or coefficient-smallness as a perturbative error.

The immediate B10 source is r21,

`yspennstate/math-open-problems@3136d1f31dd7e723ddef05d06edce6fe769dc384`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T231827Z-account03-B10-QFORM-r21/REPORT.md`.

The analytic engine used in this run is the completed capped-basis Fresnel theorem,

`QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`,

at

`yspennstate/math-open-problems@8c04ccbc1f032d1a82ad505223f08e3c344bde74`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

It states: if a rank-three physical coefficient frame `L` admits a probability law `w` on nonsingular three-column bases whose coordinate marginals are all at most `1/2`, then, writing

`Z_w=exp(H(w)+E_w log det(L_S)^2)`,

for every independent cap-one product input and every invertible symmetric spectral matrix `D`,

`||p_Q||_infinity <= 3e (|det D| Z_w)^(-1/3)`,                 (1.1)

and the density has a continuous representative. Arbitrary affine terms are allowed.

The exact designated partner `account04/B10` still has no completed current-QFORM mathematical artifact at the fresh lookup; only QFORM login evidence is visible. No theorem is attributed to it. A completed compatible account04 result is applied in Section 6.

## 2. Collinear physical bank and its exact complementary pair law

Write an exact-rank-three form as

`A=R M R^T`, `R^T R=I_3`,                                      (2.1)

where the rows of `R` are physical spectral rows `u_i in R^3`, and `M` is real symmetric invertible. Put

`D=|det M|`.

Let a nonempty original-coordinate bank `B` lie on one unit spectral ray `r`:

`u_i=alpha_i r`, `i in B`,

and set

`L=sum_(i in B) alpha_i^2`, `0<L<=1`.                            (2.2)

No nullity assumption on `r^T M r` is needed for the theorem below. Let `C=B^c`, and for `j in C` put

`y_j=P_(r^perp) u_j`.

Parseval gives

`sum_(j in C) u_j u_j^T=I-L rr^T`,

hence on the two-dimensional plane `r^perp`,

`sum_(j in C) y_j y_j^T=I_(r^perp)`.                             (2.3)

For `j<k` in `C` define

`nu_jk=det(r,u_j,u_k)^2=det_(r^perp)(y_j,y_k)^2`.                (2.4)

### Lemma 2.1 — exact complement-pair probability law

The numbers `(nu_jk)` form a probability distribution on complementary pairs:

`sum_(j<k) nu_jk=1`.                                            (2.5)

Its coordinate marginal at `j` is exactly the transverse leverage

`q_j:=sum_(k != j) nu_{min(j,k),max(j,k)}=||y_j||^2`.           (2.6)

#### Proof

Equation (2.5) is the two-dimensional Cauchy--Binet identity applied to (2.3). For (2.6), let `J` be the quarter-turn matrix on `r^perp`. Then

`sum_k det(y_j,y_k)^2
 = y_j^T J^T (sum_k y_k y_k^T) J y_j
 = ||y_j||^2`,

and the `k=j` summand is zero. QED.

Thus the condition

`max_(j in C) ||P_(r^perp)u_j||^2 <=1/2`                        (2.7)

is exactly the statement that every complement coordinate marginal of the pair law is capped by `1/2`.

## 3. Optimize the bank marginal before taking absolute Fourier values

Write

`a_i=alpha_i^2`, `h=max_(i in B) a_i`, `s=L-h`.                 (3.1)

We need a probability distribution `p=(p_i)` on the bank with `p_i<=1/2`. Define the determinant-entropy objective

`F(p)=sum_i p_i log(a_i/p_i)`.                                  (3.2)

Since

`F(p)=log L - KL(p || a/L)`,                                    (3.3)

its exact maximizer under `p_i<=1/2` is the information projection of the natural bank-volume law onto the cap.

### Lemma 3.1 — exact capped bank score

If `h<=L/2`, take

`p_i=a_i/L`.

Then every `p_i<=1/2` and

`exp(F(p))=L`.                                                   (3.4)

If `h>L/2`, the maximizing coordinate is unique. Let `i_*` be its index and take

`p_(i_*)=1/2`,
`p_i=a_i/[2(L-h)]` for `i != i_*`.                              (3.5)

Then every `p_i<=1/2` and

`exp(F(p))=2 sqrt(h(L-h))=2 sqrt(hs)`.                           (3.6)

#### Proof

The first case is equality in (3.3). In the second case the unconstrained optimizer has `a_(i_*)/L>1/2`, so the unique active KKT constraint is `p_(i_*)=1/2`; strict concavity of `F` forces the other masses to be proportional to `a_i`. Their total is `1/2`, giving (3.5). Substitution gives

`F=(1/2)log(2h)+(1/2)log(2s)=log(2sqrt(hs))`.

QED.

## 4. Main theorem: whole collinear bank paid by one capped basis distribution

### Theorem 4.1 — `QFORM-COLLINEAR-BANK-CAPPED-BASIS-v1`

Assume (2.1)-(2.7). Let

`Z_B = L` if `h<=L/2`,

and

`Z_B = 2sqrt(h(L-h))` if `h>L/2`.                               (4.1)

Then for arbitrary independent original-coordinate probability densities bounded by one,

`boxed: ||p_Q||_infinity <=3e (D Z_B)^(-1/3).`                  (4.2)

Moreover `Q` has a continuous density representative.

#### Proof

For each nonsingular physical basis consisting of one bank coordinate `i in B` and one complement pair `j<k in C`, define

`w_(i,j,k)=p_i nu_jk`,                                          (4.3)

where `p` is the optimizer from Lemma 3.1.

By Lemma 2.1, `w` is a probability law. Its bank-coordinate marginals are `p_i<=1/2`, while its complement-coordinate marginal at `j` is

`sum_i p_i sum_(k != j)nu_jk=q_j<=1/2`.                         (4.4)

Hence `w` satisfies the capped-basis hypothesis of (1.1).

The physical basis determinant factorizes exactly:

`det(u_i,u_j,u_k)^2
 = alpha_i^2 det(r,u_j,u_k)^2
 = a_i nu_jk`.                                                  (4.5)

Therefore the determinant-entropy score is

`log Z_w
 = sum_(i,j<k) p_i nu_jk log[(a_i nu_jk)/(p_i nu_jk)]`
` = sum_i p_i log(a_i/p_i)`                                    (4.6)

(the pair-volume factor cancels before any reciprocal payment). By Lemma 3.1, `Z_w=Z_B`. Apply (1.1) with coefficient frame `R^T` and spectral matrix `M` to obtain (4.2). The same theorem supplies continuity. QED.

### Why this is different from selecting a physical triple

Every individual determinant in (4.5) may tend to zero. The theorem never chooses one of them and never sums reciprocal local determinants. It first places a probability law on the whole product of the bank distribution and the exact two-dimensional Cauchy--Binet pair law; only the aggregate determinant-entropy score is paid.

No projected spectral coordinates are declared independent. The only independence used by the capped-basis theorem is the original physical product law.

## 5. Direct closure of most of B10's near-endpoint nonnested null-bank branch

Return now to the exact null-ray bank from B10 r15/r17:

`r^T M r=0`, `D=|det M|>=1`,                                    (5.1)

and to the near endpoint

`L>=7/8`.                                                        (5.2)

B10 r17's remaining **nonnested** condition after cap-one compression is that every complement row has transverse leverage at most `1/2`. The compression whitening in r15 scales only the `r` direction, so the transverse component is unchanged. Consequently the r17 nonnested condition is exactly (2.7) in the original pre-compression frame, and Theorem 4.1 applies directly there.

There are two quantitatively paid subbranches.

### 5.1 Diffuse null bank

If `h<=L/2`, then `Z_B=L>=7/8`; hence

`boxed: ||p_Q||_infinity
 <=3e(8/7)^(1/3)
 =8.5260207568... .}`                                           (5.3)

### 5.2 One clipped heavy atom but a nontrivial null-ray remainder

Assume `h>L/2` and

`s=L-h>=1/64`.                                                   (5.4)

Then `h>L/2>=7/16`, so

`Z_B=2sqrt(hs)
 >=2sqrt((7/16)(1/64))
 =sqrt(7)/16`.                                                   (5.5)

Therefore

`boxed: ||p_Q||_infinity
 <=3e(16/sqrt(7))^(1/3)
 =14.8572828292... .}`                                          (5.6)

Both (5.3) and (5.6) include a continuous density representative.

### 5.3 Exact shape of the survivor

If neither paid subbranch applies, then one actual ORIGINAL null-ray coordinate carries

`h>L-1/64>=55/64`.                                               (5.7)

Thus the former high-cardinality nonnested null-bank obstruction is reduced to a genuine **single physical null hub** of leverage `>55/64`, plus less than `1/64` of additional exact-null-ray bank mass, while every complementary row has transverse leverage at most `1/2`.

Write every complement row as

`u_j=t_j r+y_j`, `y_j in r^perp`.                               (5.8)

Parseval gives the exact mixed-row ledger

`sum_(j in C)t_j^2=1-L<=1/8`,
`sum_(j in C)y_j y_j^T=I_2`,
`sum_(j in C)t_j y_j=0`,
`||y_j||^2<=1/2`.                                                (5.9)

This is substantially narrower than the previous generic near-null/two-sheet survivor. It retains precisely the product-origin longitudinal/transverse overlap which the live conditional-cap counterexample says cannot be discarded.

## 6. Completed compatible account04 result applied at an actual inequality

Fresh lookup still finds no completed current-QFORM theorem from the exact designated `account04/B10`, so none is fabricated.

I apply the completed compatible account04/B20 r4 theorem

`QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T011956Z-account04-B20-QFORM-r4/REPORT.md`.

It proves that, for an exact-rank-three target with a heavy physical row `u_0=sqrt(c)e`, `c>=1/2`, if all other original-coordinate rows can be partitioned into a purely longitudinal bank (parallel to `e`) and a purely transverse bank (in `e^perp`), and if `|e^T M e|<=1/2`, then

`||p_Q||_infinity
 <= C_* 2^(7/6) D^(-1/3)
 <105.463`,                                                      (6.1)

where `C_*=103680^(1/3)`.

Apply this to the survivor (5.7)-(5.9), with `e=r`, `c=h>55/64`, and `r^TMr=0`. If no genuinely mixed complement row exists, the hypotheses of account04/B20 r4 are exactly met and (6.1) yields

`boxed: ||p_Q||_infinity<105.463.`                               (6.2)

Equivalently, after the present run and the completed account04 theorem, every still-unpaid member of the near-endpoint nonnested null-bank branch must contain a genuinely mixed original row

`t_j !=0`, `y_j !=0`,                                           (6.3)

inside the exact orthogonality ledger (5.9). In fact, if the bank `B` is chosen maximal among rows exactly collinear with `r` and `L<1`, then (5.9) forces such a mixed row automatically.

This is an actual application of completed account04 mathematics to the new reduction, not an extension of its hypotheses.

## 7. First unpaid implication after this run

The first B10 exact-rank-three debt is now

`QFORM-SINGLE-NULL-HUB-MIXED-ROW-v1`:

prove a universal density bound in the exact-rank-three state having

1. one ORIGINAL physical row `u_0=sqrt(h)r` with `h>55/64` and `r^TMr=0`;
2. additional rows exactly collinear with `r` of total leverage `<1/64`;
3. complementary rows `t_j r+y_j` satisfying the exact product-frame ledger (5.9), with `||y_j||^2<=1/2`;
4. at least one genuinely mixed row, so the longitudinal scalar bank and transverse two-dimensional product projection overlap in original-coordinate support.

The live `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` correction explains why merely observing a bounded transverse two-dimensional projection density and a bounded conditional longitudinal density is insufficient. The next payment must use the exact product-linear provenance and orthogonality `sum t_j y_j=0`, before taking any conditional-height supremum.

This is also the mixed-row approximate-coloop/anchor-shear obstruction identified independently by account04/B20 r4. The small coefficient norm `sum t_j^2<=1/8` is **not** treated as a perturbative error.

The full exact-rank-three theorem remains open. Arbitrary additional spectral directions remain a separate debt for the full owner target.

## 8. Deterministic regression check

`VERIFY.py` in this run folder checks the exact pair-law marginal identity and determinant-entropy factorization on two Parseval fixtures: a diffuse bank and a clipped-heavy bank. The maximum frame, pair-mass and marginal errors are at machine precision (`<=4.45e-16`), and the full basis entropy score agrees with the closed form to machine precision. It also reproduces the constants

`3e(8/7)^(1/3)=8.526020756855885`,

`3e(16/sqrt(7))^(1/3)=14.857282829214617`.

These computations are regression checks only; Sections 2-6 are algebraic proofs.

## 9. Status and regularity

Proved here:

- `QFORM-COLLINEAR-BANK-CAPPED-BASIS-v1` with exact optimized determinant-entropy score;
- continuous density in that theorem;
- universal bounds `<8.527` and `<14.858` for the two large portions of the r17 nonnested near-endpoint null-bank branch;
- reduction of the remaining branch to one original null hub of leverage `>55/64` plus the exact mixed-row ledger (5.9);
- by direct application of account04/B20 r4, the no-mixed-row endpoint is already universally paid.

Not proved: `QFORM-SINGLE-NULL-HUB-MIXED-ROW-v1`, the unrestricted exact-rank-three theorem, the arbitrary-extra-spectrum passage, or the full owner conjecture.

**Full QFORM conjecture: OPEN / NOT PROVED.**
