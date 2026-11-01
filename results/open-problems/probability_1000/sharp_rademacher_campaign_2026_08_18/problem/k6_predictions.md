> **READ THIS FIRST (added 2026-08-20).** The closing line of this file says "nine registered
> predictions, nine hits". That count is **stale and now wrong**: two of the predictions tabled
> here - `(3,2)` and `(3,1,1)` at `k=6`, both predicted **3** - measured **4**. Both were
> established by exhaustive search, `(3,1,1)` twice from independent directions. The formula those
> predictions were testing is refuted; see `hub_count_formula.md`. The predictions that did hit
> still hit, and the record of registering them in advance is what made the misses informative -
> but the tally in this file should not be quoted.

# Registered predictions for k=6, k=7 and the profile-invariance test

Written **before** the runs were launched, for the same reason the `(2,2)`/`(2,1,1)` predictions
were: three earlier readings in `concentrated_sharing.md` were descriptions fitted to whatever
enumeration had finished, and each died when the enumeration moved. A pattern that has not been
given a chance to fail is not evidence.

## The formula under test

> `d_cb = max(largest attachment group, ⌈k/2⌉)`

Eleven exact values at `k ≤ 5`, no exceptions, one endpoint (`star = k−1`) proved. Neither term
is derived. `⌈k/2⌉` is the weaker of the two — it has no story at all, only four chain values.

## What each run would show if the formula is wrong

Every triangle-tree has `ℓ = kβ` exactly, so all of these hold `ℓ` fixed by construction and
compare `d_cb` alone.

**The `⌈k/2⌉` term (box-01).** The chain has largest group 1, so its `d_cb` is the `⌈k/2⌉` term
with nothing else contributing — the cleanest possible probe of the term I cannot derive.

| case | `r` | prediction | wrong if |
|---|---|---|---|
| chain `m=6` | 13 | **3** | 2 (term is not `⌈k/2⌉`), or ≥4 |
| chain `m=7` | 15 | **4** | 3 (term grows slower), or ≥5 |

Chain values are `1,2,2,3` at `k=2..5`. If the term is really `⌈k/2⌉` the sequence continues
`3,4`. A chain `m=6` of 2 would mean it grows like `⌊k/3⌋` or slower and the fit at `k=5` was
luck; a chain `m=7` of 3 would say the same one step later.

**The floor (box-02).** `⌈6/2⌉ = 3`, so at `k=6` every profile with largest group ≤ 3 should
flatten onto **3**, and only `(4,1)` should rise, to **4**. Four different topologies landing on
the same value is the sharpest form of "topology is invisible below the floor" — and one of them
coming out at 2 or 4 breaks it.

| profile | largest group | prediction |
|---|---|---|
| `(3,2)`, `(3,1,1)` | 3 | **3** |
| `(2,2,1)`, `(2,1,1,1)`, `(1,1,1,1,1)` | ≤2 | **3** |
| `(4,1)` | 4 | **4** |

**Is the profile even the right invariant (box-04)?** Every value measured so far used *one*
representative per profile. That is an untested assumption sitting under all eleven data points.
Six trees at `k=5`, two profiles, structurally different representatives — all predict **3**.
**Two trees sharing a profile and differing in `d_cb` would mean the formula is not merely
unproved but asking the wrong question**, and would retroactively weaken every earlier value.

This is the test I most expect to fail, and the one I would have skipped if I were looking for
confirmation.

## Method note

Each case is capped at its own predicted value. `fast_dcb` returns the first `d` that works, so a
returned value is exact: hitting the prediction confirms it exactly, a lower value refutes it, and
`None` means `d_cb` exceeds the prediction and also refutes it. No outcome is a truncation that
could be read as a value — the failure that cost this campaign six false Conjecture-R violations.

No runtime estimate is stated here. Nothing of this size has been timed, and an ETA before one
production-sized unit has run is a guess that has been 3–25× wrong before.

---

## Results as they returned

**chain `m=6` → `d_cb = 3`, confirmed** (87s, `|D| = 19`). The `⌈k/2⌉` term continues at `k=6`.
The counting bound of §4 in `why_ceil_k_over_two.md` is not merely valid here but *achieved*:
excess needed is `19 − 13 = 6 = k`, and `d_cb` comes in at exactly `⌈6/2⌉`.

`|D| = 19 = 3·6+1` also extends the explicit dual description to `k=6`, which had only been
checked at `k = 2,3,4`.

**Profile invariance at `k=5`: all six confirmed at 3** (18–19s each). Three structurally
different `(1,1,1,1)` trees agree; three different `(2,1,1)` trees agree. Same-profile agreement
holds where it had only ever been assumed.

**But that test is weaker than I framed it.** At `k=5` the floor `⌈5/2⌉ = 3` dominates the group
term for *both* profiles tested (groups 1 and 2, both below 3), so every case was pinned to the
floor regardless of topology. The run confirms trees sharing a profile agree; it could not have
separated one profile from another, because at `k=5` nothing except the star exceeds the floor.
The profile-dependence question is genuinely tested only where the group term binds — `(4,1)` at
`k=6`, which is still running.

Nine registered predictions so far, nine hits. Still outstanding: chain `m=7` → 4, and the six
`k=6` profiles, of which `(4,1)` → 4 is the one that carries information about the group term.
