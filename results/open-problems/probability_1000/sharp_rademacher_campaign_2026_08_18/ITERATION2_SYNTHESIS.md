# Iteration-2 synthesis: what survived, what is dead, what is open

Campaign: sharp Rademacher singularity, session `claude-c53c1d50`, written 2026-08-19 by the
synthesizer agent under the parent session's write claim. Sources read in full for this document:
`STATE.md`, `LOG.md`, `attacks/referee_iter1.md`, `problem/referee_cluster.md`,
`attacks/attack_rank.md`, `attacks/attack_entropy.md`, `attacks/attack_transfer.md`,
`problem/telescope_reconstruction_draft1.md`, `problem/cluster_lemma_attempt1.md`,
`problem/cluster_lemma_v2_residuals.md`, `problem/layer3_interface_note.md`,
`problem/encoding_interface_reconstruction.md`.

**Standing honesty header.** The sharp Rademacher singularity conjecture
Pr(det B_n = 0) = (1+o(1))·2n²·2⁻ⁿ is **OPEN**. Nothing in this campaign proves it, approaches
proving it, or bears on its truth. The campaign's target is one deterministic lemma — the rooted
high-corank connector-rigidity theorem (dossier p.8, p.28, p.53; boxed S6 p.123) — which is Layer II
of a three-layer program whose Layer III (the centered-moment / Jain–Sah–Sawhney endpoint transfer)
**is not written anywhere**, in the dossier or here (dossier p.53; S1 p.56; S6 p.113). Even a
complete proof of the Layer-II target would not be the conjecture. The single hardest open piece —
the block-internal certificate for dense connector-incoherent cores — **has not moved.**

---

## 0. What actually landed (operational, and it changes how §1 must be read)

The iteration-2 workflow was launched with 3 hostile referees + 3 attack lanes + 3 source digesters.
On disk at synthesis time:

| Promised | Landed | Consequence |
|---|---|---|
| Referee: cluster note Bands I–V | **YES** — `problem/referee_cluster.md`, disposition PARTIALLY BROKEN | §1, §2 below |
| Referee: telescope draft (T1/G1/G2) | **NO** | T1a/T1b/T1c, G1, G2, target (A) remain **UNREFEREED**; three live conditionals hang on them |
| Referee: entropy memo (NK/sliver/Conj. B) | **NO** (second pass) | the memo was refereed once in iteration 1 (`referee_iter1.md`, objections E1–E6); that pass stands as its only adjudication |
| Attack: rank lane (re-run) | **YES** — `attacks/attack_rank.md` | the campaign's largest single output — and **nobody has refereed it** |
| Attack: overlapping-support case | **NO** | the one case Band V leaves open is untouched |
| Attack: adversarial computational search for the gating question | **NO** | costs nothing: the cluster referee answered that question negatively **by hand** (§2), and the note now forbids running it |
| 3 source digesters + store ingester | **YES** | `mathbrain/dossier_objects.jsonl` 97 → **325** objects, `edges.jsonl` 176 → **602**, quarantine 0 |

Also on disk from the main session, all **unrefereed**: `cluster_lemma_v2_residuals.md`,
`layer3_interface_note.md`, `encoding_interface_reconstruction.md`.

Read §1 with that asymmetry in mind. **Every document that was refereed lost load-bearing pieces.**
The two documents that are currently steering the campaign — `attack_rank.md` and
`telescope_reconstruction_draft1.md` — are exactly the two that no referee has seen.

---

## 1. What survived refereeing

### 1.1 Confirmed, unchanged

