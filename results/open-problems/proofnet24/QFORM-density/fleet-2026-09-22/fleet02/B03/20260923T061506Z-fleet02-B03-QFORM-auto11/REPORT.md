SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-23T06:15:06Z.
attacking: the heavy-row angular-cancellation endpoint by retaining the genuine grouped-hub density inside the Fourier/Brascamp–Lieb integral, then comparing the resulting critical collision certificate with the newest physical-row receiver.

# fleet02/B03 — hub-density augmentation of the decoupled time integral

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Run:** `20260923T061506Z-fleet02-B03-QFORM-auto11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW_SUPPORTING_THEOREM / HEAVY-ROW-GAP-NARROWED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains open.  This report proves a new source-valid Fourier/Brascamp–Lieb receiver for the current heavy-right-plane angular-cancellation state and turns the residual obstruction into a quantitative near-coloop collar.  It never conditions on a conjugate sum/difference variable, never declares post-rotation coordinates independent, never invokes a worst conditional density cap, and never uses the refuted law-uniform pointwise quadratic-phase estimate.

## 1. Source state and completed inputs actually used


Three source-pinned inputs are used at displayed inequalities.

1. **Required newest Claude/e5 Fourier package**

   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

   and its `FOURIER_ROUTE_REPORT.md`.  I use the damped Fresnel linearisation and the proved twisted characteristic-function inequality

   `int |Psi(s)|^p ds <= 4 pi/sqrt(p),  p>=2`,                       (1.1)

   inside an actual new Brascamp–Lieb integral in Section 2.

2. **Newest designated partner fleet03/B03 actually consumed**

   `yspennstate/math-open-problems@b580b09027d8c20c3d3bbea0bea6cf8caa04d541`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T045638Z-fleet03-B03-QFORM-r27/REPORT.md`.

   In the current one-sided packet it proves, for every heavy physical right-plane row `r` with `h_r!=0`,

   `||p_Q||_infinity
    <=(16 sqrt(60)/s_3(A)) sqrt(rho/|h_r|)`.                         (1.2)

   It also proves the dependence-safe whole-residual half-Riesz time identity/bound after pivoting such a row.  This report uses (1.2) as one side of a new structural alternative in Section 6.

3. **Exact-coloop endpoint already paid after r27**

   fleet03/B14 r27, latest corrected source through
   `yspennstate/math-open-problems@ba66d82dd8e99e4b651a0442ef3a1175a953bf90`,

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T053308Z-fleet03-B14-QFORM-r27/REPORT.md`.

   If deleting the heavy row makes the two right-plane coefficient vectors collinear, it proves

   `||p_Q||_infinity <=48 sqrt(10)/s_3(A)`.                          (1.3)

   Thus a useful new result should be stable away from, and approach, this exact-zero-area endpoint rather than reprove it.

The exact one-sided geometry used below is inherited from fleet01/B06 r21/r24 and partner r27.  There is a physical pivot and disjoint original-coordinate banks such that

`Q=a^(-1) H^2+2 sigma U V`,                                         (1.4)

`H=a X_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                                (1.5)

where `u,v` are unit vectors and

`h_R=beta v+m q`, `q perp v`, `||q||=1`, `m>0`.                     (1.6)

Put

`rho^2=a^2+||k||^2`, `m=rho y`, `y^2>1/2`,
`gamma=rho^2/|a|`.                                                   (1.7)

The source spectral identities give

`gamma |sigma|>=s_3(A)^2`,                                          (1.8)

`gamma sigma^2=s_1(A)s_2(A)s_3(A)>=s_3(A)^3`.                       (1.9)

The diffuse right-plane branch `max_j(v_j^2+q_j^2)<=1/2` is already paid by fleet01/B06 r24.  Hence the only state relevant here has at least one heavy physical row.

## 2. New analytic theorem — keep the hub density inside Brascamp–Lieb

Let `Y=(Y_1,...,Y_m)` have independent probability densities `f_j<=1`.  Let `Omega` be independent of `Y`.  Let `U=U(Omega)` have probability density `p_U<=L`, while `xi(Omega)` and `F(Omega)` may depend arbitrarily on `U`.  Let `h,v in R^m` be linearly independent.  Let `A d!=0`, and allow arbitrary one-coordinate real phases `phi_j(Y_j)`.  Define

`T=A(h.Y+xi(Omega))^2+2d U(Omega)(v.Y)
   +F(Omega)+sum_j phi_j(Y_j)`.                                     (2.1)

