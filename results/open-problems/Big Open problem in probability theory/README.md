# Big Open problem in probability theory

Started: 2026-06-08

This project is the workspace for the requested long-running attempt to solve a
major open problem in probability theory.

## Selected target

The target selected in round 1 is the Benjamini-Schramm non-uniqueness
conjecture for Bernoulli bond percolation on nonamenable quasi-transitive
graphs, in the stronger operator form
\[
    p_c(G) < p_{2\to 2}(G).
\]

For a connected, locally finite, quasi-transitive graph \(G\), this stronger
inequality implies \(p_c(G)<p_u(G)\), hence gives a non-empty phase with
infinitely many infinite clusters. This is a central problem in modern
percolation theory.

## Why this is not the already-solved local problem

The local solved-problem register in
`~\Open problem project\solved_register.md` concerns Gaussian
phase retrieval, Balan-Wang type stability, Plucker reductions, and related
random-matrix/probability problems. It does not list percolation, nonamenable
graphs, or the Benjamini-Schramm conjecture as solved work.

## Current status

- The problem is verified as still open in the generality targeted here; see
  `research/open_status.md`.
- The current work is not a completed solution. The first paper draft records
  definitions, current literature, a precise operator-theoretic target, and
  proof reductions that will be developed in later rounds.
- The final objective remains active until there is a complete rigorous proof,
  a full LaTeX paper, and a compiled PDF.

## Layout

- `research/open_status.md`: evidence that the selected problem is still open.
- `research/problem_selection.md`: why this target was chosen.
- `research/proof_strategy.md`: proof program and immediate technical tasks.
- `notes/round_*.md`: round-by-round working logs.
- `paper/main.tex`: working LaTeX manuscript.
- `paper/references.bib`: bibliography for the manuscript.
