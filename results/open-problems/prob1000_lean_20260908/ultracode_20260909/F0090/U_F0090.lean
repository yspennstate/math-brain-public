import Mathlib

/-!
# Kalai, Three puzzles (ICM 2018), Conjecture 8: entropy of the spectral and pivotal
samples of the percolation crossing event is O(I(f)).

The proof in the memo bounds the entropy of a random subset S of the R x R box by a dyadic
tree encoding, `H(S) <= log 2 + log 15 * sum_k sum_B P(S meets B)`, then bounds each box
marginal by the four-arm probability. Three elementary steps are certified here.

1. `card_nonempty_subsets_fin4`: a dyadic box has 4 children, so an occupied box has at most
   15 nonempty child patterns (the `log 15` in the tree bound).
2. `scale_term_bound`: at scale r, quasi-multiplicativity `a4(r) a4(r,R) <= C a4(R)` together
   with the lower bound `g <= r^2 a4(r)` (from the four-arm exponent being < 2, GPS (2.6)) gives
   `(R/r)^2 a4(r,R) <= C R^2 a4(R) / g`.
3. `geom_tail`: with `g = c r^eps`, `r = R 2^{-k}`, the terms are geometric in k, and the
   partial sums are bounded by `1/(1-q)`.
-/

open Finset

namespace KalaiConj8

/-- An occupied dyadic box with four children has 15 possible nonempty child patterns. -/
theorem card_nonempty_subsets_fin4 :
    ((Finset.univ : Finset (Finset (Fin 4))).filter Finset.Nonempty).card = 15 := by
  decide

/-- One scale of the box sum: `(R/r)^2 a4(r,R) <= C R^2 a4(R) / g` from
quasi-multiplicativity and the lower bound `g <= r^2 a4(r)`. -/
theorem scale_term_bound (R r a4r a4rR a4R C g : ℝ)
    (hr : 0 < r) (hg : 0 < g) (ha4rR : 0 ≤ a4rR)
    (hqm : a4r * a4rR ≤ C * a4R) (hlow : g ≤ r ^ 2 * a4r) :
    (R / r) ^ 2 * a4rR ≤ C * R ^ 2 * a4R / g := by
  have hnn : 0 ≤ (R / r) ^ 2 * a4rR := mul_nonneg (sq_nonneg _) ha4rR
  have h1 : (R / r) ^ 2 * a4rR * g ≤ R ^ 2 * (C * a4R) := by
    calc (R / r) ^ 2 * a4rR * g ≤ (R / r) ^ 2 * a4rR * (r ^ 2 * a4r) := by
          exact mul_le_mul_of_nonneg_left hlow hnn
      _ = R ^ 2 * (a4r * a4rR) := by
          rw [div_pow]; field_simp
      _ ≤ R ^ 2 * (C * a4R) := by
          exact mul_le_mul_of_nonneg_left hqm (sq_nonneg _)
  rw [le_div_iff₀ hg]
  linarith [h1]

/-- Partial sums of a geometric series with ratio in `[0,1)` are bounded by `1/(1-q)`. -/
theorem geom_tail (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q < 1) (K : ℕ) :
    ∑ k ∈ range K, q ^ k ≤ 1 / (1 - q) := by
  rw [Finset.range_eq_Ico]
  have h := geom_sum_Ico_le_of_lt_one hq0 hq1 (m := 0) (n := K)
  simpa using h

end KalaiConj8

#print axioms KalaiConj8.card_nonempty_subsets_fin4
#print axioms KalaiConj8.scale_term_bound
#print axioms KalaiConj8.geom_tail
