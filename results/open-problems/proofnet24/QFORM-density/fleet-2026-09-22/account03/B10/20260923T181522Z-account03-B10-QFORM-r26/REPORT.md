SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-23T18:15:22Z.
attacking: the positive-leakage near-null physical-hub collar; force the surviving leaves below the projected-volume marginal threshold and apply the new arbitrary-rank projected-crossing receiver at an actual rank-three factorization.

# account03/B10 r26 — 1/61 transverse payment and projected-crossing Pluecker bridge

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository transport was used, no authenticated native-brain receiver was invoked.  
Classification: `NEW SUPPORTING THEOREMS / PROJECTED-CROSSING MARGINAL GATE CLOSED / FULL QFORM OPEN`.


The current correction boundary is retained: no independence after spectral rotation, no arbitrary-joint coarea cap, no conditional projection-height shortcut, no law-uniform pointwise quadratic-phase decay, no moment/support/log-concavity hypothesis, and no perturbative deletion of a small random quadratic term.

## 1. Exact live near-coloop state

I use the already established B10 reduction, in particular the near-coloop state recorded in

`yspennstate/math-open-problems@b364b657106d0ea3dc67404808c6708e20ccac4d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T044329Z-account03-B10-QFORM-r24/REPORT.md`

and the positive-leakage checkpoint

`yspennstate/math-open-problems@17509df0fcf11b1522e5f8c199eee51b67d00fde`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T141808Z-account03-B10-QFORM-r25/CHECKPOINT.md`.

Thus, after all previously paid exits, the exact-rank-three form can be written

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`, `D:=|det M|>=1`,               (1.1)

with an ORIGINAL physical hub row

`u_0=sqrt(c)e`, `||e||=1`, `c>63/64`,                                  (1.2)

and positive leakage

`rho:=1-c`, `0<rho<1/64`.                                                (1.3)

The physical pivot and normalized Rayleigh quotient obey

`|A_00|<1/64`, `alpha:=e^T M e`, `|alpha|<1/16`.                         (1.4)

Every leaf row has the unique decomposition

`u_j=t_j e+p_j`, `p_j perpendicular e`.                                 (1.5)

Parseval gives the exact ledger

`sum_j t_j^2=rho`, `sum_j t_j p_j=0`, `sum_j p_j p_j^T=I_2`.             (1.6)

In particular

`|t_j|<1/8` for every leaf.                                               (1.7)

The aim is not to replace the leaves by independent spectral coordinates; all partitions below are partitions of ORIGINAL coordinates.

## 2. New leakage-improved compression: every surviving leaf has transverse leverage <1/61

### Lemma 2.1 — `QFORM-NEARCOLOOP-1OVER61-WITT-v1`

Let a leaf be `u=t e+p` and put `h=||p||^2`. If

`h>=1/61`,                                                               (2.1)

then at least one of

`|e^T M u|>=1/64`,                                                       (2.2)

`|u^T M u|>=1/128`                                                       (2.3)

holds.

#### Proof

Put `v=p/sqrt(h)`, and abbreviate

`b=e^T M u`, `q=u^T M u`.

In the orthonormal basis `(e,v)` of `E=span(e,v)`, the compression of `M` to `E` is

`C=[[alpha,delta],[delta,zeta]]`,                                        (2.4)

with the exact identities

`delta=(b-alpha t)/sqrt(h)`,                                             (2.5)

`zeta=(q-2tb+alpha t^2)/h`.                                              (2.6)

Suppose both (2.2) and (2.3) fail. Since `h>=1/61`, we have `1/sqrt(h)<=sqrt(61)<8`; together with (1.4) and (1.7),

`|delta|<8(1/64+1/128)=3/16`.                                            (2.7)

Similarly,

`|zeta|<61(1/128+1/256+1/1024)=793/1024`.                               (2.8)

Thus the absolute row sums of `C` are bounded by

`1/16+3/16=1/4`,                                                         (2.9)

`3/16+793/1024=985/1024<1`.                                             (2.10)

Therefore `||C||_op<1`.

But `E` has dimension two while `E^perp` has dimension one. Hence the map

`P_(E^perp) M |_E : E -> E^perp`

has a nonzero kernel. Choose a unit `z` in that kernel. Then `Mz` lies in `E`, so

`||Mz||=||Cz||<1`,                                                       (2.11)

contradicting `sigma_min(M)>=1`. QED.

The improvement from the earlier `1/4` gate to `1/61` comes from using the actual leakage estimate `|t|<1/8`; no upper bound on `||M||` enters.

### Theorem 2.2 — `QFORM-NEARCOLOOP-1OVER61-TRANSVERSE-PAYMENT-v1`

Every near-coloop state having a leaf with `||p_j||^2>=1/61` has an essentially bounded density with

