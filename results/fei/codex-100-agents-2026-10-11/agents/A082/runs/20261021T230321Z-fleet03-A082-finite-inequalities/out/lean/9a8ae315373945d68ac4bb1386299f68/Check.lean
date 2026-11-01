import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Probability.Independence.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic

example (h : ℚ) : 1 - (5/4:ℚ)*h + (13/16:ℚ)*h^2 = (27/52:ℚ) + (13/16:ℚ)*(h-10/13)^2 := by ring
