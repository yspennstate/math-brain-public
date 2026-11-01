Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-10 progress-extrapolation — frequency-weighted hysteretic packet migration at the critical scale

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run stays on P24's already-frozen semigroup pair, preserves the productive NM13-10 successor chain, does not reopen the already-written Agresti--Veraar Problems 4--5 package, and attacks the within-excursion packet-migration obstruction left by the immediately preceding countable-restart theorem.

The new theorem below is **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**. The parent unrestricted critical endpoint remains **PARTIAL / OPEN**.

A pre-report sanity check caught an essential physical-frequency factor in a first unweighted draft of the block-hitting argument. The final theorem below is the corrected frequency-weighted statement; no unweighted center-count theorem is claimed.

---

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

The immediately preceding substantive report was

`2026-09-20T18-49-01+0300__countable-branch-critical-gluing.md`

with reported commit

`f7b476e3992ded33ccd319021e65fb356cc7c950`.

It proved exact countable disjoint gluing at `Z_{3,2/3}` and a countable stopping-time randomized-band restart theorem: once a genuine restart has occurred and the selected packet is `F_tau`-measurable, countably many possible packet labels cause no endpoint loss. The residual obstruction was packet-center change while the same high-level excursion remained alive.

Retained earlier NM13-10 results include:

1. the exact subcritical frozen-pair stochastic-input norm;
2. the full critical rearrangement bracket `[2/3,1]` and the conditional `4/9` lower endpoint constant;
3. exact one-shell and comparable-band `alpha=2/3` theorems;
4. the full-spectrum little-`Z_{3,1}` theorem;
5. passive unequal-shell Hellinger/decoherence with a horizon-independent finite-memory constant;
6. the exact state spectral-variance Bellman defect;
7. the joint state-input Bellman slack and near-extremizer alignment;
8. approximate three-block active-migration coercivity.

**Fixed strong endpoint before:** `r_*=3`, strong `p=3` excluded.  
**Fixed strong endpoint after:** `r_*=3`, strong `p=3` excluded.

**Exact subcritical norm before/after:**

`C_p^g(T)=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)C_p^g(T)->4`.

**Full critical rearrangement bracket before:** `[2/3,1]`.  
**Full critical rearrangement bracket after:** `[2/3,1]`.

**Conditional full-pair `alpha=2/3` lower constant before/after:** `4/9 -> 4/9`.

Thus the source-level theorem is unchanged. The strict gain is a new critical Carleson estimate on **within-excursion packet migration in the correct inverse-frequency parabolic clock**.

---

## 1. Exact source Problem 3 and the frozen P24 claim

The published survey asks:

> If `(A,B) in SMR^bullet_{p,0}` for some `p in [2,infinity)`, and `B` is not assumed small, must `(A,B)` belong to `SMR^bullet_{r,0}` for every `r>2`, or at least for a larger range of `r`?

The frozen P24 pair is a concrete nonsmall self-adjoint realization inside this source problem, not a replacement by an easier operator. The present endpoint problem is the critical behavior of the stochastic-input map for

`dZ=-AZ dt+A^(1/2)(Z+Y)dW`.

For the scalar output

`F(omega,t)=||Z_t(omega)||_{L^2(Torus)}`

and

`L_T(s)=1+log(T/s)`,

define

`||F||_{Z_{3,alpha}(T)}
 =sup_{0<s<T} s^(1/3)F^*(s)/L_T(s)^alpha`.

The full frozen-pair unresolved endpoint is the least `alpha` for which

`||T_TY||_{Z_{3,alpha}(T)} <= C ||Y||_{L^3(Omega x (0,T);L^2)}`

holds uniformly for all progressive inputs. Its current bracket is `[2/3,1]`.

---

## 2. Full retained proof of the exact subcritical norm and the `[2/3,1]` bracket

This section is included so the new theorem does not rely on an unverified inherited number.

### 2.1 Bellman functional and sharp Hessian contraction

For `p>=2`, put

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

Let `z_s=e^{-sA}z`, `y_s=e^{-sA}y`, and `r_s=||z_s||`. Semigroup differentiation gives

`D Psi_p(z)[-Az]=-||z||^p`.

