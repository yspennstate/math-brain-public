import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Probability.Independence.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic

theorem query_normalizer_deficit (x y : ℚ) (h : x + y = 2) : 1 - x * y = (x - 1)^2 := by nlinarith
