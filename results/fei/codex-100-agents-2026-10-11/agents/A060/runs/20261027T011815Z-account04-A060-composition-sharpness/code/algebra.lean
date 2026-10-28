import Mathlib
example (A q t J d fee : ℝ) : A*t*J-fee-q*A*t*(J-d)=t*(A*(1-q)*J+q*A*d)-fee := by ring
