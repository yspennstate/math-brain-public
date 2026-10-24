Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0034: `N_rep: 2 -> 2`; authoritative shared stagnation count remains UNKNOWN. SECTION-I STUCK-RECOVERY-1/2. Methods actually used: #7 TAKE THE LIMIT, #12 FIND WHAT IS CONSERVED, #26 HUNT THE SPORADIC CASE.**

# R14 HARD OUTSIDE — D0034 Bradley Question 6 — stuck recovery 1/2

## 1. Continuity, source, ownership, and why this is a thinking run

I reread the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current owner directive, the canonical D0034 claim, the newest R14 D0034 report, and the repo search hits for neighboring Bradley/finitely-dependent-coloring work before doing mathematics. I found no later source-level closure or competing canonical owner for D0034. The earlier R14 handoffs of the negative-margin spherical perceptron, H0017, D0036, and D0039 remain in force; this run does not reopen them.

The outside source is Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys 2 (2005), arXiv:math/0511078, Question 6: whether there exists a strictly stationary `psi`-mixing (perhaps even 1-dependent) sequence which is not an instantaneous function of any stationary Harris recurrent Markov chain. The fixed candidate remains the Holroyd--Liggett stationary 1-dependent 4-coloring `X_HL`. Holroyd--Liggett prove finite-state hidden-Markov impossibility and explicitly leave countable hidden state open; Holroyd--Hutchcroft--Levy later construct other finitely dependent colorings that *are* functions of countable-state Markov chains, so a generic infinite-dimensional extension of the finite-state argument is impossible.

A bounded current-literature check on 2026-09-18 used Bradley `math/0511078`, Holroyd--Liggett `arXiv:1403.2448`, Holroyd--Liggett `arXiv:1407.4514`, Holroyd `arXiv:1411.1463`, and Holroyd--Hutchcroft--Levy `arXiv:1706.09526`. I did not find a later source-matching theorem deciding countable-state representability of the 1-dependent 4-coloring or Bradley Question 6. This is negative search evidence only, not a novelty certificate.

There are now three consecutive own immutable D0034 reports with no certified metric movement after the Nummelin correction. Owner policy requires authoritative shared stagnation counts to remain UNKNOWN, so I do not replace that field by a guessed number; nevertheless the own-report history triggers Section-I stuck recovery. This invocation is therefore deliberately a **thinking run with no new theorem claims and no checker manufacture**.

## 2. Fixed metric and exact blocker

The certified metric remains

`N_rep = number of hidden-state cardinality regimes still requiring exclusion for X_HL`.

The two regimes are:

1. irreducible positive recurrent countable-state hidden Markov chains;
2. general stationary Harris recurrent hidden Markov chains.

Thus `N_rep=2` before and after this run.

For the countable-state regime, the blocker can now be written as one exact positive-realization problem. Let `S` be countable, `P` an irreducible positive recurrent transition kernel, `pi` its stationary law, and `f:S->{1,2,3,4}`. Let `D_c` denote multiplication by `1_{f=c}`. Holroyd--Liggett's exact cylinder law is

\[
 \mathbb P(X_1=x_1,\ldots,X_n=x_n)
   = \frac{B(x_1\cdots x_n)}{(n+1)!\,2^n}
\]

for every proper word, where `B` is the building number. The countable-state obligation is to prove that there is **no** quadruple `(S,P,pi,f)` satisfying

\[
\boxed{
 \pi D_{x_1}P D_{x_2}P\cdots P D_{x_n}{\bf 1}
 = \frac{B(x_1\cdots x_n)}{(n+1)!\,2^n}
 \quad\text{for every }n\ge1\text{ and every proper }x\in[4]^n.
}
\tag{COUNTABLE-HL}
\]

The general-Harris obligation is the analogous statement with a positive Harris recurrent standard-Borel kernel in place of `(S,P)`; the previous attempted reduction of this regime to COUNTABLE-HL was retracted because `m`-step Nummelin splitting can leave one-dependent original-time regeneration blocks.

## 3. Route ledger: what has been tried, and why each route currently fails

