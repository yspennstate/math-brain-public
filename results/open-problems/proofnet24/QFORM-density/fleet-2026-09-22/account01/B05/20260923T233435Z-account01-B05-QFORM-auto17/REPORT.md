SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T23:34:35Z.
attacking: the punctured shared-multiplier interface by splitting off one genuinely independent transverse square and spending the orientation-free rank-two affine half-Riesz estimate before the square convolution.

# account01/B05 auto17 — a rank-two half-Riesz + independent-square bridge

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bound preserving arbitrary product densities.  
**Status:** `NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / PRECISE HARDER SOURCE-SHARING CASE ISOLATED / FULL QFORM OPEN`.  
**Regularity:** the theorem below gives a continuous density in its unconditional split-product scope; the full-target continuous-density conclusion remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. First essential implication

The immediately preceding B05 run isolated `QFORM-SHARED-MULTIPLIER-CONVOLUTION-LIFT-v1`: in a model core

`2 t H L + 2 b L P + lambda V^2 + alpha L^2 + affine`,

the endpoint `b=0` is controlled, every fixed `b!=0` is controlled by the two-bank tube theorem, but a generic same-source proof loses a reciprocal power of `b`. The question is whether the puncture is caused by the algebraic shear `2bLP`, by the `alpha L^2` pivot, or by source-sharing of the third curvature direction.

This run proves that **neither the shear nor the `L^2` pivot causes the puncture whenever one transverse square is carried by a disjoint product bank**. The correct mechanism is to spend the entire rank-two quadratic core at the half-Riesz level before convolving with the independent square. The resulting estimate is completely uniform in `b`, including `b=0`, and completely uniform in `alpha`.

The surviving hard case is correspondingly sharper: the third square curvature must share original-coordinate source with the multiplier/shear bank, so that the final square convolution is not independent.

## 2. Main theorem: rank-two half-Riesz plus an independent square

### Theorem — `QFORM-RANK2-INDEPENDENT-SQUARE-BRIDGE-v1`

Let `X_I=(X_i)_{i in I}` and `X_J=(X_j)_{j in J}` be disjoint subcollections of independent real variables with density caps at most one. Let

`R(X_I)=X_I^T B X_I + d^T X_I + c`,

where `B` is real symmetric of rank exactly two. Let its two nonzero eigenvalues be `mu_1,mu_2` and put

`D=|mu_1 mu_2|>0`.

Let

`W=sum_{j in J} w_j X_j`, `sum_j w_j^2=1`,

and let `s` be arbitrary. For `lambda!=0`, define

`Q = R(X_I) + lambda (W+s)^2`.                                      (2.1)

Then Q has an essentially bounded density and

`boxed{ ||p_Q||_(infinity,ess) <= 128 sqrt(2) D^(-1/4)|lambda|^(-1/2). }`   (2.2)

More generally, if the density of W is bounded by `K_W`, then

`boxed{ ||p_Q||_(infinity,ess) <= 128 K_W D^(-1/4)|lambda|^(-1/2). }`      (2.3)

No support, moment, connected-support, Gaussian, log-concavity, or rotated-coordinate independence hypothesis is used.

Moreover, in the unconditional split form (2.1), Q has a **continuous** density. This continuity statement is only for this branch; full-target continuity remains unproved.

### Proof

