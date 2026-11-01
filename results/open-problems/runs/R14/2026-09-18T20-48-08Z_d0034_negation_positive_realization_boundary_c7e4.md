Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0034: `N_rep: 2 -> 2`; authoritative shared stagnation count remains UNKNOWN. Methods actually used: #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT.**

# R14 HARD OUTSIDE — D0034 negation test, positive-realization obstruction, and critical boundary

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **D0034 PARTIAL / source OPEN / active exclusive R14 claim.** The negative-margin spherical perceptron, H0017, D0036, and D0039 remain handed off and are not reopened.

## 1. Continuity, source, exclusions, ownership

I reread the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical ownership file `operations/claims/D0034.md`, the newest R14 report, and neighboring ownership/status reports. The controlling claim remains D0034 / Bradley 2005 Question 6, exclusively owned by R14 in the HARD OUTSIDE lane, with fixed candidate the Holroyd--Liggett stationary 1-dependent 4-coloring `X_HL`.

The fixed metric remains

`N_rep = number of hidden-state cardinality regimes still requiring exclusion for X_HL after the known finite-state impossibility theorem.`

The two surviving regimes are

1. countably infinite-state stationary Markov representations;
2. genuinely general / uncountable-state stationary Harris recurrent representations.

The previous R14 report corrected the attempted Harris-to-countable collapse: for a general `m`-step Nummelin minorization, original-time regenerative blocks can retain one-step dependence, so the earlier `2 -> 1` movement was unsupported. The certified entering value here is therefore `N_rep=2`.

Fresh bounded literature checks on 2026-09-18 recover:

- Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions* (Probability Surveys 2, 2005), Question 6: whether there exists a stationary `psi`-mixing, perhaps even 1-dependent, process that is not an instantaneous function of any stationary Harris recurrent Markov chain.
- Holroyd--Liggett, *Finitely Dependent Coloring* (Forum Math. Pi 4 (2016), arXiv:1403.2448): the 1-dependent 4-coloring exists; no stationary finitely dependent coloring is a function of a finite-state Markov chain; the countable-state version is posed as an open problem.
- Holroyd--Hutchcroft--Levy, *Mallows Permutations and Finite Dependence* (Ann. Probab. 48 (2020), arXiv:1706.09526): off the critical curve they construct finitely dependent colorings that are functions of countable-state Markov chains with exponential return tails. Their critical boundary contains `(k,q)=(1,4)`, and they explicitly treat the original 1-dependent 4-coloring as a boundary case rather than as one of their countable-Markov constructions.

The bounded search did **not** locate a later source-matching theorem deciding whether the Holroyd--Liggett 1-dependent 4-coloring is a countable-state Markov factor or resolving Bradley Question 6. This is negative dispatch evidence only, not a novelty certificate.

## 2. Method #2 — ATTACK THE NEGATION FIRST: try to build the hidden chain from the known color-renewal points

The most natural counter-route to our candidate is to exploit Holroyd--Liggett's exact fact that, for a fixed color `c`, the indicator process `1[X_i=c]` is a renewal process. If the full color excursions between consecutive `c`'s formed a finite-order Markov chain, then one could hope to use those excursions as a countable hidden state and thereby kill `X_HL` as a Bradley-Q6 candidate.

This route fails in a strong exact sense.

Fix colors `0` and `1`, condition on `X_0=0`, and let `W_1,W_2,...` be the successive finite nonzero-color words between consecutive occurrences of color `0` to the right. Let `w=(1)` denote the one-site excursion `0 1 0`.

### Proposition 2.1 — the observable excursion process has no finite Markov order

For every `r>=1`,

\[
\mathbb P(W_1=\cdots=W_r=w\mid X_0=0)
=\frac{2}{(2r+2)!}.
\]

Consequently `(W_j)` cannot be an `m`-step Markov chain for any finite `m`.

### Proof

Holroyd--Liggett define the 4-coloring cylinder law by

\[
\mathbb P(X_1\cdots X_n=x)=\frac{B(x)}{(n+1)!2^n},
\]

where `B(x)` is the number of proper buildings of the word `x`, and their deletion recursion is

\[
B(x)=\sum_{i=1}^n B(\widehat x_i)
\]

for a proper word.

For an alternating two-color word `a_n=0101...` of length `n`, deleting any internal symbol creates an equal adjacent pair, while deleting either endpoint leaves `a_{n-1}`. Hence

