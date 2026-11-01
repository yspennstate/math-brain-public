import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Probability.Independence.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic

theorem a067_pair_likelihood (p0 p1 q0 q1 l : Rat) (h0 : p0 = l*q0) (h1 : p1 = l*q1) : p0*(q0+q1) = q0*(p0+p1) := by rw [h0,h1]; ring
