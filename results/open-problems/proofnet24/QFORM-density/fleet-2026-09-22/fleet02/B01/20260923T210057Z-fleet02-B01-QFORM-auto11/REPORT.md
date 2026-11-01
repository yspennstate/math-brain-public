SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B01, 2026-09-23T21:00:57Z.
attacking: the exact W2=0 near-null endpoint, by preserving its global diagonal-plus-rank-two structure through the partner's scalar-Schur routing and paying every residual rank-two tube with the bilateral half-Riesz receiver.

# fleet02/B01 — W2-zero diagonal-plus-rank-two routing and rank-two tube payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T210057Z-fleet02-B01-QFORM-auto11`  
Role: Oscillatory replacement / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING ROUTING THEOREM + PAID RANK-TWO SUBBRANCH / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction boundary

The target is unchanged: independent real coordinates with probability densities at most one, arbitrary real symmetric `A` with `s_3(A)>=1`, and no moment, compact-support, iid, Gaussian, log-concavity, connected-support, diagonal-basis or post-rotation-independence assumption. Essential boundedness is the target; continuity is separate.

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with no fleet02/B01 pause or stop. The live corrections are retained. In particular no law-uniform scalar pointwise quadratic-phase decay is used, no independence is asserted after rotation, no arbitrary-joint coarea bound is used, and no small random quadratic tail is discarded on unbounded inputs. The phase-aligned fragmented-support counterexample to uniform pointwise Fresnel decay remains valid and is not weakened by this run.

## 2. Sources actually used

### 2.1 Required 20260922T211500Z Fourier package

Pinned source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Two exact interfaces are used.

First, the fractional-potential/square-peel interface gives, after completing one ORIGINAL coordinate with coefficient `a!=0`,

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`,                       (2.1)

where `R` is the exact scalar Schur residual and

`H_(1/2)(R)=sup_s E|R-s|^(-1/2)`.

Second, Theorems D, D' and D5 spend third/fifth cross volume. Section 4 below applies them to a concrete obstruction: in the exact `W2=0` class every physical cross block has rank at most two, so their `Z_3` and `Z_5` currencies vanish identically.

### 2.2 Previous bilateral projected-Plancherel receiver

Source: `yspennstate/math-open-problems@5aaab64e61035d0ccb3be7f947e50f55d9a4711b`, fleet02/B01 r36.

For a residual quadratic polynomial on two disjoint ORIGINAL-coordinate banks whose physical cross block has exact rank two with nonzero singular values `sigma_1,sigma_2`, arbitrary same-bank quadratic curvature and affine terms are allowed and

`H_(1/2)(R) <= 8 (sigma_1 sigma_2)^(-1/4)`.                       (2.2)

Equivalently its proof uses the joint averaged-frequency envelope

`|phi_R(t)| <= min(1, 2*pi/(|t| sqrt(sigma_1 sigma_2)))`,         (2.3)

then integrates only after inserting the half-Riesz weight. This is the oscillatory replacement used below.

### 2.3 Newest designated partner fleet03/B01

Source: `yspennstate/math-open-problems@d78ae0f6e38047072728cc9a0c53d3499d242222`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T212842Z-auto11/REPORT.md`.

The partner proves scalar-Schur singular-value persistence and the following high-physical-diagonal routing at threshold `alpha=beta=1/64`. If `s_3(A)>=1` and some literal physical diagonal satisfies `|A_ii|>=1/64`, then either

`||p_Q||_infinity < 3444.312`,                                   (2.4)

or after completing that literal coordinate the exact scalar Schur matrix `H` admits an ORIGINAL-coordinate cut `J|K` with `N=H[J,K]` satisfying

`||N||_F^2 > E0 := 3969/8192`,                                   (2.5)

`sum_(r=1)^4 s_r(N)^2 > (63/64)||N||_F^2`,                       (2.6)

and

`s_3(N) < 1/256`.                                                 (2.7)

The partner also pays diffuse fifth-volume and quantitative rank-three cross branches before reaching this survivor.

## 3. Exact `W2=0` structure

Let a literal physical pair `P={p,q}` have invertible principal block `B=A[P,P]`. Write the remaining coordinates as `L`, let `C=A[P,L]`, and let

`S=A/B=A[L,L]-C^T B^(-1) C`                                     (3.1)

