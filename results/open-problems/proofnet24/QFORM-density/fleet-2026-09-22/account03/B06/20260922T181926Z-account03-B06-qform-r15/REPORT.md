SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B06, 2026-09-22T18:19:26Z.
attacking: product-weighted curved-fiber aggregation; upgrade the shear-invariant transverse e2 reserve from a 5/6 ridge-leverage collar to an arbitrary 1-epsilon collar, then spend the resulting fractional Fourier integrability through a genuine original-coordinate square.

# account03/B06 QFORM r15 — arbitrary near-coloop ridge collar from curved transverse mass

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T181926Z-account03-B06-qform-r15`  
**Assignment:** Curved fiber integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target status:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** not proved by the new theorem below; only absolute continuity plus an essential `L^infinity` bound on its paid branch.

## 0. Fresh source state and exact scope

The current owner control read at the beginning of this run was revision `2026-09-22.11`, with QFORM as the only research programme. The source owner message still contains proposed rank-three/coarea and scalar-conditioning ideas, but the live proof-first correction and `CURRENT_RESEARCH.md` explicitly override two of those proposed premises: arbitrary-joint rank-three coarea from only a joint-density cap is false, and every fixed positive moment of the worst conditional spectral projection density below exponent two can diverge even for a target product-law family. Neither route is used here.

The exact target remains: for every finite `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite essential bound for the density of `Q=X^TAX`, or give a target-valid counterexample. Rotating the random vector and then asserting independence is forbidden. The theorem below is a supporting payment inside the current product-preserving O0/transverse branch, not a solution of the whole target.

### Completed inputs actually used

1. **account03/B08, shear-invariant transverse reserve and the 5/6 payment.** Canonical mathematics `yspennstate/math-open-problems@053ed5a463b2d66682876bd9fd7ba9f55d5ae29a`. In the calibrated O0 branch, after selecting an original physical row and making its arbitrary scalar-Schur shear, the actual residual cross block `H` has singular values `h_j`, while a shear-invariant transverse matrix `D` has singular values `delta_j` satisfying

   `e_2(D D^T)>=2/3`, `||D||op<=1`, and `delta_j<=h_j/gamma`.

   Consequently, with

   `x_j=min(1,h_j^2/gamma^2)`,

   one has

   `e_2(x)>=2/3`.                                                     (0.1)

   That report spent only one fixed smaller scale and obtained a residual ridge-leverage gate `<=5/6`.

2. **Full-form ridge graph estimate.** Canonical mathematics `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`. For any original-coordinate cross block `H`, scale `g>0`, and `1<=q<=2`, if

   `max_i (K_g(H))_ii <= q/2`,

   where

   `K_g(H)=H H^T(g^2 I+H H^T)^(-1)`,

   the proof gives, for the full residual quadratic form including arbitrary same-side quadratic terms, outside couplings and affine terms,

   `|phi_R(t)| <= D_g^(-1/(4q)) [L_q/(2g|t|)]^(theta_g/(2q))`,        (0.2)

   with `theta_g=tr K_g(H)`, `D_g=det(I+HH^T/g^2)`, and `L_q=pi e sqrt(2/q)`. This estimate itself does not require `theta_g>2q`; that stronger inequality is only needed for direct `L^1` Fourier inversion. Also `log D_g>=theta_g`, hence after writing (0.2) as `min(1,(t0/|t|)^beta)` one may take

   `t0 <= pi sqrt(2e/q)/(2g)`.                                      (0.3)

3. **Compatible completed account04 result actually applied.** The designated `account04/B06` still had no completed current-QFORM canonical report or handoff at the fresh search, so no result is fabricated for it. The completed account04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical claim source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, proves the dependence-safe square kernel. Its proof yields, before its final `L^infinity` bathtub step, the exact domination

   `p_(R+aV_R^2)(t) <= |a|^(-1/2) int_0^infinity p_R(t-sgn(a)u) u^(-1/2) du`,   (0.4)

   whenever the conditional density of `V_R` is at most one. This is applied below with an `L^p`, rather than `L^infinity`, base density. Thus an actual completed account04 inequality is used, while the exact assigned-partner absence is reported honestly.

