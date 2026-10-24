import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.InverseDeriv

/-!
Fifth group of formal checks for "Quadratic forms with nine large eigenvalues have bounded densities":
the antiderivatives behind the exact formula for J(d) in Lemma 5.5 and behind the integral in Lemma 5.6.
-/

open Real

namespace QformNine

/-- Lemma 5.5: 2 log(sqrt y + sqrt(y + d)) is an antiderivative of y^{-1/2} (y + d)^{-1/2} on y > 0. -/
theorem antideriv_left (d y : ℝ) (hd : 0 < d) (hy : 0 < y) :
    HasDerivAt (fun y => 2 * Real.log (Real.sqrt y + Real.sqrt (y + d)))
      (1 / (Real.sqrt y * Real.sqrt (y + d))) y := by
  have hyd : 0 < y + d := by linarith
  have ha : 0 < Real.sqrt y := Real.sqrt_pos.mpr hy
  have hb : 0 < Real.sqrt (y + d) := Real.sqrt_pos.mpr hyd
  have hsum : 0 < Real.sqrt y + Real.sqrt (y + d) := by linarith
  have h1 : HasDerivAt (fun y => Real.sqrt y) (1 / (2 * Real.sqrt y)) y := Real.hasDerivAt_sqrt hy.ne'
  have h2 : HasDerivAt (fun y => Real.sqrt (y + d)) (1 / (2 * Real.sqrt (y + d))) y := by
    have h := ((hasDerivAt_id y).add_const d).sqrt hyd.ne'
    simpa using h
  have h3 := ((h1.add h2).log hsum.ne').const_mul 2
  convert h3 using 1
  simp only [Pi.add_apply]
  have ha' := ha.ne'
  have hb' := hb.ne'
  have hs' := hsum.ne'
  field_simp
  ring

/-- Lemma 5.5: 2 log(sqrt x + sqrt(x - d)) is an antiderivative of x^{-1/2} (x - d)^{-1/2} on x > d > 0. -/
theorem antideriv_right (d x : ℝ) (hd : 0 < d) (hx : d < x) :
    HasDerivAt (fun x => 2 * Real.log (Real.sqrt x + Real.sqrt (x - d)))
      (1 / (Real.sqrt x * Real.sqrt (x - d))) x := by
  have hx0 : 0 < x := by linarith
  have hxd : 0 < x - d := by linarith
  have ha : 0 < Real.sqrt x := Real.sqrt_pos.mpr hx0
  have hb : 0 < Real.sqrt (x - d) := Real.sqrt_pos.mpr hxd
  have hsum : 0 < Real.sqrt x + Real.sqrt (x - d) := by linarith
  have h1 : HasDerivAt (fun x => Real.sqrt x) (1 / (2 * Real.sqrt x)) x := Real.hasDerivAt_sqrt hx0.ne'
  have h2 : HasDerivAt (fun x => Real.sqrt (x - d)) (1 / (2 * Real.sqrt (x - d))) x := by
    have h := ((hasDerivAt_id x).sub_const d).sqrt hxd.ne'
    simpa using h
  have h3 := ((h1.add h2).log hsum.ne').const_mul 2
  convert h3 using 1
  simp only [Pi.add_apply]
  have ha' := ha.ne'
  have hb' := hb.ne'
  have hs' := hsum.ne'
  field_simp
  ring

/-- Lemma 5.6: with s = sqrt y, F(y) = 2 sqrt y (c - log y) + 4 sqrt y has derivative (c - log y)/sqrt y, so the
integral of (c - log y) y^{-1/2} over (0, delta) is 2 sqrt delta (c + 2 - log delta). -/
theorem pair_antideriv (c s : ℝ) (hs : 0 < s) :
    HasDerivAt (fun y => 2 * Real.sqrt y * (c - Real.log y) + 4 * Real.sqrt y)
      ((c - Real.log (s^2)) / s) (s^2) := by
  have hy : 0 < s^2 := by positivity
  have hsq : Real.sqrt (s^2) = s := Real.sqrt_sq hs.le
  have h1 : HasDerivAt (fun y => Real.sqrt y) (1 / (2 * Real.sqrt (s^2))) (s^2) := Real.hasDerivAt_sqrt hy.ne'
  have h2 : HasDerivAt (fun y => c - Real.log y) (0 - (s^2)⁻¹) (s^2) :=
    (hasDerivAt_const (s^2) c).sub (Real.hasDerivAt_log hy.ne')
  have h3 := ((h1.const_mul 2).mul h2).add (h1.const_mul 4)
  convert h3 using 1
  rw [hsq]
  have hs' := hs.ne'
  field_simp
  ring

end QformNine
