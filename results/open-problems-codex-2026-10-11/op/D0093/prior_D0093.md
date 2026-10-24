# Canonical claim — D0093

- **Problem ID:** D0093
- **Owner:** P13 / native slot `6aa7b253b37c8191b693d8dc79298d37`
- **Category:** CLOSABLE OUTSIDE
- **Claim status:** EXCLUSIVE / OPEN / PARTIAL
- **Source:** Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), arXiv:1906.05037v2, Section 6.2, open problem immediately after Theorem 6.1 / estimate (6.3).
- **Exact source target:** In the one-dimensional cycle ARW fast regime of Section 6.2, remove the `log^2 n` factor from the high-probability upper bound on the total number `T` of topplings, i.e. prove an order-`n` bound under the same source hypotheses.

## Frozen metric

`beta_fast` is the infimum exponent among **proved source-domain bounds of the exact form**

`P(T <= kappa n (log n)^beta) >= 1 - n^{-delta}`

for constants `kappa < infinity`, `delta > 0` depending only on the fixed source parameters, uniformly for all sufficiently large `n`, under the same fast-regime parameter domain used for (6.3) (equivalently, the proof chooses `zeta < zeta' < lambda/(1+lambda)`).

- **Baseline at admission:** `beta_fast = 2` (source Theorem 6.1 / (6.3)).
- **Source target:** `beta_fast = 0`.
- Auxiliary lemmas, different initial laws, open-boundary boxes, or infinite-volume odometer estimates do **not** move this metric unless they yield the exact finite-cycle Poisson-source bound above.

## Admission evidence / boundaries

- Direct pre-claim fetch of `operations/claims/D0093.md` returned 404.
- Repository-wide exact-ID searches recovered intake/catalog/prior-attempt material but no canonical owner or current D0093 research report.
- The original intake records D0093 as source-open/unverified and its prior attempt identifies odometer tails as the barrier.
- Fresh literature screening on 18 September 2026 found Johnson–Richey (arXiv:2510.05514v2, 2025), which proves stretched-exponential subcritical odometer tails on `Z` for i.i.d. Bernoulli initial data. This materially changes the route but does **not** itself solve D0093, whose source uses i.i.d. Poisson initial data on a finite cycle.
- Searches also recovered the original cycle theorem and later ARW papers, but no source-matching order-`n` finite-cycle theorem. This is bounded negative evidence, not a global openness or novelty certificate.

## Exclusions

- Do not reopen retired P13 I0051.
- Do not reopen or relabel handed-off P0082.
- Do not substitute a Bernoulli/infinite-line theorem, an open-boundary theorem, or a narrower parameter subcase for the source finite-cycle Poisson statement.
- Closure still requires a source-exact full proof, prior-art review with limitations, a P26 end-to-end audit, and a second independent OTHER-track end-to-end audit.
