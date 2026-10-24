# The second horn reduces to one global statement: total pure-leak rank is O(ℓ)

Author: main session c53c1d50, 2026-08-19 ~04:0x. Executes item (6) of `ITERATION2_SYNTHESIS.md` §3 — *"Attack the second horn (common-lift failure). Nobody has. This is the campaign's largest untouched territory, and its size has been hidden by both delivered lanes adopting S1's strong conjunctive class form instead of p.53's disjunction."* Status: the reduction is elementary given inputs that are themselves labelled; the conclusion is conditional and says so.

## 1. What the second horn is, and why it has been invisible

The dossier's class characterisation at p.53 is a **disjunction**: a surviving block *either* has entropy-normalized congestion κ ≳ log n in every useful junction basis, *or* it fails the common-lift condition. Both delivered attack lanes adopted S1's stronger conjunctive phrasing, so both worked horn 1 exclusively — the iteration-1 referee flagged this (T4) and the synthesis repeated it. Nothing in the campaign has addressed horn 2.

**Horn 2 is, on its face, the easier half — and that is exactly why it has been overlooked.** On it, congestion is bounded, so S9's Theorem 1 *already* delivers the quotient clause with an O(1) coefficient. There is nothing left to prove about clause (i). The entire open content of horn 2 is clause (ii): absorption.

## 2. The reduction

Inputs, each with its status:
- **(R1)** [PROVED, elementary, `attack_rank.md`] `dim((R+R_<)/R_<) = dim((R+B)/B) + λ` with `λ = dim(((R∩B)+R_<)/R_<)`.
- **(S9 Thm 1)** [PROVED in the dossier] `dim((R+B)/B) ≤ (2κ+1)·L_{Q|W}`; on horn 2, `κ = O(1)`, so this is `O(L_B)`.
- **(T1b)** [PROVED, `telescope_reconstruction_draft1.md`] `Σ_B L_B ≤ ℓ` by the entropy chain rule.
- **(T1a)** [PROVED but **UNREFEREED**] under paid-once filtration bookkeeping, the assembled residual rank equals `Σ_i dim((R_{B_i} + V_{i−1})/V_{i−1})` — each direction charged exactly once, at the step that first generates it.

Split each block's *new* directions (those not already in `V_{i−1}`) into two kinds:
- **(a) directions with a nonzero private part.** These survive the projection modulo `span W_B`, so their count is at most `dim((R_B+B)/B) = O(L_B)` on horn 2. Summing and applying T1b: `Σ_B O(L_B) = O(ℓ)`. **Done — this half needs nothing new.**
- **(b) pure-boundary directions** (entirely inside `span W_B`). These are exactly the leaks `λ`. Under *ancestor-only* bookkeeping each can be re-charged at every descendant — the depth loss the dossier warns of (p.8: "the same boundary direction can be charged at each generation"), which is why absorption is demanded as a clause. **Under filtration bookkeeping they are charged once globally.**

So, on horn 2 and conditional on T1a:

> **Reduction.** `d_cb(component) ≤ O(ℓ) + Λ`, where **`Λ := dim( span of all pure-boundary residual directions generated anywhere in the tree )`**.
> Horn 2 closes iff **`min over certificates of Λ = O(ℓ)`** [PHRASING CORRECTED 04:2x by `lambda_first_multiblock.md`: Λ is certificate-DEPENDENT - the same NAE path has Λ = 0 under a boundary-selector certificate and Λ = Θ(N) under a private-selector one - so the hypothesis is a minimum over certificates, not a property of the tree alone] — a single global statement about the whole decomposition, replacing a per-block clause that must hold for every block.

## 3. Why this is a genuine simplification, and what the campaign already knows about Λ

Absorption as the packet states it is a **universally quantified per-block** condition (`R_B ∩ span W_B ⊆ R_<^B` for every B), and the packet's own counterexamples show it cannot be derived from any local hypothesis — sparsity, bounded support, bounded incidence degree all fail (S9 §5). `Λ = O(ℓ)` is instead a **single existential/global budget**: individual blocks may leak freely provided the leaks do not span too much in total. Every campaign result about leaks is naturally a statement about Λ:

- **The m = 1 interval** (S14 §7) leaks exactly one direction with `L → 0`. Fatal to per-block absorption; harmless to Λ, since it contributes 1 to a budget of order ℓ.
- **The k-arm star** leaks `k−1` directions — and its own defect is `kβ`, so it contributes `(k−1)` to Λ against `ℓ = kβ`, i.e. `Λ/ℓ → 1/β = 2.409`. Bounded. (And under the arm decomposition it leaks nothing at all: `mu_on_dense_stars.md` addendum 2.)
- **The NAE-star** leaks exactly 1 (exhaustively verified over all 10,976 certificates) at `L = 19/27`.
- **The embedded crosspolytope** (r = 4, three rootings) leaks **0**.
Every leak the campaign has ever measured is O(1) per block, and the only family where leaks accumulate is the star, where they accumulate at exactly the sharp constant. **No object we possess pushes Λ above `ℓ/β`.**

That is not evidence that `Λ = O(ℓ)` in general — every one of those objects is a known non-member of the residual class, which is the campaign's standing limitation (`ITERATION2_SYNTHESIS.md` ledger item 63). It *is* evidence that the reduction points somewhere the existing machinery can actually reach.

## 4. Honest status

- The reduction is elementary given R1, S9 Thm 1, T1b and T1a. Three of those are proved; **T1a is unrefereed**, and the campaign's own standing rule forbids building on it. So horn 2's closure is conditional on a document the synthesis identifies as one of the two steering the campaign without adjudication. **This note therefore raises the value of refereeing the telescope draft: it is now load-bearing for horn 2 as well as for W1-rooted.**
- `Λ = O(ℓ)` is *not proved* for anything. It is a reformulation that (i) replaces a per-block universal by a global budget, (ii) is immune to the counterexamples that kill per-block absorption, and (iii) is measurable on every object the campaign owns.
- Nothing here touches horn 1, where the rank lane's forced Θ(log n) deficit stands, nor the block-internal certificate for dense connector-incoherent cores.
- The conjecture is OPEN.

**Next concrete step:** compute Λ for a *two-level tree of blocks* rather than for single blocks — the campaign has never done a genuinely multi-block computation, and Λ is a tree-level quantity that single-block measurements cannot see. The star-of-stars and a tree of crosspolytope batches are both constructible from machinery already written.
