# fleet03/B08 — block-remainder diffuse extension and rank-three definite closure

**Run:** `20260922T122924Z-fleet03-B08-qform-diffuse-v2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** fleet03/B08, `Diffuse eigenvector case`  
**Classification:** `TARGET_SUPPORTING_THEOREMS`; **full conjecture OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Exact target and source state

The target remains: for every dimension `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal finite bound for the density of `Q=X^T A X`, or produce a valid counterexample. No moment, support, log-concavity, centering, identical-law, or eigenbasis-independence assumption is introduced below.

This report consumes the live correction inbox. In particular it does **not** use the refuted law-uniform pointwise one-dimensional Fresnel decay, does not rotate the product input and then assume independence, and does not replace a curved fiber by an unrestricted fiber supremum.

The previous B08 theorem, source

`yspennstate/math-open-problems@9dcddd0bf3fbcb8e0b3396e0a4d883924d3f4ada`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T114830Z-fleet03-B08-qform-diffuse-v1/REPORT.md`

proved a dimension-free Fourier–Brascamp–Lieb estimate for a rank-`r` spectral frame `R` whenever every row leverage is at most `1/2`. It also isolated the first debt: an arbitrary off-diagonal spectral remainder destroys the coordinatewise factorization used by that argument.

Two completed peer results are applied here.

1. **Cross-block Fourier theorem**, interactive canonical source
   `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`:
   if an original-coordinate cut `I|J` has cross block of rank `r>2` and product `Delta` of nonzero singular values, then
   `||p_Q||_infinity <= (2r/(r-2)) Delta^(-1/r)`, with arbitrary within-side quadratic terms retained.
2. **Dependent square smoothing**, fleet04/B18 canonical source
   `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`:
   if `R0` has density at most `M` and, conditional on `R0=r`, `V` has density at most one, then
   `R0+aV^2` has density at most `2 sqrt(M/|a|)`.

The named assignment partner `fleet04/B08` had no completed current-QFORM handoff at both the initial and final source checks used for this derivation, so no theorem is attributed to that worker.

## 1. New theorem: diffuse selected spectrum with a block-diagonal off-diagonal remainder

The previous B08 Fourier theorem allowed only coordinatewise remainder phases. The next theorem allows genuinely off-diagonal interactions inside physical coordinate blocks.

### Theorem 1 — `QFORM-DIFFUSE-BLOCK-REMAINDER-v1`

Let

`A = R Lambda R^T + C`,

where `R` is an `n x r` real matrix with orthonormal columns, `r>2`, and `Lambda` is real symmetric and invertible. Partition the **original independent coordinates** into disjoint nonempty blocks

`G_1 union ... union G_m = {1,...,n}`

such that `C` is block diagonal for this partition:

`C[G_k,G_l]=0` whenever `k != l`.

Put

`M_k = R_{G_k}^T R_{G_k}`

and assume

`mu := max_k ||M_k||_op < 1/r`.

Then for every admissible independent product input law, `Q=X^TAX` has a bounded continuous density and

`||p_Q||_infinity
 <= [4r / ((r-2)(1-sqrt(r mu)))] |det Lambda|^(-1/r).`

No condition is imposed on the signs, sizes, or internal off-diagonal entries of the blocks of `C`.

### Proof

Because `R^T R=I_r`,

`sum_k M_k = I_r`,

and each `M_k` is positive semidefinite. Color the blocks independently with Bernoulli variables `epsilon_k in {0,1}` of mean `1/2`, and set

`D = sum_k (epsilon_k-1/2) M_k`.

Using independence and centering,

`E ||D||_F^2
 = (1/4) sum_k ||M_k||_F^2`.

For a positive semidefinite matrix,

`||M_k||_F^2 = tr(M_k^2)
 <= ||M_k||_op tr(M_k)
 <= mu tr(M_k)`.

Therefore

`E ||D||_F^2
 <= (mu/4) sum_k tr(M_k)
 = r mu/4`.

Hence at least one deterministic coloring satisfies

`||D||_op <= ||D||_F <= sqrt(r mu)/2`.

Let `I` be the union of blocks colored one and `J=I^c`. Their selected-frame Gram matrices are

`Sigma_I = R_I^T R_I = I_r/2 + D`,
`Sigma_J = R_J^T R_J = I_r/2 - D`.

Thus both obey

`Sigma_I, Sigma_J >= alpha I_r`,

where

`alpha = (1-sqrt(r mu))/2 > 0`.

Because `I` and `J` are unions of whole `C`-blocks,

`C[I,J]=0`.

Consequently the **actual cross block of the full matrix** is

`A[I,J] = R_I Lambda R_J^T`.

Factor

`R_I = P Sigma_I^(1/2)`,
`R_J = Q Sigma_J^(1/2)`,

with `P,Q` isometries. Hence the nonzero singular values of `A[I,J]` are those of

`Sigma_I^(1/2) Lambda Sigma_J^(1/2)`,

and their product is exactly

`Delta
 = |det Lambda| sqrt(det Sigma_I det Sigma_J)
 >= |det Lambda| alpha^r`.

Apply the completed cross-block Fourier theorem to the original-coordinate cut `I|J`. It allows all within-`I` and within-`J` quadratic terms, including the full blocks of `C`. Therefore

`||p_Q||_infinity
 <= (2r/(r-2)) Delta^(-1/r)
 <= (2r/(r-2)) |det Lambda|^(-1/r) alpha^(-1)`

which is exactly

`[4r / ((r-2)(1-sqrt(r mu)))] |det Lambda|^(-1/r).`

The peer theorem also gives continuity. QED.

### Target-level interpretation

If `R` consists of any chosen `r>=3` large eigenvectors of the target matrix and `C` is the remaining spectral part, then `C R=0` automatically. The theorem requires only the additional **physical-coordinate component structure** above. Thus it is a genuine extension beyond the previous diagonal/coordinatewise remainder: each remainder component may contain arbitrary dense off-diagonal couplings.

For `r=3`, `|det Lambda|>=1`, and block spectral mass `mu<1/3`,

`||p_Q||_infinity <= 12/(1-sqrt(3 mu)).`

The full arbitrary remainder can have one giant physical component and is not covered.

## 2. New localized complement: every rank-three definite form is uniformly bounded

The next result closes the complete rank-exactly-three **definite** branch, including highly localized eigenvectors. It combines the previous B08 diffuse theorem with fleet04/B18's dependent square-smoothing lemma.

### Theorem 2 — `QFORM-RANK3-DEFINITE-ALL-LEVERAGE-v1`

Let

`A=R Lambda R^T`

have rank exactly three, where `R` is `n x 3` with orthonormal columns and either

`Lambda >= I_3`

or

`Lambda <= -I_3`.

For arbitrary independent inputs with densities bounded by one, `Q=X^TAX` has an essentially bounded density satisfying

`||p_Q||_infinity <= 3e.`

No localization, support, or moment assumption is needed.

### Proof

Reflect `Q` if necessary, so take `Lambda>=I_3`. Write the rows of `R` as `v_i^T` and their leverages as

`c_i=||v_i||^2`.

#### Case 1: all `c_i<=1/2`

The previous B08 theorem `QFORM-DIFFUSE-SPECTRAL-FRAME-v1` applies with `r=3`, `V_i=0`, and `|det Lambda|>=1`, giving

`||p_Q||_infinity <= 3e`.

#### Case 2: some `c_i>1/2`

Fix such an index and abbreviate

`v=v_i`, `c=||v||^2`,
`z=R_{-i}^T X_{-i}`,
`a=v^T Lambda v`.

Since `Lambda>=I`,

`a>=c>1/2`.

Expand and complete the square only in the original independent coordinate `X_i`:

`Q
 = (v X_i+z)^T Lambda (v X_i+z)
 = a (X_i + a^(-1) v^T Lambda z)^2 + z^T S z`,

where

`S = Lambda - Lambda v v^T Lambda/a`.

The matrix `S` is positive semidefinite of rank two and `S v=0`. Let `P` be a `3 x 2` matrix whose columns are an orthonormal basis for `v^perp`, and put

`Y=P^T z`, `B=P^T S P`.

Then `B` is positive definite and

`z^T S z = Y^T B Y`.

Crucially, the two columns of the physical projection matrix `R_{-i}P` remain orthonormal:

`(R_{-i}P)^T(R_{-i}P)
 = P^T(I-vv^T)P
 = I_2`.

Thus `Y` is a genuine two-dimensional orthogonal projection of the product law of the remaining original independent coordinates. The product-marginal theorem used in the completed cross-block peer proof gives

`||p_Y||_infinity <= 2`.

It follows directly from ellipse shell volume that the positive quadratic pushforward

`R0=Y^T B Y`

has density bounded by

`M <= 2 pi / sqrt(det B)`.

Indeed, under `u=B^(1/2)y`, the area of

`{s <= |u|^2 <= s+h}`

is at most `pi h`, and the Jacobian is `1/sqrt(det B)`.

Now compute `det B`. Let `e_1=v/sqrt(c)` and complete it by the columns of `P` to an orthogonal basis of `R^3`. In that basis, `B` is the Schur complement of the scalar entry

`e_1^T Lambda e_1 = a/c`.

Therefore

`det Lambda = (a/c) det B`,

or

`det B = c det Lambda/a`.

Hence

`M <= 2 pi sqrt(a/(c det Lambda)).`

Set

`V=X_i+a^(-1)v^T Lambda z`.

Conditional on `R0=r`, the law of `V` is a mixture of translations of the law of `X_i`, because `X_i` is independent of all remaining coordinates. Consequently its conditional density is still bounded by one. The fleet04/B18 dependent square-smoothing lemma now applies to

`Q=R0+aV^2`:

`||p_Q||_infinity
 <= 2 sqrt(M/a)
 <= 2 sqrt(2 pi) (a c det Lambda)^(-1/4).`

Using `a>=c`, `det Lambda>=1`, and `c>1/2`,

`||p_Q||_infinity
 < 4 sqrt(pi)
 < 3e.`

This proves the heavy-leverage case and therefore the theorem. QED.

### What is new here

The previous diffuse theorem stopped exactly at leverage `1/2`; the present argument covers the entire complementary localized region for definite rank three. It never rotates the input into independent eigen-coordinates. The orthogonal projection `Y` is used only through a valid marginal-density bound, and the original physical coordinate `X_i` supplies the final square smoothing.

Continuity is established by the Fourier argument in the diffuse subcase. The localized argument above proves the required essentially bounded density; no stronger continuity claim is made here.

## 3. Quantitative indefinite corollary and the narrowed residual

The same calculation has a useful indefinite form. Suppose rank three has inertia `(2,1)` or `(1,2)`, choose a physical row `v` with scalar pivot

`a=v^T Lambda v !=0`,

and suppose `a` has the **minority sign**. Sylvester inertia additivity then makes the rank-two Schur complement `B` definite. Repeating the preceding proof gives

`||p_Q||_infinity
 <= 2 sqrt(2 pi) (|a| c |det Lambda|)^(-1/4).`

This is target-relevant but is not by itself universal because an indefinite Rayleigh quotient `|a|` may be arbitrarily small by cancellation even when all three spectral magnitudes are at least one.

Thus, after combining the old and new B08 mechanisms, the pure rank-three obstruction is sharply concentrated in the **localized indefinite near-isotropic/majority-pivot branch**: leverage exceeds `1/2`, while available physical pivots can be majority-sign or have very small quadratic coefficient. This agrees with the current fleet04/B19 synthesis, which independently identifies the localized indefinite majority-pivot/near-isotropic residue as the first pure-rank-three debt.

## 4. Why these results do not prove the full conjecture

Two distinct debts remain.

1. For a general target matrix, the spectral remainder after selecting three large eigenvectors need not be block diagonal in small physical components. Theorem 1 therefore does not yet control an arbitrary dense `C`.
2. Even with rank exactly three, indefinite forms can have a localized direction close to the null cone of `Lambda`; Theorem 2's definite inequality `a>=c` then disappears. A new mixed bilinear/elliptic-trace payment is required.

No negative result here refutes the owner target. The full conjecture remains OPEN.

## 5. Next concrete mechanism

The next B08 step should attack `QFORM-LOCALIZED-INDEFINITE-NEAR-NULL-v1`: for a heavy row `v` with `c>1/2` and small `|v^T Lambda v|`, exploit the necessarily large orthogonal coupling `P^T Lambda v` together with the original-coordinate product structure. A successful estimate should interpolate between square smoothing when `|a|` is large and a bilinear/cross-block estimate when `|a|` is small. In parallel, Theorem 1 suggests grouping a sparse spectral remainder by its physical interaction components rather than treating all off-diagonal terms as one monolithic phase.

## 6. Status summary

**Proved in this run:**

- `QFORM-DIFFUSE-BLOCK-REMAINDER-v1`, a continuous-density bound for selected diffuse spectrum plus arbitrary off-diagonal remainder inside small physical components;
- `QFORM-RANK3-DEFINITE-ALL-LEVERAGE-v1`, a universal `3e` essential-density bound for **every** rank-exactly-three definite target form;
- the quantitative minority-sign pivot bound above.

**Applied completed peer mathematics:** cross-block Fourier smoothing and fleet04/B18 dependent square smoothing.

**Not proved:** arbitrary dense spectral remainder; localized indefinite near-null branch; the full universal conjecture.
