SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T22:55:17.506789Z.
attacking: partner r36 mu-average transverse cancellation: turn it into an aggregate Pluecker-rectangle obstruction without any single-minor floor, then combine it with the pinned D5 cross-tail bound.

# account02/B13 r37 — aggregate Pluecker rectangles and denominator-free four-point stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **new supporting theorem proved; full unrestricted QFORM remains OPEN / NOT PROVED / NOT DISPROVED; continuity remains separate.**

No moment, compact-support, connected-support, Gaussian, log-concavity, diagonal-basis, post-rotation independence, attained bathtub optimizer, common support diameter, fixed fragment count, or perturbative deletion of a coefficient-small quadratic form is used.

## 1. First unpaid implication

The first unpaid B13 implication is now

`QFORM-PLUCKER-RECTANGLE-TO-BANK-RECEIVER-v1`:

> Convert the positive aggregate four-point matching mass proved below into a product-preserving finite-center/bank density receiver, uniformly through the branch where one perfect matching is Pluecker-small; simultaneously retain the pinned `s_5=O(rho^-1)` physical cross-tail obstruction in the general (not exactly diagonal-plus-rank-two) survivor. If this cannot be paid, construct a genuine bounded-finite-union product-indicator counterexample.

The point of the new theorem is that the previous lower-bound hypotheses on one `q_ki` and one complementary determinant are no longer needed. The remaining alternative is an aggregate projective pairing/balance problem.

## 2. Source-pinned premises

Fresh brain control was resolved at `yspennstate/math-research-brain@6a95a4416c962266163428cb1d9adea982d3f05d`, with OWNER CONTROL revision `2026-09-22.15`, no account02/B13 stop, and QFORM as the sole research target.

The latest completed designated partner result consumed is account03/B13 r36:

`yspennstate/math-open-problems@a558625206539a6eaee5aa6b2c6d851ccd2f1990`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T223116Z-account03-B13-qform-r36/REPORT.md`.

Its exact chamber is

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i c_i<=1/3`, `c_i=||u_i||^2`, `s_3(A)>=1`.    (2.1)

It selects a physical coordinate `k` with `|d_k|>=1`. For unordered physical pairs `E={i,j}` disjoint from `k`, put

`q_ij=det(u_i,u_j)^2`,

`Delta_E=sum_{F disjoint E,k} q_F`,

`W=sum_E q_E Delta_E`,

`mu(E)=q_E Delta_E/W`.                                               (2.2)

The partner proves

`W>=1/1152`.                                                         (2.3)

In its non-rank-one branch it also proves

`E_mu |tau_E| <= C_mu/rho`,                                         (2.4)

where

`tau_ij=d_k q_ij+d_i q_kj+d_j q_ki`,

`C_mu=437400000/(1536 e^2)=38538.836515426...`,                      (2.5)

and `rho=P{X^TAX in J}/|J|` is any slab ratio. The partner's proof already works for arbitrary cap-one product inputs.

The owner-required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed result used below is the unconditional fifth-volume theorem `D5`; no numerical counterexample-search output is used as proof.

## 3. Canonical four-set law behind the partner pair law

For every physical four-set `R={a,b,c,d}` disjoint from `k`, let

`w_1=q_ab q_cd`,
`w_2=q_ac q_bd`,
`w_3=q_ad q_bc`,

and

`S_R=w_1+w_2+w_3`.                                                  (3.1)

If `p_ij=det(u_i,u_j)` is the signed Pluecker coordinate, the two-dimensional Pluecker identity is

`p_ab p_cd-p_ac p_bd+p_ad p_bc=0`.                                 (3.2)

Each of the three signed products is a sum/difference of the other two. Therefore

`w_m <=2(sum_{ell !=m} w_ell)`

for every `m`, hence

`boxed: max_m w_m <=(2/3)S_R.`                                     (3.3)

On the other hand, by the definition of `Delta_E`, every unordered pair of disjoint physical pairs appears twice in `W`. Thus

`boxed: W=2 sum_R S_R.`                                            (3.4)

In particular `sum_R S_R>=1/2304`. Define the probability law

`nu(R)=S_R/(sum_T S_T)`.                                           (3.5)

There is a useful exact sampling interpretation. Given `R~nu`, choose one of its three perfect matchings with probability `w_m/S_R`, then choose one of the two edges of that matching uniformly. The resulting edge has law exactly `mu`. Indeed a disjoint ordered pair `(E,F)` receives weight `q_Eq_F/W`, and summing over `F` gives `q_E Delta_E/W`.

This coupling is the mechanism that upgrades an average over physical pairs to an aggregate statement over four-point packets.

## 4. Main theorem: weighted Pluecker-rectangle stability

### Theorem `QFORM-MU-PLUCKER-RECTANGLE-STABILITY-v1`

Assume (2.1)-(2.5). Let

`M=E_mu |tau_E|`.

Fix parameters `0<eta<1/6` and `0<gamma<1`. Call a physical pair **good** when

