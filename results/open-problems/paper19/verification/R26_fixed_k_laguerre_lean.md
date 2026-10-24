# R26 verification - fixed-k Laguerre tail and Lean sign theorem

Date: 2026-06-28.

## Scope

This round used exactly five tool-managed review agents:

1. `019f0c7e-0bdf-7883-979e-f7c56aa65bb2` proved the finite-`m`
   polynomial-loss Laguerre-Selberg tail for the fixed-`k` Gaussian
   one-matrix problem.
2. `019f0c7e-1ee1-79c1-8412-699d1fbba56d` audited fixed-`k` promotion and
   confirmed that the finite-`m` tail is the required guardrail.
3. `019f0c7e-30fc-70f2-9f78-39d8339935c0` identified the fixed-`k`
   finite-budget Gaussian lower side as the strongest safe theorem-quality
   promotion.
4. `019f0c7e-6877-7631-aafb-206817c5aae8` supplied a Lean extension proving
   the arbitrary-`m` sign-frame theorem.
5. `019f0c7e-7d43-7a42-83fb-e46d231ecb28` audited residual notation,
   roadmap, and ledger consistency.

No terminal-launched agents, background daemons, or scheduled tasks were
created.

## Main changes

1. Added `kth:laguerre-tail`, a finite-`m` fixed-`k` Gaussian
   Laguerre-Selberg tail:
   \[
     \PP\{\sigma_{m-k+1}(G)\le t\}
       \le C_{\F,k}m^{B_{\F,k}}t^{d_\F k^2},
       \qquad 0<t\le 1.
   \]
   The proof uses the ordered Laguerre density, separates the first `k`
   eigenvalues from the remaining block, bounds cross terms by powers of the
   large block, and controls the resulting ratio of Laguerre-Selberg
   normalizing constants polynomially in `m`.
2. Promoted `kth:lower`, the fixed-`k` Gaussian finite-budget lower side:
   \[
     \PP\{M_m[k]\le
       \exp[-(\log\binom{N_m}{m}+B_{\F,k}\log m+\log C_{\F,k}+u_m)/
       (d_\F k^2)]\}\le e^{-u_m}.
   \]
   For fixed aspect `N_m/m -> gamma>1`, this proves the lower base
   `h(gamma)/(d_F k^2)`.
3. Kept the exact fixed-`k` extremal law conjectural. The lower side is now
   proved, but the matching upper side still requires a codimension-`k`
   pair-correlation/second-moment theorem.
4. Extended `paper19/lean/SignCritical.lean` to prove the full arbitrary-`m`
   deterministic pigeonhole obstruction `signCritical`, matching
   `prop:sign-critical`.
5. Cleaned notation and roadmap entries: the proportional-excess separation
   constant is no longer `kappa`, Bonferroni row-pair notation uses `I,J`, and
   the fixed-`k` roadmap distinguishes the proved lower side from the exact-law
   gap.

## Verification

Standalone build:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Exit code 0. Final PDF:

```text
paper19/extremal_hard_edge.pdf
40 pages, 612712 bytes
```

Targeted log scan found no undefined citations/references and no rerun request.
The only diagnostics matched by the broad scan were the existing
`\theHfootnote` warning, package `rerunfilecheck` informational lines, and the
existing overfull box in `parts/ldp.tex` lines 81--89.

Lean check:

```text
lean.exe SignCritical.lean
```

with the local Mathlib `LEAN_PATH`, exit code 0.

Process check after Lean verification found no `lean`, `lake`, or `elan`
processes.
