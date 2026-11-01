# Hostile referee report: `cluster_lemma_attempt1.md`

Referee: adversarial subagent, campaign session c53c1d50, iteration 2, 2026-08-19 ~05:0x.
Everything below is my own re-derivation or my own exact local computation; I did not accept
any quotation, constant, or arithmetic from the note or from `attack_entropy.md` without
redoing it. Scripts (local, seconds, BelowNormal, no files written outside the scratchpad):
`scratchpad\referee_cluster_checks.py`, `scratchpad\referee_cluster_checks2.py`.
Dossier text checks are against `rademacher_dossier.txt` by extraction line number.

Labels: **[BROKEN]** = false, counterexample or reversed step shown. **[CORRECT]** = I re-proved
it or verified it exactly. **[VACUOUS]** = true but carries no content beyond what is already
available. **[OVERREACH]** = stated more broadly than the argument supports. **[UNRESOLVED]**.

## 0. Verdict table

| # | Target | Verdict |
|---|---|---|
| — | Part (1) of the lemma (`D ≤ 1 + C₁(ℓ + Π)`) | **[VACUOUS]** — immediate corollary of Lemma NK(a)+(b) with an absolute constant; nothing in Bands II–V is needed for it |
| — | Part (2) and the note's *repaired* Part (2) | **[BROKEN]** — explicit counterexample below (double-star cluster), support-4 differences, medium mass, defect → 2 |
| 2 | Band III (second moment / half-integer support) | **[BROKEN]** — the change of measure is reversed; conclusion false on the canonical NAE cluster (4 ≤ 3.16) |
| 1 | Band V (disjoint supports via KL superadditivity) | skeleton **[CORRECT]**; shape classification **[BROKEN]**; floor value survives for support ≥ 3 (exact min 0.27807); "Consequence" paragraph **[OVERREACH]** |
| 3 | Band IV (marginal-entropy bound) | proposition **[CORRECT]**; vacuity interval **[BROKEN]** (it is (0.2271, 1], not (0.227, 0.773)); "every counting/entropy route" **[OVERREACH]**; illustrative 45 → 63.6 |
| 4 | Overlap obstruction + balanced slab | slab arithmetic **[CORRECT]**; the section's conclusion is true but hollow (the repaired statement it defends is false anyway) |
| 5 | Support-≤2 dichotomy | **[CORRECT]** — three-line proof given, valid over ℝ with no integrality assumption |
| 6 | 280-sample check | **[VACUOUS]** — zero power by construction; measured: 280/280 settled by the trivial count `D ≤ 2Π` |
| — | "3-adic image bound `D ≤ 1.71 ℓ_B`" (line 18) | **[BROKEN]** — false (D = 7 vs 1.67) and does not follow from image counting in the stated direction |
| — | "second-order differences leave the ternary class" (line 49) | **[BROKEN]** — `d_a − d_b = h_a − h_b` is ternary; the class *is* closed under differences |

---

## 1. MOST DAMAGING: the lemma's part (1) is already free, and part (2) — with the repair — is false

This is one finding in two halves. Together they say the note spent four bands proving something
its own toolkit gives away, and left standing a repaired statement that dies to a hand construction.

### 1.1 Part (1) follows from Lemma NK alone, with an absolute constant [PROVED HERE]

