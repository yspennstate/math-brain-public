# Early substantive checkpoint

Candidate theorem now proved up to endpoint bookkeeping: the sharp QFORM constant can be tested on a countable generic compact-support core. Using the exact compact smooth-kernel normal form from account01/B15 run 20260923T031931Z, every target value can be approximated with no loss by data satisfying simultaneously: each marginal is the indicator of a bounded finite union of rational intervals of total length one; the center is rational with |y|>2; A is rational symmetric, 1<s_3(A)<2, has simple spectrum, and every nonempty principal minor is nonzero. The proof uses bounded-support continuity of the fixed smooth payoff in (A,y), a tiny upward spectral scaling before rational perturbation, and symmetric-difference approximation of the product sets. Hence exact zero physical pivots/principal minors are not a separate obstruction to the sharp constant; only near-zero pivots can matter.

Planned partner application: on this generic core every physical 3x3 block is invertible. Apply account02/B15 20260923T030440Z Theorem 6.1 to an indefinite block B to get, for the compact kernel kappa with integral one,

s_3(A) E[kappa(y-Q) 1_{Z^T B Z>=0}] <= pi*sqrt(2) s_3(A)/sigma_min(B),

with Z the original-coordinate completed-square variable. This pays the entire majority-sheet part and leaves only the minority/two-sheet contribution plus near-singular block geometry.

Full QFORM remains OPEN. No rotated-independence, pointwise Fourier decay, arbitrary-joint coarea, or projection-only shortcut is used.
