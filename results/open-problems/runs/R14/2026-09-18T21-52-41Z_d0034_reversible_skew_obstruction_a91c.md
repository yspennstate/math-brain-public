Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0034: `N_rep: 2 -> 2`; authoritative shared stagnation count remains UNKNOWN. Methods actually used: #3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS.**

# R14 HARD OUTSIDE — D0034: quantitative nonreversibility obstruction for every hidden representation

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **D0034 PARTIAL / source OPEN / active exclusive R14 claim.** The negative-margin spherical perceptron, H0017, D0036 and D0039 remain handed off and are not reopened.

## 1. Continuity, source, ownership, and bounded current-status check

Before new mathematics I reread or queried the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical claim `operations/claims/D0034.md`, the newest R14 D0034 report, current neighboring ownership/status reports, and the D0034 intake entry under `probability_1000_intake_D_20260908`.

The controlling source is still Bradley (2005), Question 6: whether there exists a strictly stationary **psi-mixing**, perhaps even **1-dependent**, sequence which is not an instantaneous function of any strictly stationary Harris recurrent Markov chain. The fixed source-closing candidate remains the Holroyd--Liggett stationary 1-dependent 4-coloring `X_HL`.

The fixed metric remains

`N_rep = number of hidden-state cardinality regimes still requiring exclusion for X_HL after the known finite-state impossibility theorem.`

The certified entering value is still `N_rep=2`:

1. countably infinite-state stationary Markov representations;
2. genuinely general / uncountable-state stationary Harris recurrent representations.

The preceding report killed the most obvious countable-state construction from the observable one-color renewal skeleton, isolated `PRODUCT-MINORANT-HL` as a sufficient infinite-cylinder obstruction, and showed that the HHL off-critical countable-Markov mechanism degenerates at the critical `(k,q)=(1,4)` point. It did not eliminate either complete cardinality regime.

A fresh bounded search on 2026-09-18 UTC checked Bradley's source, Holroyd--Liggett (2016), Holroyd--Hutchcroft--Levy (2020), Berbee--Bradley (1984), Berbee (1987), and 2026 adjacent finitely-dependent-coloring literature. I did not find a source-matching resolution of Bradley Question 6 or a theorem deciding countable-state Markov representability of `X_HL`. This is bounded negative search evidence, not a novelty certificate.

Important adjacent facts retained:

- Holroyd--Liggett prove finite-state hidden-Markov impossibility and explicitly leave the countable-state question open.
- Holroyd--Hutchcroft--Levy construct other finitely dependent proper colorings, including a 1-dependent 5-coloring, which **are** functions of countable-state Markov chains. Therefore no generic “finite dependence forbids countable hidden Markov” argument can be correct.
- Berbee--Bradley's long-block minorization obstruction cannot settle the present candidate: their own Remark 4.3 notes that the necessary minorization property is automatic for psi-mixing processes.
- Berbee's 1987 countable Markov representation theorem for chains with complete connections uses a strong uniform continuity / positivity hypothesis. A proper coloring has forbidden transitions, and at the critical 4-color point the allowed alternating continuation probabilities can approach zero, so that theorem cannot simply be invoked to manufacture a countable representation.

## 2. Method #3 — PROVE SOMETHING STRONGER: exclude every *reversible* hidden chain, on arbitrary state space

The finite-state trace proof is not the right object here. There is a much more direct obstruction if the hidden transition is reversible. It works on an arbitrary measurable state space and gives a quantitative lower bound on how nonreversible any hypothetical hidden representation must be.

### Theorem 2.1 — reversible hidden-chain obstruction

Let `X=(X_n)_{n in Z}` be a stationary, color-symmetric, 1-dependent proper `q`-coloring, with `q>=3`. Suppose

\[
X_n=f(Y_n)
\]

in distribution for a stationary Markov chain `Y` with invariant probability `pi` and Markov operator `P` on `L^2(pi)`. Let `P^*` be the time-reversed Markov operator. Put

\[
A_c=f^{-1}(c),\qquad p=\pi(A_c)=\frac1q,
\]

and let

\[
\mathcal G:=\Bigl\{h\circ f:\sum_{c=1}^q h(c)=0\Bigr\}\subset L^2(\pi)
\]

be the centered color subspace.

Then for every `g in G`,

\[
\boxed{\quad \langle P^*g,Ph\rangle_\pi=0\quad\text{for all }g,h\in\mathcal G,\quad}
\]

so the two subspaces `P G` and `P^* G` are orthogonal. Moreover, for every `g in G`,

