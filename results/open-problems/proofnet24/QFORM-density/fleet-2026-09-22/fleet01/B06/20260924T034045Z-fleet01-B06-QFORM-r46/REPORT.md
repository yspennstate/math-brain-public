SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-24T03:40:45Z.
attacking: heavy-carrier Pluecker deletion — condition away literal physical hubs only after aggregating carrier volume, and force either a diffuse residual carrier or a three-coordinate hitting-set obstruction.

# fleet01/B06 r46 — weighted physical deletion of a rank-three carrier

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW SUPPORTING STRUCTURAL/CONTINUOUS-DENSITY THEOREM + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains open. This run addresses the heavy-carrier obstruction left by r45. The point is to remove a small number of literal physical coordinates only after measuring how much of the complete Pluecker volume law survives; conditional independence is therefore genuine, and no curved-fiber supremum or reciprocal individual minor is introduced.

## 1. Sources and allowed premises


Immediate predecessor:

`yspennstate/math-open-problems@3145295734fbc4152341278a804b6b39cd2e9167`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T023755Z-fleet01-B06-QFORM-r45/REPORT.md`.

Its theorem `QFORM-DIFFUSE-SEPARABLE-RANKK-FRESNEL-BL-v1` says: for a Parseval frame `R in R^(n x k)` with every row leverage at most `1/2`, invertible symmetric `Lambda`, independent cap-one inputs, and arbitrary coordinate-separable phases,

`||p_Q||_infinity <= e k/(k-2) |det Lambda|^(-1/k)`, `k>=3`,

and the density is continuous `C_0`. For `k=3` the constant is `3e`.

The designated completed partner input is fleet02/B06:

`yspennstate/math-open-problems@159d52912827d75566d254e155d93a8183ab254f`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/fleet02-B06-20260924T013401Z-1fca9092/REPORT.md`,

theorem `QFORM-DIAG-RANK1-SQRT-SMALLBALL-v1` and its indefinite-pair upgrade. For a literal invertible indefinite physical pair `B` with exact Schur residual `S=D+lambda w w^T`, it proves

`||p_Q||_infinity <= 18.280856344644523 [|det B| sigma_min(B) ||S||op]^(-1/4)`.   (1.1)

This partner inequality is applied to the same exact pair residual in Section 7 below.

## 2. Exact physical-deletion identity

Let `k>=3`, let `R in R^(n x k)` have orthonormal columns, let `Lambda` be invertible symmetric, and put

`L=R Lambda R^T`.

Let `D` be any diagonal matrix in the original coordinates. Thus the relevant coefficient matrix is

`A=D+L`.                                                          (2.1)

Linear terms may be present as well.

For a literal physical coordinate set `H`, put `J=H^c` and

`G_H=R_J^T R_J=I_k-R_H^T R_H`.                                  (2.2)

Assume `G_H` is positive definite and define

`theta_H=det G_H`,
`bar R=R_J G_H^(-1/2)`,
`bar Lambda=G_H^(1/2) Lambda G_H^(1/2)`.                         (2.3)

Then

`bar R^T bar R=I_k`,                                              (2.4)

and the surviving carrier is exactly

`L_{J,J}=bar R bar Lambda bar R^T`.                              (2.5)

Moreover

`boxed: |det bar Lambda|=|det Lambda| theta_H.`                  (2.6)

For each surviving literal coordinate `j in J`, its leverage in the residual orthonormal carrier is

`boxed: ell_j^(H)=r_j^T G_H^(-1) r_j.`                           (2.7)

These are identities; no probability has yet been used.

## 3. Weighted curved-fiber deletion theorem

### Theorem `QFORM-PLUCKER-DELETION-DIFFUSE-v1`

Let the independent original coordinates have densities at most one. In (2.1), suppose `G_H>0` and

`max_(j in J) ell_j^(H) <=1/2`.                                  (3.1)

Then the full ambient quadratic form, including arbitrary fixed values of the coordinates in `H`, all diagonal terms in `D`, all linear terms, and all cross terms induced by conditioning, has a conditional density satisfying uniformly in `X_H`

`boxed:
 ||p_(Q | X_H)||_infinity
 <= e k/(k-2) [|det Lambda| theta_H]^(-1/k).`                    (3.2)

Consequently the unconditional law has a continuous `C_0` density with the same bound.

For rank three,

`boxed:
 ||p_Q||_infinity <=3e [Delta_3 theta_H]^(-1/3),`                (3.3)

where `Delta_3=|det Lambda|=|pdet L|`.

### Proof

