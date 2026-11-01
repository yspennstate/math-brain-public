# Cluster lemma v2: phrased on residuals, not spans

Author: main session c53c1d50, 2026-08-19 ~02:0x. Written on the explicit recommendation of `problem/referee_cluster.md` §9.6 ("Re-aim the programme at the right invariant… A cluster lemma phrased on residuals is not refuted by anything in this report"). Status: §1–§2 are proved or exactly computed; §3 is a conjecture with its mechanism identified and its failure modes named. Nothing here claims the conjecture, which is OPEN; nothing here moves the block-internal certificate.

## 0. Why v1 was the wrong object (settled, not re-argued)

v1 bounded `dim span{q_a}` — the span of the cluster rows' core parts. The rooted target consumes the *minimal residual dimension over choices of coordinate basis and signed selectors*. The referee's double-star exhibits the gap: span `2k` versus residual `2`, at defect `ℓ ≈ 2`. So v1 was charging for directions no certificate ever pays. See the banner on `cluster_lemma_attempt1.md`.

## 1. The right invariant, and when two rows can share a residual

**Definition.** For a cluster of ±1-valued rows `h_1, …, h_k` (sharing a private part) and a coordinate basis `F` drawn from the full dual, a *selection* assigns each row `a` a signed basis element `σ_a f_a`; its residual is `r_a = h_a − σ_a f_a`. The cluster's cost is
  `d_clu := min over bases and selections of dim span{r_1, …, r_k}`.
Every `r_a` is a difference of two ±1-valued forms, hence **ternary on the fibre** (values in {0, ±2}).

**Lemma S (sharing criterion).** Two rows can be given the *same* residual under some selection iff `h_a − h_b = σ_a f_a − σ_b f_b` for basis elements `f_a, f_b` — i.e. iff their difference is a signed difference of two basis elements. When `F` is the coordinate basis this says `supp(h_a − h_b) ≤ 2`.
*Proof.* Immediate from `r_a = r_b ⟺ h_a − h_b = σ_a f_a − σ_b f_b`. ∎

**Corollary (why the dichotomy is the load-bearing fact after all).** `h_a − h_b` is always ternary on the fibre. By the support dichotomy (proved in the referee's §6: a form ternary on the *whole cube* has support ≤ 2), the rows partition into sharing-classes, and two rows lie in different classes exactly when their difference is ternary *only on the fibre* — i.e. carries genuine fibre content. So `d_clu ≤ #classes`, and distinct classes are separated by real constraints, not by bookkeeping. This is the honest role the dichotomy plays; v1 asked it to bound constraint content, which the referee showed it cannot do.

## 2. The referee's counterexample, solved (exact)

Double-star: private `x₀`, hubs `h₁, h₂`, leaf sets `L₁, L₂` of size `k`; rows `x₀ + x_{h_i} + x_leaf`. Fibre: `{i : x_i = x₀}` is an independent set of the double star.

- **Sharing.** For `a, b` in the same leaf set, `h_a − h_b = x_a − x_b`, support 2 → same class. Across leaf sets the difference has support 4 → different classes. So exactly **2 classes**, and selecting each row against its own leaf coordinate gives residuals `x₀ + x_{h₁}` and `x₀ + x_{h₂}`: `d_clu = 2`, matching the referee's count.
- **The masses collapse — this is the mechanism.** `r = x₀ + x_{h₁}` is nonzero exactly when `x_{h₁} = x₀`. But if the hub takes the root's value, every leaf in `L₁` is forced off it, killing `2^k` configurations: `Pr(x_{h₁} = x₀) = 1/(1 + 2^k)`. So the residual mass is **exponentially small in k**, and the total `Π = 2/(1+2^k) → 0`.
- **Therefore NK(a) alone finishes it**: `D ≤ ℓ + log₂(1/(1−Π)) = ℓ + o(1)`, and `ℓ(A) = 2[1 − log₂(1+2^{−k})] → 2`. Bound `≈ 2`, truth `= 2`. **Exact, in the regime where v1's analogue blew up by a factor of k.**

The contrast is the whole point: on the *same* object, the span invariant has mass `Π ≈ k/2` (medium mass, the vacuous band) while the residual invariant has mass `→ 0` (NK's strongest band). **Optimal selection is a mass-reduction device.**

## 3. The conjecture, its mechanism, and how it could fail

**Conjecture C (cluster lemma v2).** For every cluster in a rooted block there is a basis and selection with
  `d_clu ≤ C · L_{Q|W}` for an absolute constant `C` (or, per the campaign's scoping, any uniform `C = o(log n)`).

**Mechanism that makes it plausible.** A residual is near-vanishing exactly when the selected basis element usually agrees (up to sign) with the row on the fibre. Fibre constraints *create* such agreements: in the double-star the constraint "leaves adjacent to a hub cannot share the root's value" is precisely what forces `x_{h₁} = −x₀` almost always, which is what makes `x₀ + x_{h₁}` almost always zero. Denser constraints ⇒ more forced agreements ⇒ smaller residual masses ⇒ NK's near-vanishing band, where the bound is `ℓ + O(1)`. This runs *with* the density of the residual class rather than against it, which is the opposite of v1's behaviour and is why the reformulation is worth pursuing.

**How it could fail — the honest list.**
1. **No good selector exists.** The mechanism needs, for each class, a basis element that agrees with the row on most of the fibre. Nothing proves one exists; a fibre could spread every row's agreement thinly across many coordinates. *Concrete check:* compute `min_f Pr(h_a ≠ ±f)` over the full dual for the dossier's dense test families (the slice-rooted NAE cycles and dense stars of `attack_entropy.md` §5) — those are the campaign's only dense objects with exactly known duals.
2. **Class count itself could be large.** `d_clu ≤ #classes` is only useful if the classes are few or their representatives' masses are small. The double-star has 2 classes because it has 2 hubs; a fibre with `Θ(ℓ log n)` "hubs" would have that many classes, and then Conjecture C needs the *masses*, not the count, to do the work.
3. **Currency.** Everything above is stated against the fibre's own defect; the rooted target is charged in `L_{Q|W}`. The slice-transfer repair (in `cluster_lemma_attempt1.md`) moves any monotone bound into the right currency at cost of a factor 2, and applies verbatim here.
4. **The optimisation is over bases too**, and the minimum over bases is not obviously attained by the coordinate basis — Lemma S's clean "support ≤ 2" reading is coordinate-basis-specific. A general-basis version of the sharing criterion is unwritten.

**What this note does NOT do.** It does not prove Conjecture C, does not touch clause (ii) absorption, and does not bear on the block-internal certificate for dense connector-incoherent cores, which remains exactly as open as it was. What it does is replace a refuted formulation with one that (a) is the quantity the target actually consumes, (b) reproduces the exact answer on the object that killed the old one, and (c) has an identified mechanism pointing at NK's strongest regime rather than its vacuous one.

**Next concrete step:** failure mode 1's computation — `min_f Pr(h ≠ ±f)` over the full duals of the two known dense families. If those minima are bounded away from 0, Conjecture C is in trouble and the note says so; if they collapse the way the double-star's do, the mechanism has its second data point and a proof attempt is warranted.
