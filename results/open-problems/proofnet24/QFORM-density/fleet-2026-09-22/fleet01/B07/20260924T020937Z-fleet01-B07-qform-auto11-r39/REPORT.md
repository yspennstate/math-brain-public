SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-24T02:09:37Z.
attacking: the low-pivot overlap-two operator-star survivor — use a fixed-pair Sylvester compound ladder to force either a principal-triple payment, anchored fourth-compound regeneration, or a diffuse rank-one Schur shadow, without reciprocating the tiny pair determinant.

# fleet01/B07 r39 — fixed-pair Sylvester compound ladder

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / GEOMETRY  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Status: **NEW EXACT FIXED-PAIR COMPOUND IDENTITY / LOW-PIVOT H2 STAR REDUCED TO PRINCIPAL-TRIPLE OR E4 OR DIFFUSE RANK-ONE SCHUR SHADOW / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.

All coordinates below are ORIGINAL physical coordinates. No random variable is rotated. No moment, bounded-support, connected-support, Gaussian, log-concavity, iid, diagonal-basis, or post-rotation independence assumption is added. No small nonzero quadratic direction is deleted.

## 1. Incoming unpaid state

The predecessor is fleet01/B07 r38,

`yspennstate/math-open-problems@a6688b11032f2e29ad10a8ab2c8356811bae926e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/20260924T011014Z-fleet01-B07-qform-auto11-r38/REPORT.md`.

Its theorem `QFORM-C3-OVERLAP-OPERATOR-STAR-FUNNEL-v1` decomposes the third compound by physical row/column overlap. The only unpaid overlap-two state is an actual physical pair

`H={i,j}`

for which the zero-diagonal bordered-minor star `S_H` satisfies

`||S_H||_op >= 1/12`,                                             (1.1)

while

`m_H := max(|A_ii|,|A_jj|,|A_ij|) < 1/64`.                       (1.2)

The complete incident overlap-two squared-minor packet therefore has mass at least `1/144`. The previous fixed-pair receiver already pays the complementary branch `m_H>=1/64`.

The designated partner fleet02/B07 was refreshed at

`yspennstate/math-open-problems@ec29bb4321feffe020e5cb0185d148f2f6de847e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260924T013622Z-fleet02-B07-qform-auto11/REPORT.md`.

Its theorem `QFORM-E2-BOUNDED-SUPPORT-BALANCE-v1` says for every real matrix `K` of rank `r>=2`,

`E2(K) <= (r-1) s2(K)^2 ||K||_F^2`.                              (1.3)

The partner also gives a target-valid unbalanced rank-two stress, so no step below infers a balanced carrier merely from aggregate `E2`.

## 2. Exact fixed-pair bordered-minor matrix

Fix an ordering of the two coordinates in `H` and write

`B=A[H,H]`, `delta=det B`, `O=[n]\H`.

For `r,c in O`, define the ORIENTED bordered-minor matrix

`D_H(r,c) = det A[(H,r),(H,c)]`,                                  (2.1)

where the rows are ordered with `H` first and then `r`, and the columns with `H` first and then `c`. If the usual increasing-order physical minors are used instead, there is a diagonal sign matrix `J` such that

`D_H^(physical) = J D_H J`.                                       (2.2)

Hence operator norms, Frobenius norms, singular values, ranks, diagonal entries in absolute value, and every squared compound mass are unchanged. I work with (2.1).

Writing the full matrix over `H union O` as

`A = [[B,U],[U^T,M]]`,                                            (2.3)

the one-border determinant formula is the exact inverse-free identity

`boxed:
D_H = delta M - U^T adj(B) U.
`                                                                    (2.4)

When `delta!=0`, this is equivalently

`D_H = delta S_H^Schur`,
`S_H^Schur = M-U^T B^(-1)U`.                                     (2.5)

The matrix `D_H` is symmetric.

## 3. Main algebraic theorem — Sylvester compound ladder

### Theorem 3.1 — `QFORM-FIXEDPAIR-SYLVESTER-COMPOUND-LADDER-v1`

For every integer `k>=1` and every `R,C subset O` with `|R|=|C|=k`, one has the polynomial identity

`boxed:
det D_H[R,C]
 = delta^(k-1) det A[(H,R),(H,C)].
}`                                                                    (3.1)

Here all determinants use the same appended orientation convention. With canonical increasing-order physical minors, the two sides differ only by the corresponding harmless row/column sign factors.

#### Proof

First suppose `delta!=0`. By (2.5),

