Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0290 — a three-state obstruction to the second-order light-traffic counterexample route

## Source target and scope

Target: Lasse Leskelä, *Ross’s second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), Problem 2 on journal p. 214. Under the stable Cox/GI/1 setting of Problem 1, the source asks whether the mean stationary workload remains nonincreasing when the Cox intensity is `lambda_c(t)=f(X(ct))`, where `X` is a stationary doubly stochastically monotone CTMC and `f` is an arbitrary deterministic nonnegative function (Boolean is explicitly allowed).

Primary accepted-manuscript URL:
`https://acris.aalto.fi/ws/portalfiles/portal/89616571/Ross_s_second_conjecture_and_supermodular_stochastic_ordering.pdf`

This artifact does **not** solve P0290. It proves a structural obstruction to the already recovered P0289/P0290 second-order light-traffic counterexample mechanism. In particular, it shows that three hidden states are too few for that mechanism, even if one assumes only forward stochastic monotonicity rather than the source's stronger double monotonicity.

## Recovered light-traffic baseline

The earlier campaign derivation for unit deterministic service and small intensity `epsilon f(X(ct))` has the form

`w_epsilon(c) = epsilon*m/2 + epsilon^2 J_f(c) + R_epsilon(c)`,

where `m=E[f(X_0)]`, the remainder is uniformly `O(epsilon^3)` on the source-faithful finite-state models used there, and

`J_f(c) = int_0^1 (1-u) E[f(X_0) f(X_{cu})] du`.

Thus a strict rise of `J_f` at two speeds is a sufficient second-order mechanism for a sufficiently small-intensity counterexample. The existing P0290 searches did not find such a rise on small doubly monotone chains.

The goal here is to explain exactly why the three-state search cannot succeed through this coefficient.

---

# B18 — say the coefficient in another language: variance of a time average

Let

`m = E[f(X_0)]`, `g=f-m`, and `C(t)=E[g(X_0)g(X_t)]`.

Stationarity gives

`E[f(X_0)f(X_t)] = m^2 + C(t)`.

Hence

`J_f(c) = m^2/2 + J_g(c)`,

where

`J_g(c) = int_0^1 (1-u) C(cu) du`.

Now define the empirical time average over a window of length `c`:

`A_c = c^{-1} int_0^c g(X_t) dt`.

Because the scalar covariance of a real stationary process is even,

`C(-t)=C(t)`.

Double-count pairs `(s,t)` in the square `[0,c]^2`:

`Var(A_c)
 = c^{-2} int_0^c int_0^c C(t-s) ds dt
 = (2/c^2) int_0^c (c-r) C(r) dr
 = 2 int_0^1 (1-u) C(cu) du`.

Therefore

**(1)** `boxed( J_g(c) = (1/2) Var(A_c) )`.

So the second-order P0290 problem is exactly the following variance question:

> Can the variance of the time average of a deterministic observable of a doubly stochastically monotone CTMC increase when the averaging window gets longer?

This translation is useful because a generic stationary process can indeed have such an increase: in spectral language the filter is a squared-sinc kernel, which oscillates as the window changes. Therefore stationarity alone does not prove monotonicity. The hidden-chain order restrictions have to do real work.

---

# B2 — attack the negation at the smallest hidden state size

Consider an ordered three-state CTMC on `0<1<2` with generator

```
Q = [ -(a+b)      a          b
          c     -(c+d)       d
          e        f       -(e+f) ],
```

where all off-diagonal rates are nonnegative and the chain is irreducible.

## Lemma 1 — forward stochastic monotonicity forces real spectrum

For a three-state generator, the standard generator criterion for stochastic monotonicity has only two nontrivial inequalities:

**(2)** `b <= d` and `c >= e`.

Indeed, for the pair `(0,1)` the only upper set excluding both states is `{2}`, giving `q_02 <= q_12`; for `(1,2)` the only lower set excluding both is `{0}`, giving `q_10 >= q_20`. No additional nontrivial set remains for `(0,2)`.

Write

`u=d-b >= 0`, `v=c-e >= 0`.

Since every generator has eigenvalue zero, the other two eigenvalues are the roots of

`lambda^2 + S lambda + P = 0`,

where

`S=a+b+c+d+e+f`

and the sum of the three principal `2 x 2` minors is

`P = (ce+cf+de) + (ae+af+bf) + (ad+bc+bd)`.

A direct expansion after substituting `c=e+v`, `d=b+u` gives

**(3)**

