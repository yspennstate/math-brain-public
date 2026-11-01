import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Algebraic core of the smearing stability argument in ATTEMPT.md.
-- A: ordered point-pair energy; A': ordered smeared-pair energy without self terms.
-- B and B': point and smeared background interactions; C: background self energy.
theorem smearing_stability
    (A A' B B' C N K F S : ℝ)
    (hpair : A' ≤ A)
    (hbg : B - B' ≤ K * N)
    (hF : F = A / 2 - B + C / 2)
    (hS : S = (A' + N) / 2 - B' + C / 2)
    (hpos : 0 ≤ S) :
    -(K + 1 / 2) * N ≤ F := by
  nlinarith

-- Entropy cancellation used after the stability estimate.
theorem entropy_stability
    (beta K N meanF logZ D : ℝ)
    (hbeta : 0 ≤ beta)
    (hF : -K * N ≤ meanF)
    (hZ : 0 ≤ logZ)
    (hD : D = -beta * meanF - logZ) :
    D ≤ beta * K * N := by
  nlinarith
