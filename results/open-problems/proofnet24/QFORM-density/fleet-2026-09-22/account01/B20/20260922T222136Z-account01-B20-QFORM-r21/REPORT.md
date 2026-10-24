# account01/B20 QFORM r21 — fractional volume-sampling closure and a two-anchor O0 packet

Run: `20260922T222136Z-account01-B20-QFORM-r21`

Classification: **ESSENTIAL_STEP_APPLIED / O0-FRACTIONAL-BL-DIFFUSE-BRANCH-PAID / O0-TWOANCHOR-PACKET-FORCED / FULL_TARGET_OPEN**.

The full conjecture remains open. The argument below proves a new full-ambient density theorem at an enlarged volume-sampling leverage range and uses it to sharpen the remaining O0 third-compound branch. On the branch paid by the Fourier argument, the density is in fact continuous. No global continuity conclusion is claimed.

## 1. Target and guards

The target is the exact QFORM problem: `X_1,...,X_n` are arbitrary independent real random variables with probability densities `0<=f_i<=1`; `A` is arbitrary real symmetric with at least three eigenvalues of absolute value at least one; prove that `Q=X^TAX` has an essentially bounded density with one universal finite bound, or produce a valid counterexample.

No Gaussian, moment, iid, compact-support, log-concavity, connected-support, post-rotation independence, or conditional spectral-density hypothesis is introduced. The false law-uniform pointwise quadratic oscillatory-decay route is not used. The arbitrary-joint rank-three coarea shortcut and the false conditional projected-moment/supremum gates are not used.

Fresh programme control was read at the start. The owner revision is `2026-09-22.15`; QFORM is the sole active research target.

## 2. Source results actually consumed

### 2.1 Newest completed designated partner account02/B20 r20

Source: `yspennstate/math-open-problems@2c967d975f242fa53556b8ec132ac668dcf003a0`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260922T215937Z-account02-B20-QFORM-r20/REPORT.md`.

That report proves that the localized high-window state is already fully paid: if a source-valid physical outer pivot has `|a|>=tau>=1/4` and the exact second Schur row has `max{|d|,||c||_2}>tau/9`, then `||p_Q||_infinity<5262`. Consequently the genuine debt moves upstream to structural exhaustion, explicitly including the O0 singleton-plus-five-bank / third-compound branch. I use that logical relocation here: no work is spent on the already-paid downstream two-anchor compatibility state.

### 2.2 account02/B20 r13 O0 full-matrix certificate

Source report: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260922T165822Z-account02-B20-QFORM-r13/REPORT.md`; canonical source recorded by the partner handoff as `yspennstate/math-open-problems@ccd703b260df4eca8b539b6614e2cecdad3e7465`.

The O0 structural reduction supplies a physical cross cut `B=A[L,R]` with

`Z := e_3(B^T B) = sum_{|S|=|T|=3} det(B[S,T])^2 >= 1/256`.                  (2.1)

This is an actual original-coordinate cross block of the full quadratic form; all same-side blocks and outside couplings remain arbitrary.

### 2.3 Reviewed volume-sampling decoupling theorem D and sharp Hausdorff-Young refinement

Reviewed source: `yspennstate/math-open-problems@9844891a9fbe96a65e37f71122bf0300b53dcc80`, `proofnet24/QFORM-density/interactive/20260922T220600Z-claude-review/REVIEW.md`, reviewing the Claude-attributed package `yspennstate/math-open-problems@7359c982f3fa85f61b99e8768b915cce6e596d36`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For volume weights

`w_ST = det(B[S,T])^2 / Z`,

write

`alpha_i = P_w(i in S)`,   `beta_j = P_w(j in T)`.

The reviewed theorem D pays the full ambient form if all row marginals satisfy `alpha_i<=1/2`; the sharp reviewed refinement gives `||p_Q||_infinity<=3 e Z^(-1/6)`. The proof is a product-preserving Weyl differencing / Brascamp-Lieb argument and retains arbitrary same-side quadratic terms and outside couplings.

The new theorem below changes the Brascamp-Lieb exponents and enlarges the admissible marginal range.

## 3. New theorem: fractional volume-sampling Brascamp-Lieb

### Theorem `QFORM-FRACTIONAL-VOLUME-BL-v1`

Let `I,J` be disjoint physical coordinate sets, `M=A[I,J]`, and

`Z=e_3(M^T M)>0`.

Let `w_ST=det(M[S,T])^2/Z` on row/column triples with nonzero minors, and let `alpha_i,beta_j` be its row and column inclusion marginals. Fix

`2/3 < theta < 1`.

Assume

`theta * alpha_i <= 1/2` for every `i in I`.                         (3.1)

