SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-22T19:46:03Z.
attacking: two-eigenvalue half-Riesz synthesis and the exact zero-physical-pivot one-cross branch inside the bilinear-block mechanism.

# fleet01/B09 r16 — zero-pivot one-cross and two-eigenvalue half-Riesz closure

**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Live owner control at derivation/publication:** revision `2026-09-22.15`; sole target QFORM.

## 1. Target and what changes in this run

The full target remains open: for every dimension, independent real physical coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a single dimension-free bound on the density of `X^T A X`, or produce a valid counterexample. Continuity is a separate desired conclusion.

This run attacks the first still-unpaid B09/Schur geometry: after a scalar physical pivot has been completed, the residual may have two large spectral directions but only one visibly strong physical cross direction. Fleet03/B09 r15 pays a residual with a second physical pivot of size at least `1/2` or a two-singular-direction cross bank, but leaves a one-strong-cross branch. The exact-zero-pivot endpoint of that branch is paid here. The same calculation combines with the one-scale ridge theorem to give a uniform half-Riesz estimate for every **hollow** residual with two large eigenvalues, arbitrary rank, arbitrary signs, arbitrary extra spectrum and arbitrary affine term.

No pointwise van-der-Corput estimate, post-rotation independence, arbitrary-joint coarea theorem, conditional spectral-density moment, or fiber-supremum step is used.

## 2. Source-pinned inputs actually consumed

1. **One-scale ridge characteristic estimate.** `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`. In its notation, for an original-coordinate cross block `B`, `gamma>0`, `q in [1,2]`,

   `K_gamma = BB^T (gamma^2 I + BB^T)^(-1)`, `theta=tr K_gamma`, `D=det(I+BB^T/gamma^2)`,

   and if `max_i (K_gamma)_ii <= q/2`, then

   `|phi(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`,

   with `L_q=pi e sqrt(2/q)`. The report proves this while allowing arbitrary self blocks and affine/coordinate-separable perturbations. I use this inequality below at `q=1`, but only require a half-Riesz weighted time integral, so the threshold becomes `theta>1`, not the density threshold `theta>2`.

2. **Designated partner fleet02/B09 r7.** `QFORM-RANK3-BILINEAR-SCHUR-BANK-v1`, canonical `yspennstate/math-open-problems@caa2cef304844e9d6f841acaf2e003f0bc1c24b5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T183809Z-fleet02-B09-QFORM-r7/REPORT.md`. For an exact-rank-three zero-diagonal matrix and an edge `(i,j)`, with

   `R_ij = |A_ij|^2 sum_{k != i,j} |A_ik A_jk|`,

   it proves

   `||p_Q||_infinity <= 2^(5/4) sqrt(15) R_ij^(-1/4)`.

   I convert this actual density inequality into a half-Riesz payment in Section 7.

3. **Current neighboring gap.** fleet03/B09 r15, `yspennstate/math-open-problems@2589a6230149bd8c3b4b2a0aad6f404bc7ab034a`, proves a uniform half-Riesz bound when a residual with `s_2>=1` has a physical diagonal at least `1/2`, and another when a physical cross block has two singular values bounded below. It identifies the remaining one-strong-cross geometry.

4. **Concurrent compatible result.** fleet03/B04 r17, `yspennstate/math-open-problems@77c5654ee92f27e444b650ee1635c868af5f76c9`, proves a scalar-square plus invertible rank-two banked-Schur half-Riesz closure. Its remaining hard branch explicitly includes a zero/near-isotropic scalar pivot with rank-deficient residual bank. The theorem below addresses the exact-zero physical-pivot endpoint of that residual geometry rather than duplicating the invertible rank-two bank packet.

The live correction ledger was reread before publication. In particular the proof respects `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE`, the false arbitrary-joint coarea claim, the false positive conditional-projection moment, and the false law-uniform pointwise Fresnel decay.

## 3. Two elementary rearrangement facts

For a real random variable `Z` with density bounded by `M` and total mass one,

`sup_t E |Z-t|^(-1/2) <= 2 sqrt(2M)`.                                      (3.1)