be the exact pair Schur complement in ORIGINAL coordinates. In the scalar-pivot notation of the overlap-two theorem,

`W2 = det(B)^2 sum_(k!=l) S_kl^2`.                               (3.2)

Hence `W2=0` iff `S` is diagonal.

In that case define

`D=diag(0_P,S)`,

`R=[[B,C],[C^T,C^T B^(-1) C]]`.                                 (3.3)

If `K=[B,C]` is the `2 x n` row block, then exactly

`R=K^T B^(-1) K`,                                                 (3.4)

so

`A=D+R`,   `D` diagonal,   `rank R<=2`.                          (3.5)

This is the algebraic checkpoint already saved early in this run. If `d_1>=d_2>=...` are the decreasing absolute diagonal entries of `D`, then `s_3(A)>=1` implies

`d_1>=1`,                                                         (3.6)

and the singular-value sum inequality gives

`max{d_2,s_2(R)}>=1/2`.                                          (3.7)

Thus `W2=0` is not spectrally empty even when its defining physical pair is arbitrarily near singular.

## 4. Required volume theorem applied at a concrete obstruction

For every disjoint original-coordinate cut `I|J`, the diagonal matrix `D` contributes no cross entries and

`A[I,J]=R[I,J]`.                                                  (4.1)

By (3.5),

`rank A[I,J] <= 2`.                                               (4.2)

Consequently

`e_3(A[I,J]^T A[I,J])=0`,
`e_5(A[I,J]^T A[I,J])=0`                                        (4.3)

for every physical cut. Therefore the required-source Theorem D, its relaxed-marginal extension D', and the unconditional fifth-volume theorem D5 have exactly zero currency throughout this class. This is an actual structural obstruction, not a summary of those theorems.

The strict-N3 witness in `EARLY_CHECKPOINT.md` shows that this obstruction occurs inside the owner target: one can have `W2=0`, at least four eigenvalues of modulus greater than one, yet every physical diagonal and every physical two-by-two principal determinant arbitrarily small.

## 5. New lemma: diagonal-plus-rank-two survives every scalar Schur completion

### Lemma 5.1 — `QFORM-DIAGRANK2-SCALAR-SCHUR-CLOSED-v1`

Suppose

`A=D+U C0 U^T`,                                                   (5.1)

where `D` is diagonal, `U` has at most two columns, and `C0` is a symmetric matrix of the corresponding size. Let `i` be any ORIGINAL coordinate with physical pivot

`a=A_ii=d_i+u_i^T C0 u_i !=0`,                                  (5.2)

where `u_i^T` is row `i` of `U`. Then the exact scalar Schur complement on the remaining original coordinates is

`H=D_-i + U_-i C1 U_-i^T`,                                      (5.3)

where

`C1=C0-a^(-1) C0 u_i u_i^T C0`.                                 (5.4)

In particular

`rank(H-D_-i)<=2`,                                                (5.5)

and every physical cross block of `H` has rank at most two.

#### Proof

The off-diagonal pivot column is exactly

`r=U_-i C0 u_i`,                                                  (5.6)

because `D` is diagonal. Hence

`H=A_-i,-i-a^(-1)rr^T`
` =D_-i+U_-i[C0-a^(-1)C0u_i u_i^T C0]U_-i^T`,                   (5.7)

which is (5.3)-(5.5). No probability, rotation, or approximation is involved. QED.

Applied to (3.5), this shows that the partner's scalar-Schur survivor `N=H[J,K]` is not merely approximately low rank: it has

`rank N<=2`                                                       (5.8)

exactly. Hence (2.6) is automatic and (2.7) strengthens to `s_3(N)=0`.

## 6. New analytic payment: every genuinely rank-two survivor is bounded

Assume the partner reaches its survivor (2.5)-(2.7). By (5.8) let the only possible nonzero singular values of `N` be `s_1>=s_2>=0`.

If

`s_2 >= eta := 1/256`,                                           (6.1)

then (2.5) gives

`s_1 >= sqrt(E0/2)=63/128`.                                      (6.2)

Therefore the rank-two singular product satisfies

`Delta=s_1 s_2 >= (63/128)(1/256)=63/32768`.                    (6.3)

