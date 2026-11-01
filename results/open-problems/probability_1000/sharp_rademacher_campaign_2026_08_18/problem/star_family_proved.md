# The k-arm star satisfies the rooted target for every k, by explicit construction

Author: main session c53c1d50, 2026-08-19 ~12:1x. Everything else this session measured objects one at a time. This proves a statement about an **infinite family**, which is the first thing here that is not a computation on a fixed object.

## 1. The star's dual, exactly

For the k-arm NAE star — coordinates `q`, `x_i`, `z_i` with `NAE(q, x_i, z_i)` on each arm — the full dual is exactly

  `D = {coordinates} ∪ {h_i = e_q + e_{x_i} + e_{z_i} : i = 1..k}`,

since not-all-equal on a sign triple forces `q + x_i + z_i ∈ {±1}`. So `|D| = (2k+1) + k = 3k+1`, which matches every computed value: 4, 7, 10, 13, 16, 19 at `k = 1..6`.

## 2. The construction achieving `d_cb ≤ k − 1`

Every certificate I built by hand gave rank `k`, so I extracted an optimal one from the exact search and read it off. Writing `u_i = e_{x_i} + e_{z_i}`:

**Basis** (`2k+1` forms): all `h_i`, all `e_{z_i}`, and `e_{x_1}`.

**Leftover forms** needing residuals: `e_q, e_{x_2}, …, e_{x_k}` — exactly `k` of them.

**Selectors:**

| form | selector | residual |
|---|---|---|
| `e_q` | `h_2` | `−u_2` |
| `e_{x_2}` | `−e_{z_2}` | `+u_2` |
| `e_{x_j}`, `j ≥ 3` | `h_1` | `e_{x_j} − e_q − u_1` |

**The cancellation is the whole trick.** `e_q` and `e_{x_2}` produce `−u_2` and `+u_2` — the *same line*. That pair costs one dimension instead of two. Each remaining arm then contributes one fresh direction, and the `e_{x_j} − e_q − u_1` are independent of each other and of `u_2` because they differ in the `e_{x_j}` coordinate.

  `rank = 1 + (k − 2) = k − 1`.

Verified against the exact search at `k = 2, 3` (which produced this certificate) and consistent with the exact `d_cb = 3` at `k = 4`.

## 3. What that proves, for every k

`L = kβ` exactly (each arm contributes `log₂3` of conditional entropy against 2 coordinates, i.e. `2 − log₂3 = β`). Rooted at the hub, `R_< = 0` — the ancestor block is a single unconstrained coordinate whose dual is one form, its own basis, so nothing needs a residual. Hence the target's left side is `rank(R) = d_cb` exactly, and

  left side `≤ k − 1`  <  `k` = `(1/β)·L` = budget.

> **The rooted target with `C = 1/β` holds strictly on the entire k-arm star family, for every `k`, with margin exactly 1 in absolute terms.** Proved by construction, not measured.

This is the first infinite-family statement the campaign has on the rooted target, and it costs one paragraph once the certificate is seen.

## 4. What is still not proved

**The lower bound.** `d_cb = k−1` is verified exactly only at `k ≤ 4`; the construction gives `≤`. So tightness is `≤ (k−1)/k`, an upper bound rising to 1, and **the saturation claim — that the star family approaches exactly tight — still needs `d_cb ≥ k−1`.** That is the same bound-vs-value gap that has bitten three times today, and it is named here rather than glossed: what is proved is that the star never *violates* the target, not that it approaches it.

A lower-bound argument would need to show no certificate does better than `k−1`. The counting is suggestive — `k` forms need residuals and only one coincidence is available — but "only one coincidence is available" is exactly what would have to be proved, and I do not have it.

**Scope.** The star is a known non-member of the residual class, so this is a statement about the machinery on a family we can compute, not about the class.

## 5. Toward the lower bound: a structural lemma, and the k ≤ 3 case closed by structure

§4 named the missing half — `d_cb ≥ k−1`. Here is real progress on it, and a precise statement of what is left.

