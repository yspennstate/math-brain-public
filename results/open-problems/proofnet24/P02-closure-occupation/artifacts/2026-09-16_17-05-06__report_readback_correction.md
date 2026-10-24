# P02 2026-09-16 17:05:06 immutable-report readback correction

Canonical report read back at creation commit `cf078f1a1762c7b18cf032287314b3a0ca5ffc68`, blob `a7bdb9c7d9d9f7a6904f0b1631332ddc9c73bb8d`:

`proofnet24/P02-closure-occupation/runs/2026-09-16/2026-09-16_17-05-06__run-report.md`.

The complete readback found one typographical LaTeX error in equation (5.3). The report displays

```tex
d_b=\begin{cases}\nu_b/\pi_b,&b\in A,\\
0,&b\notin A.
\end{cases}
```

The authoritative intended definition is

```tex
d_b=\begin{cases}u_b/\pi_b,&b\in A,\\
0,&b\notin A.
\end{cases}
```

That is, `\nu_b` is a one-character notation typo for the already-defined kernel coordinate `u_b`. The immediately following sentence in the report explicitly uses `u_b=pi_b d_b`, and every subsequent equation uses `u`, so no mathematical claim, proof step, checker, ledger status, metric, or audit count changes.

The immutable report itself is not edited. This file is the authoritative readback correction for that typo.
