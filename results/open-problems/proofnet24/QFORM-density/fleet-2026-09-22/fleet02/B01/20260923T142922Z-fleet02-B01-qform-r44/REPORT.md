SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T14:29:22Z.
attacking: the rank-three volume endpoint left by the three-hub theorem; convert three heavy volume marginals into a physical three-hub packet, and isolate/stress the genuinely remaining at-most-two-heavy-per-side class.

# fleet02/B01 — volume marginal concentration compiled into three hubs

Run: `20260923T142922Z-fleet02-B01-qform-r44`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Oscillatory replacement / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING ROUTING LEMMA + STRICT-N3 SURVIVOR CLASSIFICATION; FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Independent end-to-end review: **not supplied**.

## 1. Fresh source boundary and the first unpaid implication


The target remains the unrestricted statement: independent original-coordinate real variables with probability densities bounded by one; arbitrary real symmetric `A`; at least three eigenvalues of `A` of modulus at least one; prove one universal bound for the essential supremum of the density of `X^T A X`, or give a valid counterexample. No moment, support, Gaussian, log-concavity, connected-support, diagonal-basis or post-rotation-independence assumption is added. Continuity is separate.

The required Claude source was reread at the owner-pinned commit `e5f71d79eff325201dd0274053d20268ce65b837` and checked against the latest compatible master state observed during the run. The newer owner-supplied volume-stability package at `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` was also consumed. In particular its sharp fractional three-volume theorem says: if `M=A[I,J]`, `Z=e_3(M^T M)>0`, and every row volume marginal obeys `alpha_i<=q/2` for some `1<=q<3/2`, then

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.          (1.1)

All self-blocks and outside couplings remain arbitrary, and the proof is an averaged-frequency/decoupling/Brascamp--Lieb argument rather than a scalar pointwise Fresnel estimate.

The immediately preceding fleet02/B01 theorem, source `f98635ec90f47da9c38e40516896462bb423f3c6`, is `QFORM-THREE-HUB-JOINT-PLANCHEREL-v1`: if `H` is a set of three ORIGINAL coordinates and `B=A[H,H^c]` has rank three, with

`Pi_3(B)=sqrt(det(BB^T))`,

then, with arbitrary curvature on the three hubs and on their complement,

`||p_Q||_infinity <=3 sqrt(2) Pi_3(B)^(-1/3)`.               (1.2)

Its characteristic function has an integrable joint three-hub envelope. This theorem does not use law-uniform scalar quadratic-phase decay.

The first unpaid implication was `QFORM-N3-THREE-HUB-OR-VOLUME-ROUTING-v1`: given a target-scale rank-three cross-volume packet, understand the volume-marginal endpoint where the completed D/D' gates fail, without first inverting a tiny physical pair. This run attacks that implication directly.

The phase-aligned-density obstruction is preserved throughout: for each prescribed scalar frequency one can choose an admissible fragmented density whose one-dimensional quadratic-phase expectation is arbitrarily close to one. Nothing below asserts a law-uniform scalar `O(|t|^{-1/2})` estimate. The replacements are volume averaging, joint original-coordinate Plancherel, and the completed mixed-hub theorem.

## 2. Volume law and a deterministic concentration identity

Let `I,J` be disjoint ORIGINAL coordinate sets and put

`M=A[I,J]`.

Assume

`Z := e_3(M^T M)
   = sum_(|S|=|T|=3) det(M[S,T])^2 >0`.                       (2.1)

Use the completed Claude volume probability law

`w_(S,T)=det(M[S,T])^2/Z`.                                    (2.2)

Let

`alpha_i=P_w(i in S)`, `i in I`,
`beta_j=P_w(j in T)`, `j in J`.                               (2.3)

Then `sum_i alpha_i=sum_j beta_j=3`.

For a fixed three-row set `H={i_1,i_2,i_3}`, the elementary union bound in the *reverse* direction gives

`P_w(S=H)
 =P_w(i_1,i_2,i_3 all belong to S)
 >= alpha_(i_1)+alpha_(i_2)+alpha_(i_3)-2`.                   (2.4)

Because `|S|=3`, the event that all three indices occur is exactly `S=H`. By Cauchy--Binet,

`det(M_H M_H^T)
 =sum_(|T|=3) det(M[H,T])^2
 =Z P_w(S=H).`                                                (2.5)

