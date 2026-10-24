SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-22T22:52:16Z.
attacking: the general-angle off-zero maximum for the saturated opposite-sign two-heavy centered-interval stress family, seeking a global branch bound below 3*sqrt(2).

# account02/B17 — global off-zero exclusion for the saturated opposite-sign two-heavy plane

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B17-20260922T225216Z-r11-sat-offzero`  
Assignment: Sharp constant and witnesses  
Status: `NEW SUPPORTING THEOREM / FULL QFORM OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source pins

The unrestricted target remains open: independent real coordinates with densities at most one, arbitrary dimension, and real symmetric `A` with at least three eigenvalues of modulus at least one. Nothing here inserts moment, support, centering, or post-rotation independence assumptions into that full target.

Fresh owner control at invocation start was `yspennstate/math-research-brain@5733ca0e4607880ed32e682af76d984c53555475`; before the substantive write it was refreshed to `04edff7e43fb4b59d74d5d73f84d12926a4073af`. OWNER CONTROL remained revision `2026-09-22.15`, QFORM was the sole target, and no B17 pause/stop was present. The proof-first continuation and live correction state were consumed. This proof does not use the refuted arbitrary-joint coarea lemma, conditional-projection positive moments, worst scalar conditional-density gates, law-uniform pointwise oscillatory decay, or post-rotation independence.

The previous B17 theorem used below only for provenance of the finite stress family is `yspennstate/math-open-problems@3ebad57a9816b238c1f04dc3894971f10066d89b`, same account/slot, run `B17-20260922T214456Z-r11`.

The designated partner `account03/B17` was actually consumed from its immutable proof `yspennstate/math-open-problems@63f692146f592bc250af369056573dc5e3720a8e`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260922T221945Z-account03-B17-QFORM-r19/REPORT.md`. It proves that fully coupled three-diffuse-bank orientations can approach the `3sqrt(2)` obstruction with no coupling-only first-order gap. The theorem below attacks the complementary maximal-leverage geometry: two saturated opposite-sign-plane rows and one diffuse bank, and now closes its previously unpaid off-zero maximum.

## 2. Exact source-valid family

Let

`J=diag(1,1,-1)`,

`v1=(cos(theta),0,sin(theta))`,

`v2=(-sin(theta),0,cos(theta))`,

`w=(0,1,0)`.

For each `m>=1`, let the `(m+2) x 3` frame `R_m` have rows `v1,v2` and `m` copies of `w/sqrt(m)`. Then exactly

`R_m^T R_m=I_3`,

so

`A_{m,theta}=R_m J R_m^T`

has exact nonzero spectrum `{1,1,-1}` for every finite `m`. Put independent `Uniform[-1/2,1/2]` laws on every physical coordinate. If `X,Y` are the two heavy coordinates and

`S_m=m^(-1/2) sum_{k=1}^m U_k`,

then

`Q_{m,theta}=q_theta(X,Y)+S_m^2`,

`q_theta(x,y)=cos(2theta)(x^2-y^2)-2sin(2theta)xy`.

As `m->infinity`, `S_m` converges locally in density to `G~N(0,1/12)`. The limiting branch is

`Q_theta=q_theta(X,Y)+G^2`.

The density of `G^2` is

`h(u)=sqrt(6/pi) u^(-1/2) exp(-6u) 1_{u>0}`.                    (2.1)

## 3. A uniform logarithmic density envelope for every heavy-plane angle

### Lemma 3.1

For every `theta`, the density `f_theta` of `q_theta(X,Y)` satisfies, for `s!=0`,

`f_theta(s) <= L(s):=log(1/|s|) 1_{|s|<1}`.                  (3.1)

### Proof

Rotate `(X,Y)` to spectral coordinates `(Z1,Z3)` so that

`q_theta=Z1^2-Z3^2`.

Now set

`U=Z1-Z3`, `V=Z1+Z3`.

The map `(Z1,Z3)->(U,V)` has determinant magnitude two. Since `(X,Y)` has density one on the unit square, `(U,V)` has density `1/2` on a rotated square `P` of area two. Moreover `X^2+Y^2<=1/2`, so by Cauchy

`|U|,|V|<=sqrt(2)sqrt(Z1^2+Z3^2)<=1`; hence `P subset [-1,1]^2`.

Because `q_theta=UV`, the standard product-density formula gives

`f_theta(s)=(1/2) int_R 1_P(u,s/u) du/|u|`.

The box containment forces `|s|<=|u|<=1`. Therefore

`f_theta(s) <= (1/2)*2 int_|s|^1 du/u = log(1/|s|)`

for `0<|s|<1`, and the right side is zero outside the stated envelope. `QED`

This step uses a rotation only to compute the law of one explicit two-variable product source; it does not transfer independence to rotated coordinates in the full conjecture.

## 4. Global convolution theorem: the off-zero peak is also below `3sqrt(2)`

Define

`I(t)=(L*h)(t)=int_0^infinity h(u)L(t-u) du`.                  (4.1)

By Lemma 3.1 and positivity,

`p_{Q_theta}(t) <= I(t)`                                      (4.2)

for every `theta,t`.

### Lemma 4.1 — the logarithmic majorant is globally maximized at zero

For all real `t`,

`I(t)<=I(0)`.                                                  (4.3)

### Proof

For `t=-a<=0`, if `a>=1` then `I(t)=0`. If `0<=a<1`,

`I(-a)=int_0^(1-a) h(u) log(1/(a+u)) du <= int_0^1 h(u)log(1/u)du=I(0)`.

Now let `0<t<1`. Since the logarithmic kernel vanishes at `|t-u|=1`, differentiation of the improper logarithmic integral gives

`I'(t)=PV int_0^(t+1) h(u)/(u-t) du`.                         (4.4)

