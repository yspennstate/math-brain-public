SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T02:20:10Z.
attacking: QFORM-N3-O0-GROUPED-DUST-PAYMENT-v1 by mixing the anchored third-volume packet with the physical residual pair-volume law before any reciprocal minor is selected.

# fleet01/B20 auto11 — anchored-3 / residual-2 mixed-volume payment

## Status

**ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN.**

The unrestricted conjecture is not proved or disproved here. The theorem below completely pays a new, explicit subbranch of the current fleet02/B20 P2 packet and reduces every remaining P2 survivor to either a fixed-scale physical pair-wedge hub or a doubly nested anchored-third-minor packet. Continuity is proved in the paid mixed-volume branch because the resulting characteristic function is in `L^1`; global continuity remains open.

Execution is `WITHOUT_VERIFIED_BRAIN`: authenticated repository reads/writes occurred, but no native learned-memory receiver use was exposed. Model self-report is GPT-5.6 Sol. Configured reasoning effort and provider usage/thinking counters are not exposed and remain `UNKNOWN/null`.

## 1. Sources and exact retained scope

Fresh owner control remained QFORM-only at revision `2026-09-22.15`. I preserve the live corrections: there is no uniform law-independent pointwise quadratic oscillatory decay; no post-rotation independence is used; no arbitrary-joint coarea or conditional projected-density moment is used; and no single physical minor is assumed uniformly large.

The newest completed designated partner actually consumed is fleet02/B20 auto11:

`yspennstate/math-open-problems@34a57f18778ea4be069a3f39a953801296d01864`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T000049Z-fleet02-B20-QFORM-auto11/REPORT.md`.

Its P2 state is an actual original-coordinate cross block, after physical permutations,

`B = [[b,r^T],[c,D]]`,

with a fixed row anchor `i`, column anchor `a`, and anchored physical third-minor mass

`Z := sum_{j<k, p<q} det B[{i,j,k},{a,p,q}]^2 > 1/768`,             (1.1)

while the completed physical-deshear inequality gives, on P2 inside `N3(1/128)`,

`E2 := e_2(D^T D) > 1/48`.                                           (1.2)

The partner's high fifth-volume subbranch `e_5(D^T D)>=1/1024` is already paid by its D5 input, so (1.1)-(1.2) are used here as actual downstream inequalities, not merely cited structurally.

The analytic engine actually applied is fleet01/B01's completed mixed-order physical-minor Brascamp--Lieb/Fourier theorem:

`yspennstate/math-open-problems@86f318f0826325e6df3504e1e8ec15f4316cc861`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T001242Z-b01-qform-auto11/REPORT.md`.

For a probability law `Omega` on nonzero square **physical** minors of a cross block, let `alpha_u=P_Omega(u in row-set)`, let `kbar=E_Omega |S|`, and

`K(Omega)=exp(E_Omega log det(M_ST)^2 + H(Omega))`.

If every row marginal is at most `1/2` and `kbar>2`, then the full ambient quadratic form, with arbitrary same-side blocks, outside coordinates, couplings and induced affine terms, has a bounded continuous density with

`||p_Q||_infinity <= 2 sqrt(e) kbar/(kbar-2) K(Omega)^(-1/(2 kbar)).`   (1.3)

This theorem is source-coordinate/product-preserving; it is not the refuted scalar pointwise Fresnel shortcut.

## 2. The new mixed-volume theorem

### Theorem `QFORM-O0-ANCHOR-PAIR-MIXED-VOLUME-PAYMENT-v1`

Assume (1.1)-(1.2). Define the natural anchored third-minor law `w3` by

`w3(j,k,p,q) = det B[{i,j,k},{a,p,q}]^2 / Z`                         (2.1)

on the nonzero anchored `3x3` minors. For every residual physical row `j`, write

`a_j := P_w3(j is selected)`,                                        (2.2)

so

`sum_j a_j = 2`.                                                      (2.3)

Define the natural physical pair-volume law `v2` on nonzero `2x2` minors of `D` by

`v2(S,T)=det(D[S,T])^2/E2`,                                          (2.4)

and let

`q_j := P_v2(j is selected)`,                                        (2.5)

so

`sum_j q_j=2`.                                                        (2.6)

If

`boxed: a_j + 3 q_j <= 2 for every residual physical row j,`          (2.7)

then the full ambient quadratic form has a bounded continuous density and

`boxed: ||p_Q||_infinity < 72.220.`                                  (2.8)

The identical assertion holds after transposing the cross block, with row and column marginals exchanged.

### Proof

Mix the two physical-minor laws before taking any reciprocal determinant:

`Omega := (1/4) w3 + (3/4) v2`.                                     (2.9)

The fixed anchor row `i` occurs only in the order-three component, hence its `Omega` row marginal is exactly `1/4`. A residual row `j` has marginal

`alpha_j(Omega)=(a_j+3q_j)/4 <=1/2`                                 (2.10)

by (2.7). Thus every row marginal obeys the Brascamp--Lieb admissibility gate.

The mean determinant order is

`kbar=(1/4)3+(3/4)2=9/4>2`.                                         (2.11)

Because the order-three and order-two supports are disjoint, and because the natural determinant-squared law has entropy-determinant currency equal to its total squared-minor mass,

`K(w3)=Z`, `K(v2)=E2`,                                               (2.12)

