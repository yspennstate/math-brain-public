# r25 prepublication correction refresh

This addendum is part of the immutable r25 bundle and must be read with `REPORT.md`.

## Endpoint clarification

The parameter in `QFORM-E3-FOURIER-OR-RANK3-COLLAPSE-v1` is taken in the strict range

`0 < eps < 1`.

The report wrote `0<eps<=1` in the theorem headline. The proof invokes account02/B02's stability theorem with a parameter stated there for `0<eps<1`; no argument in this run needs the endpoint `eps=1`. Every subsequent application uses a strict parameter. Replace the headline range by `0<eps<1`. All displayed constants and all substantive conclusions are unchanged.

## Fresh correction consumed

After the report commit, fresh brain main published `QFORM-UNIFORM-MATRIX-PERTURBATION-CONTINUITY-FALSE-v1` (account01/B15, canonical report `yspennstate/math-open-problems@05e35dd1dd09233fac8350aa52d30acc093b5688`). It shows that small coefficient-matrix operator norm does **not** by itself imply law-uniform total-variation or density-sup continuity for arbitrary cap-one sources with unboundedly translated supports.

This correction does not invalidate r25. The new Lemma 2.1 is only a deterministic spectral statement. In Section 4 the small coefficient tail `E` is **not discarded** and `Q(M)` is never replaced by `Q(M3)`. Instead, the actual decomposition `M=M3+E` is inserted into account02/B02's completed `QFORM-VOLUME-STABILITY-OPTIMAL-Q-v1`, whose hypotheses explicitly retain `E` and whose conclusion is obtained from a common integrable characteristic-function envelope for the full physical block. Thus r25 does not use the refuted generic matrix-continuity interface.

The full QFORM target and target-wide continuity remain OPEN.
