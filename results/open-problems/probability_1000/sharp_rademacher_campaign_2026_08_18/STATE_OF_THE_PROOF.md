# State of the proof: what a complete argument would now have to supply

Author: main session c53c1d50, 2026-08-19 ~06:4x. This assembles the campaign's mathematics into one chain and tests whether the pieces compose. It is the "read one file" document for the mathematics; `ITERATION2_SYNTHESIS.md` remains the adjudicated claim ledger, and where the two differ the ledger's labels win.

**Standing:** the sharp Rademacher singularity conjecture `Pr(det B_n = 0) = (1+o(1))·2n²·2⁻ⁿ` is **OPEN**. Nothing below proves it or any part of it. The block-internal certificate for dense connector-incoherent cores has not moved all campaign.

---

## 1. Where the difficulty is (Layer III)

**The constant names the mechanism.** `2n²2⁻ⁿ` is exactly the expected number of coincident row-or-column pairs — `C(n,2)` pairs × 2 orientations × `2⁻ⁿ`, doubled for columns. So the conjecture asserts that singularity is asymptotically caused by two equal or opposite rows or columns and nothing else. The lower bound is the easy direction; **the whole difficulty is a one-sided upper bound on the non-dominant sum**, which is union-bound shaped.

**The defect is anticoncentration.** In the reconstructed framework a component is `k` rows plus the fibre of their column-restrictions, and a dependency `c` confines that fibre to a hyperplane, giving the identity
  `ℓ = −log₂ Pr[c·x = 0]`.
Erdős's Littlewood–Offord bound then forces **`ℓ ≥ 1`, with equality exactly for support-2 dependencies**, and quantises the bottom of the spectrum: `ℓ = 1` (support 2), then `1.4150` (support 3–4), then `1.6781` (support 5–6). **No component has `ℓ ∈ (1, 1.4150)`.**

**Hence the budget.** Affordability of a slice reads `log₂N_fibre < n(ℓ−1) + 2log₂n − o(n)`. At `ℓ = 1` that is `2log₂n` bits and no exponential room — saturated exactly by the ~`2n²` coincident pairs, which *is* the conjecture's constant. Above the gap the budget is at least `0.415n` bits and at class parameters it is `≈ n(½log₂log n − 1)`, against a naming cost of `≈ nℓ/log n` — a **ratio of Θ(log n)**.

> **Consequence for strategy.** All of the conjecture's difficulty sits at `ℓ = 1` and is a *counting* problem. The entire Layer-II apparatus — rigidity, congestion, absorption, the connector theorem — operates in the regime that has a `log n` factor to spare. That also re-derives the transfer lane's W1 threshold from Erdős rather than from the packet's bookkeeping, explaining where the factor comes from.

*(Caveat carried: this is the reconstructed framework, not the packet's verbatim one; the ambient-vs-Gale-dual parametrization is unresolved, so constants do not transfer. And §1's count is a first moment — a singular matrix has many components.)*

---

## 2. The Layer-II target splits exactly

`dim((R+R_<)/R_<) = dim((R+B)/B) + λ`, with `λ` the leak — so the rooted target is exactly **[quotient bound] + [λ = 0]**, and `λ = dim B̄(ker P)` is the boundary image of the private-part dependencies. The packet's Theorem 1 already bounds the quotient by `2ν + L` with `ν` the two-shadow matching number.

The class splits **disjunctively**: high congestion (horn 1) *or* common-lift failure (horn 2).

---

## 3. Horn 2 — reduced to a definition

1. Horn 2 has bounded congestion, so Theorem 1 already gives clause (i); the whole content is absorption.
2. Under filtration bookkeeping the assembled rank is `O(ℓ) + Λ`, with `Λ` the total pure-leak span — a **global budget** replacing a per-block universal clause that the packet proved underivable from any local hypothesis.
3. The leak is **boundary multiplicity**: `λ ≤ Σ_j(d_j − 1)`, and with the packet's core bound, `λ ≤ (D−1)(2κ+1)L`, so on horn 2 `λ = O(D·L)`.
4. `D ≥ log n` means a large star core; **large stars dissolve** — arm decomposition gives every child the full rooted target at exactly `1/β`, for any size.
5. The class is what survives every *admissible* exchange, so if arm decomposition is admissible, class members have `D = o(log n)` and horn 2 closes under W1.

> **Horn 2's remaining content is two yes/no questions about a definition:** is the arm decomposition an admissible Gale exchange, and does it lift to a block carrying other structure? The term is never defined in the 200 pages, and the tree that defines it is not on this machine.

**[EXTENDED by §8, 2026-08-19 — read it with this section.]** Two *necessary conditions* on "admissible" are now derived rather than guessed (no form spanning incomparable blocks; no rooting that drives `L_{Q|W} → 0` while the dual is untouched), so the term is no longer wholly opaque. Separately, an attempted correction claiming this chain's step 3 **fails** for class members was itself false and was withdrawn — strong connectivity does not forbid cut vertices — so this section's CONDITIONAL labelling stands unchanged.

