# PROB10-07 idea before persisted checker — repair the complete-tripartite transfer

Parent target: Grimmett–Winkler pairwise negative edge correlation for the uniform measure on **all forests** of a finite graph. Parent status remains OPEN/PARTIAL. This scope does not touch P14/HARD10-01 complete graph-order enumeration.

## Integrity obligation from the preceding run

The 10:38Z PROB10-07 report found that the earlier complete-tripartite checkers mishandled distinguished vertices in the repeated third part. If the full marked pair touches repeated-side vertices `R`, the residual exponent is `x=n-|R|`; therefore every vertex of `R` must be processed in every one of the four conditioned counts `Z,Z_e,Z_f,Z_ef`. A distinguished repeated-side vertex carrying no forced marked spoke in a given condition contributes the ordinary unmarked transition `M`, not the identity.

The corrected formula must be

`v_C = core_C * prod_{r in R} T_{S_r(C)}`,

with `T_empty=M`, followed by

`Z_C(n)=v_C M^(n-|R|) 1`.

This is the first obligation of this run: either restore or retract the earlier tripartite all-`n` claims using the corrected formula.

## Three materially different routes considered

### A. Corrected marked-vertex exposure (chosen)

Keep the Bell-partition transfer for the fixed `K_{a,b}` core, but expose the full set `R` of third-part vertices touched by the pair before applying the residual power. For every conditioning event, process all of `R`; use a forced-spoke operator when required and `M` otherwise. Since `M=(a+b+1)I+N` with `N^(a+b)=0`, every conditioned count is still exactly `(a+b+1)^x` times a polynomial in `x`, and each Rayleigh difference has an exact finite polynomial certificate on the full `n>=1` range.

Critical falsification check: on every family, compare the corrected transfer against direct original-edge-subset enumeration for small `n`, including pair orbits touching two distinct repeated-side vertices. This is the orbit type that exposed the preceding omission in the split computation.

### B. Deletion–contraction in the third-part vertex

For a marked pair `e,f`, expand `Delta=Z_e Z_f-Z Z_ef` by deleting/contracting all spokes incident to one repeated-side vertex. This gives exact identities but produces mixed polarization terms analogous to the P14/HARD10 three-terminal obstruction. Endpoint Rayleigh signs alone do not control these mixed terms. This route is not chosen because it risks reproducing an already documented obstruction rather than repairing the concrete transfer defect.

### C. Component exponential formula

A tree component with `q>=1` vertices from the first two parts and `r` vertices from the repeated third part can be counted by complete-multipartite tree formulas; one can in principle build marked-edge exponential generating functions and compare the four coefficients entering `Delta`. This may lead to an all-width theorem, but the two-marked-edge component types are substantially more involved. It is retained as the next method if coefficient positivity breaks after the corrected transfer.

## Exact scope attempted

Re-run the complete-tripartite chain already claimed earlier, but now with the corrected exposure rule, for all sorted fixed pairs `(a,b)` with `a+b<=9`, namely

`(1,2); (1,3),(2,2); (1,4),(2,3); (1,5),(2,4),(3,3); (1,6),(2,5),(3,4); (1,7),(2,6),(3,5),(4,4); (1,8),(2,7),(3,6),(4,5)`.

For each family `K_{a,b,n}`, exhaust all edge-pair symmetry orbits, derive the exact normalized Rayleigh polynomial, require coefficientwise nonnegativity in ordinary powers of the physical shifted variable `x=n-|R|`, and require strict positivity at the first physical integer. Then independently brute-force small original graphs with a checker that does not use the transfer formula.

Success criterion: restore the theorem `a+b<=9` under a corrected checker and explicit proof, or identify the first exact failing orbit/polynomial and retract the affected range.