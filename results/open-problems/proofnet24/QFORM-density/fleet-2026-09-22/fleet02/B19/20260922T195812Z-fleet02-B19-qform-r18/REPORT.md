SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-22T19:58:12.929167Z.
attacking: the scalar-Schur half-Riesz endpoint — eliminate the affine/singular interface exactly and pay the disjoint aggregate two-square S2 endpoint without selecting a local minor.

# fleet02/B19 — normalized Schur half-Riesz core and aggregate two-square payment

**Run:** `20260922T195812Z-fleet02-B19-qform-r18`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Owner control used before publication:** revision `2026-09-22.15`, fresh brain main observed at `dfa756b132f50fef8a9132eb5478bebf9daf30d5`.  
**Classification:** `ESSENTIAL_STEP_APPLIED`; full target OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction discipline

The target remains: for arbitrary independent real coordinates with one-dimensional densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `Q=X^TAX`, or give a valid target counterexample.

This report uses no moment/support/log-concavity hypothesis, no post-rotation independence, no arbitrary-joint rank-three coarea cap, no positive conditional projection-density moment, no law-uniform pointwise quadratic oscillatory decay, and no inference of one fixed physical minor from an aggregate exterior bank. In particular it preserves the live corrections against single-Schur rank-two extraction, same-square one-heavy-row absorption, and near-zero-diagonal half-Riesz substitution.

## 2. Source-pinned inputs actually used

1. **Incoming fleet02/B19 r17 scalar-Schur reduction.** Canonical report readable at `yspennstate/math-open-problems@fc8343c379bbddf14be670349f664f7fcb39994a`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260922T192830Z-fleet02-B19-qform-r17/REPORT.md`, blob `e99359e8d98f04fc1a1d5388e2f5a6000127fbc4`. It proves that any nonzero physical scalar pivot of a target parent has exact Schur residual `S` with `s_2(S)>=1`, gives the S0/S1/S2 physical-overlap trichotomy, pays diffuse S0, and refutes selecting one principal pair from the S2 aggregate.

2. **Current named partner fleet03/B19 r17.** Canonical `yspennstate/math-open-problems@9989e8640c2933ba54cd8de88723ac5c223be3b1`. Its exact three-heavy-row theorem closes every O0 state with at least three `3/4`-heavy rows. Therefore only the at-most-two-heavy O0 branch reaches the incoming B19 scalar-Schur machinery.

3. **Orientation-free rank-two affine half-Riesz theorem.** Canonical `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, claim `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`: for independent cap-one inputs and an invertible two-dimensional quadratic coefficient `Lambda`,

`sup_t E|Q_2+affine-t|^(-1/2) <=128 |det Lambda|^(-1/4)`.

4. **One-dimensional product projection cap.** The incoming r17 source pins the completed projection theorem at `yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`; a unit linear form in an original-coordinate product bank has density cap at most `sqrt(e)`.

5. **New compatible fleet03/B07 colored-exterior result.** Canonical `yspennstate/math-open-problems@4ee3cfb2d6682d5be670819cf5de173ad859f6cf`. Applied to r17's exact Schur S0 resource `e_2(BB^T)>=1/48`, it extracts four original-coordinate banks with matching-block squared-Frobenius product at least `1/768` and rainbow second-minor mass at least `1/192`. I use this only at that exact structural scope; it is not converted into a fictitious fixed minor.

## 3. First new theorem: affine and singular residuals cost nothing

For a symmetric matrix `S` and product vector `Z`, write

`H(S,ell,c):=sup_t E|Z^T S Z+ell^T Z+c-t|^(-1/2)`.

### Theorem 3.1 — `QFORM-SCHUR-HALFRIESZ-NORMAL-FORM-v1`

The following two statements have the same best universal constant `C`.

**(A)** For every finite dimension, every **invertible** real symmetric `T` with `s_2(T)=1`, and every independent cap-one product vector `Y`,

`sup_t E|Y^T T Y-t|^(-1/2) <= C`.                              (3.1)