| Result | Status after refereeing | Who confirmed it, and how |
|---|---|---|
| **Lemma NK** (a)(b)(c) — near-kernel dimension, field-uniform over ℝ and odd 𝔽_p | **PROVED** | `referee_iter1` §2.1 checked the proof; `referee_cluster` §1.1 **re-proved NK(b) from scratch** rather than trusting it. Two independent re-derivations, different sessions. Exactly tight on the S9 star (D = 3, saturated). |
| **Forcing-mass identity** Σ_j p_j ≤ ℓ | PROVED | `referee_iter1`; it is the robust form of the dossier's own `|N₀| ≤ ℓ` (p.34) |
| **Quadric-rank necessary condition** (rank₂(A) ≫ r·ℓ would refute the unrooted target) | PROVED | `referee_iter1` §2.4 checked the (h·x)²=1 argument and the r(1+d)+d² count. Still the cheapest refutation tool the campaign owns. |
| **Support-≤2 dichotomy** (a form ternary on the whole cube has support ≤ 2) | PROVED | `referee_cluster` §6 gave a shorter proof, valid over ℝ with **no** integrality assumption, plus a brute-force check |
| **Transfer guardrails**: additive-slack warning (t·k² kills any "+t per block"); no-double-anticoncentration-credit (§4.4); no-typical-block (only cardinality lawfully discounts a subfamily) | PROVED / VERIFIED | `referee_iter1` §3.2–3.4. Permanent campaign assets — they stop future lanes making natural mistakes. |
| **Witness-point encoding lemma** and the per-row budget wall (1−o(1))ℓlog n/C₀ ≤ b ≤ (1+o(1))min(r,j) | PROVED (elementary) | `referee_iter1` §3.5. Its content is negative and it is the transfer lane's best observation: raw naming sits within (1+o(1)) of the budget, so the entire deterministic gap is compressing dense rows a diverging factor below raw. |
| **C ≥ 1/log₂(4/3) = 2.40942** floor for absolute-constant forms (NAE three-circuit products) | VERIFIED | `referee_iter1` citation audit against S6 tag (5) p.114 |
| Band I; slab extremal and its arithmetic; Band II **with the added hypothesis ℓ_B = ω(log D)** | CORRECT | `referee_cluster` §3, §5, §8 |
| **Band V's skeleton** (data processing + KL superadditivity against a product reference) | CORRECT — the referee's own verdict is that it is "the best thing in the note and genuinely new relative to NK" | `referee_cluster` §3(a)(b), verified symbolically and numerically |
| **Band IV's proposition** D ≤ ℓ_B + Σ(h(p_a)+p_a) | CORRECT, with "affine slice" replacing "coset" | `referee_cluster` §4 supplied the affine cube-point count the note glossed |

### 1.2 Confirmed but downgraded in scope — these cost the campaign real ground

**W1 (any uniform coefficient γ_n = o(log n) closes Layer II at the endpoint) — arithmetic
confirmed, reading scoped twice.** The computation is literally the dossier's own (27a)–(27b) with
γ_n in κ's seat, re-read verbatim by the referee. But **T4**: p.53 states the residual class
*disjunctively* ("either congestion at least of order log n **or** fails the common-lift
condition"). On the common-lift horn a block already has an O(1) quotient coefficient, so W1 buys
**nothing** there. The honest reading is: *the quotient clause got a log factor easier; absorption is
exactly as hard as yesterday.* And **T2**: the rooted form of W1 rests on
`recursive_paired_block_tree_entropy.md`, which is conclusively absent from every machine we control
— so it rests on the unrefereed reconstruction instead.

**W2/W3 (description-length interface; certify-or-count) — moved CONDITIONAL → RECONSTRUCTED
(structural), constants unverified.** `encoding_interface_reconstruction.md` executed referee item
(a) and the declared fail-stop did **not** fire. Its verification is genuinely convincing at k = 2:
the framework reproduces (1+o(1))·2n²·2⁻ⁿ exactly, which I re-derived here and which
`layer3_interface_note.md` §1 obtains independently from folklore outside the dossier. Two named
holes remain: the parametrization question (is the packet's fibre the column-restriction set or its
Gale dual?) leaves **constants untransferable**, and the reconstruction is a first-moment sketch that
over-counts components per singular matrix — plausibly the very thing the packet's centered-moment
machinery exists to control. The phrase "dossier-grade" stays banned.

**Crosspolytope inadmissibility — component scale ONLY (T3).** The transfer lane's campaign-level
advice ("set the crosspolytope aside as a certificate-side pathology") is **retracted**. A log-scale
crosspolytope embedded as the dense batch of an admissible component has marginal defect ≈ r′ −
log₂2r′ ≤ ℓ and congestion ≈ log n — *exactly the class signature*. This downgrade turns out to be
the most useful thing the iteration-1 referee did: see §4.

**Entropy §5a (slice-rooted NAE cycles) — connector status downgraded, certificate upgraded.** E4:
the certificate is **not** connector-transverse in p.49's sense; it satisfies absorption only if the
parent selects h₀ and pays that residual — conditional compatibility, strictly weaker. Separately and
in the other direction, the rank lane's **Lemma DRR proves the family's "+1" in general**, where the
entropy lane had only seven enumerated cases. Same item, downgraded by one document and generalised
by another, through genuinely different methods (algebraic contraction vs exact enumeration).

**Band V's constant.** The floor 0.278 is right **only for support ≥ 3** (the referee computed the
exact minimum 0.27807 over the whole realizable class, attained at s = 4); the note's shape
classification is false, and the referee's shape-free Littlewood–Offord replacement —
**D ≤ 2.5Π + 6.70ℓ** for every disjoint family of support-≥3 ternary forms — is strictly better and
assumption-free.

