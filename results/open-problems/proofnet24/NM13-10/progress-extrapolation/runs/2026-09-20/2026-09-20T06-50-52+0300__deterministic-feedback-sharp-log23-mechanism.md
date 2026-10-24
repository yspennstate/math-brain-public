Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-10 progress-extrapolation — sharp logarithmic 2/3 mechanism for deterministic proportional feedback

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Frozen P24 source-scale pair, unchanged:

- one real Brownian driver;
- `X_0=H^{-1}(T)`;
- `X_{1/2}=L^2(T)`;
- `X_1=H^1(T)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` (`beta=1`);
- source output norm `L^p(Omega;L^p(0,T;X_1))`; after `Z=A^(1/2)u`, this is the `L^p(Omega x (0,T);L^2(T))` norm used below.

The posted Agresti--Veraar Problems 4--5 package is not reopened or reused.

## 0. Continuity and exact before/after quantities

The old NM13-10 admission worker ended at screen 52 with `ADMISSION_PENDING` and no mathematical movement. `operations/PROGRESS20_2026-09-20.md` then redirected this slot to the P24 extrapolation line; that handoff remains historical and is not reset.

The productive successor chain on the exact P24 pair is preserved:

1. P24 proved the exact strong endpoint for `(Lambda,beta Lambda^(1/2))`,
   `r_*(beta)=1+2/beta^2`, endpoint excluded. Thus for `beta=1`, `r_*=3` and `p=3` is excluded.
2. NM13-10 recovered and sharpened the source-scale Bellman argument to the exact subcritical stochastic-input norm
   `C_p^g(T)=R_p=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)R_p ->4`.
3. NM13-10 proved the positive critical rearrangement estimate `T_T:L^3 -> Z_{3,1}(T)` and ruled out ordinary weak `(3,3)`.
4. The immediately preceding run proved that no `L^3 -> Z_{3,alpha}(T)` bound can hold for any `alpha<2/3`, so the currently demonstrated full-pair critical bracket is
   `2/3 <= alpha_*(T) <= 1`.

**Fixed strong source endpoint before:** `r_*=3`, endpoint `p=3` excluded.

**Fixed strong source endpoint after:** `r_*=3`, endpoint `p=3` excluded.

**Full critical rearrangement bracket before:** `2/3 <= alpha_*(T) <= 1`.

**Full critical rearrangement bracket after:** `2/3 <= alpha_*(T) <= 1`.

So this run makes **no source-level endpoint movement** and does not pretend that a restricted theorem is the source theorem.

What moves is the mechanism: the run proves that the exponent `2/3` is already *sharp* for a broad source-valid deterministic proportional-feedback class on the exact one-shell reduction. Therefore optimizing the preceding lower-witness route inside this class cannot improve the lower obstruction beyond `2/3`. Any stronger lower obstruction must use genuinely progressive/random feedback, non-proportional forcing, or common-noise interaction of unequal scales.

Status of the new theorem: **RESTRICTED-CLASS THEOREM PROVED / SELF-CHECKED; full endpoint remains PARTIAL and awaits a different mechanism.**

---

## 1. Exact one-shell reduction and theorem

On a Fourier eigenvector of `Lambda` with eigenvalue `lambda`, the exact source equation scales, after `s=lambda t` and Brownian rescaling, to

`dZ_s = -Z_s ds + (Z_s+Y_s)dW_s`.                       (1.1)

As in the preceding run, the source input/output ratio is invariant under this shell scaling, so a source-valid scalar construction transfers back to the same frozen torus pair.

Fix a scale `a>0`. On the seed interval `[0,1]`, prescribe

`Y_s=2a-Z_s`.                                              (1.2)

Then

`dZ_s=-Z_s ds+2a dW_s`, `Z_0=0`,                         (1.3)

so `Z_1=aG`, where `G` is a fixed centered nondegenerate Gaussian. Let

`E={a<=Z_1<=2a}`.                                         (1.4)

This has fixed positive probability independent of all later parameters.

After time `1`, on `E` choose a deterministic measurable feedback coefficient

