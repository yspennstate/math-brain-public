SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-23T22:16:26Z.
attacking: endpoint-stable gluing in the nonzero near-null rank-three hub collar via an exact sheared Schur discriminant and a product-safe receiver.

# fleet03/B10 r25 — leakage-free hub discriminant and partner conditioning contraction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Status: `NEW EXACT CANCELLATION + NEW PARTNER CONDITIONING REDUCTION / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository transport was used, no authenticated native-brain receiver was invoked.


The live correction boundary is preserved: no independence after spectral rotation, no arbitrary-joint coarea cap, no conditional projection-height supremum, no law-uniform pointwise quadratic-phase decay, no moments/support/log-concavity assumption, no deletion of a small random quadratic term, and no fixed-good-minor inference.

The immediate B10 geometric predecessor is

`yspennstate/math-open-problems@4f1f31064431e8bb0d0be813ed5540d0b12ab590`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T181522Z-fleet03-B10-QFORM-r26/REPORT.md`.

It reduces the still-unpaid exact-rank-three collar to the following state.

## 1. Live near-coloop state

Write

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`, `D:=|det M|>=1`.          (1.1)

There is one ORIGINAL physical hub row

`u_0=sqrt(c)e`, `||e||=1`, `c>63/64`, `rho:=1-c in (0,1/64)`,           (1.2)

and the other physical rows are

`u_i=t_i e+p_i`, `p_i perpendicular e`,                              (1.3)

with the exact Parseval ledger

`sum_i t_i^2=rho`, `sum_i t_i p_i=0`, `sum_i p_i p_i^T=I_2`.           (1.4)

All still-unpaid leaves also obey `||p_i||^2<1/61`. Put the spectral block of `M` relative to `R e direct_sum e^perp` in the form

`M = [[alpha,m^T],[m,N]]`,                                            (1.5)

where `m in R^2`, `N=N^T in R^(2x2)`. The physical hub pivot satisfies `A_00=c alpha`, with `|A_00|<1/64` and hence `|alpha|<1/16`.

For the original leaf variables set

`T=sum_i t_i X_i`, `P=sum_i p_i X_i in R^2`,                          (1.6)

and let `H=X_0`. Then the exact spectral projection is

`R^T X = e(sqrt(c)H+T)+P`.                                            (1.7)

No random rotation has occurred; `(T,P)` is generally dependent.

## 2. New exact adapted-hub conditional cap

### Lemma 2.1 — `QFORM-ADAPTED-HUB-CONDITIONAL-CAP-v1`

Let

`Z=sqrt(c)H+T`.                                                        (2.1)

Then the joint law of `(Z,P)` admits a density `r(z,p)` satisfying

`boxed: r(z,p) <= c^(-1/2) p_P(p)`                                   (2.2)

for almost every `(z,p)`, where `p_P` is the marginal density of `P`. Consequently, for almost every `p` with `p_P(p)>0`,

`boxed: ||p_{Z | P=p}||_infinity <= c^(-1/2) < sqrt(64/63) <1.008.`   (2.3)

The same bound holds after any measurable shear `Z -> Z+psi(P)`.

#### Proof

Because `rho>0`, the three leaf coefficient vectors

`t/sqrt(rho)`, `p^(1)`, `p^(2)`                                      (2.4)

are orthonormal in physical coefficient space by (1.4). Hence `(T,P)` is a rank-three linear image of the absolutely continuous leaf product law and has a joint density, say `g(t,p)`. The hub `H` is an independent ORIGINAL coordinate and its density `f_0` satisfies `0<=f_0<=1`. Therefore

`r(z,p)=c^(-1/2) int_R f_0((z-t)/sqrt(c)) g(t,p) dt`                  (2.5)

and so

`r(z,p) <= c^(-1/2) int_R g(t,p)dt = c^(-1/2)p_P(p)`.                (2.6)

Division by the marginal gives (2.3). A shear by a function of `P` only translates each conditional density and changes no cap. QED.

This is a genuine endpoint-stable statement: neither the size `rho` of the longitudinal leakage nor fragmentation of the hub density appears. It does **not** by itself control the indefinite quadratic pushforward; using (2.3) as an arbitrary-joint coarea theorem would violate the live correction boundary.

## 3. New exact discriminant cancellation: all longitudinal leakage disappears

Substitute (1.7) into the quadratic form:

`Q=alpha Z^2+2Z(m.P)+P^T N P`, `Z=sqrt(c)H+T`.                        (3.1)

Fix all leaf variables and a target level `s`. As a polynomial in the ORIGINAL hub variable `H`,

