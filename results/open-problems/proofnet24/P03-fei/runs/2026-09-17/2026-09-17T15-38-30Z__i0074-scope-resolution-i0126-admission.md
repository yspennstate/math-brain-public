Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, or applied-routing receipt, so I do not claim GPT-6 or maximum reasoning. **SUCCESSOR ADMITTED: I0126 / Kelly–Ulam Graph Reconstruction Conjecture. Active source metric `n_recon^cert: 13 -> 13`, NO MOVEMENT on the first attack. I0074 remains unclaimed and NOT READY after exact scope reconciliation. Methods for the I0126 first attack: #1 CHANGE THE CATEGORY, #14 FIND THE GROUP ACTING, #20 FIND WHY THE ALGORITHM FAILS.**

# P03 HARD OUTSIDE — I0074 exact scope reconciliation, I0126 admission, and first extension-collision attack

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Entry state: `TH17_KNOWN / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED`.  
Predecessor report: `proofnet24/P03-fei/runs/2026-09-17/2026-09-17T14-41-51Z__successor-admission-hold-i0074-scope.md`, creation commit `13a765cc98915eae65fd61393457d91577ed50e6`, blob `b907861e6989298aef7b9a95f1ff58e17e5834af`.

## 1. Metric and status first

The admission-only predecessor had no live successor metric. This run finishes the I0074 gate, then lawfully admits a different HARD OUTSIDE successor.

New active target:

**I0126 — Kelly–Ulam Graph Reconstruction Conjecture.** Every finite simple graph on at least three vertices is determined, up to isomorphism, by the multiset of its one-vertex-deleted induced subgraphs.

Frozen source-matching metric:

`n_recon^cert` = largest integer `n` for which a rigorous theorem proves that **every** finite simple graph on at most `n` vertices is reconstructible from its full vertex deck.

Supported baseline and after-state:

`n_recon^cert: 13 -> 13` — **NO MOVEMENT**.

The baseline is Brendan McKay, *Reconstruction of Small Graphs and Digraphs*, arXiv:2102.01942v4 / Australasian Journal of Combinatorics (2022), which proves the conjecture for all graphs through order 13. The old owner-requested queue note saying the verified order was believed 11 is stale and is not used.

Broad target status: **OPEN / PARTIAL**. A proof at order 14 would move the metric to 14 but remain PARTIAL for the unrestricted conjecture. One pair of nonisomorphic finite simple graphs with identical vertex decks would REFUTE the source.

No finite experiment, heuristic collision count, or unverified external computation moves this metric.

---

## 2. Repository continuity and ownership

