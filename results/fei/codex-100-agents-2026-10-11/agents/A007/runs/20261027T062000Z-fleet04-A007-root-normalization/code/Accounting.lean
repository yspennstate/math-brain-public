import Std.Tactic

theorem a007_surplus_refund (a C D B v z : Int)
    (identity : a * C = D - B + a * v * z)
    (surplus_nonnegative : 0 <= B)
    (normalizer_nonpositive : a * v * z <= 0) : a * C <= D := by
  omega
