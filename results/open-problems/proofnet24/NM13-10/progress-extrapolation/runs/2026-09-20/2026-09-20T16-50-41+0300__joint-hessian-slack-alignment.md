Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-10 progress-extrapolation — joint Bellman Hessian slack, sharp-cone stability, and active-migration penalty

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run stays on P24's already-frozen semigroup pair, preserves the productive NM13-10 successor chain, does not reopen the already-written Agresti--Veraar Problems 4--5 package, and uses a different mechanism from the immediately preceding state-only spectral-variance stability argument: the full joint state-input Hessian slack.

New theorem status: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW** for the joint-slack theorem below. The parent critical endpoint remains **PARTIAL / OPEN**.

## 0. Short predecessor handoff and fixed theorem before/after

The frozen realization is unchanged:

- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)`;
- one real Brownian driver, `beta=1`;
- after the source-scale transform,
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`,
  with input and output in `L^p(Omega x (0,T);L^2(Torus))`.

Retained predecessor facts:

1. strong fixed-pair endpoint `r_*=3`, with the `p=3` strong endpoint excluded;
2. exact subcritical stochastic-input norm
   `C_p^g=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, and `(3-p)C_p^g ->4`;
3. for
   `||F||_{Z_{3,alpha}(T)}=sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`,
   the full-spectrum critical bracket is `2/3<=alpha_*(T)<=1`;
4. the exact additive saddle witness gives the conditional full-pair lower operator constant `4/9` at a possible `alpha=2/3` endpoint;
5. one-shell and comparable-band critical `2/3` bounds, finite multiband gluing, the full-spectrum little-`Z_{3,1}` theorem, passive cross-scale Hellinger/decoherence, and the immediately preceding exact state spectral-variance Hessian defect remain productive successors.

**Fixed strong endpoint before:** `r_*=3`, endpoint excluded.  
**Fixed strong endpoint after:** `r_*=3`, endpoint excluded.

**Full critical exponent bracket before:** `[2/3,1]`.  
**Full critical exponent bracket after:** `[2/3,1]`.

**Conditional full-pair `alpha=2/3` lower constant before/after:** `4/9 -> 4/9`.

The advance below is therefore a mechanism theorem on the exact frozen pair, not a false source-level exponent change.

---

## 1. Complete retained proof behind the `[2/3,1]` bracket

### 1.1 Exact subcritical norm

For `p>=2`, set

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

The source-scale semigroup identities used by P24/NM13-10 are

`D Psi_p(z)[-Az]=-||z||^p`,

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`,

and, by positivity of the Hessian and Hessian Cauchy--Schwarz,

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.

For stopped finite-dimensional approximations write

`I=E int_0^T ||Z||^p dt`, `J=E int_0^T ||Y||^p dt`,
`delta=(3-p)/2`.

Ito applied to `Psi_p(Z)` and the three sharp Hessian bounds gives

`delta I
 <=(p-1)I^((p-1)/p)J^(1/p)
   +(p-1)/2 I^((p-2)/p)J^(2/p)`.

If `R=(I/J)^(1/p)`, then

`delta R^2 <=(p-1)R+(p-1)/2`.

The positive root is

`R <= [(p-1)+sqrt(2(p-1))]/(3-p)
    =1/(sqrt(2/(p-1))-1)=:R_p^*`.

The retained one-shell neutral-feedback construction attains this asymptotically on every fixed physical horizon after high-frequency scaling, so the norm is exact. In particular `(3-p)R_p^* ->4`.

### 1.2 Positive logarithmic endpoint

Let `F=||T_TY||_2` on `Omega x (0,T)` and `ell=log(T/s)`. Finite-measure embedding yields

`F^*(s) <= R_p^* s^(-1/p)T^(1/p-1/3)||Y||_3`.

For `ell>=3`, take `p=3-3/ell`. Then `R_p^*<=4ell/3` and

`ell(1/p-1/3)=1/p<=1/2`.

Thus

`s^(1/3)F^*(s) <= (4sqrt(e)/3) ell ||Y||_3`,

and the bounded-`ell` region is covered by the exact `p=2` estimate. Hence `alpha_*(T)<=1`.

### 1.3 Lower obstruction below `2/3`

On one exact Fourier shell, scaled time gives