No pointwise law-uniform quadratic-phase decay, unrestricted fiber supremum, generic X-ray cap, post-rotation independence, fixed good local minor, direct Pluecker-to-pivot support claim, or scalar worst-conditioning claim is used.

## 1. Compact conditional end-to-end route

The branch starts after an original scalar pivot `a!=0` has been selected in the current O0 construction. Completing only that physical coordinate gives

`Q = R_0 + a V^2`,                                                   (1.1)

where `R_0` is the exact Schur-residual quadratic form in the remaining original coordinates and `V` is the original scalar input translated by a measurable function of those remaining coordinates. Conditional on the residual coordinates, and hence after disintegration over `R_0`, the density of `V` is still at most one.

The current missing implication is therefore not to bound a fiber supremum. It is to prove enough **integrated** regularity of `R_0` from the transverse curvature bank so that the one-sided square kernel in (0.4) becomes bounded. The B08 transverse reserve (0.1) gives exactly the nonlocal curvature mass needed for this.

The new theorem below proves that for **every fixed** `0<epsilon<=1/2`, it is enough that the residual ridge leverage at a correspondingly smaller scale be at most `1-epsilon`. Thus the previously paid `5/6` collar is upgraded to an arbitrary near-coloop collar. The price is an explicit constant that deteriorates as `epsilon downarrow0`, which is acceptable for any fixed collar used in a universal branch decomposition.

## 2. Scalar concentration lemma: `e2` forces almost two ridge directions at a smaller scale

Put

`C0 := 4+2 sqrt(3)`.                                                   (2.1)

### Lemma 2.1 — `QFORM-E2-TO-ARBITRARY-COLLAR-RIDGE-v1`

Let `x_1,...,x_m in [0,1]` satisfy

`e_2(x)=sum_(i<j) x_i x_j >=2/3`.                                     (2.2)

For `0<epsilon<=1/2`, set

`lambda_epsilon := epsilon/C0`.                                       (2.3)

Then

`sum_j x_j/(lambda_epsilon+x_j) >= 2-epsilon`.                         (2.4)

#### Proof

Let `S=sum_j x_j`. Since

`e_2(x) = (S^2-sum_j x_j^2)/2 <= S^2/2`,

(2.2) gives

`S>=2/sqrt(3)=1+r0`, `r0:=2/sqrt(3)-1`.                               (2.5)

For fixed `lambda>0`, define

`F_lambda(x)=x/(lambda+x)`, `0<=x<=1`.

This function is increasing, concave and satisfies `F_lambda(0)=0`. On the polytope `0<=x_j<=1`, `sum x_j=S`, a concave function achieves its minimum at an extreme point. Thus, when `1<=S<2`, the minimum of `sum F_lambda(x_j)` is `F_lambda(1)+F_lambda(S-1)`; for `S>=2` it is at least `2F_lambda(1)`. Since the objective is increasing with the available total mass, (2.5) therefore yields uniformly

`sum_j F_lambda(x_j) >= F_lambda(1)+F_lambda(r0)`.                     (2.6)

Now

`2-F_lambda(1)-F_lambda(r0)
 = lambda/(1+lambda)+lambda/(r0+lambda)
 <= lambda(1+1/r0)`.                                                   (2.7)

A direct rationalization gives

`1+1/r0 = 4+2sqrt(3)=C0`.                                              (2.8)

Taking `lambda=lambda_epsilon=epsilon/C0` proves (2.4). QED.

### Why this is the right kind of estimate

