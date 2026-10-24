# account03/B07 r37 — determinant-weighted coordinate transfer from a rank-two physical interface

**Status.** New coordinate-transfer supporting theorem proved. Full QFORM remains OPEN. During the mandatory pre-publication refresh, a newer source was found that had independently added the determinant/geometric-mean refinement to the exact-rank physical-crossing theorem. Therefore that refinement is treated below as a fresh dependency, not as a new B07 claim. The genuinely new B07 contribution is the row-minor inclusion/coordinate-transfer compiler and its reduction to a paid branch or a low-rank-plus-entrywise-small chamber. No individual coordinate minor is inverted.

## 1. Scope and dependencies

Target: for independent real inputs with densities at most one and symmetric real `A` with at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `X^T A X`, or give a counterexample.

This report does **not** solve the full target. It uses only original-coordinate cuts, so independence is never asserted after a spectral rotation.

Dependencies used exactly as stated:

1. **LPP product-projection density bound:** an orthogonal `k`-dimensional projection of independent cap-one coordinates has density at most `2^(k/2)`.
2. **Exact-rank physical crossing Fourier theorem with determinant refinement**, latest pre-publication source `yspennstate/math-open-problems@d9b3190196190fff223b48f71d0668dcf07ec702`, path `proofnet24/QFORM-density/interactive/20260923T194300Z-exact-cross-rank-fourier/REPORT.md`. For a literal original-coordinate cut whose entire crossing block has exact rank `k>=3` and nonzero singular values `d_1,...,d_k`, with `g=(prod_j d_j)^(1/k)`, it proves a bounded continuous full-ambient density with `||p_Q||_infty <= 2k/((k-2)g)`. This source appeared after my initial read, so duplicate work on this exact scope stops here.
3. **Designated partner account04/B07 coordinate-core theorem**, source `yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`: if an original-coordinate block of size `r+3` has `D+R+E`, `|D_ii|>=d`, `rank R<=r`, `|E|_max<=eps`, then `s_3>=d-(r+3)eps` and the full ambient quadratic form has density at most `2 sqrt(6 pi (r+3))/(d-(r+3)eps)` when the denominator is positive. Its source does not claim full-target continuity.

The live correction ledger prohibiting pointwise van-der-Corput decay, rotated-coordinate independence, naive fiber-sup arguments, and replacement of small nonzero terms by zero is respected throughout.

## 2. Fresh source-matching determinant payment

The pre-publication source refresh records the exact-rank theorem in the following determinant form. If a physical crossing `B` has exact rank `k>=3` and

`Delta_k(B)=prod_{j=1}^k s_j(B)=sqrt(pdet(BB^T))`,

then

`||p_Q||_infty <= [2k/(k-2)] Delta_k(B)^(-1/k)`.

For exact rank three,

`||p_Q||_infty <= 6 / (s_1(B)s_2(B)s_3(B))^(1/3)`.

Its proof keeps the determinant in the same projected-bank Plancherel estimate rather than replacing every singular value by the smallest one. I use this theorem below; I do not claim it as a new B07 theorem.

## 3. Row-minor inclusion accounting for an exact rank-two physical cut

Let `L sqcup R=[n]` be an original-coordinate partition and assume

`K=A[L,R]`

has exact rank two. Define

`Z=e_2(KK^T)=(s_1(K)s_2(K))^2>0`.

Equivalently, `Z` is the sum of the squares of all literal physical `2x2` minors of `K`.

For `i in L`, let `K_hat_i` be `K` with row `i` deleted, and set

`Z_i=e_2(K_hat_i K_hat_i^T)`.

Define the row inclusion marginal

`mu_i=1-Z_i/Z`.

Because every squared `2x2` minor uses exactly two rows,

`sum_i mu_i=2`.

Hence the heavy set

`H={i: mu_i>2/3}`

has cardinality at most two, and every `i notin H` satisfies

`Z_i >= Z/3`.

This is the determinant-weighted deletion principle used below. It is dimension free and does not select a single minor.

## 4. Moving one original coordinate across the cut

Write `C=A[L,L]`. For `i in L`, define the physical self-column with its diagonal entry removed,

`c_i=A[L\{i},{i}]`,

and

`q_i=dist(c_i, col(K_hat_i))`.

If `i notin H`, move the original coordinate `i` from the left bank to the right bank. The new *entire* physical crossing is

`B_i=A[L\{i}, R union {i}] = [K_hat_i, c_i]`.

Since `K_hat_i` has rank two, `B_i` has rank at most three. If `q_i>0`, it has exact rank three. Gram-Schmidt / exterior algebra gives the exact identity

`Delta_3(B_i)^2 = e_3(B_i B_i^T)=Z_i q_i^2`,

so

`Delta_3(B_i)=sqrt(Z_i) q_i`.

Therefore, for any `delta>0`, if some nonheavy row satisfies `q_i>=delta`, the fresh exact-rank determinant theorem pays the **full ambient form** with a continuous density:

`||p_Q||_infty <= 6 [sqrt(Z/3) delta]^(-1/3)`.

This is the first branch of the new B07 compiler.

## 5. If every movable column is nearly contained in the rank-two interface

Assume now

`q_i<delta` for every `i notin H`.

Let `U=col(K)`, a two-dimensional subspace of `R^L`. For each nonheavy `i`, choose `u_i in U` whose restriction away from coordinate `i` approximates `c_i` within Euclidean norm `delta`. Put these `u_i` as the nonheavy columns of a matrix `L_0`, and put zero columns on `H`. Then

`rank L_0<=2`.

Set

`S=(L_0+L_0^T)/2`,

so `S` is symmetric and `rank S<=4`. For distinct nonheavy `i,j`, both column approximations imply