\[
\boxed{
\|Pg\|_2\ge \frac1{q-1}\|g\|_2,
\qquad
\|P^*g\|_2\ge \frac1{q-1}\|g\|_2,
}
\]

and therefore

\[
\boxed{
\|(P-P^*)g\|_2
\ge \frac{\sqrt2}{q-1}\,\|g\|_2,
\qquad g\in\mathcal G.
}
\]

In particular a reversible hidden chain (`P=P^*`) is impossible. For the Holroyd--Liggett 4-coloring,

\[
\boxed{
\|(P-P^*)g\|_2\ge \frac{\sqrt2}{3}\|g\|_2
\quad\text{for every }g\in\mathcal G.
}
\]

Thus any hidden Markov realization of `X_HL`, countable-state or general-state Harris, must be **uniformly and quantitatively nonreversible already on the three-dimensional color subspace**.

### Proof

Because `X` is 1-dependent, `X_0` and `X_2` are independent. Hence for centered color functions `g,h in G`,

\[
0
=\mathbb E[g(X_0)h(X_2)]
=\langle g,P^2h\rangle_\pi
=\langle P^*g,Ph\rangle_\pi.
\]

This proves

\[
P^*\mathcal G\perp P\mathcal G.
\tag{2.1}
\]

Next use only the one-step color law. Color symmetry and properness give

\[
\mathbb P(X_1=j\mid X_0=i)=
\begin{cases}
0,&j=i,\\[1mm]
\frac1{q-1},&j\ne i.
\end{cases}
\]

Let `Q` denote this `q x q` transition matrix on color functions. If `g` is centered, then

\[
Qg=-\frac1{q-1}g.
\tag{2.2}
\]

The orthogonal projection from `L^2(pi)` onto the sigma-field generated by `X_0=f(Y_0)` sends `Pg` to

\[
\mathbb E[g(X_1)\mid X_0]=Qg=-\frac1{q-1}g.
\]

Orthogonal projection cannot increase norm, so

\[
\|Pg\|_2\ge\frac1{q-1}\|g\|_2.
\tag{2.3}
\]

The reversed output process has the same one-step pair law (indeed the pair law is uniform on unequal colors), so identically

\[
\|P^*g\|_2\ge\frac1{q-1}\|g\|_2.
\tag{2.4}
\]

Finally (2.1) with `h=g` gives `Pg perpendicular P^*g`, hence

\[
\begin{aligned}
\|(P-P^*)g\|_2^2
&=\|Pg\|_2^2+\|P^*g\|_2^2
 -2\langle Pg,P^*g\rangle\\
&=\|Pg\|_2^2+\|P^*g\|_2^2\\
&\ge \frac{2}{(q-1)^2}\|g\|_2^2.
\end{aligned}
\]

Taking square roots proves the claimed quantitative bound. If `P=P^*`, the left side is zero for every nonzero `g in G`, contradiction. `square`

### Why this is stronger than the obvious color-indicator argument

For one color `c`, writing

\[
g_c=\mathbf 1_{A_c}-1/q,
\]

properness alone gives `Pg_c=-1/q` on `A_c`, and likewise for `P^*g_c`; 1-dependence gives

\[
\langle P^*g_c,Pg_c\rangle=0.
\]

That already rules out reversibility. The theorem above is stronger because it uses the entire centered color subspace simultaneously and yields a uniform singular-value lower bound `sqrt(2)/(q-1)`, not merely one nonzero skew direction.

## 3. Method #15 — BREAK THE SYMMETRY ON PURPOSE: a single color forces directed hidden flow

The process `X_HL` is reversible and fully `S_4`-symmetric, so it is tempting to search only among similarly symmetric or reversible hidden chains. The theorem shows that this is exactly the wrong hidden category.

Fix a color `c` and let

\[
g_c=\mathbf 1_{A_c}-\frac14.
\]

Properness implies, for `pi`-a.e. hidden state `y in A_c`,

\[
P\mathbf 1_{A_c}(y)=0,
\qquad
P^*\mathbf 1_{A_c}(y)=0.
\]

Therefore

\[
Pg_c(y)=P^*g_c(y)=-\frac14
\quad (y\in A_c).
\tag{3.1}
\]

But 1-dependence forces

\[
\langle P^*g_c,Pg_c\rangle=0.
\tag{3.2}
\]

The contribution of `A_c` to the inner product in (3.2) is strictly positive:

\[
\int_{A_c}\frac1{16}\,d\pi=\frac1{64}.
\]

