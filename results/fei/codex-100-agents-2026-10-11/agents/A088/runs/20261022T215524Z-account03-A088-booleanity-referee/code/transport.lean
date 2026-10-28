import Std

theorem A088_same_owner (bank debit transfer : Int) :
    (bank + transfer) - (debit + transfer) = bank - debit := by
  omega
