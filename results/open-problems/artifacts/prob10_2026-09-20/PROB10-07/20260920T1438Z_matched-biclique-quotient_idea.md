# PROB10-07 idea before code — quotient the matched-biclique two-layer algebra

Parent target remains Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests**. This note is only a pre-code mathematical plan. It does not change P14/HARD10-01 ownership or their complete-order-nine census.

## Nonoverlap / consumed boundary

Read before choosing scope: `operations/PROB10_2026-09-20.md`, root `POSTED.md`, P14 mandatory forest handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`, P14 successor handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md`, `operations/claims/G0007.md`, HARD10-01 forest handoff `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`, the preceding PROB10-07 matched-biclique report `runs/prob10_2026-09-20/PROB10-07/20260920T1357Z_matched-biclique-m6-m7-two-nilpotent.md`, and the current NM13-04 triangle/star follow-up `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T13-24-00Z__triangle-star-forest-sign-theorem.md`.

P14/HARD10-01 retain graph-order enumeration and the generic three-separator obstruction. NM13-04 studies `K_3` joined to star forests. This run keeps only the distinct family

`G_m(k,r)=K_{m,2k+r}+M_k`,

where the left part is independent, the right side has `k` disjoint matching edges plus `r` isolated vertices, and every left-right edge is present. No arbitrary-graph census is repeated.

## Three materially different approaches

### A. Stabilizer quotient of the two-nilpotent transfer — primary route

The preceding width-6/7 proof used the full Bell lattice. A marked pair touches at most two left terminals, so quotient terminal partitions by the symmetric group on the other `m-d` terminals, `d<=2`. This should reduce the state count from Bell growth to a partition-number scale and permit substantially larger terminal widths without changing the mathematical certificate.

For a fresh unmatched right vertex let `S=T_empty`; as before `S=(m+1)I+N` with `N^m=0`.

For a fresh matched pair `(u,v)` with internal edge `h=uv`, split the layer exactly by `h`:

- `h` absent: process the `u`-star and `v`-star sequentially, so the transition with forced spoke sets `U,V` is `T_U T_V`;
- `h` present: every currently connected terminal block may be incident to at most one of `u,v`; optional selected blocks have two endpoint choices. Thus the `h`-present transition is a single coarsening operator `H_{U,V}` in which every optional selected block `B` has weight `2|B|`, every forced block has weight one, and any collision of forced labels in the same current terminal block is forbidden.

Therefore the exact marked-pair transition is

`P_{U,V,hforced}=H_{U,V}` if `h` is forced,

and

`P_{U,V}=T_U T_V+H_{U,V}` if `h` is not forced.

In particular

`P=S^2+H_empty=lambda I+Q`, `lambda=m^2+4m+2`.

Because singleton and matched-pair layers use disjoint fresh vertices, `SP=PS`; subtracting scalar diagonals gives `NQ=QN`. Every non-scalar action strictly coarsens the terminal partition, so `Q^i N^j=0` for `i+j>=m`. This gives an exact bivariate polynomial response in residual matched-pair count `x` and residual singleton count `y`.

The goal is to certify every one of the existing 14 marked-edge orbit polynomials by exact rational coefficient signs, now on the quotient state space, and push the width frontier strictly beyond 7.

### B. Quantitative deletion–contraction domination — distinct analytic route

The preceding run proved

`AB Delta_G = B(A+B)Delta_A + A(A+B)Delta_B - E_e E_f`.

A general induction would follow from a sharp inequality controlling `E_eE_f` by the two endpoint gaps. The exact width-6 witness shows endpoint nonnegativity alone is insufficient. In this run I will not recycle that failed implication. A possible future route is a family-specific spectral/response estimate proving

`E_eE_f <= B(A+B)Delta_A + A(A+B)Delta_B`

for one matching-edge deletion/contraction. If the quotient certificate fails at a larger width, the failure polynomial can be used to test whether this domination has any chance of holding there.

### C. Counterexample-first exact arithmetic — falsification route

A negative normalized Rayleigh polynomial at any physical integer `(k,r)` would be an exact counterexample in the original all-forests model. Before interpreting a quotient sign failure as merely a proof failure, evaluate the exact polynomial at its first physical points and, when edge count permits, directly enumerate original edge subsets in a small member of the same family. A verified negative value supersedes all restricted-family proof work.

## Critical claim to falsify before promotion

The key new technical claim is that the quotient is strongly lumpable not only for the singleton star transition but also for the matched-pair `h`-present operator `H_{U,V}`. Its transition weight depends only on current block sizes and which distinguished labels lie in each block: optional selected blocks contribute `2|B|`, forced blocks contribute one, and the target is obtained by merging all selected blocks. If two forced labels lie in one block, the transition is zero. This description is invariant under permutations of undistinguished labels, hence should be strongly lumpable.

The checker must reconstruct these transitions from exact combinatorics, verify `NQ=QN` and mixed nilpotence, classify all 14 pair orbits without residue, and preserve an actual execution transcript. Parent status remains OPEN/PARTIAL unless the universal source problem itself is solved and independently validated.
