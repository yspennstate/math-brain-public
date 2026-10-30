import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Probability.Independence.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic

example (e : ?) : (1+3*e)*(1-2*e+2*e^2)-(1+3*e^2)= e*(1-e)*(1-6*e) := by ring
