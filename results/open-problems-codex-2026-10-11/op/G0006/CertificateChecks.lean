import Mathlib.Data.Rat.Lemmas
import Mathlib.Tactic.Linarith

-- Algebra used in the local-exit-certificate obstruction.
theorem degree_square_bound (k : ℤ) (hk : 4 ≤ k) :
    k + 1 ≤ (k - 1)^2 := by
  nlinarith [sq_nonneg (k - 3)]

theorem cubic_exponent_gap (r : ℤ) (hr : 1 ≤ r) :
    2 * (r + 1) < (2 * r + 1)^2 := by
  nlinarith [sq_nonneg r]

-- Exact low-density percolating row-plus-noise example.
def rowP : ℚ := 1 / 100
def noiseP : ℚ := 1 / 10
def density : ℚ := rowP + (1 - rowP) * noiseP
def horizontalPair : ℚ := rowP + (1 - rowP) * noiseP^2
def conditionalDegree : ℚ := 2 * horizontalPair / density + 2 * density

theorem exact_density : density = 109 / 1000 := by decide +kernel
theorem density_small : 0 < density ∧ density < 1 / 8 := by decide +kernel
theorem exact_horizontal_pair : horizontalPair = 199 / 10000 := by decide +kernel
theorem degree_below_two : conditionalDegree < 2 := by decide +kernel
