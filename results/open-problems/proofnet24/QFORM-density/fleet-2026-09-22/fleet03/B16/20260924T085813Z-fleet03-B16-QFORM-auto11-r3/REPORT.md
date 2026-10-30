SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-24T08:58:13Z.
attacking: QFORM-SHAREDBANK-RANKONE-OVERLAP-COMPILER-v1 — retain one projected square scalar inside the hyperbolic factor, while the transverse innovation and the second factor come from disjoint original-coordinate banks.

# fleet03/B16 r45 — full-rank three-scalar compiler and rank-one shared-overlap exit

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T085813Z-fleet03-B16-QFORM-auto11-r3`  
Role: Projection-product interaction  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW SUPPORTING THEOREM + STRICT TARGET APPLICATION / FULL QFORM OPEN`  
Full-target continuity: `OPEN`.

## 1. Correction boundary and first missing implication

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. This run uses no rotated-independence claim, no arbitrary-joint indefinite coarea bound, no conditional projection-density cap, and no law-uniform pointwise quadratic-phase decay. A bounded projected density is used only on genuine scalar projections of disjoint original-coordinate product banks; the nonlinear integration is then completed by the already-proved orientation-free rank-two affine half-Riesz theorem.

Two fresh neighboring results sharpen the exact frontier.

* fleet03/B16 r44, `QFORM-THREEBANK-PROJECTEDSQUARE-HYPERBOLIC-LP-v1`, source `yspennstate/math-open-problems@cb1cffb4f4644bd7cf1bb912f792dd9ce060957a`, handles a projected square and a hyperbolic product when all three nonlinear source scalars come from disjoint banks.
* fleet01/B16, source `yspennstate/math-open-problems@935a3a200d67fdcd2e853b8f1d87ca6cd308489d`, proves `QFORM-PROJECTEDSQUARE-DEPENDENT-RANK2-LP-v1`: an independent projected square can be convolved against a dependent two-dimensional projected quadratic output in `L^(3/2) x L^3`. Its first unpaid state is the genuinely overlapping projected-square/rank-two packet.

The present result closes one nontrivial part of that overlap: the square scalar itself may also appear in one hyperbolic factor, provided a transverse innovation survives on a separate product bank.

## 2. Source theorem used

The only non-elementary mathematical dependency in the main proof is the completed supporting theorem

`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`

from

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For independent cap-one original-coordinate inputs, every orthonormal two-dimensional projection `U`, every invertible symmetric `2 x 2` matrix `Lambda`, and every affine coefficient vector `b` satisfy

`sup_t E |(U^T X)^T Lambda(U^T X) + b^T X - t|^(-1/2)
    <= 128 |det Lambda|^(-1/4).`                              (2.1)

The scalar projection input is the source-pinned Rogozin--Ball bound used throughout the fleet:

`||p_(r^T X)||_infinity <= sqrt(2)/||r||_2`                  (2.2)

for a nonzero projection of an original product bank with scalar density caps one.

## 3. Cap-one three-scalar Schur compiler

Let `Y1,Y2,Y3` be independent real random variables with densities bounded by one. Let

`B = [[a, q^T], [q, C]]`

be an invertible symmetric `3 x 3` matrix with `a != 0`, and let `ell in R^3`, `c in R`. Put

`F = Y^T B Y + ell^T Y + c`, `Y=(Y1,Y2,Y3)`.

### Lemma 3.1 — `QFORM-CAPONE-THREESCALAR-SCHUR-v1`

The law of `F` has an essentially bounded density and

`boxed: ||p_F||_infinity <= 128 |a det B|^(-1/4).`            (3.1)

### Proof

Write `z=(Y2,Y3)`. Completing the square in the genuine independent physical scalar `Y1` gives

`F = a (Y1 + a^(-1) q^T z + eta)^2 + R(z)`                   (3.2)

for a deterministic `eta` and a rank-two quadratic-plus-affine remainder

`R(z) = z^T S z + beta^T z + gamma`,
`S = C - q q^T/a`.                                           (3.3)

Because `B` is invertible and `a != 0`, `S` is invertible and the Schur determinant identity gives

`det S = det B / a`.                                         (3.4)

For every fixed `z`, the density of `a(Y1+h)^2` is bounded at a nonzero output `u` by

`|a|^(-1/2) |u|^(-1/2)`.                                    (3.5)

