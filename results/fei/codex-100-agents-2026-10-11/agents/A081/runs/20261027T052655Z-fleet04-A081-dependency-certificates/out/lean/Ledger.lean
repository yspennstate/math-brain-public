import Std
theorem ledgerCancellation (root resets loss terminal : Int) (h : terminal = root + resets - loss) : root + resets = loss + terminal := by omega
