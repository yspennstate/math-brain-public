Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-10 progress-extrapolation — uniform one-shell critical log-2/3 endpoint by excursion charging

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run stays on P24's exact frozen pair, does not reopen the posted Problems 4–5 package, and develops a new level-excursion route after the preceding covariance/Hellinger run. The theorem below is a **restricted but source-exact invariant-subspace theorem**, not the full source Problem 3 and not the full-spectrum critical endpoint.

Status of the new theorem: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**. Parent critical endpoint status remains **PARTIAL**.

## 0. Short handoff; fixed quantities before and after

The original NM13-10 intake state remains preserved historically as `ADMISSION_PENDING`, `UNMEASURED -> UNMEASURED`; PROGRESS20 redirected this slot to the productive P24 maximal-regularity successor and that predecessor state is not reset.

The exact frozen P24 realization is unchanged:

- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` (`beta=1`);
- one real Brownian driver;
- after the source-scale transform, stochastic-input equation
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`;
- input and output measured in `L^p(Omega x (0,T);L^2(Torus))`.

Retained productive chain:

1. P24 proved the exact strong fixed-pair endpoint `r_*=3`, with `(A,B) notin SMR_{3,0}`. For the commuting beta-family, `r_*(beta)=1+2/beta^2`, endpoint excluded.
2. NM13-10 later sharpened the full stochastic-input subcritical constant to
   `C_p^g(T)=R_p=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)R_p -> 4`.
3. NM13-10 proved the critical spacetime rearrangement bracket
   `2/3 <= alpha_*(T) <= 1` for
   `||F||_{Z_{3,alpha}(T)}=sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`.
4. The exact additive saddle witness gives a full-pair conditional endpoint-norm lower bound `4/9` at `alpha=2/3` if that endpoint is bounded.
5. The immediately preceding run proved that, after forcing stops at an arbitrary stopping time, unequal Fourier shells lose critical cubic coherence at Hellinger rate `exp(-(9/8)(sqrt(lambda_n)-sqrt(lambda_m))^2 t)`, and the total full-spectrum passive off-diagonal cubic occupation has finite memory.

**Fixed strong source endpoint before:** `r_*=3`, endpoint excluded.  
**Fixed strong source endpoint after:** `r_*=3`, endpoint excluded.

**Full-spectrum critical spacetime bracket before:** `[2/3,1]`.  
**Full-spectrum critical spacetime bracket after:** `[2/3,1]`.

**Full-spectrum critical endpoint lower constant before/after:** `4/9 -> 4/9`.

So there is no source-level bracket movement. The new gain is exact on every single spectral eigenspace and uniform over the spectral parameter: **for arbitrary progressive input inside one eigenspace, the critical logarithmic exponent is exactly `2/3` uniformly over all torus shells.** Consequently the only remaining mechanism capable of forcing a larger full-pair exponent is active interaction of unequal scales.

---

## 1. Recovered proof behind the current full-pair bracket

This run does not take `[2/3,1]` as unexplained history.

For `p>=2`, the corrected source-scale Bellman functional is

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`

in the transformed `L^2` coordinate (equivalently P24's source-scale `Phi_p(x)=int ||Ae^{-sA}x||_{H^{-1}}^p ds`). The exact `1/p` Hessian argument gives

`D Psi_p(z)[-Az]=-||z||^p`,

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y] <= (p-1)||z||^(p-2)||y||^2`,

and, by positive-semidefinite Hessian Cauchy–Schwarz,

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]| <= (p-1)||z||^(p-1)||y||`.

For the finite-dimensional stopped equation, with

`I=E int ||Z||^p`, `J=E int ||Y||^p`, `delta=(3-p)/2`,

Ito gives

`delta I <= (p-1) I^((p-1)/p)J^(1/p)
           +(p-1)/2 I^((p-2)/p)J^(2/p)`.

Putting `R=(I/J)^(1/p)` yields

`delta R^2 <= (p-1)R+(p-1)/2`.

The positive root simplifies exactly to

`R_p=1/(sqrt(2/(p-1))-1)`.

The source-valid one-shell neutral-feedback construction supplies the reverse inequality, so this is the exact full frozen-pair stochastic-input norm for every `2<=p<3`. In particular `(3-p)R_p ->4`.

For the positive critical rearrangement endpoint, Chebyshev and finite-measure embedding imply, with `L=log(T/s)`,

`s^(1/3)F^*(s) <= R_p exp(L(1/p-1/3)) ||Y||_3`.

Use `p=2` for bounded `L` and `3-p=3/L` for large `L`. Since `R_p=O((3-p)^(-1))`, this gives

`||T_TY||_{Z_{3,1}(T)} <= C ||Y||_3`,

and the retained proof gives the explicit constant `C=1+sqrt(2)`. Hence `alpha_*(T)<=1`.

For the lower side, the earlier source-valid one-shell near-critical feedback witness has

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`,

`sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`,

on a long interval

`L=log(1/gamma)/(2gamma)`.

Its input cost is `||Y||_3 <= C gamma^(-1/3-gamma/2)`. With

`kappa=2d/sigma^2`, `t_*=L-2sqrt(L)`, `x=dt_*`,

the exact Gaussian identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 = d^2(t-t_*)^2/(2sigma^2 t)`

and a Mills lower bound on a `sqrt(L)` saddle window give spacetime tail at least `c exp(-kappa x)`. The identities

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

then give

`||Z||_{Z_{3,alpha}}/||Y||_3
 >= c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`; exact Fourier-shell scaling transfers it to any fixed physical torus horizon. Therefore `alpha_*(T)>=2/3` and the recovered full-pair bracket really is

`2/3 <= alpha_*(T) <=1`.

Nothing below changes that parent baseline.

---

## 2. New target: arbitrary progressive forcing on one exact torus eigenspace

Let `E_n` be the real eigenspace of `Lambda` for

`lambda_n=1+n^2`.

For `n>=1`, `E_n` includes the sine/cosine multiplicity and is two-dimensional; for `n=0` it is one-dimensional. Assume only that `Y` is progressive and `E_n`-valued. Since the equation is diagonal in the spectral decomposition, `Z` remains in the same `E_n` and satisfies

`dZ=-lambda_n Z dt+sqrt(lambda_n)(Z+Y)dW`, `Z(0)=0`.       (2.1)

No deterministic, proportional, scalar-direction, or feedback restriction is imposed inside `E_n`.

Scale time by `s=lambda_n t` and set `B_s=sqrt(lambda_n)W_{s/lambda_n}`. Then (2.1) becomes

`dZ=-Z ds+(Z+Y)dB`,                                      (2.2)

on horizon `lambda_n T`.

If

`J=E int_0^T ||Y||^3 dt`,

and

`m_R=E int_0^T 1_{||Z||>R} dt`,

then the scaled quantities are `J_sc=lambda_n J` and `m_R^sc=lambda_n m_R`. Therefore any inequality involving only `J/R^3`, `T R^3/J`, and `m_R` is exactly invariant under the shell scaling. It is enough to prove the result for (2.2) in an arbitrary finite-dimensional Hilbert space `E`.

---

## 3. A stopped subcritical p-moment estimate with the right critical cost

Fix `2<=p<3` and write

`delta=(3-p)/2 in (0,1/2]`.

Let `r=||Z||`, `u=||Y||`. For `f(z)=||z||^p`,

`D^2f(z)[xi,xi]
 <=p(p-1)r^(p-2)||xi||^2`.

The generator of (2.2) therefore obeys

`L_Y r^p
 <=-p delta r^p
   +p(p-1)r^(p-1)u
   +p(p-1)/2 r^(p-2)u^2`.                               (3.1)

For `r>0`, put `t=u/r`. Since `p-1<=2`, the cross contribution after division by `p r^p` is at most `2t+t^2`. We claim

`2t+t^2 <= delta/2+136 delta^(-(p-1)) t^p`.             (3.2)

This is elementary and exact enough for the endpoint. If `t<=delta/8`, then

`2t+t^2 <= delta/4+delta^2/64 < delta/2`.

If `t>delta/8`, then

`2t <=128 delta^(-(p-1))t^p`

because `8^(p-1)<=64`, and

`t^2 <=8 delta^(-(p-1))t^p`.

Thus (3.2) follows. Substituting into (3.1),

`L_Y r^p
 <=-(p delta/2)r^p+136p delta^(-(p-1))u^p`.           (3.3)

At `r=0` the inequality follows directly by continuity/regularization (for `p=2` directly from the quadratic Hessian). Applying stopped Ito, first with bounded localization and then passing to the limit, gives for every bounded stopping time `tau`

`E r_tau^p+(p delta/2)E int_0^tau r^p dt
 <=r_0^p+136p delta^(-(p-1))E int_0^tau u^p dt`.         (3.4)

In particular, if a process starting at `0` is stopped at the first hit of radius `R` or the horizon,

`P(hit R) <=136p delta^(-(p-1))R^(-p)J_p`,             (3.5)

where `J_p=E int u^p` on that attempt interval.

---

## 4. Critical logarithmic drift on a high-level excursion

The key new point is to charge time spent near a high level by a *cubic* input cost rather than by another subcritical spacetime moment.

On `r>0`, let `e=Z/r` and put

`a=<e,Y>/r`,

`v^2=(||Y||^2-<e,Y>^2)/r^2`,

`s=||Y||/r`, so `a^2+v^2=s^2`.

Ito's formula for `log r` in (2.2) gives drift

`b=-3/2-a-a^2/2+v^2/2`.                                (4.1)

We claim the pointwise inequality

`b <= -1/2+s^3`.                                        (4.2)

Indeed

`b+1/2=-1-a-a^2+s^2/2`.

For fixed `s`, maximize this concave quadratic over `a in [-s,s]`. If `s<=1/2`, the maximizer is `a=-s` and the value is

`-1+s-s^2/2<0`.

If `s>=1/2`, the maximizer is `a=-1/2` and the value is

`-3/4+s^2/2 <=s^3`,

because `s^3-s^2/2+3/4>0` on `[1/2,infinity)`.

Now consider an excursion which starts when `r=R` and stops at the first downcrossing of `R/2` or at the terminal horizon. During the excursion, `r>=R/2`, so (4.2) gives

`b <= -1/2+8||Y||^3/R^3`.                               (4.3)

Let `D` denote the excursion duration. The terminal radius is at least `R/2`, hence

`log(r_end/R)>=-log 2`.

After localizing the martingale in the log-Ito formula and taking expectations, (4.3) yields

`E D <=2 log 2+16 R^(-3) E int_exc ||Y||^3 dt`.         (4.4)

This is the critical mechanism: each high-level excursion has a universal finite base lifetime plus a lifetime paid directly by cubic forcing energy.

---

## 5. Count excursions by subcritical hitting, then charge their length critically

Define recursively:

- `tau_1`: first time `r` hits `R`;
- after `tau_k`, `sigma_k`: first time `r` downcrosses `R/2` (or the horizon);
- after `sigma_k<T`, `tau_{k+1}`: next hit of `R` (or the horizon).

Let `N` be the number of actual hits/excursions by time `T`.

The initial attempt starts at zero, so (3.5) applies directly. Every later attempt starts at radius `R/2`. Applying (3.4) conditionally on its starting sigma-field gives

`P(tau_{k+1}<=T)
 <=2^(-p)P(tau_k<=T)
   +136p delta^(-(p-1))R^(-p)
      E int_attempt_k ||Y||^p dt`.                       (5.1)

All attempt intervals are disjoint. Summing the geometric recursion therefore gives

`E N
 <=[136p/(1-2^(-p))]
   delta^(-(p-1))R^(-p)J_p`.                            (5.2)

Every time at which `r>=R` lies inside one of the excursion intervals. Summing (4.4), using disjointness of the excursion intervals, and then (5.2), gives

`m_R:=E int_0^T 1_{r>=R}dt`

`<= [272p log2/(1-2^(-p))]
    delta^(-(p-1))R^(-p)J_p
    +16R^(-3)J_3`.                                      (5.3)

For `2<=p<3`,

`272p log2/(1-2^(-p)) <755`.                            (5.4)

This already differs structurally from the old global subcritical estimate: the `delta` blow-up pays only for the *number* of excursions, while their duration is paid at the critical cubic scale.

---

## 6. Optimize p at the tail level: a log-squared critical tail theorem

Let

`J=J_3=E int_0^T ||Y||^3dt`.

If `J=0`, then `Y=0` a.e. and `Z=0`, so assume `J>0`. By the finite-measure embedding,

`J_p <=J^(p/3)T^(1-p/3)`.

Put

`A=J/R^3`, `rho=T/A=TR^3/J`.

Then (5.3)-(5.4) become

`m_R <=755 delta^(-(p-1)) A rho^(2delta/3)+16A`.        (6.1)

If `rho<=e^6`, the trivial `m_R<=T=rho A` and `e^6<621` give the desired estimate below.

If `rho>e^6`, choose

`delta=3/log rho`, `p=3-2delta`.

Then `0<delta<1/2`,

`rho^(2delta/3)=e^2`,

and because `delta<1` and `p-1<2`,

`delta^(-(p-1))<=delta^(-2)=(log rho)^2/9`.

Also `16 <=(16/36)(log rho)^2`. Hence

`m_R
 <=[755e^2/9+16/36]A(log rho)^2`

`<621 A(1+log rho)^2`.                                  (6.2)

Combining both cases proves the uniform critical tail estimate

> **Theorem NM10-AVP3-UNIFORM-SHELL-TAIL-13.** For the scaled exact-shell equation (2.2), for every progressive Hilbert-valued input and every `R>0`,
>
> `m_R <=621 (J/R^3) [1+log_+(TR^3/J)]^2`.             (6.3)

The proof used no deterministic-control or fixed-direction assumption.

Because `T`, `J`, and `m_R` all acquire the same factor `lambda_n` under the physical shell scaling, (6.3) is exactly invariant under `lambda_n`. Thus it holds on every exact torus eigenspace `E_n` with the same constant `621`.

---

## 7. Rearrangement endpoint: uniform one-shell exponent exactly 2/3

Let `F=||Z||` on `Omega x (0,T)` and let `F^*` be its decreasing rearrangement. For `0<s<T`, put

`L=1+log(T/s)>=1`

and choose

`R_s=50 J^(1/3)s^(-1/3)L^(2/3)`.                        (7.1)

Then

`J/R_s^3=s/(50^3L^2)`

and

`rho=TR_s^3/J=50^3L^2(T/s)`.

Since `log L/L<=1/e` for `L>=1`,

`1+log rho
 =L+3log50+2log L
 <=L(1+3log50+2/e)`.                                    (7.2)

Substitute (7.1)-(7.2) into (6.3):

`m_{R_s}/s
 <=[621/50^3](1+3log50+2/e)^2`

`=0.901643049949...<1`.                                 (7.3)

Therefore `F^*(s)<=R_s`, and

`sup_{0<s<T} s^(1/3)F^*(s)/[1+log(T/s)]^(2/3)
 <=50 J^(1/3)`.                                         (7.4)

Returning to the physical torus shell gives the main new theorem.

> **Theorem NM10-AVP3-UNIFORM-SHELL-CRITICAL-13.** Let `E_n` be any eigenspace of `Lambda=I-partial_x^2`. For the exact frozen P24 equation
>
> `dZ=-Lambda Zdt+Lambda^(1/2)(Z+Y)dW`, `Z(0)=0`,
>
> if `Y` is any progressive `E_n`-valued input, then `Z` is `E_n`-valued and
>
> `||Z||_{Z_{3,2/3}(T)} <=50 ||Y||_{L^3(Omega x (0,T);E_n)}`
>
> for every `n` and every `T>0`, with the same constant `50`.

The already-certified high-frequency one-shell witnesses show that no exponent `alpha<2/3` admits a constant uniform over `n`. The exact additive saddle witness furthermore gives endpoint norm at least `4/9`. Hence, for the restriction of the frozen torus problem to one arbitrary spectral eigenspace, the uniform critical exponent is now exactly

`alpha_shell=2/3`,

with uniform endpoint norm bracket

`4/9 <= C_shell <=50`.                                  (7.5)

This is a genuine exact-pair theorem, but it is **not** the source theorem: arbitrary full-spectrum progressive inputs may simultaneously force unequal scales, and (7.4) does not control that interaction.

---

## 8. What this removes, and the precise remaining obstruction

The preceding run showed that after input is switched off, unequal shells lose cubic coherence with a summable finite-memory kernel. This run shows that while input is active, **a single shell cannot be worse than the critical `log^(2/3)` law even for arbitrary progressive vector-valued forcing**.

Therefore a full-pair counterexample with `alpha_*(T)>2/3`, if one exists, must use a genuinely active unequal-scale mechanism: it must repeatedly create common-Brownian cross-scale coherence while paying less cubic input energy than the shellwise excursion charge detects.

Conversely, a proof of the full endpoint can now target exactly one missing step: combine the shellwise high-level excursion decomposition with the previous Hellinger/decoherence estimate to show a summable Carleson charge for *active* unequal-scale intervals. There is no longer a need to optimize deterministic proportional feedback, scalar additive forcing, equal-eigenvalue multiplicity, or passive two-scale propagation; those mechanisms are all quantitatively controlled.

The parent full-spectrum quantities remain unchanged and are not overclaimed:

`r_*=3`, endpoint excluded;

`2/3 <= alpha_*(T) <=1`.

---

## 9. Essential check actually executed

The accompanying checker

`2026-09-20T11-49-58+0300__critical_one_shell_log23_check.py`

was executed before persistence. It checks on a dense logarithmic grid the generator inequality (3.2), checks the exact two-case constants `128+8=136`, verifies the log-drift maximization numerically, and checks the constants used in the tail and rearrangement optimization.

Archived output:

`2026-09-20T11-49-58+0300__critical_one_shell_log23_check.out`.

Key lines are

`crude excursion coefficient = 754.144132449220 < 755`,

`large-rho tail coefficient = 620.304150521404 < 621`,

`quantile factor for C=50 = 0.901643049949 < 1`,

and the output ends

`CHECK_PASS`.

The checker is only a sanity check; the inequalities above are proved analytically.

---

## 10. Bounded current literature check

Dated check: 2026-09-20.

- Agresti–Veraar, arXiv:2501.18561 / NoDEA 32 (2025), remains the source containing Problem 3.
- Evangelopoulos-Ntemiris–Veraar, arXiv:2505.22145, studies discrete stochastic maximal regularity and discrete extrapolation, not this nonsmall state-multiplicative exact pair.
- Lorist–van Neerven–Veraar, arXiv:2608.20266, studies necessary Banach-geometry conditions for deterministic/stochastic maximal regularity, not this frozen critical rearrangement endpoint.
- Agresti–Veraar, arXiv:2509.07803, concerns failure of temporal regularity for additive SPDEs and is a different endpoint question.

The bounded search did not locate a theorem resolving the exact full-spectrum `L^3 -> Z_{3,2/3}` question for this frozen pair. This is not a worldwide novelty certificate.

---

## 11. ledger_delta and next attack

Companion ledger delta:

`2026-09-20T11-49-58+0300__ledger_delta.json`.

Compact delta:

- parent strong endpoint: `3 -> 3`, no movement;
- parent critical spacetime bracket: `[2/3,1] -> [2/3,1]`, no movement;
- new exact restricted theorem: uniform arbitrary-progressive one-eigenspace endpoint exponent `alpha_shell=2/3`;
- new tail inequality: `m_R <=621(J/R^3)(1+log_+(TR^3/J))^2`;
- new shell endpoint norm bracket: `[4/9,50]`;
- parent status: `PARTIAL`;
- theorem status: `CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW` at the stated one-eigenspace scope.

Next attack: a two-shell active-forcing Carleson inequality. Use the present excursion stopping times shellwise; on intervals where one shell receives little cubic input, invoke the previous passive Hellinger finite-memory estimate, while intervals with substantial input are charged directly. The target is a summable two-shell estimate with the same `log^2` tail profile and a kernel in `|sqrt(lambda_n)-sqrt(lambda_m)|`; only after that succeeds should it be lifted across the full torus by the already-proved square-root spectral-gap summation.

No T05 fallback is due: this run produced a strict theorem-level gain, even though the parent full-spectrum bracket itself did not move.
