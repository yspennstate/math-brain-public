SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T09:20:10Z.
attacking: dependence-safe critical time integral in the strict near-coloop heavy-row collar; convert the account02/B03 augmented-BL collision estimate into an averaged linear small-ball bound without conditional sum/difference caps.

# account01/B03 — outer-pivot/product splice for the strict near-coloop collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T092010Z-account01-B03-QFORM-auto11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW_STRUCTURAL_SPLICE / DEPENDENCE_SAFE_TIME_COROLLARY / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. This run does not claim a new proof of the product half-Riesz lemma: an early calculation matched the already-completed account01/B09 theorem exactly, so I stopped duplicate theorem work and used that source as an input. The new contribution is the quantitative splice of that completed product receiver with the newest account02/B03 heavy-row/augmented-BL classification, plus an explicit dependence-safe collision-energy corollary and a sharp warning that the collision energy alone cannot imply an L-infinity density bound.

## 1. Fresh sources actually used

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. The live corrections were reread before publication. In particular I do not use law-uniform pointwise quadratic-phase decay, post-rotation independence, conditional density caps for a sum/difference pair, arbitrary-joint rank-three coarea, positive moments of worst conditional projection caps, or selection of one universally good physical minor.

### 1.1 Newest Claude/e5 result applied at an equation

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

Lemma 4.2 there is the physical square peel

`D(Q) <= |a|^{-1/2} H_{1/2}(S)`,                                    (1.1)

where after completing an original coordinate

`Q=a(X_i+ell)^2+S`

and

`H_{1/2}(S)=sup_t E|S-t|^{-1/2}`.

I apply (1.1) to the exact current one-sided packet in Section 3.

### 1.2 Source match discovered; no duplicate novelty claim

Repository search after the early checkpoint found the exact product half-Riesz theorem already proved in

`yspennstate/math-open-problems@19a5e6e88d2d5756ebd92e85b00122ec0bdec699`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/B09-20260922T164451Z-r14/REPORT.md`.

Its Lemma 3.1 proves for independent U,V with density caps M,N,

`sup_t E|t-cUV|^{-1/2} <= 8 sqrt(MN)/sqrt(|c|)`,                     (1.2)

and its physical three-bank square-hyperbolic theorem gives, with the sharp one-dimensional original-product projection cap `sqrt(2)`,

`D(a(X_i+shift)^2+2 sigma U V) <= 8/sqrt(|a sigma|)`                 (1.3)

when U and V are unit projections of disjoint original-coordinate banks. This report therefore treats (1.2)-(1.3) as completed source material, not as a new B03 theorem.

### 1.3 Designated partner account02/B03 actually consumed

Newest partner handoff before publication:

`yspennstate/math-open-problems@ba17177f429b7864c9d41ce754c9c8983720cc08`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T061506Z-account02-B03-QFORM-auto11/REPORT.md`.

It proves `QFORM-HUB-DENSITY-AUGMENTED-BL-v1` and splices it with the heavy-row physical-pivot receiver. In the current one-sided exact-rank-three packet, after choosing the heavy obstruction row j, its quantitative classification is:

- if `|h_j| >= rho/16`, the physical-row receiver pays the density by at most `128 sqrt(15)/s`, where `s=s_3(A)`;
- if its augmented-BL threshold `x_* <= 15/16`, the Fourier/BL receiver pays it by a smaller universal multiple of `1/s`;
- otherwise one is forced into the strict collar

`|h_j| < rho/16`,                                                    (1.4)

`eta_j > 1969/2048`,                                                 (1.5)

`sqrt(det(B_{-j}^T B_{-j}))/m < sqrt(79/2048) < 0.196404`.           (1.6)

The exact coloop boundary `eta_j=1` is independently paid by the existing B14 endpoint, so the genuine survivor is nonzero but close to that boundary. I use (1.4)-(1.6) at the actual implication (4.4) below.

## 2. The assigned dependence-safe time integral

Let U,V be independent and let

`R=c U V`, `c!=0`,                                                    (2.1)

with density caps M,N. Let R' be an independent copy of the **whole scalar R**. The source theorem (1.2) gives

