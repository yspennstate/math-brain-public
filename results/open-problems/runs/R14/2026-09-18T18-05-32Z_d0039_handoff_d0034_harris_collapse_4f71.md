Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. D0039 TERMINAL HANDOFF at `B_spectrum=2`; fresh HARD OUTSIDE successor D0034 moves `N_rep: 2 -> 1`. Methods actually used: #1 CHANGE THE CATEGORY, #20 FIND WHY THE ALGORITHM FAILS, #28 REPLACE “FOR ALL” WITH “FOR TYPICAL”.**

# R14 HARD OUTSIDE — terminal D0039 handoff; D0034 Harris-to-countable Markov reduction

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **D0039 PARTIAL / source OPEN / terminally handed off. D0034 PARTIAL / source OPEN / active R14 claim.**

## 1. Continuity and mandatory rotation

I reread/recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, the canonical D0039 claim, the newest R14 D0039 reports, the nearest neighboring D0039 admission/status reports, and the Bradley D-intake around D0034. `RESULTS.md` remains stale for parts of the R-series, so immutable newer track reports and canonical claims control continuity rather than the stale row.

The immediately preceding R14 report,

`runs/R14/2026-09-18T16-49-54Z_d0039_stuck_recovery2_palm_fusion_threshold_7a4e.md`,

was explicitly **Section-I stuck recovery 2/2** for D0039. It froze the remaining beta-Hermite obligation as a same-environment conditional child theorem, `BLOCK_{3/8}`, and stated that a third recovery was not authorized. No independent result in the repository moved `B_spectrum` after that report. Therefore this invocation performs the required terminal D0039 handoff before doing successor research.

The negative-margin spherical perceptron, H0017, and Bradley D0036 remain handed off and are not reopened.

## 2. Terminal D0039 handoff

D0039 is Bálint Virág's beta-Hermite spectral-measure multifractal-spectrum question. R14 leaves the fixed metric at

`B_spectrum = 2`.

Nothing in this invocation is relabeled as progress on D0039.

The clean handoff frontier is:

- the fixed-energy beta-4 Christoffel-kernel speed-`log N` LDP and its explicit rate are on file;
- Gaussian-quadrature / Chebyshev--Markov--Stieltjes reduction transfers quadrature-weight exponents to actual spectral masses once a nested good-cell theorem is available;
- the independent endpoint Dirichlet factor is polynomially exponent-neutral on the interior target window;
- the root-Palm calculation and the independent branching calculation agree on the natural second-moment boundary `t<1` / `x>1/4`;
- the simplest unproved local-dimension test remains

\[
\dim_H\{E:d_{\mu_4}(E)=3/4\}=23/32;
\]

- the immediately prior stochastic obligation is still the conditional descendant estimate `BLOCK_{3/8}` in the **same semi-infinite Jacobi environment**. One-size GSE moments, deterministic-energy LDPs, and Sine-beta fusion do not supply this cross-degree conditional statement.

That is the complete D0039 handoff. It should not be reassigned by simply continuing the same Palm/fusion auxiliary-lemma sequence; a fresh owner needs a genuinely new route to the cross-degree filtration problem.

## 3. Successor admission: D0034

### Source

Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys 2 (2005), Question 6 in Section 3.3 / intake `D0034`:

> Does there exist a strictly stationary psi-mixing (or perhaps even 1-dependent) sequence which cannot be represented as an instantaneous function of a strictly stationary, Harris recurrent Markov chain?

This question descends from Berbee--Bradley's 1984 paper *A limitation of Markov representation for stationary processes*. That paper constructs a strongly `psi*`-mixing non-Harris-representable process but explicitly states that the analogous problem for `psi`-mixing, even 1-dependent processes, is open in their framework.

### Ownership and status screen