**The arm structure forces the shape of every certificate.** Only three dual forms have a nonzero component in arm `i`'s two-dimensional space `V_i = span(e_{x_i}, e_{z_i})`: namely `e_{x_i}`, `e_{z_i}`, and `h_i`. A basis must span `V_i`, so it contains **at least two of those three, for every arm** — that is `2k` forms, and `|G| = 2k+1`, so every basis is *exactly two per arm plus one more*. Consequently **exactly `k` forms are left over** needing residuals.

**Lemma (verified over every basis at `k = 2,3,4`; zero violations).**
1. exactly `k` residuals;
2. every residual has a **nonzero** component in its own arm's `V_i`;
3. a residual touches **at most one other arm** — it has a single selector, and a selector has arm-support in at most one arm.

**The consequence, which is the useful part.** Take any dependency `Σ_{i∈S} c_i R_i = 0` with all `c_i ≠ 0`. Read its `V_i`-component for `i ∈ S`: `R_i` contributes something nonzero by (2), and any other `R_j` contributes only if it touches arm `i`, which by (3) happens for at most one arm per residual. So if arm `i` is touched by no other residual in `S`, the equation reads `c_i·(nonzero) = 0` and `c_i = 0` — a contradiction.

> **So every arm in `S` must be touched from within `S`.** Defining `φ(R_j)` = the one foreign arm `R_j` touches, `φ` must map `S` onto `S` with `φ(i) ≠ i` — a **derangement**. Dependencies therefore live on unions of `φ`-cycles of length ≥ 2, and the number of independent dependencies is at most the number of disjoint such cycles:
>
>   `rank(R) ≥ k − (number of disjoint φ-cycles)`.

**This closes `k ≤ 3` by structure rather than by search.** A cycle needs at least 2 elements, so `k = 2` and `k = 3` admit at most one cycle, giving `rank ≥ k − 1` — matching the exact values 1 and 2. No enumeration required.

**What is left, stated precisely.** At `k ≥ 4` two disjoint 2-cycles are combinatorially available, so the counting alone permits `rank = k − 2`. The exact computation nevertheless gives `k − 1` at `k = 4`, which means **the vector equations block multi-cycle dependencies even when the combinatorics allow them**. Completing the lower bound requires showing a `φ`-cycle cannot actually realise a dependency — for a 2-cycle `φ(1)=2, φ(2)=1` this reduces to asking whether `R_1`'s own-arm component can be parallel to `R_2`'s foreign component in `V_1`, and simultaneously the mirror condition in `V_2`. That is a finite check on the small set of possible own-arm and foreign parts, and it is the concrete next step — much smaller than the general problem it came from.

### 5.1 Pure cycles are impossible — and where the argument stops

The finite check §5 called for goes through, for cycles of **any** length.

In a pure cycle each arm `i` in the support is touched by exactly one other residual (its predecessor), so the `V_i` equation has exactly two terms:

  `c_i·a_i + c_j·b_j = 0`.

If `R_i`'s own selector is *foreign*, it contributes nothing to `V_i`, so `a_i` is `f_i`'s **raw** arm-`i` part — one of `e_{x_i}, e_{z_i}, u_i`. Those three are pairwise non-parallel, and `b_j = −σ_j(g_j`'s arm-`i` part`)` is also one of them up to sign. So `a_i ∥ b_j` forces `f_i` and `g_j` to be the *same* arm-`i` form — impossible, since `f_i` is leftover (`∉ G`) and `g_j ∈ G`. **No cycle of any length realises a dependency.**

**Which is why the construction's dependency runs through the hub.** `e_q` is a leftover only in the case `e_q ∉ G`, and it has **no own arm**, so it is not subject to the argument above. In the construction, `e_q − h_2 = −u_2` and `e_{x_2} + e_{z_2} = +u_2` are parallel precisely because the second residual's selector is an *own-arm* form (`−e_{z_2}`), making its `a_2` a **difference** (`u_2`) rather than a raw part — and a difference can be anything in `V_2`.