`0<=gamma(t)<=1`,
`Y_{1+t}=gamma(t)Z_{1+t}`, `0<=t<=L`.                    (1.5)

On `E^c` put

`Y_{1+t}=-Z_{1+t}`.                                       (1.6)

Then the noise vanishes on `E^c`, so that branch simply decays by `dZ=-Zdt`. The entire control is progressive because `E in F_1` and `gamma` is deterministic.

For a spacetime random variable `F`, define the high-amplitude logarithmic endpoint quasi-norm

`||F||_{W^{amp}_{3,alpha}(a)}
 := sup_{R>=2ea} R mu{|F|>R}^{1/3}/(1+log(R/a))^alpha`,   (1.7)

where `mu=P x dt` on the scaled interval.

> **Theorem NM10-AVP3-DETERMINISTIC-FEEDBACK-LOG23-06.** There is an absolute constant `C` such that every source-valid control (1.2), (1.5), (1.6) satisfies
>
> `R^3 mu{|Z|>R}
>  <= C ||Y||_{L^3(P x dt)}^3 (1+log(R/a))^2`,           (1.8)
>
> for every `R>=2ea`. Equivalently,
>
> `||Z||_{W^{amp}_{3,2/3}(a)} <= C ||Y||_3`.             (1.9)
>
> Moreover exponent `2/3` is sharp in this class: for every `alpha<2/3`, the constant-feedback witnesses from the preceding run give controls of this form for which
>
> `||Z||_{W^{amp}_{3,alpha}(a)}/||Y||_3 -> infinity`.    (1.10)

This theorem is on the exact frozen source pair after the exact one-shell scaling, but it is a **restricted control-class theorem**, not the full arbitrary-progressive-input critical endpoint.

---

## 2. Active branch: exact lognormal representation

Condition on the event `E` and on `Z_1=z in [a,2a]`. Put

`sigma(t)=1+gamma(t)`,
`V(t)=int_0^t sigma(s)^2 ds`,
`D(t)=t+V(t)/2`,
`Q(t)=V(t)-t`.                                            (2.1)

Because `gamma` is deterministic on `E`,

`M_t=int_0^t sigma(s)dB_s ~ N(0,V(t))`,                  (2.2)

and the exact solution is

`Z_{1+t}=z exp(M_t-D(t))`.                                (2.3)

Write

`q(t)=sigma(t)^2-1=2gamma(t)+gamma(t)^2`.                 (2.4)

Since `0<=gamma<=1`,

`0<=q(t)<=3gamma(t)`.                                     (2.5)

The conditional third moment is exact:

`F_z(t)^3 := E(|Z_{1+t}|^3 | Z_1=z)
           = |z|^3 exp(3Q(t))`.                           (2.6)

Hence

`F_z(t)=|z|e^{Q(t)}`,
`F_z'(t)=q(t)F_z(t)`.                                     (2.7)

The conditional active feedback cost is

`J_z^3 := int_0^L gamma(t)^3 F_z(t)^3 dt`.               (2.8)

Combining (2.5)--(2.8),

`int_0^L |F_z'(t)|^3 dt <= 27 J_z^3`.                    (2.9)

By Holder on `[0,t]`,

`F_z(t)
 <= |z| + int_0^t |F_z'(s)|ds
 <= |z| + 3 J_z t^{2/3}`.                                (2.10)

Therefore

`F_z(t)^3 <= 4|z|^3+108 J_z^3 t^2`,                     (2.11)

using `(x+y)^3<=4(x^3+y^3)`.

This one-dimensional Sobolev estimate is the origin of the exponent `2/3`: cubic control cost produces at most `t^{2/3}` growth in the cubic-moment amplitude.

---

## 3. Gaussian tail and exact completion of the exponent

Fix `R>=2ea` and set

`ell=log(R/|z|)`.                                         (3.1)

Since `|z|<=2a`, the threshold assumption gives `ell>=1`.

From (2.3),

`P(|Z_{1+t}|>R | Z_1=z)
 <= barPhi((ell+D(t))/sqrt(V(t)))`.                       (3.2)

