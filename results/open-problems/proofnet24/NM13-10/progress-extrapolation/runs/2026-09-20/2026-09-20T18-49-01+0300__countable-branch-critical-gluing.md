Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-10 progress-extrapolation — exact countable branch gluing at the critical endpoint

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run stays on P24's already-frozen pair, preserves the actual NM13-10 successor chain, does not reopen the already-written Agresti--Veraar Problems 4--5 package, and develops the precise high-level packet-restart obstruction left by the predecessor active-migration theorem.

The new disjoint-gluing theorem below is **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**. Its stochastic restart corollary uses the retained comparable-band endpoint theorem and therefore inherits that theorem's candidate status. The parent full-spectrum critical endpoint remains **PARTIAL / OPEN**.

## 0. Short predecessor handoff; fixed theorem before and after

The exact frozen realization is unchanged:

- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)`;
- one real Brownian driver;
- `beta=1`;
- after the source-scale transform,
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`;
- stochastic input and output are measured in `L^p(Omega x (0,T);L^2(Torus))`.

The immediately preceding report was committed as

`e8c2506d102789de1f5d7c188ea54ac5875bab40`

and proved the approximate packet active-migration inequality

`Sigma_p(z,y)
 >=(p-1)||z||^(p-1)||Qy||^2/||y||
   -22 d_P(z)^(p-2)||z||^(p-1)||y||`

for every spectral projection `P`, together with its integrated three-block-packet consequence. Retained earlier NM13-10 results include the sharp subcritical norm, the `[2/3,1]` critical rearrangement bracket, the `4/9` additive-shell lower constant at a possible critical endpoint, exact one-shell and comparable-band `alpha=2/3` estimates, finite-multiband gluing, the full-spectrum little-`Z_{3,1}` theorem, passive Hellinger/decoherence, the state spectral-variance defect, and the joint Bellman slack.

**Fixed strong endpoint before:** `r_*=3`, strong `p=3` excluded.  
**Fixed strong endpoint after:** `r_*=3`, strong `p=3` excluded.

**Exact subcritical norm before/after:**

`C_p^g(T)=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, and `(3-p)C_p^g(T)->4`.

**Full critical rearrangement bracket before:** `[2/3,1]`.  
**Full critical rearrangement bracket after:** `[2/3,1]`.

**Conditional full-pair `alpha=2/3` lower constant before/after:** `4/9 -> 4/9`.

Thus this run does not claim a source-level exponent change. The strict gain is that **countably many possible packet locations cause no endpoint loss at all when the packet choice is a genuine branch/restart choice**. This removes the packet-count entropy obstruction from the restart part of the proposed excursion argument and isolates within-excursion packet migration as the remaining problem.

---

## 1. Source Problem 3 and complete retained proof behind the bracket

The source survey states, for nonsmall `B`, the extrapolation question: if `(A,B)` has stochastic maximal regularity at some `p>=2`, must it have stochastic maximal regularity for all `r>2`, or at least for a larger range? The frozen pair above is the exact P24 realization being studied here; it is not replaced by an easier operator.

For `p>=2`, define

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

Because `A` is positive self-adjoint on `L^2(Torus)`, differentiation along the semigroup gives

`D Psi_p(z)[-Az]=-||z||^p`.

The sharp Hessian contraction recovered in the predecessor chain is

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`,

and positivity of the Hessian yields

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.

For stopped finite-dimensional approximations put

`I=E int_0^T ||Z||^p dt`,
`J=E int_0^T ||Y||^p dt`,
`delta=(3-p)/2`.

Ito's formula, expectation, and deletion of the nonnegative terminal Bellman term give

`delta I
 <=(p-1) E int ||Z||^(p-1)||Y||
   +(p-1)/2 E int ||Z||^(p-2)||Y||^2`.

Holder implies

`delta I
 <=(p-1)I^((p-1)/p)J^(1/p)
   +(p-1)/2 I^((p-2)/p)J^(2/p)`.

For `R=(I/J)^(1/p)`,

`delta R^2 <=(p-1)R+(p-1)/2`.

The positive root is

`R_p^*
 =[(p-1)+sqrt(2(p-1))]/(3-p)
 =1/(sqrt(2/(p-1))-1)`.

The one-shell neutral-feedback construction attains this asymptotically. On one exact Fourier shell, after a finite-cost seed, set

