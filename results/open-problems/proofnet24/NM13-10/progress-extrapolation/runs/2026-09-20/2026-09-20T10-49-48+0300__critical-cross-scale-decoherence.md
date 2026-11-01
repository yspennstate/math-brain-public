Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-10 progress-extrapolation — critical cross-scale cubic decoherence on the exact frozen torus pair

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run keeps the exact P24 semigroup pair and source norm, does not reopen the posted Problems 4–5 package, and deliberately changes method from the recent Bellman/moment route to a covariance/Hellinger comparison because the parent critical bracket has remained unchanged across several substantive runs.

Status of the new theorem below: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW**. The parent critical spacetime endpoint remains **PARTIAL**.

## 0. Short handoff and exact before/after quantities

The original NM13-10 intake history remains preserved as `ADMISSION_PENDING`, `UNMEASURED -> UNMEASURED`; PROGRESS20 redirected this slot to P24's already-frozen extrapolation program.

The exact frozen pair and norms remain:

- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` (`beta=1`);
- one real Brownian driver;
- after the source-scale transform, stochastic input equation
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`, with output norm `L^p(Omega x (0,T);L^2)` and input norm of `Y` in the same product space.

The productive predecessor chain is retained exactly:

1. P24 proved the strong fixed-pair endpoint `r_*=3`, endpoint excluded.
2. NM13-10 sharpened the full stochastic-input subcritical norm to
   `C_p^g(T)=R_p=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)R_p ->4`.
3. NM13-10 established the critical spacetime rearrangement bracket
   `2/3 <= alpha_*(T) <=1` for
   `||F||_{Z_{3,alpha}(T)}=sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`.
4. The exact additive saddle witness improved the conditional endpoint norm lower bound at `alpha=2/3` to `4/9`.
5. The immediately preceding substantive report
   `2026-09-20T09-47-30+0300__critical-grand-bellman-trace.md`
   proved a full-spectrum terminal Bellman trace with critical blow-up exponent `2/3`, and on one shell obtained the separate terminal bracket `[1/2,2/3]`.

**Fixed strong source endpoint before:** `r_*=3`, endpoint excluded.

**Fixed strong source endpoint after:** `r_*=3`, endpoint excluded.

**Critical spacetime exponent bracket before:** `[2/3,1]`.

**Critical spacetime exponent bracket after:** `[2/3,1]`.

**Critical spacetime endpoint lower constant before/after:** `4/9 -> 4/9`.

Thus there is no source-level endpoint or bracket movement in this run. The new gain is a source-exact mechanism theorem: at the critical exponent `p=3`, once the input is switched off at an arbitrary stopping time, every unequal pair of Fourier shells loses common-Brownian cubic coherence at an explicit Gaussian/Hellinger rate, and the total full-spectrum off-diagonal cubic occupation has a horizon-uniform finite-memory bound.

This addresses the exact unequal-scale/common-noise obstruction rather than replacing the operator by a scalar model.

---

## 1. Recovered proof chain behind the current `[2/3,1]` bracket

The current bracket is not taken as a black box. Its essential proof chain is as follows.

For `p>=2`, define the semigroup Bellman functional

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

The exact `1/p` convex combination in the Hessian computation gives

`D Psi_p(z)[-Az] = -||z||^p`,

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`,

and Hessian Cauchy–Schwarz gives

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.

For the stopped finite-dimensional equation, Itô therefore yields, with

`I=E int ||Z||^p`, `J=E int ||Y||^p`, `delta=(3-p)/2`,

`delta I
 <=(p-1)I^((p-1)/p)J^(1/p)
   +(p-1)/2 I^((p-2)/p)J^(2/p)`.

Writing `R=(I/J)^(1/p)` gives the quadratic

`delta R^2 <=(p-1)R+(p-1)/2`.

Its positive root simplifies exactly to

`R_p=1/(sqrt(2/(p-1))-1)`.

P24's one-shell source-admissible neutral-feedback construction supplies the reverse inequality, so this is the exact full frozen-pair stochastic-input norm for every `2<=p<3`. In particular `(3-p)R_p ->4`.

For the positive critical endpoint, Chebyshev and the finite-measure embedding give, if `L=log(T/s)`,

`s^(1/3)F^*(s)
 <=R_p exp(L(1/p-1/3)) ||Y||_3`.

Using `p=2` for bounded `L` and `3-p=3/L` for large `L` gives the already-certified estimate

`||T_TY||_{Z_{3,1}(T)} <=(1+sqrt(2))||Y||_3`,

hence `alpha_*(T)<=1`.

For the lower side, the immutable report
`2026-09-20__critical-log-exponent-lower-bound-run11.md`
contains the complete source-valid construction. On one exact shell, after an OU seed, take near-critical progressive feedback `Y=gamma Z`; then

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`,

`sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`,

and choose

`L=log(1/gamma)/(2gamma)`.

The input cost satisfies

`||Y||_3 <= C gamma^(-1/3-gamma/2)`.

For `X_t=sigma B_t-dt`, with `t_*=L-2sqrt(L)`, `x=dt_*`, and

`kappa=2d/sigma^2=1+2/sigma^2`,

the exact identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`

plus a Mills lower bound on a `sqrt(L)` saddle window gives

`int_0^L P(|Z_{1+t}|>e^x)dt >= c e^(-kappa x)`.

The two algebraic identities

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

then imply

`||Z||_{Z_{3,alpha}}/||Y||_3
 >= c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`, and exact one-shell scaling transfers it to every fixed physical torus horizon. Hence `alpha_*(T)>=2/3`.

Therefore the recovered parent bracket is indeed

`2/3 <= alpha_*(T) <=1`.

Nothing in the theorem below silently changes this baseline.

---

## 2. New route: critical cubic tilts and their exact Hellinger overlap

The previous Bellman route controls moments while forcing is active. The new route instead studies what common Brownian noise can do **after forcing stops**, exactly at the critical exponent.

Let `E_n` be the real eigenspace of `Lambda` for

`lambda_n=1+n^2`, `n=0,1,2,...`,

with `E_n` grouping the equal-eigenvalue `+n/-n` multiplicity. Put

`a_n=sqrt(lambda_n)=sqrt(1+n^2)`.

Suppose at some stopping time `tau` the stochastic input is switched off. Conditional on `F_tau`, write

`z_n=P_n Z_tau`, `r_n=||z_n||`,

where `P_n` is the orthogonal projection onto `E_n`. By the strong Markov property of Brownian motion, for `t>=0`,

`P_n Z_{tau+t}=M_n(t) z_n`,

where

`M_n(t)=exp(a_n Delta W_t-(3/2)a_n^2 t)`.

At the critical exponent,

`E[M_n(t)^3]=1`.

Thus every individual shell has exactly persistent cubic moment:

`E[||P_n Z_{tau+t}||^3 | F_tau]=r_n^3`.

Now define the cubic tilt density

`D_n(t)=M_n(t)^3
       =exp(3a_n Delta W_t-(9/2)a_n^2 t)`.

It is a mean-one exponential martingale. For two shells `n!=m`, their Hellinger affinity is exact:

`E[(D_n(t)D_m(t))^(1/2)]
 =exp(-(9/8)(a_n-a_m)^2 t)`.                              (2.1)

Indeed the Gaussian moment is

`exp( (1/2)[(3/2)(a_n+a_m)]^2 t
      -(9/4)(a_n^2+a_m^2)t )`,

and the exponent simplifies to `-(9/8)(a_n-a_m)^2 t`.

Equivalently,

`E[(M_n(t)M_m(t))^(3/2)]
 =exp(-kappa_nm t)`,

`kappa_nm=(9/8)(a_n-a_m)^2`.                              (2.2)

This is the exact covariance/comparison quantity missing from the old two-unequal-scale discussion: equal shells remain perfectly coherent, but distinct scales become exponentially Hellinger-orthogonal on the clock set by the square-root spectral gap.

---

## 3. Sharp two-coordinate geometric inequality

For `x,y>=0`, set

`c_* = 2sqrt(2)-2 = 2(sqrt(2)-1)`.

Then

`0 <= (x^2+y^2)^(3/2)-x^3-y^3
   <= c_* (xy)^(3/2)`.                                  (3.1)

The constant `c_*` is sharp.

To prove it, divide by `(xy)^(3/2)` and put `s=x/y`. The normalized excess is

`h(s)=((1+s^2)^(3/2)-1-s^3)/s^(3/2)`.

Let `u=s+s^(-1)>=2`. Then

`h(s)=u^(3/2)-(u-1)sqrt(u+2)=:H(u)`.

Differentiate:

`H'(u)
 =(3/2)[sqrt(u)-(u+1)/sqrt(u+2)] <0`,

because `u(u+2)<=(u+1)^2`, strictly for finite `u`. Hence the maximum is at `u=2`, i.e. `s=1`, and

`H(2)=2sqrt(2)-2`.

By induction this yields, for every finite nonnegative family `(x_n)`,

`0 <= (sum_n x_n^2)^(3/2)-sum_n x_n^3
   <= c_* sum_{n<m}(x_n x_m)^(3/2)`.                    (3.2)

The induction step applies (3.1) to

`S=(sum_{n<N}x_n^2)^(1/2)` and `x_N`,

and uses the concavity inequality

`S^(3/2)=(sum_{n<N}x_n^2)^(3/4)
 <=sum_{n<N}x_n^(3/2)`.

---

## 4. Exact finite-spectrum cross-scale decoherence

Apply (3.2) with

`x_n=r_n M_n(t)`.

Using the critical marginal identity `E M_n^3=1` and the overlap formula (2.2), we obtain conditionally on `F_tau`:

`0 <= E[||Z_{tau+t}||^3 | F_tau]-sum_n r_n^3`

`<= c_* sum_{n<m}(r_n r_m)^(3/2)
              exp(-(9/8)(a_n-a_m)^2 t)`.                (4.1)

For two unequal shells this is already a complete quantitative answer to the passive common-noise question:

`0 <= E||(Z_n,Z_m)||^3-r_n^3-r_m^3`

`<= c_*(r_n r_m)^(3/2)e^{-kappa_nm t}`.                 (4.2)

Therefore the total future two-shell excess occupation obeys

`int_0^infinity [E||(Z_n,Z_m)||^3-r_n^3-r_m^3]dt`

`<= [c_*/kappa_nm](r_n r_m)^(3/2)`.                     (4.3)

This is an explicit finite-memory theorem at the exact critical exponent `p=3`. The critical marginal shell energies do not decay, but the unequal-scale contribution does.

---

## 5. Full-torus summation with an explicit horizon-independent constant

The key point is that the exact torus spectrum makes (4.1) summable without a truncation-dependent loss.

The function

`f(x)=sqrt(1+x^2)`

is strictly convex on `[0,infinity)` because

`f''(x)=(1+x^2)^(-3/2)>0`.

Hence the adjacent gaps `a_{n+1}-a_n` are increasing, and their minimum is

`d_0=a_1-a_0=sqrt(2)-1`.                                 (5.1)

Thus, for `m>n`,

`a_m-a_n >= d_0(m-n)`.                                  (5.2)

Integrating (4.1) in time gives

`int_0^infinity offdiag(t)dt`

`<= c_*(8/9) sum_{n<m}
   (r_n r_m)^(3/2)/(a_m-a_n)^2`

`<= c_*(8/9)d_0^(-2)
   sum_{h>=1} h^(-2) sum_n r_n^(3/2)r_{n+h}^(3/2)`.      (5.3)

Put `x_n=r_n^(3/2)`. Cauchy–Schwarz gives, for every `h>=1`,

`sum_n x_n x_{n+h} <= sum_n x_n^2`.

Therefore

`sum_{h>=1} h^(-2) sum_n x_n x_{n+h}
 <=(pi^2/6)sum_n x_n^2`.                                (5.4)

Finally

`sum_n x_n^2=sum_n r_n^3
 <=(sum_n r_n^2)^(3/2)=||Z_tau||^3`.                    (5.5)

Combining (5.3)–(5.5), and using `c_*=2d_0`, gives the explicit constant

`C_dec
 = c_*(8/9)d_0^(-2)(pi^2/6)
 = 8 pi^2 (sqrt(2)+1)/27
 = 7.059950459368...`.                                  (5.6)

This proves the main theorem.

> **Theorem NM10-AVP3-CRITICAL-CROSS-SCALE-DECOHERENCE-12.**
> Consider the exact frozen torus pair `(A,B)=(Lambda,Lambda^(1/2))` at the critical exponent `p=3`. Let `tau` be a stopping time and suppose the stochastic input is zero on `[tau,infinity)`. If `E||Z_tau||^3<infinity`, then, grouping equal Fourier eigenspaces `E_n`,
>
> `0 <= E[||Z_{tau+t}||^3 | F_tau]-sum_n ||P_n Z_tau||^3`
>
> `<= c_* sum_{n<m}
>    (||P_nZ_tau|| ||P_mZ_tau||)^(3/2)
>    exp(-(9/8)(a_n-a_m)^2 t)`
>
> for every `t>0` (first on finite projections, then by monotone convergence), and
>
> `int_0^infinity E[
>    E(||Z_{tau+t}||^3 | F_tau)
>    -sum_n ||P_n Z_tau||^3] dt`
>
> `<= C_dec E||Z_tau||^3`,
>
> where
>
> `c_*=2sqrt(2)-2`,
>
> `C_dec=8pi^2(sqrt(2)+1)/27 <7.06`.

For an infinite Fourier expansion, take nested finite shell projections. The left side is nonnegative and the projected Euclidean norms increase pointwise to the full norm; the shell-cube sum increases to `sum r_n^3`; the uniform bound (5.6) gives the needed domination/Fatou passage. This removes the finite-dimensional truncation.

The same proof is conditional at every stopping time because Brownian increments after `tau` are independent of `F_tau`; the result therefore fits the source stopping-time conventions rather than only deterministic restart times.

---

## 6. Equivalent kernel form and why this matters for the parent endpoint

Define

`kappa_0=(9/8)(sqrt(2)-1)^2=0.193019484660...`

and

`K(t)=sum_{h>=1} exp(-kappa_0 h^2 t)`.

The same Cauchy–Schwarz step before time integration gives the pointwise full-spectrum estimate

`offdiag(t)
 <= c_* K(t) ||Z_tau||^3`.                               (6.1)

Moreover

`int_0^infinity K(t)dt
 =(pi^2/6)/kappa_0`,                                     (6.2)

which is exactly the origin of `C_dec`.

Thus the common Brownian driver has a very specific critical memory structure:

- diagonal/equal-eigenvalue cubic mass is exactly conserved in expectation;
- distinct-shell cubic coherence is represented by a Gaussian heat kernel in the square-root spectral distance;
- on the one-dimensional torus, that kernel has finite `L^1_t(ell^2->ell^2)` mass after grouping multiplicity.

This is a new extrapolation mechanism, not merely a restatement of the scalar endpoint. It says that **passive unequal-scale coherence cannot be responsible for any long-horizon critical divergence beyond the diagonal shell mechanism**.

In particular, a construction that uses an admissible seed up to a stopping time and then turns off the input cannot obtain a worse critical endpoint by exploiting two or many unequal scales: all extra vector interaction after the seed costs at most `C_dec E||Z_tau||^3` in total cubic occupation.

This rules out the old “seed once, then let common Brownian unequal scales amplify forever” route. Any counterexample to the conjectural `L^3 -> Z_{3,2/3}` endpoint, or any mechanism forcing exponent strictly above `2/3`, must continually inject/adapt forcing during the periods when cross-scale coherence is being created. Conversely, an energy-stopping proof of the positive endpoint now only has to charge those **active** intervals; the off-input intervals have an explicit summable boundary cost.

For a family of disjoint stopping intervals on which the input is zero, restarting the theorem at the left endpoint gives immediately

`sum_j int_{tau_j}^{sigma_j} offdiag_j(t)dt
 <= C_dec sum_j E||Z_{tau_j}||^3`.                        (6.3)

This is the concrete bridge to the previously requested level-truncated Bellman/energy-stopping attack.

---

## 7. What this run does not prove

The theorem is critical and full-spectrum, but it is intentionally not mislabeled.

1. It does **not** change `r_*=3` or restore strong `p=3` maximal regularity.
2. It does **not** improve the parent spacetime exponent bracket `[2/3,1]` yet.
3. It does **not** prove `T_T:L^3 -> Z_{3,2/3}(T)` for arbitrary progressive inputs, because active forcing can continuously recreate cross-scale coherence.
4. It does **not** replace the arbitrary-pair wording of Agresti–Veraar Problem 3 by a commutative sufficient condition.
5. It does **not** reopen Problems 4–5, which remain excluded by `POSTED.md`/campaign history.

The exact residual obligation is now narrower: prove a Carleson/energy charge for the active intervals in a level-stopping decomposition. The passive intervals are controlled by (6.3).

Because this run produced a new theorem-level mechanism after deliberately changing methods, there have not been two failed recovery routes and the T05 fallback is not triggered.

---

## 8. Essential checker

`2026-09-20T10-49-48+0300__critical_cross_scale_decoherence_check.py`

was executed locally before persistence. It checks:

- the exact Hellinger exponent algebra symbolically;
- the sharp pair constant `c_*=2sqrt(2)-2` and its maximizing ratio `x=y`;
- the torus square-root spectral gap numerically at high precision across the first 501 adjacent gaps, consistent with the analytic convexity proof;
- the discrete `1/h^2` Schur bound on finite test vectors;
- the closed form
  `C_dec=8pi^2(sqrt(2)+1)/27`;
- representative overlap decays.

The archived output ends `CHECK_PASS` and reports

`C_dec=7.059950459368033`.

The checker is a sanity check; the theorem proof is the analytic argument in Sections 2–5.

---

## 9. Bounded current literature check, 20 September 2026

A bounded fresh search was made for source-matching extrapolation or endpoint results, using combinations of `Agresti Veraar 2501.18561 Problem 3`, `stochastic maximal regularity extrapolation 2026`, and `multiplicative noise maximal regularity`.

Recovered relevant items:

- Agresti–Veraar, arXiv:2501.18561 / NoDEA 32 (2025), article 123, published 1 September 2025: still the Problem 3 source.
- Bechtel–Veraar, *An extrapolation result in the variational setting*, published 11 July 2025: gives some `p>2` extrapolation under the variational/symmetry framework, not the exact nonsmall multiplicative frozen-pair endpoint developed here.
- Evangelopoulos-Ntemiris–Veraar, *Discrete stochastic maximal regularity*, published 13 February 2026: concerns temporal numerical/discrete SMR and continuous-to-discrete transfer, not this state-multiplicative common-Brownian endpoint.
- Lorist–van Neerven–Veraar, arXiv:2608.20266, submitted 20 August 2026: studies necessary Banach-geometry conditions for stochastic maximal regularity and canonical test operators, not this exact critical torus endpoint.

No bounded-search result was found that supplies the cross-scale cubic decoherence theorem above or resolves the full `L^3 -> Z_{3,2/3}` claim for the frozen pair. This is not a worldwide novelty certificate.

---

## 10. Next attack

Use (6.3) inside the actual level/energy stopping decomposition suggested by the previous Bellman-trace run. On intervals where the input energy stays below the stopping threshold, turn the equation into a boundary term plus homogeneous continuation and charge all unequal-shell occupation with `C_dec`. The remaining task is then an active-interval Carleson estimate whose charge is the cubic input energy. A successful bound with the correct layer summability would prove the full `alpha=2/3` endpoint; a failure should expose an explicit repeatedly-forced adaptive counterexample rather than another passive two-scale construction.

No auditor or peer result is required before executing that attack.