Since `1<=sigma<=2`,

`t<=V(t)<=4t`,
`D(t)=t+V(t)/2 >= 3t/2`.                                 (3.3)

Thus the Gaussian parameter is bounded below by a constant multiple of `sqrt(t)`. Mills' upper bound yields

`P(|Z_{1+t}|>R | z)
 <= C(1+t)^(-1/2)
    exp(-(ell+D(t))^2/(2V(t)))`.                         (3.4)

Now define

`m(t)=3V(t)-D(t)=(5/2)V(t)-t`.                            (3.5)

There is an exact identity

`(ell+D(t))^2/(2V(t)) - 3ell
 = (ell-m(t))^2/(2V(t)) - 3Q(t)`.                        (3.6)

Multiplying (3.4) by `R^3=|z|^3 e^{3ell}` and using (2.6) gives

`R^3 P(|Z_{1+t}|>R | z)
 <= C F_z(t)^3 (1+t)^(-1/2)
    exp(-(ell-m(t))^2/(2V(t)))`.                         (3.7)

Identity (3.6) is the key exact comparison: the exponential third-moment growth is separated from a Gaussian localization kernel centered where `m(t) approximately ell`.

---

## 4. Kernel lemma

Set

`I_k(ell)=int_0^L t^k(1+t)^(-1/2)
 exp(-(ell-m(t))^2/(2V(t))) dt`, `k=0,2`.                 (4.1)

We claim uniformly over all deterministic `0<=gamma<=1` and all `L`:

`I_0(ell)<=C`,
`I_2(ell)<=C(1+ell)^2`.                                  (4.2)

Indeed,

`V'(t)=sigma(t)^2 in [1,4]`,
`m'(t)=(5/2)V'(t)-1 in [3/2,9]`.                         (4.3)

Also from `t<=V<=4t`,

`(3/2)t <= m(t) <= 9t`.                                  (4.4)

Thus the change of variables `u=m(t)` has uniformly bounded Jacobian, and `t`, `V(t)`, and `u` are comparable up to absolute constants. Therefore it is enough to bound

`J_k(ell)=int_0^infinity (1+u)^(k-1/2)
 exp(-c(ell-u)^2/u) du`.                                 (4.5)

For `ell>=1`, split into three intervals.

### 4.1 `0<u<=ell/2`

Here `(ell-u)^2/u >= ell^2/(4u)`, so after the substitution `v=ell^2/u`, the exponential decay dominates every polynomial. This gives a bounded contribution for `k=0` and `O(ell^2)` for `k=2`.

### 4.2 `ell/2<=u<=2ell`

Here `u comparable ell`. Put `u=ell+sqrt(ell)v`; then

`exp(-c(ell-u)^2/u) <= exp(-c'v^2)`.                    (4.6)

The integration window has natural width `sqrt(ell)`. Hence the factor `(1+u)^(-1/2)` gives an `O(1)` integral for `k=0`, while `(1+u)^(3/2)` gives `O(ell^2)` for `k=2`.

### 4.3 `u>=2ell`

Now `(u-ell)^2/u >= u/4`, so the tail is exponentially integrable. The contribution is `O(1)` for `k=0` and, a fortiori, `O((1+ell)^2)` for `k=2`.

The case `0<=ell<1` is immediate by the same exponential tail estimate. This proves (4.2).

---

## 5. Conditional active-branch tail bound

Insert (2.11) into (3.7), integrate in time, and use (4.2):

`R^3 int_0^L P(|Z_{1+t}|>R | z)dt
 <= C[|z|^3 I_0(ell)+J_z^3 I_2(ell)]`

`<= C[|z|^3+J_z^3(1+ell)^2]`.                            (5.1)

Because `z in [a,2a]`,

`1+ell <= C(1+log(R/a))`.                                (5.2)

Moreover the deterministic feedback makes

`J_z^3 = |z|^3 K^3`,
`K^3=int_0^L gamma(t)^3 e^{3Q(t)}dt`.                    (5.3)