`sup_z E|R-z|^{-1/2} <= 8 sqrt(MN)/sqrt(|c|)`.                       (2.2)

Using only the exact independent-copy identity

`|phi_R(t)|^2 = phi_{R-R'}(t)`                                       (2.3)

and the one-dimensional Riesz identity

`int_R |t|^{-1/2} phi_{R-R'}(t) dt
 = sqrt(2 pi) E|R-R'|^{-1/2}`,                                      (2.4)

we get

`boxed:
 int_R |t|^{-1/2}|phi_R(t)|^2 dt
 <= 8 sqrt(2 pi) sqrt(MN)/sqrt(|c|).
}`                                                                   (2.5)

For the actual residual `R=2 sigma U V` and the sharp cap `M=N=sqrt(2)` for unit original-product projections,

`boxed:
 int_R |t|^{-1/2}|phi_R(t)|^2 dt
 <= 8 sqrt(2 pi)/sqrt(|sigma|)
 =20.0530261970... /sqrt(|sigma|).
}`                                                                   (2.6)

No `X-X'` variable is ever conditioned on, normalized against, or declared independent of its conjugate `X+X'`. The independent-copy operation is performed on R as a whole.

### 2.1 Why (2.5) alone is not an L-infinity theorem

This is an important endpoint boundary. Fix `0<alpha<1/2` and let

`p_alpha(x)=(1-alpha)x^{-alpha} 1_{(0,1)}(x)`.                       (2.7)

Then `p_alpha` is an unbounded probability density but belongs to L2, with

`||p_alpha||_2^2=(1-alpha)^2/(1-2alpha)`.                            (2.8)

For independent Y,Y' with this density, the difference density g obeys

`||g||_infinity <= ||p_alpha||_2^2`                                 (2.9)

by L2 convolution. Since g is supported on [-1,1],

`E|Y-Y'|^{-1/2}
 <=4 (1-alpha)^2/(1-2alpha) < infinity`.                             (2.10)

Hence

`int |t|^{-1/2}|phi_Y(t)|^2dt < infinity`                            (2.11)

while `||p_Y||_infinity=infinity`. Thus no abstract implication from the critical weighted collision integral to a bounded density is available. A valid linear-small-ball transducer must use additional structure. In the current packet that extra structure is the untouched original physical square in Section 3.

## 3. Actual linear-small-ball transducer for the one-sided packet

The current exact-rank-three one-sided packet, source-pinned through account01/B06 and account02/B03, is

`Q = a^{-1} H^2 + 2 sigma U V`,                                      (3.1)

`H=a X_i+h_L.X_L+h_R.X_R+h_K.X_K`,                                  (3.2)

where U and V are unit projections of disjoint original-coordinate banks L,R and X_i is a further independent original coordinate. Put

`rho^2=a^2+||k||^2`, `gamma=rho^2/|a|`, `s=s_3(A)`.                 (3.3)

The exact spectral identity gives

`gamma |sigma| >= s^2`.                                              (3.4)

Complete the **original coordinate X_i**, not a rotated coordinate:

`Q=a(X_i+B/a)^2+2 sigma U V`,                                        (3.5)

where B depends on the remaining original coordinates. Apply the newest Claude/e5 square peel (1.1) and the completed B09 product theorem (1.2):

`D(Q)
 <= |a|^{-1/2} H_{1/2}(2 sigma U V)
 <= 8/sqrt(|a sigma|).`                                              (3.6)

This is the promised real integrability-to-linear-small-ball closure. It uses the one-copy translation-uniform half-Riesz potential, while (2.6) is the assigned whole-copy collision integral for the same residual. From (3.4),

`|a sigma|
 = (|a|^2/rho^2) gamma|sigma|
 >= s^2 (|a|/rho)^2`.                                                (3.7)

Therefore

`boxed:
 D(Q) <= (8/s) rho/|a|.
}`                                                                   (3.8)

Equivalently every interval I obeys

`P(Q in I) <= (8/s)(rho/|a|)|I|`.                                   (3.9)

