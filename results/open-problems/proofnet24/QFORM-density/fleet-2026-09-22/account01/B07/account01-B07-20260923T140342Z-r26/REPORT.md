SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T14:03:42Z.
attacking: the E2 near-coloop survivor by an exact anchored E2-to-E1 determinant shadow and a mixed order-2/order-1 half-Riesz receiver; in parallel, downshift the latest account02/B07 support-diffuse star-star-Frobenius currency without selecting a reciprocal minor.

# account01/B07 r26 — E2→E1 shadow, mixed 2/1 half-Riesz, and star-star-F collision splitting

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `account01-B07-20260923T140342Z-r26`  
Owner control: revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **ESSENTIAL STEP APPLIED / NEW E2→E1 FRACTIONAL SHADOW + MIXED 2/1 HALF-RIESZ RECEIVER / LATEST DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.

The unrestricted theorem is not claimed. All probabilistic conditioning is in ORIGINAL independent coordinates. No Gaussian, moment, log-concavity, compact-support, connected-support, diagonal-basis, or independence-after-rotation hypothesis is added. The report does not use the refuted law-uniform pointwise quadratic-phase estimate, arbitrary-joint coarea bound, positive conditional projection-density moment, naive fiber-sup integration, or a one-good-minor reciprocal reduction. Continuity is tracked separately.

## 1. Sources actually consumed

1. Own preceding B07 report:
   `yspennstate/math-open-problems@fa0ddeb784bad52ae142e49e7c9448d4772decf8`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T130435Z-r25/REPORT.md`.
   It proves `QFORM-E2-FRACTIONAL-TRACE-v1`, the scalar-square peel, and leaves an E2 near-coloop `theta_j>3/4` as the first large-diagonal obstruction.
2. Own mixed-compound derivation:
   `yspennstate/math-open-problems@7bf5a0bd8a8d2fa12a5c2370811ecfe5d2cf7444`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T090322Z-r20/REPORT.md`.
   Its determinant expansion / Lieb--Brascamp--Lieb / Hausdorff--Young calculation is reused below with compound orders 2 and 1; only the final fractional integration changes.