Then the **full ambient quadratic form**, with arbitrary `A[I,I]`, `A[J,J]`, all outside coordinates/couplings and all affine terms, has a bounded continuous density satisfying

`||p_Q||_infinity <= C_theta Z^(-1/6)`,                              (3.2)

where

`C_theta = e * [3 theta/(3 theta-2)] * K_theta^(-1/(6 theta))`,       (3.3)

and

`K_theta = theta^(-theta) (1-theta)^(-(1-theta))`.                   (3.4)

Equivalently,

`C_theta = e * [3 theta/(3 theta-2)] * theta^(1/6) * (1-theta)^((1-theta)/(6 theta))`.

The theorem is orientation-symmetric: it can be applied to `M^T`, replacing the row marginals `alpha` by the original column marginals `beta`.

### Proof

The Weyl-differencing step of theorem D is source-valid for the full ambient form and gives

`|phi_Q(t)|^2 <= integral_{R^J} prod_i |psi_i(2t <a_i,w>)| prod_j g_j(w_j) dw`,    (3.5)

where `a_i` are the physical rows of `M`, `psi_i` are the characteristic functions of the original physical inputs on `I`, and `g_j=f_j*f_j_tilde` are probability densities satisfying `0<=g_j<=1`. All same-side quadratic terms disappear in this Cauchy-Schwarz difference exactly as in theorem D; no rotation of the source variables occurs.

Set

`c_i = theta alpha_i`,    `d_j = 1-theta beta_j`.                    (3.6)

Then

`sum_i c_i = 3 theta`,
`sum_j d_j = |J|-3 theta`,
`sum_i c_i + sum_j d_j = |J|`.                                      (3.7)

By (3.1), `0<=c_i<=1/2`. Since `theta<1` and `0<=beta_j<=1`, every `d_j` lies in `(0,1]`.

We claim that the Brascamp-Lieb datum consisting of the row maps `a_i:R^J->R` with exponents `c_i` and the coordinate maps `e_j:R^J->R` with exponents `d_j` has Gaussian constant at most

`K_theta^(-1/2) Z^(-theta/2) prod_i c_i^(-c_i/2) prod_j d_j^(-d_j/2)`.    (3.8)

To prove this, take positive Gaussian parameters and put

`D_I=diag(x_i)`, `D_J=diag(y_j)`

with `x_i=c_i p_i`, `y_j=d_j q_j`. Cauchy-Binet gives

`det(D_J+M^T D_I M)`
` = det(D_J) det(I+N^T N)`
` >= det(D_J) [1+e_3(N^T N)]`,                                      (3.9)

where `N=D_I^(1/2) M D_J^(-1/2)`. Moreover

`e_3(N^T N)`
` = sum_{S,T} det(M[S,T])^2 prod_{i in S} x_i prod_{j in T} y_j^(-1)`
` >= Z prod_i x_i^(alpha_i) prod_j y_j^(-beta_j)`                    (3.10)

by weighted AM-GM with the exact volume weights `w_ST`.

For every `u>0`,

`1+u >= K_theta u^theta`,                                            (3.11)

because `(1+u)u^(-theta)` is minimized at `u=theta/(1-theta)` and the minimum is exactly (3.4). Combining (3.9)-(3.11),

`det(D_J+M^T D_I M)`
` >= K_theta Z^theta prod_i x_i^(theta alpha_i) prod_j y_j^(1-theta beta_j)`
` = K_theta Z^theta prod_i x_i^(c_i) prod_j y_j^(d_j)`.              (3.12)

The Gaussian Brascamp-Lieb ratio therefore gives (3.8), and Lieb's Gaussian-exhaustion theorem transfers that bound to the full datum.

Apply Brascamp-Lieb to (3.5) with

`F_i(s)=|psi_i(2ts)|^(1/c_i)`, `G_j(s)=g_j(s)^(1/d_j)`

(omit zero `c_i`). Since `c_i<=1/2`, the exponent `1/c_i>=2`, and sharp Hausdorff-Young in the Fourier convention used by the reviewed theorem gives

`[integral |psi_i(2ts)|^(1/c_i) ds]^(c_i)`
` <= (pi/|t|)^(c_i) (1-c_i)^(-(1-c_i)/2) c_i^(c_i/2).`               (3.13)

The `c_i^(c_i/2)` factors cancel those in (3.8). Also, because `0<=g_j<=1` and `integral g_j=1`,

`[integral g_j^(1/d_j)]^(d_j) <= 1`.                                (3.14)

Thus

`|phi_Q(t)|^2`
` <= K_theta^(-1/2) Z^(-theta/2) (pi/|t|)^(3theta) R_theta D_theta`,  (3.15)

where

`R_theta=prod_i (1-c_i)^(-(1-c_i)/2)`,
`D_theta=prod_j d_j^(-d_j/2)`.

