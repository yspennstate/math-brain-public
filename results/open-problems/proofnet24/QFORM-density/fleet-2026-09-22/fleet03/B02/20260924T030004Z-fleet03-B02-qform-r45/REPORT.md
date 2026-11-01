SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-24T03:00:04Z.
attacking: the balanced near-rank-two FULL physical cut left by r44/r11; physicalize same-side transverse curvature into a genuine E3 cut or overlap-one third-compound mass, and otherwise force the final matrix into the completed diffuse spectral-window receiver or a literal physical hub.

# fleet03/B02 r45 — mixed 2+1 volume physicalization on the propagated full cut

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **NEW SUPPORTING STRUCTURAL/FOURIER COMPILER; FULL QFORM OPEN; TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moment, compact/connected support, iid, diagonal-basis independence, post-rotation independence, conditional projection-density cap, or deletion of a small quadratic random term is used. Rotations below are coefficient algebra only.


## 1. Source-pinned inputs actually used

### 1.1 Immediate full-cut predecessor

The fresh complementary B02 predecessor is fleet02/B02 r11:

`yspennstate/math-open-problems@b34c3df7995a27f90540057d7dc1fcc33d6e7e39`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/fleet02-B02-20260924T023712Z-r11/REPORT.md`.

On the live ultra-near-rank-two packet, its full-cut propagation theorem gives a literal full physical cut

`N=A[L,R]`, `L disjoint R`, `L union R=[n]`,

whose squared singular values `x1>=x2>=...` obey

`x1*x2 > kappa := 247/576`,                                      (1.1)

`tau^2 := sum_(j>=3) xj < 18/1011712`.                            (1.2)

If its preceding physical-E3 exit fires then the full law is already paid; the present run attacks the survivor (1.1)-(1.2). The same source records the marginal-free physical-E3 Fourier receiver

`E3(B)>0 => ||p_Q||inf <= C3 E3(B)^(-1/6)`,

`integral_R |phi_Q(t)|dt <= 2*pi*C3 E3(B)^(-1/6)`,                (1.3)

with `C3=10.345083232147514...` and a continuous `C0` density.

### 1.2 Spectral-window receiver

The completed final-matrix spectral-window theorem is

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

If the spectral projection

`P_H=1_{|A|>=1/64}`

satisfies `max_i (P_H)_ii<=1/32`, then the exact full ambient law has a continuous `C0` density and

`||p_Q||inf <= 288*sqrt(3e)/13 =63.2640518778... <64`.             (1.4)

The theorem retains every smaller spectral direction, however numerous, signed, dense, or nonzero.

### 1.3 Designated partner fleet04/B02

The completed partner theorem used at an actual new inequality in Section 6 is

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.

On its exact overlap, a nonsingular physical principal triple `H0` with a zero diagonal entry gives

`L2 := integral_R |phi_Q(t)|^2 dt
 <= 6*pi*2^(2/3)*|det H0|^(-1/3)`.                                (1.5)

No partner claim outside that scope is used.

## 2. Main deterministic theorem — `QFORM-MIXED-2PLUS1-PHYSICALIZATION-v1`

Let `L,R` be a literal partition of the ORIGINAL coordinates and write

`N=A[L,R]`, `D=A[L,L]`.                                           (2.1)

Let `u1,u2` be the top two LEFT singular vectors of `N`, let

`P2=u1*u1^T+u2*u2^T`, `Q2=I-P2`,                                 (2.2)

and let `x1,x2` be the corresponding squared singular values.

For `t in L`, a physical row triple `I subset L`, `|I|=3`, and a physical right-column pair `J subset R`, `|J|=2`, define

`m(I,J,t)=det [ N[I,J] | D[I,t] ]`.                               (2.3)

Set

`T = sum_t sum_I sum_J m(I,J,t)^2`,                               (2.4)

and split it into

`T_off = sum_(t notin I) m(I,J,t)^2`,
`T_ov  = sum_(t in I)    m(I,J,t)^2`.                             (2.5)

Thus `T=T_off+T_ov`.

### Theorem 2.1 — aggregate lower bound

`boxed: T >= x1*x2 * ||Q2 D||_F^2.`                               (2.6)

#### Proof

Right-rotate only the coefficient columns of `N` by a singular-vector matrix. The sum over all two-column subsets `J` in (2.4) is invariant because the induced action on `Lambda^2` is orthogonal. Hence we may compute with columns `sqrt(x_j) u_j`.

Fix one column `d=D[:,t]`. Cauchy--Binet / Gram determinant gives, for every singular pair `p<q`,

`sum_(|I|=3) det[sqrt(x_p)u_p[I],sqrt(x_q)u_q[I],d[I]]^2
 = x_p*x_q * ||P_(span{u_p,u_q}^perp)d||_2^2`.                   (2.7)

All terms are nonnegative. Retaining only `(p,q)=(1,2)` and then summing over `t` gives exactly (2.6). QED.

### Theorem 2.2 — physicalization / overlap-one fork

At least one of the following holds:

`(A) there is an ORIGINAL-coordinate physical cut B=A[S,S^c] with`

`boxed: E3(B) >= T/32;`                                           (2.8)

or

`(B) the global overlap-one third-compound mass V1 obeys`

`boxed: V1 >= T/2.`                                               (2.9)

Here `V1` means the sum of squared `3x3` minors `det A[I,K]^2` with `|I|=|K|=3` and `|I cap K|=1`.

#### Proof

If `T_ov>=T/2`, then every term in `T_ov` is literally a third-compound minor with row triple `I` and column triple `J union {t}`. Because `J subset R`, `I subset L`, and `t in I`, the two triples intersect in exactly the one physical coordinate `t`. Thus these terms form a subfamily of `V1`, proving (2.9).

Assume instead `T_off>=T/2`. Independently color every coordinate of `L` into `S` with probability `1/2`; keep every coordinate of `R` outside `S`. For a fixed term with `t notin I`, the four physical coordinates in `I union {t}` are distinct, and the event

`I subset S`, `t notin S`                                         (2.10)

has probability `2^-4=1/16`. On that event, the exact determinant (2.3) is one of the literal `3x3` minors of the physical cross block `A[S,S^c]`, using row triple `I` and column triple `J union {t}`. Distinct `(I,J,t)` give distinct such minors. Therefore

`E_S E3(A[S,S^c]) >= T_off/16 >= T/32`.                           (2.11)

Some deterministic physical `S` realizes at least its expectation, proving (2.8). QED.

### Why this is correction-safe

The theorem aggregates before taking any reciprocal power. It does not select a uniformly good individual physical minor. The singular vectors occur only inside the coefficient identity (2.6); no rotated random variables are introduced. The final smoothing object in (2.8) is a literal ORIGINAL-coordinate physical cut. No small coefficient is deleted from the random quadratic form.

## 3. Near-rank-two full cuts: either mixed volume is physicalized or the FINAL matrix is near rank four

Now also write

`C=A[R,R]`                                                        (3.1)

and let `V2` be the top-two RIGHT singular space of `N`, with projection `R2`. Define the two transverse same-side energies

`delta_L^2=||(I-P2)D||_F^2`,
`delta_R^2=||(I-R2)C||_F^2`,                                      (3.2)

and the cross tail

`tau^2=sum_(j>=3)xj`.                                              (3.3)

Let `N2=P2 N R2` be the top-two singular truncation and define

`A0 = [[P2 D P2, N2], [N2^T, R2 C R2]]`.                          (3.4)

Then `rank(A0)<=4`, since its range is contained in the four-dimensional coefficient space `range(P2) direct_sum range(R2)`.

### Lemma 3.1 — exact near-rank-four estimate

`boxed: ||A-A0||_F^2 <= 2(delta_L^2+delta_R^2+tau^2).`             (3.5)

#### Proof

With `Q=I-P2`, symmetry of `D` gives

`D-P2DP2 = QDP2 + P2DQ + QDQ`,

whose three displayed blocks are Frobenius-orthogonal except for the transpose pair. Thus

`||D-P2DP2||_F^2
 =2||QDP2||_F^2+||QDQ||_F^2
 <=2||QD||_F^2=2 delta_L^2`.                                      (3.6)

The same argument gives `||C-R2CR2||_F^2<=2delta_R^2`. The two symmetric off-diagonal copies of `N-N2` contribute `2tau^2`. Add the three block contributions. QED.

Consequently

`s5(A) <= ||A-A0||op <= sqrt(2(delta_L^2+delta_R^2+tau^2)).`       (3.7)

This is coefficient/spectral information only. It is NOT used to delete `A-A0` from the random phase.

## 4. Concrete application to the fresh r11 propagated full cut

Use (1.1)-(1.2) and put

`d0^2=2^-15`.                                                      (4.1)

### 4.1 One same-side transverse energy is large

If either `delta_L^2>=d0^2` or `delta_R^2>=d0^2`, apply Theorem 2.2 to `N,D` or to the transposed cut `N^T,C`. Equation (2.6) and (1.1) give

`T > kappa*2^-15`.                                                 (4.2)

Therefore either there is a literal physical cross cut `B` with

`boxed:
 E3(B) > Z0 := kappa*2^-20
 =247/603979776
 =4.08954090542e-7,
}`                                                                  (4.3)

or

`boxed:
 V1 > V10 := kappa*2^-16
 =247/37748736
 =6.54326544868e-6.
}`                                                                  (4.4)

The first alternative is immediately paid by (1.3):

`boxed: ||p_Q||inf <120.075636215,`                                (4.5)

`boxed: integral_R |phi_Q(t)|dt <754.457473215.`                   (4.6)

Hence this branch has a continuous `C0` density.

The second alternative is a fixed absolute overlap-one third-compound packet. It can be fed directly into the existing r39/r43 grouped overlap-one compilers. In particular, on their grouped-two-star subbranch the r43 theorem at `theta=1/4` gives either one of its four explicit low-rank collars or

`||p_Q||inf <=50.8250418688 V1^(-1/6)
             <371.631046692`,                                      (4.7)

with genuine Fourier `L1` and a continuous `C0` density. I do NOT claim that every `V1` packet automatically lands in that grouped-two-star subbranch; the alternate grouped-pivot branch remains part of the shared proof architecture.

### 4.2 Both same-side transverse energies are small

Assume instead

`delta_L^2<2^-15`, `delta_R^2<2^-15`.                              (4.8)

Then (1.2) and (3.5) give the exact rational bound

`||A-A0||_F^2
 < 2(2*2^-15 + 18/1011712)
 =319/2023424
 =0.000157653561488...`                                           (4.9)

and therefore

`boxed: s5(A)<0.012556016944<1/64.`                               (4.10)

Thus the FINAL spectral window

`P_H=1_{|A|>=1/64}`                                               (4.11)

has rank at most four. There are now two exhaustive subcases.

If

`max_i (P_H)_ii<=1/32`,                                           (4.12)

the completed full-matrix spectral-window theorem (1.4) applies to `A` itself and gives

`boxed: ||p_Q||inf<64`                                             (4.13)

with genuine Fourier `L1` and a continuous `C0` density.

If (4.12) fails, choose a physical coordinate `i` with `(P_H)_ii>1/32`. The elementary final-matrix square-energy inequality gives

`||A e_i||_2^2=(A^2)_ii
 >=(1/64)^2 (P_H)_ii
 >1/131072.`                                                       (4.14)

Since

`||Ae_i||_2^2=A_ii^2+||A[i,i^c]||_2^2`,                           (4.15)

one literal physical certificate must hold:

`boxed: |A_ii|>1/512  OR  ||A[i,i^c]||_2>1/512.`                  (4.16)

So the low-transverse-curvature endpoint is not an unspecified aligned rank-two core: it is either already paid by the final spectral-window Fourier theorem or it contains a fixed-scale ORIGINAL-coordinate hub. Because `rank(P_H)<=4`, the total high-window leverage budget is at most four as well.

## 5. Exhaustive live packet after r44 + r11 + the present compiler

Starting from the actual ultra-near-rank-two packet inherited by r11, all already-paid E3 exits included, one reaches only the following new exhaustive list:

1. **physical E3 Fourier exit:** some literal cut has `E3>Z0` and (4.5)-(4.6) hold;
2. **fixed overlap-one packet:** `V1>V10`, to be routed through the existing grouped-pivot / grouped-two-star compilers;
3. **diffuse final spectral window:** the complete final matrix is paid by (4.13), with continuity;
4. **physical hub:** `|A_ii|>1/512` or `||A[i,i^c]||_2>1/512` for an actual source coordinate.

This replaces the previous vague endpoint “balanced near-rank-two full cut plus internal curvature” by literal source-coordinate currencies or a completed Fourier theorem. No coefficient-size perturbation of the random output is used.

## 6. New equation-level use of designated fleet04/B02

On the physical-E3 branch (4.3), use the completed uniform physical-E3 tail

`|phi_Q(t)| <= min{1,
 4*sqrt(e)*pi^(3/2)*E3(B)^(-1/4)|t|^(-3/2)}`.                     (6.1)

On the exact overlap where the designated partner's zero-diagonal triple `H0` exists, (1.5) gives

`L2=integral |phi_Q|^2
 <=6*pi*2^(2/3)|det H0|^(-1/3)`.                                 (6.2)

For any `T>0`, Cauchy--Schwarz on `|t|<=T` and (6.1) on the tail give

`integral |phi_Q|
 <=sqrt(2 L2 T)+4K T^(-1/2),`                                    (6.3)

where

`K=4*sqrt(e)*pi^(3/2)*E3(B)^(-1/4)`.                             (6.4)

The exact optimizer is `T=4K/sqrt(2L2)`, yielding

`||p_Q||inf
 <=2^(8/3)*3^(1/4)*e^(1/4)
   |det H0|^(-1/12) E3(B)^(-1/8)`.                               (6.5)

Using the NEW physicalized threshold (4.3),

`boxed:
 ||p_Q||inf
 <67.474747757 |det H0|^(-1/12).
}`                                                                  (6.6)

This is an actual new inequality using fleet04/B02, not a citation-only dependency. Continuity on this overlap comes from the physical-E3 `L1` theorem, not from the partner `L2` estimate alone.

## 7. Deterministic computation / regression

A seeded checker (adjacent `CHECKS.py`) generated 120 dense symmetric block matrices with left-bank dimensions 4--6 and right-bank dimensions 2--4. It exhaustively enumerated the mixed minors and every left-bank physical split. Results:

- aggregate inequality (2.6): `0` violations;
- physicalization expectation consequence (2.8): `0` violations;
- near-rank-four Frobenius estimate (3.5): `0` violations;
- maximum numerical negative discrepancy in (2.6), relative to its lower bound: `1.17e-15`;
- minimum observed ratio `max_S E3(A[S,S^c])/(T_off/16)`: `5.2745088877`;
- maximum observed ratio `||A-A0||_F^2/[2(delta_L^2+delta_R^2+tau^2)]`: `0.9110494275`.

The finite computation is corroborative only. The proof is the exterior/Cauchy--Binet identity, the exact Bernoulli physicalization expectation, and the block Frobenius calculation above.

## 8. What is and is not closed

`QFORM-MIXED-2PLUS1-PHYSICALIZATION-v1`: **PROVED supporting deterministic theorem**.

`QFORM-BALANCED-FULLCUT-R2-TO-E3-OR-V1-OR-RIDGE-OR-HUB-v1`: **PROVED on the live r11 propagated full-cut packet**.

The full unrestricted QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. A target-wide universal bound on unweighted `integral |phi_Q|` remains **OPEN / not refuted**.

The next B02 edge is now `QFORM-FIXEDSCALE-V1-PIVOT-OR-HUB-L1-v1`: pay the fixed overlap-one packet (4.4) on its grouped-pivot branch and splice the fixed physical-hub branch (4.16) into the two remaining large spectral credits, without using the refuted one-heavy-row absorption shortcut. The grouped-two-star generic subbranch and the diffuse final spectral window are already paid.

MODEL: GPT-5.6 Sol. THINKING LEVEL: `UNKNOWN_NOT_EXPOSED`; maximum supported reasoning requested. Reasoning-token and provider thinking-time telemetry were unavailable/null.
