SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T09:30:27Z.
attacking: finite-mixture extremal-product reduction, then a partner-derived high-ratio cross-singular profile and optimized global max-volume skeleton.

# fleet01/B13 auto19 — L1 product-mixture compiler and high-ratio global skeleton

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Extremal product laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING REDUCTION + PROVED TARGET-LEVEL STRUCTURAL CONSEQUENCES / FULL QFORM OPEN / CONTINUITY OPEN**

## 1. Target, corrections, and pinned premises

The full target remains OPEN: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal linear slab bound

`P(X^T A X in J) <= C |J|`

for all intervals `J`, or give a valid counterexample. Continuity of the density is a separate stronger conclusion.

No step below uses pointwise quadratic oscillatory decay, independence after rotating the physical coordinates, projection-density-only control of an indefinite quadratic pushforward, the false arbitrary-joint rank-three coarea inequality, positive moments of conditional projection-density caps, a single interval or centered uniform extremizer, bounded support diameter, a uniform fragment count, or perturbative deletion of a small quadratic coefficient on remote fragmented supports.

Completed premises actually used:

1. **Designated partner `fleet02/B13`, r24.**  
   `yspennstate/math-open-problems@cc40e95933db0262eddb6e679211145a84dca081`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T085705Z-fleet02-B13-extremal-r24/REPORT.md`.

   For every integer `m>=5`, define the complete disjoint exterior energy

   `D_m^perp(A)=sum_{R cap C=empty, |R|=|C|=m} det A[R,C]^2`.

   The partner proves the cut-free slab/density estimate

   `||p_Q||_infinity <= C_m [D_m^perp(A)]^(-1/(2m)),`
   `C_m=2 sqrt(2e) m/(m-4)`,                                      (1.1)

   with the corresponding geometric product-set inequality and arbitrary same-side/outside terms retained.

   For an ORIGINAL scalar pivot `a=A_kk!=0`, with full scalar Schur complement

   `S=A[-k,-k]-a^(-1)A[-k,k]A[k,-k]`,                            (1.2)

   and complete disjoint scalar-bordered energy `B_{m+1,k}^perp(A)`, the same report proves

   `B_{m+1,k}^perp(A)=a^2 D_m^perp(S)`                            (1.3)

   and

   `||p_Q||_infinity <= T_m ( |a|^(2(m-1)) B_{m+1,k}^perp(A) )^(-1/(4m)),`
   `T_m=4(2e)^(1/4) sqrt(m/(m-4))`.                              (1.4)

   The partner also proves finite-family product purification. This run does not merely restate it: Section 2 supplies a stronger law-level finite-mixture approximation in `L1`, and Sections 4–5 apply (1.1) and (1.4) to actual singular-value inequalities.

2. **Earlier `fleet01/B13` max-volume skeleton.**  
   `yspennstate/math-open-problems@66b5ff888a219c7c8e754dd25062fac6aecb2f22`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T002634Z-fleet01-B13-qform-auto12/REPORT.md`.

   If every disjoint physical cross block has `(r+1)`-st singular value at most `sigma`, a single maximum-volume disjoint `r x r` physical pivot yields

   `A=D+R+E`,                                                      (1.5)

   where `D` is diagonal, `R` is symmetric with `rank R<=4r`, `E` is symmetric with zero diagonal, `E` vanishes on every row or column meeting the `2r`-coordinate pivot core, and

   `|E_ij| <= (r+1) sigma`.                                       (1.6)

   If no invertible disjoint `r x r` minor exists, the exact cross rank is at most `r-1` and the same source gives `A=D+R` with `rank R<=4(r-1)` and `E=0`.

All uses below stay in original physical coordinates.

## 2. Finite-mixture convexification of one cap-one density

The partner's finite-family purification produces one product indicator that approximately preserves finitely many tests. For inequalities linear in the law there is a complementary, stronger uniform mechanism: approximate the **whole law in L1** by a finite convex mixture of indicator laws. This simultaneously controls every bounded test without choosing a finite battery in advance.

### Theorem 2.1 — `QFORM-CAP1-L1-FINITE-MIXTURE-v1`

Let

`F={f in L1(R): 0<=f<=1, int_R f=1}`.

For every `f in F` and every `eta>0` there are finitely many weights `theta_l>=0`, `sum_l theta_l=1`, and bounded finite unions of intervals `E_l subset R`, each of Lebesgue measure exactly one, such that

