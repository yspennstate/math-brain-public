# Late named-partner addendum — low-stable-rank localization of the remaining synthesis debt

A newer named-partner result arrived after the main report was written and is incorporated here before finish.

Source: fleet03/B19 run `20260922T140323Z-fleet03-B19-QFORM-r11`, brain handoff blob `71a42797beab63ba1622edb7a846de5b7b392c50`, canonical package `yspennstate/math-open-problems@a22b97b292c1e3d313e0c8c79edff61d5b0d22cb`.

The partner proves: with `H=A-diag(A)`, either the near-diagonal branch pays, or if `sr(H)>=32` a fair physical cut plus the regularized-determinant theorem yields a continuous density with universal bound `<70`. Therefore every full-target counterexample must lie in the simultaneous residual

`||H||op > 1/4`, `sr(H)<32`.

This is applied to the main report's open implication. The synthesis debt `QFORM-BALANCED-MIXED-AGGREGATION-v2` now only needs to be solved inside the **low-stable-rank off-diagonal regime**. In particular, the two-heavy + one-diffuse exact-rank-three model isolated by `QFORM-SEQUENTIAL-HEAVY-DETBANK-v1` is not one branch among arbitrary high-complexity off-diagonal matrices: it sits inside a residual whose off-diagonal energy has stable rank <32. The next extraction theorem may therefore use a constant-size singular bank, but it still may not rotate the independent input law or pay a reciprocal tiny physical minor.

A quantitative consequence useful for the next attack is the thresholded SVD count: for every `tau>0`, the number of singular values of `H` at least `tau||H||op` is `<32/tau^2`. Thus for example at most 128 off-diagonal singular directions can exceed `||H||op/2`. This finite-bank statement by itself does not solve QFORM because the remaining small-operator tail is nonseparable and `||H||op` has no universal upper bound. It does, however, source-validly replace an unbounded-dimensional mixed-profile search by a constant-cardinality large-singular bank plus a small-relative-operator tail.

The full target remains OPEN. No new full-proof claim is made.
