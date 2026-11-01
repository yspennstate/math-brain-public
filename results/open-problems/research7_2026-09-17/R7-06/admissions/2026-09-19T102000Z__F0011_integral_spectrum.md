Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is not GPT-6 at maximum; no authenticated binding model/effort selector or runtime telemetry is exposed.

# R7-06 admission — F0011 / integral spectrum of a random symmetric sign matrix

Date of admission check: 2026-09-19 UTC  
Slot: `R7-06`  
Native task id: `6aa7f3e486b08191a454c696b45f7ae1`  
Root: `research7_2026-09-17/R7-06/`  
Initial-selection shard: `sum(ord(c) for c in "F0011") = 264 ≡ 5 (mod 7)` — eligible.

## Exact outside source

- Author: **Van H. Vu**.
- Title: **Recent progress in combinatorial random matrix theory**.
- Journal/current bibliographic version: *Probability Surveys* **18** (2021), 179–200, DOI `10.1214/20-PS346`.
- Original preprint: arXiv:`2005.02797`, submitted 2020-05-06.
- Source URLs: `https://arxiv.org/abs/2005.02797` and `https://doi.org/10.1214/20-PS346`.
- Locator: **Conjecture 9.4 (Integral spectrum), Section 9, source PDF p. 15**. Vu's 2020 RMTA slides reproduce the same conjecture under the heading “Conjecture (Integral spectrum)”.

### Model and full quantified statement

Let `M_n^sym` be the random real symmetric `n × n` matrix whose entries on and above the diagonal are mutually independent Rademacher variables, each equal to `+1` or `-1` with probability `1/2`, and whose lower-triangular entries are fixed by symmetry. Then, as `n→∞`,

`P(M_n^sym has an integral spectrum) = 2^{-(1/2+o(1)) n^2}`,

where “integral spectrum” means that **all `n` eigenvalues are integers, counted with algebraic multiplicity**.

This is an asymptotic source conjecture. Full source closure requires both matching upper and lower exponential rates `-(1/2+o(1)) n^2`; a finite classification, a `2^{-c n^{3/2}}` upper bound, or a special family is only PARTIAL.

## Dated source/current-version and follow-up checks

Checked on 2026-09-19:

1. The arXiv record still identifies Vu's preprint `2005.02797`, submitted 2020-05-06; the journal version is Probability Surveys 18 (2021), DOI `10.1214/20-PS346`.
2. Ahmadi–Alon–Blake–Shparlinski, *Graphs with integral spectrum*, Linear Algebra Appl. 430 (2009), proved only an exponential rarity result for integral graph spectra.
3. Costello–Williams, *On the number of integral graphs*, Linear Algebra Appl. 493 (2016), 447–454, DOI `10.1016/j.laa.2015.11.027`, proved an upper proportion `2^{-c n^{3/2}}`; their own current research page still describes the correct exponent as expected to be proportional to `n^2`.
4. Yi Han, *On the rank of a random symmetric matrix in the large-deviation regime*, J. London Math. Soc. 113 (2026), e70581, first published 2026-05-30, proves `P(corank A ≥ k) ≤ exp(-c'kn)` for `1≤k≤c√n`; it cites Ahmadi et al., Costello–Williams and Vu's survey. This strengthens the rank technology relevant to the old multiplicity route but, at `k=Θ(√n)`, remains naturally on the `n^{3/2}` scale and does not state the integral-spectrum conjecture as resolved.
5. Bounded web searches on 2026-09-19 for the exact phrases “integral spectrum”, “random symmetric Rademacher matrix”, “Conjecture 9.4”, Vu, and `2^{-c n^{3/2}}`, including 2021–2026 follow-up terms, did not surface a paper claiming the `2^{-(1/2+o(1))n^2}` result.
6. Bounded later-author/source searches found later work solving other Vu survey conjectures (simplicity/irreducibility/rank questions) but no later Vu-authored source retracting or resolving this integral-spectrum conjecture.

These misses are **negative evidence only**. They do not certify novelty or global openness.

## Repository ownership, aliases, exclusions, and recovered attempts

- Canonical intake row: `probability_1000_intake_F_20260908/problems.jsonl`, `F0011`.
- Exact previous substantive attempt recovered: `F0011-A001` in `probability_1000_intake_F_20260908/attempts.jsonl`.
- That attempt used `tr(M^2)=n^2`, a semicircle/multiplicity pigeonhole, and a reduction to bounding cospectral classes. It explicitly records the obstruction that a single-eigenvalue multiplicity argument reaches only the `n^{3/2}` exponent scale; it also notes that only `2^{O(n)}` integer spectra satisfy the trace-square constraint, so a `2^{o(n^2)}` uniform cospectral-class bound would imply the source conjecture.
- Fresh direct read of `operations/claims/F0011.md` on current master before this admission returned **404 / absent**. Repository search found no competing `operations/claims/F0011.md`; search hits were intake/catalog/attempt material and a CLOSABLE-screen rejection saying F0011 is HARD, not an ownership claim.
- `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `RESULTS.md`, root `POSTED.md`, and the current claim search do not mark F0011 PROVED, REFUTED, KNOWN, posted, held, or retired in this exact source scope.

Therefore the target is admitted as **HARD OUTSIDE / PARTIAL-history / source-open under bounded current checks**. This is not a claim that literature search has proved openness.

## Frozen metric and first concrete milestone

Frozen metric for this successor:

`N_exact := largest n for which every switching-normalized symmetric {±1} n×n matrix has been exhaustively classified by an exact integer certificate as integral-spectrum or non-integral-spectrum, with exact counts.`

Evidence baseline: **UNKNOWN / UNMEASURED**. The recovered `F0011-A001` contains no exhaustive finite `N_exact` certificate, and absence from that attempt is not evidence that no older finite computation exists elsewhere.

First concrete milestone: derive source-valid arithmetic and switching obstructions, then produce a **no-floating-point exhaustive certificate through at least `n=7`** if feasible in this run. Movement in `N_exact` is a finite milestone only; it does not resolve the asymptotic conjecture.

## Initial attack

Start with the required new-target obstruction search and the preferred nonrepeating triple:

1. **B2 — attack the negation / arithmetic obstruction:** reduce the characteristic polynomial modulo 2 (and derive any resulting 2-adic coefficient/eigenvalue restrictions).
2. **B14 — exploit group symmetry:** quotient diagonal sign-switching `M↦DMD`, prove the orbit/canonical-normal-form count exactly, and ensure no integral matrices are lost.
3. **B16 — exact small cases:** enumerate the quotient with integer arithmetic only; certify candidate integer spectra from trace/power identities/Newton identities; no floating eigenvalue acceptance.

Mathematical status at admission: **OPEN / no source-level resolution claimed**.
