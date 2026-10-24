# R11 / I0054 — idea note before code: thinned shadow refresh and the sharp universal threshold

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum, and I do not claim otherwise.**

This note is intentionally committed before any new checker for the run.

## Three new-method moves actually used

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT.** Insert a thinning factor `theta_N` into C092's independent inactive shadow stream and ask how the whole-path error depends on the single effective refresh rate `rho_N = theta_N R_N`.
- **#12 FIND WHAT IS CONSERVED.** Uniform thinning preserves the conditional law of a shadow mark exactly. The hash/extractor law from U076 is therefore unchanged; only the refresh clock rate changes. This separates distributional quality from temporal refresh frequency.
- **#27 SWAP THE QUANTIFIERS.** Instead of asking whether one chosen branch schedule `b_N` works for one chosen thinning schedule, ask for a criterion that works **for every deterministic branch schedule `b_N`**. The expected answer is an if-and-only-if threshold in `rho_N`.

## Setup

Use the same active window as C092,

`I=[1/2,4/5)`,

ordinary harmonic rates

`lambda_{N,s}=N/(2s(N-s))`,

active total rate

`W_N=sum_{s/N in I} lambda_{N,s} -> log 2`,

and inactive total rate

`R_N=sum_{s/N notin I} lambda_{N,s}=H_{N-1}-W_N ~ log N`.

At every ordinary inactive mark use the source paintbox `p=s/N`. At every ordinary active mark use the cyclic-logit bias determined by the current phase `J in Z/d_N Z` and an arbitrary integer branch count `b_N`.

Now replace C092's full shadow stream by uniformly thinned shadow clocks

`theta_N lambda_{N,s}` for inactive `s`, with `0<theta_N<=1`.

A shadow ring never changes the partition. It only resets the phase to the deterministic U076 hash `h_N(s)`. Uniform thinning leaves the conditional shadow-mark distribution exactly

`pi_{N,s}=lambda_{N,s}/R_N`.

Hence the hash error

`epsilon_N = || h_N(pi_N)-U_{d_N} ||_TV`

is exactly the same as in U076. Only the aggregate refresh rate changes to

`rho_N = theta_N R_N`.

Children inherit the current phase at a visible split and thereafter receive independent thinned shadow streams.

## Candidate theorem U077(A): sufficiency

For each fixed visible `k` and time horizon `T`, couple the thinned-shadow hierarchy to U073's fresh-dither hierarchy.

Between a carrier block's birth (or its preceding active proposal) and its next active proposal, compare the active proposal clock of rate `W_N` with its shadow refresh clock of rate `rho_N`. The probability that the active proposal arrives before any new shadow refresh is

`q_N = W_N/(W_N+rho_N)`.

If at least one shadow refresh occurs first, the last shadow mark is independent of the active proposal and has law `pi_N`, so its hashed phase can be coupled to a fresh uniform phase with error `epsilon_N`.

At all times there are at most `k` visible carrier blocks. The total number of active proposals on visible carriers up to time `T` has expectation at most `k T W_N`. Sequential coupling therefore gives

`TV(path_thin, path_fresh) <= k T W_N ( q_N + epsilon_N )`.

U073 gives

`TV(path_fresh, path_CTCS) <= C_{k,T}(1/d_N + 1/N)`.

Therefore

`TV(path_thin, path_CTCS) <= k T W_N( W_N/(W_N+theta_N R_N) + epsilon_N ) + C_{k,T}(1/d_N+1/N)`.

So if

