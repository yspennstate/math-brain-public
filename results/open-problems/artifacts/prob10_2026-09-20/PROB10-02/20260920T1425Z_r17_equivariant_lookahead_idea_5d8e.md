# PROB10-02 / R17 — idea before code: equivariant lookahead matching with a synchronizing source atom

Model request: GPT-6 / maximum reasoning. This runtime exposes no authenticated applied-model or applied-effort selector/receipt, so actual model/effort metadata remains UNVERIFIED.

Target remains the genuine Chvatal--Sankoff binary constant for two independent iid fair source strings. No independent Bernoulli matching array is introduced.

## Continuity / ownership frozen before mathematics

Controlling directive: `operations/PROB10_2026-09-20.md`.

Newest completed own report read before this note:
`runs/prob10_2026-09-20/PROB10-02/20260920T1402Z_r17_greedy_frontier_upper_84c7.md`.
That run changed method to canonical greedy-embedding frontiers and proved a rigorous stopping-line upper transfer, but did not move the source interval.

The pre-refocus R17 successor is still H0021. `operations/claims/H0021.md` has blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`; H0021 is released/unassigned, `Delta_near=2`, with R16's six-run stagnation/two recoveries and R17's one substantive H0021 unchanged run preserved. Navigation commit `c8891869a1335d67bada83f23f63f2ce09603565` remains the historical pointer. Nothing in H0021 is reset.

Same-source split is not overwritten: P02 owns the covering/cone stationary upper-dual lane, P13 owns the strip/boundary recursion lane, and R17 uses a constructive finite-lookahead policy lane. The current source lower endpoint is `L=0.792665992`; P02's newest durable internal upper certificate entering this run is the p-adic type-0/type-1 endpoint `U_01` from `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T13-10-25Z__padic-type01-dual-report.md`. Therefore the source metric entering this run is `W=U_01-L`; no finite policy certificate counts as endpoint progress unless it exceeds `L`.

## New idea

Fix a lookahead length `k`. A state is a pair `(x,y)` of binary `k`-windows cut from the *actual* two source strings. If the leading bits agree, match them and shift both windows, revealing one fresh iid source bit on each side. If the leading bits disagree, choose exactly one side to discard/shift, revealing one fresh iid bit only on that side. Thus every reward-one transition is a genuine common-subsequence match.

For a stationary policy `pi`, let `r` be match reward, let `c_X,c_Y` be source-symbol consumptions, and put `c=(c_X+c_Y)/2`. Seek a swap-equivariant policy (`pi(y,x)` is the swapped action of `pi(x,y)`) and a potential `h` satisfying the exact Bellman lower certificate

`E[r-rho*c+h(S')-h(S) | S=s] >= 0` for every finite state `s`.

If the induced finite chain has a unique stationary law, swap equivariance forces equal stationary X/Y consumption rates. Then the certificate should give a rigorous constructive lower bound `gamma_2 >= rho`.

The key transfer issue is not to assume uniqueness/mixing from symmetry. I will instead try to prove a policy-independent synchronizing source event. Candidate: prescribe a common alternating fresh tail on both sources. Once one window has been flushed, its head alternates whenever it is shifted; a lagging frozen head must then agree within at most two decisions, forcing a joint shift. This should flush both windows in bounded time. Once both are in alternating tails, at most one mismatch shift aligns their phases; then equal-head transitions can keep the windows diagonal. Appending common zeros for another `k` joint shifts reaches `(0^k,0^k)`. If correct, this yields a uniform atom `P^m(s,(0^k,0^k)) >= delta_k>0` for *every* deterministic equal-head-matching policy, hence a proved finite-to-stationary error rather than an unverified ergodic assumption.

## Three attacks fixed before code

1. **Exact Bellman certificate.** Use relative-value iteration only to *discover* an equivariant deterministic policy/potential at the largest feasible `k`; round the potential to integers and then verify every Bellman inequality by exact integer arithmetic. Float output is not a certificate.
2. **Synchronizing-atom transfer.** Prove from source bits, not simulation, a uniform finite-step path to a common atom for any deterministic policy that always matches equal heads. Use the resulting Doeblin contraction to construct a bounded Poisson solution for the X-minus-Y consumption drift and derive an explicit finite-`n` LCS lower error at the stopping time when one coordinate has consumed `n` symbols.
3. **Compression falsification / continuation.** Test whether the discovered Bellman policy/value factors through a much smaller natural suffix statistic (heads plus common-prefix/suffix/run information). A single exact pair of states with the same proposed statistic but different certified preferred actions is an obstruction and will be archived. If a quotient survives, use it to push `k` farther; otherwise do not claim compression.

The run remains OPEN/PARTIAL unless a certificate beats the rigorous public lower endpoint and the full repository closure standard is separately met.