`|tau_E|<=M/eta`.                                                   (4.1)

For a four-set, call a perfect matching clean when both of its edges are good. Let `C_3` be the four-sets for which all three perfect matchings are clean. Let `C_2` be those with exactly two clean matchings; for `R in C_2`, let `m_0(R)` be its unique non-clean matching and put

`kappa_R=w_{m_0(R)}/S_R`.                                         (4.2)

Then

`boxed:
 nu( C_3 union {R in C_2: kappa_R<=gamma} )
 >=1-6 eta-2 eta/gamma.}`                                         (4.3)

This is an aggregate statement: it loses neither the number of physical coordinates nor a reciprocal individual minor.

### Proof

Markov gives

`mu{E: E is bad}<=eta`.                                            (4.4)

Use the sampling interpretation after (3.5). A sampled perfect matching is non-clean only if at least one of its two sampled edges is bad, so

`P{sampled matching non-clean}<=2 eta`.                            (4.5)

If a four-set has at most one clean matching, its conditional clean-matching probability is at most `2/3` by (3.3). Its conditional non-clean probability is therefore at least `1/3`. Hence

`nu{R: R has at most one clean matching}<=6 eta`.                  (4.6)

For `R in C_2`, the conditional probability of selecting the unique dirty matching is exactly `kappa_R`. Therefore (4.5) gives

`integral_{C_2} kappa_R dnu(R)<=2 eta`.                            (4.7)

Markov on (4.7) gives

`nu{R in C_2:kappa_R>gamma}<=2 eta/gamma`.                         (4.8)

Removing the sets in (4.6) and (4.8) proves (4.3). QED.

### Concrete parameter choice

Take

`eta=1/64`, `gamma=1/4`.                                           (4.9)

Then

`boxed:
 nu( C_3 union {R in C_2:kappa_R<=1/4}) >=25/32.}`                 (4.10)

Thus at least `25/32` of the **entire aggregate four-point matching mass** lies in one of two explicit packet types.

For the `C_2` packet, the dirty perfect matching has weight at most `S_R/4`, while each of the two clean matchings has weight at least `S_R/12`: indeed their total weight is at least `3S_R/4`, and no matching can exceed `2S_R/3` by (3.3). So this branch is a genuine cross-dominant Pluecker/two-cluster geometry, not merely the existence of one small minor.

For the `C_3` packet, all six physical pair invariants `tau_ij` on the four leaves are small simultaneously. Section 5 turns that into a denominator-free four-point obstruction.

## 5. Exact denominator-free four-point identity

Fix four distinct leaves `r,s,t,u` disjoint from `k`. Put

`Q_i=q_ki`.                                                        (5.1)

A direct expansion of the four `tau` terms cancels every coefficient `d_r,d_s,d_t,d_u` and leaves only `d_k`. The resulting exact polynomial identity is

`boxed:
 |tau_rt Q_s Q_u+tau_su Q_r Q_t-tau_ru Q_s Q_t-tau_st Q_r Q_u|
 =2|d_k| sqrt(Q_r Q_s Q_t Q_u q_rs q_tu).}`                        (5.2)

One proof is to rotate only the two-dimensional coefficient basis so `u_k=(a,0)`, expand both sides in the coordinates of the four rows, and square. Both sides become the same polynomial; hence the identity also covers zero star determinants by continuity. No random variables are rotated.

Suppose the two perfect matchings

`{rt,su}` and `{ru,st}`                                            (5.3)

are clean at threshold `T`. Relabel the remaining matching as `{rs,tu}`. From (5.2),

`2|d_k| sqrt(Q_r Q_s Q_t Q_u q_rs q_tu)
 <=T (Q_r+Q_s)(Q_t+Q_u).`                                         (5.4)

Define the star-balance factor

`beta_ab=2 sqrt(Q_aQ_b)/(Q_a+Q_b) in [0,1]`,                      (5.5)

with value zero if the denominator vanishes. Then

`boxed:
 |d_k| beta_rs beta_tu sqrt(q_rs q_tu)<=2T.`                       (5.6)

This is the key gain over the prior local four-point estimate: no `q_ki` is inverted. Tiny physical star weights remain visible as balance degeneration.

## 6. Quantitative consequence on the `25/32` aggregate core

In the partner non-rank-one branch, (2.4) says `M<=C_mu/rho`. Under (4.9), every good edge satisfies

`|tau_E|<=64 C_mu/rho`.                                            (6.1)

For every `R in C_3`, choose the heaviest of its three perfect matchings as the base matching `{rs,tu}`. By (3.3),

`1/3 <= kappa_R=q_rs q_tu/S_R <=2/3`.                              (6.2)

All four cross edges in (5.3) are good, so (5.6), `|d_k|>=1`, and (6.2) give

`boxed:
 beta_rs beta_tu sqrt(S_R)
 <=128 sqrt(3) C_mu/rho
 <8544156.533/rho.}`                                               (6.3)

Combining (4.10) and (6.3) yields the following exhaustive aggregate alternative on at least `25/32` of the canonical `nu` mass:

- **Pluecker two-cluster packet:** exactly two matchings are clean, their weights are each at least `S_R/12`, and the unique dirty matching has weight at most `S_R/4`; or
- **balanced-volume collapse packet:** all six edges are clean and, after choosing the largest base matching, its paired star balances times the square root of the total four-row matching volume are at most `8.545e6/rho`.

No lower bound on a single `q_ki`, `q_ij`, or `Delta_{kij}` has been introduced. This is precisely the missing aggregation feature in the partner's local finite-center theorem.

The constants are intentionally not optimized; the point is the dimension-free positive aggregate mass and the absence of reciprocal local minors.

## 7. Extremal product-law transfer — no optimizer is assumed

The partner chain includes the optimizer-free cap-one product-law reduction: for every nonnegative measurable kernel `K`, the supremum over probability densities `0<=f_i<=1` is the supremum over products of unit-measure indicator sets, with strict witnesses approximable by bounded finite unions and with no uniform diameter or fragment-count bound.

For completeness, the only transfer used here is the safe approximation implication. If `g_i` approximates `f_i` in `L^1`, then

`||prod_i f_i-prod_i g_i||_1 <= sum_i ||f_i-g_i||_1`.              (7.1)

For a slab kernel `K=1_{x^TAx in J}`, (7.1) transfers any strict slab violation with arbitrarily small loss. Expanding each finite convex mixture, at least one product of unit-measure bounded finite-union indicators inherits the violation. Therefore every coefficient obstruction in Sections 3-6 applies without asserting a global attained bathtub optimizer, a centered interval, bounded support diameter, or fixed number of fragments.

In particular, a hypothetical diverging-density sequence can be sought inside these finite-union product witnesses **only in the approximation sense**; remote fragments and increasing fragment counts remain allowed.

## 8. Required pinned Fourier result applied to the surviving general obstruction

The pinned unconditional `D5` theorem says that for every disjoint original-coordinate cut `I,J`, with

`M=A[I,J]`,

`||p_Q||_infinity <=5 sqrt(2e) e_5(M^T M)^(-1/10)`.                (8.1)

Therefore every slab witness of ratio `rho` must satisfy

`boxed:
 e_5(M^T M) <=(5 sqrt(2e)/rho)^10.`                               (8.2)

Since

`e_5(M^T M)>=s_1(M)^2 ... s_5(M)^2>=s_5(M)^10`,

we obtain the concrete obstruction

`boxed:
 s_5(A[I,J]) <=5 sqrt(2e)/rho
 =11.658219907986.../rho`                                         (8.3)

for **every** disjoint physical cut.

This use is complementary rather than cosmetic. In the exact chamber `D+U Lambda U^T`, every off-diagonal physical cross block has rank at most two, so `D5` is identically blind there and Sections 3-6 address exactly that missing geometry. In a general high-density survivor, however, (8.3) says that any extra physical cross interaction attached to the finite-center packets can have at most four transverse modes above the same `O(rho^-1)` scale. The coefficient-small tail may not be discarded as a random quadratic perturbation on rough/unbounded inputs; (8.3) is retained only as a singular-value obstruction.

The pinned `COUNTEREXAMPLE_SEARCH.md` reports no valid counterexample in its tested families. Those numerics are not used in any proof here.

## 9. What this rules out, and what remains

Partner r36 had already shown that the diffuse exact-rank-two non-rank-one chamber has `mu`-average transverse cancellation `O(rho^-1)`, but its quantitative four-point theorem needed pointwise lower floors on `q_ki` and complementary volume. The new theorem removes that bottleneck at the **aggregate packet-selection level**:

1. the pair law is lifted exactly to the physical four-set law `nu`;
2. at least `25/32` of all matching mass is forced into cross-dominant two-cluster packets or six-edge-good packets;
3. on the six-edge-good packets the exact identity (5.2) converts cancellation into a denominator-free balance/volume inequality;
4. no single reciprocal minor or coordinate count enters.

What is not yet proved is a density receiver that consumes these packets while preserving the original product structure when the cross-dominant pairing varies from packet to packet, or when the balance factor in (6.3) degenerates. Small balance can be caused by extreme star-weight ratios, and arbitrary fragmented/unbounded supports forbid treating the associated coefficient-small directions perturbatively.

That precise remaining step is `QFORM-PLUCKER-RECTANGLE-TO-BANK-RECEIVER-v1` from Section 1. A valid closure should aggregate the packet law before inversion, likely producing a finite number of physical banks/centers; otherwise this is the place to seek a source-valid finite-union product counterexample.

## 10. Integrity / status

The algebraic identities above are exact. A symbolic polynomial check of (5.2) was used only as a sanity check; the proof is the displayed expansion. The Pluecker matching bound (3.3) and probability estimates (4.3) are deterministic.

No claim is made that the unrestricted conjecture is solved. No continuity statement is inferred. No output of the pinned numerical search is promoted to proof.
