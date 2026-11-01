# fleet01/B08 — diffuse curvature budget and grouped zero-self cross-bank smoothing

**Run:** `20260922T184021Z-fleet01-B08-qform-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control:** revision `2026-09-22.11`  
**Assignment:** diffuse eigenvector case  
**Outcome:** `PROVED_SUPPORTING_THEOREMS / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction discipline

The target remains the unrestricted conjecture: if the coordinates of `X` are independent and have probability densities bounded by one, and a real symmetric `A` has at least three eigenvalues of absolute value at least one, prove that `X^T A X` has a density with one universal dimension-free `L^infinity` bound, or produce a genuine counterexample. Continuity is tracked separately.

This report does not use the refuted arbitrary-joint rank-three coarea bound, the refuted positive conditional projection-density moment, the refuted worst scalar-`Q_rest` conditional supremum, any post-rotation independence, any law-uniform pointwise quadratic-phase decay, or any one-minor reciprocal payment. In particular, the preceding fleet01/B08 run constructed an exact target-valid example for which `ess sup_b ||p_(Q3|Q'=b)||_infinity=infinity` although the full output density is bounded. The present mechanism stays in the original physical product coordinates.

Two complementary statements are proved below. The first is an exact **curvature conservation identity** for a delocalized selected three-eigenvector frame across a physical cut. The second is a **group-before-inversion density theorem** for a zero-self physical bank; it converts many cross directions directly into a continuous density bound without selecting a single small minor.

## 2. Exact selected-frame block identity

Let `R in R^(n x 3)` have orthonormal columns and let

`A R = R Lambda`,

where `Lambda` is real diagonal (more generally symmetric) and

`s_min(Lambda)>=1`.

Split the original physical coordinates into `I disjoint_union J`. Put

`G=R_I^T R_I`, `H=R_J^T R_J=I_3-G`.

Assume `G,H` are positive definite. Define the whitened physical selected frames

`W_I=R_I G^(-1/2)`, `W_J=R_J H^(-1/2)`,

so `W_I^T W_I=W_J^T W_J=I_3`, and define

`S=W_I^T A_II W_I`,
`T=W_I^T A_IJ W_J`,
`V=W_J^T A_JJ W_J`.

Restricting `A R=R Lambda` to the two coordinate blocks and multiplying by the whitened frames gives the exact identities

`S G^(1/2)+T H^(1/2)=G^(1/2)Lambda`,                    (2.1)

`T^T G^(1/2)+V H^(1/2)=H^(1/2)Lambda`.                  (2.2)

Equivalently,

`S=G^(1/2)Lambda G^(-1/2)-T H^(1/2)G^(-1/2)`,          (2.3)

`V=H^(1/2)Lambda H^(-1/2)-T^T G^(1/2)H^(-1/2)`.        (2.4)

No assumption on the complementary spectrum of `A` occurs here. In particular, an arbitrary residual operator annihilating the selected spectral space is already included.

### Exact half-cut

If `G=H=I_3/2`, then

`boxed(S+T=Lambda,  V+T^T=Lambda.)`                       (2.5)

Since `S,V,Lambda` are symmetric, (2.5) forces `T=T^T` and hence

`boxed(S=V=Lambda-T.)`                                    (2.6)

Thus on an exact physical half-cut the selected spectral curvature is literally divided between the normalized cross block and the two normalized self blocks.

A useful exact model is

`R=2^(-1/2)[I_3;I_3]`,

`C=(1/2)[D,-D;-D,D]`,

`A=R Lambda R^T+C`,

with arbitrary symmetric `D`. Then `C R=0`, `G=H=I/2`,

`S=(Lambda+D)/2`, `T=(Lambda-D)/2`, `V=S`,

so (2.5)-(2.6) hold identically even with an arbitrary complementary residual.

## 3. Quantitative cross-versus-self curvature budget

Assume for some `0<a<=1/2` that

`a I_3 <= G,H <= (1-a)I_3`.                                (3.1)

Set

`c_a=sqrt(a/(1-a))`, `C_a=sqrt((1-a)/a)`.

Then

`s_min(G^(1/2)Lambda G^(-1/2))>=c_a`,

and

`||H^(1/2)G^(-1/2)||<=C_a`.                                (3.2)

