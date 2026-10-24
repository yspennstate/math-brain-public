# Early substantive checkpoint — account01/B12

Run: `20260923T151555Z-account01-B12-QFORM-auto11`

Target: additional-eigenvalue control for the QFORM density conjecture.

## New matrix-level observation

Let `A=A0+R` with `A0=A0^T`, `R=R^T`, and let `H` be an ORIGINAL-coordinate set. Then

`A^2=A0^2+(A0 R+R A0)+R^2`,

hence, because `R^2>=0`,

`A^2[H,H] >= A0^2[H,H] - eta_H I_H`,

where

`eta_H := || [ P_H(A0 R+R A0)P_H ]_- ||op`

is the operator norm of the negative part of the localized anticommutator. Therefore if

`lambda_6(A0^2[H,H]) >= g0^2 > eta_H`,

then

`lambda_6(A^2[H,H]) >= g0^2-eta_H`.

This is strictly different from paying `||R||op`: `R` may have arbitrarily large norm. In particular, if `A0 R=0` (orthogonal spectral supports) or more generally `{A0,R}=0`, then `eta_H=0` and every spectral-square carrier certificate of `A0` survives **with zero loss**, regardless of the signs, multiplicities, or magnitudes of all eigenvalues carried by `R`.

This directly matches the natural decomposition of a final symmetric matrix into a selected spectral core plus all remaining eigenmodes: the core and remainder have orthogonal spectral supports, so the remainder is free for any proof branch whose deterministic hypothesis is a lower bound on `A^2`.

## Planned receiver application

Apply the completed partner theorem `QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1` from account02/B12, canonical source

`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T145451Z-account02-B12-QFORM-r36/REPORT.md`.

For a six-eigenmode core `A0=U Lambda U^T`, `|lambda_j|>=s0`, and any original-coordinate carrier `H` with `alpha=s_6(P_H U)>0`,

`A0^2[H,H] >= s0^2 (P_H U)(P_H U)^T`,

so `lambda_6(A0^2[H,H])>=s0^2 alpha^2`. Every orthogonal spectral remainder is therefore absorbed at zero cost, and the partner theorem applies to the actual final matrix with carrier parameter `g=s0 alpha`.

Full QFORM is not claimed: a rank-three spectral core cannot itself provide six nonzero spectral-square carrier modes. The remaining structural bridge is still to obtain an adequate carrier/receiver alternative from only three large final eigenvalues.
