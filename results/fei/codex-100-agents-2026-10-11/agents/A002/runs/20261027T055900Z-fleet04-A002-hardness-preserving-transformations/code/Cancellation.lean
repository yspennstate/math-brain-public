import Lean.Elab.Tactic.Omega

-- This is the binary-node cancellation after clearing finite dyadic reaches.
-- It certifies this scalar algebra only, not the Boolean/entropy premises.
theorem A002_weighted_cancellation
    (d dl dr tl tr e el er k kl kr : Int)
    (h : 2*d-dl-dr+2*e = 2*k)
    (hl : dl-tl+el = kl) (hr : dr-tr+er = kr) :
    2*d-tl-tr+(2*e+el+er) = 2*k+kl+kr := by
  omega
