Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-10 progress-extrapolation — approximate packet active-migration rigidity from the joint Bellman slack

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run remains on P24's already-frozen semigroup pair, preserves the actual NM13-10 successor chain, does not reopen the posted Agresti--Veraar Problems 4--5 package, and spends the mathematical effort on the residual active packet-migration obstruction left by the immediately preceding joint-Hessian-slack theorem.

New theorem status: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW** for the packet-migration theorem below. The parent critical endpoint remains **PARTIAL / OPEN**.

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
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`,
  with input and output measured in `L^p(Omega x (0,T);L^2(Torus))`.

Retained proved NM13-10 results include:

1. the strong fixed-pair endpoint `r_*=3`, with strong `p=3` excluded;
2. the exact subcritical stochastic-input norm
   `C_p^g=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, and `(3-p)C_p^g ->4`;
3. the full-spectrum rearrangement bracket `2/3<=alpha_*(T)<=1`;
4. the exact additive-shell saddle lower constant `4/9` at a possible full `alpha=2/3` endpoint;
5. one-shell and comparable-band `alpha=2/3` theorems, finite-multiband gluing, the full-spectrum little-`Z_{3,1}` theorem, and passive cross-scale Hellinger/decoherence;
6. the state spectral-variance defect, which forces near-extremal states into a moving three-adjacent-dyadic-block packet;
7. the immediately preceding joint Bellman slack `Sigma_p(z,y)`, whose zero cone is exactly one eigenspace with positive proportional forcing.

**Fixed strong endpoint before:** `r_*=3`, endpoint excluded.  
**Fixed strong endpoint after:** `r_*=3`, endpoint excluded.

**Full critical exponent bracket before:** `[2/3,1]`.  
**Full critical exponent bracket after:** `[2/3,1]`.

**Conditional full-pair `alpha=2/3` lower constant before/after:** `4/9 -> 4/9`.

Thus this run does not claim a source-level exponent change. Its gain is a new coercive bridge from the joint Bellman slack to *active forcing outside the moving packet*.

---

## 1. Complete retained proof behind the `[2/3,1]` bracket

### 1.1 Exact subcritical stochastic-input norm

For `p>=2`, define

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

Because `A` is positive self-adjoint on `L^2(Torus)`, differentiation along the semigroup gives

`D Psi_p(z)[-Az]=-||z||^p`.

The sharp Hessian contraction recovered and proved in the predecessor chain is

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`.

The Hessian is positive semidefinite, hence Hessian Cauchy--Schwarz also gives

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.

For stopped finite-dimensional approximations write

`I=E int_0^T ||Z||^p dt`,
`J=E int_0^T ||Y||^p dt`,
`delta=(3-p)/2`.

Ito applied to `Psi_p(Z)` yields, after expectation and discarding the nonnegative terminal term,

`delta I
 <=(p-1) E int ||Z||^(p-1)||Y||
   +(p-1)/2 E int ||Z||^(p-2)||Y||^2`.

Holder therefore gives

`delta I
 <=(p-1) I^((p-1)/p)J^(1/p)
   +(p-1)/2 I^((p-2)/p)J^(2/p)`.

For `R=(I/J)^(1/p)`, this is

`delta R^2 <=(p-1)R+(p-1)/2`.

The positive root equals

`R_p^*
 =[(p-1)+sqrt(2(p-1))]/(3-p)
 =1/(sqrt(2/(p-1))-1)`.

This upper bound is exact. On one exact Fourier shell, after scaling time by the shell eigenvalue, use a finite-cost seed and then the proportional feedback `Y=gamma Z` with

`gamma=sqrt(2/(p-1))-1`.

The shell equation is

`dZ=-Z dt+(1+gamma)Z dW`.

The choice of `gamma` makes the `p`-th moment neutral because

`-p+p(p-1)(1+gamma)^2/2=0`.

On a long scaled interval the seed cost is negligible and `||Z||_p/||Y||_p ->1/gamma=R_p^*`. High-frequency scaling embeds arbitrarily long scaled intervals into every fixed physical horizon. Therefore

`C_p^g(T)=R_p^*=1/(sqrt(2/(p-1))-1)`

for `2<=p<3`, and `(3-p)C_p^g(T)->4`.

### 1.2 Positive logarithmic endpoint

Let `F=||T_TY||_2` on `Omega x (0,T)`, let `0<s<T`, and put `ell=log(T/s)`. The exact `L^p` bound and finite-measure embedding give

`F^*(s)
 <=R_p^* s^(-1/p)T^(1/p-1/3)||Y||_3`.

For `ell>=3`, take

`p=3-3/ell`.

Then

`R_p^*=[(p-1)+sqrt(2(p-1))]/(3-p) <4ell/3`,

and

`ell(1/p-1/3)=1/p<=1/2`.

Hence

`s^(1/3)F^*(s)
 <=(4sqrt(e)/3) ell ||Y||_3`.

The bounded-`ell` region is covered by the exact `p=2` estimate. Therefore

`alpha_*(T)<=1`.

### 1.3 Lower obstruction below `2/3`

On one exact Fourier shell the scaled equation is

`dZ=-Z ds+(Z+Y)dB`.

After a finite-cost OU seed, on a fixed positive-probability event with `1<=Z_1<=2`, use the progressive near-critical feedback

`Y=gamma Z`, `0<gamma<<1`.

Set

`sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`.

Then

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`.

