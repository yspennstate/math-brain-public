# PROB10-07 idea note — width-nine complete-tripartite boundary

Runtime request: GPT-6 / maximum reasoning. Authenticated runtime model/effort telemetry is unavailable here, so the eventual report must say `UNVERIFIED` rather than claiming the requested setting.

Parent source: Grimmett–Winkler uniform measure on **all forests** of a finite graph. For distinct edges `e,f`, write `Z,Z_e,Z_f,Z_ef` for the exact forest counts and `Delta=Z_e Z_f-Z Z_ef`. The parent conjecture asks `Delta>=0` for every finite graph. This note does not claim that universal statement.

## Continuity / nonoverlap

The current PROB10-07 theorem covers all complete tripartite `K_{r,s,t}` with sorted part sizes `r<=s<=t` and `r+s<=8`. P14/HARD10-01 own the arbitrary-graph order-nine census and 3-connected/minimal-counterexample history; this iteration does not enumerate graph orders or edit their claims. The historical R13 handoff remains preserved.

## Three materially different attacks considered

### A. Deletion–contraction / closed formula

Use `Z_e(G)=Z(G/e)` and `Z_ef(G)=Z(G/e/f)` and seek a closed formula for the all-forest partition function of complete multipartite graphs and the contracted multigraphs arising from marked edges. This would be conceptually strongest and could remove the fixed-width restriction. The obstruction remains that ordinary matrix-forest determinants naturally count rooted forests, whereas the source gives equal weight to each unrooted forest; contractions also introduce parallel classes. I will not substitute a rooted-forest identity for the source model.

### B. Symmetry quotient of terminal partitions

For the next boundary `r+s=9`, quotient the `B_9=21147` terminal partitions by `S_r x S_s` and, when `r=s`, the part swap. This could make much larger widths feasible. The proof obligation is simultaneous strong lumpability not only of the unmarked fresh-vertex operator but also of every forced-spoke operator needed separately for `Z,Z_e,Z_f,Z_ef`. Unless that is proved exactly, this route cannot certify the Rayleigh differences.

### C. Full Bell transfer at width nine, but with exact sparse preprocessing

Take the four new boundary families

`K_{1,8,n}, K_{2,7,n}, K_{3,6,n}, K_{4,5,n}` (`n>=1`).

Keep the complete Bell state space on the nine fixed terminals. For a fresh third-part vertex, a spoke set is legal iff it hits each current terminal-connectivity block at most once. The unmarked transition therefore has

`M_9 = 10 I + N_9`,

and every `N_9` transition strictly coarsens the terminal partition, hence `N_9^9=0`. A marked edge pair touches at most two repeated-part vertices. Expose those distinguished vertices first with forced-spoke operators. Then every relevant forest count is `10^x` times a polynomial of degree at most eight in `x=n-k`, and every Rayleigh difference is `10^(2x)` times a rational polynomial of degree at most sixteen.

The exact finite certificate will quotient only the **edge-pair list** by graph automorphisms, not the Bell states. For every orbit polynomial I will require a coefficientwise nonnegative monomial expansion plus strict positivity at the first physical integer `x`; that certifies the entire parameter range, not a finite list of `n` values.

To keep the computation bounded, core forests of each fixed `K_{r,s}` will be enumerated once and simultaneously accumulated into the unmarked, single-required-edge, and pair-required-edge terminal-partition vectors used by the orbit representatives. This avoids re-enumerating up to `2^20` core subsets for every marked condition.

## Intended metric movement

If all four boundary families certify, then the structural metric moves

`two smallest complete-tripartite part sizes sum <= 8`

to

`two smallest complete-tripartite part sizes sum <= 9`.

The complete arbitrary-graph order metric stays 9, and the parent remains OPEN/PARTIAL. A failure of coefficientwise positivity will be preserved as an exact obstruction; it will not be hidden by sampling integer `n` values.