`|| f - sum_l theta_l 1_{E_l} ||_1 < eta`.                        (2.1)

Moreover the sets can be chosen as finite unions of equal-length grid cells.

#### Proof

**Step 1: compactify without violating the cap or mass.**  
Choose `R` so that

`delta=int_{|x|>R} f(x) dx`

is arbitrarily small. Choose a bounded interval `I` disjoint from `[-R,R]` with `|I|=delta`, and set

`g=f 1_{[-R,R]}+1_I`.

Then `0<=g<=1`, `int g=1`, `g` has bounded support, and

`||f-g||_1 <=2 delta`.                                            (2.2)

**Step 2: equal-cell conditional expectation.**  
Fix a large integer `q`. Cover the bounded support of `g` by finitely many adjacent half-open cells

`C_j=[a+(j-1)/q,a+j/q)`, `j=1,...,N`,

of common length `1/q`. Define

`alpha_j=q int_{C_j} g(x) dx`.                                   (2.3)

Because `0<=g<=1`, `0<=alpha_j<=1`. Because the cells cover the support and `int g=1`,

`sum_{j=1}^N alpha_j=q`.                                          (2.4)

Let

`s_q=sum_j alpha_j 1_{C_j}`.                                     (2.5)

As the mesh `1/q` tends to zero, `||s_q-g||_1 ->0`. One proof is to approximate `g` in `L1` by a continuous compactly supported function; equal-cell averaging converges uniformly for the continuous approximation, and conditional expectation is an `L1` contraction.

**Step 3: the hypersimplex is the convex hull of fixed-cardinality 0-1 vectors.**  
The coefficient vector `alpha=(alpha_1,...,alpha_N)` lies in the finite-dimensional hypersimplex

`H_{N,q}={u in [0,1]^N: sum_j u_j=q}`.                            (2.6)

Every extreme point of `H_{N,q}` is a `0-1` vector with exactly `q` ones. Indeed, if two coordinates are strictly between zero and one, they can be perturbed by `+epsilon,-epsilon` while remaining in `H_{N,q}`, so the point is not extreme. Since the coordinate sum is the integer `q`, there cannot be exactly one fractional coordinate. Therefore, by finite-dimensional convexity (or Caratheodory),

`alpha=sum_l theta_l v^(l)`,                                     (2.7)

where every `v^(l)` is a `0-1` vector with exactly `q` ones, `theta_l>=0`, and `sum_l theta_l=1`. Caratheodory gives at most `N+1` vertices if a numerical bound on the number of mixture terms is desired.

For each vertex put

`E_l=union_{j:v_j^(l)=1} C_j`.                                   (2.8)

Then `E_l` is bounded, is a finite union of intervals, and

`|E_l|=q*(1/q)=1`.                                                (2.9)

Equations (2.5) and (2.7) give the exact identity

`s_q=sum_l theta_l 1_{E_l}`.                                     (2.10)

Choose first `delta`, then `q`, so that (2.2) plus `||g-s_q||_1` is below `eta`. This proves (2.1). QED.

The theorem is a finite-mixture approximation statement, not an assertion that a single interval is extremal and not a fixed-fragment theorem. The number and locations of grid cells may depend on `f` and `eta`.

## 3. Product-law mixture and an exact geometric-to-law compiler

### Theorem 3.1 — `QFORM-PRODUCT-L1-MIXTURE-COMPILER-v1`

Let `f_1,...,f_n in F`. For every `eta>0` there is a finite probability mixture

`h_eta(x)=sum_beta w_beta 1_{E_{1,beta_1}}(x_1)...1_{E_{n,beta_n}}(x_n)`,  (3.1)

where every `E_{i,beta_i}` is a bounded finite union of intervals of measure one, such that

`|| prod_i f_i - h_eta ||_{L1(R^n)} < eta`.                       (3.2)

#### Proof

Apply Theorem 2.1 to each marginal with errors `eta_i` satisfying `sum_i eta_i<eta`, obtaining probability densities

`g_i=sum_alpha theta_{i,alpha}1_{E_{i,alpha}}`,
`||f_i-g_i||_1<eta_i`.                                           (3.3)

The telescoping tensor-product identity and `||f_i||_1=||g_i||_1=1` give