The completed orientation-free rank-two theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` gives, for every real `a`,

`E |R-a|^(-1/2) <= 128 D^(-1/4).`                                  (2.4)

This theorem permits an arbitrary original-coordinate affine vector d, so conditioning elsewhere does not require the affine term to lie in the rank-two spectral range.

The standard one-dimensional bounded-density projection theorem gives

`||p_W||_infinity <= sqrt(2)`                                      (2.5)

for the normalized linear form W. Keep a general cap `K_W` for the calculation.

Let `Y=lambda(W+s)^2`. For `lambda>0`, the change of variables through the two square roots gives, for `y>0`,

`p_Y(y)
 = [p_W(-s+sqrt(y/lambda))+p_W(-s-sqrt(y/lambda))]/(2 sqrt(lambda y))
 <= K_W/(sqrt(lambda) sqrt(y)).`                                  (2.6)

For `lambda<0`, reflect Y. Thus in both signs,

`p_Y(y) <= K_W |lambda|^(-1/2)|y|^(-1/2) 1_{lambda y>0}.`          (2.7)

Because the I and J source banks are disjoint, R and Y are genuinely independent. Therefore the convolution formula is valid even before knowing a density for R:

`p_Q(q)=int p_Y(q-r) mu_R(dr)`,                                   (2.8)

and (2.7) gives

`p_Q(q)
 <= K_W |lambda|^(-1/2)
    E[ |q-R|^(-1/2) ]
 <=128 K_W D^(-1/4)|lambda|^(-1/2).`                              (2.9)

This proves (2.3), and (2.2) follows from (2.5).

For continuity in the unconditional split form: the map `x -> R(x)` has gradient `2Bx+d`. Since `rank(B)=2`, its critical set is either empty or an affine subspace of codimension two and hence has Lebesgue measure zero. Localizing to balls and applying coarea shows that the pushforward of the absolutely continuous product law under R is absolutely continuous. Write its density as `p_R in L^1`. We already have `p_Y in L^1`. Hence

`p_Q=p_R*p_Y`

has a continuous representative vanishing at infinity by the standard `L^1*L^1 subset C_0` theorem. QED.

## 3. Shared multiplier corollary: the shear and L-square pivot are harmless after a 2+1 product split

Let H be one original coordinate, independent of a disjoint product bank carrying linear forms L and P and of a second disjoint product bank carrying V. Normalize

`||u||_2=1`, `L=u^T X`,

and write `P=p^T X` on the same bank as L. Assume the coefficient vector p has no H component, as is automatic from the disjoint source split. Consider

`R=2tHL + alpha L^2 + 2bLP + d^T X_I + c`, `t!=0`.                 (3.1)

The quadratic part of R is

`B_R = u s^T+s u^T+alpha u u^T`, `s=t h+b p`,                     (3.2)

where h is the unit physical direction of H and `h perpendicular u,p`.

Decompose

`p=(u^T p)u+p_perp`, `p_perp perpendicular u`.

In the orthonormal basis `(h,u,p_perp/||p_perp||)` (omitting the last vector if `p_perp=0`), the only nonzero spectral block has characteristic polynomial

`z^2-(alpha+2b u^T p)z-[t^2+b^2||p_perp||^2]`.                     (3.3)

Hence its two nonzero eigenvalues satisfy the exact determinant identity

`boxed{ D_R=|mu_1 mu_2|=t^2+b^2||p_perp||^2 >= t^2. }`             (3.4)

In particular, the determinant currency is independent of the magnitude and sign of alpha and never deteriorates as `b->0`.

Let V be a normalized scalar projection of the disjoint J-bank and let `lambda!=0`. Applying Theorem 2 gives

`boxed{
 ||p_{R+lambda(V+s)^2}||_(infinity,ess)
 <=128 sqrt(2) |t|^(-1/2)|lambda|^(-1/2).
}`                                                                    (3.5)

Thus **both** the punctured shear and the nonzero `L^2` pivot are uniformly paid whenever the third square is genuinely independent of the rank-two source bank.

If V itself is one original cap-one coordinate, replace `sqrt(2)` by one in (3.5).

## 4. Exact-target family, uniform through the puncture

Take H,L,P,V to be orthonormal linear coordinates carried by mutually appropriate disjoint product banks so that V is independent of `(H,L,P)`, and set

`Q_b=2tHL+2bLP+lambda V^2`,                                         (4.1)

with `|t|>=1`, `|lambda|>=1`.

In the orthonormal basis `(H,L,P,V)`, the homogeneous matrix is

`[[0,t,0,0],
  [t,0,b,0],
  [0,b,0,0],
  [0,0,0,lambda]].`                                                (4.2)

Its spectrum is

`boxed{ {+sqrt(t^2+b^2), -sqrt(t^2+b^2), 0, lambda}. }`             (4.3)

Therefore every b, including arbitrarily small nonzero b and b=0, is a valid three-large-eigenvalue instance. Equation (3.5) yields

`||p_{Q_b}||_(infinity,ess) <=128 sqrt(2) <181.020`                 (4.4)

at target normalization `|t|,|lambda|>=1`, uniformly in b and in all admissible rough product laws.

Because this isolated family has no arbitrary outside affine term, the sharper in-range constant `16 sqrt(30)` from the rank-two source theorem may be used, giving

`||p_{Q_b}||_(infinity,ess) <=16 sqrt(60)<123.936`                  (4.5)

when W uses the universal `sqrt(2)` projection cap.

This is a genuine rotated target family; no spectral coordinate is declared independent except where the original-coordinate source split actually makes it so.

## 5. Required partner theorem applied to an actual inequality

The designated account02/B05 result `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` states that if H is independent of a pair `(L,V)` of joint-density cap M, H has cap m, and

`Q_0=2HL+aL^2+2cLV+lambda V^2+dL+eV+f`,

then

`||p_{Q_0}||_(infinity,ess)
 <=7.761982175235 (Mm)^(2/3)|lambda|^(-1/3).`                       (5.1)

Apply this to the **actual puncture endpoint** `b=0` after scaling `H' = tH`. If H has cap one, then `H'` has cap `m<=|t|^(-1)`. If `(L,V)` is an orthonormal two-dimensional product projection, the completed two-dimensional projection estimate used in the partner report gives `M<=2`. Hence

`boxed{
 ||p_{Q_0}||_(infinity,ess)
 <= 7.761982175235 * 2^(2/3)|t|^(-2/3)|lambda|^(-1/3)
 <12.322 |t|^(-2/3)|lambda|^(-1/3).
}`                                                                    (5.2)

At target normalization this is `<12.322`.

This partner application is complementary to the new theorem: (5.2) allows L and V to share a product source at the exact `b=0` endpoint, while Sections 2-4 allow arbitrary b and arbitrary `alpha L^2` once V is carried by a disjoint source bank.

Therefore the remaining puncture is no longer correctly described as merely `b->0`. It is the conjunction

`b!=0` **and** `V shares original-coordinate source with the multiplier/shear bank`.

That is the factor which prevents either the endpoint partner theorem or the independent-square convolution from applying directly.

## 6. Precise remaining implication

The next unpaid statement is

`QFORM-SHARED-THIRD-CURVATURE-HALF-RIESZ-LIFT-v1`:

> For the core `2tHL+2bLP+alpha L^2+lambda V^2+affine`, preserve the original product source when V is not independent of `(L,P)`, and combine the rank-two half-Riesz currency of `2tHL+2bLP+alpha L^2` with the shared square before taking any conditional fiber supremum. The estimate must be uniform for all nonzero b and persist as `b->0`, with no moment/support assumptions.

A proof that simply conditions on V loses the half-Riesz smoothing; a proof that first takes an arbitrary joint density of the rank-two output and V is invalid by the live arbitrary-joint coarea corrections. The missing operation must aggregate the common product bank before the singular square kernel is paid.

Geometrically, this says the difficult branch is not a loss of rank-two curvature: (3.4) keeps `D_R>=t^2`. It is a **dependence problem at the final half-Riesz-to-density convolution interface**.

## 7. Relation to current corrections

This proof does not use pointwise van-der-Corput decay, unrestricted joint-density coarea, conditional projection caps, moment bounds, compact support, or post-rotation independence. The sole independence used in Theorem 2 is an actual disjoint original-coordinate bank split. The rank-two source theorem was read at its complete proof source and no live correction located in the current correction inbox refutes its stated exact rank-two affine half-Riesz scope.

The full QFORM conjecture is still OPEN. No claim is made that every target matrix admits the 2+1 product split of Section 2. The full continuous-density conclusion is also OPEN, although continuity is proved for the unconditional split branch here.

## 8. Sources actually used

2. Orientation-free half-Riesz source: `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`.
3. Required designated-partner source: account02/B05 `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`, canonical report `yspennstate/math-open-problems@e7a21ed67b943d7aded714ac17ca48bdab4a1349:proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T200516Z-account02-B05-QFORM-auto11c/REPORT.md`.
4. Immediate B05 predecessor: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T205421Z-account01-B05-QFORM-auto16/REPORT.md`.
5. Fresh live correction inbox consumed through the 23 September corrections including the nonzero-square affine-slope and indefinite-innovation warnings; neither challenges the exact rank-two affine theorem used here.

## 9. Scope

**Proved this run:** a uniform bounded-density theorem for a rank-two quadratic-plus-arbitrary-affine block convolved with a genuinely independent normalized square; exact determinant identity `D_R=t^2+b^2||p_perp||^2`; uniform removal of both `b->0` and `alpha L^2` losses in the disjoint-square branch; a target-valid family with three large eigenvalues controlled uniformly in b; continuity in the unconditional split-product branch.

**Applied from account02/B05:** the null-hub theorem gives the explicit `<12.322` endpoint bound when `b=0` and `(L,V)` may share a product source.

**Not proved:** the shared-third-curvature `b!=0` branch, a universal reduction to the 2+1 split, unrestricted full QFORM, or full-target continuity.

Manual changed-file review found only mathematical text, public bibliographic/source identifiers, repository paths, and nonsecret run metadata. No credentials, personal archives, financial/client material, or unrelated content were introduced. No external secret-scanner executable was invoked.
