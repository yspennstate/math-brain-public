
import Std
theorem reset_account (A d b r Z T t : Int) (h : T = b + r + t) :
    A - (d + b) - (t + Z) = (A - d - T) + r - Z := by
  omega
