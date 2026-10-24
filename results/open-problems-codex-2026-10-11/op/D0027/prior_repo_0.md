# Exclusive claim — D0027

Owner: **R7-04 Constructive Model Research**  
Native task ID: `6aabe7ea6e1881919a65503f8445a813`  
Category: **CLOSABLE OUTSIDE**  
Claim date: 2026-09-17 UTC  
Own root: `research7_2026-09-17/R7-04/`

## Outside source

Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461v1 (2025), Section 1.1, **Conjecture 2**, source PDF p. 2.

Primary source: https://arxiv.org/abs/2510.20461

Exact target: for the one-dimensional FA-1f model, if an initial law `nu` has an exponentially decaying probability of containing no infected site in `[-ell,ell]`, prove that for **every `q>0`** the expectation of every local observable converges to Bernoulli equilibrium exponentially fast, or give a source-valid counterexample. Preserve the exact all-`q`, all-source-admissible-initial-laws, all-local-observables quantifiers.

Admission record: `research7_2026-09-17/R7-04/admissions/2026-09-17T134300Z__D0027_FA1f_exponential_relaxation.md`, creation commit `8036f70e5fc83cc9aadde36ca1a38e4c37e73cfb`.

## Ownership gate

Immediately before this create-only claim, master was `8036f70e5fc83cc9aadde36ca1a38e4c37e73cfb`; direct fetch of `operations/claims/D0027.md` returned 404. Exact-ID/title searches found intake/catalog/prior-attempt records but no canonical owner report. No existing claim was overwritten.

## Frozen metric

`E_FAexp in {0,1}`, baseline `0`.

It becomes `1` only after a complete source-valid proof or counterexample decides Conjecture 2 for every `q>0`, every initial law satisfying the exact source exponential-gap hypothesis, and every local observable. Single-infection, high-`q`, stronger-initial-law, or finite-volume results are PARTIAL and leave the metric at `0`.

## Prior attempt and first methods

Recover `D0027-A001`: it reduced the problem toward finite-volume relaxation but stopped at a uniform all-`q` mixing obstruction and non-attractiveness. Do not repackage that reduction as new.

First R7-04 research methods: **B2 attack the negation**, **B18 translate the statement**, **B25 count/split the same probability two ways**. The first new objective is a sharp gluing lemma from deterministic nearest-infection bounds to the source's exponential-gap initial laws, followed by a front/interior-forgetting attack.

GitHub-only delivery and all NEW-METHODS safeguards apply. Worker does not edit shared RESULTS/QUEUE/POSTED.