Indeed the decreasing kernel `|x-t|^(-1/2)` is maximized under the constraints `0<=p<=M`, `int p=1`, by filling the centered interval of length `1/M`; hence

`M int_{-1/(2M)}^{1/(2M)} |x|^(-1/2) dx = 2 sqrt(2M)`.

We also use the standard one-dimensional product-projection bound already used in the designated partner's proof: if `Y_j` are independent with densities at most one and `b != 0`, then

`||p_{b dot Y}||_infinity <= sqrt(2)/||b||_2`.                              (3.2)

Translations do not change this cap.

## 4. Exact zero-pivot one-cross half-Riesz theorem

Define

`H_(1/2)(F) = sup_t E |F-t|^(-1/2)`.

### Theorem 4.1 — `QFORM-HALFRIESZ-ZEROPIVOT-ONECROSS-v1`

Let `X` be a scalar and `Y=(Y_1,...,Y_m)` a disjoint original-coordinate product bank; all coordinates are independent and have densities at most one. Let `b in R^m`, `b != 0`, `beta in R`, and let `R(Y)` be an arbitrary measurable real function finite almost surely. Then

`F = 2 X (b dot Y + beta) + R(Y)`

satisfies

`boxed: H_(1/2)(F) <= 2^(11/4) ||b||_2^(-1/2).`                           (4.1)

No restriction is placed on the quadratic or nonquadratic complexity hidden in `R(Y)`.

### Proof

Condition on `Y` and put `L=b dot Y+beta`. For `L != 0`,

`E_X |2 L X + R(Y)-t|^(-1/2)`
` = (2|L|)^(-1/2) E_X |X-x_0|^(-1/2)`
` <= 2 |L|^(-1/2)`,                                                        (4.2)

where (3.1) was used with `M=1`. The exceptional event `L=0` has probability zero because `L` has a density. By (3.2), `L` has density cap

`M_L <= sqrt(2)/||b||_2`.

Applying (3.1) again,

`E |L|^(-1/2) <= 2 sqrt(2 M_L)`.

Combining with (4.2),

`H_(1/2)(F) <= 4 sqrt(2 M_L)`
` <= 4 sqrt(2 sqrt(2)/||b||_2)`
` = 2^(11/4)||b||_2^(-1/2)`.

This proves (4.1). QED.

### Why exact zero matters

If the physical scalar has a nonzero square coefficient, arbitrary same-bank curvature can cancel into a single square; fleet02/B09's correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` gives precisely this obstruction. The theorem therefore makes no unsupported near-zero extension.

## 5. Two-large-eigenvalue diffuse half-Riesz theorem

The one-scale ridge proof used three large cross directions to make the characteristic function itself integrable. A half-Riesz potential needs only

`int_0^infinity t^(-1/2)|phi(t)| dt < infinity`,

so **two** cross directions suffice.

### Theorem 5.1 — `QFORM-TWOEIG-RIDGE-HALFRIESZ-v1`

Let `S` be real symmetric with at least two eigenvalues of modulus at least one. Let `P` be its spectral projection onto all eigenspaces with `|lambda(S)|>=1/64`. Assume

`max_i P_ii <= 1/32`.                                                       (5.1)

For independent cap-one physical coordinates `Y`, every affine perturbation `b^T Y+c`, and

`F=Y^T S Y+b^T Y+c`,

one has

`boxed: H_(1/2)(F) < 25.46 < 26.`                                           (5.2)

### Proof

Repeat the spectral-window partition from the source-pinned ridge report. The MSS two-part partition of the high spectral frame gives disjoint physical banks `I,J` with both restricted Gram matrices between `7I/32` and `25I/32`. Because the high spectral part now has **at least two** singular values at least one, the high cross block has

`s_2(B_0)>=7/32`.

The discarded tail has operator norm at most `1/64`, so the full cross block `B=S[I,J]` has

`s_2(B)>=sigma=7/32-1/64=13/64`.                                            (5.3)

Exactly as in the ridge report, `range(B_0)=range(U_I)` has row leverage at most `1/7`. Set

`gamma=sigma/sqrt(6)=13/(64 sqrt(6))`.

The ridge perturbation estimate gives

