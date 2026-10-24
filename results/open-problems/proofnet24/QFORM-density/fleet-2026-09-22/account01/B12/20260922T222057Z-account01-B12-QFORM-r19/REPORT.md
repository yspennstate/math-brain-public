SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-22T22:20:57Z.
attacking: additional-eigenvalue control by weighted hostile-spectrum dilution, removing one arbitrary hostile spike before local physical-triple payment.

# QFORM additional-eigenvalue control: one-spike-free hostile-tail budget

**Run:** `20260922T222057Z-account01-B12-QFORM-r19`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`  
**Owner control observed at start:** `yspennstate/math-research-brain@b4c5c0cb7fa5d4a140b53317c26dff3631168a6e`, control revision `2026-09-22.15`  
**Final pre-publication refresh:** `yspennstate/math-research-brain@07949e3e9f85765be1b0e6d75d4e3d0aeb2ca0cd`, same active target/control revision; no later stop observed.  
**Assignment:** Additional eigenvalue control  
**Status:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full conjecture is not proved here. All arguments remain in original coordinates. No spectral rotation is used to claim independence; no pointwise van-der-Corput estimate, arbitrary-joint coarea lemma, normalized conditional-fiber supremum, or fixed-cross-minor dichotomy is used.

## 1. Completed source actually applied

The named partner `account02/B12` proved the hostile-sign Ky-Fan budget for `K` disjoint definite physical triples:

`yspennstate/math-open-problems@dd063cf7cfb9b0748193f8ab2eaf75f30d42c9bb`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T215532Z-account02-B12-QFORM-r18/REPORT.md`.

Its input theorem is the source-valid physical-three-block result

`yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`:

if one original-coordinate `3 x 3` principal block has two eigenvalues at least `L>0`, or two eigenvalues at most `-L`, then after conditioning every outside original coordinate,

`||p_Q||_infinity <= C_*/L`,

where

`C_* = 2*pi + 3*sqrt(3) + sqrt((2*pi+3*sqrt(3))^2+3*pi^2)`

`= 24.183038289961516...`.

All outside quadratic coefficients and cross couplings are arbitrary. This theorem proves essential boundedness in this scope; continuity is not supplied.

The account02/B12 partner theorem says that if `T_1,...,T_K` are disjoint physical triples with one signed definite core `sigma A_0[T_j,T_j] >= L I_3`, and `sigma E=G-H`, `G,H>=0`, then with `N_-=tr H`,

`||p_{X^T(A_0+E)X}||_infinity <= C_*/(L-N_-/(2K))`

whenever the denominator is positive. The factor `1/(2K)` comes from averaging the second hostile local eigenvalue over disjoint triples. I apply this result below as one term of a strictly stronger spectral-tail budget.

## 2. Weighted physical-core setup

Let `F` be any finite family of original-coordinate triples, with probability weights `w_T>=0`, `sum_T w_T=1`. Fix `sigma in {+1,-1}` and assume

` sigma A_0[T,T] >= L I_3`                                      (2.1)

for every `T` in the support of `w`, where `L>0`.

Let `A=A_0+E`. Allow a general decomposition

` sigma E = G - H + S`,                                        (2.2)

where `G,H>=0` and `S` is symmetric with

`||S||_op <= delta`.                                            (2.3)

There is no rank or magnitude restriction on `G` or `H`; `delta` may be zero. Define the one- and two-coordinate inclusion marginals

`alpha_i = P_w(i in T)`,
`beta_ij = P_w({i,j} subset T)`,                                (2.4)

and `alpha=max_i alpha_i`, `beta=max_{i<j} beta_ij`.

Write the hostile eigenvalues

`h_1 >= h_2 >= ... >= h_n >=0`                                 (2.5)

and choose a unit top eigenvector `v_1`. Set

`R = H - h_1 v_1 v_1^T >=0`.                                   (2.6)

Thus `spec(R)={h_2,...,h_n}` (with zeros as needed). The point of the next theorem is that the top hostile eigenvalue `h_1` can be removed completely before paying the local two-direction damage.

## 3. Five source-valid local hostile budgets

For a triple `T`, let `H_T=H[T,T]` and let `mu_2(H_T)` be its second largest eigenvalue.

### 3.1 Global second hostile eigenvalue

By Cauchy interlacing for principal compressions,

`mu_2(H_T) <= h_2`                                               (3.1)

for every `T`.

### 3.2 Partner trace budget

For a positive semidefinite `3 x 3` matrix,

`mu_2(H_T) <= tr(H_T)/2`.                                       (3.2)

Moreover

`E_w tr(H_T) = sum_i alpha_i H_ii <= alpha tr H`.               (3.3)

Hence some triple obeys

`mu_2(H_T) <= (alpha/2) tr H`.                                  (3.4)

For `K` disjoint triples with uniform weights, `alpha=1/K`; this is exactly the account02/B12 partner inequality `tr H/(2K)`. Thus the named partner theorem is consumed at an actual bound in the final minimum below.