The full principal-value transform is explicit:

`PV int_0^infinity h(u)/(u-t) du
 =-sqrt(6/pi)*pi*t^(-1/2)*exp(-6t)*erfi(sqrt(6t)) <0`.         (4.5)

For completeness, substitute `u=x^2` and use

`PV int_0^infinity exp(-beta x^2)/(x^2-a^2) dx
 =-(pi/(2a)) exp(-beta a^2) erfi(a sqrt(beta))`,

which follows from the elementary Gaussian resolvent formula by analytic continuation (or equivalently from the Dawson integral identity).

The omitted tail in (4.4) is positive because `u>t+1>t`; hence

`I'(t)=PV int_0^infinity h(u)/(u-t)du - int_(t+1)^infinity h(u)/(u-t)du <0`.

Thus `I` decreases strictly on `(0,1)`. For `t>1`,

`I(t)=int_(-1)^1 L(s) h(t-s) ds`,

and `h` is strictly decreasing on `(0,infinity)`, so `I` again decreases in `t`. Continuity at `t=1` finishes (4.3). `QED`

### Theorem 4.2 — saturated opposite-sign heavy plane, global no-escape

For every angle `theta`,

`||p_{Q_theta}||_infinity <= C_log`,                          (4.6)

where

`C_log=sqrt(6/pi) int_0^1 u^(-1/2)e^(-6u)log(1/u)du
      =3.7553425409647818916... <3sqrt(2)`.                    (4.7)

The decimal is a deterministic check only. A simple analytic strict comparison is as follows. Differentiating the gamma integral at `1/2` gives

`sqrt(6/pi) int_0^infinity u^(-1/2)e^(-6u)log(1/u)du
 = gamma_E + log(24)`.

Therefore

`C_log=gamma_E+log(24)+T`,

`T=sqrt(6/pi) int_1^infinity u^(-1/2)e^(-6u)log(u)du`.

For `u>=1`, `log u<=u` and `sqrt(u)<=u`, so using `sqrt(6/pi)<3/2` and `e^6>400`,

`0<T<(3/2) int_1^infinity u e^(-6u)du
      =(3/2)*(7/36)e^(-6)<1/1000`.

The elementary bounds `gamma_E<0.6` and `log 24<3.2` yield

`C_log<3.801<4.2<3sqrt(2)`.

Combining (4.2)-(4.7) proves the theorem. `QED`

This closes the off-zero gap left by the previous B17 theorem: no output location and no heavy-plane angle in this saturated centered-interval branch can reach the diffuse obstruction `3sqrt(2)`.

## 5. Uniform return to exact finite target matrices

Let `g_m` be the density of `S_m` and `g` that of `G`. The elementary local CLT for centered bounded uniforms gives

`delta_m:=||g_m-g||_infinity ->0`.

The square densities satisfy

`|h_m(u)-h(u)|<=delta_m u^(-1/2)`, `u>0`.                     (5.1)

Using (3.1), for every `theta,t`,

`|p_{Q_{m,theta}}(t)-p_{Q_theta}(t)|
 <=delta_m J(t)`,

`J(t)=int_(-1)^1 L(s)(t-s)_+^(-1/2) ds`.                      (5.2)

The bound is uniform. For `-1<=t<=2`, Holder with exponents `3` and `3/2` gives

`J(t)<=||L||_3 ||x^(-1/2)1_(0,3)(x)||_(3/2)
      =(12)^(1/3)(4*3^(1/4))^(2/3)=4sqrt(3)`.

For `t>2`, `J(t)<=2`, and for `t<-1`, `J(t)=0`. Hence

`sup_(theta,t)|p_{Q_{m,theta}}(t)-p_{Q_theta}(t)| <=4sqrt(3) delta_m ->0`.   (5.3)

Consequently

`limsup_(m->infinity) sup_theta ||p_{Q_{m,theta}}||_infinity <= C_log <3sqrt(2)`.  (5.4)

Thus the exclusion is not merely a Gaussian relaxation: it is approached uniformly by exact finite cap-one product sources and exact matrices with nonzero spectrum `{1,1,-1}`.

## 6. Application of the completed designated-partner result

The current account03/B17 theorem says a qualitatively fully coupled all-diffuse three-bank orientation can approach `3sqrt(2)` with first-order deficit arbitrarily close to the diagonal-bank optimum; nonzero coupling alone gives no fixed gap. The present theorem gives the complementary statement at maximal two-row leverage: after two opposite-sign-plane directions are saturated by physical coordinates and the third direction is diffuse, an angle-uniform **global**, not merely central, gap remains:

`3sqrt(2)-C_log =0.4872981461545032548...`.

Taken together, these results sharpen the stress geometry. Near-sharp witnesses can be fully coupled when all three active directions remain diffuse, but this particular attempt to concentrate two active directions into saturated heavy rows loses a fixed amount even after optimizing the output location. A witness above `3sqrt(2)`, if it exists, must leave both solved mechanisms—for example through intermediate/mesoscopic leverage, fragmented nonuniform heavy laws, three-or-more interacting macroscopic rows, non-Gaussian residual banks, or additional spectral directions.

This is a supporting branch theorem, not a proof that `3sqrt(2)` is the universal sharp constant and not a proof of the full conjecture.

## 7. Deterministic checks

The sibling checker records the gamma-integral value, tail identity, strict gap to `3sqrt(2)`, and representative direct angular-convolution evaluations. No histogram or Monte Carlo is used. The analytic proof above does not depend on the decimal evaluation.