- `d_N -> infinity`,
- `epsilon_N -> 0` (for example U076's `log d_N=o(R_N)` deterministic hashes), and
- `theta_N R_N -> infinity`,

then every fixed finite restriction converges in whole-path TV on `[0,T]`, hence in finite-state `J_1`, and projectively to CTCS(infinity), **uniformly over arbitrary deterministic branch schedules `b_N`**.

## Candidate theorem U077(B): necessity for universal-in-b convergence

The key question is whether `theta_N R_N -> infinity` is merely sufficient or genuinely sharp for a compiler that must work for **every** branch schedule.

Assume instead that along an infinite subsequence

`rho_N=theta_N R_N <= M < infinity`.

Use U074's simultaneous Dirichlet construction to choose integers `b_N` so every active fractional logit phase lies within `1/N` of the compactified seam. Let `w_N` be the harmonic active weight landing on the `0+` side. In the seam limit, two specified split observables have active contributions

`A_11(w) = log(2) [ 8/25 + (9/50) w ]`,

`A_13(w) = log(2) [ 68/625 + (81/5000) w ]`,

whereas CTCS requires respectively

`3/10` and `21/250`.

Their zero locations are

`w_11=(15-16 log2)/(9 log2)`,

`w_13=4(105-136 log2)/(81 log2)`,

with

`w_11-w_13 = 5(80 log2-57)/(81 log2)`.

Strict convexity gives

`2/3 < log 2 < 17/24 < 57/80`.

Hence

`|w_11-w_13| > 5/243`.

The smaller slope is `81 log2/5000 > 27/2500`. Therefore for **every** seam weight `w in [0,1]`,

`max( |A_11(w)-3/10|, |A_13(w)-21/250| ) > 1/9000`.

Thus for all sufficiently large `N`, at initial phase zero at least one of the two specified visible split rates differs from its CTCS rate by a fixed amount, say `delta=1/10000`. By pigeonhole, one of the two observables has this discrepancy along an infinite subsequence.

Because `rho_N<=M`, the hidden refresh rate is uniformly bounded. For either visible state (`k=2` for `1|1`, or `k=4` for a fixed `1|3` split), the total rate of all **state-changing** events (visible splits plus shadow refreshes) is uniformly bounded by a constant `K(M,k)`; ordinary null proposals can be removed by Poisson thinning. Uniformization / the one-jump expansion then gives for the relevant path cylinder event `E_t`

`P_N(E_t)=r_N t + O(K^2 t^2)`,

while CTCS gives

`P_CTCS(E_t)=r_* t + O(K_*^2 t^2)`.

Choose one fixed sufficiently small `t=t(M)>0`. The linear discrepancy `|r_N-r_*|>=delta` dominates the quadratic remainders, so the path-law TV distance stays bounded below along that subsequence. Therefore convergence to CTCS fails.

This would prove the sharp universal statement:

> Under the U076 hash-quality assumptions, the uniformly thinned shadow compiler converges to CTCS for **every** deterministic branch schedule `b_N` iff `theta_N R_N -> infinity`.

The converse is a worst-case-in-`b_N` statement, not a claim that every individual `b_N` fails below threshold.

## Candidate new model C093

Take the same deterministic U076 hash alphabet as C092,

`d_N = 2^{max(1,r_N)}`, where `r_N=max{r:2^{r^2}<=N}`,

retain the concrete doubly-exponential branch schedule from C092, and thin the shadow stream by

`theta_N = 1 / max(2, floor(sqrt(log_2 N)))`.

Then `theta_N -> 0`, so the auxiliary shadow traffic is an asymptotically vanishing fraction of C092's shadow mechanism, while

`theta_N R_N ~ sqrt(log N) -> infinity`.

U077(A) would therefore prove the complete whole-path CTCS limit.

At `N=4`, `theta_4=1/2`, so the only inactive shadow clock has rate `1/3` rather than C092's `2/3`. With the same two finite phase paintboxes used by C092,

phase 0: `(1/4,1/2,3/4)`,

phase 1: `(1/4,2/3,3/5)`,

the exact balanced-root absorption equations are

`B_1 = a_1/(a_1+u_1)`,

`B_0 = (a_0 + (1/3) B_1)/(a_0+u_0+1/3)`.

The checker should verify that this differs exactly from CTCS and from C092/C091/C090/C084, providing the finite non-equivalence certificate required by the frozen metric.

## What would falsify this route

1. If the per-active-proposal coupling needs a refresh after every ordinary inactive null proposal rather than only after birth/preceding active proposal, the stated error bound is wrong. Current reasoning says it does not: inactive ordinary proposals use the source bias and do not inspect or alter the phase.
2. If the seam discrepancy could vanish simultaneously for the `1|1` and `1|3` coordinates, the necessity argument fails. The explicit incompatible zero locations and the `1/9000` quantitative separation rule this out.
3. If state-changing rates on fixed visible restrictions were not uniformly bounded, the small-time necessity argument would fail. They are bounded: active proposal rate tends `log 2`, source inactive visible split rates are bounded by the finite CTCS split rate, and the shadow rate is assumed `<=M` on the necessity subsequence.

No closure claim is made in this idea note; the theorem and finite witness still require a written final proof plus an exact self-check.