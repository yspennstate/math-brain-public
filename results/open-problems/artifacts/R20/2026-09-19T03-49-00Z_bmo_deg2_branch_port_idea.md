Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# R20 idea before code — degree-two branch graph via four-state chain ports

## Continuity

R20 continues the exclusive Bensmail--Marcille--Orenga Conjecture 2.6 claim `operations/claims/BMO-2025-PUSHING-DELTA.md`. The stale scheduler-title I0100 Paley target is not reopened. Entering metric is `n_all=9`; the previous R20 theorem covers subcubic graphs whose degree-three vertices in the 2-core induce a matching. The next structural frontier is `Delta(C[B])<=2`.

## Fresh route before any validation code

Use Section-B moves **#3 PROVE SOMETHING STRONGER**, **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE**, and **#19 MAKE IT AN ALGORITHM**.

The previous chain rule artificially restricted ports to `{1,2}`. Instead put **every branch vertex at push 3** provisionally and allow the first/last push on each subdivided branch-to-branch chain to lie in `{0,1,2,3}`. If the chain has `k` internal vertices and both branch pushes are 3, then direct calculation suggests the exact transfer law:

- `k=1`: the two port values are the same variable;
- `k=2`: every ordered pair of *distinct* port values is realizable;
- `k>=3`: **every** ordered port pair in `{0,1,2,3}^2` is realizable by a proper internal chain word.

Thus long chains decouple their endpoints completely. The branch problem becomes a finite constraint system on the cubic suppression skeleton. If `D=C[B]` is the graph of unsubdivided branch--branch edges and `P_b` is the sum of port values on subdivided incidences at `b`, then with branch push 3

`Sigma(b)=12+3 d_D(b)+P_b`.

For `Delta(D)<=2`, every branch has at least one port. Direct edges therefore ask only for neighboring values of `3d_D+P` to differ. The only nonlocal chain constraints left are equality on one-internal-vertex chains and inequality on two-internal-vertex chains.

The all-3 ansatz can still fail as a *method*: equality chains can identify port variables at endpoints whose direct-edge sums would otherwise need different values. The next step is not to abandon the port reduction, but to use push 2 as a defect state only where these equality identifications create an obstruction. This should turn the branch problem into a finite-state coloring/automaton on path and cycle components of `D`, with state `(branch push in {2,3}, incident port values)`.

## What to test after this note

1. Prove the chain transfer law on the page, including an explicit construction for `k>=3`, rather than relying on search.
2. Enumerate the finite branch states and transitions for degree-1 and degree-2 vertices of `D`; look for a period-2/period-3 path rule and the smallest odd-cycle defect.
3. Stress-test the state rule on suppressed cubic skeletons with `Delta(D)<=2`, especially cases where one-internal-vertex chains form a matching whose contractions make the all-3 port-coloring highly chromatic.

Any finite search is only a self-check. A theorem claim requires an explicit path/cycle construction or a finite transition lemma proved exhaustively with exact arithmetic and then lifted to arbitrary chain lengths.
