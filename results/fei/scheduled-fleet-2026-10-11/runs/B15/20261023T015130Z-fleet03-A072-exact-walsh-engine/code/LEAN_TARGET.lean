import Mathlib
example (s0 s1 a0 a1 s a e : Real) (hs : (s0+s1)/2=s+e) (ha : (a0+a1)/2=a) : ((s0+a0)+(s1+a1))/2=s+a+e := by linarith
