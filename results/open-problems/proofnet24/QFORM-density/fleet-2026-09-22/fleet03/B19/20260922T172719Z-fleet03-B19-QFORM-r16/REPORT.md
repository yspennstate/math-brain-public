# fleet03/B19 QFORM r16 — exact cross-bank Fourier payment

## Status and scope

Programme: `QFORM-DENSITY-3EIG-20260922` under fresh owner control revision `2026-09-22.8`.

Worker: `fleet03/B19`, universal proof assembly.  Execution remains `WITHOUT_VERIFIED_BRAIN`; repository synchronization is not a claim of native learned-memory ingestion.

Full target: for independent real coordinates with densities `0<=f_i<=1` and symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for `X^T A X`, or produce a counterexample.

**Outcome of this run:** `ESSENTIAL_STEP_APPLIED / O0-ANALYTIC-PAYMENT-STRENGTHENED / FULL_TARGET_OPEN`.

The new theorem below is a product-preserving analytic payment for an original-coordinate cross bank.  It is not a reduction showing that every target matrix has such a bank with a universal determinant.  The aggregate-to-local passage remains structural and is explicitly not inferred from third-compound mass alone.

Continuity: the new cross-bank branches below give a bounded **continuous** density.  This does not establish continuity in all remaining branches of the full conjecture.

---

## 1. Source state used

The live third-compound reduction of fleet03/B07 gives an O0 alternative consisting of a disjoint original-coordinate cross block `B=A[L,R]` with

`e_3(BB^T) >= 1/256`,

but the live correction forbids turning this aggregate identity into one dimension-free good physical `3 x 3` minor without an additional localization argument.

The current ridge theorem pays the diffuse-leverage part of O0, while fleet01/B07's heavy-core factorization leaves a finite physical row core plus a projected residual determinant packet.  The missing analytic question is therefore what one may do once an honest finite cross bank (or exact-rank cross bank) is available, without post-rotation independence or a scalar quadratic-phase estimate.