The target as stated in `attack_entropy.md` §Next-step (and copied into this note's line 3) is
`dim span{q_a} ≤ 1 + C₁(ℓ + Σπ_a)` for an **absolute** `C₁`. Take a maximal linearly independent
subfamily of the differences `{d_a}` (this only lowers the mass sum) and split on `u := Π/D`:

* If `u ≥ 1/25`, then `D ≤ 25Π`. Done, no structure used.
* If `u < 1/25`, then `2Π < D/2`, so NK(b) applies in the regime its proof needs and gives
  `D ≤ ℓ + φ(u)·D + log₂(2Π+1) + 1` with `φ(u) = 2u(1 + log₂(e/2u))`.
  `φ` is increasing on `(0,1)` (`φ' = 2 − 2log₂(2u) > 0`), and I computed `φ(0.04) = 0.4869`.
  Hence `0.513·D ≤ ℓ + log₂(0.08D+1) + 1`. For `D ≥ 64` the log term is below `0.1D`, giving
  `D ≤ 2.43·ℓ`. For `D < 64`: if `Π ≥ ½` then `D ≤ 128Π`, else NK(a) gives `D ≤ ℓ + 1`.

So **`D ≤ 1 + 128(ℓ + Π)` unconditionally** — no fibre structure, no shapes, no KL, no field
restriction beyond NK's own (ℝ and odd 𝔽_p). I made no attempt to optimise 128.

I re-proved NK(b) itself rather than trusting it: Markov gives `|B|/2` points with
`|viol(x)| ≤ 2P`; for fixed `S`, `{viol ⊆ S}` lies in a subspace of dimension `m − D + |S|`, which
holds at most `2^{m−D+|S|}` cube points (a `k`-dimensional subspace contains ≤ 2^k cube points —
project onto `k` coordinates on which the subspace is injective); summing over `|S| ≤ ⌊2P⌋` and
using `binom(D,t) ≤ (eD/t)^t` reproduces the stated bound exactly. NK(b) is correct.

One scope caveat, stated honestly: NK applied on the fibre `A` uses the **global** defect `ℓ(A)`
with exactly the target's masses `π_a = Pr_A(...)`; the literal target writes `ℓ_supp(A_C)`, which
is ≤ ℓ (since `|A| ≤ |A_C|·2^{r−|C|}`). Applying NK on `A_C` instead delivers `ℓ_supp(A_C)` but with
masses under uniform-`A_C`, not under uniform-`A`. Either version is enough for the §3 assembly,
which charges against the block's defect. Neither needs Bands II–V.

**Consequence for the note.** Bands II, III, IV, V are not proofs of the cluster lemma; they are
attempts to improve the *constant* (or to reach the much stronger `D ≤ (1+o(1))ℓ`). The note never
says this, and its "Net effect" line — "the cluster lemma is PROVED in Bands I–III … OPEN exactly
in (medium mass) × (large core defect)" — is doubly wrong: Band III is false (§2), and the medium
band is precisely where the stated inequality is **trivial**, because medium masses mean
`Π = Θ(D)` and the right-hand side is already of order `D`. The note's organising question is
mis-posed against its own target.

### 1.2 The repaired Part (2) is FALSE — the double-star cluster [PROVED HERE + EXACT ENUMERATION]

The note's repair (line 25) is: `Σ_{a∈I} π_a ≤ C₁ · ℓ_ent(A_C)` for any independent subfamily `I`
of **support-≥3** differences. Line 26 names the falsifier it could not find:

> "A genuine test needs a fibre with many independent support-≥3 ternary forms of medium mass;
> whether one exists with sublinear defect is THE open question of this note … If such a fibre
> exists, the cluster lemma as stated is FALSE."

It exists, and it is small enough to write down. **Double-star cluster.** Coordinates: private
`x₀`; core `{h₁, h₂} ∪ L₁ ∪ L₂` with `|L₁| = |L₂| = k`. Rows (all sharing the private part `+x₀`,
same sign, exactly the cluster hypothesis):

```
h_a = x₀ + x_{h₁} + x_a   (a ∈ L₁)          h_b = x₀ + x_{h₂} + x_b   (b ∈ L₂)
```

Fibre `A = {x : every row ∈ {±1}}` — i.e. NAE on each triple; equivalently `{i : x_i = x₀}` is an
independent set of the double star. Fix `a₁ ∈ L₁` as the reference row and take the differences

```
d_b = q_b − q_{a₁} = x_{h₂} + x_b − x_{h₁} − x_{a₁}      (b ∈ L₂)
```

— support 4, all-±1 coefficients, ternary on the fibre by construction, and linearly independent
(each carries its own leaf `x_b`). Closed form `|A| = 2(2^k+1)²`, so
`ℓ = 2[1 − log₂(1+2^{−k})] → 2`. Exact enumeration confirms the formula and everything else:

| k | \|A\| | ℓ(A) | ℓ_supp(A_C) | ℓ_ent(A_C) | D | mean π | Π | Π/ℓ_ent(A_C) |
|---|---|---|---|---|---|---|---|---|
| 2 | 50 | 1.3561 | 0.4764 | 0.5161 | 2 | 0.522 | 1.043 | 2.02 |
| 4 | 578 | 1.8251 | 0.8351 | 0.8389 | 4 | 0.502 | 2.007 | 2.39 |
| 7 | 33282 | 1.9775 | 0.9777 | 0.9778 | 7 | 0.500 | 3.500 | 3.58 |

`Π ≈ k/2 → ∞` while `ℓ_ent(A_C) → 1` and `ℓ(A) → 2`. The ratio grows linearly in `k`; at `k = 100`
it is ≈ 50. **The repaired Part (2) fails by an unbounded factor, with support-4 differences of mass
exactly ½ on a fibre of O(1) defect.** (The masses above are measured both ways — under uniform-`A`
and under uniform-`A_C` — and both → ½, so no reading of "mass" or of "defect" rescues it.)

The mechanism is the one the repair does not control: **linear independence of the difference
*forms* is not independence of the *constraints* they impose.** All `k` support-4 differences here
are made cheap by the same two-bit event (`x_{h₁} = x_{h₂} = −x₀`), after which each `d_b` collapses
on the fibre to the support-2 form `x_b − x_{a₁}`. "Support ≥ 3" is a property of the form, not of
its constraint content, so the dichotomy cannot do the work the repair asks of it.

This also settles, negatively, the note's line 31 — "**one concrete search question now gates
everything** … a designated computation for the fleet". It is answered here by hand; it should not
be queued, and it gates part (2) only, not part (1) (§1.1).

### 1.3 Scope, stated honestly

The double-star does **not** threaten the dossier's actual target. In it, `dim span{q_a} = 2k`, but
`d_cb`-style accounting selects each row against its own leaf coordinate (`x_a`, `x_b` — coordinates
are always in the full dual), leaving the two-dimensional residual span `⟨x₀+x_{h₁}, x₀+x_{h₂}⟩`
against `ℓ ≈ 2`. That is comfortably linear.

Which is the real lesson, and it is worse for the route than any single arithmetic slip:
**`dim span{q_a}` is the wrong invariant.** It exceeds the residual dimension the rooted estimate
actually needs by a factor that here is `k` and in general can be `Θ(4^ℓ)` (the dossier's own core
bound `|C| ≤ C₀4^L`, extraction line 6749). Any "cluster forcing-mass lemma" phrased on the span —
proved or not — is charging for directions the certificate never pays for. The `§3` assembly in
`attack_entropy.md` inherits this: it needs the *selector residuals*, not the row spans.

---

## 2. Band III [BROKEN] — the change of measure runs backwards (target 2)

Line 15: "`E_cube[(d_a/2)²] ≤ 2^{ℓ_B}·E_A[(d_a/2)²]` (density of A-uniform w.r.t. cube-uniform is
`2^{ℓ_B}1_A`)". The parenthesis is right and it proves the **opposite** inequality: with
`dU_A/dU_cube = 2^{ℓ}1_A ≥ 0`,

