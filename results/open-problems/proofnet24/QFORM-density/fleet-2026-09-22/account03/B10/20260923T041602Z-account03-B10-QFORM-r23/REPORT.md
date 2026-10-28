SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-23T04:16:02Z.
attacking: the exact-rank-three near-null hub collar; combine the duplicated-slice diffuse theorem with a new two-row capped-basis construction so every non-near-coloop survivor is paid before any reciprocal local-minor selection.

# account03/B10 — two-row capped-basis closure of the non-near-coloop collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
**Classification:** `NEW SUPPORTING THEOREM / ENTIRE c<=63/64 SMALL-PLUECKER COLLAR PAID / FULL QFORM OPEN`.

## 1. Exact target and correction boundary

The owner target remains unrestricted: for every finite `n`, arbitrary independent real original coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite bound on the density of `Q=X^T A X`, or give a genuine target-valid counterexample. Continuity is separately requested.

This report works in the assigned **exact-rank-three** chamber

`A=R Lambda R^T`, `R^T R=I_3`, `min_j |lambda_j|>=1`, `D:=|det Lambda|>=1`.

No spectral rotation is treated as preserving independence. No arbitrary-joint rank-three coarea lemma, positive conditional projection-density moment, worst fiber supremum, pointwise law-uniform Fresnel decay, compact support, moments, log-concavity, connected support, or Gaussianity is used. The capped-basis theorem used below works directly with the characteristic-function factorization in the original independent coordinates.

The fresh B10 predecessor is

`yspennstate/math-open-problems@2734623e95f9fafea5354620290ee75ad835b7df`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T034310Z-account03-B10-QFORM-r25/REPORT.md`.

Its small-Pluecker collar reduction gives, unless an already-paid exit has fired, an ORIGINAL physical hub row

`r_0=sqrt(c)e`, `||e||=1`, `c>1/4`,                              (1.1)

with

`|A_00|<1/64`, `|e^T Lambda e|<1/16`,                            (1.2)

and fixed aggregate star norm. It also proves that if a second physical row `r_j` has transverse leverage

`h_j:=||(I-ee^T)r_j||^2 >=1/4`,                                 (1.3)

then the full density is already universally bounded (`<609`). Thus the only B10 collar state needing the argument below may assume

`h_j<1/4` for every `j!=0`.                                      (1.4)

A second completed input, account03/B16 r24,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T031836Z-account03-B16-QFORM-r24/REPORT.md`,

proves the general product-preserving duplicated-slice theorem. With

`r_j=s_j e+w_j`, `w_j perpendicular e`, `rho:=1-c`,              (1.5)

put

`delta_j=||w_j||^2+s_j^2/(2rho)`.                                (1.6)

Whenever every `delta_j<=1/2`, it proves a continuous density with

`||p_Q||_infinity
 <=3 e^(5/6)[2c rho]^(-1/6) D^(-1/3).`                           (1.7)

The remaining issue is what happens when one duplicated leverage exceeds one half. The main theorem below pays that case by an explicit capped distribution on ORIGINAL physical bases.

## 2. New theorem: two-row xor capped-basis distribution

### Theorem 2.1 — `QFORM-TWOROW-XOR-CAPPED-BASIS-v1`

Let `R` be an `n x 3` Parseval frame, `R^T R=I_3`. Select two physical rows and write

`r_0=sqrt(c)e`,
`r_1=s e+w`,                                                     (2.1)

where `||e||=1`, `w perpendicular e`, `0<c<1`, and put

`rho=1-c`, `h=||w||^2`, `theta=s^2/rho`.                         (2.2)

For every remaining row `k in C={0,1}^c`, write

`r_k=s_k e+w_k`, `w_k perpendicular e`, `u_k=||w_k||^2`.         (2.3)

Assume

`h<1/4`, `u_k<1/4` for every `k in C`,                           (2.4)

and

`theta>1-2h`.                                                     (2.5)

Then there exists an explicit probability distribution `omega` on nonsingular physical three-row bases whose every coordinate marginal is at most `1/2`. Its determinant-entropy score is exactly

`boxed: Z_omega=2 sqrt(T_0 T_1),`                                (2.6)

where

`T_0=c(1-h)`,
`T_1=s^2+rho h=rho(theta+h)`.                                    (2.7)

Consequently, for every invertible symmetric `3x3` spectral matrix `Lambda` and arbitrary independent cap-one original inputs,

`Q=X^T R Lambda R^T X`

has a bounded continuous density and