I reread/recovered the required current repository surfaces before assignment: root `README.md`; `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`; current `FLEET_RULES.md` and NEW-METHODS controls; `operations/FLEET_2026-09-16.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the newest P03 report; current canonical claims used in screening; the earlier I0074 admission material; the R09 I0126--I0129 successor screen; and the newest accessible P04/I0101 report used for the directed audit.

Large root/intake surfaces are connector-truncated when rendered wholesale. I used exact-path / exact-ID reads and searches and do **not** claim a byte-for-byte visible reread of every intake row.

Current exclusions were rechecked rather than inherited blindly. In particular, I0123/Borsuk and I0127/Seymour have canonical owners, as do the earlier I0078/I0028 reserve rows. TH18, RS-2026-BIS32, the complete-mixability family, FEI, Salez I0111 and Manhattan I0003 remain unavailable to P03 under the recorded ownership/handoff state.

Immediately before claiming I0126, direct fetch of `operations/claims/I0126.md` returned 404. Repository search recovered only queue/admission-screen material and no canonical owner. I therefore created the canonical claim **create-only**, without overwriting another owner:

`operations/claims/I0126.md`

Creation commit: `a8a6793fc851824ab1e85568ab729e3c52291fda`.  
Readback blob: `7bc60b5449d3cef5b461da8b635f57d6c9fb963c`.

The claim was read back at that exact creation commit before substantive successor work continued.

---

## 3. Mandatory I0074 reconciliation — exact answer is still PENDING, but the blocker is now sharp

Candidate I0074 is David Aldous, *Note: a conjectured compactification of some finite reversible MCs*, Conjecture 1. The source says: sample iid stationary points `xi_i`, form the function-valued array

`X^*_{ij}(t)=p^*(xi_i,xi_j;t)`,

let `Psi` be its law, and conjecture that two symmetric Markov processes with the same `Psi` are isomorphic.

The decisive issue is not vague overlap with later work. It is the exact class of processes.

### 3.1 Aldous's literal source class is under-specified at exactly the dangerous point

Aldous Section 0.3 views a stationary symmetric Markov process as transition densities satisfying Chapman--Kolmogorov **“with a UTC on the t downarrow 0 behavior”**; the footnote says only **“unspecified technical condition.”** His isomorphism is described by a **bijection** of state spaces preserving the stationary two-time laws/transition densities. Section 0.5 again lists “the UTC from section 0.3” among the intrinsic array axioms without defining it.

Thus there is no source-exact predicate by which a later example can be checked for membership in Aldous's intended class.

### 3.2 Towsner's explicit class is not the same stated class

Henry Towsner, *Limits of Sequences of Markov Chains*, arXiv:1404.3815v3 / EJP 20 (2015), Definition 2.6 defines a pseudofinite chain by stochasticity, symmetry, Chapman--Kolmogorov, diagonal Chapman--Kolmogorov, finite trace, normalization, and **L2 continuity at every t>0**. There is no identity-separating or other stated condition at `t downarrow 0`.

This matters because Section 7 starts by asking for exactly the naive same-array uniqueness and then says explicitly that it is **false** in the pseudofinite class. Towsner takes a two-point chain and replaces one atom by an uncountable blob of indistinguishable points. The original and blown-up chains have the same density array but are not isomorphic; blowing up opposite atoms gives examples neither of which embeds in the other.

So, under Towsner's explicit pseudofinite axioms:

`same density array => original-chain isomorphism` is **REFUTED**.

### 3.3 What Towsner actually proves

Towsner's repair is canonicalization, not proof of naive uniqueness for the original objects.

- Definition 7.1: `saturated` means every wide type is realized; `twin-free` means no type is realized by more than one point.
- Lemma 7.3: every pseudofinite chain maps measure-preservingly to a twin-free saturated chain preserving the kernels. This map can collapse indistinguishable points and need not be an isomorphism of the original chain.
- Theorem 7.5: if two pseudofinite chains are twin-free and saturated, have the same density array, and their sigma-algebras are the smallest ones making the kernels measurable, then there is a measure-preserving bijection **up to null sets** between them.

Hence the refined/canonical uniqueness statement is **KNOWN**, but it has extra hypotheses and an a.e. isomorphism convention not literally identical to Aldous's source wording.

### 3.4 Admission decision for I0074

The Towsner blob counterexample is extremely likely to be exactly why Aldous inserted a `t downarrow 0` technical condition: instantaneous indistinguishable twins are what a small-time identity condition would normally exclude. But Aldous did not state the condition, so I cannot prove that Towsner's pair is source-valid, nor can I prove that the intended UTC implies twin-freeness/saturation or upgrades an a.e. canonical representative to Aldous's literal bijective process isomorphism.

Therefore the honest disposition is option (d):

`I0074 = UNASSIGNED_RESERVE / PENDING_SOURCE_CLASS_UNDERSPECIFIED / NOT READY`.

More precisely:

- naive uniqueness on Towsner's explicit pseudofinite class: **REFUTED**;
- uniqueness of Towsner's canonical twin-free saturated representatives with minimal sigma-algebra: **KNOWN** up to null sets;
- Aldous literal Conjecture 1 with its unspecified UTC and stronger direct-isomorphism wording: **PENDING**, because source membership of the counterexample and equivalence with Towsner's refined class cannot be checked.

This is a scope resolution, not a claim that a failed literature search proves openness. I0074 remains unclaimed.

Aldous's current compactification status page still says Towsner supplies a measure-theoretic limit construction while obtaining the desired nice topological version remains open. That broader open topological problem is not silently substituted for literal Conjecture 1.

---

## 4. Why I0126 is the next lawful HARD successor

After I0074 remained NOT READY, I advanced into the newly replenished finite/famous reserve rather than recycling already-owned rows.

- I0123/Borsuk is already claimed HARD OUTSIDE.
- I0127/Seymour is already claimed HARD OUTSIDE.
- I0128/Sendov's queued scope was screened elsewhere as overtaken by a 2026 full proof.
- I0129/Singmaster is HARD but follows I0126 in the replenished cursor and its queued finite-search quantity is not the source's universal boundedness quantifier.
- I0126 remained unowned at the pre-claim snapshot.

Fresh status checks support I0126 as genuinely current and HARD:

1. Dufresne--Jeronimo--Kenkel--Lindo--Villamizar, arXiv:2604.16567 (17 Apr 2026), states the exact full Graph Reconstruction Conjecture and develops an invariant-theoretic approach without resolving it.
2. McKay's 2022 exact computation proves all graphs through 13 vertices and some limited larger classes, not all order-14 graphs.
3. Aravind--Monikandan, arXiv:2601.00620 (2 Jan 2026), gives new structural reductions and reconstructible pair parameters but still states RC as open.
4. A fresh bounded September-2026 search recovered modern sources continuing to call the unrestricted conjecture open; no accepted source-matching proof or counterexample was found. A 2026 formally verified weak bipartite result is materially restricted and is not promoted to the full source.

Negative search evidence is not a novelty certificate. The combination of exact source, current-open status, HARD lane fit and cleared ownership is enough for admission.

---

## 5. First research idea, before code

**Idea.** Do not enumerate 14-vertex graphs directly. A hypothetical order-14 counterexample pair has a common 13-vertex card. Fix that card as a base graph `C` and rewrite both parents as one-vertex extensions of the same `C`. Then the entire order-14 conjecture becomes an exact collision problem for subset orbits under `Aut(C)`.

This attacks the negation first while changing category from “pairs of huge unlabeled graphs” to “extension signatures over a fixed base graph.” No code is needed to prove the reduction, and I did not manufacture a checker merely to obtain a receipt.

The three Section-B methods are deliberately new relative to the predecessor screens:

- **#1 CHANGE THE CATEGORY** — graph pairs -> one-card extension collisions / invariant signatures;
- **#14 FIND THE GROUP ACTING** — `Aut(C)` acts on possible neighborhoods of the added vertex;
- **#20 FIND WHY THE ALGORITHM FAILS** — locate the exact global bottleneck after the local extension search becomes finite.

---

## 6. Exact extension-collision reformulation

Let `C` be any graph on `n-1` vertices and let `A subseteq V(C)`. Write `G_A` for the graph obtained by adding one new vertex `z` adjacent exactly to the vertices of `A`.

Define the extension-deck signature

`Phi_C(A) := D(G_A)`,

the full unlabeled vertex-deleted deck of the parent extension.

### Proposition — exact order-n counterexample criterion

For every `n >= 3`, the Graph Reconstruction Conjecture fails at order `n` **if and only if** there exist an `(n-1)`-vertex graph `C` and subsets `A,B subseteq V(C)` such that

1. `G_A` and `G_B` are nonisomorphic, and
2. `Phi_C(A)=Phi_C(B)` as multisets of unlabeled `(n-1)`-vertex graphs.

Moreover any such collision necessarily has `|A|=|B|`; and if `A` and `B` lie in the same `Aut(C)` orbit then the two extensions are isomorphic, so only distinct subset orbits can participate in a genuine counterexample.

### Proof

**Forward direction.** Suppose `G,H` are nonisomorphic `n`-vertex graphs with the same deck. Choose any card occurrence from the common deck. Thus there are vertices `u in V(G)`, `v in V(H)` and an `(n-1)`-vertex graph `C` with

`G-u ~= C ~= H-v`.

Fix isomorphisms of both cards with one common copy of `C`. Let `A` be the image in `C` of `N_G(u)` and `B` the image of `N_H(v)`. Then `G ~= G_A`, `H ~= G_B`, and the original deck equality says exactly `Phi_C(A)=Phi_C(B)`. Nonisomorphism of `G,H` gives condition 1.

**Reverse direction.** If such `C,A,B` exist, then `G_A,G_B` are by assumption nonisomorphic graphs with identical vertex decks, hence are a counterexample at order `n`.

**Equal sizes.** The total number of edges is reconstructible from a vertex deck because each parent edge occurs in exactly `n-2` cards. Thus equal decks imply `|E(G_A)|=|E(G_B)|`. Since both contain the same base `C`,

`|E(G_A)|=|E(C)|+|A|`, `|E(G_B)|=|E(C)|+|B|`,

so `|A|=|B|`.

**Group quotient.** If an automorphism `sigma in Aut(C)` sends `A` to `B`, extend `sigma` by fixing the new vertex. It is then an isomorphism `G_A ~= G_B`. Hence a genuine collision must use different `Aut(C)`-orbits. QED.

I label this result **`P03-I0126-EXTENSION-COLLISION-247 = PROVED / EXACT-REFORMULATION / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`**. It is elementary and may be implicit in reconstruction algorithms; I do not claim publication novelty. Its value is operational: it states exactly what an order-14 negation search must find.

For `n=14`, each fixed 13-vertex base has only `2^13=8192` raw neighborhood subsets before quotienting by `Aut(C)` and by equal neighborhood size. Thus the local collision test is finite and exact, and automorphisms can reduce it further.

---

## 7. #20 — why this algorithm does not yet move 13 to 14

The reformulation removes the **parent** explosion but not the **base-card** explosion. To prove order 14 globally, one still needs to rule out extension-deck collisions for every 13-vertex base graph `C` (or prove a structural theorem covering them in classes). There are far too many unlabeled 13-vertex bases for a naive P03 sweep, and an unreviewed external enumeration would violate the compute/script discipline anyway.

So the exact failure formula is now:

`n_recon^cert >= 14`

would follow from

`forall C on 13 vertices, forall distinct Aut(C)-orbits [A],[B] with |A|=|B|: Phi_C(A) != Phi_C(B) whenever G_A !~= G_B`.

This is an exact finite statement, but the universal quantifier over `C` is the blocker.

The closest current structural reduction is KNOWN prior art, not P03 novelty: Aravind--Monikandan Theorem 7 reduces full RC to 2-connected graphs satisfying either `gamma(G)=2` or `diam(G)=diam(complement G)=2`. Therefore an order-14 proof may restrict the parent extensions `G_A` to that union without loss. Their paper also notes disconnected graphs are reconstructible and uses complement symmetry.

The next attack should combine the extension-collision formulation with that reduction: prove extension-rigidity uniformly for one of those two 14-vertex parent classes, rather than enumerate arbitrary bases.

### Prior-art route kill

I also checked the tempting shortcut “a unique asymmetric `(n-2)`-vertex subgraph lets us glue two cards canonically.” That mechanism is already squarely in the anchor/asymmetry literature (Farhadian 2016/2017 and older unique-subgraph reconstruction work). I therefore do **not** repackage it as P03 progress. It remains useful as a filter: bases/parents with a suitable anchor can be removed before attacking the symmetric residue.

Exact remaining source obligation after this run:

- either prove no extension collision exists for every 13-vertex base compatible with the two known reduced parent classes, thereby moving `n_recon^cert` from 13 to 14;
- or exhibit one exact nonisomorphic collision with identical full decks, which would refute the conjecture.

---

## 8. Source and prior-art record for I0126

Primary/current formulation used for status:

- Emilie Dufresne, Gabriela Jeronimo, Jenny Kenkel, Haydee Lindo, Nelly Villamizar (2026), *Shuffling the Deck: Invariant Theory and the Graph Reconstruction Conjecture*, arXiv:2604.16567v1. Exact source model: finite simple undirected graph, vertex-deleted deck, isomorphism.

Certified finite baseline:

- Brendan D. McKay (2022), *Reconstruction of Small Graphs and Digraphs*, arXiv:2102.01942v4: all graphs through 13 vertices.

Current reductions / nearby work checked:

- J. Antony Aravind and S. Monikandan (2026), arXiv:2601.00620: RC reduction to 2-connected `gamma=2` or two-diameter-2 cases and reconstructible pair parameters in a large complementary regime.
- Dufresne et al. 2026: invariant-theoretic orbit/separating-set viewpoint.
- Farhadian 2016/2017: unique induced anchors/asymmetry reconstruction; this kills the temptation to claim the anchor gluing observation as new.
- modern 2026 weak bipartite/formal reconstruction results: materially restricted, not the source theorem.

A fresh dated search did not recover an accepted full proof or counterexample. Search misses are bounded evidence only.

---

## 9. Directed P04 / I0101 second audit — new claim 25

Audited peer file:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T14-00-25Z__run-report.md`

