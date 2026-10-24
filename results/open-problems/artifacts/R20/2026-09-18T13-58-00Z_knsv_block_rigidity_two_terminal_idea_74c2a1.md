# R20 idea before validation: graphical low-block rigidity + two-terminal attack

Model request in task text: GPT-6 / maximum. Actual runtime model: GPT-5.6 Sol; reasoning telemetry UNVERIFIED.

Current target is the exclusive R20 claim `operations/claims/KNSV-2026-LOOPY-U.md`, not the retired I0100 predecessor. Frozen metric remains `N_sep > 11`.

## Route A — use the graphical origin that Example 9.6 lacks

Section 9.2 writes, for a block `B` of size `s`,

`C_G(B;q) = q^(s-1) A_B(1+q)`

and applies the linear map `T_s(q^(s-1)(1+q)^r)=x_(s-1+r)` block by block. The source's arbitrary-set-function obstruction at profile `(2,2)` uses polynomials that cannot arise from simple 2-vertex induced graphs. Exploit this aggressively.

For a simple graph:

* size 2: `C_B` is either `0` or `q`, so `T_2(C_B)` is either `0` or `x_1`;
* size 3: `C_B` is `0`, `q^2`, or `3q^2+q^3 = q^2(2+(1+q))`, so writing `u=1+q`, every normalized 3-block polynomial is `alpha+beta u` with `(alpha,beta)` in `{(0,0),(1,0),(2,1)}`.

Therefore a profile consisting only of blocks of sizes 1,2,3 should be automatic: after factoring `q^(#2+2#3)`, the coefficient of `u^k` in the ordinary block sum is exactly the coefficient that becomes `x_2^(#3-k) x_3^k` after the blockwise transform, with fixed `x_0` and `x_1` factors.

A second automatic family should be `(s,2^a,1^c)`: after choosing the unique `s`-block, the 2-blocks are simply a matching in the complement of that block, and linearity of `T_s` applies after factoring `q^a`.

If both claims are correct, any genuinely graphical block-transform obstruction must contain one block of size at least 4 and a second block of size at least 3. The minimal nonautomatic profile becomes `(4,3)`, much later than the source's arbitrary-function `(2,2)` example.

At `(4,3)`, write `C_B/q^3 = sum_{j=0}^3 a_j(B)u^j` on the 4-block and `C_C/q^2 = alpha_C+beta_C u` on the 3-block, where `beta_C=1` exactly for triangles. If `s_k` are the known coefficients of the symmetrized ordinary block sum, the only potentially hidden data are the cross-correlations

`h_k = sum_{B disjoint C, C triangle} a_(k-1)(B)`, `k=1,2,3`.

(`h_4` equals the top known coefficient.) This turns the first obstruction into a concrete triangle-versus-4-block activity correlation problem instead of an undirected search over all loopy coefficients.

## Route B — actually leave the one-root architecture at n=12

The previous run proved that the ten-vertex KNSV seed pair has matching one-root U and pointed-L states only at roots 2 and 9, and that all one-root gadgets on up to three new vertices fail. The first qualitatively new finite architecture is two-terminal.

For every unordered pair of old vertices on each seed, compute the exact two-terminal U state: terminal connectivity, terminal component sizes, all other component sizes, and total cyclomatic number. Glue an arbitrary simple graph on those two terminals plus two new labelled vertices. This state is sufficient for exact ordinary-U convolution.

Search the full `n=12` family whose combined old-neighbour support has size at most two, allowing the terminal edge when it is absent from the seed and forbidding duplicate edges when it is already present. Group exact U collisions first; compute `L(1,x)` only for collision-involved graphs using a base-first spanning-forest/activity DP. The attack direction stays the source-prioritized one: `U_G=U_H` but `L_G!=L_H`.

These are methods #15 BREAK THE SYMMETRY, #18 SAY IT IN ANOTHER LANGUAGE, and #25 COUNT THE SAME THING TWICE. No metric movement is claimed before the exact check.