`max_i (K_gamma)_ii <= (1/sqrt(7)+sqrt(6)/13)^2 < 1/2`.                     (5.4)

With `q=1`, the two singular values in (5.3) give

`theta=tr K_gamma >= 2*(6/7)=12/7`.

Put `beta=theta/2>=6/7`. Equation (5.4) of the source-pinned ridge report yields

`|phi_F(t)| <= min(1,(t_0/|t|)^beta)`,                                     (5.5)

where

`t_0 = [L_1/(2 gamma)] D^(-1/(2theta))`, `L_1=pi e sqrt(2)`.

Since `log D>=theta`,

`t_0 <= pi sqrt(2e)/(2 gamma) = 32 pi sqrt(12e)/13.                         (5.6)

The Riesz kernel identity, justified by Abel regularization because the right side below is absolutely integrable, gives

`E|F-x|^(-1/2)`
` <= sqrt(2/pi) int_0^infinity t^(-1/2)|phi_F(t)| dt`.                      (5.7)

Using (5.5),

`int_0^infinity t^(-1/2) min(1,(t_0/t)^beta) dt`
` = sqrt(t_0) [2+1/(beta-1/2)]`
` <= (24/5) sqrt(t_0)`.                                                     (5.8)

Substitution of (5.6) into (5.7)-(5.8) gives

`sqrt(2/pi)*(24/5)*sqrt(32 pi sqrt(12e)/13) = 25.452384... <25.46`.

This proves (5.2). QED.

The theorem is a genuine two-eigenvalue fractional-trace statement; it does not assert a bounded density for a two-large-eigenvalue quadratic form.

## 6. Arbitrary-rank hollow residual is paid

### Theorem 6.1 — `QFORM-HOLLOW-TWOEIG-HALFRIESZ-v1`

Let `S` be any real symmetric matrix satisfying

`S_ii=0` for every physical coordinate `i`,                                  (6.1)

and having at least two eigenvalues of modulus at least one. For independent cap-one physical coordinates and every affine perturbation,

`F=Y^T S Y+b^T Y+c`,

one has

`boxed: H_(1/2)(F) <=128.`                                                   (6.2)

The rank of `S` is arbitrary; extra eigenvalues may be numerous, small or large, positive or negative.

### Proof

Let `P` be the `|lambda|>=1/64` spectral projection.

**Diffuse high window.** If `max_i P_ii<=1/32`, Theorem 5.1 gives the stronger `<26` bound.

**Heavy high-window coordinate.** Otherwise choose `i` with `P_ii>1/32`. Because `S_ii=0`, write

`F=2Y_i (b_i dot Y_{-i}+beta_i)+R(Y_{-i})`,

where `b_i=(S_ij)_{j != i}` and the affine coefficient of `Y_i` is absorbed into `beta_i`. Spectrally,

`||b_i||_2^2 = ||S e_i||_2^2`
` = sum_alpha lambda_alpha^2 |u_alpha(i)|^2`
` >= (1/64)^2 P_ii > 2^(-17)`.                                              (6.3)

Thus `||b_i||_2>2^(-17/2)`. Theorem 4.1 gives

`H_(1/2)(F) < 2^(11/4) 2^(17/4)=2^7=128`.

This proves (6.2). QED.

A slightly broader routing statement is immediate: the same conclusion holds whenever either the high spectral window is diffuse as in (5.1), or there exists a high-leverage physical coordinate `i` with `S_ii=0`. Hollowness is only the clean exhaustive special case.

## 7. Density consequence after one outer physical square

Let a full quadratic form be written after completing one **original physical scalar pivot** as

`Q = a (X_0+m(Y))^2 + Y^T S Y + b^T Y+c`,                                  (7.1)

where `a!=0`, `X_0` is independent of the remaining original-coordinate product bank `Y`, and the translation `m(Y)` may depend arbitrarily on `Y`. For fixed `Y`, the density kernel of `a(X_0+m(Y))^2` is bounded by

`|a|^(-1/2)|u|^(-1/2)`.

Therefore

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(Y^T S Y+b^T Y+c)`.                  (7.2)

Consequently, if `S` is hollow and has two eigenvalues of modulus at least one,