Before research I checked the canonical claims directory directly: `operations/claims/D0034.md` did not exist. The current `POSTED.md` / campaign settled lists do not identify D0034 as posted, PROVED, REFUTED, or KNOWN. Recent R7/R15 successor screens independently classified it as open-looking and HARD rather than CLOSABLE, and neither claimed it.

A fresh bounded literature search on 2026-09-18 recovered Bradley's source, Berbee--Bradley (1984), Berbee (1987), Holroyd--Liggett (2016), Holroyd--Hutchcroft--Levy (2020), Spinka (2020), and Nummelin-splitting references, but no source-matching resolution of Bradley Question 6 and no theorem deciding whether the Holroyd--Liggett stationary 1-dependent 4-coloring is a function of a countable-state Markov chain. This is bounded negative dispatch evidence, **not** a novelty or worldwide-openness certificate.

I then created the create-only exclusive claim

`operations/claims/D0034.md`

at commit `c6a42e9f8e2b7bb8b3fb5578a9827e4a212e4e4e`.

### Fixed source-closing candidate

Fix `X_HL`, the Holroyd--Liggett stationary 1-dependent 4-coloring of `Z`. It is finite-valued and stationary, and 1-dependence makes it a source-valid candidate for Bradley Q6. Holroyd--Liggett prove that no stationary finitely dependent proper coloring can be a function of a **finite-state** Markov chain; their paper explicitly says the countable-state case remains open.

The successor route is therefore not to invent a new process. It is to determine whether this already-extremal 1-dependent process lies outside Bradley's Harris representation class.

## 4. Fixed metric

Define

`N_rep := number of hidden-state cardinality regimes still requiring exclusion for X_HL after the known finite-state impossibility theorem.`

At admission there are two a priori regimes:

1. countably infinite-state stationary Markov representations;
2. genuinely general / uncountable-state Harris recurrent representations.

Thus

`before = 2`.

The theorem below collapses regime 2 into regime 1 for **every countable-output process**. Hence

`after = 1`.

The source-closing target is `N_rep=0`, i.e. exclude a countable-state positive recurrent hidden-Markov representation of `X_HL`. This run therefore has genuine fixed-metric movement but **does not** close D0034.

## 5. Method #1 — CHANGE THE CATEGORY: Harris representation to a countable regenerative hidden chain

The old D0034 intake note correctly pointed toward regeneration but overstated it by saying, without qualification, that instantaneous functions of Harris chains are “exactly” iid regeneration-block processes. What is actually needed is a split-chain argument. Once it is written correctly, a useful exact reduction follows.

### Theorem 5.1 — countable-output Harris-collapse lemma

Let `A` be a finite or countable alphabet. Let

\[
X=(X_n)_{n\in\mathbb Z},\qquad X_n\in A,
\]

be strictly stationary. Suppose `X` has the same law as

\[
(f(Y_n))_{n\in\mathbb Z}
\]

for some strictly stationary Harris recurrent Markov chain `Y` on a standard Borel state space and measurable `f` with range contained in `A`.

Then `X` is also an instantaneous function of a strictly stationary **countable-state, irreducible positive recurrent Markov chain**.

Periodicity is allowed.

#### Proof

Because `Y` is Harris recurrent and already carries an invariant **probability** law (strict stationarity), it is positive Harris recurrent. By the standard Athreya--Ney / Nummelin splitting theorem, after passing if necessary to an `m`-skeleton associated with a positive-mass small set and enlarging the state by the split indicator, one obtains an augmented Markov chain with an accessible atom and regeneration epochs

\[
\cdots<T_{-1}<T_0<T_1<T_2<\cdots
\]

such that:

1. the `Y`-coordinate of the augmented chain has exactly the original stationary law;
2. at a regeneration epoch the post-regeneration state is drawn from a fixed law independent of the pre-regeneration past;
3. the successive nonoverlapping tours between post-regeneration epochs are iid under the Palm law of a regeneration;
4. because the original chain is positive recurrent, the tour length
   \[
   L_i:=T_{i+1}-T_i
   \]
   is finite almost surely and has finite mean.