Thus if the sum of three row marginals exceeds two, that concentration is not merely a probabilistic nuisance: it forces an actual three-row aggregate Gram determinant.

Now let

`B_H=A[H,H^c]`                                                (2.6)

be the FULL slope matrix from these three original coordinates to their entire physical complement. Since `J subset H^c`,

`B_H B_H^T = M_H M_H^T + N N^T >= M_H M_H^T`                 (2.7)

for the remaining complement columns `N`. Whenever the right side of (2.5) is positive, determinant monotonicity on positive definite matrices gives

`Pi_3(B_H)^2=det(B_H B_H^T)
 >= Z [alpha_(i_1)+alpha_(i_2)+alpha_(i_3)-2].`               (2.8)

This is the bridge from the volume endpoint to the previous three-hub receiver.

## 3. Main compiler: diffuse volume, three heavy marginals, or at most two heavy coordinates

### Theorem 3.1 — `QFORM-VOLUME-MARGINAL-TO-THREE-HUB-v1`

Keep (2.1)--(2.3). Sort the row marginals as

`alpha_(1)>=alpha_(2)>=alpha_(3)>=...`.

If

`delta_L:=alpha_(1)+alpha_(2)+alpha_(3)-2 >0`,               (3.1)

then the full quadratic form has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <=3 sqrt(2) delta_L^(-1/6) Z^(-1/6).
`                                                                  (3.2)

The same assertion holds with the column marginals and

`delta_R:=beta_(1)+beta_(2)+beta_(3)-2`.                       (3.3)

#### Proof

Take the three rows attaining the left side of (3.1). Equations (2.4)--(2.8) give

`Pi_3(B_H)>=delta_L^(1/2) Z^(1/2)`.                            (3.4)

Apply `QFORM-THREE-HUB-JOINT-PLANCHEREL-v1`, equation (1.2):

`||p_Q||_infinity
 <=3 sqrt(2) Pi_3(B_H)^(-1/3)
 <=3 sqrt(2) delta_L^(-1/6) Z^(-1/6).`                       (3.5)

The theorem tolerates all hub self-curvature, complement self-curvature, affine terms and outside couplings, so no extra block hypothesis is introduced. The column statement is the same argument after swapping `I,J`. QED.

### Corollary 3.2 — fixed universal routing threshold

Fix

`h=43/64`,                                                     (3.6)

so `2/3<h<3/4` and `3h-2=1/64`.

On either orientation of `M`, if every constrained-side marginal is at most `h`, apply the *newest* sharp fractional three-volume theorem (1.1) with

`q=2h=43/32`.                                                  (3.7)

It gives

`||p_Q||_infinity
 <= [3e/((3-4h)sqrt(2h))] Z^(-1/6)
 = (48e/5) sqrt(32/43) Z^(-1/6)
 <22.512 Z^(-1/6).`                                           (3.8)

If instead at least three row marginals are `>=h`, then (2.4) gives `P(S=H)>=1/64`, so Theorem 3.1 gives

`||p_Q||_infinity
 <=3 sqrt(2) 64^(1/6) Z^(-1/6)
 =6 sqrt(2) Z^(-1/6)
 <8.486 Z^(-1/6).`                                            (3.9)

Again the same two alternatives hold for the column marginals by transposition.

Therefore:

`boxed:` for every cross block with `Z>0`, **either** one of the two orientations is already paid by the sharp fractional three-volume theorem, **or** one orientation has at least three `43/64`-heavy volume coordinates and is paid by the physical three-hub theorem, **or**, if all four paid tests fail, each side has **exactly one or two** coordinates whose volume marginal exceeds `43/64`.                                      (3.10)

In particular, whenever `Z` itself is bounded below at target scale, every branch before the final alternative has one universal density constant. The remaining rank-three volume endpoint is no longer an arbitrary high-leverage configuration: it is a `<=2`-heavy-by-`<=2`-heavy core.

This is the main new routing reduction of the run.

### Relation to the owner-supplied volume-stability theorem

The volume-stability package proves, under its near-diffuse projection/tail hypotheses, the stronger gate `alpha_i<=0.6222...<2/3`; those matrices therefore fall immediately into (3.8). Corollary 3.2 is aimed at the complementary volume-concentrated endpoint. It does not redo the stability theorem and it does not claim that the bare spectral hypothesis automatically supplies a target-scale `Z`.

## 4. The `<=2 x <=2` heavy survivor is real in strict N3

The final alternative in (3.10) is not an artefact of the proof. It occurs in a clean target-valid strict-N3 family.

Let `k>=4` and set

`m=k^4`.

Split the left bank into two singleton coordinates `a,c` and a diffuse bank `L={x_1,...,x_m}`. Split the right bank into singleton coordinates `b,d` and a diffuse bank `R={y_1,...,y_m}`. Put `u=m^(-1/2)(1,...,1)` on each diffuse bank. Define the left-right cross block by the three orthogonal rank-one directions

`M_k
 = k e_a u_R^T
 + k u_L e_b^T
 + k^(-2) e_c e_d^T.`                                        (4.1)

All same-side blocks are zero for the basic family, and define

`A_k=[[0,M_k],[M_k^T,0]].`                                    (4.2)

The three singular values of `M_k` are exactly

`k, k, k^(-2)`,                                                (4.3)

so the nonzero spectrum of `A_k` is

`{k,k,k^(-2),-k,-k,-k^(-2)}`.                                (4.4)

Hence there are four eigenvalues of modulus at least one. Moreover

`Z=e_3(M_k^T M_k)=k^2*k^2*k^(-4)=1`.                          (4.5)

Every physical diagonal is zero. Every nonzero physical entry is either

`k/sqrt(m)=1/k` or `k^(-2)`,                                  (4.6)

so every nonzero physical `2 x 2` principal determinant has magnitude at most `1/k^2`. Thus for any fixed no-pivot threshold, this family eventually lies in strict N3.

Because `M_k` has exact rank three, its volume marginals are the row/column leverages of its singular frames. On the left,

`alpha_a=alpha_c=1`, `alpha_(x_r)=1/m`;                       (4.7)

on the right,

`beta_b=beta_d=1`, `beta_(y_r)=1/m`.                           (4.8)

Thus both orientations fail every D' gate with `h<3/4`, while each side has exactly two heavy volume coordinates. Theorem 3.1 also necessarily deteriorates: the largest three-marginal sum is `2+1/m`, so `delta_L=delta_R=1/m`. Equivalently the best three-row hub packet has

`Pi_3=k^(-2)`,                                                  (4.9)

and the three-hub bound grows like `3sqrt(2) k^(2/3)`.

This is an explicit obstruction to the stronger hoped-for implication

`target-scale Z_3 + failure of diffuse D' => target-scale three-hub Pi_3`.

