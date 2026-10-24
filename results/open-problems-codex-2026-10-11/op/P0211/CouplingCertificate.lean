import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Nlinarith
import Mathlib.Tactic.Positivity

-- All claims below are algebraic sublemmas of the written proof.
-- They do not purport to formalize the Markov-chain or harmonic decomposition.

theorem stageII_identity (b n r a : ℝ) (hn : n ≠ 0) (hd : r+a-1 ≠ 0) :
    -r^2/(n*(r+a-1)) + b + r/n =
      b + r*(a-1)/(n*(r+a-1)) := by
  field_simp [hn, hd]
  <;> ring

theorem high_count_certificate (n r a : ℝ) (hn : 0 < n)
    (ha : 2 ≤ a) (hr : a ≤ r) :
    a/(4*n) ≤ r*(a-1)/(n*(r+a-1)) := by
  have hd : 0 < r+a-1 := by linarith
  have hp : a*(r+a-1) ≤ 4*r*(a-1) := by
    have h1 : 0 ≤ (r-a)*(3*a-4) := mul_nonneg (by linarith) (by linarith)
    have h2 : 0 ≤ a*(2*a-3) := mul_nonneg (by linarith) (by linarith)
    nlinarith
  apply (div_le_div_iff₀ (by positivity : 0 < 4*n) (by positivity : 0 < n*(r+a-1))).2
  nlinarith [mul_nonneg hn.le (sub_nonneg.mpr hp)]

theorem stageI_death_bound (n k a : ℝ) (hn : 0 < n)
    (hk : 1 ≤ k) (ha : 1 ≤ a) :
    k*(k-1)/(n*(k+a-1)) ≤ k/n := by
  have hd : 0 < k+a-1 := by linarith
  apply (div_le_div_iff₀ (by positivity : 0 < n*(k+a-1)) hn).2
  have h : 0 ≤ n*k*a := mul_nonneg (mul_nonneg hn.le (by linarith)) (by linarith)
  nlinarith

theorem harmonic_sector_identity (b n k l a : ℝ)
    (hn : n ≠ 0) (hd : k+a-1 ≠ 0) :
    -(k-1)*(k-l)/(n*(k+a-1)) + l*b + l*(k-1)/n =
      l*b + (k-1)*((l-1)*k+l*a)/(n*(k+a-1)) := by
  field_simp [hn, hd]
  <;> ring

theorem count_double_reciprocal_identity (b n k a : ℝ)
    (hn : n ≠ 0) (hd : k+a-1 ≠ 0) :
    -2*k*(k-1)/(n*(k+a-1)) + b + 2*k/n =
      b + 2*k*a/(n*(k+a-1)) := by
  field_simp [hn, hd]
  <;> ring

theorem high_sector_certificate (n k a : ℝ) (hn : 0 < n)
    (ha : 2 ≤ a) (hk : a ≤ k) :
    a/(3*n) ≤ (k-1)*a/(n*(k+a-1)) := by
  have hd : 0 < k+a-1 := by linarith
  have h0 : 0 ≤ 3*(k-1)-(k+a-1) := by linarith
  have h1 : 0 ≤ n*a*(3*(k-1)-(k+a-1)) :=
    mul_nonneg (mul_nonneg hn.le (by linarith)) h0
  apply (div_le_div_iff₀ (by positivity : 0 < 3*n) (by positivity : 0 < n*(k+a-1))).2
  nlinarith

theorem low_sector_certificate (b n k l a : ℝ)
    (hb : 0 ≤ b) (hn : 0 < n) (ha : 2 ≤ a)
    (hk : 1 ≤ k) (hka : k ≤ a) (hlk : l ≤ k)
    (han : a ≤ n/4) :
    b*n/(5*a) ≤ b*(n-k-l)/(k+a+1) := by
  have ha0 : 0 < a := by linarith
  have hd : 0 < k+a+1 := by linarith
  have hN : n/2 ≤ n-k-l := by linarith
  have hD : k+a+1 ≤ 5*a/2 := by linarith
  have hp : n*(k+a+1) ≤ (n-k-l)*(5*a) := by
    calc
      n*(k+a+1) ≤ n*(5*a/2) := mul_le_mul_of_nonneg_left hD hn.le
      _ = (n/2)*(5*a) := by ring
      _ ≤ (n-k-l)*(5*a) := mul_le_mul_of_nonneg_right hN (by positivity)
  apply (div_le_div_iff₀ (by positivity : 0 < 5*a) hd).2
  nlinarith [mul_nonneg hb (sub_nonneg.mpr hp)]
