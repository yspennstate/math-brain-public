# PROB10-07 idea before code — two commuting nilpotents for matched-biclique layers

Parent target: Grimmett–Winkler pairwise negative correlation for the uniform measure on **all forests** of an arbitrary finite graph. Parent status remains OPEN/PARTIAL unless a source-valid counterexample or full proof is obtained.

## Ownership/nonoverlap checked before scope

This route does not touch P14/HARD10-01's complete graph-order census or their 3-connected minimal-counterexample claim. It also does not repeat NM13-08's three-terminal theorem `G_{k,r}=K_{3,2k+r}+M_k`: the proposed new scope has **four or five fixed terminals**, and the algebraic mechanism changes at terminal width four.

Candidate family: for `m in {4,5}`, `k>=1`, `r>=0`, let

`G_m(k,r) = K_{m,2k+r} + M_k`,

where `M_k` is a matching on `2k` vertices of the right part and there are no other right-right edges. The target is strict unit-weight Rayleigh positivity for every distinct edge pair, uniformly in both parameters.

## Three materially different approaches

### A. Extend the one-generator `K_3` layer algebra — falsify first

For one right vertex let `S_m` be its terminal-partition transfer and `N_m=S_m-(m+1)I`. For one matched pair of right vertices plus their internal matching edge let `P_m` be its transfer. NM13-08 has, at `m=3`, a special identity putting `P_3` in the one-generator algebra `Q[N_3]`.

Test whether `P_m=sum_{j=0}^{m-1} c_j N_m^j` persists. It does **not** already at `m=4`: the exact linear system for `(c_0,...,c_3)` has no solution. Thus simply extending the old one-generator argument is blocked by an exact algebraic obstruction.

### B. Two-generator commuting nilpotent algebra — chosen

Disjoint fresh layers may be processed in either order, so `S_m P_m=P_m S_m`. Their diagonal entries are constant:

- `S_m=(m+1)I+N_m`;
- `P_m=lambda_m I+Q_m`, with `lambda_m=m^2+4m+2`.

The formula for `lambda_m` is direct: without the internal matching edge, `(m+1)^2` choices leave terminal connectivity unchanged; with the internal edge present, only the internal edge alone or it plus one spoke are acyclic without merging terminal blocks, contributing `1+2m`.

Both `N_m` and `Q_m` strictly coarsen the terminal partition whenever they act nontrivially. Hence every word of total length at least `m` vanishes. Since they commute,

`P_m^x S_m^y = lambda_m^x (m+1)^y sum_{i+j<m} binom(x,i) binom(y,j) lambda_m^{-i}(m+1)^{-j} Q_m^i N_m^j`.

This gives an exact bivariate polynomial response for arbitrary numbers of unmarked matched-pair and singleton layers, without requiring `P_m` to be a polynomial in `N_m`.

For a marked edge pair, expose all one or two layers touched by the full pair in **all four** conditioned counts (`0,e,f,ef`), using the unmarked transfer when a distinguished layer carries no forced edge. If `a` matched layers and `b` singleton layers are distinguished, put `x=k-a`, `y=r-b`. After the positive factor `lambda_m^{2x}(m+1)^{2y}` is removed, each Rayleigh difference is an exact polynomial `R(x,y)`. The automorphism group leaves fourteen edge-pair templates, exactly as in the three-terminal matched-layer problem. The intended certificate is coefficientwise nonnegativity in the shifted physical variables `x,y>=0`, with positive constant term whenever the orbit exists.

This is the main route to implement and falsify.

### C. Delete/contract the internal matching edges

Deleting all matching edges gives the already understood complete bipartite graph. Contracting one matching edge produces a fused right vertex with doubled parallel incidence to the left terminals. Expanding the Rayleigh difference in one matching-edge activity gives positive endpoint terms but an uncontrolled mixed polarization term, analogous to the P14 environmental-covariance obstruction. Unless the special biclique symmetry gives a new sign identity, this route does not presently close the family. Keep it as a structural comparison, not as the main calculation.

## Falsification conditions for Route B

The candidate theorem fails if any of the following occurs in exact arithmetic:

1. `S_m` and `P_m` fail to commute;
2. `N_m^i Q_m^j` is nonzero for some `i+j>=m`;
3. the fourteen orbit list is incomplete under `S_m` terminal symmetry and layer permutations;
4. any shifted normalized Rayleigh polynomial has a negative coefficient or is nonpositive at a physical integer point;
5. direct edge-subset enumeration of small original-model instances disagrees with transfer counts.

Only if all checks pass will this be promoted to a restricted theorem. No claim is made here.