`Q-s = A_h H^2+B_h H+C_h`,                                           (3.2)

where

`A_h=alpha c`,
`B_h=2sqrt(c)(alpha T+m.P)`,
`C_h=alpha T^2+2T(m.P)+P^T N P-s`.                                  (3.3)

A direct expansion gives the exact identity

`boxed: B_h^2-4A_h C_h
 =4c[(m.P)^2-alpha P^T N P+alpha s].`                                (3.4)

Every occurrence of the longitudinal leakage variable `T` cancels. This is the first essential implication attempted in this run: the nonzero-pivot hub-root geometry is **exactly independent of the leakage realization**, not merely perturbatively close to the null endpoint.

Define the transverse discriminant matrix

`B_alpha := m m^T-alpha N`.                                          (3.5)

Then

`(m.P)^2-alpha P^TNP+alpha s = P^T B_alpha P+alpha s`.               (3.6)

The `2x2` determinant is exact:

`boxed: det B_alpha = alpha det M`.                                  (3.7)

Indeed,

`det(alpha N-mm^T)=alpha^2 det N-alpha m^T adj(N)m
                 =alpha det M`,                                     (3.8)

and in two dimensions changing the sign of the whole matrix leaves the determinant unchanged.

### Proposition 3.2 — source-valid absolute hub-root payment

For `alpha!=0`, conditioning on the leaves and summing the at most two hub roots gives

`p_Q(s) <= c^(-1/2)
 E[(P^T B_alpha P+alpha s)_+^(-1/2)]`.                               (3.9)

The completed rank-two affine half-Riesz theorem applies directly to the ORIGINAL leaf product law because the two columns formed by the `p_i` are orthonormal by (1.4). Hence

`sup_s E |P^T B_alpha P+alpha s|^(-1/2)
 <=128 |det B_alpha|^(-1/4)
 =128 (|alpha|D)^(-1/4)`.                                            (3.10)

Therefore

`boxed: ||p_Q||_infinity <=128 c^(-1/2)(|alpha|D)^(-1/4).`            (3.11)

Equation (3.11) recovers the previously paid scalar-pivot rate by a different exact route, but (3.4) adds useful structural information: **the entire positive leakage `rho` disappears before the half-Riesz payment.** The only singular parameter left in the absolute-root route is the true hub Rayleigh coefficient `alpha`.

At `alpha=0`, `B_alpha=mm^T` has rank one and (3.9) degenerates to a reciprocal linear-form payment, which may diverge for admissible rough product laws. Thus taking absolute values at the hub roots cannot be the endpoint-stable gluing mechanism. This precisely matches the already-proved exact-null mixed-Fresnel theorem, which keeps oscillation and gives a finite constant rather than taking this reciprocal expectation.

This is an obstruction to the **method**, not a counterexample to QFORM.

## 4. Designated partner fleet04/B10: a new condition-away contraction

The required completed partner theorem is

`QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1`,

source

`yspennstate/math-open-problems@afdea9634d9e3f5fb09659da436292cf7dbe5b20`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B10/20260923T061725Z-fleet04-B10-QFORM-r4/REPORT.md`.

Apply it to the **whole current leaf bank**. Here the transverse Gram is `G=I_2`, the global regression vector is zero by (1.4), its residuals are exactly `e_i=t_i`, and their energy is `rho`. The partner supplies a partition of ORIGINAL indices

`L = S disjoint_union Y disjoint_union Z`                              (4.1)

such that

`rho_S M(G_Y,G_Z) >= (2/81)rho`,                                     (4.2)

where

`rho_S=sum_(i in S)t_i^2`,
`G_Y=sum_(i in Y)p_i p_i^T`, `G_Z=sum_(i in Z)p_i p_i^T`,              (4.3)

and `M(H,K)=tr(adj(H)K)`.

Because `rho_S<=rho` and, for positive semidefinite `2x2` matrices,

`M(G_Y,G_Z)<=det(G_Y+G_Z)<=det I_2=1`,                                (4.4)

(4.2) yields the two actual inequalities

`boxed: rho_S >=(2/81)rho`,                                          (4.5)
`boxed: M(G_Y,G_Z)>=2/81`.                                           (4.6)

Put `G_R=G_Y+G_Z`. Since

`det G_R=det G_Y+det G_Z+M(G_Y,G_Z)`,                                (4.7)

we obtain

`boxed: det G_R>=2/81, lambda_min(G_R)>=2/81`.                        (4.8)

The second inequality uses `0<=G_R<=I_2`, so `lambda_max(G_R)<=1`.

Now condition on the entire ORIGINAL bank `X_S`. This is a legitimate product-preserving conditioning step. The coordinates `X_0,X_Y,X_Z` remain independent with their original cap-one laws; every term involving the frozen `S` bank becomes only an affine or constant term in the remaining variables. The remaining longitudinal energy obeys the strict contraction

`boxed: sum_(i in Y union Z)t_i^2 = rho-rho_S <=(79/81)rho`,           (4.9)

while (4.8) says that the two-dimensional transverse geometry left alive after the conditioning is absolutely nondegenerate.

This is a concrete new use of the partner theorem. It is stronger than merely recording a three-bank packet: one can remove a fixed fraction of the dangerous longitudinal energy **without** destroying the transverse plane and without splitting any original coordinate.

The fixed-hub physical principal-triple packet also remains absolute. Since for the hub row `u_0=sqrt(c)e`,

`|det A_{ {0,j,k} }|=D c det(p_j,p_k)^2`,                             (4.10)

(4.6) gives

`boxed: sum_(j in Y,k in Z)|det A_{ {0,j,k} }|
      =D c M(G_Y,G_Z)
      >(63/64)(2/81)=7/288.`                                         (4.11)

No reciprocal individual minor is selected.

## 5. Interaction with the newest rough-law receiver

During this run fleet01/B10 published the source-valid theorem

`QFORM-THREE-BANK-HYPERBOLIC-SQUARE-RECEIVER-v1`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B10/20260923T222440Z-fleet01-B10-QFORM-auto11/REPORT.md`.

