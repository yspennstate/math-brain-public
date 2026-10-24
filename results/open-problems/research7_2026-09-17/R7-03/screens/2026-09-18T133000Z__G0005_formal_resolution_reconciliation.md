# R7-03 admission-side source reconciliation: G0005 has a source-matching formal resolution claim

Date of check: 2026-09-18.

Slot: R7-03 (`6aabe7be74008191b526b109ee4e9e80`).

This is an admission-side reconciliation, not a claim of R7-03 ownership and not a repository-wide status edit. No `operations/claims/G0005.md` is created here.

## 1. Source scope recovered

Outside source: Gady Kozma and Shahaf Nitzan, **“A reduction of the $\theta(p_c)=0$ problem to a conjectured inequality”**, 2024, arXiv:2401.12397.

Primary locator: Conjecture 3, p. 15 (with the finite-graph setup and arbitrary independent edge probabilities defined earlier in the paper). The source's Conjecture 3 is the uniform near-one gluing assertion:

> For every `epsilon > 0` there exists `delta > 0`, independent of the finite graph and relay-set size, such that if `P(o <-> A) > 1-delta` and `P(a <-> b) > 1-delta` for every `a in A`, then `P(o <-> b) > 1-epsilon`.

The historical intake row `G0005` records the constant-edge-probability specialization of this statement. Therefore a theorem for arbitrary edge weights in `[0,1]` is stronger than, and in particular closes, the intake scope.

## 2. Direct inspection of the pinned formal artifact

I inspected the public `anthropics/formal-math` artifact at pinned commit

`795efb86f191735c5481675763537cfb4ff37e55` (2026-08-28).

The following are direct source-level facts from that pinned tree.

### 2.1 Exact formal statement

`percolation/Percolation/Continuity/Statements.lean` defines `NearOneGluing` as

```text
forall epsilon : R, 0 < epsilon -> exists delta : R, 0 < delta and
forall n, w : Sym2 (Fin n) -> [0,1], A, o, b,
P_w(o <-> A) > 1-delta ->
(forall a in A, P_w(a <-> b) > 1-delta) ->
P_w(o <-> b) > 1-epsilon.
```

The file explicitly identifies this proposition as Kozma--Nitzan Conjecture 3 and notes that its content is uniformity in `|A|`.

The same file defines the stronger **additive gluing** statement:

```text
if t >= 0 and P_w(a <-> b) >= 1-t for every a in A,
then P_w(o <-> b) >= P_w(o <-> A)-t.
```

Here the weights are arbitrary pairwise Bernoulli probabilities in `[0,1]`; weight zero encodes an absent edge.

### 2.2 Closed theorem declarations

`percolation/Percolation/Continuity/MainTheorem.lean` contains the closed theorems

```text
theorem additiveGluing_holds : AdditiveGluing := ...
theorem kozmaNitzan_conjecture3_holds : KozmaNitzan2024_conjecture3 := ...
```

and states explicitly that the latter uses `delta = epsilon/2`.

The same pinned release states that the principal declarations depend only on the standard Lean axioms `propext`, `Classical.choice`, and `Quot.sound`; the release's own audit records no `sorry` outside the two deliberate statement-file placeholders.

## 3. Independent semantic bridge: additive gluing implies exactly Conjecture 3

This implication is elementary and removes the main semantic ambiguity relevant to G0005.

Fix `epsilon > 0` and put

`delta = epsilon/2 > 0`.

Assume the exact source hypotheses

`P(o <-> A) > 1-delta`

and

`P(a <-> b) > 1-delta` for every `a in A`.

Because strict inequality implies weak inequality, additive gluing with `t=delta` gives

`P(o <-> b) >= P(o <-> A)-delta`.

Hence

`P(o <-> b) > (1-delta)-delta = 1-epsilon`.

The same `delta(epsilon)=epsilon/2` works simultaneously for every finite graph, every relay set `A`, all vertices `o,b`, and every independent edge-weight function. Thus the pinned formal theorem matches all of the source quantifiers and is stronger than the constant-parameter `G0005` intake formulation.

This semantic bridge does not require the lattice reduction, any asymptotic limit, or an interpretation of `theta(p_c)`: it stays entirely inside the finite-graph source statement represented by G0005.

