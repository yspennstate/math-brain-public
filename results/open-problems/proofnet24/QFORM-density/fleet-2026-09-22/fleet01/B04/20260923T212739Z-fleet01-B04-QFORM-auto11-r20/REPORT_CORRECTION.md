# Read-back correction to REPORT.md

Run: `20260923T212739Z-fleet01-B04-QFORM-auto11-r20`.

The exact formula in REPORT.md is authoritative:

`H_1 = 2^(3/4) exp(1/4) Gamma(1/4)`.

Its decimal value is

`H_1 = 7.829376757708328...`,

not `7.832957...` as mistyped in the one explanatory numerical sentence of Section 3. No displayed theorem, exponent, symbolic constant, stress-family bound, or downstream comparison changes. In particular

`C_* = 4 sqrt(2 H_1) = 2^(23/8) exp(1/8) sqrt(Gamma(1/4)) = 15.828457165708429...`

and the `epsilon=10^(-6)` stress bound remains

`6.655046444819971...`.