`dZ=-Z ds+(Z+Y)dB`.

After a finite-cost OU seed, on a fixed positive-probability event with `1<=Z_1<=2`, use the progressive near-critical feedback

`Y=gamma Z`, `0<gamma<<1`.

Let

`sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`,

so

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`.

With

`L_gamma=log(1/gamma)/(2gamma)`,

one has `||Y||_3=gamma^(-1/3+o(1))`. If

`kappa=2d/sigma^2`, `t_*=L_gamma-2sqrt(L_gamma)`, `x=dt_*`,

then the Gaussian exponent has the exact saddle identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`.

A Mills lower bound on a `sqrt(L_gamma)` saddle window gives a spacetime tail `m_x>=c exp(-kappa x)` at output level comparable to `exp(x)`. The exact identities

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

and `q^2L_gamma ->0`, `q sqrt(L_gamma)->0` imply

`||Z||_{Z_{3,alpha}}/||Y||_3
 >=c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`, and exact shell scaling transfers the witness to every fixed physical horizon. Therefore `alpha_*(T)>=2/3`.

Combining 1.2 and 1.3 gives the retained full proof of

`boxed{ 2/3 <= alpha_*(T) <= 1 }`.

---

## 2. New object: the full joint Bellman Hessian slack

For `z!=0`, define the positive-semidefinite bilinear form

`H_{p,z}(u,v)
 :=D^2 Psi_p(z)[A^(1/2)u,A^(1/2)v]`.

Write

`r=||z||`, `u=||y||`,

`a=H_{p,z}(z,z)`, `b=H_{p,z}(z,y)`, `c=H_{p,z}(y,y)`.

The sharp diagonal Hessian bounds and Hessian Cauchy--Schwarz give

`a <= A0:=(p-1)r^p`,

`c <= C0:=(p-1)r^(p-2)u^2`,

`b <= sqrt(ac) <= sqrt(A0 C0)=:B0=(p-1)r^(p-1)u`.

Define the total sharp-envelope slack

`boxed{
 Sigma_p(z,y)
 :=A0+2B0+C0-(a+2b+c).
}`                                                         (2.1)

Then `Sigma_p(z,y)>=0`. More precisely,

`Sigma_p
 =(A0-a)+(C0-c)
  +2(sqrt(A0C0)-sqrt(ac))
  +2(sqrt(ac)-b).`                                         (2.2)

Every term on the right is nonnegative. This simultaneously records three independent losses:

- the state Hessian loss `A0-a`;
- the input-direction Hessian loss `C0-c`;
- the Hessian Cauchy/alignment loss `sqrt(ac)-b`, together with the mismatch between the diagonal envelopes and actual diagonal Hessians.

The immediately preceding run identified the first term exactly:

`A0-a=Delta_p(z)`

with

`Delta_p(z)
 =p(p-2) int_0^infinity
 Var_{mu_{z,s}}(sqrt(lambda)) ||e^{-sA}z||^p ds.`           (2.3)

Hence

`Sigma_p(z,y)>=Delta_p(z)`                                 (2.4)

but `Sigma_p` is strictly stronger: it can be positive even when `z` lies in a single eigenspace and therefore `Delta_p(z)=0`.

---

## 3. Exact Ito identity and a stronger effective gap

For the transformed equation

`dZ=-AZ dt+A^(1/2)(Z+Y)dW`,

Ito gives, before taking expectations,

`d Psi_p(Z)
 =[-||Z||^p + (1/2)H_{p,Z}(Z+Y,Z+Y)]dt + dM_t`.

By the definition of `Sigma_p`, the drift can be written *exactly* as

`-delta ||Z||^p
 +(p-1)||Z||^(p-1)||Y||
 +(p-1)/2 ||Z||^(p-2)||Y||^2
 -(1/2)Sigma_p(Z,Y)`,                                      (3.1)

where `delta=(3-p)/2`.

After finite-dimensional stopping/localization, expectation, and the same projection/localization limit used in the recovered P24 proof, set

`I_p=E int_0^T ||Z||^p dt`,
`J_p=E int_0^T ||Y||^p dt`,
`S_p=E int_0^T Sigma_p(Z,Y) dt`.

Then

