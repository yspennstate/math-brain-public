# r24 exact checks

These are deterministic algebra/constant checks for `QFORM-LOCAL-3X3-PRINCIPAL-COMPILER-v1`; they are diagnostics, not an independent proof review.

Let

`kappa0 = sqrt(3/8)-1/2 = (sqrt(6)-2)/4`.

If all three physical diagonal entries of a symmetric `3x3` matrix `B` satisfy `|B_ii|<s/2` while `sigma_min(B)>=s`, then

`tr(B^2)>=3s^2`

and

`sum_{i<j} B_ij^2 = (tr(B^2)-sum_i B_ii^2)/2 > (3-3/4)s^2/2 = 9s^2/8`.

Hence one off diagonal satisfies

`|B_ij|^2 > (9/8)/3 s^2 = 3s^2/8`.

For the selected physical pair `C`,

`det C <= |B_ii B_jj|-B_ij^2 < s^2/4-3s^2/8=-s^2/8`,

so `C` is invertible indefinite. Comparing it with `[[0,B_ij],[B_ij,0]]` gives

`sigma_min(C) >= |B_ij|-max(|B_ii|,|B_jj|) > kappa0 s`.

The pair-log constant is therefore at most

`C_pair = 8 sqrt(5) kappa0^(-3/4)`.

The large-diagonal branch constant is

`C_diag = 128*2^(1/4)`.

Numerically,

`kappa0 = 0.11237243569579447...`

`C_pair = 92.16799570280665...`

`C_diag = 152.2185107203483...`.

For an exact comparison without decimals, `sqrt(6)>12/5`, hence `kappa0>1/10`, so

`C_pair < 8 sqrt(5) 10^(3/4)`.

After dividing by `8`, compare fourth powers:

`(sqrt(5) 10^(3/4))^4 = 25*10^3 = 25000`,

`(16*2^(1/4))^4 = 16^4*2 = 131072`.

Thus `C_pair<C_diag`.

CHECK RESULT: `QFORM_B13_R24_LOCAL3_COMPILER_CHECK_PASS`.
