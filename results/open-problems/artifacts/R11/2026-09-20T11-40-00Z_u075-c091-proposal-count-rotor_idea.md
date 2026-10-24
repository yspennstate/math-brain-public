# R11 / I0054 idea note — proposal-count rotor before code

Model requested by owner: GPT-6 maximum. Actual runtime: GPT-5.6 Sol; reasoning level UNVERIFIED.

Methods selected from the preceding handoff: **#10 DERANDOMIZE, #22 READ THE FAILURES, #28 REPLACE FOR ALL WITH TYPICAL**.

## Starting point

The preceding run proved U073: at each active harmonic proposal, an independent uniform cyclic dither `J in Z/d_N` kills arbitrary compact-logit aliasing, for arbitrary branch counts `b_N`, giving whole-path CTCS(infinity) convergence with error `O(1/d_N+1/N)`. The new goal is to eliminate that fresh dither draw without returning to a previously exhausted deterministic-rotor class.

A rotor advanced only at active proposals fails as a route: the active proposal rate is asymptotically constant (`W_N -> log 2`), so on a fixed time interval only `O(1)` active marks occur and a rotor with `d_N -> infinity` does not sample its cycle. A random initial phase plus deterministic active-step rotation also does not solve the correlation problem: finitely many active phases remain almost frozen as `d_N -> infinity`.

The successful observation is that the **total** harmonic proposal rate is `H_{N-1} ~ log N`, whereas the active-window rate is only `W_N -> log 2`. Therefore the already-existing raw proposal marks can drive the rotor quickly even though visible active proposals remain rare.

## Candidate U075

For each current nonsingleton clade, attach a rotor phase `R in Z/d_N`. The phase is inherited by both children when the clade splits. Every harmonic proposal, active or inactive, deterministically advances

`R <- R+1 mod d_N`.

For inactive marks, keep the source harmonic paintbox bias `s/N`. For an active mark `s/N in I=[1/2,4/5)`, use the compact-logit bias

`p = sigma( L * { b_N alpha_{N,s} + R/d_N } )`,

where `L=log 4`, `alpha_{N,s}=logit(s/N)/L`, and `b_N` is an arbitrary positive integer. Colors remain iid Bernoulli(p), as in the preceding compact-logit classes. There is **no fresh random dither variable**.

The proposal clocks are the usual independent Poisson clocks of rates

`lambda_{N,s}=N/[2 s(N-s)]`.

Hence a live clade has total raw proposal rate

`H_{N-1}=sum_s lambda_{N,s}`

and active-window rate

`W_N=sum_{s in S_N} lambda_{N,s} -> log 2`.

Let `q_N=W_N/H_{N-1}`. Between successive active proposals on a carrier lineage, the number `K` of all raw proposals is geometric with success probability `q_N`, independent of the active mark itself. Thus the active-phase transition is

`R' = R + K mod d_N`.

For residues `r=1,...,d`,

`mu_q,d(r)=q(1-q)^{r-1}/[1-(1-q)^d]`.

If `q d <= 1`, Bernoulli's inequality gives

`1-qd <= d mu_q,d(r) <= 1/(1-qd/2)`,

hence

`||mu_q,d-Unif(Z/d)||_TV <= qd/2`.

This bound is uniform in the incoming rotor phase.

Therefore the active-phase chain can be coupled to the iid-uniform dithers of U073 with mismatch probability at most `qd/2` per active proposal. On a fixed visible restriction `[k]`, at most `k` carrier blocks exist and each has active proposal rate `W_N`, so the expected number of active proposals by time `T` is at most `k W_N T`. The total rotor-vs-fresh-dither path mismatch is therefore

`<= k W_N T * q_N d_N / 2 = O_{k,T}(d_N/H_{N-1})`.

Combining with the U073 fresh-dither-to-CTCS estimate gives the candidate theorem

`TV(path_Rotor^[k], path_CTCS^[k]) <= C_{k,T}(1/d_N + 1/N + d_N/H_{N-1})`.

Thus any

`d_N -> infinity`, `d_N/H_{N-1} -> 0`

works, uniformly for **arbitrary branch counts b_N**. The balanced choice is `d_N ~ sqrt(log N)`.

The phase-inheritance rule is essential for exact restriction consistency: an invisible hidden-only split must not reset the phase. Every proposal increments the phase before any split; both children inherit that updated phase. After restriction, a hidden-only split is therefore indistinguishable from a null visible proposal followed by a memoryless restart of the Poisson clocks.

## Candidate C091

Take

`d_N=max(2,floor(sqrt(log_2 N)))`

and the same deliberately huge branch schedule as C090,

`b_N=1` for `N<=4`, and `b_N=2^(2^(N-4)-1)` for `N>=4`.

At `N=4`, `d_4=2`, `b_4=1`. The embedded mark probabilities are `(4/11,3/11,4/11)` for `s=1,2,3`. Starting rotor phase 0 and incrementing before the mark is used gives active biases

- after phase 1: `s=2 -> 2/3`, `s=3 -> 3/5`;
- after phase 0: `s=2 -> 1/2`, `s=3 -> 3/4`;
- inactive `s=1` always uses `1/4`.

Let `a_r` be the one-proposal balanced `2|2` probability and `n_r` the null probability from incoming phase `r`. Exact absorption then satisfies

`B_0=a_0+n_0 B_1`, `B_1=a_1+n_1 B_0`.

The expected exact witness from hand derivation is

`P_C091(2|2)=357573111/981185971`,

which differs from source CTCS(4), `3/11`, and from C090, `3200871/8926643`.

## What needs checking after this note

1. Exact arithmetic for the `N=4` absorbing-chain witness, including direct Bernoulli color enumeration.
2. Exact finite checks of the geometric-mod-d residue law and the `TV <= qd/2` bound for rational `q` in a nontrivial range.
3. Exact harmonic total-rate identity `sum_s lambda_{N,s}=H_{N-1}` and rational active-window rates for finite N.
4. The final report must spell out whole-path coupling, inherited-phase restriction consistency, current literature/prior attempts, and must remain PARTIAL at source level pending the two required outside audits.
