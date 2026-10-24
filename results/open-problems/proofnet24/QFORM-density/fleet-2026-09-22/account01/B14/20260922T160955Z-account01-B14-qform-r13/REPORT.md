# account01/B14 — arbitrary-cycle-offset three-gap localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Control source:** `yspennstate/math-research-brain@d6c698fc290c365a92173e8d0c7effabac9e78d2`  
**Run:** `20260922T160955Z-account01-B14-qform-r13`  
**Assignment:** translations and localization  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_THEOREM / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and partner dependency

The full owner target remains open: for every dimension, every independent real coordinates with probability densities bounded by one, and every symmetric matrix having at least three eigenvalues of absolute value at least one, prove a universal density bound for `X^T A X`, or construct a valid counterexample.

This run consumes the completed partner theorem

- `yspennstate/math-open-problems@3f241388d9bcacf1379ef8ef640b35d7d14aad91`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T150227Z-b14-qform-localization-r14/REPORT.md`.

That theorem proves, for independent cap-one `X_1,X_2,X_3`, cycle-consistent shifted pair gaps and exponents `a,b,c<1`, `a+b+c<2`, a uniform inverse-gap moment bound. In the symmetric square-root case the constant is `61+12*pi < 98.70`. It also proves that total pair-gap exponent `2` is the sharp obstruction for this raw absolute compiler.

The remaining localization issue is that sequential completion of squares or root extraction can produce three pair-gap centers with an **incompatible cycle defect**: the three edge offsets need not equal `tau_i-tau_j` for any three vertex shifts. The partner theorem does not directly cover that case.

This report proves that arbitrary edge offsets are still harmless throughout the same sharp subcritical exponent range. Thus the pair-gap compiler does not require cycle consistency.

## 2. Main theorem: arbitrary edge offsets

Let `X_1,X_2,X_3` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1` and `int f_i=1`. Let

`alpha_12, alpha_23, alpha_31 in [0,1)`

and put

`s = alpha_12 + alpha_23 + alpha_31 < 2`.

For arbitrary real offsets `d_12,d_23,d_31`, define

`R = |X_1-X_2-d_12|^{-alpha_12}`
`    |X_2-X_3-d_23|^{-alpha_23}`
`    |X_3-X_1-d_31|^{-alpha_31}`.

Then

`E R <= C_off(alpha_12,alpha_23,alpha_31) < infinity`,

uniformly over all three offsets and all admissible laws.

An explicit constant is as follows. For the three edges `e`, write `alpha_e` for the corresponding exponent and set

`q_e = alpha_e + ((2-s)/(3-s)) (1-alpha_e)`.

Then

`alpha_e < q_e < 1`, `sum_e q_e = 2`.

Define

`A_e = 2/(1-alpha_e)`,

`T_e = [ 2 q_e/(q_e-alpha_e) ]^{q_e}`.

Then one may take

`C_off = 1 + sum_e A_e + sum_{e<e'} A_e A_e' + prod_e T_e`.      (2.1)

In particular, for three square-root gaps,

`alpha_12=alpha_23=alpha_31=1/2`,

we have `q_e=2/3`, `A_e=4`, `T_e=4`, and therefore

`E prod_cyc |X_i-X_j-d_ij|^{-1/2} <= 1+12+48+64 = 125`.          (2.2)

No support radius, moments, fragment count, connectedness, centering, or cycle-consistency relation among the offsets is assumed.

## 3. Proof

For `0<=alpha<1` define the truncated kernel

`k_alpha(u)=|u|^{-alpha} 1_{|u|<=1}`.

For every `r>0`,

`r^{-alpha} <= 1 + k_alpha(r)`.                                  (3.1)

Expanding the product of the three factors reduces the expectation to the empty term, three one-edge terms, three two-edge terms, and one three-edge term.

### 3.1 One-edge terms

Fix an edge, say `(1,2)`, with offset `d`. Conditional on `X_1=x`,

`int k_alpha(x-y-d) f_2(y) dy`
` <= int_{|u|<=1} |u|^{-alpha} du`
` = 2/(1-alpha)=A_e`.                                            (3.2)

This is uniform in `x,d`, hence the one-edge contribution is at most `A_e`.

### 3.2 Two-edge terms

Any two edges of a triangle share one vertex. For example, conditioning on `X_2=y`, independence of `X_1,X_3` gives

`E[k_a(X_1-X_2-d_12) k_b(X_2-X_3-d_23) | X_2=y]`
` <= A_12 A_23`.                                                 (3.3)

The other two pairs are identical after relabeling. This yields the pairwise terms in (2.1).

### 3.3 Three-edge term and the cycle defect

Orient the three edge expressions as

`u = x_1-x_2-d_12`,
`v = x_2-x_3-d_23`.

Then

`x_3-x_1-d_31 = -(u+v+Delta)`,

where the entire incompatibility of the three offsets is the scalar cycle defect

`Delta = d_12+d_23+d_31`.                                       (3.4)

Use `(t,u,v)` as coordinates, with `t=x_2`; the Jacobian is one. For fixed `u,v`, the integral over `t` of the three density factors is at most one, because the pointwise product is at most any one factor and each translated factor integrates to one. Therefore the full three-edge term is at most

`I_Delta = int_R int_R k_a(u) k_b(v) k_c(u+v+Delta) du dv`.       (3.5)

Thus

`I_Delta <= ||k_a * k_b * k_c||_infinity`.                       (3.6)

