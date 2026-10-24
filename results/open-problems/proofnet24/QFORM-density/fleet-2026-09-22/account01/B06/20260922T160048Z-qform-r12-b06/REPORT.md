# account01/B06 — anisotropic three-coordinate curved coarea and the determinant-averaging wall

**Run:** `20260922T160048Z-qform-r12-b06`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / LOCAL_POSTHOC_AGGREGATION_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact target, source pins, and mechanism change

The full target remains: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite constant, or give a valid counterexample. Continuity is a separate desired conclusion.

Fresh control was read from `yspennstate/math-research-brain` main, initially at `4d9d79dd39e1d60c472a38221f1bb79e57d49e67` and refreshed before publication at `826a575b8bc348d611335689eea11e169b0ad0ce`; revision remained `2026-09-22.5`. The live correction inbox was refreshed and all currently listed counterexamples were respected, in particular `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, and `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`.

The named partner result actually used is account02/B06 run `b06-20260922T113045Z-d47192d10a82`, canonical report `yspennstate/math-open-problems@6902eb62f21a7c833ca27dcca69f34d50e711a7d:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`, blob `9cced3d58d10574ef548c119c8d5a67276dc870f`. Its proved determinant-mass identities are used explicitly in Section 5 below.

The preceding B06 route isolated the correlated spectral-addition problem after proving a universal `pi e` bound for the pure same-sign rank-two spectral component. This run deliberately changes mechanism: instead of another spectral-marginal or X-ray attempt, it performs direct original-coordinate coarea on a three-variable physical block, keeping arbitrary outside couplings.

## 1. Compact conditional end-to-end argument

Condition on all original coordinates except a physical triple `I={i1,i2,i3}`. The conditional polynomial is

`q_w(x)=x^T M x + 2 b(w)^T x + c(w)`,  with  `M=A[I,I]`.

If one can find a triple for which the explicit anisotropic curvature cost `K(M)` defined below is universally bounded, then the full conditional law has a density bounded by a universal constant, uniformly in the outside variables, and averaging closes the full `Q` density bound.

The first essential issue is therefore not the outside coupling: it disappears into a translation after conditioning. The issue is whether the three-large-eigenvalue hypothesis forces enough *aggregate* physical curvature. The theorem below gives the exact local curved-fiber payment. Section 6 then shows, using the partner determinant-mass construction, that simply averaging this already-sharp local payment over Pluecker-weighted triples still loses linearly with dimension in the delocalized Hadamard family. Thus the next step must aggregate product structure **before** the local reciprocal-curvature bound is taken.

## 2. A two-dimensional anisotropic reciprocal-distance lemma

### Lemma 2.1 — `QFORM-ANISOTROPIC-1OVER-R-v1`

Let `C:R^2 -> R^m` be injective and let

`d(C)=sqrt(det(C^T C))>0`

be its two-dimensional area Jacobian. If `g_1,g_2` are probability densities on `R` satisfying `0<=g_j<=1`, then

`int_{R^2} g_1(u_1) g_2(u_2) / |C u| du <= 2 sqrt(2 pi) d(C)^(-1/2)`.    (2.1)

### Proof

For any `R>0`, split into `|Cu|<=R` and `|Cu|>R`. On the near region, drop the factors `g_1 g_2<=1` and use the area formula on the two-plane `C(R^2)`:

`int_{|Cu|<=R} du/|Cu| = d(C)^(-1) int_{|v|<=R, v in C(R^2)} dv/|v| = 2 pi R/d(C)`.

On the far region, `1/|Cu|<=1/R`, while `int g_1 g_2=1`, so the contribution is at most `1/R`. Optimizing

`2 pi R/d + 1/R`

at `R=sqrt(d/(2 pi))` gives (2.1). `QED`

The lemma uses both facts available from the original coordinates: pointwise cap one near the singularity and probability normalization away from it. It does not assume connected support, moments, or rearrangement extremality.

## 3. Main curved-block theorem

For an invertible real symmetric `3x3` matrix `M`, write

`D=|det M|`,  `m_j=|M e_j|`  for `j=1,2,3`,

and define the anisotropic curvature cost

`K(M)=D^(-1/2) ( m_1^(1/3)+m_2^(1/3)+m_3^(1/3) )^(3/2)`.              (3.1)

### Theorem 3.1 — `QFORM-THREE-COORDINATE-CURVED-COAREA-v1`

Let `Z_1,Z_2,Z_3` be independent real random variables with probability densities bounded by one. For arbitrary `b in R^3`, `c in R`, put

`T=Z^T M Z + 2 b^T Z + c`.

Then `T` has an essentially bounded density and

`||p_T||_infinity <= 2 sqrt(2 pi) K(M)`.                                  (3.2)

No sign assumption on `M` is required.

### Proof

Complete the square. Since `M` is invertible,

`Z^T M Z+2b^T Z+c = Y^T M Y + c'`,