`boxed( S^2 - 4P = (a-f-u+v)^2 + 4uv >= 0. )`

Thus both nonzero eigenvalues are real. Irreducibility then puts them on the negative real axis.

This proves something stronger than needed for the source: **every irreducible three-state forward-stochastically-monotone CTMC has real spectrum.** Double stochastic monotonicity is not needed for this spectral conclusion.

In particular, the directed-cycle/oscillatory complex-eigenvalue mechanism used in the broader P0289 counterexample cannot occur with only three hidden states under P0290's hypotheses.

---

# B25 — count the time-average pairs twice, then dualize their two-mode covariance

The real-spectrum fact alone is not enough: a sum of two real decaying exponentials can have one negative coefficient, so its covariance need not be pointwise decreasing. What matters is the smoothed coefficient `J_g`.

We first prove a standalone two-mode theorem.

## Lemma 2 — every positive-definite two-real-exponential covariance has decreasing time-average variance

Let a real stationary process have centered covariance

**(4)** `C(t)=A exp(-alpha |t|) + B exp(-beta |t|)`

with `0<alpha<beta`. Then

**(5)** `J(c)=int_0^1 (1-u) C(cu) du`

is nonincreasing for `c>0`.

### Proof

Define

`phi(x) = (exp(-x)-1+x)/x^2 = int_0^1 (1-u) exp(-xu) du`.

Then

`J(c)=A phi(alpha c)+B phi(beta c)`.

Put

**(6)** `g_0(x)=-phi'(x)=[x-2+(x+2)exp(-x)]/x^3`.

We need two elementary facts.

### Fact 1: `g_0` is nonincreasing and positive on `(0,infinity)`

Differentiation gives

**(7)** `x^4 g_0'(x)=6-2x-(x^2+4x+6)exp(-x)`.

For `x>=3` the right side is immediately negative. For `0<x<3`, (7) is nonpositive exactly when

`(6-2x)e^x <= x^2+4x+6`.

Set

`F(x)=x^2+4x+6-(6-2x)e^x`.

Then `F(0)=F'(0)=0` and

`F''(x)=2[1-(1-x)e^x] >= 0`,

because `h(x)=(1-x)e^x` has derivative `-x e^x <=0` and hence `h(x)<=h(0)=1`. Thus `F(x)>=0` and `g_0'(x)<=0`.

Also `g_0(x)>0` because `phi` is the integral of `(1-u)e^{-xu}` and is strictly decreasing in `x`.

### Fact 2: `x^2 g_0(x)` is nondecreasing

A direct derivative gives

**(8)** `x^2 d/dx[x^2 g_0(x)] = 2-(x^2+2x+2)e^{-x}`.

The right side is nonnegative because

`2e^x >= 2+2x+x^2`

by the exponential series. Hence `x^2 g_0(x)` is nondecreasing.

### Use positive definiteness

The Fourier transform of (4), apart from the harmless common factor `2`, is

`A alpha/(alpha^2+omega^2) + B beta/(beta^2+omega^2)`.

Because a stationary covariance is positive definite, this spectral density is nonnegative for every real `omega`. Multiplying by its positive denominator, the numerator is

**(9)**

`alpha beta (A beta+B alpha) + (A alpha+B beta) omega^2`.

Therefore

**(10)** `A beta+B alpha >=0`,

**(11)** `A alpha+B beta >=0`.

Now

**(12)** `J'(c)=-A alpha g_0(alpha c)-B beta g_0(beta c)`.

There are only three sign patterns to consider.

- If `A>=0` and `B>=0`, (12) is immediately nonpositive.
- If `A<0<B`, put `a_0=-A`. From (10), `B/a_0 >= beta/alpha`. Hence

  `J'(c)
   <= a_0 alpha g_0(alpha c) - a_0 (beta^2/alpha) g_0(beta c)
   = (a_0/alpha)[alpha^2 g_0(alpha c)-beta^2 g_0(beta c)] <=0`,

  where the final inequality is Fact 2.
- If `B<0<A`, put `b_0=-B`. From (11), `A/b_0 >= beta/alpha`. Hence

  `J'(c)
   <= -b_0 beta g_0(alpha c)+b_0 beta g_0(beta c) <=0`,

  by Fact 1.

Both coefficients cannot be negative under (10)–(11). Zero cases follow by continuity. This proves Lemma 2. `square`

---

# Theorem — no three-state second-order P0290 reversal

