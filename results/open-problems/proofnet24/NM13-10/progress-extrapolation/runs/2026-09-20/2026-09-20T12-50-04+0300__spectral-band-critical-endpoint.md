Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-10 progress-extrapolation — critical log-2/3 endpoint on arbitrary comparable spectral bands

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run stays on P24's exact already-frozen semigroup pair, preserves the productive NM13-10 successor chain, does not reopen Problems 4–5, and spends the substantive work on a new proof mechanism rather than an audit loop.

New theorem status: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**. The parent full-spectrum critical endpoint remains **PARTIAL**.

## 0. Short handoff and fixed quantities before/after

The historical NM13-10 admission state remains preserved as `ADMISSION_PENDING`, `UNMEASURED -> UNMEASURED`; PROGRESS20 redirected the slot to P24's productive extrapolation successor and that old baseline is not reset.

The exact frozen P24 realization remains

- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` with `beta=1`;
- one real Brownian driver;
- transformed stochastic-input equation
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`;
- stochastic input/output measured in `L^p(Omega x (0,T);L^2(Torus))`.

Retained productive predecessor results:

1. P24 proved the exact strong fixed-pair endpoint `r_*=3`, endpoint excluded. For the commuting beta-family, `r_*(beta)=1+2/beta^2`.
2. NM13-10 sharpened the full frozen-pair stochastic-input norm to
   `C_p^g(T)=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)C_p^g(T)->4`.
3. NM13-10 proved the critical spacetime rearrangement bracket
   `2/3 <= alpha_*(T) <= 1` for
   `||F||_{Z_{3,alpha}(T)}=sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`.
4. The exact additive saddle witness gives the conditional lower constant `4/9` at `alpha=2/3` if the full endpoint is bounded.
5. The preceding covariance run proved passive cross-scale cubic decoherence after forcing stops; the immediately preceding excursion run proved the exact `alpha=2/3` endpoint uniformly on every single eigenspace for arbitrary progressive forcing inside that eigenspace.

**Fixed strong source endpoint before:** `r_*=3`, endpoint excluded.  
**Fixed strong source endpoint after:** `r_*=3`, endpoint excluded.

**Full-spectrum critical bracket before:** `[2/3,1]`.  
**Full-spectrum critical bracket after:** `[2/3,1]`.

**Conditional full-pair endpoint lower constant before/after:** `4/9 -> 4/9`.

Thus there is deliberately no false source-level closure. The new gain is that the one-eigenspace excursion theorem extends to **all simultaneously active unequal Fourier modes whose eigenvalues lie in one fixed spectral band**, with a constant depending only on the band's condition ratio and not on its location or dimension.

---

## 1. Recovered proof behind the current full-pair bracket

This run again records the proof dependencies rather than treating `[2/3,1]` as unexplained history.

For `p>=2`, define on the transformed Hilbert coordinate

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

The exact `1/p` weighted Hessian contraction established earlier is

`D Psi_p(z)[-Az]=-||z||^p`,

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y] <= (p-1)||z||^(p-2)||y||^2`,

and positive-semidefinite Hessian Cauchy–Schwarz gives

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]| <= (p-1)||z||^(p-1)||y||`.

For the stopped finite-dimensional equation, put

`I=E int ||Z||^p`, `J=E int ||Y||^p`, `delta=(3-p)/2`.

Ito's formula gives

`delta I <= (p-1) I^((p-1)/p)J^(1/p)
          +(p-1)/2 I^((p-2)/p)J^(2/p)`.

If `R=(I/J)^(1/p)`, then

`delta R^2 <= (p-1)R+(p-1)/2`.

The positive root simplifies exactly to

`R_p=1/(sqrt(2/(p-1))-1)`.

The source-valid one-shell neutral-feedback construction supplies the reverse inequality, hence

`C_p^g(T)=R_p`, `2<=p<3`, every `T>0`,

and `(3-p)R_p->4`.

For the positive critical rearrangement estimate let `F=||T_TY||`, `L=log(T/s)`. Rearrangement plus finite-measure embedding gives

`F^*(s) <= R_p s^(-1/p)T^(1/p-1/3)||Y||_3`.

For `0<=L<=3`, take `p=2`; since `R_2=1+sqrt(2)` and `e^(L/6)/(1+L)<=1`, this yields