Creation commit: `ef655e1ba4fbd5b9b0510437d8bcb89800dee19a`.  
Verified report blob at that commit: `69c25fc0c11d52d5af6cde80400dae53afa90578`.  
Peer claim: `P04-I0101-LEVEL4-SIXCHANNEL-LIFT-25`.

This is not P03's already-audited anharmonic-parity claim 23, sparse-tangent claim 24, or any earlier P03 audit.

### Claim under audit

For `p == 5 (mod 24)`, set

`V={x !=0,1 : chi(x)=chi(x-1)=1}`,

`D_p=P^1(F_p) \ {0,infinity,t:t^4=1}`,

and

`x(t)=((1-t^2)/(1+t^2))^2`.

The claim says `x:D_p->V` is exactly four-to-one with deck group `K=<t->-t,t->1/t>`, while `R=J o x` is a 24-sheeted octahedral cover of `U_p=J(V)`. Every one of the six anharmonic block signs `chi(x(t)-g x(s))` lifts to the quadratic character of a fixed degree-four rational factor in level-4 coordinates, and their product is `chi(R(t)-R(s))`.

### Independent verification

1. Since `p==5 mod24`, `p==1 mod4`; all four fourth roots of 1 are rational and distinct. Thus `|D_p|=(p+1)-6=p-5`.

