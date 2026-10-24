Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-10 progress-extrapolation — a full-spectrum critical grand-Bellman trace estimate and an all-progressive one-shell terminal endpoint

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run keeps the exact frozen P24 pair, does not reopen the posted Problems 4–5 package, and does not replace the parent theorem by a restricted sufficient condition.

## 0. Short handoff and exact before/after quantities

The original NM13-10 intake history remains `ADMISSION_PENDING`, `UNMEASURED -> UNMEASURED`; PROGRESS20 redirected the slot to P24's already-frozen maximal-regularity pair. The productive successor chain is preserved:

- `X_0=H^{-1}(Torus)`, `X_{1/2}=L^2(Torus)`, `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`, `B=Lambda^(1/2)`, one real Brownian driver, beta=1;
- transformed stochastic-input equation
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`, with `Y=g`;
- exact strong endpoint `r_*=3`, endpoint excluded;
- exact subcritical stochastic-input norm, recovered and sharpened by NM13-10,
  `C_p^g(T)=R_p=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)R_p ->4`;
- critical spacetime rearrangement norm
  `||F||_{Z_{3,alpha}(T)}=sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`;
- current exact-pair spacetime exponent bracket `2/3 <= alpha_*(T) <=1`;
- exact additive saddle lower constant at alpha=2/3 equal to `4/9` if that endpoint is bounded.

**Fixed strong source endpoint before:** `r_*=3`, `p=3` excluded.

**Fixed strong source endpoint after:** `r_*=3`, `p=3` excluded.

**Critical spacetime exponent bracket before:** `[2/3,1]`.

**Critical spacetime exponent bracket after:** `[2/3,1]`.

**Critical spacetime lower constant before/after:** `4/9 -> 4/9`.

So there is no source-level endpoint or spacetime-bracket movement in this run.

The new mechanism gain is different and source-exact: the sharp Hessian from the preceding runs implies a **full-spectrum terminal Bellman trace estimate with only `(3-p)^(-2/3)` critical blow-up**, rather than the `(3-p)^(-1)` blow-up of the spacetime operator norm. On every exact Fourier shell this extrapolates to a terminal Lorentz–Zygmund estimate with exponent `2/3` for **arbitrary progressive inputs**, not merely deterministic feedback or the explicit additive witness.

This localizes the remaining parent obstruction: the extra loss occurs when terminal trace control is converted into full spacetime occupation, not in instantaneous critical amplification.

Status of the new theorem: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**. The parent `L^3 -> Z_{3,2/3}(T)` claim remains **PARTIAL / UNRESOLVED**.

---

## 1. Recovered source problem and proof dependency behind the current bracket

P24's current handoff records Problem 3 in the journal version as asking whether `(A,B) in SMR^bullet_{p,0}` at one exponent forces membership for all `r>2`, or at least for some larger pair-dependent range. P24's commuting torus family proves that no pair-independent right-neighborhood exists and, for beta=1, fixes the exact strong endpoint at `3`.

For the transformed equation, define for `p>=2`

`Psi_p(z)=integral_0^infinity ||e^{-sA}z||^p ds`.                  (1.1)

The recovered sharp source-scale Bellman identities are

`D Psi_p(z)[-Az]=-||z||^p`,                                      (1.2)

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`,                                    (1.3)

and, by positive-semidefinite Hessian Cauchy–Schwarz,

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.                                      (1.4)

The proof of (1.3), already recovered in the predecessor, is the exact `1/p` convex combination of

`<v,A^(1/2)w>^2 <= ||v||^2 ||A^(1/2)w||^2`

and

`<v,A^(1/2)w>^2 <= <v,Av> ||w||^2`,

inside the semigroup Hessian integral. It turns the entire Hessian density into `-(p-1)/p` times the derivative of `||e^{-sA}z||^(p-2)||e^{-sA}y||^2`, giving (1.3) after integration. Equality is attained on a single eigenspace, so that Hessian constant cannot be improved.

Applying stopped Itô to (1.1) and then Hölder gives, for the spacetime quantities

`I=E int ||Z||^p`, `J=E int ||Y||^p`,

`delta I <= (p-1) I^((p-1)/p)J^(1/p)
            +(p-1)/2 I^((p-2)/p)J^(2/p)`,                       (1.5)

where

`delta=1-(p-1)/2=(3-p)/2`.                                      (1.6)