where `Y=Z+M^{-1}b`. The three one-dimensional densities are merely translated and remain independent probability densities bounded by one. It suffices to treat

`q(y)=y^T M y`.

Let `a_j=M e_j` denote the columns of `M`, so `|a_j|=m_j`. For a.e. level `t`, coarea gives

`p_q(t)=int_{q=t} G(y)/|grad q(y)| d sigma(y)`,

where `G(y)=prod_j g_j(y_j)` and `grad q=2My`.

Choose positive numbers `beta_j` and partition the noncritical part of the level surface into three measurable charts `E_j` by assigning `y` to an index maximizing

`|(My)_j|/beta_j`.

Put `B=(beta_1^2+beta_2^2+beta_3^2)^(1/2)`. On `E_j`,

`|(My)_j| >= beta_j |My|/B`.                                                (3.3)

Fix `j`, and let `u` be the two coordinates other than `y_j`. For fixed `u`, the equation `q(y)=t` is a polynomial of degree at most two in `y_j`, hence has at most two roots contributing to `E_j` (the exceptional case where the polynomial is independent of `y_j` has `(My)_j=0` and therefore belongs to another chart away from the unique critical point).

Let `P_j` be orthogonal projection in `R^3` onto `a_j^perp`, and let `C_j:R^2->a_j^perp` be the map formed from the other two columns after this projection. Since `M` is invertible, `C_j` is injective. For every value of the solved coordinate,

`|My|=|a_j y_j + sum_{k!=j} a_k u_k| >= |C_j u|`.                           (3.4)

The volume identity for the three columns gives

`d(C_j)=sqrt(det(C_j^T C_j)) = D/m_j`.                                      (3.5)

On a graph branch, `d sigma/|grad q| = du/|partial_j q| = du/(2 |(My)_j|)`. By (3.3)-(3.4), each branch contributes at most

`[B/(2 beta_j)] g_k(u_k) g_l(u_l) / |C_j u|`.

There are at most two branches, and `g_j<=1`, so the entire `j`-chart contributes at most

`(B/beta_j) int g_k(u_k)g_l(u_l)/|C_j u| du`
` <= 2 sqrt(2 pi) B beta_j^(-1) (m_j/D)^(1/2)`                              (3.6)

by Lemma 2.1 and (3.5). Summing (3.6) over `j` yields

`p_q(t) <= 2 sqrt(2 pi) B sum_j A_j/beta_j`,

where `A_j=(m_j/D)^(1/2)`. Optimize over positive `beta_j`. With

`beta_j proportional to A_j^(1/3)`, 

`B sum_j A_j/beta_j = (sum_j A_j^(2/3))^(3/2)`.

Since `A_j^(2/3)=D^(-1/3)m_j^(1/3)`, (3.2) follows. The bound is uniform for a.e. `t`, hence gives an essentially bounded density. `QED`

## 4. Arbitrary outside coupling and the exact three-dimensional target

