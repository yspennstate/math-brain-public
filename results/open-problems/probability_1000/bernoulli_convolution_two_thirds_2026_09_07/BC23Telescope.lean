import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# The variance-estimate route: the boxed estimate implies summability

Referee route (7 September 2026): if the conditional-variance defect satisfies
  j_n - j_{n+1} ≥ (K/2) j_n^(1+θ)    (K > 0, 0 < θ < 1)
for a nonnegative decreasing sequence j, then ∑ j_n ≤ 2 j_0^(1-θ) / (K (1-θ)) < ∞.

This file checks that implication. The estimate itself (that the actual fibre
information of the two-thirds Bernoulli measure obeys such a decrement) is the
open mathematical target and is NOT proved here.
-/

open Real

namespace BC23

/-- Concavity of t ↦ t^(1-θ) on [0,∞) in tangent form: for 0 ≤ x ≤ y,
    (1-θ) y^(-θ) (y - x) ≤ y^(1-θ) - x^(1-θ). -/
lemma concave_step {θ x y : ℝ} (hθ0 : 0 < θ) (hθ1 : θ < 1) (hx : 0 ≤ x) (hxy : x ≤ y) :
    (1 - θ) * y ^ (-θ) * (y - x) ≤ y ^ (1 - θ) - x ^ (1 - θ) := by
  rcases eq_or_lt_of_le (hx.trans hxy) with hy0 | hy
  · -- y = 0 forces x = 0
    have hx0 : x = 0 := le_antisymm (hxy.trans hy0.symm.le) hx
    subst hy0; subst hx0
    simp [Real.zero_rpow (by linarith : (-θ) ≠ 0), Real.zero_rpow (by linarith : (1 - θ) ≠ 0)]
  · -- Bernoulli with exponent p = 1-θ ∈ (0,1): (1+s)^p ≤ 1 + p s, s = x/y - 1 ≥ -1
    have hp0 : 0 ≤ 1 - θ := by linarith
    have hp1 : 1 - θ ≤ 1 := by linarith
    have hs : -1 ≤ x / y - 1 := by
      have : 0 ≤ x / y := div_nonneg hx hy.le
      linarith
    have hb := rpow_one_add_le_one_add_mul_self hs hp0 hp1
    -- (x/y)^(1-θ) ≤ 1 + (1-θ)(x/y - 1)
    have hxy' : (1 + (x / y - 1)) = x / y := by ring
    rw [hxy'] at hb
    have hdiv : (x / y) ^ (1 - θ) = x ^ (1 - θ) / y ^ (1 - θ) := Real.div_rpow hx hy.le _
    rw [hdiv] at hb
    have hypos : 0 < y ^ (1 - θ) := Real.rpow_pos_of_pos hy _
    have hb' : x ^ (1 - θ) ≤ y ^ (1 - θ) * (1 + (1 - θ) * (x / y - 1)) := by
      rw [div_le_iff₀ hypos] at hb; linarith
    -- y^(1-θ) (1 + (1-θ)(x/y - 1)) = y^(1-θ) - (1-θ) y^(-θ) (y - x)
    have hkey : y ^ (1 - θ) * (1 + (1 - θ) * (x / y - 1)) = y ^ (1 - θ) - (1 - θ) * y ^ (-θ) * (y - x) := by
      have h1 : y ^ (1 - θ) = y * y ^ (-θ) := by
        rw [show (1 - θ) = 1 + (-θ) by ring, Real.rpow_add hy, Real.rpow_one]
      rw [h1]
      field_simp
      ring
    linarith [hb', hkey]

/-- If a nonnegative decreasing sequence obeys j_n - j_{n+1} ≥ (K/2) j_n^(1+θ), its partial sums are
    bounded by 2 j_0^(1-θ) / (K (1-θ)); hence it is summable with that bound on its sum. -/
theorem summable_of_variance_decrement (j : ℕ → ℝ) (K θ : ℝ) (hK : 0 < K) (hθ0 : 0 < θ) (hθ1 : θ < 1)
    (hnn : ∀ n, 0 ≤ j n) (hdec : ∀ n, j (n + 1) ≤ j n)
    (hstep : ∀ n, (K / 2) * (j n) ^ (1 + θ) ≤ j n - j (n + 1)) :
    Summable j ∧ ∑' n, j n ≤ 2 * (j 0) ^ (1 - θ) / (K * (1 - θ)) := by
  have hθ' : 0 < 1 - θ := by linarith
  -- one step: j n ≤ (2/(K(1-θ))) (j n^(1-θ) - j (n+1)^(1-θ))
  have step : ∀ n, j n ≤ (2 / (K * (1 - θ))) * ((j n) ^ (1 - θ) - (j (n + 1)) ^ (1 - θ)) := by
    intro n
    rcases eq_or_lt_of_le (hnn n) with h0 | hpos
    · -- j n = 0: right side is ≥ 0 since j (n+1) = 0 too
      have h1 : j (n + 1) = 0 := le_antisymm (by linarith [hdec n]) (hnn (n + 1))
      rw [← h0, h1]; simp
    · have hc := concave_step hθ0 hθ1 (hnn (n + 1)) (hdec n)
      -- (K/2) j^(1+θ) ≤ d, so j = (K/2)^{-1} (K/2) j^(1+θ) j^(-θ) ≤ (2/K) d j^(-θ)
      have hs := hstep n
      have hjt : (j n) ^ (1 + θ) * (j n) ^ (-θ) = j n := by
        rw [← Real.rpow_add hpos]; norm_num
      have hneg : 0 < (j n) ^ (-θ) := Real.rpow_pos_of_pos hpos _
      have h2 : (K / 2) * j n ≤ (j n - j (n + 1)) * (j n) ^ (-θ) := by
        calc (K / 2) * j n = (K / 2) * ((j n) ^ (1 + θ) * (j n) ^ (-θ)) := by rw [hjt]
          _ = ((K / 2) * (j n) ^ (1 + θ)) * (j n) ^ (-θ) := by ring
          _ ≤ (j n - j (n + 1)) * (j n) ^ (-θ) := by gcongr
      -- and (1-θ) j^(-θ) d ≤ j^(1-θ) - j(n+1)^(1-θ)
      have h3 : (1 - θ) * ((j n - j (n + 1)) * (j n) ^ (-θ)) ≤ (j n) ^ (1 - θ) - (j (n + 1)) ^ (1 - θ) := by
        have := hc; nlinarith [this]
      have hKθ : 0 < K * (1 - θ) := by positivity
      have h4 : (1 - θ) * (K / 2) * j n ≤ (j n) ^ (1 - θ) - (j (n + 1)) ^ (1 - θ) := by
        nlinarith [h2, h3, hθ']
      have hid : j n = (2 / (K * (1 - θ))) * ((1 - θ) * (K / 2) * j n) := by
        field_simp
      calc j n = (2 / (K * (1 - θ))) * ((1 - θ) * (K / 2) * j n) := hid
        _ ≤ (2 / (K * (1 - θ))) * ((j n) ^ (1 - θ) - (j (n + 1)) ^ (1 - θ)) := by gcongr
  -- partial sums telescope
  have hpartial : ∀ N, ∑ n ∈ Finset.range N, j n ≤ 2 * (j 0) ^ (1 - θ) / (K * (1 - θ)) := by
    intro N
    have htel : ∑ n ∈ Finset.range N, ((j n) ^ (1 - θ) - (j (n + 1)) ^ (1 - θ))
        = (j 0) ^ (1 - θ) - (j N) ^ (1 - θ) := by
      rw [Finset.sum_range_sub' (fun n => (j n) ^ (1 - θ))]
    have hN : 0 ≤ (j N) ^ (1 - θ) := Real.rpow_nonneg (hnn N) _
    calc ∑ n ∈ Finset.range N, j n
        ≤ ∑ n ∈ Finset.range N, (2 / (K * (1 - θ))) * ((j n) ^ (1 - θ) - (j (n + 1)) ^ (1 - θ)) :=
          Finset.sum_le_sum (fun n _ => step n)
      _ = (2 / (K * (1 - θ))) * ((j 0) ^ (1 - θ) - (j N) ^ (1 - θ)) := by
          rw [← Finset.mul_sum, htel]
      _ ≤ (2 / (K * (1 - θ))) * (j 0) ^ (1 - θ) := by
          gcongr; linarith
      _ = 2 * (j 0) ^ (1 - θ) / (K * (1 - θ)) := by ring
  have hsum : Summable j := summable_of_sum_range_le hnn hpartial
  exact ⟨hsum, tsum_le_of_sum_range_le hnn hpartial⟩

end BC23

#print axioms BC23.summable_of_variance_decrement
