import Mathlib

/-!
# E0062 (Rozikov, Problem 5): the product step behind the transitive-tournament theorem

For a Volterra operator whose sign tournament is transitive, the top species `w` satisfies
`w (n+1) = w n * (1 + f n)` with `f n = ∑_j p_j u_j n ≥ 0`, where the `u_j` are the other
coordinates and `p_j > 0`. The lemma: if `w 0 > 0` and `w n ≤ 1` then `f` is summable,
hence every `u_j` (being `0 ≤ u_j ≤ f / p_j`) is summable and tends to `0`, so the orbit
converges to the vertex of `w`. Nothing here depends on the dimension `m`.
-/

open Finset BigOperators

namespace VolterraTransitive

theorem prod_one_add_ge (f : ℕ → ℝ) (hf : ∀ k, 0 ≤ f k) (n : ℕ) :
    1 + ∑ k ∈ range n, f k ≤ ∏ k ∈ range n, (1 + f k) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [prod_range_succ, sum_range_succ]
    have h1 : 0 ≤ ∑ k ∈ range n, f k := sum_nonneg fun k _ => hf k
    nlinarith [hf n, h1, ih]

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
  have : w 0 * (1 + ∑ k ∈ range n, f k) ≤ 1 := by
    calc w 0 * (1 + ∑ k ∈ range n, f k) ≤ w 0 * ∏ k ∈ range n, (1 + f k) :=
          mul_le_mul_of_nonneg_left h hw0.le
      _ ≤ 1 := hn
  rw [le_div_iff₀ hw0]
  nlinarith [this]

theorem summable_of_prod (w f : ℕ → ℝ) (hw0 : 0 < w 0) (hle : ∀ n, w n ≤ 1)
    (hf : ∀ k, 0 ≤ f k) (hrec : ∀ n, w (n + 1) = w n * (1 + f n)) :
    Summable f :=
  summable_of_sum_range_le (c := (1 - w 0) / w 0) hf
    (fun n => sum_le_of_prod w f hw0 hle hf hrec n)

/-- A dominated species: `0 ≤ u ≤ f / p` with `p > 0` forces `u` summable, hence `u → 0`. -/
theorem dominated_tendsto_zero (w f u : ℕ → ℝ) (p : ℝ) (hp : 0 < p)
    (hw0 : 0 < w 0) (hle : ∀ n, w n ≤ 1) (hf : ∀ k, 0 ≤ f k)
    (hrec : ∀ n, w (n + 1) = w n * (1 + f n))
    (hu0 : ∀ n, 0 ≤ u n) (hu : ∀ n, p * u n ≤ f n) :
    Filter.Tendsto u Filter.atTop (nhds 0) := by
  have hs : Summable f := summable_of_prod w f hw0 hle hf hrec
  have hs' : Summable (fun n => f n / p) := hs.div_const p
  have : Summable u := by
    refine Summable.of_nonneg_of_le hu0 (fun n => ?_) hs'
    rw [le_div_iff₀ hp]
    linarith [hu n]
  exact this.tendsto_atTop_zero

end VolterraTransitive

#print axioms VolterraTransitive.summable_of_prod
#print axioms VolterraTransitive.dominated_tendsto_zero
