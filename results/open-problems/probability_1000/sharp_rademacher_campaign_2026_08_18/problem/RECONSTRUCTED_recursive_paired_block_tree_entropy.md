# RECONSTRUCTED: recursive_paired_block_tree_entropy.md

**This is a reconstruction, not a recovery.** Written 2026-08-22 (lane P6_telescope, agent
claude-8e06e1f7-P6, 30h campaign task R16) from the surviving citations of the lost file. The
original is absent from every machine we control (search closed 2026-08-19 with positive controls:
`problem\the_missing_tree_hunt_closed.md`, STATE.md 00:5x, ITERATION2_SYNTHESIS.md row 64). Nothing
below is the lost text. It is new mathematics written to stand where the lost file stood, meeting the
interface spec assembled in `TELESCOPE_SKELETON.md` (same directory) from every surviving consumption
point: dossier S6 p.113 (extraction lines 6116–6152), S9 p.152 (lines 9276–9432), S14 pp.199–200
(lines 13195–13357), plus the campaign consumers (attack_transfer W1, second_horn_reduction,
g2_sharpened, the mathbrain objects). Per-claim labels: **RE-PROVED** (complete proof written here),
**CONDITIONAL** (proved under stated extra hypotheses), **TESTIMONY** (a surviving source's statement
about the lost text — checkable for consistency, not re-provable), **UNRECOVERABLE**, **OPEN**.

Relation to prior work: this builds on `problem\telescope_reconstruction_draft1.md` (2026-08-19),
`problem\telescope_self_referee.md`, and `problem\T1a_independent_referee_20260822.md`, and
re-verifies every proof it uses rather than citing labels. It supersedes none of them. Machine
checks: `telescope_sanity_check.py` + `sanity_check_output.txt` (this directory; 300 exact-rational
instances, controls and anti-vacuity counters all live). **Nothing here advances the conjecture,
which is OPEN. The block-internal certificate for dense connector-incoherent cores is untouched.**

---

## 0. What the lost file was consumed FOR (the interface)

Three sentences in the dossier are the entire surviving specification:

1. (S6, after stating rooted estimate (3): per block, (i) dim((R+R_<)/R_<) ≤ C·L_{Q|W} and
   (ii) R ∩ span W ⊆ R_<) — "Boundary-only forms are assigned to the parent. The second condition in
   (3) is the connector-absorption condition. Conditional defects then telescope, and
   `recursive_paired_block_tree_entropy.md` gives one global constant. Without the second condition,
   a boundary residual can be paid again at every descendant."
2. (S9) — "The common-linear-lift language in `recursive_paired_block_tree_entropy.md` is precisely
   condition 3 [of Lemma 2]."
3. (S14) — "[treating a one-private-vertex interval as an independent cyclic core] would repeat
   precisely the connector direction which condition (14) of `recursive_paired_block_tree_entropy.md`
   was designed to absorb."

So the file must supply: a TELESCOPE (per-block rooted estimates ⇒ one component-level bound with one
global constant), the ROLE of absorption in it (the failure mode without clause (ii)), the
COMMON-LIFT form of absorption, and the ABSORPTION discipline for defect-poor acyclic blocks (m=1).
Everything below is organised against that spec; §10 is the status table.

## 1. Setup

A component with fibre A ⊆ {±1}^r, spanning and full-closed, over K = R or an odd finite field
(entropies always w.r.t. the uniform measure on A, base 2; ℓ(A) := r − log₂|A|). A block
decomposition: blocks B_1, …, B_m with private sign-coordinate sets Q_i partitioning [r]; each block's
incoming boundary W_i is a tuple of sign forms that are functions of the private coordinates of B_i's
ancestors. The block-level "boundary-depends-on" digraph is assumed ACYCLIC — discharged structurally
whenever blocks are the strongly connected components of the dependency structure, since the
condensation of any digraph by its SCCs is a DAG (this hypothesis was hidden in draft1 and made
explicit by the self-referee; it is carried explicitly here). Fix a topological order (ancestors
before descendants) and use it for everything below. Per-block conditional defect
L_i := |Q_i| − H(Q_i | W_i). Each block's certificate contributes a residual space R_i (span of its
signed-selector residuals). Write V_i := R_1 + ⋯ + R_i (V_0 = 0).

