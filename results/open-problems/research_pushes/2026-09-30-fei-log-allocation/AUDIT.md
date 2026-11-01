# Independent mathematical audit

Date: 2026-09-30. A separate mathematical reviewer checked the construction and logarithmic replacement from their exact definitions. Verdict: both are valid. This is not publication novelty clearance or formal verification.

## Positive inequality

The reviewer confirmed C_log=2+3/(2 ln2), the packet log-sum argument and the exceptional-fiber payment. One alternate proof of the nonexceptional mass bound is: for alpha=Eg and beta=Eh after folded normalization, |alpha-beta|<=2epsilon and |alpha+beta|<=2(1-epsilon), hence |alpha^2-beta^2|<=4epsilon(1-epsilon). This implies Q_non<=kappa+2epsilon(1-epsilon).

The report already defines epsilon as the folded mismatch j_i, so the reviewer's warning to distinguish raw mismatch from folded mismatch is satisfied. The endpoint epsilon=0 is treated separately.

## Sparse activation

The reviewer independently obtained the exact child influences (7). For r=2k,

    max(I(G),I(H))=k p[5/2-2sqrt(delta)+6delta]<(5k/2)p.

The report's simpler 5kp bound is therefore conservative. It suffices for the quantifiers.

The review also strengthens the allocation lower bound. Put m=delta^(-1/2) and L(t)=t log2(t)-(t-1)log2(t-1). Every packet has q/e at least t_+=(m-1)^2+1. For nonempty data packets the possible ratios are (+/-m-1)^2+1; for empty data and nonempty control packets the ratio is (m^2-m+1)^2+1; and for the fully empty packet it is [m^2(1/p-1)+m-1]^2+1. All query-containing coefficients have magnitude pdelta, and their squared masses sum to pdelta. Hence

    B_y/j_y>=L(t_+)>=k.

For the last step, t_+>=2^(k-1) when k>=4, and L(t)>=log2(t)+1 for t>=2. The report preserves its elementary weaker bound (1-delta)(k-2), which is already sufficient and is the one directly exercised in the checker.

The reviewer confirmed that the sparse example makes the coefficient of the logarithmic term asymptotically necessary. Its largest child coefficient is the constant coefficient, giving the stated exact kappa.

## Quantifiers and surviving gap

The no-go multiplier must be bounded near the origin in the closed nonnegative quadrant. Local boundedness only in the open positive quadrant would permit divergence at the origin and is not rejected. The report states the correct near-origin condition.

This is a prescribed-coordinate obstruction. It does not refute an existential paid-coordinate selector, a stopping-tree theorem, or FEI itself. The new logarithmic charge still requires a nonreusing global payment. The independent review does not supply it.