3. Latest completed designated partner account02/B07:
   `yspennstate/math-open-problems@d57825ed929db0db057013ee2a12d547fd7cacac`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T133358Z-account02-B07-qform-r11auto/REPORT.md`.
   Its genuinely support-diffuse residual-E3 survivor supplies, in the notation of Section 5 below,
   `||r|| ||c|| ||E||_F > (sqrt(2)/3) a^3`.

The current brain control and live correction ledger were refreshed immediately before publication; no later B07 stop was observed.

## 2. Mixed order-2/order-1 characteristic-function theorem

The r20 determinant argument is not special to orders 3 and 2. The next statement is the exact version needed for an E2 packet with a fixed physical row.

### Theorem 2.1 — `QFORM-MIXED21-FRACTIONAL-HALFRIESZ-v1`

Let `M=A[I,J]` be any cross block between disjoint ORIGINAL-coordinate banks. Let `P2` be a positive fractional packet of physical `2x2` minors and `P1` a positive fractional packet of physical `1x1` minors, with coefficients in `[0,1]`, masses

`Z2 = sum_(S,T) theta_2(S,T) det M[S,T]^2 >0`,
`Z1 = sum_(i,j) theta_1(i,j) M_ij^2 >0`.

Let `alpha_i^(2), alpha_i^(1)` be their normalized row inclusion marginals. Choose `0<w<1`, set

`r = 1+w`,
`p_i = w alpha_i^(2) + (1-w) alpha_i^(1)`,
`K_w = w^(-w) (1-w)^(-(1-w)) Z2^w Z1^(1-w)`.

If for some

`1 <= q < r`

we have the one-sided gate

`max_i p_i <= q/2`,

then for the FULL ambient quadratic-plus-affine form `R` (arbitrary same-bank curvature, arbitrary outside couplings, all other spectrum retained),

`boxed:
 sup_s E |R-s|^(-1/2)
 <= [4 r sqrt(e/2)/(r-q)] q^(-1/4) K_w^(-1/(4r)).
}`

The transposed column-side version is identical.

#### Proof

Condition outside `I union J`; the conditional phase has arbitrary same-bank functions plus the bilinear term `2 X_I^T M X_J`. Original-coordinate Weyl differencing in `X_J`, exactly as in r20, gives

`|phi_R(t)|^2 <= E_D prod_(i in I) |psi_i(2t(MD)_i)|`,

with the difference coordinates independent and their densities bounded by one.

For positive Gaussian parameters `D_I=diag(d_i)`, `D_J=diag(e_j)`, the diagonal-plus-Gram identity is

`det(D_J+M^T D_I M)
 = sum_(k>=0) sum_(|S|=|T|=k)
   det M[S,T]^2 prod_(i in S)d_i prod_(j notin T)e_j`.

All summands are nonnegative, so retain the fractional order-2 and order-1 packet sums. Weighted AM--GM inside each packet, followed by weighted AM--GM between the two retained sums, gives

`det(D_J+M^T D_I M)
 >= K_w prod_i d_i^(p_i) prod_j e_j^(c_j)`,

where the column exponents are the corresponding mixed complement marginals. The same Gaussian-exhaustion calculation as r20 therefore gives the Brascamp--Lieb constant

`C_BL <= K_w^(-1/2) prod_i p_i^(-p_i/2) prod_j c_j^(-c_j/2)`.

Apply Jensen with power `q` and the scalar Hausdorff--Young estimate. The gate `p_i<=q/2` ensures every required Fourier exponent `q/p_i` is at least two. The identical entropy cancellation from r20 yields

`|phi_R(t)|
 <= min{1,
   e^(r/(2q)) q^(-r/(4q)) K_w^(-1/(4q))
   pi^(r/(2q)) |t|^(-r/(2q)) }`.

Equivalently, with

`t0 = pi e q^(-1/2) K_w^(-1/(2r))`,

`|phi_R(t)| <= min{1,(t0/|t|)^(r/(2q))}`.

Because `q<r`, the exponent `r/(2q)` is strictly larger than `1/2`. Under the Fourier convention used in r20/r25,

`widehat{|x|^(-1/2)}(t)=sqrt(2pi)|t|^(-1/2)`.

Abel regularization followed by monotone convergence gives

`sup_s E|R-s|^(-1/2)
 <= (2pi)^(-1/2) integral_R |phi_R(t)| |t|^(-1/2) dt`.

Writing `alpha=r/(2q)`, direct integration gives

`integral_R min{1,(t0/|t|)^alpha}|t|^(-1/2)dt
 = [4r/(r-q)] sqrt(t0)`.

Substitution of `t0` proves the theorem. No density claim for an order-2 or order-1 form alone is being made. QED.

## 3. Exact anchored E2→E1 determinant shadow

Let `C` be a physical cross block. Fix one physical row `s` and one physical column `j`. Define the complete doubly anchored second-volume bank

`G = sum_(i!=s,k!=j)
      det C[{s,i},{j,k}]^2 >0`.

For each residual physical row `i!=s`, put

`g_i = sum_(k!=j) det C[{s,i},{j,k}]^2`,
`R_s = ||C[s,*]||_2`,
`W_i = ||C[i,*]||_2^2`.

Then `G=sum_i g_i`.

### Theorem 3.1 — `QFORM-ANCHORED-E2-EXACT-E1-SHADOW-v1`

For every residual row `i`,

`boxed: g_i <= R_s^2 W_i.`

Consequently there is a fractional physical order-1 determinant packet, supported away from row `s`, with total mass

`boxed: Z1=G/R_s^2`

whose normalized row law is exactly

`mu_i=g_i/G`.

#### Proof

Cauchy--Binet for the complete two-row matrix gives

`g_i
 <= sum_(|T|=2) det C[{s,i},T]^2
 = det( C[{s,i},:] C[{s,i},:]^T )`.

For two vectors `u=C[s,:]`, `v=C[i,:]`, their Gram determinant is

`||u||^2||v||^2-<u,v>^2 <= R_s^2 W_i`,

proving the inequality.

When `W_i>0`, set

`eta_i=g_i/(R_s^2 W_i) in [0,1]`;

set `eta_i=0` if `W_i=0`. Give every physical `1x1` minor in residual row `i` the fractional coefficient `eta_i`. The retained order-1 mass in row `i` is

`eta_i sum_k C_ik^2 = g_i/R_s^2`.

Summing gives `Z1=G/R_s^2`, and normalization gives precisely `mu_i`. No coordinate minor is inverted or individually selected. QED.

## 4. Pay a one-column E2 near-coloop unless a second physical near-coloop appears

Normalize the anchored E2 bank `G` itself. Its row inclusion marginals are

`alpha_s^(2)=1`,
`alpha_i^(2)=mu_i` for `i!=s`.

The shadow of Theorem 3.1 has

`alpha_s^(1)=0`,
`alpha_i^(1)=mu_i`.

More generally, for every `h in (1/2,1)`, choose

`w=h`, `q=2h`, `r=1+h`.

Then at the fixed row,

`p_s=h=q/2`,

while every residual row has `p_i=mu_i`. Thus if `max_i mu_i<=h`, Theorem 2.1 applies and yields

`boxed:
 sup_t E|R-t|^(-1/2)
 <= C_21(h) G^(-1/[4(1+h)])
              R_s^((1-h)/[2(1+h)]),
}`

where

`C_21(h)
 = [4(1+h)/(1-h)] sqrt(e/2)(2h)^(-1/4)
   [h^(-h)(1-h)^(-(1-h))]^(-1/[4(1+h)]).`

At the threshold needed by r25, `h=3/4`,

`boxed:
 sup_t E|R-t|^(-1/2)
 <= 27.2194298438 G^(-1/7) R_s^(1/14).
}`

This is `QFORM-E2-ONECOLOOP-MIXED21-PAYMENT-v1`.

Now apply it to the exact r25 scalar-Schur state. There the incident E2 packet has total mass `Z=Z2^S` and a fixed physical row `s`; if the old q=3/2 E2 receiver fails, a physical column `j` has inclusion marginal

`theta_j>3/4`.

Let `G_j` be the part of that same packet whose column pair contains `j`. Then

`G_j=theta_j Z >3Z/4`.

Condition on this anchored packet and write its residual-row law as `mu_i`. If `max mu_i<=3/4`, the new theorem gives

`sup_t E|R-t|^(-1/2)
 < 27.2194298438 (3Z/4)^(-1/7) R_s^(1/14).`

Using the r25 scalar-square peel

`||p_Q||_infinity <= |a|^(-1/2) sup_t E|R-t|^(-1/2)`,

together with its exact lower bounds

`|a| >= sqrt(H)/(2F^2)`,
`Z >= H/F^2`,

we get the explicit natural-scale payment

`boxed:
 ||p_Q||_infinity
 <= 40.1090534232 F^(9/7) H^(-11/28) R_s^(1/14).
}`

In the same principal-pair large-diagonal branch one has `|a|>=|b|/2`; with the r25 notation `v'=v-(b/a)u`, this implies

