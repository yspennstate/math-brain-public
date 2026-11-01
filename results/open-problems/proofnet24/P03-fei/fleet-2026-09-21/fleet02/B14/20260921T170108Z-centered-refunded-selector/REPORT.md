TASK: B14 ACCOUNT: fleet02 RUN: 2026-09-21T17:01:08.308949+00:00 — centered refunded erasure selector and critical-core localization

Status: OPEN / PARTIAL. Full Friedgut–Kalai Fourier entropy-influence (FEI) remains OPEN / NOT PROVED.

Execution context: WITHOUT_VERIFIED_BRAIN. No authenticated math_brain or cognitive-memory retrieval was used in the derivation.

Model self-report: GPT-5.6 Sol. Reasoning effort requested: maximum actually supported. Configured reasoning level and provider reasoning usage: UNKNOWN / not exposed.

## 0. Fresh sources and exact scope



Fresh `yspennstate/math-open-problems` master was `4d927de8da1be5a61aa9dec10d418660e4686e87`. I read `FLEET_RULES.md`, `proofnet24/P03-fei/README.md`, and the September-21 TASKS/REPORT/APPROACHES continuation. The unrestricted FEI target is not the older Hod/read-once scale: the current recorded certified lower bound is `C_FEI > 6.521845710923046575` from Numaro's 18-variable monotone seed plus amplification. Full FEI still has no known finite universal upper bound.

This run continues the newest B14 `refunded-selector-proof` artifacts (`f861d76963f528f8446efe64ea60417d03b645b8`, `c2e7696a1a73fdfb62f3afe0c955e10083460f57`) rather than restarting the fixed-seed route. Those artifacts established the raw refunded selector algebra but also preserved the parity-padding failure of a selector based only on unshifted singleton Fourier mass. The new step below removes deterministic parity padding by an influence-nonincreasing character gauge and then compiles the selector back to the ORIGINAL physical restriction recurrence.

Primary-literature/status check this run: González–MacManus–Pereyra (arXiv:2606.00246, 29 May 2026) use a restriction-decrement/stopping-tree framework; Potapov (arXiv:2609.21563, 18 Sep 2026) proves FEI for plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2; Han's published bound is `H=O(I+sum_i I_i log(1/I_i))`. A bounded search did not locate the centered-shell lemma below. That search failure is NOT evidence of novelty; priority is UNVERIFIED.

## 1. Normalization and exact quantities

Let `f:{-1,+1}^n->{-1,+1}` be Boolean, with Fourier-Walsh coefficients `fhat(S)`. Let the spectral sample `X` have

`mu(S)=Pr[X=S]=fhat(S)^2`.

Write

`H(f)=H(X)` (bits),
`p_i=Pr[i in X]=Inf_i(f)`,
`I(f)=sum_i p_i=E|X|`.

For coordinate `i`, let

`B_i(f)=H(X_i | X_{-i})`

be the singleton spectral erasure. The exact restriction decomposition recovered earlier is

`Delta_i H(f) := H(f) - (H(f_{i=+1})+H(f_{i=-1}))/2 = B_i(f)+JS_i(f)`,       (1)

with the inherited sharp-enough envelope

`0 <= JS_i(f) <= kappa min(p_i,1-p_i)`,  `kappa=2/ln 2`.                    (2)

Also

`I(f)=p_i+(I(f_{i=+1})+I(f_{i=-1}))/2`.                                  (3)

The known false statement is that every prescribed relevant coordinate always obeys a universal upper payment. Nothing below asserts that. Every selector conclusion is existential in `i`.

Define for `a,b>=0`

`E(a,b)=a log_2((a+b)/a)+b log_2((a+b)/b)`,

with zero terms interpreted continuously. Thus `E(a,b)=(a+b) h_2(b/(a+b))`.

For `0<t<=1`, define

`Gamma(t)=E((1-t)/t,1-t)`,
`F(t)=Gamma(t)+2(1-t)`.                                                    (4)

Both arguments of `E((1-t)/t,1-t)` decrease with `t`, while `E` is increasing in each argument, hence `Gamma` and `F` are decreasing.

## 2. PROVED: raw refunded selector for a centered Boolean function

### Lemma 2.1 (coordinate refunded erasure bound)

Let `g` be Boolean and fix a coordinate with influence `q>0`. Put

`c = ghat(empty)^2`,
`e = ghat({i})^2`,
`t = e/q`.

Then `0<=t<=q<=1`, and

`B_i(g)-E(c,e) <= q Gamma(t)`,                                             (5)
`E(c,e) <= 2q(1-t)`,                                                       (6)
`B_i(g) <= q F(t)`.                                                        (7)

#### Proof

First, the oriented Boolean derivative in direction `i` takes values in `{-1,0,+1}`. Its expectation, up to sign convention, is `ghat({i})`, while its absolute expectation is `q`. Hence

`|ghat({i})| <= q`, so `e<=q^2` and therefore `t=e/q<=q`.                  (8)