Solving the corresponding quadratic in `R=(I/J)^(1/p)` and matching P24's one-shell lower control gives the exact inherited norm

`C_p^g(T)=1/(sqrt(2/(p-1))-1)`.                                 (1.7)

At `p=3-epsilon`,

`epsilon C_p^g(T) ->4`.                                         (1.8)

For the upper critical spacetime endpoint, let `L=log(T/s)`. Chebyshev plus (1.7) gives

`s^(1/3)F^*(s)
 <= C_p^g(T)(T/s)^(1/p-1/3)||Y||_3`.                            (1.9)

Using `p=2` for bounded `L` and `3-p=3/L` for large `L` yields

`||T_TY||_{Z_{3,1}(T)} <=(1+sqrt(2))||Y||_3`,                   (1.10)

so `alpha_*(T)<=1`.

The lower side is source-valid and explicit. On a Fourier shell, scaled time reduces the equation to

`dZ=-Z ds+(Z+Y)dW`.                                             (1.11)

With

`M_s=exp(W_s-3s/2)`, `Y_s=M_s`,                                (1.12)

the exact solution is

`Z_s=M_s(W_s-s)`.                                               (1.13)

The predecessor solved the exact level boundary and Gaussian saddle. For thresholds `R_{r,c}=cr exp(3r/2)` and scaled horizon `S_r/r->1`, `(S_r-r)/sqrt(r)->infinity`, the full spacetime tail satisfies

`exp(9r/2) int_0^{S_r} P(|Z_t|>R_{r,c})dt ->16/(9c^3)`,         (1.14)

hence

`R_{r,c}^3 m_{r,c}/r^3 ->16/9`.                                (1.15)

After Fourier rescaling to every fixed physical `T>0`, this proves every `alpha<2/3` fails and, at the unresolved boundary, any bounded endpoint has norm at least `4/9`. Thus the inherited bracket is exactly

`2/3 <= alpha_*(T) <=1`.                                       (1.16)

No part of this run resets that baseline.

---

## 2. New theorem: critical full-spectrum Bellman trace has only `delta^{-2/3}` blow-up

Let

`delta=(3-p)/2`,                                               (2.1)

and restrict first to

`5/2 <= p <3`.                                                 (2.2)

> **Theorem NM10-AVP3-GRAND-BELLMAN-TRACE-10.** For the exact frozen torus pair, every progressive source input `Y` and every `t>0` satisfy
>
> `E Psi_p(Z_t)
>  +(delta/2) E int_0^t ||Z_s||^p ds
>  <=520 delta^{-(p-1)} E int_0^t ||Y_s||^p ds`.                (2.3)
>
> Consequently,
>
> `(E Psi_p(Z_t))^(1/p)
>  <=520^(1/p) delta^{-(p-1)/p}
>    ||Y||_{L^p(Omega x (0,t);L^2)}`.                          (2.4)

The exponent in (2.4) tends to `2/3` as `p↑3`; this is one full power of `delta^(1/p)` better than the spacetime operator norm blow-up `delta^{-1}`.

### Proof

Work first on a finite Fourier projection and stop the process so all Itô terms are integrable. Equations (1.2)–(1.4) give

`d/dt E Psi_p(Z_t)`

`<= -E||Z||^p
    +(p-1)/2 E||Z||^p
    +(p-1)E[||Z||^(p-1)||Y||]
    +(p-1)/2 E[||Z||^(p-2)||Y||^2]`.                           (2.5)

Since `1-(p-1)/2=delta`, this is

`d/dt E Psi_p(Z_t)
 +delta E||Z||^p`

`<= (p-1)E[||Z||^(p-1)||Y||]
   +(p-1)/2 E[||Z||^(p-2)||Y||^2]`.                            (2.6)

For nonnegative `a,b` and any `eta>0`, direct one-variable maximization gives

`a^(p-1)b
 <= eta a^p
   +[(p-1)^(p-1)/p^p] eta^{-(p-1)}b^p`,                       (2.7)

and

`a^(p-2)b^2
 <= eta a^p
   +(2/p)[(p-2)/p]^((p-2)/2)
      eta^(-(p-2)/2)b^p`.                                     (2.8)

In the first term of (2.6), choose

`eta_1=delta/[4(p-1)]`;                                       (2.9)

in the second choose

`eta_2=delta/[2(p-1)]`.                                       (2.10)

The two absorbed pieces are each `delta a^p/4`, so together they use only half of the dissipative term.

