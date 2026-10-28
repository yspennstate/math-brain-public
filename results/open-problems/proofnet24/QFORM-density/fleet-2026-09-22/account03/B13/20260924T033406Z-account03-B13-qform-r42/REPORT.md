SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-24T03:34:06Z.
attacking: combine diagonal fifth-order sparsification with the all-pair tau law to remove slope outliers and isolate an aggregate diffuse transverse-bank alternative.

# account03/B13 r42 — diagonal-tail assisted two-line localization and diffuse-bank extraction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T033406Z-account03-B13-qform-r42`  
Role: extremal product laws / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW TARGET-LEVEL STRUCTURAL THEOREMS IN THE EXACT DIAGONAL+RANK-TWO HARD CHAMBER / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

All coordinates below are original physical coordinates. No random-variable rotation is declared independent. No Gaussian, log-concavity, moment, compact-support, connected-support, single-interval extremality, bounded support diameter, bounded fragment count, pointwise van-der-Corput estimate, unrestricted joint coarea estimate, or deletion of a coefficient-small quadratic error is used.

## 1. Source-pinned premises actually used


### 1.1 Designated partner account04/B13 — diagonal fifth-order sparsification

Fresh completed partner report:

`yspennstate/math-open-problems@13f6435b5e542a496a489cff844110f4834bdec3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260924T031520Z-account04-B13-diagonal-sparsification-r2/REPORT.md`.

In the exact rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `rank(U Lambda U^T)<=2`, `s_3(A)>=1`,

write `d_(1)>=d_(2)>=...` for the decreasing rearrangement of `|d_i|`. The partner proves for every slab ratio

`rho=P{X^T A X in J}/|J|`

that

`d_(5) <= C5/rho`,                                                 (1.1)

where

`C5=2 sqrt(30 pi)=19.41625912555699...`.                           (1.2)

Equivalently, all but at most four physical diagonal coefficients obey `|d_i|<=C5/rho`. The proof is a literal five-coordinate principal-block gate, not a probabilistic deletion of the remaining diagonal tail.

The same partner report also proves the optimizer-free bathtub reduction: for every bounded nonnegative kernel, cap-one mass-one product laws can be replaced, at the level of the supremum and with arbitrarily small prescribed witness loss, by products of unit-measure measurable sets; bounded finite-union epsilon-witnesses are available. It does **not** assert interval extremality, an attained global optimizer, bounded diameter, or a uniform fragment count.

### 1.2 Hard exact-rank-two slab branch

From the earlier completed account04/B13 slab dichotomy,

`yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`,

in the diffuse exact-rank-two chamber

`max_i c_i<=1/3`, `c_i=||u_i||_2^2`,

there is a physical coordinate `k` with `|d_k|>=1`. In the hard non-rank-one branch,

`|det Lambda| > H0 rho^(-2)`,                                     (1.3)

where

`H0=sqrt(1536 e^2)=106.534455308869...`.                          (1.4)

The complementary partner branch is already the coefficient certificate

`dist_op(U Lambda U^T, SymRank_{<=1}) <=10.321552951 rho^(-1)`.    (1.5)

This run works only on the hard branch (1.3), leaving (1.5) untouched.

### 1.3 Grouped three-leaf receiver

The completed account01/B13 theorem is source-pinned at

`yspennstate/math-open-problems@38a8a2ae1cb319211ab4be60f6f8d6f7f03f85f9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T223205Z-account01-B13-qform-auto11/REPORT.md`.

Rotate only the deterministic latent two-dimensional coefficient basis so

`u_k=(sqrt(c),0)`, `c=c_k`,                                       (1.6)

and for `i!=k` write

`u_i=(x_i,y_i)`, `s_i=y_i^2`, `t_i=x_i/y_i` when `s_i>0`.          (1.7)

Then

`q_ki=c s_i`,
`q_ij=s_i s_j(t_i-t_j)^2`,                                        (1.8)