`Y=gamma Z`,
`gamma=sqrt(2/(p-1))-1`.

Then, after shell time scaling,

`dZ=-Z dt+(1+gamma)Z dW`,

and the `p`-th moment exponent is

`-p+p(p-1)(1+gamma)^2/2=0`.

On a long scaled interval the seed cost becomes negligible and the output/input `L^p` ratio tends to `1/gamma=R_p^*`. High-frequency scaling places arbitrarily long scaled intervals inside every fixed physical horizon, so

`C_p^g(T)=R_p^*`, `2<=p<3`,

and `(3-p)C_p^g(T)->4`.

For the positive endpoint, let `F=||T_TY||_2` on `Omega x (0,T)`, `0<s<T`, and `ell=log(T/s)`. Rearrangement and finite-measure embedding give

`F^*(s)
 <=R_p^* s^(-1/p)T^(1/p-1/3)||Y||_3`.

For `ell>=3`, choose `p=3-3/ell`. Then

`R_p^*<=4ell/3`

and

`(T/s)^(1/p-1/3)=exp(1/p)<=sqrt(e)`.

The bounded `ell` region is handled by the exact `p=2` estimate. Consequently

`||T_TY||_{Z_{3,1}(T)} <=(1+sqrt(2))||Y||_3`,

where

`||F||_{Z_{3,alpha}(T)}
 =sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`.

Hence `alpha_*(T)<=1`.

For the lower side, the retained source-valid one-shell near-critical feedback is

`Y=gamma Z`, `sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`,

with

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`

on the feedback interval. Taking

`L_gamma=log(1/gamma)/(2gamma)`,
`kappa=2d/sigma^2`,
`t_*=L_gamma-2sqrt(L_gamma)`,
`x=dt_*`,

the Gaussian exponent satisfies the exact saddle identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`.

A Mills lower bound on a `sqrt(L_gamma)` saddle window and the exact identities

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

give

`||Z||_{Z_{3,alpha}}/||Y||_3
 >=c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`, and shell scaling transfers the witness to every fixed physical horizon. Therefore

`boxed{ 2/3 <= alpha_*(T) <= 1 }`.

This is the fixed parent bracket used below.

---

## 2. Why the previous finite-block gluing loss is not intrinsic to branch choice

The earlier finite-multiband theorem combined simultaneously present spectral blocks by a generic square-function estimate and obtained an `N^(1/6)` loss for `N` blocks. That estimate is correct for simultaneous overlap, but it leaves open whether an unbounded *number of possible packet locations* creates a real endpoint entropy loss when only one packet is chosen on each branch/restart.

The answer proved here is no. The logarithmic normalization itself has an exact Jensen compatibility with countable disjoint branching.

This matters for the current packet-migration program. The predecessor state-rigidity theorem says a bad high-level branch is increasingly localized in one moving three-dyadic-block packet. If one can restart at downcrossings and freeze the packet until the next restart, then the number and separation of possible packet locations is irrelevant: the endpoint constants glue with no loss. Therefore the unresolved cost is specifically packet change *before* a genuine restart.

---

## 3. Exact disjoint gluing lemma for `Z_{3,2/3}`

Let `(S,mu)` be a finite measure space, `mu(S)=T`, and let

`S = disjoint_union_j S_j`

be a finite or countable measurable partition with `T_j=mu(S_j)`. Ignore zero-measure pieces. For a function supported on `S_j`, define its local endpoint norm by rearrangement with respect to `mu|_{S_j}` and ambient mass `T_j`:

`||f||_{Z_j}
 =sup_{0<s<T_j} s^(1/3)f_j^*(s)
   /(1+log(T_j/s))^(2/3)`.

### Theorem 3.1 — exact countable branch gluing

Suppose `f_j` is supported on `S_j` and, for numbers `A_j>=0`,

`||f_j||_{Z_j} <= K A_j^(1/3)`

with one constant `K` independent of `j`. Put `f=sum_j f_j` and `A=sum_j A_j`. Then

`boxed{
 ||f||_{Z_{3,2/3}(S)} <= K A^(1/3).
}`

The gluing constant is exactly `1`; in particular it is independent of the number of pieces.

### Proof

Fix `R>0` and let

`s_j=mu({x in S_j: |f_j(x)|>R})`,
`s=sum_j s_j=mu({|f|>R})`.