**The star constant: 4.26 → 1.42 / 2.84.** `STATE.md` carried "constant ≥ 81/19 ≈ 4.26" from the
S9 NAE star. The rank lane's exhaustive certificate search shows that is the **worst** of 10,976
boundary-preserving certificates, realised by 4 of them. Honest floors: leak/L ≥ 27/19 = 1.42 and
dim((R+R_<)/R_<)/L ≥ 54/19 = 2.84. **A campaign number was 3× pessimistic and had already been
propagated.**

> **Independent re-check run for this synthesis** (local, exact rational arithmetic, seconds,
> BelowNormal; `scratchpad/synth_check_star.py`, a different method from the rank lane's
> branch-and-bound). Confirmed: |A| = 54; ℓ = 3log₂(4/3) = 1.245112; |A_W| = 46; H(q|W) = 8/27;
> L = 19/27; the projective full dual is **exactly** the 10 classes {x_i, z_i, q, Y_i} (this answers
> the rank memo's own worry #6 — there is no eleventh form); the explicit witness basis
> {x₁,z₁,x₂,z₂,x₃,z₃,Y₃} with selectors q→−z₂, Y₂→x₂, Y₁→z₃ is a genuine full-dual basis whose
> residuals span **exactly 2** dimensions. And the lower bound: over all **91** candidate
> one-dimensional residual directions, the minimum number of collapsed projective classes is **8 > 7**
> basis slots, so no certificate with dim R = 1 exists. **d_cb(star) = 2 exactly.** Not checked by me:
> the min-leak-1 count over 10,976 certificates, and the r ≤ 5 census.

### 1.3 Landed this iteration, elementary, but NOT YET REFEREED (do not build on)

From `attack_rank.md`: R1 (the rooted target splits exactly into quotient + leak, by Dedekind's
modular law — **I re-derived this proof and it is correct**), R2 (leak = excess rank
dim B̄(ker P)), R3 (Theorem 1 really bounds 2ν + L with ν the two-shadow matching number; κ, κ_avg,
4^L are three estimates of ν; **nothing in the packet's LO arguments sees rank** — they bound support
and then bound rank by support), R4/R4a (the forced Θ(log n) deficit), Lemma DRR, R5/R5b
(exchange densifies without alignment; κ = O(1) is strictly stronger than the target), R7
(dim((R+R_<)/R_<) ≤ 2ν + L + μ **with no absorption hypothesis at all**), the LO support lemmas, and
the §8 counting lower bound.

From `telescope_reconstruction_draft1.md`: T1a (paid-once filtration; rank telescopes with no
absorption clause), T1b (defects telescope by the chain rule) — both elementary and I checked the
arguments — plus G1 (assembly into one full-dual basis, written out), G2 (admissibility; explicitly
**underivable** from this dossier, resting on one inherited definition layer), and target (A),
verified exactly on the rooted NAE cycle. The draft's own falsifier (§5.5) already killed T1c's
per-block form at m = 1 granularity and replaced it with the amortized statement — a self-inflicted
downgrade, honestly recorded.

From `cluster_lemma_v2_residuals.md`: Lemma S, and the exact solution of the referee's double-star
(**mass 1/(2^k+1) — I verified this by hand:** a hub taking the root's value forces all k of its
leaves off it, so only 1 of the 2^k+1 independent sets contains the hub).

---

## 2. What is dead, and what that closes off

**Band III (second moment / half-integer support) — FALSE.** The change of measure runs backwards:
dU_A/dU_cube = 2^ℓ·1_A gives E_A[g] ≤ 2^ℓ·E_cube[g], never the reverse (take g = 1_{Aᶜ}). Broken on
the campaign's canonical cluster: |A| = 18, ℓ = 0.8301, p = 4/9, and the claimed bound reads
"4 ≤ 3.16". Not patchable by any constant. **Closes off:** the only band that was linear in Π with no
log factor, and the entropy memo's designated real-field fallback route.

**Cluster lemma Part (2), and the note's own repaired Part (2) — FALSE.** The referee's double-star
cluster: Π ≈ k/2 → ∞ while ℓ_ent(A_C) → 1 and ℓ(A) → 2, with support-4 differences of mass exactly ½
at O(1) defect; ratio ≈ 50 at k = 100. The mechanism: **linear independence of the difference forms
is not independence of the constraints they impose** — all k differences are made cheap by one
two-bit event. "Support ≥ 3" bounds the form, not its constraint content. **Killed twice
independently**: the iteration-1 referee's E3 (an active difference fixes the values of two dual
rows, not any coordinate of x, so coordinate-determination accounting does not apply) is a second,
different mechanism against the same step. **Closes off:** the forcing-mass route to the entropy
memo's Gap 1, which was that lane's *named single next move*.