The obstruction is intermediate only; it is not a counterexample to QFORM.

## 5. The newest Claude mixed-hub theorem pays the survivor at an actual inequality

The same family shows what the next correct mechanism is. Use the two singleton coordinates

`H={a,b}`                                                       (5.1)

as physical hubs. Use the two diffuse banks `L union R` as the theorem-H leaf set `I`, and place the remaining singleton pair `{c,d}` into the arbitrary outside bank `J`.

On the leaf set,

`A_II=0`,                                                       (5.2)

so Theorem H has `r=0`. Each `x_r` is coupled only to hub `b`, with coefficient `1/k`; each `y_r` is coupled only to hub `a`, also with coefficient `1/k`. Hence the augmented two-dimensional Gram is exactly

`G~=diag(m/k^2,m/k^2)=diag(k^2,k^2)`,                          (5.3)

and every leaf leverage is

`1/m=k^(-4)<=1/2`.                                             (5.4)

The small hyperbolic pair `c-d` lies entirely in the arbitrary `J-J` block and is not discarded.

The completed Claude Theorem H therefore gives, for the full form and arbitrary cap-one product laws,

`|phi_Q(t)|
 <= min(1, 4 pi^2 k^(-2) |t|^(-2)).`                          (5.5)

Integrating this actual envelope,

`int_R min(1,4pi^2 k^(-2)t^(-2)) dt =8pi/k`,                  (5.6)

and Fourier inversion yields

`boxed:
 ||p_(X^T A_k X)||_infinity <=4/k <=1  (k>=4).
`                                                                  (5.7)

Thus the `2 x 2` heavy-volume survivor is real, but in this orthogonal crossed-star model it routes cleanly to the newest mixed-hub averaged-frequency theorem. This is an equation-level application of the required newest report, not a status citation.