`R_s=||v'|| <= ||v||+2||u|| <=3F`.

Therefore

`boxed:
 ||p_Q||_infinity
 <= 43.389\, F^(19/14) H^(-11/28).
}`

(the displayed constant is deliberately rounded upward). If a preceding branch supplies `H>=cF^6`, this scales exactly as `c^(-11/28)F^(-1)`. This is an essential-supremum payment; continuity is not promoted by this half-Riesz/scalar-square argument.

If the new payment fails, there is a residual physical row `i0` with

`mu_i0>3/4`.

Hence

`g_i0 > (3/4)G_j > (9/16)Z`.

Thus the formerly one-sided E2 near-coloop is reduced to a concrete **double near-coloop**:

`boxed:
 sum_(k!=j) det C[{s,i0},{j,k}]^2 > (9/16) Z.
}`

This retains more than 56 percent of the entire incoming E2 currency on one fixed physical row pair and one fixed physical column, before any reciprocal pivot. The transposed statement is identical.

## 5. Actual use of the latest designated partner account02/B07

The latest completed designated partner leaves, on its genuinely support-diffuse residual-E3 branch, the exact physical decomposition

`D=[[b,r^T],[c,E]]`

and proves that one lower-compound alternative is

`boxed:
 ||r||_2 ||c||_2 ||E||_F > (sqrt(2)/3) a^3.
}`

I now apply that completed partner inequality to a new exact collision selector.

### Lemma 5.1 — `QFORM-STARSTAR-E1-COLLISION-OR-FOURBANK-v1`

For arbitrary nonzero physical star vectors `c,r` and a nonzero physical matrix `E`, write

`C=||c||_2`, `R=||r||_2`, `F_E=||E||_F`.

Then at least one of the following holds:

1. a physical row coefficient satisfies `|c_i|>=C/2`;
2. a physical column coefficient satisfies `|r_j|>=R/2`;
3. there are four pairwise disjoint residual physical banks `L0,L1` on the row side and `R0,R1` on the column side such that