Fix a threshold `tau>0` and let

`r_tau(T)=#{j:s_j(T)>tau}`.

Write `T=T_hi+T_lo` by singular-value truncation, where

`rank(T_hi)<=r_tau(T)`, `||T_lo||<=tau`.

Let

`d_a(tau)=c_a-tau C_a`.                                    (3.3)

Whenever `d_a(tau)>0`, the kernel of

`T_hi H^(1/2)G^(-1/2)`

has dimension at least `3-r_tau(T)`. On that kernel, (2.3) and (3.2) give

`||S v|| >= d_a(tau)||v||`.                                (3.4)

By the min-max characterization of singular values, `S` has at least

`3-r_tau(T)`

singular values at least `d_a(tau)`. Since `S` is symmetric, these are absolute eigenvalue bounds. Compression interlacing, separately for the positive and negative eigenvalues, then gives:

### Theorem 3.1 — `QFORM-DIFFUSE-CROSS-SELF-CURVATURE-BUDGET-v1`

Under (3.1), both physical principal blocks `A_II` and `A_JJ` have at least

`boxed(3-r_tau(T))`

eigenvalues of absolute value at least

`boxed(d_a(tau)=sqrt(a/(1-a))-tau sqrt((1-a)/a).)`          (3.5)

At the same time, if `r_tau(T)=r`, then the true physical cross block `A_IJ` has at least `r` singular values greater than `tau`, because `T=W_I^T A_IJ W_J` is an orthogonal compression.

This is a deterministic conservation law: strong selected curvature cannot disappear simultaneously from both the cross block and the two self blocks.

## 4. Concrete diffuse corollary from the completed floating paving

The earlier fleet01/B08 theorem `QFORM-FINITE-RANK-FLOATING-PAVING-v1` proves that for a three-column orthonormal frame `R` with row leverage

`delta=max_i ||r_i||^2`,

there is an original-coordinate partition with

`||R_I^T R_I-I_3/2||op <= sqrt(3/2) delta`.                 (4.1)

Therefore, if

`boxed(delta <= 1/(6 sqrt(3/2)) = 0.1360827634...)`,       (4.2)

one can choose a cut with

`I_3/3 <= G,H <= 2I_3/3`.                                  (4.3)

Use Theorem 3.1 with `a=1/3` and `tau=1/8`. Then

`d_(1/3)(1/8)=1/sqrt(2)-sqrt(2)/8=3/(4sqrt(2))`.           (4.4)

Consequently every selected-three-frame satisfying (4.2) admits a physical cut for which exactly one of the following integer alternatives holds:

- `r=0`: each of `A_II,A_JJ` has at least three eigenvalues of modulus at least `3/(4sqrt(2))`;
- `r=1`: each has at least two such eigenvalues;
- `r=2`: each has at least one such eigenvalue;
- `r=3`: the normalized selected cross compression `T` has all three singular values greater than `1/8`, and hence the true physical cross block has at least three singular values greater than `1/8`.

This does **not** by itself solve QFORM: arbitrary residual self curvature and the affine terms produced by conditioning still have to be paid product-preservingly. It does, however, replace an unstructured 'remainder may be anywhere' statement by an exact finite curvature budget.

## 5. Group-before-inversion theorem for a zero-self physical bank

The second result is independent of the selected-frame algebra and directly addresses the live instruction to aggregate coordinate banks before paying reciprocal minors.

Let `I,J` be disjoint original-coordinate groups. Write `X=X_I`, `Y=X_J`; their coordinates remain mutually independent and have density caps one. Consider

`Q = R(Y)+2 X^T M Y + b_I^T X + b_J^T Y`,                    (5.1)

where `R(Y)` is an arbitrary measurable quadratic/affine expression in `Y`, and

`M in R^(p x q)`

has rank at least `k>=2`. This is exactly the quadratic-form situation in which the physical self block on `I` is zero; all outside self curvature and all cross coupling are retained.

Let `s_1(M)>=...>=s_k(M)>0` be any first `k` singular values. Let `C_lin` be a universal constant in the standard Rudelson--Vershynin bounded-density projection theorem already source-transferred in the QFORM archive: every `d`-dimensional orthogonal projection of a vector with independent cap-one coordinates has density at most `C_lin^d`.

