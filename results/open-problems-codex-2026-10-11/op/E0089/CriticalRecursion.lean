import Mathlib.Tactic.Ring

-- Rational polynomial identities for d=4, k=2, vacant core threshold r=3.
theorem critical_recursion_identity (z : ℚ) :
    (8/9 : ℚ) * (3 * (3/4+z)^2 - 2 * (3/4+z)^3) - (3/4+z)
      = -(4/3 : ℚ) * z^2 - (16/9 : ℚ) * z^3 := by
  ring

theorem root_density_identity (z : ℚ) :
    (8/9 : ℚ) * (4 * (3/4+z)^3 - 3 * (3/4+z)^4) - 21/32
      = (3/2 : ℚ)*z - z^2 - (40/9 : ℚ)*z^3 - (8/3 : ℚ)*z^4 := by
  ring

theorem perturbed_recursion_identity (z eta : ℚ) :
    ((8/9 : ℚ)+eta) * (3*(3/4+z)^2-2*(3/4+z)^3) - (3/4+z)
      = -(4/3 : ℚ)*z^2-(16/9 : ℚ)*z^3
        + eta*((27/32 : ℚ)+(9/8 : ℚ)*z-(3/2 : ℚ)*z^2-2*z^3) := by
  ring

theorem initial_gap : (8/9 : ℚ)-(3/4 : ℚ) = 5/36 := by
  decide +kernel

theorem minimum_shrink_factor :
    1-(4/3 : ℚ)*(5/36 : ℚ)-(16/9 : ℚ)*(5/36 : ℚ)^2 = 569/729 := by
  decide +kernel

theorem reciprocal_increment_upper :
    ((4/3 : ℚ)+(16/9 : ℚ)*(5/36 : ℚ))/(569/729 : ℚ) = 1152/569 := by
  decide +kernel