\[
B(a_n)=2B(a_{n-1}),\qquad B(a_1)=1,
\]

so `B(a_n)=2^{n-1}`. Therefore

\[
\mathbb P(X_1\cdots X_n=a_n)=\frac{1}{2(n+1)!}.
\]

The event `W_1=...=W_r=(1)` under the Palm condition `X_0=0` is precisely the alternating cylinder of length `2r+1` beginning and ending in `0`. Since `P(X_0=0)=1/4`,

\[
p_r:=\mathbb P(W_1=\cdots=W_r=(1)\mid X_0=0)
=4\frac{1}{2(2r+2)!}
=\frac{2}{(2r+2)!}.
\]

Thus

\[
\frac{p_{r+1}}{p_r}=\frac1{(2r+3)(2r+4)},
\]

which depends strictly on `r` and tends to zero. If `(W_j)` were `m`-step Markov, then after `r>=m` repeated copies of `w`, the conditional probability of one more `w` would depend only on the last `m` copies and hence would be constant in `r`, contradiction. `\square`

The exact checker records, for example,

\[
p_1=\frac1{12},\qquad p_2=\frac1{360},\qquad p_3=\frac1{20160},
\]

and already at first order

\[
p_3p_1=\frac1{241920}\ne \frac1{129600}=p_2^2.
\]

So the obvious observable-renewal construction is dead: any predictive hidden state must carry genuinely unbounded information across successive color-renewal blocks.

### A second negative check: the radius-one dependence is *not* enough

The preceding report found that, conditioned on `X_0=c`, for side colors `a,b != c`,

\[
Q_{ab}:=\mathbb P(X_{-1}=a,X_1=b\mid X_0=c)
=\begin{cases}
1/12,&a=b,\\
1/8,&a\ne b.
\end{cases}
\]

One might hope this finite table already obstructs a hidden-state mixture of conditionally independent past/future laws. It does not. The exact checker gives

\[
\det Q=\frac1{1728}>0,
\]

so ordinary rank is three, and there is an explicit three-component nonnegative product factorization. Put `K=3Q`; then every row of `K` is stochastic and

\[
Q_{ab}=\frac13\sum_{h=1}^3 \mathbf 1_{\{a=h\}}K_{hb}.
\]

Thus radius-one data admit a three-class latent explanation. Any countable-state obstruction has to be genuinely multiscale, not a finite 3-by-3 nonnegative-rank argument.

## 3. Method #18 — SAY IT IN ANOTHER LANGUAGE: countable hidden Markov becomes a positive-realization problem

Suppose, toward a countable-state representation, that `M` is a stationary irreducible positive recurrent Markov chain on a countable set `S`, with transition matrix `P`, invariant law `pi`, and deterministic output map `f:S->[4]` giving `X_HL` in distribution. Write

\[
D_c(s,s)=\mathbf 1_{\{f(s)=c\}}.
\]

Then every cylinder probability has the countable nonnegative realization

\[
\mathbb P(X_1\cdots X_n=x_1\cdots x_n)
=\pi D_{x_1}P D_{x_2}P\cdots P D_{x_n}\mathbf 1.
\]

Proper coloring forces `D_cPD_c=0` for every color `c`.

More importantly, the Markov property gives a cut decomposition. Fix a center color `c` and let `mu_c` denote the conditional law of the whole left/right pair

\[
(X_{(-\infty,-1]},X_{[1,\infty)})\mid X_0=c.
\]

Conditioning further on the hidden state `M_0=s in f^{-1}(c)` makes the past and future independent. Hence necessarily

\[
\boxed{
\mu_c=\sum_{s\in f^{-1}(c)} w_s\,\alpha_s\otimes\beta_s,
\qquad w_s>0,\quad \sum_s w_s=1,
}
\]

for probability laws `alpha_s` on left-infinite words and `beta_s` on right-infinite words.

This yields a concrete sufficient obstruction to the entire countable-state regime:

\[
\boxed{
\texttt{PRODUCT-MINORANT-HL: }
\mu_c\text{ contains no nonzero product component.}
}
\]

Equivalently, there do not exist probability laws `alpha,beta` and a finite constant `C` such that

\[
\alpha\otimes\beta\le C\mu_c
\]

on every cylinder rectangle. Indeed, any hidden state `s` would supply such a component with `C=1/w_s`.