Three paid-space bookkeepings for block i, ordered by inclusion:

- **Declared** (unsound alone): any R_< ⊆ span W_i handed down by fiat. Sound only when the
  declaration is HONEST — R_<^i ⊆ Σ_{j ∈ anc(i)} R_j, i.e. genuinely "already paid by ancestors",
  S6's own defining phrase, threaded top-down as the recursion's invariant — AND clause (ii)
  disciplines the block's own residuals. Clause (ii) alone is NOT enough: a block whose boundary
  residual sits inside a declared-but-never-generated R_< satisfies (ii) and is charged zero while
  the assembled rank grows (this is exactly the sanity check's control, 52/299 violations).
  This pair of invariants is the packet's compositional world.
- **Ancestor-paid**: P_i := (Σ_{j ∈ anc(i)} R_j) ∩ span W_i — what ancestors actually generated.
- **Filtration (arising)**: F_i := V_{i−1} ∩ span W_i — what ANY earlier block generated.

P_i ⊆ F_i ⊆ V_{i−1} always (ancestors precede i in every topological order; intersections preserve
inclusion). This chain of containments is the load-bearing fact of §2, and it is what the sanity
check's control deliberately breaks (declared span W_i ⊄ V_{i−1} ⇒ the aggregation genuinely fails:
52/299 violations when paid is declared-but-ungenerated).

## 2. Theorem RT-1 (the rank telescope) — **RE-PROVED**

For ANY choice of per-block residual spaces R_i and any topological order:

  dim(R_1 + ⋯ + R_m) = Σ_i dim((R_i + V_{i−1})/V_{i−1})
                      ≤ Σ_i dim((R_i + F_i)/F_i)          [filtration bookkeeping]
                      ≤ Σ_i dim((R_i + P_i)/P_i)          [ancestor-only bookkeeping]

No absorption clause is used anywhere.

*Proof.* The equality is the dimension filtration of a sum. For the inequalities, use the second
isomorphism theorem: for any subspace U, dim((R+U)/U) = dim R − dim(R ∩ U). With U ranging over
V_{i−1} ⊇ F_i ⊇ P_i and the same R = R_i, monotonicity of dim(R_i ∩ ·) gives
dim(R_i ∩ V_{i−1}) ≥ dim(R_i ∩ F_i) ≥ dim(R_i ∩ P_i), hence the reversed chain on quotients. ∎

Provenance of confidence: the filtration half is draft1's T1a, argued there by surjection, re-derived
by the independent referee (2026-08-22) via the isomorphism route above, machine-checked by that
referee on 300 abstract instances with a working control, and re-checked here (300 fresh instances,
0 violations, control fails 52 times, separations nonzero). The ancestor-only extension (P_i) is new
here (draft1 §3c asserted the comparison without proof in one direction); its proof is the same
monotonicity, and the sanity check exercises it non-vacuously (24 instances with strict separation).
**Consequence: the rank-sum aggregation is valid under BOTH the packet's ancestor-paid bookkeeping
and the filtration bookkeeping.** The lost file's aggregation step, whichever of the two it used, is
re-proved.

## 3. Theorem RT-2 (the defect telescope) — **RE-PROVED**

Under §1's hypotheses (boundaries measurable w.r.t. ancestor privates; block digraph acyclic):

  Σ_i L_i ≤ ℓ(A).

