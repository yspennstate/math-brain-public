TASK: B13 ACCOUNT: fleet02 RUN: 2026-09-21T16:24:18.302657Z — one-point-defect Boolean block/profile sharpness and a macroscopic projection-credit obstruction

MODEL: GPT-5.6 Sol
THINKING LEVEL: UNKNOWN; source=not_exposed; requested=maximum actually supported
THINKING USAGE: reasoning tokens NOT_EXPOSED; provider thinking time NOT_EXPOSED; coverage=unavailable
RESEARCH EXECUTION: WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-side brain context was consumed.

## Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

This run follows the later direct owner order `FEI-SEVEN-TASKS-2026-09-21`, which supersedes the still-provisional benchmark row for B13. The mathematical target is approach 2/13: Boolean block-influence/correlation profiles and two-sided Booleanity constraints.

The concrete advance is a genuine Boolean stress family showing two things simultaneously:

1. the previously derived two-sided physical block-parity atom caps are **simultaneously sharp for every nonempty block on one Boolean function family**, so no pointwise improvement of those one-block constants can close FEI; and
2. B18's scaled projection credit can be only `O(I)` while the spectral total correlation is `Theta(n I)`. Therefore no universal lemma of the form `K_{floor(theta n)} >= c_theta T` with fixed `theta in (0,1)` and `c_theta>0` can hold for all Boolean spectra.

The second statement is a counterexample only to that proposed bridge, **not** to FEI. It redirects the projection programme toward influence-scale or genuinely multiscale payment.

## 1. Exact Boolean family

Fix `n>=2`, put `N=2^n`, and let

`f_n(x)=-1` at one cube vertex `x_0` and `f_n(x)=+1` at every other vertex.

By translating the cube we may take `x_0=0` without changing squared Fourier masses. With normalized Walsh coefficients,

`hat f(empty)=1-2/N`,

and for every nonempty `S`,

`hat f(S)=-2/N`.

Hence the spectral law `mu(S)=hat f(S)^2` is

`mu(empty)=(1-2/N)^2`,

`mu(S)=4/N^2` for every `S != empty`.                                      (1)

For every coordinate `i`,

`j_i=P_mu(i in S)=2/N`,

so

`I(f_n)=sum_i j_i = 2n/N`.                                                (2)

This is the same genuine Boolean family on which B12's Palm-prefix mean-depth constant `1/4` is sharp; here it is used for block/correlation and projection geometry instead.

## 2. Simultaneous sharpness of every two-sided block-parity cap

For a nonempty block `J subseteq [n]`, write

`c_J = E_mu (-1)^{|S cap J|}`.

The standard Fourier autocorrelation identity gives

`c_J = E_x f_n(x) f_n(x^J)`.

Because `J` is nonempty, exactly the two points `x_0` and `x_0^J` contribute `-1`; all other points contribute `+1`. Therefore

`c_J = 1 - 4/N`                                                       (3)

for **every nonempty block J**, independently of `|J|`.

Let

`alpha_J=P_mu(|S cap J| even)=(1+c_J)/2`.

Then

`alpha_J=1-2/N`.                                                       (4)

The earlier B13 Boolean block-parity lemma gives the two raw atom caps

- if `|S cap J|` is even, `mu(S) <= alpha_J^2`;
- if `|S cap J|` is odd, `mu(S) <= (1-alpha_J)^2`.

For the present family, (1) and (4) yield

`mu(empty)=(1-2/N)^2=alpha_J^2`,                                      (5)

while **every** atom `T` with `|T cap J|` odd satisfies

`mu(T)=4/N^2=(1-alpha_J)^2`.                                          (6)

Thus for every nonempty `J`, both sides of the two-sided block lemma are sharp, and this happens simultaneously on one Boolean spectrum. Equivalently, the conditional caps are saturated:

`P(S=empty | parity_J even)=alpha_J`,

and for every odd atom `T`,

`P(S=T | parity_J odd)=1-alpha_J`.

### Consequence

There is no universal improvement replacing either cap by a strictly smaller multiplicative constant, even if one assumes the full collection of such one-block inequalities at once. Any successful FEI argument built from these constraints must exploit **compatibility between different blocks**, overlap/multiscale allocation, or additional signed information; sharpening the one-block endpoint itself is impossible.

The matched-product comparison makes the missing compatibility visible. Since every marginal is `j_i=2/N`, the matched product law has parity moment

`d_J=(1-2j_i)^{|J|}=(1-4/N)^{|J|}`,                                  (7)

whereas the actual Boolean spectrum has `c_J=1-4/N` for every nonempty `J`. Thus for `|J|>1` the dependence is genuinely collective:

`c_J-d_J=(1-4/N)-(1-4/N)^{|J|}>0`.                                  (8)

The same rare physical defect forces a common block correlation across all scales.

## 3. Exact projection profile

Let `B subseteq [n]` have size `q>=1`, and let `mu_B` be the projection of the spectral inclusion vector to `B`. Symmetry makes the projected law depend only on `q`.

For every nonempty `R subseteq B`, exactly `2^{n-q}` spectral sets project to `R`, all nonempty, so by (1)

`mu_B(R)=2^{n-q} * 4/N^2 = 4/(N 2^q)`.                               (9)

For the empty projected atom,

`mu_B(empty)=1-4/N+4/(N 2^q)`.                                      (10)

Hence the projected nonempty mass is

`V_q = (4/N)(1-2^{-q})`,                                              (11)

and its entropy is exactly