This formulation is stronger than one-cut nonnegative rank and automatically respects all cylinder scales. It is also exact: proving `PRODUCT-MINORANT-HL` would eliminate the countable-state regime and move `N_rep:2 -> 1`.

### Exact multiscale evidence, but not yet the universal obstruction

For nested alternating cylinders one already sees ratios collapsing. Let the left and right blocks each be the length-`m` alternating word compatible with a center `c`. The two side blocks separately have probability `1/[2(m+1)!]`, while the concatenated alternating word through the center has probability `1/[2(2m+2)!]`. Relative to the product of the two side-cylinder probabilities and `P(X_0=c)=1/4`, the likelihood ratio is

\[
D_m
=\frac{8(m+1)!^2}{(2m+2)!}
=\frac{8}{\binom{2m+2}{m+1}}
\longrightarrow0.
\]

Thus no product component that keeps uniformly comparable mass on this particular nested alternating ray can survive. What is still missing is the quantifier swap needed for a theorem: an arbitrary product component might avoid this ray. One must prove that **every** nonzero `alpha\otimes beta` is forced onto some family of cylinder rectangles on which the corresponding `mu_c` likelihood ratio tends to zero.

That is now the sharpest metric-moving countable-state route on file.

## 4. Method #24 — FIND THE EXTREMAL OBJECT: the known countable-Markov family dies exactly at `(k,q)=(1,4)`

Holroyd--Hutchcroft--Levy provide a particularly informative deformation from the solved countable-state regime to our critical case. Their finite-dependence tuning equation is

\[
qt[k]_t=[2]_t[k+1]_t.
\]

For `k=1` this becomes

\[
qt=(1+t)^2,
\qquad
q=t+2+t^{-1},
\]

and therefore

\[
\boxed{q-4=\frac{(1-t)^2}{t}.}
\]

Their countable-Markov construction for the off-critical family uses an iid `u`-zero-weighted `t`-geometric code `L`, with

\[
u=\frac{q-1}{q-2},
\]

and the hidden state records, among other finite data, the nearest zeros

\[
f_k^+=\min\{i>0:L_i^k=0\},
\qquad
f_k^-=\max\{i\le0:L_i^k=0\}.
\]

The paper identifies the zero set of `L` with the bubble endpoints of the corresponding constraint graph. From the displayed zero-weighted geometric law,

\[
\delta(t):=\mathbb P(L_i=0)
=\frac{u}{u+t/(1-t)}.
\]

Substituting the `k=1` tuning relation gives exactly

\[
\boxed{
\delta(t)=\frac{1-t^3}{1+t}
=\frac{(1-t)(1+t+t^2)}{1+t}.
}
\]

Hence at the critical Holroyd--Liggett point `q=4`, one has `t=1` and

\[
\boxed{\delta(1)=0.}
\]

The finite bubble endpoints disappear. The very coordinates `f_k^\pm` used by this explicit countable Markov representation cease to be finite. This is a certified failure of the most natural deformation/negation route, not a proof that *no other* countable-state representation exists.

The critical divergence is quantitative. Since

\[
q-4=\frac{(1-t)^2}{t},
\]

as `q downarrow 4`, `1-t ~ sqrt(q-4)`, while

\[
\delta(t)\sim \frac32(1-t)\sim\frac32\sqrt{q-4}.
\]

Thus the mean bubble spacing diverges as

\[
\frac1{\delta(t)}\sim\frac{2}{3\sqrt{q-4}}.
\]

This makes the critical 4-coloring an actual extremal boundary of the known countable-state mechanism rather than merely an omitted parameter value.

## 5. What moved and what did not

The three attacks changed the research frontier but did **not** eliminate either fixed hidden-state regime.

- **#2 ATTACK THE NEGATION FIRST:** the obvious construction based on the known one-color renewal skeleton fails strongly: the full excursion-word process is not finite-order Markov. However this does not exclude a different countable hidden state.
- **#18 SAY IT IN ANOTHER LANGUAGE:** the countable-state problem is reduced to a precise infinite-cylinder positive-realization obstruction, `PRODUCT-MINORANT-HL`. The radius-one side-color table explicitly *does* have a three-component nonnegative product factorization, proving finite local rank cannot be the answer.
- **#24 FIND THE EXTREMAL OBJECT:** the HHL countable-Markov/Mallows family degenerates exactly at the 1-dependent 4-coloring: bubble endpoint density goes to zero as `~(3/2)sqrt(q-4)`, so its positive-recurrent finite-bubble state has no critical limit.

