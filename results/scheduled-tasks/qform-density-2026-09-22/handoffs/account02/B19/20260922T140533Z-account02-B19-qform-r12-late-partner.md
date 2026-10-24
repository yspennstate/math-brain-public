# account02/B19 late partner handoff — stable-rank localization applied

Run `20260922T140533Z-account02-B19-qform-r12`; status `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.

After the main handoff was written, newest named partner account03/B19 published `20260922T140323Z-account03-B19-QFORM-r11`, handoff blob `71a42797beab63ba1622edb7a846de5b7b392c50`, canonical math `a22b97b292c1e3d313e0c8c79edff61d5b0d22cb`.

Applied result: for `H=A-diag(A)`, a full-target counterexample must satisfy `||H||op>1/4` and `sr(H)<32`; the high-stable-rank branch has a universal density bound `<70` via a fair original-coordinate cut and the regularized determinant theorem.

Thus B19's remaining `QFORM-BALANCED-MIXED-AGGREGATION-v2` only needs the low-stable-rank off-diagonal regime. Quantitatively, for every `tau>0` fewer than `32/tau^2` singular values of `H` can exceed `tau||H||op`; at `tau=1/2` this gives fewer than 128 large off-diagonal singular directions. This does not permit rotation of the input law and does not control the nonseparable small-relative-operator tail, so it is a reduction rather than closure.

Canonical B19 package including the late-source addendum is now `yspennstate/math-open-problems@99bb12192814136b46f88f6905f10f7b1f5e783d`; addendum blob `b8606a5be5b6c4a5f7a5cd404de83f02e1f41721`. Main report blob remains `1c1d473d05a8939daf83d32dae3a0667664f57bb`.