`H_q = h_2(V_q) + V_q log_2(2^q-1)`.                                 (12)

Every projected coordinate still has marginal `2/N`, so its total correlation is

`T_q = q h_2(2/N)-H_q`.                                               (13)

Because all `q`-coordinate projections are identical, B18's averaged profile satisfies

`bar T_q = T_q`.                                                       (14)

If `T=T_n`, B18's scaled projection credit is

`K_q = T - (n/q) bar T_q`.

The marginal-entropy terms cancel exactly, leaving the especially simple identity

`boxed: K_q = (n/q) H_q - H_n`.                                      (15)

This is an exact Boolean formula, not an asymptotic heuristic.

## 4. Refutation of a fixed-fraction macroscopic projection-credit bridge

Take a sequence `q=q_n` with `q/n -> theta` for fixed `theta in (0,1)`. Since `N=2^n` and `V_q=4/N+o(1/N)`, the elementary small-mass expansion gives

`H_q = (4/N)(n+q-2+log_2 e) + o(n/N)`,                               (16)

uniformly for `q/n` bounded away from zero. In particular,

`T/I = n-5+log_2 e+o(1)`,                                             (17)

while (15) gives

`K_q/I -> 2(theta^{-1}-1)`.                                           (18)

Therefore

`K_q/T -> 0`.                                                         (19)

At the especially natural half scale `q=n/2`,

`K_{n/2}/I -> 2`,                                                     (20)

but

`T/I = n-5+log_2 e+o(1) -> infinity`.                                (21)

### Corollary: proposed bridge is false

For every fixed `theta in (0,1)` and every `c_theta>0`, there are genuine Boolean functions for which

`K_{floor(theta n)} < c_theta T`.

So the universal fixed-scale statement

`K_{floor(theta n)} >= c_theta T`

is false.

This does **not** kill the B18 projection/Han programme. The same family has a nonzero limiting **influence-scale** refund (18). What fails is demanding that one macroscopic projection capture a fixed fraction of the much larger total correlation. A viable argument must instead accumulate credits across scales, compare `K_q` directly to an influence/restriction toll, or use cross-block signed structure.

## 5. Why this family is a useful joint stress test

Three independently derived Boolean mechanisms become simultaneously sharp or near-extremal on the one-point defect:

1. **B13 block caps:** every nonempty block attains the even cap at the empty atom and the odd cap at every odd atom, Sections 2--3 above.
2. **B12 Palm prefix depth:** the latest B12 theorem records exact equality in its `1/4 log_2(1/j_i)` mean-prefix lower bound on this same family.
3. **B18 projection credit:** at fixed fractional scale, `K_q/I` stays bounded while `T/I` diverges linearly.

This combination is informative: very strong total spectral dependence can coexist with locally sharp Booleanity inequalities and only `O(I)` one-scale projection refund. Thus a universal proof needs a **global bookkeeping identity** that pays an influence-scale amount many times without double counting, rather than a stronger local endpoint.

The most promising next target for B13 is therefore a multiscale block profile. One concrete formulation is to seek a nonnegative measure `w(dq)` and a Boolean identity/inequality of the shape

`integral K_q d w(q) <= C I`

or, in the direction useful for paying a restriction toll,

`UNPAID <= C I + integral Phi_q(K_q, signed block correlations) d w(q)`,

where the one-point-defect family forces the weights to accumulate bounded `O(I)` credits over many scales rather than require a fixed fraction of `T` at one scale. Any candidate should be tested against products/tribes and the current Numaro-based lower-bound seed as well.

## 6. Executed exact checks

The attached standard-library checker directly constructs the Walsh spectrum of the one-point defect and verifies, for every `n=2,...,8`:

- all nonempty spectral atoms have mass `4/N^2`;
- every nonempty block has parity-even mass `1-2/N`;
- the raw even/odd block caps are saturated exactly as in (5)--(6);
- every projected atom for every nonempty coordinate block matches (9)--(10).

Exact rational counts:

- spectral-atom checks: **501**;
- nonempty-block parity checks: **501**;
- projection-atom checks: **9,830**;
- block-cap saturation equalities: **43,935**;
- total exact rational checks: **54,767**.

It also evaluates the exact entropy formulas at high decimal precision for `n=20,40,80,160`, `q=n/2`; `K_q/I` approaches `2` while `K_q/T` approaches zero, matching (18)--(20). Those decimal values are a self-check only; the theorem follows from the exact formulas and asymptotic expansion above.

## 7. Literature scope and classification

A fresh 2026 literature search located Potapov's September 18 plateaued/partially-bent FEI result and the May 2026 stopping-binary-tree/restriction work of González--MacManus--Pereyra. Neither search result is used as support for the theorem above, and **no novelty or publication-priority claim is made** from the search.

Classification:

- **PROVED:** exact one-point-defect spectrum (1)--(2).
- **PROVED:** simultaneous sharpness of the two-sided Boolean block-parity atom caps for every nonempty block (3)--(6).
- **PROVED:** exact projected law, projected entropy, total-correlation profile and scaled-credit identity (9)--(15).
- **PROVED:** for fixed fractional projection scale, `K_q/I -> 2(theta^{-1}-1)` while `K_q/T -> 0`; hence the fixed-fraction macroscopic projection-credit bridge is false.
- **SELF-CHECKED FINITELY:** 54,767 exact rational identities through `n=8`, plus high-precision asymptotic diagnostics.
- **OPEN:** a bounded multiscale/cross-block payment sufficient for full FEI.
- **OPEN:** full uniform-cube FEI.