```
E_A[g] = E_cube[2^ℓ 1_A g] ≤ 2^ℓ E_cube[g]        (for g ≥ 0)
```

i.e. `E_A ≤ 2^ℓ E_cube`, never `E_cube ≤ 2^ℓ E_A`. No inequality of the note's form can hold for
any constant: take `g = 1_{A^c}` — `E_A[g] = 0` while `E_cube[g] > 0`.

Break shown on the *canonical cluster of the whole campaign* (two NAE rows sharing a private
coordinate — `h₁ = x₀+x₁+x₂`, `h₂ = x₀+x₃+x₄`, `d = h₂−h₁`, support 4):

```
|A| = 18, ℓ = 0.8301, p = 4/9 = 0.4444
E_A[(d/2)²]     = 0.4444  (= p, so that step of the note is correct)
E_cube[(d/2)²]  = 1.0000  vs the note's claimed bound 2^ℓ·E_A = 0.7901   → FALSE
Band III conclusion |supp(d)| ≤ 4·2^ℓ·p :  4 ≤ 3.1605                     → FALSE
```

The aggregate conclusion `D ≤ 4·2^{ℓ_B}Π` is false too, not merely unproved: a single form with
`d = x₁+x₂+x₃+x₄` on `A = {d = 0} ∪ {one point with d = 2}` in `m = 10` has `ℓ = 1.4113`,
`Π = 1/385 = 0.0026`, so the claimed bound is `0.0276` while `D = 1`. And the inequality cannot be
patched by a better constant: for `d = Σ_{i≤s} x_i` on the fibre `{|d| ≤ 2}`, support grows like
`s` while `2^ℓ ≍ √s`.