The point of this recovery is to compress the failure history into one obstruction rather than add another auxiliary identity.

### A. Finite-state / trace route

Schramm's finite-state Hilbert-space argument rules out finite hidden state. It does not extend automatically to countable state: the finite-dimensional trace identity is lost, and later HHL examples show that some finitely dependent proper colorings really do have countable-state Markov representations. Any successful continuation must use a feature special to the critical 1-dependent 4-coloring.

### B. General-Harris collapse through Nummelin regeneration

The first R14 D0034 run claimed that every countable-output Harris factor collapses to a countable-state hidden chain. This was corrected. For an `m>1` minorization, the original-time blocks retain bridge memory and can be one-dependent rather than iid. Thus no certified `2 -> 1` movement survives from that route.

### C. Observable renewal / one-color returns

A fixed-color indicator is renewal-like, but the full coloring does not regenerate at a color occurrence. Exact side-color conditional probabilities already violate left/right product structure. More strongly, the sequence of observable excursions between fixed-color visits is not finite-order Markov: repeated one-site excursions have factorial rather than eventually geometric repetition probabilities. This kills the naive idea that the obvious observable return times are the hidden Markov regeneration times, but hidden states may refine each color fiber.

### D. Product-minorant / nonnegative-rank route

Conditioning on a center color in a countable hidden representation gives a countable mixture of left/right product laws. A universal no-product-minorant theorem would exclude the countable regime. Radius one is too weak: the exact `3 x 3` side-color matrix already admits a finite nonnegative factorization. Along one alternating cylinder ray the likelihood ratio against the product marginals tends to zero, but an arbitrary product component may avoid that particular ray. The missing quantifier is universal selection of a bad ray for every nonzero product component.

### E. Berbee / complete-connections construction route

Known countable-state representation theorems for chains with complete connections rely on positivity/regularity hypotheses. Proper coloring has structural zero one-step transitions, and the critical alternating continuations approach zero too fast for a direct use of those hypotheses. Hence this route currently supplies neither a construction nor an impossibility theorem.

### F. Reversibility route

The newest R14 theorem proves that any hidden representation must be quantitatively nonreversible on the centered color subspace: for `q=4`, `||(P-P*)g|| >= sqrt(2)/3 ||g||`. This eliminates all reversible hidden chains on arbitrary state spaces. It does **not** eliminate the countable or Harris regimes because reversible observed laws can have irreversible hidden realizations.

### G. Off-critical HHL construction route

The known HHL countable-state construction for neighboring finitely dependent colorings has a positive-density regenerative/bubble structure with exponential-tail coding. In the `k=1` parameterization, the relation

\[
 q=t+2+t^{-1},\qquad q-4=\frac{(1-t)^2}{t}
\]

places the 1-dependent 4-coloring at the critical endpoint `t=1`. The previously extracted bubble-marker density tends to zero there, and the corresponding mean spacing diverges. This shows why the *known* positive construction degenerates at `q=4`; it does not prove that every possible countable representation must use the same marker mechanism.

## 4. Method #7 — TAKE THE LIMIT: identify the critical quantity that actually disappears

The useful message of the `q downarrow 4` limit is not merely that one formula blows up. HHL gives a solved countable-state representation on the off-critical side with an explicit source of positive recurrence: recurrent markers divide the configuration into finite bubbles, and their spacing has an exponentially controlled law. At the critical 4-color endpoint, that marker density collapses.

This suggests the correct contrapositive target:

> Any countable-state positive-recurrent hidden realization of `X_HL` would have to manufacture positive recurrence **without** a positive-density observable/latent bubble decomposition of the HHL type.

So the next proof must not try to continue HHL's markers continuously to `t=1`. It must instead show that *some* nondegenerate recurrent structure is unavoidable in every positive recurrent hidden realization, and then show that the exact 4-color cylinder probabilities forbid it.

That universal-forcing statement is exactly what all earlier routes lack.

## 5. Method #12 — FIND WHAT IS CONSERVED: stationary cycle/flow mass as the candidate invariant