Choose `p_e=1/q_e`. Since `sum q_e=2`,

`1/p_12 + 1/p_23 + 1/p_31 = 2`.                                 (3.7)

Also `alpha_e p_e = alpha_e/q_e <1`, so `k_alpha_e in L^{p_e}` and

`||k_alpha_e||_{p_e}`
` = [ int_{-1}^1 |u|^{-alpha_e p_e} du ]^{1/p_e}`
` = [ 2/(1-alpha_e/q_e) ]^{q_e}`
` = [ 2q_e/(q_e-alpha_e) ]^{q_e}`
` = T_e`.                                                        (3.8)

Generalized Young convolution inequality on `R`, applied twice, gives

`||k_a*k_b*k_c||_infinity <= T_12 T_23 T_31`.                   (3.9)

This bound is independent of `Delta`, hence of all three edge offsets. Combining (3.1)--(3.9) proves (2.1).

For `a=b=c=1/2`, take `p_e=3/2`. Then

`||k_{1/2}||_{3/2}`
` = [2/(1-3/4)]^{2/3}=8^{2/3}=4`,

so the three-edge term is at most `64`, and (2.2) follows.

## 4. Partner theorem applied, not merely cited

When the offsets are cycle-consistent, i.e.

`d_12=tau_1-tau_2`, `d_23=tau_2-tau_3`, `d_31=tau_3-tau_1`,

we have `Delta=0`. In that branch the exact account02/B14 theorem applies directly and improves the square-root constant from `125` to

`61+12*pi < 98.70`.                                               (4.1)

The new theorem is needed only for the genuinely incompatible branch `Delta != 0`, where no three vertex shifts can absorb all edge centers simultaneously.

Thus a deterministic-outside shell estimate may now be compiled as follows:

- cycle-consistent shifted square-root gaps: use partner constant `61+12*pi`;
- arbitrary independently generated edge centers: use the new constant `125`.

This is an actual extension of the partner interface rather than a duplicate proof of its special case.

## 5. Deterministic-outside localization compiler

Let `S={i,j,k}` be an original-coordinate active triple, selected before localizing the complement. Suppose that for every deterministic outside vector `z`, every interval `J`, and the actual independent cap-one laws on the three active coordinates, a source-valid shell/coarea argument proves

`P{Q_A(X_S,z) in J | z}`
` <= K |J| E_S prod_{r<s in S}`
`    |X_r-X_s-d_rs(z)|^{-theta_rs}`,                             (5.1)

where each `theta_rs<1` and their sum is `<2`. The offsets `d_rs(z)` may be arbitrary measurable functions of `z`; no cocycle condition is required.

Then the theorem gives, pointwise in every outside vector,

`P{Q_A(X_S,z) in J | z}`
` <= K C_off(theta) |J|`.                                       (5.2)

Integrating the actual outside product law yields

`P{X^T A X in J} <= K C_off(theta)|J|`.                          (5.3)

Hence arbitrary outside shifts, distant fragments and unbounded supports incur **zero additional localization loss** once the active shell singularities are represented by three subcritical pair gaps, even if their edge centers are mutually incompatible.

For the shell-relevant square-root case, (5.3) holds with the explicit factor `125`, and with `61+12*pi` whenever the three offsets are cycle-consistent.

## 6. Sharpness of the exponent threshold

The new offset freedom does not change the sharp threshold. The partner report already supplies a target-valid cap-one witness at zero offsets: iid `Uniform[0,1]` gives divergence of the raw three-gap moment when the total exponent is `>=2` (logarithmic at equality, power above). Since zero offsets are a special case of arbitrary offsets, no uniform arbitrary-offset compiler can extend beyond total exponent `<2` without using additional cancellation or structure.

Thus the new result enlarges the **translation geometry** of the safe region, not the exponent region.

## 7. What changed and what remains unpaid

**Old unpaid localization implication.** A useful active-triple shell estimate had to preserve the singular factors as differences of three individually shifted coordinates, because the available partner theorem required cycle-consistent pair-gap centers.

**New proved implication.** Cycle consistency is unnecessary. Any three arbitrary edge-center functions are admissible with the same sharp power-counting condition `theta_e<1`, `sum theta_e<2`; for three square-root factors the universal localization cost is at most `125`.

This materially loosens the deterministic-outside shell target for the heavy/localized branch: sequential completion of squares may generate distinct root centers on each edge without first proving they arise from a common triple of vertex translations.

**Still unpaid.** Derive such a deterministic-outside quadratic shell/coarea estimate from the remaining heavy/localized matrix geometry, with total pair-gap exponent below two. This report does not prove that every three-large-eigenvalue matrix admits that representation, and therefore does not prove the full QFORM conjecture.

## 8. Correction closure

Fresh source corrections consumed before publication include:

- `QFORM-CROSSMINOR-ALONE-FALSE`;
- `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`;
- `QFORM-TWOSHEET-XRAY-ONLY-FALSE`;
- `QFORM-UV-CONDITIONAL-CAP-FALSE`;
- `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`;
- `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`;
- `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`;
- `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`;
- `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`;
- `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`;
- `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`;
- `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`;
- `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`.

No refuted pointwise Fourier decay, post-rotation independence, fiberwise trace cap, bounded-diameter reduction, fixed fragment-count reduction, or cross-minor-only implication is used.

The full conjecture remains OPEN.
