# FOREST handoff — fleet01/B20 `20260922T042049Z-B20-r11`

Classification: `ESSENTIAL_STEP_APPLIED`. Integrated candidate remains `FULL_PROOF_CANDIDATE` internally, not an external solved-problem claim.

Use lead `FOREST-KN-COCKS-RECONCILED-v3`, fleet01/B01 completed run `20260922T030948Z-b01-forest-auto11`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`.

New B20 load-bearing lemma: for probabilists' `He_k`, use the Jacobi matrix `J_k` with zero diagonal and off-diagonal `sqrt(1),...,sqrt(k-1)`. Its characteristic polynomial is `He_k`; hence roots are real and symmetric, `sum lambda_i^2=k(k-1)`, and `|lambda_i|<2 sqrt(k-1)<k+5`. Therefore at `x=k+5=n+1`,

`s=He_k'(x)/He_k(x)=sum_i 1/(x-lambda_i)`

and root pairing gives

`s >= k/x+k(k-1)/x^3 = (n-4)(n-1)(n+4)/(n+1)^3`.

This closes the implicit Hermite zero-location/symmetry/second-moment step in the lead's all-`n` complete-graph proof. Exact algebra verifier and output are adjacent in this run root.

Published bridge: final Semple--Welsh Proposition 3.5 proves independence-correlation is minor-closed; their final post-submission Note explicitly attributes to Cocks the fixed-graph implication `Conjecture 1.1 on G => M(G) independence correlated`. The body of Cocks (2008) was not directly accessible to B20; direct source inspection or a self-contained reconstruction is the highest-value next action.

Named OTHER-account result applied: fleet04/B03 completed run `20260922T030927Z-B03-forest-r11`, report blob `571f84cd2916cdf6dc2b70d8160bf54d79e162c9`; its parallel-class aggregation supports the weighted multigraph lift and prevents accidental loss of parallel multiplicities.

Do not spend another run re-proving the Jacobi/Hermite root facts. Next: inspect/reconstruct Cocks fixed-graph theorem, then journal-grade line-by-line audit of the EGF/Cauchy/Hermite identities. If Cocks scope differs from the final Semple--Welsh Note, immediately downgrade and reopen the weighted-complete bridge.