Consequently there must be compensating negative contribution outside `A_c`. In words: **for every color, some hidden states outside that color must have forward and backward one-step tendencies toward that color on opposite sides of the stationary baseline `1/4`.** The hidden representation cannot merely be nonreversible globally; it must carry directed predictive circulation visible in each color fiber.

A coarse one-vector consequence is

\[
\|Pg_c\|_2^2\ge\frac1{64},\qquad
\|P^*g_c\|_2^2\ge\frac1{64},
\]

hence

\[
\|(P-P^*)g_c\|_2^2\ge\frac1{32}.
\]

The full-subspace theorem improves this to the normalized lower bound `sqrt(2)/3` on all nonzero centered color directions.

This has a useful research consequence. A hypothetical countable-state realization cannot be obtained by taking a nearly reversible perturbation of the very symmetric observable process. The hidden chain has to encode substantial orientation that cancels completely after applying the color map.

## 4. Method #27 — SWAP THE QUANTIFIERS: replace “find a bad cylinder for every product component” by one operator identity valid for every hidden realization

The preceding run's `PRODUCT-MINORANT-HL` route has the form

\[
\forall\;\alpha\otimes\beta\neq0,
\quad
\exists\;\text{cylinder rectangle on which domination fails}.
\]

That quantifier structure is difficult because the product component is allowed to avoid any preselected alternating ray.

This run swaps the order of attack. For an arbitrary hidden representation first form its Markov operator `P`, and then use 1-dependence to get a universal identity on the fixed three-dimensional output subspace:

\[
\boxed{
P^*\mathcal G\perp P\mathcal G.
}
\tag{4.1}
\]

The proper-color one-step law simultaneously forces both images to have norm at least one third of the input norm:

\[
\boxed{
\inf_{0\ne g\in\mathcal G}
\frac{\|Pg\|_2}{\|g\|_2}\ge\frac13,
\qquad
\inf_{0\ne g\in\mathcal G}
\frac{\|P^*g\|_2}{\|g\|_2}\ge\frac13.
}
\tag{4.2}
\]

Equations (4.1)--(4.2) are representation-independent. Any successful hidden chain must contain two orthogonal three-dimensional predictive images generated from the same observable color subspace while also respecting positivity and the four color fibers. This is a much tighter target for the next attack than searching arbitrary cylinder pairs one product component at a time.

### Why output reversibility does not finish the argument

One might hope that because `X_HL` itself is reversible, a hidden representation could be taken reversible without loss of generality. That inference is false in hidden-Markov theory: detailed balance of the hidden chain implies reversible observations, but reversible observations can arise from an irreversible hidden chain. Current HMM literature gives explicit finite-state examples of this phenomenon. Therefore Theorem 2.1 is a genuine subclass obstruction, not a hidden way of closing `N_rep`.

This is also consistent with Holroyd--Hutchcroft--Levy: their countable-state Markov realizations produce reversible finitely dependent colorings, so the hidden state mechanism need not inherit the observable reversibility.

## 5. Relation to the Holroyd--Liggett Hilbert-space proof

Holroyd--Liggett Section 5 associates to a stationary process a Hilbert space `U` and an operator `R`. For a 1-dependent process, `R^2` sends the centered part to zero, and for a coloring `U` decomposes into color sectors with `R U_j perpendicular U_j`. Finite hidden state makes `U` finite dimensional, so a trace argument rules out a finite-state hidden Markov representation.

The present theorem is different in two ways:

1. it does not require the hidden state space to be finite, countable, atomic, Harris, or even discrete;
2. it uses the hidden transition operator itself and time reversal, not a trace.

The cost is exactly the reversibility restriction. Infinite-dimensional nonreversible nilpotent-type behavior is not excluded by the Holroyd--Liggett trace argument, and HHL's countable-state examples show that such behavior can really occur.

I did not find the quantitative bound `sqrt(2)/(q-1)` stated in the checked literature. **Novelty is UNVERIFIED**; the argument is short enough that it may be folklore.

## 6. A failed stronger port: Berbee's complete-connections representation theorem does not cross the critical coloring boundary

I also checked whether the countable-state regime could be killed in the opposite direction by proving it actually **exists** via Berbee's 1987 Markov-representation theorem for chains with complete connections.