`s^(1/3)F^*(s)/(1+L) <= (1+sqrt(2))||Y||_3`.

For `L>=3`, take `p=3-3/L`. Rationalization gives `R_p<=4L/3`, while

`(T/s)^(1/p-1/3)=exp(1/p)<=sqrt(e)`.

Thus

`s^(1/3)F^*(s)/(1+L) <= (4sqrt(e)/3)||Y||_3 <(1+sqrt(2))||Y||_3`.

Therefore

`||T_TY||_{Z_{3,1}(T)} <=(1+sqrt(2))||Y||_3`,

so `alpha_*(T)<=1`.

For the lower side, use the retained source-valid one-shell seed and near-critical feedback. After a finite-cost seed produces a positive state, set on a long interval

`Y=gamma Z`, `sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`,

so

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`.

Choose

`L_gamma=log(1/gamma)/(2gamma)`.

The cubic input cost is of order `gamma^(-1/3+o(1))` in norm. Put

`kappa=2d/sigma^2`, `t_*=L_gamma-2sqrt(L_gamma)`, `x=d t_*`.

The exact Gaussian identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`

and a Mills lower bound on a `sqrt(L_gamma)` saddle window yield a spacetime tail at least `c exp(-kappa x)`. The exact algebra

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

then gives

`||Z||_{Z_{3,alpha}}/||Y||_3
 >= c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`. Exact Fourier-shell scaling transfers the construction to every fixed physical horizon `T>0`. Hence `alpha_*(T)>=2/3` and the recovered full-pair bracket is exactly

`2/3 <= alpha_*(T) <=1`.

Nothing in the new theorem below changes that parent baseline.

---

## 2. New theorem: arbitrary progressive forcing in a comparable spectral band

Let `E` be an `A`-invariant finite-dimensional spectral subspace such that for some `lambda_0>0` and `K>=1`,

`lambda_0 I <= A|_E <= K lambda_0 I`.

Assume `Y` is an arbitrary progressive `E`-valued input. Then `Z` remains in `E`.

Scale time by `s=lambda_0 t` and Brownian motion by `B_s=sqrt(lambda_0)W_{s/lambda_0}`. The equation becomes

`dZ=-AZ ds+A^(1/2)(Z+Y)dB`,

where, after renaming the scaled operator,

`I <= A <= K I`.                                           (2.1)

If

`J=E int_0^T ||Y||^3 dt`,

`m_R=(P x dt){||Z||>R}`,

then both `J` and `m_R` acquire the same factor `lambda_0` under this scaling. Thus the final tail estimate below is invariant under the physical spectral location of the band.

> **Theorem NM10-AVP3-BAND-12.** Under (2.1), for every progressive `Y in L^3(Omega x (0,T);E)`,
>
> `m_R <=1243 K^(3/2) J R^(-3)
>          [1+log_+(T R^3/(K^(3/2)J))]^2`                 (2.2)
>
> for every `R>0` (with the right side interpreted as zero if `J=0`). Consequently
>
> `||T_TY||_{Z_{3,2/3}(T)} <=65 sqrt(K)||Y||_3`.          (2.3)
>
> The constants are independent of the location and dimension of the band.

For the torus, taking the dyadic spectral block

`E_j=1_[2^j,2^(j+1))(Lambda)L^2(Torus)`

gives `K<=2` and therefore the uniform block bound

`||T_T Y||_{Z_{3,2/3}(T)} <=65 sqrt(2)||Y||_3
                           <91.924||Y||_3`                (2.4)

for every progressive input supported in that block. Since the prior high-frequency one-shell counterexamples lie inside such blocks and rule out every exponent `<2/3` uniformly over block location, the **uniform dyadic-block family** has exact critical exponent `2/3`.

This is a restricted exact-pair theorem, not the full source theorem.

---

## 3. Subcritical stopped moment estimate with only `K^(p/2)` loss

Fix `2<=p<3` and

`delta=(3-p)/2`.

Write `r=||Z||`, `u=||Y||`, and on `r>0` set

`e=Z/r`, `eta=Y/r`,

`q=<Ae,e>`,

`c=<e,A^(1/2)e>`,

`s=<Ae,eta>`,

`h=<e,A^(1/2)eta>`,

`v=<A eta,eta>`.

