# r27 notation correction

The mathematical inequality used in REPORT.md (3.8)-(3.9) is correct, but the first display in (3.8) was written with garbled shorthand. The exact derivation is:

Under `v_-=c h_-`, put `H=||h_-||_2`. From the exact wedge identity,

`m = H |v_r-c h_r|`.

Therefore

`m <= H |v_r| + H |c| |h_r|`
`   = H |v_r| + ||v_-||_2 |h_r|`
`   <= H + |h_r|`,

because `v` is unit, so both `|v_r|<=1` and `||v_-||_2<=1`. Hence the stated consequence

`H >= m-|h_r|`

is exact. No theorem, constant, scope, or subsequent inequality changes.
