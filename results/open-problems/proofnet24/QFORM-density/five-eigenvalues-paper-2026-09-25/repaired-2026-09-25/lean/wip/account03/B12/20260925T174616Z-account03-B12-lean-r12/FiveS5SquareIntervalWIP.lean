import FiveS5Square

/-!
account03/B12 WIP for the remaining statement-level wrapper in repaired Lemma 5.1.

Target source: yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa,
paper.tex blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a, lines 403--414.

The canonical compiled theorem `QformFiveB.lemma51b` proves the closed-interval case
`[c,c+2ρ]`.  The paper states the estimate for every interval U of length `2ρ`.
This file supplies the missing statement-level wrapper: in fact the same estimate holds
for every set U contained in such a closed interval, hence for each of the standard
open/closed endpoint conventions.

UNCOMPILED in this runtime: neither `lean` nor `lake` is exposed and installation
or remote workflow execution is forbidden.  Do not count this file as verified coverage
until it is compiled with Lean 4.29.1 / Mathlib 5e932f97, checked to contain no
`sorry`/`admit`/new `axiom`, and its theorems pass `#print axioms`.
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

/-- Strong wrapper for Lemma 5.1(b): any set contained in a closed interval of width
`2ρ` has the same quadratic preimage bound.  This is stronger than the paper's
"every interval of length `2ρ`" formulation. -/
theorem lemma51b_of_subset_Icc
    (a β γ c ρ : ℝ) (ha : a ≠ 0) (hρ : 0 ≤ ρ) (U : Set ℝ)
    (hU : U ⊆ Icc c (c + 2 * ρ)) :
    volume {y : ℝ | a * y ^ 2 + β * y + γ ∈ U}
      ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |a|)) := by
  refine (measure_mono ?_).trans (lemma51b a β γ c ρ ha hρ)
  intro y hy
  exact hU hy

/-- Open interval endpoint convention. -/
theorem lemma51b_Ioo
    (a β γ c ρ : ℝ) (ha : a ≠ 0) (hρ : 0 ≤ ρ) :
    volume {y : ℝ | a * y ^ 2 + β * y + γ ∈ Ioo c (c + 2 * ρ)}
      ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |a|)) := by
  apply lemma51b_of_subset_Icc a β γ c ρ ha hρ
  intro z hz
  exact ⟨le_of_lt hz.1, le_of_lt hz.2⟩

/-- Left-closed, right-open interval endpoint convention. -/
theorem lemma51b_Ico
    (a β γ c ρ : ℝ) (ha : a ≠ 0) (hρ : 0 ≤ ρ) :
    volume {y : ℝ | a * y ^ 2 + β * y + γ ∈ Ico c (c + 2 * ρ)}
      ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |a|)) := by
  apply lemma51b_of_subset_Icc a β γ c ρ ha hρ
  intro z hz
  exact ⟨hz.1, le_of_lt hz.2⟩

/-- Left-open, right-closed interval endpoint convention. -/
theorem lemma51b_Ioc
    (a β γ c ρ : ℝ) (ha : a ≠ 0) (hρ : 0 ≤ ρ) :
    volume {y : ℝ | a * y ^ 2 + β * y + γ ∈ Ioc c (c + 2 * ρ)}
      ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |a|)) := by
  apply lemma51b_of_subset_Icc a β γ c ρ ha hρ
  intro z hz
  exact ⟨le_of_lt hz.1, hz.2⟩

/-- Closed interval endpoint convention, exposed under the same wrapper family. -/
theorem lemma51b_Icc
    (a β γ c ρ : ℝ) (ha : a ≠ 0) (hρ : 0 ≤ ρ) :
    volume {y : ℝ | a * y ^ 2 + β * y + γ ∈ Icc c (c + 2 * ρ)}
      ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |a|)) :=
  lemma51b a β γ c ρ ha hρ

end QformFiveB