For the Hessian, differentiating `||.||^p` yields

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 =int_0^infinity [
   p r_s^(p-2)||A^(1/2)y_s||^2
  +p(p-2)r_s^(p-4)<z_s,A^(1/2)y_s>^2] ds`.

There are two elementary bounds on the square:

`<z_s,A^(1/2)y_s>^2
 <= r_s^2 ||A^(1/2)y_s||^2`,

and, by self-adjointness,

`<z_s,A^(1/2)y_s>^2
 =<A^(1/2)z_s,y_s>^2
 <=||A^(1/2)z_s||^2||y_s||^2`.

Using the convex combination with weights `1/p` and `(p-1)/p`,

`<z_s,A^(1/2)y_s>^2
 <=(1/p)r_s^2||A^(1/2)y_s||^2
   +(p-1)/p ||A^(1/2)z_s||^2||y_s||^2`.

Equivalently, after collecting coefficients, the Hessian integrand is at most

`(p-1)(-d/ds)[r_s^(p-2)||y_s||^2]`.

Indeed

`-d/ds[r_s^(p-2)||y_s||^2]
 =(p-2)r_s^(p-4)||A^(1/2)z_s||^2||y_s||^2
  +2r_s^(p-2)||A^(1/2)y_s||^2`.

Integration from `0` to `infinity` therefore gives the sharp contraction

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`.                         (2.1)

Since `Psi_p` is convex, its Hessian is positive semidefinite, and Hessian Cauchy--Schwarz plus (2.1) gives

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.                            (2.2)

### 2.2 Stopped Ito inequality and exact norm

Apply Ito's formula to finite-dimensional spectral truncations and stop before the usual norm/localization cutoffs. For

`delta=(3-p)/2`,

using `D Psi_p[-AZ]=-||Z||^p`, (2.1), and (2.2), the drift is bounded by

`-delta ||Z||^p
 +(p-1)||Z||^(p-1)||Y||
 +(p-1)/2 ||Z||^(p-2)||Y||^2`.

After expectation, deletion of the nonnegative terminal Bellman term, and passage through the standard spectral/localization limit,

`delta I
 <=(p-1)I^((p-1)/p)J^(1/p)
   +(p-1)/2 I^((p-2)/p)J^(2/p)`,                     (2.3)

where

`I=E int_0^T ||Z||^p dt`, `J=E int_0^T ||Y||^p dt`.

For `R=(I/J)^(1/p)`, (2.3) is

`delta R^2 <=(p-1)R+(p-1)/2`.

The positive root is

`R_p^*
 =[(p-1)+sqrt(2(p-1))]/(3-p)
 =1/(sqrt(2/(p-1))-1)`.                               (2.4)

Thus `C_p^g(T)<=R_p^*` for every `2<=p<3`.

For sharpness, use one exact Fourier shell. After a finite-cost seed, impose progressive proportional feedback

`Y=gamma Z`,

`gamma=sqrt(2/(p-1))-1`.

After shell time scaling the equation is

`dZ=-Z dt+(1+gamma)Z dW`.

Its `p`-moment exponent equals

`-p + p(p-1)(1+gamma)^2/2 =0`.

On a long scaled interval the seed cost is negligible, while the output/input ratio tends to `1/gamma=R_p^*`. High-frequency shell scaling places arbitrarily long scaled intervals inside every fixed physical horizon. Hence

`boxed{ C_p^g(T)=1/(sqrt(2/(p-1))-1), 2<=p<3 }`,

and `(3-p)C_p^g(T)->4`.

### 2.3 Positive critical endpoint: `alpha<=1`

Let `F=||T_TY||_2`, `0<s<T`, and `ell=log(T/s)`. Rearrangement and the finite-measure embedding `L^3 -> L^p` give

`F^*(s)
 <=R_p^* s^(-1/p)T^(1/p-1/3)||Y||_3`.

For `ell>=3`, choose `p=3-3/ell`. Then `R_p^*<=4ell/3`, while

`(T/s)^(1/p-1/3)=exp(ell(1/p-1/3))`

is bounded by an absolute constant. The bounded-`ell` region is controlled by the exact `p=2` estimate. Therefore

`||T_TY||_{Z_{3,1}(T)} <= C ||Y||_3`,

and in the predecessor normalization one may take `C=1+sqrt(2)`. Thus `alpha_*(T)<=1`.

### 2.4 Negative side: every `alpha<2/3` fails

On one shell, after an OU seed, take near-critical positive feedback `Y=gamma Z`. Put

`sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`.

Then on the feedback interval

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`.

Choose

`L_gamma=log(1/gamma)/(2gamma)`,
`kappa=2d/sigma^2`,
`t_*=L_gamma-2sqrt(L_gamma)`,
`x=dt_*`.

The Gaussian large-deviation exponent has the exact saddle identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`.                           (2.5)

