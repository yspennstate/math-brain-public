/-
P0208 — Aldous & Fill, *Reversible Markov Chains and Random Walks on Graphs*,
Open Problem 7.27 (Chapter 7, 31 January 1994, PDF p. 259):

  "Is it true that, over arc-transitive graphs excluding the n-cycles,
   tau* = O(n log n), tau2 = O(n) and tau*/(2 tau0) = 1 + o(1)?"

Counterexample: the lexicographic product C_m[K2-bar] for odd m >= 5 — take the
m-cycle and split every vertex into two NON-adjacent twins.  n = 2m, 4-regular,
connected, arc-transitive, not a cycle.  (Aldous & Fill's Example 7.14 is the
*ladder* Z_m x Z_2, which is only vertex-transitive precisely because its rungs
are distinguishable from its cycle edges; deleting the rungs removes that
obstruction.)

This file certifies the ARITHMETIC CORE of the refutation.  The probabilistic
inputs used but not formalised here are standard: (i) for a finite irreducible
chain the linear system (I-P)h = 1 off the target has a unique solution, so
exhibiting a solution identifies the mean hitting times; (ii) A(C_m[K2-bar])
= A(C_m) (x) J_2, whose eigenvalues are 4 cos(2 pi k/m) and 0, so the walk's
relaxation time is that of the m-cycle.  Both were checked numerically to
machine precision at m = 5,7,9,11,15,21, and arc-transitivity was confirmed by
computing the arc orbit of the subgroup (Z_2)^m x| D_m at m = 5,7,9.
-/
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace P0208

/-- Mean hitting time of a fixed vertex from any vertex at cycle-distance `j`
from it (`j = 0` returns the average over the target's own fibre, `m`). -/
def g (m j : ℤ) : ℤ := j * (m - j) + m

/-- **The harmonic equation.**  From `(j,e)` the walk steps to fibre `j±1`
with probability `1/2` each, uniformly over the twin, so `g` must satisfy
`g j = 1 + (g (j-1) + g (j+1))/2`.  It does, for every `m` and `j`. -/
theorem g_harmonic (m j : ℤ) : 2 * g m j = 2 + g m (j - 1) + g m (j + 1) := by
  unfold g; ring

/-- **The twin hitting time.**  From the target's twin the walk reaches fibre
`±1` in one step, so `t = 1 + g 1`; this equals `2m`, the recorded value. -/
theorem twin_hitting (m : ℤ) : 1 + g m 1 = 2 * m := by
  unfold g; ring

/-- The boundary value is consistent: `g 0 = m` is exactly the average of `0`
(the target) and `2m` (its twin) over the target's fibre. -/
theorem g_zero_is_fibre_average (m : ℤ) : 2 * g m 0 = 0 + 2 * m := by
  unfold g; ring

/-- **Maximum commute time.**  Commute time between vertices at distance `j` is
`2 g j`, and `j(m-j)` is maximised at `j = (m±1)/2`.  Upper bound: -/
theorem hit_le (m j : ℤ) : 4 * (j * (m - j)) ≤ m ^ 2 := by
  nlinarith [sq_nonneg (m - 2 * j)]

/-- and it is attained at `j = k` when `m = 2k+1`, giving `floor(m^2/4)`. -/
theorem hit_max_odd (k : ℤ) :
    4 * (k * ((2 * k + 1) - k)) = (2 * k + 1) ^ 2 - 1 := by ring

/-- So for odd `m = 2k+1` the maximal commute time is `2*floor(m^2/4) + 2m`. -/
theorem tau_star_odd (k : ℤ) :
    2 * g (2 * k + 1) k = 2 * (k * (k + 1)) + 2 * (2 * k + 1) := by
  unfold g; ring

/-- `S n m = sum_{j=0}^{n-1} j * (m - j)`. -/
def S : ℕ → ℤ → ℤ
  | 0,     _ => 0
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

/-- **Mean hitting time from stationarity.**  The cycle sum is the classical
`m(m^2-1)/6`. -/
theorem cycle_sum (m : ℕ) : 6 * S m (m : ℤ) = (m : ℤ) * ((m : ℤ) ^ 2 - 1) := by
  have h := S_closed m (m : ℤ); nlinarith [h]

/-- Total un-normalised hitting mass to a fixed target: the twin contributes
`2m`, and each of the two vertices in fibre `j != 0` contributes `g j`. -/
def TotalHit (m : ℕ) : ℤ := 2 * (m : ℤ) + 2 * (S m (m : ℤ) + (m : ℤ) * ((m : ℤ) - 1))

/-- **tau0 = (m^2-1)/6 + m.**  Stated without division: `TotalHit/(2m)` is that
value, i.e. `6 * TotalHit = 2m * (m^2 - 1 + 6m)`. -/
theorem tau0_formula (m : ℕ) :
    6 * TotalHit m = 2 * (m : ℤ) * (((m : ℤ) ^ 2 - 1) + 6 * (m : ℤ)) := by
  unfold TotalHit
  have h := cycle_sum m
  linarith [h]

/-- For odd `m = 2k+1`: `tau* = 2k^2+6k+2` and `6*tau0 = 4k^2+16k+6`. -/
def tauStar (k : ℤ) : ℤ := 2 * (k * (k + 1)) + 2 * (2 * k + 1)

def sixTau0 (k : ℤ) : ℤ := ((2 * k + 1) ^ 2 - 1) + 6 * (2 * k + 1)

/-- **The ratio does not tend to 1; it tends to 3/2.**  Since
`tau*/(2 tau0) = 3*tau*/sixTau0`, the identity below shows the numerator of
`2*(3 tau*) - 3*sixTau0` is LINEAR in `m` while both terms are quadratic, so the
ratio tends to `3/2`.  In particular it is not `1 + o(1)`. -/
theorem ratio_three_halves (k : ℤ) :
    2 * (3 * tauStar k) - 3 * sixTau0 k = -6 * (2 * k + 1) := by
  unfold tauStar sixTau0; ring

/-- **tau* is quadratic, refuting `O(n log n)`**: with `n = 2m = 4k+2`,
`8 * tau* = n^2 + 8n - 4 > n^2`. -/
theorem tau_star_quadratic (k : ℤ) :
    8 * tauStar k = (4 * k + 2) ^ 2 + 8 * (4 * k + 2) - 4 := by
  unfold tauStar; ring

end P0208

#print axioms P0208.g_harmonic
#print axioms P0208.twin_hitting
#print axioms P0208.hit_le
#print axioms P0208.hit_max_odd
#print axioms P0208.tau_star_odd
#print axioms P0208.cycle_sum
#print axioms P0208.tau0_formula
#print axioms P0208.ratio_three_halves
#print axioms P0208.tau_star_quadratic
