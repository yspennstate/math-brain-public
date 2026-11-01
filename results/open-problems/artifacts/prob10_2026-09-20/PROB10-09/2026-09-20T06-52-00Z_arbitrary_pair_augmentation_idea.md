# PROB10-09 idea before code — robustness under arbitrary added generator pairs

Runtime model metadata: GPT-5.6 Sol; reasoning effort UNVERIFIED. GPT-6 maximum was requested in the task text, but the scheduler exposes no authenticated model/effort selector or per-run effort receipt.

## Frozen parent target

For iid bond percolation on every locally finite Cayley graph of every finitely generated nonamenable group, prove `p_c(G) < p_u(G)`. This note is only a restricted-family attack and cannot close the parent conjecture.

## New route

Continue the central-surface-extension operator lane from the previous PROB10-09 run, but do not merely change the central exponents of the standard horizontal generators: those central slants can be induced by automorphisms and would not genuinely enlarge the graph class.

Instead, let

`E_{g,e}=<a_1,b_1,...,a_g,b_g,z | z central, prod_i [a_i,b_i]=z^e>`, `g>=3`, `e != 0`,

and begin with the standard symmetric generating set

`S_0={a_i^{+/-1},b_i^{+/-1}:1<=i<=g} union {z^{+/-1}}`.

Adjoin *arbitrary* additional inverse-pairs

`{c_1^{+/-1},...,c_k^{+/-1}}`,

with no repetitions or collisions with `S_0`, and write `S` for the resulting symmetric set. The candidate theorem is that every such augmentation with `0 <= k <= g-2` still has a strict Bernoulli bond-percolation nonuniqueness phase.

The reason this may work is asymmetric robustness of the two sides:

1. The old embedded `F_{2g-1} x Z` subgraph survives after adding edges, so an upper bound for `p_c` survives unchanged. I will sharpen this side to the exact uniform strict inequality `p_c < 1/(4g-2)` using the full vertical-Z fibre cluster pgf rather than a finite truncation.
2. Each arbitrary new inverse-pair increases the adjacency-operator norm by at most `2`. The central Fourier/diamagnetic estimate therefore changes from `||A|| <= 4 sqrt(g)+2` to `||A|| <= 4 sqrt(g)+2+2k`. The nonbacktracking/two-point transfer can tolerate a finite amount of this perturbation.
3. The exact margin calculation appears to tolerate every `k <= g-2` for all `g>=3`, giving a genuinely broader collection of Cayley graphs, not an isomorphic reparametrization of the old one.

## Negation test before coding

The obvious stronger claim, allowing arbitrarily many added generators, cannot follow from this norm argument: every added pair costs up to `2` in the operator bound while the `p_c` witness is fixed. Thus the method itself predicts a finite robustness radius and gives a falsifiable inequality for its scope.

A second alternative is to add a second independent central direction and use an `F_r x Z^2` fibre witness. Preliminary hand analysis shows this could be stronger geometrically, but it requires an exact finite reliability/cluster computation in `Z^2`; a numerical Monte Carlo crossing would not be an admissible certificate. I therefore keep that as a separate failed-for-now route rather than promote numerics.

## Intended exact checkpoint

For the concrete first new subfamily `g=3, k=1`, the target certificate is

`p_c < 1/10 < 1/(2+2 sqrt(3)+sqrt(1+8 sqrt(3))) <= p_{2->2} <= p_u`,

so the auxiliary gap lower bound should be

`delta = 1/(2+2 sqrt(3)+sqrt(1+8 sqrt(3))) - 1/10 > 0`.

Only after this idea is written will I run exact checks of the algebra and save code/output.