**(B)** For every finite dimension, every real symmetric `S` with `s_2(S)>=1`, every independent cap-one product vector `Z`, every affine vector `ell` and constant `c`,

`H(S,ell,c)<=C`.                                                (3.2)

Thus the affine term, an exact nullspace, and the scale `s_2(S)>1` are not separate debts in the incoming r17 implication.

#### Proof

(B) trivially implies (A). Assume (A). Choose a sequence `eps_m ->0` for which

`S_m=S+eps_m I`

is invertible; only finitely many forbidden values occur. Let

`sigma_m=s_2(S_m)`.

By continuity of singular values, `sigma_m -> s_2(S)>=1`. Define

`T_m=S_m/sigma_m`,

so `T_m` is invertible and `s_2(T_m)=1` exactly.

For arbitrary `ell`, put

`h_m=(1/2) S_m^(-1) ell`.

Then the exact physical-coordinate identity is

`Z^T S_m Z+ell^T Z+c
 =(Z+h_m)^T S_m (Z+h_m)+c-h_m^T S_m h_m`.             (3.3)

The translated vector `Z+h_m` still has independent coordinates and the same density caps; no rotation has occurred. Therefore (A), scaling by `sigma_m`, and the harmless translation of the scalar target give, for every `t`,

`E|Z^T S_m Z+ell^T Z+c-t|^(-1/2)
 <= C sigma_m^(-1/2)`.                                         (3.4)

Pointwise in `Z`, the inside of (3.4) converges to the corresponding expression with `S`. Fatou's lemma gives

`E|Z^T S Z+ell^T Z+c-t|^(-1/2)
 <= C s_2(S)^(-1/2) <= C`.                                     (3.5)

Taking the supremum over `t` proves (B). QED.

**Consequence.** The incoming open implication `QFORM-SCHUR-S2-AGGREGATE-HALFRIESZ-v1` may henceforth be attacked in the strict normal form

`S invertible,  s_2(S)=1,  ell=0, c=0`,                         (3.6)

without any loss in the eventual universal constant. This eliminates the tempting but unnecessary nullspace-conditioning interface, where conditional projection caps are known to fail.

## 4. Second new theorem: disjoint aggregate square channels are fully paid

The incoming S2 counterexample shows that a collective principal-pair bank can be perfectly healthy even while every coordinate-pair determinant tends to zero. Its correct endpoint is aggregation, not reciprocal minor selection.

### Theorem 4.1 — `QFORM-DISJOINT-AGGREGATE-TWO-SQUARE-v1`

Let `Y,Z,W` be mutually independent, where the scalar random variables `Y,Z` have densities bounded by `M_Y,M_Z`. Let `h(W),k(W),c(W)` be arbitrary measurable functions and let `alpha,beta` be nonzero. Put

`R=alpha (Y+h(W))^2 + beta (Z+k(W))^2 + c(W)`.                  (4.1)

Then, for arbitrary signs,

`sup_t E|R-t|^(-1/2)
 <=128 (M_Y M_Z)^(1/2) |alpha beta|^(-1/4)`.                    (4.2)

If `alpha beta>0`, the sharper self-contained bound is

`sup_t E|R-t|^(-1/2)
 <=2 sqrt(2 pi) (M_Y M_Z)^(1/2) |alpha beta|^(-1/4)`.           (4.3)

#### Proof of the arbitrary-sign bound

Condition on `W=w`. The shifts and constant are now deterministic and `Y,Z` remain independent. Rescale

`Y'=M_Y Y`, `Z'=M_Z Z`.

Their densities are bounded by one. The conditioned quadratic is an invertible rank-two diagonal form with coefficients `alpha/M_Y^2` and `beta/M_Z^2`, plus an arbitrary affine term. Applying the source-pinned orientation-free rank-two theorem gives

`128 |alpha beta/(M_Y^2 M_Z^2)|^(-1/4)
 =128 (M_YM_Z)^(1/2)|alpha beta|^(-1/4)`.

