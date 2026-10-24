Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-10 progress-extrapolation — critical Lorentz-Zygmund endpoint and failure of weak-(3,3)

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Frozen P24 source-scale pair, unchanged throughout this run:

- one real Brownian driver;
- `X_0=H^{-1}(T)`;
- `X_{1/2}=L^2(T)`;
- `X_1=H^1(T)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` (equivalently `beta=1`).

This run does not reopen the already-written Agresti-Veraar Problems 4-5 package and does not substitute a different operator.

## Result summary

**Fixed strong source endpoint before:** `r_*=3`, endpoint `p=3` excluded.

**Fixed strong source endpoint after:** `r_*=3`, endpoint `p=3` excluded.

There is therefore **no movement in the strong source endpoint**. The preceding NM13-10 run instead settled the quantitative subcritical successor exactly:

`C_p^g(T)=R_p:=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, every `T>0`,

and hence `(3-p)C_p^g(T)->4`.

The genuinely unresolved next endpoint question was what, if anything, survives at the critical exponent after strong `L^3` fails. This run proves two complementary statements for the same exact pair.

> **Theorem NM10-AVP3-ENDPOINT-ZYGMUND-03.** Let `T>0`. Let `mathcal T_T` be the stochastic-input solution map for the transformed equation
>
> `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`,
>
> on `Omega x (0,T)`, where `Z=A^(1/2)u` and `Y=g`. If `F=||mathcal T_T Y||_H` and `F^*` denotes the decreasing rearrangement with respect to `P x dt`, define
>
> `||F||_{Z_3(T)} := sup_{0<s<T} s^(1/3) F^*(s)/(1+log(T/s))`.
>
> Then for every progressive `Y in L^3(Omega x (0,T);H)`,
>
> `||mathcal T_T Y||_{Z_3(T)} <= (1+sqrt(2)) ||Y||_3`.
>
> The same estimate is uniform under the source stopping-time localization after zero extension to `(0,T)`.

Thus the critical map has a logarithmically weakened Lorentz endpoint, usually denoted schematically `L^3 -> L^{3,infinity}(log L)^(-1)` on this finite measure space.

> **Theorem NM10-AVP3-NO-WEAK3-04.** For every `T>0`, the same exact stochastic-input map is **not** of weak type `(3,3)`. In particular there is no finite `W_T` such that
>
> `sup_{lambda>0} lambda [mu{||mathcal T_TY||>lambda}]^(1/3) <= W_T ||Y||_3`
>
> for all progressive `Y`. Therefore no standard Lorentz endpoint `L^3 -> L^{3,q}` with `q<=infinity` can hold.

Both claims are **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**. They sharpen the critical picture without falsely relabeling the strong source theorem as solved at `p=3`.

---

## 1. Short handoff and exact predecessor dependency

The old NM13-10 admission loop ended at screen 52 with `ADMISSION_PENDING` and `UNMEASURED -> UNMEASURED`; that history remains preserved. `operations/PROGRESS20_2026-09-20.md` redirected NM10 to P24's extrapolation theory.

Two substantive progress runs followed.

1. The first recovered P24's full source-scale proof and improved the unresolved global stochastic-input bracket using a mixed Bellman-Hessian spectral-ratio estimate.
2. The second proved the sharp weighted Hessian contraction

   `D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y] <= (p-1)||z||^(p-2)||y||^2`,

   where `Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`, and used the `theta=1/p` convex combination of the two Cauchy estimates to make the Hessian integrand an exact derivative.

Stopped Ito then gave, with `I=E int ||Z||^p`, `J=E int ||Y||^p`,

`delta R^2 <= (p-1)R + (p-1)/2`,

`delta=1-(p-1)/2`, `R=(I/J)^(1/p)`,

whose positive root is exactly

`R_p=1/(sqrt(2/(p-1))-1)`.

P24's one-shell neutral-feedback construction supplies the reverse inequality, so for every fixed physical `T>0`,

`||mathcal T_T||_{L^p -> L^p}=R_p`, `2<=p<3`.            (1.1)

At `p=2`,

`R_2=1/(sqrt(2)-1)=1+sqrt(2)`.                          (1.2)

At the endpoint, writing `p=3-epsilon`, rationalization gives

`R_{3-epsilon}`

`=2 sqrt(1-epsilon/2) [1+sqrt(1-epsilon/2)]/epsilon`

`<=4/epsilon`,                                           (1.3)

and

`epsilon R_{3-epsilon} -> 4`.                            (1.4)

These are the only predecessor facts needed below.

No T05 fallback is triggered: both preceding progress runs and this one make strict mathematical gains, so there have not been two failed recoveries.

---

## 2. Exact endpoint rearrangement setup

Let

`S_T=Omega x (0,T)`, `mu=P x dt`, so `mu(S_T)=T`.

For an `H`-valued measurable function `G`, write

`g=||G||_H`

and denote by `g^*:(0,T)->[0,infinity]` its decreasing rearrangement. The elementary rearrangement bound is

`g^*(s) <= s^(-1/p) ||G||_{L^p(S_T;H)}`                (2.1)

for every `p>0`.

For `Y in L^3(S_T;H)`, finite measure embedding gives

`||Y||_p <= T^(1/p-1/3)||Y||_3`, `2<=p<3`.              (2.2)

Combining (1.1), (2.1), and (2.2),

`F^*(s) <= R_p s^(-1/p) T^(1/p-1/3)||Y||_3`,            (2.3)

where `F=||mathcal T_TY||_H`.

The point is to choose `p` as a function of the quantile `s` rather than trying to send a single strong estimate to `p=3`.

---

## 3. Limiting extrapolation theorem at the critical exponent

### Theorem 3.1

For every `Y in L^3(S_T;H)`,

`sup_{0<s<T} [s^(1/3)F^*(s)/(1+log(T/s))]`

`<= (1+sqrt(2))||Y||_3`.                                (3.1)

### Proof

Put

`L=log(T/s)>=0`.                                         (3.2)

There are two regimes.

### Regime A: `0<=L<=3`

Use the exact `p=2` bound. From (2.3) and (1.2),

`s^(1/3)F^*(s)`

`<= R_2 (T/s)^(1/6)||Y||_3`

`=R_2 e^(L/6)||Y||_3`.                                  (3.3)

Hence

`s^(1/3)F^*(s)/(1+L)`

`<= R_2 [e^(L/6)/(1+L)]||Y||_3`.                        (3.4)

On `[0,3]`,

`d/dL log[e^(L/6)/(1+L)] = 1/6-1/(1+L)<0`,              (3.5)

because `1+L<=4<6`. Therefore the bracket in (3.4) is at most its value `1` at `L=0`, giving

`s^(1/3)F^*(s)/(1+L) <= R_2||Y||_3`.                    (3.6)

### Regime B: `L>=3`

Choose

`epsilon=3/L`, `p=3-epsilon`.                            (3.7)

Then `0<epsilon<=1`, so `2<=p<3`. Equation (2.3) gives

`s^(1/3)F^*(s)`

`<= R_p (T/s)^(1/p-1/3)||Y||_3`.                        (3.8)

Since

`1/p-1/3=(3-p)/(3p)=epsilon/(3p)`,                      (3.9)

and `epsilon L=3`,

`(T/s)^(1/p-1/3)`

`=exp[L epsilon/(3p)]`

`=exp(1/p)`

`<=sqrt(e)`.                                             (3.10)

By (1.3),

`R_p <=4/epsilon=4L/3`.                                  (3.11)

Therefore

`s^(1/3)F^*(s)/(1+L)`

`<= [4 sqrt(e)/3] [L/(1+L)] ||Y||_3`

`<= [4 sqrt(e)/3]||Y||_3`.                              (3.12)

Finally,

`4 sqrt(e)/3 = 2.198295... < 1+sqrt(2)=2.414213...`.     (3.13)

Combining (3.6) and (3.12) proves (3.1). QED.

### Stopping-time compatibility

The source Definition 3.7 uses arbitrary starting/stopping times. For `tau<=T`, apply the already-uniform subcritical estimate to the stopped input/output and extend both by zero on `(tau,T)`. The ambient measure remains at most `T`, and exactly the same rearrangement proof applies. Thus the logarithmic critical estimate is compatible with the source localization convention rather than being an easier deterministic-time substitute.

---

## 4. Explicit critical tail corollary

The rearrangement theorem is the clean endpoint statement. A direct tail form is also useful.

Let

`a=||Y||_3/T^(1/3)`,                                     (4.1)

and assume `lambda>=e^3 a`. Put

`x=lambda/a`, `epsilon=3/log x`, `p=3-epsilon`.          (4.2)

Chebyshev, (1.1), and finite-measure embedding give

`mu{F>lambda}/T <= R_p^p x^(-p)`.                       (4.3)

Using `R_p<=4/epsilon`, `p<=3`, and `x^epsilon=e^3`,

`mu{F>lambda}`

`<= (4e/3)^3 [||Y||_3^3/lambda^3] [log(lambda/a)]^3`.   (4.4)

So the endpoint failure is controlled by one logarithm in rearrangement scale, equivalently by a cubic logarithm in this simple explicit tail estimate.

This is not claimed optimal.

---

## 5. Weak-(3,3) is impossible

The positive logarithmic endpoint is not merely a weak-`L^3` estimate written inefficiently. Standard weak type actually fails.

### Theorem 5.1

For any fixed `T>0`, no finite `W` can satisfy

`mu{||mathcal T_TY||>lambda} <= W^3 lambda^(-3)||Y||_3^3`  (5.1)

for all `lambda>0` and all progressive `Y in L^3(S_T;H)`.

### Proof

Assume such a finite `W` exists. We already have strong type `(2,2)` with exact constant

`A=R_2=1+sqrt(2)`.                                      (5.2)

For `2<p<3`, fix `lambda>0` and split an arbitrary input `Y` at amplitude `alpha lambda`:

`Y_hi=Y 1_{||Y||>alpha lambda}`,

`Y_lo=Y 1_{||Y||<=alpha lambda}`.                       (5.3)

Since `mathcal T_T` is linear, the output norm is pointwise subadditive, so

`mu{||TY||>2lambda}`

`<=mu{||TY_hi||>lambda}+mu{||TY_lo||>lambda}`

`<=A^2 lambda^(-2)||Y_hi||_2^2`

` +W^3 lambda^(-3)||Y_lo||_3^3`.                        (5.4)

Multiply by `p 2^p lambda^(p-1)` and integrate `lambda` from `0` to `infinity`. Tonelli gives

`||TY||_p^p`

`<=p 2^p { A^2 alpha^(-(p-2))/(p-2)`

`          +W^3 alpha^(3-p)/(3-p) } ||Y||_p^p`.          (5.5)

The minimizing split is

`alpha=A^2/W^3`.                                         (5.6)

Substitution yields the explicit Marcinkiewicz estimate

`||mathcal T_T||_p^p`

`<=p 2^p A^[2(3-p)] W^[3(p-2)]`

`  *[1/(p-2)+1/(3-p)]`.                                 (5.7)

But the exact predecessor theorem says the left side is `R_p^p`. Put `p=3-epsilon`. By (1.4),

`R_{3-epsilon}^{3-epsilon} asymp epsilon^(-3)`,          (5.8)

whereas for fixed finite `A,W`, the right side of (5.7) is only

`O(epsilon^(-1))`.                                      (5.9)

This is impossible as `epsilon->0`. Hence no finite weak-`(3,3)` constant exists. QED.

### Consequence

Every standard Lorentz space `L^{3,q}`, `1<=q<=infinity`, embeds into weak `L^3=L^{3,infinity}`. Therefore the critical output cannot lie in any ordinary `L^{3,q}` with a uniform source-input estimate. A logarithmic or otherwise genuinely weaker endpoint scale is necessary.

This is stronger than the already-known statement `(A,B) notin SMR_{3,0}`: even replacing the strong target by weak `L^3` does not rescue the endpoint.

---

## 6. Relation to the full source equation

The source equation also permits a progressive drift input `f`. On this frozen self-adjoint torus realization the deterministic maximal-regularity component at `p=3` is already finite; it is not the critical obstruction. Strong `L^3` embeds continuously into the above `Z_3(T)` rearrangement scale because

`F^*(s)<=s^(-1/3)||F||_3`

and `1+log(T/s)>=1`.

Thus the stochastic theorem above supplies the missing critical component for a full-equation logarithmic endpoint estimate, up to the standard quasi-triangle constant of the rearrangement space and the existing deterministic maximal-regularity constant. No claim is made that this changes the source's strong `SMR_{3,0}` status: it does not.

---

## 7. What moved and what did not

### Fixed source theorem

Before: `r_*=3`, strong endpoint excluded.

After: `r_*=3`, strong endpoint excluded.

**No source-endpoint movement.**

### Quantitative successor before this run

For every `T>0` and `2<=p<3`,

`C_p^g(T)=1/(sqrt(2/(p-1))-1)`,

with exact endpoint blow-up amplitude `4`.

### Quantitative successor after this run

At `p=3`:

1. ordinary weak `L^3` is impossible;
2. the exact same source-input map satisfies the uniform critical rearrangement estimate

   `||TY||_{Z_3(T)} <= (1+sqrt(2))||Y||_3`.

This turns the previous bare statement “endpoint excluded” into a two-sided functional description: the endpoint lies strictly below weak `L^3`, but no worse than one logarithmic weakening of weak `L^3` in rearrangement scale.

### Mechanism gain

The reusable extrapolation mechanism is **quantile-dependent exponent selection**. Instead of sending a single `p` to the critical value, choose

`3-p = 3/log(T/s)`

at rearrangement quantile `s`. The exact `1/(3-p)` norm blow-up is thereby converted into one logarithm. The exact subcritical norm also rules out weak type through the explicit interpolation contradiction in Section 5.

This is a genuine endpoint-extrapolation mechanism, not a new restrictive sufficient condition on `(A,B)`.

---

## 8. Essential actual check

Executed checker:

`2026-09-20T04-48-00+0300__endpoint_log_extrapolation_checker.py`.

Archived output:

`2026-09-20T04-48-00+0300__endpoint_log_extrapolation_checker.out`.

It checks:

- the exact rationalization of `R_{3-epsilon}`;
- `R_{3-epsilon}<=4/epsilon` over representative scales;
- `4sqrt(e)/3 < 1+sqrt(2)`;
- the moderate-quantile monotonicity bound;
- the variable-`p` small-quantile coefficient on a dense logarithmic grid;
- the asymptotic separation between the exact strong norm (`epsilon^{-3}` after taking the p-th power) and any fixed weak-`(3,3)` Marcinkiewicz RHS (`epsilon^{-1}`).

The archived execution ends `CHECK_PASS`. The proof itself is analytic; the checker is only a sanity check.

---

## 9. Current literature boundary checked this run

A bounded current check on 20 September 2026 recovered:

- Agresti-Veraar, arXiv:2501.18561 / NoDEA 32 (2025), containing Problem 3 in the same extrapolation program;
- Bechtel-Veraar, *An extrapolation result in the variational setting*, published 11 July 2025, which obtains higher integrability under quantitative variational/self-adjoint hypotheses and does not provide the above exact critical endpoint for the nonsmall multiplicative pair;
- Evangelopoulos-Ntemiris-Veraar, *Discrete stochastic maximal regularity*, published 13 February 2026, whose extrapolation concerns the discrete/operator stochastic-convolution framework rather than the present state-multiplicative pair;
- Evangelopoulos-Ntemiris, *Fully discrete stochastic maximal regularity and H-infinity-calculus for second-order elliptic operators*, arXiv:2609.07436, dated 7 September 2026, again in a fully discrete elliptic approximation setting.

No bounded-search source found a source-matching theorem that makes the strong critical endpoint true or supplies this exact Lorentz-Zygmund statement. This is not a proof of worldwide novelty.

---

## 10. Residual obstruction and next attack

The strong endpoint is already known false and weak `L^3` is now also ruled out. The positive theorem loses exactly one logarithm in rearrangement scale, but this run does **not** prove that exponent `1` is optimal.

The next decisive problem is therefore:

> determine the smallest `alpha>=0` for which
>
> `sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`
>
> is bounded by a universal multiple of `||Y||_3` for the exact frozen pair.

The cleanest lower-bound laboratory is the scalar critical one-shell equation over a finite scaled horizon with adapted feedback. Its finite-horizon control/occupation law should reveal whether the exact strong-norm blow-up `R_p~4/(3-p)` forces a logarithmic exponent strictly below, equal to, or above the present upper value `alpha=1`. Only after that scalar critical law is understood should unequal Fourier scales be reintroduced.

This is a new route, not another audit or repetition of the settled Hessian optimization.

---

## ledger_delta

```json
{
  "source_endpoint_before": "r_*=3, strong p=3 excluded",
  "source_endpoint_after": "r_*=3, strong p=3 excluded",
  "source_endpoint_movement": false,
  "successor_before": "exact subcritical C_p^g(T)=R_p and endpoint blow-up amplitude 4",
  "successor_after": "critical map is not weak-(3,3), but obeys L^3 -> Z_3(T) with constant <=1+sqrt(2)",
  "mechanism_gain": "quantile-dependent limiting extrapolation plus explicit Marcinkiewicz contradiction",
  "claim_ids": ["NM10-AVP3-ENDPOINT-ZYGMUND-03", "NM10-AVP3-NO-WEAK3-04"],
  "status": "CANDIDATE_FULL_SELF_CHECKED_PENDING_INDEPENDENT_REVIEW",
  "t05_fallback_triggered": false,
  "next_attack": "optimal critical logarithmic exponent via scalar finite-horizon adapted-control/occupation analysis"
}
```