`E Psi_p(Z_T)+delta I_p+(1/2)S_p
 =(p-1) E int ||Z||^(p-1)||Y||
 +(p-1)/2 E int ||Z||^(p-2)||Y||^2.`                      (3.2)

This is stronger than the previous state-only inequality because no joint Hessian loss has been discarded.

When `I_p>0`, define

`sigma_p=S_p/I_p`,

`R_p(Y)=(I_p/J_p)^(1/p)`.

Holders inequality in (3.2) gives the new effective-gap estimate

`boxed{
 (delta+sigma_p/2) R_p(Y)^2
 <=(p-1)R_p(Y)+(p-1)/2.
}`                                                         (3.3)

Since `S_p>=D_p:=E int Delta_p(Z)`, one has `sigma_p>=kappa_p=D_p/I_p`; thus (3.3) strictly strengthens the previous spectral-variance effective gap whenever there is any input-direction or alignment loss.

---

## 4. Stronger full-spectrum critical quantile refinement

Let

`ell=log(T/s)>=6`, `p_ell=3-3/ell`, `delta=3/(2ell)`.

Put

`bar_sigma_p=min(sigma_p,1)`.

Replacing `sigma_p` by `bar_sigma_p` weakens the left side of (3.3), so it remains valid. For `p>=5/2`,

`epsilon=delta+bar_sigma_p/2 <=3/4<1`.

With `b=p-1<=2`, the positive root of

`epsilon R^2 <= bR+b/2`

satisfies

`R <=(1+sqrt(2))/epsilon
   =2(1+sqrt(2)) ell/(3+bar_sigma_p ell)`.

The same finite-measure embedding as in the retained endpoint proof gives the factor `exp(1/p)<=sqrt(e)`. Since

`2(1+sqrt(2))sqrt(e)
 =7.960730504594...<8`, one obtains

`boxed{
 s^(1/3)F^*(s)
 <= 8 ell/(3+min(sigma_{p_ell},1) ell) ||Y||_3.
}`                                                         (4.1)

This is a strict improvement of the preceding state-only bound because `min(sigma_p,1)>=kappa_p` (the preceding theorem has `0<=kappa_p<=p-2<=1`).

Consequences:

- if `sigma_{p_ell}>=c ell^(-2/3)`, then (4.1) is already at the desired critical `ell^(2/3)` scale;
- therefore any branch capable of forcing growth strictly above the critical scale must satisfy
  `sigma_{p_ell}=o(ell^(-2/3))` along the obstructing quantiles;
- unlike `kappa_p`, this condition suppresses not only spectral variance of the state but also non-extremal state-input geometry.

This is the new extrapolation mechanism applied directly to the exact unresolved full-spectrum claim.

---

## 5. Near-sharp subcritical responses must annihilate the *joint* slack

Let `R_p^*` be the exact sharp subcritical norm from Section 1, so

`delta=(p-1)/R_p^* +(p-1)/(2(R_p^*)^2)`.

Assume

`R_p(Y)>=q R_p^*`, `0<q<=1`.

From (3.3), using that the right-hand side divided by `R^2` is decreasing in `R`,

`sigma_p/2
 <= (p-1)/R_p(Y)+(p-1)/(2R_p(Y)^2)-delta
 <= delta(q^(-2)-1)`.

Hence

`boxed{
 sigma_p <=2 delta(q^(-2)-1).
}`                                                         (5.1)

If `q=1-epsilon>=1/2`, then

`q^(-2)-1 <=6 epsilon`,

so

`boxed{
 sigma_p <=12 epsilon delta.
}`                                                         (5.2)

Thus an asymptotically sharp sequence `R_p(Y)/R_p^* ->1` as `p->3` satisfies

`sigma_p=o(delta)`.

Because `Sigma_p` dominates every term in the nonnegative decomposition (2.2), this means simultaneously:

- the state spectral-variance defect is `o(delta I_p)`;
- the input-direction Hessian defect is `o(delta I_p)`;
- the Hessian Cauchy/alignment defect is `o(delta I_p)`.

This is stronger than the preceding packet-rigidity theorem, which controlled only the first item.

### 5.1 Quantitative cross-Hessian saturation

Define

`K_1=E int ||Z||^(p-1)||Y||`,

and, when `K_1>0`,

`chi_p
 := [E int H_{p,Z}(Z,Y)] / [(p-1)K_1]`.

