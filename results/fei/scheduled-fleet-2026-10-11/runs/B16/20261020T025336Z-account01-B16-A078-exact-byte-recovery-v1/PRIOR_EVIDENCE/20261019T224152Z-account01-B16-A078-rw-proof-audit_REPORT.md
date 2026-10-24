# B16/A078 run report — corrected random-walk proof audit

- Run: `20261019T224152Z-account01-B16-A078-rw-proof-audit`
- Primary packet: A078
- Stable gap: `G-A078-BOOLEAN-CODING-PADDING`
- Model: GPT-6
- Reasoning effort: UNKNOWN
- Endpoint: `2026-10-21T19:15:57Z`, unchanged

## Result

I independently re-derived the constant chain of the corrected random-walk/central-band proof at the level of inequalities and arithmetic. No new fatal algebraic error was found in the checked chain. This is a B16 self-audit, not an independent end-to-end review, not acceptance, and not native ingestion.

The candidate family has exact `H=2n`, `I=U=n`. Conditional on the all-dimensional proof, `G_y >= n+n^2/C`, `C=34,406,400`, for `n>=131072`; hence for every fixed `a>=0`, `0<=b<1`, `N=max(131072,floor(C(a+b+2))+1)` gives normalized GU residual `>3`. For `(a,b)=(4,3/4)`, `N=232,243,201` and the lower residual is exactly `3+1/C`.

## Important comparison correction

The single-central-atom alternative and the random-walk proof should both be retained. Their normalized y-block excesses are respectively `sqrt(n)/16000` and `n/C`. The atom route has the larger excess at `n=131072` (`0.02263` versus `0.00381`), but the random-walk route dominates for `n>(C/16000)^2≈4,624,220`, and it gives an all-parameter witness dimension linear in `a+b` instead of quadratic. This audit corrects any overly broad claim that the atom bound is weaker at every dimension.

## Verification

`python3 verify_audit.py` passed. It checked exact central-binomial comparisons for `m=3..4096`, central-window count/adjacent-mass ratio inequalities for `m=1024..4096`, Chernoff constants, selected-interval geometry, the frozen-pair residual, and the comparison of the two mechanisms. The analytic monotonicity arguments extend the endpoint bounds beyond the finite checks; the script itself does not prove the all-dimensional theorem.

## Next action

A092 should independently reconstruct the central-window/Paley–Zygmund crossing event and extension tail. A088 should independently reconstruct the signed matching-fraction inequality with the terminal extension retained. A080 should audit the all-parameter GU residual and scope. B20 alone reconciles shared mathematical status after actual review evidence.

## Persistence

Local report/code/output and integrity metadata are included. The standing source/write hold remains binding; no remote canonical save, Brain mirror, alternate route, shared-index update, or scheduler edit was attempted. Remote persistence and independent reviews remain unconfirmed.
