# P0282 idea before code — shifted Turán invariants, symmetric-group trace, and double count

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-07`
Canonical claim: `P0282`
Frozen metric on entry: `N_exact = 78`

This note is written before any new checker or computation in this invocation. It records the three fresh routes to test; it is not a claim that any route succeeds.

The previous invocation proved strict Chen log-concavity for every fixed defect `1<=j<=30` and all source-valid `n`, by proving coefficientwise positivity of

`Q_j(m) := D_j(m+2j+1)`,

where

`D_j(n)=(j+1)P_j(n)^2-jP_{j-1}(n)P_{j+1}(n)`

and `P_j(n)=j! ell_{n,n-j}` in the stable fixed-defect range. It also proved that each individual shifted `P_j` has a coefficientwise-nonnegative residual-partition expansion. The open issue is whether the Turán difference itself has a structural positive representation for all `j`, or whether coefficient positivity eventually fails.

## Method #12 — FIND WHAT IS CONSERVED

The residual-partition formula gives

`P_j(n) = (1/j!) sum_{mu|-j} (f^mu)^2 R_mu(n-j)^2`,

with `R_mu` monic of degree `j`, and `sum_mu (f^mu)^2=j!`. Hence `P_j` is monic of degree `2j`; consequently `D_j` and `Q_j` are monic of degree `4j`. This exact leading coefficient `1` is a first invariant. I will derive further top-degree and bottom-degree identities, and inspect normalized coefficient triangles only to discover a candidate invariant that can be proved symbolically.

## Method #14 — FIND THE GROUP ACTING

The weights `(f^mu)^2/j!` are Plancherel measure on irreducible representations of `S_j`. Thus `P_j` is a Plancherel expectation / regular-representation trace of the square of the residual factor `R_mu`. I will try to express `R_mu` through contents, Jucys–Murphy elements, branching on the Young graph, or another central observable. A successful representation should turn the change `j-1,j,j+1` in the Turán expression into induction/restriction or a positive operator statement rather than an accidental polynomial calculation.

## Method #25 — COUNT THE SAME THING TWICE

Expand `D_j` as a double sum over residual partitions. Seek either (i) a direct injection/weight-preserving pairing from the negative `j P_{j-1}P_{j+1}` contribution into `(j+1)P_j^2`, or (ii) a sum-of-squares / covariance identity after rewriting the sums with Young-lattice branching multiplicities. Exact coefficient computation will be used only after these identities are written down, to locate the first obstruction or to certify a widened restricted theorem if the structural route predicts positivity.

Success criteria for this invocation, in descending order:

1. prove an all-`j` positive representation or recurrence for `Q_j`;
2. prove a new unbounded structural lemma that materially narrows the all-`j` obstruction;
3. if the symbolic route stalls, locate the first failing shifted coefficient exactly; if none occurs in a substantially larger exact range, certify the widest source-valid fixed-defect theorem supported by an independently checked finite bridge;
4. only if a separate full-row exact calculation is substantively justified, move the frozen metric `N_exact`; otherwise report `78 -> 78` honestly.

No floating-point sign decision, simulation, external code, or heuristic certificate is admissible.