For a fixed final frequency `t`, define twisted characteristic functions

`Psi_j(r)=int f_j(z) exp(i t phi_j(z)) exp(i r z) dz`.               (2.2)

### Theorem 2.1 — `QFORM-HUB-DENSITY-AUGMENTED-BL-v1`

Fix `tau>0`.  Put

`b_0=(0,tau)`, `b_j=(h_j,v_j)`,
`G_tau=sum_(j>=0) b_j b_j^T`,                                       (2.3)

and

`c_k=b_k^T G_tau^(-1)b_k`.                                          (2.4)

Assume

`c_j<=1/2` for every physical product row `j>=1`.                    (2.5)

No upper restriction on `c_0` is required for the estimate itself.  Write

`alpha=3/2-c_0`.                                                     (2.6)

Then

`|phi_T(t)|<=min(1,K_tau |t|^(-alpha))`,                            (2.7)

where

`K_tau=(4pi)^(3/2-c_0) 2^(c_0-1)c_0^(-c_0/2)
       |A|^(-1/2)|d|^(c_0-1) tau^c_0 L^(1-c_0)
       det(G_tau)^(-1/2)`.                                          (2.8)

If `c_0<1/2`, then `alpha>1`, `phi_T` is integrable, `T` has a continuous density, and

`boxed:
 ||p_T||_infinity
 <= alpha/[pi(alpha-1)] K_tau^(1/alpha).
}`                                                                    (2.9)

At the critical value `c_0=1/2`, absolute integrability may fail, but the whole-copy collision integral remains finite:

`boxed:
 int_R |t|^(-1/2)|phi_T(t)|^2 dt
 <=[4+2/(2alpha-1/2)] K_tau^(1/(2alpha)).
}`                                                                    (2.10)

In particular at `c_0=1/2`, `alpha=1` and the outside coefficient in (2.10) is `16/3`.

### Proof

The e5 damped Fresnel identity, with damping removed by dominated convergence exactly as in the source proof, gives

`|phi_T(t)|
 <=(4pi|tA|)^(-1/2)
   int ds int p_U(u)
   prod_j |Psi_j(s h_j+2td u v_j)| du`.                              (2.11)

Let

`T_0=2|td|`, `eta=2td u`.

Then

`|phi_T(t)|
 <=(4pi|tA|)^(-1/2) T_0^(-1)
   int_R2 p_U(eta/T_0)
   prod_j |Psi_j(s h_j+eta v_j)| ds deta`.                           (2.12)

The key change from the earlier grouped-hub proof is that **the factor `p_U` remains inside this two-dimensional integral**.

Set `z=G_tau^(1/2)(s,eta)`.  The normalized rows

`r_k=G_tau^(-1/2)b_k`

form a tight frame in `R^2`, with squared lengths `c_k` and `sum c_k=2`.  Let `a_k=r_k/sqrt(c_k)`.  Geometric rank-one Brascamp–Lieb says

`int prod_k F_k(a_k.z)^c_k dz
 <=prod_k (int F_k)^c_k`.                                           (2.13)

For `j>=1` take

`F_j(r)=|Psi_j(sqrt(c_j)r)|^(1/c_j)`.

By (2.5), `1/c_j>=2`, so the source inequality (1.1) gives

`(int F_j)^c_j
 =c_j^(-c_j/2)(int |Psi_j|^(1/c_j))^c_j
 <=(4pi)^c_j`.                                                       (2.14)

For the auxiliary row define

`H_0(r)=p_U(r/(tau T_0))`,
`F_0(r)=H_0(sqrt(c_0)r)^(1/c_0)`.                                   (2.15)

Probability mass one and `p_U<=L` imply

`int p_U(u)^(1/c_0) du<=L^(1/c_0-1)`.                               (2.16)

Therefore

`(int F_0)^c_0
 <=c_0^(-c_0/2)(tau T_0)^c_0 L^(1-c_0)`.                           (2.17)

Restoring the Jacobian gives the exact integrated estimate

`int_R2 p_U(eta/T_0)prod_j|Psi_j(s h_j+eta v_j)|dsdeta`
`<=det(G_tau)^(-1/2)(4pi)^(2-c_0)c_0^(-c_0/2)
   (tau T_0)^c_0 L^(1-c_0)`.                                       (2.18)

Substitution into (2.12), using `T_0=2|td|`, is exactly (2.7)-(2.8).

If `alpha>1`,

`int_R min(1,K|t|^-alpha)dt
 =2 alpha/(alpha-1) K^(1/alpha)`.                                   (2.19)

