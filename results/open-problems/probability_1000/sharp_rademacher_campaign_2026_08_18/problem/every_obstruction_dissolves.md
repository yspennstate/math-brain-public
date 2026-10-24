# Every obstruction object in the campaign dissolves — and nobody has ever displayed a class member

Author: main session c53c1d50, 2026-08-19 ~03:0x. This applies the standard established in `mu_on_dense_stars.md` addendum 2 — *an object obstructs only if it fails under every admissible decomposition* — to every concrete object the campaign or the dossier has proposed as an obstruction. Status: the per-object verdicts are cited or computed; §3's reformulation is a proposal with its logical strength stated exactly, not a claim of progress.

## 1. The audit

| object | proposed as | verdict under the standard | authority |
|---|---|---|---|
| **k-arm NAE star** (S9's is k=3) | absorption cannot follow from sparsity | **DISSOLVES.** Under the natural tree (homogenizer as root, arms as children) every child meets the full rooted target at exactly 1/β, leak 0, no ancestor payment | computed here, `mu_on_dense_stars.md` addendum 2 |
| **m = 1 interval** (S14 §7) | no defect-only bound with an absolute constant | **DISSOLVES — and the packet nearly says so.** S14 §8: the pathology "occurs *after cutting* them into an acyclic one-vertex interval, and that pathology is exactly resolved by ancestor residual absorption rather than by a new cyclic estimate". The cut IS a decomposition choice; the pathology is created by it | dossier S14 §8, extraction lines ~13340–13356 |
| **Walsh crosspolytope** | the dense-witness bootstrap is false | **NOT AN OBSTRUCTION TO THE TARGET AT ALL.** `d_cb = r − ⌊log₂2r⌋` against `ℓ = r − log₂2r`, so the ratio → 1: it is *linear already*. The dossier says as much ("does not refute linear rigidity"); the rank lane showed it is not even a counterexample to the ν-form; the transfer lane showed it is inadmissible as an endpoint component at component scale. It obstructs **techniques**, not the theorem | dossier p.43; `attack_rank.md` §3(b); `attack_transfer.md` §4.2 |
| **double-star** (referee's) | my cluster lemma's Part (2) is false | **DISSOLVES for the target** (it did kill my lemma, correctly). The referee himself: "d_cb-style accounting selects each row against its own leaf coordinate, leaving the two-dimensional residual span against ℓ ≈ 2. That is comfortably linear" | `referee_cluster.md` §1.3 |
| **rooted NAE cycles** | the constant-one ceiling is false | Never an obstruction to linearity — the packet solves them exactly and their ratio tends to 1.09; they kill only the constant `C = 1` | dossier S10 |
| **NAE three-circuit products** | the constant floor | Not an obstruction: they *satisfy* the target, and pin `C ≥ 1/β = 2.409` | dossier S6 tag (5) |

**Every single one dissolves, is technique-only, or is a constant constraint.** Not one of them is a witness that the target is hard, let alone false.

## 2. The observation that follows

The residual class is defined by a **conjunction of universal negatives** — a singleton-layer cyclic SCC *after every admissible Gale basis exchange*, of relation corank ≥ 5, with no sparse-cyclomatic fundamental graph, no `o(log n)` feedback set, no large disjoint-support matching, no `o(log n)` star core, no low-rank shared form, no multiplicative subgroup/coset fibre, and congestion ≳ log n *in every useful junction basis* or common-lift failure (S6 p.123).

Two facts sit next to each other and, as far as I can find, have never been put together:

1. **No member of this class is displayed anywhere in the 200 pages.** The rank lane reached the same point independently and made it its concrete check for R4: "the dossier never displays a member" (`attack_rank.md` §11.1).
2. **Every concrete object anyone has produced as an obstruction dissolves** (§1), and the dissolution is always by the same move: choose the decomposition, the invariant, or the scale correctly.

## 3. The reformulation, with its logical strength stated exactly

> **Route E (emptiness).** Show the residual class is empty. Then Layer II closes: every component is covered by the already-proved theorems (the global exponential bridge, bounded-congestion rigidity, the exact NAE/stable-set/median/paired-Gale certificates, the closed low-corank endpoints), and the deterministic bridge holds outright.

**Exact strength — this is the part that must not be overstated.** Emptiness is a **sufficient** condition, and it is **strictly stronger** than the target: a nonempty class whose members all satisfy the rigidity estimate would also close Layer II. So Route E is not an equivalent restatement and not a shortcut; it is a *different* sufficient route with a completely different attack surface — structural dissolution instead of uniform certificates.

**Why it may nonetheless be the better surface.** The class's definition is a conjunction of negatives, and each conjunct is a *dissolution move that has already been shown to work on some object*: the Gale-exchange clause is the decomposition move (the star), the "no star core" clause excludes exactly what dissolves under re-rooting, the basis clause is the invariant move (the double-star), the scale clauses exclude the crosspolytope. **The class is, almost literally, "the objects that survive every move we know". Whether anything does is an open question that nobody appears to have asked in this form.**

**How Route E could fail, honestly.** (a) The class is probably nonempty — a counting argument (there are vastly more fibres than dissolution moves) would be the natural first attempt to show it, and I have not attempted it. (b) Even a proof of emptiness must be uniform in n, and the dissolution moves so far are exhibited on families, not proved to cover. (c) The absence of a displayed member is evidence about the *document*, not about the mathematics — the earlier project tree that the dossier cites may well display one, and that tree is the same lost layer that has blocked three other questions in this campaign. (d) Most soberly: if the class were easy to prove empty, the packet's authors — who clearly knew every one of these dissolutions — would likely have said so.

**The concrete next move Route E suggests**, and it is cheap: attempt to *construct* a class member. Take the constraints one at a time and try to satisfy them simultaneously at small rank by exhaustive or structured search (the campaign already has exact full-dual and `d_cb` machinery for r ≤ 5, and the rank lane's census infrastructure). Either a member appears — which would be the first ever displayed, and would immediately become the campaign's central object — or the constraints are shown to conflict at small rank, which is the first real evidence for Route E. Both outcomes are worth more than another certificate attempt, and neither requires the missing tree.

## 4. CORRECTION to §3's "concrete next move" (03:2x, before it was acted on)

The move I proposed — "try to construct a class member at small rank" — **does not type-check, and I should have seen it while writing it.** The class's defining conditions are asymptotic: `relation corank ≥ 5` is finite, but `no o(log n) feedback set`, `no o(log n) ordinary star core`, `congestion ≳ log n in every useful basis`, and the defect threshold `ℓ ≥ ½log₂log n + ½log₂log log n − O(1)` are all statements about **sequences**, not about individual fibres. There is no such thing as a class member at r = 6. **The class is a class of families**, and Route E must be posed as *no family survives*, with the construction attempt building a family rather than an object.

This matters beyond bookkeeping: it is the same category error the whole campaign has been circling. The dossier "never displays a member" (rank lane §11.1) partly because a member is not the kind of thing that can be displayed on a page — it is an infinite family with uniform properties. So the absence of a displayed member is weaker evidence for Route E than §2 implies, and §2 is hereby weakened accordingly.

**What IS finite-checkable, and is the sharpest falsifiable statement the campaign owns:** the rank lane's **Conjecture RC**, `d_cb(A) ≤ ℓ(A)/β` with `β = log₂(4/3)`, equality at NAE three-circuit products. That is a statement about individual fibres, decidable by exact computation, and a single fibre with `d_cb/ℓ > 1/β` refutes it. The rank lane's exhaustive census settled `r ≤ 5` (nothing exceeds 1/β; the r=5 spanning count 60,879 matches the dossier's own enumeration). **So the honest replacement for §3's move is: hunt for `d_cb/ℓ > 1/β` at r = 6–7 over structured and random full-closed fibres.** A hit refutes RC and hands the counterexample lane its target; no hit after a real search is the first evidence for RC beyond r ≤ 5 and beyond the two families that attain it.

Method note for whoever runs it: a greedy selector search returns an **upper** bound on `d_cb`, hence an upper bound on the ratio — enough to *find* candidates, not enough to *claim* a refutation. Any candidate that clears 1/β must then be verified by exhaustive search over bases and signed selectors before it is reported. (The greedy did find the exact optimum on the S9 star, where an independent exhaustive result exists to check it against, which is why it is trustworthy as a filter.)

## Honest footer

Nothing here proves the conjecture, closes Layer II, or shows the class is empty. What it establishes is that the campaign's entire stock of obstruction objects has no witness in it, and that "is there a member at all?" is a question the programme has never posed. The block-internal certificate for dense connector-incoherent cores remains exactly as open as it was; Route E is a proposal about where to point next, not a result.
