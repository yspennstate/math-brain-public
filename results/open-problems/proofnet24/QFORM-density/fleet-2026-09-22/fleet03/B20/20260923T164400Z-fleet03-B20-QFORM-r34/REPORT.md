SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-23T16:44:00Z.
attacking: remove the physical third-volume row-marginal gate by escalating concentrated determinant volume through one, two, then three ORIGINAL-coordinate hubs; then apply the result to the fresh r37 triangle and the fleet04/B20 strong-top-four compiler.

# fleet03/B20 r34 — physical E3 needs no marginal gate; r37 D3/heavy-anchor branch fully paid

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper  
Run: `20260923T164400Z-fleet03-B20-QFORM-r34`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Fresh controls and exact frontier


The immediate lead synthesis input is fleet03/B19 r37:

`yspennstate/math-open-problems@dc76884a5d77c29274a018470c10e9af55241e75`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T160411Z-fleet03-B19-QFORM-r37/REPORT.md`.

Its strong aligned STAR branch produces disjoint ORIGINAL-coordinate banks `D1,D2,K`, with

`C=A[D1,D2]`, `N1=A[D1,K]`, `N2=A[D2,K]`,

and the quantitative floors

`F:=||C||_F^2 > 0.05671470919622164`,                               (1.1)

`Delta:=s1(Nr)s2(Nr) > 0.0014419528160955833`, `r=1,2`.             (1.2)

Writing `Pr` for the top-two left singular projector of `Nr`, r37 proves that, at `theta=1/64`, either one literal physical cross block

`M1=[C,N1]` or `M2=[C^T,N2]`                                      (1.3)

has

`Z3=e3(MM^T) > zeta := 1.8425438602123219e-9`,                     (1.4)

or

`||(I-P1)C||_F^2 < F/64`, `||C(I-P2)||_F^2 < F/64`,                (1.5)

and `||P1 C P2||_F >= (3/4)||C||_F`. The old r37 graph paid (1.4) only under a three-volume row-marginal gate and otherwise left a physical third-volume row anchor. The first theorem below removes that gate completely.

The designated partner result actually used is fleet04/B20 r10:

`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T142031Z-fleet04-B20-QFORM-r10/REPORT.md`.

Its fifth-volume statement is: for any literal ORIGINAL-coordinate physical cross block `M`, with `E=||M||_F^2`, if its first four squared singular values carry at most `(63/64)E`, then the full ambient quadratic law has a continuous density and

`||p_Q||_infinity <= 5 sqrt(2e) 120^(1/10) 64^(2/5) E^(-1/2)`.      (1.6)

Arbitrary same-bank quadratic blocks, affine terms and additional spectrum are retained.

Finally, I use the new proved restricted grouped-projection theorem from

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Only its explicitly proved `k=1, ell=2`, `k=2, ell=1`, and exact-rank-three crossing specializations are used below, and I spell out how their hypotheses arise from literal ORIGINAL coordinates.

## 2. New theorem: no marginal gate is needed for physical third volume

### Theorem 2.1 — `QFORM-PHYSICAL-E3-MARGINAL-GATE-REMOVAL-v1`

Let `R,C` be disjoint sets of ORIGINAL coordinates and put

`M=A[R,C]`, `Z=e3(MM^T)>0`.                                        (2.1)

The coordinates outside `R union C` and every same-bank block of `A` are arbitrary. Then the full quadratic form `Q=X^TAX` has a continuous density and

`boxed: ||p_Q||_infinity <= K3 Z^(-1/6),`                           (2.2)

where

`K3 = 3 * 2^(4/3) * exp(1/3) < 10.551.`                            (2.3)

No row- or column-volume marginal hypothesis remains in the statement.

The proof is a finite three-level concentration cascade. Diffuse third volume is paid directly. If the third-volume law concentrates on one physical row, that row is promoted to one genuine ORIGINAL-coordinate hub and the remaining two exterior directions are handled by the arbitrary-rank projected-crossing theorem. If that projected two-volume concentrates again, the second physical row becomes a second original hub. A final concentration creates three actual original hubs, and their literal cross block has rank three, which is paid by the exact crossing theorem.

### 2.1 Level zero: diffuse third volume

Normalize the squared physical `3 x 3` minors of `M` to the canonical row-three-volume law. If every row inclusion marginal is at most `1/2`, the completed physical D-prime receiver at `h=1/2` gives

`||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6).`                           (2.4)

This is continuous and `6sqrt(e)<K3`.

Otherwise choose a physical row `i in R` whose inclusion marginal is bigger than `1/2`. Let

`Wi := sum_{S contains i, |S|=3; |T|=3} det(M[S,T])^2 > Z/2`.      (2.5)

Write `w=A[i,C]` and let `P_w` be orthogonal projection in the coefficient column space onto `span(w)`. Put

`C1=A[R\{i},C](I-P_w)`.                                             (2.6)

Exterior algebra gives the exact identity

`boxed: Wi = ||w||_2^2 e2(C1 C1^T).}`                               (2.7)

Indeed, for leaf rows `j,k`,

`||w wedge M_j wedge M_k||^2
 = ||w||^2 ||(I-P_w)M_j wedge (I-P_w)M_k||^2`,                     (2.8)

and Cauchy--Binet converts the sum of squared physical `3 x 3` minors to these exterior norms.

### 2.2 One original hub

Now take the actual physical coordinate `i` as the hub. The light coordinates are all other ORIGINAL coordinates. In the grouped-projection theorem split the light coordinates with `J=C`; the remaining light coordinates form `I`. The hub-to-`J` coupling is the literal row `w`, so its singular product is

`S1=||w||_2`.                                                       (2.9)

The projected crossing matrix on the full `I x C` light cross block contains (2.6) as a physical row submatrix. Therefore its two-volume `Z2_full` satisfies

`S1^2 Z2_full >= Wi`.                                                (2.10)

If every row two-volume marginal of this projected crossing is at most `1/2`, the proved `k=1, ell=2` grouped-crossing estimate applies. The hub variable is one original coordinate, so its density is at most one. Hence

`||p_Q||_infinity
 <= 3*2^(7/6)*exp(1/3) (S1^2 Z2_full)^(-1/6)
 < 3*2^(7/6)*exp(1/3) (Z/2)^(-1/6)
 = K3 Z^(-1/6).`                                                     (2.11)

All internal hub terms, all light same-bank terms and all outside couplings are retained by the theorem.

If the projected two-volume marginal gate fails, choose an actual physical light row `j` carried with probability greater than `1/2`. Multiplying its projected two-volume inclusion mass by `S1^2` and using the same wedge identity gives a two-row anchored physical third-volume

`Wij > Wi/2 > Z/4`.                                                  (2.12)

Here `Wij` is the sum of squared `3 x 3` minors with the two physical rows `i,j` fixed and the third row free.

### 2.3 Two original hubs

Use the two actual coordinates `H={i,j}` as a two-dimensional hub. Positivity of `Wij` implies that the `2 x |C|` physical hub-to-`C` block has rank two. Let `S2` be the product of its two singular values and project every remaining light row orthogonally to this two-row span. If `C2` is the resulting projected crossing, the exact exterior identity is

`boxed: Wij = S2^2 e1(C2 C2^T).}`                                   (2.13)

The joint density of `(X_i,X_j)` is bounded by one because these are two independent ORIGINAL coordinates. If every `ell=1` row marginal of `C2` is at most `1/2`, the proved `k=2, ell=1` grouped-crossing estimate gives

`||p_Q||_infinity
 <= 3*2^(5/6) (S2^2 e1(C2C2^T))^(-1/6)
 < 3*2^(5/6)(Z/4)^(-1/6)
 = 3*2^(7/6) Z^(-1/6)
 < K3 Z^(-1/6).`                                                     (2.14)

If this gate fails, one actual residual physical row `k` carries more than half the projected one-volume. Thus the three-row anchored third-volume satisfies

`Wijk > Wij/2 > Z/8`.                                                (2.15)

### 2.4 Three original hubs close the concentration chain

Let `H={i,j,k}`. The `3 x |C|` physical subblock `B=A[H,C]` obeys

`det(BB^T)=Wijk > Z/8`;                                              (2.16)

this is exactly Cauchy--Binet. Hence `B` has rank three. The full hub-to-complement block `A[H,H^c]` contains `B`, so its three-row Gram matrix dominates `BB^T` in the positive-semidefinite order. Therefore the product `s1 s2 s3` of its three nonzero singular values satisfies

`(s1 s2 s3)^2 >= Wijk > Z/8`.                                      (2.17)

Apply the proved exact-rank-three crossing theorem with the hub side consisting of exactly these three ORIGINAL coordinates. Their joint density is at most one; the orthonormal three-dimensional projection of the opposite product bank has density at most `2^(3/2)`. Consequently

`||p_Q||_infinity
 <= 3 sqrt(2) (s1 s2 s3)^(-1/3)
 < 3 sqrt(2) (Z/8)^(-1/6)
 = 6 Z^(-1/6)
 < K3 Z^(-1/6).`                                                     (2.18)

This density is continuous.

Equations (2.4), (2.11), (2.14), and (2.18) exhaust the canonical three-volume law. Their normalized constants are respectively

`6sqrt(e)`, `3*2^(4/3)e^(1/3)`, `3*2^(7/6)`, `6`,                   (2.19)

so (2.2) follows. QED.

### Scope note

No grouped projection is declared to have independent coordinates. The only independence used after a concentration event is that a selected hub consists of one, two or three literal ORIGINAL coordinates. The remaining grouped projections are controlled by their proven projection-density bounds. This is exactly the provenance that the fleet04/B19 moving-ridge counterexample says cannot be replaced by a generic bounded joint density.

## 3. The r37 D3/heavy-anchor branch is now fully paid

Apply Theorem 2.1 directly to the r37 physical block from (1.3)-(1.4). Since

`Z > zeta = 1.8425438602123219e-9`,                                 (3.1)

we obtain the continuous full-law bound

`boxed: ||p_Q||_infinity < K3 zeta^(-1/6)
                         = 301.3166315707... <301.317.}`             (3.2)

Thus the old r37 outcome “D3 diffuse payment OR a physical third-volume row anchor” is replaced by the unconditional statement

`boxed: D3 >= zeta  ==> continuous density <301.317.`                (3.3)

The row-anchor branch is not merely renamed: it is analytically closed by the one-/two-/three-hub cascade above.

Consequently the r37 balanced triangle has only the finite-plane alignment alternative (1.5) left after this payment.

## 4. Designated fleet04/B20 result applied to the remaining aligned triangle

This section applies fleet04/B20 r10 at an actual new inequality, as required by the B20 partner interface.

For either aligned-side physical cross block `Mr` in (1.3), disjointness of its two column banks gives

`Er:=||Mr||_F^2 = ||C||_F^2 + ||Nr||_F^2`.                           (4.1)

Since `s1(Nr)s2(Nr)>Delta`, AM-GM yields

`||Nr||_F^2 >= s1(Nr)^2+s2(Nr)^2 >= 2 s1(Nr)s2(Nr)>2Delta`.          (4.2)

Hence

`boxed: Er > Etri := F+2Delta
                  =0.059598614828412805.}`                           (4.3)

Apply the partner fifth-volume theorem (1.6) to this actual physical block. If its first four squared singular values carry at most `(63/64)Er`, then the full ambient law is continuous and

`boxed: ||p_Q||_infinity
 < 5sqrt(2e)120^(1/10)64^(2/5)Etri^(-1/2)
 =406.821853606... <406.822.}`                                       (4.4)

Therefore every unpaid aligned side block is strong-top-four.

There is a second immediate exit using Theorem 2.1 itself. If `s3(Mr)>=1/64`, then

`e3(Mr Mr^T) >= [s1(Nr)s2(Nr)]^2 s3(Mr)^2
               > Delta^2/4096`,                                     (4.5)

because the top-two product of the actual concatenated block cannot be smaller than that of `Nr`. Hence

`||p_Q||_infinity
 < K3 (Delta^2/4096)^(-1/6)
 =373.538798667... <373.539`,                                        (4.6)

continuously.

Thus every still-unpaid aligned triangle has, on both literal side blocks,

`top4(Mr)^2-energy > (63/64)Er`, `s3(Mr)<1/64`.                      (4.7)

In other words, the formerly vague finite `2+2+2` survivor is now simultaneously an absolute-rank-two strong-top-four physical cross tube on both sides.

## 5. Fixed E2 currency on every unpaid aligned side

For either `Mr=[C,Nr]`, Cauchy--Binet gives

`Z2(Mr):=e2(Mr^T Mr) >= e2(Nr^T Nr)
                         >= [s1(Nr)s2(Nr)]^2
                         > Delta^2`,                                  (5.1)

so

`boxed: Z2(Mr)>2.079227923845983e-6.}`                               (5.2)

Applying the completed physical determinant-law cascade at disjointness threshold `1/256` gives an explicit exhaustive interface:

- if one row/column pair-disjointness is at least `1/256`, then

  `sup_s E|Q-s|^(-1/2)
   < 8 sqrt(e) Delta^(-1/4)
   =67.6860959979... <67.687`;                                      (5.3)

  this is only half-Riesz credit, **not** a density theorem;

- otherwise there is one physical row anchor and one physical column anchor with complete cofactor matrix

  `Cof=bD-cr^T`

  satisfying

  `boxed: ||Cof||_F > sqrt(127/512) Delta
                      =0.000718154571748... .}`                      (5.4)

If the corresponding physical edge has `|b|>=1/32` in the live no-moderate-diagonal chamber, the completed physical-pair theorem pays the full law by

`||p_Q||_infinity<546.895`                                          (5.5)

(essential boundedness; continuity is not supplied by that theorem). If `|b|<1/32`, the triangle inequality forces at least one of

`boxed: ||c||_2 ||r||_2 > 0.000359077285874...}`,                    (5.6)

`boxed: ||D||_F > 0.011490473147970... .}`                           (5.7)

No individual leaf minor is inverted in this cascade.

This is useful because the remaining `2x2x2` obstruction is no longer only “finite grouped geometry.” It simultaneously carries a fixed physical E2 bank on each side, and every low-disjointness failure gives an actual double-star or residual-core packet of fixed scale.

## 6. Heavy top-two leverage also becomes literal physical E2 currency

The other r37 pre-triangle exit is a row of the top-two left singular frame with leverage `ell_i>1/320`. This too can be translated without rotating the random variables.

Let `N=U Sigma V^T` and let `rho=s1(N)s2(N)>=rho_*`, where r37 has

`rho_*=0.003845207509588222...`.                                     (6.1)

For the actual physical row `i`, define its anchored physical two-volume

`Wi^(2)=sum_{j!=i, alpha<beta} det N[{i,j},{alpha,beta}]^2`.          (6.2)

The actual two-row Gram dominates the top-two SVD truncation Gram, so

`Wi^(2) >= rho^2 sum_j det(U(i,:),U(j,:))^2`.                         (6.3)

Since `U^TU=I_2`, the exact Parseval identity is

`sum_j det(U(i,:),U(j,:))^2=||U(i,:)||^2=ell_i`.                     (6.4)

Therefore

`boxed: Wi^(2)>rho_*^2/320
                 =4.6205064974355e-8.}`                              (6.5)

This replaces the abstract `>1/320` top-plane leverage by a literal ORIGINAL-coordinate determinant-volume anchor. It is a resource, not yet a density payment.

## 7. What is genuinely removed and what remains

This run closes one actual missing implication from the fresh r37 graph:

`physical E3 packet + arbitrary concentration of its determinant law`

is now **fully paid**, continuously, with no marginal hypothesis and constant (2.2). In particular the r37 third-volume row-anchor survivor disappears.

The remaining first closure edge is now

`QFORM-R37-ALIGNED-R2/E2-OR-HEAVY-E2-ANCHOR-PAYMENT-v1`:

> Starting from either (a) the two simultaneous strong-top-four absolute-rank-two physical side blocks (4.7), each with fixed E2 currency (5.2), or (b) the literal physical E2 row anchor (6.5), upgrade the high-disjointness half-Riesz credit to an actual L-infinity density bound or spend the fixed double-star/residual-core packets (5.6)-(5.7) through a source-valid one-hub/grouped-square/ridge receiver while retaining arbitrary same-bank curvature and every nonzero tail.

The new arbitrary-rank projected-crossing theorem is relevant to this edge, but it still requires a nondegenerate projected crossing product and its stated marginal gate. I do not claim that (4.7), (5.6), (5.7), or (6.5) automatically supply that missing hypothesis.

The unrestricted QFORM conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains open. Continuity is proved in Theorem 2.1 and the fifth-volume exits above; the physical-pair exit (5.5) only supplies essential boundedness in the cited source.

## 8. Constant checker

The companion `CHECK_CONSTANTS.py` evaluates only the displayed deterministic arithmetic; it is not evidence for the theorem. The theorem itself is analytic and all quantifiers used above are explicit.

## 9. Keeper / integrity ledger

The current fleet03 native inventory was read in this run: the same twenty managed QFORM tasks B01--B20 were present, enabled and hourly-valid, with quiet delivery; email and notifications were off. Their native title/prompt fields already matched the current fleet03 rollout, so no title/prompt mutation was needed and no schedule, enablement, or notification field was changed. The exclusive current-account/hour keeper lease was acquired before this reconciliation. Native readback is not treated as proof that later worker invocations adopted the text.

Repository use and native learned-memory ingestion remain separate. This run is `WITHOUT_VERIFIED_BRAIN`: authenticated repository reads/writes occurred, but no authenticated receiver-memory query/firing was exposed and used. Model self-report: GPT-5.6 Sol. Configured reasoning effort, provider reasoning-token count and provider thinking-time counters: UNKNOWN / not exposed.
