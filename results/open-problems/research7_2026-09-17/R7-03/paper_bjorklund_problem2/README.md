# Source scope — Björklund Problem 2

Status: **PROVED CANDIDATE / protocol closure open**. Publication novelty is **UNVERIFIED**.

## Exact source

Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2 (2014), Appendix II §7.1, **Problem 2**, printed PDF p.24:

> Construct a countable measured group `(G,mu)` and an infinite-index subgroup `H<G` such that `G/H` does not admit any nonconstant left `(quasi-)mu`-harmonic functions whatsoever.

Primary source: `https://arxiv.org/abs/1406.0763`.

The source defines a measured group as a countable group equipped with a probability measure whose support generates the group as a semigroup. Its left convolution uses `check(mu)`; the construction here is symmetric, so `check(mu)=mu`. The source's general quasiharmonic definition uses an arbitrary constant defect `ell(phi)`; it does **not** force the value at the identity/basepoint to vanish.

## Construction proved in `main.tex`

Take

- `G = Sym_fin(N_0)`, the finitary symmetric group;
- `H = Stab_G(0)`;
- `tau_n=(0 n)` for `n>=1`;
- `mu(tau_n)=2^{-n}`.

The star transpositions semigroup-generate `G`, `G/H≅N_0`, and the induced left convolution is the infinite-star kernel

`P(0,n)=2^{-n}` and `P(k,0)=2^{-k}`, `P(k,k)=1-2^{-k}`.

The proof actually works for every strictly positive probability vector `(p_n)`: any integrable constant-defect solution `Pu=u+c` obeys `u(k)=u(0)-c/p_k`. Center integrability then forces `c=0`, and hence `u` is constant.

## Scope and dependencies

The source-level proof is elementary and self-contained. It depends only on basic permutation-group facts, absolute integrability of a complex probability integral, and the source's definitions. There is no numerical or solver dependency.

The controlling source-interface correction is archived at

`research7_2026-09-17/R7-03/artifacts/2026-09-18/2026-09-18T052600Z__E0070_source_definition_correction.md`.

It supersedes the earlier immutable normalization addendum

`research7_2026-09-17/R7-03/artifacts/2026-09-18/2026-09-18T003800Z__E0070_source_normalization_addendum.md`

**only** on that addendum's claim that Björklund's general definition identifies the defect with the integral itself and therefore forces `u(H)=0`. The main arbitrary-defect theorem already covered the correct source definition and remains valid.

The main full-proof artifact is

`research7_2026-09-17/R7-03/artifacts/2026-09-18/2026-09-18T003400Z__E0070_star_transposition_solution.md`.

## Dated prior-art status

Bounded searches on 2026-09-18 checked the current arXiv version, exact problem wording and exact §4.1 quasiharmonic definition, later Björklund random-walk/stationary-action work, finitary-symmetric-group random walks, star transpositions, and related homogeneous-space/Poisson-boundary literature. No explicit later source-matching resolution or this exact construction was located. **This is negative evidence only and does not certify novelty.**

## Closure checklist

- source-level written proof: **present**;
- exact source-scope README: **present**;
- useful proof artifacts: **present**;
- source-definition correction incorporated in `main.tex`: **present**;
- independent P26 full-proof audit: **missing (0/1)**;
- distinct OTHER-track independent full-proof audit: **missing (0/1)**;
- public posting: **not authorized / not performed**.

Do not label this package audit-complete until both independent audits exist and pass.
