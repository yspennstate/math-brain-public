SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T00:03:55Z.
attacking: singleton-heavy-hub plus two-bank aggregate state: convert the fixed-hub exterior packet into an exact bordered principal-volume identity and identify the correct nonlocal payment interface.

# B10 rank-three coupled case — bordered hub volume identity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T000355Z-account01-B10-QFORM-r21`  
Status: `ESSENTIAL_STEP_APPLIED / NEW_EXACT_BORDERED_VOLUME_IDENTITY / METHOD_BARRIER / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full arbitrary exact-rank-three theorem is **not proved** in this report. The contribution is an exact structural reduction of the surviving singleton-heavy-hub/two-bank state, together with a dimension-free aggregate physical certificate obtained by applying the newest designated account02/B10 theorem. The report also identifies two proof architectures that cannot pay this state without a genuinely new bordered/grouped estimate.

## 1. Source state and designated partner theorem

The designated partner is account02/B10 run `20260922T225540Z-account02-B10-QFORM-auto11`, canonical source

`yspennstate/math-open-problems@9005415f079b7b46c0618c0187bf29b3f8d44167`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T225540Z-account02-B10-QFORM-auto11/REPORT.md`.

Its heavy-hub delete-or-isolate theorem begins with a normalized exact-rank-three core and, in the near-unit heavy-hub alternative, conditions away the other rows of the hub bank and retains an active set

`{h} union B_2 union B_3`.

After whitening this active set, one has rows `r_i in R^3` and a symmetric invertible spectral matrix `N` such that

`sum_i r_i r_i^T = I_3`,

`|det N| >= 2^(-18)`, `sigma_min(N) >= 2^(-18)`,

and a fixed-hub exterior packet

`T_h := sum_(j in B_2,k in B_3) det(r_h,r_j,r_k)^2 >= 1/512`.

The whitened hub remains heavy; writing `L=||r_h||^2`, one has `L>511/512`. The physical active quadratic block is

`A_active = R N R^T`,

where the `i`th row of `R` is `r_i^T`. Conditioning the already-deleted original coordinates produces only affine terms and does not change this active quadratic block.

The only use of whitening here is deterministic spectral geometry. No claim is made that spectral coordinates are independent. All random variables remain the original independent physical coordinates indexed by the active rows.

## 2. Exact transverse packet identity

Rotate only the deterministic spectral basis so that

`r_h = sqrt(L) e_1`.

For every other active row write

`r_i = a_i e_1 + w_i`, `w_i in e_1^perp ~= R^2`.

Parseval gives the exact identities

`sum_(i != h) a_i^2 = 1-L`,

`sum_(i != h) a_i w_i = 0`,

`sum_(i != h) w_i w_i^T = I_2`.

Define the transverse bank Grams

`S_2 = sum_(j in B_2) w_j w_j^T`,

`S_3 = sum_(k in B_3) w_k w_k^T`.

Then

`S_2+S_3=I_2`.

In particular `S_2` and `S_3` commute and may be simultaneously diagonalized. If the eigenvalues of `S_2` are `lambda,mu`, those of `S_3` are `1-lambda,1-mu`.

For every `j,k`,

`det(r_h,r_j,r_k)^2 = L det(w_j,w_k)^2`.

The standard two-dimensional Cauchy--Binet identity gives

`sum_(j,k) det(w_j,w_k)^2 = tr(adj(S_2) S_3)`.

Since `S_3=I_2-S_2`,

`tr(adj(S_2)S_3)
 = lambda(1-mu)+mu(1-lambda)
 = 1-det S_2-det S_3`.

Hence the fixed-hub packet has the exact form

`T_h = L tr(adj(S_2)S_3)
     = L(1-det S_2-det S_3).`                    (2.1)

This is `QFORM-HUB-TRANSVERSE-PACKET-IDENTITY-v1`.

Consequences include

`1-det S_2-det S_3 >= 1/(512 L) >= 1/512`,

and at least one of the two complementary transverse products obeys

`lambda(1-mu) >= 1/(1024 L)`

or

`mu(1-lambda) >= 1/(1024 L)`.

Thus the unpaid hub state carries quantitatively complementary transverse mass in the two disjoint original-coordinate banks. It is not merely a statement that some individual physical row is large.

