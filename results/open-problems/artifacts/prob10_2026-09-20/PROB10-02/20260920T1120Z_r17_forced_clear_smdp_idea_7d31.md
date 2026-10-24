# PROB10-02 / R17 idea-before-code — forced-clear information options and ratio Bellman

Model request: GPT-6 maximum reasoning. Applied model/effort metadata is not authenticated by this runtime, so it remains UNVERIFIED.

Target remains the true binary Chvatal--Sankoff constant for two independent iid fair binary strings. All proposed transitions below are to be realized by actual source bits; no independent Bernoulli matching array is permitted.

Continuity is not reset. H0021 remains released/unassigned under `operations/claims/H0021.md`, with `Delta_near=2`, R16's six-run historical stagnation and two consumed recoveries, and R17's one H0021 unchanged run preserved. Navigation point: `c8891869a1335d67bada83f23f63f2ce09603565`. The newest R17 LCS report is `runs/prob10_2026-09-20/PROB10-02/20260920T1046Z_r17_one_sided_information_debt_f2c4.md`; its no-free-peek theorem, one-sided debt Bellman operator, source-valid transfer, exact checks through ell=6, and failed leading-run shortcut are inherited rather than restarted. P02 owns the covering/cone upper route; P13 owns the strip/boundary recursion. This run stays on R17's finite-lookahead/information-state route.

The inherited exact source metric is `L=99083249/125000000=0.792665992` and the newest visible P02 matched-successor-defect upper certificate `U_new`, with the symbolic definition and rigorous separator recorded in the 10:46 R17 report. This run will not attribute P02's endpoint progress to R17.

## New method

The persistent-debt operator from the preceding run uses `3*4^ell` states. The new attempt eliminates persistent debt *without forgetting an exposed source bit*: whenever a mismatch action peeks at the next X bit and then advances Y instead of X, the next micro-decision is forced to clear that outstanding X bit. Thus every composite option starts and ends in an ordinary no-debt state `(a,b)`.

For a visible-window pair `(a,b)` of length `ell`, define an X-oriented forced-clear option at a mismatch as follows. Reveal the actual next X bit `u`. For each observed `u` the policy may either:

1. advance X immediately, ending the option after one micro-step in `(sigma_u a,b)`, reward `0`, consumption `(1,0)`; or
2. advance Y first, drawing the actual Y refill `v`. If the new heads mismatch, force an X advance using the already exposed `u`, ending after two micro-steps in `(sigma_u a,sigma_v b)`, reward `0`, consumption `(1,1)`. If the new heads match, take that match, drawing only the next actual Y refill `w`, and end in `(sigma_u a,sigma_w(sigma_v b))`, reward `1`, consumption `(1,2)`.

There is a swapped Y-oriented option. Ordinary immediate match and ordinary one-side advances are retained as admissible options. Every option is causal and uses each source bit exactly once; the exposed bit is never resampled or forgotten.

This is naturally a finite semi-Markov decision process (SMDP) on only `4^ell` no-debt states. For an option `o` let `r(o)` be its common-subsequence reward, `c_X(o),c_Y(o)` its consumed symbols, and `S_o` its random successor. For a candidate source-rate `alpha`, define the ratio residual

`R_alpha h(s,o) = E[ r(o) - (alpha/2)(c_X(o)+c_Y(o)) + h(S_o)-h(s) ]`.

The mathematical target is to prove: if for every state `s` there is an admissible option with `R_alpha h(s,o)>=0`, then `gamma_2>=alpha`. The proof should use an X-oriented policy and its swapped Y-oriented copy on independent fresh blocks, so the expected X/Y consumption imbalance cancels while the potential telescopes; bounded window/overshoot terms vanish. This is a new finite-to-infinite transfer, not a simulation heuristic.

If correct, the forced-clear construction may permit exact certificates at much larger `ell` because the state space is `4^ell` rather than persistent-debt `3*4^ell`, and because each residual can be evaluated locally over a bounded option tree.

## Three attacks fixed before code

### Attack A — prove the forced-clear SMDP ratio transfer and compute exact small-width certificates

Derive the option kernels and prove the source realization and block-pair transfer with exact hypotheses. Then use floating relative-value iteration only to propose potentials; freeze a rational/integer potential and verify every Bellman residual exactly. The source metric moves only if an exact certificate gives `alpha>L`.

### Attack B — strengthen the option set without persistent information debt

Allow a bounded two-sided forced-clear macro: after a first peek/skip, permit one swapped-side peek provided all exposed bits are consumed before the macro ends. Prove a deterministic bound on macro length and source consumption, then test whether the enlarged finite option set strictly improves the certified ratio at the same `ell`. If the macro can leave a bit unconsumed, it is rejected by the inherited no-free-peek theorem rather than silently resampled.

### Attack C — test a local quotient for the forced-clear inequality, and preserve a counterexample if false

Test whether the maximizing residual/action can be determined from a small invariant such as `(head-match flag, leading-run lengths capped at k, LCS(a,b), Hamming weight of a xor b)`. This would give an inequality quotient rather than the already-exhausted exact behavioral quotient. Exhaustively search small `ell` for two states sharing the proposed invariant but requiring incompatible maximizing actions/residuals. A counterexample is useful because it prevents another large-scale run on a false compression.

## Success / failure criteria

A finite computation is mechanism progress only unless the proved transfer yields an endpoint improvement. Source-level before/after remains the exact inherited interval unless `alpha>L` or a new independently source-valid upper certificate is proved. Three distinct attacks will be recorded, with false lemmas and counterexamples retained. Status remains OPEN/PARTIAL unless the full constant is determined and closure audits exist.