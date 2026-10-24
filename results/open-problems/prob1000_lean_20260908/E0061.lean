import Mathlib

/-!
# The product step in the Volterra ergodic-theorem proof (Rozikov Problem 4)

If `w (n+1) = w n * (1 + f n)` with `f n ≥ 0`, `w 0 > 0` and `w n ≤ 1` for all `n`, then the
partial sums of `f` are bounded by `(1 - w 0)/w 0`, hence `f` is summable and tends to `0`.
This is the step that sends the two dominated species to zero once the top species' coordinate
is known to be nondecreasing and bounded.
-/

open Finset BigOperators

namespace VolterraErgodic

/-- `∏_{k<n} (1 + f k) ≥ 1 + ∑_{k<n} f k` for nonnegative `f`. -/
theorem prod_one_add_ge (f : ℕ → ℝ) (hf : ∀ k, 0 ≤ f k) (n : ℕ) :
    1 + ∑ k ∈ range n, f k ≤ ∏ k ∈ range n, (1 + f k) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [prod_range_succ, sum_range_succ]
    have h1 : 0 ≤ ∑ k ∈ range n, f k := sum_nonneg fun k _ => hf k
    have h2 : 1 + ∑ k ∈ range n, f k ≤ ∏ k ∈ range n, (1 + f k) := ih
    nlinarith [hf n, h1, h2]

/-- The partial sums of `f` are bounded when the product stays at most `1 / w 0`. -/
theorem sum_le_of_prod (w f : ℕ → ℝ) (hw0 : 0 < w 0) (hle : ∀ n, w n ≤ 1)
    (hf : ∀ k, 0 ≤ f k) (hrec : ∀ n, w (n + 1) = w n * (1 + f n)) (n : ℕ) :
    ∑ k ∈ range n, f k ≤ (1 - w 0) / w 0 := by
  have hprod : ∀ n, w n = w 0 * ∏ k ∈ range n, (1 + f k) := by
    intro n
    induction n with
    | zero => simp
    | succ n ih => rw [hrec, ih, prod_range_succ, mul_assoc]
  have h := prod_one_add_ge f hf n
  have hn := hle n
  rw [hprod n] at hn
  -- w 0 * (1 + S) ≤ w 0 * prod ≤ 1
  have : w 0 * (1 + ∑ k ∈ range n, f k) ≤ 1 := by
    calc w 0 * (1 + ∑ k ∈ range n, f k) ≤ w 0 * ∏ k ∈ range n, (1 + f k) :=
          mul_le_mul_of_nonneg_left h hw0.le
      _ ≤ 1 := hn
  rw [le_div_iff₀ hw0]
  nlinarith [this]

/-- Hence `f` is summable, and so tends to zero. -/
theorem summable_of_prod (w f : ℕ → ℝ) (hw0 : 0 < w 0) (hle : ∀ n, w n ≤ 1)
    (hf : ∀ k, 0 ≤ f k) (hrec : ∀ n, w (n + 1) = w n * (1 + f n)) :
    Summable f := by
  exact summable_of_sum_range_le (c := (1 - w 0) / w 0) hf
    (fun n => sum_le_of_prod w f hw0 hle hf hrec n)

theorem tendsto_zero_of_prod (w f : ℕ → ℝ) (hw0 : 0 < w 0) (hle : ∀ n, w n ≤ 1)
    (hf : ∀ k, 0 ≤ f k) (hrec : ∀ n, w (n + 1) = w n * (1 + f n)) :
    Filter.Tendsto f Filter.atTop (nhds 0) :=
  (summable_of_prod w f hw0 hle hf hrec).tendsto_atTop_zero

end VolterraErgodic

#print axioms VolterraErgodic.summable_of_prod
#print axioms VolterraErgodic.tendsto_zero_of_prod