Band III is the note's only "genuinely linear in Π with NO log factor" band and the only one it
flags as the fallback route if the cluster lemma fails ("the entropy memo's §3 program needs the
Band-III real-field route plus a separate F_p argument", line 26). It is dead. Nothing else in the
note depends on it, so the damage is contained — but the "PROVED in Bands I–III" claim must go.

---

## 3. Band V [skeleton CORRECT, shape step BROKEN, constant survives] (target 1)

**(a) Data processing — CORRECT.** `KL(U_A ‖ U_cube) = Σ_{x∈A} (1/|A|)log₂((1/|A|)/2^{−m}) = m −
log₂|A| = ℓ` bits, and KL decreases under the pushforward `X ↦ (d_a(X))_a`. Direction and base
correct. (In the cluster application the relevant reference is the core marginal, where the same
computation gives the *entropy* defect — fine, and worth writing explicitly.)

**(b) Superadditivity — CORRECT.** For a product reference `Q = ∏Q_a`,
`KL(P‖Q) = −H(P) + ΣH(P_a) + ΣKL(P_a‖Q_a) = KL(P‖P_prod) + ΣKL(P_a‖Q_a)`, and `KL(P‖P_prod) ≥ 0`
is the multi-information. I verified the identity symbolically and numerically (three random
3×4 joints, residual 2e−16). Disjoint supports are exactly what makes the cube law a product —
the hypothesis is used correctly and is not removable.

**(c) The shape fact — BROKEN as stated, harmless in effect.** The note asserts the only realizable
difference shapes are "all-±1 coefficients on even support s ≥ 4, or the 2,2-shape", with natural
mass in `[4/7, 2/3]`. Wrong. A difference of two ±1-coefficient rows has coefficients in
`{0,±1,±2}`, so the realizable class is `(2^j, 1^t)` with `t` even (parity: the row `λx_j + q` is
±1-valued only if `|supp(q)|` is even, and `t = |supp(q_a) △ supp(q₁)|`). Realizable and missing
from the note's list, with cube masses I computed exactly:

| shape | natural conditional mass | note's claimed range |
|---|---|---|
| (2,1,1) — e.g. rows `x₀+x₁+x₂`, `x₀−x₁+x₃` | 2/3 | inside |
| (2,2,1,1) | 0.6 | inside |
| (1,1) support 2 | 1/2 | **outside** |
| (2,2) | 0 | **outside** |
| (2), (2,2,2) | 1 | **outside** |

The verified numbers the note does state are right: `s = 4 → 4/7`, `s = 6 → 0.6`, `s = 8 → 0.6154`,
`→ 2/3`.

**(d) The floor 0.278 — the number is right for support ≥ 3, the stated claim is not.** Two
problems. First, line 46's formula as literally written mixes an unconditioned `q₀ = 0.375` with a
*conditioned* `q₂ = 4/7` and evaluates to **0.201014**, not 0.278; line 47's version
(`q₀ = 6/16, q₂ = 8/16`, both unconditioned) evaluates to **0.278072**. They are not, as line 47
says, "the SAME arithmetic". Use line 47's — it is the legitimate one (lumping the ±2 masses is a
valid lower bound by the log-sum inequality). Second, "κ₀ ≥ 0.278 uniformly over shapes" is false
once support-2 ±1 shapes are admitted (and they are realizable in clusters): there
`q₀ = q₂ = ½`, the floor at `p = 0.4` is **0.0290**, and it → 0 as `p → ½`.

I then computed `min_{p ≤ 0.4} KL` over the whole realizable class `(2^j,1^t)`:
**the minimum over support ≥ 3 is 0.27807, attained exactly at the note's `s = 4` shape**; every
mixed shape is strictly worse for the adversary (0.629, 0.795, 1.044, …), and the degenerate
`(2,2)`, `(2)`, `(2,2,2)` give an infinite floor. So the constant survives — for the right reason,
which the note did not give.

