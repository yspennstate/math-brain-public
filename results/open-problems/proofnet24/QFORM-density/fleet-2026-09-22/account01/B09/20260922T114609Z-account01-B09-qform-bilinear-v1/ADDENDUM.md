# Addendum: unconditional continuity and neighboring rank-two mechanisms

This addendum records two clarifications to `REPORT.md` without rewriting the immutable main report.

1. In Theorem 2.1, boundedness survives averaging conditional densities. Continuity of the **unconditional** density follows more directly by averaging the conditional characteristic functions first: the same deterministic envelope

`|phi_cond(t)| <= min(1,(2 pi)^(r/2)|t|^(-r/2)D^(-1/2))`

holds for every value of the conditioned outside coordinates. Hence the unconditional characteristic function obeys the identical envelope, belongs to `L^1(R)` for `r>=3`, and Fourier inversion gives a bounded continuous representative. No equicontinuity claim about the family of conditional densities is needed.

2. A contemporaneous account03/B09 result (math-open-problems commit `41fc39eccdd44a0dcae6619676bf41f5ea21bb3e`) proves a complementary rank-two theorem when one side is genuinely linear: `H(U)+2U^TMV` has density at most `2 sqrt(pi)/sqrt(s1 s2)`. Together with account02/B09's zero-pivot theorem and counterexample, this sharpens the mechanism boundary: rank two is sufficient when the conditioning exposes an uncurved linear block, but arbitrary curvature on both blocks can retain the logarithmic obstruction; rank three makes the two-sided Plancherel tail integrable without requiring either side to be uncurved.

No status change: the full quadratic-form conjecture remains OPEN.