Then `q>=1`, `v<=K(u/r)^2`, `c^2<=q`, and

`|s|<=sqrt(qv)`, `|h|<=sqrt(v)`, `c<=sqrt(q)`.

For `f(z)=||z||^p`, direct differentiation gives

`L_Y r^p/(p r^p)
 =-q/2 +(p-2)c^2/2
   +s +(p-2)ch
   +v/2 +(p-2)h^2/2`.                                    (3.1)

The passive part satisfies

`-q/2 +(p-2)c^2/2
 =-[q-(p-2)c^2]/2
 <=-(3-p)q/2
 =-delta q`.                                              (3.2)

The input terms satisfy

`s +(p-2)ch +v/2 +(p-2)h^2/2
 <=2sqrt(qv)+v`.                                          (3.3)

Put `w=sqrt(v/q)`. Then (3.3) is at most

`q(2w+w^2)`.

The elementary estimate retained from the one-shell run is

`2w+w^2 <=delta/2+136 delta^(-(p-1))w^p`.                (3.4)

Combining (3.1)–(3.4),

`L_Y r^p/(p r^p)
 <=-delta q/2
   +136 delta^(-(p-1)) q^(1-p/2)v^(p/2)`.

Because `q>=1`, `p>=2`, and `v<=K(u/r)^2`,

`q^(1-p/2)v^(p/2) <=K^(p/2)(u/r)^p`.

Hence

`L_Y r^p
 <=-(p delta/2)r^p
   +136p K^(p/2)delta^(-(p-1))u^p`.                       (3.5)

After the standard smooth regularization at `r=0`, stopped Ito and localization yield, for every bounded stopping time `tau`,

`E r_tau^p +(p delta/2)E int_0^tau r^p dt
 <=r_0^p
   +136p K^(p/2)delta^(-(p-1))E int_0^tau u^p dt`.        (3.6)

Therefore an attempt starting at zero and stopped on first hitting `R` satisfies

`P(hit R)
 <=136p K^(p/2)delta^(-(p-1))R^(-p)J_p`,                (3.7)

where `J_p=E int u^p` on that attempt interval.

The key improvement relative to a naive band estimate is the square-root condition loss `K^(p/2)`, not `K^p`. It comes from measuring the input through the Rayleigh quotient `v/q` before applying Young's inequality.

---

## 4. Critical log-radius drift with `K^(3/2)` cubic cost

For `g(z)=log||z||`, Ito's formula gives the drift

`b=-q/2+s+v/2-(c+h)^2`.                                  (4.1)

Dropping the last nonpositive term and using `|s|<=sqrt(qv)`,

`b <=-q/2+sqrt(qv)+v/2`.                                 (4.2)

Put `a=sqrt(v)` and `rho=sqrt(q)>=1`. The right side of (4.2) is

`-rho^2/2+rho a+a^2/2`.

For fixed `a`, maximizing over `rho>=1` gives

- if `0<=a<=1`, `-1/2+a+a^2/2`;
- if `a>=1`, `a^2`.

Both are bounded by

`-1/4+4a^3`.                                              (4.3)

For the first regime, the only nontrivial scalar inequality is

`(-1/4+a+a^2/2)/a^3 <=4`.

The ratio has derivative

`-(2a^2+8a-3)/(4a^4)`

and its positive critical point is

`a_0=(sqrt(22)-4)/2`.

At that point the ratio is exactly

`50/27+11sqrt(22)/27=3.762761976...<4`.

For `a>=1`, `a^2<=-1/4+4a^3` is immediate. Thus

`b <=-1/4+4v^(3/2)
   <=-1/4+4K^(3/2)(u/r)^3`.                              (4.4)

Consider a high-level excursion beginning when `r=R` and ending at the first downcrossing of `R/2` or at the terminal horizon. Throughout the excursion `r>=R/2`, so

`b <=-1/4+32K^(3/2)u^3/R^3`.                            (4.5)

If `D` is its duration, then the terminal radius is at least `R/2`; hence

`log(r_end/R)>=-log2`.

Localizing the log martingale and taking expectations in (4.5) gives

`E D <=4log2
       +128K^(3/2)R^(-3)E int_exc u^3 dt`.               (4.6)

This is the critical charging step: band width appears only as `K^(3/2)` in the cubic energy term.