Terms with `s_j=0` may be omitted. Set

`L_j=1+log(T_j/s_j)>=1`.

By the definition of decreasing rearrangement, for every `0<u<s_j` one has `f_j^*(u)>=R`; letting `u` increase to `s_j` in the local endpoint inequality gives

`R^3 s_j <= K^3 A_j L_j^2`,

or equivalently

`A_j >= R^3 s_j/(K^3 L_j^2)`.                         (3.1)

Let

`w_j=s_j/s`.

Since `T_j=s_j exp(L_j-1)`,

`T/s = sum_j w_j exp(L_j-1)`.

Define the global logarithmic scale

`L=1+log(T/s)`.

Then

`exp(L-1)=sum_j w_j exp(L_j-1)`.

Convexity of the exponential gives

`sum_j w_j L_j <= L`.                                  (3.2)

The function `x -> x^(-2)` is convex on `(0,infinity)`, so Jensen and (3.2) yield

`sum_j w_j/L_j^2
 >=1/(sum_j w_j L_j)^2
 >=1/L^2`.                                               (3.3)

Summing (3.1) and using (3.3),

`A
 >=R^3 s/K^3 * sum_j w_j/L_j^2
 >=R^3 s/(K^3 L^2)`.

Thus every level `R` satisfies

`R^3 mu({|f|>R})
 <=K^3 A [1+log(T/mu({|f|>R}))]^2`.                    (3.4)

The standard tail/rearrangement equivalence, obtained by applying (3.4) to levels below `f^*(s)` and then taking a limit, gives

`s^(1/3)f^*(s)
 <=K A^(1/3)[1+log(T/s)]^(2/3)`

for every `0<s<T`, proving the theorem.

The constant `1` cannot be improved at the level of this abstract gluing statement because the one-piece case is included.

### Remark 3.2 — the Jensen mechanism is not special to `2/3`

The same proof works for a logarithmic power `alpha>0`: local tail bounds

`R^3 s_j <=K^3 A_j L_j^(3alpha)`

glue with the same constant, since `x -> x^(-3alpha)` is convex and decreasing. The critical `alpha=2/3` case is exactly the square power used in (3.1)--(3.4).

---

## 4. Conditional branch scaling is exactly invariant

Suppose an event `E` has probability `pi>0`. On the conditional probability space `(E,P(.|E))`, let the time horizon be `H`, let `u` be a conditional spacetime quantile, and let a local critical estimate have size `a`:

`u^(1/3)F_E^*(u)
 <=a [1+log(H/u)]^(2/3)`.

In the original probability measure restricted to `E`, spacetime masses are multiplied by `pi`: the ambient mass is `pi H`, the quantile is `pi u`, and a cubic budget is multiplied by `pi`. Therefore

`(pi u)^(1/3) [pi^(-1/3)F_E^*(u)]
 /(1+log(pi H/(pi u)))^(2/3)`

is exactly the original local ratio. There is no branch-probability loss and no extra logarithm.

This exact invariance is the stochastic counterpart of the deterministic Jensen gluing in Section 3.

---

## 5. Countable stopping-time randomized-band restart theorem

The retained comparable-band endpoint theorem states the following. Let `E` be any `A`-invariant spectral subspace satisfying

`lambda_0 I <= A|_E <= K lambda_0 I`.

For zero initial state and arbitrary progressive `E`-valued forcing,

`||T_H Y||_{Z_{3,2/3}(H)}
 <=65 sqrt(K)||Y||_{L^3(Omega x (0,H);L^2)}`.            (5.1)

The constant is independent of `lambda_0` and the dimension of `E`.

### Theorem 5.1 — zero-seed countable randomized restart

Let `tau` be a stopping time and let `H>0` be deterministic. Let `(E_j)_j` be a finite or countable family of `A`-invariant spectral bands, each with condition ratio at most `K`. Let `J` be an `F_tau`-measurable countable-valued random index, and write

`Omega_j={J=j}`.

Consider the shifted Brownian motion

`W_hat(t)=W_{tau+t}-W_tau`, `0<=t<=H`,

and the restarted zero-initial equation

`dZ_hat=-A Z_hat dt+A^(1/2)(Z_hat+Y_hat)dW_hat`,
`Z_hat(0)=0`.