*Proof.* In the topological order, W_i is a function of (Q_j : j ∈ anc(i)) ⊆ (Q_1, …, Q_{i−1}), so
σ(W_i) ⊆ σ(Q_1, …, Q_{i−1}) and conditioning on the finer algebra can only lower entropy:
H(Q_i | W_i) ≥ H(Q_i | Q_1, …, Q_{i−1}). Summing, and using the entropy chain rule with the fact that
the Q_i partition the coordinates (so (Q_1, …, Q_m) determines the point of A):
Σ_i H(Q_i | W_i) ≥ Σ_i H(Q_i | Q_{<i}) = H(Q_1, …, Q_m) = log₂|A|. Hence
Σ_i L_i = r − Σ_i H(Q_i | W_i) ≤ r − log₂|A| = ℓ(A). ∎

(Equality is attained on the k-arm NAE star family — `problem\mu_on_dense_stars.md` verified
Σ L_i = kβ = ℓ exactly — so RT-2 is sharp and not improvable in general.)

## 4. Corollary RT-3 ("one global constant", and uniformity) — **RE-PROVED** (rank level)

If every block's certificate satisfies the rank clause dim((R_i + R_<^i)/R_<^i) ≤ γ·L_i with R_<^i
its paid space under EITHER sound bookkeeping (P_i or F_i), then

  dim(Σ_i R_i) ≤ γ · Σ_i L_i ≤ γ · ℓ(A).

The coefficient enters exactly once, multiplying Σ L_i; nothing in the proof compares constants
across levels or compounds them, so γ may be an absolute constant or a uniform sequence γ_n → ∞
(in particular γ_n = o(log n), the endpoint-relevant case): the aggregation is linear in γ.
*Proof:* chain RT-1 with the hypothesis, then RT-2. ∎

This discharges, FOR THE RECONSTRUCTION, attack_transfer's caveat 3 ("the lost file could use
constancy of C in a hidden comparison"): the reconstructed telescope provably does not. Whether the
LOST proof did is unknowable (§11), but the campaign needs only some correct telescope with this
property, which now exists. W1-rooted's conditionality therefore moves: no longer "conditional on an
unreadable file", now conditional on the d_cb assembly step (§8) like everything else.
Scope caveat (from draft1 §5.5, verified there by the unit-block falsifier): the PER-BLOCK hypothesis
with any uniform γ is unachievable at m=1 granularity (L_i → 0 with cost 1 remaining — §7). RT-3 is
vacuous on decompositions that isolate such blocks; the usable form is either on coarsenings whose
blocks satisfy the hypothesis, or the amortized target (A) of draft1 §5.6
(Σ_i dim((R_i+F_i)/F_i) ≤ γ·Σ_i L_i in aggregate), which RT-1/RT-2 support identically and which is
verified exactly on the rooted NAE cycle (ratio → 1/(3(1−log₂φ)) ≈ 1.09, re-checked arithmetic).

## 5. Absorption: the leak identity and the common lift — **RE-PROVED**

Fix a block; write B := span W for its boundary span, R_< ⊆ B its paid space, P_0 its private span.
Decompose the residual generators r_a = b_a + p_a (b_a ∈ B, p_a ∈ P_0 — unique since coordinates
split). Let F be the free coefficient space on the generators, P: F → P_0, e_a ↦ p_a, and
B̄: F → B/R_<, e_a ↦ b_a + R_<.

**(RT-5a) Leak identity.** dim((R+R_<)/R_<) = dim((R+B)/B) + λ, where
λ := dim(((R∩B) + R_<)/R_<) = dim B̄(ker P).
*Proof.* The projection (R+R_<)/R_< → (R+B)/B (v+R_< ↦ v+B) is well defined (R_< ⊆ B) and
surjective; its kernel is ((R∩B)+R_<)/R_< ≅ (R∩B)/(R∩B∩R_<). For the second expression: a
combination v = Σ λ_a r_a lies in B iff its private part vanishes, Pλ = 0; and then v = Σ λ_a b_a,
whose class mod R_< is B̄λ. So {classes mod R_< of R∩B} = B̄(ker P), and both expressions for λ
agree. ∎

