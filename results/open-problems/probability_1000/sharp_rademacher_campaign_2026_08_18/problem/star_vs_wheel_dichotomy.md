# Why the star saturates the constant and the wheel does not

Author: main session c53c1d50, 2026-08-19 ~13:3x. The star family was proved today to force `C ≥ 1/β` (`star_family_proved.md` §6). The obvious question is whether that is generic. It is not, and the contrast is sharp.

## 1. The two families, exactly

| family | `d_cb` | `L` | tightness `d_cb·β/L` | limit |
|---|---|---|---|---|
| k-arm star | `k − 1` (**proved**) | `kβ` exactly | `(k−1)/k` | **→ 1, saturates** |
| k-spoke wheel | `⌈k/3⌉` | `k − log₂(Lucas_k) → 0.30575k` | — | **→ 0.4525** |

Exact `d_cb` for the wheel at `k = 3..7`: **1, 2, 2, 2, 3**, with tightness 0.4150, 0.6960, 0.5388, 0.4536, 0.5813 — sawtoothing as the ceiling function steps, and trending to `(k/3)β / 0.30575k = 0.4525`.

## 2. Two corrections the exact computation forced

**The greedy was wrong again — fourth time today.** It reported `d_cb(wheel k=6) = 3`; the exact value is **2**. So the pattern I had read off greedy values, `⌊k/2⌋`, is false, and the tightness limit I extrapolated from it (0.679) was wrong.

**And my first reading of the exact values was wrong too.** With `k = 3..6` in hand (1, 2, 2, 2) I took `d_cb` to be plateauing, which would have sent tightness to 0. `k = 7` gives 3, so it grows — slowly. Waiting for one more data point before writing the conclusion is what caught it.

## 3. The wheel's value is one the campaign already knows

`⌈k/3⌉` is not a new number here. The campaign's entropy lane recorded **rooted NAE cycles have `d_cb = ⌈n/3⌉`**, and the wheel *is* a rooted NAE cycle — hub plus rim. So this reproduces a known campaign result **through a completely different code path**: my machinery computes the full dual, enumerates all bases and all selector assignments, and lands on the same formula the entropy lane obtained by its own enumeration.

That is worth more than the wheel numbers themselves. It is an independent validation that the fibre semantics, dual construction, and certificate definition I have been computing with all session agree with the campaign's — on a nontrivial value, not on a triviality.

## 4. What the contrast says

The star's arms are **coordinate-disjoint**: each contributes a full `β` of defect, and the certificate can only buy one coincidence in total (the hub's residual colliding with one arm's — §6 proves no other dependency exists). So `d_cb` tracks `k` and tightness climbs to 1.

The wheel's rim is **shared**: consecutive spokes overlap in a coordinate, so each constraint contributes less defect (`0.306` rather than `0.415`), *and* the residuals can be shared roughly three-to-one. Both effects run the same way — `d_cb` grows at `k/3` while `L` grows at `0.306k` — leaving tightness less than half the ceiling.

> **Saturation tracks whether constraints contribute independent defect.** Disjoint private parts force one residual dimension apiece and drive tightness to 1; shared coordinates let residuals collapse faster than the defect accumulates, and the family falls away from the constant.

**Consequence for the campaign, stated carefully.** The constant `1/β` is forced by the *disjoint* family, not by the entangled one. That cuts against the intuition that richly-connected objects are the hard ones — for this target, the extremal family is the one whose constraints barely interact. Whether that survives into the residual class is unknown: the class is dense and connector-incoherent, and both of these are known non-members.

## 5. Status

`d_cb(star k) = k−1` is proved. `d_cb(wheel k) = ⌈k/3⌉` is exact at `k = 3..7` and matches the campaign's independently-derived NAE-cycle formula, but is not proved here for general `k`. The tightness limits follow from those, so the star's is proved and the wheel's is conditional on its formula.