2. Direct algebra gives

`1-x(t)=4t^2/(1+t^2)^2`.

On `D_p`, denominators are nonzero and both `x(t)` and `1-x(t)` are nonzero squares, hence `x(t) in V`.

3. If `x(s)=x(t)`, writing `z=t^2,w=s^2` shows

`(1-w)/(1+w)= +/- (1-z)/(1+z)`.

The plus sign gives `w=z`; the minus sign gives `w=z^{-1}`. Hence the fiber is exactly

`{t,-t,t^{-1},-t^{-1}}`,

so the fiber group is the stated Klein four group and `x` is exactly four-to-one.

4. Substituting `x(t)` into

`J(x)=(x^2-x+1)^3/[x^2(1-x)^2]`

gives

`R(t)=(t^8+14t^4+1)^3/[16 t^4 (t^4-1)^4]`.

The numerator identity follows by multiplying

`(t^4-2t^3+2t^2+2t+1)(t^4+2t^3+2t^2-2t+1)=t^8+14t^4+1`.

5. Let `i^2=-1`. Direct substitution gives

`x(i t)=x(t)^{-1}`

and, for `s(t)=(1-t)/(1+t)`,

`x(s(t))=1-x(t)`.

These induce the two standard anharmonic generators modulo `K`. The six quotient transforms have four lifts each, and distinct quotient images cannot lie in the same `K` fiber; hence the generated projective Möbius group has exactly `4*6=24` elements. They all preserve `R=J o x`. Since `deg R=24`, this is the full generic deck group.