I also consume the completed fleet02/B06 theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`: if `R` has orthonormal columns and `Y=R^T X` for independent cap-one coordinates, then the `k`-dimensional projection density satisfies

`||p_Y||_infinity <= exp(k/2)`.

This is a fiber-integral Brascamp--Lieb statement, not a forbidden fiber supremum.

The designated partner fleet04/B19 result `QFORM-FINITE-UNION-CORE-v1` is applied in Section 5 to transfer the actual interval inequality from bounded finite-union indicator inputs to arbitrary cap-one product densities with no loss.  A direct arbitrary-law proof is also included, so the partner use is not standing in for a missing analytic step.

---

## 2. Main theorem: exact-rank cross-bank mixed-Hessian payment

### Theorem 2.1 (`QFORM-EXACT-CROSS-RANK-L2-v1`)

Let `I,J` be disjoint sets of original coordinates.  Put `U=X_I`, `V=X_J`, and condition on every coordinate outside `I union J`.  The conditional quadratic form has the exact shape

`Q_w(U,V)=F_w(U)+2 U^T C V+G_w(V)+c_w`,

where `C=A[I,J]`; `F_w,G_w` are arbitrary real quadratic-affine functions produced by the conditioned coordinates.  The laws of `U,V` remain independent products of cap-one densities.

Assume `rank(C)=r>=3`, with nonzero singular values `sigma_1,...,sigma_r`, and write

`Pi_r(C)=prod_{j=1}^r sigma_j`.

Then `Q=X^TAX` has a bounded continuous density and

`||p_Q||_infinity <= e * r/(r-2) * Pi_r(C)^(-1/r)`.        (2.1)

If one of the active banks consists of exactly `r` original coordinates and `C` has full row/column rank there, the factor `e` improves to `sqrt(e)`:

`||p_Q||_infinity <= sqrt(e) * r/(r-2) * Pi_r(C)^(-1/r)`. (2.2)

If both active banks consist of exactly `r` original coordinates, so `C` is an invertible physical `r x r` cross minor, then

`||p_Q||_infinity <= r/(r-2) * |det C|^(-1/r)`.          (2.3)

In particular, for any two disjoint physical triples `I,J`,

`det A[I,J] != 0  =>  ||p_Q||_infinity <= 3 |det A[I,J]|^(-1/3)`.  (2.4)

All estimates are uniform in the conditioned outside coordinates, all within-bank quadratic terms, all affine shifts, all signs, all extra spectrum, and all cap-one marginal laws.

### Proof

Fix an outside value `w` for which the regular conditional expression exists.  First prove the general exact-rank statement.  Take a thin singular-value decomposition

`C=P Sigma R^T`,

where `P` and `R` have `r` orthonormal columns and `Sigma=diag(sigma_1,...,sigma_r)`.

Set

`Y=P^T U`, `Z=R^T V`.

Let `p_Y,p_Z` be their densities.  By `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`,

`||p_Y||_infinity <= exp(r/2)`, `||p_Z||_infinity <= exp(r/2)`.   (2.5)

Disintegrate the two product laws over `Y` and `Z`.  For every real `t`, define the complex fiber amplitudes

`a_{t,w}(y)=p_Y(y) E[ exp(i t F_w(U)) | Y=y ]`,

`b_{t,w}(z)=p_Z(z) E[ exp(i t G_w(V)) | Z=z ]`.

They obey the pointwise bounds

`|a_{t,w}(y)|<=p_Y(y)`, `|b_{t,w}(z)|<=p_Z(z)`.

Since each marginal has mass one,

`||a_{t,w}||_2 <= ||p_Y||_2 <= ||p_Y||_infinity^(1/2) <= exp(r/4)`,

and likewise `||b_{t,w}||_2<=exp(r/4)`.  Thus

`||a_{t,w}||_2 ||b_{t,w}||_2 <= exp(r/2)`.               (2.6)

The conditional characteristic function is exactly

`phi_w(t)=exp(i t c_w) int int a_{t,w}(y) b_{t,w}(z)
                     exp(2 i t y^T Sigma z) dy dz`.      (2.7)

No residual mixed term is hidden in the fibers: all nonzero singular directions of the active cross bank were retained.  This is why the theorem is stated for an exact-rank active bank; one may not simply discard additional nonzero cross directions in (2.7).

Use the Fourier convention

`hat b(xi)=int exp(i xi dot z) b(z) dz`.

For `t!=0`, the inner integral in (2.7) is `hat b_{t,w}(2t Sigma y)`.  Cauchy--Schwarz, the change of variables `xi=2t Sigma y`, and Plancherel give

`|phi_w(t)|
 <= ||a_{t,w}||_2 ||hat b_{t,w}(2t Sigma .)||_2
 =  ||a_{t,w}||_2 (2|t|)^(-r/2) Pi_r(C)^(-1/2)
      ||hat b_{t,w}||_2
 =  pi^(r/2) |t|^(-r/2) Pi_r(C)^(-1/2)
      ||a_{t,w}||_2 ||b_{t,w}||_2`.

Together with (2.6),

`|phi_w(t)| <= (pi e)^(r/2) |t|^(-r/2) Pi_r(C)^(-1/2)`.  (2.8)

Also `|phi_w(t)|<=1`.  Averaging in the outside coordinates preserves the same pointwise majorant for the unconditional characteristic function `phi_Q`, so

`|phi_Q(t)| <= min(1, A |t|^(-r/2))`,

where

`A=(pi e)^(r/2) Pi_r(C)^(-1/2)`.                         (2.9)

Because `r>2`, this majorant is integrable.  Put

`t_0=A^(2/r)=pi e Pi_r(C)^(-1/r)`.

An exact one-dimensional integration gives

`int_R min(1,A|t|^(-r/2)) dt
 = 2 [ t_0 + A int_{t_0}^infinity t^(-r/2) dt ]
 = 2 t_0 * r/(r-2)`.                                    (2.10)

Fourier inversion therefore yields a continuous density and

`||p_Q||_infinity
 <= (1/(2pi)) ||phi_Q||_1
 <= e * r/(r-2) * Pi_r(C)^(-1/r)`,

proving (2.1).

For (2.2), suppose, say, `|I|=r`.  Then `P` is a square orthogonal matrix on the physical `U` bank.  The joint density of `U` is `prod_{i in I} f_i`, has `L^infinity` norm at most one, and orthogonal change of variables preserves this cap.  Hence the first bound in (2.5) improves from `exp(r/2)` to `1`; only the `Z` projection pays `exp(r/2)`.  Thus the product of the two `L^2` amplitude norms in (2.6) is at most `exp(r/4)`.  Repeating (2.8)--(2.10) replaces `e` by `sqrt(e)`.

For (2.3), both `P` and `R` are square orthogonal changes on `r` physical coordinates, so both marginal caps in (2.5) improve to one.  Then

`|phi_Q(t)| <= min(1, pi^(r/2)|det C|^(-1/2)|t|^(-r/2))`.

The same exact integration gives (2.3).  The case `r=3` is (2.4).  QED.

### Why this does not contradict the live three-cross-direction warning

The direct `L^2` factorization uses **all** mixed directions in the active bank.  If a large global cross block has rank greater than three, projecting to only its top three singular directions leaves residual cross terms coupling the two fibers, so (2.7) is no longer valid.  Thus three large singular values of an arbitrary higher-rank global cross block are not silently treated as an exact rank-three bank.  A physical `3 x 3` subbank is legitimate because all coordinates outside those six variables are conditioned, turning their couplings into affine terms rather than residual active cross terms.

---

## 3. O0 consequence and exact rank-three endpoint

The fleet03/B07 O0 alternative provides a disjoint cross block `B=A[L,R]` with

`e_3(BB^T)>=1/256`.                                         (3.1)

If this O0 block has **exact rank three**, then its three nonzero singular values obey

`Pi_3(B)^2=e_3(BB^T)>=1/256`, hence `Pi_3(B)>=1/16`.

The general exact-rank theorem (2.1) therefore gives the target-level bound

`||p_Q||_infinity <= 3 e * 16^(1/3) < 20.549`.             (3.2)

So an O0 survivor can no longer be an exact-rank-three cross bank, regardless of its orientation, self blocks, affine shifts, outside couplings, or marginal shapes.  This is a genuine closure of a current target-level branch.

More generally, whenever the structural machinery localizes a physical disjoint `3 x 3` minor of magnitude at least `delta`, (2.4) immediately pays it with

`||p_Q||_infinity <= 3 delta^(-1/3)`.                       (3.3)

Equation (3.3) is an analytic payment only.  The correction `QFORM-CROSSMINOR-ALONE-FALSE` is retained: (3.1) by itself does not yield a dimension-free `delta` for one physical minor.

---

## 4. Splice into the finite heavy-core factorization

Fleet01/B07 proves the following exact heavy-core factorization on the ridge-heavy O0 residue.  At a calibrated scale `gamma`, a finite physical heavy row set `H` has size at most four, and for some nonempty `T subset H`, writing `C=H^c`,

`gamma^(-2|T|) det(B_T B_T^T)
 * det(I_C + gamma^(-2) B_C P_T^perp B_C^T) >= e^3/16`.   (4.1)

Let

`r=|T|`,
`D_res=det(I_C + gamma^(-2) B_C P_T^perp B_C^T)`.

When `r` is 3 or 4, `B_T` has exact row rank `r` and one active bank consists of exactly `r` physical coordinates.  The one-sided version (2.2) gives

`||p_Q||_infinity <= sqrt(e) * r/(r-2)
                     * det(B_T B_T^T)^(-1/(2r))`.          (4.2)

Combining (4.1) and (4.2) gives the exact quantitative splice: for every `M>=1`, either

`D_res > M`,                                                   (4.3)

or

`det(B_T B_T^T)^(1/2)
 >= gamma^r e^(3/2)/(4 sqrt(M))`,                              (4.4)

and hence

`||p_Q||_infinity
 <= sqrt(e) * r/(r-2) * gamma^(-1)
    * (4 sqrt(M)/e^(3/2))^(1/r)`.                              (4.5)

Thus the `r=3,4` heavy-core branch is no longer an unstructured finite-core payment problem.  It reduces sharply to a **scale/residual determinant** issue: either the physical core itself is paid by (4.5), or a large regularized determinant is forced into the projected residual bank.  No tiny principal minor, conditional spectral cap, or post-rotation independence is invoked.

If `r<=2`, (2.2) is deliberately not claimed: the mixed-Hessian Fourier tail is `|t|^{-r/2}` and is not integrable at infinity for `r<=2`.  Those cases are exactly where a genuinely additional residual direction or a different grouped mechanism is still required.

---

## 5. Designated-partner application

The designated partner fleet04/B19 proved `QFORM-FINITE-UNION-CORE-v1`: for each fixed measurable quadratic-form concentration problem under independent density caps one, the concentration supremum over arbitrary cap-one product densities equals the supremum over products of indicators of bounded finite unions of intervals, each of measure one.

Apply that theorem to the actual interval inequality supplied by (2.3).  On every finite-union core and every outside conditioning,

`P{Q in K} <= [r/(r-2)] |det A[I,J]|^(-1/r) |K|`            (5.1)

for disjoint physical `r`-sets with invertible cross block.  The partner theorem transfers (5.1), **with the same coefficient and no localization/fragment loss**, to all arbitrary independent cap-one marginal densities.  In particular the physical-triple certificate is exactly

`P{Q in K} <= 3 |det A[I,J]|^(-1/3) |K|`.                  (5.2)

The direct characteristic-function proof above independently establishes the same arbitrary-law scope and additionally yields continuity.  The partner application is therefore a genuine no-loss extremal transfer of the actual new inequality, not a citation without use.

---

## 6. Compact conditional proof map after this run

A current full-proof assembly can be organized as follows.

1. The already-proved low-offdiagonal normal-form branch pays `s_2(A-diag A)<1/2` with a universal constant once a fixed margin from `1/2` is specified; the current B19 threshold `499/1000` has an explicit bound `<84`.
2. In the remaining high-offdiagonal regime, the third-compound identity gives O0/O1/O2/O3 overlap packets.
3. O0 diffuse-leverage states are paid by the completed ridge-window theorem.
4. **New in this run:** any O0 state that localizes an exact-rank `r>=3` active cross bank is paid by Theorem 2.1; in particular exact-rank-three O0 is paid by (3.2), and every honest physical `3 x 3` cross minor has the sharp local certificate (3.3).
5. In the ridge-heavy O0 finite-core factorization, the `|T|=3,4` cases now reduce by (4.3)--(4.5) to the projected-residual determinant/scale branch.  The analytically hard finite core itself is no longer the obstacle there.
6. O1 singular hyperbolic packets, O2 bordered-polynomial packets, O3 aggregate principal triples, and the O0 `|T|<=2` / large-residual-determinant splice remain to be assembled without reciprocal tiny-minor selection.

This is not a full theorem: no step above turns aggregate third-compound mass into one uniformly large local cross determinant, and the correction evidence explicitly forbids making that inference.

---

## 7. First unpaid implication after the new payment

`QFORM-O0-HEAVY-RESIDUAL-DETERMINANT-SPLICE-v1`:

> In the O0 ridge-heavy state with the fleet01/B07 factorization (4.1), pay the surviving cases `|T|<=2`, or `D_res` large / `gamma` small, by coupling the at-most-two physical heavy directions to a residual ridge/grouped bank while preserving the original product law.  Equivalently, prove that the forced residual determinant packet yields either a diffuse ridge gate, a third source-realizable mixed direction that upgrades the active bank to the integrable `r>=3` theorem above, or a previously paid grouped-square/physical-pivot branch.

The exact-rank-three endpoint is no longer part of this debt.  A successful splice here would close the O0 heavy branch and leave the O1/O2/O3 aggregate branches as the next overlap obligations.

---

## 8. Corrections and forbidden shortcuts explicitly retained

- No law-uniform pointwise quadratic van-der-Corput/Fresnel decay is used.
- No general rotation is claimed to preserve coordinate independence.
- No bounded-density projection theorem is used to control an indefinite quadratic pushforward by itself.
- No unrestricted fiber supremum is used; the only projection input is the proved weighted fiber-integral Brascamp--Lieb bound.
- No one-good-minor conclusion is inferred from aggregate minor mass.
- No Monte Carlo or finite checker is used as proof.
- Extra spectrum, repeated eigenvalues, arbitrary signs, arbitrary supports, and arbitrary affine shifts survive the theorem.

Full QFORM status: **OPEN**.
