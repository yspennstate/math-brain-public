SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-24T03:20:47Z.
attacking: replace the leverage upper bound on third-compound overlap by the exact shared-coordinate collision functional, then compute it on a high-collision rotated indefinite involution where the previous B04 certificate fails.

# fleet01/B04 r27 — exact third-compound collision and orthogonal zero-diagonal formula

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW STRICT REFINEMENT OF r26 / EXACT STRUCTURAL IDENTITY / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Continuity: the new paid branch has `p_Q in C_0(R)`; unrestricted continuity remains OPEN.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. All random variables remain original product coordinates. No post-rotation independence, moment/support/log-concavity assumption, arbitrary-joint coarea bound, fiber-supremum estimate, or law-uniform pointwise quadratic-phase decay is used.

## 1. Fresh source boundary and first missing implication

Fresh `math-research-brain/main` was resolved at control commit

`dd5a4025756b11e275f3e344211fab71a7d7ef0c`.


The analytic receiver used below is fleet03/B04 `QFORM-CROSS-E3-OPTIMAL-THRESHOLD-v1`, source

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T215155Z-fleet03-B04-QFORM-auto11-r42/REPORT.md`.

For every literal original-coordinate cross block `M`, with arbitrary same-bank quadratic curvature and induced affine terms,

`||p_Q||_infinity <= C_* E_3(M)^(-1/6)`,

`C_*=8.45302122552817687470491804598...`,                         (1.1)

and the characteristic function is in `L^1`, hence the density lies in `C_0(R)`.

The preceding B04 r26 theorem introduced

`chi_3(S)=sum_i ell_i mu_i`

and proved

`Delta_3^disj(S)>=(1-chi_3(S))e_3(S^2)`.                          (1.2)

The first missing implication attacked here is that `chi_3` is still only an **upper bound** on actual row-column overlap. It can equal `3` even when a constant fraction of the third-compound energy is already disjoint. The correct next currency is the exact shared-coordinate collision itself.

## 2. Exact compound-collision hierarchy

Let `S=S^T` be any real symmetric physical coefficient carrier with

`E=e_3(S^2)=||C_3(S)||_F^2>0`,                                   (2.1)

where `C_3(S)=wedge^3 S` is indexed by physical three-subsets.

For each physical subset `H` with `1<=|H|<=3`, let `P_H` denote the coordinate projection in third exterior power onto basis triples containing `H`. Define

`zeta_q(S)=E^(-1) sum_(|H|=q) ||P_H C_3(S) P_H||_F^2`,
`q=1,2,3`.                                                        (2.2)

Put the canonical squared-minor law

`q_S(R,T)=det(S[R,T])^2/E`, `|R|=|T|=3`.                          (2.3)

If `K=|R intersect T|`, then directly from (2.2),

`boxed: zeta_q(S)=E_q[binom(K,q)].}`                              (2.4)

Indeed a fixed squared minor is counted once for every `q`-subset of `R intersect T`.

Therefore binomial inversion at `K in {0,1,2,3}` gives the exact identity

`boxed:
 Delta_3^disj(S)/E
 =1-zeta_1(S)+zeta_2(S)-zeta_3(S).`                               (2.5)

Equivalently, if `W_k` denotes the fraction of squared-minor energy with intersection size exactly `k`, then

`zeta_1=W_1+2W_2+3W_3`,
`zeta_2=W_2+3W_3`,
`zeta_3=W_3`,
`W_0=1-zeta_1+zeta_2-zeta_3`.                                    (2.6)

Since

`zeta_2-zeta_3=W_2+2W_3>=0`,                                     (2.7)

we obtain the simple but strictly sharper collision theorem

`boxed:
 Delta_3^disj(S)>=(1-zeta_1(S))E.`                                (2.8)

The improvement over r26 is literal. Its proof gave, for each coordinate,

`||P_i C_3(S)P_i||_F^2 <= ell_i mu_i E`.                          (2.9)

Summing (2.9) yields

`boxed: zeta_1(S)<=chi_3(S)<=sum_i ell_i^2.}`                     (2.10)

Thus every r25/r26 collision certificate is preserved, while actual overlap can be much smaller than either leverage surrogate.

### Theorem `QFORM-EXACT-THIRDCOMPOUND-COLLISION-v1`

For every symmetric carrier `S` with `E>0` and `zeta_1(S)<1`, some literal original-coordinate cut `I disjoint-union J` satisfies

`E_3(S[I,J]) >= (1-zeta_1(S))E/64`.                              (2.11)

Consequently any ambient quadratic form whose retained physical block differs from `S` only by diagonal terms satisfies

`boxed:
 ||p_Q||_infinity
 <=2 C_* [(1-zeta_1(S))e_3(S^2)]^(-1/6),}`                       (2.12)

and

`boxed: p_Q in C_0(R).}`                                         (2.13)

More sharply, using (2.5),

`||p_Q||_infinity
 <=2 C_* [E(1-zeta_1+zeta_2-zeta_3)]^(-1/6)`                     (2.14)

whenever the bracket is positive.

#### Proof

Color physical coordinates independently into labelled banks `I,J` with probability `1/2`. Every ordered disjoint pair `(R,T)` of triples lands with `R subset I`, `T subset J` with probability `2^-6`. Hence

`E_cut E_3(S[I,J])=Delta_3^disj(S)/64`.                           (2.15)

Use (2.8) or the exact identity (2.5), choose a deterministic cut achieving at least the mean, and apply (1.1). The receiver is uniform in arbitrary same-bank curvature and affine terms and supplies an `L^1` Fourier majorant, proving (2.12)-(2.14) and `C_0`. QED.

## 3. Closed formula for symmetric orthogonal zero-diagonal carriers

The exact collision functional can be computed without any leverage estimate on an important high-collision family.

### Theorem `QFORM-ZERODIAG-ORTHOGONAL-COLLISION-v1`

Let `S=S^T`, `S^2=I_n`, and `S_ii=0` for every physical coordinate. Then

`boxed: zeta_1(S)=6/(n-1).}`                                      (3.1)

Hence for `n>=8`,

`boxed:
 Delta_3^disj(S)
 >=[(n-7)/(n-1)] binom(n,3).}`                                   (3.2)

For a nonzero scalar `c`, the same collision parameter holds for `cS`, while

`e_3((cS)^2)=|c|^6 binom(n,3)`.                                  (3.3)

Therefore every ambient form with the same off-diagonal coefficients as `cS` obeys

`boxed:
 ||p_Q||_infinity
 <= [2C_*/|c|]
    {[(n-7)/(n-1)] binom(n,3)}^(-1/6),
 p_Q in C_0(R),`                                                  (3.4)

for `n>=8`.

#### Proof of (3.1)

Because `S` is orthogonal, every row of `C_3(S)` has squared norm one, so the row triple `R` is uniform under the canonical law and

`E=binom(n,3)`.                                                    (3.5)

Fix a physical triple `R` and let `B=S[R,:]`. Its three rows are orthonormal. Cauchy-Binet with one marked column (equivalently, differentiate `det(B diag(w) B^T)` at `w_i=1`) gives

`sum_(T contains i, |T|=3) det(B[:,T])^2
 = sum_(r in R) S_ri^2`.                                         (3.6)

Therefore

`sum_T |R intersect T| det(S[R,T])^2
 = sum_(i in R) sum_(r in R) S_ri^2
 = ||S[R,R]||_F^2`.                                               (3.7)

Sum over all triples `R`. Every ordered off-diagonal pair `(r,i)`, `r!=i`, belongs to exactly `n-2` triples, whereas diagonal entries contribute zero. Since `S` is orthogonal and has zero diagonal,

`sum_(r!=i) S_ri^2=||S||_F^2=n`.                                 (3.8)

Thus the numerator of `zeta_1` equals `n(n-2)`. Dividing by (3.5),

`zeta_1=n(n-2)/binom(n,3)=6/(n-1)`.                               (3.9)

QED.

This theorem exposes a regime missed completely by r26: because `S` is full rank with equal singular values, `ell_i=1`, `mu_i=3/n`, and therefore

`chi_3(S)=3`,                                                      (3.10)

so r26 gives no positive disjoint-energy lower bound, while (3.1) is `<1` as soon as `n>=8`.

## 4. Genuinely rotated indefinite eight-dimensional stress matrix

Let

`H=(1/2)*[[ 1, 1, 1, 1],
           [ 1,-1, 1,-1],
           [ 1, 1,-1,-1],
           [ 1,-1,-1, 1]]`,                                     (4.1)

so `H H^T=I_4`, and define

`S_0=[[0,H],[H^T,0]]`.                                            (4.2)

Then `S_0=S_0^T`, `S_0^2=I_8`, and `diag(S_0)=0`. Put

`A_*=2S_0+(1/8)I_8`.                                              (4.3)

The physical form is non-diagonal and mixes four coordinates against four Hadamard combinations. Its spectrum is exactly

`{17/8 (x4), -15/8 (x4)}`,                                       (4.4)

so it is genuinely indefinite and satisfies the owner's spectral hypothesis very strongly.

The new general orthogonal formula gives

`zeta_1(S_0)=6/7`,
`e_3((2S_0)^2)=64 binom(8,3)=3584`.                               (4.5)

Therefore (2.12) yields

`boxed:
 ||p_(X^T A_* X)||_infinity
 <= C_*/sqrt(2)
 =5.977188630084794...,
 p_(X^T A_* X) in C_0(R).}`                                      (4.6)

The exact collision hierarchy is sharper still on this matrix. Direct exact arithmetic gives, for the unscaled `S_0`, intersection-size squared-minor energies

`(W_0,W_1,W_2,W_3)=(20,24,12,0)`,
`E=56`.                                                           (4.7)

Hence

`zeta_1=6/7`, `zeta_2=3/14`, `zeta_3=0`,
`Delta_3^disj/E=5/14`.                                           (4.8)

For `2S_0`,

`Delta_3^disj=64*20=1280`.                                       (4.9)

Random cutting therefore guarantees a literal physical crossing with

`E_3(M)>=1280/64=20`,                                             (4.10)

and the exact version (2.14) improves (4.6) to

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=C_* 20^(-1/6)
 =5.130664621761596... .}`                                       (4.11)