The first remainder coefficient is

`C_1(p) delta^{-(p-1)}`,

`C_1(p)=4^(p-1)(p-1)^(2p-1)/p^p`.                             (2.11)

On `5/2<=p<3`, the coarse analytic bounds

`4^(p-1)<=16`, `(p-1)^(2p-1)<=2^5`, `p^p>=1`

give

`C_1(p)<=512`.                                                 (2.12)

The second remainder coefficient is

`C_2(p) delta^{-(p-2)/2}`,                                    (2.13)

with

`C_2(p)
 =[(p-1)/2](2/p)[(p-2)/p]^((p-2)/2)
   [2(p-1)]^((p-2)/2)`.                                      (2.14)

Here `(p-1)/2<=1`, `2/p<=1`, and the last base is below `4`; since `(p-2)/2<=1/2`,

`C_2(p)<=2`.                                                   (2.15)

Also `delta<=1` and `(p-2)/2 <= p-1`, hence

`delta^{-(p-2)/2} <= delta^{-(p-1)}`.                         (2.16)

Thus a deliberately coarse common coefficient `520` dominates both remainders. Substituting (2.7)–(2.16) into (2.6),

`d/dt E Psi_p(Z_t)
 +(delta/2)E||Z_t||^p
 <=520 delta^{-(p-1)}E||Y_t||^p`.                             (2.17)

Integrating from `0` to `t`, using `Z_0=0`, proves (2.3). Dropping the nonnegative occupation term gives (2.4).

The stopping is removed by monotone/localization convergence. For the full torus operator, use nested finite Fourier projections, which commute with `A` and `A^(1/2)`, pass the source inputs through the projections, and then apply Fatou/monotone convergence to `Psi_p` and the occupation terms exactly as in the recovered predecessor Bellman proof. This proves the theorem on the full frozen pair. QED.

---

## 3. A new full-spectrum critical grand trace space

The theorem naturally defines a source-exact endpoint trace quantity. For `t>0`, set

`G_t(Z_t)
 :=sup_{5/2<=p<3}
   delta^((p-1)/p)
   t^(1/3-1/p)
   (E Psi_p(Z_t))^(1/p)`,                                   (3.1)

where again `delta=(3-p)/2`.

Because

`||Y||_{L^p(Omega x (0,t))}
 <= t^(1/p-1/3)||Y||_{L^3(Omega x (0,t))}`,                  (3.2)

(2.4) gives immediately

`G_t(Z_t)
 <=520^(2/5)||Y||_{L^3(Omega x (0,t);L^2)}`.                 (3.3)

This is a genuine positive critical estimate on the **full frozen spectral pair** and exact source input norm. It is not the source maximal-regularity theorem because `G_t` is a terminal semigroup/Bellman trace rather than the spacetime `H^1` norm. The point is mechanism-level: the critical loss attached to the terminal Bellman boundary is exactly of order `(3-p)^(-2/3)`, while the final time integration in the known spacetime estimate supplies the remaining `(3-p)^(-1/3)`.

That separation was not available in the predecessor bracket.

---

## 4. One exact Fourier shell: arbitrary-progressive terminal exponent `2/3`

On one scaled Fourier shell `A=1`,

`Psi_p(z)=|z|^p/p`.                                          (4.1)

Therefore (2.4) yields, for `5/2<=p<3`,

`||Z_t||_{L^p(Omega)}
 <=(520p)^(1/p)
   delta^(-(p-1)/p)
   ||Y||_{L^p(Omega x (0,t))}`.                             (4.2)

The case `p=2` admits a sharper elementary estimate. From Itô,

`d/dt E|Z|^2
 =E[-|Z|^2+2ZY+|Y|^2]
 <=2E|Y|^2`,                                                  (4.3)

because `-z^2+2zy+y^2=-(z-y)^2+2y^2`. Hence

`||Z_t||_2 <=sqrt(2)||Y||_{L^2(Omega x (0,t))}`.             (4.4)

Let `Z_t^*(q)` be the decreasing rearrangement on the probability space, `0<q<1`, and define

`L(t,q)=1+log_+(t/q)`.                                        (4.5)

> **Corollary NM10-AVP3-ONE-SHELL-TRACE-11.** For every `t>0` and every progressive one-shell input `Y in L^3`,
>
> `sup_{0<q<1}
>   q^(1/3) Z_t^*(q)/L(t,q)^(2/3)
>  <=22 ||Y||_{L^3(Omega x (0,t))}`.                          (4.6)