That splits the residuals cleanly:

- **own-selector** residuals: `a_i` is a difference, unconstrained in `V_i`, but they touch **no** foreign arm, so they cannot serve as anyone's toucher;
- **foreign-selector** residuals: `a_i` is a raw part, and any single toucher of arm `i` produces the contradiction above.

**So in the single-toucher regime the lower bound follows.** Every arm in a dependency's support needs a foreign toucher; foreign-selector residuals lead to the contradiction; own-selector residuals cannot touch. Only the hub residual can touch, and it touches exactly one arm — so a dependency is confined to `{R_hub, R_m}` for that one arm `m`, the dependency space has dimension ≤ 1, and `rank ≥ k − 1`. With the §2 construction achieving `k−1`, that would give **`d_cb = k−1` exactly**.

**The gap, stated so it is not mistaken for closed.** The step "any single toucher of arm `i`" assumes exactly one other residual touches arm `i`. Nothing forbids **several** residuals choosing selectors from the same arm: then the `V_i` equation has several terms, `G_i` spans `V_i`, and the parallelism obstruction evaporates. Ruling that out needs a counting argument on how many foreign touches are available against how many arms need them — every foreign-selector residual still owes its own arm a toucher, which is a real constraint but not one I have closed.

**Status.** `d_cb ≥ k−1` is **proved for `k ≤ 3`** (§5's cycle count) and **proved in general modulo the multi-toucher case**. Exact computation confirms `k−1` at `k = 4`, where multi-toucher configurations exist and evidently do not help — consistent with the gap being closable, which is not the same as closed.

### 5.2 The proof step machine-checked — and the check is stronger than the prose

§5.1's step is exactly the kind that gets built on as if true, so it was checked directly rather than trusted: over **every basis and every selector assignment** at `k = 2, 3`, compute the residuals and examine the dependency space.

| `k` | hub **in** basis | hub **leftover** |
|---|---|---|
| 2 | 900 assignments, **0 dependencies**, min rank **2 = k** | 600 assignments, **0** where the non-hub residuals are themselves dependent, min rank **1 = k−1** |
| 3 | 74,088 assignments, **0 dependencies**, min rank **3 = k** | 74,088 assignments, **0** bad, min rank **2 = k−1** |

**The check covers the case my prose could not.** §5.1's argument handles single touchers and explicitly leaves open the multi-toucher configurations, where several residuals draw selectors from the same arm and the parallelism obstruction dissolves. The enumeration includes all of those, and they produce no dependency either. So at `k = 2, 3` the conclusion is established over every certificate, not merely over the cases the argument reaches.

**Consequences, now verified rather than argued.**

1. **Hub in the basis ⟹ the residuals are independent**, rank exactly `k`. So a certificate that keeps `e_q` can never beat `k`.
2. **Hub as a leftover ⟹ the non-hub residuals are always independent**, so every dependency carries a nonzero hub coefficient. Two independent dependencies would differ by one supported off the hub — impossible. Hence the dependency space has dimension **at most 1**, and `rank ≥ k−1`.
3. Combining with §2's construction: `d_cb = k−1` exactly, at `k = 2, 3`, over all certificates. The box computation gives the same at `k = 4`.

**A structural fact worth stating on its own:** the optimal certificate **must exclude `e_q` from the basis**. Case A's minimum is exactly `k`, so the entire saving of one dimension comes from treating the hub coordinate as a leftover and letting its residual collide with an arm's. That is why the construction looks the way it does, and it is not something I would have guessed.

**Honest scope.** `d_cb = k−1` is now established over all certificates at `k ≤ 3`, and by exhaustive basis search at `k = 4`. The *general-`k`* argument still has the multi-toucher gap of §5.1 — the enumeration shows it is not a real obstruction at small `k`, which is evidence that it is closable, not a proof that it closes.

## 6. The gap closes: `d_cb(star k) = k − 1` for all k, and the star forces `C ≥ 1/β`

§5.1 left the multi-toucher case open. It closes, and by the counting the case itself supplies.

**Step 1 — the leftover structure (proved).** Only `e_{x_i}, e_{z_i}, h_i` have arm-`i` support; a basis must span `V_i`, so it holds ≥2 of them per arm — `2k` forms — and `|G| = 2k+1` leaves exactly one extra. Either the extra is `e_q` (**Case A**, leftovers are `k` arm forms) or a third form of some arm `m` (**Case B**, leftovers are `e_q` plus one arm form for each arm `≠ m`).

**Step 2 — own-arm components never vanish (proved).** `R_i`'s `V_i` part is `f_i^{(i)} − σ_i g_i^{(i)}·[g_i ∈ G_i]`. With a foreign selector it is the raw part `f_i^{(i)} ≠ 0`. With an own-arm selector it is a difference of two *distinct* members of `{e_{x_i}, e_{z_i}, u_i}`, which are pairwise non-proportional, so it is again nonzero.

**Step 3 — no dependency is supported on arm leftovers alone (proved).** Let `S` be the support of a dependency, all `c_j ≠ 0`, all leftovers in `S` arm forms. Arm `i` needs a *foreign* toucher: some `j ∈ S`, `j ≠ i`, whose selector `g_j` is an arm-`i` form. Write `ψ(j)` for the arm of `g_j`. A residual with `ψ(j) = j` touches no foreign arm and covers nothing, so the covering must be done by `{j : ψ(j) ≠ j}`, which must hit all `|S|` arms of `S`. Since `|ψ(S)| ≤ |S|`, **ψ|_S is a fixed-point-free bijection onto the arms of `S`** — a derangement.

Two consequences follow at once. Every `j ∈ S` has a *foreign* selector, so by Step 2 each `a_j` is the **raw** part `f_j^{(j)} ∈ {e_{x_j}, e_{z_j}, u_j}`. And each arm `i` has **exactly one** toucher `j`, so its `V_i` equation is two-term:

  `c_i·a_i + c_j·b_j = 0`,  `b_j = −σ_j g_j^{(i)}`.

Both `a_i` and `b_j` lie in `±{e_{x_i}, e_{z_i}, u_i}`, a pairwise non-proportional triple, so parallelism forces them to be the *same* member — i.e. `f_i = g_j`. But `f_i` is a leftover (`∉ G`) and `g_j ∈ G`. Contradiction. ∎

**This is exactly where the multi-toucher case dies, and it dies of its own counting.** Two residuals selecting into one arm cover at most `|S|−1` arms among the `|S|` needing cover, so some arm is untouched and its coefficient is zero — contradicting full support. Multi-touching cannot occur inside a dependency's support at all.

**Step 4 — assembling.** In Case A there is no hub leftover, so by Step 3 there is no dependency: rank `= k`. In Case B every dependency has a nonzero hub coefficient; two independent ones would differ by a dependency supported off the hub, which Step 3 forbids. So the dependency space has dimension **at most 1** and rank `≥ k−1`. §2's construction attains `k−1`.

> **Theorem. For the k-arm NAE star, `d_cb = k − 1` for every `k ≥ 2` (and `1` at `k = 1`).**

Consistent with every exact computation: `1, 1, 2, 3` at `k = 1..4`, the last from the exhaustive box run.

**What it gives the campaign.** With `L = kβ` and `R_< = 0` at the hub rooting, the target's left side is exactly `k−1` against a budget of `k`. So a constant `C` works on this family only if `k − 1 ≤ C·kβ` for every `k`, i.e.

  `C ≥ sup_k (k−1)/(kβ) = 1/β`.

> **The star family forces `C ≥ 1/β`, for all `k`, proved.** That is an independent derivation of the campaign's floor — previously carried from NAE three-circuit products — from a different family, and it is *asymptotic* rather than attained: tightness `(k−1)/k` approaches 1 without reaching it, so the target holds strictly at every finite `k` while leaving no room in the limit.

**Scope, unchanged.** The star is a known non-member of the residual class. This is a theorem about the machinery on a family we can compute, not about the class.
