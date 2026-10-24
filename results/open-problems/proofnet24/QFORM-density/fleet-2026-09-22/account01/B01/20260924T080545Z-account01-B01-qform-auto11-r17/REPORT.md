SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-24T08:05:45Z.
attacking: uniform spectral stabilization of the two-hub rank-one arrowhead as the leaf-slope tail tends to zero.

# Uniform spectral stabilization of a two-hub rank-one arrowhead

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T080545Z-account01-B01-qform-auto11-r17`  
Role: account01/B01, Oscillatory replacement  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN / INDEPENDENT REVIEW PENDING**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

All scalar random variables below are ORIGINAL independent coordinates with probability densities bounded by one. No Gaussian, iid, moment, compact-support, connected-support, log-concavity, or smoothness assumption is used. No rotated random coordinates are declared independent. All statements below concern essential boundedness; continuity for arbitrary merely measurable input densities is not proved.

The phase-aligned fragmented-support obstruction remains binding. For any fixed nonzero frequency `t` and small `eta>0`, the set

`E_eta(t)={x: dist(t x^2,2 pi Z)<=eta}`

has arbitrarily large finite-measure truncations. Choose a measurable subset `E` of measure one in such a truncation and let `f=1_E`. Then

`Re int exp(i t x^2) f(x) dx >= cos eta`.

Thus no positive law-uniform pointwise power decay `|E exp(i t X^2)|<=C|t|^{-alpha}` can hold over all cap-one densities. Nothing below uses such a claim. The replacement mechanism is spectral allocation followed by already-proved **integrated fractional-potential** estimates on literal original-coordinate blocks.

Fresh programme controls mark the unrestricted conjecture and the full continuity assertion OPEN.

## 2. Source-pinned premises actually used

### 2.1 Previous account01/B01 rank-one-slope compiler

Source:

`yspennstate/math-open-problems@5a750c5b1188ea297a92c01b9692de5d87ab7f4c`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260924T041020Z-account01-B01-qform-auto11-r12/REPORT.md`.

Its theorem `QFORM-TWOHUB-RANK1-SLOPE-COMPILER-v1` states the following. After one literal original-coordinate completion

`Q=a(X_0+h)^2+R`, `a!=0`,

suppose

`R=H^T C H + 2(b^T H)(z^T Y)+sum_j d_j Y_j^2 + affine`,

where `H=(H_1,H_2)` are two original hub variables, `Y` is a disjoint original leaf bank, `C=C^T` is arbitrary, and

`kappa=||b||_2 ||z||_2>0`.

If `s_3(A)>=s>0`, then

`||p_Q||_infinity
 <= |a|^(-1/2) max{
      128*2^(3/4) kappa^(-1/2),
      41.3265039834376 kappa^(-2/5) s^(-1/10)
    }.`                                                     (2.1)

This is product-preserving and uses distribution-function / joint-frequency estimates rather than scalar pointwise Fresnel decay.

### 2.2 Newest designated partner: 3D two-large-direction half-Riesz

Source:

`yspennstate/math-open-problems@522585af1e80eff6ad75808d7e3be55a3a2bc8ac`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T070034Z-account02-B01-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-3D-S2-HALFRIESZ-v1` states: if a symmetric `3x3` coefficient matrix `B` has at least two singular values at least one, then for three independent cap-one original coordinates and arbitrary affine terms,

`H_(1/2)(Z^T B Z+affine)<169`,                               (2.2)

where `H_(1/2)(W)=sup_u E|W-u|^(-1/2)`.

By homogeneity, if `s_2(B)>=rho>0`, then

`H_(1/2)(Z^T B Z+affine)<169 rho^(-1/2).`                    (2.3)

The partner proof itself uses original-coordinate spectral allocation, a physical-edge averaged quarter-potential, and a logarithmic square interface; it does not use the false scalar pointwise-decay claim.

### 2.3 Orientation-free rank-two affine half-Riesz

Source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an invertible symmetric `2x2` coefficient `Lambda`, two original independent coordinates, and arbitrary affine terms,

`H_(1/2)<=128 |det Lambda|^(-1/4).`                          (2.4)

The theorem is orientation-free and has no affine-in-range assumption.

### 2.4 Literal scalar-square peel

The pinned Fourier package used by both preceding sources gives: for an exact completion in one original coordinate,

`Q=a(X_0+h(Z))^2+R(Z)`, `a!=0`,                              (2.5)

one has

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R).`                (2.6)

Only essential boundedness is inferred from this interface.

## 3. Exact rank-one completion persistence

Write the full quadratic coefficient in the outer original coordinate as

`A=[[a,r^T],[r,B]]`, `a!=0`,

and let

`S=B-r r^T/a`                                                  (3.1)

be its exact Schur coefficient after completing that scalar. Then

`A=(1/a) [a;r][a;r]^T + diag(0,S).`                            (3.2)