Pointwise `H_{p,Z}(Z,Y)<=B0`, and by (2.1)

`Sigma_p >=2(B0-H_{p,Z}(Z,Y))`.

Hence

`1-chi_p <= (S_p/2)/[(p-1)K_1]`.                         (5.3)

From (3.2) and Holder,

`(p-1)K_1
 >=delta I_p -(p-1)/(2R_p(Y)^2) I_p`.

For `5/2<=p<3` the executed exact check gives

`[(p-1)/(2(R_p^*)^2)]/delta
 <=0.071796769724491`.

Therefore if `q>=1/2`,

`(p-1)K_1 >=(1-0.071797/q^2)delta I_p`,

and combining with (5.1) gives

`boxed{
 1-chi_p <=1.41(q^(-2)-1).
}`                                                         (5.4)

In particular, for asymptotically sharp responses `q->1`,

`chi_p ->1`.

So the sharp `(3-p)^(-1)` blow-up is possible only when the *cross* Hessian term asymptotically saturates its positive envelope as well as the state Hessian term. This is the active-forcing rigidity missing from the state-only variance theorem.

---

## 6. Exact shell formula: the sharp cone is positive proportional feedback

The preceding alignment statement becomes completely explicit on a single eigenspace.

Assume

`Az=a^2 z`, `z!=0`, `e=z/||z||`.

Decompose an arbitrary `y` as

`y=eta e + y_0 + sum_{b!=a} y_b`,

where `y_0` lies in the same eigenspace as `z` and is orthogonal to `e`, while `Ay_b=b^2y_b`.

Direct integration in the definition of `H_{p,z}` gives

`H_{p,z}(z,z)=(p-1)r^p`,

`H_{p,z}(z,y)=(p-1)r^(p-1)eta`,

and

`H_{p,z}(y,y)
 =r^(p-2)[
   (p-1)eta^2+||y_0||^2
   +sum_{b!=a} c_p(b/a)||y_b||^2
 ]`,

where

`c_p(x)=p x^2/(p-2+2x^2)`.

Consequently the joint slack has the exact closed form

`boxed{
 Sigma_p(z,y)
 =2(p-1)r^(p-1)(||y||-eta)
  +r^(p-2)[
    (p-2)||y_0||^2
    +sum_{b!=a} d_p(b/a)||y_b||^2
  ],
}`                                                         (6.1)

with

`d_p(x)
 =(p-1)-c_p(x)
 =(p-2)[(p-1)+x^2]/[p-2+2x^2]
 >=(p-2)/2.`                                               (6.2)

Every term in (6.1) is nonnegative. Therefore

`boxed{
 Sigma_p(z,y)=0
 iff y=gamma z for some gamma>=0.
}`                                                         (6.3)

Combining this with the preceding exact state-defect identity gives the global equality characterization for `p>2`:

`boxed{
 Sigma_p(z,y)=0
 iff z lies in one eigenspace of A and y=gamma z, gamma>=0.
}`                                                         (6.4)

This identifies the exact sharp cone behind the P24/NM13-10 one-shell feedback obstruction. It is not an accident that the lower witness uses positive proportional feedback: those are exactly the joint Bellman directions in which *all* sharp-Hessian slack disappears.

There is also an explicit migration penalty. Since

`||y||-eta
 >= (||y||^2-eta^2)/(2||y||)`

for `y!=0`, (6.1) implies

`Sigma_p(z,y)
 >=(p-1)r^(p-1)
   [||y-eta e||^2/||y||]
  +(p-2)/2 r^(p-2)||y-eta e||^2.`                         (6.5)

Thus, at an exact shell state, forcing that turns away from the current state direction or injects a new Fourier shell pays an explicit linear-plus-quadratic Bellman slack. This is precisely the coercive quantity needed to charge active packet migration.

---

## 7. Connection to the preceding packet theorem and residual obstruction

The previous run proved that near-sharp subcritical responses have small weighted distance to a three-adjacent-dyadic packet; more precisely, with the previous constant

`c_*=5(3-2sqrt(2))/24`,

`E int ||Z||^p d_3(Z)^2 / I_p
 <= (2/c_*) kappa_p`.

Since `kappa_p<=sigma_p`, (5.1) now yields the joint near-extremizer statement