6. Independent expansion gives the exact difference formula

`x(t)-x(h) = -4 (h-t)(h+t)(th-1)(th+1) / [(1+t^2)^2(1+h^2)^2]`.

The denominator is a square. Also `chi(-4)=1` because `p==1 mod4`. If `h=gamma(s)` is a Möbius lift, clearing its denominator across the four factors contributes a fourth power, again invisible to quadratic character. Therefore

`chi(x(t)-g x(s))`

is indeed the quadratic character of a fixed four-factor rational expression, uniformly in `p`.

7. Finally, the exact anharmonic factorization

`J(X)-J(Y)`

has, after removal of its square denominator, the six factors

`(X-Y)(XY-1)(X+Y-1)(XY-X+1)(XY-X-Y)(XY-Y+1)`.

These are the six relative transforms `X-gY` up to factors that are squares on `V` (and `-1` is a square here). Thus multiplying the six lifted signs gives exactly

`chi(J(x(t))-J(x(s))) = chi(R(t)-R(s))`.

### Audit verdict

`P03-AUDIT-P04-I0101-LEVEL4-SIXCHANNEL-LIFT-248 = PASS (CLAIM-SCOPED)`.

The algebraic cover and six-channel lift are correct. This audit does **not** prove Randomstrasse Conjecture 27, does not certify P04's extreme spectral edge, and does not audit P04 claim 26. No peer file was edited.

