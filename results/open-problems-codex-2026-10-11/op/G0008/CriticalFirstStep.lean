import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Checked algebra only; geometric hypotheses are justified in ATTEMPT.md.
theorem critical_orbit_bound
    (s a b g d e : Real)
    (hs : 0 <= s) (ha : 0 <= a) (hb : 0 <= b)
    (hg : 0 <= g) (hd : 0 <= d) (he : 0 <= e)
    (hn : s + 4*a + 2*b + 2*g + 4*d + e = 1)
    (hdual : 4*s + 8*a + 4*b - 2*d - 3*e = 0)
    (hfkg : (b + 2*d + e)^2 <= e) :
    (1/2:Real)*s + 2*a + (3/4:Real)*g + (1/2:Real)*d - (1/8:Real)*e
      >= (9/8:Real)*d + (1/4:Real)*g := by
  let t := b + 2*d + e
  have ht : 0 <= t := by dsimp [t]; linarith
  have hf : t^2 <= e := hfkg
  have heq : 2*a + (3/4:Real)*e + t + (5/2:Real)*d + 2*g = 1 := by
    dsimp [t]; linarith
  have htquad : t + (3/4:Real)*t^2 <= 1 := by nlinarith
  have htupper : t <= (2/3:Real) := by
    by_contra h
    have hx : (2/3:Real) < t := lt_of_not_ge h
    nlinarith [sq_nonneg (t - (2/3:Real))]
  have hprod : 0 <= ((2/3:Real)-t)^2 := sq_nonneg _
  have hgap : (5/4:Real)*d + g <= (2/3:Real)-t := by
    nlinarith
  have hsq : 0 <= (t - (2/3:Real))^2 := sq_nonneg _
  have hformula :
    8*((1/2:Real)*s + 2*a + (3/4:Real)*g + (1/2:Real)*d - (1/8:Real)*e)
      = 4 + 3*e - 8*t + 4*d - 2*g := by
    dsimp [t]; linarith
  nlinarith

#print axioms critical_orbit_bound
