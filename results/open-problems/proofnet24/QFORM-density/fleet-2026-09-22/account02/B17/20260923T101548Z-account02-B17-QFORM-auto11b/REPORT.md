SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T10:15:48Z.
attacking: after the one-heavy equal-bank branch and finite-activity diffuse fragments were excluded, test a genuinely two-heavy/shared-coordinate exact-spectrum family with a critically fragmented bank.

# QFORM B17 — lightlike two-heavy forms are stable under Gaussian shifts and growing-activity fragmentation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING THEOREM / SHARP-WITNESS NO-ESCAPE**. The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity for the full target remains separate.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target family

For every `m>=2`, let `b_m=(m^{-1/2},...,m^{-1/2}) in R^m` and let `R_m` be the `(m+2) x 3` matrix with columns the first two physical coordinate vectors and `(0,0,b_m)`. Thus

`R_m^T R_m=I_3`.

Put

`B=[[1/2,-1/2,-1/sqrt(2)],[-1/2,1/2,-1/sqrt(2)],[-1/sqrt(2),-1/sqrt(2),0]]`.

Writing `u=(1/2,1/2,1/sqrt(2))^T`, one has `B=I-2uu^T`, hence `B^2=I` and

`spec(B)={1,1,-1}`.

Define the physical matrix

`A_m=R_m B R_m^T`.

Since `R_m` is an isometry onto its three-dimensional range, every finite `A_m` has **exact nonzero spectrum**

`{1,1,-1}`.

Let the first two physical variables `X_{1,m},X_{2,m}` be arbitrary independent real variables with probability densities bounded by one, and let the remaining `m` bank variables be independent of them. Put

`U_m=(X_{1,m}+X_{2,m})/sqrt(2)`, `V_m=(X_{1,m}-X_{2,m})/sqrt(2)`.

The orthogonal heavy-plane change has Jacobian one, so `(U_m,V_m)` has a joint probability density `rho_m<=1`; **no independence of `U_m,V_m` is asserted or used**. If `S_m` is the normalized bank sum, then exactly

`Q_m=X^T A_m X = V_m^2-2U_m S_m`.                                      (1.1)

Thus this is a genuinely nonseparable source-valid rank-three family with two macroscopic physical coordinates coupled to every bank coordinate.

## 2. Analytic extension of the completed partner theorem

The completed `account03/B17` r22 theorem is