Hence a Mills lower bound on a `sqrt(L_gamma)` window around `t_*` gives

`int_0^{L_gamma} P(|Z_{1+t}|>e^x) dt
 >= c e^(-kappa x)`

up to the retained seed normalization. The algebraic identities

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`                       (2.6)

then yield

`||Z||_{Z_{3,alpha}}/||Y||_3
 >=c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

For every `alpha<2/3` this diverges as `gamma downarrow 0`. Exact shell scaling again transfers the witness to every fixed physical horizon. Thus `alpha_*(T)>=2/3`.

Combining the two sides gives the retained full frozen-pair bracket

`boxed{ 2/3 <= alpha_*(T) <=1 }`.

The previously proved additive-shell saddle also implies that if the full `alpha=2/3` endpoint holds, its operator constant is at least `4/9`; that number is unchanged here.

---

## 3. Relevant predecessor ingredients for the new attack

The preceding packet-rigidity runs supply two facts used here.

First, dyadic spectral blocks are

`Q_j = 1_[2^j,2^(j+1))(A)`, `j>=0`,

and a three-block packet is

`P_j=Q_{j-1}+Q_j+Q_{j+1}`

(with empty negative-index blocks). Three adjacent blocks have spectral condition ratio at most `8`.

Second, on any spectral band with condition ratio `K`, the predecessor radial calculation gives for `5/2<=p<3`, `delta=(3-p)/2`, after scaling the lower spectral edge to one,

`L_Y r^p
 <=-(p delta/2)r^p
   +136p K^(p/2)delta^(-(p-1))u^p`.                    (3.1)

For a dyadic block `Q_h`, physical time scaling introduces its base frequency `2^h`. Thus, for any stopped block solution `U=Q_h Z`, `V=Q_hY`,

`E_tau ||U_sigma||^p
 <=||U_tau||^p
   +136p 2^(p/2) delta^(-(p-1)) 2^h
      E_tau int_tau^sigma ||V_t||^p dt`.                (3.2)

This `2^h` is essential. It is exactly why the correct migration count below is inverse-frequency weighted.

For three-block packets, the predecessor logarithmic generator estimate in physical time is

`drift(log ||P_jZ||)
 <= lambda_0[-1/4+4*8^(3/2)(||P_jY||/||P_jZ||)^3]`,     (3.3)

where `lambda_0` is the lower spectral edge of the packet.

---

## 4. New deterministic lemma: hysteresis localizes a center change to four boundary blocks

Fix

`eta=1/4`, `epsilon=2^-12=1/4096`.

For nonzero `z`, define the packet mass fraction

`m_j(z)=||P_jz||^2/||z||^2`.

A hysteretic packet rule retains the current center `j` while

`m_j(z)>1-eta`.

When it reaches `1-eta`, switch only if a replacement packet `P_k` satisfies

`m_k(z)>=1-epsilon`.

### Lemma 4.1 — local geometry of a switch

At such a switch:

1. `|k-j|<=2`;
2. the new-only part `P_k\P_j` carries at least `eta-epsilon` of the squared state mass;
3. therefore one of the four boundary blocks

`B(j)={j-3,j-2,j+2,j+3}`

(with negative indices omitted) carries at least `(eta-epsilon)/2` of the squared state mass.

**Proof.** If `|k-j|>=3`, the three-block packets are disjoint. But then

`m_j+m_k >= (1-eta)+(1-epsilon)>1`,

impossible. Hence `|k-j|<=2`.

Write `I=P_j cap P_k`, `O=P_j\P_k`, `N=P_k\P_j`. Then

`m_k-m_j = mass(N)-mass(O)`.

Since `mass(O)>=0`,

`mass(N)>=m_k-m_j >=eta-epsilon`.

For `|k-j|<=2`, `N` contains at most two dyadic blocks, all belonging to `B(j)`. One of them therefore carries at least half the new-only mass. QED.

Now restrict attention to an annulus

`R<=||Z_t||<=2R`.

At the beginning of an attempt with packet `P_j` satisfying `m_j>=1-epsilon`, every boundary block in `B(j)` has norm at most

`aR`, `a=2sqrt(epsilon)=1/32`.

At a switch, Lemma 4.1 says that some boundary block has norm at least

`bR`,

`b=sqrt((eta-epsilon)/2)=0.353380714934...`.

Thus the required growth ratio is

`theta=a/b=0.088431537657...`.                          (4.1)