Fourier inversion gives (2.9).

For (2.10), square (2.7), multiply by `|t|^-1/2`, and split at `t_0=K^(1/alpha)`:

`int_R |t|^-1/2 min(1,K^2|t|^(-2alpha))dt`
`=[4+2/(2alpha-1/2)]K^(1/(2alpha))`.                                (2.20)

This is the claimed dependence-safe collision estimate.  It uses the independent-copy identity only for the whole variable,

`|phi_T(t)|^2=E exp(it(T-T'))`,                                      (2.21)

so no `X_j+X_j'` is separated from `X_j-X_j'`.  QED.

## 3. Exact two-plane leverage algebra

Apply Theorem 2.1 to the right bank in (1.4)-(1.6).  Set

`H_R^2=||h_R||^2=beta^2+m^2`,                                      (3.1)

`eta_j=v_j^2+q_j^2`,
`delta_j=h_j^2/H_R^2`.                                               (3.2)

Then

`sum_j eta_j=2`, `sum_j delta_j=1`, and `delta_j<=eta_j`,            (3.3)

because `h_R/H_R` is a unit vector in the plane `span(v,q)`.

Introduce the dimensionless regularization parameter

`x=H_R^2 tau^2/m^2`.                                                (3.4)

A direct inversion of

`G_tau=[[H_R^2,beta],[beta,1+tau^2]]`

shows

`det G_tau=m^2(1+x)`,                                                (3.5)

`c_0=x/(1+x)`,                                                       (3.6)

`boxed:
 c_j=(eta_j+x delta_j)/(1+x).
}`                                                                    (3.7)

Thus every row with `eta_j<=1/2` is automatically admissible for every `x>=0`.  For a heavy row `eta_j>1/2`, admissibility `c_j<=1/2` is equivalent to

`delta_j<1/2`

and

`x>=x_j:=(2eta_j-1)/(1-2delta_j)`.                                  (3.8)

Define

`x_*:=max_(eta_j>1/2) x_j`,                                         (3.9)

with `x_*=0` if there is no heavy row.  Whenever `x_*<1`, choose any

`x_*<=x<1`.                                                         (3.10)

Then every physical row satisfies (2.5), while

`c_0=x/(1+x)<1/2`.                                                   (3.11)

Hence Theorem 2.1 produces an actual `L^infinity` density bound.

The obstruction has a precise geometric meaning.  Let `B` be the physical row matrix with rows `(h_j,v_j)`.  Deleting row `j` gives

`det(B_-j^T B_-j)=det(B^TB)(1-eta_j)=m^2(1-eta_j)`.                  (3.12)

Thus the critical condition `eta_j+delta_j>=1` is equivalent to

`boxed:
 |h_j|/H_R >= sqrt(1-eta_j),
}`                                                                    (3.13)

namely: the normalized square coefficient on the heavy row dominates the normalized residual two-plane area left after deleting that same row.  This is the exact near-coloop/square-alignment collar where the augmented row cannot create a strict BL margin.

## 4. Target-homogeneous density bound in every strict branch

Let `s=s_3(A)`.  In the one-sided packet use

`A=1/a`, `d=sigma`, `L<=sqrt(e)`                                    (4.1)

(the completed scalar product-projection bound), together with (3.4)-(3.6).  Put

`c=x/(1+x)`,
`alpha=3/2-c=(3+x)/(2(1+x))`.                                      (4.2)

The matrix-scale denominator in (2.8) is

`D=|a|^(-1/2)|sigma|^(1-c)m^(1-c)H_R^c`                             (4.3)

` =[sigma^2m^2/|a|]^((1-c)/2)[H_R^2/|a|]^(c/2)`.                   (4.4)

Since `H_R>=m=rho y`,

`D>=gamma^(1/2)|sigma|^(1-c)y`.                                    (4.5)

The two source spectral inequalities (1.8)-(1.9) imply

`boxed:
 gamma^(1/2)|sigma|^(1-c)>=s^(3/2-c)=s^alpha.
}`                                                                    (4.6)

Indeed write `gamma=sg`, `|sigma|=sr`; then `gr>=1` and `gr^2>=1`.  If `r>=1`, use `g>=1/r`; if `r<=1`, use `g>=1/r^2`.  In either case `g^(1/2)r^(1-c)>=1` for `0<=c<=1/2`.

Therefore

`D>=s^alpha y`, `y>1/sqrt(2)`.                                      (4.7)

The remaining dimensionless factor in `K_tau` simplifies because