`math-open-problems@ba000d70d1d4f523a2396155a24d5088d5c94802`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T021034Z-account03-B17-QFORM-r22/REPORT.md`.

It proves, for an arbitrary joint probability density `rho(u,v)<=1` and independent `G_0~N(0,sigma_0^2)`, `sigma_0^2=1/12`,

`||p_{V^2-2UG_0}||_infinity <= C_x`,

where

`C_x=2^(13/6) sqrt(3/pi) Gamma(5/4)^(2/3)=4.109270566451296...<3sqrt(2)`.    (2.1)

Its proof actually yields the following stronger shift/variance-stability statement.

### Theorem `QFORM-LIGHTLIKE-GAUSSIAN-SHIFT-STABILITY-v1`

Let `(U,V)` have any joint probability density `rho<=1`. Let `G_sigma~N(0,sigma^2)` and let `H` be an arbitrary real random variable, with `(G_sigma,H)` independent of `(U,V)` and `G_sigma` independent of `H`. If `sigma>=sigma_0=1/sqrt(12)`, then

`boxed( ||p_{V^2-2U(G_sigma+H)}||_infinity <= C_x (sigma_0/sigma)^(2/3) )`.   (2.2)

In particular the right side is always strictly below `3sqrt(2)`.

### Proof

Condition on `H=h`. For fixed `(u,v)`, `u!=0`, the conditional density at output `s` is

`K_{s,h}(u,v)=c_sigma/|u| * exp[-a_sigma (v^2-s-2uh)^2/u^2]`,              (2.3)

with

`c_sigma=1/(2 sigma sqrt(2pi))`, `a_sigma=1/(8 sigma^2)`.

For `delta>0` and every real center `c`, the exact elementary level-set estimate used in r22 is

`|{v: |v^2-c|<delta}| <= 2sqrt(2delta)`.                                 (2.4)

Crucially, (2.4) is **uniform in `c`**. Hence the r22 superlevel calculation is unchanged when `c=s+2uh`. It gives

`|{(u,v): K_{s,h}(u,v)>lambda}| <= D_sigma lambda^(-3/2)`,                (2.5)

uniformly in both `s` and `h`, where

`D_sigma = D_0 (sigma_0/sigma)`.                                         (2.6)

Indeed the r22 formula is proportional to `a_sigma^(-1/4)c_sigma^(3/2)`, which scales as `sigma^(1/2)sigma^(-3/2)=sigma^(-1)`.

Layer cake and `rho<=1`, `int rho=1`, now give

`p(s) <= int_0^infinity min(1,D_sigma lambda^(-3/2)) dlambda
      =3 D_sigma^(2/3)
      =C_x (sigma_0/sigma)^(2/3)`.                                      (2.7)

The estimate is uniform in `h`, so averaging over the arbitrary law of `H` proves (2.2). This uses the partner's completed two-dimensional weak-`L^(3/2)` mechanism in its actual scope; it does not use post-rotation independence or an arbitrary-joint quadratic coarea theorem.

## 3. Application of the newest completed partner result: finite activity

The latest completed `account03/B17` result read in this invocation is

`math-open-problems@5f4048aeb8c04ee61aa695b961ca8ae213dc3293`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T100331Z-account03-B17-QFORM-auto11/REPORT.md`.

Among its proved ingredients is a weighted one-bank local limit for the cap-one remote-fragment law with probability `lambda/m` in an interval centered at `a sqrt(m)`: the normalized bank converges locally, with polynomial control, to

`G_0+aN`, `G_0~N(0,1/12)`, `N~Poisson(lambda)`, independent.              (3.1)

Apply this **completed partner local limit** not to the partner's three-bank matrix, but to the exact lightlike two-heavy matrix (1.1). The transfer estimate from r22 is uniform over every heavy-plane density `rho_m<=1`; conditional on `N`, Theorem (2.2) with `sigma=sigma_0` and `H=aN` gives the common ceiling `C_x`. Therefore the corresponding exact finite source-valid fragmented family satisfies

`boxed( limsup_m ||p_{Q_m}||_infinity <= C_x <3sqrt(2) )`.                (3.2)

This is a real cross-result application: the newest partner's Gaussian-plus-Poisson bank theorem supplies the bank limit, while the present shifted weak-`L^(3/2)` inequality supplies the output obstruction in a different, two-heavy shared-coordinate matrix geometry.

## 4. New growing-activity adversary

Finite activity leaves open the natural bridge `lambda_m->infinity`. Fix `a>0` and take any sequence

`lambda_m->infinity`, `lambda_m=o(m)`.

Set

`epsilon_m=lambda_m/m`, `D_m=a sqrt(m/lambda_m)`.                         (4.1)

For all sufficiently large `m`, the three intervals below are disjoint. Put

`I=[-1/2,1/2]`,

`R_{m,+}=[D_m-epsilon_m/4,D_m+epsilon_m/4]`,
`R_{m,-}=[-D_m-epsilon_m/4,-D_m+epsilon_m/4]`,

and define the physical one-coordinate probability density

`f_m(x)=(1-epsilon_m) 1_I(x)+1_{R_{m,+}}(x)+1_{R_{m,-}}(x)`.             (4.2)

Each remote interval has length `epsilon_m/2`, so

`0<=f_m<=1`, `int f_m=1`.                                                (4.3)

The law is symmetric, highly disconnected, and its support diameter tends to infinity. There is no hidden fixed-support, moment-uniformity, log-concavity or connected-support assumption.

