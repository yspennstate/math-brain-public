SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B07, 2026-09-23T20:34:21Z.
attacking: the nonexact rank-two-interface tail — robust determinant-weighted coordinate transfer using the heavy E2 singular pair, then physical coordinate-core reduction without discarding the tail.

# fleet02/B07 — robust E2 carrier transfer with the nonzero interface tail retained

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T203421Z-fleet02-B07-qform-f6c2a1`  
Role: coordinate minor selection / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING TAIL-ROBUST TRANSFER + BOUNDED-DIMENSIONAL CORE COMPILER / FULL QFORM OPEN / FULL CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

The unrestricted theorem is not proved or disproved here. Every coordinate set below is an ORIGINAL physical-coordinate set. No post-rotation independence, moment/support/log-concavity assumption, arbitrary-joint coarea estimate, pointwise stationary-phase estimate, or deletion of a small nonzero quadratic tail is used. Determinant volume is aggregated before any reciprocal operation; no universally good individual minor is inferred.

## 1. Fresh source state and exact incoming debt

Fresh owner control remains revision `2026-09-22.15`, with the continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and the full QFORM target still open. The current Claude continuation was refreshed through the live `20260922T231000Z-semidefinite-and-hub-reduction/README.md`; its conditional single-hub adaptation proposal is not used as a proved premise.

The latest designated partner read in this run is fleet03/B07 r37:

`yspennstate/math-open-problems@65ed9ea70175fb28541d756aea01f6aeb491fd6c`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T193839Z-fleet03-B07-qform-r37/REPORT.md`.

It proves an exact-rank-two physical coordinate-transfer compiler and leaves as an explicit essential gap the same transfer when the physical interface has a nonzero higher-rank tail. Its preceding r35-r36 determinant-weighted state supplies the exact packet used below. There are disjoint original-coordinate banks `L,R`,

`K=A[L,R]`,

`Z=e_2(KK^T)>Z_0 h^4`,

with

`Z_0=854675.100194511`,

`h=(2sqrt(2)-1)/1572864=1.1624826588606455e-6`.

Write the positive squared singular values of `K` as `x_1,x_2,...`, with left singular vectors `u_r`. The natural E2 singular-direction inclusion marginal is

`alpha_r=x_r(sum_s x_s-x_r)/Z`,

and `sum_r alpha_r=2`. On the genuinely two-heavy branch, the partner calculation selects two directions `p,q` with `alpha_p,alpha_q>2/3` and proves

`boxed: x_p x_q > Z/3.`                                           (1.1)

The same low-E3 branch retains, rather than deletes, the full interface tail. For every column extension `T=[K Y]`, if `V=e_3(TT^T)<h^6`, the partner's compound-defect projection satisfies

`||(I-P)T||_F^2 <= 9V/Z`,                                        (1.2)

so in the actual packet the interface lies within `0.003245045040 h` in Frobenius norm of its heavy rank-two carrier. Equation (1.2) remains only deterministic coefficient information; it is not treated as a small random error.

The analytic receiver used after producing real third volume is fleet03/B02 r35,

`yspennstate/math-open-problems@52cef3abd27c641ae6666d6ee3bbc25d90cb4813`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T170106Z-fleet03-B02-qform-r35/REPORT.md`.

Its proved theorem `QFORM-CROSS-E3-MARGINALFREE-L1-v1` says that for any literal original-coordinate cross block `B`,

`V_3=e_3(BB^T)>0`

implies a continuous `C_0` full-ambient density with

`boxed: ||p_Q||_infinity <= C_E3 V_3^(-1/6),`                    (1.3)

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.

Arbitrary same-bank curvature, outside couplings, affine terms and additional spectrum remain present.

The bounded-dimensional spectral receiver used below is the completed fleet04/B07 theorem

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`.

If an actual physical block on `r+3` coordinates decomposes as

`D+R+E`, `|D_ii|>=d`, `rank R<=r`, `|E|_max<=eps`,

then