---

## 4. Horn 1 — a proved obstruction and a structural tension

1. **The packet's own tool cannot close it.** On horn 1, every batching has `ν ≥ (c₀/2−o(1))·log n·log₂log n`, so in the threshold window the support route outputs a coefficient `≥ Θ(log n)` — precisely what the endpoint cannot afford. The deficit is *support versus rank*: every Littlewood–Offord argument in the packet bounds support and then bounds rank by support.
2. **Target R-C** names the repair: selectors whose residual private parts span `O(L)` dimensions inside a core of support `≍ log n·log log n` — a factor-`Θ(log n)` rank compression.
3. **But compression manufactures leaks.** Compressing to private-span `d` over `k` rows creates `k−d` dependencies, and `λ` is exactly their boundary image. So clause (i) and clause (ii) pull against each other, and both hold only when **boundary parts are constant on private-sharing clusters**.

> **Horn 1's remaining content:** a rank compression that follows boundary-constant structure. Not "compress harder" — compress *along* the structure that keeps boundary parts equal.

---

## 5. What a complete proof would now have to supply

1. **Layer III:** the `ℓ = 1` slice handled *exactly* (never by generic machinery — the slice-union costs another `O(log n)` bits, absorbed only under exact treatment), plus multiplicity control for the first-moment overcount.
2. **Horn 2:** the admissibility of arm decomposition, and its lifting. **[EXTENDED by §8, 2026-08-19: two *necessary conditions* on "admissible" are now derived rather than guessed — no full-dual form may span incomparable blocks, and no admissible rooting may drive `L_{Q|W} → 0` while the dual is untouched. Admissibility binds the PAIR (decomposition, rooting). Do not read this item without §8.]**
3. **Horn 1:** Target R-C's rank compression, respecting §4.3's constraint.
4. **Aggregation:** the composition step (G2) — assembling per-block certificates into one global `d_cb` certificate — which remains the telescope reconstruction's one live gap.

---

## 6. The dependency chain, honestly

| Result | Status | Rests on |
|---|---|---|
| ℓ = −log₂Pr; ℓ ≥ 1; the spectral gap | PROVED (Erdős) | reconstructed framework |
| the ℓ = 1 slice is the constant | EXACT arithmetic | folklore, verified twice |
| Layer-III margin Θ(log n) | DERIVED | the framework's interface reading |
| R1 splitting; R2 leak = excess rank | PROVED, elementary | — (**unrefereed**) |
| R3 ν-form; R4 forced deficit | PROVED / CONDITIONAL | dossier's class assertion; **unrefereed** |
| T1a filtration; T1b defect telescoping | PROVED (T1b's acyclicity discharged by SCC condensation) | **UNREFEREED — self-refereed only** |
| horn-2 reduction to Λ | DERIVED | **T1a** |
| leak = boundary multiplicity | DERIVED | packet Theorem 1 |
| horn 2 closes | CONDITIONAL | **T1a** + an undefined term |
| clause tension | PROVED, elementary | R2 |

**Three results and the entire horn-2 chain rest on T1a, which no independent referee has seen.** That is the campaign's largest single exposure, and it is first in line when limits reset.

---

## 7. What has not moved

The block-internal certificate for dense connector-incoherent cores. Every mechanism proved this campaign — DRR, the arm decomposition, the boundary-multiplicity bound — covers the *aligned* or *low-multiplicity* case, which is exactly what incoherence denies. And the campaign still possesses **no explicit member of the residual class**, so every number computed here is a measurement on a known non-member.

---

## 8. Added 2026-08-19 (04:00–11:30): the constant is no longer a free parameter

This section supersedes nothing above; it adds a derivation the chain did not have. Detail and controls: `problem/beta_is_the_absorption_threshold.md`.

**The constant `1/β` is now derived rather than assumed.** The campaign carried `C ≥ 1/β = 1/log₂(4/3) = 2.40942` as a floor forced by NAE three-circuit products. Three facts now sit under it.

1. **The deciding property is absorbability, not `d_cb`.** If a certificate's whole residual space lies in `span W`, clause (ii) gives `R ⊆ R_<` and the target's left side is **0** — whatever the rank, however small `L`. And absorbability has a closed form: with `π` the restriction to coordinates outside `W`, absorbable ⟺ some basis of the dual meets every ±-class of `π(D)`. No rank minimisation required.

2. **`β` is the threshold, and it is universal.** Exhaustively over every NAE-triple set and boundary set (`r ≤ 6`, 393,212 configurations, 17,587 with `L < β`): **no configuration with `L < β` is non-absorbable.** Across constraint types built by forbidding `k` antipodal pattern-pairs on `n` variables, the separation is exact at `β` over two arities and eight types — including the decisive `n=5,k=3` at defect 0.2996, strictly inside the previously-tested gap, predicted absorbable in advance and confirmed.

3. **Why `β`, in the dossier's own units.** `max ψ = 3/4` is the largest fraction of the cube on which a non-coordinate dual form can be `±1`-valued — the dossier's §3.1 tag (13) plus classical Littlewood–Offord at §3.2 tag (14). A private constraint must push its allowed set below `3/4` before an extra dual form, hence any obstruction, can exist. Since the dossier sets `c_s = −log₂ψ(a_s+1)`, this says **`β = min_s c_s`**: the rooted constant `1/β` is the reciprocal of the smallest per-batch cost its congestion bookkeeping can charge. That is why the same constant surfaces independently in the entropy lane and the rigidity lane.

**And it is tight.** At the threshold object — two disjoint NAE triples, `W` equal to one — `L = β` exactly, and the minimum of `dim((R+R_<)/R_<)` over all 2,304 optimal residual spaces is exactly **1**, against a budget of `(1/β)·β = 1.000000`. Equality, zero margin. So on the computable family `1/β` is not merely a floor but **the smallest constant that works, and it is attained**.

**A finding that cuts against the packet's framing.** Minimising the unpaid boundary rank exactly (R7's `μ`), **`μ_min = 0` on every object tested except wheel `k=3` at `|W| = 2`.** Where `μ_min = 0`, R7 alone delivers the rooted estimate with **no absorption hypothesis at all**. The rank lane nominated `μ = O(L)` as the cheapest unexplored hypothesis; on everything computable it holds at zero. Absorption is not the binding constraint on these objects.