Take

`L_gamma=log(1/gamma)/(2gamma)`.

The input obeys `||Y||_3=gamma^(-1/3+o(1))`. Let

`kappa=2d/sigma^2`,
`t_*=L_gamma-2sqrt(L_gamma)`,
`x=dt_*`.

The Gaussian exponent has the exact saddle identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`.

A Mills lower bound on a `sqrt(L_gamma)` saddle window therefore gives spacetime tail at least `c exp(-kappa x)` at output level comparable to `exp(x)`. The exact algebraic identities

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

and the facts `q^2L_gamma->0`, `q sqrt(L_gamma)->0` yield

`||Z||_{Z_{3,alpha}}/||Y||_3
 >=c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`. Exact shell scaling transfers the construction to every fixed physical horizon, so

`alpha_*(T)>=2/3`.

Combining Sections 1.2 and 1.3 recovers the full reported bracket

`boxed{ 2/3 <= alpha_*(T) <= 1 }`.

---

## 2. Retained joint Bellman slack and state-packet rigidity

For `z!=0`, define

`H_{p,z}(u,v)
 :=D^2 Psi_p(z)[A^(1/2)u,A^(1/2)v]`.

Write `r=||z||`, `u=||y||` and

`a=H_{p,z}(z,z)`, `b=H_{p,z}(z,y)`, `c=H_{p,z}(y,y)`.

Set

`A0=(p-1)r^p`,
`B0=(p-1)r^(p-1)u`,
`C0=(p-1)r^(p-2)u^2`.

The predecessor joint slack is

`Sigma_p(z,y)=A0+2B0+C0-(a+2b+c)>=0`.

The exact Ito identity is

`E Psi_p(Z_T)+delta I_p+S_p/2
 =(p-1)E int ||Z||^(p-1)||Y||
 +(p-1)/2 E int ||Z||^(p-2)||Y||^2`,

where

`I_p=E int ||Z||^p`,
`J_p=E int ||Y||^p`,
`S_p=E int Sigma_p(Z,Y)`,
`sigma_p=S_p/I_p`,
`R_p=(I_p/J_p)^(1/p)`.

Consequently

`(delta+sigma_p/2)R_p^2
 <=(p-1)R_p+(p-1)/2`.                              (2.1)

The state component of the slack is

`Delta_p(z)
 =(p-1)||z||^p-H_{p,z}(z,z)
 =p(p-2) int_0^infinity
   Var_{mu_{z,s}}(sqrt(lambda)) ||e^{-sA}z||^p ds`.

Let `Q_j=1_[2^j,2^(j+1))(A)` and

`Pi_j=Q_{j-1}+Q_j+Q_{j+1}`

(with the obvious endpoint convention). Define

`d_3(z)=inf_j ||(I-Pi_j)z||/||z||`.

The preceding spectral-variance theorem proved

`Delta_p(z)/||z||^p
 >=c_* sum_{j<k, k-j>=2} theta_j theta_k`,

where

`theta_j=||Q_jz||^2/||z||^2`,

and

`c_*=5(3-2sqrt(2))/24`.

If `J,J'` are iid with law `(theta_j)`, then the probability that `|J-J'|>=2` equals twice the displayed separated-pair sum. Averaging the mass outside the three-block packet centered at `J` therefore shows that some packet satisfies

`d_3(z)^2
 <=(2/c_*) Delta_p(z)/||z||^p`.                    (2.2)

Write

`C_pack:=2/c_*
 =48(3+2sqrt(2))/5
 =55.952900397563...`.

Since `Sigma_p(z,y)>=Delta_p(z)`, (2.2) will let the new active-input estimate below inherit the already-proved state concentration.

---

## 3. New analytic lemma: Holder continuity of the Bellman Hessian in the state

Put

`phi_p(x)=||x||^p`,
`alpha=p-2 in [1/2,1)`.

For `x!=0`,

`D^2 phi_p(x)
 =p||x||^alpha [I+alpha P_x]`,

where `P_x` is the orthogonal projection onto `span{x}`; set `D^2phi_p(0)=0`.

### Lemma 3.1

For `5/2<=p<3`,

`||D^2phi_p(x)-D^2phi_p(w)||_op
 <=6p ||x-w||^alpha`.                                    (3.1)

#### Proof

Let `r=||x||`, `s=||w||`, `d=||x-w||`. Since `0<alpha<=1`,

`|r^alpha-s^alpha|<=d^alpha`.

Using

`D^2phi_p(x)=p r^alpha(I+alpha P_x)`,

write the difference as the sum of a radial term and a projection term. The radial term has norm at most

`p(1+alpha)d^alpha<=2p d^alpha`.

For the projection term, it is enough to show

`s^alpha ||P_x-P_w||<=4d^alpha`.

If `s<=2d`, this follows from `||P_x-P_w||<=2`. If `s>2d`, then the unit-vector estimate gives

`||P_x-P_w||<=4d/s`,

so

`s^alpha||P_x-P_w||
 <=4s^(alpha-1)d
 <=4(2d)^(alpha-1)d
 <=4d^alpha`.

Thus the projection term is at most `4p alpha d^alpha<=4p d^alpha`, proving (3.1).

### Corollary 3.2

For the Bellman Hessian,

`|H_{p,z}(u,v)-H_{p,w}(u,v)|
 <=3p ||z-w||^alpha ||u|| ||v||`.                         (3.2)

Indeed, insert (3.1) into the semigroup formula for `H`. Since `e^{-sA}` is contractive,

`||e^{-sA}(z-w)||<=||z-w||`,

and Cauchy--Schwarz together with the exact energy identity

`int_0^infinity ||A^(1/2)e^{-sA}u||^2 ds
 =||u||^2/2`

gives

`int_0^infinity
 ||A^(1/2)e^{-sA}u||\,||A^(1/2)e^{-sA}v|| ds
 <=||u||||v||/2`.

Multiplying `6p` by `1/2` proves (3.2).

This continuity estimate is the new technical bridge needed to perturb the exact-shell migration penalty to an approximately localized packet.

---

## 4. New pointwise theorem: approximate spectral-packet active-migration penalty

Let `P` be **any orthogonal spectral projection of `A`**, and set `Q=I-P`. For `z!=0`, define

`d_P(z)=||Qz||/||z||`.

### Theorem 4.1

For every `5/2<=p<3`, every `z!=0`, and every `y` (with the quotient interpreted as zero when `y=0`),

`boxed{
 Sigma_p(z,y)
 >=(p-1)||z||^(p-1) ||Qy||^2/||y||
   -22 d_P(z)^(p-2)||z||^(p-1)||y||.
}`                                                               (4.1)

#### Proof

Put

`z_0=Pz`, `h=Qz`, `r=||z||`, `u=||y||`, `d=||h||/r`,

and write

`b=H_{p,z}(z,y)`,
`b_0=H_{p,z_0}(z_0,y)`.

Because `P` is spectral, it commutes with `A` and the semigroup. If `y_Q=Qy`, then in the explicit semigroup formula for `H_{p,z_0}(z_0,y_Q)` both the first scalar product and the second-factor scalar product pair disjoint spectral subspaces. Therefore

`H_{p,z_0}(z_0,Qy)=0`,

and hence

`b_0=H_{p,z_0}(z_0,Py)`.

The sharp Hessian contraction gives

`b_0
 <=(p-1)||z_0||^(p-1)||Py||
 <=(p-1)r^(p-1)||Py||`.                                  (4.2)

Next,

`b-b_0
 =H_{p,z}(h,y)
  +[H_{p,z}(z_0,y)-H_{p,z_0}(z_0,y)]`.

The first term is bounded by Hessian Cauchy--Schwarz and the sharp diagonal contraction:

`|H_{p,z}(h,y)|
 <=(p-1)r^(p-2)||h||u
 =(p-1)d r^(p-1)u`.

The second term is bounded by Corollary 3.2:

`|H_{p,z}(z_0,y)-H_{p,z_0}(z_0,y)|
 <=3p ||h||^(p-2)||z_0||u
 <=3p d^(p-2) r^(p-1)u`.

Since `d<=1` and `p-2<=1`, one has `d<=d^(p-2)`. Also `(p-1)+3p=4p-1<=11`. Therefore

`b
 <=(p-1)r^(p-1)||Py||
   +11d^(p-2)r^(p-1)u`.                                  (4.3)

Recall `B0=(p-1)r^(p-1)u`. Since the state and input diagonal Hessian slacks are nonnegative,

`Sigma_p(z,y)
 =(A0-a)+(C0-c)+2(B0-b)
 >=2(B0-b)`.

By (4.3),

`B0-b
 >=(p-1)r^(p-1)(u-||Py||)
   -11d^(p-2)r^(p-1)u`.

Finally,

`u-||Py||
 =(u^2-||Py||^2)/(u+||Py||)
 =||Qy||^2/(u+||Py||)
 >=||Qy||^2/(2u)`.

Multiplying by `2` proves (4.1).

### Interpretation

For an *exactly* packet-supported state (`d_P=0`), forcing outside that packet costs a first-order Bellman alignment penalty

`Sigma_p(z,y)
 >=(p-1)||z||^(p-1)||Qy||^2/||y||`.

This is substantially stronger near the sharp cone than the purely quadratic input-direction Hessian defect. The new theorem shows that the penalty survives approximate state localization, with an explicit error of order `d_P^(p-2)`.

---

## 5. New integrated theorem on the exact frozen torus pair

For each nonzero `z`, choose a three-adjacent-dyadic-block packet `Pi(z)` attaining `d_3(z)`; ties are broken by the least center index. Since the block masses tend to zero at infinity, an attaining center exists, and this rule is measurable. Put

`Q(z)=I-Pi(z)`.

Define the active migration charge

`M_p
 :=E int_0^T
   ||Z||^(p-1) ||Q(Z)Y||^2/||Y|| dt`,                    (5.1)

with zero integrand on `{Y=0}`.

### Theorem 5.1

For `5/2<=p<3`, if `I_p>0`,

`boxed{
 M_p/I_p
 <=1/(p-1) [
      sigma_p
      +22 (C_pack sigma_p)^((p-2)/2)/R_p
   ].
}`                                                               (5.2)

#### Proof

Apply Theorem 4.1 pointwise with `P=Pi(Z)`, then integrate:

`(p-1)M_p
 <=S_p
  +22 E int d_3(Z)^(p-2)||Z||^(p-1)||Y||`.

Normalize by `I_p` and introduce the probability measure

`dmu=||Z||^p d(P x dt)/I_p`.

On `{Z!=0}`, set

`v=||Y||/||Z||`.

Then the error divided by `I_p` is

`E_mu[d_3^(p-2)v]`.

From (2.2) and `Delta_p<=Sigma_p`,

`E_mu[d_3^2]
 <=C_pack sigma_p`.                                      (5.3)

Let

`alpha=p-2`,
`q=2/(4-p)`.

The conjugate exponents `2/alpha` and `2/(2-alpha)=q` give

`E_mu[d_3^alpha v]
 <=(E_mu d_3^2)^(alpha/2)
   (E_mu v^q)^(1/q)`.

For `5/2<=p<3`, `q<=p`. Since `mu` is a probability measure,

`(E_mu v^q)^(1/q)
 <=(E_mu v^p)^(1/p)
 =(J_p/I_p)^(1/p)
 =1/R_p`.

Combining this with (5.3) proves (5.2).

This is the first estimate in the successor chain that simultaneously uses

- state spectral localization,
- the full joint state-input Bellman slack,
- and active forcing outside the *state-dependent moving packet*.

It is therefore directly targeted at the residual mechanism left open by the previous run.

---

## 6. Critical-quantile rigidity: large output forces both state and input to track one packet

Let

`F=||T_TY||_2`,
`ell=log(T/s)>=6`,
`p=3-3/ell`,

and define the normalized critical quantile height

`Q_s:=s^(1/3)F^*(s)/||Y||_3`.

The preceding joint-slack effective-gap theorem gives

`Q_s
 <=8ell/[3+min(sigma_p,1)ell]`.                         (6.1)

There is also a reverse link from the same quantile to the actual subcritical response ratio. Indeed,

`I_p^(1/p)>=s^(1/p)F^*(s)`,

while

`J_p^(1/p)<=T^(1/p-1/3)||Y||_3`.

Since for the chosen `p`,

`ell(1/p-1/3)=1/p`,

one gets

`R_p>=e^(-1/p)Q_s`.                                      (6.2)

### Corollary 6.1

If `Q_s>8`, then necessarily `sigma_p<1`, and

`boxed{ sigma_p <8/Q_s. }`                               (6.3)

Moreover the weighted state leakage satisfies

`boxed{
 [E int ||Z||^p d_3(Z)^2]/I_p
 <8 C_pack/Q_s
 =447.6232031805.../Q_s.
}`                                                               (6.4)

The normalized active migration charge obeys

`boxed{
 M_p/I_p
 <=1/(p-1)[
      8/Q_s
      +22 e^(1/p)(8C_pack/Q_s)^((p-2)/2)/Q_s
   ].
}`                                                               (6.5)

#### Proof

If `sigma_p>=1`, (6.1) gives `Q_s<8`; hence `Q_s>8` forces `sigma_p<1`. Rearranging (6.1) then gives (6.3). Equation (6.4) follows from (5.3). Finally insert (6.3) and the reciprocal of (6.2) into (5.2).

For a clean asymptotic numerical form, if

`Q_s>=Q_0:=8C_pack=447.6232031805...`,

then `(8C_pack/Q_s)<=1`, `(p-2)/2>=1/4`, `1/(p-1)<=2/3`, and `e^(1/p)<1.5`. Therefore

`boxed{
 M_p/I_p
 <=16/(3Q_s)
   +22(8C_pack)^(1/4) Q_s^(-5/4)
 <5.334 Q_s^(-1)+101.194 Q_s^(-5/4).
}`                                                               (6.6)

### Consequence for any putative exponent above `2/3`

Suppose along a sequence `s_k downarrow0` one had

`Q_{s_k} >=c ell_k^beta`,

with `beta>2/3` and `ell_k=log(T/s_k)->infinity`. Then (6.3)--(6.6) imply

`[E int ||Z||^p d_3(Z)^2]/I_p =O(ell_k^(-beta))`,

and

`M_p/I_p=O(ell_k^(-beta))`.

Thus every genuinely supercritical branch is forced into the following simultaneous rigidity:

1. the state lies, in response-weighted spacetime average, inside a moving three-adjacent-dyadic-block packet;
2. active forcing outside that very packet has vanishing Bellman migration charge;
3. the vanishing rate is at least the inverse critical quantile height.

This is stronger than the previous state-only packet theorem and stronger than the preceding exact-shell alignment formula: it is an *approximate moving-packet* theorem on the full frozen spectrum.

---

## 7. What remains open, and why this is a demonstrated mechanism gain rather than a restricted substitute

The source-level bracket is still `[2/3,1]`; no stronger uniform exponent is claimed here. The new theorem instead narrows the only possible mechanism for failure of the critical `2/3` endpoint.

Previously known pieces now fit as follows:

- variance-rich states already satisfy the desired critical scale through the effective-gap estimate;
- a fixed shell or comparable spectral band already has the full `2/3` endpoint;
- finitely many bands can be glued, though with a band-count loss;
- passive unequal-scale coherence has finite memory by the Hellinger/decoherence theorem;
- the joint Bellman slack vanishes only on one-shell positive proportional forcing;
- **new here:** even when the state is only approximately localized, forcing outside its instantaneous three-block packet pays the quantitative charge (4.1), and every large critical quantile forces that charge to vanish as in (6.5)--(6.6).

Therefore a counterexample with exponent strictly above `2/3` cannot merely spread over many frequencies at once, and cannot merely use nonaligned forcing. It must perform a more specific maneuver: **move a narrow, nearly aligned packet through unboundedly many dyadic locations while keeping the cumulative migration charge small.**

The next decisive target is consequently a stopping-time/Carleson estimate for changes of the selected packet center. The natural ingredients are now all quantitative: use (4.1) on active intervals to charge forcing that creates a new packet, and use the existing Hellinger gap kernel on passive intervals to charge separated old/new packets. A summable center-jump estimate would close the remaining multiscale obstruction and is the next direct route to the full `L^3 -> Z_{3,2/3}` theorem.

No T05 fallback is triggered in this run because a strict new theorem-level mechanism gain was obtained.

---

## 8. Essential checks actually executed

The immutable checker

`2026-09-20T17-50-29+0300__packet_migration_checker.py`

was executed before persistence. It verifies:

1. `c_*=0.035744349011210...` and
   `C_pack=55.952900397563489...`;
2. the exponent compatibility `q=2/(4-p)<=p` throughout the required range;
3. 5,000 randomized finite-dimensional tests of the Hilbert-space Hessian Holder bound, with observed maximal ratio `1.907608720855<6`;
4. 240 randomized diagonal-spectral tests of the new pointwise migration inequality, including 146 tests where its lower bound was positive; the smallest numerical margin was `1.868507584070e+00`;
5. the simplified critical constants
   `Q_0=447.623203180508...` and
   `22(8C_pack)^(1/4)=101.193083221760...`.

The archived output ends `CHECK_PASS`.

These numerical tests are sanity checks only; Sections 3--6 contain the analytic proof.

---

## 9. Bounded current literature check

A bounded search on 20 September 2026 still found Agresti--Veraar arXiv:2501.18561 as the Problem-3 source. Recent related work found in the same bounded search includes Lorist--van Neerven--Veraar, arXiv:2608.20266 (20 August 2026), on necessary Banach-space geometric conditions for deterministic/stochastic maximal regularity, Evangelopoulos-Ntemiris--Veraar, arXiv:2505.22145, on discrete stochastic maximal regularity and discrete extrapolation, and Evangelopoulos-Ntemiris, arXiv:2609.07436 (7 September 2026), on fully discrete stochastic maximal regularity. None of those search hits states a resolution of this exact nonsmall state-multiplicative torus rearrangement endpoint. This is only a bounded dated search, not a worldwide novelty certificate.

---

## 10. Ledger-level conclusion

**Fixed theorem before:** strong endpoint `r_*=3`, `p=3` excluded; exact `C_p^g`; full critical bracket `[2/3,1]`; conditional critical lower constant `4/9`.

**Fixed theorem after:** unchanged.

**New demonstrated gain:** the pointwise approximate spectral-packet migration inequality (4.1), its full-spectrum integrated form (5.2), and the critical-quantile rigidity estimates (6.3)--(6.6). Large critical quantiles now force not only state packet concentration but also quantitative suppression of active forcing outside the same moving packet.

**Residual obstruction:** control the cumulative cost of changes in the packet center. The next attack is a packet-center stopping-time Carleson estimate combining the new active charge with the existing passive Hellinger/decoherence kernel.
