Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but authenticated runtime metadata does not establish GPT-6/maximum, so this artifact does not claim it.

# PROB10-08 artifact — polynomial localization and a subpolynomial doubled-time Green criterion for cutoff

Status: **PROVED auxiliary/reduction theorem / Salez Problem 2.3 remains OPEN / no new source graph class claimed / independent validation pending / worldwide novelty UNVERIFIED**.

This artifact concerns Justin Salez, arXiv:2508.21055, Problem 2.3, under the source's rate-one continuous-time simple-random-walk convention. It is not the posted Abelian Cayley/product-condition target.

## 1. Why this is a genuinely different recovery

The two immediately preceding PROB10-08 runs showed that a source-admissible affine Cayley expander can have polynomially large actual heat-kernel chi-square distance at the fastest tree/Ramanujan scale. Thus **L2 mixing at the TV scale is not a viable universal target**. The old R16/I0112 moving-weight-Poincare/AEP, synchronous-tensor, product-varentropy, Hecke/information-curvature, and tree-subcommutation routes are also already exhausted and are not restarted here.

The present route asks a weaker question: how large may the heat-kernel L2 excess be while cutoff is still forced? The answer below is: **any subpolynomial excess at the mixing scale is enough**. More importantly, failure of cutoff forces a very concrete obstruction: at a fixed TV mixing threshold, a positive amount of the heat-kernel mass must live on a polynomially small set. This is an actual likelihood/Green-function obstruction, not another near-uniform-L2 criterion.

The newest neighboring P26 route is also distinct. P26 controls NBRW shell collision and transfers it through specially constructed distance graphs. Here there is no shell graph and no transfer: the criterion concerns the **actual source walk** through its doubled-time on-diagonal heat kernel.

## 2. Setup

Let `(G_n)` be finite connected `d_n`-regular vertex-transitive graphs with

- `3 <= d_n <= D < infinity`,
- `n:=|V(G_n)| -> infinity`,
- `gamma_n:=1-lambda_2(P_n) >= gamma >0`,

where `P_n` is discrete simple random walk. Use Salez's rate-one continuous-time semigroup

`H_t = exp(t(P_n-I))`.

Fix `epsilon in (0,1/2)`, and write

`t_n := t_mix^(n)(epsilon)`,

`w_n(epsilon):=t_mix^(n)(epsilon)-t_mix^(n)(1-epsilon)`.

By vertex transitivity all one-point heat-kernel statistics below are independent of the root; fix `o_n` and set

`mu_n(y):=H_{t_n}(o_n,y)`,

`Z_n(y):=n mu_n(y)`.

When `Y_n~mu_n`, `log Z_n(Y_n)` is the information content relative to uniform stationarity, and its variance is the varentropy at time `t_n`.

Define the doubled-time return-density exponent

`R_n(epsilon):= n H_{2t_n}(o_n,o_n)`,

`rho_n(epsilon):= log R_n(epsilon)/log n`.

Since the chain is reversible and transitive,

`R_n = n sum_y mu_n(y)^2 = E_{mu_n}[Z_n] >= 1`.                 (2.1)

## 3. Uniform polynomial range of the likelihood at the mixing scale

We first record a self-contained bound needed only to turn tail estimates into a variance estimate.

### Lemma 3.1

For fixed `D,gamma,epsilon`, there is `K<infinity` such that, for all sufficiently large `n` and every `y`,

`|log Z_n(y)| <= K log n`.                                      (3.1)

### Proof

First, `t_n=Theta(log n)` with constants depending only on `D,gamma,epsilon`.

For the upper bound, the spectral gap gives

`d_TV(t) <= (1/2) sqrt(n-1) exp(-gamma_n t)`,

so, for large `n`,

`t_n <= gamma^{-1} log n`.                                     (3.2)

For the lower bound, let

`c_D:=1/(8 log(D-1))`.

At time `c_D log n`, the number of jumps is Poisson with mean `c_D log n` and is at most `2c_D log n` with probability tending to one. A degree-`D` ball of that radius has at most

`C_D (D-1)^(2c_D log n)=C_D n^(1/4)`

vertices. Hence the walk has mass `1-o(1)` on a set of stationary mass `O(n^(-3/4))`, so its TV distance tends to one. Therefore