Averaging over `E` therefore gives

`R^3 mu_E{|Z|>R}
 <= C a^3 [1+K^3(1+log(R/a))^2]`.                       (5.4)

---

## 6. The killed branch and total source-input cost

On `E^c`, by construction `Y=-Z`, so the stochastic term vanishes and

`Z_{1+t}=Z_1 e^{-t}`.                                    (6.1)

For any starting magnitude `r=|Z_1|`, the time spent above `R` is exactly `log_+(r/R)`. Using `log u<=u^3/3` for `u>=1`,

`R^3 log_+(r/R) <= r^3/3`.                               (6.2)

Taking expectation shows that the killed branch contributes at most `C a^3` to `R^3 mu{|Z|>R}`. Its input cost is also at most `C a^3` because

`int_0^infinity |Y_{1+t}|^3dt
 = |Z_1|^3 int_0^infinity e^{-3t}dt`.                    (6.3)

The seed cost from (1.2)--(1.3) is `C_seed a^3` by exact scaling.

On `E`, (5.3) and `Z_1=aG` give

`E[1_E J_{Z_1}^3]
 = a^3 E[G^3 1_{1<=G<=2}] K^3
 = c_E a^3 K^3`,                                        (6.4)

where `c_E>0` is fixed.

Consequently

`c a^3(1+K^3) <= ||Y||_3^3 <= C a^3(1+K^3)`.            (6.5)

Combining (5.4), (6.2), and (6.5) proves

`R^3 mu{|Z|>R}
 <= C ||Y||_3^3 (1+log(R/a))^2`,                         (6.6)

which is (1.8), hence (1.9).

---

## 7. Sharpness of 2/3 inside this class

The preceding run's lower witness is a special case of the present class: after the same seed event, choose constant `gamma` on `E` and length

`L_gamma=log(1/gamma)/(2gamma)`, `gamma downarrow0`.      (7.1)

Then, writing

`sigma=1+gamma`,
`q=sigma^2-1`,
`d=1+sigma^2/2`,                                         (7.2)