`s_3 >= d-(r+3)eps`,                                              (1.4)

and, when positive,

`||p_Q||_infinity <= 2sqrt(6pi(r+3))/(d-(r+3)eps)`.              (1.5)

This is an actual finite physical core theorem, not a single-minor theorem.

## 2. Physical E2 row marginals retain the heavy singular pair

Define the physical row inclusion marginal of the complete squared-2-minor law of `K` by

`mu_i = (1/Z) sum_{S,T: |S|=|T|=2, i in S} det K[S,T]^2`.         (2.1)

By Cauchy-Binet in exterior degree two and the SVD of `K`,

`boxed:
mu_i = sum_{a<b} (x_a x_b/Z) [u_a(i)^2+u_b(i)^2].
`                                                                    (2.2)

Indeed `w_ab=x_a x_b/Z` is the spectral pair law for `wedge^2 K`, and contraction of the unit bivector `u_a wedge u_b` with the physical basis vector `e_i` has squared norm `u_a(i)^2+u_b(i)^2`. Summing (2.2) in `i` gives

`sum_i mu_i=2`.                                                    (2.3)

Choose the deliberately smaller physical-heavy threshold

`H={i in L: mu_i>1/6}`.                                           (2.4)

Then

`boxed: |H|<=11.`                                                 (2.5)

For `i notin H`, put

`ell_i=u_p(i)^2+u_q(i)^2`.                                        (2.6)

The single spectral pair `(p,q)` is one nonnegative term of (2.2). By (1.1),

`mu_i >= (x_p x_q/Z) ell_i > ell_i/3`.                            (2.7)

Thus every movable nonheavy physical coordinate satisfies

`boxed: ell_i<1/2.`                                               (2.8)

After deleting row `i`, write `hat u_p,hat u_q` for the restrictions. Since `u_p,u_q` were orthonormal,

`boxed:
||hat u_p wedge hat u_q||^2
 = (1-u_p(i)^2)(1-u_q(i)^2)-u_p(i)^2u_q(i)^2
 =1-ell_i
 >1/2.
`                                                                    (2.9)

This is the key loss-control that survives the nonexact interface tail.

## 3. Tail-robust coordinate transfer

For `i notin H`, let

`c_i=A[L\{i},{i}]`                                                (3.1)

be the physical self-column with its diagonal coordinate removed, and define its transverse distance from the heavy singular plane by

`d_i=dist(c_i, span{hat u_p,hat u_q}).`                           (3.2)

Move the original coordinate `i` to the column side and form the literal physical cross block

`B_i=A[L\{i}, R union {i}]=[K_hat_i,c_i].`                        (3.3)

### Theorem 3.1 — `QFORM-NONEXACT-R2-TAIL-ROBUST-TRANSFER-v1`

For every `i notin H`,

`boxed:
e_3(B_iB_i^T) > (Z/6)d_i^2.
`                                                                    (3.4)

In particular, for every `delta>0`, if one nonheavy physical row has `d_i>=delta`, then

`boxed: e_3(B_iB_i^T)>Z delta^2/6,`                              (3.5)

and the full ambient quadratic form is paid by (1.3):

`boxed:
||p_Q||_infinity
 < C_E3 (Z delta^2/6)^(-1/6).
`                                                                    (3.6)

The density is continuous and vanishes at infinity on this branch.

### Proof

Right-multiply the `K_hat_i` columns by the orthogonal right-singular basis of `K`, extending it by the identity on the new column `c_i`. This deterministic coefficient rotation does **not** rotate the random variables and is used only to compute `B_iB_i^T`; it leaves that Gram matrix, and hence `e_3(B_iB_i^T)`, unchanged.

In those coefficient columns, the `p,q` columns of `K_hat_i` are

`sqrt(x_p) hat u_p`, `sqrt(x_q) hat u_q`.

Cauchy-Binet expresses `e_3(B_iB_i^T)` as a sum of squared three-column wedge volumes. Keeping only the nonnegative term from these two transformed columns and `c_i`,

