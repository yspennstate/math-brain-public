SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-22T21:42:06Z.
attacking: the off-zero maximum in the saturated noncollinear two-heavy family, starting from the maximal-cross angle and then a quantitative angle wedge.

# Addendum — global maximal-cross bound and a global limiting angle wedge

Status: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL QFORM OPEN`. Full-target continuity remains separately open. Execution memory: `WITHOUT_VERIFIED_BRAIN`.

This addendum preserves the pre-existing immutable run report and adds a distinct theorem derived after consuming the newly completed designated-partner result fleet02/B17 `QFORM-SATURATED-OPPOSITE-HEAVY-ZERO-v1`, canonical proof `yspennstate/math-open-problems@3ebad57a9816b238c1f04dc3894971f10066d89b:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/B17-20260922T214456Z-r11/REPORT.md`.

The partner supplies the exact source-valid family, for every angle `theta`, with heavy rows

`v1=(cos theta,0,sin theta)`, `v2=(-sin theta,0,cos theta)`

and `m` diffuse rows `e2/sqrt(m)`. Thus `R_m^T R_m=I_3` and `A_m=R_m diag(1,1,-1)R_m^T` has nonzero spectrum exactly `{1,1,-1}` at every finite `m`. For independent physical `Uniform[-1/2,1/2]` inputs,

`Q_{m,theta}=q_theta(X,Y)+S_m^2`,

`q_theta=cos(2theta)(X^2-Y^2)-2sin(2theta)XY`,

`S_m=m^(-1/2) sum_{j=1}^m U_j`.

The partner proves `p_theta(0)<=C_sat<3sqrt(2)` for every `theta` and leaves the off-zero maximum for general `theta` as the first unpaid successor. The results below attack precisely that successor.

## A. Finite-dimensional global theorem at `theta=pi/4`

At the maximal-cross angle, `q_{pi/4}(X,Y)=-2XY`.

### Theorem A (`QFORM-SATURATED-CROSS-FINITE-GLOBAL-v1`)

For every integer `m>=1`, the exact finite target family above satisfies

`boxed( ||p_{Q_{m,pi/4}}||_infinity <= 3sqrt(2) ).`

Let `Z=-2XY`. Its exact density is `f_Z(z)=-log(2|z|) 1_{0<|z|<1/2}`. Hence

`||f_Z||_4^4=2 int_0^(1/2)[-log(2z)]^4 dz=int_0^1(-log u)^4du=24`,

so `||f_Z||_4=24^(1/4)`.

Let `g_m` be the density of `S_m`. It is symmetric, and Ball's cube-slicing theorem applied to the unit Euclidean coefficient vector `(1/sqrt(m),...,1/sqrt(m))` gives `M_m:=||g_m||_infinity<=sqrt(2)`.

The density `h_m` of `S_m^2` is `h_m(y)=g_m(sqrt(y))/sqrt(y)`, `y>0`, and

`||h_m||_(4/3)^(4/3)=2 int_0^infinity g_m(x)^(4/3)x^(-1/3)dx`.

Since `g_m^(4/3)<=M_m^(1/3)g_m`, and the decreasing weight `x^(-1/3)` is maximized under `0<=g<=M_m`, `int_0^infinity g=1/2` by the bathtub profile `M_m 1_[0,1/(2M_m)]`,

`||h_m||_(4/3)^(4/3) <= 3*2^(-2/3) M_m^(2/3)`.

Thus

`||h_m||_(4/3) <=3^(3/4)2^(-1/2)M_m^(1/2) <=3^(3/4)2^(-1/4)`.

Young's convolution inequality now gives

`||p_{Q_{m,pi/4}}||_infinity <=24^(1/4) 3^(3/4)2^(-1/4)=3sqrt(2)`.

No equality claim is made for the actual finite family. This is global in the output location and finite-dimensional, not merely a limiting zero-density estimate.

## B. Strict global angle wedge in the diffuse Gaussian limit

Let `Q_theta=q_theta(X,Y)+G^2`, where `G~N(0,1/12)` is independent of centered unit-interval `X,Y`. This is the partner family's diffuse-bank limit.

### Theorem B (`QFORM-SATURATED-CROSS-WEDGE-GLOBAL-v1`)

If `|cos(2theta)|<=2/5`, then

`boxed( ||p_{Q_theta}||_infinity <= C_wedge <3sqrt(2) )`,

where, with `L=log(7/5)`,

`C_wedge=[L^4+4L^3+12L^2+24L+24]^(1/4)*sqrt(6/pi)*Gamma(1/3)^(3/4)/8^(1/4)`
`       =4.142687005720009...`.

At `theta=pi/4`, the sharper limiting bound is `3.808492147724579...`.

Factor the indefinite part by

`u=(cos theta-sin theta)X-(sin theta+cos theta)Y`,
`v=(cos theta+sin theta)X+(cos theta-sin theta)Y`.

Then `q_theta=uv`. The map `(X,Y)->(u,v)` has orthogonal rows of norm `sqrt(2)` and determinant `2`, so `(u,v)` is uniform with density `1/2` on a centered square `P_theta` of area `2`.

Set `K=(1+|cos(2theta)|)/2`. The coordinate half-width of `P_theta` is `sqrt(K)`, hence `P_theta subset[-sqrt(K),sqrt(K)]^2`. Also `u^2+v^2=2(X^2+Y^2)<=1`, so `|uv|<=1/2` on `P_theta`.

If `f_theta` denotes the density of `q_theta`, then for `z!=0`,

`f_theta(z)=(1/2) int 1_{(u,z/u) in P_theta} du/|u| <=log(K/|z|) 1_{|z|<1/2}`.

Writing `ell=log(2K)>=0`,

`||f_theta||_4^4 <=int_0^1[ell-log x]^4dx =ell^4+4ell^3+12ell^2+24ell+24`.  (B.1)

The density of `G^2` is `h(y)=sqrt(6/pi)y^(-1/2)e^(-6y)1_{y>0}`, so

`||h||_(4/3)=sqrt(6/pi)*Gamma(1/3)^(3/4)/8^(1/4)`.  (B.2)

Young's inequality applied to `p_{Q_theta}=f_theta*h` proves the claimed expression. Under `|cos(2theta)|<=2/5`, `K<=7/10` and `ell<=log(7/5)`.

For an elementary strict certification use `log(7/5)<337/1000`, `Gamma(1/3)<11/4`, `pi>157/50`. The logarithm bound follows from the cubic Taylor lower bound for `e^x` at `x=337/1000`. For the Gamma bound, the degree-six alternating Taylor polynomial upper-bounds `e^{-t}` on `[0,1]`, giving

`int_0^1 t^(-2/3)e^(-t)dt <=8042117/3319680`.

On `[1,infinity)`, splitting at two gives

`int_1^infinity t^(-2/3)e^(-t)dt <=e^(-1)-(1-2^(-2/3))e^(-2) <46/125-37/900`,

using `e>1957/720>125/46`, `e<3`, and `2^(-2/3)<63/100`. Thus

`Gamma(1/3)<684546263/248976000<11/4`.

For `P(x)=x^4+4x^3+12x^2+24x+24`,

`P(337/1000)=33616816929761/10^12`,

and

`324-P(337/1000)*(9/2)*(11/4)^3/(157/50)^2 =6201481198392981/1262028800000000>0`.

Since `(3sqrt(2))^4=324`, this certifies `C_wedge<3sqrt(2)`. At `theta=pi/4`, `K=1/2`, `ell=0`, and (B.1) is the exact identity `||f||_4^4=24`, giving the displayed `3.808492...` limiting bound.

## C. What changed and what remains

The designated partner's all-angle theorem excluded the central peak of this saturated opposite-sign two-heavy family. This addendum resolves its off-zero problem on a nontrivial portion: the maximal-cross angle is excluded globally for every finite source-valid bank size, and the diffuse limiting family is excluded globally and strictly on the band `|cos(2theta)|<=2/5`.

The remaining branch is the global off-zero maximum for `|cos(2theta)|>2/5`, especially the transition to aligned geometry, followed by arbitrary fragmented heavy laws, three-or-more macroscopic rows, non-Gaussian residual banks, finite/mesoscopic overshoot, and additional spectral directions.

Standing corrections remain in force. No arbitrary-joint coarea estimate, conditional-density cap/moment, law-uniform pointwise oscillatory decay, scalar worst-conditioning, fixed-fragment reduction, or independence after a general spectral rotation is used. The full QFORM conjecture and full continuity conclusion remain OPEN.
