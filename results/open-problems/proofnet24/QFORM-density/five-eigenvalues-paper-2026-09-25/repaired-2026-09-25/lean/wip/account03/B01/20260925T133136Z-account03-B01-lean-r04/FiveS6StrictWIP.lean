import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
WIP exact repaired-Section-6 adapters for
paper.tex @ 4e530247ec0ef4101a6e5ecf621bd35a969c42aa
(blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a).

IMPORTANT: this file is deliberately WIP/UNVERIFIED. account03/B01 did not have
a local Lean/lake executable in this run and remote workflow execution is not
authorized. Nothing below counts as verified until this exact file (or an exact
matching successor theorem) compiles in Lean 4.29.1 / Mathlib 5e932f97 with
no sorry/admit/new axiom and matching #print axioms evidence.

The point of this artifact is to close two exact-statement mismatches between
the repaired wording and the already-compiled original-source Section 6:
(1) strict |a_ij| < 5/48 under strict no-pivot hypotheses;
(2) the strict exact-gamma margin needed to upgrade the general non-strict
    ApproxGE conclusion once a finite strict uniform diagonal bound is supplied.

It intentionally does NOT claim the full repaired Proposition 6.4, Lemma 6.2(b),
or Lemma 6.3 expectation statement.
-/

open Real

namespace QformFiveRepairedSection6

/-- Exact gamma_m from repaired Proposition 6.4. -/
def gammaM (m : ℕ) : ℝ :=
  (44 - 5 * Real.sqrt 2 * (((2 * m - 1 : ℕ) : ℝ))) / 96

/-- Algebraic identity relating repaired gamma_m to eta=1/12 and a0=5/48. -/
theorem gammaM_identity (m : ℕ) :
    gammaM m =
      (1 - (1 / 12 : ℝ) -
          Real.sqrt 2 * (5 / 48 : ℝ) * (((2 * m - 1 : ℕ) : ℝ))) / 2 := by
  unfold gammaM
  ring

/--
Exact repaired no-pivot strict off-diagonal estimate.

The compiled original-source theorem QformFive.nopivot_entries only concluded
<= 5/48.  The repaired paper uses the strict inequality.  This proof preserves
strictness in both inputs rather than weakening them with .le.
-/
theorem nopivot_entries_strict {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ)
    (hd : ∀ i, |A i i| < (1 / 12 : ℝ))
    (hp : ∀ i j, i ≠ j →
      |A i i * A j j - A i j ^ 2| < (1 / 256 : ℝ))
    (i j : Fin n) (hij : i ≠ j) :
    |A i j| < (5 / 48 : ℝ) := by
  have h1 := hd i
  have h2 := hd j
  have h3 := hp i j hij
  have hprodabs :
      |A i i| * |A j j| < (1 / 12 : ℝ) * (1 / 12 : ℝ) := by
    exact mul_lt_mul h1 h2 (abs_nonneg _) (by norm_num)
  have hprod : A i i * A j j < (1 / 144 : ℝ) := by
    calc
      A i i * A j j ≤ |A i i * A j j| := le_abs_self _
      _ = |A i i| * |A j j| := abs_mul _ _
      _ < (1 / 12 : ℝ) * (1 / 12 : ℝ) := hprodabs
      _ = (1 / 144 : ℝ) := by norm_num
  have hneg :
      -(A i i * A j j - A i j ^ 2) < (1 / 256 : ℝ) :=
    lt_of_le_of_lt (neg_le_abs _) h3
  have hsq : A i j ^ 2 < (5 / 48 : ℝ) ^ 2 := by
    nlinarith
  rw [abs_lt]
  constructor <;> nlinarith [sq_nonneg (A i j)]

/--
If a common off-diagonal cap a is at most a0=5/48 and a common diagonal cap
delta is strictly below eta=1/12, then the already-formalized general Prop. 6.4
threshold is strictly larger than the repaired paper's exact gamma_m.

This is the formal strictness bridge needed after extracting a finite
delta < 1/12 from the repaired no-pivot hypotheses.
-/
theorem gamma_strict_of_uniform_bounds (m : ℕ) (a δ : ℝ)
    (ha : a ≤ (5 / 48 : ℝ))
    (hδ : δ < (1 / 12 : ℝ)) :
    gammaM m <
      (1 - δ - Real.sqrt 2 * a * (((2 * m - 1 : ℕ) : ℝ))) / 2 := by
  have hk : 0 ≤ (((2 * m - 1 : ℕ) : ℝ)) := by positivity
  have hmul1 :
      Real.sqrt 2 * a ≤ Real.sqrt 2 * (5 / 48 : ℝ) :=
    mul_le_mul_of_nonneg_left ha (Real.sqrt_nonneg 2)
  have hmul :
      Real.sqrt 2 * a * (((2 * m - 1 : ℕ) : ℝ)) ≤
        Real.sqrt 2 * (5 / 48 : ℝ) * (((2 * m - 1 : ℕ) : ℝ)) :=
    mul_le_mul_of_nonneg_right hmul1 hk
  rw [gammaM_identity]
  linarith

end QformFiveRepairedSection6
