# Finite checks for account01/B03 r30

These checks validate arithmetic and exact matrix identities only; they are not a proof of the unrestricted conjecture.

## Constants

Using the formulas in `REPORT.md`:

- `K2 = 2*pi*sqrt(2e) = 14.65015120674476`
- `4*sqrt(2e) = 9.326575926388497`
- `(16/3)*sqrt(2*pi)*(2e)^(1/4) = 20.41360850273567`
- `(16/3)*(2e)^(1/4) = 8.143851527303443`
- `8*(2e)^(1/4) = 12.215777290955167`
- even-bank obstruction-family constant `8*sqrt(2)*(2e)^(1/4) = 17.275717919798065`
- all `m>=2` obstruction-family constant `8*(2e)^(1/4)*(9/2)^(1/4) = 17.791978079303735`.

## Heavy-row exterior identity

For 1000 fixed-seed (`20260923`) Gaussian matrices `B` of size `6 x 5`, and every tested row `i`, the identity

`||b_i||^2 sum_{j != i} ||b_j(I-P_{b_i})||^2 = sum_{j != i}|b_i wedge b_j|^2`

had maximum relative discrepancy `7.46e-16` (denominator clipped below by one in the finite checker).

Among tested heavy rows `alpha_i>1/2`, whenever the largest projected one-volume marginal also satisfied `beta_j>1/2`, the implication

`|b_i wedge b_j|^2 > Z_2/4`

had zero violations.

The proof in `REPORT.md` is exact and does not depend on these numerical checks.