Assume that on `Omega_j`, the progressive restarted input `Y_hat` takes values in `E_j` for all `0<t<H`. Then

`boxed{
 ||Z_hat||_{Z_{3,2/3}(Omega x (0,H))}
 <=65 sqrt(K)
   ||Y_hat||_{L^3(Omega x (0,H);L^2)}.
}`                                                           (5.2)

There is no dependence on the number of possible bands or on their spectral separation.

### Proof

By the strong Markov property, `W_hat` is a Brownian motion independent of `F_tau`. Conditioning on an event `Omega_j in F_tau` preserves the Brownian law of future increments; the shifted input is progressive on that conditional filtered probability space. Hence (5.1) applies on each conditional branch with the same constant `65 sqrt(K)`.

Let

`J_j=E[1_{Omega_j} int_0^H ||Y_hat||^3 dt]`.

By the exact branch scaling of Section 4, the branch output, viewed on the restricted spacetime set `Omega_j x (0,H)` of mass `P(Omega_j)H`, satisfies the local endpoint estimate

`||1_{Omega_j}||Z_hat||||_{Z_j}
 <=65 sqrt(K) J_j^(1/3)`.

The sets `Omega_j x (0,H)` are disjoint. Apply Theorem 3.1 with

`A_j=J_j`

and `K` there replaced by `65 sqrt(K)` here. Since

`sum_j J_j=E int_0^H ||Y_hat||^3 dt`,

(5.2) follows.

### Corollary 5.2 — arbitrary random three-block packet location

For the three-adjacent-dyadic packet

`Pi_j=1_[2^(j-1),2^(j+2))(A)`,

the condition ratio is at most `8`. Thus an arbitrary `F_tau`-measurable countable choice of packet, followed by zero-seed forcing confined to that packet for the restart horizon, satisfies

`||Z_hat||_{Z_{3,2/3}}
 <=65 sqrt(8)||Y_hat||_3
 =130 sqrt(2)||Y_hat||_3
 <183.848||Y_hat||_3`.

The packet center may have an unbounded distribution. The theorem loses nothing from that countable spectral entropy.

This is the precise restart statement needed by the moving-packet program.

---

## 6. Nonzero restart seed: a passive critical `L^3` contraction

A high-level excursion restart generally carries a boundary state. The passive equation has an exact critical contraction that lets this seed be included without spectral-count loss.

Consider

`dU=-AU dt+A^(1/2)U dW`, `U(0)=x`.

In a spectral eigenbasis of `A`, write `A e_n=lambda_n e_n`, `a_n=sqrt(lambda_n)`, and

`x=sum_n x_n e_n`.

Then

`U_n(t)=x_n M_n(t)`,
`M_n(t)=exp(a_n W_t-3 lambda_n t/2)`.

If `x!=0`, put

`theta_n=|x_n|^2/||x||^2`.

Since `q -> q^(3/2)` is convex,

`||U_t||^3
 =||x||^3 (sum_n theta_n M_n(t)^2)^(3/2)
 <=||x||^3 sum_n theta_n M_n(t)^3`.

But

`E M_n(t)^3
 =E exp(3a_n W_t-9lambda_n t/2)
 =exp(9lambda_n t/2-9lambda_n t/2)
 =1`.

Therefore

`boxed{ E||U_t||^3 <=||x||^3 }`                         (6.1)

for every `t>=0`. For an `F_tau`-measurable random seed, condition on `F_tau` and use the shifted Brownian motion to get

`E_tau ||U_t||^3 <=||x||^3`.

Integrating over a restart horizon `H`,

`||U||_{L^3(Omega x (0,H);L^2)}
 <=H^(1/3)(E||x||^3)^(1/3)`.                            (6.2)

Since the `Z_{3,2/3}` norm is bounded by the ordinary `L^3` norm on a finite measure space,

`||U||_{Z_{3,2/3}(H)}
 <=H^(1/3)(E||x||^3)^(1/3)`.                            (6.3)

This estimate is full-spectrum; no band assumption is needed for the passive seed itself.

---

## 7. Countable restart theorem with branchwise band-supported seed

For later excursion use it is convenient to combine the passive seed with the forced band response.

First record a quasi-triangle constant for the endpoint norm. If `f,g` are scalar nonnegative functions on a measure space of mass `T`, then

`(f+g)^*(s)<=f^*(s/2)+g^*(s/2)`.

