SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T15:05:07Z.
attacking: the E2 double-near-coloop survivor by a second exact E2-to-E1 determinant shadow; force either a half-Riesz payment or one macroscopic physical 2x2 minor, then spend its induced edge with the completed account02/B07 pair-tail receiver.

# account01/B07 r27 — iterated near-coloop compression to a macroscopic coordinate minor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `account01-B07-20260923T150507Z-r27`  
Owner control: revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **ESSENTIAL STEP APPLIED / DOUBLE-NEARCOLOOP -> THIRD PAYMENT OR MACROSCOPIC 2x2 MINOR / PARTNER PAIRTAIL APPLIED / FULL QFORM OPEN**.

The unrestricted theorem is not claimed. All conditioning is in ORIGINAL independent coordinates. No Gaussian, moment, log-concavity, compact-support, connected-support, diagonal-basis, or independence-after-rotation assumption is added. The refuted law-uniform pointwise oscillatory estimate, arbitrary-joint coarea bound, conditional projection-density moment, naive fiber-sup integration, and one-tiny-minor reciprocal shortcut are not used.

## 1. Sources actually consumed

1. Current owner/control state in `yspennstate/math-research-brain` main, including `AGENTS.md`, `scheduled_tasks/README.md`, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, `scheduled_tasks/PROTOCOL.md`, programme `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account01/B07.json`. The full conjecture and continuous-density upgrade remain OPEN.
2. Own immediately preceding report:
   `yspennstate/math-open-problems@dfb5c8b66cb2f60c1bd3dd202c609902cd5208b2`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T140342Z-r26/REPORT.md`.
   In particular it proves `QFORM-MIXED21-FRACTIONAL-HALFRIESZ-v1` and the first anchored E2->E1 shadow, and leaves a double-near-coloop with more than `9/16` of the incoming E2 determinant currency.
3. Completed designated partner account02/B07 pair-tail theorem:
   `yspennstate/math-open-problems@3e36370502df5afeb00457b74d05cdbfd87168b0`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T104812Z-account02-B07-qform-r13/REPORT.md`.
   Its `QFORM-PAIRTAIL-CURVATURE-RECEIVER-v1` is applied below to the new macroscopic edge produced in this run.
4. The latest completed account02/B07 handoff available at startup was also read:
   `yspennstate/math-open-problems@d57825ed929db0db057013ee2a12d547fd7cacac`, support-diffuse residual-E3 compiler. It confirms the current lower-compound survivor structure but is not substituted for the exact pair-tail scope used in Section 6.

## 2. Incoming state: the E2 double-near-coloop

The r25/r26 scalar-Schur branch has an outer physical scalar coefficient `a` and an ORIGINAL-coordinate Schur remainder. In its notation there is a physical E2 determinant packet of mass `Z>0` satisfying

`|a| >= sqrt(H)/(2 F^2)`,
`Z >= H/F^2`,                                                     (2.1)

where `F` is the ambient Frobenius scale and `H` is the inherited fixed-double-pair third-volume bank.

At threshold

`h=3/4`,

the order-two fractional-trace gate fails only if one physical column `j` has E2 inclusion marginal `>h`. Conditioning the same determinant law on that column and applying the r26 mixed order-2/order-1 gate on the row side fails only if one residual physical row `i0` has conditional marginal `>h`. Therefore the still-unpaid state has one fixed physical row pair `{s,i0}` and one fixed physical column `j` with

`G := sum_(k != j) det C[{s,i0},{j,k}]^2 > h^2 Z = 9Z/16`.       (2.2)

Here `C` is the actual physical cross block in the Schur remainder. No individual minor has yet been selected.

The question is whether the determinant mass in (2.2) can remain arbitrarily diffuse over the residual columns `k`. The next exact shadow answers this.

## 3. A second exact E2->E1 shadow, now on the column side

Write the two fixed physical rows of `C` as vectors `u,v`. For the fixed physical column `j`, put

`L_j^2 = u_j^2 + v_j^2`.

For each residual physical column `k != j`, define

`d_k = det [[u_j,u_k],[v_j,v_k]] = u_j v_k - v_j u_k`,
`W_k = u_k^2 + v_k^2`.

Then (2.2) is `G=sum_(k != j) d_k^2`.

### Theorem 3.1 — `QFORM-FIXEDPAIR-E2-EXACT-E1-COLUMN-SHADOW-v1`

For every `k != j`,

`boxed: d_k^2 <= L_j^2 W_k.`                                      (3.1)

Consequently, if `L_j>0`, there is a genuine fractional physical order-one determinant packet, supported on the two rows `{s,i0}` and residual columns `k != j`, with total mass

`boxed: Z1 = G/L_j^2`                                               (3.2)

whose normalized COLUMN law is exactly

`rho_k = d_k^2/G`.                                                  (3.3)

If `L_j=0`, then every `d_k=0`, contradicting `G>0`, so the positive-bank case automatically has `L_j>0`.

#### Proof

Equation (3.1) is the two-dimensional Gram determinant inequality:

`(u_j v_k-v_j u_k)^2 <= (u_j^2+v_j^2)(u_k^2+v_k^2)`.

For `W_k>0`, set

`eta_k = d_k^2/(L_j^2 W_k) in [0,1]`;                              (3.4)

set `eta_k=0` when `W_k=0`. Give both physical 1x1 minors `u_k` and `v_k` fractional coefficient `eta_k`. The retained order-one mass in column `k` is

`eta_k(u_k^2+v_k^2)=d_k^2/L_j^2`.

Summing proves (3.2), and normalization proves (3.3). This is an aggregate shadow before inversion: no minor is divided by its determinant. QED.

## 4. Third mixed 2/1 gate: payment or one macroscopic 2x2 minor

Use the same E2 packet from (2.2) as the order-two packet in `QFORM-MIXED21-FRACTIONAL-HALFRIESZ-v1`, and use Theorem 3.1 as the order-one packet. Apply the theorem on the COLUMN side.

The E2 column inclusion marginals are

`alpha_j^(2)=1`,
`alpha_k^(2)=rho_k` for `k != j`.

The E1 shadow has

`alpha_j^(1)=0`,
`alpha_k^(1)=rho_k`.

More generally, for any `1/2<h<1`, choose mixed weight `w=h`, `q=2h`, `r=1+h`. Then the mixed marginal is exactly

`p_j=h=q/2`,
`p_k=rho_k`.

Hence if

`max_(k != j) rho_k <= h`,                                         (4.1)

the r26 theorem gives the full-ambient half-Riesz estimate

`sup_t E |R-t|^(-1/2)
 <= C_21(h) G^(-1/[4(1+h)]) L_j^((1-h)/[2(1+h)]).`                 (4.2)

At `h=3/4`,

`boxed:
 sup_t E |R-t|^(-1/2)
 <= 27.2194298438 G^(-1/7) L_j^(1/14).`                             (4.3)

If (4.1) fails, there is a physical residual column `k0` such that

`d_k0^2 > h G`.                                                     (4.4)

Combining (4.4) with the two preceding near-coloop failures gives the clean three-stage selection law:

### Corollary 4.2 — `QFORM-E2-THREE-NEARCOLOOPS-MACROMINOR-v1`

Starting from E2 mass `Z`, if the first column gate, the second residual-row gate, and the third residual-column gate all fail at the same threshold `h`, then one actual physical `2x2` minor satisfies

`boxed: |det B_*|^2 > h^3 Z.`                                      (4.5)

At `h=3/4`,

`boxed: |det B_*|^2 > 27 Z/64.`                                    (4.6)

Thus the eventual selected minor is not a tiny representative. It carries more than 42 percent of the entire incoming determinant currency. The selection occurs only after determinant-weighted averaging has failed three times.

This is the main coordinate-minor selection result of the run.

## 5. Quantitative payment of the third gate in the scalar-Schur branch

Return to the inherited scalar peel. The standard square-kernel estimate gives

`||p_Q||_infinity
 <= |a|^(-1/2) sup_t E|R-t|^(-1/2).`                               (5.1)

If the third mixed gate pays, use (4.3), `G>9Z/16`, `L_j<=F`, and (2.1). Then

`||p_Q||_infinity
 < sqrt(2) * 27.2194298438 * (16/9)^(1/7)
   F^(19/14) H^(-11/28)`.

Numerically,

`boxed:
 ||p_Q||_infinity
 < 41.792 F^(19/14) H^(-11/28).`                                   (5.2)

If a preceding branch supplies `H>=c F^6`, (5.2) becomes

`||p_Q||_infinity < 41.792 c^(-11/28) F^(-1)`.

This establishes essential boundedness in the stated branch. Continuity is NOT promoted by this half-Riesz/scalar-square argument.

## 6. If the third gate fails: a macroscopic edge and a partner pair-tail payment

Assume now (4.6). Since for a `2x2` matrix all four entries bounded by `beta` imply `|det|<=2 beta^2`, the selected physical cross minor contains a physical edge of magnitude at least

`beta >= sqrt(|det B_*|/2)
      > [sqrt(3 sqrt(3))/4] Z^(1/4)`.

Put

`c_edge = sqrt(3 sqrt(3))/4 = 0.5698767642386944...`.               (6.1)

Using `Z>=H/F^2`,

`boxed: beta > c_edge H^(1/4) F^(-1/2).`                            (6.2)

Because `C` is an actual symmetric Schur remainder on original coordinates, this edge belongs to an actual physical principal pair

`P_beta = [[d_r,beta],[beta,d_c]]`.

There is an exhaustive deterministic alternative:

* either `max(|d_r|,|d_c|) >= |beta|/2`, producing a second quantitatively large physical diagonal in the remainder;
* or both diagonals have magnitude `<|beta|/2`, in which case the pair is invertible indefinite and

`boxed: Delta:=|det P_beta| >= 3 beta^2/4,`                          (6.3)
`boxed: kappa:=sigma_min(P_beta) >= |beta|/2.`                      (6.4)

