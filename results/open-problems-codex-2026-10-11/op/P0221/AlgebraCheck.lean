import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

open scoped BigOperators

-- Each accepted-surplus square is bounded by f times the surplus.
theorem surplus_square_bound (f c w : ℝ)
    (hc : 0 ≤ c) (hcf : c ≤ f) (hw : 0 ≤ w) :
    w * (f-c)^2 ≤ f * (w * (f-c)) := by
  have h := mul_nonneg hw (mul_nonneg hc (sub_nonneg.mpr hcf))
  nlinarith

-- At an admissible root, the slope sum is at least two.
theorem admissible_slope {ι : Type*} (s : Finset ι) (w c : ι → ℝ)
    (f : ℝ) (hf : 0 < f)
    (hw : ∀ i ∈ s, 0 ≤ w i) (hc : ∀ i ∈ s, 0 ≤ c i)
    (hcf : ∀ i ∈ s, c i ≤ f)
    (heq : ∑ i ∈ s, w i * (f-c i)^2 = 2*f) :
    2 ≤ ∑ i ∈ s, w i * (f-c i) := by
  have h : (∑ i ∈ s, w i * (f-c i)^2) ≤
      ∑ i ∈ s, f * (w i * (f-c i)) := by
    apply Finset.sum_le_sum
    intro i hi
    exact surplus_square_bound f (c i) (w i) (hc i hi) (hcf i hi) (hw i hi)
  rw [← Finset.mul_sum] at h
  rw [heq] at h
  nlinarith

-- Two roots whose slope sums are admissible must coincide.
theorem quadratic_admissible_unique (A B C f g : ℝ)
    (hf : A*f^2-2*B*f+C = 2*f)
    (hg : A*g^2-2*B*g+C = 2*g)
    (hsf : 2 ≤ A*f-B) (hsg : 2 ≤ A*g-B) : f = g := by
  have he : (f-g)*(A*f+A*g-2*B-2) = 0 := by
    calc
      _ = (A*f^2-2*B*f+C-2*f) - (A*g^2-2*B*g+C-2*g) := by ring
      _ = 0 := by linarith
  rcases mul_eq_zero.mp he with h | h
  · exact sub_eq_zero.mp h
  · exfalso
    linarith

-- Core two-component inequality for the 8/3 supersolution.
theorem pair_potential_bound (q : ℝ) (hq : 4 ≤ q) :
    3/4*(q-1) ≤ q-2+1/q := by
  have hq0 : 0 < q := by linarith
  have hp : 0 ≤ (q-1)*(q-4) :=
    mul_nonneg (by linarith) (by linarith)
  -- Rewrite the target as an inequality after multiplication by q.
  have he : q-2+1/q = (q*(q-2)+1)/q := by
    field_simp [ne_of_gt hq0]
    <;> ring
  rw [he]
  apply (le_div_iff₀ hq0).mpr
  nlinarith

theorem many_component_bound (k q T : ℝ)
    (hk : 3 ≤ k) (hq : k^2 ≤ q) (hT : 0 ≤ T) :
    3/4*(q-1) ≤ q-k+T := by
  have hp : 0 ≤ (k-1)*(k-3) :=
    mul_nonneg (by linarith) (by linarith)
  nlinarith

-- Exact scalar integration result for n=3 in random order.
example : (5/8:ℚ)^2/2 + (3/8)*(5/8) + (1-5/8) = 103/128 := by
  norm_num
