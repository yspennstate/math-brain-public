SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T21:25:00Z.
attacking: aggregate the moving-coordinate E2-to-E3 transfer before choosing any pivot; either a single literal physical cut receives the total mixed third-volume currency, or the current two-heavy E2 carrier synchronizes the self-block into a common rank-16 plus Frobenius-small form and then a rank-34 plus operator-small tube.

# account01/B07 r34 — aggregate moving-coordinate physicalization and operator-norm synchronization

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW DIMENSION-FREE MIXED-E3 PHYSICALIZATION + NEW COMMON-PLANE FROBENIUS SYNCHRONIZATION + NEW RANK34/OPERATOR-TAIL REFINEMENT / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

All coordinate sets below are ORIGINAL physical coordinates. Orthogonal singular-vector calculations are used only as deterministic coefficient identities; no random variables are rotated and no independence after rotation is asserted. No moment, support, log-concavity, Gaussian, iid, compactness or connected-support hypothesis is added. A small nonzero coefficient tail is retained, never replaced by zero.

## 1. Source-pinned state

Fresh owner control remains `2026-09-22.15`, with continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; the unrestricted theorem and its global continuity upgrade remain open.

The latest completed designated partner available at the substantive source refresh is account02/B07:

`yspennstate/math-open-problems@726fef06d05f2d3024bd1565c736df43efb45d62`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T203421Z-account02-B07-qform-f6c2a1/REPORT.md`.

Its live two-heavy E2 carrier supplies a physical partition and crossing

`K=A[L,R]`,

`Z=e_2(KK^T)>Z_0 h^4`,

`Z_0=854675.100194511`,

`h=(2sqrt(2)-1)/1572864`,

and two singular directions `p,q`, with squared singular values `x_p,x_q`, such that

`boxed: x_p x_q>Z/3.`                                             (1.1)

It also supplies the exact physical E2 row-inclusion identity

`mu_i=sum_{a<b}(x_a x_b/Z)[u_a(i)^2+u_b(i)^2`,

so `sum_i mu_i=2`. Its sharpened heavy threshold is

`H={i:mu_i>2/7}`, hence `|H|<=6`.                                 (1.2)

The current account03/B07 tail-stable transfer is

`yspennstate/math-open-problems@f822a8dfdb6a2cbc763373954a8b9dadb498568d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T203843Z-account03-B07-qform-r38/REPORT.md`.

For a general-rank crossing it defines, after deleting physical row `i`, the second Newton transform and a rank-at-most-two determinant-heavy plane `P_i`. For all but at most two physical rows,

`J_i >= (Z/9) q_i^2`,                                             (1.3)

where `q_i=dist(A[L\{i},{i}],range(P_i))` and `J_i` is exactly the added-column third-volume packet defined below. This retains every crossing singular direction.

The analytic receiver used below is the completed marginal-free physical-E3 theorem

`yspennstate/math-open-problems@52cef3abd27c641ae6666d6ee3bbc25d90cb4813`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T170106Z-account03-B02-qform-r35/REPORT.md`:

for any literal original-coordinate crossing `B` with

`V_3=e_3(BB^T)>0`,

one has a continuous `C_0` full-ambient density and

`boxed: ||p_Q||_infinity <= C_E3 V_3^(-1/6),`

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.                  (1.4)

Arbitrary same-bank curvature, outside couplings, affine terms and extra spectrum are retained.

The finite-coordinate diagonal-plus-rank receiver used in Section 5 is the completed account04/B07 theorem pinned in the designated-partner report:

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

If an actual physical block on `r+3` coordinates has `D+R+E`, `|D_ii|>=d`, `rank R<=r`, `|E|_max<=eps`, then

`s_3 >= d-(r+3)eps`

and, when positive,

`||p_Q||_infinity <= 2sqrt(6pi(r+3))/(d-(r+3)eps)`.              (1.5)

I do not infer continuity from (1.5).

## 2. Exact mixed third-volume packet

Fix disjoint physical banks `L,R`. For `i in L`, delete row `i` from `K=A[L,R]`:

`K_i=K[L\{i},R]`, `G_i=K_iK_i^T`,

and let

`c_i=A[L\{i},{i}]`                                               (2.1)

be the physical self-column with its diagonal coordinate removed. Append that column to the crossing:

`B_i=[K_i,c_i]=A[L\{i},R union {i}]`.                            (2.2)

Define only the **new-column** third-volume packet

`J_i := e_3(B_iB_i^T)-e_3(G_i)`.                                (2.3)

By Cauchy--Binet this has the literal original-coordinate expansion

`boxed:
J_i=
 sum_{S subset L\{i}, |S|=3}
 sum_{J subset R, |J|=2}
 det A[S,J union {i}]^2.
`                                                                    (2.4)

Equivalently, with the second Newton transform

`H_2(G)=G^2-tr(G)G+e_2(G)I`,

one has the exact rank-one update identity

`J_i=c_i^T H_2(G_i)c_i`.                                         (2.5)

The distinction between `J_i` and the full `e_3(B_iB_i^T)` is useful: every determinant in `J_i` has one distinguished moved physical column `i`, so the packets for different `i` can be aggregated without ambiguity.

## 3. Main new theorem: aggregate moving-coordinate physicalization

### Theorem 3.1 — `QFORM-MIXED-E3-RANDOM-CUT-PHYSICALIZATION-v1`

For every subset `I_0 subset L`, there exists a physical bipartition

`L=U sqcup V`

such that the literal crossing

`M=A[U,R union V]`                                                (3.1)

satisfies

`boxed:
e_3(MM^T) >= (1/16) sum_{i in I_0} J_i.
`                                                                    (3.2)

No individual `2x2` or `3x3` minor is selected or inverted.

### Proof

Color every coordinate of `L` independently red/blue with probability `1/2`, and set `U=red`, `V=blue`. Consider one fixed summand of (2.4), indexed by `(i,S,J)` with `i in I_0`, `|S|=3`, `S subset L\{i}`, `J subset R`, `|J|=2`.

This exact determinant occurs as a `3x3` minor of `A[U,R union V]` whenever

- `i` is blue, so its moved column lies in `V`, and
- all three coordinates of `S` are red, so they lie in the row bank `U`.

The four relevant coordinates are distinct, so this event has probability exactly `2^(-4)=1/16`. Every selected summand is nonnegative and every selected determinant is part of the complete `e_3(MM^T)` Cauchy--Binet sum. Therefore

`E e_3(MM^T)
 >= (1/16) sum_{i in I_0} J_i`.

At least one deterministic coloring attains the expectation. QED.

This is the dimension-free averaging step that is missing from a pointwise moving-coordinate argument: a large *total* transverse defect cannot hide by spreading over many coordinates.

## 4. First application: the arbitrary-rank moving planes are paid in l2

Apply Theorem 3.1 to the nonheavy rows from account03/B07 r38. Its exact Newton-transform inequality (1.3) gives

`sum_{i notin H_phys} J_i
 >= (Z/9) sum_{i notin H_phys} q_i^2`,                             (4.1)

where `|H_phys|<=2`. Hence one literal physical crossing satisfies

`boxed:
e_3(MM^T)
 >= (Z/144) Q_mov^2,
qquad
Q_mov^2:=sum_{i notin H_phys} q_i^2.
`                                                                    (4.2)

Consequently the full ambient form has a continuous density whenever `Q_mov>0`, with

`boxed:
||p_Q||_infinity
 <= C_E3 (Z Q_mov^2/144)^(-1/6).
`                                                                    (4.3)

This strictly strengthens the pointwise r38 exit: r38 requires one `q_i>=delta`; (4.3) pays whenever the **aggregate** Euclidean defect satisfies `Q_mov>=delta`, even if every individual `q_i<delta`.

At the live scale, choose

`delta=h/1024`.                                                   (4.4)

If `Q_mov>=delta`, then

`e_3(MM^T)
 > [Z_0/(144*1024^2)] h^6
 =0.0056602895272739135 h^6`,                                    (4.5)

and

`boxed:
||p_Q||_infinity
 <24.991153492 h^(-1)
 <2.150e7.
`                                                                    (4.6)

The branch (4.6) is continuous and vanishes at infinity by (1.4). No synchronization of the varying planes `P_i` was assumed in deriving it.

## 5. Designated-partner application: a common fixed plane and Frobenius synchronization

Now use the stronger structure from the latest completed **designated partner account02/B07**. Its two-heavy singular directions `u_p,u_q` obey (1.1).

For a physical row `i`, set

`ell_i=u_p(i)^2+u_q(i)^2`.                                       (5.1)

Take the partner's sharpened physical-heavy set `H={mu_i>2/7}`. Since the single spectral pair `(p,q)` contributes nonnegatively to the exact marginal formula,

`mu_i >= (x_p x_q/Z) ell_i > ell_i/3`.                            (5.2)

Thus every `i notin H` satisfies

`ell_i<6/7`,                                                      (5.3)

and after deleting coordinate `i`,

`||hat u_p wedge hat u_q||^2=1-ell_i>1/7`.                       (5.4)

Define the distance of the physical self-column from this **one common global singular plane** by

`d_i=dist(c_i,span{hat u_p,hat u_q}).`                            (5.5)

The new-column packet (2.4) is invariant under an orthogonal change of coefficient basis inside the two chosen `K_i` columns. Keeping only the `(p,q,c_i)` nonnegative Cauchy--Binet contribution gives

`J_i
 >=x_p x_q ||hat u_p wedge hat u_q wedge c_i||^2
 =x_p x_q(1-ell_i)d_i^2
 >(Z/21)d_i^2`.                                                   (5.6)

This is an equation-level application of the completed partner inequality `x_p x_q>Z/3`; no reciprocal star or determinant is paid.

Put

`D_perp^2:=sum_{i notin H} d_i^2`.                               (5.7)

Combining (5.6) with Theorem 3.1 yields a single literal physical crossing with

`boxed:
e_3(MM^T) > (Z/336) D_perp^2.
`                                                                    (5.8)

Therefore

`boxed:
||p_Q||_infinity
 < C_E3 (Z D_perp^2/336)^(-1/6)
`                                                                    (5.9)

with a continuous density on this branch.

At the same live scale `D_perp>=h/1024`,

`e_3(MM^T)
 > [Z_0/(336*1024^2)]h^6
 =0.002425838368831677 h^6`,                                     (5.10)

and

`boxed:
||p_Q||_infinity<28.781655200 h^(-1)<2.476e7.
`                                                                    (5.11)

The point of the weaker constant compared with (4.6) is structural: failure of (5.11) synchronizes *all* nonheavy self-columns to one fixed global two-plane, which can be compiled into an operator-norm tube.

## 6. Failure of the aggregate fixed-plane exit gives a Frobenius-small residual

Assume

`D_perp<delta`.                                                   (6.1)

For every nonheavy `i`, choose `v_i in U:=span{u_p,u_q}` whose restriction away from coordinate `i` minimizes (5.5):

`||c_i-(v_i)_{hat i}||_2=d_i`.                                  (6.2)

Let `L_0` be the matrix whose nonheavy column `i` is `v_i`, and whose heavy columns are zero. Then

`rank L_0<=2`.                                                    (6.3)

Set

`S=(L_0+L_0^T)/2`, so `rank S<=4`.                               (6.4)

Write `C=A[L,L]`. Let `P_H` be the coordinate projection onto the at-most-six heavy coordinates and `Q_H=I-P_H`. Put

`M_0=C-S`,

`R_H=P_H M_0+Q_H M_0P_H`.                                       (6.5)

This symmetric matrix agrees with `M_0` on every entry touching `H`, and

`rank R_H<=2|H|<=12`.                                            (6.6)

Hence

`N=M_0-R_H=Q_HM_0Q_H`                                           (6.7)

is supported on the nonheavy-by-nonheavy block. Let

`D_0=diag(N)`,

`E=N-D_0`,

`R_0=S+R_H`.                                                     (6.8)

Then

`boxed:
C=D_0+R_0+E,
rank R_0<=16,
diag E=0.
`                                                                    (6.9)

The new point is the **dimension-free Frobenius bound**

`boxed: ||E||_F^2 <= sum_{i notin H}d_i^2=D_perp^2<delta^2.`     (6.10)

### Proof of (6.10)

For nonheavy `i`, define the column error

`epsilon^(i)_j=C_{ji}-(v_i)_j`, `j!=i`,

so `sum_{j!=i}|epsilon^(i)_j|^2=d_i^2`. For distinct nonheavy `i,j`, symmetry gives

`E_ij=C_ij-S_ij
     =(epsilon^(i)_j+epsilon^(j)_i)/2`.                           (6.11)

Therefore

`sum_{i!=j; i,j notin H}|E_ij|^2
 <=sum_{i notin H}sum_{j!=i}|epsilon^(i)_j|^2
 =D_perp^2`.                                                     (6.12)

All other entries of `E` vanish. QED.

This is strictly stronger than an entrywise-small remainder: its operator norm is automatically at most `delta`, independent of dimension.

## 7. Finite-core payment or rank-34 plus operator-small tail

The decomposition (6.9)-(6.10) feeds the completed account04/B07 coordinate-core theorem (1.5) with `r=16` and `eps=delta`.

If at least nineteen diagonal entries of `D_0` satisfy

`|D_0(ii)|>=20delta`,                                             (7.1)

choose any nineteen of those ORIGINAL coordinates. Then

`d-(r+3)eps >=20delta-19delta=delta`,                             (7.2)

and (1.5) gives

`boxed:
||p_Q||_infinity <= 2sqrt(114pi)/delta.
`                                                                    (7.3)

I claim essential boundedness only from this source, not continuity.

Otherwise at most eighteen diagonal entries have magnitude at least `20delta`. Absorb those coordinate diagonals into the rank part. Since a diagonal matrix supported on at most eighteen coordinates has rank at most eighteen, one gets

`boxed:
A[L,L]=R_L+T_L,
rank R_L<=34,
||T_L||_op<21delta.
`                                                                    (7.4)

Indeed the unabsorbed diagonal has operator norm `<20delta`, while `||E||_op<=||E||_F<delta`.

At the live choice `delta=h/1024`,

`boxed: ||T_L||_op<(21/1024)h=2.38399764024e-8.`                  (7.5)

This is the main deterministic refinement over the previous rank-34 **entrywise** tube: the surviving tail is now small in operator norm with no dimension factor. It is still retained as a genuine nonzero quadratic coefficient matrix; no moment argument is used to delete it.

## 8. Two-sided consequence in the current full physical cut

The current account03/B07 r38 chamber has a literal physical cut `L sqcup R=[n]`. Run Sections 5-7 on the left and, by transposition, on the right.

On the live low-E3 two-heavy branch, account03/B07 r36 supplies an actual rank-two crossing carrier `K_2` with

`||K-K_2||_F<0.003245045040 h`.                                  (8.1)

If neither side is paid by (5.11) or (7.3), write

`A[L,L]=R_L+T_L`, `rank R_L<=34`, `||T_L||_op<21delta`,

`A[R,R]=R_R+T_R`, `rank R_R<=34`, `||T_R||_op<21delta`.          (8.2)

Then the entire symmetric matrix decomposes as

`A=R+T`,                                                         (8.3)

where

`R=[[R_L,K_2],[K_2^T,R_R]]`,

so

`boxed: rank R<=34+34+2 rank(K_2)<=72,`                           (8.4)

and

`T=[[T_L,K-K_2],[(K-K_2)^T,T_R]]`.

The block-diagonal part has norm `<21delta`, while the symmetric off-diagonal tail has operator norm exactly `||K-K_2||_op<=||K-K_2||_F`. Thus

`boxed:
||T||_op<21delta+0.003245045040 h.
`                                                                    (8.5)

At `delta=h/1024`,

`boxed:
||T||_op<0.02375285754 h<2.762e-8.
`                                                                    (8.6)

Since the original target has `s_3(A)>=1`, Weyl's inequality implies that this rank-at-most-72 carrier `R` itself has at least three eigenvalues of absolute value exceeding `1-2.762e-8`. This is deterministic coefficient information only; it does **not** justify dropping `T` for arbitrary unbounded cap-one inputs.

Thus the current two-heavy low-E3 survivor is reduced to:

1. a continuous E3-paid branch from aggregate moving-coordinate volume;
2. an actual nineteen-coordinate diagonal-plus-rank payment;
3. or a global `rank<=72 + operator-norm <2.762e-8` coefficient tube whose nonzero tail is retained.

The remaining analytic implication is therefore sharply isolated as

`QFORM-R72-OPSMALL-ROUGHLAW-RECEIVER-v1`:

> Consume a symmetric target matrix `A=R+T` with `rank R<=72`, `s_3(A)>=1`, and the explicit dimension-free coefficient bound `||T||_op<2.762e-8`, for arbitrary independent cap-one laws, without treating `X^T T X` as a small random perturbation and without moments; or force fresh physical E3 / grouped-hub currency from the tail.

The rank-one-heavy interface sibling remains separate. Full QFORM is still OPEN.

## 9. Numerical constants and regression status

At the live scale:

- arbitrary-rank aggregate moving-plane payment:
  `Z_0/(144*1024^2)=0.0056602895272739135`,
  density coefficient `24.991153492/h`;
- fixed common-plane aggregate payment:
  `Z_0/(336*1024^2)=0.002425838368831677`,
  density coefficient `28.781655200/h`;
- synchronized self-block tail:
  `||E||_F<h/1024`;
- post-diagonal rank-34 tail:
  `||T_L||_op<21h/1024`;
- two-sided full-matrix tube:
  `rank<=72`, `||T||_op<(21/1024+0.003245045040)h<2.762e-8`.

A finite regression script in this run folder checks the exact `1/16` random-color expectation, domination by the full E3 crossing, the fixed-pair packet inequality, and the Frobenius synchronization identity on random finite symmetric matrices. It is regression evidence only; the proof is Sections 2-8.

## 10. Scope

No claim here solves the full conjecture or the global continuity request. Continuity is established only on the marginal-free E3 branches through (1.4). The coordinate-core branch is recorded only as an essential density bound. The final operator-small coefficient tail is **not** deleted, and no stochastic smallness is inferred from its operator norm.

The proof uses the designated account02/B07 result at the actual inequality (5.2)-(5.6), and uses account03/B07 r38 only for the independent arbitrary-rank aggregate extension (4.1)-(4.6). The two mechanisms are kept distinct.