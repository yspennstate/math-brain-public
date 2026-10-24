Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# F0014 source-scope reconciliation: transpose obstruction

Worker: R7-02 (`6aabe797a39081919acc889f29f4c556`)
Run-start master: `3eca581996fa3f970f22547c4fbd97e6970f8815`
Fresh master before this write: `97c2dc9cbd7edfb834f8e9876ec1f7790b8d236e`
Previous R7-02 report: `research7_2026-09-17/R7-02/runs/2026-09-18/2026-09-18T132042Z__report.md` @ `471de2e985b2f96c18d20d2885809bc1071b2525`.

## Canonical source record

F0014 is Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 11.2 (intake locator Section 11, PDF p. 17). The repository transcription says that a `+-1 matrix` is determined by its spectrum if no other `+-1 matrices` other than trivial permutations have the same spectrum, and conjectures that almost all such matrices are determined by their spectrum. It separately says the same question can be raised for the symmetric Rademacher model / `G(n,1/2)`.

Current literature needs this scope parsed carefully. Da Zhao, *One can almost never hear the shape of a digraph*, arXiv:2604.02165 (2026-04-02), describes Vu's conjecture as concerning **symmetric** `+-1` matrices. This is material because the unrestricted nonsymmetric reading has an elementary transpose obstruction unless transposition itself is explicitly declared a trivial equivalence.

Primary/later-source URLs checked 2026-09-18:
- Vu: https://doi.org/10.1214/20-PS346
- Zhao: https://arxiv.org/abs/2604.02165

This is a scope reconciliation, not a worldwide novelty claim.

## Exact transpose obstruction

### Proposition

Let `A` be an `n x n` iid Rademacher matrix. Interpret the source's “trivial permutations” as simultaneous permutation similarity `A ~ P A P^{-1}`. Then

`P(exists a permutation matrix P with A^T = P A P^{-1}) <= n! 2^{-(n^2-n)/2}`,

which tends to zero. Consequently, if transposition is *not* included among the trivial equivalences, the unrestricted nonsymmetric statement “almost all +-1 matrices are determined by their spectrum” is false: with probability tending to one, `A^T` is a cospectral mate not obtainable by simultaneous relabeling.

### Proof

Fix a permutation `pi` and its permutation matrix `P`. The equality

`A^T = P A P^{-1}`

is equivalent entrywise to

`a_{r,s} = a_{pi(s),pi(r)}`

for every ordered pair `(r,s)` in `[n]^2`.

Define a permutation `T_pi` of `[n]^2` by

`T_pi(r,s) = (pi(s),pi(r))`.

The iid signs of `A` must be constant on every orbit of `T_pi`. A fixed point satisfies

`(r,s)=(pi(s),pi(r))`,

hence `r=pi^2(r)` and then `s=pi(r)`. For each `r` there is at most one such `s`, so `T_pi` has at most `n` fixed ordered pairs. Every remaining orbit has cardinality at least two. Therefore the number `N_pi` of orbits is at most

`N_pi <= n + (n^2-n)/2 = (n^2+n)/2`.

There are `2^{n^2}` possible Rademacher matrices, while matrices constant on the `T_pi`-orbits number exactly `2^{N_pi}`. Thus

`P(A^T=PAP^{-1}) = 2^{N_pi-n^2} <= 2^{-(n^2-n)/2}`.

Taking a union bound over the `n!` permutation matrices gives

`P(exists P: A^T=PAP^{-1}) <= n! 2^{-(n^2-n)/2}`.

Since `log_2(n!)=O(n log n)=o(n^2)`, the right-hand side tends to zero. Finally, `A` and `A^T` always have the same characteristic polynomial because

`det(lambda I-A^T)=det((lambda I-A)^T)=det(lambda I-A)`.

Therefore, except on an event of probability at most `n!2^{-(n^2-n)/2}`, transposition supplies a non-permutation-similar cospectral mate. QED.

## What this does and does not establish

1. This does **not** refute the symmetric Rademacher version: there `A^T=A` identically.
2. This does **not** refute an unrestricted formulation whose definition of “trivial” explicitly includes transposition.
3. It does show that the canonical intake wording cannot safely be treated as an unqualified nonsymmetric permutation-similarity conjecture.
4. Zhao's 2026 wording is consistent with the mathematically meaningful modern target being the symmetric model.
5. F0014 already has substantive prior-attempt history and has independently been classified HARD rather than finite/short CLOSABLE. This reconciliation therefore does not make it admissible for R7-02.

Disposition: `F0014 = NOT_ADMISSIBLE_AS_R7-02_CLOSABLE; SOURCE_EQUIVALENCE_CONVENTION_REQUIRES_RECONCILIATION; SYMMETRIC_VERSION_REMAINS_DISTINCT_HARD_TARGET`.

No canonical claim is created. No successor mathematical metric is frozen.