and the entropy of the mixture contributes the binary mixing factor. Therefore

`K(Omega)
 =4^(1/4)(4/3)^(3/4) Z^(1/4) E2^(3/4).`                            (2.13)

Using the **actual partner inequalities** (1.1)-(1.2),

`K(Omega)
 >4^(1/4)(4/3)^(3/4)(1/768)^(1/4)(1/48)^(3/4)`
` =1/(24*3^(3/4)).`                                                  (2.14)

Apply (1.3) with `kbar=9/4`. Since

`2 sqrt(e) kbar/(kbar-2)=18 sqrt(e)`,                               (2.15)

we obtain

`||p_Q||_infinity
 <18 sqrt(e) (24*3^(3/4))^(2/9)`
` =72.2193481943... <72.220.`                                        (2.16)

The mixed-order theorem proves `phi_Q in L^1`, hence a bounded continuous density in this subbranch. No random coordinate is rotated. QED.

## 3. Exhaustive structural consequence when the mixed payment fails

Suppose the row-oriented condition (2.7) fails at a physical row `j`. Then

`a_j+3q_j>2`.                                                        (3.1)

Because `a_j<=1`, necessarily

`boxed: q_j>1/3.`                                                     (3.2)

If in addition `q_j<=1/2`, then (3.1) forces

`boxed: a_j>1/2.`                                                     (3.3)

Thus every unpaid row obstruction is already a quantitatively nontrivial physical pair-wedge hub, and if it is not a `q_j>1/2` hub it is simultaneously co-heavy for anchored third-volume. Since `sum_jq_j=2`, there are at most five bad rows satisfying (3.1). The same conclusions hold for physical columns after transposition.

A useful fixed-margin refinement is obtained at `5/12`. If the row condition fails but every row pair-volume marginal satisfies `q_j<=5/12`, then for the failing row

`a_j>2-3(5/12)=3/4`.                                                 (3.4)

If the transpose condition also fails and every column pair-volume marginal is at most `5/12`, choose a failing residual row `j` and failing residual column `p`. Their anchored-third-volume marginals both exceed `3/4`; hence under `w3`, by the union bound,

`P_w3(j and p are both selected)>1/2`.                               (3.5)

Multiplying by `Z>1/768` gives the completely physical doubly-nested packet

`boxed:
 sum_{k != j, q != p}
 det B[{i,j,k},{a,p,q}]^2 > Z/2 >1/1536.
`                                                                        (3.6)

Consequently every P2 state satisfying the partner inequalities (1.1)-(1.2) obeys the exhaustive trichotomy:

1. the row or column mixed-volume condition holds, and the branch is paid by (2.16);
2. some residual physical row or column has natural pair-volume marginal `>5/12`;
3. there are fixed residual physical row and column anchors for which the common anchored `3x3` minor mass exceeds `1/1536` as in (3.6).

This statement keeps aggregate determinant mass intact; it does not infer one large coefficient or one large minor.

## 4. Why this advances the fleet02/B20 spike/dust frontier

The explicit partner spike/dust family shows that `E2>1/48`, small `E3`, small `E5`, and the full three-large-eigenvalue hypothesis do not force a robust second singular direction. The theorem above does not try to do that. Instead it spends the anchored third-volume and the residual second-volume **jointly**, before any reciprocal local object is selected.

This is exactly the regime in which a rank-one spike may coexist with many tiny dust directions: if that dust is spread enough that the mixed row marginals satisfy (2.7), it is already paid by a dimension-free Fourier budget. If it is not spread enough, the failure itself identifies a bounded-size list of physical pair-wedge hubs; with the fixed `5/12` split, absence of such a hub forces the stronger doubly nested packet (3.6).

Thus the P2 part of `QFORM-N3-O0-GROUPED-DUST-PAYMENT-v1` is reduced to the source-coordinate implication

`QFORM-P2-HUB-OR-DOUBLE-NESTED-PAYMENT-v1`:

pay a natural pair-volume hub of marginal `>5/12`, or pay the doubly nested anchored-third-minor packet of mass `>1/1536`, while retaining arbitrary same-side quadratic blocks and ambient couplings.

The partner's zero-edge doubly-transverse and double-star branches remain separate unpaid packets; they are not claimed closed by the present theorem.

## 5. Scope and correction audit

- Full QFORM: **OPEN**.
- Full target continuity: **OPEN**.
- Mixed-volume branch (2.7), or its transpose: **PROVED bounded continuous density**, with explicit bound `<72.220`.
- No Gaussian, moment, iid, compact-support, connected-support or log-concavity hypothesis was introduced.
- No post-rotation independence is asserted.
- No uniform pointwise scalar quadratic oscillatory decay is used.
- No arbitrary-joint coarea, conditional projection-height moment, or unrestricted fiber supremum is used.
- No `small operator-norm remainder can be discarded` step is used.
- No single physical determinant is selected before aggregation.

The first remaining implication in this route is therefore the fixed-scale physical **pair-wedge-hub / doubly-nested-anchor payment**, together with the partner's still-separate zero-edge and star packets. A natural next attack is a second mixed-order law that conditions the pair-volume law on the hub and mixes its complementary order-two wedges with the nested anchored order-three law; the target is again mean determinant order `>2` with every physical row occupancy at most `1/2`.