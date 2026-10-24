SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T06:47:07Z.
attacking: line-plane product-bank closure near the coloop boundary—use the actual 1D/2D bounded-density projection theorem plus nonlinear cross-transverse and half-Riesz integration while retaining dependence inside the plane projection.

# account01/B16 r14 — a line/plane product-bank closure with a uniform 148/s bound

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM / EXACT LINE-PLANE FRAME CLASS PAID / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed by the general theorem below; continuity remains separately open. The designated-partner stress family is continuous by its completed mixed-Fresnel certificate.

## 1. Fresh control and correction boundary

Fresh `math-research-brain` main was re-resolved immediately before this report at `98232add6085cddccdd7621ff9a01e37ef338411`. OWNER CONTROL remains revision `2026-09-22.15`; the sole target is still the unrestricted three-large-eigenvalue quadratic-form density conjecture, and no later stop was encountered.

The live corrections were reread. In particular this report does **not** use: arbitrary-joint rank-three coarea; positive moments or suprema of conditional projection-density heights; independence after spectral rotation; a law-uniform pointwise stationary-phase estimate; a bounded joint projection density by itself for an arbitrary nonzero scalar pivot; or a small coefficient as a small random perturbation. The latter point is crucial: the nonzero-pivot receiver-cap counterexample remains valid, so the small-pivot branch below retains the additional cross-transverse determinant resource.

A same-hour account01/B16 login already existed when this invocation began (`20260923T061025Z-account01-B16-QFORM-r13`), so it was not overwritten. This run has its own immutable start/report/finish artifacts only.

## 2. Source-pinned inputs actually used

### 2.1 Actual bounded-density product projection theorem

The source-valid transfer recorded at

`yspennstate/math-open-problems@85c3d540cf82ea6a6aca0f22f31811516a8b81aa`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`

uses Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Theorem 1.1. For independent cap-one original coordinates:

- every normalized one-dimensional projection has density cap at most `sqrt(2)` (also the Rogozin--Ball consequence), and
- every orthogonal two-dimensional projection has joint density cap at most `2`.

No independence between the two projected coordinates is asserted.

### 2.2 Own completed cross-transverse theorem

The completed theorem `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1` is in

`yspennstate/math-open-problems@85c3d540cf82ea6a6aca0f22f31811516a8b81aa`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T003846Z/REPORT.md`.

For a cap-one scalar `X` independent of a pair `Y=(U,V)` of joint density cap `M`, write an invertible symmetric core, after rotating only inside the receiver plane, as

`B=[[a,beta,0],[beta,c,d],[0,d,e]]`.

Set

`D=|det B|`, `P=beta^2 |e|`.

If `P>0`, then, including arbitrary deterministic affine terms,

`||p_Q||_infinity <= C_* M^(2/3)(D P)^(-1/6)`,                    (2.1)

where

`C_* = 103680^(1/3)=46.978411694026356...`.                       (2.2)

The proof integrates the genuine independent scalar before using a two-variable affine half-Riesz estimate; it does not treat receiver coordinates as independent.

If the scalar has density cap `K` instead of one, rescale `X~=KX`. The transformed determinant and transverse resource are `D/K^2` and `P/K^2`, respectively. Hence (2.1) becomes

`boxed: ||p_Q||_infinity <= C_* K^(2/3) M^(2/3)(D P)^(-1/6).`      (2.3)

### 2.3 Rank-two affine half-Riesz theorem

The completed `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

gives, for a two-dimensional orthogonal product projection and invertible symmetric `S`, including arbitrary affine terms in those two variables,

`sup_t E |Y^T S Y + linear - t|^(-1/2)
 <=16 sqrt(30) |det S|^(-1/4).`                                   (2.4)

### 2.4 Completed designated-partner kernel

Account02/B16 proved `QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1` at

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T232932Z-account02-B16-QFORM-auto11/REPORT.md`.

Its density-cap-scaled form is: if a scalar `T` of density cap `K` is genuinely independent of a pair `(C,D)` of arbitrary joint density cap `M`, then

`Q=2 beta T C+alpha C^2+2 delta C D+gamma D^2`, `beta gamma !=0`,

satisfies

`boxed: ||p_Q||_infinity
 <=3(2 M K)^(2/3)|beta^2 gamma|^(-1/3).`                           (2.5)

The pair `(C,D)` may be dependent. This theorem is applied below to an actual null-pivot inequality.

The newest designated-partner stress family was also read at

