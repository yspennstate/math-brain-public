SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T17:07:32Z.
attacking: the rank-two crossing half-power debt when the third square is NOT a fresh independent source, but is a third projection of the same original-coordinate bank as the crossing pair.

# account01/B16 — dependent overlap-square closure for a rank-two crossing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN`  
**Regularity:** continuous density is proved in the theorem below; global QFORM continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source discipline and exact gap

The full target remains: independent real original-coordinate inputs with one-dimensional densities at most one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moments, support, identical-law, log-concavity, post-rotation independence, or smoothness assumptions are used.

Fresh control remained OWNER CONTROL revision `2026-09-22.15`. The live corrections retained here are:

- a bounded joint projection density by itself does **not** bound an indefinite quadratic level-set integral;
- a spectral rotation does **not** make projected coordinates independent;
- normalized conditional projection caps need not be uniformly bounded;
- uniform pointwise one-dimensional quadratic-phase decay is false.

Pinned projection input: `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T115514Z-qform-B18-a01/REPORT.md`, Theorem 3.1. If `T` is a full-row-rank `k x n` map applied to a product density with one-dimensional caps one, then

`||p_(TX)||_infinity <= 2^(k/2) / sqrt(det(TT^T)).`                 (1.1)

In particular orthonormal 2- and 3-dimensional projections have joint density caps `2` and `2 sqrt(2)`. This is only a joint-density statement, not projected independence.

Newest completed designated partner actually used: account02/B16,

`yspennstate/math-open-problems@44bff195ea0a90c3fe24628eb2cf3b405368c37c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/account02-B16-20260923T153432Z-auto11/REPORT.md`.

Its `QFORM-CROSS2-ARBITRARY-SELFBLOCK-L32-v1` proves that a genuine rank-two crossing with arbitrary same-side phases gives only an `L^(3/2)` characteristic function, while `QFORM-CROSS2-PLUS-FRESH-SQUARE-v1` closes Fourier inversion if a **disjoint fresh scalar square** is available. The remaining half-power debt is precisely what happens when the square shares the same original source bank as one crossing pair.

The current interactive projected-crossing theorem at

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`

allows arbitrary internal hub functions, but for an exact rank-two crossing by itself still produces the borderline `|t|^-1` envelope. The theorem below extracts the missing time integrability from a rank-one quadratic inside that same hub bank without declaring it independent of the crossing pair.

## 2. New theorem — the third square may overlap the crossing pair in source space

### `QFORM-CROSS2-OVERLAP-SQUARE-L1-v1`

Let the active ORIGINAL source coordinates split into two disjoint banks `I` and `J`. Let

`(Z,T) in R^2 x R`

be a three-dimensional linear image of `X_I`, and let

`W in R^2`

be a two-dimensional linear image of `X_J`. The vectors `(Z,T)` and `W` are genuinely independent because the source banks are disjoint, but the three coordinates inside `(Z,T)` may be arbitrarily dependent, and the two coordinates inside `W` may be arbitrarily dependent. Assume their joint densities satisfy

`||rho_(Z,T)||_infinity <= M`,
`||rho_W||_infinity <= N`.                                          (2.1)

Let `Sigma=diag(s_1,s_2)` with `s_1,s_2>0`, let `lambda!=0`, let `h in R^2`, `u_0 in R`, and let `r:R^2->R` be any real quadratic-plus-affine polynomial. Let `H(X_J)` be an **arbitrary measurable real function** of the `J` source bank. Consider

`Q = 2 Z^T Sigma W
     + lambda (T+h^T Z+u_0)^2
     + r(Z)
     + H(X_J).`                                                     (2.2)

Then `Q` has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= C_* (MN)^(2/5) (s_1s_2)^(-2/5) |lambda|^(-1/5),`              (2.3)

where

`C_* = 5 (675/256)^(1/5)
     = 6.069917185377548... .`                                     (2.4)

Thus the third smoothing direction need not be a fresh independent scalar. It may be a third, arbitrarily dependent projection of the **same original source bank** that produces the two crossing coordinates.

### Proof

Shear the third projected coordinate by

`S=T+h^TZ+u_0`.                                                     (2.5)

For each fixed `z`, this is a translation in the scalar fiber, so the transformed joint density `rho(z,s)` still satisfies `rho<=M`, and its `z`-slice mass

`m(z)=int_R rho(z,s) ds`                                           (2.6)

still satisfies `int_R2 m(z)dz=1`.

For each fixed `z`, define

`G_z(t)=int_R rho(z,s) exp(i t lambda s^2) ds`.                    (2.7)

If `m(z)=0`, put `G_z=0`. If `m(z)>0`, normalize the slice to the probability density

`f_z(s)=rho(z,s)/m(z)`,                                            (2.8)

whose density cap is at most `M/m(z)`. The completed square `L^3` estimate used in the designated-partner fresh-square theorem states that for a probability density of cap `L`,

`int_R |E exp(i t lambda Y^2)|^3 dt <= 50 pi L^2/|lambda|`.        (2.9)

Applying (2.9) to (2.8) and multiplying back by `m(z)^3` gives the **unnormalized slice estimate**

