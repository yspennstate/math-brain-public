# Round 001 log

Date: 2026-06-08

## Actions

- Inspected the existing local open-problem project.
- Found that the already-solved local work is phase retrieval/RMT/Balan-Wang
  related, not percolation.
- Verified current external literature around the Benjamini-Schramm
  percolation conjecture.
- Created the project `~\Big Open problem in probability theory`.
- Started a LaTeX manuscript and bibliography.
- Compiled `paper/main.pdf`; current draft is 11 pages.  It is a working
  manuscript, not the final solved-problem paper.

## Selected target

The project targets the stronger \(L^2\) form of the Benjamini-Schramm
non-uniqueness conjecture:

\[
    p_c(G)<p_{2\to 2}(G)
\]

for every connected, locally finite, quasi-transitive, nonamenable graph.

## Current mathematical state

No full solution yet. The main line is to turn a failure of Hutchcroft's
finite-set escape criterion into almost-invariant finite sets for the graph,
contradicting nonamenability.

## Next round

The next useful piece is the failure-extraction lemma:

If finite-set escape fails, construct \(p_n\uparrow p_c\), finite sets \(K_n\),
and normalized indicators \(f_n\) for which
\[
    \langle f_n, Q_{p_n} f_n\rangle \ge \epsilon,
    \quad Q_p=T_p/\bar\chi_p.
\]

Then try to convert this into a graph-isoperimetric contradiction.
