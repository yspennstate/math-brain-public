SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T01:28:54Z.
attacking: a dependence-safe averaged-frequency compiler for the critical two-hub packet, removing the fresh account04/B01 residual-independence obstruction when the residual is conditionally L^r after fixing the slope bank.

# account03/B01 — conditional-L^r residual gluing for the critical two-hub packet

Run: `20260924T012854Z-account03-B01-qform-auto11-r40`.

Status: **NEW AVERAGED-FREQUENCY THEOREM / PARTNER RESULT APPLIED / AFFINE RESIDUAL ENTANGLEMENT REMOVED / FULL QFORM OPEN**.

Execution: `WITHOUT_VERIFIED_BRAIN`.

Continuity: **proved for the scoped theorem below; the unrestricted target continuity remains OPEN.**

## 1. Control and correction boundary

Fresh control was read from `yspennstate/math-research-brain` main and refreshed immediately before publication. OWNER CONTROL remains revision `2026-09-22.15`; QFORM is the sole research target and the full conjecture remains open. The live correction inbox was reread. No step below uses post-rotation independence, a pointwise law-uniform Fresnel estimate, arbitrary-joint coarea, a conditional projection-height cap, moment/support assumptions, compact or connected support, or deletion of a small random quadratic perturbation.

The phase-aligned obstruction is preserved: for every prescribed `s>0` and small `eta>0`, choose a finite union of intervals of total length one inside

`{x : dist(s x^2,2 pi Z) <= eta}`.

Its indicator is an admissible density and satisfies

`Re E exp(i s X^2) >= cos(eta)`.

Hence no law-uniform positive-power pointwise decay of a one-dimensional quadratic phase is being asserted.

## 2. Source-valid inputs

### 2.1 Critical two-hub complex-pushforward theorem

The completed source

`yspennstate/math-open-problems@8d7d0ff65e86e787e8da9cb04afe3bfdf5401a59`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T161404Z-account01-B01-qform-auto11/REPORT.md`

proves the following. Let `H=(H_1,H_2)` be two original independent cap-one hub variables and let `Y` be a disjoint product bank. For

`S=BY+d`, `rank(B)=2`,

write `p_S` for the two-dimensional density of `S`. If `a_t(s)` is the complex pushforward through `S` of any weight on `Y` of modulus at most one, then fixed-frequency two-dimensional Plancherel in the ORIGINAL hub coordinates gives

`|phi(t)| <= pi |t|^(-1) ||a_t||_2`.                              (2.1)

The same source gives

`||p_S||_infinity <= 2 det(BB^T)^(-1/2)`.                        (2.2)

The key point for the present run is that (2.1) is a statement about the actual complex pushforward `a_t`, not merely the unweighted density `p_S`.

### 2.2 Fresh designated partner account04/B01

The newest completed designated partner is

`yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

For `1<r<=2`, with

`alpha=(r-1)/r`,                                                     (2.3)

it proves for an affine hyperbolic edge built from two independent cap-one original coordinates

`Z=2cUV+beta U+gamma V+delta`, `c!=0`,

that

`||p_Z||_r <= 2^alpha |c|^(-alpha)`.                              (2.4)

It then glues an **independent** `L^r` residual to the critical two-hub packet. Its stated remaining obstruction is residual entanglement. The theorem below removes that obstruction when the entanglement is through the slope bank and the residual retains a uniform conditional `L^r` density.

## 3. Main theorem: conditional-L^r gluing

### Theorem `QFORM-TWO-HUB-CONDITIONAL-LR-RESIDUAL-v1`

Let the original independent coordinates be split into

- two cap-one hubs `H=(H_1,H_2)`;
- a disjoint product bank `Y`;
- a further source-disjoint product bank `W`, independent of `(H,Y)`.

Let

`S(Y)=BY+d`, `rank(B)=2`,                                           (3.1)

and assume `S` has density `p_S` with

`K:=||p_S||_infinity < infinity`.                                  (3.2)

Let `R(Y)` be arbitrary measurable. For each `y`, let `Z_y=Z(y,W)` be a real random variable whose density `q_y` exists and satisfies, for one fixed `1<r<=2`,

`ess sup_y ||q_y||_r <= M_r`.                                      (3.3)

No independence between `Z_y` and `Y` is asserted: its law may change arbitrarily with `y`. Put

`Q = H^T C H + 2 H^T S(Y) + R(Y) + Z(Y,W)`,                       (3.4)

with arbitrary symmetric `2 x 2` matrix `C`.

Define

`r'=r/(r-1)`,
`beta=(r-1)/2`,
`q=1/beta=2/(r-1)`,
`A_r=[2(3-r)/(r-1)]^((3-r)/2)`.                                   (3.5)

Then `phi_Q in L^1(R)`. Hence `Q` has a continuous density in `C_0(R)`, and

`boxed:
 ||p_Q||_infinity
 <= C_cond(r) K^(1/(r+1)) M_r^(r/(r+1)),`                         (3.6)

where

