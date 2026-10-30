SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T14:38:33Z.
attacking: the degenerate physical-pair endpoint left by r33 — replace the determinant blow-up at a rank-one principal pair by an exact parabolic-fiber integral in the original two physical product coordinates, and pay the surviving reciprocal singularity with the true product-projection law of the light bank.

# fleet01/B06 r34 — weighted parabolic fibers at a rank-one physical pair

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREMS_PROVED / RANKONE-DEGENERATE-PAIR-ENDPOINT-CLOSED / FULL_TARGET_OPEN`.

The full arbitrary-dimensional quadratic-form bounded-density conjecture is **not** proved or disproved here. The new result is a mechanism change from r33's determinant-only nondegenerate physical-pair estimate: r33 becomes singular as a physical `2 x 2` principal block approaches rank one; this run treats the **exact rank-one endpoint** directly and also proves the exact zero-quadratic two-row bilinear endpoint. The estimates keep the original product factors inside the curved integration. No spectral-coordinate independence is used.

Global continuity is **not** proved. The new conclusions are essential-density bounds. Execution label remains `WITHOUT_VERIFIED_BRAIN`: repository transport was used, but no authenticated native learned-memory retrieval plus receiver use was established.

## 1. Fresh controls and completed inputs actually used


- no law-uniform pointwise quadratic-phase decay from a density cap;
- no independence after rotating to spectral or other linear coordinates;
- no use of an unrestricted fiber supremum whose integral grows with dimension;
- a bounded projection density alone does not control an arbitrary indefinite quadratic pushforward;
- no inference of a uniformly good individual physical minor from aggregate determinant mass.

Two completed fleet02/B06 inputs are used at equation level.

1. `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.
   If `P` has `k` orthonormal rows and `Z` has independent cap-one coordinates, then

   `||p_(P Z)||_infinity <= exp(k/2)`.

   In particular a normalized scalar projection has density cap `sqrt(e)` and a normalized planar projection has density cap `e`.

2. The latest fleet02/B06 hub compiler,
   `yspennstate/math-open-problems@328a550b1ddde3d2d9b7c2d245678f0b6fd5e7ae`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260923T105551Z-182f201f81de/REPORT.md`, gives in its exact-rank-three heavy-star survivor

   `either ||p_Q||_infinity < 1447/s,
    or ||A_(i,L)||_2 >= s/(16 sqrt(2)) for every heavy i`.

   The new endpoint below is intended for the latter robust-light geometry when a physical pair compression becomes singular; it does not reopen the already-paid branch.

The immediate own predecessor is fleet01/B06 r33,
`yspennstate/math-open-problems@ababe93762d210413fe9f19389e3b45f5dd150ba`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260923T130129Z-fleet01-B06-QFORM/REPORT.md`.
Its determinant-only quarter-Riesz theorem pays every **invertible indefinite** physical pair, but its factor `|det B|^(-3/8)` necessarily diverges at `rank(B)=1`. This run attacks that endpoint directly rather than pretending the determinant estimate is stable there.

## 2. One-dimensional quadratic pullback lemma

### Lemma 2.1 — exact pullback bound

Let `f` be a probability density on `R` with `0<=f<=1`. For real `A!=0,B,C`,

`boxed:
 int_R f(A s^2+B s+C) ds <= 2 / sqrt(|A|).`                         (2.1)

#### Proof

Complete the square:

`A s^2+B s+C=A(s-s_0)^2+c_0`.

If `A>0`, the two inverse branches on `[c_0,infinity)` give exactly

`int_R f(A(s-s_0)^2+c_0) ds
 = |A|^(-1/2) int_(c_0)^infinity f(y)(y-c_0)^(-1/2)dy`.              (2.2)

The kernel is decreasing away from `c_0`. Under `0<=f<=1` and `int f=1`, the bathtub principle maximizes the last integral by putting unit density on the adjacent interval of length one, hence

