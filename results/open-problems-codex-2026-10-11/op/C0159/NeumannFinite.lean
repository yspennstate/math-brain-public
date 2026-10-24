import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Data.Real.Basic

open scoped BigOperators

-- The finite Neumann identity works even in a noncommutative ring.
theorem finite_neumann_remainder {R : Type*} [Ring R] (z : R) (n : ℕ) :
    (1 - z) * (∑ i ∈ Finset.range n, z ^ i) = 1 - z ^ n := by
  exact mul_neg_geom_sum z n

-- The scalar upper bound used to dominate all finite operator truncations.
theorem finite_neumann_bound (z : ℝ) (n : ℕ)
    (hz0 : 0 ≤ z) (hz1 : z < 1) :
    (∑ i ∈ Finset.range n, z ^ i) ≤ 1 / (1 - z) := by
  apply (le_div_iff₀ (sub_pos.mpr hz1)).2
  rw [geom_sum_mul_neg]
  exact sub_le_self 1 (pow_nonneg hz0 n)
