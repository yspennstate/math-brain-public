/-
Machine-checked finite steps from
"Cover-time fluctuations beyond the maximal hitting-time scale".

Part 1: the clique-star graph G_k (Sections 2-6).

The probability spaces, stopping times and limit theorems of the paper are not
formalised. What is checked here is every finite identity and inequality on which
those arguments rest, stated as it appears in the text: the hitting-time table and
t_hit(G_k) (Proposition 3.1), the excursion transform, its derivative at 1 and its
second-order Taylor data (Lemma 3.2), the algebra behind the moment-generating bound
(3.6), the stage transform and the coupon-clock closed forms (Proposition 4.1), the
third-moment bounds of Lemma 4.2, the union bound of Lemma 5.1, the initial variances
(5.5), the scaling of Theorem 6.1, the interpolation exponent of (2.7), and the
second-order mean expansion (2.2) from the exact formula (5.4) with an explicit
error constant.
-/
import Mathlib.Tactic
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.NumberTheory.Harmonic.EulerMascheroni

open Finset

namespace CoverTime.CliqueStar

/-! ### Proposition 3.1: the hitting-time table -/

/-- Target a leaf `a`. With `A = H(s,a)`, `B = H(g,a)`, `C = H(q,a)`, the three first-step
equations of the text force the first three entries of the table. -/
theorem target_leaf (k A B C : ℚ)
    (h1 : C = B + k - 1)
    (h2 : k * B = k + A + (k - 1) * C)
    (h3 : (k + 1) * A = k + 1 + (k - 1) * (1 + A) + B) :
    A = k ^ 2 + k + 1 ∧ B = 2 * k ^ 2 + 2 ∧ C = 2 * k ^ 2 + k + 1 :=
  ⟨by linear_combination (k - 1) * h1 + h2 + h3,
   by linear_combination 2 * (k - 1) * h1 + 2 * h2 + h3,
   by linear_combination (2 * k - 1) * h1 + 2 * h2 + h3⟩

/-- A walk from another leaf `b` first steps to `s`: `H(b,a) = 1 + H(s,a) = k² + k + 2`. -/
theorem target_leaf_from_leaf (k A : ℚ) (hA : A = k ^ 2 + k + 1) :
    1 + A = k ^ 2 + k + 2 := by
  rw [hA]; ring

/-- Target the centre `s`: the gateway and clique equations give
`H(g,s) = k² - k + 1` and `H(q,s) = k²`. -/
theorem target_centre (k Hg Hq : ℚ)
    (h1 : k * Hg = k + (k - 1) * Hq)
    (h2 : (k - 1) * Hq = (k - 1) + Hg + (k - 2) * Hq) :
    Hg = k ^ 2 - k + 1 ∧ Hq = k ^ 2 :=
  ⟨by linear_combination h1 + (k - 1) * h2, by linear_combination h1 + k * h2⟩

/-- Target the gateway `g`: each unsuccessful attempt from `s` costs two steps, so
`H(s,g) = 2k + 1`; from a non-gateway clique vertex `H(q,g) = k - 1`. -/
theorem target_gateway (k Hs Hq : ℚ)
    (h1 : (k + 1) * Hs = (k + 1) + k * (1 + Hs))
    (h2 : (k - 1) * Hq = (k - 1) + (k - 2) * Hq) :
    Hs = 2 * k + 1 ∧ Hq = k - 1 :=
  ⟨by linear_combination h1, by linear_combination h2⟩

/-- Target a non-gateway clique vertex `q`: with `X = H(g,q)`, `Y = H(q',q)`, `W = H(s,q)`
the three equations of the text give `kX = k² + 3k + 4`, `kW = 3k² + 4k + 4` and
`kY = k² + k + 2`, i.e. `X = k + 3 + 4/k`, `W = 3k + 4 + 4/k`, `Y = k + 1 + 2/k`. -/
theorem target_clique (k X Y W : ℚ)
    (h1 : 2 * Y = k - 1 + X)
    (h2 : W = 2 * k + 1 + X)
    (h3 : k * X = k + W + (k - 2) * Y) :
    k * X = k ^ 2 + 3 * k + 4 ∧ k * W = 3 * k ^ 2 + 4 * k + 4 ∧ k * Y = k ^ 2 + k + 2 :=
  ⟨by linear_combination (k - 2) * h1 + 2 * h2 + 2 * h3,
   by linear_combination (k - 2) * h1 + (k + 2) * h2 + 2 * h3,
   by linear_combination (k - 1) * h1 + h2 + h3⟩

/-- The comparison in the proof of Proposition 3.1:
`k(2k² + k + 1) - k(3k + 5 + 4/k) = 2k³ - 2k² - 4k - 4`, which at `k = 3 + t` equals
`2t³ + 16t² + 38t + 20`. -/
theorem comparison_polynomial (t : ℚ) :
    2 * (3 + t) ^ 3 - 2 * (3 + t) ^ 2 - 4 * (3 + t) - 4
      = 2 * t ^ 3 + 16 * t ^ 2 + 38 * t + 20 := by
  ring