`c^(-c/2)x^(c/2)(1+x)^(-1/2)
 =(1+x)^(-1/(2(1+x)))`.                                             (4.8)

Define

`B(x)=(4pi)^alpha 2^(c-1)(1+x)^(-1/(2(1+x)))`,                      (4.9)

`K_0(x)=sqrt(2) B(x) exp(1/(2(1+x)))`.                              (4.10)

Then

`K_tau<=K_0(x)s^(-alpha)`.                                          (4.11)

Using

`alpha/(alpha-1)=(3+x)/(1-x)`,                                     (4.12)

Theorem 2.1 yields the clean target-scale statement:

### Theorem 4.1 — `QFORM-HEAVY-PLANE-STRICT-AUGMENTED-BL-v1`

If `x_*<1`, then for every `x` with `x_*<=x<1`,

`boxed:
 ||p_Q||_infinity <= C_aug(x)/s_3(A),
}`                                                                    (4.13)

where

`C_aug(x)= (3+x)/(pi(1-x))
 [K_0(x)]^(2(1+x)/(3+x)).`                                          (4.14)

This proves a linear small-ball estimate at the correct homogeneous scale, with no reciprocal physical minor.

For reference,

`C_aug(1/2)=30.05564799...`,
`C_aug(3/4)=64.42943154...`,
`C_aug(7/8)=133.45507519...`,
`C_aug(15/16)=271.62455155...`.                                     (4.15)

These constants are diagnostics; the theorem is the exact formula (4.14).

## 5. Critical independent-copy endpoint

The strict density constant necessarily deteriorates as `x->1-`, because `alpha->1+`.  However the assigned decoupled-time quantity does **not** deteriorate.

At `x=1`,

`c_0=1/2`, `alpha=1`,                                                (5.1)

and (3.7) becomes

`c_j=(eta_j+delta_j)/2`.                                             (5.2)

Hence if

`eta_j+delta_j<=1` for every row,                                    (5.3)

all physical BL exponents remain legal at the critical endpoint.  Equations (4.9)-(4.11) give

`K_tau<=2^(7/4) pi e^(1/4) s^(-1)`.                                (5.4)

Using (2.10),

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=(16/3) sqrt(2^(7/4) pi e^(1/4)) s^(-1/2)
 <19.646 s^(-1/2).
}`                                                                    (5.5)

Equivalently, by the exact Riesz identity,

`E|Q-Q'|^(-1/2)<7.838 s^(-1/2)`.                                    (5.6)

This is a genuinely stable whole-copy collision certificate at the boundary where the `L^1_t` proof becomes logarithmically critical.  No conjugate sum and difference are separately density-capped.  It does **not** by itself imply `L^infinity` for `Q`, so the full endpoint remains a structural rather than a collision-integrability debt.

## 6. Actual splice with the newest partner result

The partner r27 estimate (1.2) can be applied to **any** heavy physical row in this packet.  This gives the following quantitative alternative.

Fix

`0<theta<1/2`, `0<x_0<1`.                                           (6.1)

### Branch A — a noncancelled heavy row

If some heavy row satisfies

`|h_j|>=theta rho`,                                                  (6.2)

