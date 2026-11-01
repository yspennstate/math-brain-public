# L315 total-variation finding
Verdict: PASS mathematically; Lean UNCHECKED.

For every finite measurable partition (B_j) of B,
sum_j |nu_x(B_j)| <= sum_j P(Y in B_j) = P(Y in B).
Taking the supremum over finite measurable partitions gives domination of the variation of nu_x by Law(Y).

New formalization progress: a local candidate reduces the corresponding Mathlib preVariationFun bound to exactly this finite-partition hypothesis via iSup_le. The remaining formal bridge is variation domination -> complex RN derivative with norm <= p_Y a.e.