theorem comparison_positive (t : ℚ) (ht : 0 ≤ t) :
    0 < 2 * t ^ 3 + 16 * t ^ 2 + 38 * t + 20 := by
  positivity

/-- Every entry of the table is at most `2k² + k + 1` for `k ≥ 3`; the four entries
carrying a `1/k` are compared after multiplication by `k`. Hence `t_hit(G_k) = 2k² + k + 1`. -/
theorem table_max (k : ℚ) (hk : 3 ≤ k) :
    k ^ 2 + k + 1 ≤ 2 * k ^ 2 + k + 1 ∧ 2 * k ^ 2 + 2 ≤ 2 * k ^ 2 + k + 1 ∧
    k ^ 2 + k + 2 ≤ 2 * k ^ 2 + k + 1 ∧ k ^ 2 - k + 1 ≤ 2 * k ^ 2 + k + 1 ∧
    k ^ 2 ≤ 2 * k ^ 2 + k + 1 ∧ 2 * k + 2 ≤ 2 * k ^ 2 + k + 1 ∧
    k ^ 2 + 3 * k + 4 ≤ k * (2 * k ^ 2 + k + 1) ∧
    3 * k ^ 2 + 4 * k + 4 ≤ k * (2 * k ^ 2 + k + 1) ∧
    3 * k ^ 2 + 5 * k + 4 ≤ k * (2 * k ^ 2 + k + 1) ∧
    k ^ 2 + k + 2 ≤ k * (2 * k ^ 2 + k + 1) := by
  have h0 : 0 ≤ k - 3 := by linarith
  have h1 : 0 ≤ k ^ 2 * (k - 3) := mul_nonneg (sq_nonneg k) h0
  have h2 : 0 ≤ k * (k - 3) := mul_nonneg (by linarith) h0
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> nlinarith

/-! ### Lemma 3.2: the excursion transform and its moments -/

/-- (3.2): the generating function `z²/(k-1-(k-2)z)` of `D_i = 1 + Geom₁(1/(k-1))`
substituted into the generating function `(1/k)/(1-(1-1/k)u)` of `F ~ Geom₀(1/k)`,
times `z²` for the steps `s → g` and `g → s`, is the closed form `f_k(z)` of the text. -/
theorem excursion_transform (k z : ℚ) (hk : 3 ≤ k) (hz0 : 0 ≤ z) (hz1 : z ≤ 1) :
    z ^ 2 * ((1 / k) / (1 - (1 - 1 / k) * (z ^ 2 / (k - 1 - (k - 2) * z)))) =
      z ^ 2 * (k - 1 - (k - 2) * z) / (k * (k - 1) - k * (k - 2) * z - (k - 1) * z ^ 2) := by
  have hk0 : (0 : ℚ) < k := by linarith
  have hk0' : k ≠ 0 := hk0.ne'
  have hz2 : z ^ 2 ≤ 1 := pow_le_one₀ hz0 hz1
  have hd1 : 0 < k - 1 - (k - 2) * z := by
    nlinarith [mul_nonneg (sub_nonneg.2 hz1) (by linarith : (0 : ℚ) ≤ k - 2)]
  have hd1' : k - 1 - (k - 2) * z ≠ 0 := hd1.ne'
  have hd2 : 0 < k * (k - 1) - k * (k - 2) * z - (k - 1) * z ^ 2 := by
    nlinarith [mul_nonneg (sub_nonneg.2 hz1) (mul_nonneg hk0.le (by linarith : (0 : ℚ) ≤ k - 2)),
      mul_nonneg (sub_nonneg.2 hz2) (by linarith : (0 : ℚ) ≤ k - 1)]
  have hd2' : k * (k - 1) - k * (k - 2) * z - (k - 1) * z ^ 2 ≠ 0 := hd2.ne'
  have hinner : 1 - (1 - 1 / k) * (z ^ 2 / (k - 1 - (k - 2) * z)) =
      (k * (k - 1) - k * (k - 2) * z - (k - 1) * z ^ 2) / (k * (k - 1 - (k - 2) * z)) := by
    generalize hd : k - 1 - (k - 2) * z = d at hd1'
    rw [eq_div_iff (mul_ne_zero hk0' hd1')]
    field_simp
    rw [← hd]
    ring
  rw [hinner]
  field_simp

