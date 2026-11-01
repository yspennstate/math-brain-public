import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Finite and algebraic steps in "Correlation of leaf heights at mesoscopic separation in the
critical beta-splitting tree". Equation and lemma numbers refer to the paper. -/

/-- The potential is nonnegative: `ab ≥ m` when `a + b = m + 1` and `a, b ≥ 1` (Section 2). -/
theorem potential_nonneg (a b m : ℝ) (ha : 1 ≤ a) (hb : 1 ≤ b) (hm : a + b = m + 1) :
    m ≤ a * b := by
  nlinarith [mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hb)]

/-- Loss of the potential at a cut removing `l` leaves on the near side, in ratio form (2.1). -/
theorem loss_ratio (a b m l : ℝ) (hm : m ≠ 0) (hb : b ≠ 0) (hal : a - l ≠ 0) (hml : m - l ≠ 0) :
    (a * b / m) / ((a - l) * b / (m - l)) = a * (m - l) / (m * (a - l)) := by
  field_simp

/-- The substitution behind (2.2): with `t = x(m-a)/(a(m-x))`, `1 - t = m(a-x)/(a(m-x))`. -/
theorem substitution (a m x : ℝ) (ha : a ≠ 0) (hmx : m - x ≠ 0) :
    1 - x * (m - a) / (a * (m - x)) = m * (a - x) / (a * (m - x)) := by
  field_simp
  ring

/-- The rate identity (3.1): `1/(m-k) - a_r(m,k) = r/((m-r)k)`. -/
theorem pair_rate_deficit (m k r : ℝ) (h1 : m - r ≠ 0) (h2 : k ≠ 0) (h3 : m - k ≠ 0) :
    1 / (m - k) - m * (k - r) / ((m - r) * k * (m - k)) = r / ((m - r) * k) := by
  field_simp
  ring

/-- The separating-cut weight (Lemma 4.1): `1/(i(m-i)) = (1/i + 1/(m-i))/m`. -/
theorem weight_decomposition (i m : ℝ) (hi : i ≠ 0) (hm : m ≠ 0) (hmi : m - i ≠ 0) :
    1 / (i * (m - i)) = (1 / i + 1 / (m - i)) / m := by
  field_simp
  ring

/-- Ranks after the separating cut `i = j + a - 1` in a clade `m = s + r` (Section 4):
the right tag sits at `b = r + 1 - a` from the left and `h = s + 1 - j` from the right. -/
theorem ranks_after_cut (j a r s : ℤ) :
    (j + r) - (j + a - 1) = r + 1 - a ∧
    ((s + r) - (j + a - 1)) + 1 - (r + 1 - a) = s + 1 - j ∧
    (r + 1 - a) + (s + 1 - j) - 1 = (s + r) - (j + a - 1) := by
  refine ⟨by ring, by ring, by ring⟩

/-- Reflection `(j,a) ↦ (h,b)` sends the cut `i` to `m - i` (Lemma 4.1). -/
theorem reflection_cut (j a r s : ℤ) :
    (s + 1 - j) + (r + 1 - a) - 1 = (s + r) - (j + a - 1) := by ring

/-- Exit rate of a dyadic bin (Lemma 2.2): `⌊k/2⌋ / (2(k-1)) ≥ 1/4` for `k ≥ 2`. -/
theorem bin_exit_count (k : ℕ) (hk : 2 ≤ k) : k - 1 ≤ 2 * (k / 2) := by omega

/-- Killing below `4r` (Proposition 3.2): `r/(m-1) > 1/4` when `m < 4r`. -/
theorem kill_below (r m : ℕ) (h : m < 4 * r) : m - 1 < 4 * r := by omega

/-- Polarization used in (5.3): `2xy = x^2 + y^2 - (x-y)^2`. -/
theorem polarization (x y : ℝ) : 2 * x * y = x ^ 2 + y ^ 2 - (x - y) ^ 2 := by ring

/-- The elementary inequality used for the cross term in Lemma 4.1: `t u^2 ≤ (t^3 + 2u^3)/3`. -/
theorem amgm_three (t u : ℝ) (ht : 0 ≤ t) (hu : 0 ≤ u) : t * u ^ 2 ≤ (t ^ 3 + 2 * u ^ 3) / 3 := by
  nlinarith [sq_nonneg (t - u), mul_nonneg ht hu, mul_nonneg (mul_nonneg ht hu) hu,
    mul_nonneg (sq_nonneg (t - u)) (add_nonneg ht (mul_nonneg (by norm_num : (0:ℝ) ≤ 2) hu))]

#print axioms potential_nonneg
#print axioms loss_ratio
#print axioms substitution
#print axioms pair_rate_deficit
#print axioms weight_decomposition
#print axioms ranks_after_cut
#print axioms bin_exit_count
#print axioms amgm_three
