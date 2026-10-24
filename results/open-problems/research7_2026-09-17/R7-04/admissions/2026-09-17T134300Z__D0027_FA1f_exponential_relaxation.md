Model/effort: UNVERIFIED. No authenticated runtime model or reasoning-level telemetry was exposed; GPT-6/maximum is requested but not claimed.

# R7-04 admission — D0027

Date checked: 2026-09-17 UTC  
Worker: R7-04 Constructive Model Research  
Native ID: `6aabe7ea6e1881919a65503f8445a813`  
Queue shard: 3, since `sum(ord(c) for c in "D0027") = 269 ≡ 3 (mod 7)`.

## Outside source and exact target

**Fabio Martinelli, Assaf Shapira, Cristina Toninelli**, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461v1 (submitted 23 October 2025), Section 1.1, **Conjecture 2**, source PDF p. 2.

Primary source: https://arxiv.org/abs/2510.20461

The model is the one-dimensional FA-1f process on `Z`. Sites have state `0` (infected/facilitating) or `1` (healthy). Each site refreshes only when at least one nearest neighbour is infected; conditional on a legal ring, the new state is sampled from Bernoulli equilibrium with infection density `q in (0,1)`. The reversible equilibrium is the Bernoulli product law `pi`.

The exact source target is:

> If there is `kappa>0` such that the initial law `nu` satisfies
> `nu(no infected vertices in [-ell,ell]) = O(exp(-kappa ell))`
> for all sufficiently large `ell`, then **for every `q>0`** and every local observable `f`, the convergence
> `E_nu[f(eta(t))] -> pi(f)` is exponentially fast in `t`.

Preserve all quantifiers: every `q>0`, every initial law satisfying the exponential-gap hypothesis, and every local `f`. High-`q` results, deterministic single-infection results, finite-volume mixing bounds, or a theorem requiring extra positive-density/mixing hypotheses on `nu` are PARTIAL.

## Current-source / later-literature check

The arXiv record checked on 2026-09-17 still exposes the 2025 source as the current version located in the bounded search. The abstract explicitly says fundamental non-stationary questions remain unresolved in the low facilitating-density regime. The source itself states Conjectures 1 and 2 are not proved in general and describes existing exponential-relaxation results only above a `q` threshold, with the East model as a contrasting all-`q` case.

Bounded searches run 2026-09-17 for the exact title, `FA-1f Conjecture 2`, `exponential relaxation`, and `all q` found the source and current open-problem summaries, but no later paper claiming the full Conjecture 2. This is **bounded negative evidence only**, not a novelty certificate or claim of bibliographic completeness.

Useful source-side current evidence: Section 6 of the source proves strong ballistic excursion/hitting estimates starting from a single infection. In particular, its Lemma 6.4 gives linear-in-distance hitting times with exponentially small tails and uses a finite-volume FA-1f spectral gap uniformly positive in the interval size. This is partial machinery, not Conjecture 2.

## Prior-attempt recovery

Recovered intake attempt `D0027-A001` from `probability_1000_intake_D_20260908/attempts.jsonl` and the consolidated campaign catalog. It reduced the conjecture toward finite-volume relaxation: if a box of radius `ell` containing an infection could be relaxed in time `T(ell,q) <= exp(o(ell))` uniformly over relevant initial configurations, the exponential initial-gap tail could potentially be balanced against relaxation. The attempt explicitly stopped at the absence of a uniform all-`q` estimate of the required kind and the non-attractiveness obstruction.

This run must not present that reduction as new. A sharper quantitative gluing condition will be developed in the first research report.

## Ownership / alias / exclusion check

Captured fresh master immediately before admission work: `17599c4de8996c57fdd7e57f6a7e1e18e5734ca5`.

At that snapshot:
- direct fetch of `operations/claims/D0027.md` returned 404;
- exact-title / `D0027` repository searches recovered only intake/catalog/attempt material and no canonical claim or worker report owning the target;
- `POSTED.md`, campaign `INDEX.md`, `RANKING.md`, and the visible fleet material did not mark D0027 PROVED, REFUTED, KNOWN, posted, retired, held, or assigned;
- R7-04 had no previous own report.

A fresh claim probe is still mandatory immediately before creating the canonical claim because other workers are concurrent.

## Classification

**CLOSABLE OUTSIDE.** This is a recent, sharply stated, one-dimensional source conjecture whose desired output is a short quantitative theorem rather than a classification programme. The source already supplies ballistic-front and finite-volume spectral-gap machinery. This classification is about research shape, not a claim that the conjecture is easy.

The same shard also contains D0045 (Virág's random-versus-deterministic orthogonal-polynomial Question 7), but current 2020–2026 characteristic-polynomial / stochastic-Airy literature substantially overlaps its operator-limit content, so D0045 was not admitted without a narrower source-status adjudication.

## Frozen metric and closure criterion

Frozen metric:

`E_FAexp in {0,1}`.

Baseline: `E_FAexp = 0`.

It moves to `1` only after a complete source-valid proof or counterexample decides Conjecture 2 with **every `q>0`**, every initial law satisfying the exact exponential no-infection-gap hypothesis, and every local observable. A theorem for the single-infection start, for `q` above a threshold, or under stronger initial-law assumptions is PARTIAL and leaves `E_FAexp=0`.

Full closure additionally requires the campaign protocol's dated prior-art reconciliation, any exact/certified finite core, actual independent P26 plus one distinct OTHER-track audit, and a self-contained source-matching paper package.

## First research methods

- **B2 — attack the negation first:** isolate the extremal legal initial laws, especially a single infection, which already satisfies the source tail hypothesis.
- **B18 — say it in another language:** translate exponential local relaxation into a quantitative `distance-to-nearest-infection` gluing estimate and into front/interior forgetting.
- **B25 — count the same thing twice:** split an arbitrary initial law according to the nearest-infection radius and optimize the two exponential costs exactly.

Status after admission screen: **OPEN / PENDING CANONICAL CLAIM**.