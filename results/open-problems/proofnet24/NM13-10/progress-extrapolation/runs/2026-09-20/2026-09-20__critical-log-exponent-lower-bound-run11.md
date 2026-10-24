Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-10 progress-extrapolation — a source-valid lower obstruction for the critical logarithmic endpoint

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Frozen P24 source-scale pair, unchanged in this run:

- one real Brownian driver;
- `X_0=H^{-1}(T)`;
- `X_{1/2}=L^2(T)`;
- `X_1=H^1(T)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` (`beta=1`);
- source output norm `L^p(Omega;L^p(0,T;X_1))`, equivalently after `Z=A^(1/2)u`, `L^p(Omega x (0,T);L^2(T))`.

This run does not reopen the already-written Agresti--Veraar Problems 4--5 package and does not replace the source pair by an easier operator.

## Result summary

**Fixed strong source endpoint before:** `r_*=3`, endpoint `p=3` excluded.

**Fixed strong source endpoint after:** `r_*=3`, endpoint `p=3` excluded.

So there is **no movement in the strong source endpoint**.

The newest genuinely unresolved successor from the preceding NM13-10 run is the critical rearrangement scale. For

`dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`,

let `T_T:Y -> Z` be the stochastic-input map and define, for `alpha>=0`,

`||F||_{Z_{3,alpha}(T)} = sup_{0<s<T} s^(1/3) F^*(s)/(1+log(T/s))^alpha`.

The preceding run proved

`||T_T Y||_{Z_{3,1}(T)} <= (1+sqrt(2)) ||Y||_3`

and proved ordinary weak `(3,3)` (`alpha=0`) impossible.

This run gives a new quantitative lower obstruction:

> **Theorem NM10-AVP3-CRITICAL-LOG-LOWER-05.** For every fixed physical horizon `T>0` and every `0<=alpha<2/3`, there is no finite constant `K_{alpha,T}` such that
>
> `||T_T Y||_{Z_{3,alpha}(T)} <= K_{alpha,T} ||Y||_{L^3(Omega x (0,T);H)}`
>
> for all progressive source-admissible `Y`.
>
> Consequently, if
>
> `alpha_*(T)=inf{alpha>=0: T_T:L^3 -> Z_{3,alpha}(T) is bounded}`,
>
> then
>
> `2/3 <= alpha_*(T) <= 1`
>
> for every `T>0`.

Status: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**.

This is a genuine endpoint gain on the exact frozen pair: the previously known critical-log exponent interval `[0,1]` is narrowed to `[2/3,1]`.

---

## 1. Continuity and recovered predecessor proof

The old NM13-10 admission loop ended at screen 52 with `ADMISSION_PENDING` and `UNMEASURED -> UNMEASURED`; that history stays preserved. `operations/PROGRESS20_2026-09-20.md` redirected NM10 to P24's maximal-regularity/extrapolation line.

P24's frozen handoff proves for the commuting family `(Lambda,beta Lambda^(1/2))`

`r_*(beta)=1+2/beta^2`

with endpoint nonmembership, so for `beta=1` the exact strong endpoint is `3`.