**`dim span{q_a}` is the wrong invariant — the finding that reorganises the route.** The target
consumes the minimal residual dimension over basis + signed selectors. In the double-star the span is
2k while the residual span is 2 against ℓ ≈ 2; in general the gap can be Θ(4^ℓ) (dossier's own
|C| ≤ C₀4^L). **Closes off:** any cluster lemma phrased on the span, and `attack_entropy.md` §3's
assembly as written, which inherits it.

**Cluster lemma Part (1) — VACUOUS.** D ≤ 1 + 128(ℓ + Π) follows from Lemma NK(a)+(b) alone with an
absolute constant, no fibre structure, no shapes, no KL. **Closes off:** the note's organising
question. Bands II–V are constant-improvement work, and the "medium band" the note framed as the hard
region is precisely where the stated inequality is trivial (medium masses ⇒ Π = Θ(D)).

**`attack_entropy.md` §3 Gap 1's escape hatch for support-≤2 clusters — FALSE**, and this one was
missed by the iteration-1 referee. Rows h_a = x₀ + x_a + x_u give a cluster with ℓ ≈ 1,
ℓ_supp(A_C) = 0, and m−2 independent support-2 differences of mass ≈ ½ each — total ≈ (m−2)/2, not
"summing into ℓ". Support-≤2 clusters are unhandled, not easy.

**The 280-sample check — ZERO POWER, measured not argued.** 280/280 trials were settled by the
trivial count D ≤ 2Π before ℓ was consulted; the sampler cannot emit Π/D < ½ because a support-4
ternary form's natural cube mass is 4/7. **Closes off:** "the bound survives its first contact" as
evidence of anything. A positive control would have caught this before it was written.