Therefore

\[
\boxed{N_{\rm rep}:2\to2.}
\]

D0034 remains **PARTIAL / OPEN**. The authoritative shared stagnation count remains `UNKNOWN`; I do not manufacture it from local chronology.

## 6. Exact checker

The finite algebraic claims above were checked with exact rational/symbolic arithmetic in

`artifacts/R14/2026-09-18T20-48-08Z_d0034_boundary_checker.py`

with archived output

`artifacts/R14/2026-09-18T20-48-08Z_d0034_boundary_checker.out`.

The output ends

`ALL_EXACT_CHECKS_PASS`.

The checker verifies the `3x3` side matrix determinant and factorization, the first repeated-excursion probabilities and first-order Markov failure, the `k=1` HHL tuning identity, and the critical endpoint-density algebra.

## 7. Remaining obligations and next methods

The countable-state regime now has one clean target:

\[
\boxed{
\texttt{PRODUCT-MINORANT-HL:}
\quad
\forall\alpha,\beta,\ C<\infty,
\quad
\alpha\otimes\beta\not\le C\mu_c.
}
\]

A proof eliminates every irreducible positive recurrent countable-state Markov representation. A construction of even one product minorant is not by itself a hidden Markov representation, but would refute this obstruction route and force a new method.

Only after the countable regime moves should the distinct general-Harris/Nummelin one-dependent-block regime be attacked again; the previous `m`-step collapse remains invalid.

The next nonrepeating Section-B triple is:

- **#3 PROVE SOMETHING STRONGER:** try to show every nonzero product law on the two one-sided word spaces has cylinder rectangles whose `mu_c` likelihood ratio tends to zero exponentially.
- **#15 BREAK THE SYMMETRY ON PURPOSE:** fix a definite ordered side-color pair and use the exact building recursion in that sector instead of averaging over `S_4`; the local rank-three factorization shows symmetry-averaged finite windows are too permissive.
- **#27 SWAP THE QUANTIFIERS:** instead of testing proposed hidden states one at a time, prove a universal cylinder-selection lemma: for every pair `(alpha,beta)` there exists a nested pair of words `(u_m,v_m)` with positive product mass but `mu_c([u_m]\times[v_m])/(alpha[u_m]beta[v_m]) -> 0`.

Another local cylinder identity alone will not count as metric movement.

## 8. Model / scheduler-control status

The exposed scheduler surface still provides prompt/title/schedule/timing/enabled controls but no binding model-family selector, reasoning-effort selector, guaranteed-runtime field, or authenticated completed-run model telemetry. Thus `GPT-6 / maximum` remains a prompt request and is not claimed as the actual runtime here.

The historical `You cannot modify this task` error for a P26 context remains an authorization-context issue rather than a permission to bypass controls. Current repository reconciliation records a later successful P26 update from another authorized context. The legitimate workaround for any still-inaccessible native task is its authorized owning/admin context or platform support; no scheduler state or permissions were changed in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD OUTSIDE
  active_target:
    id: D0034
    source: "Bradley 2005, Basic Properties of Strong Mixing Conditions, Question 6"
    candidate: "Holroyd-Liggett stationary 1-dependent 4-coloring"
    status: "PARTIAL / OPEN"
    claim_path: operations/claims/D0034.md
  metric:
    name: N_rep
    definition: "hidden-state cardinality regimes still requiring exclusion after finite-state impossibility"
    before: 2
    after: 2
    movement: false
    authoritative_stagnation_count: UNKNOWN
  methods:
    - 2
    - 18
    - 24
  new_certified_obstructions:
    - "observable fixed-color excursion words are not finite-order Markov"
    - "radius-one conditional side matrix has nonnegative rank 3, so local rank is not an obstruction"
    - "HHL finite-bubble countable-Markov construction loses all bubble endpoints at the q=4 critical boundary"
  new_metric_moving_route:
    id: PRODUCT-MINORANT-HL
    statement: "prove the center-conditioned two-sided cut law has no nonzero product minorant"
  handoffs_preserved:
    - negative-margin-spherical-perceptron
    - H0017
    - D0036
    - D0039
  next_methods:
    - 3
    - 15
    - 27
```
