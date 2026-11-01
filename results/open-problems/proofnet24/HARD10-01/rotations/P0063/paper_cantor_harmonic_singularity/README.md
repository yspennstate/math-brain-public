# P0063 — Cantor harmonic-measure singularity proof package

## Exact source target

Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, maintained paperback/electronic edition (version 19 August 2026), Question 16.7, printed p. 542:

> Let `E` be the middle-thirds Cantor set. For integer base `b`, let `mu_b` be harmonic measure of simple random walk on the maximal coding tree `T_[b](E)` and `nu_b` the corresponding pushforward to `E`. Thus `nu_3` is Cantor--Lebesgue measure. Is `nu_2 \perp nu_3`?

## Theorem in this package

`main.tex` proves the exact source statement

`nu_2 \perp nu_3`.

The proof does **not** replace `nu_2` by an iid digit law. The base-2 conditional probabilities are the genuine harmonic-current splits of the infinite maximal dyadic coding tree.

## Proof architecture

1. Dyadic Hellinger affinities
   `A_n = sum_{I in D_n} sqrt(nu_2(I) nu_3(I))`
   decrease, and mutual singularity is equivalent to `A_n -> 0`.
2. The exact one-step Hellinger cocycle shows that hypothetical non-singularity forces
   `sum_n E_{w_n}[(p_v-q_v)^2] < infinity`.
3. An exact electrical-network certificate gives a genuine infinite harmonic split asymmetry at the normalized scenery
   `(u0,r0)=(52/243,128/243)`.
4. A variational continuity argument plus finite topology stability thickens this to an open scenery neighborhood with a uniform split gap.
5. Under hypothetical non-singularity, the Hellinger level measures `lambda_n` converge in total variation to a fixed overlap law `lambda << nu_3`, allowing varying good-cell events to be transferred back to the Hellinger weights.
6. Allen--Chow--Yu's published Fourier-product/digit-change estimates give suffix/position mixing for every `lambda << nu_3`.
7. The suffix `22`, together with irrational recurrence of `log_3 2`, produces a positive-overlap family of isolated dyadic sceneries with a uniform split gap infinitely often, contradicting the finite Hellinger-loss series.

## Exact finite evidence

The canonical exact scripts and archived outputs remain in the track artifact directory:

- `../artifacts/2026-09-18T11-16-20Z__infinite_split_checker.py`
  - creation commit: `76dceba302605a0e5220ef8030841d188f7da7b0`
  - blob: `7d6986bb248e464da3f7b8a137f7c87d46b85f08`
- `../artifacts/2026-09-18T11-16-20Z__infinite_split_checker.out`
  - creation commit: `ffa6590d981d25185312fbe6eb648d395927f4b1`
  - blob: `a24f94e90e8c21917ba2e8ac0f30affb64b500a6`
  - begins `EXACT_CHECK_PASS`
- `../artifacts/2026-09-18T12-30-19Z__scenery_gap_checker.py`
  - creation commit: `51b582a26f4ea0636b6ddb0d49b19f0f5c97e570`
  - blob: `35c188dd4475b516c02ea54e61ae179becd04ee9`
- `../artifacts/2026-09-18T12-30-19Z__scenery_gap_checker.out`
  - creation commit: `3acb96dfe5f63fc787a161c55106b15f4b4e36e4`
  - blob: `a5895830e5ccc9f09e7bc6cb5e25ede6b673d96b`
  - begins `EXACT_CHECK_PASS`

Copies of the two theorem-critical scripts and their archived outputs are also stored in this paper folder for a self-contained submission package.

## Imported prior art

The proof imports, and explicitly credits, Demi Allen, Sam Chow and Han Yu, *Dyadic approximation in the middle-third Cantor set*, Selecta Mathematica 29 (2023), Article 11:

- Lemma 2.6: Fourier-product decay in terms of ternary digit changes;
- Theorem 1.13: the Stewart / Bugeaud--Cipu--Mignotte digit-change lower bound in multiplicatively independent bases.

These arithmetic results are prior art and are not claimed as new. The electrical/Hellinger/scenery bridge is the source-specific proof mechanism developed here.

A bounded search on 2026-09-18 found no source-matching resolution, while the maintained Lyons--Peres PDF still explicitly labels Question 16.7 open. This is current-status evidence, **not** by itself a priority/novelty certificate.

## Closure status

Mathematical metric: `C_Cantor = 1` (source theorem proved).

Fleet closure: **PENDING**. The project protocol requires two independent end-to-end full-proof audits by OTHER tracks. This worker's proof hardening and exact scripts are self-checks and do not count toward those two audits. No public posting should be inferred from this package until the audit gate is satisfied.
