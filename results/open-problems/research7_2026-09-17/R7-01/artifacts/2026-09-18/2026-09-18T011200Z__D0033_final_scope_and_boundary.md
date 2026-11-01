Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed; `C_phi_rhostar: 1 -> 1` (**NO MOVEMENT**); methods **B3 / B15 / B26**.

# D0033 final research note: standard-Borel path tensorization, a symmetry-broken stress family, and the exact meaning of the `kappa=1/2` boundary

Target: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, *Probability Surveys* 2 (2005), 107–144, Question 5, Section 3, printed p.119 / source-PDF p.13:

> If a given Markov chain is phi-mixing, does it follow that it is rho-star-mixing?

This note is cumulative. It assumes the preceding R7-01 proof of the robust one-step coefficient

\[
\kappa(n)\le 2\sqrt{2\phi(n)}
\]

and Bradley's Theorem 3.3(6), which says that one strict inequality `rho*(n0)<1` implies exponential rho-star mixing. The purpose here is to close the remaining proof-interface questions, deliberately stress the nonstationary/nonreversible scope, and determine whether the abstract `kappa<1/2` threshold is a genuine Markov obstruction.

The fixed source metric was already `1`; none of the results below changes that metric.

---

## 1. Primary-source scope rechecked

Bradley's Section 3.1 explicitly begins with a **not necessarily stationary** Markov chain and states the one-time reduction of the ordinary dependence coefficients. Theorem 3.3 is likewise stated for a not-necessarily-stationary Markov chain. Its part (6) says that if `rho*(n)<1` for one lag, then `rho*(n)` decays at least exponentially. Question 5 follows immediately and does not reimpose stationarity.

For convenience Bradley takes the state space to be `R`, which is standard Borel. The argument below is naturally stated for any standard-Borel state space, so it contains Bradley's source scope.

Primary source checked 2026-09-18:

- arXiv:math/0511078;
- DOI 10.1214/154957805100000104;
- Section 3.1, Theorem 3.3(6), Question 5.

The external tensorization input was also rechecked in Remi Peyre, *Tensorizing maximal correlations*, arXiv:1004.1602v2 (2010), Theorem 3.3.1 and Section 3.4(a), “Minimal Hypotheses.” The latter permits exactly the prefix sigma-field used below.

---

# 2. B3 — stronger theorem: the finite interlacing reduction works on every standard-Borel Markov path

We isolate the exact theorem used by the Bradley-Q5 proof.

## Definition 2.1 — robust channel maximal correlation

Let `(E,E)` be standard Borel and let `(X_k)_{k in Z}` be a not-necessarily-stationary Markov chain. For `s<t`, choose a regular transition kernel

\[
K_{s,t}(x,\cdot)=\Pr(X_t\in\cdot\mid X_s=x),
\]

and let `mu_s,mu_t` denote the one-time laws.

For each pair `(s,t)` choose a full-`mu_s` Borel set `A_{s,t}` on which