Condition on the literal original coordinates `X_H`. The remaining coordinates `X_J` are still independent and retain their original density caps `<=1`. The conditional quadratic coefficient on `J` is

`D_J+R_J Lambda R_J^T
 =D_J+bar R bar Lambda bar R^T`.                                 (3.4)

The cross terms between `H` and `J` become a linear function of `X_J`; hence they are coordinate-separable phases. Equation (2.4) says `bar R` is a Parseval frame, (3.1) is exactly the leverage hypothesis of r45, and (2.6) gives its determinant. Therefore r45 applies conditionally and gives (3.2) uniformly in the conditioned value.

For continuity, use the stronger form of the same conditional argument: r45 gives a common integrable characteristic-function envelope depending only on `k`, `|det Lambda| theta_H`, not on `X_H`. Averaging conditional characteristic functions preserves that envelope. Fourier inversion therefore gives an unconditional continuous `C_0` density with the same `L^infinity` bound. QED.

This is a weighted replacement for the forbidden fiber maximum. The removed physical coordinates are not charged by a supremum; their only cost is the exact surviving carrier-volume factor `theta_H`.

## 4. Pluecker probability interpretation

The deletion factor has an exact product-geometric meaning. For every physical `k`-subset `I`, put

`mu(I)=det(R_I)^2`.                                               (4.1)

Cauchy--Binet and `R^T R=I_k` give

`sum_(|I|=k) mu(I)=1`,                                           (4.2)

so `mu` is a probability law on literal physical `k`-subsets. Then another Cauchy--Binet expansion gives

`boxed:
 theta_H=det(R_J^T R_J)
       =sum_(I subset J, |I|=k) mu(I)
       =Pr_(I~mu){I cap H=empty}.`                               (4.3)

Thus `theta_H` is exactly the Pluecker volume mass that survives deletion of `H`.

Condition this law on avoiding `H`. For `I subset J`,