`t_n >= c_D log n`                                             (3.3)

for every fixed `epsilon<1` and all large `n`.

Next, expansion gives diameter `O(log n)`. Cheeger's inequality yields conductance at least `gamma/2`. Thus every set `S` of size at most `n/2` has at least `(gamma/2)|S|` new boundary vertices (each outside vertex accounts for at most `d_n` crossing edges). Consequently balls grow by a factor at least `1+gamma/2` until they exceed `n/2`, and hence

`diam(G_n) <= C_0(gamma) log n`.                               (3.4)

Fix `y`, let `r=dist(o_n,y)`, and choose a geodesic of length `r`. The continuous-time Poisson expansion contains the event of exactly `r` jumps following this geodesic, so

`H_{t_n}(o_n,y) >= exp(-t_n) t_n^r/(r! d_n^r)`

`                  >= exp(-t_n) (t_n/(d_n r))^r`,              (3.5)

with the `r=0` case even simpler. By (3.2)--(3.4), both `t_n` and `r` are `O(log n)` and `r/t_n` is uniformly bounded. Thus (3.5) is at least `n^{-K_1}` for a constant `K_1(D,gamma,epsilon)`. Since trivially `H_t<=1`,

`n^{1-K_1} <= Z_n(y) <= n`.

Enlarging the constant gives (3.1). `QED`

Remark: Salez's spatial heat-kernel regularity lemma gives a comparable compact-range statement. The direct proof above keeps the present reduction self-contained in the regular graph setting.

## 4. The polynomial-localization estimate

For `a>0`, define the high-likelihood set

`B_n(a):={y: Z_n(y) >= n^a}`

and its own-law mass

`L_n(a):=mu_n(B_n(a))`.

### Lemma 4.1 — positive and negative likelihood tails

For every fixed `a>0`,

`L_n(a) <= n^(rho_n-a)`,                                       (4.1)

and

`P_{Y_n~mu_n}(Z_n(Y_n) <= n^{-a}) <= n^{-a}`.                  (4.2)

### Proof

By (2.1), Markov's inequality under `mu_n` gives

`P_mu(Z_n>=n^a) <= E_mu[Z_n]/n^a = R_n/n^a = n^(rho_n-a)`,

which is (4.1).

For (4.2), use the exact identity

`E_mu[Z_n^{-1}]`

` = sum_y mu_n(y)/(n mu_n(y))`

` = 1`,                                                        (4.3)

where positivity of the continuous-time heat kernel follows from connectedness. Markov applied to `Z_n^{-1}` gives (4.2). `QED`

Thus **negative polynomial likelihood tails are automatically negligible for every finite chain**; only the positive tail can obstruct information concentration.

## 5. Quantitative varentropy and window bound from the Green exponent

Let

`W_n:=log Z_n(Y_n)/log n`.

By Lemma 3.1, `|W_n|<=K`. For any `a in (0,1)`, split according to `|W_n|<=a`, `W_n>a`, and `W_n<-a`. Lemma 4.1 gives

`Var(W_n) <= E[W_n^2]`

` <= a^2 + K^2 ( n^(rho_n-a) + n^{-a} )`.                     (5.1)

Hence the varentropy satisfies

`V_KL^(n)(t_n)`

` <= (log n)^2 [ a^2 + K^2(n^(rho_n-a)+n^{-a}) ]`.             (5.2)

Salez's general varentropy window theorem gives, for fixed `epsilon`,

`w_n(epsilon) <= C_epsilon gamma_n^{-1}`

`                 * (1+sqrt(V_KL^(n)(t_n)))`.                  (5.3)

Combining (3.3), (5.2), `gamma_n>=gamma`, and (5.3) proves the following theorem.

### Theorem 5.1 — quantitative doubled-time Green criterion

There is `C=C(D,gamma,epsilon)<infinity` such that for every fixed `a in (0,1)` and all large `n`,

`w_n(epsilon)/t_n`

` <= C [ 1/log n + a + sqrt(n^(rho_n-a)+n^{-a}) ].              (5.4)

In particular, if

`rho_n(epsilon)=o(1)`, equivalently

`n H_{2t_mix(epsilon)}(o_n,o_n)=n^{o(1)}`,                     (5.5)

then choose

`a_n=rho_n+4 log log n/log n`.

For large `n`, `a_n<1`, and (5.4) gives

`w_n(epsilon)/t_n`

` = O_{D,gamma,epsilon}(rho_n + log log n/log n).               (5.6)