`det D_H[R,C] = delta^k det S_H^Schur[R,C]`.                       (3.2)

The block determinant formula on the physical rows `H union R` and columns `H union C` gives

`det A[(H,R),(H,C)] = delta det S_H^Schur[R,C]`.                  (3.3)

Combining (3.2)-(3.3) yields (3.1) for every matrix with `delta!=0`. Both sides of (3.1) are polynomials in the entries of `A`, and the set `delta!=0` is dense. Hence (3.1) holds identically, including `delta=0`. QED.

### Consequence 3.2 — exact singular-pair collapse

Take `k=2`. If `delta=0`, then **every** `2x2` minor of `D_H` is zero. Therefore

`boxed: rank D_H <= 1.`                                           (3.4)

This is exact; no approximation or reciprocal pivot is involved. In particular an exactly singular physical pair cannot support a genuinely rank-two bordered third-minor shadow.

### Consequence 3.3 — anchored fourth-compound energy

Define the complete anchored physical fourth-minor currency

`Phi_H = sum_{|R|=|C|=2} det A[(H,R),(H,C)]^2`.                   (3.5)

By (3.1) and Cauchy--Binet for the second compound,

`boxed:
E2(D_H):=e2(D_HD_H^T)=delta^2 Phi_H.
}`                                                                    (3.6)

Thus the next compound order is not guessed or selected: it is exactly the `E2` energy of the full bordered-minor matrix.

## 4. Apply the ladder to the r38 low-pivot overlap-two star

The star matrix in r38 is the off-diagonal part of the physical-sign version of `D_H`. Therefore (1.1) says

`||Off(D_H)||_op >= 1/12`.                                       (4.1)

From (1.2), writing `B=[[a,b],[b,c]]`,

`|delta|=|ac-b^2| < 2/64^2 = 1/2048`.                            (4.2)

Set

`d0=1/96`, `epsilon=1/8`.                                        (4.3)

There are now three exhaustive branches.

### Branch A — one principal bordered determinant is macroscopic

If some `r in O` satisfies

`|D_H(r,r)| = |det A[H union {r},H union {r}]| >= 1/96`,          (4.4)

then r35 `QFORM-PHYSICAL3-DETERMINANT-ONLY-v1` applies directly with `d=1/96` and gives the full ambient form an essentially bounded density with

`boxed:
||p_Q||_infinity <= 128 sqrt(2) 96^(1/3)
                 < 828.862.
}`                                                                    (4.5)

Continuity is not claimed from that receiver.

### Branch B/C setup — all principal bordered determinants are small

Assume instead

`max_r |D_H(r,r)| < 1/96`.                                       (4.6)

Since `||diag D_H||_op<1/96`, (4.1) and the triangle inequality imply

`boxed:
L:=||D_H||_op >= 1/12-1/96 = 7/96.
}`                                                                    (4.7)

Let

`rho_1 := dist_F(D_H, rank<=1)`.                                 (4.8)

Because `D_H` is symmetric, if its singular values are `s1=L>=s2>=...`, then

`rho_1^2=sum_{j>=2}s_j^2`                                        (4.9)

and

`E2(D_H)=sum_{i<j}s_i^2s_j^2 >= L^2 rho_1^2`.                    (4.10)

### Branch B — transverse bordered-minor energy regenerates a huge anchored E4 packet

If

`rho_1 >= L/8`,                                                  (4.11)

then by (4.10), (4.7), (4.2), and (3.6),

`E2(D_H) >= L^4/64`,                                             (4.12)

and therefore

`Phi_H = E2(D_H)/delta^2
       > (1/64)(7/96)^4 (2048)^2
       = 2401/1296
       = 1.852623456790... .`                                    (4.13)

The case `delta=0` cannot occur in Branch B because (3.4) gives `rho_1=0`. Hence (4.13) is valid without division by zero.

This is a dimension-free aggregate-before-inversion conclusion: the tiny physical pair determinant is not inverted in a density estimate; instead failure of rank-one alignment forces more than `1.85` units of squared **anchored fourth-compound** mass.

### Branch C — a diffuse rank-one bordered-minor / Schur shadow

If

`rho_1 < L/8`,                                                   (4.14)

let `lambda v v^T` be a best symmetric rank-one approximation, with `||v||_2=1` and `|lambda|=L`, and put

`D_H=lambda v v^T+E`, `||E||_F<L/8`.                             (4.15)

For every physical residual coordinate `r`, (4.6) and (4.15) give

`L v_r^2 <= |D_H(r,r)|+|E_rr|
          < 1/96 + L/8`.                                         (4.16)