`int_R |G_z(t)|^3 dt
 <= 50 pi M^2 m(z)/|lambda|.`                                     (2.10)

Also `|G_z(t)|<=m(z)`. Hence

`int_R |G_z(t)|^4 dt
 <= 50 pi M^2 m(z)^2/|lambda|.`                                   (2.11)

Set

`H_4(t) = (int_R2 |G_z(t)|^2 dz)^(1/2).`                           (2.12)

Minkowski, applied to `H_4(t)^2`, yields

`||H_4||_4^2
 = || int |G_z(.)|^2 dz ||_2
 <= int (int |G_z(t)|^4 dt)^(1/2) dz
 <= sqrt(50 pi) M |lambda|^(-1/2) int m(z)dz.`                    (2.13)

Therefore

`boxed:
 ||H_4||_4 <= (50 pi)^(1/4) M^(1/2)|lambda|^(-1/4).`              (2.14)

This is the key overlap step: it is an averaged-in-time estimate for the curved scalar fibers. It never asks for a conditional density cap and it does not require `T` to be independent of `Z`.

Now push the complex measure

`exp(i t H(X_J)) dP_(X_J)`

onto `W`. Its complex density `b_t(w)` satisfies

`|b_t(w)|<=p_W(w)`, hence `||b_t||_2<=sqrt(N)`.                    (2.15)

The `I`-bank contributes the function

`F_t(z)=exp(i t r(z)) G_z(t)`,                                    (2.16)

so `||F_t||_2=H_4(t)`. Genuine independence of the two original source banks gives

`phi_Q(t)
 = int_R2 int_R2 F_t(z)b_t(w)
   exp(2 i t z^T Sigma w) dz dw.`                                 (2.17)

With Fourier convention `hat F(xi)=int exp(i xi.z)F(z)dz`, Cauchy-Schwarz in `w`, the change of variables `xi=2t Sigma w`, and two-dimensional Plancherel give, for `t!=0`,

`|phi_Q(t)|
 <= sqrt(N) [int |hat F_t(2t Sigma w)|^2 dw]^(1/2)`

` = [pi sqrt(N)/( |t| sqrt(s_1s_2) )] H_4(t).`                    (2.18)

This uses the dependent pair `W` only through its true joint `L^2` cap; no independence is inserted inside `W`.

For any `T_0>0`, combine `|phi_Q|<=1`, (2.18), Holder with exponents `4` and `4/3`, and (2.14):

`int_R |phi_Q(t)|dt
 <= 2T_0
 + [pi sqrt(N)/sqrt(s_1s_2)] ||H_4||_4
   (int_(|t|>T_0)|t|^(-4/3)dt)^(3/4)`

` <=2T_0+E T_0^(-1/4),`                                           (2.19)

where

`E = 6^(3/4) pi sqrt(N)(s_1s_2)^(-1/2)
     (50pi)^(1/4)M^(1/2)|lambda|^(-1/4).`                         (2.20)

The minimizing choice is

`T_0=(E/8)^(4/5)`,                                                 (2.21)

and then

`int |phi_Q|
 <=10*8^(-4/5) E^(4/5).`                                         (2.22)

Fourier inversion gives a continuous density and

`||p_Q||_infinity <= (2pi)^(-1) int|phi_Q|`.                       (2.23)

Substituting (2.20) into (2.22), the factor `pi` cancels and the remaining numerical constant is

`5*8^(-4/5)*50^(1/5)*6^(3/5)
 =5(675/256)^(1/5)=C_*`,                                         (2.24)

which is exactly (2.3). QED.

## 3. Product-projection corollary

Suppose the three coefficient vectors producing `(Z,T)` are orthonormal on the `I` source bank and the two coefficient vectors producing `W` are orthonormal on the disjoint `J` bank. The actual bounded-density projection theorem (1.1) gives

`M<=2^(3/2),   N<=2`.                                              (3.1)

Therefore `(MN)^(2/5)<=2`, and (2.3) becomes

`boxed:
 ||p_Q||_infinity
 <= 2 C_* (s_1s_2)^(-2/5)|lambda|^(-1/5)
 < 12.140 (s_1s_2)^(-2/5)|lambda|^(-1/5).`                        (3.2)

The joint 3-dimensional projection is never split into independent coordinates.

A non-orthonormal version follows immediately from (1.1): if the `3 x |I|` map has Gram `G_I>0` and the `2 x |J|` map has Gram `G_J>0`, then

`M<=2^(3/2)(det G_I)^(-1/2),`
`N<=2(det G_J)^(-1/2)`,                                            (3.3)

which may be inserted directly into (2.3).

## 4. Actual full-target family that the fresh-square theorem does not cover

Let `U` have two orthonormal columns on source bank `I`, let `a` be a unit vector on the same bank orthogonal to both columns of `U`, and let `V` have two orthonormal columns on a disjoint source bank `J`. Put

`Z=U^T X_I`, `T=a^T X_I`, `W=V^T X_J`.                             (4.1)

The scalar `T` is generally **dependent** on the pair `Z`; it is not a fresh source. Let `B_J` be any symmetric matrix on the `J` bank with