Writing `L(s)=1+log(T/s)`, we have

`L(s/2)=L(s)+log 2 <=(1+log2)L(s)`

because `L(s)>=1`. Therefore

`||f+g||_{Z_{3,2/3}}
 <=c_sum (||f||_{Z_{3,2/3}}+||g||_{Z_{3,2/3}})`,        (7.1)

where

`c_sum=2^(1/3)(1+log2)^(2/3)
      =1.789808115889274...`.

### Theorem 7.1 — branchwise band seed and forcing

Under the stopping-time branch setup of Theorem 5.1, assume in addition that the restart seed `x` is `F_tau`-measurable and, on `Omega_j`, lies in the same band `E_j` as the subsequent forcing. Let `Z_hat` start from `x`. Then

`boxed{
 ||Z_hat||_{Z_{3,2/3}(Omega x (0,H))}
 <=2(1+log2)^(2/3)
   [ H E||x||^3
     +(65 sqrt(K))^3 E int_0^H ||Y_hat||^3 dt
   ]^(1/3).
}`                                                           (7.2)

The numerical outside factor is

`2(1+log2)^(2/3)=2.841143285983855...`.

### Proof

On branch `Omega_j`, decompose by linearity

`Z_hat=U_j+V_j`,

where `U_j` is the passive solution from seed `x` and `V_j` is the zero-seed forced solution. By (6.3) and (5.1), after exact branch-probability scaling,

`||1_{Omega_j}||U_j||||_{Z_j}
 <=H^(1/3) X_j^(1/3)`,

`||1_{Omega_j}||V_j||||_{Z_j}
 <=65 sqrt(K) J_j^(1/3)`,

where

`X_j=E[1_{Omega_j}||x||^3]`,
`J_j=E[1_{Omega_j} int_0^H ||Y_hat||^3 dt]`.

Using (7.1), the local branch norm is at most

`c_sum [H^(1/3)X_j^(1/3)+65sqrt(K)J_j^(1/3)]`.

Apply Theorem 3.1 with local cubic budgets equal to the cubes of these local bounds. Since

`(a+b)^3<=4(a^3+b^3)`,

summing branch budgets gives at most

`4 c_sum^3 [H sum_j X_j +(65sqrt(K))^3 sum_j J_j]`.

Taking the cube root and observing

`4^(1/3)c_sum
 =2(1+log2)^(2/3)`

gives (7.2).

---

## 8. Demonstrated connection to the unresolved parent endpoint

This theorem is not presented as a more restrictive replacement for Agresti--Veraar Problem 3. The parent fixed-pair endpoint remains open. The point is that it removes a specific mechanism that had survived the finite-block theorem.

The predecessor chain had reached the following picture for a hypothetical branch with unusually large critical quantile:

1. the joint Bellman slack must be small;
2. the state is then close, in weighted spacetime average, to a three-adjacent-dyadic-block packet;
3. forcing outside that current packet is charged by the active-migration inequality;
4. after forcing stops, separated unequal scales have finite passive Hellinger memory.

The finite-multiband theorem still had an `N^(1/6)` simultaneous-block loss, so it was not previously clear whether an *unbounded number of possible packet centers* could by itself create an extra logarithmic entropy loss.

Theorem 3.1 and Theorem 5.1 show that it cannot, once the packet choice occurs at a genuine branch/restart. Countably many packet locations, arbitrarily far apart, glue at `alpha=2/3` with **exactly no count penalty**. Therefore a counterexample forcing `alpha_*(T)>2/3`, or the missing step in a proof of equality, must exploit packet migration **while the same high-level excursion is still alive**. Merely selecting a new packet after a restart does not generate the missing logarithm.

This turns the next target into a cleaner stopping-time statement:

> Let `tau_k` be successive high-level downcrossing/restart times. Charge every change of the selected three-block center before `tau_{k+1}` either to the active joint-slack migration term or, on intervals with no forcing, to the passive Hellinger/decoherence term. If the total center-change charge is summable in the cubic input budget, Theorem 5.1 glues all restart branches for free and the full `L^3 -> Z_{3,2/3}` endpoint follows.

So the current missing lemma is no longer an entropy summation over packet labels. It is a **within-excursion center-change Carleson estimate**.

---

## 9. A failed shortcut recorded explicitly

