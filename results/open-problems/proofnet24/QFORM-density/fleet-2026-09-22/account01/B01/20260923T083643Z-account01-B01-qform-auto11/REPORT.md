SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T08:36:43Z.
attacking: the same-hour high-leverage collapse endpoint by mixed time/frequency smoothing, with no scalar pointwise Fresnel envelope.

# Leverage-free mixed-time smoothing for a rank-two cross packet plus exact three-dimensional receiver curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T083643Z-account01-B01-qform-auto11`  
Role: account01/B01, Oscillatory replacement  
Status: **NEW AVERAGED-FREQUENCY SUPPORTING THEOREM / A HIGH-LEVERAGE COLLAPSE SUBCLASS PAID / FULL QFORM OPEN**  
Execution/memory: `WITHOUT_VERIFIED_BRAIN`.

## 1. Why this run changes mechanism rather than repeating the 08:17 result

A same-hour B01 report already paid a large high-leverage receiver class by completing one physical receiver coordinate and then applying the rank-two half-Riesz estimate. Its remaining collapse set includes states in which the high-leverage coordinate has **zero physical pivot** or its Schur two-area vanishes. The present run does not repeat that square-completion mechanism. It keeps the zero-pivot receiver coordinate untouched and instead uses a joint mixed `(time, two-dimensional cross-frequency)` estimate.

The live correction remains binding: for cap-one one-dimensional densities there is no law-uniform pointwise estimate `|E exp(i s X^2)| <= C |s|^{-1/2}`. A finite union of phase-aligned intervals can make that scalar transform arbitrarily close to one at a prescribed large frequency. The theorem below therefore permits arbitrarily large spikes in a scalar quadratic phase; only its **cubic time budget after a three-dimensional product projection** is used.

The full target remains open. No Gaussianity, moment, log-concavity, compact support, connected support, identical-law assumption, or independence after rotation is introduced.

## 2. Source-valid inputs

### 2.1 Product projection bounds

The Livshyts--Paouris--Pivovarov product-marginal theorem gives, for original independent cap-one coordinates, a density cap `2^(k/2)` for every `k`-dimensional orthogonal marginal. The instances used here are

`||p_(U^T X_I)||_infinity <=2` for `dim U=2`,

and

`||rho_(T^T X_J)||_infinity <=2^(3/2)` for an orthonormal three-frame `T`.

These are ordinary marginal statements. No independence of projected coordinates is asserted.

### 2.2 B01 scalar cubic frequency budget

The completed B01 theorem at

`yspennstate/math-open-problems@d58130b048c1e7ef8a22cf7a52a0d23b610c5fa7`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260922T230746Z-b01-qform-auto11/REPORT.md`

proves that if a probability density has cap `M`, then uniformly in translations,

`int_R |E exp(i t a(Y+b)^2)|^3 dt <=72*pi*M^2/|a|`.               (2.1)

The proof is a pushforward density estimate plus Hausdorff--Young; it is not pointwise stationary phase.

### 2.3 Newest designated partner actually applied

The newest completed account02/B01 report read in this run is

`yspennstate/math-open-problems@e7fdc2430ce640363582b98adce7771f8797e686`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T081654Z-account02-B01-qform-auto14/REPORT.md`.

Its Theorem 4.1 states that an exact rank-two physical cross packet of area `Delta`, together with a **source-disjoint** off-diagonal packet of energy `F_D`, has, at `beta=1/4`,

`||p_Q||_infinity <=22.104 Delta^(-2/5) F_D^(-1/10)`,              (2.2)

while retaining arbitrary same-bank curvature in the two rank-two-cross banks and arbitrary outside couplings through the theorem's stated `W` bank. Section 8 below applies (2.2) to an actual target-valid extension of the stress family.

## 3. The new theorem

### Theorem 3.1 — `QFORM-RANK2-CROSS-3D-RECEIVER-MIXEDTIME-v1`

Split the ORIGINAL independent physical coordinates into two disjoint banks `I,J`. Every one-dimensional density is at most one. Suppose the full physical cross block is exact rank two,

`K=A[I,J]=U Sigma V^T`,

where `U,V` have two orthonormal columns and `Sigma=diag(kappa_1,kappa_2)` with positive entries. Put

`Delta=kappa_1 kappa_2`.

Choose a unit receiver vector `w` orthogonal to `range(V)` and set the orthonormal three-frame

`T=[V w]`.

Assume the **entire receiver quadratic part** is supported on this three-dimensional subspace:

`A[J,J]=T C T^T`                                                    (3.1)

for some real symmetric `3x3` matrix `C`. Write

`a=C_33=w^T A[J,J] w`

and assume `a!=0`. Receiver affine terms are allowed provided they lie in `S=range(T)`. The `I`-bank self part may be an arbitrary real measurable function `H(X_I)`; in particular it may be an arbitrary quadratic form plus arbitrary affine terms.