### Corollary 4.1 — `QFORM-PHYSICAL-TRIPLE-CONDITIONAL-v1`

For the original `n`-dimensional quadratic form `Q=X^T A X`, suppose some physical triple `I` has an invertible principal block `M=A[I,I]`. Then, with `K(M)` from (3.1),

`||p_Q||_infinity <= 2 sqrt(2 pi) K(M)`.                                   (4.1)

All couplings between `I` and `I^c`, and the whole outside quadratic block, are arbitrary.

**Proof.** Condition on `X_{I^c}`. The conditional polynomial in the three independent coordinates `X_I` has fixed Hessian block `M` and an arbitrary outside-dependent linear term. Theorem 3.1 is uniform in that linear term and constant shift. Average the conditional densities. `QED`

### Corollary 4.2 — universal bound when the physical triple itself has three large singular values

If the three singular values of `M` are all at least `kappa>0`, then

`K(M) <= 3^(3/2)/kappa`

and therefore

`||p_Q||_infinity <= 6 sqrt(6 pi)/kappa`.                                  (4.2)

In particular, for `n=3` under the exact owner hypothesis, all three eigenvalues of `A` have absolute value at least one, so

`||p_Q||_infinity <= 6 sqrt(6 pi) < 26.05`.                                (4.3)

This proves the complete target in physical dimension three, for arbitrary signs, arbitrary independent input densities bounded by one, and arbitrary translations generated by conditioning. It is a supporting theorem only; the arbitrary-dimensional target remains open.

**Proof of the cost estimate.** Write the singular values of `M/kappa` as `s_1,s_2,s_3>=1`. For `N=M/kappa`, every column norm satisfies `|N e_j|<=s_max(N)<=|det N|`, because the product of the other two singular values is at least one. Hence

`(sum_j |N e_j|^(1/3))^(3/2) <= (3 |det N|^(1/3))^(3/2)=3^(3/2)|det N|^(1/2)`.

Insert this into (3.1) and restore the scalar factor `kappa`. `QED`

**Regularity note.** These statements prove existence of an essentially bounded density. They do not separately prove a continuous representative, so the owner's additional continuity request remains open here.

## 5. Actual application of the account02/B06 determinant-mass theorem

The completed partner theorem gives for a same-sign orthonormal pair `r,s` the normalized Pluecker weights

`w_ij=(r_i s_j-r_j s_i)^2`,  `sum_{i<j} w_ij=1`.

Its same report also records the rank-three Cauchy--Binet analogue. Let `U=[r s t]` be an orthonormal three-frame and put

`d_ijk=det U[{i,j,k},:]`.

Then

`sum_{i<j<k} d_ijk^2=1`.                                                     (5.1)

A useful exact bridge from the partner's pair weights to triple curvature is

`sum_k d_ijk^2 = |u_i x u_j|^2`
` = (r_i s_j-r_j s_i)^2 + (r_i t_j-r_j t_i)^2 + (s_i t_j-s_j t_i)^2`
` >= w_ij`,                                                                  (5.2)

where `u_i=(r_i,s_i,t_i)` is the `i`th row of `U`. Equation (5.2) follows from Parseval because `sum_k u_k u_k^T=I_3`. Thus no same-sign pair determinant mass disappears when it is lifted to the three-dimensional spectral truncation: it is redistributed among extending triples.

If `A=U Lambda U^T` has exact rank three, then for every physical triple `I`,

`|det A_I|=|det Lambda| d_I^2`,

and by (5.1)

`sum_{|I|=3}|det A_I|=|det Lambda|`.                                         (5.3)

This is the partner determinant mass applied to the exact local coarea theorem: (5.3) identifies the conserved numerator available to pay (3.1). The only remaining local loss is the reciprocal curved-block cost involving the column geometry of `A_I`.

## 6. Source-valid obstruction: post-hoc determinant averaging of the local bounds still loses dimension

The partner's Hadamard family shows that one cannot finish by first applying Theorem 3.1 separately on each physical triple and only afterward averaging those upper bounds with determinant-mass weights.

