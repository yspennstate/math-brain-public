import Std.Tactic

-- Integer-scaled two-child ledger identity only; this is not an FEI theorem.
theorem retained_debit_telescoping
    (parent child0 child1 debit excess : Int)
    (h : child0 + child1 = 2 * (parent + excess)) :
    child0 + child1 - 2 * (debit + excess) = 2 * (parent - debit) := by
  omega
