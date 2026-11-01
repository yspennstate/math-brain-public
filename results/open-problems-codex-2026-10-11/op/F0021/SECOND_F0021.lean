import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- The ASCII spelling avoids shell encoding damage to mathematical symbols.
-- Merging two increments cannot increase travel entropy.
theorem merge_entropy (x y s t : Real) (hs : 0 < s) (ht : 0 < t) :
    LE.le ((x + y)^2 / (s + t)) (x^2 / s + y^2 / t) := by
  have hst : 0 < s + t := add_pos hs ht
  have hiden : (x^2 / s + y^2 / t) * (s + t) - (x + y)^2 =
      (t * x - s * y)^2 / (s * t) := by
    field_simp [ne_of_gt hs, ne_of_gt ht]
    ring
  have hnon : LE.le 0 ((x^2 / s + y^2 / t) * (s + t) - (x + y)^2) := by
    rw [hiden]
    exact div_nonneg (sq_nonneg _) (le_of_lt (mul_pos hs ht))
  apply (div_le_iff₀ hst).2
  linarith

theorem sparse_exponents (q k : Real) (hk : k < (1 : Real) / 3)
    (hprod : (5 : Real) / 3 < q * k) :
    And ((5 : Real) / 3 - q * k < 0)
      (And ((2 : Real) / 3 - k * (q - 1) < 0) (1 - k * (q - 2) < 0)) := by
  constructor
  · linarith
  constructor <;> nlinarith

theorem layer_allocation (energy beta B D E : Real)
    (hbeta : LE.le 0 beta) (hD : 0 < D) (hDB : LE.le (16 * beta) D)
    (hB : LE.le 0 B) (hE : B / 2 < E) (henergy : LE.le energy (4 * B / D)) :
    beta * energy < E / 2 := by
  have hm : LE.le (beta * energy) (beta * (4 * B / D)) :=
    mul_le_mul_of_nonneg_left henergy hbeta
  have hp : LE.le (16 * beta * B) (D * B) :=
    mul_le_mul_of_nonneg_right hDB hB
  have hb : LE.le ((4 * beta * B) / D) (B / 4) := by
    apply (div_le_iff₀ hD).2
    nlinarith [hp]
  have heq : beta * (4 * B / D) = (4 * beta * B) / D := by ring
  rw [heq] at hm
  linarith