`||prod_i f_i-prod_i g_i||_1 <=sum_i ||f_i-g_i||_1<eta`.          (3.4)

Expanding `prod_i g_i` gives (3.1), with weights equal to products of the one-dimensional mixture weights. QED.

### Corollary 3.2 — positive-kernel compiler

Let `K:R^n->[0,infinity]` be measurable. Suppose that for every bounded-finite-union unit product indicator,

`int K(x) prod_i 1_{E_i}(x_i) dx <=H`.                            (3.5)

Then for every cap-one product law,

`int K(x) prod_i f_i(x_i) dx <=H`.                               (3.6)

#### Proof

First replace `K` by `K_M=min(K,M)`. For the approximating finite mixture (3.1), linearity and (3.5) give `int K_M h_eta<=H`. Therefore

`int K_M prod f_i <= H+M eta`.

Send `eta->0`, then `M->infinity` and use monotone convergence. QED.

Thus the reduction applies with no constant loss not only to slab indicators but also to singular nonnegative kernels such as fractional Riesz kernels, whenever the geometric product-set estimate is uniform.

### Corollary 3.3 — exact three-way equivalence for the QFORM slab inequality

For fixed real symmetric `A` and a fixed finite constant `C`, the following are equivalent:

1. for every cap-one product law and every interval `J`,
   `P(X^TAX in J)<=C|J|`;
2. for every measurable `E_i subset R`, `|E_i|=1`, and every interval `J`,
   `|{x in prod_i E_i:x^TAx in J}|<=C|J|`;
3. the same inequality as in 2 holds only for **bounded finite unions of intervals** `E_i` of measure one.

`1=>2=>3` is immediate. `3=>1` follows from Theorem 3.1 applied to the slab indicator kernel. Hence a proof on bounded finite-union product sets is exactly sufficient for the original arbitrary-law target; there is no need to first prove a one-interval rearrangement theorem.

The linear interval domination also implies the existence of an absolutely continuous output law with essential density at most `C`: domination extends from intervals to open sets and hence to all Borel sets by outer regularity. This says nothing additional about continuity of a chosen density representative.

## 4. Actual application of the designated fleet02/B13 r24 theorem

We now apply the partner's completed cut-free exterior theorem to an actual inequality, not merely cite it.

Let an interval `J` and a cap-one product law have slab ratio

`rho := P(X^TAX in J)/|J| >0`.                                   (4.1)

For every integer `m>=5`, partner r24 gives the geometric inequality

`|{x in prod E_i:x^TAx in J}|
 <= C_m [D_m^perp(A)]^(-1/(2m)) |J|`                             (4.2)

for every bounded finite-union unit product set. Corollary 3.3 transfers (4.2) to the actual cap-one product law with the same constant. Therefore, if `D_m^perp(A)>0`,

`rho <= C_m [D_m^perp(A)]^(-1/(2m))`,

and hence

`D_m^perp(A) <= (C_m/rho)^(2m)`.                                 (4.3)

If `D_m^perp(A)=0`, (4.3) is trivially true.

Now let `I,L` be any two disjoint physical-coordinate sets and put

`M=A[I,L]`.

Cauchy--Binet gives

`e_m(M^T M)
 =sum_{R subset I,C subset L, |R|=|C|=m} det A[R,C]^2
 <=D_m^perp(A)`.                                                  (4.4)

If `s_1(M)>=s_2(M)>=...` are the singular values, then

`e_m(M^TM)>=prod_{j=1}^m s_j(M)^2>=s_m(M)^(2m)`.                 (4.5)

Combining (4.3)--(4.5) proves the following target-level necessary condition.

### Theorem 4.1 — `QFORM-HIGHRATIO-ALLCUT-SINGULAR-PROFILE-v1`

Every slab witness of ratio `rho` satisfies, simultaneously for every integer `m>=5` and every disjoint original-coordinate cross block,

`boxed:
 s_m(A[I,L]) <= C_m/rho,
 C_m=2 sqrt(2e) m/(m-4).
`                                                                    (4.6)

In particular,

`s_5(A[I,L]) <= 10 sqrt(2e)/rho =23.316439815971.../rho`          (4.7)

for every disjoint physical cut. This is a direct high-ratio-to-low-cross-rank implication with no finite-grid normalization, no selected good cut, and no reciprocal individual minor.