`int_0^1 r^(-1/2)dr=2`.                                             (2.3)

The case `A<0` is identical on the opposite half-line. This proves (2.1). `QED`

This lemma is deliberately support-free: fragmented, disconnected, and unbounded supports are allowed.

## 3. Pure bilinear two-row receiver with arbitrary same-bank background

This is the exact zero-quadratic endpoint.

### Theorem 3.1 — `QFORM-BILINEAR-TWOROW-WEIGHTED-v1`

Let `X_1,X_2,Z_1,...,Z_m` be mutually independent real random variables, each with probability density at most one. Let `C` be a real `2 x m` matrix of row rank two and put

`Delta := sqrt(det(C C^T)) > 0`.                                    (3.1)

For **arbitrary measurable** `R=R(Z)`, define

`T = 2 (X_1,X_2) C Z + R(Z)`.                                      (3.2)

Then `T` has an essentially bounded density and

`boxed:
 ||p_T||_infinity <= 2 sqrt(pi e) Delta^(-1/2)
                   < 5.845 Delta^(-1/2).`                           (3.3)

No independence between `CZ` and `R(Z)` is required.

#### Proof

Let `Y=CZ=(Y_1,Y_2)`. For fixed `Z=z`, `R(z)` is only a translation of the output. By conditioning on whichever of the two original physical variables has the larger coefficient,

`||p_(2Y_1 X_1+2Y_2 X_2 | Z=z)||_infinity
 <= 1/(2 max(|Y_1|,|Y_2|))
 <= 1/(sqrt(2)||Y||_2)`.                                            (3.4)

This uses the original independent variables `X_1,X_2`; no rotated variables are declared independent.

Now normalize the light-bank map. With `G=C C^T`,

`P=G^(-1/2) C`