## 3. Exact bordered principal-volume identity

For each pair `j in B_2`, `k in B_3`, let

`T={h,j,k}`

and let `R_T` be the square matrix with those three rows. Since

`A[T,T]=R_T N R_T^T`,

taking determinants gives exactly

`det A[T,T] = det(N) det(R_T)^2
            = det(N) det(r_h,r_j,r_k)^2`.          (3.1)

Every nonzero determinant on the left therefore has the **same sign**, namely `sign(det N)`. Summing (3.1) and applying the designated partner bounds gives the actual dimension-free inequality

`sum_(j in B_2,k in B_3) |det A[{h,j,k},{h,j,k}]|
 = |det N| T_h
 >= 2^(-18) * 2^(-9)
 = 2^(-27).`                                      (3.2)

This is `QFORM-SINGLETON-HUB-BORDERED-VOLUME-v1`.

Equation (3.2) is the main new payment-ready certificate from this run. It is genuinely aggregate: the partner's exact target family shows that every individual principal triple can tend to zero while the sum in (3.2) stays bounded below.

## 4. Expanded bordered mixed-discriminant identity

Write the active physical matrix in the block order `h | B_2 | B_3`:

`A = [[a, beta_2^T, beta_3^T],
      [beta_2, C_22, C_23],
      [beta_3, C_23^T, C_33]].`

For one pair `(j,k)`, expansion of its principal `3x3` determinant gives

`det A_{hjk}
 = a(A_jj A_kk-A_jk^2)
   - A_hj^2 A_kk
   - A_hk^2 A_jj
   + 2 A_hj A_hk A_jk`.

Summing over `j in B_2,k in B_3` yields the exact identity

`det(N) T_h
 = a[(tr C_22)(tr C_33)-||C_23||_F^2]
   - ||beta_2||_2^2 tr C_33
   - ||beta_3||_2^2 tr C_22
   + 2 beta_2^T C_23 beta_3.`                    (4.1)

Combining with (3.2), the absolute value of the right side is at least `2^(-27)`. Consequently one of the four aggregate mechanisms on the right must have fixed size. More precisely, at least one of

`|a| |(tr C_22)(tr C_33)-||C_23||_F^2| >= 2^(-29)`,

`||beta_2||_2^2 |tr C_33| >= 2^(-29)`,

`||beta_3||_2^2 |tr C_22| >= 2^(-29)`,

`|beta_2^T C_23 beta_3| >= 2^(-30)`

holds. This is only an algebraic dichotomy; no density conclusion is being asserted from those four inequalities separately.

The important feature of (4.1) is that it retains the correct three-way interaction: hub edges, transverse self-curvature, and cross-bank curvature. None of those pieces may safely be replaced by a single local scalar coefficient.

## 5. Pivot versus aggregate hub-edge energy

There is a second exact identity which is useful for routing the hub.

Let

`a=A_hh=r_h^T N r_h`,

`beta_i=A_hi=r_h^T N r_i`, `i != h`.

Parseval gives

`sum_(i != h) beta_i^2
 = r_h^T N (I-r_h r_h^T) N r_h
 = r_h^T N^2 r_h-a^2`.                            (5.1)

Since `sigma_min(N)>=s:=2^(-18)`,

`sum_(i != h) beta_i^2 >= s^2 L-a^2`.              (5.2)

Hence either

`|a| >= (s sqrt(L))/2`,

in which case the already-established physical-pivot rank-three theorem gives a finite universal payment

`||p_Q||_infinity
 <= 128 [L |a| |det N|]^(-1/4)
 <= 128 [2^(-37) L^(3/2)]^(-1/4)`,                (5.3)

or else

`||(beta_i)_(i != h)||_2
 >= (sqrt(3)/2) s sqrt(L)
 > (sqrt(3)/2) 2^(-18) sqrt(511/512).`             (5.4)

Thus the truly unpaid state may be taken to have a tiny hub pivot but a **dimension-free aggregate hub-edge norm**. Again, (5.4) is an aggregate bank statement; it does not force one physical edge to be large.

## 6. Two exact method barriers

### 6.1 A `B_2 x B_3` cross-block theorem alone cannot close the hub state

