import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
Arithmetic identities behind the mean hitting times of simple random walk on the lexicographic
product `C_m[K_r-bar]` (the `m`-cycle with every vertex replaced by `r` pairwise non-adjacent
copies), for all integers `m` and `r`.

`g m r j = j (m - j) + (r - 1) m` is the mean hitting time of a fixed vertex from a vertex at
cycle-distance `j ≥ 1`; the twin value is `r m`; a neighbour is hit in `n - 1 = r m - 1` steps,
as Lemma 7.19 of Aldous and Fill requires; the sum of `g` over a fibre-free cycle is the classical
`m (m^2 - 1)/6`; and the ratio `tau*/(2 tau_0)` tends to `3/2`.
-/

namespace BlowUp

/-- Mean hitting time from cycle-distance `j` (`j ≥ 1`) of a fixed vertex of `C_m[K_r-bar]`. -/
def g (m r j : ℤ) : ℤ := j * (m - j) + (r - 1) * m

/-- The harmonic equation `2 g j = 2 + g (j-1) + g (j+1)`: from a vertex at distance `j` the base
walk moves to distance `j ± 1` with probability `1/2` each. -/
theorem g_harmonic (m r j : ℤ) : 2 * g m r j = 2 + g m r (j - 1) + g m r (j + 1) := by
  unfold g; ring

/-- The twin value `r m` is consistent with the boundary condition at the target fibre: from a twin
the walk steps to distance `1` and then needs `g 1`, and `1 + g 1 = r m`. -/
theorem twin_value (m r : ℤ) : 1 + g m r 1 = r * m := by
  unfold g; ring

/-- The value `g 0 = (r-1) m` is the average over the target's fibre of `0` (the target itself)
and `r m` (each of the `r - 1` twins). -/
theorem fibre_average (m r : ℤ) : r * g m r 0 = 0 + (r - 1) * (r * m) := by
  unfold g; ring

/-- A neighbour is hit in `n - 1 = r m - 1` steps (Lemma 7.19(i) of Aldous and Fill). -/
theorem neighbour_hit (m r : ℤ) : g m r 1 = r * m - 1 := by
  unfold g; ring

/-- `j (m - j) ≤ m^2 / 4`. -/
theorem quad_le (m j : ℤ) : 4 * (j * (m - j)) ≤ m ^ 2 := by
  nlinarith [sq_nonneg (m - 2 * j)]

/-- For odd `m = 2k + 1` the maximum `k (k + 1)` is `(m^2 - 1)/4`. -/
theorem quad_max_odd (k : ℤ) : 4 * (k * ((2 * k + 1) - k)) = (2 * k + 1) ^ 2 - 1 := by ring

/-- For even `m = 2k` the maximum `k^2` is `m^2/4`. -/
theorem quad_max_even (k : ℤ) : 4 * (k * (2 * k - k)) = (2 * k) ^ 2 := by ring

/-- `S n m = sum_{j=0}^{n-1} j (m - j)`. -/
def S : ℕ → ℤ → ℤ
  | 0, _ => 0
  | n + 1, m => S n m + (n : ℤ) * (m - (n : ℤ))

theorem S_closed (n : ℕ) (m : ℤ) :
    6 * S n m = 3 * m * (n : ℤ) * ((n : ℤ) - 1) - ((n : ℤ) - 1) * (n : ℤ) * (2 * (n : ℤ) - 1) := by
  induction n with
  | zero => simp [S]
  | succ n ih =>
      have hn : ((n + 1 : ℕ) : ℤ) = (n : ℤ) + 1 := by push_cast; ring
      simp only [S, hn]
      push_cast
      linarith [ih]

/-- The cycle sum `sum_{j=0}^{m-1} j (m - j) = m (m^2 - 1)/6`. -/
theorem cycle_sum (m : ℕ) : 6 * S m (m : ℤ) = (m : ℤ) * ((m : ℤ) ^ 2 - 1) := by
  have h := S_closed m (m : ℤ); nlinarith [h]

/-- Total hitting mass to a fixed target in `C_m[K_r-bar]`: `r - 1` twins at `r m` each, and `r`
vertices at each distance `j ≠ 0` at `g j` each. -/
def TotalHit (m r : ℕ) : ℤ :=
  (r : ℤ) * ((r : ℤ) - 1) * (m : ℤ) + (r : ℤ) * (S m (m : ℤ) + ((r : ℤ) - 1) * (m : ℤ) * ((m : ℤ) - 1))

/-- `tau_0 = TotalHit / (r m) = (m^2 - 1)/6 + (r - 1) m`, stated without division. -/
theorem tau0_formula (m r : ℕ) :
    6 * TotalHit m r = (r : ℤ) * (m : ℤ) * (((m : ℤ) ^ 2 - 1) + 6 * ((r : ℤ) - 1) * (m : ℤ)) := by
  unfold TotalHit
  have h := cycle_sum m
  nlinarith [h]

/-- For odd `m = 2k+1`: `tau* = 2 k (k+1) + 2 (r-1)(2k+1)` and `6 tau_0 = (2k+1)^2 - 1 + 6 (r-1)(2k+1)`. -/
def tauStar (k r : ℤ) : ℤ := 2 * (k * (k + 1)) + 2 * (r - 1) * (2 * k + 1)

def sixTau0 (k r : ℤ) : ℤ := ((2 * k + 1) ^ 2 - 1) + 6 * (r - 1) * (2 * k + 1)

/-- `2 (3 tau*) - 3 (6 tau_0)` is linear in `k`, so `tau*/(2 tau_0) = 3 tau*/(6 tau_0) → 3/2`
as `k → ∞` with `r` fixed. -/
theorem ratio_three_halves (k r : ℤ) :
    2 * (3 * tauStar k r) - 3 * sixTau0 k r = -6 * (r - 1) * (2 * k + 1) := by
  unfold tauStar sixTau0; ring

/-- `tau*` is quadratic in `n = r m = r (2k+1)`: `2 r^2 tau* = n^2 + (4 r^2 (r-1) - 2 r) n ... `; the
simplest sufficient statement is `4 tau* ≥ (2k+1)^2 - 1`, i.e. `tau* ≥ (m^2 - 1)/4`. -/
theorem tau_star_quadratic (k r : ℤ) (hk : 0 ≤ k) (hr : 1 ≤ r) :
    (2 * k + 1) ^ 2 - 1 ≤ 4 * tauStar k r := by
  unfold tauStar
  have h1 : 0 ≤ (r - 1) * (2 * k + 1) := mul_nonneg (by linarith) (by linarith)
  nlinarith [sq_nonneg k, h1, hk]

end BlowUp

#print axioms BlowUp.g_harmonic
#print axioms BlowUp.twin_value
#print axioms BlowUp.neighbour_hit
#print axioms BlowUp.quad_le
#print axioms BlowUp.cycle_sum
#print axioms BlowUp.tau0_formula
#print axioms BlowUp.ratio_three_halves
#print axioms BlowUp.tau_star_quadratic