The proof aggregates the **whole elementary-symmetric mass** before making any reciprocal payment. If the `e_2` mass is spread over many tiny directions, then there are many terms in (2.4); if it is concentrated, the box constraint `x_j<=1` forces at least a second nontrivial direction. The estimate therefore has no ambient-dimension factor and does not select a weakest singular direction.

## 3. Transfer to the actual Schur cross block

Return to the B08 transverse setup and let `h_j` be the singular values of the exact Schur cross block `H`. From (0.1),

`x_j=min(1,h_j^2/gamma^2)` satisfies `e_2(x)>=2/3`.                    (3.1)

For fixed `epsilon in (0,1/2]`, define the smaller ridge scale

`g_epsilon := gamma sqrt(lambda_epsilon)
            = gamma sqrt(epsilon/(4+2sqrt(3)))`.                      (3.2)

Then

`theta_epsilon := tr K_(g_epsilon)(H)
 = sum_j [h_j^2/gamma^2]/[lambda_epsilon+h_j^2/gamma^2]`.              (3.3)

The scalar map `u -> u/(lambda+u)` is increasing and `h_j^2/gamma^2 >= x_j` whenever the latter was truncated at one. Therefore Lemma 2.1 gives

`boxed(theta_epsilon >=2-epsilon.)`                                   (3.4)

This is the new quantitative curvature bank. B08 used one fixed scale to get `theta>=16/9`; (3.4) lets the guaranteed effective ridge dimension approach two arbitrarily closely, while keeping a fully explicit scale.

## 4. Fractional ridge integrability up to leverage `1-epsilon`

Set

`q_epsilon := 2(1-epsilon)`,
`s_epsilon := 2-epsilon`,
`p_epsilon := s_epsilon/(s_epsilon-1)`.                               (4.1)

For `0<epsilon<=1/2`, one has `1<=q_epsilon<2`, `1<s_epsilon<2`, and `p_epsilon>2`.

Assume the residual ridge leverage obeys the single quantitative gate

`max_i (K_(g_epsilon)(H))_ii <=1-epsilon = q_epsilon/2`.               (4.2)

The ridge graph estimate (0.2) is therefore admissible. Put

`beta=theta_epsilon/(2q_epsilon)`.

By (3.4),

`beta >= beta0 := (2-epsilon)/(4(1-epsilon))`.                         (4.3)

The key borderline arithmetic is exact:

`beta0 s_epsilon
 = (2-epsilon)^2/[4(1-epsilon)]
 = 1 + epsilon^2/[4(1-epsilon)] >1`.                                  (4.4)

Thus, although `theta_epsilon` need not exceed `2q_epsilon` and direct Fourier `L^1` inversion need not hold, the characteristic function is in the strictly stronger-than-critical space `L^(s_epsilon)` needed before a square smoothing step.

Write (0.2) as

`|phi_R0(t)| <= min(1,(t0/|t|)^beta)`.                                (4.5)

Using `log D>=theta` as in the source theorem and `q=q_epsilon`,

`t0 <= pi sqrt(e/(1-epsilon))/(2g_epsilon).`                           (4.6)

Since `x/(x-1)` decreases for `x>1`, (4.4) gives

