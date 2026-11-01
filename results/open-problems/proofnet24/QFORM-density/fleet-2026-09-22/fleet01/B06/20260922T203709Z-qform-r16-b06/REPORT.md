SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B06, 2026-09-22T20:37:09Z.
attacking: the final near-rank-two curved-fiber survivor by converting the near-coloop area budget plus the deleted-row tube into a quantitatively well-conditioned rank-two cross core before any reciprocal-minor payment.

# fleet01/B06 QFORM r16 — bicolooop area forces a strong rank-two cross core

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Run:** `20260922T203709Z-qform-r16-b06`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Continuity:** not proved here; only supporting structure for the essential-boundedness argument.

## 1. Exact scope and source state

The sole target remains the unrestricted statement: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a probability density with one dimension/law/matrix-independent essential `L^infinity` bound, or give a target-valid counterexample. No moment, compact-support, centering, log-concavity, connected-support, diagonal-basis, or post-rotation independence assumption is made.

The fresh control observed owner revision `2026-09-22.15` and QFORM as the sole research target. The live corrections excluding law-uniform pointwise quadratic-phase decay, unrestricted fiber suprema, arbitrary-joint coarea, positive worst-conditional projection-density moments, and fixed-good-minor reductions remain in force.

This run consumes two completed results at actual inequalities:

1. **Assigned partner fleet02/B06** — `QFORM-NEAR-COLOOP-RIDGE-AREA-BUDGET-v1`, canonical mathematics `yspennstate/math-open-problems@baf159fa655efe4d683c6d1e33a233d088f0db64`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T193018Z-76cbee5f2059/REPORT.md`. For

   `K=H(H^T H+g^2 I)^(-1)H^T`,

   every row `j` satisfies

   `sum_(k!=j) det K[{j,k}] = K_jj tr K-(K^2)_jj >= K_jj(tr K-1)`.      (1.1)

2. **Latest complete fleet03/B06 curved-fiber state** — `QFORM-ONE-ROW-E2-HYBRID-L3-v1`, canonical mathematics `yspennstate/math-open-problems@897d37adecb8f18c46b456569884b2ee22eeb3ee`, correction bundle `fc92e85ebc8099f25a9770d81348d74d5d2aa4d5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T201841Z-fleet03-B06-qform-r18/REPORT.md`. In the live B08 near-coloop state at `g=gamma/16`, after normalizing

   `Z=H(g^2 I+H^T H)^(-1/2)`,

   its paid branch is `E_2(Z_0)>=1/64`, where `Z_0` deletes the near-coloop row. In the only remaining branch `E_2(Z_0)<1/64`, r18 proves

   `256/129 <= ||Z||_F^2 < 201/100`,                                 (1.2)
   `||z_j||^2>99/100`,                                                (1.3)

   and, writing the singular values of `Z_0` as `s_1>=s_2>=...`,

   `sum_(p>=2) s_p^2 < 129/4064`.                                    (1.4)

Thus the first genuine missing implication is the stability of the already-paid exact-rank-two cross mechanism under the small but nonzero normalized remainder in (1.4). The theorem below sharpens that survivor substantially.

## 2. Compact conditional end-to-end route

The current nonzero physical-pivot proof tree is:

- the ridge/integrable branches are already paid;
- the two-sided high-leverage survivor supplies a left near-coloop row and a right near-coloop column;
- fleet03/B06 r18 pays the branch where the deleted-row second exterior energy is at least `1/64`;
- therefore only (1.2)--(1.4) remains;
- if that survivor can be reduced to a quantitatively stable rank-two cross-bank `L^3` estimate, the completed dependence-safe original-coordinate square kernel finishes the physical-pivot branch.

The first required step is therefore not another local minor. It is to show that the r18 tube contains a **uniformly nondegenerate rank-two core**. This is what is proved next.

## 3. New theorem — `QFORM-BICOLOOP-STRONG-RANK2-TUBE-v1`

Assume `Z` is the normalized cross block in the r18 survivor, so (1.2)--(1.4) hold. Let its singular values be

`zeta_1>=zeta_2>=zeta_3>=...>=0`,

and let `h_1>=h_2>=...` be the singular values of the unregularized cross block `H`. Put

`delta := 129/4064`,
`B0 := 4191/4300`,
`L0 := B0-(201/100)delta-delta^2/2
    = 32326017789/35509606400
    >0.9103457082`.                                                    (3.1)

Then:

**(a) strong normalized rank-two core**

`zeta_1^2 zeta_2^2 > L0`, and in particular

`zeta_2^2 > L0`.                                                       (3.2)

**(b) dimension-free normalized rank-two tail**

`sum_(p>=3) zeta_p^2 < delta`.                                        (3.3)

**(c) strong actual cross singular value**

Because `zeta_p^2=h_p^2/(g^2+h_p^2)`,

`h_2^2/g^2 > L0/(1-L0)
 = 32326017789/3183588611
 >10.15395572`,                                                        (3.4)

so

`h_2 >3.18652721 g =0.19915795 gamma`.                                (3.5)

**(d) small actual cross tail relative to the core**

`sum_(p>=3) h_p^2 < [delta/(1-delta)] g^2
                    = (129/3935) g^2`,                               (3.6)

and hence

`(sum_(p>=3)h_p^2)^(1/2) <0.18105999 g
                         <0.05682048 h_2`.                            (3.7)

Thus every r18 unpaid survivor is not merely “near rank two”: its top two cross singular directions are uniformly nondegenerate while the entire remaining cross bank has Frobenius norm below `5.683%` of the second singular value.

### Proof

Set

`K=ZZ^T=H(H^T H+g^2I)^(-1)H^T`.

By the assigned partner's identity (1.1), the near-coloop row `j` satisfies

`A_j := sum_(k!=j) det K[{j,k}]
    >= K_jj(tr K-1)`.

Using `K_jj>99/100` and `tr K>=256/129`,

`A_j > (99/100)(127/129)=4191/4300=B0`.                               (3.8)

This is an actual application of the named partner theorem. Each determinant in `A_j` is the squared area of the corresponding pair of physical rows of `Z`; therefore `A_j` is a sub-sum of the total second exterior energy

`E_2(Z)=sum_(p<q) zeta_p^2 zeta_q^2`.

Hence

`E_2(Z)>B0`.                                                          (3.9)

Now let `Z_0` be `Z` with row `j` deleted. Keep row `j` exactly and replace `Z_0` by its best rank-one approximation. This produces a matrix of rank at most two whose squared Frobenius error is exactly `sum_(p>=2)s_p(Z_0)^2`, which is `<delta` by r18. By Eckart--Young,

`tau := sum_(p>=3) zeta_p^2 <delta`,                                  (3.10)

proving (3.3).

Write `a=zeta_1^2`, `b=zeta_2^2`. Then

`E_2(Z)=ab+(a+b)tau+E_2(zeta_3^2,zeta_4^2,...)`.

Since `a+b<=||Z||_F^2<201/100` and, for nonnegative numbers of total mass `tau`, their second elementary symmetric sum is at most `tau^2/2`,

`E_2(Z) <= ab +(201/100)tau+tau^2/2`.

Combining this with (3.9), `tau<delta`, and monotonicity of the right-hand error term gives

`ab > B0-(201/100)delta-delta^2/2=L0`.                                (3.11)

All singular values of `Z` are strictly below one, because `zeta=h/sqrt(g^2+h^2)` with `g>0`. Thus `a<1`, so (3.11) implies `b>L0`, proving (3.2).

The relation `b=h_2^2/(g^2+h_2^2)` is equivalent to

`h_2^2/g^2=b/(1-b)>L0/(1-L0)`,

which is (3.4)--(3.5).

Finally, for `p>=3`, `zeta_p^2<=tau<delta`; hence

`h_p^2/g^2 = zeta_p^2/(1-zeta_p^2)
           <= zeta_p^2/(1-delta)`.

Summing and using (3.10),

`sum_(p>=3)h_p^2/g^2 <delta/(1-delta)=129/3935`,

which proves (3.6). Dividing its square root by the lower bound in (3.4) gives

`||H-H_2||_F/h_2
 < sqrt[(129/3935)/(L0/(1-L0))]
 <0.05682048`,

where `H_2` is the best rank-two truncation. QED.

## 4. A second direct use of the partner's grouped-fiber theorem

Let `H_2=R diag(h_1,h_2) S^T` be the rank-two core from Theorem 3, with `R,S` having orthonormal columns on the two disjoint original-coordinate banks. For the **core bilinear form**

`T_core=2(R^T X)^T diag(h_1,h_2)(S^T Y)+alpha^T(R^T X)+beta^T(S^T Y)+c`,

the assigned partner's completed `QFORM-WEIGHTED-HYPERBOLIC-TWO-BANK-v1` gives

`||p_(T_core)||_infinity <= e sqrt(2pi)/h_2
                           < [16 e sqrt(2pi)/3.18652721] gamma^(-1)
                           <34.213/gamma`.                             (4.1)

This is not asserted for the live full residual: its arbitrary within-bank quadratic terms and the nonzero cross tail must still be retained. Rather, (4.1) quantifies exactly how much smoothing is already present in the dominant grouped cross core before that remaining dependence-safe stability problem is paid.

The stronger exact-rank-two arbitrary-self-block theorem of fleet03/B06 r17 already pays the case `H-H_2=0`. Theorem 3 above shows the only r18 survivor has a tail less than `5.683%` of the second core singular value, giving a precise stability regime instead of an unspecified “near rank two” condition.

## 5. What this does and does not prove

This run proves a new dimension-free structural consequence in the first unpaid curved-fiber branch:

`r18 near-coloop survivor  =>  strong rank-two core + <=5.683% relative cross tail`.

It uses the assigned fleet02/B06 area-budget theorem at the decisive inequality (3.8), rather than merely citing it. It also explains why selecting one physical pair is unnecessary: the core is a **grouped** rank-two object.

It does **not** justify dropping the tail. Under the target assumptions the input laws may have arbitrarily fragmented and remote support and no moments, so coefficient-smallness is not by itself a probabilistic perturbation parameter. Any stability proof must retain the tail inside a product-preserving Fourier/coarea estimate, or turn it into a second paid curvature mechanism.

The next exact implication is therefore

`QFORM-STRONG-RANK2-TAIL-STABILITY-v1`:

> For a disjoint-bank quadratic form with arbitrary within-bank quadratic/affine terms and cross block `H=H_2+E`, prove a universal `L^3` (or directly square-smoothing) bound whenever `rank(H_2)=2`, `sigma_2(H_2)>=c gamma`, and `||E||_F<=0.057 sigma_2(H_2)`, **without moments or support assumptions**; or convert `E` into an already-paid second-curvature/ridge branch.

The constants furnished by this run are `c=0.19915` in the live normalization and relative tail `<0.056821`.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. The separate continuous-density conclusion remains open.