For `0<=x<1`, `-(1-x)log(1-x)<=x`. Hence

`log R_theta <= (1/2) sum_i c_i = 3theta/2`,
`log D_theta <= (1/2) sum_j (1-d_j) = 3theta/2`,                     (3.16)

so `R_theta D_theta<=e^(3theta)`. Taking square roots,

`|phi_Q(t)| <= min{1, A_theta |t|^(-3theta/2)}`,                     (3.17)

with

`A_theta = K_theta^(-1/4) e^(3theta/2) Z^(-theta/4) pi^(3theta/2)`.  (3.18)

Because `theta>2/3`, put `gamma=3theta/2>1`. Then

`integral_R min{1,A |t|^(-gamma)} dt`
` = 2 [gamma/(gamma-1)] A^(1/gamma)`.                               (3.19)

Fourier inversion therefore applies absolutely and gives a bounded continuous density. Substituting (3.18) into (3.19) and dividing by `2pi`,

`||p_Q||_infinity`
` <= e [gamma/(gamma-1)] K_theta^(-1/(6theta)) Z^(-1/6)`
` = C_theta Z^(-1/6)`.                                               (3.20)

This is (3.2)-(3.3). QED.

### Scope comments

1. The theorem does **not** assert that every cross block satisfies (3.1).
2. It uses the actual volume-sampling marginals of the actual original-coordinate cross block.
3. No post-rotation independence is invoked.
4. The arbitrary same-side blocks are retained through the same Weyl-difference step as reviewed theorem D.
5. Taking `theta -> 1` recovers the sharp theorem-D constant `3e Z^(-1/6)` formally; the endpoint `theta=1` is handled by the reviewed theorem's endpoint convention.
6. A fixed `theta>2/3` is essential for a universal numerical bound. One must not let `theta` depend on a marginal approaching the endpoint in a way that makes `3theta-2 ->0` and then call the resulting family uniformly bounded.

## 4. Concrete theta=3/4 payment: the volume-marginal gate improves from 1/2 to 2/3

Take

`theta=3/4`.

Then condition (3.1) is simply

`max_i alpha_i <= 2/3`.                                              (4.1)

Here

`K_(3/4)=4/3^(3/4)`,

and

`C_(3/4)=9 e (3^(3/4)/4)^(2/9)`
`         =9 e 3^(1/6) / 4^(2/9)`
`         =21.5906685951...`.                                       (4.2)

In the account02/B20 O0 certificate (2.1), `Z>=1/256`, so

`||p_Q||_infinity`
` <= C_(3/4) 256^(1/6)`
` = 9 e 3^(1/6) 2^(8/9)`
` =54.4050756888... <54.406`.                                       (4.3)

This is a target-level full-ambient density bound, not a small-ball-only statement.

The same is true after reversing the physical cut. Therefore **the O0 branch is already paid whenever either**

`max_{i in L} alpha_i <= 2/3`                                       (4.4)

or

`max_{a in R} beta_a <= 2/3`.                                       (4.5)

This strictly enlarges the original theorem-D diffuse gate `<=1/2` on both orientations.

## 5. What an unpaid O0 state must now contain: two volume-heavy physical anchors

Suppose the O0 state is not paid by (4.3) in either orientation. Then there are physical coordinates

`i in L`, `a in R`

such that

`alpha_i>2/3`, `beta_a>2/3`.                                        (5.1)

Under the exact squared-minor volume distribution,

`P_w(i in S and a in T)`
` >= alpha_i+beta_a-1`
` > 1/3`.                                                            (5.2)

Hence the actual squared third-minor mass simultaneously containing the two physical anchors satisfies

`Z_{ia}:=sum_{S contains i, T contains a} det(B[S,T])^2 > Z/3 >= 1/768`.    (5.3)

This is a direct inequality-level application of the account02/B20 O0 certificate `Z>=1/256`.

Now independently two-color `L\{i}` and two-color `R\{a}`. Every minor contributing to `Z_{ia}` has exactly two remaining rows and two remaining columns; the probability that each pair receives different colors is `(1/2)(1/2)=1/4`. Therefore some deterministic physical partitions

`L\{i}=L_1 disjoint_union L_2`,
`R\{a}=R_1 disjoint_union R_2`

satisfy

`P_ia := sum_{j in L_1,k in L_2,b in R_1,c in R_2}`
`        det B[{i,j,k},{a,b,c}]^2`
`      > Z_{ia}/4`
`      > 1/3072`.                                                    (5.4)

Thus the old O0 singleton-plus-five-bank debt can be replaced, after the new diffuse payment, by a **two-anchor plus four-bank packet**. Both anchors are genuine original coordinates, and all six blocks preserve the source product structure.