Consequently, if (5.5) holds for every fixed `epsilon in (0,1/2)`, the sequence exhibits TV cutoff.

This is strictly weaker than demanding L2 mixing at `t_n`: since

`chi^2(H_{t_n}(o_n,.),pi)=R_n-1`,

condition (5.5) allows `chi^2` to diverge arbitrarily fast subject only to subpolynomial growth.

## 6. Equivalent positive-tail criterion and the exact obstruction to non-cutoff

The same proof gives a criterion that no longer mentions `R_n`.

### Theorem 6.1 — polynomial-delocalization criterion

Suppose that for every fixed `epsilon in (0,1/2)` and every fixed `a>0`,

`L_n(a)=P_{Y~H_{t_mix(epsilon)}(o,.)}`

`       [ n H_{t_mix(epsilon)}(o,Y) >= n^a ] -> 0`.             (6.1)

Then `(G_n)` exhibits TV cutoff.

### Proof

For fixed `a`, Lemma 4.2's negative-tail estimate and (6.1), together with the uniform bound (3.1), imply

`limsup Var(W_n) <= a^2`.

Let `a downarrow 0`. Hence

`V_KL^(n)(t_n)=o(log^2 n)`

for every fixed `epsilon`. Since `gamma_n t_n >= gamma c_D log n`, Salez's varentropy criterion gives cutoff. Equivalently, one may use (5.3) directly. `QED`

The contrapositive is the useful obstruction.

### Corollary 6.2 — macroscopic polynomial localization is necessary for a counterexample

If a bounded-degree vertex-transitive expander sequence fails cutoff, then there exist fixed constants

`epsilon in (0,1/2)`, `a>0`, `b>0`,

and a subsequence such that, at `t_n=t_mix(epsilon)`, the set

`B_n={y:nH_{t_n}(o_n,y)>=n^a}`                               (6.2)

satisfies

`H_{t_n}(o_n,B_n)>=b`,                                         (6.3)

while

`|B_n| <= n^(1-a)`.                                            (6.4)

Indeed, non-cutoff contradicts the conclusion of Theorem 6.1, so (6.1) must fail for some `epsilon,a`; pass to a subsequence on which `L_n(a)>=b`. Since every point of `B_n` has `mu_n(y)>=n^{a-1}` and total mass is at most one, (6.4) follows.

Thus a counterexample cannot be caused merely by a rare L2 spike. It must carry a **positive amount of its own heat-kernel mass on a polynomially sublinear set at a fixed TV mixing threshold**.

## 7. Green-function form of the obstruction

Corollary 6.2 automatically produces a polynomial doubled-time return spike. By Cauchy--Schwarz,

`H_{2t_n}(o_n,o_n)`

` = sum_y H_{t_n}(o_n,y)^2`

` >= sum_{y in B_n} H_{t_n}(o_n,y)^2`

` >= H_{t_n}(o_n,B_n)^2/|B_n|`

` >= b^2 n^{a-1}`.                                             (7.1)

Therefore

`R_n(epsilon)=nH_{2t_n}(o_n,o_n) >= b^2 n^a`.                  (7.2)

This proves an exact source-level obstruction:

> **Any counterexample to Salez Problem 2.3 must have polynomial on-diagonal heat-kernel excess at twice some fixed-threshold mixing time.**

The converse is false: the preceding affine stress-test already warns that polynomial chi-square/return excess can be carried by vanishing own-law mass. The new point is that **non-cutoff requires the stronger macroscopic localization (6.3), not merely (7.2)**.

## 8. Three approaches compared this run

### A. Likelihood-tail truncation + varentropy — SUCCESS

The key observation is the pair of exact moments under the heat-kernel law:

`E_mu Z = nH_{2t}(o,o)`,

`E_mu Z^{-1}=1`.

They control the positive and negative polynomial tails separately. Combined with the compact `O(log n)` information range at mixing time, this turns a weak subpolynomial Green estimate into the quantitative window bound (5.4). This is the retained theorem.

### B. Try to prove the Green estimate from the ordinary spectral gap — FAILS, exact reason isolated