one has

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`                          (7.3)

on `E`. At

`t_*=L-2sqrt(L)`,
`x=d t_*`,
`R=a e^x`,                                                (7.4)

the finite-horizon Gaussian saddle estimate proved in the preceding run gives

`m_R:=mu{|Z|>R} >= c e^{-kappa x}`,                      (7.5)

where

`kappa=1+2/sigma^2`.                                     (7.6)

The same exact algebra as before gives

`R m_R^(1/3) >= c e^{qL}(1+o(1))`,                       (7.7)

while the cubic input norm obeys

`||Y||_3 <= C gamma^{-1/3-gamma/2}`                      (7.8)

and `e^{qL}=gamma^{-1-gamma/2}`. Therefore

`R m_R^(1/3)/||Y||_3 >= c gamma^{-2/3}(1+o(1))`.         (7.9)

Also `log(R/a) comparable L comparable gamma^{-1}log(1/gamma)`. Thus for any `alpha<2/3`,

`R m_R^(1/3) /
 [(1+log(R/a))^alpha ||Y||_3]`

`>= c gamma^{alpha-2/3}[log(1/gamma)]^{-alpha}(1+o(1))`

`-> infinity`.                                           (7.10)

So exponent `2/3` in Theorem (1.8) is sharp for this deterministic proportional-feedback mechanism.

---

## 8. What this does and does not prove

### Demonstrated gain

The preceding run only showed that one explicit near-critical proportional feedback destroys every exponent `alpha<2/3`. It remained possible that a more sophisticated deterministic time-dependent proportional feedback might push the lower obstruction above `2/3`.

This run rules that out: **every deterministic `0<=gamma(t)<=1` proportional feedback after the source-valid seed satisfies the matching high-tail logarithmic `2/3` estimate**. Therefore the previous lower witness is optimal within this whole route.

### Not proved

This does **not** prove

`alpha_*(T)=2/3`                                          (8.1)

for arbitrary progressive stochastic input. In particular, the amplitude-log quasi-norm (1.7) is a high-threshold formulation tied to the seed scale `a`, while the full endpoint quantity is the rearrangement norm

`||F||_{Z_{3,alpha}(T)}
 = sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`.         (8.2)

A full `alpha=2/3` theorem must control arbitrary progressive, non-proportional inputs and all amplitude layers simultaneously. The exact full bracket therefore remains

`2/3 <= alpha_*(T) <= 1`.                                (8.3)

The theorem does, however, identify the next necessary structural ingredient: either lift the occupation argument to random progressive relative feedback, or derive a Bellman/good-lambda inequality that charges every amplitude layer by the full source input rather than by a deterministic feedback energy.

---

## 9. Essential checker

The archived checker

`2026-09-20T06-50-52+0300__deterministic_feedback_tail_checker.py`

verifies exactly:

1. the completion identity (3.6);
2. `q=2gamma+gamma^2` and `3gamma-q=gamma(1-gamma)`;
3. the conditional third-moment exponent `3q` for constant feedback;
4. numerical sanity of the kernel bounds `I_0=O(1)` and `I_2=O((1+ell)^2)` for representative constant-feedback parameters.

Its archived output ends `CHECK_PASS`. The proof above is analytic; the numerical grid is only a sanity check, not evidence substituted for the theorem.

---

## 10. Bounded current literature check

Dated 20 September 2026, the bounded current check still finds:

- Agresti--Veraar Problem 3 in the published NoDEA survey as the source extrapolation question;
- Bechtel--Veraar's 2025 variational extrapolation theorem, which proves higher integrability under variational/self-adjoint structure rather than the exact nonsmall multiplicative frozen pair here;
- Evangelopoulos-Ntemiris--Veraar's 2026 discrete stochastic maximal-regularity work, which concerns the discrete/operator stochastic-convolution setting;
- the September 2026 fully discrete SMR paper, which concerns elliptic space/time discretizations rather than this exact multiplicative endpoint.

No bounded-search source-matching theorem was found that resolves (8.3). This is not a worldwide novelty certificate.

---

## 11. Residual obstruction and next attack

The full strong endpoint remains settled at `r_*=3`; the unresolved exact-pair successor remains the critical rearrangement exponent (8.3).

This run closes one entire lower-bound route: deterministic nonnegative proportional feedback cannot force an exponent above `2/3` by high-tail occupation growth. The next attack will therefore be materially different in the relevant sense:

1. first try to replace deterministic `gamma(t)` by a progressive relative control and identify an adapted occupation-energy inequality;
2. in parallel, seek a Bellman/good-lambda decomposition for arbitrary `Y` whose layer energy has cubic summability and therefore produces exactly the `2/3` logarithm;
3. if two such recovery routes fail without gain, follow `PROGRESS20_2026-09-20.md` and move to a distinct T05 covariance/comparison application while preserving this complete extrapolation handoff and coordinating with NM13-09.

The T05 fallback is **not due in this run**, because the deterministic-feedback route produced a strict new theorem-level mechanism gain.

## ledger_delta

```json
{
  "track": "NM13-10",
  "fixed_strong_endpoint_before": "r_*=3; p=3 excluded",
  "fixed_strong_endpoint_after": "r_*=3; p=3 excluded",
  "critical_rearrangement_bracket_before": "2/3 <= alpha_*(T) <= 1",
  "critical_rearrangement_bracket_after": "2/3 <= alpha_*(T) <= 1",
  "source_level_movement": "none",
  "mechanism_gain": "sharp exponent 2/3 for the exact one-shell source-valid deterministic proportional-feedback high-tail endpoint",
  "status": "RESTRICTED-CLASS THEOREM PROVED / SELF-CHECKED; full endpoint PARTIAL",
  "checker_result": "CHECK_PASS",
  "next_attack": "progressive-control occupation inequality or full-input Bellman/good-lambda lift",
  "t05_fallback_due": false
}
```

Companion machine-readable delta: `2026-09-20T06-50-52+0300__ledger_delta.json`.
