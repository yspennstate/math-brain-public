SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T06:27:11Z.
attacking: QFORM-RANK2-CROSS-FRAME-DEFECT-IDENTITY-v1 — convert the near-range self-curvature survivor into a scale-invariant near-coloop/rank-drop parameter using an exact determinant identity.

# account03/B19 r27 — exact frame-defect identity for the rank-two-cross survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / quantitative inequalities  
**Fresh owner control:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL IDENTITY / BALANCED-FRAME BRANCH PAID / FULL QFORM OPEN`.

The unrestricted conjecture remains open. The result below is a deterministic exact-rank-three structural theorem and a direct payment of the balanced-frame part of the current rank-two-cross survivor. It uses only original-coordinate product inputs through already completed peer theorems. It adds no Gaussianity, moments, compact support, log-concavity, connected support, post-rotation independence, arbitrary-joint coarea, pointwise stationary phase, or one-good-minor premise.

## 1. Incoming proof state

The previous account03/B19 theorem at

`yspennstate/math-open-problems@82773d6d0339c8867b76c777216b6c564939f2ae`

proves that, for a rank-two original-coordinate cross bank with singular product `rho=s1(C)s2(C)` and a nonzero transverse source curvature `lambda`, one gets a continuous density bound

`||p_Q||_infinity < 12.01 |lambda|^(-1/4) rho^(-3/8)`.

Fresh account01/B19 auto11 at commit

`d72be34399b8d0325c715973e7af3a37df7ce227`

strengthens the receiver in exactly the needed direction. In its stated three-dimensional source-bank scope, writing `P=range(C)`, taking `r` unit transverse to `P`, and putting

`lambda=r^T B r`, `delta=||PBr||_2`, `R=sqrt(lambda^2+delta^2)=||Br||_2`,

it proves the uniform near-null estimate

`||p_Q||_infinity <= C_* R^(-1/4) rho^(-3/8)`,                 (1.1)

where

`C_*=2^(15/4)3^(-3/8)<8.912`,                                  (1.2)

including `lambda=0` whenever `delta>0`. Thus the analytic singularity is no longer tied to the scalar entry `lambda`; the only possible loss is when the **entire transverse self row** `Br` is small.

The current compound-energy branch supplies

`rho >= rho0 := sqrt(29/3072)=0.097160198469675...`.             (1.3)

The purpose of this run is to identify `R` exactly in spectral-frame geometry and isolate the only remaining scale-free obstruction.

## 2. Exact-rank-three setup

Let the entire target matrix have exact rank three,

`A=R0 M R0^T`, `R0^T R0=I_3`,                                  (2.1)

where `M=M^T` is invertible and every eigenvalue of `M` has absolute value at least one. Split the ORIGINAL physical coordinates into a genuine partition `I union J`. Write

`P=R0_I`, `S=R0_J`,
`G=P^T P`, `H=S^T S=I-G`,                                      (2.2)

and the physical block decomposition

`B=A_II=PMP^T`, `C=A_IJ=PMS^T`, `D=A_JJ=SMS^T`.                (2.3)

Assume

`rank(P)=3`, `rank(C)=2`.                                       (2.4)

Because `P` is injective on `R^3` and `M` is invertible,

`rank(C)=rank(S)=2`.                                             (2.5)

Thus `H` has rank two. Let `u` be a unit vector spanning `ker H`. Since `H=I-G`,

`Gu=u`.                                                          (2.6)

Let `W=u^perp`. Both `G` and `H` preserve `W`; on `W` their eigenvalues are

`g1,g2` and `1-g1,1-g2`, respectively, with `0<g1,g2<1`.        (2.7)

The strict inequalities follow from `rank(P)=3` and `rank(S)=2`.

Let

`rho=s1(C)s2(C)>0`.                                              (2.8)

Inside the three-dimensional physical source space `range(P)`, let `r` be the unit vector orthogonal to `range(C)`. Put

`lambda=r^TBr`, `delta=||Proj_range(C) Br||_2`,
`Rperp:=sqrt(lambda^2+delta^2)=||Br||_2`.                        (2.9)

## 3. Main identity

### Theorem 3.1 — `QFORM-RANK2-CROSS-FRAME-DEFECT-IDENTITY-v1`

Under (2.1)-(2.9),

`boxed:
 rho * Rperp
 = |det M| * sqrt(det(G|_W) det(H|_W))
 = |det M| * sqrt(g1 g2 (1-g1)(1-g2)).
