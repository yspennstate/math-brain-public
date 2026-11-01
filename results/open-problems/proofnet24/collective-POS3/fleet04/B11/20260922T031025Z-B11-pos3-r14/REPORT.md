# POS3 fleet04/B11 — universal shallow-cut concentration in the bounded-variance residue

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose uniform-linear-extension ordering probability lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run stays on the exceptional bounded-variance/high-comparability regime. It does **not** assume a finite kernel. The new point is instead an arbitrary-size, quantitative **finite-depth cut reduction**: in a hypothetical counterexample, more than `80/81` of all extensions cross the first majority block through at most `406` width-two ideal states of depth at most `27`. Moreover more than `17/81` of all extensions realize the first-boundary minority orientation through those same shallow states. The residual posets behind those states may still be arbitrarily large, so this is not a finite census.

## 1. Exact source-bound state consumed

The current source target is the width-at-most-three scope under the uniform law on all linear extensions. The following completed inputs were read before the derivation.

1. **Team lead fleet04/B10, latest complete version.**  
   `proofnet24/collective-POS3/fleet04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`, blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`. It proves that at the first strong-majority Hasse fork the sibling predecessor sets are nested and the proper predecessor difference is a delayed chain. This makes the current lead route a strict nested-predecessor corridor problem rather than an arbitrary two-sided distinguisher problem.

2. **Assigned partner fleet01/B19, latest complete version.**  
   `proofnet24/collective-POS3/fleet01/B19/20260922T024644Z-b19-pos3-r11/REPORT.md`, blob `d1a22bb63b9a5fa57541e1970dac09d7aec14937`. It deletes the first strong-majority element `c`, proves that the set of elements incomparable with `c` is a width-at-most-two ideal, and gives the exact ideal-cut convolution and exact hitting-time tilt. This is applied below as the one-element instance of the new shallow-cut theorem.

3. **Assigned-partner block recurrence used for the block endpoint.**  
   `proofnet24/collective-POS3/fleet01/B19/20260922T021702Z-pos3-b19-r11/REPORT.md`. It proves that the first maximal strong-majority chain block `C` is an order ideal and gives the exact first-interruption renewal decomposition after deleting `C`, with a genuine uniform prefix component of mass `alpha=e(P\C)/e(P)`.

4. **Variance input.**  
   `proofnet24/collective-POS3/fleet03/B10/20260922T0214Z-a03-b10-r11/REPORT.md`, blob `3e50b4d0adaa18c79a96079139d660b832418a2d`. It combines the lead's endpoint pinned-rank atom with Stanley rank log-concavity and Aravinda's sharp discrete log-concave inequality
   `M(X)^2(1+Var(X))<=1`
   to prove that every element in the first or last strong-majority block has rank variance `<65/16`.

5. **Endpoint probability cap.**  
   `proofnet24/collective-POS3/fleet02/B10/20260922T014627Z-fleet02-B10-pos3-r12/REPORT.md`, blob `acdb868b3e35a9248d494126311bfff3bfee150b`. At the first and last strong-majority boundaries it proves the exact strict cap
   `2/3 < p < 7/9`
   and activates both Hasse-blocker channels.

6. **Prior local falsification boundary.**  
   `proofnet24/collective-POS3/fleet04/B11/20260922T021940Z-B11-pos3-r13/REPORT.md`, blob `5075f5ae42742da375b0688cef37dbc8e8c65484`. It refutes the stronger statement that an arbitrary pair balanced in the smaller uniform poset must stay balanced after restoring the exact insertion weights. The induction therefore needs an adaptive/existential transfer, not fixed-pair stability.

External source for item 4: Heshan Aravinda, *Entropy-variance inequalities for discrete log-concave random variables via degree of freedom*, Discrete Mathematics 347 (2024), 113683, DOI `10.1016/j.disc.2023.113683`, Theorem 1.4; its equivalent form is exactly `M(X)^2(1+Var(X))<=1`. The broader bounded-width/range route remains Max Aires and Jeff Kahn, arXiv:2510.26134.

## 2. Compact conditional end-to-end route

Assume for contradiction that POS3 fails and choose a cardinality-minimal counterexample `P`. Let `L_*` be the inherited transitive strong-majority order. Let

`C={c_1<...<c_m}`

be its first maximal contiguous chain block, put `x=c_m`, let `y` be the first element of the second block, and put

`Q=P\C`.

The assigned partner proves that `C` is an ideal and that the exact projected law on `Q` is a mixture of genuine uniform residual-poset laws, with the `C`-prefix component having mass

`alpha=e(Q)/e(P)`.

By minimality, the smaller nonchain `Q` has a balanced pair under its **uniform** law. The unresolved induction step is to choose one that survives the exact projected law, or else force a balanced pair meeting `C`. The previous B11 run shows that an arbitrary uniform-balanced pair need not survive.

The first missing quantitative issue is therefore: **can the nonuniform part of the projection hide its relevant mass arbitrarily deep in an unbounded initial interruption?** The theorem below shows that it cannot. Bounded endpoint rank variance gives a universal, size-independent depth tail.

## 3. The endpoint cut ideal

For a full extension `L in L(P)`, define

`I_x(L)={q in Q : q precedes x in L}`

and put

`J(L)=|I_x(L)|`.

### Lemma 3.1 — width-two endpoint cut

For every `L`, `I_x(L)` is an order ideal of `Q`, every member of `I_x(L)` is incomparable with `x`, and hence all possible `I_x(L)` lie in a width-at-most-two poset.

### Proof

If `q in I_x(L)` and `u<q` in `Q`, then every linear extension places `u` before `q`, hence before `x`, so `u in I_x(L)`. Thus `I_x(L)` is an ideal.

Every element of `Q` lies after `x` in `L_*`. If such a `q` were comparable with `x`, then `q<x` would contradict that `L_*` extends the poset, while `x<q` would force `x` before `q` in every linear extension. Therefore a `q` that actually occurs before `x` is incomparable with `x`.

Let `S_x={q in Q:q||x}`. A three-element antichain in `S_x` together with `x` would be a four-element antichain, impossible at width at most three. Hence `width(S_x)<=2`. `square`

Because the other `m-1` elements of `C` are forced before `x`,

`rank_L(x)=m+J(L)`.                                             (3.1)

Also

`J=0  iff  C is the initial block of L`.                        (3.2)

Consequently

`Pr(J=0)=alpha=e(Q)/e(P)`.                                      (3.3)

This is the block-endpoint analogue of the assigned partner's exact first-element ideal cut. The partner's latest theorem is recovered when `m=1`.

## 4. A universal second-moment bound for interruption depth

The first-block endpoint theorem gives

`Pr(J=0)=alpha>4/9`,                                            (4.1)

and the variance theorem gives

`Var(J)=Var(rank(x))<65/16`.                                   (4.2)

Let `mu=E[J]` and `q=Pr(J=0)`. By Cauchy--Schwarz on the event `J>0`,

`mu^2 <= Pr(J>0) E[J^2] = (1-q)E[J^2]`.

Therefore

`Var(J)=E[J^2]-mu^2 >= q mu^2/(1-q)`,

so, using `q>4/9`,

`mu^2 < (65/16)*(5/4)=325/64`.                                (4.3)

Hence

### Theorem 4.1 — universal endpoint-cut second moment

Every hypothetical width-three counterexample satisfies

`E[J^2] = Var(J)+mu^2 < 65/16+325/64 = 585/64`.                (4.4)

In particular, for every integer `r>=1`,

`Pr(J>=r) < 585/(64 r^2)`.                                     (4.5)

This uses the actual uniform law on `L(P)` throughout. No projected law is replaced by a uniform surrogate.

## 5. The 28-level / 406-state shallow-cut theorem

Taking `r=28` in (4.5),

`Pr(J>=28) < 585/(64*28^2) = 585/50176 < 1/81`,                (5.1)

because `585*81=47385<50176`.

Now choose any two-chain cover of the width-at-most-two poset `S_x`. For an ideal `I subseteq S_x`, its intersection with each chain is a prefix. Therefore `I` is determined injectively by the pair of prefix lengths `(a,b)`. If `|I|=a+b<=27`, the number of possible pairs is at most

`sum_{j=0}^{27}(j+1)=28*29/2=406`.                              (5.2)

Thus:

### Theorem 5.1 — universal shallow endpoint-cut concentration

In every hypothetical width-three POS3 counterexample, at the first strong-majority block endpoint `x`,

> more than `80/81` of all linear extensions have at most `27` elements of `Q=P\C` before `x`, and those extensions are supported on at most `406` possible endpoint cut ideals.

The statement is arbitrary-size. It does **not** say that `P`, `Q`, or any residual poset has bounded size.

By order reversal the same theorem holds at the last majority block.

### Assigned-partner specialization

For the assigned partner's latest one-element deletion, `C={c}` and its cut ideal `I(L)={z:z||c, z<c in L}` is exactly the partner's random ideal. Therefore the same estimate gives

`Pr_partner(|I|>=28)<1/81`,

with more than `80/81` of its exact ideal-cut mixture on at most `406` shallow width-two ideals. This is a direct quantitative application of the latest fleet01/B19 state.

## 6. The first-boundary minority mass is also shallow

The endpoint blocker-product theorem gives

`Pr(x<y)<7/9`,

hence

`Pr(y<x)>2/9`.                                                   (6.1)

Whenever `y<x`, the element `y` belongs to `I_x(L)`, so this is necessarily a non-prefix cut. Combining (6.1) with the deep-cut tail (5.1),

`Pr(y<x and 1<=J<=27)`
`>= Pr(y<x)-Pr(J>=28)`
`> 2/9-1/81 = 17/81`.                                          (6.2)

There are at most `405` nonempty ideals among the shallow states. Therefore:

### Theorem 6.1 — shallow endpoint reversal transport

More than `17/81` of **all** linear extensions realize the minority orientation `y<x` through one of at most `405` nonempty width-two endpoint cut ideals of size at most `27`.

The dual statement holds at the last boundary.

This is stronger than merely saying that the non-prefix component has positive mass. It says that the endpoint reversal flow cannot hide in arbitrarily deep interruptions: a fixed positive fraction of the entire uniform measure is already carried by bounded-depth cut states.

## 7. Exact relation to the latest lead corridor

The newest lead theorem reduces the first Hasse-fork exception to a nested predecessor difference `D`, which is a delayed chain. The present theorem supplies an orthogonal quantitative constraint on that same endpoint: regardless of how long the delayed corridor becomes, all but `<1/81` of the measure crosses the first block through at most `27` incomparable predecessors of `x`, and the first-boundary minority orientation itself has `>17/81` mass inside that bounded-depth envelope.

This does not yet prove that a long delayed predecessor chain is impossible. A delayed distinguisher may affect the sibling comparison while occurring after `x`, so cutting at depth `27` is **not** a finite-kernel proof and does not erase the global corridor. What it does prove is that any successful multi-boundary transport argument may charge the deep-cut contribution by an additive error `<1/81`; the substantial endpoint reversal mass remains in a bounded front layer.

That is precisely the bounded-variance payment missing from the earlier qualitative `7<=pi(P)<=K` residue.

## 8. Remaining essential implication

The adaptive transfer problem is now sharper.

Let `mu` be the exact projected law after deleting the first block and let `mu_<` denote its conditional restriction to the endpoint cut states `|I_x|<=27`. Then

`||mu-mu_<||_TV < 1/81`                                        (8.1)

for events measured only through this cut partition, and in particular every pair-order probability differs from the corresponding shallow/deep decomposition by at most `1/81` when the deep component is discarded and renormalized in the standard mixture bound.

Therefore it is enough to prove an **adaptive shallow-cut selection statement with a `1/81` safety margin**: find an incomparable pair whose probability under the shallow exact mixture lies in

`[1/3+1/81, 2/3-1/81]`,

or derive such a pair meeting the first block. The full law would then be balanced automatically.

What remains genuinely unpaid is the existence of that pair. The `406` shallow states still contain uniform laws on residual posets of unbounded size, so enumerating the states is not a proof. The next useful mechanism is to combine the lead's nested-predecessor corridor and the partner's exact uniform-residual recurrence **inside this shallow envelope**, where the entire uncontrolled deep mass is below the lead's own `1/81` pinned-rank atom.

## 9. Status, failures, and provenance

- POS3: **OPEN / NOT PROVED**.
- Finite-kernel reduction from bounded range/variance: **still unavailable and not assumed**.
- Previous arbitrary-pair transfer shortcut: **still refuted**.
- Universal endpoint-cut second moment `<585/64`: **PROVED**.
- Deep endpoint-cut tail `Pr(J>=28)<1/81`: **PROVED**.
- At most `406` shallow endpoint cut ideals: **PROVED**.
- First-boundary reversal mass `>17/81` inside the shallow envelope: **PROVED**.
- Full adaptive shallow-cut selection lemma: **OPEN**.

No computation was used to establish the mathematical statements in this report; the constants are elementary consequences of the displayed inequalities. No finite experiment is promoted to proof.

No benchmark gold, FEI material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive data, paid model/API/Codex execution, remote workflow, public posting, permission change, or production-brain mutation was used. No authenticated brain retrieval/context use occurred, so this report remains `WITHOUT_VERIFIED_BRAIN`.