`boxed:
 ||c_L0||_2 ||r_R0||_2 ||E[L1,R1]||_F
 > C R F_E/(4sqrt(2)).
}`

#### Proof

Let

`p_i=c_i^2/C^2`, `q_j=r_j^2/R^2`,
`u_i=||E[i,*]||^2/F_E^2`, `v_j=||E[*,j]||^2/F_E^2`.

Define collision probabilities

`A_c=sum_i p_i u_i`, `A_r=sum_j q_j v_j`.

If `A_c>=1/4`, then `max_i p_i>=A_c>=1/4`, proving alternative 1. Similarly `A_r>=1/4` proves alternative 2.

Assume both are below `1/4`. Independently sample `I` with law `p`, `J` with law `q`, and an edge `(K,L)` with law `E_KL^2/F_E^2`. Then

`P(I=K)=A_c`, `P(J=L)=A_r`,

so by the union bound

`P(I!=K and J!=L)>1/2`.

Equivalently,

`sum_(i!=k,j!=l) c_i^2 r_j^2 E_kl^2
 > (1/2) C^2 R^2 F_E^2.`

Independently two-color the residual row coordinates into `L0,L1` and the residual column coordinates into `R0,R1`. A disjoint monomial with roles `(i,k;j,l)` is retained in the prescribed role colors `(L0,L1;R0,R1)` with probability `1/16`. Therefore some coloring satisfies

`||c_L0||^2 ||r_R0||^2 ||E[L1,R1]||_F^2
 > C^2R^2F_E^2/32`.

Taking square roots proves alternative 3. QED.

Applying the partner inequality gives the actual quantitative consequence:

- in alternative 1,
  `|c_i| ||r|| ||E||_F > (sqrt(2)/6)a^3`;
- in alternative 2,
  `|r_j| ||c|| ||E||_F > (sqrt(2)/6)a^3`;
- in alternative 3,
  `boxed: ||c_L0|| ||r_R0|| ||E[L1,R1]||_F > a^3/12.`

Thus the partner's star-star-Frobenius branch is no longer an unstructured three-factor norm. It is reduced to a physical collision coefficient or to four mutually disjoint ORIGINAL-coordinate banks with a dimension-free product lower bound. No selected determinant is reciprocated. This does not yet pay arbitrary same-bank far curvature; it supplies the next product-preserving receiver with separated provenance.

## 6. What changed / first remaining implication

Two previously separate B07 debts have narrowed.

**Large-diagonal / E2 near-coloop debt.** The one-column near-coloop of r25 is now analytically paid unless conditioning the determinant law on that column creates a second row near-coloop. The sole survivor carries more than `9/16` of the incoming E2 mass on a fixed physical row pair plus fixed physical column. The next precise obligation is

`QFORM-E2-DOUBLE-NEARCOLOOP-RECEIVER-v1`:

spend that `>9/16` fixed-row-pair/fixed-column E2 packet while retaining the exact nonzero Schur tail and arbitrary same-bank curvature.

**Partner support-diffuse E3 debt.** The edge-times-E2 partner branch remains available separately. Its star-star-F branch now reduces to a literal star collision or a four-disjoint-bank product `>a^3/12`. The next obligation there is

`QFORM-FOURBANK-STARSTAR-E1-CURVATURE-RECEIVER-v1`:

combine the two separated hub-star banks and the separated E1 cross energy before taking reciprocals; arbitrary far curvature must remain in the phase.

Neither obligation is the full conjecture. Full QFORM remains OPEN; full-target continuity remains OPEN.

## 7. Integrity / checks

The mixed-2/1 theorem is an algebraic reuse of the already source-pinned r20 determinant/BL proof with the compound orders changed from `(3,2)` to `(2,1)`. The half-Riesz integral is computed explicitly and the `h=3/4` constant equals `27.2194298438`. The star collision lemma is an exact probability/coloring identity. Finite numerical checks, if used, are regression evidence only and are not premises of these proofs.

Pre-publication control source: `yspennstate/math-research-brain@c96d67458e3b0b131ee625b6003344143caabe20`; OWNER CONTROL revision `2026-09-22.15`; no B07 pause. Execution remains `WITHOUT_VERIFIED_BRAIN`: repository reads/writes are not authenticated native learned-memory ingestion.