For three genuinely independent scalar bank observables `Z,Y,W` with density caps `K_Z,K_Y,K_W`, it proves

`||p_(2sZY+bY^2+2cYW+dW^2)||_infinity
 <=4sqrt(2)K_W sqrt(K_Z K_Y)/sqrt(|sd|)`,                             (5.1)

and permits the stated triangular shears. The theorem is insensitive to fragmentation and, in its exact scope, pays the null-axis endpoint without a leakage factor.

Equations (4.5)-(4.11) show that the current generic collar has enough **aggregate** source-disjoint transverse geometry after a legal conditioning step. What is not yet proved is the conversion of the mixed-row banks `Y,Z` into the triangular scalar observables required by (5.1) without splitting one original variable into independent longitudinal/transverse pieces. This is precisely where a naive use of spectral coordinates would violate product provenance.

Thus the first unpaid B10 implication is now sharper than r26:

`QFORM-TWOBANK-MIXEDROW-TRIANGULAR-RECEIVER-v1`:

> In the conditioned state supplied by (4.8)-(4.9), with one original hub, two independent ORIGINAL leaf banks whose combined transverse Gram has `lambda_min>=2/81`, total remaining longitudinal energy at most `(79/81)rho<1/64`, and fixed-hub aggregate principal-triple packet at least `7/288`, prove a uniform density bound through the null/punctured collar while retaining all same-bank longitudinal/transverse contamination. Equivalently, obtain a grouped Fourier/real-variable analogue of the three-scalar hyperbolic-square receiver that spends the aggregate mixed volume before any fiber supremum or reciprocal tiny minor.

The exact discriminant cancellation (3.4) says that a successful proof should not pay the size of `rho` at all; the partner conditioning reduction says that if a grouped receiver needs a mild geometric separation first, one can acquire it without losing the transverse plane. The remaining singularity is the phase-sensitive transition `alpha ->0`, not absence of curvature.

## 6. Deterministic checks

A fixed-seed 2000-frame regression checked the exact discriminant cancellation (3.4) and the underlying bank spectral decomposition. Maximum absolute discrepancies were respectively

`5.684341886080802e-14`, `8.881784197001252e-16`.

The full diagnostic record is `REGRESSION.md` in this run directory. These computations are checks only; the proof is the exact algebra above.

## 7. Scope and status

- `QFORM-ADAPTED-HUB-CONDITIONAL-CAP-v1`: **PROVED**.
- Exact leakage cancellation in the physical-hub discriminant (3.4), including `det B_alpha=alpha det M`: **PROVED**.
- Absolute nonzero-pivot consequence (3.11): **PROVED**, but not endpoint-stable in `alpha`.
- Partner condition-away contraction (4.5)-(4.11): **PROVED**, in ORIGINAL coordinates.
- Generic mixed-row near-coloop collar: **OPEN**.
- Arbitrary exact rank three: **OPEN**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuity: no new unrestricted continuity theorem is claimed here; existing exact-null/projected-crossing subbranches retain their previously proved continuity.

No task identity, schedule, enabled/paused state, email/push setting, repository visibility, permission, paid API/Codex call, public workflow, or cross-account authentication was changed.