### 3.3 One-spike-free tail-trace budget

Since

`H_T = h_1 v_{1,T} v_{1,T}^T + R_T`,                            (3.5)

Weyl's inequality gives

`mu_2(H_T) <= lambda_2(h_1 v_{1,T}v_{1,T}^T)+lambda_1(R_T)`
`            = ||R_T||_op`
`            <= tr R_T`.                                       (3.6)

Averaging,

`E_w tr R_T = sum_i alpha_i R_ii <= alpha tr R`
`           = alpha sum_{j>=2} h_j`.                            (3.7)

Therefore some triple satisfies

`mu_2(H_T) <= alpha sum_{j>=2} h_j`.                            (3.8)

The magnitude of `h_1` has disappeared completely.

### 3.4 One-spike-free tail-Frobenius budget

Again `mu_2(H_T)<=||R_T||_op<=||R_T||_F`. Also

`E_w ||R_T||_F^2`
` = sum_i alpha_i R_ii^2 + 2 sum_{i<j} beta_ij R_ij^2`
` <= alpha ||R||_F^2`
` = alpha sum_{j>=2} h_j^2`.                                   (3.9)

Hence some triple satisfies

`mu_2(H_T) <= sqrt(alpha sum_{j>=2} h_j^2)`.                    (3.10)

### 3.5 Exterior-square / pair-marginal budget

For a positive semidefinite `3 x 3` matrix with eigenvalues `mu_1>=mu_2>=mu_3>=0`,

`mu_2^2 <= mu_1 mu_2 <= e_2(H_T)`.                              (3.11)

The second elementary symmetric polynomial is the sum of principal `2 x 2` minors, so

`e_2(H_T)=sum_{{i,j} subset T} det H[{i,j}]`.                   (3.12)

Every such principal minor is nonnegative. Consequently

`E_w e_2(H_T)`
` = sum_{i<j} beta_ij det H[{i,j}]`
` <= beta e_2(H)`.                                              (3.13)

Thus some triple satisfies

`mu_2(H_T) <= sqrt(beta e_2(H))`.                               (3.14)

No input distribution has entered any of these estimates; they are exact matrix inequalities in the original coordinate system.

## 4. Main theorem: weighted hostile-tail stability

### Theorem — `QFORM-WEIGHTED-HOSTILE-TAIL-v1`

Under (2.1)-(2.6), define

`Delta = min {`
`  h_2,`
`  (alpha/2) tr H,`
`  alpha sum_{j>=2} h_j,`
`  sqrt(alpha sum_{j>=2} h_j^2),`
`  sqrt(beta e_2(H))`
`}`.                                                            (4.1)

If

`delta + Delta < L`,                                            (4.2)

then for every independent cap-one product source,

`||p_{X^T A X}||_infinity <= C_* /(L-delta-Delta)`.             (4.3)

All favorable-sign added spectrum in `G` is completely free, with arbitrary rank and magnitude. The top hostile eigenvalue `h_1` is also completely free in the third and fourth alternatives of (4.1): its magnitude can tend to infinity without changing those terms.

#### Proof

Each of Sections 3.1-3.5 separately guarantees a triple `T` with

`mu_2(H_T)` bounded by the corresponding scalar in (4.1). Choose the mechanism attaining the minimum `Delta`, and its associated triple. On that triple,

`sigma A[T,T]`
` = sigma A_0[T,T] + G_T-H_T+S_T`
` >= L I_3-H_T+S_T`.                                           (4.4)

By Weyl,

`lambda_2(sigma A[T,T])`
` >= L-mu_2(H_T)-||S_T||_op`
` >= L-Delta-delta >0`.                                        (4.5)

Thus this physical block has two eigenvalues of sign `sigma` and magnitude at least `L-Delta-delta`. Apply `QFORM-TWO-SAMESIGN-THREEBLOCK-v1` after conditioning on every outside original coordinate. The conditional bound is uniform in all affine tilts and outside values, so averaging gives (4.3). QED.

### Exact weighted version

The scalar `alpha,beta` form is convenient but not optimal. The same proof yields the sharper quantity

`Delta_exact = min {`
` h_2,`
` (1/2) sum_i alpha_i H_ii,`
` sum_i alpha_i R_ii,`
` [sum_i alpha_i R_ii^2 + 2 sum_{i<j} beta_ij R_ij^2]^(1/2),`
` [sum_{i<j} beta_ij det H[{i,j}]]^(1/2)`
`}`.                                                            (4.6)

Replacing `Delta` by `Delta_exact` in (4.2)-(4.3) remains valid. This orientation-sensitive form may be useful when the hostile eigenspaces have known coordinate leverage.

## 5. Disjoint triples: strict refinement of the partner theorem

For `K` pairwise-disjoint triples with uniform weights,

`alpha=beta=1/K`.                                               (5.1)

The theorem becomes