The bound is uniform in `w`; averaging proves (4.2).

#### Proof of the same-sign improvement

After reflection assume both coefficients are positive. Set

`u=sqrt(alpha)(Y+h(w))`, `v=sqrt(beta)(Z+k(w))`.

The joint density of `(u,v)` is a probability density bounded by

`M=(M_YM_Z)/sqrt(alpha beta)`.

For any scalar `s`, set `K_s(u,v)=|u^2+v^2-s|^(-1/2)`. For every `lambda>0`,

`area{K_s>lambda}
 = area{|u^2+v^2-s|<lambda^(-2)}
 <=2 pi lambda^(-2)`.                                          (4.4)

Hence

`P(K_s>lambda)<=min(1,2 pi M lambda^(-2))`.

Layer cake at `lambda_0=sqrt(2 pi M)` yields

`E K_s <= lambda_0 + integral_(lambda_0)^infty 2 pi M lambda^(-2) d lambda
 =2 sqrt(2 pi M)`.                                             (4.5)

This is (4.3), uniformly in `w`; average over `W`. QED.

### Corollary 4.2 — original-coordinate grouped channels

If `Y=u^T X_U` and `Z=v^T X_V` are unit linear forms on disjoint original-coordinate banks, the completed product-projection theorem gives `M_Y,M_Z<=sqrt(e)`. Therefore

`H_(1/2)(R) <=128 sqrt(e)|alpha beta|^(-1/4)`                   (4.6)

for arbitrary signs, and

`H_(1/2)(R) <=2 sqrt(2 pi e)|alpha beta|^(-1/4)
 =8.265462708244986... |alpha beta|^(-1/4)`                     (4.7)

for equal signs.

If an additional independent physical scalar pivot gives

`Q=a(X_i+g)^2+R`,

then the standard scalar-square transducer immediately gives

`||p_Q||_infinity
 <= |a|^(-1/2) H_(1/2)(R)`.                                    (4.8)

This theorem permits arbitrary `W`-dependent shifts and arbitrary residual `c(W)`; it does not condition a rotated spectral coordinate and does not delete hidden curvature in the active banks.

## 5. The r17 S2 adversary is now paid at the exact missing half-Riesz level

Recall r17's family

`S_m = direct_sum_(r=1)^m J_m/m`, `m>=3`,                       (5.1)

which has `s_2(S_m)=1`, S2 principal-pair bank `(m-1)/(2m)>=1/3`, but every physical pair determinant at most `1/m^2`.

For block `r`, write

`Y_r=m^(-1/2) sum_j X_(r,j)`.

Different `Y_r` use disjoint original-coordinate banks and are independent; each has density cap at most `sqrt(e)`. Choosing the first two blocks in Theorem 4.1 with `alpha=beta=1` and absorbing all remaining block squares into `c(W)` gives the dimension-free exact statement

`boxed(H_(1/2)(Z^T S_m Z) <=2 sqrt(2 pi e)<8.266.)`             (5.2)

Thus the source-valid S2 adversary remains a refutation of the one-pair selector, but it is **not** an obstruction to the aggregate half-Riesz programme. For the target parent `[1] direct_sum S_m`, (4.8) gives density `<8.266` directly.

This is stronger than merely observing bounded density by convolving two square laws: it pays exactly the fractional potential required by the scalar-Schur route.

## 6. Application of new compatible peer work

The newest compatible fleet03/B07 theorem is applied to the incoming S0 branch rather than treated as background. From r17's exact physical cross resource

`e_2(BB^T)>=1/48`,

it produces four disjoint original-coordinate matching banks with

`||B[L_1,R_sigma(1)]||_F^2 ||B[L_2,R_sigma(2)]||_F^2 >=1/768`,  (6.1)

and rainbow second-minor mass at least `1/192`. This improves the structural description of high-leverage S0. It does **not** yet give a density or half-Riesz bound in the presence of arbitrary self blocks; no reciprocal coordinate minor is inferred from (6.1).