`boxed:
 ||p_Q||_infinity
 <=3e [2 |det Lambda| sqrt(T_0T_1)]^(-1/3).`                     (2.8)

Arbitrary deterministic affine terms are allowed by the same capped-basis theorem.

### Proof

The argument is entirely in the physical-coordinate Parseval frame.

#### Step 1: the two available basis packets

For any three physical rows put

`d_{abc}=det(r_a,r_b,r_c)^2`.

Define the two disjoint packets

`B_0={ {0,k,l}: k<l, k,l in C }`,
`B_1={ {1,k,l}: k<l, k,l in C }`.                               (2.9)

First compute their total squared Pluecker masses.

Because

`sum_(k in C) w_k w_k^T=I_2-w w^T`,                              (2.10)

Cauchy--Binet in `e^perp` gives

`T_0:=sum_(k<l in C)d_{0kl}
 =c det(I_2-w w^T)
 =c(1-h).`                                                        (2.11)

For the second packet use the standard Parseval inclusion identities, which follow immediately by contracting exterior products against `sum r_k r_k^T=I_3`:

`sum_(S:1 in S, |S|=3) det(R_S)^2=||r_1||^2=s^2+h`,              (2.12)

and

`sum_(S:{0,1} subset S, |S|=3)det(R_S)^2
 =||r_0 wedge r_1||^2=ch.`                                      (2.13)

Subtracting gives

`T_1:=sum_(k<l in C)d_{1kl}
 =s^2+h-ch
 =s^2+rho h.`                                                     (2.14)

Both are positive under the hypotheses.

#### Step 2: equalize the two special-coordinate marginals

On `B_a` use its normalized squared-determinant law

`nu_a({a,k,l})=d_{akl}/T_a`, `a=0,1`.                            (2.15)

Define

`omega=(1/2)nu_0+(1/2)nu_1`.                                    (2.16)

Then the special coordinates have exactly

`alpha_0=alpha_1=1/2`.                                           (2.17)

It remains to prove that no residual coordinate has marginal above one half.

#### Step 3: residual marginal in the 0-packet

Fix `k in C`. If `h u_k>0`, write

`z=(w dot w_k)/sqrt(h u_k)`, `|z|<=1`;                           (2.18)

the zero cases follow by continuity. The probability `q_{0k}` that packet `nu_0` contains `k` is

`q_{0k}
 =[||r_0 wedge r_k||^2-d_{01k}]/T_0`
` =u_k(1-h+h z^2)/(1-h).`                                       (2.19)

Hence

`q_{0k}<=u_k/(1-h)<1/3`.                                        (2.20)

#### Step 4: residual marginal in the 1-packet

Put

`t_k=s_k/sqrt(rho)`.                                             (2.21)

Parseval in the `e` direction gives

`sum_(k in C)s_k^2=rho-s^2=rho(1-theta)`,                        (2.22)

so

`|t_k|<=sqrt(1-theta).`                                         (2.23)

The two-row principal Gram constraint `I-R_{0,1}R_{0,1}^T >=0` gives

`rho(1-h)-s^2>=0`, hence

`theta<=1-h`.                                                     (2.24)

Thus

`1-2h<theta<=1-h`.                                               (2.25)

For the packet `nu_1`, exterior-product contraction gives

`q_{1k}
 =[||r_1 wedge r_k||^2-d_{01k}]/T_1`.`                           (2.26)

A direct expansion yields the exact nonnegative decomposition

`||r_1 wedge r_k||^2-d_{01k}
 =||s w_k-s_k w||^2
   +rho det(w,w_k)^2.`                                           (2.27)

After dividing by `rho` and using `z` from (2.18),

`q_{1k}
 =[theta u_k+h t_k^2
   -2 sqrt(theta h u_k)t_k z
   +h u_k(1-z^2)]/(theta+h).`                                   (2.28)

For an upper bound replace the cross term by its absolute value and put

`v=|z|`, `tau=|t_k|`.

Consider

`F=q_{0k}+q_{1k}`.                                               (2.29)

For fixed `h,theta`, the upper majorant for `F` is increasing in `u_k` and in `tau`; by (2.4),(2.23) its supremum therefore occurs at

`u_k=1/4`, `tau=sqrt(1-theta)`.                                  (2.30)

As a function of `v in [0,1]`, the coefficient of `v^2` in the majorant is

`h u_k [1/(1-h)-1/(theta+h)]
 =h u_k (theta+2h-1)/[(1-h)(theta+h)]>0`,                        (2.31)

and the linear term is nonnegative. Thus the supremum occurs at `v=1`.

We are reduced to

`F<= 1/[4(1-h)]
 +[ (sqrt(theta)/2)+sqrt(h(1-theta)) ]^2/(theta+h).`             (2.32)

The second term is decreasing in `theta` on the interval (2.25). Indeed put

`T=sqrt((1-theta)/theta)<=1`.

Then it equals

`g(T)=[1/2+sqrt(h)T]^2/[1+h(1+T^2)]`,                            (2.33)

and

`g'(T)` has the sign of

