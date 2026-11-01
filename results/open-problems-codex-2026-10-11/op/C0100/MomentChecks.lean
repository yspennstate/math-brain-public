import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring

namespace C0100
-- Exact inversion of the four-height factorial moments.
theorem moment_inverse (p0 p1 p2 p3 : ℚ) :
    let m0 := p0 + p1 + p2 + p3
    let m1 := p1 + 2*p2 + 3*p3
    let m2 := p2 + 3*p3
    let m3 := p3
    (p0 = m0 - m1 + m2 - m3) ∧
    (p1 = m1 - 2*m2 + 3*m3) ∧
    (p2 = m2 - 3*m3) ∧
    (p3 = m3) := by
  dsimp
  constructor
  · ring
  constructor
  · ring
  constructor
  · ring
  · rfl

-- Height probabilities have two free coordinates after fixing mass and mean.
theorem mean_preserving_direction (a b c d t : ℚ) :
    (a+t) + (b-2*t) + (c+t) + d = a+b+c+d ∧
    (b-2*t) + 2*(c+t) + 3*d = b+2*c+3*d := by
  constructor <;> ring
-- Exhaustive four-height factorial-moment table, evaluated by the kernel.
theorem binomial_table : ∀ h : Fin 4,
    (((h.val : ℚ) * ((h.val : ℚ) - 1) / 2) =
      (if h.val = 2 then 1 else if h.val = 3 then 3 else 0)) ∧
    (((h.val : ℚ) * ((h.val : ℚ) - 1) * ((h.val : ℚ) - 2) / 6) =
      (if h.val = 3 then 1 else 0)) := by
  decide +kernel

end C0100