Let the bank consist of `m` iid variables with density `f_m`, and put

`S_m=m^(-1/2) sum_{k=1}^m W_{m,k}`.                                      (4.4)

The exact row variance is

`v_m=(1-epsilon_m)/12 + epsilon_m(D_m^2+epsilon_m^2/48)`
`   =1/12+a^2-lambda_m/(12m)+lambda_m^3/(48m^3)`,                        (4.5)

so

`v_m -> sigma_a^2:=1/12+a^2`.                                           (4.6)

Moreover every row is centered and

`max |W_{m,k}|/sqrt(m) <= a/sqrt(lambda_m)+o(1) ->0`.                    (4.7)

Thus the triangular-array Lindeberg condition holds deterministically and

`S_m => G_a~N(0,sigma_a^2)`.                                            (4.8)

The pointwise CLT is not enough for a density-peak conclusion. The next section proves the required uniform local limit.

## 5. Uniform local limit for the growing fragmented bank

Write `sinc x=sin(x)/x`. The one-row characteristic function is exactly

`phi_m(s)=(1-epsilon_m)sinc(s/2)
          +epsilon_m sinc(epsilon_m s/4) cos(D_m s)`.                    (5.1)

The normalized-bank characteristic function is

`psi_m(t)=phi_m(t/sqrt(m))^m`.                                           (5.2)

### 5.1 Integrable domination and tail control

For `|s|<=1`, the alternating Taylor series gives the crude bound

`sinc(s/2)<=1-s^2/30`.

For large `m`, `epsilon_m<=1/2`, so

`|phi_m(s)|<=exp(-s^2/60)`, `|s|<=1`,                                   (5.3)

and therefore

`|psi_m(t)|<=exp(-t^2/60)`, `|t|<=sqrt(m)`.                              (5.4)

Let

`q=max_{1<=|s|<=12}|sinc(s/2)|<1`, `q_1=(1+q)/2<1`.

For all large `m`,

`|phi_m(s)|<=q_1`, `1<=|s|<=12`.                                        (5.5)

For `12<=|s|<=4/epsilon_m`, using `|sinc(s/2)|<=2/|s|` and the trivial bound on the remote sinc factor,

`|phi_m(s)|<=1/6+epsilon_m<=1/3`.                                       (5.6)

Finally, for `|s|>=4/epsilon_m`,

`|phi_m(s)|<=2/|s|+4/|s|=6/|s|`.                                       (5.7)

After the substitution `t=sqrt(m)s`, (5.5)-(5.7) imply

`int_{|t|>sqrt(m)} |psi_m(t)| dt ->0`;                                  (5.8)

indeed the three pieces are bounded respectively by

`O(sqrt(m) q_1^m)`,
`O(sqrt(m) epsilon_m^(-1) 3^(-m))`,

and

`[8sqrt(m)/(epsilon_m(m-1))] (3epsilon_m/2)^m`,                          (5.9)

all of which tend to zero.

Together with pointwise convergence from (4.8), (5.4) and dominated convergence give

`boxed( int_R |psi_m(t)-exp(-sigma_a^2 t^2/2)| dt ->0 )`.                (5.10)

Fourier inversion therefore yields the uniform local limit

`delta_m:=||h_m-gamma_{sigma_a}||_infinity ->0`,                         (5.11)

where `h_m` is the density of `S_m`.

### 5.2 Required newest-Claude result applied to a real inequality

Lemma 1 of the required pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,

proves for every cap-one probability density `f` and every `p>=2`

`int |hat f(s)|^p ds <=4pi/sqrt(p)`.                                    (5.12)

Apply it to the **actual fragmented physical row density** `f_m` with `p=m`. Since (5.2) is the characteristic function of the normalized sum,

`int |psi_m(t)| dt
 =sqrt(m) int |hat f_m(s)|^m ds
 <=4pi`.                                                                (5.13)

Hence Fourier inversion gives the uniform bank-density cap

