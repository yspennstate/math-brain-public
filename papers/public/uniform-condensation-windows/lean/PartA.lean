/-
Machine-checked algebraic steps from
"Uniform condensation windows for zero-radius random allocations".
Part A: the finite inequalities used in Sections 3, 5 and 7.
-/
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Analysis.SpecialFunctions.Log.Base

open Finset

namespace Condensation

/-- Section 3, proof of the insertion lemma: the falling factorial `(n-t)_Q`
is at least `(n/2)^Q` once `t + Q ≤ n/2`. -/
theorem falling_ge_half_pow (n t Q : ℕ) (h : 2 * (t + Q) ≤ n) :
    ((n : ℝ) / 2) ^ Q ≤ ∏ i ∈ range Q, ((n : ℝ) - t - i) := by
  have key : (∏ _i ∈ range Q, ((n : ℝ) / 2)) ≤ ∏ i ∈ range Q, ((n : ℝ) - t - i) := by
    refine prod_le_prod (fun i _ => by positivity) ?_
    intro i hi
    have hiQ : (i : ℝ) + 1 ≤ (Q : ℝ) := by exact_mod_cast mem_range.mp hi
    have h2 : 2 * ((t : ℝ) + Q) ≤ (n : ℝ) := by exact_mod_cast h
    linarith
  have hc : (∏ _i ∈ range Q, ((n : ℝ) / 2)) = ((n : ℝ) / 2) ^ Q := by
    rw [prod_const, card_range]
  rwa [hc] at key

/-- Section 3, last display of the insertion proof: the exponent bookkeeping that
turns `(n/2)^{1+R+C}` divided by `R` factors `m/K` and `C` factors `n`
into `(n / 2^{C+1}) (nK/2m)^R`. -/
theorem insertion_exponent (n m K : ℝ) (R C : ℕ) (hn : 0 < n) (hm : 0 < m) (hK : 0 < K) :
    (n / 2) ^ (1 + R + C) / ((m / K) ^ R * n ^ C)
      = n / 2 ^ (C + 1) * (n * K / (2 * m)) ^ R := by
  have hn' : n ≠ 0 := ne_of_gt hn
  have hm' : m ≠ 0 := ne_of_gt hm
  have hK' : K ≠ 0 := ne_of_gt hK
  simp only [div_pow, mul_pow]
  field_simp
  ring

/-- Section 7: the record definition forces `q_j = w_j e^{-hj} ≤ j^{-b}`
for every supported `j ≤ u`. -/
theorem q_le_rpow (w h b : ℝ) (j : ℕ) (hj : 1 ≤ j) (hw : 0 < w)
    (hrec : (Real.log w + b * Real.log j) / j ≤ h) :
    w * Real.exp (-(h * j)) ≤ (j : ℝ) ^ (-b) := by
  have hj0 : (0 : ℝ) < j := by exact_mod_cast hj
  have hstep : Real.log w + b * Real.log j ≤ h * j := by
    rw [div_le_iff₀ hj0] at hrec; linarith
  have : Real.log w - h * j ≤ -(b * Real.log j) := by linarith
  calc w * Real.exp (-(h * j)) = Real.exp (Real.log w - h * j) := by
        rw [Real.exp_sub, Real.exp_log hw, Real.exp_neg]; ring
    _ ≤ Real.exp (-(b * Real.log j)) := Real.exp_le_exp.mpr this
    _ = (j : ℝ) ^ (-b) := by
        rw [Real.rpow_def_of_pos hj0]; ring_nf

/-- Section 7, the Markov step: the finite condition on the auxiliary mean
makes the expected background mass at most half the pigeonhole threshold,
uniformly over the window. -/
theorem markov_threshold (α δ k n μ : ℝ) (hα : 0 < α) (hδ : 0 < δ) (hk : 0 < k)
    (hn : 0 ≤ n) (hnle : n ≤ (1 + 5 * δ) * k / α) (hμ0 : 0 ≤ μ)
    (hμ : μ ≤ α * δ / (2 * (1 + 5 * δ))) :
    n * μ ≤ δ * k / 2 := by
  have h5 : (0 : ℝ) < 1 + 5 * δ := by linarith
  calc n * μ ≤ ((1 + 5 * δ) * k / α) * (α * δ / (2 * (1 + 5 * δ))) := by
        apply mul_le_mul hnle hμ hμ0
        positivity
    _ = δ * k / 2 := by field_simp

/-- Section 5, the greedy construction: the residual left by a stage at
geometric index `i` has a strictly smaller geometric index. -/
theorem greedy_index_decrease (a x : ℝ) (i : ℕ) (ha : 1 < a) (hx : 0 < x)
    (hlt : x < 2 * a ^ i) : Real.logb a (x / 2) < i := by
  have ha0 : (0 : ℝ) < a := by linarith
  have h1 : x / 2 < a ^ i := by linarith
  have h2 : Real.logb a (x / 2) < Real.logb a (a ^ i) :=
    Real.logb_lt_logb ha (by positivity) h1
  rw [Real.logb_pow, Real.logb_self_eq_one ha, mul_one] at h2
  exact h2

theorem greedy_floor_decrease (a x : ℝ) (i : ℕ) (ha : 1 < a) (hx : 0 < x)
    (hlt : x < 2 * a ^ i) : ⌊Real.logb a (x / 2)⌋ < (i : ℤ) := by
  have := greedy_index_decrease a x i ha hx hlt
  exact_mod_cast Int.floor_lt.mpr (by exact_mod_cast this)

end Condensation

#print axioms Condensation.falling_ge_half_pow
#print axioms Condensation.insertion_exponent
#print axioms Condensation.q_le_rpow
#print axioms Condensation.markov_threshold
#print axioms Condensation.greedy_index_decrease
#print axioms Condensation.greedy_floor_decrease
