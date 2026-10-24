# C0033: the conditional implication has one direction

Label: proof of a conditional implication, awaiting w346. This continues the corrected C0033-A002 record, without proving its premise.

Assume finite-kernel determinantal entropy is midpoint-concave for every finite index set. Let f,g be measurable symbols on the circle with values in [0,1], and let P_f,P_g be their stationary determinantal processes on Z. Their N-coordinate kernels are linear in the symbols, so the kernel of the restriction for (f+g)/2 is the arithmetic mean of the two restricted kernels. The assumption gives H_N(P_((f+g)/2)) >= [H_N(P_f)+H_N(P_g)]/2.

For every stationary binary process, H_N is subadditive: H_(N+M)<=H_N+H_M by the entropy chain rule and stationarity. Fekete's lemma therefore gives a limit h(P)=lim H_N(P)/N, with 0<=h(P)<=log(2). Divide the finite inequality by N and take the limits to obtain h(P_((f+g)/2)) >= [h(P_f)+h(P_g)]/2.

Thus the full finite-kernel conjecture implies the stationary entropy-rate conjecture. This argument supplies no converse; the old store wording "equivalently" is not justified by it. The newly proved fixed-diagonal two-site result also does not establish the premise for all N.