### Lemma 5.1 — capped-density inverse-radius integral

If a probability density `g` on `R^k` satisfies `g<=L` and `k>=2`, then uniformly in every translation `z_0`,

`int g(z)/||z-z_0|| dz
 <= [k/(k-1)] omega_k^(1/k) L^(1/k)`,                         (5.2)

where `omega_k` is the volume of the Euclidean unit ball in `R^k`.

Proof. By layer cake,

`E ||Z-z_0||^(-1)
 =int_0^infinity P(||Z-z_0||<1/t) dt`.

The probability is at most `min(1,L omega_k t^(-k))`. Splitting at `t=(L omega_k)^(1/k)` gives (5.2). Equivalently, the extremal cap-only majorant fills a centered ball. QED.

### Theorem 5.2 — `QFORM-ZERO-SELF-GROUPED-CROSSBANK-v1`

For (5.1), `Q` has a **continuous density vanishing at infinity**, and

`boxed(
 ||p_Q||_infinity
 <= (C_lin^2/2) [k/(k-1)] omega_k^(1/k)
    (prod_(j=1)^k s_j(M))^(-1/k).
 )`                                                          (5.3)

The estimate is dimension-free and assumes no moments, support regularity, log-concavity, or sign condition.

#### Proof

Condition on `Y=y` and put

`c(y)=M y+b_I/2`.

Then

`Q|Y=y = R_b(y)+2 c(y)^T X`,                                 (5.4)

where `R_b` absorbs the terms depending only on `y`. For `c!=0`, the one-dimensional projection theorem and scaling give the conditional density bound

`||p_(Q|Y=y)||_infinity <= C_lin/[2||c(y)||]`.               (5.5)

Take an SVD `M=U Sigma V^T` and project `c(Y)` onto the first `k` left singular directions. Its law is a translation of

`diag(s_1,...,s_k) V_k^T Y`.

The `k`-dimensional projection theorem therefore gives density cap

`L <= C_lin^k/(prod_(j=1)^k s_j)`.                            (5.6)

Since `||c||` dominates the norm of this `k`-dimensional projection, Lemma 5.1 yields

`E ||c(Y)||^(-1)
 <= [k/(k-1)] omega_k^(1/k) C_lin
    (prod_(j=1)^k s_j)^(-1/k).`                              (5.7)

Integrating (5.5) proves (5.3).

For continuity, the random vector `c(Y)` has an absolutely continuous component on an affine subspace of dimension at least two. Hence, outside a null set of `y`, at least two physical coefficients of `c(y)` are nonzero. For such `y`, the conditional density in (5.4) is a convolution containing at least two scaled input densities. Each scaled input density belongs to `L^1 intersect L^infinity`, hence to `L^2`; the convolution of two `L^2` functions is continuous and vanishes at infinity, and convolution with the remaining probability densities preserves `C_0`. The majorant in (5.5) is integrable by (5.7). Dominated convergence therefore proves that the mixture density `p_Q` itself is continuous and belongs to `C_0(R)`. QED.

### Two-row form: exact aggregate-minor payment

If `p=2` and `rank M=2`, take `k=2`. Cauchy--Binet gives

`(s_1 s_2)^2=det(MM^T)=sum_(r<s) det(M[:,{r,s}])^2`.         (5.8)

Thus

`boxed(
 ||p_Q||_infinity
 <= C_lin^2 sqrt(pi)
    [sum_(r<s) det(M[:,{r,s}])^2]^(-1/4).
 )`                                                          (5.9)

Equation (5.9) is the desired **aggregate-before-inversion** feature: all column-pair Pluecker mass is summed first, and only then is a fourth root paid. No single reciprocal minor is selected.

This exactly matches the currency generated in the newest fleet03/B08 near-coloop analysis whenever the corresponding two physical rows can be placed in a zero-self/grouped-linear branch. The remaining difficulty is structural: the general near-coloop branch can carry an arbitrary two-row self block, so (5.9) cannot yet be applied universally.

## 6. Named fleet02/B08 partner result applied to an actual diffuse branch

The assigned partner result actually used here is fleet02/B08 `QFORM-SCALAR-ORTHOGONAL-CROSSBLOCK-v1`, canonical source