`C_cond(r)
 = (1+beta)/(pi beta)
   [ (beta pi A_r /2) (2pi)^beta ]^(2/(r+1)).`                    (3.7)

At `r=2`, this simplifies exactly to

`boxed:
 ||p_Q||_infinity
 <= 3*2^(-2/3) [ K^(1/2) M_2 ]^(2/3).`                           (3.8)

### Proof

For fixed `t`, set

`g_t(y)=E_W exp(i t Z(y,W))`.                                      (3.9)

By Hausdorff--Young with the convention `hat f(t)=int exp(itx)f(x)dx`, for almost every `y`,

`||g_.(y)||_(r') <= (2pi)^(1/r') ||q_y||_r
                 <= (2pi)^(1/r') M_r`.                           (3.10)

Push the complex measure

`exp(i t R(y)) g_t(y) dP_Y(y)`                                    (3.11)

through `s=S(y)`. Denote its Radon--Nikodym density by `a_t(s)`. Since the weight has modulus at most one,

`||a_t||_1 <= 1`.                                                  (3.12)

More importantly, disintegrating over `S=s` gives

`a_t(s)=p_S(s) E[ exp(itR(Y)) g_t(Y) | S=s ]`.                    (3.13)

Jensen therefore yields

`|a_t(s)|^(r')
 <= p_S(s)^(r') E[ |g_t(Y)|^(r') | S=s ]`.                        (3.14)

Using `p_S<=K`, integrating first in `s` and then in `t`, and applying (3.10),

`int_R ||a_t||_(r')^(r') dt
 <= K^(r'-1) E int_R |g_t(Y)|^(r') dt
 <= 2pi K^(r'-1) M_r^(r')`.                                      (3.15)

Interpolate in the **physical slope variable** `s` between `L^1` and `L^(r')`. Since

`1/2=(1-r/2)/1 + (r/2)/r'`,                                       (3.16)

we have

`||a_t||_2 <= ||a_t||_(r')^(r/2)`.                                (3.17)

Raise to the power

`q=2/(r-1)`,                                                       (3.18)

so that `q r/2=r'`. Equation (3.15) then gives

`|| ||a_t||_2 ||_(L^q(dt))
 <= (2pi)^beta K^(1/2) M_r^(r/2)`.                                (3.19)

Now perform the same two-original-hub Plancherel calculation as in the completed account01/B01 theorem. For every nonzero `t`,

`|phi_Q(t)| <= pi |t|^(-1) ||a_t||_2`.                            (3.20)

Combine this with `|phi_Q(t)|<=1`. For `T>0`, Holder in **frequency** gives

`int |phi_Q(t)|dt
 <= 2T + pi int_(|t|>T) |t|^(-1)||a_t||_2 dt
 <= 2T + pi A_r (2pi)^beta K^(1/2)M_r^(r/2) T^(-beta)`.          (3.21)

Indeed the conjugate exponent to `q` is `q/(q-1)`, and

`[ int_(|t|>T) |t|^(-q/(q-1)) dt ]^((q-1)/q)
 = A_r T^(-1/q)
 = A_r T^(-beta)`.                                                (3.22)

Write

`L=pi A_r (2pi)^beta K^(1/2)M_r^(r/2)`.                           (3.23)

The minimum of `2T+L T^(-beta)` occurs at

`T_*=(beta L/2)^(1/(1+beta))`.                                   (3.24)

At the minimizer, `L T_*^(-beta)=2T_*/beta`. Fourier inversion therefore yields

`||p_Q||_infinity
 <= (1+beta)/(pi beta)
    [ (beta pi A_r/2)(2pi)^beta K^(1/2)M_r^(r/2) ]^(1/(1+beta))`, (3.25)

which is exactly (3.6)-(3.7) because `1/(1+beta)=2/(r+1)`. The bound (3.21) proves `phi_Q in L^1`, hence the density is continuous and vanishes at infinity. QED.

## 4. Fresh partner result applied: Y-entangled hyperbolic edge

### Corollary `QFORM-TWO-HUB-Y-ENTANGLED-HYPERBOLIC-EDGE-v1`

Assume the source split is `H | Y | U | V`, where `U,V` are independent cap-one original coordinates and source-disjoint from `(H,Y)`. Let

`Q = H^T C H + 2H^T(BY+d) + R(Y)
     +2cUV + alpha(Y)U + gamma(Y)V + delta(Y)`,                    (4.1)

where `rank(B)=2`, `c!=0`, and `R,alpha,gamma,delta` are arbitrary measurable functions for which the displayed expression is finite almost surely. For an actual quadratic form, `alpha,gamma` are affine-linear in `Y` and `delta,R` are quadratic-affine, but the theorem does not need that restriction.

Put

`D=det(BB^T)>0`.                                                    (4.2)

For fixed `y`, complete the hyperbolic product:

`2cUV+alpha(y)U+gamma(y)V+delta(y)
 =2c(U+gamma(y)/(2c))(V+alpha(y)/(2c))
  +delta(y)-alpha(y)gamma(y)/(2c)`.                                (4.3)

