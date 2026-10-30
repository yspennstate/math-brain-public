SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T01:47:01Z.
attacking: threshold-preserving elimination of arbitrary additional spectral directions, with a grouped original-coordinate Schur bank replacing single-pivot losses and final dependent remainder absorbed by the fleet04/B12 mixed-norm shear compiler.

# fleet03/B12 r22 — hostile-inertia budget for arbitrary additional eigenvalues

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Additional eigenvalue control  
**Run:** `20260923T014701Z-qform-eigenvalue-r22`  
**Status:** `PROVED SUPPORTING TARGET-LEVEL STABILITY THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains open.  The theorem below gives a dimension-free bound whenever the spectrum is cofinite on one side of a fixed threshold and shows that, under arbitrary spectral additions, only the inertia opposing that side is costly.  Added eigenvalues may be arbitrarily small or arbitrarily large, may be dense in the original coordinates, and need not commute with the baseline matrix.  No independence after spectral rotation is used.


## 1. Inputs actually used

### 1.1 Finite physical-core theorem

The completed projected-gradient theorem is source-pinned at

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`.

Its Corollary 4.1 states that on `m>=3` independent original coordinates, if the actual symmetric quadratic matrix has at least three eigenvalues of modulus at least `sigma`, then every quadratic-plus-affine output has an essentially bounded density satisfying

`||p||_infinity <= 2 sqrt(6 pi m)/sigma`.                         (1.1)

The affine term is unrestricted.  The proof uses only original-coordinate slicing and a two-dimensional product-marginal theorem; all other eigenvalues of the `m x m` matrix are unrestricted.  For `m=3` the same source gives the sharper constant `6 sqrt(pi)/sigma`.

### 1.2 Designated partner fleet04/B12

The designated completed partner result is

`yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260922T192552Z-fleet04-B12-mixed-shear-r1/REPORT.md`.

For a joint density `h(u,z)`, define

`M(h)=int esssup_u h(u,z) dz`.                                    (1.2)

For every measurable `psi`, it proves

`||p_(U+psi(Z))||_infinity <= M(h)`,                              (1.3)

without requiring `U` and `Z` to be independent.  I apply (1.3) at an actual inequality in Section 5.

## 2. Threshold-preserving hostile-inertia lemma

For a symmetric matrix `M` and `L>0`, write

`N_+(M;L)=#{eigenvalues of M >= L}`,
`N_-(M;L)=#{eigenvalues of M <=-L}`.

For a symmetric perturbation `E`, let `nu_+(E)` and `nu_-(E)` be its positive and negative inertia counts.  Zero eigenvalues count in neither.

### Theorem 2.1 — `QFORM-THRESHOLD-HOSTILE-INERTIA-BUDGET-v1`

For all real symmetric `A0,E` of the same size and every `L>0`,

`boxed: N_+(A0+E;L) >= N_+(A0;L)-nu_-(E),`                        (2.1)

and

`boxed: N_-(A0+E;L) >= N_-(A0;L)-nu_+(E).`                        (2.2)

There is **no norm or magnitude factor** in these inequalities.

#### Proof

Let `V_+` be the spectral subspace of `A0` corresponding to eigenvalues at least `L`; put `p=dim V_+=N_+(A0;L)`.  Write the spectral positive/negative decomposition of the perturbation

`E=E_+-E_-`, `E_+,E_- >=0`, `E_+ E_-=0`.

The kernel of `E_-` has codimension `nu_-(E)`.  Hence

`dim(V_+ cap ker E_-) >= p-nu_-(E)`.                              (2.3)

For every `x` in this intersection,

`x^T(A0+E)x = x^T A0 x + x^T E_+ x >= L ||x||^2`.                (2.4)

The Courant-Fischer min-max principle therefore gives at least `p-nu_-(E)` eigenvalues of `A0+E` at least `L`, proving (2.1).

For (2.2), let `V_-` be the spectral subspace of `A0` for eigenvalues at most `-L` and intersect it with `ker E_+`.  On that intersection,

`x^T(A0+E)x = x^T A0 x - x^T E_- x <=-L ||x||^2`,                (2.5)

and the negative-side Courant-Fischer characterization gives (2.2). QED.

### Interpretation

For a positive large spectral packet, **every positive added eigenvalue is free**, regardless of its size or direction; only negative inertia can erase positive threshold directions, at a cost of at most one direction per hostile eigenvalue.  For a negative packet the roles reverse.  In particular, if `rank(E)<=r`, then either threshold count can fall by at most `r`, but (2.1)-(2.2) are sharper because helpful-sign rank is not charged at all.

## 3. Cofinite one-sided spectrum forces a bounded physical core

Define the positive and negative threshold deficiencies

