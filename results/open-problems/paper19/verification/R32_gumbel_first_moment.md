# R32 verification - Gumbel first moment and critical overlap guardrails

Date: 2026-06-28.

Target: integrate the pending Gumbel/fluctuation note without overclaiming the
full Poisson law.

Five tool-managed audit agents checked:

- finite-\(m\) hard-edge regular variation at the exponentially small centered
  threshold;
- exact centering, first-moment identities, and Markov bounds;
- factorial-moment and overlap requirements at the centered scale;
- integration location and notation;
- Lean feasibility and the Gumbel sign convention.

Main guardrails:

- The fixed-\(m\), \(t\to0\) expansion alone is not enough when \(m\to\infty\)
  and \(t=e^{-b_m}\).  The integrated text explicitly uses finite-\(m\)
  Gaussian hard-edge regular variation; it also records what follows from only
  the polynomial two-sided bound.
- The full Poisson/Gumbel law is not reduced by the existing bulk problem
  `prob:pc` alone.  At the centered scale, small/intermediate overlap clusters
  are not removed by `prop:small-D-negligible`.  A separate critical Poisson
  overlap condition is stated.
- The Gumbel sign is corrected:
  \[
    P\{\log M_m+b_m\le x\}\to 1-e^{-e^{d_\F x}}
  \]
  is equivalent to
  \[
    P\{-(\log M_m+b_m)\le x\}\to e^{-e^{-d_\F x}}.
  \]
- Lean was left unchanged; the mathematical risk is asymptotic probability and
  overlap control, not finite algebra.

Integrated content:

- `parts/open_problems.tex` now records exact centering, leading centering
  asymptotics, first intensity, one-sided Markov bound, and a critical Poisson
  overlap condition after `conj:gumbel`.
- `parts/ldp.tex` now points to the first-moment result and states that the full
  law requires critical-scale factorial moments.
- `STATE.md` keeps `FLU` as `PARTIAL`, with the full law still conjectural.

Build:

- `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  passed twice.
- Final standalone PDF: 49 pages, 686,844 bytes.
- Log scan found no undefined citations/references and no rerun request. The
  remaining diagnostics are the known `\theHfootnote` warning and the
  pre-existing overfull hbox in `parts/ldp.tex` lines 81--89.
- Lean was intentionally left unchanged.