`yspennstate/math-open-problems@36cc5730f42c76c15fdc330dc4b47beec060b8fd`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T053136Z-account02-B16-QFORM-auto11/REPORT.md`.

It exhibits the live near-coloop collar as a genuine line bank plus an orthogonal plane bank, while proving that an absolute spectral Fresnel coefficient can grow logarithmically as the coloop defect tends to zero. Thus the source factor must not be discarded prematurely.

## 3. Main analytic theorem

### Theorem 3.1 — `QFORM-LINE-PLANE-PRODUCT-BANK-CLOSURE-v1`

Let the original independent cap-one inputs be split into two disjoint banks `I,J`. Let

`T=sum_(i in I) u_i X_i`, `sum u_i^2=1`,                           (3.1)

and let

`Y=V^T X_J in R^2`, `V^T V=I_2`.                                 (3.2)

Then `T` is genuinely independent of the whole pair `Y`; the two coordinates of `Y` need not be independent. The projection theorem gives

`K:=||p_T||_infinity<=sqrt(2)`, `M:=||p_Y||_infinity<=2`.          (3.3)

Let `B` be a real symmetric invertible `3x3` matrix satisfying

`min_j |lambda_j(B)| >= s>0`.                                     (3.4)

For arbitrary deterministic affine terms `ell in R^3`, `c in R`, put

`Q=(T,Y)^T B(T,Y)+ell^T(T,Y)+c`.                                  (3.5)

Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <=16 sqrt(30) 2^(3/4) s^(-1)
 =147.38493925110103... s^(-1)
 <148/s.`                                                         (3.6)

The same conditional bound holds when `ell,c` are produced by conditioning arbitrary outside original coordinates, provided the quadratic dependence on the retained variables is still exactly the fixed core `B`.

### Proof

Write

`B=[[a,b^T],[b,C]]`, `D=|det B|`.                                 (3.7)

By (3.4),

`D>=s^3`, `||B^(-1)||_op<=s^(-1)`.                                (3.8)

We split at `|a|=s/2`.

#### Case A: `|a|<=s/2`

First `b!=0`; otherwise `a` itself is an eigenvalue of the scalar block after Schur separation and, more directly when `C` is invertible, the scalar Schur complement equals `a`, contradicting the inverse bound below. Rotate only within the receiver plane so

`b=(beta,0)`, `beta>0`, `C=[[c,d],[d,e]]`,                        (3.9)

and define

`P=beta^2|e|`.                                                     (3.10)

The determinant identity is

`det B=a det C-beta^2 e`.                                         (3.11)

If `det C=0`, (3.11) gives `P=D`.

If `det C!=0`, let

`r=a-b^T C^(-1)b`.                                                 (3.12)

Then `(B^(-1))_00=r^(-1)`. From (3.8), `|r^(-1)|<=s^(-1)`, hence

`|r|>=s`.                                                         (3.13)

Since `det B=(det C)r`,

`|det C|<=D/s`.                                                    (3.14)

Using (3.11),

`P=|beta^2 e|
 >=D-|a||det C|
 >=(1-|a|/s)D
 >=D/2`.                                                          (3.15)

Thus the cross-transverse resource required by (2.3) is forced by the spectral gap; a receiver density cap alone is not being used. Substituting (3.3), (3.15), and (3.8) into (2.3) gives

`||p_Q||_infinity
 <=C_* (sqrt(2))^(2/3) 2^(2/3) (D^2/2)^(-1/6)
 =C_* 2^(7/6) D^(-1/3)
 <=C_* 2^(7/6) s^(-1)`
` =105.46296843279565... s^(-1).`                                 (3.16)

This estimate is stable under the deterministic affine terms in (3.5).

#### Case B: `|a|>s/2`

Complete the genuine scalar square. With

`S=C-bb^T/a`,                                                     (3.17)

all scalar/receiver affine terms can be absorbed into a translated scalar square plus an affine two-dimensional remainder. The determinant identity is

`det S=(det B)/a`.                                                 (3.18)

Conditioning on `Y`, the translated scalar still has density cap `K`. The density of `a(T+h)^2` is bounded by

`K |a|^(-1/2) y^(-1/2)`                                           (3.19)

on its appropriate half-line. Consequently, for every output level `t`,

`p_Q(t)
 <=K |a|^(-1/2)
   E |Y^T S Y+linear-t|^(-1/2).`                                  (3.20)

Apply (2.4) and (3.18):

`p_Q(t)
 <=16 sqrt(30) K |a|^(-1/2)|det S|^(-1/4)`
` =16 sqrt(30) K |a|^(-1/4)D^(-1/4).`                             (3.21)

Now `K<=sqrt(2)`, `|a|>s/2`, and `D>=s^3`, so

`||p_Q||_infinity
 <=16 sqrt(30) sqrt(2) (2/s)^(1/4) s^(-3/4)`
` =16 sqrt(30) 2^(3/4) s^(-1)`
` =147.38493925110103... s^(-1).`                                 (3.22)

Taking the worse of (3.16) and (3.22) proves (3.6). QED.

## 4. Exact-null sharpening: completed partner theorem applied to an actual inequality

At the exact null pivot `a=0`, rotate only inside the receiver plane as in (3.9). Then