and for the physical triple `{k,i,j}`

`tau_ij=d_k q_ij+d_i q_kj+d_j q_ki`                               (1.9)

satisfies the exact normalized identity

`tau_ij/(s_i s_j)
 =d_k(t_i-t_j)^2+c(d_i/s_i+d_j/s_j)`.                             (1.10)

If `I=[n]\{k,i,j}` and

`Delta_ij=det(U_I^T U_I)>0`,                                      (1.11)

with the triple also spanning the latent two-space, then every slab ratio obeys

`Delta_ij (det Lambda)^2 |tau_ij|
 <= C_T rho^(-5)`,                                                 (1.12)

where

`C_T=759375/2=379687.5`.                                           (1.13)

No individual physical minor is inverted in (1.12).

## 2. First new theorem: diagonal-tail assisted simultaneous tau control

Assume henceforth the hard branch (1.3). If `rho<=C5`, the desired universal slab-ratio bound is already finite inside this chamber, so the only asymptotic survivor has

`rho>C5>1`.                                                        (2.1)

Let `S` be four physical indices carrying the four largest values of `|d_i|` (if fewer than four coordinates exist, take all of them). By (1.1),

`|d_i|<=C5/rho` for every `i notin S`.                             (2.2)

Because `|d_k|>=1>C5/rho`, necessarily

`k in S`.                                                          (2.3)

Now set

`eta=2/7`                                                          (2.4)

and define the additional high-leverage centers

`H={i notin S: c_i>eta}`.                                          (2.5)

Since `sum_i c_i=tr(U^T U)=2`, strict inequality in (2.5) implies

`|H|<=6`.                                                          (2.6)

Put

`C=S union H`.                                                     (2.7)

Then

`|C|<=10`, `k in C`,                                               (2.8)

and every noncenter `i notin C` obeys simultaneously

`c_i<=2/7`, `|d_i|<=C5/rho`.                                      (2.9)

### Theorem 2.1 — `QFORM-TENCENTER-ALLPAIR-TAU-v1`

For every two distinct noncenters `i,j notin C` with `s_i,s_j>0`,

`boxed:
 |tau_ij| < K_tau rho^(-1),}`                                     (2.10)

where

`K_tau
 = C_T/[1536 e^2 (2/21)^2]
 = 3688.287088390375...`.                                         (2.11)

#### Proof

Because `c_k<=1/3` and `c_i,c_j<=2/7`, for every unit latent vector `v`,

`v^T U_I^T U_I v
 =1-(u_k^T v)^2-(u_i^T v)^2-(u_j^T v)^2`
`>=1-c_k-c_i-c_j`
`>=1-1/3-4/7`
`=2/21`.                                                           (2.12)

Thus both eigenvalues of `U_I^T U_I` are at least `2/21`, so

`Delta_ij>= (2/21)^2`.                                             (2.13)

Since `s_i>0`, the pair `u_k,u_i` already spans the latent two-space, while (2.13) says the complement does as well. Hence (1.12) applies. Squaring (1.3) gives

`(det Lambda)^2>1536 e^2 rho^(-4)`.                               (2.14)

Insert (2.13)-(2.14) into (1.12) to obtain (2.10)-(2.11). QED.

The threshold `2/7` is chosen to keep at most six leverage centers while retaining a positive uniform complement determinant. This theorem is simultaneous for all remaining positive-transverse pairs.

## 3. Partner theorem applied at the actual slope inequality

The designated account04/B13 result is now used at equation level, not only cited as a structural status.

For two noncenters with `s_i,s_j>0`, combine (1.10), `|d_k|>=1`, `c<=1/3`, (2.2), and (2.10). The triangle inequality gives

`boxed:
 (t_i-t_j)^2
 <= K_tau rho^(-1)/(s_i s_j)
    +(C5/3) rho^(-1)(1/s_i+1/s_j).}`                              (3.1)

