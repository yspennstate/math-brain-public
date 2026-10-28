import Lean.Elab.Tactic.Omega

-- This checks the accounting rearrangement only, not the entropy identities.
theorem projection_ledger_balance (initial terminal js loss : Int)
    (h : terminal - initial = js - loss) :
    terminal + loss = initial + js := by omega

theorem paid_conversion_step (before after fee bank : Int)
    (paid : after + fee ≤ before) (funded : before ≤ bank) :
    after + fee ≤ bank := by omega
