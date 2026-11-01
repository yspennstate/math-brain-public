SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T19:20:55Z.
attacking: remove the aggregate third-volume row-marginal gate by recursively promoting concentrated ORIGINAL-coordinate rows to one-, two-, and three-hub bilinear receivers before any reciprocal physical minor is selected.

# fleet03/B09 r40 — unconditional third cross-volume by marginal promotion

## Status

This run proves a new source-coordinate supporting theorem, **`QFORM-CROSS-E3-MARGINAL-PROMOTION-CLOSURE-v1`**, pending independent review.

For **any** disjoint original-coordinate cut `I|J`, if the physical cross block `B=A[I,J]` has positive aggregate squared third volume

\[
Z_3(B):=e_3(BB^T)
=\sum_{R\subset I,\ |R|=3}\det(B_RB_R^T)>0,
\]

then the full quadratic form, with arbitrary same-side curvature on both banks, arbitrary outside coordinates/couplings, arbitrary affine terms and arbitrary signs, has a continuous density satisfying

\[
\boxed{\|p_Q\|_\infty\le C_3 Z_3(B)^{-1/6}},\qquad
C_3=3\,2^{4/3}e^{1/3}<10.551.
\tag{0.1}
\]

The identical coefficient multiplies every interval length:

\[
\Pr\{Q\in L\}\le C_3 Z_3(B)^{-1/6}|L|.
\tag{0.2}
\]

The point is not the numerical constant. The point is that **no row-volume marginal/leverage hypothesis remains**. If the third-volume law concentrates on a physical row, that row is promoted to a literal hub. If the induced two-volume law concentrates again, a second literal hub is promoted. If the remaining one-volume law concentrates, a third physical hub is promoted and exact-rank-three Plancherel closes the branch. At each promotion, the aggregate exterior volume is preserved by an exact Gram/Schur identity.

This is stronger than selecting one physical `3x3` minor and avoids the square-root probability loss. It is especially useful for rank `>3` cross blocks near a rank transition, because `Z_3` spends all three-volume and is insensitive to an arbitrarily small fourth singular value.

The unrestricted three-large-eigenvalue QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. Continuity is proved on the branch (0.1).

Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source pins actually consumed


Live correction inbox at that refresh: blob `6bdbd9987a4eefeba79d53915cfe7e232263f8ec`. In particular this proof does **not** use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, a positive conditional-density moment, or a fiber supremum.

The analytic receivers are:

1. **Audited third-volume decoupling / Theorem D**, source
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
   If the determinant-weighted third-volume row marginals of a physical cross block are all `<=1/2`, it proves
   \[
   \|p_Q\|_\infty\le 6\sqrt e\,Z_3^{-1/6},
   \tag{1.1}
   \]
   with an integrable characteristic-function envelope. Dense same-side blocks cancel only inside the valid source-coordinate decoupling.

2. **Grouped projected crossing**, source
   `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
   `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.
   Its `(GC)` theorem permits `k` literal/grouped hub directions and an `ell`-volume crossing remainder, retaining arbitrary hub functions and arbitrary light-side quadratic curvature. The two instances used below are:
   - `k=1, ell=2`:
     \[
     \|p_Q\|_\infty\le
     3\,2^{7/6}e^{1/3}M_H^{1/3}S^{-1/3}Z_2^{-1/6};
     \tag{1.2}
     \]
   - `k=2, ell=1` (no entropy exponential):
     \[
     \|p_Q\|_\infty\le
     3\,2^{5/6}M_H^{1/3}S^{-1/3}Z_1^{-1/6}.
     \tag{1.3}
     \]
   In both cases the relevant projected-volume row marginals must be `<=1/2`.

3. **Exact-rank crossing with arbitrary internal functions**, Section 1 of the same source. If a rank-three crossing has singular product `S`, and the two grouped projection densities have caps `M_X,M_Y`, then
   \[
   \|p_Q\|_\infty\le3(M_XM_Y/S)^{1/3}.
   \tag{1.4}
   \]
   For three literal physical hub coordinates, `M_X<=1`; for an arbitrary three-dimensional orthonormal projection of a cap-one product law, the source projection theorem gives `M_Y<=2^{3/2}`.