The designated account02/B10 report provides an exact Parseval family with

`N=[[0,1,0],[1,0,0],[0,0,1]]`,

one near-unit `e_1` hub, bank `B_2` split into many tiny `e_1` and `e_2` rows, and bank `B_3` split into many tiny `e_3` rows. In that family the fixed-hub packet stays order one, while every individual local pivot/pair/triple tends to zero.

For that same family,

`A[B_2,B_3]=0`

identically: `N e_3=e_3`, whereas every `B_2` row lies in `span(e_1,e_2)`. Therefore **no payment depending only on singular values or minors of the cross block `A[B_2,B_3]` can be exhaustive**, even though the bordered packet (3.2) is uniformly nonzero.

The missing theorem has to combine hub--bank coupling with curvature from the other bank (or its symmetric counterpart).

### 6.2 The existing weighted D' theorem cannot be applied naively to a packet sharing one hub

The current weighted D' theorem for disjoint `3x3` cross minors requires the physical-row marginals on one side to be `<3/4`. A principal-triple packet in which every triple contains the same hub has hub marginal exactly one, so its hypotheses fail.

More structurally, replaying the same scalar Hausdorff--Young/BL exponent bookkeeping would require `q/alpha_h >=2`; with `alpha_h=1`, this forces `q>=2`. The resulting three-volume time exponent is at most

`3/(2q) <= 3/4`,

which is not `L^1(dt)`. This does **not** refute a new bordered D' theorem. It proves that the current symmetric weighted-D' architecture cannot simply be reused without treating the hub by a different one-dimensional mechanism.

## 7. Compatibility with the newest grouped-square theorem

The newest account04/B01 grouped-square theorem pays exact decompositions into disjoint original-coordinate scalar innovations and, for a same-sign pair, gives a continuous density bound

`2 pi /(sigma_j sigma_k sqrt(|lambda_j lambda_k|))`.

That theorem confirms the right philosophy: aggregate first, then smooth by independent grouped innovations. The singleton-hub state above is not yet in its hypotheses, because the two bank projections generally overlap internally with the longitudinal hub leakage. Regression may produce independent residual scalar innovations only in special zero-Schur-defect subbranches already handled by earlier B10 work. Therefore this run does not claim a new application of the grouped-square theorem to the whole hub chamber.

## 8. First unpaid implication

The remaining analytic step is now more precise than `whole-bank bilinear/Fresnel`:

`QFORM-BORDERED-DPRIME-HUB-HYPERBOLIC-v1`.

A sufficient theorem would take a singleton original coordinate `X_h` and two disjoint independent original-coordinate banks, assume a lower bound on the **aggregate bordered principal-volume packet**

`sum_(j,k) |det A_{hjk}|`,

with the rank-three physical block generated by a Parseval frame, and prove a universal density bound while allowing arbitrary same-bank quadratic curvature and affine terms. The hub must be treated by a scalar hyperbolic/half-Riesz or equivalent one-dimensional smoothing step, while the two remaining determinant slots are aggregated before any reciprocal local coefficient is introduced.

Equation (4.1) gives the exact algebraic interface for such a theorem. The designated partner family proves why a theorem using only `A[B_2,B_3]` cannot suffice; the marginal-one calculation proves why the current weighted D' theorem cannot simply be invoked unchanged.

## 9. Status and regularity

- New identities (2.1), (3.1)--(3.2), (4.1), and (5.1)--(5.4): proved exactly in this report.
- Designated partner result actually applied: account02/B10 `auto11`, producing the explicit new inequality (3.2), `sum |det A_hjk| >=2^(-27)`.
- Large-hub-pivot subbranch: paid by the existing physical-pivot theorem as in (5.3).
- Small-hub-pivot singleton/two-bank aggregate branch: still open.
- Full exact-rank-three target: OPEN / NOT PROVED / NOT DISPROVED.
- Full owner QFORM conjecture: OPEN / NOT PROVED / NOT DISPROVED.
- Continuity: no new continuity statement is proved for the unpaid hub branch in this report.

No pointwise law-uniform Fresnel decay, post-rotation independence, fiber supremum, positive conditional-density moment, or uniformly good local minor is used.
