Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-10 idea checkpoint — pruned Richardson growth as an asynchronous-frontier certificate

Status at this checkpoint: **SOURCE OPEN / `c_*=0`**. This file records the mathematical mechanism before repository certificate code. Any exploratory scratch computation is non-rigorous until replaced by the exact certificate described below.

## Why change mechanism now

The canonical axis/diagonal milestone is
\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ is proved}\}.
\]
The latest PROB10-10 run left `c_*=0`, while proving that synchronizing a finite antidiagonal frontier incurs the exact harmonic toll `H_k/2`. Thus another synchronized independent-block compiler is the wrong object. The state must retain asynchronous arrival information.

For iid `Exp(1)` edge weights there is a model-specific way to retain that information without carrying a continuum of clock ages: the Richardson/Dijkstra exploration is Markov. Conditional on the explored history, every surviving active boundary edge has an independent `Exp(1)` residual clock by memorylessness. Consequently a deliberately pruned infection front can be encoded by a **finite combinatorial state** rather than a vector of real arrival labels.

This is genuinely different from the retired R08 local-detour route, the independent point-to-line blocks, the rounded Bellman block, and the selected-reversal block.

## Selected mechanism

Use rotated coordinates
\[
s=x+y,\qquad d=x-y.
\]
Fix integers `W,L>=1`. Restrict growth to the diagonal strip `|d|<=W`. Let `M` be the largest infected `s`-coordinate. Keep only infected vertices with
\[
M-L\le s\le M,
\]
and permanently suppress transmissions from vertices discarded behind `M-L`. This can only delay infection relative to unrestricted FPP.

A state consists of:

1. the parity `M mod 2`; and
2. the retained infected subset in relative coordinates `(r,d)=(s-M,d)`, `-L<=r<=0`, `|d|<=W`.

At any state, every physical boundary edge from a retained infected vertex to an allowed uninfected vertex rings at rate one. Multiple boundary edges into the same child add their rates. A ring to level `M+1` increments `M`, shifts all relative levels down by one, and discards the new states below `-L`.

Because the state space is finite, the resulting process is a finite continuous-time Markov chain on the reachable states.

Let `a(eta)` be its instantaneous rate of `M`-advancing transitions and `Q` its generator. A finite potential `h` satisfying
\[
\boxed{a(\eta)+(Qh)(\eta)\ge v\quad\text{for every reachable state }\eta}
\tag{I.1}
\]
is an **exact average-speed certificate**.

Indeed, `M_t+h(eta_t)-int_0^t[a(eta_u)+(Qh)(eta_u)]du` is a martingale. For the hitting time `tau_N=inf{t:M_t=N}`, optional stopping at `tau_N wedge t`, boundedness of `h`, and `M_{tau_N wedge t}<=N` give
\[
v\,E(\tau_N\wedge t)\le N+\operatorname{osc}(h).
\]
Letting `t` increase proves `E tau_N <= (N+osc(h))/v` and in particular `tau_N<infinity` a.s.

When `N=2n`, the first infected strip vertex on `H_{2n}` differs from `(n,n)` by at most `W` in `d`. For each finitely many possible endpoints choose a fixed lattice connector to `(n,n)`. The random chosen connector is bounded pathwise by the maximum of finitely many fixed connector passage sums; its expectation is a constant `C_W<infinity`, independent of `n`. Hence
\[
E T(0,(n,n))\le E\tau_{2n}+C_W,
\]
and therefore
\[
\boxed{\mu(1,1)\le 2/v.}
\tag{I.2}
\]
This has a complete finite-to-infinite error:
\[
\frac{E T(0,(n,n))}{n}\le \frac{2}{v}+\frac{\operatorname{osc}(h)/v+C_W}{n}.
\tag{I.3}
\]

Thus the finite core is now precise: enumerate the reachable chain and exhibit an integer/rational potential satisfying (I.1) exactly.

## Three materially different attacks compared

### A. Pruned Richardson finite-state drift certificate — SELECTED

This is the route above. Its advantage is that the exponential memoryless property pays the asynchronous-frontier bookkeeping exactly. Its falsification points are finite and explicit: state enumeration, transition multiplicities, and every inequality in (I.1) can be integer-checked.

### B. Two-terminal residual/Jensen semigroup — COMPLEMENTARY, not duplicated

The neighboring P20 lane has converted the directional defect into a two-terminal residual metric and proved strict local Jensen curvature for the exponential Bellman operator. Its remaining obligation is a controlled-error factorization through fresh asynchronous frontier blocks. The present finite-state Richardson chain may eventually supply such a factorization, but this run does not relabel P20's claims as PROB10-10 results.

### C. Coarse two-choice fluctuation compiler — held in reserve

A different idea is to build edge-disjoint coarse corridors with random costs `W_L` and greedily select between two fresh forward corridors. The one-step gain is `E|W_L-W_L'|/2`; strictness would follow if that gain dominates the corridor's finite-size bias over `L mu(e_1)`. The unresolved difficulty is geometric: enough disjoint corridor width is needed to approach the unrestricted axis constant while preserving a source-valid embedding. This is not the same missing lemma as (I.1), so it remains a real fallback if the finite-state speed stalls.

## Negation tests that must be passed before accepting the route

1. **Static-edge versus clock-process bug.** The Markov statement must be proved from the original static iid exponential edge lengths, not assumed from a different contact-process model. At each Dijkstra stopping time, survival of an active edge conditions `tau_e` only by `tau_e>elapsed`; exponential memorylessness gives an independent residual `Exp(1)`. This is the exact bridge.
2. **Pruning direction bug.** Deleting infected vertices and suppressing their future transmissions can only make the constructed hitting time later, so it produces an upper bound on unrestricted passage time, the correct direction for (I.2).
3. **Adaptive endpoint connector bug.** One must not assert that a connector chosen after seeing the environment is fresh. Instead dominate its cost by the maximum over the finitely many predetermined connectors; only finiteness and translation invariance are used.
4. **Finite sampling bug.** A numerical stationary speed is not a theorem. The accepted artifact must contain an exact rational potential and verify (I.1) state by state using integer arithmetic.

## Source metric

Before: `c_*=0`.
At idea stage: `c_*=0`.

A diagonal upper-bound improvement is **auxiliary only** until combined with a source-valid lower bound strong enough to make `2 mu(e1)-mu(1,1)>0`. Full strict convexity remains much stronger still.
