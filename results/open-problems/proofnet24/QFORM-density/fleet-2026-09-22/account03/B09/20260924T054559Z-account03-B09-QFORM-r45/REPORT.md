SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T05:45:59Z.
attacking: pair-resource aggregation or paid routing; remove reciprocal dependence on an individual Schur scalar/star by polynomializing the three physical pair currencies and aggregating them before selecting a pair.

# account03/B09 r45 — polynomialized aggregate pair-Schur currency

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / quantitative inequalities and rigorous computations  
Run: `20260924T054559Z-account03-B09-QFORM-r45`  
Status: **NEW SUPPORTING ALGEBRA + AGGREGATE RECEIVER / FORCING SUBCLAIM REFUTED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

All coordinates below are literal ORIGINAL coordinates. No spectral rotation is applied to random variables. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, or post-rotation independence assumption is used. This report does not use the refuted law-uniform pointwise quadratic-phase decay claim.

## 1. Immediate source boundary

The same-slot predecessor is account03/B09 r44,

`yspennstate/math-open-problems@1d81e62c818d6b592a6a6da78870f12f533d615a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T044555Z-account03-B09-QFORM-r44/REPORT.md`.

Its combined scalar-or-star theorem says that for a literal invertible indefinite physical pair `B`, after exact Schur completion with scalar coefficient `s` and whole physical Schur-star row `m`, the full ambient quadratic form has an essentially bounded density with

`||p_Q||_infinity <= C44 [ |det B| sigma_min(B) (|s|+||m||) ]^(-1/4)`,   (1.1)

where

`C44=15.059181790788745`.                                                (1.2)

The coefficient is uniform through `s=0`. Continuity is not asserted by this pair-log receiver.

The present run attacks the next debt: aggregate the quantity in (1.1) over the three physical pairs in a three-coordinate packet without dividing by an individual `det B` or by `s`.

## 2. Rank-two packet and polynomialized Schur stars

Let `L={1,2,3}` be three literal coordinates and `J` a disjoint literal bank. Conditional on every outside coordinate, write the relevant coefficient packet as

`Q = Y^T P Y + 2 Y^T C Z + G(Z) + affine terms`,                        (2.1)

where `P=P^T` is `3 x 3`, `C` is `3 x |J|`, and here `rank C=2`.

For `k in L`, put

`H_k=L\{k}`,
`B_k=P[H_k,H_k]`,
`p_k=P[H_k,k]`,
`c_k=C[k,:]`,
`C_k=C[H_k,:]`.                                                         (2.2)

Define the **polynomial Schur-star row**

`g_k := det(B_k) c_k - p_k^T adj(B_k) C_k`.                            (2.3)

This definition makes sense even when `B_k` is singular. If `B_k` is invertible and

`s_k=P_kk-p_k^T B_k^(-1)p_k`,
`m_k=c_k-p_k^T B_k^(-1)C_k`,                                           (2.4)

then exactly

`det(B_k) s_k = det P`,
`g_k = det(B_k) m_k`.                                                   (2.5)

Thus the dangerous inverse pair determinant has disappeared from `(det P,g_k)`.

## 3. Exact determinant identity

### Theorem 3.1 — `QFORM-RANK2-PAIR-SCHUR-CAUCHYBINET-v1`

Let `Delta=sigma_1(C)sigma_2(C)`, and let `n` be a unit vector spanning `ker(C^T)`. Then

`boxed:
 det(P^2 + C C^T)
 = (det P)^2 + sum_{k=1}^3 ||g_k||_2^2 + Delta^2 ||P n||_2^2.
`                                                                        (3.1)

This is an exact coefficient identity in the original coordinate packet.

### Proof

Set `M=[P C]`, a `3 x (3+|J|)` matrix. Since `P=P^T`,

`M M^T=P^2+CC^T`.                                                       (3.2)

Cauchy--Binet expands `det(MM^T)` as the sum of squares of all `3 x 3` column minors of `M`.

There are four types.

1. Three `P` columns. Their contribution is `(det P)^2`.

2. Two `P` columns and one `C` column. For the two-column set `H_k` and a physical column `C[:,j]`, block expansion gives

`det[ P[:,H_k], C[:,j] ] = +/- (g_k)_j`.                               (3.3)

Hence the total contribution is `sum_k ||g_k||^2`.