The new route-level idea is to use the stationary directed flow

\[
J(s,t)=\pi(s)P(s,t)
\]

rather than the transition operator alone. Positive recurrence conserves total flow through every state, while proper coloring forces `J(s,t)=0` whenever `f(s)=f(t)`.

The exact 4-color law has a particularly violent signature on two-color alternating words: their probabilities decay factorially in the word length, not merely exponentially. By contrast, if a hidden two-color restriction contains a fixed directed alternating cycle with positive transition product and positive stationary mass at one cycle state, repeated traversal of that cycle would contribute an exponentially decaying lower bound to the corresponding alternating cylinders.

This is the most promising candidate invariant found in the recovery: **pair-color cycle mass cannot remain at a fixed positive scale**. The intended next theorem is not asserted here; it is the following route to prove:

1. convert factorial alternating-cylinder decay into a statement that every fixed two-color recurrent cycle has zero stationary flow contribution;
2. deduce that any hypothetical representation must push all two-color alternating flow farther and farther into the state-space tail as the alternating run length grows;
3. combine that “cycle escape” with positive recurrence/tightness of `pi` to force a contradiction.

The missing step is (3). Positive recurrence gives tight stationary mass on a countable state space, but it does not by itself say that long observed alternating runs must start or spend a fixed fraction of time inside a fixed finite high-mass set. A proof needs a quantitative bridge from stationary tightness to the conditioned hidden paths supporting those rare cylinders.

This is a genuinely different obstruction from the failed trace and product-minorant routes: it uses **stationary flow plus superexponential cylinder decay**.

## 6. Method #26 — HUNT THE SPORADIC CASE: what is special about `(k,q)=(1,4)`

The sporadic feature is now sharply identified. Nearby HHL finitely dependent colorings admit countable-state Markov representations with finite-mean/exponential-tail coding, while the original Holroyd--Liggett 1-dependent 4-coloring lies exactly at the endpoint where the known bubble density vanishes. At the same time, its two-color alternating cylinders have factorial decay.

Therefore a putative hidden chain at `(1,4)` must simultaneously have:

- positive recurrence globally;
- no reversible realization (previous R14 theorem);
- no finite-state realization (Schramm);
- no obvious observable regeneration at color returns;
- and hidden two-color mechanisms capable of producing arbitrarily long alternating observed words with factorially small probabilities.

The simplest special case still unproved that exposes this critical tension is:

`FINITE-PAIR-HL`: rule out a countable-state positive recurrent representation in which, for at least one unordered color pair `{a,b}`, only finitely many hidden states can participate in positive-probability paths whose observed colors stay in `{a,b}`.

This special case is deliberately narrow. It should collapse to a finite directed-graph argument: arbitrarily long alternating cylinders force arbitrarily long hidden paths in the finite pair-support graph; a finite directed graph then forces an alternating directed cycle; repeating such a cycle gives exponential rather than factorial cylinder decay. The full proof and the exact quantifiers are deferred to the next substantive run, because this invocation is a Section-I thinking run and makes no new theorem claim.

If `FINITE-PAIR-HL` is completed, the useful conclusion is not metric movement by itself; it identifies the next unavoidable property of any hypothetical representation: **every color pair must use infinitely many hidden states and its alternating mass must escape to infinity.** That is the form in which positive recurrence can then be attacked.

## 7. What a full proof must contain that no route so far contains

To move `N_rep:2 -> 1`, a proof must exclude *all* irreducible positive recurrent countable-state solutions of (COUNTABLE-HL). Every previous argument imposed an extra condition—finite state, observable regeneration, one selected product ray, reversibility, complete-connection positivity, or HHL's specific bubble coding.

The missing universal ingredient can now be stated succinctly:

\[
\boxed{
\text{factorial two-color cylinder decay}
+\text{ stationary positive recurrence}
\Longrightarrow
\text{a contradiction, without any finite-state/reversibility assumption.}
}
\]