The current named partner fleet03/B19 r17 remains applied upstream: its three-heavy-row closure is what reduces O0 to the at-most-two-heavy branch before the B19 r16/r17 scalar-Schur analysis. Missing newer partner work is not assumed.

## 7. Compact conditional end-to-end proof map

A correction-safe current route is now:

1. Apply the completed low-offdiagonal/ridge/third-compound reductions at their exact source scopes.
2. In O0, use the current named partner fleet03/B19 r17 to pay every state with at least three `3/4`-heavy rows.
3. In the remaining at-most-two-heavy O0 branch, use B19 r16 and r17 to reach a genuine nonzero physical scalar pivot when available and form its exact Schur residual `S`; then `s_2(S)>=1`.
4. Use r17's exhaustive S0/S1/S2 overlap reduction. Diffuse S0 is already paid. Fleet03/B07 now supplies the stronger matching-bank currency (6.1) inside the remaining S0 branch. True curvature-free S1 affine-hyperbolic packets are paid by their source theorem; hidden curvature is retained otherwise.
5. For the residual half-Riesz obligation, Theorem 3.1 removes all affine, singular, and scale bookkeeping: it is enough to prove the homogeneous normalized invertible core (3.6).
6. In S2, whenever two disjoint aggregate rank-one square channels are exposed, Theorem 4.1 pays them with no local-minor loss. In particular the exact r17 one-pair adversary (5.1) is now fully paid at the needed half-Riesz level.
7. What remains is an aggregate transducer for the normalized invertible core in high-leverage S0, curved S1, and genuinely coupled S2, together with the no-usable-scalar-pivot parent branches already tracked by the global synthesis.

## 8. First unpaid implication after this run

`QFORM-HOMOGENEOUS-INVERTIBLE-AGGREGATE-HALFRIESZ-v1` (OPEN):

> There is a universal finite `C_H` such that for every finite `d`, every **invertible** real symmetric `S` with `s_2(S)=1`, and every independent real product vector `Z=(Z_1,...,Z_d)` whose coordinate densities are bounded by one,
>
> `sup_t E|Z^T S Z-t|^(-1/2) <= C_H`.                           (8.1)

By Theorem 3.1, (8.1) is **equivalent with the same constant** to the full affine/singular residual implication used in r17. The first structural content still missing is therefore not nullspace conditioning or affine translation: it is the genuinely coupled aggregate payment inside the normalized invertible core.

At the current source state, the unpaid subcases can be named without hiding any correction:

- high-leverage S0 after the `1/48` exterior bank and the new `1/768` matching-bank extraction;
- curved S1 after excluding the source-valid affine-hyperbolic packets;
- collective S2 after excluding exact disjoint aggregate two-square packets paid by Theorem 4.1.

A proof of (8.1), combined with the existing scalar-pivot transducer, closes every target state having a usable physical scalar pivot. The complementary all-small/no-usable-diagonal parent remains the separate high-offdiagonal/zero-self branch; it is not silently absorbed here.

## 9. Status

- `QFORM-SCHUR-HALFRIESZ-NORMAL-FORM-v1`: **PROVED**.
- `QFORM-DISJOINT-AGGREGATE-TWO-SQUARE-v1`: **PROVED**.
- r17 block-rank-one S2 adversary: **PAID at half-Riesz level**, bound `<8.266`.
- fleet03/B07 S0 matching-bank result: **APPLIED at exact source scope**.
- `QFORM-HOMOGENEOUS-INVERTIBLE-AGGREGATE-HALFRIESZ-v1`: **OPEN**.
- Full three-large-eigenvalue QFORM target: **OPEN / NOT PROVED / NOT DISPROVED**.
- No continuity claim is made from the new half-Riesz statements alone.

A small verifier beside this report checks only the displayed constants, the affine-completion identity, singular-value continuity sanity, and the finite `S_m` arithmetic. It is not used as proof of any universal assertion.