3. One `P` column and two `C` columns. If `c_r,c_s` are two physical columns of `C`, then summing over the three `P` columns gives

`sum_i det[P[:,i],c_r,c_s]^2 = ||P(c_r x c_s)||_2^2`.                 (3.4)

Because `rank C=2`, every `c_r x c_s` lies in the one-dimensional space `ker(C^T)=span{n}`. Moreover

`sum_{r<s} (c_r x c_s)(c_r x c_s)^T = adj(CC^T)=Delta^2 n n^T`.       (3.5)

Therefore the whole one-`P`/two-`C` contribution equals

`Delta^2 ||Pn||^2`.                                                     (3.6)

4. Three `C` columns. This contribution vanishes because `rank C=2`.

Adding the four classes proves (3.1). QED.

A second exact bookkeeping identity follows. Put

`D_k := (det P)^2+||g_k||^2`.                                           (3.7)

Then

`sum_k D_k = 3(det P)^2 + sum_k ||g_k||^2`.                            (3.8)

Thus the scalar Schur curvature and the whole Schur star can be aggregated before any physical pair is selected.

## 4. Aggregate pair receiver

Let

`E={k: B_k is invertible and indefinite}`,
`kappa_k=sigma_min(B_k)` for `k in E`.                                 (4.1)

Define the eighth-order aggregate pair currency

`R_pair := sum_{k in E} kappa_k^2 D_k
         = sum_{k in E} kappa_k^2[(det P)^2+||g_k||^2]`.               (4.2)

### Theorem 4.1 — `QFORM-INDEFINITEPAIR-AGGREGATE-CURRENCY-v1`

If `R_pair>0`, then the full ambient quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C44 |E|^(1/8) R_pair^(-1/8)
 <= 17.275934 R_pair^(-1/8).
`                                                                        (4.3)

Consequently every interval `I` obeys

`P{Q in I} <= 17.275934 R_pair^(-1/8) |I|`.                            (4.4)

Continuity is not separately proved by this receiver.

### Proof

For every `k in E`, (2.5) turns the exact r44 resource into

`|det B_k| kappa_k (|s_k|+||m_k||)
 = kappa_k (|det P|+||g_k||)
 >= kappa_k sqrt(D_k)`.                                                 (4.5)

Applying r44 to that pair gives

`||p_Q||_infinity <= C44 [kappa_k sqrt(D_k)]^(-1/4)`.                  (4.6)

Choose the best `k in E`. Since

`max_{k in E} kappa_k^2 D_k >= R_pair/|E|`,                            (4.7)

we obtain (4.3). Because `|E|<=3`,

`C44*3^(1/8)=17.275933866216054`.                                      (4.8)

No reciprocal `det B_k`, `s_k`, or `m_k` appears in the aggregate currency. QED.

### Useful full-indefinite specialization

If all three principal physical pairs are invertible indefinite and

`kappa_* = min_k sigma_min(B_k)`,                                      (4.9)

then by (3.8)

`R_pair >= kappa_*^2 [3(det P)^2+sum_k||g_k||^2]`.                    (4.10)

Writing

`T=det(P^2+CC^T)`, `V=Delta^2||Pn||^2`,                               (4.11)

Theorem 3.1 gives

`3(det P)^2+sum||g_k||^2 = T+2(det P)^2-V >= T-V`.                    (4.12)

Hence if `V<=T/2`,

`||p_Q||_infinity
 <= C44*6^(1/8) kappa_*^(-1/4) T^(-1/8)
 <18.842 kappa_*^(-1/4) T^(-1/8)`.                                   (4.13)

This cleanly separates the local row-volume into a pair-Schur-paid part and the already identified rank-two overlap currency `V`.

## 5. Target-valid regression

Take

`P=[[0,1,1],[1,0,1],[1,1,0]]`,
`C=(1/2)[[1,0],[0,1],[0,0]]`,
`A=[[P,C],[C^T,0_2]]`.                                                  (5.1)

The spectrum is approximately

`{-1.20710678,-1.08113883,0,0.20710678,2.08113883}`,                   (5.2)

so this is target-valid: exactly three eigenvalues have modulus at least one.

Every physical pair `B_k=[[0,1],[1,0]]` is invertible indefinite with `kappa_k=1`. Direct evaluation gives

`det P=2`,
`D_1=D_2=D_3=4.5`,
`R_pair=13.5`.                                                         (5.3)

Therefore the new aggregate theorem gives the explicit full-law bound

`boxed: ||p_Q||_infinity <= 12.478138789189643`,                       (5.4)

and the same constant times interval length. This is an actual `O(|I|)` conclusion, not a square-root small-ball estimate.

## 6. A necessary correction: pair-resource scale is not forced by s_3(A)>=1

### Proposition 6.1 — `QFORM-PAIRRESOURCE-UNIVERSAL-SCALE-FALSE-v1`

The target spectral hypothesis does **not** force `R_pair>0`, even in a five-coordinate rank-two-cross packet.

Let

`S=[[1,1,1],[1,1,-1],[1,-1,1]]`,
`P=2S`,
`C_eps=eps [[1,0],[0,1],[0,0]]`,
`A_eps=[[P,C_eps],[C_eps^T,0_2]]`,                                    (6.1)

with `0<eps<=1/2`.

The eigenvalues of `P` are `{-2,4,4}`. The off-diagonal block perturbation has operator norm `eps`, so Weyl's inequality gives one eigenvalue of `A_eps` at most `-2+eps<=-3/2` and two eigenvalues at least `4-eps>=7/2`. Thus every `A_eps` satisfies the owner's three-large-eigenvalue hypothesis.

But every `2 x 2` principal block of `P` is

`[[2,+/-2],[+/-2,2]]`,                                                 (6.2)

with eigenvalues `{0,4}`. Therefore `E` is empty and

`R_pair=0`                                                             (6.3)

for the entire family.

At `eps=1/2` the numerical full spectrum is

`{-2.08063488,-0.06155281,0.05976600,4.02086888,4.06155281}`.          (6.4)

Hence a proof cannot finish by forcing a universal lower bound on the aggregate indefinite-pair resource. The singular/definite-pair chamber must be routed to a different paid mechanism. This refutes only that intermediate forcing claim, not QFORM.

## 7. Designated account04/B09 result applied

The completed account04/B09 physical-cross theorem at

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`,