`||B_J||_op<=1/2`,                                                 (4.2)

and consider

`Q_shared = 4 Z^T W + T^2 + X_J^T B_J X_J.`                       (4.3)

The theorem applies with `s_1=s_2=2`, `lambda=1`, `M<=2sqrt(2)`, `N<=2`, and arbitrary `H(X_J)=X_J^TB_JX_J`. Hence

`boxed:
 ||p_(Q_shared)||_infinity
 <=2 C_* 4^(-2/5)
 =6.972503885811421... <6.973.`                                   (4.4)

The density is continuous.

This is an actual member of the owner's spectral target. With `B_J=0`, the nonzero spectrum is

`{2,2,-2,-2,1}`.                                                   (4.5)

For general (4.2), compress to the four-dimensional `span(U,V)` crossing space. Its pure crossing eigenvalues are `{2,2,-2,-2}`, and the `J`-side perturbation has norm at most `1/2`, so the compression has two eigenvalues at least `3/2` and two at most `-3/2`. Orthogonal-compression interlacing transfers these four large eigenvalues to the full matrix. Independently, `a` remains an exact eigenvector of eigenvalue `1`, because it is orthogonal to the crossing range and the perturbation acts only on `J`. Thus at least three eigenvalues have modulus at least one.

The designated-partner fresh-square theorem cannot be invoked on (4.3): its square variable must come from a source bank disjoint from both crossing banks, whereas `T` reuses the `I` bank. Equation (4.4) is therefore a strict source-provenance extension of that mechanism.

## 5. Applying the newest completed account02/B16 result to an actual inequality

For comparison, retain the same disjoint crossing banks but now let `Y` be a genuinely fresh physical scalar from a third source bank, and let `B_I,B_J` be arbitrary symmetric same-side blocks satisfying

`||B_I||_op, ||B_J||_op <=1/2`.                                   (5.1)

With the same orthonormal rank-two projections `Z,W`, set

`Q_fresh
 = X_I^T B_I X_I + X_J^T B_J X_J
   +4 Z^T W + Y^2.`                                                (5.2)

Here the cross block has singular values `s_1=s_2=2`, and the scalar `Y` has density cap one. Applying the completed partner theorem `QFORM-CROSS2-PLUS-FRESH-SQUARE-v1` at its actual equation (3.2) gives

`boxed:
 ||p_(Q_fresh)||_infinity
 <= 900^(1/3) (4)^(-1/3)
 =225^(1/3)
 =6.082201995573399... <6.083.`                                   (5.3)

The partner proof also gives a continuous density. The pure crossing block has eigenvalues `{2,2,-2,-2}`; perturbing its two same-side blocks by operator norm at most `1/2` leaves two eigenvalues at least `3/2` and two at most `-3/2`, while `Y^2` adds an exact eigenvalue `1`. Thus (5.3) is a genuine target-level family.

Moreover, if `R` is **any** random quadratic form on additional disjoint original coordinates, then independence gives

`p_(Q_fresh+R)=p_(Q_fresh)*mu_R`,                                  (5.4)

so

`boxed: ||p_(Q_fresh+R)||_infinity <6.083.`                        (5.5)

Convolution with a probability law also preserves continuity of the bounded continuous representative from the partner theorem. This supplies an arbitrary-dimensional block-direct-sum extension of the actual partner inequality.

## 6. Exact gain and remaining B16 debt

The new theorem pays one concrete part of the designated partner's `QFORM-SUPERDIFFUSE-OVERLAP-HALFPOWER-TRANSDUCER-v1` debt:

- rank-two crossing alone, with arbitrary same-side phases, is borderline (`L^(3/2)` characteristic function);
- a **fresh** independent square closes it by ordinary Holder (partner theorem);
- now a **same-bank overlapping square** also closes it, provided the hub-side quadratic phase factors through a genuine 3-dimensional projection `(Z,T)` with nonzero `T^2` coefficient. The proof uses a slice `L^4_t(L^2_z)` estimate and never conditions on `Z` with a normalized density cap.

What remains unpaid is the truly arbitrary overlapping-curvature chamber: the hub-bank quadratic/affine phase may involve source directions outside the 3-dimensional `(Z,T)` projection, or the surviving curvature may lie entirely inside the two crossing directions so that no nonzero transverse square coefficient is available. In those cases the conditional complex slice amplitude can itself depend on `T`, and estimate (2.10) cannot simply be reused. A full structural theorem still must force either the projected-volume receiver, the overlap-square configuration above, a fresh-source closure, or another source-preserving half-power mechanism with quantitative parameters.

This report does **not** claim the full QFORM conjecture proved. Global continuity is likewise still open.

## 7. Integrity / changed-file review

Changed-file allowlist for the canonical mathematics publication is only this run-owned report path. Manual fallback privacy review found only mathematical notation, public literature/source pins, run identifiers, and repository paths; no credentials, personal archives, financial/client material, signed URLs, or permission changes are present. No schedule, notification, account binding, task count, public visibility, paid/remote call, or cross-account authentication was changed.
