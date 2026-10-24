# Round 022 log

Date: 2026-06-08

## Focus

Pushed the exact finite-length SAW operator computation one step further for
\(T_3\square\mathbb Z\).  The direct labelled-tree DFS reaches length \(14\) but
stalls at length \(15\), so I replaced it with a quotient-state dynamic program.

## Quotient-state enumeration

A state records the finite rooted tree of visited fibers, decorated by:

- the set of visited heights in each fiber;
- the unique current fiber and current height.

Children are treated as unordered.  When the walk moves to a new child fiber,
the transition carries the correct multiplicity of unused tree slots: \(3\) at
the root and \(2\) at every other tree vertex.  Moves to existing parent or
child fibers and vertical moves are then deterministic once the target visited
height set is checked.

This quotient still counts labelled self-avoiding walks exactly.  The endpoint
totals remain divisible by the tree-sphere sizes, giving the same coefficients
\(a_{r,h}^{(m)}\) used in the spherical transform formula.

## New exact bound

The quotient computation reaches \(m=15\).  For \(T_3\square\mathbb Z\),
\[
  \|C_{15}\|_{2\to2}
  =
  134618428+95108784\sqrt2,
\]
and hence
\[
  \|C_{15}\|_{2\to2}^{1/15}\le 3.647512.
\]

This improves the previous finite-length value \(3.657847\) at \(m=14\), but it
is still far above the current target \(200/61\approx3.27869\) coming from the
interval-branching \(p_c\) bound.

The computation is now reproducible with
`scripts/saw_quotient_bound.py --degree 3 --length 15 --progress`.

## Interpretation

The exact roots are decreasing:
\[
  3.683286,\quad 3.669978,\quad 3.657847,\quad 3.647512
\]
for \(m=12,13,14,15\).  The decrease is too slow for brute-force
submultiplicativity to be a plausible closure mechanism by itself.  The next
SAW-side step should be an asymptotic finite-memory or structural bound that
captures repeated line/tree commutation obstructions uniformly in \(m\), rather
than another one-step extension of the exact enumeration.
