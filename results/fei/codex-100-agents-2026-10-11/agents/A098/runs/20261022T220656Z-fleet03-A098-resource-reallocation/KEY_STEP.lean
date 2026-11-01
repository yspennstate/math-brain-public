import Mathlib

-- This scalar consequence does not certify the entropy hypotheses or imported claims.
example (B co c cn e L : ℝ) (he : 0 < e)
    (hB : B < 12*e) (hco : co < c+11*e) (hcn : cn ≤ c) :
    B+(co+(cn+20*e*(L-1)))/2 < c+10*e*L+8*e := by
  nlinarith