**(e) Final split — CORRECT.** `p_a ≥ 0.4 ⇒ D_high ≤ Π_high/0.4 = 2.5Π_high`; `p_a < 0.4 ⇒
0.278·D_low ≤ ΣKL ≤ ℓ ⇒ D_low ≤ 3.60ℓ`. Arithmetic fine. With support-2 shapes admitted the
constant degrades to `ℓ/0.029 = 34.5ℓ` but the *conclusion* still holds (the true, unlumped KL for a
support-2 form at mass p is `1 − h(p)`, which beats `(1−2.5p)/3.6` throughout `p ≤ 0.4`).

**(f) "Consequence" paragraph — OVERREACH.** "THE OPEN CASE IS NOW ONLY OVERLAPPING SUPPORTS" reads
as though the frontier had narrowed to a technicality. The double-star of §1.2 lives exactly there,
and it is not a frontier, it is a counterexample to the note's own repaired Part (2). Also, in a
cluster the disjoint-support case is structurally special: disjointness forces `q_a = q₁ + e_a` with
the `e_a` disjointly supported, and then the fibre constraint forces every nonzero `e_a(x)` to carry
the *same* sign `−h₁(x)` — a strong extra constraint the proof never uses and which should be stated
so a reader does not overrate the generality.

**One line the note gets wrong in its own favour:** step (iii) says the divergence "is 0 only at the
natural mass". Against the unconditioned reference the minimum is `log₂(1/(q₀+q₂)) > 0` (0.1926 at
`s = 4`), not 0.

---

## 4. Band IV [proposition CORRECT, frontier BROKEN, universality OVERREACH] (target 3)

**Proposition — CORRECT, and I checked the step the note glosses.** Conditioning on the sign
pattern puts `x` in an *affine* slice `{d_a = ±2 or 0 as specified}`, not a linear coset — the note
says "coset of ⋂ker d_a", which is not literally right. The bound survives: an affine subspace of
dimension `k` contains at most `2^k` points of `{±1}^m` (project onto `k` coordinates on which the
direction space is injective), so `H(X|pattern) ≤ m − D` still holds. With `H(X) = m − ℓ_B` and
`H(pattern) ≤ Σ H(sign d_a) = Σ(h(p_a)+p_a)` (even ± split maximises, correct), the proposition
`D ≤ ℓ_B + Σ(h(p_a)+p_a)` is proved. Field-agnostic and structure-free, as claimed.

**Vacuity frontier — BROKEN.** The note states `h(p)+p ≥ 1` "exactly for p ∈ (≈0.227, 1]" and then,
two sentences later, that the pay-1-bit region is "precisely `p_a ∈ (≈0.227, 0.773)`". The second is
wrong and contradicts the first: `h(p)+p` is not symmetric about ½ (the `+p` term breaks it). Solved
numerically: the lower root is `p₀ = 0.227092`, and `h(p)+p > 1` for every `p ∈ (p₀,1)`, with
equality only at `p = 1` (`h(0.773)+0.773 = 1.546`, `h(0.99)+0.99 = 1.071`). **The correct vacuity
region is (0.2271, 1]** — larger than claimed, so the note's "the vacuity frontier is now exact"
overstates in the direction of the bound being *more* useful than it is.

**"Every counting/entropy route pays ≥ 1 bit per dimension" — OVERREACH.** This is a claim about
arguments not yet invented, supported only by three specific bounds (NK(b), the coset/binomial
count, and this one). It is refuted in spirit by the note's own next section: Band V is an entropy
route (pattern map + KL) that is non-vacuous at `p = ½` for support-4 shapes. Retain the honest
version: *these three routes* are vacuous there.

**Illustrative arithmetic — wrong.** "100 forms at p = 0.05, ℓ_B = 30: NK(b) ≈ 77, this ≈ 45". I get
Band IV `= 30 + 100(h(0.05)+0.05) = 30 + 33.64 = 63.6`, and NK(b) `= 92.1` with all its terms
(77.6 if the `+1`s are dropped). The qualitative point — Band IV wins in the many-small-masses
regime, with no log factor — is right; the number 45 is not.

---

