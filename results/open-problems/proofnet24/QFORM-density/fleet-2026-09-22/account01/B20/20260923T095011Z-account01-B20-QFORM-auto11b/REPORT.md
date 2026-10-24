SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T09:50:11Z.
attacking: the newest completed account02/B20 exact-rank-three survivor; first pay a large physical hub scalar, then compile every remaining heavy physical row into either a robust original-bank transverse plane or an exact near-hyperbolic two-bank split.

# account01/B20 auto11b — heavy-row scalar/star payment and transverse hyperbolic compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Owner control:** revision `2026-09-22.15`; QFORM sole target on the fresh protected-brain refresh; no later B20 stop observed before this mathematics was written.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `ESSENTIAL_STEP_APPLIED / LARGE-HUB-SCALAR SUBBRANCH PAID / HEAVY-ROW RESIDUAL COMPILED / FULL QFORM OPEN`.

The unrestricted owner target remains OPEN. Global continuity remains OPEN. No Gaussian, iid, moment, support, log-concavity, or post-rotation-independence assumption is used.

## 1. Completed partner actually consumed

The completed account02/B20 result used here is

`yspennstate/math-open-problems@6a4e9c575bcea2bbc12efd5a439bfb94f290d399`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T090422Z-account02-B20-QFORM-auto11/REPORT.md`.

Its exact-rank-three survivor has

`A = R M R^T`, `R^T R = I_3`, `M=M^T`, `s_min(M)>=1`,                 (1.1)

and, after all branches paid in that report, contains an ORIGINAL physical row `h` with leverage

`c := ||r_h||^2 > 1/2`.                                               (1.2)

The partner also supplies three disjoint original-coordinate packets with designated masses `>1953/16384`, one packet of size at most 18. Those packet currencies remain available, but the first router below needs only the partner's stronger fact (1.2).

Two previously completed analytic inputs are used at their proved scope:

1. `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, canonical `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, gives for any physical coordinate `i` with `A_ii!=0`

`||p_Q||_infinity <= 128 [ c_i |A_ii| |det M| ]^(-1/4)`.             (1.3)

2. `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, gives an `R^2` orthogonal projection of an original-coordinate cap-one product vector joint density at most `e`. More generally, after an invertible deterministic `2 x 2` scaling with Gram `H`, the density cap is multiplied by `(det H)^(-1/2)`.

No statement below treats a rotated spectral coordinate as probabilistically independent.

## 2. First new theorem: a heavy spectral row gives a scalar-or-strong-star dichotomy

### Theorem 2.1 — `QFORM-HEAVYROW-SCALAR-STAR-DICHOTOMY-v1`

Under (1.1), fix a physical row `h` and put

`a=A_hh`, `b=A[h,h^c]`.                                              (2.1)

Then

`boxed: a^2 + ||b||_2^2 >= c.`                                      (2.2)

Consequently, on the actual partner survivor (1.2), either

`|a|>=1/4`,                                                          (2.3)

in which case the full density is already paid by

`boxed: ||p_Q||_infinity < 128*8^(1/4) < 215.270,`                  (2.4)

or else

`boxed: ||b||_2 > sqrt(7)/4 = 0.6614378... .}`                       (2.5)

#### Proof

Because `R^T R=I_3`,

`A^2 = R M^2 R^T`.                                                    (2.6)

Therefore the squared Euclidean norm of physical column `h` is

`a^2+||b||_2^2
 = e_h^T A^2 e_h
 = r_h^T M^2 r_h`.                                                    (2.7)

All eigenvalues of `M^2` are at least one, hence (2.2). If (2.3) holds, then `|det M|>=1`, `c>1/2`, and (1.3) gives

`||p_Q||_infinity
 <=128[c|a||det M|]^(-1/4)
 <128(1/8)^(-1/4)
 =128*8^(1/4)<215.270`.                                              (2.8)

If instead `|a|<1/4`, (2.2) and `c>1/2` give

`||b||_2^2 > 1/2-1/16=7/16`,                                       (2.9)

which is (2.5). QED.

This is a genuine partner-level payment: every account02/B20 auto11 survivor with a quarter-scale physical scalar at its forced high-leverage row is removed from the proof debt. The complementary state has a much stronger aggregate physical star than a one-entry selection would reveal.

## 3. Exact transverse Parseval geometry around the heavy row

Assume now the unpaid side `|a|<1/4`. Define

`u = r_h/sqrt(c)`, `P=I-u u^T`, `q_i=P r_i` for `i!=h`.              (3.1)

Identify the two-dimensional plane `u^perp` with `R^2`. Since the rows of `R` form a Parseval frame,

