# Problem selection memo

## Requirement mapping

The user requested:

- an open problem in probability theory;
- not the open problem already solved in the local project;
- verified still open;
- known and interesting enough that a solution would impress mathematicians;
- a route toward a paper in LaTeX and PDF form.

## Selected problem

I selected the Benjamini-Schramm non-uniqueness conjecture for Bernoulli bond
percolation on nonamenable quasi-transitive graphs:

\[
    p_c(G)<p_u(G)
    \quad\text{for every connected, locally finite, quasi-transitive,
    nonamenable graph }G.
\]

The working project targets the stronger \(L^2\) version:

\[
    p_c(G)<p_{2\to 2}(G).
\]

Here \(p_{2\to 2}\) is the threshold at which the two-point function
\(T_p(x,y)=\mathbb P_p(x\leftrightarrow y)\) ceases to be bounded as an
operator on \(\ell^2(V)\).

## Why this target

- It is a genuine probability/percolation problem, not merely a combinatorial
  reformulation.
- It is famous enough to be recognized by percolation experts.
- It has a mature body of partial results: planar nonamenable graphs,
  hyperbolic quasi-transitive graphs, nonunimodular graphs, products, Kazhdan
  groups, and subgroup-relativization classes.
- The stronger \(p_c<p_{2\to 2}\) formulation gives a concrete analytic target:
  prove \(L^2\)-boundedness of the subcritical two-point operator beyond
  \(p_c\), or verify Hutchcroft's finite-set criterion near criticality.

## Known solved local work avoided

The existing local solved register identifies phase retrieval, Gaussian
minimum laws, and Plucker/Balan-Wang reductions. This percolation problem is
not in that solved list.

## Scope risk

This is a very hard problem. A complete proof cannot be honestly asserted until
the missing nonamenable-to-finite-set-escape implication is proved or a new
argument bypasses it. The project therefore starts with proof infrastructure
and a paper draft, and the goal remains active.