`sqrt(h)(1+h)-(h/2)T>0`.                                         (2.34)

Therefore the worst case is the lower endpoint `theta=1-2h`. Substitution gives

`F< 1/2 + [2h^2+h sqrt(2(1-2h))]/(1-h).`                         (2.35)

For `0<=h<=1/4`,

`2h^2+h sqrt(2(1-2h)) <=(1-h)/2`.                               (2.36)

For completeness, the right side after moving `2h^2` is positive; squaring (2.36) is equivalent to

`(1-h-4h^2)^2-8h^2(1-2h)>=0`,                                  (2.37)

and the left side factors as

`(4h-1)(4h^3+7h^2-2h-1)`.                                      (2.38)

On `[0,1/4]` both factors are nonpositive: the first trivially, while

`4h^3+7h^2-2h-1
 <=8h^2-1<=-1/2`                                                 (2.39)

using `h<=1/4`. Hence (2.36) holds, with strict inequality under (2.4)-(2.5). Thus

`boxed: q_{0k}+q_{1k}<1.`                                       (2.40)

The `omega`-marginal of residual coordinate `k` is

`alpha_k=(q_{0k}+q_{1k})/2<1/2`.                                (2.41)

So every physical-coordinate marginal of `omega` is capped by one half.

#### Step 5: exact determinant-entropy score

For a basis `S` in packet `a`,

`omega_S=d_S/(2T_a)`.                                            (2.42)

Therefore

`log(d_S/omega_S)=log(2T_a)`                                     (2.43)

is constant inside each packet. Since the packets carry probability one half each,

`log Z_omega
 =sum_S omega_S log(d_S/omega_S)`
` =(1/2)log(2T_0)+(1/2)log(2T_1)`,                               (2.44)

hence the exact identity

`Z_omega=2sqrt(T_0T_1)`.                                         (2.45)

Now apply the completed `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1` theorem from account01/B18,

`yspennstate/math-open-problems@8c04ccbc1f032d1a82ad505223f08e3c344bde74`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

Its hypotheses are exactly the marginal cap (2.17),(2.41), and it gives

`||p_Q||_infinity
 <=3e(|det Lambda| Z_omega)^(-1/3)`,                              (2.46)

with a continuous representative. Substituting (2.45) proves (2.8). QED.

### Interpretation

This theorem is the non-collinear continuation of the earlier exact null-ray bank score. The two special original coordinates need not be collinear. The second row may have a genuine transverse component `w`; its effect is paid by a two-packet determinant law before any reciprocal local minor is selected. No conditional density of a rotated coordinate is introduced.

## 3. Direct closure of every B10 collar state with c<=63/64

Return to the B10 r25 collar (1.1)-(1.4). Put `rho=1-c`.

Assume first

`c<=63/64`, hence `rho>=1/64`.                                   (3.1)

Because r25 already pays every row with transverse leverage at least `1/4`, we are in (1.4).

### Case A: duplicated-slice diffuse

If every residual coordinate satisfies

`delta_j=h_j+s_j^2/(2rho)<=1/2`,                                 (3.2)

apply account03/B16's completed `QFORM-DUPLICATED-SLICE-FRESNEL-v1`. Since `c>1/4`, `rho>=1/64`, and `D>=1`,

`2c rho>1/128`.                                                   (3.3)

Hence

`boxed:
 ||p_Q||_infinity
 <3e^(5/6) 128^(1/6)
 =15.4965486696... .`                                            (3.4)

This branch has a continuous density.

### Case B: one duplicated leverage is heavy

Otherwise select `j` with `delta_j>1/2`. Write

`r_j=s e+w`, `h=||w||^2`, `theta=s^2/rho`.                       (3.5)

Then

`theta>1-2h`.                                                     (3.6)

All other transverse leverages are `<1/4` by (1.4), so Theorem 2.1 applies to the special pair `(0,j)`.

Its two packet masses satisfy

`T_0=c(1-h)>(1/4)(3/4)=3/16`,                                   (3.7)

and, by (3.6),

`T_1=rho(theta+h)>rho(1-h)
 >(1/64)(3/4)=3/256`.                                             (3.8)