Write the spectral masses in physical `i`-fibres as pairs `(mu_T,mu_{T union {i}})`. The empty/singleton pair is `(c,e)`. Let

`A = sum_{T nonempty, i notin T} mu_T = 1-c-q`,
`D = sum_{T nonempty, i notin T} mu_{T union {i}} = q-e = q(1-t)`.         (9)

Because `E` is homogeneous and concave, the log-sum inequality gives

`B_i(g)-E(c,e)
 = sum_{T nonempty, i notin T} E(mu_T,mu_{T union {i}})
 <= E(A,D)
 <= E(1-q,q(1-t))
 = q E((1-q)/q,1-t)
 <= q E((1-t)/t,1-t)
 = q Gamma(t)`.                                                           (10)

The penultimate inequality uses `q>=t`, so `(1-q)/q <= (1-t)/t`, and monotonicity of `E`.

For the refund itself use Booleanity. Since `g^2=1`, the nonempty Fourier coefficient of `g^2` at `{i}` vanishes:

`ghat(empty) ghat({i}) + sum_{T nonempty, i notin T} ghat(T) ghat(T union {i}) = 0`. (11)

Cauchy-Schwarz and (9) imply

`ce <= A D = (1-c-q) q(1-t)`,

hence, after division by `q` and rearrangement,

`c <= (1-q)(1-t)`.                                                        (12)

Together with `t<=q`,

`ce = c q t <= q t(1-q)(1-t) <= q^2(1-t)^2`.                              (13)

The elementary binary-entropy inequality `h_2(x)<=2 sqrt{x(1-x)}` gives

`E(c,e) <= 2 sqrt{ce} <= 2q(1-t)`.                                        (14)

Adding (5) and (6) proves (7). QED.

### Lemma 2.2 (mass-weighted existential selector)

For nonconstant Boolean `g`, define

`W_1(g)=sum_i ghat({i})^2`,
`r(g)=W_1(g)/I(g)`.

If `r(g)>0`, then there exists a relevant coordinate `i` such that

`B_i(g)-E(c,ghat({i})^2) <= Gamma(r(g)) Inf_i(g)`,                         (15)
`B_i(g) <= F(r(g)) Inf_i(g)`.                                             (16)

#### Proof

For relevant `i` put `t_i=ghat({i})^2/Inf_i(g)`. Then

`r(g)=sum_i Inf_i(g)t_i / sum_i Inf_i(g)`                                 (17)

is an influence-weighted average. Hence some relevant coordinate has `t_i>=r(g)`. Apply Lemma 2.1 and the fact that `Gamma,F` decrease. QED.

This is existential. It does NOT imply the false every-coordinate upper payment.

## 3. PROVED NEW IMPLICATION: median-character centering makes the selector parity-padding robust

The unshifted `r(g)` is not a viable universal invariant: multiplying a hard function by a fresh parity character can make all singleton Fourier mass vanish while changing `H/I` only by an asymptotically negligible amount under tensor amplification. That failure was preserved by the preceding B14 run.

The repair is to center the SPECTRAL SAMPLE before selecting, but to pay the ORIGINAL physical influence after selecting.

For the original `f`, define the coordinatewise spectral median vector

`a_i = 1{p_i>1/2}`, `A={i:a_i=1}`,
`q_i=min(p_i,1-p_i)`, `J=sum_i q_i`.                                      (18)

Let

`g(x)=chi_A(x) f(x)`.                                                      (19)

Then `g` is Boolean and its spectral sample is `Y=X symmetric_difference A`. Therefore

`H(g)=H(f)`,
`Inf_i(g)=q_i<=p_i`,
`I(g)=J<=I(f)`.                                                            (20)

Moreover, multiplication by a character on the residual variables (and an irrelevant global sign when `i in A`) maps each physical restriction of `f` to the corresponding restriction of `g` without changing its spectral entropy. Thus

`Delta_i H(g)=Delta_i H(f)`, `B_i(g)=B_i(f)`.                              (21)

Define the centered first-shell mass and centered selector fraction

`W_1^c(f)=sum_i mu(A symmetric_difference {i}) = Pr[d_H(X,A)=1]`,
`r_c(f)=W_1^c(f)/J` when `J>0`.                                           (22)

So `r_c` has a direct probabilistic meaning:

`r_c(f) = Pr[d_H(X,A)=1] / E[d_H(X,A)]`.                                  (23)

If `J=0`, every spectral coordinate is deterministic, so `mu` is a point mass and `f` is a signed character; hence `H(f)=0`.

### Theorem 3.1 (centered refunded selector)

If `J>0` and `r_c(f)>0`, there exists a physical coordinate `i` such that

`B_i(f) <= F(r_c(f)) q_i <= F(r_c(f)) p_i`,                               (24)

and, using (1)-(2),

`Delta_i H(f) <= [F(r_c(f))+2/ln 2] q_i
              <= [F(r_c(f))+2/ln 2] p_i`.                                (25)

#### Proof

