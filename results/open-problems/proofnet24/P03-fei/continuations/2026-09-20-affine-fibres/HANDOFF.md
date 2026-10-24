# FEI handoff: affine-fibre gluing, 20 September 2026

**Full FEI remains OPEN.** This continuation proves a restricted, all-dimensional closure theorem, not the universal conjecture. Read [the full proof](REPORT.md), [the exact checker](verify_affine_fibres.py), and [the executed output](verification.json).

## Main mathematical delta

For existing physical coordinates `(x,y)`, let `pi(y)` have distinct affine fibres, let `g(y)` be Boolean, and let `Q(x)` be any quadratic. Put `F_Q=(-1)^{Q(x)+x dot pi(y)}g(y)`. If every section of each affine fibre parallel to all of its tangent physical coordinate axes satisfies `H<=C J`, then

    H(F_Q) <= max{4,C} J(F_Q) <= max{4,C} I(F_Q).

The exact fibre entropy formula is `H(F_0)=sum_a q_a[2 r_a+H(h_a)]`. Leaving-cell physical edges have exactly half-disagreement after averaging the existing tag coordinates. Charging the non-coordinate tangent directions by the two-bit entropy-deletion lemma closes the maximum constant without a cell-count or recursive-depth loss.

Quadratic intrinsic cell phases give the sharp class constant four. Standard addressing functions prove sharpness. Arbitrary quadratic phases on the tag coordinates add at most the polar rank in entropy, while their nonzero polar rows supply sufficient tag influence. Certified quadratic-twisted symmetric sections from the preceding report retain constant 12.04. Disjoint products and the earlier zero-cost isospectral splices may be interleaved with the new gluing operation.

## Two proof-reading clarifications

In REPORT Section 7's optional direct rank payment, average the quadratic derivative over the **entire affine cell** before folding its influence. A nonzero physical tangent row of the full intrinsic polar matrix has mean derivative zero over the cell, so its cell-averaged influence is one half. Apply concavity across cells to (5.1), before the additional concavity across sections used in (5.2). This yields the optional bound `J_y >= sum_a q_a(kappa_a+t_a)/2`. A derivative involving only the complement coordinates can be constant on each fixed section; one must not count its sectionwise folded influence as one half. The main gluing proof in Section 6 is unaffected.

In REPORT Section 10, “compensating terms” means shared budget across fibres; it does not require negative scalar charges. This distinction can be seen explicitly on the same one-point-defect family. Let `delta=2^{1-n}`, `psi_n(t)=n(t^(2-1/n)-t^2)`, and let `T_n` denote the exceptional fibre charge defined there. Every other fibre has the common charge

    U_n = 2 psi_n(delta) - (1/2) psi_{n-1}(2 delta).

There are `2^(n-1)-1 = 1/delta-1` such fibres. With

    a_n = n(2^(1-1/n)-1),

one obtains the exact identity

    U_n/delta^2 = 2(a_n-a_{n-1}).

Taylor expansion gives `a_n=n-2 ln 2+(ln 2)^2/n+O(n^-2)`, hence `U_n/delta^2=2+o(1)`. Meanwhile Section 10 proves `T_n/delta^2=n+3/2-2 ln 2+o(1)`. Therefore the full adaptive coordinate charge is

    A_i = T_n + (1/delta-1) U_n,
    A_i/Inf_i = T_n/delta + (1/delta-1) U_n/delta -> 2,

because `Inf_i=delta` and `n delta -> 0`. The exceptional fibre defeats a uniform *individual-fibre* payment, but its aggregate weight is too small to defeat the whole-function selector. This also explains precisely why the previous bounded whole-function one-point result is preserved. No universal endpoint selector is proved here.

## Do not remove these hypotheses

Distinct pieces with the same Fourier tag cannot be treated as independent mixture components. Fixing tag coordinates can merge labels and destroy the representation. Appending fresh tags to an arbitrary function does not transfer the bound back to that function. Mixed quadratic terms can alter the effective label map and require rechecking its affine fibres. A single unrestricted cell merely repeats the local FEI hypothesis; it does not close FEI.

## Next full-scope mathematical task

Use these functions as additional direct stopping classes. The missing theorem is a dimension-free allocation controlling arbitrary physical restriction branches, including coherent collisions, or a whole-function endpoint selector retaining shared spectral budgets. The Hellinger/KL identities and endpoint-adaptive potential in the cited predecessor reports remain live. Neither an unrestricted decomposition into this class nor the inherited universal weighted-erasure bound has been proved.

## Delivery and actual checks

Repository `yspennstate/math-open-problems`, branch `master`:

- Proof creation commit: `86b5c86b7856e702149f5c0dff1d4bf2bf2105c2`; Git blob `29d8afcabc09ee1564a1e0db51cf42a21ffa804d`.
- Checker creation commit: `80bd8b83f28f6ce5950fa866e90ca85aa4e93e9d`; Git blob `225b3be486eb7472fd023304baef24709733ab18`.
- Executed output creation commit: `491a657a03746be4b07de9da72fc0f4687249599`; Git blob `0c72b88d69926d8147dae6c440adb7b4dbddfec7`.

All three blobs were read back from master and matched the local bytes by Git blob hash. The identical checker was replayed locally and produced byte-identical output. Actual output includes 233,530 structured cases, 700,392 associated physical coordinate checks, 240 arbitrary-core cases, 3,275 sections, 240 quadratic-tag cases, and 240 quadratic-cell/tag cases. These overlapping finite families are not unrestricted Boolean coverage. The all-dimensional conclusions rest on the written proofs, not extrapolation.

No independent review, literature-priority clearance, or proof-assistant formalization is claimed. All prior results and their correction history remain intact. No schedules, permissions, visibility settings, or unrelated research were changed. Repository delivery does not by itself demonstrate that subsequent scheduled workers have consumed this handoff.
