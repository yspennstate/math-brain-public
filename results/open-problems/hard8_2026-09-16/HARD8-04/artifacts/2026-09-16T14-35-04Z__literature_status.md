# HARD8-04 dated literature/status audit — 2026-09-16

## Outside problem statement

Primary fleet source: Afonso S. Bandeira, Anastasia Kireeva, Antoine Maillard, Almut Rödder, *Randomstrasse101: Open Problems of 2024*, arXiv:2504.20539, Conjecture 14. The source target is the unrestricted Hadamard conjecture: every positive order divisible by four admits a real Hadamard matrix.

Current source page: https://arxiv.org/abs/2504.20539

The full conjecture remains OPEN in the sources checked on 2026-09-16.

## 2026 finite-order update below 2000

The owner warned that 668 is obsolete as an open finite target. This is confirmed by current evidence. OEIS A019442/A007299 were updated 12-13 August 2026 to record Levent Alpöge, Philippe Voinov, Saul Reynolds-Haertle and Claude constructions at the twelve formerly missing orders

`{668,716,892,1132,1244,1388,1436,1676,1772,1916,1948,1964}`.

Current records:

- https://oeis.org/A019442
- https://oeis.org/A007299
- https://vibemathed.com/problem/hadamard-matrix-of-order-668
- https://hadamard-668.vercel.app/

This track does not claim novelty for any of those orders. The neighboring P15 report `proofnet24/P15-hadamard/runs/2026-09-16/2026-09-16_15-24-44__run-report.md` independently reconstructed the published order-668 cyclic difference-family matrix and checked `HH^T=668 I` exactly with the published row-major hash. That exact validation is reused by path/commit rather than repeated here.

## The order-2060 status gate

Cati--Pasechnik, *A database of constructions of Hadamard matrices*, arXiv:2411.18897v2, is the most useful construction-status source recovered here:

https://arxiv.org/abs/2411.18897

Its Table 4 records `515(3)`, meaning the database has a construction at `2^3*515=4120` but not a verified `2^2*515=2060` construction. More importantly, Sect. 6 explicitly says that Sect. 7 of Masahiko Miyamoto, *A construction of Hadamard matrices*, JCTA 57 (1991), 86-108, claims some orders that their tables still list as unknown, giving `4*515` as an example; Cati--Pasechnik say they could not verify those claims because details are missing.

Therefore `2060` is **source-supported as a current candidate target but not yet certified here as genuinely unresolved**, because a historical existence claim remains unaudited. This report does not promote web silence into a nonexistence/status theorem.

The implemented Miyamoto theorem summarized by Cati--Pasechnik and SageMath is: for prime-power `q == 1 mod 4`, if `H(q-1)` exists then `H(4q)` exists. This theorem does not directly apply to 2060 because `q=515=5*103` is not a prime power. Source: https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/matrices/hadamard_matrix.html .

A related Seberry--Yamada M-structure paper is also important for avoiding a false status inference:

https://documents.uow.edu.au/~jennie/WEBPDF/139_1990.pdf

Its 8-Williamson route produces 8-Williamson matrices at order 515 in the relevant family and an associated Hadamard matrix at order `8*515=4120`, not `4*515=2060`. Thus that accessible 515 construction does **not** settle H(2060). The same paper notes that ordinary four-Williamson matrices were not known for several related orders (including 103 in its list), so a Cooper--Wallis factorization through a Williamson order 103 is not licensed by that source.

## Current 2026 Williamson search literature

Kharaghani--Mohammadian--Tayfeh-Rezaie, *A search for Hadamard matrices of Williamson type*, arXiv:2605.08661 (May 2026), searches a near-Williamson class only through small odd orders and proves existence in that class through 63. It does not supply an order-515 Williamson/near-Williamson object or H(2060).

Source: https://arxiv.org/abs/2605.08661

## Exact bounded searches performed on 2026-09-16

Search strings included:

- `"order 2060" Hadamard matrix`
- `"2060" Hadamard Goethals Seidel`
- `"2060" Williamson Hadamard`
- `"2060" Turyn Hadamard`
- `"Miyamoto" 2060 Hadamard 515`
- `"4*515" Hadamard Miyamoto`
- `"Williamson matrix" "order 103"`
- `"A search for Hadamard matrices of Williamson type" 515`

No later explicit H(2060) matrix was surfaced by those bounded searches. This is evidence only, not a proof of absence from the literature.

## Unresolved access gap

The direct full text of Miyamoto 1991 Sect. 7 was not successfully retrieved in this run: the DOI/Elsevier route exposed bibliographic metadata but the article body was inaccessible through the available web path. Because Cati--Pasechnik specifically identify missing details in that historical `4*515` claim, resolving that source gap is a prerequisite before any future run calls 2060 a *genuinely unresolved* order or assigns metric credit to a 2060 construction.

## Ownership / duplication check

Repository-wide Hadamard search found the active neighboring P15 assignment and this HARD8-04 track, with no third track claiming the same exact H32 multiplier class. P15 exhausted only the H64-multiplier-invariant bordered-GS family at `v=514`; the present run moves to the strictly larger H32-invariant family. Root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md`/`RANKING.md`, and the intake search showed no posted/retired result that closes the unrestricted Hadamard conjecture.
