# R20 idea before code — port the KNSV multigraph witness through two-terminal transfer states

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

Current exclusive target remains `operations/claims/KNSV-2026-LOOPY-U.md`; retired I0100 is not reopened.  The fixed source metric is `N_sep>11` until an exact simple U/L separator is found.

The preceding stuck report isolated the missing ingredient: the KNSV five-vertex loopless multigraph counterexample has four excess parallel-edge copies, and path-only simpleification at total order 12 destroys ordinary-U equality.  The next route should preserve the multigraph mechanism at the level of **two-terminal transfer states**, not literal paths.

Idea: keep the six-edge simple support from KNSV Example 8.11.  Replace each of the four excess parallel copies by an internally vertex-disjoint connected simple two-terminal network with no terminal edge.  Distribute exactly seven internal vertices among the four networks, so the resulting simple graphs have order 12.  For a network, quotient all labelled realizations by the exact boundary state obtained by summing over edge subsets and recording: whether the terminals are connected; how many internal vertices attach to each boundary component; sizes of closed internal components; and selected-edge count.  This state is sufficient to glue networks exactly into the fixed five-vertex support and recover the ordinary U-polynomial over Z.

Why this is genuinely new: a path is only one boundary-transfer type.  Networks with branching or local cycles can redistribute cyclomatic mass while compensating component-size data, which is the mechanism the multigraph witness has and path subdivision lacks.

Research order for this run:

1. derive and self-check the exact sufficiency/gluing rule for the two-terminal state;
2. enumerate the state quotient for 1,2,3,4 internal vertices (the only sizes needed by positive compositions of 7 into four parts);
3. search the full quotient family for a cross-side ordinary-U collision at n=12;
4. only if a U-collision exists, reconstruct representative simple graphs and test the previously isolated hidden `(h1,h2,h3)` statistic / full `L(1,x)` exactly;
5. if no collision exists, record a route-level no-go theorem for this entire network-replacement family, not a general `N_sep>12` claim.

Planned Section-B moves for the substantive run: **#10 DERANDOMIZE** (replace graph-level brute force by a finite exact transfer quotient), **#18 SAY IT IN ANOTHER LANGUAGE** (two-terminal network algebra), **#25 COUNT THE SAME THING TWICE** (validate the transfer gluing against direct U on sampled representatives).