`boxed( ||h_m||_infinity<=2 )`.                                         (5.14)

This is the concrete newest-Claude inequality used below. It is not a pointwise stationary-phase bound and it keeps the original cap-one product source.

## 6. Uniform transfer through the two-heavy kernel

For a probability density `h` on the bank variable define, for an arbitrary heavy-plane density `rho<=1`,

`P_h(s)=iint rho(u,v) [1/(2|u|)] h((v^2-s)/(2u)) du dv`.                 (6.1)

The partner r22 estimate proves that if `||h||_infinity<=M`, then for every `u!=0`, uniformly in `s`,

`int_R [1/(2|u|)] h((v^2-s)/(2u)) dv <= sqrt(2M/|u|)`.                   (6.2)

Consequently, if `h,h'` are both bounded by `M` and `delta=||h-h'||_infinity`, then for every `eta>0`, splitting at `|u|=eta` gives

`||P_h-P_{h'}||_infinity
 <= delta/(2eta)+8sqrt(2M eta)`.                                        (6.3)

For the present bank, (5.14) and the Gaussian peak allow `M=2`. Taking `eta=delta_m^(2/3)` gives, uniformly over **all m-dependent heavy laws**,

`||P_{h_m}-P_{gamma_{sigma_a}}||_infinity
 <=(33/2) delta_m^(1/3) ->0`.                                           (6.4)

Apply Theorem (2.2) with `H=0` and

`sigma_a/sigma_0=sqrt(1+12a^2)`.                                       (6.5)

We obtain the new target-level obstruction

`boxed(
 limsup_{m->infinity} sup_{f_{1,m},f_{2,m}<=1}
 ||p_{V_m^2-2U_m S_m}||_infinity
 <= C_x (1+12a^2)^(-1/3)
 < C_x
 <3sqrt(2).
)`                                                                             (6.6)

The supremum ranges over arbitrary independent cap-one laws for the two macroscopic physical coordinates, allowed to depend on `m` and to have disconnected, translated or unbounded supports.

For example, at `a=1/2`, the right side is

`2.588678243192709...`,                                                  (6.7)

well below `3sqrt(2)=4.242640687119286...`.

## 7. What this does and does not show

This run closes a genuinely unpaid adversarial mechanism: **critical growing-activity remote fragmentation in the diffuse bank cannot rescue the lightlike two-heavy/shared-coordinate geometry**. Combined with the newest partner's finite-activity Gaussian-plus-Poisson local limit and the shifted theorem (2.2), both fixed-activity and growing-activity remote-fragment variants of this geometry remain below `3sqrt(2)`.

This is not a proof that `3sqrt(2)` is the universal sharp constant, and it is not a proof of the unrestricted QFORM theorem. A witness above `3sqrt(2)` must leave this lightlike two-heavy mechanism—for example by using a non-lightlike two-heavy orientation with residual quadratic curvature in the bank, at least two interacting diffuse banks, genuinely non-Gaussian limits not decomposable as Gaussian plus an independent shift, or a higher-rank/finite mesoscopic geometry.

Failure to extend the weak-`L^(3/2)` constant from the lightlike normal form to those geometries would be a **failure of this auxiliary mechanism**, not a counterexample to QFORM. Likewise, a valid witness above `3sqrt(2)` would refute that candidate sharp constant but would not by itself refute existence of some larger universal bound.

## 8. Corrections respected

No argument above uses: post-rotation independence; arbitrary-joint rank-three coarea; positive moments of conditional projection-density caps; a uniformly good physical minor; a fixed fragment count; law-uniform pointwise oscillatory decay; or bounded support/moments for the two heavy laws. The only rotated heavy-plane statement used is the Jacobian-one density cap `rho<=1`, with dependence retained explicitly.

The exact target matrix spectrum is checked algebraically by `B^2=I` and `R_m^TR_m=I_3`; the physical bank laws satisfy the cap-one constraint directly by (4.2)-(4.3).