A tempting route is to use only the predecessor `L^2` packet leakage estimate and then apply the comparable-band log-radius drift on the good set. This does not work directly. An arbitrarily small amount of `L^2` state or forcing at extremely high frequency can dominate the instantaneous Rayleigh quotient `<Az,z>/||z||^2`, so `L^2` packet localization alone does not provide the pointwise spectral condition ratio needed by the band drift.

This is not a reason to abandon the packet route: the high-frequency leakage has a short physical lifetime, and the existing Bellman/Hellinger quantities are time-integrated. But it means the next proof must be a stopping-time/time-integrated migration argument, not a pointwise replacement of `A` by a packet condition number.

The exact restart gluing proved here is designed for that time-integrated approach.

---

## 10. Essential checker

The executed checker

`2026-09-20T18-49-01+0300__countable_branch_gluing_checker.py`

and its actual output

`2026-09-20T18-49-01+0300__countable_branch_gluing_checker.out`

verify:

- 30,000 randomized extremal-form instances of the disjoint Jensen inequality;
- the two Jensen substeps `sum w_j L_j<=L` and `sum w_j/L_j^2>=1/(sum w_j L_j)^2`;
- exact branch-probability scaling of the endpoint ratio;
- the closed form
  `4^(1/3)c_sum=2(1+log2)^(2/3)`;
- 500 randomized finite-spectrum Gauss--Hermite tests of the passive `L^3` contraction.

The archived output is

`c_sum=1.789808115889274`

`c_restart=2.841143285983855`

`c_restart_closed=2.841143285983855`

`worst_gluing_ratio=1.000000000000000`

`worst_avg_over_global=1.000000000000000`

`worst_reciprocal_jensen_ratio=1.000000000000000`

`max_passive_L3_ratio_GH120=0.999998731128453`

`max_branch_scaling_relative_error=6.661e-16`

`CHECK_PASS`.

The numerical checks support but do not replace the analytic proofs above.

---

## 11. Bounded current literature check

A bounded dated search was performed only to ensure that the exact frozen successor had not obviously been superseded.

- Agresti--Veraar's 2025 survey still states Problem 3 for nonsmall `B` as the extrapolation question from one stochastic maximal-regularity exponent to all `r>2` or at least a larger range.
- Bechtel--Veraar, published 11 July 2025, proves an extrapolation result in the variational setting under its coercive/self-adjoint framework, giving some range above `2`; it does not settle this frozen critical rearrangement endpoint.
- Evangelopoulos-Ntemiris--Veraar, published 13 February 2026, concerns discrete stochastic maximal regularity and discrete extrapolation.
- Lorist--van Neerven--Veraar, arXiv:2608.20266 dated 20 August 2026, studies necessary Banach-space geometry for deterministic and stochastic maximal regularity.
- Evangelopoulos-Ntemiris, arXiv:2609.07436 dated 7 September 2026, concerns fully discrete stochastic maximal regularity for elliptic finite-element/time-discrete schemes.

No source found in this bounded search resolves the exact nonsmall multiplicative torus endpoint treated here. This is not a worldwide novelty certificate.

---

## 12. Ledger summary and next attack

**Fixed source theorem before/after:** unchanged: `r_*=3`, strong endpoint excluded; exact `C_p^g`; full critical bracket `[2/3,1]`; conditional critical lower constant `4/9`.

**Strict mechanism gain:** exact countable disjoint gluing in `Z_{3,2/3}` plus a countable stopping-time randomized-band restart theorem with no packet-number or packet-separation loss, and a nonzero branchwise-band seed extension using the passive critical `L^3` contraction.

**Residual obstruction:** packet-center changes while a high-level excursion remains alive. The current state-only and joint Bellman slack estimates charge active migration in `L^2` geometry, while passive Hellinger controls off-input separated-scale coherence; a stopping-time Carleson estimate joining these charges is still missing.

**Next attack:** define restart times at fixed downcrossings. Between restarts, choose the best three-block packet at the excursion start. Prove that leaving that packet before the next downcrossing forces either (i) a definite integrated active-migration slack or (ii) a passive Hellinger charge. Sum those center changes; then invoke the exact countable restart gluing theorem from this run so the packet labels themselves cost nothing.

No historical or peer file was overwritten; no email, Drive, public posting, paid compute, access change, workflow execution, or schedule change was performed.