This is an all-progressive positive endpoint on the exact shell; no deterministic-feedback or additive form is assumed.

### Proof

Chebyshev and (4.2) give

`q^(1/3)Z_t^*(q)
 <=(520p)^(1/p)
   delta^(-(p-1)/p)
   (t/q)^(1/p-1/3)
   ||Y||_3`.                                                  (4.7)

If `log(t/q)>=12`, set

`epsilon=6/log(t/q)`, `p=3-epsilon`, `delta=epsilon/2`.        (4.8)

Then `p>=5/2`, and

`(t/q)^(1/p-1/3)
 =exp[epsilon log(t/q)/(3p)]
 =exp(2/p) <=exp(4/5)`.                                      (4.9)

Also

`delta^(-(p-1)/p)
 =[log(t/q)/3]^((p-1)/p)
 <=[log(t/q)/3]^(2/3)`.                                     (4.10)

Using `520p<=1560`, the numerical coefficient in (4.7) is below `22`; the archived checker finds the coarse large-log bound actually maximized at the transition `log(t/q)=12`, with value about `17.171`.

If `log_+(t/q)<12`, use (4.4):

`q^(1/3)Z_t^*(q)
 <=sqrt(2)(t/q)^(1/6)||Y||_3
 <=sqrt(2)e^2||Y||_3
 <22||Y||_3`.                                                 (4.11)

This proves (4.6). QED.

The value `22` is intentionally robust rather than optimized; the exponent `2/3`, not that constant, is the mechanism claim.

---

## 5. The one-shell terminal exponent cannot be below `1/2`

The same source-valid additive critical exponential witness gives a complementary lower obstruction for the new trace problem.

Take

`M_s=exp(W_s-3s/2)`, `Y_s=M_s`,                              (5.1)

so

`Z_t=M_t(W_t-t)` and `||Y||_3=t^(1/3)`.                       (5.2)

Set

`R_t=2t exp(3t/2)`.                                          (5.3)

For large `t`, the negative branch of `|Z_t|` is bounded and cannot reach `R_t`. On the positive branch, writing `q=W_t-t`, the function `q exp(q-t/2)` is increasing and equals `R_t` exactly at `q=2t`, i.e. `W_t=3t`. Hence

`P(|Z_t|>R_t)=barPhi(3sqrt(t))`.                              (5.4)

Mills' asymptotic gives

`barPhi(3sqrt(t))
 ~[3sqrt(2pi t)]^(-1) exp(-9t/2)`.                            (5.5)

Therefore

`R_t P(|Z_t|>R_t)^(1/3)/||Y||_3
 ~2[3sqrt(2pi)]^(-1/3)t^(1/2)`.                              (5.6)

Moreover

`log[t/P(|Z_t|>R_t)] ~(9/2)t`.                               (5.7)

Consequently any uniform one-shell terminal estimate of the form

`q^(1/3)Z_t^*(q)
 <=C[1+log_+(t/q)]^alpha ||Y||_3`                            (5.8)

must have

`alpha>=1/2`.                                                 (5.9)

At `alpha=1/2`, this witness alone gives the asymptotic lower constant

`2[3sqrt(2pi)]^(-1/3)(2/9)^(1/2)
 =0.4812307190...`.                                          (5.10)

Thus the new exact-shell terminal subproblem has the rigorously demonstrated bracket

`1/2 <= alpha_trace <=2/3`.                                  (5.11)

This is not substituted for the parent spacetime bracket `[2/3,1]`; it is a new diagnostic theorem showing that instantaneous trace behavior is strictly better than the currently proved global occupation endpoint.

---

## 6. Why the new theorem does not yet close the parent critical endpoint

If one discards the terminal Bellman term in (2.3), the remaining occupation estimate is

`(delta/2) int E||Z||^p
 <=520 delta^{-(p-1)} int E||Y||^p`,                          (6.1)

hence

`||Z||_{L^p(Omega x dt)}
 <=(1040)^(1/p) delta^(-1)||Y||_p`.                          (6.2)

The missing `delta^{-1/p}` relative to the trace estimate is therefore exactly the cost of integrating the dissipative memory over time. Optimizing (6.2) as `p↑3` reproduces one full logarithm and gives no improvement over the already sharper exact subcritical constant route.