has orthonormal rows. Applying fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` with `k=2` gives

`||p_(PZ)||_infinity <= e`.                                         (3.5)

Since `Y=G^(1/2)PZ`,

`boxed: ||p_Y||_infinity <= e/Delta =: M.`                          (3.6)

This is the designated partner result used at an actual inequality.

Average (3.4) over the **true** law of `Y`; the arbitrary correlated shift `R(Z)` has already disappeared from the conditional bound:

`p_T(t) <= (1/sqrt(2)) E ||Y||_2^(-1)`.                             (3.7)

For any planar probability density bounded by `M` and any `rho>0`,

`E ||Y||^(-1)
 <= M int_(||y||<=rho) ||y||^(-1)dy + rho^(-1)
 = 2 pi M rho + rho^(-1).`                                          (3.8)

Choose `rho=(2 pi M)^(-1/2)`. Then

`E ||Y||^(-1) <= 2 sqrt(2 pi M)`.                                  (3.9)

Substituting (3.6) into (3.7)-(3.9) gives (3.3). `QED`

### Interpretation

The reciprocal coefficient is averaged **after** the two-dimensional product projection has been aggregated. There is no sum of fiber maxima and no selected physical light coordinate. The whole area currency `Delta=sqrt(det CC^T)` is spent at once.

## 4. Exact rank-one physical-pair parabolic receiver

The next theorem is the main new curved-fiber step.

### Theorem 4.1 — `QFORM-RANKONE-PAIR-PARABOLA-WEIGHTED-v1`

Let `X_1,X_2,Z_1,...,Z_m` be mutually independent cap-one variables. Let `B` be a nonzero symmetric `2 x 2` matrix of rank one. Write

`B = sigma u u^T`,                                                   (4.1)

where `u` is a unit vector and `sigma!=0` is the nonzero eigenvalue. Let `v` be a unit vector perpendicular to `u`. For a real `2 x m` matrix `C`, put

`d = v^T C`,  `delta=||d||_2`.                                      (4.2)

Assume `delta>0`. For arbitrary measurable `R=R(Z)`, define

`T = X^T B X + 2 X^T C Z + R(Z)`,  `X=(X_1,X_2)^T`.                 (4.3)

Then `T` has an essentially bounded density and

`boxed:
 ||p_T||_infinity
 <= 2^(9/4) e^(1/4) (|sigma| delta)^(-1/2)
 < 6.108 (|sigma| delta)^(-1/2).`                                   (4.4)

Again `R(Z)` may be arbitrarily dependent on the same light bank that creates the cross term.

#### Proof

Use the orthonormal basis `(u,v)` only as a deterministic parametrization of the **two-dimensional integral**. Put

`S=u^T X`, `W=v^T X`.                                                (4.5)

We do **not** assert that `S,W` are independent. If `u=(u_1,u_2)` and `v=(v_1,v_2)`, their joint density is exactly

`g(s,w)=f_1(u_1 s+v_1 w) f_2(u_2 s+v_2 w)`,                          (4.6)

because the change of variables is orthogonal and has Jacobian one. The original product factors remain visible.

For fixed `Z=z`, define

`U=u^T C z`,  `V=v^T C z=d z`.                                      (4.7)

For `V!=0`, the level equation `T=t` can be solved **linearly** for `W`:

`W_t(s)= [t-R(z)-sigma s^2-2Us]/(2V)`.                              (4.8)

Therefore the conditional density is

`p_(T|Z=z)(t)
 = 1/(2|V|) int_R g(s,W_t(s)) ds`.                                  (4.9)

Choose `j in {1,2}` with `|v_j|>=1/sqrt(2)`. Along the curved fiber,

`x_j(s)=u_j s+v_j W_t(s)`                                           (4.10)

is a quadratic polynomial in `s` whose quadratic coefficient is

`A_j= -v_j sigma/(2V)`,                                             (4.11)

so

`|A_j| >= |sigma|/(2 sqrt(2)|V|)`.                                 (4.12)

Drop the other original density factor using `f_{3-j}<=1`, but **retain** `f_j` exactly. Lemma 2.1 gives

`int g(s,W_t(s))ds
 <= int f_j(x_j(s))ds
 <= 2 |A_j|^(-1/2)
 <= 2^(7/4) sqrt(|V|/|sigma|).`                                     (4.13)

Insert (4.13) into (4.9):

`boxed:
 ||p_(T|Z=z)||_infinity
 <= 2^(3/4) (|sigma| |V|)^(-1/2).`                                 (4.14)

The bound is independent of `U`, of the target level, and of the arbitrary background `R(z)`. This is the key curved-fiber replacement: the parabolic curvature converts the dangerous linear reciprocal `|V|^(-1)` into the integrable half-power `|V|^(-1/2)` **before** the light bank is averaged.

Now apply the designated fleet02/B06 projection theorem to the actual scalar projection. Writing `d=delta h` with `||h||=1`,

`||p_(h^T Z)||_infinity <= sqrt(e)`,                                (4.15)

hence

`||p_V||_infinity <= sqrt(e)/delta =: L`.                            (4.16)

For every one-dimensional probability density bounded by `L`, symmetric-decreasing rearrangement gives

`E |V|^(-1/2)
 <= L int_(-1/(2L))^(1/(2L)) |v|^(-1/2)dv
 = 2 sqrt(2) L^(1/2).`                                              (4.17)

Average (4.14), use (4.16)-(4.17), and obtain

`||p_T||_infinity
 <=2^(3/4)|sigma|^(-1/2) 2^(3/2)e^(1/4)delta^(-1/2)
 =2^(9/4)e^(1/4)(|sigma|delta)^(-1/2).`                             (4.18)

Because `V` has a density, `P(V=0)=0`; the conditional absolutely continuous laws therefore mix to an absolutely continuous law. This proves (4.4). `QED`

### What this theorem does and does not use

- The rotated pair `(S,W)` is **not** treated as independent.
- No compact support or moment is used.
- No pointwise oscillatory-decay claim is used.
- No conditional density cap for a spectral coordinate is manufactured.
- The arbitrary background `R(Z)` can use every light coordinate and can be completely correlated with `(U,V)`.
- Continuity is not asserted; only absolute continuity plus the essential bound is proved.

## 5. Exact-rank-three Pluecker identity at a rank-one physical pair

The parabolic receiver becomes especially clean in exact rank three.

### Theorem 5.1 — `QFORM-RANK3-RANKONE-PAIR-PLUCKER-v1`

Let

`A=R Lambda R^T`, `R^T R=I_3`,                                     (5.1)

be symmetric of exact rank three. Write its nonzero singular values as

`s_1>=s_2>=s_3=:s>0`.                                               (5.2)

Fix a physical pair `I={i,j}` whose principal compression `B=A_(I,I)` is nonzero of rank one. Let `sigma` be its nonzero eigenvalue, let `v` be a unit null vector in the physical two-plane `span{e_i,e_j}`, and put

`d=A_(I^c,I) v`, `delta=||d||_2`.                                   (5.3)

Let `r_i,r_j` be the corresponding rows of `R` and define the physical-pair spectral Pluecker area

`tau_I := ||r_i wedge r_j||^2
        = ||r_i||^2 ||r_j||^2 - <r_i,r_j>^2`.                       (5.4)

Then the exact identity

`boxed:
 |sigma| delta^2 = |det Lambda| tau_I`                              (5.5)

holds. Consequently

`boxed:
 |sigma| delta >= s_2 s_3 tau_I >= s^2 tau_I.`                     (5.6)

Therefore, whenever `tau_I>0`, Theorem 4.1 gives the ambient quadratic form the determinant-free endpoint estimate

`boxed:
 ||p_(X^T A X)||_infinity
 <= 2^(9/4)e^(1/4)/(s sqrt(tau_I))
 < 6.108/(s sqrt(tau_I)).`                                         (5.7)

The outside coordinates may contain the full exact-rank-three background; no Schur remainder independence is required.

#### Proof of (5.5)

Rotate only the deterministic basis of the physical two-plane so that

`B -> diag(sigma,0)`.                                               (5.8)

This basis change is used for algebra; probability independence is not asserted after it. In the rotated basis, for every physical `k notin I`, the principal `3 x 3` compression has the form

`[[sigma,0,c_k],
  [0,0,d_k],
  [c_k,d_k,A_kk]]`,                                                 (5.9)

hence

`det A_(I union {k}) = -sigma d_k^2`.                               (5.10)

The determinant is unchanged by the two-dimensional orthogonal congruence because its determinant enters squared.

On the other hand, exact rank three gives for every physical triple `K`

`det A_K = det(Lambda) det(R_K)^2`.                                 (5.11)

Thus all nonzero principal triple determinants have the same sign. Sum absolute values of (5.10) over `k notin I` and use (5.11):

`|sigma| ||d||^2
 = |det Lambda| sum_(k notin I) det([r_i;r_j;r_k])^2`.              (5.12)

Because the rows of `R` form a Parseval frame,

`sum_k det([r_i;r_j;r_k])^2
 = (r_i wedge r_j)^T [sum_k r_k r_k^T] (r_i wedge r_j)
 = ||r_i wedge r_j||^2
 = tau_I`.                                                          (5.13)

Terms `k=i,j` vanish. Equations (5.12)-(5.13) prove (5.5).

For (5.6), let `b=R^T v`. Since `Bv=0`, `Av` has zero coordinates on `I`, so

`delta=||Av||=||Lambda b|| <= s_1 ||b|| <= s_1`.                   (5.14)

Therefore

`|sigma|delta
 = |det Lambda| tau_I/delta
 >= (|det Lambda|/s_1) tau_I
 = s_2 s_3 tau_I
 >= s^2 tau_I`.                                                     (5.15)

Apply Theorem 4.1 with the outside product bank and `R(Z)=Z^T A_(I^c,I^c)Z` to obtain (5.7). `QED`

### A finite-hub corollary matching the partner geometry

If both physical rows are heavy in the standard frame sense,

`ell_i=||r_i||^2 >= 1/64`, `ell_j>=1/64`,                           (5.16)

and their spectral row angle is `theta`, then

`tau_I=ell_i ell_j sin^2(theta) >= sin^2(theta)/4096`.              (5.17)

Hence a rank-one principal pair with `|sin theta|>=1/8` is paid by

`||p_Q||_infinity < 3127.239/s`.                                    (5.18)

The constant is not optimized; the point is structural. In the fleet02/B06 finite heavy hub, an exact rank-one principal compression is now harmless unless the corresponding heavy spectral rows are themselves nearly collinear. This matches the partner's separate near-rank-one/common-direction obstruction instead of creating a new determinant singularity.

## 6. Relation to r33 and the first unpaid implication

R33 paid every invertible indefinite physical pair by a determinant-only quarter-Riesz estimate. Theorems 4.1 and 5.1 now pay the **exact singular rank-one endpoint** by a different mechanism: linearize in the null physical direction, keep the other original factor on the resulting parabola, and use its curvature to turn `|V|^{-1}` into `|V|^{-1/2}`. The partner projection theorem then pays the true reciprocal moment.

This does **not** by itself close a near-singular but still rank-two pair. If the second eigenvalue of `B` is nonzero, the null variable is no longer linear: solving in that variable introduces a new moving quadratic critical point. It is not valid to regard the extra small quadratic term as an independent convolution or harmless perturbation. Doing so would silently reintroduce exactly the kind of conditional-density/center error forbidden by the correction inbox.

The next precise B06 implication is therefore

`QFORM-NEAR-RANKONE-PAIR-PARABOLA-INTERPOLATION-v1`:

> interpolate between r33's nondegenerate quarter-Riesz receiver and Theorem 4.1's exact rank-one parabolic receiver **before** taking a fiber supremum. The desired currency should retain both the small second pair eigenvalue and the null-star product projection, and should remain finite as `det B ->0` whenever the rank-one limit has nonzero `delta`.

A second structural continuation is:

`QFORM-HEAVY-PAIR-PLUCKER-OR-COMMON-DIRECTION-v1`:

> in the fleet02/B06 finite robust-light hub, either expose a rank-one/near-rank-one physical pair with spectral area `tau_I` bounded below (paid here), or prove that all relevant heavy spectral rows lie in one quantitative common direction and hand that packet to the existing grouped-bank / mixed-Fresnel receiver.

These are on the same QFORM target. No switch to another research problem is made.

## 7. Sanity checks and constants

The constants used above are

`2 sqrt(pi e) = 5.844564730644556...`,                              (7.1)

`2^(9/4)e^(1/4) = 6.1078886454775825...`.                           (7.2)

The rank-one triple determinant identity is easy to audit independently: for

`M=[[sigma,0,c],[0,0,d],[c,d,r]]`,

`det M=-sigma d^2`.                                                  (7.3)

The scaling is also correct. Under `A -> alpha A`, `sigma -> alpha sigma`, `delta -> |alpha|delta`, so the right side of (4.4) scales as `|alpha|^{-1}`, exactly as a density must. In (3.3), `Delta -> alpha^2 Delta`, so `Delta^(-1/2)` again scales as `|alpha|^{-1}`.

## 8. Final status

- Full arbitrary-dimensional QFORM: **OPEN**.
- Valid target counterexample: **none produced**.
- New durable results: Theorems 3.1, 4.1, 5.1.
- Designated fleet02/B06 result: applied at the actual inequalities (3.5)-(3.6) and (4.15)-(4.16).
- Continuity: **not proved globally or for these theorems**; only absolute continuity and `L^infinity` density bounds are asserted.
- Independent end-to-end review of the r34 results: **not yet completed**.
- Execution: `WITHOUT_VERIFIED_BRAIN`.
