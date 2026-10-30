SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T02:19:03Z.
attacking: admissible fractional-volume reweighting versus intrinsic ridge certificates on the same physical cross block, with an explicit rotated indefinite stress family.

# fleet02/B04 — an exact three-volume coloop can make every admissible volume weighting impossible while square-assisted ridge stays uniformly strong

Programme: `QFORM-DENSITY-3EIG-20260922`. Run: `20260923T021903Z-fleet02-B04-QFORM-r11`. Assignment: Product Fourier rearrangement. Outcome: `ESSENTIAL_STEP_APPLIED / SOURCE-VALID OBSTRUCTION / EXPLICIT TARGET-VALID ESTIMATE / FULL QFORM OPEN`. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The unrestricted target remains OPEN. The first B04 debt is structural rather than a new Fourier integral: under only `s_3(A)>=1`, compile physical original-coordinate geometry into either an admissible aggregate volume certificate, a regularized ridge certificate enhanced by a genuine original scalar square, or an already-paid grouped/hub mechanism, without paying a vanishing local minor.

The preceding B04 run showed that raw `q=1` three-volume sampling can fail only slightly while finite-KL reweighting repairs it and a ridge certificate is stronger. This run changes mechanism to the opposite extreme: an **exact three-volume coloop**. On the family below the total third volume is positive, but every nonzero three-minor uses one weak physical row. Hence every probability weight supported on nonzero three-minors has that row marginal exactly one. The admissible fractional-volume polytope is empty and its KL repair cost is `+infinity`. Nevertheless a square-assisted one-scale ridge certificate is uniform as the weak singular value tends to zero.

Thus the correct structural currency cannot be "finite-KL admissible third volume OR failure". Near-coloops must be routed either through regularization plus another genuine smoothing factor or through grouped low-rank/hub mechanisms.

No moment, support, log-concavity, diagonal-basis, arbitrary-joint coarea, conditional spectral-density cap, post-rotation independence, or law-uniform pointwise quadratic-phase decay is used.

## 2. Source-pinned completed inputs actually applied

1. Claude Fourier package at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, especially `RESULTS.md` and `FOURIER_ROUTE_REPORT.md`. The audited Theorem D allows **arbitrary probability weights on nonzero physical 3x3 minors**: if their row marginals obey the required cap, weighted AM-GM replaces the Gibbs third volume by

   `G(w)=exp(E_w log det(M_ST)^2 + H(w))`.

   This source is applied in Section 4 to prove an actual obstruction: for the matrix constructed here every nonzero three-minor contains the same row, so every such weight has marginal one and the theorem's admissibility gate is impossible.

2. The preceding B04 weighted sharp extension, `QFORM-WEIGHTED-FRACTIONAL-VOLUME-SHARP-v1`, source report `yspennstate/math-open-problems@061327b7e45c28e5b8c898ed3729456fcea6f7d7`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T014717Z-fleet02-B04-QFORM-auto11-cont/REPORT.md`. For `1<=q<3/2`, it requires `alpha_i<=q/2<3/4`. The same exact coloop therefore blocks not only `q=1` but every exponent in the theorem's admissible range.

3. Square-assisted ridge theorem `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1`, source `yspennstate/math-open-problems@b129377880c18fe011dd4513282f2e0b60e412e0`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T155815Z-qform-r11b/REPORT.md`. If

   `Q=a(Z+m(Y))^2+R(Y)`,

   `K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta=tr K_gamma`, `D=det(I+BB^T/gamma^2)`,

   and for `1<=q<=2`, `max_i(K_gamma)_ii<=q/2`, `theta>4q/3`, then

   `||p_Q||_inf <= 8*3^(-5/8)*sqrt(e)*q^(-1/4)*sqrt(3theta/(3theta-4q))*D^(-1/(4theta))/sqrt(|a|gamma)`.

