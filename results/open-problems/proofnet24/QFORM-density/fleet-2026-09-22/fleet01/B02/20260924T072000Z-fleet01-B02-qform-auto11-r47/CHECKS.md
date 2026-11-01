# fleet01/B02 r47 deterministic checks

Run: `20260924T072000Z-fleet01-B02-qform-auto11-r47`.

## Algebraic identity check

For random real matrices `B` of sizes `4x5` and `3x4`, random nonzero vectors `c,r`, and nonzero scalar `a`, set

`M=B+c r^T/a`.

Direct enumeration of all `2x2` minors verified to floating-point tolerance in ten trials per size that

`||wedge^2 M-wedge^2 B||_HS^2
 = (||c||||r||/|a|)^2 ||P_{c^perp} B P_{r^perp}||_F^2`.

This is only a numerical check of the exact identity already proved in fleet03/B02 r32; the proof in `REPORT.md` relies on the exact source theorem, not on numerics.

## Live constants

With

`kappa=247/576=0.4288194444444444`,
`a0=1/228`,

we have

`kappa/2 = 247/1152 = 0.2144097222222222`,

`kappa/8 = 247/4608 = 0.05360243055555555`.

The residual-Schur-E2 density coefficient is

`8 e^(1/4) a0^(-1/2) (kappa/8)^(-1/8)
 = 223.6057517579245`.

The two-sided cancellation product floor is

`a0 sqrt(kappa/2)/2
 = 0.0010154473122666696`.

The designated fleet02/B02 one-bank payment is

`2 sqrt(pi) kappa^(-1/4)
 = 4.380627392825819`.

Status: `PASS`.
