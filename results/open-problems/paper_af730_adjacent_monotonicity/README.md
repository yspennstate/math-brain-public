# Aldous–Fill Open Problem 7.30 — adjacent normalized heat diffusion

This folder packages the frozen R05 source-responsive theorem for David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 7.30 (intake I0030).

## Exact claim

For every finite connected 1-walk-regular graph, and hence every finite simple connected arc-transitive graph, with rate-one continuous-time simple random walk

`H_t = exp(t(A/d - I))`,

the ratio `H_t(x,y)/H_t(x,x)` is strictly increasing in `t` for every edge `x~y`, starts at `0`, and tends to `1`.

The proof is analytic: if `a(t)=H_t(x,x)` and `b(t)=H_t(x,y)` on an edge, then `a'=b-a`; under the exponentially tilted local spectral law of `L=I-A/d`,

`r(t)=1-E_t[lambda]` and `r'(t)=Var_t(lambda)>0`.

This is a distance-one monotonicity on the source's arc-transitive class. It does **not** claim the stronger all-pairs MNHD property, which is known to fail on some Cayley graphs.

## Source relation and closure status

Aldous–Fill Proposition 7.29(ii) proves normalized heat-kernel monotonicity at every fixed distance on distance-regular graphs. Open Problem 7.30 asks whether arc-transitive graphs have *some* monotonicity stronger than Corollary 7.3. The theorem here supplies such a distance-one monotonicity.

Campaign mathematical/source-response closure gate: **complete for frozen C1**.

Independent full-proof audits:

- `R04-AUDIT-R05-I0030-C1-20260916T130900Z` — `PASS_MATH / NOVELTY_UNVERIFIED`.
- `P26-AUDIT-R05-I0030-C1-1WALK-REGULAR-13` — `PASS_FULL_MATHEMATICAL_PROOF / SOURCE_RESPONSIVE_PASS / FINITE_CERT_REEXECUTED / PRIOR_ART_UNVERIFIED / SOURCE_CLOSURE_INTERPRETIVE`.

Because the historical problem is open-ended and the proof ingredients are elementary, **publication priority/novelty remains UNVERIFIED**. No public-posting claim is made by this folder.

## Files

- `main.tex` — self-contained theorem, proof, source relation, scope, finite certificate summary, and prior-art note.
- `check_order22.py` — exact integer-arithmetic certificate for the complete order-22 arc-transitive census.
- `check_order22.out.txt` — archived output from the checker.

Run the finite certificate with

```bash
python3 check_order22.py > check_order22.out.txt
```

Expected final lines:

```text
metric_largest_fully_certified_vertex_count 22
RESULT PASS
```

The finite census is auxiliary; the theorem itself is proved analytically and does not depend on enumeration.