`yspennstate/math-open-problems@caf8de3c65ae54b8ec8df9bfe977a76bf0a6ab99`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T173452Z-r15/REPORT.md`.

It states that an original-coordinate square cross block satisfying

`B B^T=sigma^2 I_m`, `m>4`,

pays the full form, including arbitrary self blocks and outside couplings, with a continuous `C_0` density and

`||p_Q||_infinity <= [e sqrt(2)/(4 sigma)] m/(m-4)`.         (6.1)

Apply it to the genuine target matrix

`A_*=[[0,I_16],[I_16,0]]`.                                  (6.2)

All 32 eigenvalues have modulus one. Choose three `+1` eigenvectors

`r_j=2^(-1/2)(v_j,v_j)`,

where `v_1,v_2,v_3` are three normalized Sylvester-Hadamard columns in `R^16`. Every physical row leverage of this selected frame is

`delta=3/32<1/(6sqrt(3/2))`,                                (6.3)

and the natural `16|16` physical cut is exact-half: `G=H=I_3/2`, with normalized selected cross compression `T=I_3`. Hence it lies in the `r=3` cross branch of Theorem 3.1.

For the full physical cross block, `B=I_16`, so the partner theorem applies with `sigma=1,m=16` and gives the actual inequality

`boxed(||p_(X^T A_* X)||_infinity <= e sqrt(2)/3
       =1.2814103427... .)`                                  (6.4)

The density is continuous and vanishes at infinity. This is a concrete use of the completed partner theorem, not a citation-only dependency. It also illustrates the intended division of labor: the new curvature budget identifies a strong cross branch, while the partner theorem pays an important globally spread realization of that branch.

## 7. Relation to the newest near-coloop currency

The fresh fleet03/B08 result `QFORM-99PCT-NEAR-COLOOP-PAIR-CURRENCY-v1`, canonical

`yspennstate/math-open-problems@04fb94f2b622e0423272e1aefa1aaf0af59f305f`,

proves that its unpaid fine-scale branch carries

`sum_(k!=j) sum_(r<s) det H[{j,k},{r,s}]^2
 > (4191/281804800) gamma^4`,                                (7.1)

and that this currency is invariant under a second scalar Schur shear through row `j`.

Theorem 5.2 supplies a rigorous endpoint for a substantial subbranch of (7.1): once a two-row or grouped physical bank has zero self block, its complete cross-minor aggregate can be consumed directly through (5.9), without a reciprocal-minor selection. The general case still has to convert the near-coloop/two-row self block either into (i) an invertible physical pair paid by the completed pair-log theorem, (ii) a rank-two affine half-Riesz payment, or (iii) a grouped zero-self bank of the type treated here.

## 8. What remains unpaid

The full conjecture is **not proved or disproved**. The new first B08 implication is:

`QFORM-DIFFUSE-CURVATURE-BUDGET-CLOSURE-v1`.

Starting from the partition supplied by the selected-frame floating paving and the alternatives in Section 4, prove a dimension-free product-preserving payment in every branch:

1. if `r=3`, convert the strong normalized three-direction cross compression into either a ridge certificate or a grouped cross-bank theorem without imposing a scalar-orthogonal hypothesis;
2. if `r=1,2`, combine the simultaneously retained self curvature in both disjoint physical blocks with the surviving cross directions, allowing arbitrary complementary spectrum;
3. if the cross structure collapses into the near-coloop/two-row branch, use the aggregate currency before inversion and remove the remaining arbitrary two-row self block;
4. pay the zero/near-zero first physical pivot branch without introducing a worst conditional-fiber supremum.

The exact identities (2.1)-(2.4) and the grouped theorem (5.3) sharply localize the debt: selected spectral curvature is conserved across the cut, and a zero-self grouped bank is no longer an obstruction. The hard part is the arbitrary self-block coupling between those two mechanisms.

## 9. Finite diagnostic

`VERIFY.py` and `VERIFY_OUTPUT.txt` in this immutable directory check only the algebra/constants: the exact half-cut identity, an exact `r=1` curvature-budget witness, the two-row Cauchy--Binet aggregate, the diffuse threshold `3/32<1/(6sqrt(3/2))`, and the partner bound `e sqrt(2)/3`. The output ends `QFORM_B08_R17_CHECK_PASS`. These finite checks are not universal proof certificates.