4. Latest completed designated-partner result fleet03/B04 r22, source `yspennstate/math-open-problems@406753a39f5fbaf78396b31075f36ae5682ef3ad`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260923T015102Z-r22/REPORT.md`. Its `QFORM-FINITE-BANK-PLANCHEREL-v1` says that for an original three-coordinate bank and arbitrary quadratic leakage on both sides, a full-column-rank physical cross block with singular values `sigma_1,sigma_2,sigma_3` gives

   `||p_Q||_inf <= 3sqrt(e)(sigma_1 sigma_2 sigma_3)^(-1/3)`.

   Section 7 applies this theorem to the exact same matrix, making the comparison equation-level rather than bibliographic.

All cited positive results preserve original-coordinate product provenance. The live corrections that arbitrary-joint coarea, positive conditional-projection-density moments, uniformly good local minors, and post-rotation independence are false are respected.

## 3. A five-by-three rotated cross block with a weak exact coloop

Let `U` be the `5 x 3` matrix with rows

`u_1=(1,0,0)`,

`u_2=(0,1/sqrt(2),0)`,

`u_3=(0,1/2,1/2)`,

`u_4=(0,0,1/sqrt(2))`,

`u_5=(0,-1/2,1/2)`.

The last four rows form a tight frame for the last two coordinate directions, and a direct calculation gives

`U^T U=I_3`.                                                     (3.1)

Take the exact rational orthogonal matrix

`V=[[-2/3,  2/15, 11/15],
    [ 2/3, -1/3,   2/3 ],
    [ 1/3, 14/15,  2/15]]`,                                    (3.2)

for which `V^T V=I_3`, `det V=1`. For `0<epsilon<=1/4`, define

`M_epsilon=U diag(epsilon,2,2) V^T`.                             (3.3)

Its singular values are exactly

`2, 2, epsilon`.                                                (3.4)

In physical original coordinates,

`M_epsilon =`

`[ -2epsilon/3,      2epsilon/3,       epsilon/3 ]`
`[  2sqrt(2)/15,    -sqrt(2)/3,       14sqrt(2)/15 ]`
`[ 13/15,            1/3,              16/15 ]`
`[ 11sqrt(2)/15,     2sqrt(2)/3,        2sqrt(2)/15 ]`
`[  3/5,             1,                -4/5 ]`.                  (3.5)

Every one of its fifteen physical entries is nonzero for `epsilon>0`, so the example is not a diagonal-coordinate disguise.

The third elementary symmetric volume is nevertheless positive:

`E_3=e_3(M_epsilon^T M_epsilon)=16 epsilon^2`.                   (3.6)

## 4. Exact obstruction: every nonzero three-volume weight has marginal one

Delete physical row 1 from `M_epsilon`. By construction rows 2--5 have zero component in the first left singular direction. Hence

`rank M_epsilon[{2,3,4,5},:]=2`.                                (4.1)

Therefore every nonzero `3 x 3` minor of `M_epsilon` must contain physical row 1. Conversely the last four row vectors in their two-dimensional plane have no parallel pair, so every minor consisting of row 1 plus two of rows 2--5 is nonzero. Thus the support of the third-volume matroid has six bases and **row 1 is a coloop**.

Let `w` be any probability distribution supported on nonzero `3 x 3` minors. Its row inclusion marginal satisfies exactly

`alpha_1=P_w(1 in S)=1`.                                        (4.2)

Consequences:

* e5 Theorem D cannot apply for any choice of admissible weights, because it requires `alpha_i<=1/2`;
* the fractional weighted theorem cannot apply for any `1<=q<3/2`, because `q/2<3/4<1`;
* the relaxed canonical D' threshold `h<3/4` likewise cannot help.

This is stronger than merely saying the Gibbs weight is badly balanced: **the entire nonzero-minor admissible polytope is empty**.

The KL formulation makes the obstruction exact. Let `w_*` be the squared-minor Gibbs law. Since row 1 occurs in every point of its support,

`P_{w_*}(1 in S)=1`.                                             (4.3)

Any law satisfying `P_w(1 in S)<1` assigns positive mass outside that support and therefore has

`KL(w||w_*)=+infinity`.                                         (4.4)

Equivalently, if one permits weights on zero minors in the entropy formula, any such repaired law has `G(w)=0` because `E_w log det^2=-infinity`.

So the previous finite-KL repair mechanism has an exact, target-valid boundary: positive `E_3` does **not** imply any finite-KL route to admissible three-volume weights.

This is a source-valid counterexample to the intermediate statement "every positive third volume can be made admissible at finite entropy cost". It is not a counterexample to QFORM.

## 5. Embed the obstruction in a genuinely rotated indefinite target matrix

Let `Z` be one original coordinate, `X in R^5` and `Y in R^3` the remaining mutually independent original-coordinate banks. Define

`Q_epsilon = Z^2 + 2 X^T M_epsilon Y`.                           (5.1)

The physical symmetric matrix is

`A_epsilon = diag(1, [[0,M_epsilon],[M_epsilon^T,0]])`.          (5.2)

Because the cross block has singular values `(2,2,epsilon)`, the spectrum is exactly

`{-2,-2,-epsilon,0,0,epsilon,1,2,2}`.                           (5.3)

Hence for every `0<epsilon<=1/4` the matrix is indefinite and has five eigenvalues of modulus at least one. It lies strictly inside the full target. All cross entries in (3.5) are nonzero and the left/right singular bases are rotated relative to the independent coordinates.

## 6. Same physical matrix: square-assisted ridge is uniform

Use the outer original coordinate `Z` as the genuine square in the square-assisted theorem, so `a=1`, `m=0`, and the residual is `R=2X^T M_epsilon Y`. Choose

`q=1`, `gamma=1/4`.                                              (6.1)

Set

`k_epsilon=epsilon^2/(1/16+epsilon^2)`.                          (6.2)

Since each strong singular value equals two, its ridge eigenvalue at this scale is

`4/(4+1/16)=64/65`.                                              (6.3)

Therefore

`K_gamma=U diag(k_epsilon,64/65,64/65) U^T`.                    (6.4)

Its physical row diagonals are

`(K_gamma)_11=k_epsilon`,

`(K_gamma)_ii=32/65,  i=2,3,4,5`.                               (6.5)

For `epsilon<=1/4`, `k_epsilon<=1/2`, while `32/65<1/2`; hence

`max_i(K_gamma)_ii<=1/2`.                                       (6.6)

The effective dimension is

`theta=k_epsilon+128/65 >128/65=1.969230769... >4/3`,           (6.7)

while the regularized determinant is

`D=(1+16epsilon^2) 65^2 =4225(1+16epsilon^2)`.                  (6.8)

Thus `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1` applies to every law in the target class and gives the exact family estimate

`||p_{Q_epsilon}||_inf`
` <=16*3^(-5/8)*sqrt(e)*sqrt(3theta/(3theta-4))*D^(-1/(4theta)).` (6.9)

The direct one-scale ridge `L^1` theorem at this same scale would require `theta>2`, which need not hold when `epsilon` is small. Thus the extra original square is doing genuine analytic work here rather than merely reproducing direct ridge inversion.

A uniform epsilon-independent constant follows without numerical optimization. For `0<epsilon<=1/4`,

`128/65 < theta <=128/65+1/2=321/130`.                           (6.10)

The ratio `3theta/(3theta-4)` decreases with `theta`, hence

`3theta/(3theta-4) <=96/31`.                                    (6.11)

Also `D>=4225` and `1/(4theta)>=65/642`, so

`D^(-1/(4theta)) <=4225^(-65/642)`.                             (6.12)

Consequently

`boxed( ||p_{Q_epsilon}||_inf`
` <=16*3^(-5/8)*sqrt(e)*sqrt(96/31)*4225^(-65/642)`
` =10.032758849915808... <10.033 ).`                             (6.13)

This bound is uniform as `epsilon ->0`, even though `E_3=16epsilon^2 ->0` and every admissible three-volume KL repair has infinite cost.

At the concrete value `epsilon=10^(-6)`,

`k_epsilon=1.5999999999744e-11`,

`theta=1.9692307692467694`,

`D=4225.0000000676`,                                            (6.14)

and the sharper direct substitution in (6.9) yields

`boxed( ||p_{Q_{10^-6}}||_inf <=8.094894202563358 ).`           (6.15)

## 7. Apply the completed fleet03/B04 result to the same inequality

The partner's `QFORM-FINITE-BANK-PLANCHEREL-v1` applies with `Y` as the three-coordinate original bank. The complement bank contains `Z` and `X`; the `Z^2` term is harmless arbitrary same-side curvature in that theorem. The physical cross singular values are exactly `(2,2,epsilon)`. Hence

`||p_{Q_epsilon}||_inf <=3sqrt(e)(4epsilon)^(-1/3)`.             (7.1)

For `epsilon=10^(-6)`, this gives

`||p_{Q_{10^-6}}||_inf <=311.58879515467714...`.                (7.2)

This is a valid all-product-law inequality from the latest named partner, but it necessarily pays the weak coloop singular direction and diverges like `epsilon^(-1/3)`. By contrast, the square-assisted ridge estimate (6.13) regularizes that weak direction away, uses the two strong spread directions at scale `gamma=1/4`, and lets the independent scalar square supply the missing smoothing. On this exact physical matrix the hierarchy is therefore

`three-volume optimization: infeasible at every q<3/2`,

`partner exact-three-bank Plancherel: 311.589 at epsilon=10^-6`,

`square-assisted ridge: 8.095 at epsilon=10^-6, uniformly <10.033 for epsilon<=1/4`. (7.3)

This is the requested same-matrix comparison of volume weights and ridge-type certificates.

## 8. First unpaid implication after this run

`QFORM-NEAR-COLOOP-EXCISION-OR-SQUARE-RIDGE-ROUTING-v1`:

> Starting only from `s_3(A)>=1`, when an original-coordinate cross cut has its third-volume mass forced through one exact or quantitative near-coloop so that admissible volume reweighting has very large or infinite KL cost, prove one of the following before inverting any small minor: (i) the coloop direction is spectrally weak enough that two transverse directions plus an available original scalar square satisfy a square-assisted regularized-ridge certificate at universal scale; or (ii) the coloop is target-scale/heavy and the matrix enters a completed grouped rank-one/rank-two hub mechanism. Extend the exact-coloop calculation above to a quantitative near-coloop inequality.

The present family proves that the weak-coloop branch is not intrinsically hostile: it can have infinite volume-repair cost and yet a uniform product-space density bound. What remains is to force such a route structurally for an arbitrary target matrix, including zero/near-zero scalar pivots.

Full QFORM remains OPEN.

## 9. Finite exact/numerical checks

The companion script checks `U^T U=I`, `V^T V=I`, the singular values, row-deletion rank, all physical cross entries, target spectrum, ridge diagonals, constants, and the partner comparison. Numerical checking is only arithmetic support for the displayed exact identities; it is not the proof.