The second term in (3.1) is exactly where the fresh partner diagonal-fifth-order theorem is spent: it controls the arbitrary vertex terms `d_i/s_i` and `d_j/s_j` without assuming they vanish and without selecting an individual Pluecker minor.

This removes the two slope outliers left by r41.

## 4. New theorem: no-outlier two-line localization with constant 3.21

Set

`a=10.3`,
`alpha=a rho^(-1/3)`.                                              (4.1)

Partition the noncenters into

`L={i notin C:s_i<alpha}`,
`R={i notin C:s_i>=alpha}`.                                       (4.2)

Let

`ell_0=span(u_k)`.                                                  (4.3)

Every `i in L` satisfies exactly

`dist(u_i,ell_0)=|y_i|<sqrt(a) rho^(-1/6)`
`<3.210 rho^(-1/6)`.                                               (4.4)

For `i,j in R`, (3.1) and `rho>1` give

`(t_i-t_j)^2`
`<= [K_tau/a^2] rho^(-1/3)
   +[2C5/(3a)] rho^(-2/3)`
`<= W^2 rho^(-1/3)`,                                               (4.5)

where

`W^2=K_tau/a^2+2C5/(3a)`,
`W=6.001862961888005...`.                                          (4.6)

Hence all slopes in `R`, with **no outlier**, lie in a common interval of length

`W rho^(-1/6)`.                                                    (4.7)

If `R` is nonempty, fix any `t_0` among those slopes and set

`ell_1=span((t_0,1))`.                                             (4.8)

Then for every `i in R`,

`dist(u_i,ell_1)
 = |y_i||t_i-t_0|/sqrt(1+t_0^2)`
 <=sqrt(c_i) W rho^(-1/6)`
 <=sqrt(2/7) W rho^(-1/6)`
`<3.209 rho^(-1/6)`.                                               (4.9)

If `R` is empty, choose `ell_1` arbitrarily.

### Theorem 4.1 — `QFORM-TENCENTER-DIAGONAL-TWOLINE-3P21-v1`

In the hard exact-rank-two branch, either `rho<=C5`, or there are at most ten named original physical centers `C`, containing the selected `k`, and two latent coefficient lines `ell_0,ell_1` such that **every** noncenter satisfies

`boxed:
 |d_i|<=19.417 rho^(-1),}`                                        (4.10)

and

`boxed:
 dist(u_i,ell_0)<3.210 rho^(-1/6)
 or
 dist(u_i,ell_1)<3.210 rho^(-1/6).}`                              (4.11)

Compared with r41, the second-line constant falls from `24.540` to `3.210` and the two possible transverse slope outliers disappear, while the total named-center count stays at most ten.

Nothing in Theorem 4.1 asserts that the rowwise strip can be deleted from the phase.

## 5. Aggregate strengthening: Frobenius-small strip or a diffuse transverse bank

The same proof yields more than rowwise localization.

For the low-transverse bank `L`, define

`E_0=sum_{i in L}s_i`.                                             (5.1)

For the high-transverse bank `R`, the exact line-distance formula and (4.7) give

`sum_{i in R} dist(u_i,ell_1)^2`
`<=W^2 rho^(-1/3) sum_{i in R}s_i`
`<=W^2 rho^(-1/3)`,                                                (5.2)

because `sum_i y_i^2=1` after the latent basis alignment.

Let `U^(0)` on `C^c` be obtained by orthogonally projecting each `L` row to `ell_0` and each `R` row to `ell_1`. Then

`boxed:
 ||U_{C^c}-U^(0)||_F^2
 <=E_0+W^2 rho^(-1/3).}`                                           (5.3)

This gives an exhaustive dichotomy.

### Branch A — aggregate two-line strip

If

`E_0<=rho^(-1/6)`,                                                 (5.4)

then, using `rho>=1`,