/-- The geometric parameters used in the proof of (3.3)-(3.4): with `p = 1/(k-1)`,
`E D_i = 1 + 1/p = k` and `Var D_i = (1-p)/p² = (k-1)(k-2)`; with `p = 1/k`,
`E F = (1-p)/p = k - 1` and `Var F = (1-p)/p² = k(k-1)`. -/
theorem geometric_parameters (k : ℚ) (hk : 3 ≤ k) :
    1 + 1 / (1 / (k - 1)) = k ∧
    (1 - 1 / (k - 1)) / (1 / (k - 1)) ^ 2 = (k - 1) * (k - 2) ∧
    (1 - 1 / k) / (1 / k) = k - 1 ∧
    (1 - 1 / k) / (1 / k) ^ 2 = k * (k - 1) := by
  have h1 : k - 1 ≠ 0 := (by linarith : (0 : ℚ) < k - 1).ne'
  have h2 : k ≠ 0 := (by linarith : (0 : ℚ) < k).ne'
  refine ⟨?_, ?_, ?_, ?_⟩ <;> field_simp <;> ring

/-- (3.3) by the random-sum formula `E Y = 2 + E F · E D`. -/
theorem mean_random_sum (k : ℚ) : 2 + (k - 1) * k = k ^ 2 - k + 2 := by ring

/-- (3.4) by the random-sum formula `Var Y = E F · Var D + Var F · (E D)²`. -/
theorem variance_random_sum (k : ℚ) :
    (k - 1) * ((k - 1) * (k - 2)) + k * (k - 1) * k ^ 2 = k ^ 4 - 4 * k ^ 2 + 5 * k - 2 := by
  ring

/-- Numerator and denominator of the excursion transform as real functions of `z`. -/
noncomputable def num (k z : ℝ) : ℝ := z ^ 2 * (k - 1 - (k - 2) * z)

noncomputable def den (k z : ℝ) : ℝ := k * (k - 1) - k * (k - 2) * z - (k - 1) * z ^ 2

theorem num_one (k : ℝ) : num k 1 = 1 := by unfold num; ring

theorem den_one (k : ℝ) : den k 1 = 1 := by unfold den; ring

