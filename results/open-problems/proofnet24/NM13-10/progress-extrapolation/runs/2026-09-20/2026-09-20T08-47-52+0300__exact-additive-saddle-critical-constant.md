Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-10 progress-extrapolation — exact additive Gaussian saddle and a sharper critical endpoint constant

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run keeps the already-frozen P24 pair and does not reopen the excluded Agresti--Veraar Problems 4--5 package.

Frozen source-scale data, unchanged:

- one real Brownian driver;
- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` (beta=1);
- zero initial condition;
- source equation `du+Au dt=f dt+(Bu+g)dW`;
- transformed stochastic-input equation
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, with `Z=A^(1/2)u`, `Y=g`;
- stochastic-input source norm `L^p(Omega x (0,T);L^2)` and output norm `L^p(Omega x (0,T);L^2)`, exactly equivalent to the `g`-input and `H^1`-output norms above.

## 0. Short handoff and exact before/after quantities

The old NM13-10 intake worker ended with `ADMISSION_PENDING`, metric `UNMEASURED -> UNMEASURED`; that is preserved history. PROGRESS20 redirected this slot into P24's maximal-regularity/extrapolation line. The productive successor chain on the exact pair is also preserved rather than restarted:

1. P24 proved the exact strong family endpoint for `B=beta Lambda^(1/2)`,
   `r_*(beta)=1+2/beta^2`, endpoint excluded. Thus at beta=1 the strong source endpoint is exactly `r_*=3`, with `p=3` excluded.
2. NM13-10 recovered the Bellman proof and then proved the exact subcritical stochastic-input norm
   `C_p^g(T)=R_p:=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, every `T>0`, with `(3-p)R_p ->4`.
3. NM13-10 proved the positive critical rearrangement estimate `L^3 -> Z_{3,1}` and ruled out ordinary weak `(3,3)`.
4. NM13-10 then proved every logarithmic exponent `alpha<2/3` fails, giving the genuinely unresolved critical bracket
   `2/3 <= alpha_*(T) <= 1`.
5. The immediately preceding run gave an explicit source-valid additive witness at the boundary and certified the lower constant `2^(5/3)/9` for any possible `L^3 -> Z_{3,2/3}` estimate.

Here

`||F||_{Z_{3,alpha}(T)}
 := sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`,

with rearrangement on `Omega x (0,T)`.

**Fixed strong source endpoint before:** `r_*=3`, `p=3` excluded.

**Fixed strong source endpoint after:** `r_*=3`, `p=3` excluded.

**Critical exponent bracket before:** `2/3 <= alpha_*(T) <=1`.

**Critical exponent bracket after:** `2/3 <= alpha_*(T) <=1`.

So this run does **not** claim source-endpoint or exponent-bracket movement.

The quantitative endpoint bound does move:

**Certified lower bound on any possible `L^3 -> Z_{3,2/3}(T)` norm before:**

`2^(5/3)/9 = 0.35275578932626656...`.

**Certified lower bound after:**

`4/9 = 0.44444444444444444...`.

The factor improvement is exactly `2^(1/3)=1.2599210498948732...`.

The mechanism is an exact Gaussian saddle calculation for the same progressive additive critical-exponential witness used in the preceding run. It replaces a tangent-event lower bound by the exact asymptotic spacetime tail. The theorem below is **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**. The full critical endpoint `alpha_*(T)=2/3` remains **PARTIAL / UNRESOLVED**.

No T05 fallback is due: this run contains a strict new quantitative gain on the assigned extrapolation target.

---

## 1. Essential dependency: the exact P24/NM13-10 subcritical theorem

For completeness, this is the full mechanism behind the subcritical side used by the current critical bracket.

For positive self-adjoint `A` on a finite spectral truncation and `p>=2`, define

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

Its drift identity is exact:

`D Psi_p(z)[-Az]=-||z||^p`.                                (1.1)

Let `c=p-2`, `v=e^{-sA}z`, `w=e^{-sA}y`, `r=||v||^2`,
`E=||A^(1/2)w||^2`, and `m=<v,Av>/r`. The Hilbert Hessian formula gives

`(1/p)D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]`
`=int [r^(c/2)E+c r^(c/2-1)<v,A^(1/2)w>^2] ds`.          (1.2)

The mixed scalar has the simultaneous bounds

`<v,A^(1/2)w>^2 <= rE`,                                   (1.3)

