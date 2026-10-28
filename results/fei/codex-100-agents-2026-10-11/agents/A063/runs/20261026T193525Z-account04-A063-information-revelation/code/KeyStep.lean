-- Intended scalar translation only. NOT compiled: memory admission refused.
-- The Fourier/rank interpretation requires the separate analytic proof.
import Mathlib.Tactic
theorem bent_first_reset_budget (n a d m r : ℤ)
    (ha : d ≤ a) (hm : m ≤ n - a) (hr : r = n - 2*d) :
    m-r ≤ d := by omega
theorem bent_terminal_budget (n d c r : ℤ)
    (hd : 0 ≤ d) (hc : c ≤ d) (hr : r = n - 2*d) :
    c+r ≤ n := by omega