`||p_Q||_infinity<1204`.                                                 (2.12)

#### Proof

Use Lemma 2.1.

If `|A_jj|=|u_j^T M u_j|>=1/128`, then `||u_j||^2>=1/61`. The completed exact-rank-three scalar-pivot consequence of the affine rank-two half-Riesz theorem,

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

gives

`||p_Q||_infinity <=128[(1/61)(1/128)D]^(-1/4)`

`<=128(61*128)^(1/4)=1203.219664...<1204`.                               (2.13)

Otherwise `|A_jj|<1/128` and Lemma 2.1 yields `|e^T M u_j|>=1/64`. The physical cross coefficient satisfies

`|A_0j|=sqrt(c)|e^T M u_j|>=sqrt(63)/512`.                              (2.14)

Together with `|A_00|<1/64` and `|A_jj|<1/128`, the physical pair is indefinite, since

`A_0j^2 >=63/262144 > 1/8192 > |A_00 A_jj|`.                            (2.15)

Its smaller singular value obeys

`kappa >= |A_0j|-(|A_00|+|A_jj|)/2`

`>= (sqrt(63)-6)/512 >1/265`.                                           (2.16)

For this same fixed pair, the exact rank-three determinant-bank identity gives

`P_0j:=sum_(k!=0,j)|det A_{ {0,j,k} }|`

`=D [||u_0||^2||u_j||^2-<u_0,u_j>^2]`

`=D c ||p_j||^2 >=63/(64*61)`.                                          (2.17)

Apply the completed B10 theorem `QFORM-INDEFINITE-PAIR-SCHUR-BANK-v1`, source