If the minorization is for an `m`-step kernel, place the regeneration epoch at the **post-minorization endpoint**. The intervening `m-1` coordinates belong to the tour that ends at that endpoint. This avoids the harmless one-block overlap that appears in some statistical formulations of Nummelin blocks; the resulting complete tours from one regenerated endpoint to the next are independent by the strong Markov property and the atom property.

For each Palm tour define its finite **output word**

\[
W_i:=\bigl(f(Y_{T_i}),f(Y_{T_i+1}),\ldots,f(Y_{T_{i+1}-1})\bigr).
\]

(Changing which endpoint is assigned to which adjacent tour merely shifts the word convention and has no effect on the argument.) The words `W_i` are iid. Since `A` is countable, the set

\[
\mathcal W:=\{w: \mathbb P(W_0=w)>0\}
\]

of possible finite words is countable. Write

\[
q(w):=\mathbb P(W_0=w),\qquad \ell(w):=|w|.
\]

The mean word length

\[
\bar\ell:=\sum_{w\in\mathcal W}q(w)\ell(w)=\mathbb E L_0
\]

is finite.

Now define the countable state space

\[
S:=\{(w,r): w\in\mathcal W,\ 1\le r\le\ell(w)\}.
\]

Define a Markov kernel `P` on `S` by

\[
P((w,r),(w,r+1))=1,\qquad r<\ell(w),
\]

and at the end of a word