`d_+(A;L)=n-N_+(A;L)`,
`d_-(A;L)=n-N_-(A;L)`.                                           (3.1)

### Lemma 3.1 — every `(d+3)`-coordinate core works

Suppose `d_+(A;L)<=d` and `d<=n-3`.  Then **every** original-coordinate principal submatrix `B=A[H,H]` of size

`m=d+3`                                                           (3.2)

has at least three eigenvalues at least `L`.

Likewise, if `d_-(A;L)<=d`, every such `B` has at least three eigenvalues at most `-L`.

#### Proof

Order the eigenvalues of `A` as `lambda_1<=...<=lambda_n`.  The positive deficiency assumption gives

`lambda_(d+1)>=L`.                                                (3.3)

Let `mu_1<=...<=mu_m` be the eigenvalues of `B`.  Cauchy interlacing gives

`lambda_j <= mu_j <= lambda_(j+n-m)`.                             (3.4)

Since `m=d+3`, (3.3)-(3.4) at `j=d+1=m-2` give

`mu_(m-2)>=lambda_(d+1)>=L`;                                     (3.5)

hence `mu_(m-2),mu_(m-1),mu_m` are all at least `L`.

For the negative case, `d_-(A;L)<=d` means `lambda_(n-d)<=-L`.  At `j=3`, interlacing gives

`mu_3 <= lambda_(3+n-m)=lambda_(n-d)<=-L`,                        (3.6)

so the three smallest eigenvalues of `B` are at most `-L`. QED.

The strength relevant to the present assignment is that there is no coordinate search and no local-minor reciprocal loss: once the one-sided spectral deficiency is `d`, **any** `d+3` physical coordinates carry the needed three-direction curvature.

## 4. Main density theorem

### Theorem 4.1 — `QFORM-COFINITE-ONESIDED-SPECTRUM-v1`

Let `A` be a real symmetric `n x n` matrix and let `L>0`.  Assume that for one sign

`min(d_+(A;L),d_-(A;L)) <= d <= n-3`.                             (4.1)

For arbitrary independent real `X_i` with densities bounded by one and arbitrary affine coefficients `b,c`,

`Q=X^T A X+b^T X+c`                                               (4.2)

has an essentially bounded density with

`boxed:
 ||p_Q||_infinity <= C_d/L,
 C_d = 2 sqrt(6 pi (d+3)).
}`                                                                 (4.3)

Thus the constant depends only on the number `d` of spectral exceptions to one large same-sign half-line, not on `n`, their magnitudes, the remaining eigenvalues, or any eigenvector localization.

When `d=0`, the final matrix is sign-definite with `|A|>=L I`; a physical definite pair gives the sharper `pi/L`.  Formula (4.3) is retained as the uniform finite-core expression.

#### Proof

Take any original-coordinate set `H` of size `m=d+3`, and put `Z=X_(H^c)`.  By Lemma 3.1 the actual physical block `B=A[H,H]` has three eigenvalues of modulus at least `L`, all of the same sign.  Conditional on `Z=z`, the active polynomial in the untouched independent coordinates `X_H` is

`U_z=X_H^T B X_H + ell(z)^T X_H + c(z)`,                          (4.4)

where the cross couplings to `H^c` contribute only the affine vector `ell(z)`.  The finite-core theorem (1.1) therefore gives, uniformly in `z`,

`||p_(U_z)||_infinity <= 2 sqrt(6 pi m)/L = C_d/L`.               (4.5)

Averaging the conditional interval bound immediately proves (4.3).  Section 5 records the same final step explicitly through the designated fleet04/B12 mixed-norm shear theorem, so no hidden convolution claim is present. QED.

## 5. Actual application of fleet04/B12

Write the complete form on the physical decomposition `H union H^c` as

`Q=U+psi(Z)`,                                                     (5.1)

where

`U=X_H^T B X_H + 2 X_H^T A[H,H^c] Z + b_H^T X_H`,                (5.2)

and `psi(Z)` contains the **entire** outside quadratic block, outside affine term and constant.  Notice that `U` and `Z` are not independent because the cross term in (5.2) depends on `Z`.

Let `h(u,z)` be the joint density of `(U,Z)`.  By (4.5), for almost every `z`,

`esssup_u h(u,z)
 = p_Z(z) ||p_(U|Z=z)||_infinity
 <= p_Z(z) C_d/L`.                                                (5.3)

Hence the exact fleet04/B12 mixed norm is

`M(h)=int esssup_u h(u,z) dz <= C_d/L`.                           (5.4)

Applying the partner theorem (1.3) with the actual measurable quadratic remainder `psi` gives

`boxed: ||p_(U+psi(Z))||_infinity <= C_d/L.`                      (5.5)