Using `L>=7/96`,

`boxed:
max_r v_r^2 < 1/7+1/8 = 15/56 < 0.268.
}`                                                                    (4.17)

Thus the rank-one shadow is quantitatively **diffuse in the original residual coordinates**. When `delta=0`, (3.4) makes the rank-one statement exact; then `E=0` and (4.16) sharpens to `max_r v_r^2<1/7`.

When `delta!=0`, (2.5) says the true physical Schur complement is simply `D_H/delta`, so (4.14)-(4.17) are equivalently a relative rank-one Schur-complement tube with the same diffuse leading direction. No random-variable rotation is made by this deterministic coefficient statement.

### Theorem 4.1 — `QFORM-LOWPIVOT-H2-SYLVESTER-RANK1-OR-E4-v1`

Every r38 unpaid overlap-two operator-star state (`m_H<1/64`, `||S_H||_op>=1/12`) obeys at least one of:

1. **principal-triple payment:** an actual physical principal `3x3` determinant has modulus at least `1/96`, hence (4.5);
2. **anchored E4 regeneration:** `Phi_H>2401/1296`;
3. **diffuse rank-one Schur shadow:** `dist_F(D_H,rank<=1)<||D_H||_op/8`, `||D_H||_op>=7/96`, and the leading physical residual direction has leverage `<15/56`; if `det B=0`, `rank D_H<=1` exactly and the leverage improves to `<1/7`.

This closes the structural ambiguity of the low-pivot `h=2` star: it is not an unstructured collection of many small minors.

## 5. Equation-level application of the designated fleet02/B07 theorem

On Branch B, (4.12) gives the explicit second-compound lower bound

`boxed:
E2(D_H) >= (1/64)(7/96)^4
         = 2401/5435817984.
}`                                                                    (5.1)

Let `r_D=rank D_H>=2`. Apply the designated partner inequality (1.3) to the **actual bordered-minor matrix `D_H`**. It yields

`(r_D-1) s2(D_H)^2 ||D_H||_F^2 >= 2401/5435817984`,              (5.2)

or equivalently

`boxed:
s2(D_H)||D_H||_F
 >= 49/[73728 sqrt(r_D-1)].
}`                                                                    (5.3)

This is a literal new inequality, not a citation-only use of the partner result. In particular, if a Branch-B bordered-minor packet has bounded rank `r_D<=R` and normalized Frobenius spread `||D_H||_F<=M L`, then

`s2(D_H) >= L/[8 M sqrt(R-1)]`.                                  (5.4)

The partner's own unbalanced-rank-two stress shows why a bound of this kind needs an effective-rank/spread gate; I do not silently drop it.

If instead an actual `p x q` physical subblock `K` of `D_H` carries `E2(K)>=eta E2(D_H)` and has `|K_ab|<=M0`, then the partner's bounded-support corollary gives the further concrete estimate

`s2(K) >= 49 sqrt(eta) /
          [73728 M0 sqrt((rank K-1)pq)].`                          (5.5)

Thus a bounded-support portion of the regenerated E4 currency necessarily contains a quantitative second spectral direction before any individual minor is selected.

## 6. Checks

Two finite regressions were run only as algebraic checks, not as proof evidence:

- 300 random symmetric matrices of sizes `5,6,7`: the `k=2` Sylvester identity (3.1) was checked over all residual row/column pairs; maximum absolute floating discrepancy was `5.69e-14`.
- 300 random constructions with exactly singular rank-one `2x2` pair blocks and arbitrary stars/leaf curvature: the second singular value of `D_H` was at most `4.18e-15`, consistent with the exact rank-one collapse (3.4).

The proof above is exact and does not rely on these regressions.

## 7. Remaining implication

The first B07 debt is now

`QFORM-DIFFUSE-RANKONE-SCHUR-OR-ANCHORED-E4-RECEIVER-v1`.

Two genuinely different mechanisms remain:

- spend the constant anchored fourth-compound currency `Phi_H>2401/1296` without selecting a reciprocal tiny pair; or
- use the original-coordinate diffuseness `max v_r^2<15/56` of the rank-one Schur/bordered-minor shadow together with the retained two-coordinate physical pair and arbitrary outside curvature.

The newest fleet03/B09 rank-one-pair Schur-E2 receiver was checked before publication. It is compatible with part of the exact-singular-pair geometry but assumes a rank-one pair-to-leaf star and a quantified leaf-curvature defect; those hypotheses are not automatic from Theorem 4.1, so it is not silently invoked here.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**.