\[
P((w,\ell(w)),(w',1))=q(w')
\qquad(w'\in\mathcal W).
\]

Finally define the output map

\[
h(w,r):=w_r.
\]

The probability measure

\[
\pi(w,r):=\frac{q(w)}{\bar\ell}
\tag{5.1}
\]

is stationary for `P`. Indeed, if `r>1`, the only incoming transition to `(w,r)` is from `(w,r-1)`, giving incoming mass `q(w)/\bar\ell`. If `r=1`, then

\[
\sum_{v\in\mathcal W}\pi(v,\ell(v))q(w)
=\frac{q(w)}{\bar\ell}\sum_v q(v)
=\frac{q(w)}{\bar\ell}.
\]

On the support `q(w)>0`, the chain is irreducible: from any `(w,r)` it reaches the end of `w`, and at that transition it has positive probability `q(w')` to enter any prescribed word `w'`; deterministic motion then reaches every `(w',r')`. The existence of the invariant probability `\pi` therefore makes this irreducible countable chain positive recurrent.

It remains only to match the **stationary law**, not merely the Palm law. Under (5.1), the word containing time zero is selected with length bias

\[
\mathbb P_\pi(\text{current word}=w)
=\frac{q(w)\ell(w)}{\bar\ell},
\]

and conditional on that word the position `r` is uniform on `\{1,\ldots,\ell(w)\}`. To the left and right, complete words are iid with law `q`. This is exactly the equilibrium (stationary) version of the regenerative concatenation of the split-chain output tours. Since the split construction leaves the `Y`-coordinate law unchanged, that stationary concatenation has the law of `(f(Y_n))`, i.e. the law of `X`.

Thus `(h(Z_n))`, where `Z` is the stationary countable-state chain just constructed, has exactly the law of `X`. This proves the theorem. `□`

### Corollary 5.2 — what Bradley Q6 becomes on a finite alphabet

For a finite- or countable-valued candidate, to prove that it is **not** an instantaneous function of any stationary Harris recurrent chain, it is enough to rule out countable-state irreducible positive recurrent hidden-Markov representations.

In particular, for `X_HL`, the apparently separate “uncountable Harris state” regime is not a separate obligation.

### Novelty status

I am **not claiming Theorem 5.1 as novel**. It is a short consequence of standard Nummelin regeneration plus the elementary word-position Markov encoding, and it may well be folklore or implicit in representation literature. The bounded prior-art search found Nummelin's splitting theorem, Berbee's countable-state Markov representations for chains with complete connections, and several regeneration/coding papers, but I did not find this exact countable-output collapse stated in the searched sources. It is used here as a rigorous route reduction, not as a publishability claim.

## 6. Method #28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”: reduce arbitrary countable representations to one positive recurrent class

There is a second, smaller quantifier reduction that is useful for the successor target.

Suppose a stationary **countable-state** Markov chain `M` represents `X_HL`, but `M` is not assumed irreducible. Under a stationary probability law, transient states have zero stationary mass and the law decomposes over closed positive recurrent classes. Conditioning on the recurrent class gives stationary component laws for the output.

The Holroyd--Liggett 1-dependent coloring is mixing, hence ergodic. An ergodic stationary measure is an extreme point of the convex set of stationary measures. Therefore, if

\[
\mathcal L(X_{HL})
=
\int \nu_c\,\eta(dc)
\]

is the decomposition of its output law induced by the hidden recurrent class, extremality forces

\[
\nu_c=\mathcal L(X_{HL})
\quad\text{for }\eta\text{-a.e. }c.
\]

Choose one such class. Restricting `M` to that class gives an irreducible positive recurrent countable-state Markov representation of the same output law.

Hence the remaining source-closing obligation can be stated without any loss as

\[
\boxed{
\text{Rule out an irreducible positive recurrent countable-state Markov chain }M
\text{ and map }f\text{ with }f(M)\stackrel d=X_{HL}.
}
\tag{COUNTABLE-HL}
\]

This is the one surviving `N_rep` regime.

## 7. Method #20 — FIND WHY THE ALGORITHM FAILS

Two tempting old routes fail for exact, now-useful reasons.

### 7.1 Berbee--Bradley's 1984 nonrepresentation certificate cannot solve the psi-mixing question

Berbee--Bradley derive a long-block product-minorization property (their Lemma 4.1) that every stationary Harris-Markov output must satisfy. They then construct a `psi*`-mixing process violating it. But immediately afterward their Remark 4.3 says that **stationary psi-mixing processes already satisfy that same property** and explicitly records the psi-mixing / 1-dependent Harris-representation question as open.

So the 1984 successful obstruction is categorically unavailable here. It is not that one needs a sharper constant in their proof; the entire necessary property becomes automatic under the stronger source hypothesis.

That kills the most obvious attempt to recycle the old counterexample.

### 7.2 Schramm's finite-state hidden-Markov trace proof breaks exactly at infinite dimension

Holroyd--Liggett associate to any stationary process a Hilbert space `U` and bounded operator `R`. For a `k`-dependent process,

\[
R^nU=\operatorname{span}\{1\},\qquad n>k,
\]

while a proper `q`-coloring gives an orthogonal decomposition

\[
U=U_1\oplus\cdots\oplus U_q,
\qquad RU_j\perp U_j.
\]

If the process is a function of a **finite-state** Markov chain, their Lemma 15 gives `dim U<infinity`. Choosing an orthonormal basis adapted to the color decomposition yields

\[
\operatorname{tr}R=0,
\]

but finite dependence says the only nonzero eigenvalue is `1`, giving a contradiction.

For a countable hidden chain, `U` may be infinite dimensional. Holroyd--Liggett explicitly note that the operator furnished by their coloring cannot be trace class (Lidskii would otherwise recreate the contradiction). Therefore the finite-state proof fails at one precise point:

\[
\boxed{
\text{there is no legitimate ordinary trace of }R\text{ in the countable-state case.}
}
\]

This is not a technical annoyance. Holroyd--Hutchcroft--Levy later construct other stationary finitely dependent proper colorings that **are** functions of countable-state Markov chains, so no blanket extension of Schramm's finite-dimensional trace argument can be true.

The source-closing proof for `X_HL` must exploit a special feature of the 1-dependent 4-coloring, not merely finite dependence plus proper coloring.

## 8. What the special candidate gives that generic countable-state colorings do not

The Holroyd--Liggett process has substantially more structure than a generic finitely dependent coloring. In particular their Theorem 4 records, among other identities, that it is reversible and color-permutation symmetric and that for each color the one-color indicator is the descent process of iid fair Bernoulli variables. Their Proposition 16 gives, for any stationary 1-dependent coloring with single-color density `p`, a renewal gap generating function

\[
G(s)=\frac{p s^2}{1-s+p s^2}.
\]

At the symmetric 4-coloring value `p=1/4`,

\[
G(s)=\frac{s^2}{(2-s)^2},
\qquad
\mathbb P(T=n)=\frac{n-1}{2^n},\quad n\ge2.
\tag{8.1}
\]

Equation (8.1) has an exponential tail, so **single-color recurrence by itself is not an obstruction** to a positive recurrent countable hidden chain. Indeed it points the other way: the one-color projection has a simple regenerative description. The obstruction, if it exists, must live in the *joint coupling of the four renewal structures* (and the extra two-color descent identities), not in any one color separately.

This also explains why replacing an arbitrary Harris state by a regenerative countable state is useful rather than fatal: it tells us exactly where to look. A countable hidden representation would have to realize a very rigid four-way coupling while preserving the Markov property of the hidden excursion chain.

## 9. A failed “typical finite truncation” attempt, and the precise missing invariant

Positive recurrence of a countable hidden chain lets one choose finite hidden-state sets carrying stationary mass `1-epsilon`. It is tempting to compress the hidden Markov operator to those typical finite sets and apply Schramm's trace contradiction approximately.

This does **not** work for free. Compression to a finite set destroys the exact identities

\[
R^2U=\operatorname{span}\{1\}
\quad\text{and}\quad
RU_j\perp U_j
\]

by boundary leakage. An `epsilon` stationary-mass error does not give a rank-independent trace error: the truncated rank can diverge so rapidly that `epsilon * rank` is uncontrolled. In operator language, this is the same failure as lack of trace class.

Therefore the next proof needs an invariant that is stable under positive-recurrent truncation **without a dimension factor**. Candidates include:

- a Fredholm index / determinant-type quantity for a suitable compact perturbation of `R`;
- a trace taken only after applying a source-specific finite-rank polynomial in the color operators;
- a regenerative excursion identity whose expectation is absolutely summable under stationarity and whose sign is forced differently by proper coloring and 1-dependence.

No such invariant is proved in this run.

## 10. Nearest solved / known comparison problems

The current boundary is unusually informative:

1. **Berbee--Bradley (1984).** Strong `psi*`-mixing is not enough for Harris representation; their exact obstruction becomes automatic under `psi`-mixing, hence cannot answer D0034.
2. **Berbee (1987).** Under a summable continuity condition, finite/countable-alphabet chains with complete connections are instantaneous functions of countable-state Markov chains. This is a positive representation theorem, not a counterexample mechanism.
3. **Holroyd--Liggett (2016).** The stationary 1-dependent 4-coloring exists and no stationary finitely dependent coloring is a function of a finite-state Markov chain. They explicitly leave countable-state hidden Markov chains open.
4. **Holroyd--Hutchcroft--Levy (2020).** Other finitely dependent colorings can be functions of countable-state Markov chains, even with exponential-tail finitary coding. Thus “finitely dependent coloring” alone cannot rule out countable hidden states.
5. **Spinka (2020).** Every finitely dependent invariant process on a transitive amenable graph is a finitary factor of iid. Finitary iid coding does not imply an instantaneous Harris-Markov representation and so does not decide D0034.

A fresh bounded search through 2026-09-18 did not surface a later theorem settling `(COUNTABLE-HL)`. Again, that is bounded negative evidence only.

## 11. Remaining exact obligation

The metric has moved once, but the source is not closed. The remaining obligation is now singular rather than bifurcated:

\[
\boxed{
\texttt{COUNTABLE-HL: }
X_{HL}\text{ is not an instantaneous function of any irreducible positive recurrent}
\text{ countable-state Markov chain.}
}
\]

A proof of this boxed statement would give `N_rep: 1 -> 0` and, by Theorem 5.1, would supply a 1-dependent counterexample to Bradley Question 6.

The first concrete subtarget for the next run is **not** another finite-state truncation. It is to derive the hidden-state operator associated with `X_HL` under a hypothetical positive recurrent countable representation and find a summable / index-like substitute for the missing trace that uses the extra `S_4` symmetry or the exact one- and two-color marginal identities.

## 12. Next nonrepeating methods

The next methods are

- **#11 DUALIZE** — rewrite `(COUNTABLE-HL)` as a nonnegative factorization / Hankel-operator problem for the exact cylinder-probability matrix of `X_HL`;
- **#12 FIND WHAT IS CONSERVED** — search for an excursion or operator index invariant that survives countable positive recurrence but is incompatible with the 4-color identities;
- **#14 FIND THE GROUP ACTING** — exploit full `S_4` color symmetry to decompose the hypothetical hidden representation/operator into isotypic sectors before attempting an infinite-dimensional trace substitute.

These are genuinely different from the handoff triple used in this run.

## 13. Exact-checking discipline

No finite claim requiring a checker was made, so no `artifacts/R14/` file was manufactured. The substantive new claim is theorem-sized and its proof is on the page. It still requires independent outside-track audit before it could be treated as a closure component; it is not self-audited into PROVED source status.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD OUTSIDE
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  previous_target:
    id: D0039
    source: "Virag, Operator limits of random matrices, Question 1"
    status: "PARTIAL / OPEN / TERMINAL-HANDOFF"
    metric: B_spectrum
    before: 2
    after: 2
    terminal_frontier: BLOCK_3_8_same_environment_conditional_descendants
  active_target:
    id: D0034
    source: "Bradley 2005, Basic Properties of Strong Mixing Conditions, Question 6"
    status: "PARTIAL / OPEN"
    claim_path: operations/claims/D0034.md
    claim_commit: c6a42e9f8e2b7bb8b3fb5578a9827e4a212e4e4e
    fixed_candidate: "Holroyd-Liggett stationary 1-dependent 4-coloring"
    metric: N_rep
    metric_definition: "hidden-state cardinality regimes still requiring exclusion after finite-state impossibility"
    before: 2
    after: 1
    remaining_obligation: COUNTABLE-HL
    authoritative_stagnation_count: UNKNOWN
  methods: [1, 20, 28]
  substantive_results:
    - "countable-output Harris-collapse lemma: a countable-output stationary factor of a stationary Harris recurrent chain has a stationary irreducible positive recurrent countable-state Markov representation"
    - "ergodic-component reduction: for X_HL it suffices to exclude one irreducible positive recurrent countable hidden class"
    - "Berbee-Bradley Lemma 4.1 obstruction is unusable for psi-mixing because psi-mixing already has the property"
    - "Schramm trace proof fails in countable state exactly because the relevant operator need not be trace class"
  novelty: "UNVERIFIED / likely folklore for the Harris-collapse lemma; no novelty claim"
  new_finite_claims: 0
  checker: none
  next_methods: [11, 12, 14]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  permission_changes: false
  workflow_execution: false
  scheduler_modified: false
```

## 15. Model / scheduler-control status

The model-control limitation remains unchanged in the exposed scheduling surface: there is no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains request text rather than verified execution metadata, and this report does not claim otherwise.

For a task that returns `You cannot modify this task`, the permitted workaround remains the authorized owning/admin context, a supported ownership/admin change, or platform support. No permission bypass, duplicate task, or scheduler mutation is attempted here.