The first term has rank one. Therefore the standard rank-one singular-value interlacing inequality gives

`s_2(S)>=s_3(A).`                                              (3.3)

Thus under `s_3(A)>=s`, every literal outer completion leaves at least two residual singular directions at scale `s`, even though their coordinate realization can change drastically.

This is the spectral resource that stabilizes the vanishing-tail arrowhead endpoint below.

## 4. Main theorem: uniform stability as the rank-one leaf slope vanishes

### Theorem 4.1 — `QFORM-TWOHUB-RANK1-SPECTRAL-STABILITY-v1`

Assume `s_3(A)>=s>0`. Suppose one ORIGINAL coordinate has nonzero literal pivot `a` and, after its exact completion, the residual coefficient has the two-hub rank-one-arrowhead form

`S = [[C, b z^T],
      [z b^T, D]],`                                           (4.1)

where

- `C=C^T` is arbitrary `2x2` hub curvature;
- `D=diag(d_1,...,d_m)` is an arbitrary diagonal leaf block;
- `b in R^2`, `z in R^m` are arbitrary, including zero.

Then for every independent cap-one product law and arbitrary affine terms,

`boxed:
 ||p_Q||_infinity < 352 |a|^(-1/2) s^(-1/2).`                (4.2)

In particular, at owner scale `s=1`, if `|a|>=1/64`,

`boxed: ||p_Q||_infinity <2816.`                              (4.3)

The bound is uniform as the entire leaf slope tends to zero. It therefore closes the quantitative gap between the previous nonzero-slope compiler and the partner's exact single-leaf endpoint for this residual geometry.

### Proof

Set

`kappa=||b||_2 ||z||_2`.                                      (4.4)

The off-diagonal hub-leaf perturbation

`K=[[0,bz^T],[zb^T,0]]`                                       (4.5)

has operator norm exactly

`||K||=kappa`.                                                 (4.6)

Indeed the rectangular block `bz^T` has the single nonzero singular value `||b||||z||`, and the symmetric dilation in (4.5) has eigenvalues `+-kappa` plus zeros.

By (3.3),

`s_2(S)>=s`.                                                   (4.7)

Split at the fixed dimensionless threshold

`kappa = 3s/8`.                                                (4.8)

#### Case I: `kappa>=3s/8`

Apply the previous account01/B01 theorem (2.1). Its first branch is bounded by

`128*2^(3/4) kappa^(-1/2)
 <=128*2^(3/4)*(8/(3s))^(1/2)
 =351.533592560148... s^(-1/2).`                              (4.9)

Its second branch is bounded by

`41.3265039834376 kappa^(-2/5)s^(-1/10)
 <=41.3265039834376*(8/3)^(2/5)s^(-1/2)
 =61.180942152357... s^(-1/2).`                               (4.10)

Thus (4.2) holds in Case I.

#### Case II: `kappa<3s/8`

Delete only the **coefficient block** `K` for the purpose of deterministic singular-value comparison; no random quadratic term is discarded from the law. Define

`T=diag(C,D)`, so `S=T+K`.                                     (4.11)

Weyl's singular-value inequality and (4.7) give

`s_2(T)>=s_2(S)-||K||>s-3s/8=5s/8.`                           (4.12)

The singular values of `T` are exactly the multiset union of the two singular values of `C` and the numbers `|d_j|`. Therefore one of the following three spectral allocations occurs.

##### II-a. Both large directions lie in the hub block

If

`s_2(C)>=5s/8`,                                                (4.13)

condition on all leaf coordinates. The remaining quadratic polynomial in the two original hub coordinates has coefficient `C` and an arbitrary affine term. Since both singular values of `C` are at least `5s/8`,

`|det C|>=(5s/8)^2`.                                          (4.14)

The orientation-free theorem (2.4) gives, uniformly in the conditioning,

`H_(1/2)(R)
 <=128(5s/8)^(-1/2)
 =128 sqrt(8/5) s^(-1/2)
 =161.908616200621... s^(-1/2).`                              (4.15)

Averaging the conditioning and applying (2.6) proves (4.2).

##### II-b. Both large directions lie in literal leaf squares

If distinct leaves `i,j` satisfy

`|d_i|,|d_j|>=5s/8`,                                          (4.16)

condition on every residual coordinate except `Y_i,Y_j`. Their conditional quadratic coefficient is exactly `diag(d_i,d_j)`; all hub-leaf couplings become arbitrary affine terms. Hence (2.4) again gives

`H_(1/2)(R)
 <=128 |d_i d_j|^(-1/4)
 <=128 sqrt(8/5) s^(-1/2).`                                  (4.17)

Then (2.6) proves (4.2).

##### II-c. One large hub direction and one large leaf square

Assume neither II-a nor II-b occurs. Since `s_2(T)>5s/8`, necessarily

`s_1(C)>=5s/8`                                                 (4.18)

and there exists a leaf `j` with