This converts a packet-center change into a stopped hitting event for one of only four adjacent dyadic blocks.

---

## 5. New theorem: frequency-weighted packet-switch Carleson estimate

Define the center clock

`w_j=2^(-j)`.

Consider any finite or countable adapted family of disjoint annular attempts satisfying:

- during an attempt the state remains in `R<=||Z||<=2R`;
- a current packet `P_j` is retained while `m_j>1-eta`;
- a center change obeys the hysteretic rule above;
- every center change starts the next attempt; other attempt starts are called **exogenous** (a true restart, radial re-entry, or recovery from a delocalized interval).

Let

`M_w=sum_{exogenous starts} w_j`,

and

`N_w=sum_{switches j->k} w_j`,

where a switch is weighted by its old center.

### Theorem 5.1 — weighted switch estimate

For every `5/2<=p<3`, `delta=(3-p)/2`,

`boxed{
 E N_w
 <=0.009662 E M_w
   +217294 delta^(-(p-1)) R^(-p)
       E int_0^T ||Y_t||^p dt.
}`                                                               (5.1)

If

`J=E int_0^T ||Y_t||^3 dt`,
`rho=TR^3/J >= e^12`,

and `p=3-6/log rho`, then

`boxed{
 E N_w
 <=0.009662 E M_w
   +178399 (J/R^3)(log rho)^2.
}`                                                               (5.2)

In particular, with zero input, passive packet-center changes contribute less than one percent of the exogenous inverse-frequency seed clock.

### Proof

Fix one attempt with current center `j` and start time `tau`. For `h in B(j)`, stop the projected dyadic-block equation at the first time its norm reaches `bR`, or at the end of the attempt. From (3.2), on the hitting event,

`(bR)^p P_tau(hit_h)
 <=(aR)^p
   +136p 2^(p/2)delta^(-(p-1))2^h
      E_tau int_attempt ||Q_hY||^p dt`.

Therefore

`P_tau(hit_h)
 <=theta^p
  +C_p delta^(-(p-1))2^h R^(-p)
      E_tau int_attempt ||Q_hY||^p dt`,

where

`C_p=136p 2^(p/2)b^(-p)`.

For `5/2<=p<3`, direct monotonicity/numerical verification of the elementary scalar expression gives

`C_p<26151`.                                                (5.3)

If the packet switches, one of the four boundary blocks hits `bR`. Hence, by the union bound,

`P_tau(switch)
 <=q
  +26151 delta^(-(p-1))R^(-p)
      E_tau int_attempt sum_{h in B(j)}2^h||Q_hY||^p dt`,

where, since `p>=5/2`,

`q=4 theta^p <=4theta^(5/2)
  =0.009302034221...`.                                     (5.4)

Multiply by `w_j=2^(-j)`. Every candidate satisfies `h-j<=3`, so

`w_j 2^h <=8`.                                             (5.5)

Moreover the candidate blocks are orthogonal and `p>=2`, hence pointwise

`sum_{h in B(j)}||Q_hY||^p
 <=(sum_{h in B(j)}||Q_hY||^2)^(p/2)
 <=||Y||^p`.                                               (5.6)

Summing conditional estimates over the disjoint attempt intervals gives

`E N_w
 <=q E A_w
   +8*26151 delta^(-(p-1))R^(-p)J_p`,                    (5.7)

where `A_w` is the sum of the weights of all attempt starts and `J_p=E int||Y||^p`.

Every non-exogenous attempt is created by a preceding switch. Since `|k-j|<=2`,

`w_k/w_j=2^(j-k)<=4`.

Therefore

`A_w <= M_w+4N_w`.                                        (5.8)

Insert (5.8) into (5.7). Because

`1-4q=0.962791863112...>0`,

we obtain

`E N_w
 <= q/(1-4q) E M_w
  +[8*26151/(1-4q)]delta^(-(p-1))R^(-p)J_p`.

The two scalar constants are

`q/(1-4q)=0.009661521433...<0.009662`,

`8*26151/(1-4q)=217293.070304...<217294`,

which proves (5.1).

For (5.2), finite-measure embedding gives

`J_p <=T^(1-p/3)J^(p/3)`.

Thus

`R^(-p)J_p
 <=(J/R^3) rho^(1-p/3)`.                       (5.9)

When `rho>=e^12`, put `ell=log rho` and

`delta=3/ell`, `p=3-6/ell`.

Then `p>=5/2`,

`rho^(1-p/3)=e^2`,

