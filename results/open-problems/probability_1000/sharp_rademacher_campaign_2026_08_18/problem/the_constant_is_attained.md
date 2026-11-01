# The constant is attained, not merely approached: `d_cb = m` for m disjoint NAE triples

Author: main session c53c1d50, 2026-08-19 ~14:0x. The star family was proved today to force `C ≥ 1/β` asymptotically. The disjoint-triples family does better: it attains `1/β` **exactly, for every m**, and its proof is shorter.

## 1. The reformulation that found it

Conjecture RC (`d_cb ≤ L/β`) rewrites, using `L = ℓ = r − log₂|A|` and `β = log₂(4/3)`, as

  **`|A| ≤ 2^r · (3/4)^{d_cb}`** — *a fibre whose certificate needs `d_cb` residual dimensions may keep at most `(3/4)^{d_cb}` of the cube.*

Checked against every object computed this session, it holds throughout and is met with **equality by exactly two**: the NAE triangle (`6 = 2³·(3/4)`) and the two-disjoint-triples threshold object (`36 = 2⁶·(3/4)²`). Both are `m` disjoint NAE triples, at `m = 1, 2`. That is what pointed at the family.

**And the `3/4` is the same `3/4` as Claim Q** — the largest fraction of the cube on which a non-coordinate dual form can be `±1`-valued. It appears here as the price of one residual dimension. One extra dual form, one factor of `3/4`.

## 2. The family, exactly

For `m` disjoint NAE triples on `r = 3m` coordinates: `|A| = 6^m`, so

  `ℓ = 3m − log₂(6^m) = m(3 − log₂6) = m(2 − log₂3) = mβ` exactly.

**Its dual is a disjoint union.** On a product fibre a form `f` satisfies `f·x = Σ f_i·x_i ∈ {±1}` for all independent choices only if at most one block-component is non-constant — so `D(A) = ⊔_i D(A_i)`, and each triangle contributes 4 forms (its 3 coordinates and its homogenizer `h = e_a+e_b+e_c`). Hence `|D| = 4m`, confirmed at `m = 1,2,3` (4, 8, 12).

## 3. `d_cb = m`, proved

**Basis structure.** A basis must span each block's 3-dimensional coordinate space, and only that block's 4 dual forms have support there, so it holds **exactly 3 per block** — `3m = r` forms, using up the whole basis. Exactly **one form per block is left over**: `m` residuals.

**Own-block components never vanish.** `R_i`'s block-`i` part is `f_i` (if its selector lies in another block) or `f_i − σg` with `g` a *distinct* block-`i` form. The four forms `e_a, e_b, e_c, h` are pairwise non-proportional, so either way it is nonzero.

**No dependency exists.** Suppose `Σ_{i∈S} c_i R_i = 0` with all `c_i ≠ 0`. Block `i` needs a foreign toucher — some `R_j`, `j ≠ i`, whose selector lies in block `i`. A residual selecting its own block touches nothing foreign, so the covering must be done by the others and must hit all `|S|` blocks using at most `|S|` residuals: the selector map is a fixed-point-free bijection. Hence every selector is foreign, every own-block part is the **raw** `f_i`, and each block has **exactly one** toucher, giving the two-term equation `c_i f_i + c_j(−σ_j g_j) = 0`. So `f_i ∥ g_j`, both block-`i` forms from a pairwise non-proportional quadruple, forcing `f_i = g_j` up to sign — impossible, since `f_i` is a leftover and `g_j` is in the basis. ∎

**No exception, unlike the star.** In the star the hub form `e_q` belongs to no arm and escapes this argument, which is exactly what buys that family its one dependency and drops it to `k−1`. Here **every dual form lies in exactly one block**, so nothing escapes: there is no dependency at all, and `rank = m`.

> **Theorem. For `m` disjoint NAE triples, `d_cb = m` and `ℓ = mβ`, so `d_cb = ℓ/β` exactly.**

Verified exactly at `m = 1, 2, 3` (`d_cb` = 1, 2, 3; tightness 1.0000 throughout).

## 4. What this settles about the constant

The star family forces `C ≥ 1/β` in the limit, never reaching it. This family reaches it at every `m`:

> **`1/β` is exactly optimal. It cannot be lowered — the disjoint-triples family violates any smaller constant at every `m` — and it suffices with equality on that family.**

This is also the campaign's own floor family seen properly. The floor `C ≥ 1/log₂(4/3)` was carried from **NAE three-circuit products**, which is exactly this: a product of `m` NAE three-circuits. What is added here is the *exact* value `d_cb = m` with a proof, so the floor is not merely exhibited but attained with equality along an infinite family, and the cube-fraction bound is tight all along it.

## 5. Scope

Disjoint triples are a product of independent blocks — as far from the residual class as an object can be, since the class is a *single* strongly connected block. So this pins the constant for the machinery while saying nothing about the class, which remains the campaign's standing exposure.

## 6. Which target this is about — a currency check, done before anyone over-reads it

A pre-mortem on this result names one likely way it gets misused: read as settling the campaign's constant question. It does not, and the reason is a currency distinction the campaign has already been burned by once (the `μ` verdict, corrected for support-versus-conditional-defect).

**What is proved here is about the UNROOTED bridge.** `d_cb` and `ℓ = r − log₂|A|` are the unrooted quantities, so `d_cb = ℓ/β` on the disjoint family bears on

  `d_cb(A) ≤ C·ℓ`  — the dossier's **global bridge**, whose proved form is exponential, `d_cb ≤ 9·4^ℓ + ℓ`.

**The campaign's Layer-II target is the ROOTED estimate**, `dim((R+R_<)/R_<) ≤ C·L_{Q|W}` with a quotient on the left and a *conditional* defect on the right. Those are different quantities: `dim((R+R_<)/R_<) ≤ dim R = d_cb`, and `L_{Q|W} ≠ ℓ` in general.

So the honest scope is:

- **On the unrooted bridge**, this settles the constant: `1/β` is optimal, attained, and the linear form `d_cb ≤ ℓ/β` is exactly tight along an infinite family. That is a statement about the very inequality whose only proved version is exponential — which is what makes it worth having.
- **On the rooted target**, it is evidence and not more. The two agree on the star at the hub rooting only because `R_< = 0` there makes the quotient equal `d_cb` — a coincidence of that rooting, not a general identity.

Both readings are useful; conflating them would repeat exactly the error already logged in this campaign, so the distinction is recorded here rather than left to be noticed later.