`<v,A^(1/2)w>^2 <= r m ||w||^2`.                          (1.4)

Taking the convex combination with weight exactly `1/p` gives

`<v,A^(1/2)w>^2
 <= r[(1/p)E+(1-1/p)m||w||^2]`.                           (1.5)

If `F(s)=r(s)^(c/2)||w(s)||^2`, then

`-F'(s)=r^(c/2)[2E+c m||w||^2]`.                          (1.6)

Since `1+c/p=2(p-1)/p` and `c(1-1/p)=c(p-1)/p`, the integrand in (1.2) is at most `-(p-1)F'/p`. Hence

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`.                              (1.7)

The Hessian is positive semidefinite, so Hessian Cauchy--Schwarz also yields

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.                                (1.8)

Apply stopped Ito to

`dZ=-AZdt+A^(1/2)(beta Z+Y)dW`.

Writing

`I=E int_0^T ||Z||^p dt`, `J=E int_0^T ||Y||^p dt`,

(1.1), (1.7), (1.8), and Holder give

`delta I <= |beta|(p-1)I^((p-1)/p)J^(1/p)
            +(p-1)/2 I^((p-2)/p)J^(2/p)`,                (1.9)

where

`delta=1-beta^2(p-1)/2`.                                  (1.10)

For `R=(I/J)^(1/p)` this is

`delta R^2 <= |beta|(p-1)R+(p-1)/2`.                     (1.11)

The positive root simplifies because

`beta^2(p-1)^2+2delta(p-1)=2(p-1)`,                       (1.12)

so

`R <= 1/(sqrt(2/(p-1))-|beta|)`.                          (1.13)

P24's one-shell neutral-feedback lower construction reaches the same constant in the high-frequency limit. For beta=1,

`C_p^g(T)=R_p=1/(sqrt(2/(p-1))-1)`, `2<=p<3`,             (1.14)

and rationalization at `p=3-epsilon` gives

`R_{3-epsilon}
 =2 sqrt(1-epsilon/2)(1+sqrt(1-epsilon/2))/epsilon`,       (1.15)

hence

`epsilon R_{3-epsilon}->4`.                               (1.16)

This exact blow-up is the source of both the positive logarithmic endpoint and the failure of ordinary weak `L^3`.

---

## 2. Essential dependency: why the current exponent bracket is `[2/3,1]`

Let `mathcal T_T:Y -> Z` denote the stochastic-input map on `Omega x(0,T)`, and set `F=||Z||_2`.

For `2<=p<3`, rearrangement plus (1.14) gives

`F^*(s) <= R_p s^(-1/p) ||Y||_p`.                         (2.1)

Since the product space has measure `T`,

`||Y||_p <= T^(1/p-1/3)||Y||_3`.                         (2.2)

Put `L=log(T/s)`.

If `0<=L<=3`, use `p=2`. Then

`s^(1/3)F^*(s)
 <=(1+sqrt(2)) e^(L/6)||Y||_3`,                           (2.3)

and `e^(L/6)/(1+L)<=1` on `[0,3]`.

If `L>=3`, choose `epsilon=3/L`, `p=3-epsilon`. Then

`(T/s)^(1/p-1/3)=exp(1/p)<=sqrt(e)`,                     (2.4)

while from (1.15), `R_p<=4/epsilon=4L/3`. Thus

`s^(1/3)F^*(s)/(1+L)
 <=(4sqrt(e)/3)||Y||_3
 <(1+sqrt(2))||Y||_3`.                                    (2.5)

Therefore

`||mathcal T_TY||_{Z_{3,1}(T)}
 <=(1+sqrt(2))||Y||_3`.                                   (2.6)

So `alpha_*(T)<=1`.

The lower side can now be recovered from the sharper additive theorem proved in this run: Section 6 below gives a source-valid sequence for which

`||mathcal T_Tg_n||_{Z_{3,alpha}(T)}/||g_n||_3
 >= c_alpha (lambda_nT)^(2/3-alpha)(1+o(1))`.             (2.7)

Hence every `alpha<2/3` fails and `alpha_*(T)>=2/3`. This reconstructs the full currently reported bracket

`2/3 <= alpha_*(T) <=1`.                                  (2.8)

The source-level strong endpoint remains separately fixed at `r_*=3`, endpoint excluded.

---

## 3. Exact one-shell reduction and the additive critical witness

Let `phi_n` be an `L^2`-normalized Fourier eigenvector,

`Lambda phi_n=lambda_n phi_n`, `lambda_n=1+n^2`.

With `f=0`, `g_n(t)=y_n(t)phi_n`, and `u_n(t)=x_n(t)phi_n`, the source equation is

`dx_n=-lambda_n x_n dt+sqrt(lambda_n)x_n dW_t+y_n(t)dW_t`. (3.1)

Use scaled time and Brownian motion

`s=lambda_n t`,
`B_s=sqrt(lambda_n)W_{s/lambda_n}`,                        (3.2)

and set

`Z_s=sqrt(lambda_n)x_n(s/lambda_n)`,
`Y_s=y_n(s/lambda_n)`.                                     (3.3)

Then exactly

`dZ_s=-Z_s ds+(Z_s+Y_s)dB_s`, `Z_0=0`.                   (3.4)

Moreover

`||u_n(t)||_{H^1}=|Z_{lambda_n t}|`,                      (3.5)

and input/output ratios transfer without approximation.

Define on the scaled equation

`M_s=exp(B_s-3s/2)`.                                       (3.6)

Then

`dM_s=-M_s ds+M_s dB_s`,                                  (3.7)

and crucially

`E M_s^3=1`.                                               (3.8)

Choose the progressive additive input

`Y_s=M_s`.                                                  (3.9)

Writing `Z=MH`, Ito's product rule shows that

`dH=dB-ds`, `H_0=0`,                                      (3.10)

so the solution is explicit:

`Z_s=exp(B_s-3s/2)(B_s-s)`.                               (3.11)

Back in physical time this is the exact source-valid input

`g_n(t)=exp(sqrt(lambda_n)W_t-(3/2)lambda_n t)phi_n`,      (3.12)

for which

`E||g_n(t)||_2^3=1`,                                      (3.13)

and therefore

`||g_n||_3^3=T`.                                          (3.14)

This is the same frozen operator pair and source norm; no easier operator or extra sufficient hypothesis is introduced.

---

## 4. New theorem: exact spacetime tail saddle

The preceding run lower-bounded the tail of (3.11) by a convenient tangent event. That deliberately threw away part of the saddle and gave the nonsharp constant `1/9`. Here the level set is solved exactly.

Fix `c>0`. For large `r`, define

`R_{r,c}=c r exp(3r/2)`.                                  (4.1)

Let `S_r` be a scaled horizon satisfying

`S_r/r ->1`,                                               (4.2)

`(S_r-r)/sqrt(r) -> +infinity`.                           (4.3)

Define the exact scaled spacetime tail

`m_{r,c}=int_0^{S_r} P(|Z_t|>R_{r,c})dt`.                 (4.4)

> **Theorem NM10-AVP3-EXACT-ADDITIVE-SADDLE-08.** Under (4.2)--(4.3),
>
> `exp(9r/2)m_{r,c} -> 16/(9c^3)`.                        (4.5)
>
> Consequently,
>
> `R_{r,c}^3 m_{r,c}/r^3 ->16/9`,                         (4.6)
>
> independently of `c`.

The invariance in (4.6) is the quantitative mechanism gain of this run.

### Proof

For fixed `t>0`, put `w=B_t`.

If `w<=t`, writing `q=t-w>=0`, (3.11) gives

`|Z_t|=q exp(-q-t/2) <= e^(-1-t/2) <=e^(-1)`.            (4.7)

Since `R_{r,c}->infinity`, this branch never contributes for large `r`.

If `w>t`, put `q=w-t>0`. Then

`Z_t=q exp(q-t/2)`,                                       (4.8)

which is strictly increasing in `q`. Hence `Z_t>R_{r,c}` iff

`q+log q > (3/2)r+(1/2)t+log(cr)`.                        (4.9)

Let `q_{r,c}(t)>0` be the unique solution of equality in (4.9), and set

`b_{r,c}(t)=t+q_{r,c}(t)`.                                (4.10)

Thus, for all large `r`, the full absolute-value tail is exactly

`P(|Z_t|>R_{r,c})
 =barPhi(b_{r,c}(t)/sqrt(t))`.                             (4.11)

No event relaxation remains.

Now set

`q_0(t)=(3r+t)/2`,                                        (4.12)

so (4.9) at equality is

`q+log q=q_0(t)+log(cr)`.                                 (4.13)

Take the local saddle scale

`t=r+u sqrt(r)`,                                           (4.14)

with `u` in a fixed compact set. Since then `q_0=2r+O(sqrt(r))`, the mean-value theorem applied to `q ->q+log q`, whose derivative is `1+1/q`, gives uniformly on compact `u`-sets

`q_{r,c}(t)=q_0(t)+d_c+o(1)`,                             (4.15)

where

`d_c=log(c/2)`.                                            (4.16)

Indeed, substituting `q_0+d` in (4.13) shows the required correction is
`d=log(cr/q_0)+o(1)=log(c/2)+o(1)`.

Therefore

`b_{r,c}(t)
 =(3/2)(t+r)+d_c+o(1)`.                                   (4.17)

For the linear part there is the exact saddle identity

`[(3/2)(t+r)]^2/(2t)
 =(9/2)r+(9/8)(t-r)^2/t`.                                 (4.18)

Combining (4.14), (4.17), and (4.18), noting that
`((3/2)(t+r))/t ->3`, gives

`b_{r,c}(t)^2/(2t)
 =(9/2)r+3d_c+(9/8)u^2+o(1)`                             (4.19)

uniformly on compact `u`-sets. Also

`b_{r,c}(t)/sqrt(t) ~3sqrt(r)`.                           (4.20)

Mills' asymptotic `barPhi(a)~phi(a)/a` therefore yields

`sqrt(r) exp(9r/2)
 barPhi(b_{r,c}(r+u sqrt(r))/sqrt(r+u sqrt(r)))`

` -> [e^(-3d_c)/(3sqrt(2pi))] exp(-9u^2/8)`.             (4.21)

It remains to justify passing the limit under the `u` integral. On the central region `t in [r/2,2r]`, equation (4.13) and monotonicity of `q+log q` imply that `q-q_0` is bounded above and below by constants depending only on `c`: the ratio `q_0/r` stays in a fixed compact subset of `(0,infinity)`, and the correction in (4.13) is only logarithmic. Consequently `b_{r,c}(t)` differs by `O_c(1)` from `(3/2)(t+r)`. Mills' upper bound together with (4.18) then gives

`sqrt(r)e^(9r/2)
 barPhi(b_{r,c}(t)/sqrt(t))
 <= C_c exp[-c_0 (t-r)^2/r]`                              (4.22)

for universal `c_0>0` after enlarging `C_c`.

For `t<r/2`, the right side of the saddle identity (4.18) exceeds `(9/2)r+c_1r`; the same bounded/logarithmic correction from (4.13), together with a Gaussian upper tail bound, makes the contribution exponentially small after multiplication by `e^(9r/2)`. The assumptions (4.2)--(4.3) imply that the upper `u`-limit `(S_r-r)/sqrt(r)` tends to `+infinity`. Thus (4.22) and the exponentially small lower-time part give a dominated-convergence envelope on the entire contributing saddle region.

Changing variables `t=r+u sqrt(r)` in (4.4) and using (4.21),

`e^(9r/2)m_{r,c}`

` -> e^(-3d_c)/(3sqrt(2pi))
    int_{-infinity}^{infinity} exp(-9u^2/8)du`.           (4.23)

The Gaussian integral is

`int exp(-9u^2/8)du=sqrt(8pi/9)`,                         (4.24)

so

`e^(9r/2)m_{r,c}
 ->(2/9)e^(-3d_c)
 =(2/9)(2/c)^3
 =16/(9c^3)`.                                             (4.25)

This proves (4.5). Cubing (4.1) and multiplying by (4.5) gives immediately

`R_{r,c}^3m_{r,c}
 ~c^3r^3 e^(9r/2) * [16/(9c^3)]e^(-9r/2)
 =(16/9)r^3`,                                             (4.26)

which is (4.6). QED.

---

## 5. Exact improvement over the preceding tangent-event constant

For the preceding normalization `c=2`, Theorem 4 gives

`e^(9r/2)m_{r,2} ->2/9`.                                  (5.1)

The preceding tangent-event proof certified only the lower asymptotic constant `1/9`. Thus the exact level-set saddle doubles the certified tail coefficient.

More importantly, the invariant form is now

`R_{r,c}^3m_{r,c}/r^3 ->16/9`,                            (5.2)

rather than the earlier lower bound `>=8/9` at `c=2`.

This factor two in cubic tail mass becomes a factor `2^(1/3)` in the critical rearrangement norm.

---

## 6. Transfer to every fixed physical torus horizon and the new `4/9` endpoint constant

Fix arbitrary `T>0`, let

`S_n=lambda_n T`,                                         (6.1)

and choose any `K_n ->infinity` with `K_n=o(sqrt(S_n))`. Put

`r_n=S_n-K_n sqrt(S_n)`.                                  (6.2)

Then

`r_n/S_n->1`,                                              (6.3)

and

`(S_n-r_n)/sqrt(r_n)->infinity`,                          (6.4)

so Theorem 4 applies with scaled horizon `S_n`.

Take the physical input (3.12). Its norm is exactly `T^(1/3)` by (3.14). If `m_n^sc=m_{r_n,c}` is the scaled spacetime tail, then the physical spacetime tail measure is

`m_n=m_n^sc/lambda_n`.                                    (6.5)

At the rearrangement point `s=m_n`, the output exceeds `R_{r_n,c}`, so

`||mathcal T_Tg_n||_{Z_{3,alpha}(T)}/||g_n||_3`

`>= R_{r_n,c}(m_n^sc/S_n)^(1/3)
    /[1+log(S_n/m_n^sc)]^alpha`.                          (6.6)

Theorem 4 gives

`R_{r_n,c}(m_n^sc)^(1/3)
 =(16/9)^(1/3) r_n(1+o(1))`,                              (6.7)

and

`log(S_n/m_n^sc)
 =(9/2)r_n+o(r_n)`.                                       (6.8)

Since `r_n/S_n->1`, (6.6)--(6.8) imply

`liminf_n S_n^(alpha-2/3)
 ||mathcal T_Tg_n||_{Z_{3,alpha}(T)}/||g_n||_3`

`>= (16/9)^(1/3)(2/9)^alpha`.                             (6.9)

For every `alpha<2/3`, the unscaled norm ratio therefore diverges like at least `S_n^(2/3-alpha)`. This re-proves the lower half of the exact current exponent bracket without feedback or an event relaxation.

At the unresolved boundary `alpha=2/3`, (6.9) becomes

`liminf_n
 ||mathcal T_Tg_n||_{Z_{3,2/3}(T)}/||g_n||_3`

`>= (16/9)^(1/3)(2/9)^(2/3)`

`=4/9`.                                                    (6.10)

Therefore:

> **Corollary NM10-AVP3-CRITICAL-NORM-LOWER-09.** If the full frozen-pair critical estimate
>
> `mathcal T_T:L^3(Omega x(0,T);L^2) -> Z_{3,2/3}(T)`
>
> holds for any `T>0`, its operator norm is at least
>
> `4/9`.

This strictly improves the preceding certified lower bound

`2^(5/3)/9`

to

`4/9`,                                                     (6.11)

with exact factor `2^(1/3)`.

The corollary is a quantitative endpoint-bound improvement on the exact unresolved claim. It does **not** assert that the full critical estimate exists.

---

## 7. Why this does not overclaim Agresti--Veraar Problem 3

The original source-level strong theorem is unchanged: the frozen pair has strong endpoint `r_*=3` and fails at `p=3`.

The newer quantitative successor is more refined: determine the optimal critical rearrangement weakening after strong `L^3` fails. The current full information is

`2/3 <= alpha_*(T) <=1`,                                  (7.1)

and, if `alpha_*(T)=2/3` is attained as a bounded endpoint, its norm is at least

`4/9`.                                                     (7.2)

A theorem for a narrower feedback class would not settle this question, so no such substitution is made. The witness in this run is used only for a lower obstruction, where one source-valid progressive input is sufficient.

The remaining source-valid endpoint problem is:

> prove or refute boundedness of the exact frozen-pair map
>
> `mathcal T_T:L^3 -> Z_{3,2/3}(T)`
>
> for arbitrary progressive full-spectrum inputs.

A positive result would close the logarithmic exponent at `2/3`; a negative result at the boundary would have to exhibit growth beyond the exact `4/9` additive saddle mechanism.

---

## 8. Other routes tested this run and why they are not claimed as progress

### 8.1 Subcritical norm-only limiting extrapolation

Optimizing only the exact strong constants `R_p~4/(3-p)` against Chebyshev gives one full logarithm, i.e. exponent `1`. Without extra distributional information it cannot reach `2/3`. Repeating that interpolation would not move the obstruction, so it was not pursued further.

### 8.2 Direct arbitrary-progressive quotient estimate under the cubic tilt

For inputs of the form `Y=MF`, the quotient identity is

`dH=F(dW-dt)`.                                             (8.1)

Under the finite-horizon cubic exponential tilt generated by `M^3`, the drift becomes Hardy-like. A direct application of standard martingale plus Holder estimates controls the drift by a factor of order `t^(2/3)||F||_{L^3}`, which matches the witness scaling but, when inserted naively into an occupation-tail argument for arbitrary progressive `F`, loses an additional integration factor. I did not find a closed full-spectrum good-lambda estimate that removes this loss in this run. Therefore no positive `alpha=2/3` theorem is claimed from this route.

The exact saddle route above instead produces a rigorous quantitative gain and identifies what a positive theorem must dominate.

---

## 9. Essential checker and executed output

The theorem proof is analytic. The numerical checker tests the exact implicit boundary and the predicted asymptotic constant for `c=1,2,4` at increasing `r`, as well as the algebraic critical constant.

Artifacts in this run directory:

- `2026-09-20T08-47-52+0300__exact_additive_saddle_check.py`;
- `2026-09-20T08-47-52+0300__exact_additive_saddle_check.out`;
- `2026-09-20T08-47-52+0300__ledger_delta.json`.

The executed output ends `CHECK_PASS`. At `r=1280`, the relative errors against `16/(9c^3)` are approximately

- `-7.57e-4` for `c=1`;
- `+3.25e-4` for `c=2`;
- `+1.41e-3` for `c=4`.

The checker also verifies

`(16/9)^(1/3)(2/9)^(2/3)=4/9`.                            (9.1)

No finite numerical experiment is used as a substitute for the proof.

---

## 10. Bounded current literature check

Dated 20 September 2026, bounded to the exact source and recent maximal-regularity/extrapolation work relevant to this mechanism:

- Agresti--Veraar, arXiv:2501.18561 / NoDEA 32 (2025), remains the starting Problem 3 source.
- Lorist--van Neerven--Veraar, arXiv:2608.20266 (20 August 2026), studies necessary Banach-geometry conditions for deterministic/stochastic maximal regularity and condition `(S_p)`; it does not supply this frozen multiplicative-pair critical rearrangement endpoint.
- Evangelopoulos-Ntemiris, arXiv:2609.07436 (7 September 2026), develops fully discrete stochastic maximal regularity for finite-element/time-discrete elliptic schemes, again a different endpoint problem.
- The 2026 discrete stochastic maximal-regularity extrapolation line concerns numerical/discrete stochastic convolution rather than the nonsmall state-multiplicative torus pair here.

I did not find, in this bounded check, a published resolution of the exact `L^3 -> Z_{3,2/3}` frozen-pair endpoint. This is not a claim of exhaustive worldwide novelty.

---

## 11. Residual obstruction and next attack

The strict gain this run is the endpoint constant

`2^(5/3)/9  ->  4/9`.                                     (11.1)

The exponent bracket itself remains

`[2/3,1] -> [2/3,1]`.                                     (11.2)

The next attack should not optimize this additive saddle further: (4.6) is already threshold-normalization invariant. The useful target is a sharp arbitrary-progressive good-lambda/energy-stopping inequality under the critical `M^3` tilt, strong enough to recover the `2/3` logarithmic exponent without the extra time-integration loss, followed by a spectral lifting argument using self-adjointness of `Lambda` and the exact Hessian structure from Section 1.

If that route fails twice without a substantive gain, the controlling PROGRESS20 instruction calls for a distinct covariance/comparison application to T05 coordinated with NM13-09; that fallback is not triggered by the present successful run.

## ledger_delta

- slot: `NM13-10`
- fixed source endpoint: `r_*=3, endpoint excluded -> unchanged`
- critical exponent bracket: `[2/3,1] -> unchanged`
- quantitative endpoint lower constant: `2^(5/3)/9 -> 4/9`
- mechanism: exact implicit level boundary plus Gaussian saddle for the critical additive exponential witness
- theorem status: `CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW`
- full endpoint status: `PARTIAL`
- residual obligation: full arbitrary-progressive `L^3 -> Z_{3,2/3}(T)` boundedness or a boundary counterexample
- next attack: critical tilted good-lambda/energy-stopping inequality and spectral lift