Spectral expansion alone yields only

`R_n(t)=1+sum_{i>=2} exp(-2(1-lambda_i)t)`

` <= 1+(n-1)exp(-2 gamma t)`.                                  (8.1)

At `t=Theta(log n)` this can still be a fixed positive power of `n`; it does not imply `rho_n=o(1)`. The affine source-admissible family from the previous run makes this failure concrete: its actual heat kernel can have polynomial chi-square excess at the tree/Ramanujan benchmark. Therefore another spectral-gap-only trace estimate cannot close the source.

### C. Try to rule out the localized set by ordinary edge expansion/coarea — FAILS, exact reason isolated

If (6.2)--(6.4) occurs, the underlying expander gives `Omega(|B_n|)` boundary edges. But the instantaneous heat flux through a boundary edge is proportional to a **difference of heat-kernel densities**, not to the number of boundary edges. A superlevel set can have many boundary edges across which the density gap is arbitrarily small. Standard dyadic/coarea conversion recovers only the usual logarithmic-scale Sobolev loss (`Theta(1/log n)` in the worst bounded-degree expander setting), which is not enough by itself to make a `Theta(log n)` mixing window negligible.

So the source-level missing statement is now more precise than “prove AEP”: one must prevent **macroscopic polynomial localization** using transitivity, or prove the weaker Green estimate `R_n=n^{o(1)}` by a method stronger than the ordinary spectral gap. This is exactly the point at which a genuinely transitivity-sensitive Green-function estimate could settle the problem.

## 9. Relation to Altschuler's LRE proof

Altschuler (arXiv:2609.14945v1, submitted 14 September 2026) uses long-range expansion to obtain near-maximal NBRW endpoint Shannon entropy and then invokes entropy cleanup. A fresh bounded check this run found the arXiv record still at v1 and no correction/erratum.

The present theorem replaces that strong endpoint-entropy input by a much weaker **actual heat-kernel Green requirement at the mixing scale**. It does not prove that vertex transitivity plus spectral expansion implies this requirement. Therefore it is a mechanism reduction/obstruction, not a new solution of Altschuler's missing implication and not a source closure.

## 10. Relation to the earlier affine obstruction

The previous PROB10-08 run proved that, on the Haiman--Schildkraut--Zhang--Zhao affine Cayley family, actual heat-kernel chi-square distance is polynomially large at the fastest tree/Ramanujan benchmark. That showed near-L2 mixing is too strong as a universal target.

Theorem 5.1 sharpens the lesson rather than contradicting it:

- `R_n=O(1)` is unnecessary;
- even `R_n -> infinity` is harmless if `R_n=n^{o(1)}`;
- polynomial `R_n` is still not evidence of non-cutoff by itself;
- a genuine counterexample must additionally have positive own-law mass on the polynomially small high-density set.

This separates the “rare spectral spike” phenomenon from the only localization pattern that can actually obstruct cutoff under the varentropy mechanism.

## 11. Source metric and validation status

**Source before:** Salez Problem 2.3 OPEN; historical R16 `W_exp=1/2 provisional`; two consecutive newest own runs had no TV source-metric movement.

**Source after:** still **OPEN**; `W_exp=1/2 provisional` unchanged. No new complete source-admissible graph class is claimed, so there is no source-metric movement.

**Mechanism progress:** proved quantitative window estimate (5.4), the subpolynomial doubled-time Green sufficient condition (5.5)--(5.6), and the necessary macroscopic polynomial-localization obstruction (6.2)--(7.2) for any counterexample.

This is the required different-method obstruction after the repeated unchanged source metric. It does not continue sharpening the preceding L2 constants.

No finite computation is part of the theorem. No checker or mixing plot was run. The checks in this artifact are exact analytic identities/inequalities; they are self-checks, not independent audits.

The preserved R16 successor handoff remains at

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`.

The canonical claim remains

`operations/claims/I0112.md`.

The remaining full-scope gap is now concrete: derive either (6.1) or the weaker `rho_n(epsilon)=o(1)` from **vertex transitivity plus a uniform spectral gap alone**, without reintroducing long-range expansion, Sarnak--Xue density, near-Ramanujan spectrum, or one of the already-owned shell-transfer hypotheses.