`|C_ij-S_ij|<delta`.

Let `P` be the coordinate projection onto the heavy set `H`, `Q=I-P`, and `M=C-S`. Define the symmetric heavy-row/column correction

`R_H=P M + Q M P`.

It agrees with `M` on every entry touching `H`, and

`rank R_H <= 2 |H| <=4`.

Thus

`N=M-R_H=Q M Q`

is supported on the nonheavy-by-nonheavy block. Put

`D=diag(N)`, `E=N-D`, `R_0=S+R_H`.

Then

`C=D+R_0+E`,

with

`rank R_0<=8`, `diag(E)=0`, and `|E|_max<delta`.

This is a genuine original-coordinate decomposition; no spectral coordinate is declared independent.

## 6. Actual application of the completed account04/B07 theorem

Apply the designated partner theorem with `r=8`.

If at least eleven diagonal entries of `D` satisfy

`|D_ii|>=22 delta`,

restrict to any eleven such original coordinates. On that block,

`d-(r+3) eps >=22 delta-11 delta=11 delta`.

Therefore the partner theorem gives the full ambient density estimate

`||p_Q||_infty <= 2 sqrt(66 pi)/(11 delta)`.

Continuity is not asserted here because the partner source records continuity separately.

If there are fewer than eleven such diagonal entries, there are at most ten. Absorb those exceptional diagonal entries into the low-rank term. The result is

`C=R_1+E_1`,

with

`rank R_1<=8+10=18`,

and

`|E_1|_max<22 delta`.

Thus the near-containment alternative is not left vague: it either pays through the partner's eleven-coordinate core, or the whole physical self-block is within entrywise `22 delta` of rank at most eighteen.

## 7. New theorem: QFORM-R2-CROSS-TRANSFER-OR-LOWRANK-v1

For an exact-rank-two physical cut `K=A[L,R]`, `Z=e_2(KK^T)>0`, and any `delta>0`, at least one holds:

1. **Transferred exact-rank-three crossing:** the full form has a bounded continuous density

   `||p_Q||_infty <= 6 [sqrt(Z/3) delta]^(-1/3)`.

2. **Partner coordinate-core payment:** the full form has density

   `||p_Q||_infty <= 2 sqrt(66 pi)/(11 delta)`.

3. **Low-rank self-block:**

   `A[L,L]=R_L+E_L`, `rank R_L<=18`, `|E_L|_max<22 delta`.

Apply the same theorem from the opposite side. If neither side pays, then the exact-rank-two cross term itself has symmetric rank at most four, so

`A=R+E`,

with

`rank R<=18+18+4=40`,

and

`|E|_max<22 delta`.

Hence an exact-rank-two physical interface is reduced, before any tiny-minor inversion, to a paid density branch or a global `rank<=40 + entrywise-small` chamber.

## 8. Application to the current B07 rank-two-interface scale

The previous B07 r36 survivor supplies, on its genuinely exact-rank-two subcase,

`s_1(K)s_2(K) > P_0 h^2`,

with

`P_0=533.7524707810138`,

`h=(2 sqrt(2)-1)/1572864 = 1.1624826588606455e-6`.

Thus `sqrt(Z/3)>P_0 h^2/sqrt(3)`.

Choose

`delta=h/1024`.

Then the transferred-crossing determinant satisfies

`Delta_3 > [P_0/(1024 sqrt(3))] h^3`

`=0.300939582701217 h^3`,

so branch 1 gives

`||p_Q||_infty < 8.953471982 h^(-1)`

`< 7.703e6`.

Branch 2 gives

`||p_Q||_infty < 2680.921955 h^(-1)`

`<2.307e9`.

If neither side pays, the two-sided conclusion is

`A=R+E`, `rank R<=40`,

`|E|_max < (11/512) h = 2.4975213374e-8`.

This application is only to the **exact-rank-two** subcase of the r36 physical interface. The general r36 survivor can have a nonzero higher-rank interface tail; this report does not delete that tail or treat it as harmless. That remains an essential gap.

## 9. What changed and what remains

The fresh source already closes the determinant/geometric-mean exact-crossing payment. The new B07 contribution is what feeds it: determinant-weighted row deletion plus an actual original-coordinate transfer turns a transverse self-column into an exact rank-three crossing with aggregate product `sqrt(Z_i) q_i`. If every such transfer fails quantitatively, the completed account04/B07 theorem turns the failure into a paid eleven-coordinate core or a rank-eighteen-plus-entrywise-small self block. Two-sided failure gives a global rank-forty-plus-entrywise-small chamber.

The next missing implication is:

**QFORM-RANK40-ENTRYWISE-SMALL-OR-NONEXACT-R2-TAIL-RECEIVER-v1.** Either consume the resulting `rank<=40 + entrywise-small` global chamber under the original three-large-eigenvalue hypothesis, or extend the coordinate-transfer argument to the genuinely higher-rank interface with a nonzero small tail without discarding it.

The latter is especially important because the exact-rank Fourier crossing theorem cannot simply ignore extra tiny singular directions.

Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN. Continuity is proved only on the transferred exact-rank-three Fourier branch above.

## 10. Finite regression checks

`CHECKS.py` verifies on random finite matrices:

- `sum_i mu_i=2` and at most two rows satisfy `mu_i>2/3`;
- `e_3([K_hat_i,c_i][K_hat_i,c_i]^T)=e_2(K_hat_i K_hat_i^T) q_i^2`;
- the low-containment construction reconstructs `C` exactly up to floating error, with rank at most eight before absorbing exceptional diagonals and with entrywise residual below `delta`;
- all numerical constants in Section 8.

The captured output ends `STATUS=PASS`. These checks are regression evidence only, not proof evidence.