`yspennstate/math-open-problems@11505bc9c70f8dfc4c587dbdb2ebaeee1dd0ca04`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T204046Z-account03-B10-QFORM-r17/REPORT.md`.

It gives

`||p_Q||_infinity <=8*2^(3/4)(kappa P_0j)^(-1/4)`

`<8*2^(3/4)[(1/265)63/(64*61)]^(-1/4)`

`=152.305739...<153`.                                                    (2.18)

Combining (2.13) and (2.18) proves (2.12). QED.

Consequently every still-unpaid near-coloop state now satisfies the stronger pointwise geometric gate

`boxed: ||p_j||^2<1/61 for every leaf j.`                               (2.19)

No continuity claim is made for Theorem 2.2 because the scalar-pivot and pair-Schur inputs are used only at their established essential-boundedness level.

## 3. New exact factorization of the one-hub projected-crossing resource

The fresh independently checked projected-crossing theorem is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For one original hub and `ell=2`, it states that if the projected crossing has two-volume row marginals at most `1/2`, then

`||p_Q||_infinity <=3*2^(7/6)*exp(1/3)(s^2 Z_2)^(-1/6)`

`<9.4 (s^2 Z_2)^(-1/6)`,                                               (3.1)

where `s=||g_J||_2` is the hub-to-`J` cross-row norm and `Z_2=e_2(CC^T)` for the crossing projected orthogonally to that row. Arbitrary internal hub functions, all light diagonals, and arbitrary terms internal to either light side are allowed.

The following identity computes exactly the receiver resource for an exact-rank-three form.

### Lemma 3.1 — `QFORM-HUB-PROJECTED-CROSSING-PLUECKER-FACTORIZATION-v1`

Split the leaf ORIGINAL coordinates into disjoint sets `I,J`. Let

`g_J=A_{0,J}`, `s^2=||g_J||_2^2`,                                      (3.2)

`C=A_{I,J}(I-Pi_row(g_J))`,                                            (3.3)

`G_I=sum_(i in I) p_i p_i^T` on `e^perp`,                              (3.4)

`H_J=sum_(j in J) u_j u_j^T` on `R^3`.                                (3.5)

If `det G_I det H_J>0`, then automatically `s>0`, `Z_2(C)>0`, and

`boxed: s^2 Z_2(C)=D^2 c det(G_I)det(H_J).`                            (3.6)

Moreover the two-volume row marginal of `C` at row `i in I` is exactly

`boxed: alpha_i(C)=p_i^T G_I^(-1)p_i.`                                (3.7)

#### Proof

For two distinct rows `i,k in I`, the Gram determinant after projecting the two rows `A_{i,J},A_{k,J}` orthogonally to `g_J` satisfies the Schur-Gram identity

`s^2 det(C_{ {i,k} } C_{ {i,k} }^T)`

`=det Gram(g_J,A_{i,J},A_{k,J})`.                                     (3.8)

Cauchy-Binet on the right gives

`det Gram(g_J,A_{i,J},A_{k,J})`

`=sum_(K subset J, |K|=3) det(A_{ {0,i,k},K})^2`.                     (3.9)

Because `A=RMR^T` has exact rank three,

`det(A_{S,K})=det(R_S)det(M)det(R_K)`                                 (3.10)

for every physical triples `S,K`. Since the hub row is `sqrt(c)e`,

`det(R_{ {0,i,k} })^2=c det(p_i,p_k)^2`.                              (3.11)

Also Cauchy-Binet on the `J` spectral rows gives

`sum_(K subset J, |K|=3)det(R_K)^2=det(H_J)`.                          (3.12)

Combining (3.8)-(3.12),

`s^2 det(C_{ {i,k} } C_{ {i,k} }^T)`

`=D^2 c det(H_J) det(p_i,p_k)^2`.                                     (3.13)

Summing over `i<k` in `I` and using the two-dimensional Cauchy-Binet identity

`sum_(i<k in I)det(p_i,p_k)^2=det(G_I)`                               (3.14)

proves (3.6). Positivity of the right side forces both `s` and `Z_2` positive.

For a fixed `i`, summing (3.13) only over pairs containing `i` and dividing by (3.6) gives

`alpha_i(C)= [sum_(k!=i)det(p_i,p_k)^2]/det(G_I)`.

In two dimensions the numerator is `det(G_I) p_i^T G_I^(-1)p_i`, proving (3.7). QED.

The identity is useful because it exposes the full projected-crossing currency before any reciprocal local minor is selected.

## 4. The 1/61 gate automatically supplies the projected-crossing row-marginal hypothesis

Let

`G=sum_j p_jp_j^T=I_2`,                                               (4.1)

`H=sum_j u_ju_j^T=I_3-c ee^T`.                                       (4.2)

Hence

`det G=1`, `det H=rho`.                                                (4.3)

Define transverse pair weights

`a_{ik}=det(p_i,p_k)^2`, `i<k`;                                       (4.4)

then `sum a_{ik}=1`. Define leaf triple weights

`b_K=det(u_K)^2`, `|K|=3`;                                            (4.5)

then `sum b_K=rho`.

Think of an `a`-weighted random pair and an independently chosen normalized `b/rho` random triple. The row marginal of the pair law at `i` is

`sum_(k!=i)a_{ik}=||p_i||^2<1/61`                                    (4.6)

because `G=I_2`. The three row marginals of the normalized triple law sum to three. Therefore, by a union bound, the probability that the random pair intersects the random triple is strictly less than

`3/61`.                                                               (4.7)

Equivalently, the total disjoint pair-triple Pluecker mass is strictly larger than

`(58/61)rho`.                                                          (4.8)

Now colour every leaf independently: put it in `I` with probability `2/5` and in `J` with probability `3/5`. Expanding `det G_I det H_J` in the pair and triple Pluecker bases, only disjoint pair-triple configurations can occur simultaneously. A fixed disjoint pair and triple land in the required sides with probability

`(2/5)^2(3/5)^3=108/3125`.                                            (4.9)

Hence

`E[det G_I det H_J]`

`>(108/3125)(58/61)rho`

`=(6264/190625)rho`.                                                   (4.10)

Thus some deterministic original-coordinate partition satisfies

`boxed: det G_I det H_J >(6264/190625)rho.`                           (4.11)

Because `0<=H_J<=H`, determinant monotonicity for positive semidefinite matrices gives

`det H_J<=det H=rho`.                                                  (4.12)

Therefore

`det G_I>6264/190625>2/61`.                                           (4.13)

Since `0<=G_I<=I_2`, its largest eigenvalue is at most one, so

`lambda_min(G_I)>=det G_I>2/61`.                                      (4.14)

Using (2.19), every `i in I` then satisfies

`p_i^T G_I^(-1)p_i <= ||p_i||^2/lambda_min(G_I)`

`<(1/61)/(2/61)=1/2`.                                                  (4.15)

By Lemma 3.1 these are exactly the two-volume row marginals of the projected crossing `C`. Therefore the newest projected-crossing theorem applies without any further spread assumption.

This proves the new structural statement

### Theorem 4.1 — `QFORM-NEARCOLOOP-PROJECTED-CROSSING-MARGINAL-GATE-v1`

In every still-unpaid exact-rank-three near-coloop state, there exists an original-coordinate split `L=I sqcup J` such that the one-hub arbitrary-rank projected-crossing receiver has all of its `ell=2` volume marginals below `1/2`, and

`boxed: s^2 Z_2 > (6264/190625) D^2 c rho.`                            (4.16)

Consequently the law has a continuous density with

`||p_Q||_infinity`

`<3*2^(7/6)*exp(1/3)[(6264/190625)D^2 c rho]^(-1/6)`

`<16.652 rho^(-1/6)`.                                                 (4.17)

The final numerical inequality uses `D>=1`, `c>63/64`.

Equation (4.17) is a genuine density estimate for arbitrary rough cap-one product laws in this branch and keeps every internal light quadratic term. It is intentionally **not** a universal endpoint estimate because it deteriorates as the positive leakage `rho=1-c` tends to zero. This deterioration is structural for this particular projected-crossing currency: at `rho=0` the leaf spectral Gram has rank two and the right side of (3.6) vanishes. The exact-null endpoint is paid by a different mixed-Fresnel mechanism, so the remaining task is a stable gluing mechanism, not another row-marginal proof.

## 5. Designated partner account04/B10 applied at an actual inequality

The completed designated-partner theorem is

`QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1`,

source

`yspennstate/math-open-problems@afdea9634d9e3f5fb09659da436292cf7dbe5b20`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B10/20260923T061725Z-account04-B10-QFORM-r4/REPORT.md`.

