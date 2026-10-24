# account02/B03 early checkpoint — hub-density-augmented Brascamp–Lieb

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T061506Z-account02-B03-QFORM-auto11`  
Assignment: Decoupled time integral.  
Status at checkpoint: new supporting calculation proved; full target open.

The first unpaid implication attacked is the heavy-right-plane angular-cancellation state left by account03/B03 r27 and account03/B14 r27.  The mechanism change is to keep the **actual density of the grouped hub** inside the two-dimensional Fourier/Brascamp–Lieb integral instead of replacing it immediately by its `L^infinity` norm.  This creates one extra geometric BL row and can lower a heavy right-plane leverage before the final time integral.

## 1. General augmented-row estimate

Let `Y=(Y_j)` have independent cap-one coordinates and let `Omega` be independent of `Y`.  Let `U=U(Omega)` have a probability density `p_U<=L`.  Allow arbitrary measurable `xi(Omega),F(Omega)` with arbitrary dependence on `U`.  Let `h,v in R^m` be linearly independent and let `A d !=0`.  For arbitrary one-coordinate phases `phi_j`, put

`T=A(h.Y+xi(Omega))^2+2d U(Omega)(v.Y)+F(Omega)+sum_j phi_j(Y_j)`.

For the fixed final frequency `t`, write

`Psi_j(r)=int f_j(z) exp(i t phi_j(z)) exp(i r z) dz`.

The damped Fresnel identity from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives

`|phi_T(t)| <= (4 pi |t A|)^(-1/2) (2|t d|)^(-1)
  int_R2 p_U(eta/(2|t d|)) prod_j |Psi_j(s h_j+eta v_j)| ds deta`.    (1)

No pointwise quadratic-phase decay is used.

Fix `tau>0` and add the auxiliary frequency row

`b_0=(0,tau)`, `b_j=(h_j,v_j)`,
`G_tau=sum_{j>=0} b_j b_j^T`.

Put

`c_k=b_k^T G_tau^(-1)b_k`.

The normalized rows form a tight frame and `sum_k c_k=2`.  Assume

`c_j<=1/2` for every physical product row `j>=1`.                     (2)

No restriction `c_0<=1/2` is needed for the hub density because `p_U` is controlled directly in every `L^p` by interpolation between mass one and the cap `L`.

Apply geometric rank-one Brascamp–Lieb to all rows.  For the physical rows, the source `L^p` lemma

`int |Psi_j|^p <= 4 pi/sqrt(p),  p>=2`

is applicable by (2).  For the auxiliary row, with `T_0=2|td|`,

`int p_U(r/(tau T_0))^(1/c_0) dr
 <= tau T_0 L^(1/c_0-1)`.

After the exact BL cancellations,

`int_R2 p_U(eta/T_0) prod_j |Psi_j(s h_j+eta v_j)| ds deta`
`<= det(G_tau)^(-1/2) (4pi)^(2-c_0)c_0^(-c_0/2)
    (tau T_0)^c_0 L^(1-c_0)`.                                      (3)

Thus, with

`a_t=3/2-c_0`,

`|phi_T(t)| <= min(1,K_tau |t|^(-a_t))`,                             (4)

where

`K_tau=(4pi)^(3/2-c_0) 2^(c_0-1)c_0^(-c_0/2)
       |A|^(-1/2)|d|^(c_0-1) tau^c_0 L^(1-c_0)
       det(G_tau)^(-1/2)`.                                          (5)

If `c_0<1/2`, then `a_t>1` and Fourier inversion gives the genuine linear-small-ball estimate

`||p_T||_infinity <= [a_t/(pi(a_t-1))] K_tau^(1/a_t)`.               (6)

At the critical endpoint `c_0=1/2`, (4) is only `O(|t|^-1)` and is not absolutely integrable, but the assigned whole-copy collision integral is still finite:

`int |t|^(-1/2)|phi_T(t)|^2 dt
 <= [4+2/(2a_t-1/2)] K_tau^(1/(2a_t))`.                              (7)

Equation (7) is obtained by splitting at `|t|=K_tau^(1/a_t)`.  It uses the characteristic function of the whole random variable; no sum/difference pair is separated or declared independent.

## 2. Exact leverage algebra for the one-sided packet

In the account03/B03 r27 packet, on the right bank

`h=beta v+m q`, `v perp q`, `||v||=||q||=1`, `m>0`.

Put `H^2=beta^2+m^2`,

`eta_j=v_j^2+q_j^2`, `delta_j=h_j^2/H^2`,

so `sum eta_j=2`, `sum delta_j=1`, and `delta_j<=eta_j` because `h/H` is a unit vector in `span(v,q)`.

Let

`x=H^2 tau^2/m^2`.

A direct inverse of the two-by-two Gram matrix gives

`det G_tau=m^2(1+x)`,
`c_0=x/(1+x)`,
`c_j=(eta_j+x delta_j)/(1+x)`.                                      (8)

Therefore every nonheavy row `eta_j<=1/2` is automatically admissible.  A heavy row is admissible exactly when

`x >= (2 eta_j-1)/(1-2 delta_j)`                                    (9)

provided `delta_j<1/2`.  Define the exact augmented-BL obstruction parameter

`x_* = max_{eta_j>1/2} (2eta_j-1)/(1-2delta_j)`

(with `x_*=0` if there is no heavy row).  Whenever `x_*<1`, one can choose `x in [x_*,1)` and obtain an integrable estimate (6).  The boundary `x_*=1` is precisely a simultaneous heavy-leverage/square-alignment collar, not merely `eta_j>1/2`.

The deletion geometry is explicit:

`det G_{-j}=m^2(1-eta_j)`.

Thus `eta_j+delta_j>=1` is equivalent to

`|h_j|/H >= sqrt(1-eta_j)`,                                         (10)

i.e. the physical square coefficient is at least the normalized residual two-plane area after deleting the same row.  This identifies the only place where the present augmentation can become critical.

## 3. Target-scale normalization

For the one-sided exact-rank-three packet put `s=s_3(A)`.  The source geometry supplies

`gamma |sigma|>=s^2`,
`gamma sigma^2=s_1(A)s_2(A)s_3(A)>=s^3`,
`m=rho y`, `y^2>1/2`, `gamma=rho^2/|a|`.

In (5), with `A=1/a`, `d=sigma`, the matrix-scale denominator is

`D=|a|^(-1/2)|sigma|^(1-c_0)m^(1-c_0)H^c_0`
` =[sigma^2m^2/|a|]^((1-c_0)/2)[H^2/|a|]^(c_0/2)`.

Since `H>=m`,

`D >= gamma^(1/2)|sigma|^(1-c_0)y`.

The two spectral inequalities imply, for every `0<=c_0<=1/2`,

`gamma^(1/2)|sigma|^(1-c_0) >= s^(3/2-c_0)`.                       (11)

Indeed after writing `gamma=s g`, `|sigma|=s r`, the constraints are `gr>=1`, `gr^2>=1`; if `r>=1` use `g>=1/r`, while if `r<=1` use `g>=1/r^2`.

Hence with `a_t=3/2-c_0`,

`D>=s^a_t y`.                                                       (12)

So every strict augmented-BL branch is genuinely target-homogeneous: (6) is `C/s`, not a reciprocal tiny physical-minor bound.

At the critical choice `x=1` one has `c_0=1/2`, `a_t=1`.  If `eta_j+delta_j<=1` for all `j`, then (7), `L<=sqrt(e)` and `y>1/sqrt(2)` give the explicit dependence-safe endpoint

`int |t|^(-1/2)|phi_Q(t)|^2 dt
 <= 19.646 s^(-1/2)`.                                               (13)

This is not yet an `L^infinity` conclusion at the critical collar; it is a finite whole-copy half-Riesz collision certificate.  Away from the collar, any fixed strict margin gives a linear-small-ball estimate by (6).

Next in this run: splice (6) with account03/B03 r27's physical-row receiver.  That receiver pays a row with `|h_j|>=theta rho`; the new augmentation pays the complementary cancellation state unless the same row is also quantitatively near-coloop in the sense (10).  This should reduce the first unpaid implication to a narrow near-coloop collar, with account03/B14 r27 already paying its exact-zero-area endpoint.