and, since `delta<1`,

`delta^(-(p-1)) <=delta^(-2)=(ell/3)^2`.

The active constant is therefore at most

`217293.070304... * e^2/9
 =178398.965154...<178399`,

which proves (5.2). QED.

### Bounded-`rho` branch

For completeness, if `rho<e^12`, take `p=5/2`, `delta=1/4`. Then `rho^(1-p/3)=rho^(1/6)<e^2`, and the same argument gives a finite absolute active coefficient below `12,844,726`. Hence the mechanism has the same `(1+log_+rho)^2` critical shape globally, although only the large-`rho` constant matters for the endpoint obstruction.

---

## 6. Localized annular occupation: center changes no longer proliferate seed time

The weighted switch count is useful because `w_j` is exactly the parabolic time scale of a three-block packet.

Let an attempt with center `j` run until its switch or another exogenous stopping event, and assume throughout the attempt

`R<=||Z||<=2R`, `m_j(Z)>=1-eta`.

Set

`U=P_jZ`, `V=P_jY`, `c=sqrt(1-eta)=sqrt(3/4)`.

Then

`||U||>=cR`,

while at the attempt start `||U||<=2R`.

The packet `P_j` has condition ratio at most `8`. Its lower spectral edge `lambda_0` satisfies

`1/lambda_0 <=2w_j`.                                      (6.1)

Apply the predecessor log-drift estimate (3.3), localize the logarithm away from zero, and stop at the attempt end. Since the terminal packet norm is still at least `cR`, expectation gives

`E duration_j
 <=4 lambda_0^(-1) log(2/c)
   +16*8^(3/2)c^(-3)R^(-3)
      E int_attempt ||P_jY||^3 dt`.

Using (6.1),

`E duration_j
 <=6.695905735 w_j
   +557.395000 R^(-3)
      E int_attempt ||P_jY||^3 dt`.                       (6.2)

Sum (6.2) over disjoint attempts. The projection input terms sum to at most `J`, while `A_w<=M_w+4N_w`. Therefore, for `rho>=e^12`, Theorem 5.1 gives

`boxed{
 E[total localized annular duration]
 <=6.955 E M_w
   +4,778,729 (J/R^3)(log rho)^2.
}`                                                               (6.3)

Indeed the checked constants are

`6.695905734*(1+4*0.009661522)=6.954676282<6.955`,

and

`6.695905734*4*178398.965155+557.395
 =4,778,728.0101<4,778,729`.

Equation (6.3) is the main application of the switch theorem. Once a localized annular attempt has started, **arbitrarily many adaptive packet labels cannot create an uncontrolled duration loss**. Passive switching is a strict contraction in the correct inverse-frequency clock, while active switching costs the same cubic `log^2` budget required by the conjectured `alpha=2/3` endpoint.

---

## 7. What changed, and what did not

### Fixed source theorem: unchanged

The parent endpoint is still

`r_*=3`, strong `p=3` excluded,

with

`2/3 <= alpha_*(T) <=1`.

No claim here closes arbitrary-pair Agresti--Veraar Problem 3, and no more restrictive packet assumption is relabeled as the source theorem.

### Demonstrated mechanism gain

The preceding run removed packet-label entropy **after a true restart**. The present theorem removes the next obstruction: packet labels may now change repeatedly **while a localized annular excursion remains alive**, and those changes still satisfy a critical Carleson estimate once counted in the natural parabolic clock `2^{-j}`.

The correction from an unweighted to a weighted count is not cosmetic. A dyadic block at scale `2^h` evolves on physical time `2^{-h}`; the stopped block-hitting inequality necessarily carries `2^h`. Multiplication by the old-center clock `2^{-j}` cancels this factor for the only blocks capable of a hysteretic local switch (`|h-j|<=3`). This is exactly the scale covariance the endpoint argument needs.

The theorem also matches the predecessor passive Hellinger result conceptually: widely separated unequal scales lose cubic coherence after forcing stops, while the present local theorem shows that even repeated adjacent-scale center changes cannot proliferate the inverse-frequency seed clock unless the active input pays a critical cubic cost.

---

## 8. Residual obstruction and next decisive calculation

The remaining quantity in (6.3) is the **exogenous weighted start clock**

`M_w=sum 2^(-j_start)`.

Its starts are generated by three mechanisms:

1. a genuine downcrossing/restart;
2. a radial overshoot followed by re-entry into the annulus;
3. a delocalized interval on which no three-block packet captures `1-epsilon` of the state, followed by recovery of localization.

