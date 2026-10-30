# Supplement — arbitrary-decomposition and one-sided spectral-shield forms

This strengthens Theorem 3.1 of `REPORT.md` and subsumes the bookkeeping clarification in `CORRECTION.md`.

## S1. Arbitrary-decomposition footprint compiler

Let

`A=A0+H+L+T`

with all four matrices symmetric, with no rank/sign/norm restriction on `H`, and assume only

`||L||op<=h`, `||T||op<=delta`.

For disjoint ORIGINAL-coordinate sets `I,J`, define `chi(H;I,J)` as in REPORT.md (2.2). Then

`boxed: ||(A-A0)[I,J]||op <= chi(H;I,J)+h+delta.`             (S1.1)

Proof: triangle inequality, rectangular compression for `L,T`, and Lemma 2.1 for `H`. No common eigenbasis between `H,L,T` is required.

Thus the spectral-threshold theorem is only one canonical choice: if `S=sum tau_k u_k u_k^T`, choose `H=sum_{|tau_k|>h} tau_k u_k u_k^T` and `L=sum_{|tau_k|<=h} tau_k u_k u_k^T`. But an independently supplied small nonseparable matrix can always be merged into `L` or `T` without any commutation assumption.

## S2. One-sided large-eigenvalue shielding

If

`H=sum_k tau_k u_k u_k^T`

is a spectral modification, put

`G_I(H)=sum_k tau_k^2 (u_k)_I (u_k)_I^T = P_I H^2 P_I`.

Then

`boxed: ||H[I,J]||op <= ||G_I(H)||op^(1/2)`,                  (S2.1)

and symmetrically with `J`.

Consequently a whole signed cloud of arbitrarily large spectral changes is free up to budget `eta` whenever its **one-sided squared spectral energy** satisfies

`||sum_k tau_k^2 (u_k)_I(u_k)_I^T||op <= eta^2`.             (S2.2)

No hypothesis on the number, signs, or magnitudes of the `tau_k` is needed beyond this physical shielding condition. Combining (S2.2) with `||L||op<=h`, `||T||op<=delta` and the current volume-stability theorem gives, whenever the protected baseline has `s3(M0)>=a`, row-range leverage at most `1/2`, and

`eta+h+delta<=a/16`,                                          (S2.3)

the continuous bound

`||p_Q||infinity <=24sqrt(3)e/(5a)`.                          (S2.4)

Combining the same budget with the completed fleet02/B12 thresholded cross-energy theorem gives REPORT.md (5.4)--(5.6).

## S3. Why this is a genuinely matrix-level tail statement

Condition (S2.2) is deterministic and localized in ORIGINAL coordinates. It does not require that the spectral coordinates `u_k^T X` be independent. It can hold even for `|tau_k|` tending to infinity, provided the corresponding eigenvectors become proportionally shielded from the protected bank. Conversely, an operator-norm-small `L` is used only to preserve the actual cross certificate; it is never asserted that `X^T L X` is small for unbounded product inputs.

Full QFORM remains OPEN because the bare condition `s3(A)>=1` does not yet force a protected baseline cut plus (S2.3), or one of the other paid branches.
