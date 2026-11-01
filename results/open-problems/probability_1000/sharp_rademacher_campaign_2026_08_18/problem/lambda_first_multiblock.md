# Λ measured on a genuine two-level tree: it is zero, and the tree respects the constant

Author: main session c53c1d50, 2026-08-19 ~04:2x. Executes the next step named in `second_horn_reduction.md`: *"compute Λ for a two-level tree of blocks rather than for single blocks — the campaign has never done a genuinely multi-block computation, and Λ is a tree-level quantity that single-block measurements cannot see."* Done by hand (exactly, no computation), which also keeps the machine free while two other runs are in flight.

## The object

The rooted NAE path on `N` private sign coordinates `b_1..b_N` with homogenizer `a`, rows
  `Y_i = a + b_{i−1} + b_i` (each required ±1-valued),
decomposed two-level as follows — the natural alternating decomposition:
- **Root block**: `{a} ∪ {b_even}`.
- **Children** `i = 1..m` (`m = N/2`): child `i` has private `{b_{2i−1}}` and incoming boundary `{a, b_{2i−2}, b_{2i}}`, and owns the two rows `Y_{2i−1}` and `Y_{2i}`.

Every row belongs to exactly one child (each row contains exactly one odd-indexed `b`), so the root owns no rows and costs nothing. This is a real tree: children have disjoint privates, boundaries are functions of ancestor privates, and the whole fibre is the packet's own solved family.

## The certificate, and Λ

For child `i`, select the **boundary coordinate** of each of its two rows:
  `Y_{2i−1} − b_{2i−2} = a + b_{2i−1}` and `Y_{2i} − b_{2i} = a + b_{2i−1}`.
**Both rows produce the same residual.** So child `i` contributes the single direction `a + b_{2i−1}`, and:

- **Leak:** `R_i ∩ span W_i = span{a + b_{2i−1}} ∩ span{a, b_{2i−2}, b_{2i}} = 0`, because `b_{2i−1}` is private and appears in the residual. **Every child leaks nothing.**
- **Λ = 0 for the whole tree.** The first multi-block measurement of Λ, and it is the best possible value.

## The budget check

The children's directions are `a + b_1, a + b_3, …, a + b_{2m−1}` — independent (distinct private coordinates), so the assembled residual rank is exactly `m = N/2`.

For the NAE path the fibre counts independent sets, so `|A| ≍ 2·F_N` and `ℓ ≈ N(1 − log₂φ) = 0.3060·N`. Hence

  **`d_cb(this decomposition) / ℓ = 0.5N / 0.306N = 1.634`**,

comfortably inside the constant floor `1/β = 2.409`, and consistent with Conjecture RC.

**Worth stating plainly: this decomposition is suboptimal.** The packet's exact answer for the family is `⌈N/3⌉ = 0.333N` (ratio 1.09), so the alternating tree costs 1.5× the optimum. It still clears the target with room. That is the informative part — *a naive but natural decomposition of a real family satisfies the rooted estimate with zero leak and a constant well under the floor*, so the tree structure is not fragile: you do not have to find the optimal decomposition to stay inside the budget.

## What it does and does not support

**Supports:** the second-horn reduction's live hypothesis `Λ = O(ℓ)` now has its first tree-level datum, and it is the extreme value `Λ = 0`. It also gives a second worked instance of the pattern found on the star — *when a block can select against a boundary coordinate, its residual keeps a private part and no leak occurs* — which is beginning to look like the mechanism rather than a coincidence: **leaks arise when a block is forced to select against its own private coordinate**, and a block with an available boundary selector never is.

**Does not support:** anything about the residual class. The NAE path is a solved family and a known non-member; this is calibration. And `Λ = 0` here is achieved by a *choice* of certificate — the same object under the "select the private coordinate" certificate leaks 2 per child (`a + b_{2i−2}` and `a + b_{2i}`, both pure boundary), giving `Λ = Θ(N)`. **So Λ is certificate-dependent, and the reduction's hypothesis must be read as `min over certificates of Λ = O(ℓ)`** — which is how the second-horn note should have stated it, and this note corrects that phrasing.

## CORRECTION (04:4x, same session): my mechanism statement above is WRONG, and the right one is sharper

I wrote that "a leak occurs exactly when a block is forced to select against its own private coordinate". Pushing it, I first concluded that leaks can therefore *always* be avoided — put every boundary coordinate in the basis (they are always in the full dual), select each row against one, and every residual keeps a nonzero private part. That conclusion is false, and the packet says so: S9 §5 proves that for the NAE star *every* boundary-preserving basis and selector choice creates a pure-boundary residual.

**Where the reasoning broke: the leak is a property of the SPAN, not of individual residuals.** `λ = dim(R ∩ span W)`, and a combination of residuals each having a nonzero private part can still be pure boundary if the private parts *cancel*. That is exactly R2 (`λ = dim B̄(ker P)`): the leak is the boundary image of the private-part dependencies.

Worked on the two families, which is what makes the correct statement visible:
- **NAE star** (three rows `x_i + z_i + q`, one private `q`). Basis `W ∪ {q}`, selecting `x_i` for `Y_i`: residuals `z_i + q`, each with private part `q ≠ 0`. But `(z_1+q) − (z_2+q) = z_1 − z_2`, pure boundary. **Leak, despite every individual residual being private-carrying.** All three residuals share the same private part, so differences kill it — and their boundary parts `z_i` differ, so the difference survives on the boundary.
- **NAE path child** (two rows, one private `b_{2i−1}`). The two residuals are *identical* (`a + b_{2i−1}`), so the private-part dependency between them is trivial and its boundary image is `0`. **No leak.**

**The correct mechanism, therefore:**

> **A leak arises exactly when rows sharing a private part have DIFFERENT boundary parts in their residuals.** Formally `λ = 0` iff every dependency among the residuals' private parts also annihilates their boundary parts — i.e. `ker P ⊆ ker B̄`, which is precisely the packet's own Lemma 2 condition, now with a usable reading: *equal private parts must come with equal boundary parts.*

That also explains the rank lane's structural certificate #1 (private anchors: full column rank of the private projections gives `ker P = 0`, hence no leak at all) and it explains why the star is the packet's chosen counterexample — it is the minimal object where several rows are forced through *one* private coordinate with *distinct* boundary partners. And it sharpens `Λ = O(ℓ)`: the budget is consumed by exactly the private-sharing structure, so the quantity to bound is the total boundary spread of private-sharing row clusters.

**Two self-corrections in two hours on the same claim** (first the currency of the cluster lemma, now this) are worth noting as a pattern: both times I checked the residuals one at a time when the target is defined on their span. The invariant is the span — that was also the cluster referee's central finding, and I have now re-made a version of the same error after recording it.

**The sharpened question for the next pass:** is there a block that *cannot* select against a boundary coordinate — i.e. whose every full-dual form either is a private coordinate or has no boundary coordinate available in the basis? The S14 one-private-vertex interval is exactly such a block (its two edge forms differ by a pure boundary direction with `R_< = 0`), which is why it leaks and why the packet had to make absorption a clause. Characterising that obstruction is now the concrete content of `Λ = O(ℓ)`.