The first mechanism is compatible with the predecessor exact countable branch gluing. The second and third are the actual unresolved bridge.

Crucially, the inverse-frequency weight in `M_w` matches the semigroup Bellman trace: for a state supported in a packet near frequency `2^j`,

`Psi_p(z) = int_0^infinity ||e^{-sA}z||^p ds`

is comparable to `2^{-j}||z||^p`. Thus the next attack is no longer an unstructured packet-count problem. It is to prove a stopping-time trace/dwell inequality charging exogenous starts to

- the exact Bellman spectral-variance defect when localization fails;
- the full joint Bellman slack when forcing creates a new packet;
- the passive Hellinger kernel across separated scales.

If one proves

`E M_w <= C (J/R^3)(1+log_+(TR^3/J))^2`

at the relevant high levels, then (6.3), followed by the predecessor exact branch gluing, gives precisely the missing critical layer estimate at logarithmic exponent `2/3`.

So the residual obstruction is now a single frequency-weighted start-charge inequality, not packet-label entropy and not localized within-excursion migration.

No T05 fallback is triggered: this run produced a strict new theorem-level mechanism gain on the exact frozen P24 pair.

---

## 9. Essential checker and correction of the physical scale

The executed checker files are

`2026-09-20T19-50-46+0300__hysteretic_packet_carleson_checker.py`

and

`2026-09-20T19-50-46+0300__hysteretic_packet_carleson_checker.out`.

The checker verifies:

- `theta=0.088431537657...`;
- the passive union factor `q=0.009302034221...`;
- the absorption denominator `1-4q=0.962791863112...`;
- the maximal dyadic physical-scale ratio `2^(h-j)=8` for candidate switch blocks;
- the next-center weight ratio `w_k/w_j<=4`;
- the uniform stopped-hitting scalar coefficient `<26151`;
- the weighted large-`rho` critical coefficient `178398.965154...<178399`;
- the packet seed-duration constant `6.695905734...<6.696`;
- the cubic packet-duration coefficient `557.394999...`;
- the final duration coefficient `4,778,728.010...<4,778,729`;
- 20,000 randomized instances of the deterministic hysteretic packet geometry;
- 5,000 randomized checks of the scaling identity

  `R^(-p)T^(1-p/3)J^(p/3)
   =(J/R^3)(TR^3/J)^(1-p/3)`.

The archived output ends

`CHECK_PASS`.

The important soundness correction in this run was precisely the factor `2^h` in (3.2). The initial unweighted draft was discarded before the substantive report was created; the final checker, ledger, and theorem all use the corrected inverse-frequency weighting.

---

## 10. Bounded current literature check

The source survey still states Problem 3 as the nonsmall-`B` extrapolation question. A bounded current search did not find a paper resolving this exact frozen critical successor.

Relevant later work remains distinct:

- Evangelopoulos-Ntemiris--Veraar, *Discrete stochastic maximal regularity*, published 13 February 2026, treats temporal numerical schemes and discrete extrapolation;
- Lorist--van Neerven--Veraar, arXiv:2608.20266 (20 August 2026), studies necessary Banach-space geometry for stochastic maximal regularity;
- Agresti--Veraar's 2026 Comptes Rendus note concerns temporal regularity for an additive linear SPDE, not this nonsmall state-multiplicative critical endpoint.

This is a bounded dated literature check, not a worldwide novelty certificate.

`POSTED.md` / current owner policy exclusions for the already-written Agresti--Veraar Problems 4--5 package were respected.

---

## 11. Compact ledger delta

- **Before:** `r_*=3`, endpoint excluded; exact `C_p^g`; full critical bracket `[2/3,1]`; conditional `alpha=2/3` lower constant `4/9`; exact countable restart gluing available, but within-excursion center migration still uncharged.
- **After:** source quantities unchanged. New candidate theorem: frequency-weighted hysteretic center switches satisfy (5.1)--(5.2), and localized annular duration satisfies (6.3).
- **Strict gain:** adaptive center changes inside a localized high-level excursion no longer create packet-count entropy or an uncontrolled seed-time sum in the natural parabolic clock.
- **Residual:** control exogenous inverse-frequency start clock `M_w` at delocalization/radial restart times using Bellman trace + state/joint slack + passive Hellinger.
- **Status:** new mechanism `CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW`; parent endpoint `PARTIAL / OPEN`.
- **Runtime:** GPT-5.6 Sol; effort metadata UNVERIFIED.
