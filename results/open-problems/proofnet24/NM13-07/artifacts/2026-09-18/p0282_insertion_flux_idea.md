# P0282 idea before code — insertion flux for exact LIS levels

Date: 2026-09-18 UTC
Worker: NM13-07
Target: P0282 / Chen fixed-size LIS log-concavity

This note is the new route written down before archiving the row-86 checker.

For `sigma in S_n` with `LIS(sigma)=k`, define

`h(sigma) = min{r : LIS(sigma_1,...,sigma_r)=k}`,

namely the first prefix length at which the final LIS length is attained. Let

`H_{n,k} = sum_{sigma in S_n, LIS(sigma)=k} h(sigma)`

and `U_{n,k}=sum_{r<=k} ell_{n,r}`.

## Exact insertion-flux lemma

Insert the new largest letter `n+1` into one of the `n+1` gaps of `sigma`, after `p` old letters, with `0<=p<=n`.

- If `p < h(sigma)`, the prefix before the new maximum has LIS at most `k-1`; appending `n+1` cannot create an increasing subsequence longer than `k`, while the old permutation still supplies one of length `k`. Hence the child still has LIS `k`.
- If `p >= h(sigma)`, the prefix already contains an increasing subsequence of length `k`, so appending the largest letter creates one of length `k+1`. Hence the child has LIS `k+1`.

Thus exactly `h(sigma)` insertions preserve level `k`, while `n+1-h(sigma)` raise it to `k+1`. Deleting the unique letter `n+1` from a child is inverse to this construction, so for every `n>=1` and `1<=k<=n+1`, with `H_{n,0}=ell_{n,0}=0`,

`ell_{n+1,k} = H_{n,k} + (n+1) ell_{n,k-1} - H_{n,k-1}`.      (IF1)

Summing (IF1) over levels `1,...,k` telescopes:

`U_{n+1,k} = H_{n,k} + (n+1) U_{n,k-1}`,

hence the exact closed identity

`H_{n,k} = U_{n+1,k} - (n+1) U_{n,k-1}`.                       (IF2)

Under RSK, the prefix shapes are the shapes of the recording tableau restricted to entries `1,...,r`, so `h(sigma)` is exactly the entry `Q(1,k)` in the last cell of the first row of the recording tableau. Thus (IF2) is also an exact first-moment identity for that tableau entry over the Plancherel level `lambda_1=k`.

Define the normalized preservation probability

`alpha_{n,k} = H_{n,k}/((n+1) ell_{n,k})`.

Then the level probabilities `p_{n,k}=ell_{n,k}/n!` evolve by the exact nearest-neighbor flux law

`p_{n+1,k} = alpha_{n,k} p_{n,k} + (1-alpha_{n,k-1}) p_{n,k-1}`.  (IF3)

This is a genuinely different route from the determinant/minor approach: instead of trying to prove all-minor total positivity (already refuted by the archived TP5 counterexample), it asks whether the special insertion flux has a monotonicity or interlacing property strong enough to preserve log-concavity. A natural concrete target is monotonicity of `alpha_{n,k}` in `k`; finite exact exploration through `n=29` found no violation, but this note does NOT promote that finite observation to a theorem.

Section-B interpretation for this run (all recycled because all 30 labels were already used on P0282):
- #12 FIND WHAT IS CONSERVED: insertion conserves total mass and exposes the exact adjacent-level flux (IF1)-(IF3).
- #18 SAY IT IN ANOTHER LANGUAGE: the source counts are rewritten as a one-step growth process on LIS levels and as a first-row hitting-time statistic of the RSK recording tableau.
- #28 REPLACE FOR ALL WITH TYPICAL: the pointwise insertion dichotomy is averaged to `alpha_{n,k}`; the prospective proof target becomes a monotonicity statement about the conditional mean hitting time rather than an all-minor determinant statement.

No closure is claimed. The next proof question is whether `alpha_{n,k}` admits a coupling, tableau injection, or variation-diminishing inequality in `k`, and exactly what additional condition on the bidiagonal flux kernel would force preservation of log-concavity.