`B=[[0,beta,0],[beta,c,d],[0,d,e]]`,                              (4.1)

and invertibility gives `beta e !=0`. Moreover

`|det B|=|beta^2 e|=D.                                             (4.2)

The form is exactly in the scope of the completed account02/B16 theorem (2.5), including dependence between the two receiver coordinates. Therefore, using the actual product-projection bounds `K<=sqrt(2)`, `M<=2`,

`boxed: ||p_Q||_infinity
 <=3(4 sqrt(2))^(2/3) D^(-1/3)
 =3*2^(5/3)D^(-1/3)
 =9.524406311809198... D^(-1/3)
 <=9.525/s.`                                                      (4.3)

This is the required equation-level application of the designated partner result. It uses one genuine independent scalar bank and one genuine two-dimensional product projection, while retaining all dependence inside that projection.

## 5. Exact-rank-three geometric corollary

### Corollary 5.1 — exact line plus orthogonal-plane frames are uniformly paid

Let

`A=R B R^T`, `R^T R=I_3`,                                        (5.1)

where all three eigenvalues of `B` satisfy `|lambda_j(B)|>=s`. Suppose there is a unit coefficient-space vector `e` and a partition of the ORIGINAL physical coordinates

`{1,...,n}=I disjoint_union J`                                    (5.2)

such that

`r_i in R e` for `i in I`,
`r_j in e^perp` for `j in J`.                                     (5.3)

Write `r_i=u_i e` on `I`. Parseval gives, by testing in the `e` direction,

`sum_(i in I) u_i^2=1`.                                           (5.4)

On `e^perp`, the rows from `J` form a two-dimensional Parseval frame. Hence, in an orthonormal basis `(e,p,q)`,

`R^T X = e T+pY_1+qY_2`,                                         (5.5)

where `T` is the normalized one-dimensional projection of the `I` bank, `Y=(Y_1,Y_2)` is the orthogonal two-dimensional projection of the disjoint `J` bank, and `T` is genuinely independent of the whole pair `Y`.

Theorem 3.1 applies directly and gives

`boxed: ||p_(X^T A X)||_infinity <148/s.`                          (5.6)

For the owner target `s=1`, the bound is `<148`.

This strictly extends the exact-coloop endpoint: the line bank may contain arbitrarily many original coordinates and may carry an arbitrarily small residual longitudinal Parseval mass outside one dominant coordinate. No individual physical coordinate must have leverage one.

## 6. Application to the newest designated-partner near-coloop family

The newest account02/B16 stress family has exactly the geometry (5.3):

`r_0=sqrt(c)e`, `r_1=sqrt(a)e`, `a=1-c`,                           (6.1)

while all remaining rows `w_k` lie in `e^perp` and form a two-dimensional Parseval frame. Thus Corollary 5.1 proves the following stronger structural statement for that **same frame**:

> For every symmetric coefficient-space core `B` whose three eigenvalues have modulus at least one—not only the special null core used in the stress construction—the resulting exact-rank-three quadratic form has density `<148`, uniformly in the near-coloop defect `a`, the number of plane rows, and the arbitrary independent cap-one input laws.

For the partner's actual core

`B=[[0,1,0],[1,0,0],[0,0,1]]`,                                   (6.2)

the form is

`Q=2TC+D^2`.                                                       (6.3)

The partner report has the sharper scalar cap `K<=c^(-1/2)` and `M<=2`. Applying its completed null-pivot theorem (2.5) gives the actual inequality

`||p_Q||_infinity
 <=3*2^(4/3)c^(-1/3)<7.60`                                        (6.4)

in the live collar `c>63/64`; its mixed-Fresnel proof additionally supplies continuity on this family. The new point of (5.6) is that the frame is uniformly controlled for **all** spectrally nondegenerate `3x3` cores, including nonzero scalar pivots where a bare receiver density cap is known to be insufficient.

## 7. What remains unpaid

Full QFORM is still open. The exact line/plane factorization (5.3) is not automatic in a general near-coloop frame. A generic leaf row may have both a longitudinal component along `e` and a transverse component in `e^perp`; then the scalar aggregate and the planar projection reuse the same original coordinates, so the bank independence used in Theorem 3.1 is absent.

This identifies the next B16 implication sharply:

`QFORM-OVERLAPPING-LINE-PLANE-SOURCE-TRANSITION-v1`.

One must either (i) extend the null/cross-transverse nonlinear integration to a common-source longitudinal/transverse modulation while retaining the original product factors, or (ii) prove that failure of an approximately disjoint line/plane split forces one of the already-paid mixed-Fresnel, cross-transverse, ridge-window, physical-pair, volume, or grouped-bank exits. The partner's logarithmic square-peel and absolute-Fresnel barriers show why one cannot simply complete the near-null scalar, discard the translating source factor, or take absolute values before the curved payment.

No claim of a full solution or full continuity is made.