## 4. Further bounded follow-up: the stronger post-FKG conjecture also now has a formal claim

A separate public follow-up, **“Kozma--Nitzan inequalities: proofs and counterexamples”**, last updated 2026-09-05, reports a Lean development in `nitromannitol/percolation-after-anthropic` and observes that the Anthropic proof's intermediate first-contact inequality (GEN) yields the stronger Kozma--Nitzan Conjecture 1:

`P(o <-> b) >= P(o <-> A) min_{a in A} P(a <-> b)`.

The displayed argument is transparent once GEN is granted. If the first-contact events `E_a` partition `{o <-> A}`, then

`P(o <-> b, o <-> A) >= sum_a P(E_a) P(a <-> b)`

`>= min_a P(a <-> b) sum_a P(E_a)`

`= P(o <-> A) min_a P(a <-> b)`.

Dropping `{o <-> A}` on the left gives Conjecture 1. The follow-up page states that this and the remaining Kozma--Nitzan conjectures/questions are Lean-checked in its linked repository. This is not needed to exclude G0005: the older pinned Anthropic theorem already directly proves Conjecture 3. It does, however, show that the restricted unique-`o`--`b`-path theorem proved by R7-03 in the preceding run is now subsumed by a later public claim covering arbitrary finite weighted graphs.

## 5. Dated public verification/status evidence

Bounded checks on 2026-09-18 found:

1. The original 2024 Kozma--Nitzan source still provides the exact historical statement and arbitrary-edge-weight setup.
2. A 2026-09-03 Latent Seminar report identifies the pinned 2026-08-28 Lean artifact, explains that additive gluing gives Conjecture 3 with `delta=epsilon/2`, and clearly labels the artifact unrefereed.
3. A VibeMathed entry submitted 2026-09-08 reports an independent statement-level audit of the pinned lattice formalization and its trust boundary. It did not rebuild the full release and explicitly notes lack of ordinary mathematical peer review.
4. Gil Kalai's 2026-09-03 report publicized the formal solution claim with caveats; a comment on the same page points to the later verification of the remaining Kozma--Nitzan conjectures.
5. The 2026-09-05 `kn1-verification-b80e9` page reports the stronger Conjecture 1 and other follow-ups as Lean-checked.

These checks are sufficient for **admission exclusion**: G0005 is not an honest currently-open CLOSABLE source to assign to R7-03. They do **not** authorize R7-03 to edit the shared `QUEUE.md`, `RESULTS.md`, or `POSTED.md`, and they do not transform an unrefereed formal release into a peer-reviewed publication.

## 6. Section-B admission-side methods

### B18 — say the statement in another language

Translated the Lean `NearOneGluing` and `AdditiveGluing` propositions into the exact probability/quantifier language of the 2024 source. Outcome: exact source match, with arbitrary edge weights rather than only constant `p`.

### B27 — swap the order of quantifiers

Checked the dangerous uniformity point directly. The formal statement is `forall epsilon, exists delta, forall n,w,A,o,b`, not a graph-dependent or `|A|`-dependent modulus. Therefore `delta=epsilon/2` has exactly the source-required quantifier order.

### B22 — read the failure/trust boundary

Separated four claims that must not be conflated: (i) kernel checking of a formal proposition, (ii) semantic match of that proposition to Conjecture 3, (iii) the subsequent lattice theorem, and (iv) conventional independent peer review. For G0005 only (i)+(ii) matter for admission; the direct statement inspection plus the elementary bridge resolves (ii), while ordinary peer review remains pending.

## 7. Operational conclusion for R7-03

- **Do not create a G0005 ownership claim.**
- **Do not treat G0005 as current open inventory.**
- R7-03 remains `PENDING_ADMISSION` for a fresh residue-2, unclaimed, source-current, genuinely CLOSABLE OUTSIDE problem.
- Successor mathematical metric remains `UNKNOWN/UNMEASURED`; no target-specific stagnation counter starts.
- The previous R7-03 unique-path theorem remains mathematically valid as a restricted argument, but it is not a source-level novelty candidate after the 2026-09-05 stronger public follow-up.

No shared ledger was edited by this record.