Translations preserve both cap-one input bounds and independence of `U,V`. Therefore the completed **account04/B01** inequality (2.4) applies for every fixed `y` at the actual conditional inequality

`||q_y||_r <= 2^((r-1)/r)|c|^(-(r-1)/r)`.                         (4.4)

Also the completed two-dimensional projection theorem (2.2) gives

`K<=2D^(-1/2)`.                                                     (4.5)

Substituting (4.4)-(4.5) into Theorem 3 gives

`boxed:
 ||p_Q||_infinity
 <= C_ent(r)
    D^(-1/[2(r+1)])
    |c|^(-(r-1)/(r+1)),`                                         (4.6)

where

`C_ent(r)=2^(r/(r+1)) C_cond(r)`.                                  (4.7)

The density is continuous and in `C_0`.

At the collision endpoint `r=2`, the constant collapses exactly to three:

`boxed:
 ||p_Q||_infinity <= 3 D^(-1/6)|c|^(-1/3).`                       (4.8)

Thus the **same constant and scale exponents** as the previous source-disjoint hyperbolic-edge theorem survive arbitrary slope-bank-dependent affine entanglement `alpha(Y)U+gamma(Y)V+delta(Y)`. This is the main new mathematical payment of the run.

The scaling is exact: under multiplication of the full coefficient matrix by `lambda`, `D` scales by `lambda^4` and `c` by `lambda`; the total exponent in (4.6) is

`4/[2(r+1)] + (r-1)/(r+1) = 1`.                                  (4.9)

## 5. Scale-cancellation family

Let `q0>=2` be fixed and suppose

`BB^T=k^2 I_2`, so `D=k^4`,
`c=k^(-q0)`.                                                       (5.1)

Allow **arbitrary measurable** functions `R(Y),alpha(Y),gamma(Y),delta(Y)` in (4.1). Choose

`r=1+2/q0`,                                                        (5.2)

which lies in `(1,2]`. Then the exponent of `k` in (4.6) is exactly

`-2/(r+1)+q0(r-1)/(r+1)=0`.                                       (5.3)

Hence

`boxed: ||p_Q||_infinity <= C_ent(1+2/q0)`                         (5.4)

uniformly in `k` and in all admissible cap-one input laws. Numerically,

- `q0=2`, `r=2`: `C_ent=3`;
- `q0=3`, `r=5/3`: `C_ent=3.8271703677...`;
- `q0=4`, `r=3/2`: `C_ent=4.8329551123...`.

This extends the fresh account04/B01 strict-N3 scale cancellation to the branch where the hyperbolic edge is no longer additive-independent of the slope bank, but is affinely entangled with it.

## 6. Exact remaining obstruction

This theorem does **not** solve the diffuse-entry collar or the full conjecture. The remaining two-hub obstruction is now more sharply localized:

- slope-bank entanglement in the residual through `Y` is harmless whenever the conditional residual has a uniform `L^r` density;
- in particular, arbitrary `Y`-dependent affine shifts of a physical hyperbolic edge are harmless;
- what the proof still does **not** permit is direct coupling of the smoothing variables `U,V` back into the two hub slopes, i.e. terms `2H^T(aU+bV)`.

Those terms make the conditional Fourier factor depend on the hub variable itself, so the complex pushforward `a_t` is no longer fixed while performing the two-dimensional hub Plancherel step. No moment-free deletion of such small coefficients is legitimate.

For the previously isolated diffuse-entry collar

`max_i |A_ii|<1/64`,
`max_(i!=j)|A_ij|<1/32`,
`s_3(A)>=1`,                                                       (6.1)

the next B01 target is therefore:

`QFORM-DIFFUSE-COLLAR-HUB-EDGE-ENTANGLEMENT-v1` — aggregate weak physical couplings so that either a three-hub/cross-volume receiver applies, or a two-hub packet admits a residual bank whose remaining hub couplings can be absorbed without destroying the mixed-frequency estimate above.

The full target remains OPEN.

## 7. Continuity and correction audit

- The scoped Theorem 3 and Corollary 4 establish a continuous `C_0` density because they prove `phi_Q in L^1`.
- Full-target continuity remains OPEN.
- No pointwise quadratic van-der-Corput bound is used.
- No rotation is applied to the random coordinates.
- No arbitrary conditional density cap is substituted for independence; the conditional `L^r` statement is proved from the actual source-disjoint `W` bank and is integrated before the final frequency Holder step.
- No Monte Carlo or interval-extremality claim appears.
- No moment, compact-support, log-concavity, or connected-support assumption is introduced.

## 8. Exposed runtime metadata

MODEL: GPT-5.6 Sol
THINKING LEVEL: UNKNOWN; requested=maximum actually supported
THINKING USAGE: NOT_EXPOSED

The scheduler inventory available to this account records all twenty managed slots enabled/hourly-valid with email and push notifications false, while configured model/reasoning selector fields are not exposed. No schedule, task, notification, permission, public-release, or cross-account-authentication mutation is part of this run.
