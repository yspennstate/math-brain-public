# Round 044 log

## Goal

Clarify which known cases already satisfy the stronger \(L^2\) target and
remove nonunimodular graphs from the remaining obstruction list.

## Nonunimodular case

For a graph with a nonunimodular quasitransitive automorphism group, let
\(\Delta\) be the modular function and define
\[
  \chi_{p,1/2}=\sum_x \tau_p(o,x)\Delta(o,x)^{1/2}.
\]
The associated threshold \(p_t=\sup\{p:\chi_{p,1/2}<\infty\}\) satisfies
\[
  p_c<p_t
\]
by Hutchcroft's nonunimodular theorem.  Hutchcroft's tilted-to-\(L^2\)
comparison gives
\[
  p_t\le p_{2\to2}.
\]
Consequently,
\[
  p_c<p_{2\to2}
\]
for the whole nonunimodular class.

## Consequence

The genuinely hard residual problem therefore consists of graphs with no
available nonunimodular quasitransitive action.  This is a useful constraint on
future proof attempts: arguments that rely on a global modular height, a tilted
mass-transport principle, or the nonunimodular Hammersley--Welsh method need a
replacement before they can address the remaining general case.

The manuscript now has a dedicated "Nonunimodular transitive graphs" subsection
under known cases and stress tests, and the strategy document records the same
residual-target narrowing.