\[
\|K_{s,t}(x,\cdot)-K_{s,t}(x',\cdot)\|_{\rm TV}
\le 2\phi(t-s)
\quad (x,x'\in A_{s,t}).
\tag{2.1}
\]

The preceding R7-01 row lemma proves that such a common set exists: first prove the eventwise inequality for a countable generating algebra, discard the union of the corresponding null sets, and then apply the monotone-class theorem.

Define

\[
\kappa(s,t)
:=
\sup_{\lambda:\lambda(A_{s,t})=1}
\rho(U,V),
\tag{2.2}
\]

where `U~lambda` and `V|U=x ~ K_{s,t}(x,.)`, and put

\[
\kappa(n):=\sup_{t-s\ge n}\kappa(s,t).
\tag{2.3}
\]

Because all output laws obtained from input events are mixtures of a row family of TV diameter at most `2 phi(t-s)`, Bradley's two-sigma-field comparison gives

\[
\boxed{
\kappa(n)\le \min\{1,2\sqrt{2\phi(n)}\}.
}
\tag{2.4}
\]

No stationarity or time homogeneity is used.

## Theorem 2.2 — standard-Borel alternating-block theorem

Let `S,T` be finite disjoint subsets of `Z` satisfying

\[
\operatorname{dist}(S,T):=\min_{s\in S,t\in T}|s-t|\ge n.
\]

Then

\[
\boxed{
\rho\bigl(\sigma(X_s:s\in S),\sigma(X_t:t\in T)\bigr)
\le 2\kappa(n).
}
\tag{2.5}
\]

More precisely, if the selected coordinates are merged chronologically into `m` maximal monochromatic blocks, then the right side can be replaced by

\[
2\kappa(n)\cos\frac{\pi}{m+1}<2\kappa(n).
\tag{2.6}
\]

### Proof

Order the selected times in `S union T`. Merge consecutive selected times of the same colour into maximal blocks

\[
B_1<B_2<\cdots <B_m.
\]

The colours alternate. Enumerate the `S`-blocks as `U_1,...,U_r` in chronological order and the `T`-blocks as `V_1,...,V_q`. Here a block denotes the random vector of the selected coordinates it contains.

Peyre's minimal-prefix sigma-field for the pair `(U_i,V_j)` is

\[
\mathcal H_{ij}
=
\sigma(U_{i'}:i'<i,\ V_{j'}:j'<j).
\tag{2.7}
\]

We claim that the conditional/subjective maximal-correlation matrix has a nonzero entry only when `U_i` and `V_j` are adjacent in the chronological block path.

**Nonadjacent blocks.** Suppose for definiteness that `U_i` lies chronologically before `V_j` and they are not adjacent. Since colours alternate, at least one `T`-block strictly between them precedes `V_j`; hence that intervening block belongs to `H_ij`. Choose any state coordinate `X_r` in the last such intervening block. All additional variables in `H_ij` lie at or before this separator. By the Markov property, conditional on `X_r`, the sigma-field generated by the path up to `r` is independent of the sigma-field generated by the path after `r`. Conditioning additionally on variables measurable on the left/separator side does not destroy that factorization. Therefore `U_i` and `V_j` are conditionally independent given `H_ij`, so their subjective maximal correlation is zero. The case `V_j<U_i` is symmetric.

**Adjacent blocks.** Suppose `U_i` is immediately before `V_j`. Let `s` be the last selected time in `U_i` and `t` the first selected time in `V_j`. Since the colours differ and `dist(S,T)>=n`,

\[
t-s\ge n.
\tag{2.8}
\]

Every random variable in `H_ij` occurs strictly before the earlier target block. Conditional on `H_ij`, the Markov transition from `X_s` to `X_t` is therefore still `K_{s,t}`; only the input distribution of `X_s` has changed. Because `A_{s,t}` has full `mu_s` measure,

\[
\Pr(X_s\in A_{s,t}\mid\mathcal H_{ij})=1
\quad\text{a.s.}
\tag{2.9}
\]

The Markov data-processing chain is

\[
U_i \longrightarrow X_s \longrightarrow X_t \longrightarrow V_j
\quad\text{conditional on }\mathcal H_{ij}.
\tag{2.10}
\]

Maximal correlation obeys data processing, hence the subjective correlation of `(U_i,V_j)` is at most `kappa(s,t)<=kappa(n)`.

Thus Peyre's minimal-prefix matrix is supported on the edges of the alternating block path and every nonzero weight is at most `kappa(n)`. The nonnegative weighted path matrix is entrywise dominated by `kappa(n)` times the unweighted path adjacency. Its bipartite off-diagonal block has operator norm at most

\[
2\kappa(n)\cos\frac{\pi}{m+1}.
\tag{2.11}
\]

Peyre Theorem 3.3.1 now yields (2.6), and (2.5) follows. QED.

## Corollary 2.3 — the one-lag Bradley-Q5 criterion

If

\[
\phi(n_0)<\frac1{32},
\]

then by (2.4), `kappa(n0)<1/2`; hence every finite admissible interlacing has maximal correlation at most

\[
4\sqrt{2\phi(n_0)}<1.
\]

Approximation of `L^2` functions by finite-coordinate conditional expectations extends the same bound to countable index sets. Therefore

\[
\rho^*(n_0)<1.
\]

Bradley Theorem 3.3(6) gives exponential rho-star mixing. Since phi-mixing means `phi(n)->0`, every phi-mixing Markov chain satisfies the premise for some `n0`.

The proof is therefore valid in Bradley's full not-necessarily-stationary real-state scope, and in fact on arbitrary standard-Borel state spaces.

---

# 3. B15 — break symmetry on purpose: a time-inhomogeneous, nonreversible exact stress family

A hidden concern in several early D0033 attempts was that the proof might secretly use stationarity, a common invariant transition kernel, or reversibility. The following exact family removes all three conveniences.

Let the state space be `Z/3Z`. Choose

\[
a,b,c>0,\qquad a+b+c=1,\qquad b\ne c.
\]

Let `C` be the cyclic shift. Define two stochastic matrices

\[
K^+=aI+bC+cC^2,
\qquad
K^-=aI+cC+bC^2,
\tag{3.1}
\]

and use `K^+` at even times and `K^-` at odd times. Take the one-time marginal to be uniform at every time; this is consistent because both matrices are doubly stochastic.

### 3.1 It is genuinely outside the symmetric toy regime

Unless `b=c`, each one-step kernel is nonreversible with respect to the uniform law, since for neighbouring states

\[
K^+(i,i+1)=b\ne c=K^+(i+1,i).
\]

The path law is not strictly stationary when `K^+ != K^-`, because a one-step time shift swaps the two transition laws.

### 3.2 Exact mixing control

Put

\[
\eta:=\min\{a,b,c\}>0.
\]

Every entry of either one-step matrix is at least `eta`. Therefore, with `u` the uniform law,

\[
K^\pm(i,\cdot)\ge 3\eta\,u(\cdot)
\tag{3.2}
\]

as measures. The Dobrushin contraction coefficient of each step is at most `1-3 eta`. Consequently any two rows of an `n`-step transition matrix have total-variation distance at most

\[
(1-3\eta)^n.
\tag{3.3}
\]

In particular the chain is phi-mixing exponentially fast.

There is also an independent source-level rho-star check. Because both one-time marginals are uniform, the likelihood ratio of a one-step atom is

\[
\frac{\Pr(X_k=i,X_{k+1}=j)}{\Pr(X_k=i)\Pr(X_{k+1}=j)}
=3K_k(i,j)\ge 3\eta.
\]

Any event-event likelihood ratio is a weighted average of these atomic ratios, so

\[
\psi'(1)\ge 3\eta>0.
\tag{3.4}
\]

Bradley Theorem 3.3(7) independently implies rho-star mixing.

Thus a genuinely time-inhomogeneous and one-step-nonreversible family lies in the source's broad scope and behaves exactly as the R7-01 proof predicts. No stationarity, reversibility, or common-kernel step was used in Theorem 2.2.

---

# 4. B26 — hunt the sporadic boundary: `kappa=1/2` is a tensorization boundary, not a Markov boundary

The previous run found that the abstract alternating-path norm approaches `2 kappa`; hence the generic path argument needs `kappa<1/2` to produce a strict uniform contraction. Is equality a genuine obstruction for Markov chains?

No.

## Proposition 4.1 — exact boundary example

For `0<r<1`, let `(X_k)` be the stationary binary symmetric Markov chain on `{-1,+1}` with

\[
\Pr(X_{k+1}=y\mid X_k=x)=\frac{1+rxy}{2}.
\tag{4.1}
\]

Let `kappa_r(1)` be the robust one-step HGR coefficient obtained by allowing an arbitrary input law on `X_k`. Then

\[
\boxed{\kappa_r(1)=r.}
\tag{4.2}
\]

In particular, at `r=1/2`,

\[
\kappa_{1/2}(1)=\frac12,
\]

yet the chain is rho-star mixing.

### Proof of (4.2)

Let the arbitrary input law have

\[
m=\mathbb E X\in[-1,1].
\]

Because `X` and `Y` are binary, their centered square-integrable function spaces modulo constants are one-dimensional, so maximal correlation is just the absolute ordinary correlation. From (4.1),

\[
\mathbb E[Y\mid X]=rX.
\]

Hence

\[
\mathbb EY=rm,
\qquad
\mathbb E[XY]=r,
\]

and therefore

\[
\operatorname{Cov}(X,Y)=r(1-m^2),
\]

\[
\operatorname{Var}(X)=1-m^2,
\qquad
\operatorname{Var}(Y)=1-r^2m^2.
\]

For `|m|<1`,

\[
\rho(X,Y)
=
 r\sqrt{\frac{1-m^2}{1-r^2m^2}}.
\tag{4.3}
\]

Writing `z=m^2`, the squared factor `(1-z)/(1-r^2 z)` has derivative

\[
\frac{r^2-1}{(1-r^2z)^2}<0.
\]

Thus (4.3) is maximized at `m=0`, where it equals `r`. Degenerate inputs give correlation zero by convention and do not change the supremum. This proves (4.2).

At `r=1/2`, the chain has strictly positive transition probabilities, so it is a finite-state irreducible aperiodic stationary Markov chain. Bradley Theorem 3.1 states that every such chain is rho-star mixing. Therefore the source-valid Markov process is rho-star mixing even though its robust local coefficient lies exactly on the abstract path threshold. QED.

## Consequence

The number `1/2` is **not** a hidden necessary condition for rho-star mixing of Markov chains. It is only the place where the fully abstract path-norm tensorization ceases to give a uniform strict inequality. Markov compatibility can do better.

This matters strategically: trying to improve the Bradley-Q5 proof by squeezing the path norm at `kappa=1/2` is unnecessary for the source question and cannot be justified solely from the abstract minimal-prefix matrix. The source proof only needs eventual `kappa(n)<1/2`, which phi-mixing already supplies.

---

# 5. Dated literature check and honest status

Fresh bounded searches on 2026-09-18 used:

- the exact wording of Bradley Question 5;
- `phi-mixing rho-star Markov chain Bradley`;
- `interlaced maximal correlation Markov phi mixing`;
- later Bradley Markov-chain mixing work;
- Peyre maximal-correlation tensorization and citing/follow-up material.

The searches recovered Bradley's 2005 source, his earlier rho-mixing/not-rho-star example, Peyre's 2010 tensorization work, and later special-class/copula mixing papers. They did **not** locate a paper explicitly announcing a full solution of Bradley Question 5 in the full source scope. This is bounded negative evidence only. It does not certify current openness, priority, or publication novelty.

Repository audit search also still found no actual independent full-proof D0033 audit. Required closure evidence therefore remains:

- P26: `0/1`;
- distinct OTHER-track: `0/1`.

Mathematical label: **PROVED CANDIDATE**. Protocol/publication closure: **OPEN**.

---

# 6. Metric and retirement consequence

Frozen metric:

`C_phi_rhostar: 1 -> 1` — **NO MOVEMENT**.

Previous ordinary unchanged count: `5`.
Current ordinary unchanged count: `6`.

Under the owner protocol, D0033 is now retired from further ordinary R7-01 attacking work. This is a retirement because the fixed metric has remained unchanged for six ordinary runs, **not** a statement that the source is audit-complete or publication-closed. The proof candidate, source checks, paper package, exact self-checks, and all unresolved audit obligations must be preserved in an immutable handoff.