A plausible way to realize that implication is a **cycle-escape versus tightness lemma**: conditioned hidden paths supporting longer and longer alternating output words must escape every finite set, while positive recurrence plus stationarity should force enough recurrent mass through some finite set to prevent exactly that. The conditioning on an increasingly rare event is the technical obstruction; naive stationary tightness is insufficient.

To move the final `1 -> 0`, one additionally needs either a direct Harris version of the same cycle-escape argument or a correct reduction from Harris hidden chains to a countable/regenerative model that respects the `m>1` bridge dependence.

## 8. Nearest solved problem and what its proof has that this problem lacks

The nearest solved positive comparison is Holroyd--Hutchcroft--Levy, *Mallows Permutations and Finite Dependence* (arXiv:1706.09526; Ann. Probab. 2020). Their finitely dependent colorings are finitary factors with finite mean/exponential-tail coding and are functions of countable-state Markov chains. Their construction has explicit recurrent cut/bubble information that provides finite-mean returns in the hidden state description.

The critical 1-dependent 4-coloring lacks such a positive-density cut structure in the known deformation; the cut density collapses at the critical endpoint. Thus the nearest solved proof has an explicit renewal mechanism that the target process does not visibly possess. The research problem is to show that this is not merely a failure of one construction but a universal obstruction.

## 9. Recovery choice and next moves

Section I requires exactly one recovery choice. I choose:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE** — `FINITE-PAIR-HL` above.

The next run should prove or refute that special case completely, then immediately ask whether the finite-support condition can be weakened to a quantitative tightness condition on pair-color stationary flow. It should not add another finite-window identity.

Next nonrepeating Section-B moves:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** close `FINITE-PAIR-HL` with all quantifiers written exactly;
- **#13 FIND WHAT ONLY INCREASES:** search for an escape-depth or minimal pair-support level along an alternating hidden path that must diverge with cylinder length;
- **#30 DO ONE SCALE, ONE DIRECTION AT A TIME:** first prove a one-pair, one-alternating-direction tail lemma, then determine exactly why the four-color pieces do or do not glue.

If this recovery chain later reaches a second unchanged stuck recovery on D0034, the hard-task rule still permits only one more recovery before terminal handoff/rotation.

## 10. Scheduler/model control checked this run

I checked the exposed task surface during this run. It still exposes prompt text, title, schedule, timing mode, enabled/notification state, and related task metadata. It does **not** expose a binding model-family selector, a reasoning-effort selector, a guaranteed-duration field, or authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains requested in prompt text only; this run cannot honestly claim it executed that configuration.

For tasks that return `You cannot modify this task`, the legitimate remedy remains an authorized owning/admin context or platform support. The historical P26 refusal was authorization-context dependent; no permission bypass or duplicate task is justified.

No scheduler state was changed in this run.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  source: "Bradley 2005, Question 6; fixed candidate Holroyd-Liggett 1-dependent 4-coloring"
  source_kind: HARD_OUTSIDE
  target_id: D0034
  metric: N_rep
  metric_definition: "hidden-state cardinality regimes still requiring exclusion for X_HL"
  before: 2
  after: 2
  movement: "no movement"
  status: OPEN
  authoritative_shared_stagnation_count: UNKNOWN
  own_history_trigger: "three consecutive own immutable post-correction D0034 reports at 2 -> 2; therefore Section-I stuck recovery 1/2"
  methods_tried: [7, 12, 26]
  recovery_choice: "prove simplest unproved special case: FINITE-PAIR-HL"
  substantive_new_claims: []
  route_advance:
    - "critical q downarrow 4 comparison isolates loss of positive-density bubble/renewal structure"
    - "candidate stationary-flow obstruction: factorial alternating cylinders should force two-color cycle mass to escape to infinity"
    - "exact next special case FINITE-PAIR-HL isolated"
  remaining_obligation:
    - "exclude every irreducible positive recurrent countable-state solution of COUNTABLE-HL"
    - "then exclude or reduce the general stationary Harris recurrent regime"
  next_methods: [4, 13, 30]
  audit_ids: []
  artifacts_created: []
```

No shared root, peer track, email, Drive item, public post, permission, workflow, or scheduler setting was changed.