Then `Q` has a continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity
 <= (15/2^(1/5)) Delta^(-2/5) |a|^(-1/5).`                         (3.2)

Numerically,

`15/2^(1/5)=13.058258449441862...`.                                 (3.3)

No physical-coordinate leverage bound on `S` is imposed. In particular (3.2) remains valid when one receiver coordinate has leverage exactly one, where the low-leverage geometric Brascamp--Lieb gate fails maximally.

### Rank-one receiver form

If

`A[J,J]=lambda r r^T`, `||r||=1`,

write

`r=V c+Omega w`, `Omega=||(I-VV^T)r||>0`.

Then `a=lambda Omega^2`, and (3.2) becomes

`boxed: ||p_Q||_infinity
 <=(15/2^(1/5))
   (Delta Omega sqrt(|lambda|))^(-2/5).`                            (3.4)

This has the same scale-invariant currency as the designated partner's low-leverage transverse-Fresnel estimate, but does not require the augmented receiver leverage cap. Its price is the stronger structural hypothesis (3.1): there is no arbitrary diagonal receiver remainder outside the augmented three-space.

## 4. Proof: cross-frequency `L2` times a cubic time budget

Use orthonormal receiver coordinates

`Y=V^T X_J in R^2`, `Z=w^T X_J in R`.

Let `rho(y,z)` be their joint density. By the three-dimensional product-projection theorem,

`0<=rho<=M_3:=2^(3/2)`.                                             (4.1)

The receiver quadratic-plus-allowed-affine phase is a genuine quadratic polynomial

`q(y,z)=a z^2+2 L(y) z+q_0(y)`                                     (4.2)

with the same nonzero coefficient `a` for every `y`. Thus, after completing the scalar square in `z`, each fixed-`y` phase is a translated scalar quadratic with coefficient `a`.

Define

`h_t(y)=int_R rho(y,z) exp(i t q(y,z)) dz`,                         (4.3)

and let

`m(y)=int_R rho(y,z) dz`.

Then `int m=1`, and `|h_t(y)|<=m(y)`.

### 4.1 Unnormalised slice version of the cubic gate

Fix `y` with `m(y)>0`. The normalized slice `rho(y,z)/m(y)` is a probability density with cap at most `M_3/m(y)`. Applying (2.1) to (4.2) gives

`int_R |h_t(y)|^3 dt
 <=72*pi*M_3^2*m(y)/|a|`.                                          (4.4)

The identity is trivial when `m(y)=0`. Integrating over `y` and using `M_3^2=8` gives, for

`G(t)=||h_t||_(L^3(R^2_y))`,

`boxed: int_R G(t)^3 dt <=576*pi/|a|.`                             (4.5)

This is the central averaged-frequency resource. No pointwise power decay in `t` is claimed.

### 4.2 The rank-two cross coefficient supplies two-dimensional Plancherel

Put, in the `V` coordinates,

`A_I=Sigma U^T X_I in R^2`.

Its ordinary density satisfies

`||p_(A_I)||_infinity<=2/Delta`.                                    (4.6)

For fixed `t`, push the complex measure `exp(i t H(X_I)) dP_I` through `A_I`. Its Radon--Nikodym density `mu_t` with respect to Lebesgue measure satisfies

`|mu_t(a)|<=p_(A_I)(a)`,

hence

`||mu_t||_2 <=sqrt(2/Delta)`.                                      (4.7)

The receiver factor at cross coefficient `a0 in R^2` is

`F_t(a0)=int_R2 h_t(y) exp(i 2t a0 dot y) dy`.                     (4.8)

With Fourier convention `hat h(xi)=int exp(i xi dot y)h(y)dy`, two-dimensional Plancherel gives

`||hat h_t||_2=2*pi ||h_t||_2`.

The scaling `xi=2t a0` therefore yields, for `t!=0`,

`||F_t||_2 = pi |t|^(-1) ||h_t||_2`.                               (4.9)

Since the full characteristic function is the pairing of `mu_t` and `F_t`, Cauchy--Schwarz, (4.7), and (4.9) imply

`|phi_Q(t)|
 <=pi sqrt(2/Delta) |t|^(-1) ||h_t||_2`.                           (4.10)

Finally interpolate in the receiver projection:

`||h_t||_2
 <=||h_t||_1^(1/4)||h_t||_3^(3/4)
 <=G(t)^(3/4)`,                                                     (4.11)

because `||h_t||_1<=int m=1`. Hence

`boxed: |phi_Q(t)|
 <=pi sqrt(2/Delta)|t|^(-1) G(t)^(3/4).`                            (4.12)

The factor `G(t)^(3/4)` is deliberately retained. A phase-aligned law may make it large at isolated or sparse frequencies; only its global cubic budget (4.5) is used.

## 5. Integrating the mixed estimate and the exact constant

Let

`B=576*pi/|a|`,

so (4.5) is `int G^3<=B`. For any `T>0`, use `|phi_Q|<=1` on `|t|<=T`. On the two tails, apply Holder with exponents `4` and `4/3` to (4.12):

`int_(|t|>T) |phi_Q(t)| dt`

`<=pi sqrt(2/Delta)
   (int G^3)^(1/4)
   (int_(|t|>T) |t|^(-4/3) dt)^(3/4)`

`<=pi sqrt(2/Delta) B^(1/4) 6^(3/4) T^(-1/4).`                     (5.1)

Thus

`||phi_Q||_1 <=2T+A T^(-1/4)`,                                    (5.2)

where

`A=pi sqrt(2/Delta) B^(1/4) 6^(3/4)`.

The exact minimizer is

`T=(A/8)^(4/5)`,                                                     (5.3)

at which the right side of (5.2) is `10T`. Since

`A=2^(11/4) 3^(5/4) pi^(5/4)
   Delta^(-1/2)|a|^(-1/4)`,                                        (5.4)

we obtain

`||phi_Q||_1
 <=30*pi*2^(-1/5) Delta^(-2/5)|a|^(-1/5)`.                       (5.5)

Fourier inversion gives

`||p_Q||_infinity <=(2*pi)^(-1)||phi_Q||_1`,

which is exactly (3.2). Since `phi_Q in L1`, the density representative is continuous and vanishes at infinity. QED.

## 6. Why this theorem is a genuine replacement for false pointwise decay

The scalar phase correction is not weakened or bypassed. For a prescribed large `s`, one may still choose a fragmented cap-one density concentrated on intervals where `s x^2` is almost an integer multiple of `2*pi`, making the scalar quadratic transform close to one.

The proof instead needs only

`int |scalar quadratic transform|^3 dt < infinity`,

applied to **unnormalised slices of an actual three-dimensional product projection**, and combines that time-integrated resource with a two-dimensional cross-frequency Plancherel estimate. Formula (4.12) is intentionally not replaced by `C|t|^(-alpha)`.

The smoothing currency is therefore mixed:

- two random cross-frequency dimensions supply `|t|^-1` after `L2` averaging;
- the transverse receiver curvature supplies a cubic time budget;
- Holder turns the two into `L1_t` without ever asserting a pointwise scalar stationary-phase estimate.

This is exactly the type of averaged-frequency replacement requested by the assignment.

## 7. Strict-N3 high-leverage zero-pivot collapse family paid by the new theorem

This family lies in the collapse set left by the preceding 08:17 B01 square-completion theorem: the only high-leverage receiver coordinate has physical pivot zero.

Let `m=2^q>=8`, let `H_m` be a normalized Sylvester--Hadamard matrix, and choose orthonormal Walsh vectors `u_1,u_2 in R^m`. Let the receiver bank have `m+1` coordinates. Denote its first coordinate vector by `e_0`, and choose orthonormal Walsh vectors `v,w` supported on the remaining `m` coordinates, with every nonzero entry of magnitude `m^(-1/2)`.

Fix `0<eta<=1/4`, put `c=1+eta`, and define

`K=c(u_1 e_0^T+u_2 v^T)`,

`A_m=[[eta H_m, K],[K^T, w w^T]].`                                 (7.1)

### 7.1 Exact spectral condition

If the `eta H_m` block is removed, the nonzero eigenvalues are

`+c,+c,-c,-c,+1`.

The perturbation `diag(eta H_m,0)` has operator norm `eta`, so singular-value Weyl gives

`s_4(A_m)>=c-eta=1`.                                                (7.2)

Thus every `A_m` satisfies the exact QFORM spectral hypothesis (indeed it has at least four eigenvalues of modulus at least one; the receiver `w` direction in fact remains an exact eigenvalue `+1`).

### 7.2 Strict no-pivot geometry

Physical diagonals satisfy

`max_i |(A_m)_ii| <=max(eta/sqrt(m),1/m) ->0`.                      (7.3)

For two `I` coordinates, every principal pair determinant has magnitude at most `2 eta^2/m`. Receiver-receiver principal determinants vanish because `w w^T` has rank one. For one `I` coordinate and the distinguished receiver coordinate `e_0`,

`|det A[{i,e_0},{i,e_0}]|=c^2/m`.                                  (7.4)

For one `I` coordinate and one diffuse receiver coordinate,

`|det| <=eta/m^(3/2)+c^2/m^2`.                                    (7.5)

Hence for every fixed no-pivot threshold `tau>0`, all physical diagonals and all physical `2x2` principal determinants are below `tau` for sufficiently large `m`. This is a strict-N3 target family.

### 7.3 The previous high-leverage physical completion cannot start

The augmented receiver subspace is

`S=span(e_0,v,w)`.

Its leverage at the distinguished physical coordinate is exactly

`ell_0=1`.                                                          (7.6)

Thus the designated partner's low-leverage gate fails maximally. Moreover

`(A_m)_(e_0,e_0)=0`,                                                (7.7)

so the preceding 08:17 B01 high-leverage square-completion theorem cannot use this only high-leverage coordinate: its required physical pivot `a_j` is zero. This is a literal member of its surviving collapse set, not a relabelled already-paid case.

### 7.4 New mixed-time estimate stays uniform

For (7.1),

`Delta=c^2`, `a=1`.

Theorem 3.1 gives, for every collection of admissible independent cap-one input laws,

`boxed: ||p_(X^T A_m X)||_infinity
 <=(15/2^(1/5)) c^(-4/5)
 <=13.058259.`                                                      (7.8)

For the concrete stress value `eta=1/4`, `c=5/4`,

`boxed: ||p_(X^T A_m X)||_infinity
 <=10.9233852182.`                                                  (7.9)

The density is continuous. Every individual mixed physical coefficient in the diffuse part tends to zero; the theorem spends the whole rank-two cross area and the whole transverse quadratic curvature before selecting a physical pivot.

## 8. Actual application of the newest designated partner result

To apply account02/B01 auto14 to an actual inequality, augment (7.1) by a disjoint two-coordinate bank `D` with coefficient matrix

`C_D=[[0,1],[1,0]]`,

and no `D` cross terms to `I union J`. Then, in the partner's ordered convention,

`F_D=sum_(r!=s)(C_D)_(rs)^2=2`.                                    (8.1)

The target spectral hypothesis remains true because the original block (7.1) already has at least four absolute eigenvalues at least one. The partner theorem (2.2), with `Delta=c^2`, therefore gives the **actual target-level inequality**

`boxed: ||p_Q||_infinity
 <=22.104 c^(-4/5) 2^(-1/10).`                                     (8.2)

For `eta=1/4`, `c=5/4`, this is

`boxed: ||p_Q||_infinity <=17.252.`                                 (8.3)

This application retains the arbitrary `eta H_m` same-bank curvature and uses the partner's source-disjoint weighted-Fourier packet exactly at an equation. It is not a bibliography-only reference. The new theorem is sharper for the unaugmented collapse family; the partner theorem covers a different robust extension with an independent off-diagonal packet.

## 9. Finite checks

A deterministic numerical regression in this run checks powers-of-two `m=8,16,32,64` at `eta=1/4`. It finds:

- the first four singular values all exceed one;
- the fifth singular value is exactly one to numerical precision;
- the maximum physical diagonal decreases to zero;
- the maximum physical principal-pair determinant decreases to zero;
- the analytic constants are `13.0582584494...` and `10.9233852182...` for `c=1` and `c=5/4` respectively.

The calculation is only a sanity check. The spectrum and determinant estimates are proved algebraically in Section 7.

## 10. What changed in the proof map

Before this run, the rank-two-cross/one-receiver-square architecture was paid in two main ways:

1. low augmented leverage, by account02/B01's Fresnel/Brascamp--Lieb theorem;
2. high leverage with a usable nonzero physical receiver pivot whose completion leaves nonzero aggregate two-area, by the preceding B01 Schur-area theorem.

The present theorem pays a distinct part of the surviving collapse set: **the high-leverage pivot may be zero**, provided the entire receiver curvature lives in the augmented three-space and has nonzero curvature in the direction transverse to the rank-two cross row-space. No physical completion is performed.

The remaining structural obligation inside this architecture is now narrower:

`QFORM-RANK2-RECEIVER-OUTSIDE-S-ROUTING-v1`:

when the receiver self block has substantial curvature outside `S=span(range K^T,w)`, or outside-conditioned affine leakage leaves `S`, route that curvature either to the newest partner's source-disjoint weighted-Fourier packet, to a volume/ridge/grouped/hub branch, or prove a mixed-time extension that keeps the additional physical-coordinate phases without replacing them by a false scalar pointwise estimate.

The full N3 statement and hence the full QFORM theorem remain OPEN. No exhaustive spectral-to-structure reduction is claimed.

## 11. Continuity status

- Theorem 3.1 and the strict-N3 collapse family in Section 7: **continuous density proved**, because the full characteristic function is in `L1`.
- Partner application in Section 8: **continuous density proved** by the partner's `L1` Fourier theorem.
- Full QFORM continuity: **OPEN**.

## 12. Review status and provenance boundary

This is a new supporting theorem and has not received the two independent end-to-end reviews required for a full candidate solution. It does not alter the owner target or any scheduler state. Repository retrieval/writeback is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