Therefore

`Z_omega=2sqrt(T_0T_1)>3/32`.                                    (3.9)

The capped-basis density estimate gives

`boxed:
 ||p_Q||_infinity
 <3e(32/3)^(1/3)
 =17.9511376792... .`                                             (3.10)

Again the density is continuous.

Thus:

`boxed:
 every still-unpaid B10 small-Pluecker collar state with c<=63/64 is now paid; the worst new constant is <17.952.`                  (3.11)

The result is two-sided and does not use the one-sheet/majority-sign restriction.

## 4. Compatible account04 result applied to an actual inequality

A fresh search again found no completed current-QFORM mathematical artifact for the exact designated partner `account04/B10`; I do not invent one.

I do apply the completed compatible account04/B16 fixed-pair theorem,

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

For the physical hub `r_0=sqrt(c)e` and any second row `r_j=s_j e+w_j`, it gives the exact determinant-bank identity

`P_0j:=sum_(k!=0,j)|det A_{ {0,j,k} }|
 =D ||r_0 wedge r_j||^2
 =D c h_j.`                                                       (4.1)

At the actual r25 transverse-heavy threshold `h_j>=1/4`, `c>1/4`, `D>=1`, this yields

`boxed: P_0j>1/16.`                                               (4.2)

This is the bank currency used in the already-completed r25 exit together with B10 r17's aggregate indefinite-pair Schur-bank theorem. The new proof above starts only after this actual partner-certified bank exit has failed, i.e. in `h_j<1/4` for every residual row.

## 5. What remains after this run

The r25 first debt was

`QFORM-NEARNULL-HUB-LONGITUDINAL-LOCALIZATION-v1`,

with two broad regimes: a non-near-coloop state and a true near-coloop.

The present theorem removes the former completely. In the B10 small-Pluecker collar, after all earlier exits, every state with

`1-c>=1/64`                                                      (5.1)

is now continuously bounded: either duplicated-slice diffuseness gives (3.4), or its failure produces the explicit xor capped-basis law and gives (3.10).

Therefore the first exact-rank-three B10 implication is now the strictly smaller

**`QFORM-NEARNULL-TRUE-NEARCOLOOP-CLOSURE-v1`:**

> In the small-Pluecker collar, assume an ORIGINAL hub row `r_0=sqrt(c)e` has `c>63/64`, `|e^T Lambda e|<1/16`, and the aggregate physical star remains bounded below as in r25. Prove a universal two-sided density bound while retaining the positive leakage `rho=1-c`, the nonzero hub square, and all product-source correlations exactly. The exact endpoint `rho=0` is already paid, but `rho>0` may not be deleted perturbatively.

This is now a genuine **thin near-coloop interpolation** problem; the finite-localization/non-coloop alternative is no longer part of B10's exact-rank-three debt.

A determinant-volume-only proof should not be expected to bridge `rho ->0`: the current volume-optimization work independently shows that admissible third-volume certificates can deteriorate at near-coloops while square/cross mechanisms remain uniform. The next mechanism should therefore retain the near-null hub jointly with its residual cross field, rather than force one good local triple or a worst conditional projection density.

Arbitrary additional spectral directions remain a separate debt for the full owner target.

## 6. Continuity status

The new Theorem 2.1 is obtained from an `L^1` characteristic-function envelope through the capped-basis Fresnel theorem, so it supplies a bounded continuous `C_0` density. The duplicated-slice branch (3.4) is likewise continuous.

Earlier transverse-heavy/scalar-pivot exits used to reach this chamber were invoked only for essential boundedness, so this run does **not** promote the unrestricted exact-rank-three theorem, much less the full QFORM target, to a global continuity result.

## 7. Deterministic regression check

A deterministic finite checker accompanies this report. It samples the relaxed scalar parameter region used in the marginal proof and checks

`q_0+q_1<1`

along with the explicit constants (3.4),(3.10). Its maximum sampled marginal sum is below one. This is only a regression check; the proof is the exact maximization and factorization in Section 2.

## 8. Honest status

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**  
**New theorem:** `QFORM-TWOROW-XOR-CAPPED-BASIS-v1`.  
**New target-level consequence:** every B10 small-Pluecker near-null-hub collar state with `c<=63/64` is now paid; both new subbranches are continuous.  
**First remaining B10 exact-rank-three debt:** `QFORM-NEARNULL-TRUE-NEARCOLOOP-CLOSURE-v1` with `c>63/64`.  
**Native brain ingestion:** not verified; execution remains `WITHOUT_VERIFIED_BRAIN`.
