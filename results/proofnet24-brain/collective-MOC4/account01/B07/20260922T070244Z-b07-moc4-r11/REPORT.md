# MOC4 — quantitative spinor hole around every Drury external extreme

Run: `20260922T070244Z-b07-moc4-r11`  
Worker: `account01/B07`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact inherited state used

The active owner control is revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; B07 remains on MOC4 and new installation/benchmark work is stopped.

Latest complete campaign-lead result actually read: account03/B07 run `20260922T060726Z-account03-B07-MOC4-r11`, report blob `3c11567e275d39376f217a9b9e3c10693efa3127`, theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`. It proves that at a genuine global support maximizer, saturation `T=|C|` of any Spin(4) mixed-Hessian gate moves on an exactly flat genuine coordinate `SU(2)` orbit to an equal-support unitary having a zero entry. Thus a hypothetical positive-gap maximizer lies either on the zero-entry branch or in the no-zero strict branch `T>|C|` for every left/right pair gate.

Assigned OTHER-account partner actually read and applied: account02/B08 run `B08-20260922T063644Z-ab01c7`, report blob `0c44199b655f0d726b3d0b2ace56b40dde415bcb`, theorem `MOC4-COMMON-BLOCK-EXTERNAL-FACET-COLLAR-v1`. If `f(sigma)` is the 24 endpoint support datum and `M=max f`, it uses the exact 48 Drury/Saxl external functionals

`e_{tau,rho'}(f)=(2/3)(B_{rho_tau}(f)+B_{rho'}(f))-(1/3)f(tau)`

to close every true-unitary support direction with `max_external e <= M`. Its remaining boundary branch is precisely `max_external e>M`, where a genuine spinor payment is needed.

The complete source of the phase constraint used below was also read: account04/B07 run `20260922T044421Z-account04-B07-MOC4-r12`, theorem `MOC4-SPINOR-SINGULAR-VALUE-v1`. In every even-even Spin(6) gauge, the anti-linear Bogoliubov block `N` obeys

`det N=0`,

and its squared entry moduli are the gauge-selected channels `q^+` or `q^-`, with `R=q^++q^-`, `D=q^+-q^-`. It also gives the exact gauge mass identity

`||N_{r,c}||_F^2 = 2(1-P_{iota(r),iota(c)}) <= 2`

for every genuine point.

Finally I used account03/B09 `MOC4-SAXL-EXTERNAL-FACET-CLOSURE-v1` (shared blob `5614c49e68dab63b0a7c5be62aeddcdd67ee260f`). Its exact coordinates for each non-Weyl external extreme are

`P_ext=(J-P_tau)/3`,
`D_ext=-W_tau/3`,
`R_ext=R_{rho_tau}/3 + 2 R_{rho'}/3`,

where `rho'` is one of the two pointwise derangements of `rho_tau`. It verifies that every one of the 48 external extremes has twelve even-even gauges in which exactly one determinant monomial of `N` is nonzero, with squared monomial magnitude `1/27`. Individual external extremes are therefore not genuine exterior-square points, but the prior result did not quantify their separation from the genuine locus.

## 2. New exact mixed-minor inequality

### Theorem `MOC4-EXTERNAL-SPINOR-HELLINGER-HOLE-v1`

Fix any one of the 48 normalized Drury external extremes `v_ext`, and choose any one of its twelve singleton-determinant even-even gauges. Let `q^0=(q^0_{alpha beta})` be the resulting `3 x 3` matrix of squared anti-linear moduli at that external point. Then for every genuine exterior-square point `Lambda^2 U`, with the same gauge anti-linear block `N` and squared moduli

`q_{alpha beta}=|N_{alpha beta}|^2`,

one has the uniform exact separation

`sum_{alpha,beta} (sqrt(q_{alpha beta})-sqrt(q^0_{alpha beta}))^2
   >= delta_*`,

where

`delta_*=(3-sqrt(5))/6`.

Consequently, because `(sqrt(x)-sqrt(y))^2 <= |x-y|` for nonnegative `x,y`,

`||q-q^0||_1 >= (3-sqrt(5))/6`.                                      (2.1)

This is a genuine common-unitary mixed-minor inequality. It is not a bistochastic, arbitrary `SO(6)`, or independent-compound-minor relaxation.

### Proof

By the left-right symmetry of the 48 external orbit, it is enough to inspect the canonical external point `tau=id`, `rho_tau=id`, `rho'=(123)`. Substituting its exact coordinates into the gauge-selection rule from the spinor theorem shows that in every one of the twelve singleton gauges (`iota(r) != iota(c)`), after row/column permutations the selected squared-modulus matrix is

`q^0=(1/3) [[1,1,0],[0,0,1],[1,0,0]].`                            (2.2)

Thus the support graph of the corresponding magnitude matrix is acyclic. All entry phases can therefore be removed by diagonal unitary row/column multipliers, so every complex matrix `N_0` with squared moduli `(2.2)` has the same singular values. Directly diagonalizing `N_0 N_0^*` gives squared singular values

`(3-sqrt(5))/6`, `1/3`, `(3+sqrt(5))/6`.                          (2.3)

Equivalently, the unique nonzero determinant monomial has modulus `1/(3sqrt(3))`, as in the inherited exact verifier, and the additional fourth nonzero entry produces the two golden-ratio singular values in `(2.3)`.

Now let `N` be the genuine anti-linear block in the same gauge. By `MOC4-SPINOR-SINGULAR-VALUE-v1`, `det N=0`, hence `N` is singular. Construct `N_0` with moduli `sqrt(q^0)` and, on every nonzero entry of `q^0`, choose its phase equal to the phase of the corresponding entry of `N` (arbitrary when the genuine entry is zero). Because the support graph of `(2.2)` is acyclic, this phase choice does not change `(2.3)`. Therefore

`||N-N_0||_F^2
 = sum_{alpha,beta}(sqrt(q_{alpha beta})-sqrt(q^0_{alpha beta}))^2`.

By Eckart-Young, the Frobenius distance from `N_0` to the set of singular `3 x 3` matrices is exactly its least singular value. Since `N` is singular,

`||N-N_0||_F^2 >= sigma_min(N_0)^2=(3-sqrt(5))/6`.

This proves the Hellinger bound and then `(2.1)`. The other 47 external points and their twelve singleton gauges follow by the same row/column/sign symmetries used to generate the Drury orbit. QED.

## 3. Quantitative consequence inside the 72-vertex Saxl outer hull

The account03/B09/Drury reduction places every true-unitary normalized support functional in the convex hull of the 24 Weyl evaluations and 48 external extremes. Fix an external extreme `v_0` and a singleton gauge `g` as above. In that gauge `sum q_g(v_0)=4/3`. At every one of the 72 outer vertices, the selected gauge channel is nonnegative and has total mass at most `2` (the same identity `2(1-P_ij)` holds on the exact outer coordinates). Hence

`||q_g(v)-q_g(v_0)||_1 <= 10/3`                                   (3.1)

for every outer vertex `v`.

Write an arbitrary outer decomposition of a genuine point as

`x=lambda_0 v_0 + sum_{v != v_0} lambda_v v`.

By affine dependence of the gauge masses and `(2.1)`,

`delta_* <= ||q_g(x)-q_g(v_0)||_1
          <= (10/3)(1-lambda_0)`.

Thus every convex representation of a genuine point satisfies the uniform coefficient exclusion

`lambda_0 <= 1-c_*`,

with

`c_* = (3/10) delta_* = (3-sqrt(5))/20 ~= 0.0381966011`.           (3.2)

This is the first explicit quantitative payment extracted from the inherited statement that an external extreme itself is phase-impossible.

More generally, if `v_0` is the unique maximizer among the 72 outer vertices for a given structured support functional, with value `E_0`, and `H_1` is the largest value of the other 71 vertices, then every true unitary obeys

`h(U) <= E_0 - c_* (E_0-H_1)`.                                   (3.3)

The bound `(3.3)` is still weaker than the full MOC4 endpoint bound in a generic external-deficient direction, because `H_1>=M`. It is recorded as a strict quantitative spinor payment, not as closure of the external branch.

## 4. The external-deficient branch is genuinely nonempty for actual MOC4 spectral data

A possible shortcut would be to hope that determinant-product support functions always satisfy `max_external e<=M`, making the account02/B08 certificate automatically universal. That stronger claim is false even on exact rational complex spectra.

Take

`a=(-174+93 i, 95+23 i, 44-179 i, 59+38 i)/100`,

`b=(-149+118 i, -44-104 i, 101+83 i, -78+63 i)/100`,

and the real support functional

`L(z)=Im(z)-(1/40) Re(z)`.

Exact rational evaluation of all 24 permutation products gives the unique endpoint maximum

`M = 3654300159 / 1000000000`

at `sigma=(2,1,3,0)` (zero-based permutation notation in this report). For the external functional with

`tau=(3,2,1,0)`, `rho_tau=id`, `rho'=(2,0,1)`,

one obtains

`E_0 = 2969983423 / 800000000`,

and therefore

`E_0-M = 232716479 / 4000000000 > 0`.                              (4.1)

Enumeration of the other 47 external functionals shows that this is the unique outer external maximizer; the runner-up among all other 71 outer vertices is exactly the endpoint value `M` above.

Thus the partner's `max_external e<=M` branch is not vacuous merely because the support data come from genuine complex spectra. The phase/nonlinear payment is genuinely necessary. Applying `(3.3)` to this exact datum strictly reduces the Drury outer excess by the factor `c_*`, but does not remove it completely. No true-unitary MOC4 violation is claimed or produced by `(4.1)`.

## 5. Compact conditional end-to-end argument after this run

For any support direction and spectra, let `M` be the 24-endpoint maximum.

1. If all 48 external Saxl values are at most `M`, account03/B09 plus account02/B08 closes the support inequality globally over every true unitary.
2. If an external value exceeds `M`, the new theorem shows that every genuine exterior-square point stays a fixed, exact Hellinger distance `delta_*=(3-sqrt(5))/6` from each singleton-gauge realization of that external extreme. In particular no genuine support maximizer can concentrate arbitrarily close to a bad external vertex in the complementary-minor channels.
3. Independently, at a genuine global support maximizer the campaign lead sends every saturated Spin(4) gate to an equal-gap zero-entry representative. Otherwise the maximizer lies in the strictly curved no-zero branch.
4. Therefore a target counterexample, if one exists, must survive both kinds of nonlinear structure simultaneously: it must lie in an external-deficient support direction while remaining a fixed distance from each exposed external extreme, and it must satisfy either the lead zero-face structure or every strict mixed-Hessian gate.

The exact first unpaid implication is now narrower:

`MOC4-EXTERNAL-SPINOR-SUPPORT-PAYMENT-v2` — strengthen the metric hole `(2.1)` into a support-weighted payment large enough to cover `E_0-M`, using the six-term determinant-hexagon cancellation together with the structured spectral identities for `(K,X)` (and, on a maximizing point, the lead's zero-face/strict-Spin(4) dichotomy). A mere distance from an external vertex is insufficient; equation `(4.1)` is an exact stress datum on which the finite linear outer hull itself exceeds `M`.

This is precisely the nonlinear same-unitary information missing from the Drury/Saxl outer relaxation. Full MOC4 remains open.

## 6. Verification / claim limits

- The proof of `(2.1)` is algebraic: exact external coordinates, the exact gaugewise `det N=0` theorem, a `3 x 3` singular-value computation, and Eckart-Young.
- The rational stress datum in Section 4 was evaluated exactly; it is a counterexample only to the stronger lemma `all structured MOC4 support data have max_external e<=M`, not to MOC4 itself.
- No arbitrary bistochastic or unconstrained `SO(6)` witness is called a target counterexample.
- Repeated/singular spectra remain covered only through the existing boundary/continuity architecture once the generic target support inequality is closed; no new target-level closure is claimed here.