---

## 10. Failed routes and next obligation

Failed / killed routes this run:

- **Promote I0074 as KNOWN from Towsner:** false. Theorem 7.5 is a canonical refined uniqueness theorem, while Section 7 explicitly refutes naive uniqueness on the unrefined pseudofinite class.
- **Promote I0074 as REFUTED in Aldous's literal source scope:** unsupported. Aldous's `t downarrow 0` UTC is explicitly unspecified, so Towsner's instantaneous-twin blowup cannot be certified source-admissible.
- **Promote I0074 as OPEN because the topological compactification is still open:** scope error; that is a broader/different issue.
- **Use the old I0126 `n<=11` queue baseline:** stale; rigorous current baseline is 13.
- **Brute-force arbitrary 14-vertex parents:** category changed to exact extension collisions, but the universal base-card quantifier remains too large.
- **Claim unique-anchor gluing as new:** killed by Farhadian/older anchor prior art.

Next P03 research obligation on I0126: combine the extension-collision criterion with the known Aravind--Monikandan reduction and prove a uniform no-collision theorem for one entire reduced order-14 parent class, preferably the `gamma(G)=2` class first. Do not run an unaudited all-graphs enumerator.

Suggested next Section-B triple, different from this run and prior screens: **#6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #24 FIND THE EXTREMAL OBJECT**.

---

## 11. `ledger_delta` for P26

```json
{
  "worker": "P03",
  "deployment": "HARD_OUTSIDE_SUCCESSOR_ADMISSION",
  "predecessor": {
    "target": "RS-2025-TH17",
    "status": "KNOWN_RETIRED",
    "metric": "U_theta^cert",
    "value": 1
  },
  "i0074_scope": {
    "status": "UNASSIGNED_RESERVE__PENDING_SOURCE_CLASS_UNDERSPECIFIED__NOT_READY",
    "towsner_unrefined_naive_uniqueness": "REFUTED",
    "towsner_twinfree_saturated_minimal_sigma_uniqueness": "KNOWN_AE",
    "aldous_literal_scope": "PENDING_UNSPECIFIED_tDOWN0_UTC_AND_ISOMORPHISM_MISMATCH",
    "claim_created": false
  },
  "successor": {
    "target": "I0126 / Kelly-Ulam Graph Reconstruction Conjecture",
    "claim_path": "operations/claims/I0126.md",
    "claim_creation_commit": "a8a6793fc851824ab1e85568ab729e3c52291fda",
    "claim_blob": "7bc60b5449d3cef5b461da8b635f57d6c9fb963c",
    "lane": "HARD_OUTSIDE",
    "status": "OPEN_PARTIAL",
    "metric": "n_recon^cert",
    "before": 13,
    "after": 13,
    "movement": "NO_MOVEMENT",
    "baseline_source": "McKay 2022 all graphs through order 13"
  },
  "claim_247": {
    "id": "P03-I0126-EXTENSION-COLLISION-247",
    "status": "PROVED_EXACT_REFORMULATION_PARTIAL_NOVELTY_UNVERIFIED",
    "metric_movement": false
  },
  "methods_used": [1, 14, 20],
  "next_methods": [6, 12, 24],
  "peer_audit": {
    "id": "P03-AUDIT-P04-I0101-LEVEL4-SIXCHANNEL-LIFT-248",
    "peer_claim": "P04-I0101-LEVEL4-SIXCHANNEL-LIFT-25",
    "peer_path": "proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T14-00-25Z__run-report.md",
    "peer_creation_commit": "ef655e1ba4fbd5b9b0510437d8bcb89800dee19a",
    "peer_blob": "69c25fc0c11d52d5af6cde80400dae53afa90578",
    "verdict": "PASS_CLAIM_SCOPED"
  },
  "shared_roots_edited": false,
  "peer_files_edited": false,
  "email": false,
  "drive": false,
  "public_posting": false,
  "paid_compute": false,
  "permission_changes": false,
  "workflow_execution": false
}
```

**End of complete run report.**