**(RT-5b) Lemma CL (common lift, = the dossier's Lemma 2).** The following are equivalent:
(1) R ∩ B ⊆ R_< (connector absorption, = λ = 0);
(2) ker P ⊆ ker B̄;
(3) there is a linear T: im P → B/R_< with B̄ = T ∘ P.
*Proof.* (1)⟺(2): by the computation above, v = Σλ_a r_a ∈ R∩B iff Pλ = 0, and v ∈ R_< iff
B̄λ = 0. (2)⟺(3): the universal property of quotients — B̄ factors through P exactly when it kills
ker P (define T(Pλ) := B̄λ; well defined by (2), linear, and unique on im P). ∎
And when they hold, dim((R+R_<)/R_<) = dim((R+B)/B) by RT-5a with λ = 0 (S9's tag-(24) step).

Per S9's testimony, condition (3) IS the lost file's "common-linear-lift" language; what is
re-proved here is the equivalence and the identity. The attribution itself is TESTIMONY (§9).

## 6. Theorem RT-4 (what absorption is FOR: the multiplicity theorem) — **RE-PROVED**

This is the reconstruction of C1's failure-mode sentence, made precise, with STATE.md's follow-up
question ("per-descendant re-payment or sibling multiplicity?") answered. Both multiplicities are
real, in different bookkeepings; the sanity check exhibits both.

**(RT-4a) Depth multiplicity under declared (compositional) bookkeeping.** In a subtree-recursive
proof, each block's estimate must hold for the paid space it is HANDED (universally quantified — the
packet's target (3)/(41) quantifies over every R_< ⊆ span W precisely because a subtree's certificate
must stand before its siblings and cousins exist). Without clause (ii), a chain B_1 → B_2 → ⋯ → B_d
in which each descendant's certificate emits the same pure-boundary residual direction a (realisable:
S9's forced-leak result — reconfirmed by `attack_rank.md` §9.1's exhaustive search — shows blocks
exist whose every certificate leaks a pure boundary direction) is charged as follows: with nothing
prepaid (R_< = 0, as the m=1 and NAE-star obstruction proofs take it), every level counts a anew:
Σ charges = d−1 against assembled rank 1. The same boundary residual is "paid again at every
descendant" — C1's sentence, verbatim, and it is TRUE in this bookkeeping. [Witness computed exactly:
depth witness in `sanity_check_output.txt`: assembled 1, zero-paid sum 4 at d = 5, both paid
bookkeepings 1.]

**(RT-4b) No depth multiplicity under paid bookkeepings.** Under P_i or F_i bookkeeping, a direction
once generated by an ancestor lies in every deeper paid space that its boundary span admits, and
RT-1's proof counts every direction exactly once, at the step that first generates it (the equality
row). So per-descendant re-payment CANNOT occur. [Same witness: both paid sums = 1.]

**(RT-4c) Sibling multiplicity under ancestor-only bookkeeping.** Ancestor-only paid spaces do not
see siblings: k siblings each forced to leak the same direction a ∈ their common boundary span, with
no ancestor having paid a, are charged k times against assembled rank 1. The bound stays TRUE (RT-1:
it is an upper bound) but wastes k−1 budget units. Filtration bookkeeping charges 1. [Sibling
witness: ancestor sum 2, filtration sum 1, assembled 1.] So: **without absorption, the binding
failure of the compositional recursion is depth re-payment (RT-4a); the residual looseness of honest
ancestor-only accounting is sibling multiplicity (RT-4c); filtration accounting eliminates both
(RT-4b, RT-1 equality).**