`sum_(i!=h) q_i q_i^T = I_2`.                                       (3.2)

Also

`det(r_h,r_i,r_j)^2 = c det(q_i,q_j)^2`.                            (3.3)

Cauchy--Binet applied to (3.2) gives

`sum_(i<j, i,j!=h) det(q_i,q_j)^2=1`.                               (3.4)

Fairly and independently colour each residual physical coordinate U or V. Every unordered pair is separated with probability `1/2`, so some deterministic ORIGINAL-coordinate partition

`[n]\{h}=U disjoint_union V`                                       (3.5)

satisfies

`boxed: W(U,V):=sum_(i in U,j in V) det(q_i,q_j)^2 >=1/2.`          (3.6)

Equivalently, using (3.3), this partition retains anchored principal-frame volume at least `c/2>1/4`.

## 4. Main new theorem: robust transverse bank or an exact near-hyperbolic split

Put

`H=sum_(i in U)q_i q_i^T`, `K=sum_(j in V)q_j q_j^T=I_2-H`.         (4.1)

Let `x>=y` be the eigenvalues of `H`. Then `0<=y<=x<=1` and

`W(U,V)=tr(H)tr(K)-tr(HK)
      =x(1-y)+y(1-x)
      =x+y-2xy`.                                                      (4.2)

The key exact factorisation is

`W(U,V)-1/2=(x-1/2)(1-2y)`.                                         (4.3)

Since `x>=y`, (3.6) and (4.3) force

`boxed: x>=1/2>=y.`                                                  (4.4)

### Theorem 4.1 — `QFORM-HEAVYROW-TRANSVERSE-CUT-COMPILER-v1`

For every `0<delta<1/4`, the partition (3.5) obeys one of the following:

1. `det H>=delta`; or
2. `det K>=delta`; or
3. there is an orthonormal basis `(v,w)` of `u^perp` such that

`H=x vv^T+y ww^T`, `K=(1-x)vv^T+(1-y)ww^T`,                         (4.5)

with

`x>1-2delta`, `y<2delta`.                                           (4.6)

Thus in branch 3

`boxed: ||H-vv^T||op<2delta,  ||K-ww^T||op<2delta.}`                (4.7)

#### Proof

If alternatives 1 or 2 hold there is nothing to show. Otherwise

`xy<delta`, `(1-x)(1-y)<delta`.                                     (4.8)

By (4.4), `x>=1/2`, hence

`y<delta/x<=2delta`.                                                 (4.9)

Likewise `1-y>=1/2`, so

`1-x<delta/(1-y)<=2delta`.                                          (4.10)

Diagonalising `H` yields (4.5), and (4.7) follows directly. QED.

### Fixed numerical form

Take

`delta=1/64`.                                                        (4.11)

Then every still-unpaid account02/B20 heavy-row state admits a physical partition for which either

`boxed: det H>=1/64  or  det K>=1/64,}`                             (4.12)

or there is a transverse orthonormal basis `(v,w)` with

`boxed:
 sum_(i in U)<r_i,v>^2 =x>31/32,
 sum_(i in U)<r_i,w>^2 =y<1/32,
 sum_(j in V)<r_j,v>^2 =1-x<1/32,
 sum_(j in V)<r_j,w>^2 =1-y>31/32.}`                               (4.13)

This is an exact product-preserving hyperbolic geometry statement. No small term in (4.13) is deleted.

## 5. Actual analytic currency on the robust-bank branches

Suppose first `det H>=1/64`. Let `B_U` be the physical coefficient matrix whose rows are the two coordinates of `q_i`, `i in U`. Then

`B_U^T B_U=H`.                                                       (5.1)

Whiten deterministically:

`O_U=B_U H^(-1/2)`, so `O_U^T O_U=I_2`.                             (5.2)

For the ORIGINAL product bank `X_U`, the completed weighted affine-fiber theorem gives

`||p_(O_U^T X_U)||_infinity<=e`.                                    (5.3)

Since

`sum_(i in U)q_i X_i = H^(1/2) O_U^T X_U`,                          (5.4)

the change-of-variables determinant yields the actual inequality

`boxed:
 ||p_(sum_(i in U)q_i X_i)||_infinity
 <= e/sqrt(det H)
 <=8e<21.747.}`                                                      (5.5)

The same conclusion holds with V if `det K>=1/64`.

There is simultaneously a fixed anchored same-bank third-volume:

`sum_(i<j, i,j in U) det(r_h,r_i,r_j)^2
 = c det H >1/128`                                                   (5.6)

on the U branch, and analogously on the V branch. Equation (5.6) is an aggregate currency, not a claim that one physical triple determinant is large.