**The designated fleet computation ("does there exist a fibre with sublinear defect carrying many
independent support-≥3 ternary forms of medium mass?") — answered NEGATIVELY BY HAND** and must not
be queued. This is the iteration's one compute saving.

**Smaller kills:** the 3-adic image bound D ≤ 1.71ℓ_B is false (double-star: D = 7 vs 1.67), and
image counting yields a *lower* bound on D, vacuous as an upper bound. "Second-order differences
leave the ternary class" is false — the class *is* closed under differences. Band IV's vacuity
interval (0.227, 0.773) is wrong; the correct region is **(0.2271, 1]** (h(p)+p is not symmetric
about ½ — I checked: h(0.773)+0.773 = 1.546). Band IV's "every counting or entropy route pays ≥ 1 bit
per dimension" is overreach about arguments not yet invented, refuted in spirit by Band V. Band IV's
illustrative arithmetic 45 is wrong (63.6 vs NK(b)'s 92.1). Band V's shape classification is false.

**Dead as a strategy, conditional on the dossier's own class characterisation: repairing S9's
Theorem 1 by better combinatorics.** R4/R4a: on the high-congestion horn, in every batching, basis,
maximum matching, witness row and greedy order, ν ≥ (c₀/2 − o(1))·log n·log₂log n, so in the
threshold window the support route outputs a coefficient ≥ (2c₀−o(1))·log n — precisely the factor
W1 shows the endpoint cannot afford. **Closes off:** κ_avg, better matchings, better batching, the
ν-form itself, as routes to Layer II on that horn. What remains is Target R-C: exhibit selectors
whose residual private parts span O(L) = O(log log n) dimensions inside a core of support
≍ log n·log log n — a factor-Θ(log n) **rank** compression. This is conditional on an assertion the
dossier states but never proves, whose qualifier "useful junction basis" is undefined, and it covers
**at most half the class** (R4 is silent on the common-lift horn).

**Dead: T1c at m = 1 granularity.** No uniform per-block γ exists at unit-block granularity (the
telescope draft's own falsifier). Replaced by the amortized target (A) at m ≥ 2 with defect-banking
spines. Filtration bookkeeping fixes double-charging, not per-block linearity.

---

## 3. What is now open, ordered by tractability

**(1) Referee `attack_rank.md`. [hours; adversarial agent + exact enumeration]** It has redirected
the campaign (R4 killed a route, R7 opened one, and a campaign constant was corrected in place inside
`STATE.md`) and no one has checked it. Attack surfaces the memo itself names: R4's undefined
quantifier; R3 possibly being prose rather than mathematics if κ was always a hypothesis-class label;
the r ≤ 5 census measuring a slightly different object (ℚ only, no 𝔽_p case checked); and R1/R2
possibly being folklore inside S9's Lemma-2 proof. Partly done here: §1.2's box confirms §9.1 end to
end by a different method. Unconfirmed: the 10,976-certificate min-leak and the census.

**(2) Settle μ (unpaid boundary rank) and dim Π⁰_U on the dense families. [minutes of local exact
arithmetic on fibres already enumerated]** This is R7's hypothesis, and it is the *only* live attack
on clause (ii) — the clause the iteration-1 referee said neither lane had advanced. Three outcomes,
all redirecting (rank memo §12). **Caveat this synthesis adds, and it matters:** every object we can
run it on is a known **non-member** of the residual class, and most are *aligned*, which is exactly
what incoherence denies. Registered prediction, so the next agent can score me: on k-arm dense stars
I expect min-over-certificates μ to grow with k while L stays below 1, i.e. outcome (ii); the
counter-datum is that the S9 star's *optimal* certificate (verified above) has μ = 2 = O(1) with
μ/L = 2.84, so if μ stays bounded as k grows, R7's relief is real on the very family the packet built
to force absorption, and I am wrong.

**(3) Referee `telescope_reconstruction_draft1.md`. [hours]** T1a's filtration bookkeeping is the
candidate sibling-coordination mechanism that E1 demands, W1-rooted needs, and the rank memo's §2
conclusion ("clause (ii) is not needed under filtration") depends on. Its own author has already
falsified T1c at m = 1. The referee's job: find the dossier passage (if any) forcing ancestor-only
bookkeeping, and audit G1's deepest-block induction and G2's admissibility definition.

**(4) Conjecture C's failure-mode-1 computation. [minutes]** min_f Pr(h ≠ ±f) over the full duals of
the slice-rooted NAE cycles and the dense stars. If those minima stay bounded away from 0, the
residual-form cluster lemma is in trouble and the note must say so. Same code path and same objects
as (2) — run them together.

**(5) Quantify the Layer-III margin. [one page]** `layer3_interface_note.md` §3: the residual class
needs only o(n²2⁻ⁿ), not exponential smallness. Compute, at the class's own parameters
(ℓ ≈ ½log₂log n, k = O(n/log n)), how much room the count-times-probability product actually has —
which replaces "o(log n)" with a number **and** decides the strongest case against W2/W3 (if the
union bound is borderline at the endpoint, description length is necessary but not sufficient and
cancellation is doing real work).

**(6) Attack the second horn (common-lift failure). [research]** Nobody has. R4 covers at most half
the class; on the other half the quotient coefficient is already O(1) and the entire open content is
absorption — which is where (2) lives. This is the campaign's largest untouched territory, and its
size has been hidden by both delivered lanes adopting S1's strong conjunctive class form instead of
p.53's disjunction.

**(7) Get one explicit object in the residual class. [research; possibly impossible]** The campaign
has never possessed one. The dense NAE stars are excluded by name ("no o(log n) ordinary star core",
S6 p.123); the slice-rooted NAE cycles and the m-slice are solved families; the crosspolytope is
inadmissible at component scale; the double-star and the balanced slab are referee constructions.
Three dossier passages characterise the class by properties and none exhibits a member. So **every
number this campaign has computed is a measurement on a known non-member**, and R4's quantifier, R7's
hypothesis and Conjecture C have all never met the objects they are about.

**(8) Target R-C: the factor-Θ(log n) rank compression. [the actual open problem on horn 1]** Entry
point is Question R-Q (how large can dim Π⁰_U be for a dominant dense support U?), because DRR closes
the case dim Π⁰_U = 1 independently of |U|. The LO support lemmas prove single-form LO cannot see
this: it controls support at the 4^ℓ scale and says nothing about rank. The problem is self-similar —
the rank route arrives at the same core the entropy lane reached as its Gap 2.

**(9) Standing background falsifiers. [cheap, deferred]** The quadric-rank hunt (any fibre with
rank₂(A) ≫ r·ℓ refutes the unrooted target outright) and Conjecture RC (d_cb ≤ ℓ/log₂(4/3), sharp at
NAE three-circuit products). **Extrapolation warning, and it is the campaign's own scar:** RC's
support is an exhaustive census at r ≤ 5 plus five named families over ℚ only, and a family
engineered to beat 1/β would most plausibly be built at r ≥ 8 where there is no data. A value quoted
outside the measured range is a claim about data we do not have. Do not build on RC.

**(10) The named gap: the block-internal certificate for dense connector-incoherent cores.** NOT
MOVED, by any lane, in either iteration. Lemma DRR — the only rank-compression mechanism proved this
iteration — covers exactly the aligned case, and connector-incoherence is the negation of alignment.
The rank lane's own words, which this synthesis endorses: *"I did not compress rank on a single block
that is actually open."*

---

## 4. The single next move for iteration 3

**Referee `attack_rank.md` by execution: one hostile agent, one file, whose mandate is (a) re-derive
R1–R3 and R7 independently and recompute the exact star and census numbers, and (b) run the memo's
own §12 computation — μ and dim Π⁰_U as rooted blocks in a two-level tree — extended beyond the
aligned families to the campaign's only genuinely connector-incoherent dense object, an embedded
log-scale crosspolytope block, with the embedding written down explicitly as a stated assumption.**

Why this and not something else:

1. **It is where the campaign is currently exposed.** `attack_rank.md` is the only major memo nobody
   has refereed, and it is the one the campaign has already believed: `STATE.md` calls it "the
   campaign's strongest memo" and edited a constant in place on its authority. Iteration 2's measured
   base rate is unambiguous — the cluster note lost 4 items dead and 2 vacuous out of 8 refereed
   items; the entropy program was blocked three ways; the transfer lane's two boldest strategic
   conclusions were both scoped down. The rank memo's own author lists seven ways it could be wrong,
   including "the star correction could be the one thing here that is simply an error." Leaving the
   document that redirected everything unrefereed for a second iteration is the highest
   risk × leverage item on the board.

2. **The computation folded into it is the only live attack on clause (ii).** The iteration-1 referee's
   sharpest cross-lane finding was that neither delivered lane advanced absorption. R7 is the first
   statement that does anything about it — it replaces the binary, unprovable-looking absorption
   condition with a *checkable* rank hypothesis, μ = O(L). Checking it costs minutes on fibres already
   enumerated.

3. **The crosspolytope extension is what makes the computation informative, and it comes from
   combining two findings neither document connected.** T3 (the iteration-1 referee) established
   that a log-scale crosspolytope embedded as a dense batch has *exactly* the class signature —
   marginal defect ≤ ℓ, congestion ≈ log n. R5/R-Q (the rank lane) established that
   connector-incoherence is the negation of alignment, and the crosspolytope is the one dense object
   in the inventory whose full-dual forms have mutually large symmetric differences — i.e. the only
   *unaligned* one we possess. Running μ, dim Π⁰_U, d_cb and the leak λ on a rooted embedded
   crosspolytope block therefore tests the rooted target on the first object that is both dense and
   incoherent. On the aligned stars alone the computation is likely to return what those objects were
   built to show; on this one it is not.

4. **Every outcome redirects.** If the incoherent block satisfies the rooted estimate with a small
   coefficient, that is the campaign's first positive evidence on an incoherent object and Target R-C
   acquires a mechanism to generalise. If it fails, we have the first candidate counterexample to the
   rooted target on an object that is admissible at the endpoint — which would redirect Layer III
   entirely and is a far more valuable result than another partial certificate. If the embedding
   cannot be specified without inventing structure the dossier never states, that itself is the
   finding, and it must be reported as such rather than papered over — a modelling choice nobody
   asked for is a silent change to the question.

The runner-up is refereeing the telescope draft; it should follow immediately, because three live
conditionals rest on T1a. It ranks second only because the campaign already labels that draft
unrefereed and forbids building on it, whereas the rank memo is being trusted.

---

## 5. Honest campaign status, in three sentences

The sharp Rademacher singularity conjecture is **OPEN**; this campaign has proved nothing about it,
and its target is not the conjecture but one deterministic lemma which, even if fully proved, would
still have to feed an unwritten Layer-III transfer that nobody in this campaign or in the dossier has
drafted. What iteration 2 actually produced is negative and organisational: an exact splitting of the
rooted target into a quotient bound plus a leak (so exactly two things, not one, remain open beyond
S9's Theorem 1), a conditional proof that the packet's own main tool is a Θ(log n) factor too weak on
the high-congestion horn, two corrected campaign numbers, and the refutation of three of the four
bands of the campaign's own cluster lemma together with the invariant they were bounding. **The
block-internal certificate for dense connector-incoherent cores has not moved**: the one
rank-compression mechanism proved this iteration covers exactly the aligned case that
connector-incoherence denies, and the campaign still does not possess a single explicit object in the
residual class on which to test any of its hypotheses.

---

## 6. Claim ledger

Labels: **PROVED** (self-contained proof, checked by at least one adversarial reader or by me) ·
**EXACT** (finite certificate / exhaustive computation) · **CONDITIONAL** (depends on a stated
unproved input) · **HEURISTIC** · **NUMERICAL** (evidence only) · **DISPROVED** · **REFEREED-BROKEN**
(a referee exhibited the break) · **VACUOUS** · **UNREFEREED** (no adversarial pass yet — carry as
provisional).

| # | Claim | Label | Refereed? |
|---|---|---|---|
| 1 | Pr(det B_n = 0) = (1+o(1))2n²2⁻ⁿ | **OPEN** — nothing here bears on it | — |
| 2 | Rooted high-corank connector-rigidity theorem (target (41)) | **OPEN** | — |
| 3 | Block-internal certificate for dense connector-incoherent cores | **OPEN, NOT MOVED** | — |
| 4 | Lemma NK (a)(b)(c), field-uniform ℝ / odd 𝔽_p | PROVED | yes, twice, independently |
| 5 | Forcing-mass identity Σp_j ≤ ℓ | PROVED | yes |
| 6 | Quadric-rank necessary condition (refutation tool) | PROVED | yes |
| 7 | Support-≤2 dichotomy | PROVED | yes (shorter proof supplied) |
| 8 | One-dominant-batch sliver | PROVED, **scope: threshold window only** | yes (E5) |
| 9 | Transfer guardrails: additive-slack, no-double-credit, no-typical-block | PROVED / VERIFIED | yes |
| 10 | Witness-point encoding lemma + per-row budget wall | PROVED (elementary) | yes |
| 11 | W1: any uniform γ_n = o(log n) closes Layer II at the endpoint | VERIFIED-ARITHMETIC, **quotient clause on the high-κ horn only** | yes (T4 scoping) |
| 12 | W1 in rooted form | CONDITIONAL on the telescope reconstruction | yes (T2) |
| 13 | W2 / W3 (description length; certify-or-count) | RECONSTRUCTED (structural), **constants unverified** | reconstruction UNREFEREED |
| 14 | Encoding framework reproduces 2n²2⁻ⁿ at k = 2 | EXACT (re-derived here) | UNREFEREED |
| 15 | 2n²2⁻ⁿ is the coincident row/column-pair count; the hard direction is one-sided | PROVED (folklore, re-derived independently of the dossier) | UNREFEREED |
| 16 | Crosspolytope inadmissible as an endpoint **component** | DERIVED | yes |
| 17 | "Crosspolytope retired" at any larger scope | **REFEREED-BROKEN** (T3) | yes |
| 18 | ℓ-bifurcation (window ⇒ germ model; above ⇒ counting) | HEURISTIC (referee's own synthesis) | — |
| 19 | C ≥ 2.40942 floor for absolute-constant forms | VERIFIED | yes |
| 20 | R1 splitting identity: target = quotient + leak | PROVED (elementary; re-derived here) | **UNREFEREED** |
| 21 | R2 leak = excess rank dim B̄(ker P) | PROVED (elementary) | **UNREFEREED** |
| 22 | R3 ν-form: Theorem 1 bounds 2ν + L; κ, κ_avg, 4^L estimate ν | PROVED from S9's proof | **UNREFEREED** |
| 23 | R4/R4a forced Θ(log n) deficit on the high-κ horn | **CONDITIONAL** on the dossier's class assertion + threshold-window regime; covers ≤ half the class | **UNREFEREED** |
| 24 | Target R-C (factor-Θ(log n) rank compression) | FORMULATION, not a theorem | **UNREFEREED** |
| 25 | Lemma DRR (U-locality ⇒ d_cb ≤ contraction + 1, independent of \|U\|) | PROVED | **UNREFEREED** |
| 26 | DRR proves entropy §5a's "+1" in general | PROVED (cross-method corroboration) | **UNREFEREED** |
| 27 | R5/R5b: exchange densifies without alignment; κ = O(1) strictly stronger than the target | PROVED | **UNREFEREED** |
| 28 | R7: dim((R+R_<)/R_<) ≤ 2ν + L + μ, no absorption hypothesis | PROVED | **UNREFEREED** |
| 29 | Residual-class blocks have μ = O(L) | **UNKNOWN** — cheapest checkable hypothesis on the board | — |
| 30 | LO support lemmas (full-dual ≤ 16·4^ℓ; residuals ≤ 36·4^ℓ) | PROVED (elementary) | **UNREFEREED** |
| 31 | d_cb(S9 NAE star) = 2; full dual is exactly 10 classes; L = 19/27 | **EXACT** — confirmed here by a second, different method | partially (by me) |
| 32 | Min leak = 1 over all 10,976 boundary-preserving certificates | EXACT (exhaustive; confirms S9's forced-leak proof by a different method) | not re-run |
| 33 | STATE's "constant ≥ 4.26" from the star | **DISPROVED** — worst of 10,976; honest floors 1.42 / 2.84 | corrected in STATE |
| 34 | r ≤ 5 census: nothing exceeds 1/β; r=5 spanning count 60,879 matches the dossier | EXACT, EXHAUSTIVE | not re-run |
| 35 | Conjecture RC: d_cb ≤ ℓ/log₂(4/3) sharp | **CONJECTURE**, weakest claim in the campaign — ℚ only, r ≤ 5, no data at r ≥ 8 | **do not build on** |
| 36 | Conjecture B (bipolar counting) + its equivalences | CONJECTURE (r ≤ 5 exhaustive); equivalences PROVED | partially (E6) |
| 37 | T1a paid-once filtration; T1b defect telescoping | PROVED (elementary) | **UNREFEREED** |
| 38 | T1c per-block uniform γ at m = 1 granularity | **DISPROVED by the draft's own falsifier**; replaced by amortized target (A) | self-refuted |
| 39 | G1 assembly into one full-dual coordinate basis | PROVED as written | **UNREFEREED** |
| 40 | G2 / admissibility | CONDITIONAL — **underivable from this dossier** (one inherited definition layer) | **UNREFEREED** |
| 41 | Target (A) verified on the rooted NAE cycle (ratio 1.09) | EXACT on that family | **UNREFEREED** |
| 42 | Cluster lemma Part (1) | **VACUOUS** — free from NK(a)+(b) | yes |
| 43 | Cluster lemma Part (2) and its repair | **REFEREED-BROKEN** (double-star; plus E3, a second mechanism) | yes |
| 44 | Band I | PROVED | yes |
| 45 | Band II | PROVED **with the added hypothesis ℓ_B = ω(log D)** | yes |
| 46 | Band III | **DISPROVED** (measure change reversed; 4 ≤ 3.16) | yes |
| 47 | Band IV proposition | PROVED (affine slice) | yes |
| 48 | Band IV vacuity interval (0.227, 0.773) | **DISPROVED** — correct region (0.2271, 1] | yes |
| 49 | Band IV "every counting/entropy route pays ≥ 1 bit/dim" | **OVERREACH** — three named routes only | yes |
| 50 | Band V skeleton (data processing + KL superadditivity) | PROVED | yes |
| 51 | Band V shape classification | **DISPROVED**; floor 0.27807 holds for support ≥ 3 only | yes |
| 52 | Shape-free replacement D ≤ 2.5Π + 6.70ℓ (Erdős LO) | PROVED (referee's own) | — |
| 53 | 3-adic image bound D ≤ 1.71ℓ_B | **DISPROVED** | yes |
| 54 | "Second-order differences leave the ternary class" | **DISPROVED** — the class is closed under differences | yes |
| 55 | 280-sample check | **VACUOUS** — zero power, measured | yes |
| 56 | The queued "gating search question" | **ANSWERED NEGATIVELY BY HAND** — must not be run | yes |
| 57 | `dim span{q_a}` as the target's invariant | **DEAD as a route** (gap up to Θ(4^ℓ)) | yes |
| 58 | attack_entropy §3 Gap-1 escape hatch for support-≤2 clusters | **DISPROVED** (referee §5; not caught in iteration 1) | yes |
| 59 | Cluster v2 Lemma S; double-star mass 1/(2^k+1) | PROVED / EXACT (mass verified here by hand) | **UNREFEREED** |
| 60 | Conjecture C (residual-form cluster lemma) | CONJECTURE with 4 named failure modes | **UNREFEREED** |
| 61 | E1 currency mismatch (support defect vs L_{Q\|W}) | PROVED objection; repaired for the cluster note at cost of a factor 2 (slice transfer) | yes |
| 62 | Sibling coordination / "which telescopes" | **UNKNOWN** — T1a is the candidate mechanism, unrefereed | — |
| 63 | The campaign possesses an object in the residual class | **NO** — every computed object is a known non-member | — |
| 64 | `recursive_paired_block_tree_entropy.md` exists on any machine we control | **DISPROVED** (exhaustive search, positive controls passed) | — |

---

*Compute note: the only computation run for this synthesis was the local exact re-check of the S9
star described in §1.2 — seconds, single process, BelowNormal, no research box touched, nothing
written outside the scratchpad and this file.*