---

## 5. Count high excursions subcritically, charge their lifetime critically

Define alternating attempts and excursions exactly as in the one-shell proof:

- `tau_1` is the first hit of radius `R`;
- after `tau_k`, `sigma_k` is the first downcrossing of `R/2` (or horizon);
- after `sigma_k<T`, `tau_{k+1}` is the next hit of `R`.

Let `N` be the number of actual hits of `R` before `T`.

For every later attempt the starting radius is `R/2`. Applying (3.6) conditionally to each attempt gives

`P(tau_{k+1}<=T)
 <=2^(-p)P(tau_k<=T)
  +136p K^(p/2)delta^(-(p-1))R^(-p)
     E int_attempt_k u^p dt`.

The attempt intervals are disjoint, so summing the geometric recursion yields

`E N
 <=[136p/(1-2^(-p))]
    K^(p/2)delta^(-(p-1))R^(-p)J_p`.                    (5.1)

Every time with `r>=R` belongs to one of the excursion intervals. Summing (4.6) over excursions and using disjointness therefore gives

`m_R
 <=[544p log2/(1-2^(-p))]
     K^(p/2)delta^(-(p-1))R^(-p)J_p
   +128K^(3/2)R^(-3)J`.                                 (5.2)

For `2<=p<3`,

`544p log2/(1-2^(-p))
 <=2176log2
 =1508.288...<1509`.                                    (5.3)

Hence

`m_R
 <=1509 K^(p/2)delta^(-(p-1))R^(-p)J_p
   +128K^(3/2)R^(-3)J`.                                 (5.4)

---

## 6. Endpoint optimization and proof of the tail theorem

Finite measure embedding gives

`J_p <=T^(1-p/3)J^(p/3)`.

Set

`rho=T R^3/J`,

`eta=rho/K^(3/2)=T R^3/(K^(3/2)J)`.

Because `p=3-2delta`,

`1-p/3=2delta/3`, and exactly

`K^(p/2)rho^(1-p/3)
 =K^(3/2)eta^(2delta/3)`.                                (6.1)

Thus (5.4) becomes

`m_R
 <=K^(3/2)J R^(-3)
   [1509 delta^(-(p-1))eta^(2delta/3)+128]`.             (6.2)

If `eta>e^6`, let `L=log eta>6` and choose

`delta=3/L`, `p=3-6/L`.

Then

`eta^(2delta/3)=e^2`,

and since `delta<1`, `p-1<2`,

`delta^(-(p-1))<=delta^(-2)=(L/3)^2`.

Therefore

`m_R
 <=K^(3/2)J R^(-3)
   [1509 e^2 L^2/9+128]`.

Since `L>6`, `128<=128L^2/36`, and

`1509e^2/9+128/36
 =1242.453961...<1243`,

we obtain

`m_R <=1243 K^(3/2)J R^(-3)L^2`.                        (6.3)

If `eta<=e^6`, use the trivial bound `m_R<=T`. Since

`T=(K^(3/2)J/R^3)eta`

and `e^6=403.428...<1243`, the same unified estimate follows:

`m_R <=1243 K^(3/2)J R^(-3)
        [1+log_+ eta]^2`.                                (6.4)

This is (2.2).

---

## 7. Rearrangement endpoint

Let `0<s<T` and write

`L_s=1+log(T/s)`.

Choose

`R_s=65 sqrt(K) J^(1/3)s^(-1/3)L_s^(2/3)`.              (7.1)

Then

`T R_s^3/(K^(3/2)J)
 =65^3 (T/s)L_s^2`.                                      (7.2)

Applying (6.4),

`m_{R_s}/s
 <=1243/65^3
   *[(1+log(65^3(T/s)L_s^2))/L_s]^2`.

If `x=log(T/s)`, then `L_s=1+x` and the bracket equals

`[L_s+3log65+2log L_s]/L_s`.

Because `log L/L<=1/e` for `L>=1`,

`m_{R_s}/s
 <=1243/65^3 [1+3log65+2/e]^2
 =0.920246905...<1`.                                     (7.3)

Hence the decreasing rearrangement satisfies `F^*(s)<=R_s`, and therefore

`||T_TY||_{Z_{3,2/3}(T)} <=65 sqrt(K)||Y||_3`.