## 6. Exact grouped variables on the near-hyperbolic branch

Assume instead (4.13). In the eigenbasis `(v,w)`, write for `i in U`

`a_i=<q_i,v>`, `b_i=<q_i,w>`,                                      (6.1)

and for `j in V`

`a'_j=<q_j,v>`, `b'_j=<q_j,w>`.                                    (6.2)

Because `(v,w)` diagonalises `H`,

`sum_U a_i b_i=0`, `sum_U a_i^2=x`, `sum_U b_i^2=y`,               (6.3)

and, since `K=I-H`,

`sum_V a'_j b'_j=0`, `sum_V (a'_j)^2=1-x`,
`sum_V (b'_j)^2=1-y`.                                               (6.4)

Whenever the corresponding norm is nonzero, define the normalised original-bank projections

`U_0=x^(-1/2) sum_U a_i X_i`,
`U_1=y^(-1/2) sum_U b_i X_i`,
`V_0=(1-x)^(-1/2) sum_V a'_j X_j`,
`V_1=(1-y)^(-1/2) sum_V b'_j X_j`.                                 (6.5)

The coefficient vectors `(U_0,U_1)` are orthonormal in `l^2(U)`, and `(V_0,V_1)` are orthonormal in `l^2(V)`. Hence their joint density caps are at most `e` by the completed product-projection theorem. More importantly, the U-pair and V-pair are genuinely independent because they use disjoint ORIGINAL coordinate banks.

The transverse spectral contribution is **exactly**

`boxed:
 P R^T X
 = v[ sqrt(x) U_0 + sqrt(1-x) V_0 ]
 + w[ sqrt(y) U_1 + sqrt(1-y) V_1 ].}`                              (6.6)

The coefficients satisfy

`sqrt(x), sqrt(1-y)>sqrt(31/32)=0.9842509...`,
`sqrt(y), sqrt(1-x)<1/sqrt(32)=0.1767767... .`                      (6.7)

Thus the residual heavy-row state has been routed to an exact two-bank near-hyperbolic factorisation: U supplies almost all of one transverse spectral line, V supplies almost all of the orthogonal transverse line, and the two leakage terms are explicitly retained. This is precisely the aggregate mechanism exhibited by the strict-N3 extreme-coloop stress family; unlike a local-pivot claim, it survives that family.

## 7. Application to the newest account02/B20 result

Combining the completed partner auto11 with Theorems 2.1 and 4.1 gives the following sharper exact-rank-three endpoint.

Every account02/B20 auto11 survivor is either

1. **paid immediately** by

`||p_Q||_infinity<215.270`;                                         (7.1)

or it has simultaneously

`|A_hh|<1/4`, `||A[h,h^c]||_2>sqrt(7)/4`, `||r_h||^2>1/2`,          (7.2)

and an ORIGINAL-coordinate partition `U disjoint_union V` for which either

2. one transverse physical bank has Gram determinant at least `1/64`, hence its two-dimensional product projection has density cap `<8e` and its same-bank anchored third-volume exceeds `1/128`; or

3. the exact near-hyperbolic factorisation (6.6)--(6.7) holds with two independent original banks.

The partner's `|B_1|<=18` and designated packet masses remain additional available currency in branches 2--3. The present compiler does not spend them and therefore does not weaken the partner state.

This is a strict narrowing of `QFORM-SMALLPACKET-THREEPACKET-MIXED-RANGE-PAYMENT-v1`: the first unresolved analytic receiver no longer starts from three arbitrary packet ranges. It starts from either a fixed determinant-`1/64` transverse product bank with anchored third-volume, or an explicit `1/32`-leakage hyperbolic split together with the strong physical star (7.2).

## 8. Remaining implication and correction discipline

The first remaining implication after this run is

`QFORM-HEAVYROW-ROBUSTPLANE-OR-HYPERBOLIC-RECEIVER-v1`:

- on branch 2, spend the robust two-dimensional original-bank projection together with its `>1/128` anchored third-volume and the strong hub star, without selecting one tiny physical triple;
- on branch 3, spend the exact two-bank representation (6.6) while retaining both leakage variables and the longitudinal residual physical coefficients. A B06 curved square/hyperbolic receiver is the natural destination, but the leakage and longitudinal terms may not be deleted perturbatively.

The following known-invalid moves are not used: law-uniform pointwise quadratic oscillatory decay; post-rotation independence; arbitrary-joint rank-three coarea; worst-fiber conditional spectral caps; one-good-minor extraction from aggregate volume; or deletion of a small nonzero quadratic tail.

The full QFORM target and global continuity remain OPEN.