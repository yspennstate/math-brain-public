/-
Constant absorption in the entropy bound: dilation/realification bookkeeping,
the log-absorption inequality, and the norming-set injection count.

This file formalizes four elementary facts that justify "absorbing a constant
into the universal constant `C`" in `paper12/matrix_spencer_lifts.tex`.

1. Entropy bookkeeping under doubling (`thm:lift`, complex case).  The entropy of
   a block lift is `Ent = h · R`, the product of the maximal block size `h` and
   the total reduced dimension `R`.  Passing to the Hermitian dilation doubles
   both `h` and `R` (`h → 2h`, `R → 2R`), so `Ent` grows by a factor of `4`;
   realification doubles them once more, so the two together grow `Ent` by a
   factor of `16`.  The paper states this verbatim ("the entropy changes by a
   factor of four ... each doubles the dimension, so the entropy grows by a
   factor of at most 16, absorbed into the universal constant").  The content is
   the pure arithmetic identities

     (2 h)(2 R) = 4 (h R),        (2(2 h))(2(2 R)) = 16 (h R).

1a. Direct-sum entropy warning.  If all block heights are at most `H`, then
    `sum h_l R_l ≤ H * sum R_l`; if one positive-rank block has height strictly
    below `H`, this inequality is strict, while equality holds when all heights
    are exactly `H`.  The finite component entropy sum is also monotone under
    blockwise enlargement of heights/ranks and under enlarging the finite block
    index set, and splits over disjoint unions of block families.

2. Log absorption (used at every occurrence of `log(e + Ent/n)`).  A constant
   factor `c ≥ 1` inside the logarithm `log(e + c x)` is absorbed up to the
   multiplicative constant `1 + log c`:

     log(e + c x) ≤ (1 + log c) · log(e + x)        (x ≥ 0, c ≥ 1).

   This is what lets one replace `Ent/n` by `c · Ent/n` (e.g. after dilation and
   realification multiply `Ent` by `16`) and keep the same `√(n log(e + Ent/n))`
   shape with only the constant changing.  The proof uses `e + c x ≤ c (e + x)`
   and `log(e + x) ≥ 1`.

3. Norming-set injection count (`lem:grid` / the lower-bound construction).  When
   a family of `(2 w + 1)^r` distinct multi-indices injects into a norming set
   `Q`, the cardinality bound `(2 w + 1)^r ≤ |Q|` follows from
   `Fintype.card_le_of_injective`.  This is the `|Q| ≥ (2w+1)^r` step behind the
   `log(e + (2w+1)^r / n)` lower bound.

Compiles against `mathlib` (see `README.md`).
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace EntropyAbsorption

/-! ### 1. Entropy bookkeeping under doubling

`Ent = h · R`.  Hermitian dilation sends `h ↦ 2h`, `R ↦ 2R`; realification does
the same again.  These lemmas pin the resulting constants `4` and `16` exactly,
over `ℝ` and over `ℕ`. -/

/-- **Dilation entropy factor (`×4`).**  Doubling both the maximal block size
`h` and the total reduced dimension `R` multiplies the entropy `h · R` by `4`:

  `(2 h) · (2 R) = 4 · (h R)`.

This is the factor produced by Hermitian dilation alone. -/
theorem ent_double : ∀ h R : ℝ, (2 * h) * (2 * R) = 4 * (h * R) := by
  intro h R; ring

/-- **Dilation + realification entropy factor (`×16`).**  Doubling `h` and `R`
twice — once for the Hermitian dilation, once for the realification `ι` — grows
the entropy by `16`:

  `(2 (2 h)) · (2 (2 R)) = 16 · (h R)`. -/
theorem ent_double_double :
    ∀ h R : ℝ, (2 * (2 * h)) * (2 * (2 * R)) = 16 * (h * R) := by
  intro h R; ring

/-- **Tensor-amplification entropy factor.**  If tensoring by `M_c` multiplies
both the maximal block size `h` and the reduced dimension `R` by `c`, then the
entropy product is multiplied by `c^2`.  This is the arithmetic behind the
`c^2` entropy factor in the completely bounded tensor amplification step. -/
theorem ent_tensor_amplification :
    ∀ c h R : ℝ, (c * h) * (c * R) = c ^ 2 * (h * R) := by
  intro c h R; ring

/-- The `×4` factor with natural-number block size and dimension (`h R : ℕ`),
so the identity reads directly off the integer counts. -/
theorem ent_double_nat : ∀ h R : ℕ, (2 * h) * (2 * R) = 4 * (h * R) := by
  intro h R; ring

/-- The `×16` factor with natural-number block size and dimension (`h R : ℕ`). -/
theorem ent_double_double_nat :
    ∀ h R : ℕ, (2 * (2 * h)) * (2 * (2 * R)) = 16 * (h * R) := by
  intro h R; ring

/-- Natural-number version of `ent_tensor_amplification`. -/
theorem ent_tensor_amplification_nat :
    ∀ c h R : ℕ, (c * h) * (c * R) = c ^ 2 * (h * R) := by
  intro c h R; ring

/-! ### 1a. Direct-sum entropy warning -/

/-- If the block heights are all bounded by `H`, and one positive-rank block has
height strictly below `H`, then the sum of individual entropies is strictly less
than the direct-sum entropy `H * sum R`.  This is the arithmetic reason the paper
uses `(max h_l) * sum R_l`, not generally `sum_l h_l R_l`, for direct sums. -/
theorem direct_sum_entropy_sum_lt
    {ι : Type*} (s : Finset ι) (h R : ι → Nat) (H : Nat)
    (hH : ∀ i, i ∈ s → h i ≤ H)
    {j : ι} (hj : j ∈ s) (hstrict : h j < H) (hRj : 0 < R j) :
    Finset.sum s (fun i => h i * R i) < H * Finset.sum s R := by
  calc
    Finset.sum s (fun i => h i * R i) < Finset.sum s (fun i => H * R i) := by
      apply Finset.sum_lt_sum
      · intro i hi
        exact Nat.mul_le_mul_right (R i) (hH i hi)
      · exact ⟨j, hj, Nat.mul_lt_mul_of_pos_right hstrict hRj⟩
    _ = H * Finset.sum s R := by
      exact (Finset.mul_sum s (fun i => R i) H).symm

/-- If the block heights are all bounded by `H`, then the sum of component
entropies is at most the direct-sum entropy `H * sum R`.  This is the
non-strict bookkeeping direction behind the paper's warning that the maximum
block height is a global prefactor for direct sums. -/
theorem direct_sum_entropy_sum_le
    {ι : Type*} (s : Finset ι) (h R : ι → Nat) (H : Nat)
    (hH : ∀ i, i ∈ s → h i ≤ H) :
    Finset.sum s (fun i => h i * R i) ≤ H * Finset.sum s R := by
  calc
    Finset.sum s (fun i => h i * R i) ≤ Finset.sum s (fun i => H * R i) := by
      apply Finset.sum_le_sum
      intro i hi
      exact Nat.mul_le_mul_right (R i) (hH i hi)
    _ = H * Finset.sum s R := by
      exact (Finset.mul_sum s (fun i => R i) H).symm

/-- Equality case for `direct_sum_entropy_sum_le`: if every block height in the
finite family is exactly `H`, then the component entropy sum is exactly the
direct-sum entropy `H * sum R`. -/
theorem direct_sum_entropy_sum_eq_of_height_eq
    {ι : Type*} (s : Finset ι) (h R : ι → Nat) (H : Nat)
    (hh : ∀ i, i ∈ s → h i = H) :
    Finset.sum s (fun i => h i * R i) = H * Finset.sum s R := by
  calc
    Finset.sum s (fun i => h i * R i) = Finset.sum s (fun i => H * R i) := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [hh i hi]
    _ = H * Finset.sum s R := by
      exact (Finset.mul_sum s (fun i => R i) H).symm

/-- Direct-sum entropy bounded by the actual finite maximum block height.  This
is the same non-strict bookkeeping as `direct_sum_entropy_sum_le`, specialized
to the canonical prefactor `s.sup h`. -/
theorem direct_sum_entropy_sum_le_sup
    {ι : Type*} (s : Finset ι) (h R : ι → Nat) :
    Finset.sum s (fun i => h i * R i) ≤ (s.sup h) * Finset.sum s R :=
  direct_sum_entropy_sum_le s h R (s.sup h) (fun _ hi => Finset.le_sup hi)

/-- Componentwise monotonicity of the finite entropy sum.  Enlarging every
block height and every reduced dimension can only increase
`sum_i h_i * R_i`.  This is the finite-sum bookkeeping used when a lift or
coarsening dominates the original block data term by term. -/
theorem direct_sum_entropy_sum_mono
    {ι : Type*} (s : Finset ι) (h₁ R₁ h₂ R₂ : ι → Nat)
    (hh : ∀ i, i ∈ s → h₁ i ≤ h₂ i)
    (hR : ∀ i, i ∈ s → R₁ i ≤ R₂ i) :
    Finset.sum s (fun i => h₁ i * R₁ i) ≤ Finset.sum s (fun i => h₂ i * R₂ i) := by
  apply Finset.sum_le_sum
  intro i hi
  exact Nat.mul_le_mul (hh i hi) (hR i hi)

/-- Monotonicity under adding blocks.  If `s ⊆ t`, then summing the same
nonnegative component entropies over `s` is at most summing them over `t`.  This
is the bookkeeping step for passing from a subfamily to a larger block family. -/
theorem direct_sum_entropy_sum_mono_subset
    {ι : Type*} {s t : Finset ι} (h R : ι → Nat) (hst : s ⊆ t) :
    Finset.sum s (fun i => h i * R i) ≤ Finset.sum t (fun i => h i * R i) := by
  exact Finset.sum_le_sum_of_subset_of_nonneg hst (by
    intro i _ _
    exact Nat.zero_le _)

/-- Zero-rank blocks contribute no component entropy.  This is the degenerate
case of the direct-sum bookkeeping in which every reduced dimension in the
indexed family vanishes. -/
theorem direct_sum_entropy_zero_ranks
    {ι : Type*} (s : Finset ι) (h R : ι → Nat)
    (hR : ∀ i, i ∈ s → R i = 0) :
    Finset.sum s (fun i => h i * R i) = 0 := by
  apply Finset.sum_eq_zero
  intro i hi
  simp [hR i hi]

/-- Component entropy sums split over disjoint unions of block families. -/
theorem direct_sum_entropy_sum_union_disjoint
    {ι : Type*} [DecidableEq ι] (s t : Finset ι) (h R : ι → Nat)
    (hst : Disjoint s t) :
    Finset.sum (s ∪ t) (fun i => h i * R i)
      = Finset.sum s (fun i => h i * R i) + Finset.sum t (fun i => h i * R i) := by
  exact Finset.sum_union hst

/-! ### 2. Log absorption

A constant `c ≥ 1` inside `log(e + c x)` costs only the constant factor
`1 + log c`.  The two ingredients are recorded first. -/

/-- `log(e + x) ≥ 1` for `x ≥ 0`: since `e + x ≥ e = exp 1`, monotonicity of
`log` and `log (exp 1) = 1` give the bound.  (This is the slack that makes the
constant `1 + log c` an honest upper bound on `1 + log c / log(e + x)`.) -/
theorem one_le_log_e_add (x : ℝ) (hx : 0 ≤ x) : 1 ≤ Real.log (Real.exp 1 + x) := by
  have he : Real.exp 1 ≤ Real.exp 1 + x := by linarith
  calc (1 : ℝ) = Real.log (Real.exp 1) := (Real.log_exp 1).symm
    _ ≤ Real.log (Real.exp 1 + x) :=
        Real.log_le_log (Real.exp_pos 1) he

/-- The basic step `e + c x ≤ c (e + x)` when `c ≥ 1`: the constant factor only
inflates the additive `e`, since `e ≤ c · e`. -/
theorem e_add_mul_le (x c : ℝ) (hc : 1 ≤ c) :
    Real.exp 1 + c * x ≤ c * (Real.exp 1 + x) := by
  have he : Real.exp 1 ≤ c * Real.exp 1 := by
    nlinarith [Real.exp_pos 1]
  nlinarith [Real.exp_pos 1]

/-- **Log-absorption inequality.**  For `x ≥ 0` and `c ≥ 1`,

  `log(e + c x) ≤ (1 + log c) · log(e + x)`.

A constant inside the logarithm is absorbed into the leading constant: replacing
the entropy argument `Ent/n` by `c · Ent/n` (for instance after dilation and
realification multiply `Ent` by `16`, so `c = 16`) changes the bound
`√(n log(e + Ent/n))` only through the factor `1 + log c`.

Proof: `log(e + c x) ≤ log(c (e + x)) = log c + log(e + x)` by `e_add_mul_le`
and `Real.log_mul`; then `log c + log(e + x) ≤ (1 + log c) log(e + x)` because
the gap `(1 + log c) log(e + x) - (log c + log(e + x)) = log c (log(e + x) - 1)`
is `≥ 0`, using `log c ≥ 0` and `log(e + x) ≥ 1`. -/
theorem log_absorb_const (x c : ℝ) (hx : 0 ≤ x) (hc : 1 ≤ c) :
    Real.log (Real.exp 1 + c * x) ≤ (1 + Real.log c) * Real.log (Real.exp 1 + x) := by
  have hcpos : (0 : ℝ) < c := lt_of_lt_of_le zero_lt_one hc
  have hepos : (0 : ℝ) < Real.exp 1 := Real.exp_pos 1
  have hxepos : (0 : ℝ) < Real.exp 1 + x := by linarith
  -- `log c ≥ 0` and `log(e+x) ≥ 1`.
  have hlogc : 0 ≤ Real.log c := Real.log_nonneg hc
  have hlogex : 1 ≤ Real.log (Real.exp 1 + x) := one_le_log_e_add x hx
  -- Step 1: `log(e + c x) ≤ log c + log(e + x)`.
  have step1 : Real.log (Real.exp 1 + c * x)
      ≤ Real.log c + Real.log (Real.exp 1 + x) := by
    have hmono : Real.log (Real.exp 1 + c * x)
        ≤ Real.log (c * (Real.exp 1 + x)) := by
      have hpos : (0 : ℝ) < Real.exp 1 + c * x := by positivity
      exact Real.log_le_log hpos (e_add_mul_le x c hc)
    have hsplit : Real.log (c * (Real.exp 1 + x))
        = Real.log c + Real.log (Real.exp 1 + x) :=
      Real.log_mul (ne_of_gt hcpos) (ne_of_gt hxepos)
    rw [hsplit] at hmono
    exact hmono
  -- Step 2: `log c + log(e + x) ≤ (1 + log c) log(e + x)`.
  -- difference `= log c · (log(e+x) - 1) ≥ 0`.
  have step2 : Real.log c + Real.log (Real.exp 1 + x)
      ≤ (1 + Real.log c) * Real.log (Real.exp 1 + x) := by
    nlinarith [mul_nonneg hlogc (by linarith : (0:ℝ) ≤ Real.log (Real.exp 1 + x) - 1)]
  exact le_trans step1 step2

/-! ### 3. Norming-set injection count

The lower-bound construction injects `(2w+1)^r` distinct multi-indices into a
norming set `Q`; the cardinality bound `(2w+1)^r ≤ |Q|` is then immediate. -/

/-- **Norming-set cardinality bound.**  If the `(2 w + 1)^r` multi-indices
`Fin ((2 * w + 1) ^ r)` inject into a norming set `Q : Finset ι`, then

  `(2 w + 1) ^ r ≤ Q.card`.

This is the `|Q| ≥ (2w+1)^r` step in the lower bound, via
`Fintype.card_le_of_injective` (`Fin n` has cardinality `n`, and the subtype
attached to a `Finset` has cardinality `Q.card`). -/
theorem norming_card_ge
    {ι : Type*} (w r : ℕ) (Q : Finset ι)
    (f : Fin ((2 * w + 1) ^ r) → Q) (hf : Function.Injective f) :
    (2 * w + 1) ^ r ≤ Q.card := by
  have h := Fintype.card_le_of_injective f hf
  -- `Fintype.card (Fin n) = n` and `Fintype.card Q = Q.card`.
  rwa [Fintype.card_fin, Fintype.card_coe] at h

end EntropyAbsorption
