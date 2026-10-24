# PROB10-10 idea before code — asynchronous boundary carry instead of first-hit reset

Frozen source target: nearest-neighbor UNDIRECTED FPP on `Z^2` with iid `Exp(1)` physical-edge weights; canonical source defect `Delta_12=2 mu(e1)-mu(1,1)`, current proved `c_*=0`.

The 10:18Z run proved a moving-centered diagonal-slab compiler, but it throws away all terminal labels except the first hit and pays a `sqrt(N)` recentering correction. That reset is mathematically clean but numerically expensive: to beat the retained axis lower bound `mu(e1)>=0.3002823`, it needs one finite block with `q_{L,W}/L<0.6005646`.

## New route

Do **not** synchronize or recenter after each block. Partition the diagonal strip into fresh disjoint `s=x+y` bands of thickness `2L`. Carry the complete vector of terminal arrival-time offsets across the shared antidiagonal. A block is therefore an iid random min-plus operator on the asynchronous boundary vector.

For a boundary vector `z`, let `F_omega(z)` be the vector of shortest block-restricted passage times to the next boundary, using all undirected edges inside that fresh band. Normalize by

`g(z,omega)=min F_omega(z)`, `Phi(z,omega)=F_omega(z)-g(z,omega)`.

Then the admissible restricted path cost satisfies exactly

`M_{j+1}=M_j+g(Y_j,omega_j)`, `Y_{j+1}=Phi(Y_j,omega_j)`.

This is a different mechanism from the previous first-terminal reset and from the retired fixed-corner blocks: it preserves the asynchronous labels that the 02:18Z synchronization-obstruction report identified as the information that must not be discarded.

The intended rigorous certificate is an average-cost Bellman supersolution. If a lower-bounded potential `h` satisfies

`E[g(y,omega)+h(Phi(y,omega))]-h(y) <= lambda`

for every reachable normalized boundary state, then telescoping should give

`mu(1,1) <= lambda/L`

with an explicit finite-`N` error of order `1/N`, namely `(h(y0)-inf h + W)/(LN)` after the final fresh staircase correction. Therefore `lambda/L<0.6005646` would move the canonical source defect positive immediately.

## Negation-first test to run

Before attempting any rigorous state-space certificate, test whether the asynchronous carry has enough quantitative room. Simulate the exact block-restricted min-plus recursion, not the unrestricted lattice and not a finite-size curvature fit. Compare widths around the source threshold. If even width 30--40 remains above `0.6005646`, abandon this route and return to P20's Busemann/HJB disagreement compiler. If it screens below, the next mathematical target is a rigorous Bellman/rounding certificate for this **restricted** process.

## Three materially different routes considered this run

- **B2 — attack the negation:** try to falsify the hypothesis that asynchronous carry can cross `0.6005646`; width-sweep the exact restricted dynamics numerically.
- **B11 — dualize:** convert the carried min-plus dynamics into an average-cost Bellman supersolution inequality, so the source-facing upper bound is a uniform drift certificate rather than a finite-size fit.
- **B19 — make it an algorithm:** express each fresh band as a multi-source shortest-path operator and propagate the whole terminal offset vector. This exposes precisely what must be certified and avoids the old synchronization loss.

Two alternatives are deliberately not selected as the main route: (i) P20's residual/Busemann lane still lacks a path-unavoidable lower bound on disagreement energy above its finite-to-infinite error; (ii) more first-moment self-avoiding-path tuning cannot reach the diagonal at the current axis cap because of the exact monotone-path barrier proved at 10:18Z.

No theorem or source movement is claimed in this idea note. The proof obligation is to establish the carry compiler carefully, test its negation, and state exactly what finite/analytic certificate would turn it into a positive `Delta_12` bound.