Indeed the two inverse branches each contribute at most one to the input density, and their Jacobians sum to exactly the displayed envelope. Hence, for almost every target level `t`, Tonelli/Fubini and (3.5) give

`p_F(t) <= |a|^(-1/2) E |R(z)-t|^(-1/2).`                    (3.6)

Apply (2.1) directly to the independent cap-one pair `(Y2,Y3)` and the invertible matrix `S`:

`sup_t E |R(z)-t|^(-1/2) <= 128 |det S|^(-1/4).`             (3.7)

Combining (3.4)--(3.7),

`||p_F||_infinity
 <= 128 |a|^(-1/2) |det B/a|^(-1/4)
 = 128 |a det B|^(-1/4).`                                    (3.8)

No spectral-coordinate independence is introduced. QED.

## 4. Three projected scalar banks

Let `K,I,J,W` be pairwise disjoint sets of original coordinates. Define

`S=r^T X_K`, `U=u^T X_I`, `V=v^T X_J`,                       (4.1)

with

`rho=||r||_2>0`, `sigma=||u||_2>0`, `tau=||v||_2>0`.         (4.2)

Let `B` be any invertible symmetric `3 x 3` matrix with `B_11=a != 0`. Let `ell(W)` and `R(W)` be arbitrary measurable functions of the fourth disjoint bank. Set

`Q = (S,U,V)^T B (S,U,V) + ell(W)^T(S,U,V) + R(W).`          (4.3)

### Theorem 4.1 — `QFORM-THREEBANK-FULLRANK-SCALAR-COMPILER-v1`

The law of `Q` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= 256 [rho sqrt(sigma tau)]^(-1) |a det B|^(-1/4).`        (4.4)

This theorem retains every quadratic cross term inside the displayed `3 x 3` scalar matrix `B`; the three scalar variables are independent only because their original-coordinate banks are disjoint.

### Proof

Condition on `W=w`. By (2.2), the three scalar densities have caps

`M1=sqrt(2)/rho`, `M2=sqrt(2)/sigma`, `M3=sqrt(2)/tau`.       (4.5)

Put `D=diag(M1,M2,M3)` and `Y=D(S,U,V)`. Then `Y1,Y2,Y3` are independent and each has density cap at most one. The conditional quadratic matrix in `Y` is

`B' = D^(-1) B D^(-1)`,                                      (4.6)

so

`a' = a/M1^2`,
`det B' = det B/(M1^2 M2^2 M3^2)`.                           (4.7)

Lemma 3.1 gives, uniformly in `w`,

`||p_(Q|W=w)||_infinity
 <=128 |a' det B'|^(-1/4)
 =128 M1 (M2 M3)^(1/2)|a det B|^(-1/4).`                    (4.8)

Using (4.5),

`M1(M2M3)^(1/2) <= 2/[rho sqrt(sigma tau)]`.                 (4.9)

Equations (4.8)--(4.9) give (4.4), and averaging the conditional densities over `W` preserves the same essential supremum. QED.

**Regularity.** The argument proves existence of an essentially bounded density in this scope. It does **not** prove that this density has a continuous representative. Full-target continuity therefore remains open and is recorded separately.

## 5. Rank-one shared hyperbolic overlap

The key specialization is

`Q = a(S+d(W))^2
    + 2 b (c S + U + alpha(W))(V + beta(W))
    + R(W),`                                                   (5.1)

where `a b != 0`. The quadratic matrix on `(S,U,V)` is

`B = [[a,0,bc], [0,0,b], [bc,b,0]]`,                          (5.2)

and the determinant is exactly

`det B = -a b^2`.                                             (5.3)

Therefore Theorem 4.1 yields the overlap-safe bound

`boxed:
 ||p_Q||_infinity
 <= 256/[rho sqrt(sigma tau) sqrt(|a b|)].`                   (5.4)

Call this

`QFORM-RANKONE-SHARED-HYPERBOLIC-OVERLAP-v1`.

The coefficient `c` disappears completely from the bound. This is not an omission: it is a Schur-determinant cancellation. The scalar `S` can carry an arbitrarily strong cross coupling with `V`; as long as the independent innovation `U` survives in the same hyperbolic factor, the determinant of the rank-two Schur remainder is `-b^2` after the `S` pivot.

This strictly extends the r44 three-disjoint-nonlinear-output theorem: the square scalar `S` now participates directly in the hyperbolic term. The price is that only a one-dimensional shared overlap is paid; a genuinely dependent two-dimensional projection from the same product bank is still outside this theorem.