`|d_j|>=5s/8`.                                                 (4.19)

Consider the literal ORIGINAL three-coordinate block on `(H_1,H_2,Y_j)`:

`B_j=[[C,b z_j],[z_j b^T,d_j]].`                               (4.20)

Its block-diagonal part `diag(C,d_j)` has at least two singular values at least `5s/8`. The cross perturbation in (4.20) has norm

`||b|| |z_j| <= ||b|| ||z|| = kappa <3s/8`.                  (4.21)

Weyl therefore yields

`s_2(B_j)>5s/8-3s/8=s/4.`                                     (4.22)

Condition on every other leaf. Those variables can only contribute arbitrary affine terms and constants to the three-coordinate polynomial. The newest designated-partner theorem (2.3), at `rho=s/4`, gives

`H_(1/2)(R)<169(s/4)^(-1/2)=338 s^(-1/2).`                   (4.23)

Finally (2.6) proves (4.2).

The three subcases exhaust Case II, and Case I together with Case II proves the theorem. QED.

### Why this is not a rough-tail perturbation argument

The small condition `kappa<3s/8` is used only in the deterministic matrix inequality (4.12). The random term `2(b^T H)(z^T Y)` is kept exactly in every conditional law. In subcase II-c it remains inside the literal `3x3` core to which the partner theorem is applied. Thus no bounded-density law is approximated by deleting a small coefficient matrix on unbounded inputs.

## 5. Actual application of the newest designated partner theorem

For `0<=epsilon<=1`, consider four ORIGINAL independent cap-one coordinates `(X_0,H_1,H_2,Y)` and

`Q_epsilon
 =X_0^2+2H_1^2+2Y^2+2 epsilon H_1Y.`                         (5.1)

The physical coefficient matrix is

`A_epsilon=
 [[1,0,0,0],
  [0,2,0,epsilon],
  [0,0,0,0],
  [0,epsilon,0,2]].`                                          (5.2)

Its spectrum is exactly

`{0,1,2-epsilon,2+epsilon}.`                                  (5.3)

Hence it satisfies the owner target for every `0<=epsilon<=1`. After peeling `X_0^2`, the residual `3x3` core has eigenvalues

`{0,2-epsilon,2+epsilon}`,                                    (5.4)

so it has two eigenvalues of modulus at least one uniformly, including at the vanishing-coupling endpoint `epsilon=0`.

Apply the newest account02/B01 theorem `QFORM-3D-S2-HALFRIESZ-v1` directly to this residual. It gives the actual inequality

`H_(1/2)(R_epsilon)<169`,                                     (5.5)

and the literal square peel yields

`boxed:
 ||p_(Q_epsilon)||_infinity<169,
 0<=epsilon<=1.`                                              (5.6)

Thus the partner theorem supplies a uniform law-independent bound exactly across a coupling that tends to zero. The new Theorem 4.1 extends the same stability principle from this literal three-coordinate family to an arbitrary-dimensional diagonal leaf tail and arbitrary two-hub curvature.

## 6. Relation to the failed pointwise route

The proof has no scalar estimate of the form

`|E exp(i t X^2)| <= C |t|^(-alpha)`                           (6.1)

for arbitrary cap-one densities. The only analytic smoothing inputs are already-proved fractional-potential estimates obtained from integrated / joint-frequency arguments on physical original-coordinate blocks. The new step is deterministic spectral allocation before any inverse coefficient is paid.

In particular, the theorem resolves the specific `kappa ->0` divergence in (2.1) without claiming that the weak rank-one cross term itself supplies uniform oscillatory decay. When that cross term is weak, the target's two residual large singular directions are forced into the hub block, literal leaf squares, or a literal three-coordinate core, each of which has a source-valid half-Riesz receiver.

## 7. What is and is not closed

Closed in this run: after one nonzero literal outer scalar pivot, the entire residual geometry

`two original hubs + arbitrary diagonal leaf bank + rank-one hub-leaf cross block`

has a scale-free density compiler (4.2), including the exact zero-slope and almost-single-leaf limits.

Not closed: the full conjecture. The estimate still costs `|a|^(-1/2)`, so it is not uniform when every usable literal outer pivot is tiny or zero. The genuine non-arrowhead / rank-two-cross finite-leak survivor also remains to be routed without taking reciprocals of currencies allowed to vanish.

First unpaid implication:

`QFORM-OUTER-PIVOT-REMOVAL-OR-RANK2-CROSS-AGGREGATION-v1`.

Under `s_3(A)>=1`, force either a target-scale literal scalar pivot whose Schur residual falls into an already-paid geometry, or an aggregate physical-pair / rank-two-cross / grouped currency that pays the form directly before a tiny scalar pivot is inverted. Small nonzero coefficient tails must remain in the law.

The unrestricted QFORM target remains **OPEN**. The full continuous-density conclusion remains **OPEN**.