`Delta_K = min {`
` h_2,`
` tr H/(2K),`
` (sum_{j>=2} h_j)/K,`
` sqrt((sum_{j>=2} h_j^2)/K),`
` sqrt(e_2(H)/K)`
`}`.                                                            (5.2)

Whenever `delta+Delta_K<L`,

`||p_Q||_infinity <= C_* /(L-delta-Delta_K)`.                  (5.3)

The term `tr H/(2K)` is exactly the completed account02/B12 result, now combined with four independent source-valid alternatives. In particular the partner bound can be very pessimistic when a single hostile eigenvalue dominates the trace.

### Rank-two hostile spectrum: the largest hostile eigenvalue is completely irrelevant

If `H` has rank two, with eigenvalues `h_1>=h_2>=0`, then the tail-trace branch in (5.2) gives

`Delta_K <= h_2/K`.                                             (5.4)

Therefore

`boxed:  ||p_Q||_infinity <= C_* /(L-delta-h_2/K)`              (5.5)

whenever `delta+h_2/K<L`, with **no dependence at all on `h_1`**. Thus one hostile added eigendirection may have arbitrary magnitude; the second hostile direction is diluted by the number of disjoint physical cores.

This is strictly stronger than the partner trace denominator `L-(h_1+h_2)/(2K)` whenever `h_1` is sufficiently larger than `h_2`.

## 6. Sharpness of the `h_2/K` coefficient for this certificate family

Let `n=3K`, `A_0=L I_n`, and define orthonormal vectors

`v_1=K^(-1/2) sum_{j=1}^K e_{3j-2}`,
`v_2=K^(-1/2) sum_{j=1}^K e_{3j-1}`.                            (6.1)

Set

`H=h_1 v_1v_1^T+h_2 v_2v_2^T`, `h_1>=h_2>=0`.                 (6.2)

On every designated triple `T_j={3j-2,3j-1,3j}`,

`H[T_j,T_j]=diag(h_1/K,h_2/K,0)`,                              (6.3)

and hence

`mu_2(H[T_j,T_j])=h_2/K`.                                      (6.4)

So the factor `1/K` in (5.4) is attained simultaneously on every block. At `h_2=KL`, every designated final triple loses its second positive `L`-scale direction. No improvement of the coefficient `1/K` is possible using only survival of these prescribed two-same-sign physical-triple certificates.

This remains only a mechanism barrier, not a counterexample to QFORM. Indeed the full matrix has spectrum

`{L-h_1, L-h_2, L (multiplicity 3K-2)}`.                        (6.5)

For `K>=2` and `L>=1` it still has many large eigenvalues; other global or aggregate certificates can control it.

## 7. Dense scalar-core corollary

If `A_0=L I_n` and the weighted family is uniform over all coordinate triples, then

`alpha=3/n`, `beta=6/[n(n-1)]`.                                 (7.1)

Hence

`Delta_n = min {`
` h_2,`
` 3 tr H/(2n),`
` 3 sum_{j>=2}h_j/n,`
` sqrt(3 sum_{j>=2}h_j^2/n),`
` sqrt(6 e_2(H)/(n(n-1)))`
`}`.                                                            (7.2)

If `delta+Delta_n<L`, then (4.3) holds. This is a dimension-dependent redundancy statement about a scalar physical core, not a claim that the bare three-large-eigenvalue hypothesis creates such a core.

## 8. Consequence for the B12 additional-eigenvalue assignment

The theorem supplies a nonperturbative stability hierarchy in original coordinates:

1. arbitrary same-sign additional eigenvalues: free;
2. one arbitrary hostile eigenvalue: free at every magnitude;
3. further hostile eigenvalues: paid by the **tail after removing the largest hostile spike**, through trace, Frobenius, or exterior-square budgets diluted by physical-core leverage;
4. an arbitrary mixed-sign dense remainder `S` is allowed at operator-norm cost `delta`;
5. arbitrary outside coefficients and cross couplings remain free after the final physical-block conditioning.

No convolution with a dependent spectral remainder is invoked.

## 9. Remaining connection to the full conjecture

The full target remains OPEN. The missing implication is structural: from only `s_3(A)>=1`, force either an already-paid ridge / grouped-bank / cross-volume branch, or a weighted family of physical same-sign cores for which one of the hostile-tail quantities above is `<L` at a universal scale. The existing singleton-plus-two-bank and low-cross-rank correction families show that one cannot simply assume a uniformly good local triple or rank-three cross cut.

This run changed mechanism from the preceding affine-hereditary induction argument to a weighted hostile-spectrum budget. The new theorem is particularly aimed at the current hub-plus-delocalized-small-dense-tail survivor: a dominant hostile spike is no longer charged by trace, but a source-valid route is still needed to manufacture the redundant physical cores or switch to the existing hub/ridge certificates.

## 10. Regularity and status

The argument proves interval domination and therefore absolute continuity with an essentially bounded density in its stated scope. It does **not** prove a continuous representative. Continuity for the full target remains separate.

Classification: `PROVED_SUPPORTING_THEOREM_FULL_TARGET_OPEN`.
