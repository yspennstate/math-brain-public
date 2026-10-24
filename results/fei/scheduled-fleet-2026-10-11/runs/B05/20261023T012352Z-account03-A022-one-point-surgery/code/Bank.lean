import Mathlib

-- Intended scalar targets only. Admission was held; this file is NOT compiled.
example (t n : ℚ) (ht : 2 ≤ t) (hn : t/2 ≤ n) :
    13*t/576 ≤ (314*n-117*t-54)/576 := by linarith

example (t n : ℚ) (ht : 2 ≤ t) (hn : t/2 ≤ n) :
    13*t/576 ≤ (314*n-117*t-32)/576 := by linarith