`e_3(B_iB_i^T)
 >=x_p x_q ||hat u_p wedge hat u_q wedge c_i||^2`.                (3.7)

By the Gram determinant / orthogonal projection identity,

`||hat u_p wedge hat u_q wedge c_i||^2
 =||hat u_p wedge hat u_q||^2 d_i^2`.                             (3.8)

Equations (1.1), (2.9), (3.7), (3.8) give

`e_3(B_iB_i^T)>(Z/3)(1/2)d_i^2=(Z/6)d_i^2`.

No extra singular direction can cancel (3.7): all omitted Cauchy-Binet terms are nonnegative. This is exactly why the argument remains valid with the nonzero higher-rank interface tail retained. QED.

## 4. Required application of the pinned e5 result

The mandatory pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,

proves the D' extension of determinant-volume decoupling: for a physical cross block with third volume `V_3`, if its natural row third-volume marginals are at most `h_D<3/4`, then

`||p_Q||_infinity
 <=6sqrt(e)(2h_D)^(-1/2)(3-4h_D)^(-1)V_3^(-1/6)`.                (4.1)

Apply this completed result to the **actual transferred block** `B_i` in (3.3)-(3.5). If its row marginals are at most `2/3`, choose `h_D=2/3`; then (4.1) and (3.5) give the real full-ambient inequality

`boxed:
||p_Q||_infinity
 <9sqrt(3e) (Z delta^2/6)^(-1/6).
`                                                                    (4.2)

At the live scale `Z>Z_0h^4`, `delta=h/1024`,

`Z delta^2/6 > [Z_0/(6*1024^2)]h^6
              =0.13584694865457392 h^6`,                         (4.3)

so the pinned e5 theorem gives

`boxed: ||p_Q||_infinity <35.846112471/h <3.084e7`                (4.4)

on its stated marginal-gate subbranch. This is an equation-level application of the completed pinned theorem, not a nominal citation. When that D' marginal gate fails, the later marginal-free E3 theorem (1.3) pays the same transferred volume with the sharper unconditional branch bound

`boxed: ||p_Q||_infinity <14.714689250/h <1.266e7.`               (4.5)

Thus the new geometric transfer does not leave a marginal debt.

## 5. Failure of every transfer produces a bounded-dimensional coordinate-core alternative

Assume now that

`d_i<delta` for every `i notin H`.                                (5.1)

Let `U=span{u_p,u_q}`. For each nonheavy `i`, choose `v_i in U` such that after deleting coordinate `i`,

`||c_i-(v_i)_{hat i}||_2<delta`.                                  (5.2)

Put these `v_i` as the nonheavy columns of a matrix `L_0`, and put zero columns on the heavy set `H`. Since every column lies in `U`,

`rank L_0<=2`.                                                     (5.3)

Let

`C=A[L,L]`, `S=(L_0+L_0^T)/2`.                                   (5.4)

Then `S` is symmetric and

`rank S<=4`.                                                       (5.5)

For distinct nonheavy `i,j`, symmetry of `C` and (5.2) give both

`|(L_0)_{ji}-C_{ji}|<delta`, `|(L_0)_{ij}-C_{ij}|<delta`,

hence

`|C_ij-S_ij|<delta`.                                              (5.6)

Let `P_H` be coordinate projection onto the at-most-eleven-dimensional heavy set, `Q_H=I-P_H`, and `M=C-S`. Define

`R_H=P_H M+Q_H M P_H`.                                            (5.7)

This agrees with `M` on every entry touching `H`, and

`rank R_H<=2|H|<=22`.                                             (5.8)

Thus

`N=M-R_H=Q_H M Q_H`                                               (5.9)

is supported entirely on the nonheavy-by-nonheavy block. Set

`D=diag(N)`, `E=N-D`, `R_0=S+R_H`.                               (5.10)

Then the **actual physical self-block** has

`boxed:
C=D+R_0+E,
rank R_0<=26,
diag E=0,
|E|_max<delta.
`                                                                    (5.11)