`                                                                   (3.1)

Equivalently, defining the scale-free frame defect

`Theta:=sqrt(g1 g2 (1-g1)(1-g2))`,                              (3.2)

one has

`boxed: Rperp = |det M| Theta / rho.`                             (3.3)

This is exact; no inequality, conditioning, or probabilistic approximation is involved.

### Proof

Set

`z=G^(-1) M^(-1) u`, `r0=Pz`.                                   (3.4)

For every `w in W=range(S^T)`,

`<r0, PMw>
 = z^T G M w
 = (Gz)^T M w
 = (M^(-1)u)^T M w
 = u^T w
 =0`.                                                            (3.5)

Hence `r0` spans the one-dimensional orthogonal complement of `range(C)` inside `range(P)`. Its squared norm is

`q:=||r0||^2=z^T G z
  =u^T M^(-1) G^(-1) M^(-1)u`.                                  (3.6)

Since `Gz=M^(-1)u`,

`Br0=PMP^T Pz=PMGz=Pu`.                                         (3.7)

By (2.6),

`||Pu||^2=u^TGu=1`.                                              (3.8)

Therefore the normalized transverse vector is `r=r0/sqrt(q)` and

`Rperp=||Br||=q^(-1/2)`.                                        (3.9)

It remains to compute `rho`. The two nonzero squared singular values of `C` are the two nonzero eigenvalues of

`C^T C = S M G M S^T`.                                          (3.10)

By polar decomposition of `S`, their product is

`rho^2
 = det(H|_W) * det( (MGM)|_W )`.                              (3.11)

For every invertible `3x3` matrix `K` and unit `u`, Jacobi's complementary-minor identity gives

`det(K|_(u^perp))=det(K) u^T K^(-1)u`.                           (3.12)

Apply this to `K=MGM`. Then

`det(MGM)=det(M)^2 det(G)`,                                     (3.13)

and

`u^T(MGM)^(-1)u
 =u^T M^(-1)G^(-1)M^(-1)u=q`.                    (3.14)

Thus

`rho^2
 =det(H|_W) det(M)^2 det(G) q`.                                (3.15)

Because `Gu=u`, `det(G)=det(G|_W)`. Using `q=Rperp^(-2)` from (3.9) gives

`rho^2 Rperp^2
 =det(M)^2 det(G|_W)det(H|_W)`,                                 (3.16)

which is exactly (3.1). QED.

## 4. Immediate quantitative dichotomy

Because each `g_j` lies in `(0,1)`,

`0<Theta<=1/4`.                                                   (4.1)

Fix

`theta0:=2^(-12)=1/4096`.                                       (4.2)

### Corollary 4.1 — balanced frames are paid

If

`Theta>=theta0`,                                                  (4.3)

then the fresh account01/B19 receiver (1.1), the target spectral normalization `|det M|>=1`, and the current cross-product threshold (1.3) give

`||p_Q||_infinity
 <= C_* (|det M|Theta/rho)^(-1/4) rho^(-3/8)
 = C_* |det M|^(-1/4) Theta^(-1/4) rho^(-1/8)
 <= C_* theta0^(-1/4) rho0^(-1/8)
 <95.42 <96.`                                                     (4.4)

The density is continuous and vanishes at infinity because the peer receiver proves `phi_Q in L^1` in this scope.

Thus the entire current rank-two-cross aggregate branch is paid whenever the two source-bank frame directions are not too close to a rank-drop endpoint.

### Corollary 4.2 — every unpaid survivor is a quantitative near-coloop

If the balanced-frame exit (4.3) fails, then

`g1 g2 (1-g1)(1-g2)<2^(-24)`.                                   (4.5)

Consequently

`boxed:
 min{g1,g2,1-g1,1-g2}<1/64.
}`                                                                 (4.6)

Indeed, if all four factors were at least `1/64`, their product would be at least `2^(-24)`, contradicting (4.5).

So the former vague debt `QFORM-RANK2-CROSS-NEAR-RANGE-SELF-CURVATURE-v1` is replaced by the sharply scale-free structural debt

`QFORM-RANK2-CROSS-NEAR-COLOOP-STABILITY-v1`:                    (4.7)

a spectral frame direction has physical mass below `1/64` on one side of the cut (equivalently mass above `63/64` on the other), while the aggregate rank-two cross product remains at least `rho0`.

The point is that **coefficient scale has disappeared**. A huge eigenvalue of `M` cannot masquerade as a small transverse row: the exact product `rho Rperp/|det M|` is precisely the frame defect `Theta`.

## 5. Exact endpoint and designated partner application

The designated partner account04/B19 theorem

`QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`

is source-pinned at

`yspennstate/math-open-problems@1e7af7988c38150c1591910270c44f4f219164b3`.

In its proved **residual-diffuse exact-null-coloop** scope it gives, for residual determinant `D_res`,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`                        (5.1)

when `0<D_res<=1`, while its source gives separate bounded endpoints for `D_res=0` and `D_res>=1`.

Apply (5.1) to the actual interval

`e^(-8)<=D_res<=1`.                                               (5.2)

Then

`log(e/D_res)<=9`, hence

`boxed: ||p_Q||_infinity<34*3=102.`                              (5.3)

This is an equation-level use of the designated partner, and it is intentionally restricted to its exact-null-coloop residual-diffuse normal form. The new identity (3.1) shows why that endpoint is the correct model for the only surviving balanced-frame failure, but this report does **not** silently promote the partner's exact-null theorem to the near-coloop strip.

## 6. Conditional end-to-end assembly after this run

Within the current exact-rank-three aggregate-rank-two-cross route:

1. A quantitatively nonzero transverse source row is paid by account01/B19's uniform receiver.
2. The exact identity (3.1) rewrites that row scale as `|det M|Theta/rho`.
3. With `rho>=rho0`, every `Theta>=2^-12` branch is now continuously paid by `<96`.
4. Therefore every remaining survivor has a frame eigenvalue within `1/64` of `0` or `1`; it is a genuine near-coloop/near-rank-drop geometry, not merely a small coefficient.
5. Exact null-coloop residual-diffuse endpoints are covered by account04/B19 on their proved ranges, including the explicit `<102` interval (5.3).

What remains is the **near-coloop stability splice**: exploit the original-product provenance when one frame direction has mass `<1/64` on one side while the rank-two cross product stays bounded below. One must either route this to the completed rank-one-bank/grouped-coordinate compiler, to a physical-core/ridge theorem, or prove a stability version of the partner's null-coloop theorem. Deleting the small frame component as a random perturbation is forbidden because inputs have no moment or support bounds.

Arbitrary-extra-spectrum descent remains a separate global debt.

## 7. Status

- `QFORM-RANK2-CROSS-FRAME-DEFECT-IDENTITY-v1`: **PROVED**.
- Balanced-frame compound-energy rank-two-cross branch `Theta>=2^-12`: **PAID**, continuous density, explicit `<96` bound.
- Remaining exact-rank-three branch: `QFORM-RANK2-CROSS-NEAR-COLOOP-STABILITY-v1`.
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