Apply it to the **whole current leaf bank**. Here its transverse Gram is exactly `G=I_2`, and the global regression vector vanishes because `sum t_jp_j=0`. Thus its regression residuals are simply `e_j=t_j`, with

`rho=sum_j e_j^2=1-c`.                                                 (5.1)

The partner theorem therefore supplies disjoint original-coordinate banks

`S,Y,Z`

with

`rho_S M(G_Y,G_Z)>=(2/81)rho`.                                        (5.2)

Since `G_Y+G_Z<=I_2`,

`M(G_Y,G_Z)<=det(G_Y+G_Z)<=1`,                                       (5.3)

and since `rho_S<=rho`, equation (5.2) yields both actual inequalities

`boxed: rho_S >=(2/81)rho`,                                           (5.4)

`boxed: M(G_Y,G_Z)>=2/81`.                                            (5.5)

In particular

`det(G_Y+G_Z)>=2/81`.                                                  (5.6)

Thus even arbitrarily close to the coloop endpoint, a fixed fraction of the leakage can be placed on an original source bank while two disjoint original banks retain an absolute transverse mixed-volume packet. This is a real application of the designated partner result, not a citation-only handoff.

It does not by itself close the endpoint: the longitudinal currency in (5.4) is proportional to `rho`, so a receiver that pays it reciprocally still loses as `rho->0`.

## 6. What has and has not been proved

This run proves three useful facts in the actual surviving exact-rank-three geometry:

1. **Every transverse-heavy leaf is paid down to the sharp working threshold `1/61`.** Any leaf with `||p_j||^2>=1/61` gives `||p_Q||_infinity<1204`.
2. **The arbitrary-rank projected-crossing row-marginal gate is automatic below that threshold.** There is a physical split with `s^2Z_2>(6264/190625)D^2c rho` and continuous-density bound `<16.652 rho^(-1/6)`.
3. **The designated partner gives a simultaneous three-source packet** with `rho_S>=2rho/81` and `M(G_Y,G_Z)>=2/81`.

The first unpaid exact-rank-three implication is now narrower:

`QFORM-NEARCOLOOP-ENDPOINT-STABLE-GLUING-v1`:

> In the state (1.1)-(1.7), with all leaf transverse leverages below `1/61`, combine the already-paid exact-null mixed-Fresnel endpoint with either the projected-crossing packet (4.16) or the partner three-bank packet (5.4)-(5.5) to obtain a density bound uniform as `rho->0`, without moments, conditional projection-height bounds, or perturbative deletion of the leakage.

The algebra shows why a projected-crossing argument alone cannot be that gluing theorem: its exact resource contains the factor `det H=rho`. A successful receiver must use the null-endpoint square/cross curvature **before** paying the small longitudinal volume, or prove a direct adapted-hub estimate of the kind currently isolated as the open `(SP)` mechanism in the newest Claude continuation.

**Status:** exact rank three remains OPEN in this positive-leakage/nonzero-hub collar; full unrestricted QFORM remains OPEN; no target-valid counterexample is produced. The continuous-density conclusion is proved only for the projected-crossing subbranch (4.17), not uniformly for the full remaining collar or the full conjecture.

## 7. Deterministic checks

The constants and partition inequalities were checked numerically with standard double precision; the exact symbolic inequalities used in the proof are displayed above. A separate 200-frame deterministic algebra regression tested (3.6) and (3.7) for random orthonormal rank-three frames and invertible symmetric spectral matrices. The maximum relative error in (3.6) was `1.67e-16`, and the maximum absolute row-marginal error in (3.7) was `5.00e-14`. These checks are diagnostic only; the proof is the Cauchy-Binet/Schur-Gram derivation in Section 3.

No task identity, schedule, enabled/paused state, notification/email setting, repository visibility, permission, model API, Codex call, or remote workflow was changed.