This is a genuine partner application to the final inequality.  Arbitrary outside eigenvalues and all outside/cross coefficients are retained; none is replaced by an independent convolution.

## 6. Arbitrary additional-eigenvalue stability

### Theorem 6.1 — `QFORM-ADDITION-HOSTILE-INERTIA-STABILITY-v1`

Let `A=A0+E` and `L>0`.  Suppose either

`N_+(A0;L)>=n-k` and `nu_-(E)<=r`,                                (6.1)

or

`N_-(A0;L)>=n-k` and `nu_+(E)<=r`.                                (6.2)

If

`d:=k+r <= n-3`,                                                  (6.3)

then every admissible product input satisfies

`boxed:
 ||p_(X^T A X)||_infinity
 <= [2 sqrt(6 pi (k+r+3))]/L.
}`                                                                 (6.4)

The nonzero eigenvalues of `E` may have **arbitrary magnitudes**, from arbitrarily small to arbitrarily large.  Their eigenvectors may be completely delocalized, and `E` need not commute with `A0`.  In (6.1), arbitrarily many positive eigenvalues of `E` cost exactly zero; only its negative inertia `r` is charged.  The negative-base statement is symmetric.

#### Proof

Under (6.1), Theorem 2.1 gives

`N_+(A;L)>=n-k-r=n-d`,                                            (6.5)

so `d_+(A;L)<=d`.  Apply Theorem 4.1.  The other sign is identical. QED.

### Rank-r corollary

Since `nu_-(E),nu_+(E)<=rank(E)`, an arbitrary symmetric rank-`r` addition obeys the same estimate:

`rank(E)<=r => ||p_(X^T(A0+E)X)||_infinity
               <= 2 sqrt(6 pi (k+r+3))/L`                        (6.6)

whenever the baseline has `n-k` same-sign eigenvalues beyond `L` and `k+r<=n-3`.

For the especially clean base `A0>=L I_n`, adding an arbitrary rank-`r` symmetric matrix gives, independently of the added eigenvalue sizes and signs,

`r=1: C_1=17.366430109398...`,
`r=2: C_2=19.416259125557...`,
`r=3: C_3=21.269446210866...`,                                   (6.7)

all divided by `L`.  If the addition is positive semidefinite, its hostile inertia is zero and the positive-definite pair bound remains `pi/L`, regardless of its rank or norm.

This is the requested additional-eigenvalue stability mechanism: **magnitude is irrelevant; only hostile inertia consumes spectral directions.**

## 7. Relation to the previous B12 Schur theorem

The preceding fleet03/B12 run proved threshold-preserving signed Schur inheritance: eliminating `p` physical coordinates by an invertible principal Schur complement can remove at most `p` eigenvalues from either threshold count and does not degrade `L`.  The present theorem is complementary.  It shows that when the large spectrum is cofinite on one sign, no Schur recursion is needed at all: interlacing immediately compresses the full problem to `k+r+3` untouched original coordinates, and fleet04/B12 absorbs the entire dependent outside completion in one step.

Thus arbitrary extra eigenvalues are now controlled in two distinct quantitative currencies:

1. **Schur count currency:** physical eliminations spend at most their dimension and do not degrade the threshold;
2. **hostile-inertia currency:** same-sign additions are free, and opposite-sign additions spend at most one exceptional dimension each, independent of magnitude.

## 8. What this does and does not solve

The theorem is genuinely dimension-free for every fixed hostile deficiency `d=k+r`, and it permits arbitrarily many same-sign added eigenvalues.  It does **not** solve the owner target because a rank-three diffuse form with spectrum `{1,1,-1,0,...,0}` has one-sided deficiency of order `n`; (4.3) then grows like `sqrt(n)`.  This is consistent with the live correction showing that diffuse rank-three families cannot be solved by selecting one bounded physical core.

The next B12 implication is therefore not another bounded-core theorem.  It is to combine the hostile-inertia ledger with the aggregate overlap/grouped-bank machinery in the regime where both one-sided deficiencies are large, so that extra spectrum is paid before any local reciprocal curvature is selected.

**FULL QFORM STATUS:** `OPEN / NOT PROVED / NOT DISPROVED`.  
**Continuity:** not proved by Theorems 4.1/6.1.  The finite-core estimate supplies essential boundedness; the fleet04/B12 continuity upgrade requires a mixed translation modulus, which is not established here.

## 9. Computation and verification scope

`CHECK.py` performs 2,000 random finite-dimensional checks of (2.1) and of the principal-core interlacing consequence, using perturbations with hostile eigenvalues ranging over several orders of magnitude.  `CHECK_OUTPUT.txt` records `PASS` and the constants in (6.7).  These computations are sanity checks only; the proof is the exact min-max/interlacing argument above, and no Monte Carlo histogram or numerical extremality claim is used.
