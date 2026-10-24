# Late-lead integration addendum

After the main report was frozen, the team lead published a newer complete run:
account03/B07 `20260922T055130Z-account03-B07-MOC4-r11`, report blob
`055492abce4a340ed49b4dbc44787461454c2b71`, theorem
`MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`.

That theorem gives the full four-real-dimensional second-order condition for each genuine
row/column plane pair.  In the lead notation its mixed-sector matrix satisfies

`||M_{alpha gamma}||_op^2 <= 4 (T_{alpha gamma}^2-C_{alpha gamma}^2)`.

If a pair gate is flat, `T=|C|`, the lead further proves that the two weighted traceless Gram
sums in the affected block rows vanish separately; with distinct `delta X` weights the three
traceless Gram vectors are forced into the explicit one-dimensional coefficient pattern.

This late result is compatible with and sharpens the residual in `REPORT.md`.  Combining it
with this run's `MOC4-TWO-ROOK-ROOF-RIGIDITY-v1` gives the following exact branch structure for
a hypothetical MOC4 support violator/global maximizer:

1. it is strictly below every two-rook roof whose minimizing size-two matching is unique,
   because equality there forces a proper coordinate block and hence MOC4 safety;
2. it satisfies every row and column mixed-Hessian inequality above;
3. on any flat pair it additionally obeys the lead's exact Gram-cancellation/collinearity
   identities; and
4. in every Spin(6) gauge its normalized anti-linear block has the P-coupled unistochastic
   augmentation proved in this run, so the kernel deficits and overlap payments are fixed by
   the same row and column of `P=|U|^2`.

Thus the first unpaid quantitative collar can be stated more narrowly:

**`MOC4-P-HESSIAN-TWO-ROOK-COLLAR-v1` (OPEN).**  On the non-block-safe branch, use the lead's
mixed-Hessian reserve (or its flat-pair Gram cancellation when that reserve is zero) together
with the P-coupled overlap inequalities of this run to bound the strict two-rook-roof deficit
by the available subgroup/V4 support reserve strongly enough to force nonpositive total gap.
A refutation must use actual spectra/support and one genuine global maximizing unitary; free
`P,R,D` or independent gauge data do not qualify.

No additional target-level claim is made.  Outcome remains `ESSENTIAL_STEP_APPLIED`; MOC4
remains open.