For comparison, the older account02/B20 r13 + account01/B20 cascade only guaranteed a singleton-plus-five-bank packet `>1/110592`; (5.4) has a second fixed physical anchor and 36 times the determinant-mass floor.

## 6. A concrete matching-energy corollary of the two-anchor packet

Define physical squared energies

`e = B_ia^2`,
`x_q = sum_{b in R_q} B_ib^2` for `q=1,2`,
`y_p = sum_{j in L_p} B_ja^2` for `p=1,2`,
`E_pq = sum_{j in L_p,b in R_q} B_jb^2` for `p,q in {1,2}`.          (6.1)

For one determinant in (5.4), expand by its six Leibniz monomials and use

`(z_1+...+z_6)^2 <= 6(z_1^2+...+z_6^2)`.                            (6.2)

Summing over the four banks makes every monomial-square sum factor. The exact result is

`P_ia <= 6[`
` e E_11 E_22 + e E_12 E_21`
` + x_1 y_1 E_22 + x_1 E_12 y_2`
` + x_2 y_1 E_21 + x_2 E_11 y_2 ]`.                                (6.3)

Consequently at least one of the six displayed physical matching-energy products is strictly larger than

`P_ia/36 > 1/110592`.                                               (6.4)

This is not promoted to a density theorem by itself. It is a source-valid quantitative interface for the next analytic payment: every remaining O0 state contains three disjoint physical cross-energy resources whose product is dimension-free, and those resources are organized around two fixed physical anchors rather than one.

## 7. Conditional end-to-end implication after this run

The newest account02/B20 r20 already closes the localized high-window second-Schur-row state. In the O0 full-matrix route, account02/B20 r13 supplies the cross block with `Z>=1/256`. The present theorem now closes every such O0 cross block for which **either orientation** has maximum volume-sampling inclusion marginal at most `2/3`, with the explicit full density bound `<54.406` and continuity on that branch.

Therefore a still-unpaid O0 state must satisfy the much stronger source statement (5.1)-(5.4): a row anchor and a column anchor each carry more than `2/3` of the exact third-minor volume law, and more than `1/3072` of actual squared third-minor mass survives in a two-anchor/four-bank packet. Equivalently one of the six matching products in (6.3) exceeds `1/110592`.

This removes all intermediate O0 states with volume marginal in `(1/2,2/3]` that were not covered by reviewed theorem D. It is a genuine enlargement of the paid target-level region.

## 8. First unpaid implication

The first O0 implication is now:

`QFORM-O0-TWOANCHOR-FOURBANK-PAYMENT-v1`.

Given the full target source model and an O0 physical cut with the two-anchor packet (5.4), pay the full quadratic-output density, or transfer the packet by original-coordinate operations into an already-paid physical pair/triple, grouped-square, localized-high-window, ridge, or two-physical-square-plus-cross packet.

The most direct next mechanism is to keep the two physical anchors explicit and split according to the six alternatives in (6.3). The terms with `e=B_ia^2` should be compared with the reviewed physical-pair payments; the four terms without `e` are genuine two-star-plus-cross-bank configurations. Any use of a selected edge must be derived from an aggregate inequality and may not assume one coefficient is dimension-free. The known many-small-edge counterexamples remain valid.

The full QFORM theorem remains open because this two-anchor packet has not yet been universally paid, and the other full-matrix O1/O2/O3/upstream structural routes must remain at their independently proved scopes.

## 9. Arithmetic check used in this report

A deterministic checker in this run directory verifies:

- `theta=3/4` gives the gate `1/(2theta)=2/3`;
- the interpolation constant in (3.11) is minimized at `u=3` with `K_theta=1.754765350603...`;
- `C_(3/4)=21.59066859519...`;
- with `Z>=1/256`, the density cap is `54.40507568878...`;
- the two-anchor coloring floor is `1/3072`;
- the six-monomial matching-product floor is `1/110592`.

The checker is only arithmetic validation; the mathematical proof is the derivation above.

## 10. Status and integrity

- `ESSENTIAL_STEP_APPLIED`: yes.
- `QFORM-FRACTIONAL-VOLUME-BL-v1`: proved above at its stated scope.
- `O0 max row volume marginal <=2/3`: paid with bounded continuous density.
- `O0 max column volume marginal <=2/3`: paid by transposed orientation.
- `O0 unpaid => two physical anchors >2/3 plus packet >1/3072`: proved.
- Full QFORM target: **OPEN**.
- Global continuity: **OPEN**; continuity is proved only on the fractional-BL branch because `phi_Q` is absolutely integrable there.
- No counterexample to QFORM was found.
- Execution label: `WITHOUT_VERIFIED_BRAIN`; repository source retrieval is not authenticated native learned-memory ingestion.