`int_R |phi_R0(t)|^(s_epsilon) dt
 <= 2 t0 * [beta0 s_epsilon/(beta0 s_epsilon-1)]
 = 2 t0 * (2-epsilon)^2/epsilon^2.                                    (4.7)

Inverse Hausdorff--Young, with the sharp factor discarded only in the safe direction, yields an `L^(p_epsilon)` density for `R_0` satisfying

`||p_R0||_(p_epsilon)
 <= (2pi)^(-1/s_epsilon)
    [2t0 (2-epsilon)^2/epsilon^2]^(1/s_epsilon).`                      (4.8)

This step proves absolute continuity of the residual law on this branch; no pointwise stationary-phase claim is used.

## 5. Actual application of the account04 dependent-square kernel

From the original-coordinate completion (1.1), the pre-bathtub inequality in account04/B18's `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` gives exactly

`p_Q(t)
 <= |a|^(-1/2) int_0^infinity p_R0(t-sgn(a)u) u^(-1/2) du`.             (5.1)

This is the completed account04 result applied to the actual branch inequality. We now spend the `L^p` information from (4.8), rather than its theorem's stronger `L^infinity` hypothesis.

Let `p=p_epsilon` and let its conjugate be `s=s_epsilon`. For an arbitrary split point `U>0`, Holder on `[0,U]` and total mass one on `[U,infinity)` give

`int_0^infinity p_R0(t-u)u^(-1/2)du
 <= ||p_R0||_p (1-s/2)^(-1/s) U^(1/s-1/2) + U^(-1/2).`                 (5.2)

Take

`U=||p_R0||_p^(-s)`.                                                   (5.3)

Then

`sup_t int_0^infinity p_R0(t-u)u^(-1/2)du
 <= A_epsilon ||p_R0||_p^(s/2)`,                                     (5.4)

where

`A_epsilon := (epsilon/2)^(-1/(2-epsilon))+1`,                         (5.5)

because `1-s/2=epsilon/2`.

Raise (4.8) to the power `s/2` and insert (4.6). After cancellation of the Fourier `2pi` factor one obtains

`||p_Q||_infinity
 <= C_epsilon / sqrt(|a| gamma)`,                                     (5.6)

with the completely explicit constant

`boxed(
 C_epsilon
 = [(epsilon/2)^(-1/(2-epsilon))+1]
   * (2-epsilon)/(sqrt(2) epsilon)
   * [(4+2sqrt(3)) e/(epsilon(1-epsilon))]^(1/4).
 )`                                                                    (5.7)

No independence between `R_0` and the translated square variable was introduced; (5.1) is precisely the dependence-safe ingredient supplied by the account04 theorem.

## 6. Main theorem and a concrete 31/32 collar

### Theorem 6.1 — `QFORM-TRANSVERSE-ARBITRARY-COLLAR-RIDGE-CLOSURE-v1`

In the shear-invariant B08 transverse setup described in Section 0, assume an original physical scalar pivot `a!=0`. For every fixed `0<epsilon<=1/2`, define

`g_epsilon=gamma sqrt(epsilon/(4+2sqrt(3)))`.                          (6.1)

If

`max_i (K_(g_epsilon)(H))_ii <=1-epsilon`,                             (6.2)

then the full ambient quadratic form has an absolutely continuous law and

`boxed(||p_Q||_infinity <= C_epsilon / sqrt(|a| gamma))`,              (6.3)

where `C_epsilon` is given by (5.7). All same-side residual quadratic terms, arbitrary signs, outside couplings and additional spectral components already present in the residual branch are retained through the ridge estimate. The proof does **not** establish continuity of the resulting density.

This is a genuine strengthening of the fixed `5/6` gate: the collar can be pushed arbitrarily close to one while retaining a dimension-free finite constant for each fixed `epsilon`.

### Explicit useful choice

Take

`epsilon=1/32`.                                                        (6.4)

Then

`g_(1/32)=gamma / sqrt(32(4+2sqrt(3)))`,

and every branch satisfying

`max_i (K_(g_(1/32))(H))_ii <=31/32`                                   (6.5)

obeys

`C_(1/32)=2100.805325477... <2101`.                                   (6.6)

Hence

`boxed(||p_Q||_infinity <2101/sqrt(|a| gamma)).`                       (6.7)

For comparison, selected values of the explicit family are

`epsilon=1/6   -> leverage 5/6,   C_epsilon<132`,
`epsilon=1/8   -> leverage 7/8,   C_epsilon<211`,
`epsilon=1/16  -> leverage 15/16, C_epsilon<661`,
`epsilon=1/32  -> leverage 31/32, C_epsilon<2101`.

The earlier optimized B08 proof has a better constant (`<97`) at its special `5/6` point; the value of Theorem 6.1 is the **arbitrary near-one collar**, not constant optimization.

## 7. What failure now means

Fix any quantitative O0 subbranch on which `|a| gamma` already has a universal positive lower bound. For a chosen collar, say `epsilon=1/32`, Theorem 6.1 pays the branch unless an actual original physical residual row has ridge leverage exceeding `31/32` at the explicit small scale (6.4). Thus a survivor is no longer merely `>5/6`-heavy: it is forced into a quantitatively near-coloop geometry.

More generally, because the theorem is valid for every fixed `epsilon`, future structural work may choose a collar matched to a deletion/nested-heavy argument. The mechanism is stable under arbitrary Schur shear because the only spectral premise used before the ridge estimate is the shear-invariant transverse `e_2` reserve (0.1).

The exact next implication is therefore

`QFORM-TRANSVERSE-NEAR-COLOOP-PAYMENT-v1`:

> in the surviving O0 scalar-pivot branch, convert a row with residual ridge leverage `>1-epsilon` at `g_epsilon` into either a paid physical indefinite pair (to which the arbitrary-rank pair-log theorem applies), a second independent bank/ridge direction after deletion, or a product-preserving grouped-coordinate smoother, with constants uniform for one fixed epsilon such as `1/32`.

This is narrower than the previous `5/6` debt and does not invoke the refuted scalar-conditioning or conditional-projection moment routes.

## 8. Relation to the fresh finite-direction grouping theorem

A concurrent account01/B06 result, `QFORM-RANK3-FINITE-DIRECTION-GROUPING-v1`, canonical commit `0410d4dbac5e8406438a81bc9541f8d79c64a8da`, independently establishes the complementary principle **group before curvature** for exact-rank-three frames with finitely many spectral row directions. It first aggregates disjoint original-coordinate groups using the weighted affine-fiber Brascamp--Lieb theorem and only then pays a three-variable curved block. The present result handles a different side of the same obstruction: when the cross geometry is not finitely grouped but carries a shear-invariant transverse `e_2` reserve, it turns that aggregate curvature into an arbitrarily tight ridge-leverage collar before square smoothing.

These mechanisms are compatible, but neither currently supplies the missing exhaustive decomposition for arbitrary full-rank `A`.

## 9. Integrity, failed routes preserved, and status

This run does not promote a supporting branch to the full theorem. The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The following known failures remain active constraints:

- law-uniform pointwise van-der-Corput/Fresnel decay is false;
- arbitrary-joint rank-three coarea from only a joint-density cap is false;
- fixed positive moments of worst conditional spectral projection densities can diverge;
- unrestricted fiber-sup integration can grow with ambient dimension;
- a generic bounded projection/X-ray density does not by itself control an indefinite quadratic pushforward;
- direct averaging of already-inverted tiny physical-minor certificates can fail on delocalized Hadamard/Pluecker examples.

The new theorem uses an aggregate `e_2` bank, a ridge characteristic-function inequality valid with arbitrary self phases, and the dependence-safe original-coordinate square kernel. It therefore preserves the product provenance demanded by the current correction ledger.

### Claim status

- `QFORM-E2-TO-ARBITRARY-COLLAR-RIDGE-v1`: **PROVED IN THIS SOURCE**.
- `QFORM-TRANSVERSE-ARBITRARY-COLLAR-RIDGE-CLOSURE-v1`: **PROVED IN THIS SOURCE**, conditional on the already-proved B08 transverse-reserve setup and the stated nonzero physical pivot.
- `QFORM-TRANSVERSE-31/32-COLLAR-v1`: **PROVED IN THIS SOURCE**, explicit corollary.
- Full QFORM: **OPEN**.
- Full continuity statement: **OPEN**; the new `L^p`-plus-square branch proves essential boundedness, not a continuous representative.

A deterministic checker beside this report verifies the exact parameter arithmetic and finite-grid sanity instances. It is not used as a universal proof certificate.