Indeed `det P_beta=d_r d_c-beta^2 <= -3 beta^2/4`, while `||P_beta||op <= 3|beta|/2`, so `kappa=Delta/||P_beta||op >= |beta|/2`.

We now apply the completed designated-partner theorem account02/B07 `QFORM-PAIRTAIL-CURVATURE-RECEIVER-v1` to this ACTUAL principal pair in the ACTUAL Schur remainder. Let `D` be any allowed disjoint physical far cross block of the post-scalar remainder before pair completion, and let

`T_2(D)=sum_(m>=3) s_m(D)^2`.

The partner theorem gives the density of the remainder variable `R`:

`||p_R||_infinity
 <= C_* Delta^(-2/5) kappa^(-1/10) T_2(D)^(-1/20),`                 (6.5)

with `C_*=26.00795741955...`, whenever `T_2(D)>0`.

To feed this into the already-existing outer scalar square without making an unjustified density-convolution claim, use the elementary implication

### Lemma 6.1 — bounded density implies a half-Riesz bound

If a real random variable `Y` has a density bounded by `M`, then

`boxed: sup_t E|Y-t|^(-1/2) <= 4 sqrt(M).`                          (6.6)

Proof: for every `r>0`, split at `|Y-t|=r`:

`E|Y-t|^(-1/2)
 <= 4 M sqrt(r) + r^(-1/2)`.

Choose `r=1/(4M)`. QED.

Combining (6.3)--(6.6) with the scalar peel (5.1) gives

`||p_Q||_infinity
 <= 22.369299 |a|^(-1/2)
    |beta|^(-9/20) T_2(D)^(-1/40).`                                 (6.7)

In particular, if the actual far block has quantitative tail

`T_2(D) >= tau beta^2`,                                             (6.8)

then

`boxed:
 ||p_Q||_infinity
 <= 22.369299 tau^(-1/40) |a beta|^(-1/2).`                         (6.9)

Finally substitute (2.1) and (6.2):

`boxed:
 ||p_Q||_infinity
 < 41.907 tau^(-1/40) F^(5/4) H^(-3/8).`                            (6.10)

Again, if `H>=cF^6`, this is exactly natural scale:

`||p_Q||_infinity
 < 41.907 c^(-3/8) tau^(-1/40) F^(-1).`

This is the required actual application of a completed account02/B07 theorem to a new inequality produced in this run. The application occurs only after the determinant bank has forced a macroscopic physical minor and then a macroscopic physical edge; no tiny reciprocal minor is used.

I claim essential boundedness only in this partner branch. The cited pair-tail theorem does not state continuity at this scope, and Lemma 6.1 also does not add continuity.

## 7. Exact remaining survivor

After the present run, the inherited E2 double-near-coloop state is exhausted into the following branches:

1. third mixed 2/1 half-Riesz payment, equation (5.2);
2. a selected macroscopic physical `2x2` minor carrying `>27/64` of the whole E2 determinant currency;
3. from that minor, a physical edge satisfying (6.2);
4. from that edge, either a second large physical diagonal, or a quantitatively conditioned indefinite physical pair satisfying (6.3)--(6.4);
5. for the conditioned pair, the completed partner receiver pays every branch with `T_2(D)>=tau beta^2` by (6.10).

Therefore the genuinely unpaid descendant is now

`QFORM-MACROMINOR-SECOND-DIAGONAL-OR-RANK2-TAIL-TUBE-v1`:

* either the Schur remainder contains a second physical diagonal `>=beta/2`, or
* it contains the quantitative indefinite pair above but every relevant far cross block is in the rank-two Frobenius tube

`T_2(D)<tau beta^2`.

The nonzero tail is retained; it is not deleted. This is narrower than the previous one-sided E2 near-coloop or double-near-coloop obstruction.

A promising next mechanism is to combine the macroscopic-minor certificate (4.6) with the current orientation-free exact-rank-two affine half-Riesz theorem on the low-tail tube, but only after proving a perturbative interface that keeps the nonzero rank-two-tail error. The current source explicitly warns that the exact-rank-two theorem cannot simply be applied to an arbitrary higher-rank form with two large eigenvalues, so that step remains unpaid.

## 8. Deterministic regression check

A 20,000-sample random-matrix check verified (3.1) with zero violations. The closest sampled ratio `(L_j^2 W_k)/d_k^2` was `1.000000000018...`, showing the inequality is sharp. This is only a regression check; the proof is the two-dimensional Gram inequality above.

## 9. Status

`QFORM-FULL`: OPEN.  
`QFORM-CONTINUOUS-REPRESENTATIVE`: OPEN.  
New proved supporting claims:

* `QFORM-FIXEDPAIR-E2-EXACT-E1-COLUMN-SHADOW-v1`;
* `QFORM-E2-THREE-NEARCOLOOPS-MACROMINOR-v1`;
* the scale-sensitive third-gate payment (5.2);
* the macroscopic-edge corollary (6.2);
* the partner pair-tail descendant payment (6.10).

No full-solution claim is made.