## 5. Overlap obstruction and the balanced slab [CORRECT but hollow] (target 4)

Slab arithmetic verified exactly: `ℓ = m − log₂ C(m, m/2)` (1.8707 at m = 8, 2.2552 at m = 14,
against the note's `≈ ½log₂ m` + 0.326: 1.826, 2.230 — "about ½log₂ m" is fair); pair mass
`m/(2(m−1))` confirmed (0.5714 at m = 8); `D = m−1` independent differences; `Π = m/2`;
`D/Π = 2(m−1)/m → 2` (1.750 at m = 8, 1.857 at m = 14). So "any true bound is ≥ 2Π − o(Π)" and
"Band III's constant cannot drop below 2 even at ℓ_B = 0" are **correct**, for statements that admit
support-2 differences.

The dichotomy does exclude the slab (its differences are ternary on the whole cube), so the note's
self-correction inside line 26 is right. But the section is hollow: the statement it rescues from
the slab is refuted anyway by §1.2, and the note's own honesty ("the accounting is circular unless
the constraint-counting is done at the level of a well-chosen independent subfamily") is the right
instinct pointed at the wrong fix — the failure is constraint-sharing, not subfamily choice.

Separately, the parent memo's escape hatch for the excluded case — `attack_entropy.md` §3 Gap 1,
"each such row carries conditional forcing mass … and these masses again sum into ℓ" — is also
false. Rows `h_a = x₀ + x_a + x_u` (a = 1..m−1) give a cluster with `ℓ ≈ 1`, `ℓ_supp(A_C) = 0`,
`m−2` independent support-2 differences of mass ≈ ½ each, total ≈ (m−2)/2. Support-≤2 clusters are
therefore not the easy case; they are unhandled.

## 6. The support-≤2 dichotomy [CORRECT] (target 5)

I proved it rather than inheriting it, and the proof is shorter and stronger than the note's "case
analysis": let `f = Σ_{i∈S} c_i x_i` take values in `{0,±2}` on the whole cube, `c_i ≠ 0`. Flipping
`x_i` changes `f` by `2c_i`, a nonzero difference of two elements of `{0,±2}`, so `2|c_i| ∈ {2,4}`,
i.e. `|c_i| ∈ {1,2}` — no integrality assumption needed, valid over ℝ. Replacing `x_i` by `σ_i x_i`
we may take all `c_i > 0`; then `f(𝟏) = Σ|c_i| ≥ |S|`. If `|S| ≥ 3` this exceeds 2. ∎

Brute force over all integer coefficient vectors with `|c_i| ≤ 4` and support ≤ 5 agrees: six
ternary-on-cube forms, all of support ≤ 2 (`(±2)`, `(±1,±1)`), none of support ≥ 3.

The dichotomy is load-bearing for both notes and it holds. What it does *not* do is what the note
asks of it in Part (2) (§1.2): "support ≥ 3" bounds the form, not its constraint content.

## 7. The 280-sample check [VACUOUS — no power] (target 6)

The test cannot see a violation, and I measured this rather than arguing it. A violation of
`D ≤ ℓ + 2Π + 1` requires mean mass `Π/D < ½` *and* a small defect. But the natural cube mass of a
support-4 ternary form is `4/7 = 0.5714`, and random fibres do not suppress it. Replicating the
design (280 random support-4 systems, m = 14, greedy independent subfamily by increasing mass):

```
systems with nonempty fibre: 280 ;  violations: 0
systems where the TRIVIAL count D ≤ 2Π already settles it: 280/280
mean mass Π/D:  min 0.5263   mean 0.5709   max 0.6000
```

Every single sample was decided by `2Π ≥ D` before `ℓ` was even looked at. The note's own reported
worst case is the same story: `ℓ = 0.656, Π = 2.20, D = 4` has `2Π = 4.4 ≥ 4 = D`. So "zero
violations, worst margin +2.05" is not evidence for the bound — it is evidence that the sampler
never produced a family with mean mass below ½. The honest weight of the section is zero, not
"survives its first contact". A positive control (does the sampler ever emit `Π/D < ½`? — it does
not) would have caught this before it was written down.

What such a test cannot see even if repaired: adversarial constraint-sharing (the double-star's
mechanism), overlapping supports engineered at fixed `(ℓ, Π)`, non-±1 coefficient rows, `𝔽_p`, and
anything at `m` beyond ~20.

## 8. Smaller breaks and unverifiable items

* **Line 18, "the crude 3-adic image bound gives `D ≤ ℓ_B/log₂(3/2) ≈ 1.71·ℓ_B` independent of Π"
  — BROKEN.** The double-star has `D = 7` independent ternary-on-`A_C` forms at
  `ℓ_supp(A_C) = 0.9777`, i.e. `1.71ℓ = 1.67 < 7`; it fails for every `k ≥ 2` in my table. Nor does
  it follow from image counting: patterns number ≥ `|A|/2^{m−D} = 2^{D−ℓ}` and ≤ `3^D`, which yields
  `D ≥ ℓ/log₂(3/2)` — a *lower* bound on D, vacuous as an upper bound. (If the intended argument was
  "each independent ternary constraint costs `log₂(4/3)` of defect", giving `D ≤ 2.409ℓ`, that is
  false for the same reason and would also collide with the dossier's own constant floor.)
* **Line 49, "second-order differences leave the ternary class" — BROKEN.** `d_a − d_b = q_a − q_b =
  h_a − h_b`, a difference of two ±1-valued rows sharing the private part: ternary. The cluster's
  difference family is closed under differences and can be re-rooted at any member. The claim is
  used to argue "a genuinely new idea is needed there"; the conclusion may be right, the reason is
  not.
* **Band II — CORRECT with a missing hypothesis.** `D ≤ (1+o(1))ℓ_B` needs `ℓ_B = ω(log D)` for the
  `log₂(2Π+1)+1` tail of NK(b) to be absorbed; at small `ℓ_B` the statement as written is not
  supported (it is not false, just unproved — the regime is degenerate since a nonzero form on a
  low-defect fibre has mass ≥ ~½ by Littlewood–Offord).
* **Band I — CORRECT.** NK(a) plus the union bound `Pr(all vanish) ≥ 1−Π`; I re-derived the
  subspace-counting step.
* **Unverifiable as written:** the note cites `scratchpad/ternary_search.py`, seed 20260819, in a
  *different session's* scratchpad; I could not read it and did not try to. My §7 numbers are my own
  reimplementation of the described design, not a rerun of theirs. If their code disagrees with
  `Π/D ≥ ½`, that itself needs explaining.
* **Provenance of the setting — CHECKED.** Rows have the form `h_a(x) = q_a(x_C) + λ_a x_j` with at
  most one private `j ∉ C` and `λ_a = ±1` (dossier extraction lines 2013–2037, tags (20)–(21));
  the free/never-free dichotomy is at lines 6752–6760; `|C| ≤ C₀·4^L` at line 6749. The note's
  standing facts (line 5) are consistent with the source; its "coefficients of `d_a/2` are
  half-integers" is true but the operative fact is the sharper one it never states: coefficients of
  `d_a` lie in `{0,±1,±2}` with an even number of odd ones.

## 9. Repairs — what would save what is savable

1. **Delete Band III.** If anything is kept, keep only the true direction, `p_a ≤ 2^ℓ·‖c‖²/4`
   (a lower bound on support in terms of mass), and say plainly that it is useless for the lemma.
2. **Band V: drop the shape enumeration entirely and use Littlewood–Offord.** For *any* form of
   support ≥ 3 with nonzero real coefficients, Erdős's LO bound gives `q₀ = Pr_cube[d = 0] ≤ 3/8`,
   and `q₀ + q₂ ≤ 1`. The lumped floor is decreasing in both, so
   `min_{p ≤ 0.4} KL ≥ min(f(0.4)|_{q₀=3/8,q₂=5/8}, log₂(1/(q₀+q₂))) ≥ 0.1493`,
   giving **`D ≤ 2.5Π + 6.70·ℓ` for every disjoint family of support-≥3 ternary forms**, with no
   shape classification, no ±1-coefficient assumption, and no case analysis. Keep 0.278 / 3.60ℓ only
   as the sharper constant for ±1-coefficient rows (my table proves 0.27807 is exactly the minimum
   there, at s = 4). Fix line 46's formula, delete the "SAME arithmetic" sentence, and state the
   hypothesis as "support ≥ 3" instead of listing shapes.
3. **Band IV:** correct the vacuity region to `(0.2271, 1]`; replace "every counting or entropy
   route" with "these three routes"; fix 45 → 63.6; say "affine slice" not "coset" and add the
   one-line affine-subspace counting argument.
4. **Part (1):** restate as a corollary of NK(a)+(b) (§1.1) with an explicit absolute constant, and
   re-label Bands II–V as constant-improvement / coefficient-1 work, which is what they are.
5. **Part (2) and its repair:** mark DEAD with the double-star, and record the mechanism
   (constraint-sharing) as the obstruction, not "medium mass".
6. **Re-aim the programme at the right invariant.** The live question is not `dim span{q_a}` but the
   minimal residual dimension over basis + signed selectors. The double-star is the test case for
   the reformulation: `span{q_a}` has dimension `2k`, the residual span has dimension 2, `ℓ ≈ 2`.
   A cluster lemma phrased on residuals is not refuted by anything in this report.
7. **Line 18 and line 49:** delete the 3-adic bound; correct the closure-under-differences claim.
8. **Sampling:** either delete §"First sampling data point" or rebuild it with a positive control —
   the sampler must be able to emit families with `Π/D < ½` (e.g. condition fibres on suppressed
   masses, or search rather than sample), otherwise the trivial count decides every trial.

## 10. What I tried that did *not* break the note

Recorded so the next referee does not repeat it, and so the surviving parts get their due:

* **Attacking Band V's data-processing and superadditivity steps.** Both are correct; I verified the
  identity numerically and re-derived it. The idea — compare the fibre's pattern law to the cube's
  *product* pattern law and let disjointness buy superadditivity — is the best thing in the note and
  is genuinely new relative to NK. It would have broken if the cube pattern law were not a product
  (it is, under disjointness) or if the lumped-KL step were invalid (log-sum makes it valid).
* **Looking for a counterexample to Band V's conclusion using support-2 shapes at `p → ½`.** The
  stated floor collapses there (0.029 at p = 0.4, → 0 at ½), but the conclusion does not: the true
  unlumped KL for the aligned-pair fibre is exactly `log₂(4/3) = 0.415` per form, and in general
  `1 − h(p)` beats `(1 − 2.5p)/3.6` on `p ≤ 0.4`. Band V's *conclusion* survives even with the wrong
  hypothesis list.
* **Trying to falsify Band IV's proposition via the affine-vs-linear gap** in the coset step. The
  affine version of the `2^k` cube-point bound is true, so the proposition stands.
* **Trying to break part (1) with disjoint-support constructions at low mass** (`D` forms at
  `p = 0.01`): the KL cost per form (1.33 bits at s = 4) forces `ℓ ≥ 1.33D`, far above the `0.27D`
  a violation would need.
* **Trying to make the double-star break part (1) as well as part (2).** It cannot: `Π ≈ k/2` sits on
  the right-hand side. That asymmetry is exactly what shows part (1) is the weak statement.
* **Checking the slab numbers, the `4/7, 0.6, 0.6154 → 2/3` mass sequence, the `p₀ = 0.227` root,
  the `2.5Π + 3.6ℓ` split arithmetic, NK(a), NK(b)'s proof, and the dichotomy.** All correct.

---

## Disposition

**PARTIALLY BROKEN.** Band I, Band II (with a hypothesis added), Band IV's proposition, the
dichotomy, and the slab extremal are correct; Band V's skeleton is correct, its shape step is
false and its floor survives only for support ≥ 3 (and is better replaced by a shape-free
Littlewood–Offord floor). But Band III is false with the break exhibited, Part (2) *and* the note's
repaired Part (2) are false with a hand counterexample at O(1) defect, Band IV's "exact" vacuity
frontier is wrong on its upper end, the sampling section has no power, and — the finding that
reorganises the rest — Part (1) is an immediate corollary of Lemma NK, so the note's four bands are
constant-hunting on a statement that was already free, while the quantity they bound
(`dim span{q_a}`) is not the quantity the rooted target needs.

Nothing here bears on the sharp Rademacher singularity conjecture, which remains open; nothing here
moves the block-internal certificate for dense connector-incoherent cores, which remains untouched.