This branch proves absolute continuity and essential boundedness. It does **not** prove continuity for arbitrary fragmented input densities.

## 4. New splice with account02/B03: the survivor has a tiny outer pivot too

The newest partner classification already pays all states outside the strict collar (1.4)-(1.6) with the explicit common envelope

`C_partner = 128 sqrt(15)/s
 =495.7418683145.../s`.                                              (4.1)

Use (3.8) as an additional exit. For a threshold theta in (0,1),

`|a| >= theta rho`

implies

`D(Q) <= 8/(theta s)`.                                               (4.2)

Choose theta so that this new exit costs **no more than the partner's existing envelope**:

`8/theta = 128 sqrt(15)`.

Thus the optimal no-extra-constant choice is

`boxed:
 theta_* = 1/(16 sqrt(15))
          =0.0161374306092... .
}`                                                                   (4.3)

Combining (4.2) with the partner result gives the new structural alternative:

> In the current exact-rank-three one-sided heavy-right-plane endpoint, every state is paid by `128 sqrt(15)/s` unless the selected obstruction row j satisfies **all** of
>
> `boxed:
> |a|/rho < 1/(16 sqrt(15)),
> |h_j|/rho < 1/16,
> eta_j > 1969/2048,
> 0 < sqrt(det(B_{-j}^T B_{-j}))/m < sqrt(79/2048),
> x_*>15/16.
> `                                                                  (4.4)

The lower strict inequality on the deletion area records that the exact-coloop endpoint is already paid; if a later source uses a different exact-coloop parametrization, only that endpoint annotation should be changed, not the first four quantitative inequalities.

This is a genuine narrowing of the current first unpaid case. The outer physical pivot must now be tiny **simultaneously** with the heavy-row square coefficient and the deletion two-plane area. Since `m=rho y` and `y^2>1/2`, (4.4) also implies

`boxed:
 m/|a| > 16 sqrt(15/2)
        =43.8178046004... .
}`                                                                   (4.5)

Thus the remaining packet is not merely near-coloop on the right: it is also in a quantitatively singular outer-pivot regime. This is useful information for the next mechanism, because any attempted proof that pays by the X_i-square must necessarily lose here; the next receiver should use the large `a^{-1}` square on the right aggregate or a stable near-coloop grouped kernel rather than the tiny coefficient `a` after X_i completion.

## 5. Relation to the partner's collision theorem

The designated account02/B03 theorem was used at the actual structural implication (4.4), not merely cited. Its augmented-BL receiver controls the region `x_*<=15/16`; its physical-row receiver controls `|h_j|>=rho/16`; this report's completed-product/e5 square receiver controls `|a|>=rho/(16sqrt(15))`. Hence the three analytic channels are complementary:

1. augmented Fourier/BL spread in the right plane;
2. a non-cancelled heavy physical right row;
3. a non-tiny untouched outer physical square.

A state escaping all three has the simultaneous degeneracies recorded in (4.4). The exact-coloop theorem supplies the fourth boundary channel.

The collision estimate (2.6) remains valid throughout the outer-square branch and is dependence-safe, but Section 2.1 shows why it must not be advertised as a standalone L-infinity criterion. The correct endpoint currency is the translation-uniform half-Riesz potential in the e5 square peel.

## 6. What remains

The full QFORM conjecture remains **OPEN** and the full continuity conclusion remains **OPEN**.

Within this one-sided exact-rank-three route, the first unpaid implication is now the **simultaneously tiny outer-pivot / near-coloop interpolation** (4.4). A useful next attack should exploit the exact identity

`m^2 = ||h_-||^2 Delta^2 + ||h_R||^2 ||e||^2`

for the decomposition `v_-=c h_-+e`, rather than perturbatively deleting `e`: small matrix coefficients are not small random perturbations for arbitrary unbounded product inputs. The strict-collar source has both `Delta` large in the exact-coloop limit and `e` small in coefficient norm, but conditioning on `e.X` can destroy the cap of `h_-.X`; any proof must retain the original product bank through the averaging.

No new full-proof claim is made. Independent end-to-end review status: **not applicable / full candidate not reached**.