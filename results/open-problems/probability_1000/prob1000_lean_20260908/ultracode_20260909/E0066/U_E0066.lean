import Mathlib

/-!
# Two small steps in the trajectory theorem for bistochastic operators (Rozikov Problem 13)

For a bistochastic operator `V` (`V x` majorised by `x`), the partial sums of the decreasing
rearrangement are nonincreasing along every trajectory, so the sorted vector converges to some
`y`; every omega-limit point is a coordinate permutation of `y`, so the omega-limit set has at
most `m!` points and the trajectory converges to a periodic orbit.  Certified here:

* `antitone_bddBelow_tendsto`: a nonincreasing real sequence bounded below converges
  (the step that makes the sorted vector converge);
* `card_perm_images_le`: the coordinate permutations of one vector in `ℝ^m` form a set of at
  most `m!` points (the bound on the omega-limit set);
* `two_x_one_minus_x_bistochastic`: the operator `V(x₁,x₂) = (2x₁x₂, x₁²+x₂²)` on the
  1-simplex is bistochastic, i.e. `|2x(1-x) - 1/2| ≤ |x - 1/2|` for `x ∈ [0,1]`
  (the genuinely quadratic example whose trajectories all converge to the barycenter).
-/

open Filter Topology

namespace BistochasticTrajectories

/-- A nonincreasing real sequence that is bounded below converges (to its infimum). -/
theorem antitone_bddBelow_tendsto (s : ℕ → ℝ) (hs : Antitone s) (hb : BddBelow (Set.range s)) :
    Tendsto s atTop (𝓝 (⨅ n, s n)) :=
  tendsto_atTop_ciInf hs hb

/-- The set of coordinate permutations of a vector `y : Fin m → ℝ` has at most `m!` elements. -/
theorem card_perm_images_le (m : ℕ) (y : Fin m → ℝ) :
    (Finset.univ.image (fun σ : Equiv.Perm (Fin m) => y ∘ σ)).card ≤ m.factorial := by
  calc (Finset.univ.image (fun σ : Equiv.Perm (Fin m) => y ∘ σ)).card
      ≤ (Finset.univ : Finset (Equiv.Perm (Fin m))).card := Finset.card_image_le
    _ = m.factorial := by simp [Finset.card_univ, Fintype.card_perm, Fintype.card_fin]

/-- `V(x, 1-x) = (2x(1-x), x²+(1-x)²)` is bistochastic on the 1-simplex: the larger coordinate
of `V x` is at most the larger coordinate of `x`, i.e. `|2x(1-x) - 1/2| ≤ |x - 1/2|`. -/
theorem two_x_one_minus_x_bistochastic (x : ℝ) (h0 : 0 ≤ x) (h1 : x ≤ 1) :
    |2 * x * (1 - x) - 1 / 2| ≤ |x - 1 / 2| := by
  have hid : 2 * x * (1 - x) - 1 / 2 = -(2 * (x - 1 / 2) ^ 2) := by ring
  have hsq : |x - 1 / 2| ≤ 1 / 2 := by
    rw [abs_le]; constructor <;> linarith
  rw [hid, abs_neg, abs_of_nonneg (by positivity)]
  have hx : (x - 1 / 2) ^ 2 = |x - 1 / 2| ^ 2 := (sq_abs _).symm
  rw [hx]
  nlinarith [abs_nonneg (x - 1 / 2)]

end BistochasticTrajectories

#print axioms BistochasticTrajectories.antitone_bddBelow_tendsto
#print axioms BistochasticTrajectories.card_perm_images_le
#print axioms BistochasticTrajectories.two_x_one_minus_x_bistochastic