Take `n=2^k`, and the exact-rank-three matrix

`A=U diag(1,1,-1)U^T`,

where the rows of `U` are the four sign types `(1,s,t)/sqrt(n)`, each repeated `n/4` times. This is exactly the account02/B06 delocalized construction and has spectrum `{1,1,-1,0,...,0}`.

Any triple containing three distinct row types is invertible. There are

`4 (n/4)^3 = n^3/16`

such unordered triples. For each of them,

`|det U_I|=4/n^(3/2)`,  hence  `D_I=|det A_I|=16/n^3`.                       (6.1)

Moreover every entry of `n A_I` belongs to `{-1,1,3}` and every column has three nonzero entries, so

`m_{I,j}=|A_I e_j| >= sqrt(3)/n`.                                            (6.2)

Therefore the curvature cost obeys

`K(A_I)`
` >= (n^(3/2)/4) [3 (sqrt(3)/n)^(1/3)]^(3/2)`
` = (3^(7/4)/4) n`.                                                          (6.3)

The normalized determinant weights in (5.3) are simply `alpha_I=D_I` because `|det Lambda|=1`. Summing only over the invertible three-distinct-type triples gives

`sum_I alpha_I K(A_I)`
` >= (n^3/16) (16/n^3) (3^(7/4)/4)n`
` = (3^(7/4)/4)n`.                                                           (6.4)

Hence the seemingly natural estimate

`p_Q <= sum_I alpha_I [2 sqrt(2 pi) K(A_I)]`

has a right side growing linearly in `n` on a source-valid target family whose actual quadratic-form density is known from other completed routes to be uniformly controlled. This does **not** refute the QFORM conjecture or Theorem 3.1. It refutes only the post-hoc strategy “apply a reciprocal-curvature block bound first, then average the resulting constants with Cauchy--Binet determinant weights.”

This obstruction is stronger and more precise than merely saying no single physical triple is good: even the exact determinant-mass probability measure from the partner theorem does not repair the loss once the local near/far reciprocal-kernel estimate has already been collapsed to a scalar constant.

## 7. First unpaid implication and next mechanism

The new positive theorem removes arbitrary outside coupling whenever a genuine three-coordinate block has bounded anisotropic cost. The new negative calculation identifies exactly where determinant mass must enter earlier.

The next B06 implication is therefore:

### `QFORM-PREBOUND-WEIGHTED-CURVED-KERNEL-v1` — OPEN

For a three-dimensional large spectral frame, retain the original product factors and the Pluecker/determinant weights **inside** the reciprocal-distance/coarea integral, before applying the near/far split of Lemma 2.1. Prove a dimension-free aggregate inequality, or construct a source-valid target family showing that even this prebound aggregation fails.

A successful inequality must survive the four-type Hadamard frame above, the singleton-plus-two-banks family from the correction inbox, and arbitrary extra spectral directions. It may combine with the ridge-window/diffuse theorem already in the shared state, but it cannot use a fiber supremum, a conditional rotated density cap, or post-hoc averaging of `K(A_I)`.

## 8. Status

**PROVED SUPPORTING:** `QFORM-ANISOTROPIC-1OVER-R-v1`; `QFORM-THREE-COORDINATE-CURVED-COAREA-v1`; `QFORM-PHYSICAL-TRIPLE-CONDITIONAL-v1`; full owner target in dimension `n=3` with explicit bound `6 sqrt(6 pi)<26.05`; pair-to-triple determinant-mass lift (5.2).

**REFUTED MECHANISM:** post-hoc averaging of the local three-coordinate reciprocal-curvature constants with the partner's determinant-mass weights; the Hadamard family forces linear dimension loss in that proof mechanism.

**OPEN:** `QFORM-PREBOUND-WEIGHTED-CURVED-KERNEL-v1`, the arbitrary-dimensional conjecture, and the separate full-target continuity statement.