This calculation is a finite exact check of the new hierarchy; the theorem itself is analytic and does not depend on numerics.

## 5. Designated fleet02/B04 result applied to an actual inequality

The completed partner result used here is fleet02/B04

`QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`,

source path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260923T111930Z-qform/REPORT.md`

on current master. Its exact-rank-three branch states that a literal physical cross block with `rank(M)=3` and `E_3(M)=Z>0` gives

`||p_Q||_infinity <=6 Z^(-1/6)`                                  (5.1)

with a continuous `C_0` density, while retaining arbitrary same-bank curvature and induced affine terms.

Apply it to the **same** matrix `A_*`. Take any three physical rows from the first four-coordinate bank and all four columns from the second bank. The crossing is

`M=2 H_{3 x 4}`.                                                   (5.2)

The chosen Hadamard rows are orthonormal, hence

`M M^T=4I_3`,
`E_3(M)=det(MM^T)=64`.                                            (5.3)

Partner (5.1) therefore gives the actual inequality

`boxed:
 ||p_(X^T A_* X)||_infinity<=6*64^(-1/6)=3,
 p_(X^T A_* X) in C_0(R).}`                                      (5.4)

This special-geometry partner certificate is sharper than (4.11). The point of the new theorem is not to beat every hand-picked cross packet; it is to replace the r26 leverage surrogate by an exact collision currency that remains informative in classes where `chi_3=3` and therefore the previous aggregate theorem is completely silent.

The newer fleet02/B04 r16 diffuse-residual theorem was also read. Its leverage gate is not applicable to the full-rank orthogonal carrier here (`beta=1` in its full-range frame), so it is not silently invoked.

## 6. What is paid and what remains

**Paid in this run:**

1. The third-compound disjoint fraction is exactly
   `1-zeta_1+zeta_2-zeta_3`.
2. The sufficient collision gate improves from r26's `chi_3<1` to the strictly weaker exact gate `zeta_1<1`.
3. Every symmetric orthogonal zero-diagonal carrier in dimension `n>=8` has `zeta_1=6/(n-1)<1`, even though `chi_3=3` identically.
4. The resulting branch has a bounded continuous `C_0` density with explicit constant (3.4).

The full conjecture is still open. In the localized overlap-two small-pair branch from r24-r26, the complement-curvature route is now paid whenever either

`zeta_1(off(C))<1`

with target-scale `e_3(off(C)^2)`, or any earlier stronger cross/pair/ridge receiver applies.

The first remaining implication for this B04 route is sharpened to

`QFORM-SMALLPAIR-EXACT-COLLISION-OR-LOW-STABLERANK-ROUTING-v1`:

> In the small-pair overlap-two state, handle the residual cases in which the large complement curvature has either stable rank below three, or exact third-compound shared-coordinate collision `zeta_1>=1`. Use the exact hierarchy `1-zeta_1+zeta_2-zeta_3` to route large overlap-two/principal-third mass into the already-completed fixed-pair, principal, grouped-hub, projected-crossing, ridge, or square-bank receivers. Do not fall back to leverage surrogates, delete random curvature, or invert a vanishing local coefficient.

This is strictly narrower than r26's `chi_3>1/2` obstruction.

## 7. Verification status

The symbolic identities (2.4)-(2.10), the orthogonal formula (3.1), and the finite `8x8` example were checked with exact rational arithmetic. The exact enumeration gives (4.7)-(4.10), and the displayed decimal constants were separately evaluated. These checks are saved in `CHECKS.md` in this immutable run directory.

Independent end-to-end review of the new theorem is still pending. No full-solution status is claimed.
