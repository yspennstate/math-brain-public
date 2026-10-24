# R08 E0011 idea-before-code — charge balance, parallel-attempt obstruction, and vacancy-seed geometry

Date: 2026-09-19 UTC.

The previous descriptor-carrying fixed-top certificate moved the frozen metric to `B_cat >= b21_desc`, but its probability remains on the `10^-49` scale. This run therefore does not begin by tuning another Bellman constant.

Methods selected from the previous report are B9, B17, B22.

## B17: an exact pathwise charge identity

Let `Q = N_CO - N_O` on any finite protected region, modulo the obvious boundary-flux correction if a reaction crosses its boundary. In the instantaneous-reaction ZGB dynamics:

- each successful CO adsorption changes `Q` by exactly `+1`, regardless of whether the new CO survives or immediately annihilates one O;
- each successful O2 adsorption changes `Q` by exactly `-2`, regardless of the subsequent instantaneous reaction choices.

The reason is that every CO--O reaction removes one particle of each species and therefore leaves `Q` unchanged. Thus, away from boundary flux,

`Q(t)-Q(0) = A_CO(t) - 2 A_O2(t)`.

For any translation-invariant stationary law for which the usual generator/boundary averaging is valid, this suggests the exact density balance

`p rho_0 = (q/2)(rho_00^h + rho_00^v)`.

For a rotation-invariant stationary law, writing `rho_00` for the nearest-neighbor vacant-edge probability,

`p rho_0 = q rho_00`.

At the anchor `p=1/2, q=1`, any nontrivial rotation-invariant active stationary law with positive vacancy density must therefore satisfy `rho_00 = rho_0/2`. This is a structural target for a density/block argument, not a coexistence proof.

## B9: try genuine repetition rather than another rare word

A naive spatial repetition of the current exact-seed certificate does not amplify its probability: if the parent seed is replaced by `N` disjoint exact seed copies and the outgoing seed must again contain `N` exact copies, independent replication asks all `N` copies to branch and multiplies probabilities. The union event “at least one copy branches” would amplify, but its successful child location is random and therefore does not reproduce the same frozen exact seed pattern. The exact-seed quantifier is the obstruction.

A route with a chance to amplify must instead use a *seed class* / density pile with a restart or minorization property, or a different source-valid coexistence argument outside the current exact-seed metric.

## B17 numerical geometry test

The previous width calculation only tracked one direct failure mode: starting from an all-vacant `2 x w` rectangle, all vacancies can be filled by CO before the first effective O2 adsorption. There is a symmetric-looking but distinct second direct poison route: O2 dimers can cover the whole vacancy seed before any effective CO adsorption.

For a finite vacancy set `S`, let `e(S)` be its number of vacant-vacant nearest-neighbor edges. Exact exponential-race recurrences are

`q_CO(empty)=1`,
`q_CO(S)= [2/(2|S|+e(S))] sum_{v in S} q_CO(S\{v})`,

and

`q_O(empty)=1`,
`q_O(S)= [1/(2|S|+e(S))] sum_{uv in E(S)} q_O(S\{u,v})`.

These events are disjoint direct monochromatic-poison histories. I will compute both exactly for small rectangles and compare `q_CO+q_O` with the entire `1/64` failure budget. The question is whether a more isotropic vacancy seed beats the old `2 x 8` geometry and whether the first useful rectangular scale can be reduced.

## B22: what the nearest solved route has that zero stirring lacks

Durrett's source separates Problem 5 from the fast-stirring theorem. The fast-stirring proof obtains a high-probability pile-to-pile block event through convergence to a reaction-diffusion PDE and traveling-wave propagation. The no-stirring target has no such local smoothing theorem. That difference matches the current computation: exact prescribed Harris cylinders can be certified, but their probabilities remain microscopic. The next useful architecture should therefore seek a robust density pile / restart mechanism, not another prescribed word.