then partner r27 gives the actual inequality

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(60/theta)/s.
}`                                                                    (6.3)

This is the required application of the newest designated-partner result to a concrete inequality in the present proof.

### Branch B — all heavy rows cancel, but the augmented margin survives

Assume every heavy row satisfies

`|h_j|<theta rho`.                                                    (6.4)

Because `H_R>=m=rho y` and `y^2>1/2`,

`delta_j=h_j^2/H_R^2
 <theta^2/y^2<2theta^2<1/2`.                                        (6.5)

If `x_*<=x_0`, Theorem 4.1 gives

`boxed:
 ||p_Q||_infinity<=C_aug(x_0)/s.
}`                                                                    (6.6)

### Branch C — the only survivor is quantitatively near-coloop

If (6.4) holds but `x_*>x_0`, then some heavy row satisfies

`(2eta_j-1)/(1-2delta_j)>x_0`.

Hence

`eta_j>(1+x_0)/2-x_0 delta_j`

and, by (6.5),

`boxed:
 1-eta_j < (1-x_0)/2+2x_0 theta^2.
}`                                                                    (6.7)

Using (3.12), this is exactly

`boxed:
 sqrt(det(B_-j^T B_-j))/m
 <sqrt((1-x_0)/2+2x_0 theta^2).
}`                                                                    (6.8)

Thus failure of both proved analytic exits forces the same row to be simultaneously angularly cancelled and nearly a coloop of the entire right spectral plane.

A concrete universal split is

`theta=1/16`, `x_0=15/16`.                                          (6.9)

Branches A or B then satisfy

`||p_Q||_infinity
 <=max(128 sqrt(15),271.625)/s
 =128 sqrt(15)/s
 <495.742/s`.                                                        (6.10)

If neither branch applies, some heavy row obeys

`|h_j|<rho/16`,                                                      (6.11)

`eta_j>1969/2048=0.96142578125`,                                    (6.12)

and therefore

`sqrt(det(B_-j^T B_-j))/m<sqrt(79/2048)<0.19642`.                   (6.13)

The exact endpoint `eta_j=1` is already paid by fleet03/B14 r27 through (1.3).  Hence the first unpaid state has now been reduced from the entire heavy-plane angular-cancellation branch to the **strict near-coloop collar**

`0<1-eta_j<79/2048`, together with `|h_j|<rho/16`;                  (6.14)

and the parameters in (6.1) can make this collar arbitrarily thinner at the price of a larger, but still finite, already-proved constant outside it.

## 7. Why this advances the assigned decoupled-time mechanism

The previous grouped-hub Fresnel theorem immediately replaced `p_U` by its supremum `L`; in BL language that omitted the hub density from the exponent bookkeeping.  A heavy right-plane row then had leverage above `1/2` and blocked the source `L^p` characteristic-function estimate.

Theorem 2.1 instead adds the hub density as an **actual BL row**.  Its exponent `c_0` is paid by the interpolation

`||p_U||_(1/c_0)<=L^(1-c_0)`,                                       (7.1)

which is available because `p_U` is a genuine probability density, not a worst conditional cap.  The extra positive semidefinite Gram contribution lowers the heavy physical leverages by the exact formula (3.7).  At `c_0<1/2` this buys enough total time decay for `L^1_t`; at `c_0=1/2` it reaches the exact logarithmic boundary but still leaves the assigned weighted `L^2_t` collision integral uniformly finite.

This explains why the remaining obstruction is geometric rather than an exponent deficit: the only failure is when one physical row captures almost all of the right plane **and** the square direction allocates enough mass to that same row to neutralize the augmented Gram regularization.

## 8. Source-validity stress and what is not claimed

The critical collar cannot be deleted perturbatively.  Even at exact coloop one can choose a two-coordinate right plane with a physical row of leverage one and arrange the square direction so another row is the angular-cancellation row.  The augmented BL margin can then sit exactly at its critical value; fleet03/B14's real-space coloop theorem, not a perturbative Fourier deletion, is the valid payment.  Thus Section 6 deliberately leaves a **nonzero near-coloop collar** rather than claiming continuity of the exact-coloop proof in matrix coefficients under arbitrary unbounded input laws.

No target counterexample was found or claimed.  The new theorem proves a supporting branch and a stable independent-copy collision endpoint.  The full arbitrary-dimensional conjecture and global continuity remain open.

## 9. First unpaid implication after this run

`QFORM-HEAVY-ROW-STRICT-NEAR-COLOOP-AGGREGATE-v2`:

> In the one-sided exact-rank-three packet, assume a heavy right-plane row is angularly cancelled and has small but nonzero deletion area.  Combine the exact-coloop scalar localization with the augmented hub-density BL/collision estimate **before** any conditional fiber supremum, to obtain a constant stable as the deletion area tends to zero.  The residual transverse projection must remain inside the original product bank; it may not be discarded or replaced by an arbitrary dependent joint-density interface.

A natural next attack is a hybrid real/Fourier interpolation at the critical `c_0=1/2`: use (5.5) to pay the whole-copy half-Riesz collision while the exact-coloop theorem supplies the missing signed endpoint, and retain the small residual two-plane area through a product-bank Brascamp–Lieb integral rather than through a conditional projection density.

## 10. Status

- `QFORM-HUB-DENSITY-AUGMENTED-BL-v1`: **PROVED in stated scope**.
- `QFORM-HEAVY-PLANE-STRICT-AUGMENTED-BL-v1`: **PROVED in stated scope**.
- Critical whole-copy estimate (5.5): **PROVED**, dependence-safe, but not an `L^infinity` theorem by itself.
- Partner r27 applied at actual inequality (6.3): **APPLIED**.
- Exact-coloop endpoint: **already paid by source (1.3), not reproved here**.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Global continuity: **OPEN**.