**(RT-4d) What clause (ii) buys, exactly.** Absorption is the discipline that makes PER-BLOCK budgets
compose in the compositional world: it forbids a certificate from emitting an unpaid boundary
residual at all — the block must either have it prepaid (then it costs 0: it is inside R_<) or route
it as a private-containing residual (§7's fallback, cost borne once, locally). Under absorption PLUS honest
declarations (§1's pair of invariants) the compositional accounting is simultaneously sound and
declaration-invariant, by two separate mechanisms that must not be conflated: HONESTY gives
R_<^i ⊆ Σ_{j ∈ anc(i)} R_j ⊆ V_{i−1}, so RT-1's monotonicity makes the charge sum an upper bound on
the assembled rank; and CLAUSE (ii) gives dim((R_i+R_<^i)/R_<^i) = dim((R_i+B_i)/B_i) (RT-5a with
λ = 0), a quantity that does not depend on WHICH honest R_<^i ⊆ B_i was declared — so the recursion
may hand a child as much or as little of the ancestors' actual payment as its bookkeeping happens to
see, without changing any block's charge. That is why the packet could run a top-down recursion with
only ancestor-declared paid spaces and still claim one global constant: clause (ii) is the
compositional substitute for the global filtration, and honesty is what keeps declarations
meaningful. Neither alone suffices: without honesty, (ii)-compliant blocks can be undercharged and
the sum undercounts the assembled rank (exactly the sanity check's control, 52/299 violations);
without (ii), honest declarations still admit RT-4a's depth re-payment inside the
universally-quantified per-subtree statements. ∎

## 7. The one-private-vertex block and the absorption dichotomy — **RE-PROVED** (mathematics)

The m=1 interval: boundary vertices 0, 2, homogenizer A, private vertex 1, with k stable-set vertices
attached to both boundary vertices inflating the neutral pattern. Re-derived from the fibre count
(neutral endpoint pattern: 2^{k+1} extensions; each of the other three patterns: one):
H(B_1 | A, B_0, B_2) = 2^{k+1}/(2^{k+1}+3), so L_{Q|W} = 3/(2^{k+1}+3) → 0, while the exact selector
distance stays 1. Hence NO defect-only bound dim((R+R_<)/R_<) ≤ C·L with absolute C exists (take
R_< = 0). The two lawful treatments, from the edge forms C_{0,1} = A+B_0+B_1, C_{1,2} = A+B_1+B_2 in
the basis {A, B_0, B_1, B_2}:
- **Absorbed alternative** (select B_1 in both): residuals A+B_0 and A+B_2 — pure boundary. Zero new
  rank and clause (ii) satisfied IFF span{A+B_0, A+B_2} ⊆ R_< (ancestors prepaid both).
- **Private fallback** (select B_0, resp. B_2): residual A+B_1 — contains the private coordinate, so
  clause (ii) is untouched; new cost one, charged once, locally.
Treating such a block as an independent cyclic core (R_< = 0, pure-boundary residuals kept) re-emits
the connector direction at every level — RT-4a's mechanism. This is exactly what S14 says the lost
file's condition (14) was designed to absorb, and the reconstruction reproduces the design: the
dichotomy "prepaid-or-private" IS the absorption discipline at m=1. (Closed rooted NAE cycles need
none of this: their optimal certificate has R ∩ span W = 0 — absorption holds with zero paid space —
S14 §8, used in draft1 §5.6's exact verification of target (A).)

**(TC3, boundary-only forms to the parent) — CONDITIONAL.** The convention "a full-dual form
supported inside span W_B is charged to an ancestor, never to B" is well defined iff every full-dual
form has a lowest block whose (Q ∪ W)-region supports it — which is the admissibility condition of
§8. Under admissibility it is a definition plus the observation that the parent's region contains the
child's boundary; without admissibility some cross-block form has no host and the convention is
undefined. So TC3 inherits §8's conditionality. It is not separately falsifiable.

## 8. Assembly into a d_cb certificate — **CONDITIONAL** (and where the condition lives)

RT-3 bounds dim(Σ R_i). The consumers' TC1 needs d_cb(A) ≤ γ·ℓ(A): ONE coordinate basis drawn from
the full dual of A, selectors for EVERY full-dual form, all residuals in one space. Two steps:

**(G1, basis assembly) — RE-PROVED under explicit hypotheses.** Hypotheses: each block contributes
|Q_i| forms, each ±1-valued on A; each contributed form f splits as f = h_f + g_f with
supp h_f ⊆ Q_i, supp g_f ⊆ ancestor privates; and the private parts {h_f : f ∈ P_{B_i}} form a basis
of K^{Q_i}. Claim: the union F of all contributed forms (|F| = r) is linearly independent, hence a
full-dual coordinate basis. *Proof (re-verified, DAG version):* if Σ λ_f f = 0 with λ ≠ 0, pick a
block B* with a nonzero coefficient and no nonzero-coefficient strict descendant (a sink of the
induced sub-DAG; exists by finiteness and acyclicity). Project onto Q_{B*}: ancestors' forms are
supported on their own and THEIR ancestors' privates — none of which is Q_{B*}, since B* descends
from them and the digraph is acyclic; incomparable blocks' forms are supported on their privates and
their ancestors' privates, and B* is not among their ancestors; descendants carry zero coefficient.
What remains is Σ_{f ∈ P_{B*}} λ_f h_f = 0, forcing those λ_f = 0 by the private-part basis property
— contradiction. ∎ The hypotheses are supplied by the two certificate kinds the dossier uses
(literal coordinates; witness-exchanged families triangular on their pivots by tag (28)) — that
supply is the dossier's claim, not re-proved here.

**(G2, selector coverage) — CONDITIONAL, the live gap.** Every full-dual form not in the basis needs
a selector with its residual in the assembled space. Call a decomposition ADMISSIBLE iff every
full-dual form of the component is supported inside some single block's (Q_B ∪ span W_B). For
admissible decompositions, per-block certificates cover all forms and G1's basis carries the
selectors: the assembly is a d_cb certificate and TC1 concludes d_cb(A) ≤ γ·ℓ(A). For an irreducible
core (no nontrivial admissible decomposition), G2 is vacuous — one block, no cross-block forms, and
the difficulty is block-internal, as it must be. What cannot be recovered: whether "admissible" as
defined here coincides with the packet's inherited Gale-flag block-formation notion — those
definitions are in the same lost tree (draft1's Gale-passage audit found every in-dossier usage
consistent with this reading and nothing to derive it from; two necessary conditions on the notion
were later derived in `g2_sharpened.md` and `the_rooting_must_not_explain_away_the_constraints.md`).
**TC1 at full strength is therefore CONDITIONAL on: (a) blocks supplying G1's hypotheses, (b)
admissibility of the decomposition — with (b) resting on lost definitions.**

## 9. TESTIMONY items (consistent, not re-provable)

- The lost file's internal condition "(14)" is the connector-absorption clause (S14's usage; the
  edges to `m1_exact_absorbed_alternative` and `cycle_connector_absorption_exact` in the mathbrain
  store are consistent with §7 above).
- Its "common-linear-lift language" is RT-5b's condition (3) (S9's sentence).
- Both attributions are single sentences about a text nobody can read; they are consistent with the
  reconstruction and cannot conflict with any mathematics here.

## 10. Status table (spec TC → reconstruction → label)

| Spec claim (skeleton) | Where re-derived | Status |
|---|---|---|
| TC1 rank aggregation, one global constant | §2 RT-1, §4 RT-3 | **RE-PROVED** (both bookkeepings) |
| TC7 defect aggregation Σ L ≤ ℓ | §3 RT-2 | **RE-PROVED** (sharp on stars) |
| TC1 full: per-block (3) ⇒ d_cb ≤ γℓ | §8 (G1 + G2) | **CONDITIONAL** (G1 hyps; admissibility ← lost Gale-flag layer) |
| TC2 "paid again at every descendant" without (ii) | §6 RT-4a/4b/4c/4d | **RE-PROVED** (true compositionally; impossible under paid bookkeeping; sibling waste answered) |
| TC3 boundary-only forms to the parent | §7 end | **CONDITIONAL** (well defined iff admissible) |
| TC4 common lift ⟺ absorption; leak identity | §5 RT-5a/5b | **RE-PROVED** |
| TC5 condition (14) mechanics at m=1 | §7 | **RE-PROVED** (math); numbering = TESTIMONY |
| TC6 uniform γ_n passes, no compounding | §4 RT-3 | **RE-PROVED** |
| Filtration strictly richer than ancestor-only | — | **OPEN** (not used above; referee 2026-08-22, leak channel; deciding check recorded there) |
| The lost file's conditions (1)–(13), its proofs, "paired", Gale-flag definitions | §11 | **UNRECOVERABLE** |

Referee status, stated plainly: RT-1's filtration half carries two structurally different derivations
and an independent referee (2026-08-22) plus two machine checks. RT-1's ancestor extension, RT-2,
RT-3, RT-4, RT-5, §7, and G1's re-verification are THIS lane's proofs (building on draft1 and its
self-referee); they are elementary, machine-exercised where a machine can reach them, and
**unrefereed by an independent session**. The campaign's standing rule about building on unrefereed
steps applies to them until a hostile pass lands.

## 11. UNRECOVERABLE, stated as findings

1. The lost file's internal structure: conditions (1)–(13) (the numbering "(14)" proves at least
   fourteen existed), its definitions, its actual proof route. No surviving text quotes any of them.
2. Whatever "paired" in the title named. No surviving citation uses a pairing notion. (Possibility
   consistent with everything: paired = the (b_a, p_a) boundary/private splitting of §5; recorded as
   a guess, weight zero.)
3. The Gale-flag block-formation definitions G2 needs — same lost tree
   (`the_missing_tree_hunt_closed.md` row set; four campaign questions terminate there).
4. Whether the lost telescope was compositional (needing clause (ii), as C1's failure-mode sentence
   suggests) or global-order (not needing it, as RT-1 shows possible). Both are now covered: the
   reconstruction proves the telescope BOTH ways, so no consumer depends on resolving this.
None of these block any TC above beyond the conditionality already labeled; if the campaign ever
recovers the original, §12's check is the first thing to run against it.

## 12. Strongest case this reconstruction differs from what the lost file proved

The lost file's telescope may have been proved ONLY compositionally, with clause (ii) as a standing
hypothesis threaded through every statement — in which case its "one global constant" theorem was
weaker than RT-3 (which needs no absorption for the rank aggregation) but carried structure this
reconstruction lacks: per-subtree statements quantified over every handed-down R_<, which is what a
top-down recursive proof of the FULL conjecture would compose with, and possibly the Gale-flag
block-formation machinery as its §1. If so, consumers reading "the telescope is re-proved" and
concluding "so the packet's recursion composes as originally designed" would overreach: RT-3
aggregates a FIXED decomposition's certificates; it does not by itself run the packet's recursion
(build certificates top-down against declared paid spaces), whose soundness is exactly RT-4d and
whose per-block hypotheses at defect-poor blocks are only satisfiable via §7's dichotomy — i.e. the
recursion needs absorption even though the aggregation does not. The one check that would confirm the
difference: on the rooted NAE n-cycle cut at one vertex (the solved family, all certificates in
S14), run BOTH pipelines — (a) RT-3 on the fixed decomposition, (b) a top-down recursion where each
block receives only its declared R_< and must satisfy (3) with clause (ii) — and compare the
component bounds. If (b) cannot reproduce (a)'s ⌈n/3⌉ ≤ 2·L total without invoking the global
triangular activation budget (S14's own escape hatch for m=1 tails), then the lost file necessarily
contained a third mechanism (the "global triangular activation budget" S14 names) that this
reconstruction represents only as the amortized target (A) — and (A) is then the right spec for it,
not an optional strengthening. That computation uses only S14's published certificates and is a
finite check.