Let `X` be an irreducible stationary CTMC on three ordered states whose generator is stochastically monotone. Let `f` be any real deterministic function on the three states. Define

`J_f(c)=int_0^1 (1-u) E[f(X_0)f(X_{cu})]du`.

Then

**(13)** `boxed( J_f(c) is nonincreasing on (0,infinity). )`

### Proof: distinct eigenvalues

Center `f` to `g=f-Ef`; the removed mean contributes only the constant `(Ef)^2/2` to `J_f`.

By Lemma 1, the two nonzero eigenvalues are real and negative. If they are distinct, write them as `-alpha,-beta`, `0<alpha<beta`. On the two-dimensional centered subspace the semigroup is diagonalizable, and hence

`C(t)=E[g(X_0)g(X_t)] = A e^{-alpha t}+B e^{-beta t}` for `t>=0`.

By stationarity the covariance extends evenly to negative times, so it has the form in Lemma 2. Therefore `J_g`, and hence `J_f`, is nonincreasing.

### Proof: repeated eigenvalue

If the discriminant in (3) vanishes, perturb one allowed monotone rate, for example replace `d` by `d+epsilon` with `epsilon>0`. This preserves `b<=d`, preserves irreducibility, and for a sequence `epsilon_n downarrow 0` can be chosen so that the two nonzero eigenvalues are distinct. Each perturbed chain satisfies the already-proved distinct-eigenvalue conclusion.

The stationary distribution of a finite irreducible generator and its matrix exponential depend continuously on the generator. Hence for every fixed `c`, `J_f^{(epsilon_n)}(c) -> J_f(c)`. A pointwise limit of nonincreasing functions is nonincreasing. Thus (13) also holds at the repeated-eigenvalue boundary. `square`

---

# Consequence for Leskelä Problem 2

Every three-state doubly stochastically monotone CTMC is, in particular, forward stochastically monotone. Therefore the theorem applies to every three-state hidden chain allowed by P0290.

For the recovered small-intensity deterministic-service expansion,

`w_epsilon(c)=epsilon*m/2+epsilon^2 J_f(c)+O(epsilon^3)`,

the second-order coefficient **cannot rise with speed on any three-state source-admissible hidden chain**.

So any refutation through the already established P0289-style second-order mechanism needs at least four hidden states. This agrees with, and now rigorously explains, the earlier computational observation that the sampled three-state monotone chains had no complex eigenvalues while four-state doubly monotone chains sometimes did.

Important limitation: this is **not** a proof that P0290 is true for all three-state chains at arbitrary load. A higher-order light-traffic term or a moderate/heavy-load mechanism could in principle still reverse the workload even when the second-order coefficient is monotone. The theorem rules out precisely the second-order route, nothing more.

# Frozen source metric

`Delta_Ross` before: **UNKNOWN/UNMEASURED**.

`Delta_Ross` after: **UNKNOWN/UNMEASURED — NO MOVEMENT**.

This theorem shrinks the counterexample search space but does not certify a positive workload reversal or prove universal workload monotonicity. Target-specific ordinary unchanged count therefore becomes `0 -> 1`.

# Exact symbolic self-check

A separate exact SymPy checker verifies:

1. the discriminant identity (3);
2. the derivative identities (7) and (8);
3. the spectral numerator identity (9).

This checker is a self-check of algebra, not an independent audit and not evidence of source closure.

# Next mathematical attack

Do not repeat B2/B18/B25 next run. The useful next routes are:

- **B15 — break the symmetry on purpose:** seek a four-state doubly monotone family with one controllable complex conjugate eigenpair and tune its damping-to-frequency ratio instead of random-searching the full cone.
- **B24 — find the extremal object:** maximize the derivative of the exact time-average variance `J_f'(c)` over Boolean images and the four-state monotonicity cone, aiming for a boundary/extreme generator that can be handled symbolically.
- **B30 — one scale/direction at a time:** first decide whether a four-state source-admissible chain can make the *second-order* coefficient rise at all; only if yes move to the full workload and an exact queueing certificate.

# Prior-art caution

The 1998 Bäuerle–Rolski theorem proves workload decrease under monotonicity assumptions on the Markov-modulated **intensity chain** itself. Leskelä's 2022 Problem 2 asks what survives after applying an arbitrary deterministic image to a doubly monotone hidden chain. A bounded 2026-09-19 search found no source explicitly recording the three-state discriminant/time-average theorem above, but a search miss is not a novelty certificate. Status remains **OPEN / PARTIAL**.