theorem hasDerivAt_num (k : ℝ) : HasDerivAt (num k) (4 - k) 1 := by
  have h1 : HasDerivAt (fun z : ℝ => z ^ 2) (((2 : ℕ) : ℝ) * (1 : ℝ) ^ (2 - 1)) 1 :=
    hasDerivAt_pow 2 1
  have h2 : HasDerivAt (fun z : ℝ => k - 1 - (k - 2) * z) (-((k - 2) * 1)) 1 :=
    (hasDerivAt_id' (1 : ℝ) |>.const_mul (k - 2)).const_sub (k - 1)
  unfold num
  exact (h1.mul h2).congr_deriv (by norm_num <;> ring)

theorem hasDerivAt_den (k : ℝ) : HasDerivAt (den k) (2 - k ^ 2) 1 := by
  have h1 : HasDerivAt (fun z : ℝ => k * (k - 1) - k * (k - 2) * z) (-(k * (k - 2) * 1)) 1 :=
    (hasDerivAt_id' (1 : ℝ) |>.const_mul (k * (k - 2))).const_sub (k * (k - 1))
  have h2 : HasDerivAt (fun z : ℝ => (k - 1) * z ^ 2)
      ((k - 1) * (((2 : ℕ) : ℝ) * (1 : ℝ) ^ (2 - 1))) 1 :=
    (hasDerivAt_pow 2 (1 : ℝ)).const_mul (k - 1)
  unfold den
  exact (h1.sub h2).congr_deriv (by norm_num <;> ring)

/-- (3.3) by differentiation: `f_k'(1) = k² - k + 2 = μ_k`. -/
theorem hasDerivAt_transform (k : ℝ) :
    HasDerivAt (fun z => num k z / den k z) (k ^ 2 - k + 2) 1 := by
  have h := (hasDerivAt_num k).div (hasDerivAt_den k) (by rw [den_one]; exact one_ne_zero)
  exact h.congr_deriv (by rw [num_one, den_one]; ring)

/-- The second-order Taylor data of `f_k` at `z = 1`: with `T(z) = 1 + μ_k (z-1) + c (z-1)²`,
`c = k⁴ - k³ + k = f_k''(1)/2`, the numerator minus the denominator times `T` is divisible by
`(z-1)³`. Hence `f_k(1) = 1`, `f_k'(1) = μ_k` and `f_k''(1) = 2k⁴ - 2k³ + 2k = E Y_k(Y_k - 1)`. -/
theorem taylor_certificate (k z : ℝ) :
    num k z - den k z * (1 + (k ^ 2 - k + 2) * (z - 1) + (k ^ 4 - k ^ 3 + k) * (z - 1) ^ 2)
      = (z - 1) ^ 3 *
        (k * (k - 1) * (k ^ 4 + k ^ 3 * z - k ^ 3 - k ^ 2 * z - k ^ 2 + 2 * k + z - 1)) := by
  unfold num den; ring

/-- (3.4) from the Taylor data: `σ_k² = f''(1) + f'(1) - f'(1)²`. -/
theorem variance_from_transform (k : ℚ) :
    (2 * k ^ 4 - 2 * k ^ 3 + 2 * k) + (k ^ 2 - k + 2) - (k ^ 2 - k + 2) ^ 2
      = k ^ 4 - 4 * k ^ 2 + 5 * k - 2 := by
  ring

/-- The step in the proof of (3.6): if `Cc ≤ 1/2` then `(1 - 1/k)(1 + Cc/k) ≤ 1 - 1/(2k)`,
written here multiplied out by `2k²` with `x = Cc`. -/
theorem mgf_step (k x : ℚ) (hk : 3 ≤ k) (_hx0 : 0 ≤ x) (hx : x ≤ 1 / 2) :
    2 * (k - 1) * (k + x) ≤ (2 * k - 1) * k := by
  nlinarith [mul_le_mul_of_nonneg_left hx (by linarith : (0 : ℚ) ≤ 2 * (k - 1))]

/-- ... and then the geometric series over `F` is at most `2`. -/
theorem mgf_series_bound (k m : ℚ) (hk : 3 ≤ k) (hm : (1 - 1 / k) * m ≤ 1 - 1 / (2 * k)) :
    (1 / k) / (1 - (1 - 1 / k) * m) ≤ 2 := by
  have hk0 : 0 < k := by linarith
  have hk0' : k ≠ 0 := hk0.ne'
  have hpos : 1 / (2 * k) ≤ 1 - (1 - 1 / k) * m := by linarith
  have hpos' : 0 < 1 - (1 - 1 / k) * m := lt_of_lt_of_le (by positivity) hpos
  rw [div_le_iff₀ hpos']
  calc 1 / k = 2 * (1 / (2 * k)) := by field_simp
    _ ≤ 2 * (1 - (1 - 1 / k) * m) := by gcongr

/-! ### Proposition 4.1: the stage transform and the coupon-clock closed forms -/

/-- (4.1) specialised: at `v = 1` the transform `j/(k+1-u-(k-j)v)` is the `Geom₀(j/(j+1))`
transform, at `u = 1` it is the `Geom₀(j/k)` transform. -/
theorem stage_marginals (k j u v : ℚ) (hk : 0 < k) (hj : 1 ≤ j) (hu : u < j + 1)
    (hv : (k - j) * v < k) :
    j / (k + 1 - u - (k - j) * 1) = (j / (j + 1)) / (1 - u / (j + 1)) ∧
    j / (k + 1 - 1 - (k - j) * v) = (j / k) / (1 - (k - j) / k * v) := by
  have hk0 : k ≠ 0 := hk.ne'
  have hj1 : j + 1 ≠ 0 := (by linarith : (0 : ℚ) < j + 1).ne'
  have hu1 : j + 1 - u ≠ 0 := (by linarith : (0 : ℚ) < j + 1 - u).ne'
  have hv1 : k - (k - j) * v ≠ 0 := (by linarith : (0 : ℚ) < k - (k - j) * v).ne'
  constructor
  · rw [show k + 1 - u - (k - j) * 1 = j + 1 - u by ring]
    field_simp
  · rw [show k + 1 - 1 - (k - j) * v = k - (k - j) * v by ring]
    field_simp

/-- (4.2)-(4.3) from the geometric parameters: with `p = j/(j+1)` the mean `(1-p)/p = 1/j`
and the variance `(1-p)/p² = 1/j + 1/j²` of `N_j`; with `p = j/k` the mean `(k-j)/j` and
the variance `k²/j² - k/j` of `M_j`; and the covariance `E N M - E N · E M = (k-j)/j²`
from the mixed second moment `2j(k-j)/j³` of the stage transform. -/
theorem stage_moments (k j : ℚ) (hk : 0 < k) (hj : 1 ≤ j) :
    (1 - j / (j + 1)) / (j / (j + 1)) = 1 / j ∧
    (1 - j / (j + 1)) / (j / (j + 1)) ^ 2 = 1 / j + 1 / j ^ 2 ∧
    (1 - j / k) / (j / k) = (k - j) / j ∧
    (1 - j / k) / (j / k) ^ 2 = k ^ 2 / j ^ 2 - k / j ∧
    2 * j * (k - j) / j ^ 3 - (1 / j) * ((k - j) / j) = (k - j) / j ^ 2 := by
  have hj0 : j ≠ 0 := (by linarith : (0 : ℚ) < j).ne'
  have hj1 : j + 1 ≠ 0 := (by linarith : (0 : ℚ) < j + 1).ne'
  have hk0 : k ≠ 0 := hk.ne'
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> field_simp <;> ring

/-- The third raw moment of `N_j ~ Geom₀(p)`, `p = j/(j+1)`, is
`(1-p)(1 + 4(1-p) + (1-p)²)/p³ = 1/j + 6/j² + 6/j³` (Lemma 4.2). -/
theorem stage_third_moment (j : ℚ) (hj : 1 ≤ j) :
    (1 - j / (j + 1)) * (1 + 4 * (1 - j / (j + 1)) + (1 - j / (j + 1)) ^ 2) / (j / (j + 1)) ^ 3
      = 1 / j + 6 / j ^ 2 + 6 / j ^ 3 := by
  have hj0 : j ≠ 0 := (by linarith : (0 : ℚ) < j).ne'
  have hj1 : j + 1 ≠ 0 := (by linarith : (0 : ℚ) < j + 1).ne'
  field_simp
  ring

theorem stage_third_moment_bound (j : ℚ) (hj : 1 ≤ j) :
    1 / j + 6 / j ^ 2 + 6 / j ^ 3 ≤ 13 / j := by
  have hj0 : 0 < j := by linarith
  have h2 : 6 / j ^ 2 ≤ 6 / j :=
    div_le_div_of_nonneg_left (by norm_num) hj0 (by nlinarith)
  have h3 : 6 / j ^ 3 ≤ 6 / j :=
    div_le_div_of_nonneg_left (by norm_num) hj0 (by nlinarith)
  have : 13 / j = 1 / j + 6 / j + 6 / j := by ring
  linarith

/-- `μ_k + 2k = d_k`. -/
theorem d_identity (k : ℚ) : (k ^ 2 - k + 2) + 2 * k = k ^ 2 + k + 2 := by ring

/-- `σ_k² + μ_k² - 4μ_k - 4k = c_k`. -/
theorem c_identity (k : ℚ) :
    (k ^ 4 - 4 * k ^ 2 + 5 * k - 2) + (k ^ 2 - k + 2) ^ 2 - 4 * (k ^ 2 - k + 2) - 4 * k
      = 2 * k ^ 4 - 2 * k ^ 3 - 3 * k ^ 2 + k - 6 := by
  ring

/-- `E L_{k,r} = k H_r`: the stage means `1 + (k-j)/j` sum to `k H_r`. -/
theorem leaf_departure_mean (k : ℚ) (r : ℕ) :
    ∑ j ∈ Icc 1 r, (1 + (k - j) / (j : ℚ)) = k * ∑ j ∈ Icc 1 r, (1 : ℚ) / j := by
  rw [mul_sum]
  refine sum_congr rfl fun j hj => ?_
  have hj0 : (j : ℚ) ≠ 0 := by
    have := (mem_Icc.mp hj).1
    exact_mod_cast (by omega : j ≠ 0)
  field_simp
  ring

/-- (4.6): the stage means `μ_k/j + 2 + 2(k-j)/j` of `Λ_{k,r}` sum to `d_k H_r`, and the
final return step is subtracted. -/
theorem clock_mean (k : ℚ) (r : ℕ) :
    (∑ j ∈ Icc 1 r, ((k ^ 2 - k + 2) / (j : ℚ) + 2 + 2 * (k - j) / j)) - 1
      = (k ^ 2 + k + 2) * (∑ j ∈ Icc 1 r, (1 : ℚ) / j) - 1 := by
  rw [mul_sum]
  congr 1
  refine sum_congr rfl fun j hj => ?_
  have hj0 : (j : ℚ) ≠ 0 := by
    have := (mem_Icc.mp hj).1
    exact_mod_cast (by omega : j ≠ 0)
  field_simp
  ring

/-- (4.8): the stage variances `σ_k²/j + μ_k²(1/j + 1/j²)` of `S_{k,r}` sum to
`(σ_k² + μ_k²) H_r + μ_k² H_r^{(2)}`. -/
theorem trap_clock_variance (k : ℚ) (r : ℕ) :
    ∑ j ∈ Icc 1 r, ((k ^ 4 - 4 * k ^ 2 + 5 * k - 2) / (j : ℚ)
        + (k ^ 2 - k + 2) ^ 2 * (1 / j + 1 / (j : ℚ) ^ 2))
      = ((k ^ 4 - 4 * k ^ 2 + 5 * k - 2) + (k ^ 2 - k + 2) ^ 2) * (∑ j ∈ Icc 1 r, (1 : ℚ) / j)
        + (k ^ 2 - k + 2) ^ 2 * (∑ j ∈ Icc 1 r, (1 : ℚ) / (j : ℚ) ^ 2) := by
  rw [mul_sum, mul_sum, ← sum_add_distrib]
  refine sum_congr rfl fun j hj => ?_
  have hj0 : (j : ℚ) ≠ 0 := by
    have := (mem_Icc.mp hj).1
    exact_mod_cast (by omega : j ≠ 0)
  field_simp
  ring

/-- (4.9): the stage variances `k²/j² - k/j` of `L_{k,r}` sum to `k² H_r^{(2)} - k H_r`. -/
theorem leaf_departure_variance (k : ℚ) (r : ℕ) :
    ∑ j ∈ Icc 1 r, (k ^ 2 / (j : ℚ) ^ 2 - k / j)
      = k ^ 2 * (∑ j ∈ Icc 1 r, (1 : ℚ) / (j : ℚ) ^ 2) - k * (∑ j ∈ Icc 1 r, (1 : ℚ) / j) := by
  rw [mul_sum, mul_sum, ← sum_sub_distrib]
  refine sum_congr rfl fun j hj => ?_
  have hj0 : (j : ℚ) ≠ 0 := by
    have := (mem_Icc.mp hj).1
    exact_mod_cast (by omega : j ≠ 0)
  field_simp

/-- (4.10): the stage covariances `μ_k (k-j)/j²` sum to `μ_k (k H_r^{(2)} - H_r)`. -/
theorem trap_leaf_covariance (k : ℚ) (r : ℕ) :
    ∑ j ∈ Icc 1 r, (k ^ 2 - k + 2) * ((k - j) / (j : ℚ) ^ 2)
      = (k ^ 2 - k + 2) * (k * (∑ j ∈ Icc 1 r, (1 : ℚ) / (j : ℚ) ^ 2)
          - ∑ j ∈ Icc 1 r, (1 : ℚ) / j) := by
  rw [mul_sum, ← sum_sub_distrib, mul_sum]
  refine sum_congr rfl fun j hj => ?_
  have hj0 : (j : ℚ) ≠ 0 := by
    have := (mem_Icc.mp hj).1
    exact_mod_cast (by omega : j ≠ 0)
  field_simp

/-- (4.7): `Var Λ = Var S + 4 Var L + 4 Cov(S, L)` summed stage by stage equals
`c_k H_r + d_k² H_r^{(2)}`. -/
theorem clock_variance (k : ℚ) (r : ℕ) :
    ∑ j ∈ Icc 1 r, (((k ^ 4 - 4 * k ^ 2 + 5 * k - 2) / (j : ℚ)
          + (k ^ 2 - k + 2) ^ 2 * (1 / j + 1 / (j : ℚ) ^ 2))
        + 4 * (k ^ 2 / (j : ℚ) ^ 2 - k / j)
        + 4 * ((k ^ 2 - k + 2) * ((k - j) / (j : ℚ) ^ 2)))
      = (2 * k ^ 4 - 2 * k ^ 3 - 3 * k ^ 2 + k - 6) * (∑ j ∈ Icc 1 r, (1 : ℚ) / j)
        + (k ^ 2 + k + 2) ^ 2 * (∑ j ∈ Icc 1 r, (1 : ℚ) / (j : ℚ) ^ 2) := by
  rw [mul_sum, mul_sum, ← sum_add_distrib]
  refine sum_congr rfl fun j hj => ?_
  have hj0 : (j : ℚ) ≠ 0 := by
    have := (mem_Icc.mp hj).1
    exact_mod_cast (by omega : j ≠ 0)
  field_simp
  ring

/-! ### Lemma 4.2: the inequalities behind the Berry-Esseen input -/

/-- `(a + b)³ ≤ 4(a³ + b³)` for `a, b ≥ 0`. -/
theorem cube_sum_bound (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    (a + b) ^ 3 ≤ 4 * (a ^ 3 + b ^ 3) := by
  nlinarith [mul_nonneg (add_nonneg ha hb) (sq_nonneg (a - b))]

/-- `|u - m|³ ≤ (u + m)³` for `u, m ≥ 0`; with the previous bound and Jensen's
`m³ ≤ E U³` this is `E|U - EU|³ ≤ 8 E U³`. -/
theorem centred_cube_bound (u m : ℝ) (hu : 0 ≤ u) (hm : 0 ≤ m) :
    |u - m| ^ 3 ≤ (u + m) ^ 3 := by
  have h : |u - m| ≤ u + m := by
    rw [abs_le]; constructor <;> linarith
  exact pow_le_pow_left₀ (abs_nonneg _) h 3

/-! ### Section 5: the initial variances and the union bound of Lemma 5.1 -/

/-- (5.5): from a non-gateway clique vertex, `Var T_s = σ_k² + (k-1)(k-2) = k⁴ - 3k² + 2k`. -/
theorem initial_variance_clique (k : ℚ) :
    (k ^ 4 - 4 * k ^ 2 + 5 * k - 2) + (k - 1) * (k - 2) = k ^ 4 - 3 * k ^ 2 + 2 * k := by
  ring

/-- Lemma 5.1: for `n ≥ 4(k-1) log k`, `k (1 - 1/(k-1))^n ≤ k⁻³`, the union bound for the
clique `K_k` not being covered by time `n`. -/
theorem clique_cover_tail (k : ℝ) (hk : 3 ≤ k) (n : ℕ) (hn : 4 * (k - 1) * Real.log k ≤ n) :
    k * (1 - 1 / (k - 1)) ^ n ≤ 1 / k ^ 3 := by
  have hk0 : 0 < k := by linarith
  have hk1 : 0 < k - 1 := by linarith
  have hbase : 1 - 1 / (k - 1) ≤ Real.exp (-(1 / (k - 1))) := by
    have := Real.add_one_le_exp (-(1 / (k - 1)))
    linarith
  have hbase0 : 0 ≤ 1 - 1 / (k - 1) := by
    rw [sub_nonneg, div_le_one hk1]; linarith
  have hpow : (1 - 1 / (k - 1)) ^ n ≤ Real.exp (-(1 / (k - 1))) ^ n :=
    pow_le_pow_left₀ hbase0 hbase n
  rw [← Real.exp_nat_mul] at hpow
  have hexp : Real.exp (n * -(1 / (k - 1))) ≤ Real.exp (-(4 * Real.log k)) := by
    rw [Real.exp_le_exp]
    have h : 4 * Real.log k ≤ n * (1 / (k - 1)) := by
      rw [← div_eq_mul_one_div, le_div_iff₀ hk1]
      calc 4 * Real.log k * (k - 1) = 4 * (k - 1) * Real.log k := by ring
        _ ≤ n := hn
    linarith
  have hk4 : Real.exp (-(4 * Real.log k)) = 1 / k ^ 4 := by
    rw [Real.exp_neg, show (4 : ℝ) * Real.log k = ((4 : ℕ) : ℝ) * Real.log k by norm_num,
      Real.exp_nat_mul, Real.exp_log hk0, one_div]
  calc k * (1 - 1 / (k - 1)) ^ n ≤ k * (1 / k ^ 4) := by
        apply mul_le_mul_of_nonneg_left _ hk0.le
        exact hpow.trans (hexp.trans_eq hk4)
    _ = 1 / k ^ 3 := by field_simp

/-! ### Theorem 6.1: the scaling of the cumulant expansion -/

/-- With `z = θ a_k k²/b_{k,r}`, the leading term `z² b²/(2k⁴)` of the summed expansion (6.1)
divided by `a_k²` is `θ²/2`. -/
theorem moderate_deviation_scaling (θ a k b : ℝ) (ha : a ≠ 0) (hk : k ≠ 0) (hb : b ≠ 0) :
    1 / a ^ 2 * ((θ * a * k ^ 2 / b) ^ 2 * b ^ 2 / (2 * k ^ 4)) = θ ^ 2 / 2 := by
  field_simp

/-! ### Corollary 2.2: the interpolation exponent (2.7) -/

/-- `√2 · 2^{-β} (log k)^{β - 1/2} = (log k / 2)^{β - 1/2}`, with `L = log k > 0`. -/
theorem interpolation_exponent (L β : ℝ) (hL : 0 < L) :
    Real.sqrt 2 * (2 : ℝ) ^ (-β) * L ^ (β - 1 / 2) = (L / 2) ^ (β - 1 / 2) := by
  rw [Real.div_rpow hL.le (by norm_num), Real.rpow_sub (by norm_num : (0 : ℝ) < 2),
    Real.sqrt_eq_rpow, Real.rpow_neg (by norm_num)]
  have h1 : (2 : ℝ) ^ β ≠ 0 := (Real.rpow_pos_of_pos (by norm_num) _).ne'
  have h2 : (2 : ℝ) ^ (1 / (2 : ℝ)) ≠ 0 := (Real.rpow_pos_of_pos (by norm_num) _).ne'
  field_simp

/-! ### Section 5.1: the second-order mean expansion (2.2) from the exact formula (5.4) -/

/-- `log n + γ ≤ H_n ≤ log n + γ + 1/n` for `n ≥ 1`. -/
theorem harmonic_bounds (n : ℕ) (hn : 1 ≤ n) :
    Real.log n + Real.eulerMascheroniConstant ≤ (harmonic n : ℝ) ∧
      (harmonic n : ℝ) ≤ Real.log n + Real.eulerMascheroniConstant + 1 / n := by
  have hn0 : (0 : ℝ) < n := by exact_mod_cast hn
  have h1 := Real.eulerMascheroniSeq_lt_eulerMascheroniConstant n
  have h2 := Real.eulerMascheroniConstant_lt_eulerMascheroniSeq' n
  unfold Real.eulerMascheroniSeq at h1
  unfold Real.eulerMascheroniSeq' at h2
  rw [if_neg (by omega)] at h2
  have h3 : Real.log ((n : ℝ) + 1) ≤ Real.log n + 1 / n := by
    have h4 : Real.log (((n : ℝ) + 1) / n) ≤ ((n : ℝ) + 1) / n - 1 :=
      Real.log_le_sub_one_of_pos (by positivity)
    rw [Real.log_div (by positivity) hn0.ne'] at h4
    have h5 : ((n : ℝ) + 1) / n - 1 = 1 / n := by field_simp; ring
    linarith
  exact ⟨by linarith, by linarith⟩

/-- (2.2) and (5.4) with an explicit error: for `k ≥ 3` the exact leading mean
`m_{k,q} = k² + d_k H_k - 1` of a non-gateway clique start (the largest of the four
`m_{k,x}`) is within `3k log k + 5k` of `k² log k + (1 + γ) k²`. -/
theorem mean_expansion (k : ℕ) (hk : 3 ≤ k) :
    |((k : ℝ) ^ 2 + ((k : ℝ) ^ 2 + k + 2) * (harmonic k : ℝ) - 1)
        - ((k : ℝ) ^ 2 * Real.log k + (1 + Real.eulerMascheroniConstant) * (k : ℝ) ^ 2)|
      ≤ 3 * k * Real.log k + 5 * k := by
  obtain ⟨hlo, hhi⟩ := harmonic_bounds k (by omega)
  have hk3 : (3 : ℝ) ≤ k := by exact_mod_cast hk
  have hk0 : (0 : ℝ) < k := by linarith
  have hk0' : (k : ℝ) ≠ 0 := hk0.ne'
  have hlog : 0 ≤ Real.log k := Real.log_nonneg (by linarith)
  have hγ1 := Real.one_half_lt_eulerMascheroniConstant
  have hγ2 := Real.eulerMascheroniConstant_lt_two_thirds
  have hε0 : 0 ≤ (harmonic k : ℝ) - Real.log k - Real.eulerMascheroniConstant := by linarith
  have hε1 : (harmonic k : ℝ) - Real.log k - Real.eulerMascheroniConstant ≤ 1 / (k : ℝ) := by
    linarith
  have hd : ((k : ℝ) ^ 2 + k + 2) * ((harmonic k : ℝ) - Real.log k - Real.eulerMascheroniConstant)
      ≤ (k : ℝ) + 2 := by
    calc ((k : ℝ) ^ 2 + k + 2) * ((harmonic k : ℝ) - Real.log k - Real.eulerMascheroniConstant)
        ≤ ((k : ℝ) ^ 2 + k + 2) * (1 / (k : ℝ)) := by gcongr
      _ = (k : ℝ) + 1 + 2 / (k : ℝ) := by field_simp
      _ ≤ (k : ℝ) + 2 := by
          have : (2 : ℝ) / k ≤ 1 := by rw [div_le_one hk0]; linarith
          linarith
  have hd0 : 0 ≤ ((k : ℝ) ^ 2 + k + 2) *
      ((harmonic k : ℝ) - Real.log k - Real.eulerMascheroniConstant) :=
    mul_nonneg (by positivity) hε0
  have hdiff : ((k : ℝ) ^ 2 + ((k : ℝ) ^ 2 + k + 2) * (harmonic k : ℝ) - 1)
        - ((k : ℝ) ^ 2 * Real.log k + (1 + Real.eulerMascheroniConstant) * (k : ℝ) ^ 2)
      = ((k : ℝ) + 2) * (Real.log k + Real.eulerMascheroniConstant)
        + ((k : ℝ) ^ 2 + k + 2) * ((harmonic k : ℝ) - Real.log k - Real.eulerMascheroniConstant)
        - 1 := by ring
  rw [hdiff, abs_le]
  constructor
  · nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ k + 2) (by linarith : 0 ≤ Real.log k + Real.eulerMascheroniConstant)]
  · nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ 2 * k - 2) hlog,
      mul_le_mul_of_nonneg_left hγ2.le (by linarith : (0 : ℝ) ≤ k + 2)]

/-- The expansions used in the proof of (2.3): `|c_k - 2k⁴| ≤ 4k³` and `|d_k² - k⁴| ≤ 5k³`
for `k ≥ 3`. -/
theorem variance_coefficient_expansions (k : ℚ) (hk : 3 ≤ k) :
    |(2 * k ^ 4 - 2 * k ^ 3 - 3 * k ^ 2 + k - 6) - 2 * k ^ 4| ≤ 4 * k ^ 3 ∧
    |(k ^ 2 + k + 2) ^ 2 - k ^ 4| ≤ 5 * k ^ 3 := by
  have h0 : 0 ≤ k - 3 := by linarith
  have h1 : 0 ≤ k ^ 2 * (k - 3) := mul_nonneg (sq_nonneg k) h0
  have h2 : 0 ≤ k * (k - 3) := mul_nonneg (by linarith) h0
  constructor <;> rw [abs_le] <;> constructor <;> nlinarith

end CoverTime.CliqueStar