The designated fleet04/B09 partner theorem is independently recorded at
`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.
For a literal invertible physical `3x3` cross block `K` it gives
\[
\|p_Q\|_\infty\le3|\det K|^{-1/3}.
\tag{1.5}
\]
It is applied to an actual target-valid matrix in Section 8.

## 2. Exterior-volume notation

Write the rows of `B` as `b_i in R^J`, `i in I`. For each triple `R={i,j,k}` define

\[
w_R:=\det(B_RB_R^T)=\|b_i\wedge b_j\wedge b_k\|^2\ge0.
\]

Then

\[
Z_3=\sum_{|R|=3}w_R.
\]

When `Z_3>0`, let

\[
\alpha_i:=Z_3^{-1}\sum_{R\ni i}w_R.
\tag{2.1}
\]

Thus `alpha_i` are the determinant-weighted row marginals and `sum_i alpha_i=3`.

The proof recursively conditions this volume law on a selected physical row and then on a selected physical pair. No random variable is rotated.

## 3. First promotion identity: third volume to one hub plus projected two-volume

Assume some row `a` has

\[
\alpha_a>1/2.
\tag{3.1}
\]

Define its anchored third volume

\[
V_a:=\sum_{\substack{R\ni a\\|R|=3}}w_R=\alpha_a Z_3>Z_3/2.
\tag{3.2}
\]

In particular `b_a!=0`. Let `Pi_a` be orthogonal projection in `R^J` onto `span{b_a}` and, for `i!=a`, set

\[
c_i=b_i(I-\Pi_a).
\]

Let `C` be the matrix with rows `c_i`, and put

\[
Z_2(C)=e_2(CC^T)=\sum_{i<j,\ i,j\ne a}\det(C_{ij}C_{ij}^T).
\]

### Lemma 3.1

\[
\boxed{V_a=\|b_a\|_2^2 Z_2(C).}
\tag{3.3}
\]

**Proof.** For every `i,j!=a`, the Gram determinant factors after orthogonally projecting the latter two rows off `b_a`:

\[
\det\operatorname{Gram}(b_a,b_i,b_j)
=\|b_a\|_2^2\det\operatorname{Gram}(c_i,c_j).
\]

This is the Schur-complement formula for the first Gram pivot, equivalently the squared-wedge identity
`||b_a wedge b_i wedge b_j||^2=||b_a||^2||c_i wedge c_j||^2`.
Sum over unordered pairs. QED.

Let the determinant-weighted two-volume row marginals of `C` be

\[
\beta_i:=Z_2(C)^{-1}\sum_{j\ne a,i}\det\operatorname{Gram}(c_i,c_j).
\tag{3.4}
\]

If every `beta_i<=1/2`, use the **literal physical variable `X_a` as a one-dimensional hub**. Condition on all original coordinates outside the two banks. In `(GC)`, take hub `H={a}`, light split `I\setminus{a}|J`, and `M_J=b_a`. The projected crossing in `(GC)` is exactly `C`. The physical hub density cap is `M_H<=1`, the hub-to-`J` singular product is `S=||b_a||`, and (3.3) gives `S^2Z_2=V_a`. Hence

\[
\|p_Q\|_\infty
\le3\,2^{7/6}e^{1/3}V_a^{-1/6}
<3\,2^{4/3}e^{1/3}Z_3^{-1/6}.
\tag{3.5}
\]

Every coupling from `a` to the other side of its original bank remains in the hub linear map `M_I`; `(GC)` permits it. Arbitrary same-bank curvature is retained in the light polynomial.

## 4. Second promotion identity: one hub plus two-volume to two hubs plus one-volume

Suppose instead that some row `b!=a` has

\[
\beta_b>1/2.
\tag{4.1}
\]

Define the anchored pair volume

\[
V_{ab}:=\sum_{k\notin\{a,b\}}\det\operatorname{Gram}(b_a,b_b,b_k).
\tag{4.2}
\]

By (3.3)-(3.4),

\[
V_{ab}=\beta_bV_a>V_a/2>Z_3/4.
\tag{4.3}
\]

Let `B_H` be the two-row matrix `[b_a;b_b]`. Because `V_ab>0`, its rows are linearly independent. Put

\[
\Delta_{ab}:=\det(B_HB_H^T)>0,
\qquad
\Pi_{ab}:=P_{\operatorname{row}(B_H)},
\]

and for every remaining row set

\[
d_k=b_k(I-\Pi_{ab}).
\]

Let `D` have rows `d_k` and `Z_1(D)=||D||_F^2`.

### Lemma 4.1

\[
\boxed{V_{ab}=\Delta_{ab}Z_1(D).}
\tag{4.4}
\]

**Proof.** For each `k`, Schur-complementing the `2x2` Gram block of `b_a,b_b` gives

\[
\det\operatorname{Gram}(b_a,b_b,b_k)
=\Delta_{ab}\,\|b_k(I-\Pi_{ab})\|_2^2.
\]

Sum over `k`. QED.

The normalized one-volume row marginals are simply

\[
\gamma_k=\|d_k\|_2^2/Z_1(D).
\tag{4.5}
\]

If all `gamma_k<=1/2`, take the **two literal physical variables `X_a,X_b` as the hub**. Their joint product density is `<=1`, so `M_H<=1`. The hub-to-`J` singular product is

\[
S=\sqrt{\Delta_{ab}}.
\]

The projected crossing in `(GC)` is exactly `D`; by (4.4), `S^2Z_1=V_ab`. The `k=2,ell=1` receiver therefore yields

\[
\|p_Q\|_\infty
\le3\,2^{5/6}V_{ab}^{-1/6}
<3\,2^{7/6}Z_3^{-1/6}
<6.735 Z_3^{-1/6}.
\tag{4.6}
\]

Again no pair-core determinant is inverted; arbitrary internal hub curvature is absorbed into the allowed hub function.

## 5. Third promotion: a concentrated residual row gives an exact physical three-hub crossing

Finally suppose some remaining row `c` has

\[
\gamma_c>1/2.
\tag{5.1}
\]

Set

\[
V_{abc}:=\det\operatorname{Gram}(b_a,b_b,b_c).
\]

By (4.4)-(4.5),

\[
V_{abc}=\gamma_cV_{ab}>V_{ab}/2>Z_3/8.
\tag{5.2}
\]

Thus the literal three-row cross block

\[
B_{abc}=A[\{a,b,c\},J]
\]

has rank three and singular product

\[
S_{abc}=\sqrt{V_{abc}}.
\tag{5.3}
\]

Now condition on every original coordinate outside `\{a,b,c\}\cup J`. The surviving polynomial has the exact source form

\[
F(X_a,X_b,X_c)+2X_H^TB_{abc}X_J+G(X_J),
\]

with arbitrary measurable/quadratic `F,G` and affine terms included. The physical three-hub side has density cap `M_X<=1`. The orthonormal three-dimensional projection of the product `J`-bank has density cap `M_Y<=2^{3/2}`. Apply the source exact-rank crossing theorem:

\[
\|p_Q\|_\infty
\le3\left(\frac{2^{3/2}}{\sqrt{V_{abc}}}\right)^{1/3}
=3\sqrt2\,V_{abc}^{-1/6}
<6Z_3^{-1/6}.
\tag{5.4}
\]

This is the terminal branch. No fourth promotion is required because three smoothing directions make the characteristic function integrable.

## 6. Proof of the unconditional theorem

There are four exhaustive cases.

1. `max_i alpha_i<=1/2`. The audited third-volume theorem (1.1) gives
   \[
   \|p_Q\|_\infty\le6\sqrt e\,Z_3^{-1/6}
   =9.892327624\ldots Z_3^{-1/6}.
   \tag{6.1}
   \]
2. Some `alpha_a>1/2`, but all induced `beta_i<=1/2`. Equation (3.5) gives
   \[
   \|p_Q\|_\infty
   <3\,2^{4/3}e^{1/3}Z_3^{-1/6}
   =10.550168831\ldots Z_3^{-1/6}.
   \tag{6.2}
   \]
3. Some `beta_b>1/2`, but all induced `gamma_k<=1/2`. Equation (4.6) gives
   \[
   \|p_Q\|_\infty<3\,2^{7/6}Z_3^{-1/6}
   =6.734772290\ldots Z_3^{-1/6}.
   \tag{6.3}
   \]
4. Some `gamma_c>1/2`. Equation (5.4) gives
   \[
   \|p_Q\|_\infty<6Z_3^{-1/6}.
   \tag{6.4}
   \]

The maximum is the one-hub branch, exactly

\[
C_3=3\,2^{4/3}e^{1/3}=10.550168831\ldots.
\]

Each analytic receiver supplies an `L^1` characteristic-function majorant uniformly in all conditioned outside coordinates. Averaging the conditional characteristic functions preserves that majorant. Fourier inversion therefore gives a **continuous** density in every branch and the direct interval estimate (0.2). This proves (0.1).

## 7. Corollary: any balanced rank-at-most-four carrier cut is paid without a row-leverage gate

Suppose

\[
A=D+UKU^T,\qquad U^TU=I_r,\qquad r\le4,
\]

where `D` is physical diagonal and `s_3(K)>=a>0`. Let `I|J` be a literal original-coordinate partition such that

\[
U_I^TU_I\succeq\eta I_r,\qquad U_J^TU_J\succeq\eta I_r.
\tag{7.1}
\]

Then the physical cross block is

\[
B=A[I,J]=U_IKU_J^T.
\]

The min-singular-value bounds on the two frames imply

\[
s_3(B)\ge\eta s_3(K)\ge\eta a.
\tag{7.2}
\]

Consequently

\[
Z_3(B)=e_3(BB^T)\ge s_1(B)^2s_2(B)^2s_3(B)^2\ge(\eta a)^6,
\]

and the new theorem gives

\[
\boxed{\|p_Q\|_\infty\le10.551\,(\eta a)^{-1}.}
\tag{7.3}
\]

There is **no condition on the individual row leverages of `U_I`**. Thus the earlier balanced-crossing row-marginal gate is not analytically necessary once concentrated determinant mass is routed by physical-hub promotion. The remaining difficulty is purely structural: produce such a quantitatively balanced physical cut, or pay its failure by localization.

Applied to fleet03/B09 r39's nonlocalized branch, where the constructed cut has

\[
s_3(B)\ge\frac{\sqrt3}{8}\,\gamma,
\]

this improves the paid exit to

\[
\boxed{\|p_Q\|_\infty<48.730\,\gamma^{-1}},
\tag{7.4}
\]

again continuously. The finite `<=256`-coordinate localization alternative of r39 remains the current structural survivor; this run does not claim it is paid.

## 8. Designated fleet04/B09 partner applied at an actual inequality

Take `N=64`. Let `B` be the `3x64` Walsh-type matrix whose columns are

\[
N^{-1/2}(1,\chi_1(j),\chi_2(j))^T,
\]

with the four sign patterns equally represented. Its three rows are orthonormal, so

\[
BB^T=I_3,\qquad Z_3(B)=1.
\]

Form the target-valid symmetric coefficient matrix

\[
A=\begin{pmatrix}0&B\\B^T&0\end{pmatrix}.
\tag{8.1}
\]

Its nonzero spectrum is exactly

\[
\{-1,-1,-1,1,1,1\}.
\]

The third-volume row law is maximally concentrated: the left bank has exactly three rows and every row marginal equals one. The new promotion proof therefore reaches its three-hub terminal branch and gives

\[
\boxed{\|p_Q\|_\infty\le3\sqrt2=4.242640687\ldots}.
\tag{8.2}
\]

Now apply the completed designated fleet04/B09 physical-minor theorem. Choose three Walsh columns with sign patterns `(1,1)`, `(1,-1)`, and `(-1,1)`. The literal physical `3x3` cross block `K` has

\[
|\det K|=\frac4{N^{3/2}}=\frac1{128}.
\]

Therefore the partner theorem gives the actual continuous-density inequality

\[
\boxed{\|p_Q\|_\infty\le3|\det K|^{-1/3}
=\frac{3\sqrt N}{4^{1/3}}
=15.119052599\ldots.}
\tag{8.3}
\]

Both are valid. The comparison exhibits the intended mechanism: when the opposite bank is diffuse, aggregating its whole three-dimensional projection before reciprocal minor selection avoids the `sqrt(N)` deterioration of a single physical column triple.

## 9. Deterministic computation

`CHECK.py` beside this report verifies on 100 seeded random `8x7` matrices:

- `V_a=||b_a||^2 Z_2(C)`;
- `V_ab=det(B_HB_H^T) Z_1(D)`;
- `V_abc=det Gram(b_a,b_b,b_c)` after the successive determinant-weighted marginal updates.

The maximum relative errors were respectively

`8.96e-16`, `1.34e-15`, and `1.50e-15`.

For the `N=64` Walsh regression it verifies singular values `(1,1,1)`, `Z_3=1`, `|det K|=1/128`, the partner constant `15.1190525987`, and the three-hub aggregate constant `4.2426406871`. No Monte Carlo or histogram is used.

## 10. Exact remaining B09 edge

The analytic obstruction represented by a **concentrated third-volume row marginal is now removed**: it can always be promoted through at most three literal original-coordinate hubs with no loss of the aggregate `Z_3` scale beyond universal factors.

The next B09 problem is therefore

**`QFORM-R4-CARRIER-LOCALIZED-FRAME-TO-PHYSICAL-HUBS-v1`**:
start from the r39 survivor in which a rank-three/four carrier direction has more than half its squared mass on at most 256 original coordinates, and prove either

1. a quantitatively balanced cut exists and (7.3) pays it; or
2. a bounded collection of literal physical coordinates can be promoted as hubs so that the remaining crossing has positive universal-scale `Z_2`/`Z_1`; or
3. a physical diagonal/square/pair receiver pays the finite localization directly.

For the nonzero r38 residual `E`, retain it exactly inside the phase; do not discard it from a small Frobenius norm because the input laws have unbounded support and no moments.

Full QFORM: **OPEN**.  
Full-target continuity: **OPEN**.  
Continuity under `Z_3(B)>0`: **PROVED, pending independent review of this assembly**.  
Native learned-memory status: `WITHOUT_VERIFIED_BRAIN`.