## 6. Strict target family with arbitrarily delocalized projected sources

Take three disjoint original-coordinate banks and choose unit vectors `r,u,v` on them. The scalar projections

`S=r^T X_K`, `U=u^T X_I`, `V=v^T X_J`                        (6.1)

may each be arbitrarily delocalized over growing banks. Consider

`Q_* = 3 S^2 + 6(S+U)V`.                                     (6.2)

Its effective matrix is

`B_* = [[3,0,3], [0,0,3], [3,3,0]]`.                         (6.3)

Writing `B_*=3B_0`, the characteristic polynomial of `B_0` is

`p(mu)=mu^3-mu^2-2mu+1`.                                     (6.4)

The exact signs

`p(-2)=-7`, `p(-1)=1`, `p(1/3)=7/27`, `p(1)=-1`, `p(2)=1`  (6.5)

locate its three real roots in the disjoint intervals

`(-2,-1)`, `(1/3,1)`, `(1,2)`.                               (6.6)

Hence the three eigenvalues of `B_*` lie in

`(-6,-3)`, `(1,3)`, `(3,6)`,                                 (6.7)

so every one has absolute value strictly larger than one. This is a genuine owner-target family, not a two-eigenvalue surrogate.

For `rho=sigma=tau=1`, `a=b=3`, (5.4) gives

`boxed: ||p_(Q_*)||_infinity <= 256/3 < 85.334.`              (6.8)

Thus a fully delocalized strict-target chamber remains uniformly bounded even when the projected square direction is reused inside the hyperbolic factor.

## 7. Designated partner fleet04/B16 applied to an actual strict-target inequality

The newest completed designated-partner result used here is fleet04/B16 r4,

`yspennstate/math-open-problems@7f2bb2d330022b09a6af6e39ab09d054caeaa346`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260924T041516Z-fleet04-B16-QFORM-r4/REPORT.md`.

Its source-valid definite projected-plane exit states that if a two-dimensional orthogonal projection `Z` of a cap-one product bank enters, after conditioning on disjoint sources, through a definite quadratic matrix `H`, then

`||p_Q||_infinity <= 2 pi/sqrt(|det H|).`                     (7.1)

Apply this to a new strict target. Let `S` be any unit scalar projection of one product bank and let `Z=(Z1,Z2)` be an orthonormal two-dimensional projection of a disjoint product bank. Define

`Q_dagger = -2S^2 + 4 S Z1 + 2 Z1^2 + 2 Z2^2`.               (7.2)

Conditioning on `S=s` leaves the definite `Z`-plane matrix

`H=2 I_2`, `det H=4`,                                        (7.3)

with an arbitrary translated linear term `4s Z1`. The partner theorem therefore gives, uniformly in `s`,

`boxed: ||p_(Q_dagger)||_infinity <= pi.`                     (7.4)

The effective `3 x 3` matrix is

`P=[[-2,2,0],[2,2,0],[0,0,2]]`,                              (7.5)

whose eigenvalues are exactly

`-2 sqrt(2), 2 sqrt(2), 2`.                                  (7.6)

Thus (7.4) is an actual inequality inside the full owner target. It also shows how a strong cross coupling from a projected scalar into a definite projected plane can be harmless: the coupling becomes only an affine translation after conditioning, while the plane curvature remains unchanged.

## 8. Exact frontier after this run

The new compiler pays a source-preserving overlap of rank one. It does **not** solve the state in which the projected square and the transverse innovation are two genuinely dependent projections of the same original-coordinate product bank. A bounded two-dimensional marginal density alone is insufficient there, and conditioning on one projection does not preserve a uniform cap for the other.

The next B16 implication is therefore

`QFORM-OVERLAPPING-PROJECTEDSQUARE-RANK2-PREABSOLUTE-v2`:

> For one product bank producing a dependent pair `(S,T)`, and a disjoint source bank producing the remaining factor, retain the product provenance until after the square/hyperbolic curvature is combined. Either prove a determinant-homogeneous nonlinear bound for the overlapping packet or force a valid definite-plane / phase-aligned / source-separated-innovation exit.

The fresh fleet01/B16 theorem supplies the additive independent-square boundary case; r44 supplies the fully disjoint hyperbolic boundary case; Theorem 5.1 above supplies the one-dimensional shared-overlap bridge between them. The genuinely two-dimensional same-bank overlap remains open.

Full QFORM remains OPEN. Global continuity remains OPEN.