So simply integrating the new trace theorem is a failed route: it returns `alpha=1`, not `2/3`.

What the theorem changes is the shape of the residual problem. A successful critical proof must preserve the terminal boundary information while controlling level-set occupation; equivalently it needs a **level-truncated Bellman / energy-stopping inequality** in which the boundary term is charged at the `delta^{-2/3}` trace scale instead of being discarded before time integration.

That is a substantially narrower obstruction than “find a better interpolation argument.”

---

## 7. Essential checker and executed output

Artifacts in this run directory:

- `2026-09-20T09-47-30+0300__critical_trace_endpoint_check.py`;
- `2026-09-20T09-47-30+0300__critical_trace_endpoint_check.out`;
- `2026-09-20T09-47-30+0300__ledger_delta.json`.

The analytic proof does not depend on floating-point verification. The checker independently tests:

1. the exact Young-remainder coefficients used in (2.7)–(2.16);
2. the combined scalar inequality with the deliberately coarse coefficient `520` over a dense logarithmic grid;
3. the large-log extrapolation choice `3-p=6/L` and the claimed terminal constant `22`;
4. the asymptotic `delta^{-2/3}` scaling of the terminal factor.

The executed output ends `CHECK_PASS`. Its largest sampled combined-Young ratio is about `0.208821`, and its largest sampled large-log endpoint coefficient is about `17.170967`, below the claimed robust constant `22`.

---

## 8. Bounded current literature check

Dated 20 September 2026 and limited to the exact source and directly relevant maximal-regularity/extrapolation work:

- Agresti–Veraar, arXiv:2501.18561 / NoDEA 32 (2025), remains the Problem 3 source.
- Bechtel–Veraar's variational extrapolation work gives higher integrability under quantitative variational/self-adjoint structure, not this frozen nonsmall multiplicative critical trace/occupation endpoint.
- Evangelopoulos-Ntemiris–Veraar's discrete stochastic maximal regularity work treats temporal numerical/discrete stochastic maximal regularity and its extrapolation, not the source pair here.
- Agresti–Veraar's later temporal-regularity counterexample concerns persistence of temporal Sobolev regularity for additive equations and does not resolve this exact multiplicative extrapolation endpoint.

A bounded current search found no source-matching resolution of `L^3 -> Z_{3,2/3}(T)` for the frozen pair. This is not a worldwide novelty certificate.

---

## 9. Residual obstruction and next attack

The fixed source theorem and the critical spacetime bracket do not move:

`r_*=3 ->3`, endpoint excluded,                               (9.1)

`alpha_*(T): [2/3,1] -> [2/3,1]`.                            (9.2)

The demonstrated mechanism gain is:

- full frozen pair: terminal Bellman trace blow-up `delta^{-2/3}` rather than spacetime `delta^{-1}`;
- exact one shell: arbitrary-progressive terminal logarithmic upper exponent `2/3`;
- same shell: explicit additive lower obstruction `alpha_trace>=1/2`.

The next route is therefore not another subcritical interpolation or another additive saddle optimization. It is to build a **level-truncated Bellman/energy-stopping argument** which retains the terminal boundary term while estimating occupation of `||Z||>R`. The first decisive test should be the two-unequal-scale common-Brownian system left open by P24: if the stopping inequality survives the off-diagonal spectral Hessian there without a dimension loss, the same semigroup structure should be lifted to the full torus. If it fails, the failure term is a concrete candidate for a boundary counterexample.

This run is a substantive gain, so the PROGRESS20 two-failed-recovery fallback to T05 is not triggered.

## ledger_delta

- slot: `NM13-10`
- fixed source endpoint: `r_*=3, endpoint excluded -> unchanged`
- critical spacetime exponent bracket: `[2/3,1] -> unchanged`
- critical spacetime lower constant: `4/9 -> unchanged`
- new full-spectrum mechanism: `delta^{-2/3}` terminal grand-Bellman trace bound
- new exact-shell theorem: arbitrary-progressive terminal `Z_{3,2/3}`-type trace estimate with constant `22`
- new exact-shell trace bracket: `[1/2,2/3]`
- theorem status: `CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW`
- parent endpoint status: `PARTIAL`
- residual obligation: full arbitrary-progressive, full-spectrum spacetime `L^3 -> Z_{3,2/3}(T)` bound or a boundary counterexample
- next attack: level-truncated Bellman/energy stopping, tested first on two unequal Fourier scales