The mechanism is exactly compatible with the phase-aligned-density correction: the integrable `|t|^-2` decay is produced jointly by two physical hubs and a two-dimensional aggregate leaf Gram, not by any law-uniform one-coordinate quadratic-phase estimate.

## 6. Newest designated partner fleet03/B01 applied on the same strict-N3 family

The newest completed designated-partner run is `fleet03-B01-20260923T133048Z-auto11`, canonical source `40c82306ce748ae60a09a941277931ae8ca3b05b`. Its theorem says that after an invertible indefinite physical pair `B`, if an exact-rank-two Schur principal bank has nonzero-eigenvalue pseudo-determinant `Pi_2`, then

`||p_Q||_infinity
 <=min{512 kappa^(-1/2) Pi_2^(-1/4),
        64(D kappa)^(-1/4) Pi_2^(-1/8)},`                    (6.1)

where `D=|det B|` and `kappa=sigma_min(B)`.

Apply it to (4.2) using the physical hyperbolic pair

`P={a,y_1}`.                                                   (6.2)

Its off-diagonal coefficient is `1/k`, and `y_1` has no other coupling, so

`D=k^(-2)`, `kappa=k^(-1)`.                                   (6.3)

The exact Schur correction vanishes on the disjoint pair

`V={b,x_1}`,                                                   (6.4)

whose Schur principal block remains

`S[V,V]=[[0,1/k],[1/k,0]]`,                                   (6.5)

hence

`Pi_2=k^(-2)`.                                                 (6.6)

Equation (6.1) gives the valid full-form estimate

`||p_Q||_infinity
 <=min{512 k,64 k}=64 k.`                                     (6.7)

This deliberately diverges along the family while the mixed-hub theorem gives `4/k`. The comparison is structurally informative: once rank-three volume has collapsed to one or two heavy coordinates on each side, local physical-pair inversion can be catastrophically expensive even though aggregate hub currency is excellent. The correct order is to aggregate the surviving heavy stars before paying a tiny pair determinant.

## 7. Exact scope gain and remaining unpaid implication

The new result does **not** prove that arbitrary strict N3 supplies a rank-three cross block with `Z` bounded below. That stronger cross-rank-three dichotomy is already known false: there are target-valid matrices for which every coordinate cut has cross rank at most two. Nor does this run prove that every `<=2 x <=2` heavy-volume survivor satisfies the algebraic hypotheses of Theorem H; arbitrary self-curvature on the diffuse leaf bank can obstruct that direct invocation.

What has changed is the rank-three-volume branch itself. For any candidate cross block with target-scale `Z`, the only unhandled volume-concentration pattern is now quantitatively localized to at most two `43/64`-heavy coordinates on each side. Three or more heavy marginals automatically become an original-coordinate three-hub Gram and are paid by joint Plancherel; a diffuse constrained side is paid by the newest fractional-volume theorem.

The first unpaid implication is therefore

`QFORM-N3-TWO-BY-TWO-HEAVY-VOLUME-ROUTING-v1`:

> In a strict-N3 state with a target-scale rank-three cross-volume packet whose row and column volume laws each have only one or two `43/64`-heavy coordinates, prove a quantitative exit to a completed mixed-hub theorem, a rank-two/grouped receiver, a pair/Schur branch, or another already-paid mechanism while retaining arbitrary within-leaf quadratic curvature; or give a target-valid construction showing which additional invariant is necessary.

The crossed two-star family (4.1) shows that this survivor is nonempty and that the mixed-hub mechanism is the right answer in at least one extremal orthogonal model. The genuinely hard remainder is destructive/nonorthogonal overlap plus arbitrary diffuse-leaf self-curvature.

## 8. Source pins and review status

Inputs actually used at equations:

1. owner-pinned Claude package `e5f71d79eff325201dd0274053d20268ce65b837`, especially D/D'/H and the volume law;
2. compatible current source on master as observed during this run;
3. owner-supplied volume-stability theorem `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, specifically its sharp `q`-fractional three-volume estimate (1.1);
4. previous fleet02/B01 three-hub theorem `f98635ec90f47da9c38e40516896462bb423f3c6`;
5. newest completed designated partner fleet03/B01 `40c82306ce748ae60a09a941277931ae8ca3b05b`.

The full conjecture remains OPEN. No literature-wide novelty claim is made. The theorem here is a supporting routing lemma; it has not received two independent end-to-end reviews.