## 5. Optimized global max-volume skeleton

Feed (4.6) into the source-pinned max-volume skeleton (1.5)--(1.6). Let `k>=4` and use the exterior order `m=k+1`. Then every disjoint cross block has

`s_{k+1} <= C_{k+1}/rho
 = 2 sqrt(2e) (k+1)/((k+1)-4) * rho^(-1)
 = 2 sqrt(2e) (k+1)/(k-3) * rho^(-1)`.                           (5.1)

If an invertible disjoint `k x k` cross minor exists, the skeleton gives a `2k`-coordinate physical core and

`A=D+R+E`, `rank R<=4k`,                                         (5.2)

with

`|E_ij| <= (k+1) C_{k+1}/rho
 = 2 sqrt(2e) (k+1)^2/(k-3) * rho^(-1)`                          (5.3)

for every entry; `E` has zero diagonal and vanishes whenever either index belongs to the core. If no such `k x k` minor exists, the exact completion branch gives `E=0` and `rank R<=4(k-1)`.

The continuous function

`F(k)=(k+1)^2/(k-3)`, `k>3`,

has

`F'(k)=(k+1)(k-7)/(k-3)^2`,                                     (5.4)

so the best integer choice in this compiler is exactly `k=7`.

### Theorem 5.1 — `QFORM-HIGHRATIO-GLOBAL-RANK28-MAXNORM-SKELETON-v1`

For every slab witness of ratio `rho>0`, there exist

- a diagonal real matrix `D`,
- a symmetric matrix `R` with `rank R<=28`,
- a symmetric zero-diagonal matrix `E`, and
- a physical core `S0` with `|S0|<=14`,

such that

`A=D+R+E`,                                                        (5.5)

`E_ij=0` whenever `i in S0` or `j in S0`, and

`boxed:
 max_{i,j}|E_ij| <= 32 sqrt(2e)/rho
                  =74.612607411108.../rho.
`                                                                    (5.6)

If no invertible disjoint `7 x 7` physical cross minor exists, one may take `E=0` and in fact `rank R<=24`.

#### Proof

Take `k=7` in (5.1)--(5.3). Here exterior order `m=8` has

`C_8=2sqrt(2e)*8/4=4sqrt(2e)`.                                   (5.7)

The max-volume residual factor is `k+1=8`, hence

`8 C_8=32sqrt(2e)`.                                              (5.8)

All remaining assertions are exactly those of the max-volume skeleton theorem. QED.

This theorem does **not** authorize discarding `E`: a matrix with entrywise `O(1/rho)` coefficients can have large operator norm in high dimension, and the product sets may be arbitrarily translated and fragmented. The value is structural: any hypothetical ratio-divergent sequence is forced, in one global original-coordinate decomposition, toward `diagonal + rank<=28` in max norm outside at most fourteen physical coordinates.

## 6. Quadratic strengthening after a genuine scalar pivot

The partner's scalar-bordered theorem (1.4) gives a stronger profile after one original-coordinate square is completed.

Fix `k` with `a=A_kk!=0` and let `S` be the full scalar Schur complement (1.2). For every `m>=5`, if the bordered energy is nonzero, the actual slab ratio obeys

`rho <= T_m ( |a|^(2(m-1)) B_{m+1,k}^perp(A) )^(-1/(4m))`.       (6.1)

Using the exact identity `B_{m+1,k}^perp=a^2D_m^perp(S)`, rearrangement gives

`D_m^perp(S)
 <= (T_m/rho)^(4m) |a|^(-2m)`.                                  (6.2)

If the bordered energy is zero, (6.2) again holds trivially. Repeating (4.4)--(4.5), now inside the Schur matrix, yields for every disjoint physical block of `S`

`boxed:
 s_m(S[I,L]) <= T_m^2/(|a| rho^2)
 = [16 sqrt(2e) m/(m-4)]/(|a| rho^2).
`                                                                    (6.3)

This is a genuine **quadratic-in-ratio** collapse after a nonzero scalar pivot.

Apply the max-volume skeleton to `S` with `k=m-1`. The entrywise residual coefficient is

`m T_m^2
 =16 sqrt(2e) m^2/(m-4)`.                                    (6.4)

The real function `m^2/(m-4)` for `m>4` is minimized at `m=8`. Therefore:

### Theorem 6.1 — `QFORM-HIGHRATIO-SCALAR-SCHUR-RANK28-SKELETON-v1`

For every original coordinate `k` with `a=A_kk!=0`, the scalar Schur complement `S` admits

`S=D'+R'+E'`, `rank R'<=28`,                                     (6.5)

with a core of at most fourteen residual physical coordinates, `E'` symmetric and zero-diagonal, `E'` vanishing on the core rows and columns, and

`boxed:
 max_{i,j}|E'_ij|
 <= 256 sqrt(2e)/( |a| rho^2 )
 =596.900859288864.../( |a| rho^2 ).
`                                                                    (6.6)

If `S` has no invertible disjoint `7 x 7` cross minor, one may take `E'=0` and `rank R'<=24`.

This is stronger than Theorem 5.1 whenever the scalar pivot is not too small compared with the witness ratio. It remains product-safe because only the original scalar coordinate is Schur-completed; no random variable is rotated.

## 7. Consequence for a hypothetical counterexample sequence

By Theorem 3.1 and Corollary 3.3, failure of full QFORM may be witnessed, with arbitrarily small loss in any chosen slab ratio, by **bounded finite-union unit product indicators**. Thus if the universal constant fails, there is a sequence

`(A_n, prod_i 1_{E_{i,n}}, J_n)`

with each `E_{i,n}` a bounded finite union of intervals of measure one and slab ratios `rho_n->infinity`.

For that sequence, Theorem 5.1 gives exact decompositions

`A_n=D_n+R_n+E_n`, `rank R_n<=28`,                                (7.1)

with cores of size at most fourteen and

`||E_n||_max <=32sqrt(2e)/rho_n ->0`.                             (7.2)

Moreover, after every nonzero scalar pivot `a_{k,n}`, Theorem 6.1 gives an exact Schur decomposition whose residual max-norm error is

`O( (|a_{k,n}| rho_n^2)^(-1) )`.                                 (7.3)

Therefore any genuine counterexample sequence must live asymptotically in a very narrow class: `diagonal + uniformly bounded rank + max-norm-small zero-diagonal remainder`, with only a bounded physical core exempted from the small remainder. This conclusion is global across all physical cuts and follows from the actual slab ratio; it is not a random-cut or finite-grid artifact.

The remaining obstruction is that max-norm smallness is not a support-uniform perturbation norm for arbitrary product indicators. One cannot delete `E_n` by continuity: remote fragmented sets can turn a tiny quadratic coefficient into order-one phase or slab displacement. The next proof step must absorb `E_n` before reciprocal-coefficient payment or extract from it a paid grouped-bank/exterior-volume packet.

## 8. First unpaid implication

`QFORM-DIAG-RANK28-MAXNORM-RESIDUAL-CLOSURE-v1`:

> Prove a dimension-free linear slab bound for the high-ratio normal form `A=D+R+E` supplied by Theorem 5.1, where `D` is diagonal, `rank R<=28`, `E` is zero-diagonal, vanishes on the rows/columns of a physical core of size at most fourteen, and `||E||_max=O(1/rho)` along a putative bad sequence; or prove that the three-large-eigenvalue hypothesis forces an already-paid square/pair/grouped-bank/exterior mechanism before this residual can remain unpaid. In the nonzero-scalar-pivot branch, exploit the stronger `O((|a|rho^2)^(-1))` Schur residual from Theorem 6.1.

A valid closure must preserve arbitrary law, dimension, indefinite sign, translation, and fragmentation. Raw operator-norm perturbation, bounded-diameter localization, or a fixed fragment count is not available.

## 9. Arithmetic and integrity check

The constants used above are direct exact evaluations:

`C_5=10 sqrt(2e)=23.316439815971...`,
`C_8=4 sqrt(2e)=9.326575926388...`,
`8 C_8=32 sqrt(2e)=74.612607411108...`,
`8 T_8^2=256 sqrt(2e)=596.900859288864...`.

For the max-volume compiler, the coefficient function `(k+1)^2/(k-3)` is minimized at `k=7`; for the scalar-Schur compiler, `m^2/(m-4)` is minimized at `m=8`. These are exact one-variable derivative calculations, not numerical optimizations.

No public release, scheduler mutation, email/push, paid call, remote workflow, cross-account authentication, or permission expansion is used. Full QFORM remains OPEN and the new theorems have not received independent end-to-end review.