No coordinate minor has been inverted.

Now apply the completed coordinate-core theorem (1.4)-(1.5) with `r=26`, so `r+3=29`.

If at least 29 diagonal entries of `D` have magnitude at least `58delta`, choose any 29 of those ORIGINAL coordinates. On that actual core,

`d-(r+3)eps >=58delta-29delta=29delta`,                            (5.12)

therefore

`boxed:
||p_Q||_infinity
 <= 2sqrt(174pi)/(29delta).
`                                                                    (5.13)

If fewer than 29 such diagonal entries exist, at most 28 do. Absorb those exceptional diagonal entries into the low-rank part. This yields instead

`boxed:
A[L,L]=R_L+E_L,
rank R_L<=54,
|E_L|_max<58delta.
`                                                                    (5.14)

This is the completed bounded-dimensional spectral subproblem in the current branch: many large physical diagonals produce an actual 29-coordinate three-eigenvalue core; otherwise failure is compressed into a bounded-rank self-block plus an entrywise-small tail. The small tail is **not** called a small random quadratic perturbation.

At `delta=h/1024`, the core branch has the explicit unoptimized bound

`boxed: ||p_Q||_infinity <1651.130938/h <1.421e9,`                (5.15)

while the structural alternative is

`rank R_L<=54`,

`|E_L|_max<(58/1024)h=(29/512)h
          =6.584374435e-8`.                                      (5.16)

The same argument applies on the opposite physical bank with the paired right singular vectors.

## 6. What this closes in the partner r37 gap

The latest partner r37 was already complete on the **exact-rank-two** cut and explicitly left the nonexact higher-rank interface tail unpaid. Theorem 3.1 closes the determinant-transfer part of that exact gap: the extra singular directions cannot destroy the transferred third volume because the proof takes one positive Cauchy-Binet term after a deterministic coefficient-column SVD. In particular, the transfer payment (3.6) is valid even when the r35-r36 Frobenius tail is nonzero.

Combining Sections 3-5 with the partner's retained-tail estimate gives the following current compiler on the rank-two-heavy low-E3 branch. For `delta=h/1024`, on each relevant physical side at least one holds:

1. a moved original coordinate generates aggregate physical E3 and the full ambient density is `<1.266e7` (with continuity);
2. an actual 29-coordinate physical principal core pays with the unoptimized bound `<1.421e9`;
3. the self-block is `rank<=54 + entrywise<(29/512)h`, while the full nonzero crossing/interface tail remains explicitly controlled by the partner's Frobenius estimate (1.2), rather than discarded.

This is a determinant/volume-weight compiler. It does not infer a universally good single minor.

## 7. New first unpaid implication

The sharpened remaining B07 debt is

`QFORM-R54-INTERNAL-PLUS-R2-INTERFACE-ROUGH-RECEIVER-v1`:

> Pay the literal original-coordinate chamber in which the relevant self-block is `rank<=54 + entrywise<(29/512)h`, while the crossing remains in the partner's rank-two carrier tube with its true nonzero Frobenius tail retained. Preserve arbitrary complement curvature, all additional eigenvalues, arbitrary fragmented/unbounded cap-one laws and conditioning-generated affine terms. Alternatively force a new aggregate physical E3 packet or another actual bounded physical core.

The rank-one-heavy singular alternative of the partner, and its other hub/grid siblings, remain separate debts. A dimension-growing entrywise-small tail cannot be deleted under the target's moment-free laws.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains separate; continuity is obtained only on the E3-transfer branch above.

## 8. Finite regression check

A 500-instance numerical regression on synthetic nonexact rank-four interfaces with a two-heavy E2 singular pair checked the inequality

`e_3(B_iB_i^T) >= (Z/6)d_i^2`

for every generated physical row satisfying `mu_i<=1/6`; there were zero violations and the smallest observed ratio of left to right side was approximately `5.0449`. This is regression evidence only. The proof is the exterior-algebra/Cauchy-Binet argument in Section 3.