`boxed:
 ||U_{C^c}-U^(0)||_F
 <=sqrt(1+W^2) rho^(-1/12)
 <6.085 rho^(-1/12).}`                                             (5.5)

This is now a genuine aggregate Frobenius statement, unlike r41's purely rowwise tube. It is still **not** a license to delete the resulting quadratic residual under arbitrary unbounded or fragmented inputs.

### Branch B — diffuse low-transverse bank

If instead

`E_0>rho^(-1/6)`,                                                  (5.6)

define an original-coordinate unit vector supported on `L` by

`b_i=y_i/sqrt(E_0)` for `i in L`, and `b_i=0` otherwise.           (5.7)

Then

`sum_i b_i^2=1`,                                                   (5.8)

and because every `s_i<alpha=a rho^(-1/3)`,

`boxed:
 max_i b_i^2 < a rho^(-1/6),
 max_i |b_i| <sqrt(a) rho^(-1/12)
 <3.210 rho^(-1/12).}`                                             (5.9)

Moreover

`E_0=sum_{i in L}s_i<|L| alpha`,                                  (5.10)

so (5.6) implies

`boxed:
 |L|>rho^(1/6)/a
 >0.09708 rho^(1/6).}`                                             (5.11)

Thus failure of aggregate-smallness cannot remain an amorphous rowwise obstruction: it produces a genuinely diffuse **original-coordinate transverse bank** whose normalized coefficient vector has maximal squared coordinate `O(rho^(-1/6))` and whose physical cardinality grows at least like `rho^(1/6)`.

### Theorem 5.1 — `QFORM-TWOLINE-FROB-OR-DIFFUSE-TRANSVERSE-v1`

Under the hypotheses of Theorem 4.1 and `rho>C5`, after removing at most ten named physical coordinates, one of the mutually exhaustive alternatives (5.5) or (5.8)-(5.11) holds. The diagonal tail simultaneously satisfies (4.10) in both branches.

This is the main new structural compression of the run.

## 6. Extremal-product-law formulation

The designated partner's optimizer-free product reduction applies to the actual slab kernel. Therefore any strict arbitrary cap-one product-law slab witness may be replaced, with arbitrarily small prescribed loss and the same matrix `A` and interval `J`, by a unit-measure product-indicator witness. Bounded finite-union epsilon-witnesses are also available.

All inequalities in Sections 2-5 are coefficient consequences of the slab ratio and hence survive this transfer. No single interval, centered uniform law, support-diameter cap, or uniform fragment count is introduced.

## 7. What remains unpaid

Full QFORM is **OPEN / not proved / not disproved**. Global continuity is separately **OPEN**.

The new first B13 obligation is

`QFORM-DIFFUSE-LOWTRANSVERSE-OR-FROB-SMALL-RECEIVER-v1`:

1. in Branch B, use the normalized diffuse original-coordinate vector `b` together with the `O(rho^-1)` diagonal tail in a product-preserving grouped/projected-crossing, ridge, or small-ball receiver; or
2. in Branch A, retain the `O(rho^-1/12)` Frobenius strip residual inside the actual phase rather than deleting it as a small random quadratic form.

The recent account02/B13 obstruction showing that rowwise tube width alone can hide order-one aggregate energy is respected: Branch A is reached only after the explicit aggregate test (5.4), and Branch B records the complementary aggregate energy as a real diffuse bank.

## 8. Numerical constant check

The committed checker `CHECK.py` verifies

- `C5=19.41625912555699...`;
- `K_tau=3688.287088390375...`;
- `sqrt(a)=3.209361307176...`;
- `W=6.001862961888...`;
- `sqrt(2/7)W=3.208130697965...`;
- `sqrt(1+W^2)=6.084600152293...`.

Its expected terminal marker is

`QFORM_B13_R42_DIAG_TWOLINE_CHECK_PASS`.

These computations only check arithmetic constants; the proofs above are exact inequalities.