`E int ||Z||^p d_3(Z)^2 / I_p
 <= (4 delta/c_*)(q^(-2)-1)`,

while at the same time (5.4) forces cross-Hessian saturation. Thus a near-sharp branch is not merely a moving narrow state packet: its active forcing must also follow the positive sharp-Hessian cone.

This materially narrows the unresolved mechanism:

1. variance-rich states already satisfy the critical `2/3` quantile scale by the preceding effective-gap theorem;
2. a fixed or comparable packet already has the critical `2/3` endpoint by the one-band/comparable-band excursion theorem;
3. passive separated packets lose common-noise coherence with the already-proved summable Hellinger/decoherence kernel;
4. the present theorem shows that active forcing which departs from the current sharp packet/direction creates a positive joint Bellman slack and therefore cannot remain near the sharp subcritical blow-up for free.

The remaining bridge is quantitative rather than conceptual: prove an **approximate packet version of (6.5)**. Namely, if `Z` has small leakage outside a three-block packet, lower-bound `Sigma_p(Z,Y)` by a weighted amount of forcing outside that packet, up to an error controlled by the state leakage. Combining that with the previous packet-rigidity estimate and the passive Hellinger kernel is the concrete active packet-migration Carleson route toward the full `Z_{3,2/3}` endpoint.

This run therefore produced a strict mechanism theorem and does not trigger the T05 fallback.

---

## 8. Essential checks

Executed checker:

`2026-09-20T16-50-41+0300__joint_hessian_alignment_check.py`

Actual archived output:

`2026-09-20T16-50-41+0300__joint_hessian_alignment_check.out`

It verifies:

- `2(1+sqrt(2))*sqrt(e)=7.960730504594505<8`;
- `((1-eps)^(-2)-1)/eps<=6` on `0<eps<=1/2`;
- the exact shell coefficient identity
  `d_p(x)=(p-2)[(p-1)+x^2]/(p-2+2x^2)` and `d_p(x)>=(p-2)/2`;
- 10,000 random shell decompositions agree with the closed formula (6.1) to relative error below `1.1e-13`, with nonnegative slack;
- the sharp-root relation and the `q`-near-sharp slack bound;
- `[(p-1)/(2(R_p^*)^2)]/delta <=0.071796769724491` for `5/2<=p<3`, giving the cross-saturation denominator factor `<1.41` for `q>=1/2`.

The archived execution ends `CHECK_PASS`.

---

## 9. Bounded current literature boundary

A fresh bounded search was performed only for source-matching developments. Agresti--Veraar arXiv:2501.18561 remains the source and states Problem 3 as extrapolation of stochastic maximal regularity when `B` is not small. Bechtel--Veraar's variational extrapolation result was published 11 July 2025 and gives an interval above `2` in its variational/self-adjoint setting, not this frozen critical rearrangement endpoint. Lorist--van Neerven--Veraar arXiv:2608.20266 (20 August 2026) studies necessary Banach-space geometry conditions for stochastic maximal regularity. The 2026 discrete stochastic maximal-regularity work concerns equivalence with temporal numerical schemes and discrete extrapolation. The bounded search did not locate a source-matching resolution of the exact P24 successor; this is not a worldwide novelty certificate.

---

## 10. Ledger delta and next attack

**Source-level movement:** none. The strong endpoint remains `3` excluded and the full critical exponent bracket remains `[2/3,1]`.

**Demonstrated mechanism gain:** the state-only spectral variance has been upgraded to an exact **joint** state-input Bellman slack. It enters the maximal-regularity inequality as additional coercivity, strictly strengthens the data-dependent critical extrapolation bound, quantitatively vanishes on near-sharp subcritical responses, and has an exact equality cone: one eigenspace plus nonnegative proportional feedback. This identifies and penalizes active migration away from the one-shell sharp mechanism.

**Residual obstruction:** the exact shell migration penalty must be made robust when the state is only approximately localized in a moving three-dyadic-block packet.

**Next attack:** prove that robust approximate-packet lower bound for `Sigma_p`, then combine it with the preceding packet leakage estimate and the passive common-Brownian Hellinger kernel to obtain a summable active packet-migration Carleson charge.

No historical or peer file was overwritten; no email, Drive, public posting, paid compute, access change, or schedule change was used.
