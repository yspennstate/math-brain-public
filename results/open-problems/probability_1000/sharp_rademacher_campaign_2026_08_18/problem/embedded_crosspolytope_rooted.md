# The embedded crosspolytope as a rooted block: first positive data on an incoherent object — and a modelling caveat that is itself the finding

Author: main session c53c1d50, 2026-08-19 ~03:2x. This executes the single next move named in `ITERATION2_SYNTHESIS.md` §4 (agents were limit-blocked until 05:10, so the main session ran it). Code: scratchpad `crosspolytope_rooted.py`, exact rational arithmetic, BelowNormal, local.

## Why this object

The synthesis identified it by combining two findings neither source document connected: **T3** (an embedded log-scale crosspolytope has *exactly* the residual class's signature — marginal defect ≤ ℓ, congestion ≈ log n) and **R5/R-Q** (connector-incoherence is the negation of alignment, and the crosspolytope is the one dense object in the inventory whose full-dual forms have mutually large symmetric differences, i.e. the only *unaligned* one we possess). Every other object the campaign has measured is aligned, solved, or excluded by name. So this is the first rooted computation on something both dense and incoherent.

## Validation before results

Unrooted `r = 4`: `|A| = 8`, `|D| = 8`, `ℓ = 1`, **`d_cb = 1`** — matching the dossier's tag (31) `d_cb = r − ⌊log₂2r⌋ = 4 − 3 = 1`, which is also the value the rank lane used to validate *its* independent code. Same anchor, third implementation.

## Results (r = 4, exhaustive over all 70 candidate bases)

| r | \|W\| | ℓ | L_{Q\|W} | d_cb | μ | λ (leak) | d_cb/L | μ/L |
|---|---|---|---|---|---|---|---|---|
| 4 | 1 | 1.0000 | 1.00000 | 1 | 1 | **0** | 1.000 | 1.000 |
| 4 | 2 | 1.0000 | 1.00000 | 1 | 1 | **0** | 1.000 | 1.000 |
| 4 | 3 | 1.0000 | 1.00000 | 1 | 1 | **0** | 1.000 | 1.000 |

**Reading.** At every rooting, the block satisfies the rooted target with coefficient **1.0** — comfortably below the 2.409 floor — with **leak zero**, so connector absorption holds *trivially*, and with **μ = O(L)**. That is outcome (i) of the rank lane's decision tree (`attack_rank.md` §12): *the rooted estimate holds with no connector hypothesis at all, on an incoherent object.* It is the campaign's first positive datum on anything unaligned, and it is the opposite of what the synthesis's registered prediction expected for dense families.

## The caveat that is itself a finding, stated first-class rather than in a footnote

**I had to invent the embedding.** The dossier never specifies how a crosspolytope sits inside a component: which of its coordinates are the incoming boundary, which are private, and what the parent looks like. I declared "the first `|W|` coordinates are boundary" — a modelling choice nobody asked for, and the synthesis anticipated exactly this: *"if the embedding cannot be specified without inventing structure the dossier never states, that itself is the finding, and it must be reported as such rather than papered over."*

So the honest verdict has two halves:
1. **Under an arbitrary coordinate rooting, the r = 4 crosspolytope block is easy** — coefficient 1, no leak, μ = O(L).
2. **That may be an artifact of the rooting.** The result is invariant across all three rootings I tried, which is mild evidence it is not, but all three are of the same *kind* (a coordinate split), and the packet's block boundaries come from the Gale-flag layer machinery in the lost tree — the same missing layer that has now blocked the telescope reconstruction (G2), the (25) derivation, and this. **Three independent questions in this campaign now terminate at the same absent document.** That is worth recording as a structural fact about the programme, not just an inconvenience.

## Further limits, plainly

- `r = 4` is the smallest Hadamard order and has `ℓ = 1` exactly. The synthesis asked for a **log-scale** embedded block; this is not one, and asymptotic behaviour cannot be read off it. The `r = 8` case is running (128 dual forms make exhaustive basis enumeration impossible, so it uses randomized basis sampling — an upper bound on `d_cb`, therefore an upper bound on the ratio, adequate to detect an easy block but **not** to certify a hard one).
- `λ = 0` means this instance does not stress absorption at all, so it is weak evidence about clause (ii) specifically.
- The greedy selector search returns an upper bound on `d_cb`; here it returns 1, the minimum possible nonzero value, so it is tight by inspection at `r = 4`.
- The crosspolytope remains **inadmissible as an endpoint component** (transfer lane §4.2). Its relevance is only as an embedded *batch*, which is precisely T3's scope-corrected claim — and my rooting models the batch's fibre, not its embedding in a real component.

## What it changes

Target R-C acquires its first candidate mechanism on an unaligned object rather than only on aligned ones: at `r = 4` the crosspolytope's rank compression is total (support 4, rank 1). If the same holds at `r = 8` and beyond, the interesting question stops being "can incoherent blocks be certified?" and becomes "**which** incoherent blocks resist?", which is a sharper and more attackable question than the one the campaign has been carrying. If `r = 8` breaks the pattern, this note's positive reading dies with it and the r = 4 result is demoted to a small-case artifact — the run is in flight and its outcome will be recorded either way.