Apply the bilateral projected-Plancherel theorem (2.2) to the exact scalar Schur residual. It permits all same-bank curvature of `H`, so

`H_(1/2)(R) <= 8 Delta^(-1/4)`.                                  (6.4)

The outer physical pivot obeys `|a|>=1/64`; spending the required-source square peel (2.1),

`||p_Q||_infinity`
` <= 8 |a|^(-1/2) Delta^(-1/4)`
` <= 64 (32768/63)^(1/4)`
` < 305.638`.                                                     (6.5)

This estimate is uniform over dimension, signs, all remaining coefficients, and every admissible cap-one product law. It is an averaged-frequency result: the rank-two packet supplies only the borderline `1/|t|` envelope and the outer literal square supplies the half-Riesz weight. No false scalar Fresnel decay is used.

## 7. Resulting routing theorem

### Theorem 7.1 — `QFORM-W2ZERO-HIGHDIAG-RANK2-TUBE-ROUTING-v1`

Assume the full target hypothesis `s_3(A)>=1`, and assume there exists an invertible literal physical pair for which the exact overlap-two currency `W2` vanishes. If some physical diagonal of `A` has magnitude at least `1/64`, then either

`boxed: ||p_Q||_infinity < 3444.312`,                            (7.1)

or, after scalar completion at a literal original coordinate, there exists an ORIGINAL-coordinate cut of the exact residual with cross block `N` satisfying

`boxed: rank N<=2`,                                               (7.2)

`boxed: ||N||_F^2 >3969/8192`,                                   (7.3)

and

`boxed: s_2(N)<1/256`.                                           (7.4)

In the second alternative the first singular value is necessarily macroscopic:

`s_1(N)^2 > E0-(1/256)^2 =31751/65536`,                         (7.5)

so

`boxed: s_1(N)>sqrt(31751)/256 >0.696047`.                       (7.6)

Thus the previous partner survivor is reduced, inside exact `W2=0`, from a top-four low-rank tube to an explicitly **rank-one-dominant** tube. Every genuinely rank-two tube at scale `s_2>=1/256` is paid by (6.5).

The theorem does not assert that the remaining rank-one-dominant tube is already paid. Full QFORM remains open.

## 8. Relation to the low-physical-diagonal branch

The completed fleet04/B20 physical-cut theorem gives, when all physical diagonals are `<1/64`, an ORIGINAL-coordinate cut with

`||A[J,K]||_F^2 >11907/16384`.                                   (8.1)

Inside `W2=0`, (4.2) makes that cut exact rank at most two. Hence the low-diagonal side of the same endpoint is also forced into a fixed-energy rank-one/rank-two physical cross tube rather than a third- or fifth-volume branch. A rank-two cross block alone cannot imply bounded density: the r36 curved-bicore counterexample has a logarithmically divergent density. Therefore another source-preserving third-curvature mechanism is genuinely necessary there.

This observation is why the next debt below is stated in rank-one-dominant terms rather than as another volume search.

## 9. First unpaid implication

The first unpaid implication is now

`QFORM-W2ZERO-RANK1-DOMINANT-THIRD-CURVATURE-ROUTING-v1`:

in a diagonal-plus-rank-two target state with a fixed-energy original-coordinate cross packet but `s_2<1/256`, extract the required third curvature without rotating the input law. In the high-diagonal branch it must be coupled to the already present outer square; in the all-small-diagonal branch it must come from literal/grouped diagonal curvature, a hub/random-slope packet, or another completed receiver. The exact obstruction is that direct rank-one or rank-two cross smoothing is below the `L^1_t` threshold, while arbitrary same-bank curvature cannot be discarded.

A useful next test is the exact-rank-one subcase of (7.2): attempt to rewrite its product-preserving crossing as the designated partner's `QFORM-RANK1-BILINEAR-PLUS-SQUARE-LP-v1` packet using a literal/grouped square forced by (3.6)-(3.7), and identify precisely when same-bank leakage prevents that decomposition.

## 10. Scope and status

This run proves a new algebraic closure lemma and a new target-level routing/payment theorem, and applies the required newest Fourier machinery and newest designated partner result at explicit equations. It does not prove or disprove the full conjecture. No continuity conclusion is claimed for Theorem 7.1 as a whole; the bounded subbranches inherit only the regularity stated in their source theorems.
