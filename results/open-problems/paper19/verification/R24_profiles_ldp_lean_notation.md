# R24 verification: profile budgets, LDP correction, notation, and Lean

Date: 2026-06-28.

## Scope

This round used exactly five tool-managed review agents:

1. fixed-k hard-edge lower-side tail audit;
2. Lean sign-frame feasibility audit;
3. lower-tail LDP construction audit;
4. variance/density-profile theorem search;
5. pruning-notation consistency audit.

No terminal-launched agents, background daemons, or scheduled tasks were created.

## Main changes

1. Added `cor:entrywise-profile-square`, a square row-submatrix lower-side
   finite budget for entrywise density bounds
   `K_{m,i,j}`, using `K_{m,i}^*=max_j K_{m,i,j}`.  This is lower-side only;
   no column averages or exact laws are claimed.
2. Added `cor:rowwise-smoothed-lower`, a row-dependent Gaussian smoothing
   budget for `A_m=F_m+D_mG_m`.  The finite budget is
   `log binom(N_m-1,m-1)+log sum_i sigma_{m,i}^{-d_F}`, with summable
   almost-sure lower-envelope upgrade.
3. Corrected `ldp:lower-construct`: the hole identity is up to the null boundary
   event, the deterministic comparison frame is a sequence `A_{0,m}`, the
   Gaussian ball lower bound is field-uniform, and the conditional lower bound
   keeps the `m^2 log m` term.  The text now says the construction would rule
   out the double-exponential independence prediction only if the bounded
   deterministic frames exist.
4. Cleaned notation against the pruning manuscript: proportional-excess aspect
   `beta` is now `zeta`; pair-correlation row sets use `I,J`; row-weight matrix
   `W_m` is now `D_m^{row}`; smoothed-frame statements include a bridge to the
   prior `W=R+S` signal-plus-noise convention.
5. Added the Marchenko--Pastur citation and cited Rudelson--Vershynin/Tao--Vu
   at the incompressibility route.
6. Extended `paper19/lean/SignCritical.lean` from determinant core to the
   `signCritical_nplus2` finite pigeonhole theorem.

## Deferred item

The fixed-`k` singular-value lower side was not promoted.  The audit found that
promotion needs an explicit finite-`m`, polynomial-loss Laguerre tail bound for
the `k`-th smallest singular value.  The hard-edge exponent alone, or a
Bessel-kernel asymptotic citation alone, is not enough for the exponential
union bound at `t=e^{-s m}`.

## Verification

Standalone build:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
bibtex extremal_hard_edge
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Final log scan: no undefined citations/references and no rerun request.  Remaining
diagnostics are the existing `\theHfootnote` warning and one overfull box in
`parts/ldp.tex` lines 81--89.

Lean check:

```text
lean.exe SignCritical.lean
```

with the local Mathlib `LEAN_PATH`, exit code 0.

Final PDF:

```text
paper19/extremal_hard_edge.pdf
38 pages, 595082 bytes
```