The first progress-extrapolation successor recovered the complete source-scale Bellman proof and improved the remaining full-spectrum stochastic-input constant. The next run sharpened the Bellman Hessian all the way to

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y] <= (p-1)||z||^(p-2)||y||^2`,

where

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

The proof uses the two simultaneous inequalities

`<v,A^(1/2)w>^2 <= ||v||^2 ||A^(1/2)w||^2`

and

`<v,A^(1/2)w>^2 <= <v,Av> ||w||^2`

with the exact convex weight `theta=1/p`, making the full Hessian integrand a total derivative. Stopped Ito then gives the quadratic

`delta R^2 <= (p-1)R+(p-1)/2`,

`delta=1-(p-1)/2`,

whose positive root equals exactly

`R_p = 1/(sqrt(2/(p-1))-1)`.

P24's source-admissible one-shell neutral feedback gives the matching lower bound. Therefore, for every `T>0`,

`||T_T||_{L^p -> L^p}=R_p`, `2<=p<3`,                     (1.1)

and

`(3-p)R_p -> 4`.                                          (1.2)

The immediately preceding run then used (1.1) with a quantile-dependent `p` to prove the positive endpoint

`T_T:L^3 -> Z_{3,1}(T)`,                                  (1.3)

while a Marcinkiewicz contradiction from the exact growth (1.2) ruled out `alpha=0`.

The present theorem attacks the remaining exponent gap by a new explicit adapted one-shell construction rather than another moment upper bound.

No T05 fallback is triggered: the preceding progress runs and this run all contain strict substantive gains; there have not been two failed recovery routes.

---

## 2. One-shell scaling is exactly source-valid

Let `lambda` be a Fourier eigenvalue of `Lambda`. On a single normalized eigenvector, after scaled time

`s=lambda t`

and Brownian rescaling, the exact source equation becomes

`dZ_s = -Z_s ds + (Z_s+Y_s)dW_s`.                        (2.1)

If the physical horizon is `T`, the scaled horizon is `S=lambda T`.

For a scalar scaled function `F_s` and its physical-time counterpart `F_t=F_{lambda t}`, decreasing rearrangements obey

`F_phys^*(r)=F_scaled^*(lambda r)`.                       (2.2)

Hence

`||F_phys||_{Z_{3,alpha}(T)}
 = lambda^(-1/3) ||F_scaled||_{Z_{3,alpha}(S)}`,          (2.3)

while

`||Y_phys||_{L^3(0,T)}
 = lambda^(-1/3)||Y_scaled||_{L^3(0,S)}`.                (2.4)

Therefore the endpoint norm ratio is exactly invariant under this one-shell scaling. It is enough to build scalar witnesses on arbitrarily long scaled horizons, then choose `lambda_n=1+n^2 -> infinity` inside the fixed torus pair.

---

## 3. Seed phase with finite source cost

Fix scaled time `[0,1]` and prescribe the progressive feedback

`Y_s = 2-Z_s`.                                            (3.1)

Then (2.1) reduces exactly to the Ornstein--Uhlenbeck seed equation

`dZ_s=-Z_s ds+2 dW_s`, `Z_0=0`.                          (3.2)

Thus

`Z_1 ~ N(0, 2(1-e^(-2)))`.                               (3.3)

In particular

`q_0 := P(1<=Z_1<=2)>0`,                                 (3.4)

and the seed input has finite cubic cost

`C_seed := E int_0^1 |2-Z_s|^3 ds < infinity`.           (3.5)

Write

`M_3=E|Z_1|^3<infinity`.                                  (3.6)

All constants in this phase are independent of the small parameter introduced next.

This is a legitimate source input: the process defined by (3.1)--(3.2) is progressive, and substituting it into (2.1) gives exactly the displayed OU dynamics.

---

## 4. Near-critical feedback phase

Fix `0<gamma<1/2` and set, for the remaining scaled time,

`Y_s=gamma Z_s`.                                         (4.1)

Put

`sigma=1+gamma`,
`q=sigma^2-1=2gamma+gamma^2`,
`d=1+sigma^2/2`.                                         (4.2)

Then on the feedback phase, writing `B_t=W_{1+t}-W_1`,

`Z_{1+t}=Z_1 exp(sigma B_t-d t)`, `0<=t<=L`.             (4.3)

The third moment grows exactly at rate

`E|Z_{1+t}|^3=M_3 exp(3q t)`,                            (4.4)

because

`-3+3sigma^2=3q`.

Hence the total source-input cubic norm satisfies

`J_gamma^3 := E int_0^(1+L) |Y_s|^3 ds`

`= C_seed + gamma^3 M_3 (e^(3qL)-1)/(3q)`.               (4.5)

Choose

`L=L_gamma := log(1/gamma)/(2gamma)`.                    (4.6)

Then

`3qL = (3+3gamma/2) log(1/gamma)`,                       (4.7)

so from (4.5), for all sufficiently small `gamma`,

`J_gamma <= C gamma^(-1/3-gamma/2)`.                     (4.8)

In logarithmic form,

`log J_gamma <= (1/3+gamma/2)log(1/gamma)+O(1)`.         (4.9)

The seed cost is therefore negligible at the scale relevant to the endpoint obstruction, but it remains present and source-valid.

---

## 5. Exact drifted-Brownian occupation lower bound

On the seed event `E={1<=Z_1<=2}`, equation (4.3) gives

`Z_{1+t} >= exp(X_t)`

whenever

`X_t:=sigma B_t-dt`.                                     (5.1)

Let

`kappa := 2d/sigma^2 = 1+2/sigma^2`,                     (5.2)

and choose, for `L` large,

`t_* = L-2sqrt(L)`,
`x = d t_*`.                                             (5.3)

Define the scaled product-measure tail

`m_x = int_0^L P(|Z_{1+t}|>e^x) dt`.                     (5.4)

By independence of `Z_1` and the Brownian increments,

`m_x >= q_0 int_0^L P(X_t>x)dt`.                         (5.5)

We now prove the required lower bound without appealing to an asymptotic occupation theorem.

For `t>0`,

`P(X_t>x)=barPhi(a_t)`,
`a_t=(x+dt)/(sigma sqrt(t))`.                            (5.6)

Since `x=dt_*`, the Gaussian exponent is

`a_t^2/2=(x+dt)^2/(2sigma^2 t)`.

A direct identity gives

`(x+dt)^2/(2sigma^2 t) - kappa x
 = d^2(t-t_*)^2/(2sigma^2 t)`.                           (5.7)

Integrate only over

`t in [t_*, t_*+sqrt(t_*)]`.                             (5.8)

For large `L` this interval lies inside `[0,L]`. On it, the defect in (5.7) is bounded by `d^2/(2sigma^2)`, uniformly for `0<gamma<1/2`, while `a_t` is comparable to `sqrt(L)`.

The standard Mills lower bound

`barPhi(a) >= phi(a) a/(1+a^2) >= c a^(-1)e^(-a^2/2)`

for `a>=1` therefore yields

`P(X_t>x) >= c_1 L^(-1/2)e^(-kappa x)`                  (5.9)

throughout (5.8), with `c_1>0` independent of small `gamma`.

The integration window has length comparable to `sqrt(L)`, so

`m_x >= c_2 e^(-kappa x)`                               (5.10)

for a constant `c_2>0` independent of small `gamma`.

This is the decisive comparison step: the feedback creates an occupation tail with power exponent `kappa<3`, and the finite horizon captures a fixed fraction of the saddle contribution.

---

## 6. Lower bound for every critical logarithmic quasi-norm

Let `F=|Z|` on the scaled product space of total measure `S=1+L`. Since the set `{F>e^x}` has measure at least `m_x`,

`F^*(m_x) >= e^x`.                                       (6.1)

Therefore

`||F||_{Z_{3,alpha}(S)}
 >= e^x m_x^(1/3) / (1+log(S/m_x))^alpha`.               (6.2)

Using (5.10),

`e^x m_x^(1/3) >= c_3 e^((1-kappa/3)x)`.                (6.3)

Moreover `x=O(L)` and `m_x>=c_2e^(-kappa x)`, so

`1+log(S/m_x) <= C L`                                    (6.4)

for large `L`. Hence

`||F||_{Z_{3,alpha}(S)}
 >= c_4 e^(a x)L^(-alpha)`,                              (6.5)

where

`a:=1-kappa/3
   =2(sigma^2-1)/(3sigma^2)
   =2q/(3sigma^2)`.                                      (6.6)

Since `x=d(L-2sqrt(L))`,

`a x = ad L - 2ad sqrt(L)`.                              (6.7)

The key exact algebraic identity is

`q-ad = 2q^2/(3sigma^2)`.                                (6.8)

Consequently

`e^(a x)
 = e^(qL)
   exp(-2q^2 L/(3sigma^2))
   exp(-2ad sqrt(L))`.                                   (6.9)

For the choice (4.6),

`q^2 L ->0`, `q sqrt(L)->0` as `gamma->0`.               (6.10)

Thus

`||F||_{Z_{3,alpha}(S)}
 >= c_5 e^(qL)L^(-alpha)(1+o(1)).`                       (6.11)

But

`qL=(1+gamma/2)log(1/gamma)`,                            (6.12)

so

`e^(qL)=gamma^(-1-gamma/2)`.                             (6.13)

Combining (4.8) and (6.11),

`||F||_{Z_{3,alpha}(S)} / J_gamma`

`>= c_6 gamma^(-2/3) L^(-alpha)(1+o(1))`

`= c_6 2^alpha gamma^(alpha-2/3)
   [log(1/gamma)]^(-alpha)(1+o(1)).`                     (6.14)

If `alpha<2/3`, the right side tends to `+infinity`.

Therefore no uniform scaled endpoint estimate exists for any `alpha<2/3`.

---

## 7. Transfer back to every fixed physical torus horizon

Fix arbitrary physical `T>0` and take Fourier eigenvalues

`lambda_n=1+n^2 -> infinity`.

Set

`L_n=lambda_n T-1`.

For each sufficiently large `n`, there is a unique `gamma_n in (0,1/2)` solving

`L_n = log(1/gamma_n)/(2gamma_n)`                        (7.1)

(the function on the right is continuous and decreases from `+infinity` to a finite value as `gamma` increases away from zero).

Run the seed-plus-feedback witness above on the whole scaled horizon `S_n=lambda_n T`.

By the exact scaling identities (2.3)--(2.4), the physical endpoint/output-to-input ratio equals the scaled ratio in (6.14). Since `gamma_n->0`, that ratio diverges for every `alpha<2/3`.

This proves Theorem NM10-AVP3-CRITICAL-LOG-LOWER-05 for every fixed `T>0`. QED.

---

## 8. What moved and what did not

### Fixed source theorem

Before: `r_*=3`, strong endpoint excluded.

After: `r_*=3`, strong endpoint excluded.

**No movement in the strong source endpoint.**

### Quantitative subcritical successor

Before and after:

`C_p^g(T)=1/(sqrt(2/(p-1))-1)`, `2<=p<3`.

No change; this exact predecessor theorem is used rather than re-proved.

### Critical endpoint successor

Before this run:

`0 < alpha_*(T) <= 1`;

the lower statement was only `alpha_*(T)>0`, because weak `(3,3)` was impossible.

After this run:

`2/3 <= alpha_*(T) <= 1`.                               (8.1)

This is a strict source-valid improvement in the unresolved critical endpoint.

### Mechanism gain

The new reusable mechanism is **near-critical adapted feedback + exact finite-horizon drifted-Brownian occupation comparison**. The important point is not merely that a third moment grows. The proof extracts a lower rearrangement tail directly from the occupation saddle and keeps the physical/source `L^3` input charge in the comparison. The algebraic cancellation

`q-ad=2q^2/(3sigma^2)`

shows that the occupation growth matches the feedback third-moment growth to first order, leaving the power `gamma^(-2/3)` which forces the exponent `2/3`.

This mechanism is different from the preceding Bellman upper-bound route and from the preceding Marcinkiewicz weak-endpoint contradiction.

---

## 9. Essential checker

Executed checker:

`critical_log_lower_checker.py`.

It verifies exactly:

1. `a=2q/(3sigma^2)`;
2. `q-ad=2q^2/(3sigma^2)`;
3. the Gaussian exponent identity (5.7);
4. `ad/(2gamma)->1`;
5. `q^2L->0` and `q sqrt(L)->0` for `L=log(1/gamma)/(2gamma)`;
6. numerical lower-ratio proxies grow for representative `alpha<2/3` and decay above the threshold.

Archived output ends `CHECK_PASS`.

The numerical values are only a sanity check. The proof of the `2/3` obstruction is analytic.

---

## 10. Bounded current literature check

Dated bounded searches on 2026-09-20 checked:

- Agresti--Veraar, arXiv:2501.18561 / NoDEA 32 (2025), whose Problem 3 remains the source extrapolation question;
- Evangelopoulos-Ntemiris--Veraar, arXiv:2505.22145, *Discrete stochastic maximal regularity*, which concerns discrete stochastic-convolution/operator SMR and does not supply this endpoint for the nonsmall state-multiplicative pair;
- current searches for `Lorentz-Zygmund stochastic maximal regularity`, `weak L^3 stochastic maximal regularity`, and current Problem-3 extrapolation work.

No bounded-search result recovered the exact critical rearrangement theorem (8.1) for this frozen pair. This is not a worldwide novelty certificate.

Root `POSTED.md`'s Agresti--Veraar Problems 4--5 exclusion is respected.

---

## 11. Residual obstruction and next attack

The exact unresolved quantity is now

`alpha_*(T) in [2/3,1]`.

The lower construction identifies the natural candidate `2/3`, but it does **not** prove boundedness at `alpha=2/3`; at that exponent the present witness gives an extra factor `[log(1/gamma)]^(-2/3)` and therefore does not contradict boundedness.

The next decisive route is to try to prove the matching positive endpoint

`T_T:L^3 -> Z_{3,2/3}(T)`

by using linearity plus amplitude-layer decomposition of `Y`, rather than the predecessor's single-moment Chebyshev optimization. The target is to recover the missing `ell^3` summability across input layers, which is exactly the `1/3` gain needed to improve the logarithmic power from `1` to `2/3`.

If that layer argument fails without gain for three substantive runs, the route must change under PROGRESS20; no T05 switch is currently due.

---

## ledger_delta

```json
{
  "track": "NM13-10",
  "root": "proofnet24/NM13-10/progress-extrapolation",
  "source": "Agresti-Veraar arXiv:2501.18561 Problem 3",
  "frozen_pair": {
    "X0": "H^-1(T)",
    "Xhalf": "L^2(T)",
    "X1": "H^1(T)",
    "A": "Lambda=I-partial_x^2",
    "B": "Lambda^(1/2)",
    "beta": 1,
    "brownian_dimension": 1
  },
  "fixed_source_endpoint_before": "r_*=3; p=3 excluded",
  "fixed_source_endpoint_after": "r_*=3; p=3 excluded",
  "subcritical_exact_constant_before": "C_p^g(T)=1/(sqrt(2/(p-1))-1), 2<=p<3",
  "subcritical_exact_constant_after": "unchanged",
  "critical_log_exponent_before": "0<alpha_*(T)<=1",
  "critical_log_exponent_after": "2/3<=alpha_*(T)<=1",
  "new_claim": "No L^3 -> Z_{3,alpha}(T) bound exists for any alpha<2/3, for every fixed T>0",
  "mechanism": "source-valid one-shell OU seed + near-critical progressive feedback + finite-horizon drifted-Brownian occupation saddle",
  "status": "CANDIDATE_FULL_SELF_CHECKED_PENDING_INDEPENDENT_REVIEW",
  "t05_fallback_triggered": false,
  "checker_status": "CHECK_PASS",
  "next_attack": "prove or disprove the matching alpha=2/3 upper endpoint using amplitude-layer extrapolation with ell^3 summability"
}
```
