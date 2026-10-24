# PROB10-07 idea note — tripartite fixed-width six

Runtime request: GPT-6 maximum. Authenticated model/effort telemetry is unavailable here, so the eventual report must state runtime metadata as UNVERIFIED unless separately authenticated.

Parent source: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests** of an arbitrary finite simple graph. P14/HARD10-01 retain the complete-order-nine / minimal-counterexample history. This note takes a complementary fixed-core structural-transfer route and does not repeat graph-order enumeration.

Immediate predecessor: `runs/prob10_2026-09-20/PROB10-07/20260920T0436Z_tripartite-sum5-5c91.md`, which proves strict p-NC for every complete tripartite `K_{a,b,c}` whose two smallest part sizes sum to at most five. Its stated next width layer is exactly `K_{1,5,n}`, `K_{2,4,n}`, `K_{3,3,n}`. Repository search before this note found no competing claim for those three families. The newest NM13-04 forest theorem concerns `K_3 \vee (pP_3 \sqcup mK_2 \sqcup rK_1)` and is structurally different.

## Three materially different attacks compared before production code

### Route A — deletion/contraction to a complete-multipartite closed formula

For distinct tested edges `e,f`, use `Z_e=Z(G/e)` and `Z_{ef}=Z(G/{e,f})` in graphic-matroid language, aiming to reduce the Rayleigh difference to explicit all-forest counts of contracted complete multipartite graphs. This is attractive because only finitely many pair orbits occur. The obstruction is that contractions create parallel classes / identified part vertices, while no source-checked closed formula for the **unrooted all-forest** partition function of all such contracted multigraphs is available in the current chain. The matrix-forest determinant counts rooted forests and does not directly substitute for `Z`. Do not promote this route without deriving the missing unrooted formula.

### Route B — quotient the Bell transfer by `S_a x S_b`

The repeated third-part vertices see only the connectivity partition of the `m=a+b` fixed terminals. Since the fixed core is `K_{a,b}`, one can lump set partitions into orbits under `S_a x S_b` (and part swap when `a=b`). This should reduce the `B_m` state space and is the right route for widths beyond six. The nontrivial obligation is to prove strong lumpability for every marked-edge initial condition, not only for the unmarked transfer. That proof is not needed at `m=6`, where `B_6=203` is still small enough for an exact full-state computation.

### Route C — full exact Bell transfer at width six

Use the predecessor's exact transfer directly for `m=6`. For a processed forest inducing terminal partition `pi`, a new repeated vertex may choose a spoke set `S` iff `S` meets every block of `pi` in at most one terminal; legal `S` merges the blocks it meets. Therefore `M_6=7I+N_6` with `N_6^6=0`. Exposing the at most two repeated vertices carrying a marked edge pair gives four initial vectors `v_0,v_e,v_f,v_ef`; every count is `7^x` times a degree-at-most-five rational polynomial in `x`, and every Rayleigh difference is `7^{2x}` times a degree-at-most-ten exact rational polynomial.

The target finite certificate is: generate all edge-pair orbits for `(a,b)=(1,5),(2,4),(3,3)`; reconstruct the marked vectors by exact forest enumeration; prove every physical Rayleigh polynomial is positive for all integer `x>=0` by a nonnegative-coefficient certificate; and independently regress the original all-forests counts at `n=1,2` for every actual edge pair.

If Route C succeeds for all three families, then together with the predecessor theorem it proves strict p-NC for every complete tripartite `K_{a,b,c}` whose two smallest part sizes sum to at most six. The arbitrary-graph source conjecture remains OPEN/PARTIAL and the complete-order metric remains 9.