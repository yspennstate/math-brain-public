# C04.12 clarification — stationary increments, not stationary positions

This immutable clarification applies to Theorem C04.12 in

`research7_2026-09-17/R7-05/runs/2026-09-20/2026-09-20T083200Z__report.md`.

The phrase "stationary ergodic process `(Y_n)`" there should be read precisely as follows:

> There exists a two-sided **stationary ergodic increment process** `(xi_n)_{n in Z}`, with `xi_n in {-1,+1}`. Define the position process by `Y_0=0` and `Y_n=sum_{k=1}^n xi_k` for `n>0` (and analogously for negative `n`). Then `Y_n/n -> v_*>0` a.s., while the future backward depth from the stationary time origin has the stated heavy lower tail.

The position process itself is of course not stationary when it has nonzero speed. The equilibrium-renewal construction, renewal-reward computation, and lower bound

`P(R_0>=L) >= E[(B-L+1)_+]/E(2B+1) asymp 1/log L`

are unchanged. The theorem's intended obstruction is therefore a stationary-ergodic **bounded-increment / regenerative** countermodel, not a stationary position process.

No source-level RWRE claim is changed: this remains an abstract obstruction and not a counterexample to P0487.