Apply Lemma 2.2 to the Boolean function `g=chi_A f`. Its total influence is `J`; its singleton Fourier mass is exactly `W_1^c(f)`; hence its raw selector fraction is `r_c(f)`. Equation (21) transfers the erasure and restriction decrement back to the same physical coordinate of `f`. Equation (2) applied to either `f` or `g` has the same sharp marginal factor `min(p_i,1-p_i)=q_i`. Finally `q_i<=p_i`. QED.

This is the key new implication of the run. It repairs the deterministic-parity-padding obstruction without changing the physical restriction tree or pretending that character multiplication preserves total influence.

## 4. PROVED: a restriction-closed compiler and a universal critical-core localization

### Corollary 4.1 (restriction-closed centered-shell compiler)

Fix `rho in (0,1]`. Let `C` be any class of Boolean functions closed under physical restrictions and suppose every noncharacter nonconstant `h in C` satisfies

`r_c(h) >= rho`.                                                          (26)

Then every `h in C` obeys FEI with the dimension-free constant

`H(h) <= C_rho I(h)`,
`C_rho = F(rho)+2/ln 2`.                                                   (27)

#### Proof

Induct on the number of relevant variables. Characters have spectral entropy zero. Otherwise Theorem 3.1 supplies a coordinate with `Delta_i H <= C_rho Inf_i(h)`. Apply the inductive hypothesis to both physical children and combine the exact identities (1) and (3). QED.

Thus full FEI is reduced to controlling the complementary regime in which restriction descendants can have very small centered first-shell fraction. No every-coordinate assertion is needed.

### Corollary 4.2 (critical descendant localization)

For any nonconstant Boolean `f`, choose among all nonconstant physical restriction descendants a descendant `h` maximizing

`R(h)=H(h)/I(h)`.

The previously proved extremal-descendant argument gives, for every relevant physical coordinate `i` of `h`,

`Delta_i H(h) >= R(h) Inf_i(h)`, and `R(h)>=H(f)/I(f)`.                    (28)

Combine (28) with the existential centered selector (25). If `r_c(h)>0`, then

`R(h) <= F(r_c(h))+2/ln 2`.                                               (29)

Since the right side decreases in `r_c`, every counterexample above a candidate constant `C>2/ln 2` has a restriction-critical descendant with

`r_c(h) < rho(C)`,                                                        (30)

where `rho(C)` is the unique solution of

`F(rho)+2/ln 2=C`.                                                        (31)

At the CURRENT certified unrestricted lower-bound scale

`C0=6.521845710923046575`,

numerical bisection of the explicit one-variable function gives

`rho(C0)=0.3156061323581677...`.                                          (32)

Therefore a hypothetical function with `H/I>C0` has a restriction-critical descendant whose centered spectral sample satisfies

`Pr[d_H(X,A)=1] / E[d_H(X,A)] < 0.3156061323581677...`.                    (33)

Equivalently, more than

`1-rho(C0)=0.6843938676418323...`                                         (34)

of that descendant's CENTERED influence is carried by spectral distances at least two from the median character.

This is a genuine before/after improvement over the unshifted singleton selector: deterministic parity factors no longer manufacture `r=0`, because every coordinate with spectral marginal one is removed by the median character before the selector is evaluated.

## 5. What this does NOT solve; preserved counterexamples and a sharp next obligation

Full FEI remains OPEN. Character centering does not force `r_c>0` universally. The smallest finite sanity search already contains noncharacter centered-shell-zero examples. One 3-variable spectrum is uniform on

`{empty, {1,2}, {1,3}, {2,3}}`.

For it `p_1=p_2=p_3=1/2`, so the median anchor may be taken as empty, `J=3/2`, but `W_1^c=0`; its entropy is 2 bits and its FEI ratio is only `4/3`. This is not a FEI counterexample. It shows exactly why the theorem above is a localization rather than closure.

The known counterexamples to stronger every-coordinate restriction payments are untouched: Theorem 3.1 chooses ONE coordinate after a global mass-weighted comparison and never asserts a bound for a prescribed coordinate.

The next universal obligation is now sharper and parity-padding invariant:

> Rule out high-`H/I` restriction-critical Boolean functions whose spectrum, after coordinatewise median character centering, has too little mass in Hamming shell one relative to its mean centered Hamming radius.

At the current lower-bound scale, the hard regime is `r_c<0.3156061323581677`. A natural next step is to combine the Boolean convolution identities at all coordinates with the centered distance-2-and-higher mass in (34), rather than returning to an uncentered singleton-mass argument. Plateaued/partially-bent spectra are a useful positive calibration because current primary literature already proves FEI on those classes; they must not be re-announced as universal progress.

## 6. Finite sanity check (not used as theorem)

A companion exhaustive self-check over all 65,804 nonconstant Boolean functions through dimension four verifies the centered influence reduction and both existential inequalities at tolerance `5e-10`. It records 52 centered characters, 65,328 functions with positive centered shell, and 424 noncharacter centered-shell-zero cases. This finite computation is only a regression check for the analytic proof above and does not establish FEI in higher dimension.

No novelty or publication-priority claim is made. The scientific status remains OPEN / PARTIAL.
