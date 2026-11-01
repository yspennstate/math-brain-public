import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith

open scoped BigOperators

-- The finite collision bound used in the sampled-distance argument.
theorem collision_bound {ι : Type*} (S : Finset ι) (s : ι → ℝ) (K : ℝ)
    (hnonneg : ∀ i ∈ S, 0 ≤ s i) (hbound : ∀ i ∈ S, s i ≤ K) :
    (∑ i ∈ S, s i ^ 2) ≤ K * (∑ i ∈ S, s i) := by
  calc
    (∑ i ∈ S, s i ^ 2) ≤ ∑ i ∈ S, K * s i := by
      apply Finset.sum_le_sum
      intro i hi
      have hp : 0 ≤ (K - s i) * s i :=
        mul_nonneg (sub_nonneg.mpr (hbound i hi)) (hnonneg i hi)
      nlinarith
    _ = K * (∑ i ∈ S, s i) := by rw [Finset.mul_sum]

-- A ball of radius r cannot cover two points at distance strictly above 2r.
theorem separated_ball (d a b r : ℝ) (htriangle : d ≤ a + b)
    (ha : a ≤ r) (hb : b ≤ r) (hsep : 2 * r < d) : False := by
  linarith