That theorem assumes a strong uniform continuity condition (classically `sum r_n < infinity`) together with a positive lower-bound setup for the `g`-function. The Holroyd--Liggett proper coloring has structural zeros: the next color equal to the current color has conditional probability zero. More importantly, the critical two-color alternating cylinders from the preceding exact building calculation have an allowed continuation probability of order `1/n` rather than a uniform positive lower bound. Thus the theorem's hypotheses are not available at the critical point without a genuinely new extension allowing vanishing transition probabilities.

So Berbee (1987) is informative but does not currently construct a countable hidden chain for `X_HL`.

## 7. Metric and honest status

The new theorem excludes a broad and natural subclass in **both** cardinality regimes:

- no reversible countably infinite-state stationary Markov chain can generate `X_HL` instantaneously;
- no reversible general-state stationary Harris recurrent Markov chain can do so either;
- more quantitatively, any representation must satisfy

\[
\|(P-P^*)|_{\mathcal G}\|_{\rm min}\ge\frac{\sqrt2}{3},
\]

where the displayed quantity means the minimum norm expansion over the three-dimensional centered color subspace, not an operator norm over all of `L^2(pi)`.

However, arbitrary nonreversible countable-state and arbitrary nonreversible general Harris chains remain possible. Therefore neither complete fixed regime has been removed:

\[
\boxed{N_{\rm rep}:2\to2.}
\]

Status stays **PARTIAL / OPEN**. The authoritative shared stagnation count remains `UNKNOWN`; I do not manufacture it from local chronology.

No exact-arithmetic checker was created this run because the substantive result is an analytic theorem with a complete proof on the page and no finite computational core.

## 8. Next nonrepeating methods

The preceding triple was `#2,#18,#24`; this run used `#3,#15,#27`. The next triple should not repeat either and is recorded as:

- **#7 TAKE THE LIMIT:** study the critical `q downarrow 4` limit of the HHL hidden chain specifically at the level of the skew operator and ask whether positive recurrence forces the directed circulation identified above to escape to infinity;
- **#12 FIND WHAT IS CONSERVED:** look for a stationary-flow / entropy-production invariant of a hidden chain that survives the color projection and is forced both to vanish by observable reversibility and to be positive by (4.1)--(4.2);
- **#26 HUNT THE SPORADIC CASE:** test whether the critical 4-color equality case (one-color renewal gap = sum of two Geom(1/2)'s) makes the hidden-flow constraints rigid in a way that fails for the known countable-Markov 1-dependent 5-coloring.

The metric-moving obligation remains unchanged: either eliminate **all** countably infinite-state representations (`N_rep:2->1`), eliminate **all** general Harris representations by a separate source-valid argument, or construct a hidden representation and thereby kill `X_HL` as the fixed candidate. Another restricted subclass will be marked PARTIAL and will not be counted as metric movement.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  deployment: NEW-METHODS-2026-09-16
  target_id: D0034
  source: "Bradley 2005, Question 6"
  category: HARD_OUTSIDE
  ownership: "exclusive R14 claim preserved"
  fixed_candidate: "Holroyd-Liggett stationary 1-dependent 4-coloring"
  metric: N_rep
  metric_definition: "hidden-state cardinality regimes still requiring exclusion after known finite-state impossibility"
  before: 2
  after: 2
  movement: "no movement"
  authoritative_stagnation_count: UNKNOWN
  status: PARTIAL
  source_status: OPEN
  methods_used: [3, 15, 27]
  new_certified_result:
    - "Any hidden representation has P^*G orthogonal to PG on the centered color subspace G."
    - "For color-symmetric q-coloring, ||(P-P^*)g|| >= sqrt(2)/(q-1) ||g|| for all g in G."
    - "Hence no reversible hidden Markov chain on any state space can represent X_HL; at q=4 the lower bound is sqrt(2)/3."
  novelty: UNVERIFIED
  remaining_obligations:
    - "exclude all nonreversible countably infinite-state representations"
    - "exclude all nonreversible general-state Harris recurrent representations"
  next_methods: [7, 12, 26]
  shared_roots_modified: false
  peer_files_modified: false
  email: false
  drive: false
  public_posting: false
  permissions_changed: false
  workflows_run: false
  scheduler_changed: false
```

## 10. Model / scheduler limitation

The exposed scheduling interface still has no binding model-family selector, no reasoning-effort selector, no guaranteed-runtime control, and no authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains prompt text only; this report does **not** claim it actually ran.

The repository policy still records modification probes on P26/P01/P03 returning `You cannot modify this task`. The legitimate remedy is the authorized owning/admin account or workspace interface, or platform support. R14 did not bypass permissions, duplicate a denied task, or alter scheduler state.