`boxed: ||p_Q||_infinity <=128 |a|^(-1/2).`                                (7.3)

Every interval `I` then satisfies

`P(Q in I) <=128 |a|^(-1/2)|I|`.                                           (7.4)

At the current heavy-pivot threshold `|a|>=157/320`, this is `<182.75 |I|`. This theorem establishes an essentially bounded density; continuity is not asserted by this endpoint.

## 8. Designated-partner theorem applied to an actual half-Riesz inequality

For the exact-rank-three zero-diagonal branch of fleet02/B09 r7, define

`R_ij=|A_ij|^2 sum_{k!=i,j}|A_ik A_jk|`.

The partner theorem gives the density cap

`M = 2^(5/4)sqrt(15) R_ij^(-1/4)`.

Applying the exact rearrangement inequality (3.1) to this **actual partner output** yields

`boxed: H_(1/2)(X^TAX) <= 2^(17/8) 15^(1/4) R_ij^(-1/8).`                  (8.1)

Thus if such an exact-rank-three zero-diagonal block appears as an independent Schur residual beneath an outer physical square with coefficient `a`, the square-kernel argument gives

`||p_Q||_infinity <= 2^(17/8) 15^(1/4)|a|^(-1/2) R_ij^(-1/8)`.             (8.2)

This is weaker in the aggregate exponent than the partner's direct density theorem when no outer square is needed, but it is the correct fractional-trace quantity for the scalar-Schur synthesis and is an explicit application rather than a citation-only dependency.

As a control, on the partner's clone-bank family `R_12=1`, (8.1) is dimension-free; the direct partner density remains the sharper `<9.212` endpoint.

## 9. Compact conditional end-to-end routing and the first unpaid implication

For a scalar-pivot route to the full target, the current conditional chain is now:

1. complete a genuine original-coordinate scalar pivot;
2. if the two-large-direction Schur residual has diffuse `|lambda|>=1/64` projection, Theorem 5.1 pays its half-Riesz trace;
3. if it has a heavy coordinate with a diagonal at least `1/2`, fleet03/B09 r15 pays it;
4. if it has a high-leverage coordinate whose diagonal is exactly zero, Theorem 4.1 pays it; in particular every hollow residual is paid by Theorem 6.1;
5. if it has two quantitative cross singular directions, fleet03/B09 r15 pays it;
6. rank-two invertible grouped residual packets coupled to the outer square are additionally paid by fleet03/B04 r17.

The **first unpaid implication** is therefore narrower:

`QFORM-SMALL-NONZERO-HIGHPIVOT-HALFRIESZ-v1` — control the residual with `s_2(S)>=1` when its high spectral window is concentrated, every usable high-leverage physical diagonal is **strictly nonzero but <1/2**, and no two-direction cross bank or invertible grouped residual packet of bounded reciprocal cost is available. The exact-zero endpoint is now closed, but it cannot be extended to small nonzero diagonals by continuity: the same-square cancellation correction shows that arbitrary same-bank curvature can turn a nonzero scalar square plus one cross direction into a single square and recover a logarithmic half-Riesz divergence.

The zero/near-zero **outer** pivot and the exhaustive global extraction of a suitable scalar/grouped/ridge packet also remain separate debts. Therefore this report does not promote full QFORM proof status.

## 10. Integrity/status

- Full conjecture: `OPEN`.
- New Theorem 4.1: proved from product-projection/rearrangement only.
- New Theorem 5.1: proved by an explicit two-eigenvalue adaptation of the source-pinned ridge characteristic estimate.
- New Theorem 6.1 and density corollary: proved from Theorems 4.1 and 5.1.
- Designated partner fleet02/B09 r7: consumed and quantitatively applied in (8.1)-(8.2).
- Essential boundedness: proved in the stated scalar-pivot/hollow-residual scope.
- Continuity: not claimed for the new density endpoint.
- Privacy/provenance: only mathematical programme sources were used; no credentials, scheduler IDs, machine paths, email, Drive, public release, paid model/API/Codex, permission expansion or unrelated private data were used.
- Native brain ingestion: not verified; repository retrieval/synchronization is recorded separately, so execution remains `WITHOUT_VERIFIED_BRAIN`.
