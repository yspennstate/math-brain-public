# Supplement — hybrid true-gap plus fragment-SCC localization compiler

This supplement records a newer compatible partner result that appeared after the main report was committed. It does not alter the status: full QFORM remains open.

## Fresh partner dependency

Account02/B14 subsequently completed:

`yspennstate/math-open-problems@3f241388d9bcacf1379ef8ef640b35d7d14aad91`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T150227Z-b14-qform-localization-r14/REPORT.md`.

For independent cap-one `X_1,X_2,X_3` and exponents `a,b,c<1`, `s=a+b+c<2`, it proves

`E |X_1-X_2|^-a |X_2-X_3|^-b |X_3-X_1|^-c <= C_gap(a,b,c)`,

uniformly under arbitrary separate deterministic shifts, where

`C_gap(a,b,c)`

`=1 + 2/(1-a)+2/(1-b)+2/(1-c)`

` +4/((1-a)(1-b))+4/((1-a)(1-c))+4/((1-b)(1-c))`

` +[2/(2-s)] [B(1-a,1-b)+B(1-a,1-c)+B(1-b,1-c)]`.

For `a=b=c=1/2`, `C_gap=61+12*pi`. The threshold `s<2` is sharp for this raw true-pair-gap compiler.

## Hybrid theorem

Keep an original-coordinate active triple `S={1,2,3}` unfragmented. Localize only a collection of outside coordinates into interval components with labels `alpha=(alpha_1,...,alpha_m)`, lengths `ell_{i,alpha_i}` summing to one, and fragment radii

`r_{i,alpha_i}(u)=dist(u,I_{i,alpha_i})+ell_{i,alpha_i}`.

Assume that for every outside component tuple the small-ball contribution satisfies

`W_alpha(J)`

` <= K |J| [ E_S prod_{r<s}`
`      |(X_r+tau_r(alpha))-(X_s+tau_s(alpha))|^-beta_rs ]`
`    * prod_i ell_{i,alpha_i}`
`      r_{i,alpha_i}(a_i(alpha_-i))^-theta_i`,                 (H.1)

where

- every `beta_rs<1` and `beta_12+beta_23+beta_31<2`;
- each fragment anchor `a_i` is independent of its own label but may depend arbitrarily on other outside labels;
- in the directed outside-anchor graph `i->j` when `a_i` depends on `alpha_j`, every strongly connected component `C` has `Theta_C=sum_{i in C}theta_i<1`.

Then

`sum_alpha W_alpha(J)`

` <= K C_gap(beta) |J|`
`      prod_C [2^(Theta_C)/(1-Theta_C)]`.                     (H.2)

### Proof

For each fixed outside label tuple `alpha`, the shifts `tau_r(alpha)` are deterministic. Apply account02/B14 r14 to the unfragmented active triple to bound the bracketed expectation in (H.1) by `C_gap(beta)`, uniformly in all shifts and therefore uniformly in `alpha`.

The remaining fragment ledger is exactly the SCC ledger proved in the main report of this run. Summing the outside labels costs

`prod_C 2^(Theta_C)/(1-Theta_C)`.

Multiplying the two independent localization costs proves (H.2). QED.

By exact cap-preserving finite-fragment localization, if (H.1) is obtained after localizing arbitrary outside cap-one laws, then (H.2) transfers back to those arbitrary outside laws with no moment, support-radius, translation, separation, or fragment-count assumption.

## Design consequence

The newer partner theorem makes the correct hierarchy explicit:

1. **Do not fragment a coupled active triple if its shell singularities can be retained as genuine shifted pair gaps.** True pair-gap structure has the much larger sharp budget `sum beta<2`.
2. Use the SCC fragment compiler only for singularities that genuinely arise from outside component labels. There the relevant cyclic threshold is `Theta_C<1` per strongly connected component.
3. In particular, three square-root true pair gaps are fully payable by `61+12*pi`, even though replacing them prematurely by arbitrary mutually component-dependent fragment centers would create an artificial critical-cycle obstruction.

Thus the next B14 attack should first try to derive a deterministic-outside shell estimate retaining genuine pair-gap factors on the selected active triple; only the residual outside fragment dependencies should be sent through the SCC compiler.

Source control after the fresh partner handoff was observed at `yspennstate/math-research-brain@090907b3fe12ce98d06b18961665f6074c7ddd12`. No new correction in the live inbox contradicts either compiler.