**What this does and does not change for §5's four items.** Item 2 (horn 2's admissibility) gains two *necessary conditions* on the undefined term, both derived rather than guessed: no full-dual form may span incomparable blocks (`g2_sharpened.md`), and no admissible rooting may drive `L_{Q|W} → 0` while the dual is untouched (`the_rooting_must_not_explain_away_the_constraints.md`) — so admissibility binds the **pair** (decomposition, rooting). Items 1, 3 and 4 are untouched. **The conjecture remains OPEN**, and the standing exposure is unchanged and now doubly relevant: the campaign still has **no explicit member of the residual class**, so every number in this section is a measurement on a known non-member.

**Corrections logged the same session, since the chain above should not be read as a clean run:** a self-correction of the horn-2 chain that was itself false (strong connectivity does not forbid cut vertices) and was withdrawn; Conjecture R (`d_cb ≤ C·L` naively) falsified with unbounded ratio; the greedy `d_cb` shown loose by up to 3×, which had produced two registered predictions that confirmed the heuristic rather than the mathematics; two failed attempts at the absorption bridge (Criterion C too strict, Claim R′ too permissive); a first `μ` measurement declared worthless for optimising the wrong quantity; and Claim Q credited back to the dossier after a second search found what the first had missed.

## 9. Added 2026-08-19 (11:00–12:30): one proved infinite family, and the obstruction named

§8 recorded the constant's derivation. Four things since, in decreasing order of how much they are actually established.

**PROVED, and the first infinite-family statement here.** The k-arm NAE star satisfies the rooted target with `C = 1/β` **for every k**. Its dual is exactly the coordinates plus one homogenizer per arm, `h_i = e_q + e_{x_i} + e_{z_i}`, so `|D| = 3k+1`. Take the basis `{h_i} ∪ {e_{z_i}} ∪ {e_{x_1}}`; the leftover forms are `e_q, e_{x_2}, …, e_{x_k}`, and the selectors `e_q − h_2 = −u_2`, `e_{x_2} + e_{z_2} = +u_2`, `e_{x_j} − h_1 = e_{x_j} − e_q − u_1` give residual rank `1 + (k−2) = k−1`, because the first two land on the *same line*. Since `L = kβ` and `R_< = 0` at the hub rooting, the left side is exactly `d_cb ≤ k−1 < k =` budget. Detail: `problem/star_family_proved.md`.

**PROVED, one line, and it retires a claim of mine.** Every *minimal* Rado violation has deficiency exactly 1 — drop a class from a deeper violation and it still violates, contradicting minimality. So the "four classes spanning rank three" pattern I had reported was half definitional. The surviving content is the **composition**: all-private (the quarter mechanism, at `L = β`) versus two straddling forms sharing a boundary part so their difference is purely private. Detail: `problem/the_obstruction_is_four_classes_on_rank_three.md`.

**A convergence worth more than either.** That second composition is the **dual** of the campaign's own earlier conclusion — from `the_two_clauses_are_in_tension.md` — that both clauses hold exactly when boundary parts are constant on private-sharing clusters. The absorbability machinery built this session and the clause-tension analysis built earlier found the same object from opposite sides.

**MEASURED, with the direction now settled at small k.** Exact `d_cb` at star `k=4` is 3, so tightness `(k−1)/k` runs 0.500, 0.667, 0.750 — rising. Adding constraints costs room. I had claimed the reverse from four scattered objects and was wrong; the refutation then needed correcting too, because it initially rested on a bound. Both are recorded in place.

**Unchanged.** The conjecture is OPEN; `d_cb ≥ k−1` (the lower bound, hence saturation) is not proved; and every object remains a known non-member of the residual class.