states that a literal invertible original-coordinate `3 x 3` cross block `K` gives a continuous density and

`||p_Q||_infinity <= 3 |det K|^(-1/3)`.                               (7.1)

Apply it to

`K=diag(2,1,1)`,
`A=[[0,K],[K,0]]`.                                                      (7.2)

The spectrum is `{-2,-1,-1,1,1,2}` and `det K=2`, so the actual inequality is

`boxed: ||p_Q||_infinity <= 3*2^(-1/3)=2.3811015779522995`,            (7.3)

with

`P{Q in I} <= 2.3811015779522995 |I|`                                 (7.4)

and a continuous density.

## 8. What changed and next exact debt

The r44 pair resource is no longer tied to a reciprocal individual Schur determinant. The scalar and whole-star pieces have been replaced by polynomial minors `(det P,g_k)`, and all eligible physical pairs can be spent through the single aggregate currency `R_pair` before selection.

The exact Cauchy--Binet identity (3.1) also identifies the resource not seen by this aggregate: the one-`P`/two-cross term

`V=Delta^2||Pn||^2`.                                                    (8.1)

The new counterexample proves that the owner spectral hypothesis cannot force the indefinite-pair aggregate itself to positive universal scale. The next B09 debt is therefore

`QFORM-SINGULAR-DEFINITE-PAIR-ROUTING-v1`:

when `R_pair` is small or zero, route the coefficient mass in `(det P,g_k,V)` into (i) a rank-two grouped crossing receiver, (ii) a scalar/diagonal pivot, (iii) a literal disjoint third-volume block, or (iv) a finite-core receiver, while retaining every quadratic residual exactly. The first essential subcase is the singular-principal-pair chamber exposed by (6.1).

Full unrestricted QFORM remains **OPEN**. Full-target continuity remains **OPEN**. The new aggregate-pair branch proves only essential boundedness; the designated partner branch proves continuity in its own scope.

## 9. Deterministic verification

`CHECK.py` beside this report verifies (3.1) on seeded random rank-two packets, the polynomial minor identity (3.3), the regression spectrum and currencies, the no-go family, and the partner numerical inequality. `CHECK_OUTPUT.txt` records the run.