This proves (2.3).

The argument is stable under the source's stopping-time localization: apply it conditionally after the stopping time to the stopped input and zero-extend on the remaining horizon. The constants use only the spectral ratio and the remaining interval length.

---

## 8. What the new theorem changes in the full problem

The parent full-spectrum endpoint remains open, but its obstruction is now narrower.

Before this run, arbitrary progressive forcing was controlled at exponent `2/3` only on one exact eigenspace. It was still possible that even a cluster of nearby unequal scales created a worse active common-noise mechanism.

The theorem above excludes that possibility. For any spectral cluster with

`lambda_max/lambda_min <=K`,

all simultaneous active interactions inside the cluster satisfy the critical endpoint with constant `65sqrt(K)`, independently of how many torus shells occur in the cluster and independently of the cluster's absolute frequency. In particular every dyadic spectral block has a uniform constant below `91.924`.

Combining this with the previous passive Hellinger theorem gives the current structural picture:

- **single scale:** exact exponent `2/3`;
- **arbitrarily many comparable active scales:** exponent `2/3` by the new band theorem;
- **widely separated scales after forcing stops:** finite cubic memory by Hellinger decoherence;
- **remaining obstruction:** simultaneous active forcing across arbitrarily separated dyadic bands.

Thus the next source-exact target is no longer a generic two-shell estimate. It is a cross-dyadic **active** Carleson/energy charge that does not sum one endpoint constant per band. A successful estimate should combine the present Rayleigh-quotient excursion clock with the existing Hellinger gap kernel; a counterexample would have to continually recreate coherence across separated bands while paying cubic input energy.

No T05 fallback is triggered: this run produced a strict theorem-level mechanism gain, so the recovery-failure condition is not met.

---

## 9. Essential check actually executed

The archived checker

`2026-09-20T12-50-04+0300__spectral_band_endpoint_checker.py`

was executed before persistence. It verifies:

1. the exact maximizer of the scalar log-drift ratio and the strict bound `<4`;
2. the excursion-count coarse constant `<1509`;
3. the optimized large-`eta` coefficient `<1243`;
4. the small-`eta` trivial branch `e^6<1243`;
5. the rearrangement factor for constant `65sqrt(K)`, equal to `0.920246905...<1`;
6. a dense numerical sanity grid for the scalar majorant.

The archived output ends `CHECK_PASS`.

---

## 10. Bounded fresh literature boundary

A bounded fresh search on 20 September 2026 still finds Agresti–Veraar Problem 3 in the published survey: starting from `(A,B) in SMR_{p,0}` for some `p>=2`, the question asks for extrapolation to all `r>2` or at least a larger range when `B` is not small. The survey itself points to the variational/self-adjoint extrapolation result of Bechtel–Veraar, which yields only a small interval above `2` in that framework.

Later work found in the bounded check remains different from the exact critical claim here: Bechtel–Veraar's variational extrapolation paper was published 11 July 2025; Evangelopoulos-Ntemiris–Veraar study discrete stochastic maximal regularity and discrete extrapolation; Lorist–van Neerven–Veraar (20 August 2026) study necessary Banach-geometry conditions for stochastic maximal regularity; and Evangelopoulos-Ntemiris (7 September 2026) treats fully discrete elliptic schemes. I did not locate a published resolution of this exact frozen-pair `Z_{3,2/3}` full-spectrum endpoint. This is a bounded literature check, not a worldwide novelty certificate.

---

## 11. Ledger delta in prose

**Parent before:** strong endpoint `r_*=3` excluded; exact subcritical norm `R_p`; critical full-spectrum bracket `[2/3,1]`; conditional lower constant `4/9`.

**Parent after:** unchanged.

**New demonstrated mechanism:** for every invariant spectral band of the exact frozen `A` with condition ratio `K`, arbitrary progressive band-supported forcing obeys the tail estimate (2.2) and the critical endpoint (2.3). In particular arbitrary simultaneous active forcing across all comparable unequal torus scales in a dyadic block is controlled at exponent `2/3` with uniform constant `65sqrt(2)`.

**Residual obstruction:** active interaction across arbitrarily separated dyadic bands without paying a separate endpoint constant for each band.

**Status:** new band theorem `CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW`; parent full-spectrum endpoint `PARTIAL`.