`det(bar R_I)^2=det(R_I)^2/theta_H=mu(I)/theta_H.                (4.4)

Therefore the conditional Pluecker law is precisely the volume-sampling law of the residual orthonormal frame `bar R`. Its one-coordinate inclusion marginals are

`boxed:
 Pr{j in I | I cap H=empty}=ell_j^(H).`                          (4.5)

One proof of (4.5) is to sum the Cauchy--Binet weights containing row `j`; equivalently it is the diagonal of the projection `bar R bar R^T`.

For a singleton `H={i}`, if `P=RR^T`, the formulas become particularly explicit:

`theta_i=1-P_ii`,                                                 (4.6)

and Sherman--Morrison gives, for `j!=i`,

`boxed:
 ell_j^({i})=P_jj + P_ij^2/(1-P_ii).`                            (4.7)

So deleting a heavy literal row does not silently reset the geometry: the exact leverage transfer to every remaining row is visible in (4.7).

## 5. Rank-three greedy compiler: diffuse survivor or three-coordinate hitting set

The preceding identities give a dimension-free compiler without selecting an individual Pluecker minor.

### Corollary `QFORM-RANK3-DIFFUSE-OR-THREEHUB-HIT-v1`

For every rank-three carrier `L=R Lambda R^T` with `R^T R=I_3`, exactly one of the following two exits can be produced by a deterministic greedy procedure:

**Diffuse deletion exit.** There exists a literal physical set `H` with `|H|<=2` and

`theta_H>=1/8`,                                                  (5.1)

such that every residual leverage is at most `1/2`. Hence for arbitrary diagonal `D`, arbitrary linear terms and independent cap-one inputs,

`boxed:
 ||p_Q||_infinity <=6e Delta_3^(-1/3),`                          (5.2)

and the density is continuous `C_0`.

**Three-hub hitting exit.** There exists a literal physical set `H` with `|H|<=3` such that

`boxed:
 Pr_(I~mu){I cap H != empty}>7/8.`                               (5.3)

In words, more than seven eighths of the complete rank-three determinant-squared volume law hits at most three original coordinates.

### Proof

Start with `H_0=empty`, `theta_0=1`. As long as `theta_H>=1/8`, inspect the residual conditional Pluecker law. If all its one-point marginals are at most `1/2`, use Theorem 3 and stop.

Otherwise choose a literal coordinate `j` whose conditional inclusion probability

`q_j=ell_j^(H)>1/2`.

By (4.3)-(4.5), deleting it changes the surviving mass by the exact rule

`boxed:
 theta_(H union {j})=theta_H(1-q_j)<theta_H/2.`                  (5.4)

If the new mass is below `1/8`, then (5.3) holds and stop. If it remains at least `1/8`, continue.

Three successive heavy deletions would force `theta<2^-3=1/8`. Therefore the procedure stops after at most three deletions. If it stops diffusely before the third deletion, the diffuse set has size at most two and still has `theta_H>=1/8`. Then (3.3) gives

`3e(Delta_3 theta_H)^(-1/3)
 <=3e(Delta_3/8)^(-1/3)
 =6e Delta_3^(-1/3)`,

which is (5.2). QED.

This is the substantive gain of the run: the heavy-carrier failure of r45 is no longer an unstructured leverage condition. It is either paid at universal cost through an exact surviving-volume factor or compressed into at most three literal physical coordinates carrying more than `7/8` of the whole Pluecker volume law.

## 6. Relation to the full spectral target

The corollary is a rank-three-carrier statement, not a proof that an arbitrary target matrix admits a rank-three carrier with `Delta_3` bounded below by a universal constant after a coordinate-separable remainder. That structural assembly remains part of the full QFORM problem.

It also does not say that the three-hub hitting exit contains one large physical `3 x 3` determinant. The whole point is to avoid that false inference: the `7/8` statement concerns aggregate determinant-squared mass. A subsequent receiver must retain that aggregate information or exploit the hub directly.

No Gaussianity, log-concavity, moments, bounded support, connected support, iid assumption, or independence after rotation has been introduced.

## 7. Apply the designated fleet02/B06 result to r45's exact pair residual

Return to r45's exact decomposition after a literal invertible physical pair:

`A=[[B,E],[E^T,C]]`,
`C-E^T B^(-1)E=D+lambda w w^T`.                                 (7.1)

Set

`F=B^(-1)E`, `T=[I_2;F^T]`, `z=[0_2;w]`,
`L=TBT^T+lambda z z^T`.                                          (7.2)

The carrier has rank three and exact pseudodeterminant

`Delta_3
 =|lambda det B| det(I+FF^T) w^T(I+F^TF)^(-1)w`.                (7.3)

Apply the new rank-three compiler to this `L`. It yields either

`boxed: ||p_Q||_infinity <=6e Delta_3^(-1/3)`                    (7.4)

with a continuous density, or a literal at-most-three-coordinate hub hitting more than `7/8` of this carrier's Pluecker law.

On the very same equation, apply the designated completed fleet02/B06 theorem (1.1): with

`S=D+lambda w w^T`,

`boxed:
 ||p_Q||_infinity
 <=18.280856344644523
 [|det B| sigma_min(B) ||S||op]^(-1/4).`                         (7.5)

This is an actual partner-result application, not merely a citation. Equations (7.4)-(7.5) give a two-payment/one-structural-obstruction compiler: a quantitative physical-pair currency is paid by (7.5); a diffuse surviving carrier is paid by (7.4); only simultaneous small pair currency plus a carrier whose Pluecker mass is concentrated through at most three physical coordinates remains from this local geometry.

In particular, the r45 phrase "heavy-carrier / highly anisotropic effectively-rank-one shear" can be sharpened to the explicit target `QFORM-THREEHUB-HIT-PLUS-SMALLPAIR-RECEIVER-v1`.

## 8. Finite algebra audit

A direct numerical audit was run only as a sanity check, not as evidence for the theorem. Random Parseval `n x 3` frames with `n=5,8,12,30` were tested over 50 trials per dimension. For random singleton deletions the maximum observed absolute errors were

- `|det G_i-(1-P_ii)| <=1.34e-15`;
- singleton conditional leverage formula (4.7): `<=1.75e-14`;
- sum of residual leverages minus three: `<=1.78e-15`;
- total Cauchy--Binet Pluecker mass minus one: `<=5.33e-15`;
- avoiding mass minus `1-P_ii`: `<=5.67e-15`.

These checks only guard algebra/implementation mistakes; the proof is the exact argument above.

## 9. Remaining implication

The first unpaid local implication is

`QFORM-THREEHUB-HIT-PLUS-SMALLPAIR-RECEIVER-v1`:

when the physical-pair currency in (7.5) is too small and more than `7/8` of the exact rank-three carrier Pluecker law meets a literal hub of at most three coordinates, retain those hub coordinates and the full original-product environment jointly and prove a universal density payment, or route the configuration into an already verified projected-crossing/physical-block receiver. The argument must not replace the aggregate Pluecker mass by a largest minor.

The full arbitrary-dimensional QFORM conjecture remains OPEN. Global continuity remains OPEN. The branch (3.2)/(5.2)/(7.4) has a continuous `C_0` density; the partner pair endpoint (7.5) asserts essential boundedness in its stated scope but not continuity.
