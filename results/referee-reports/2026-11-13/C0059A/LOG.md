# C0059 work log

Task received: Open problem C0059; 2026-11-13 06:59 +04 (session launch).

## 2026-11-13: literature first

- Read startup instructions and compute state. One worker, nice 10 for scripts, no heavy computation.
- All task writes are restricted to this directory. Accordingly no shared brain, mesh, or global checklist state is changed; their usual registration would violate the task-specific directory restriction. This log is the local task record.
- Located Curien's author page and the older cours/peccot.pdf with Chapter VIII and the requested page numbering. Current Saint-Flour link points to Dropbox; versions will be distinguished.
- Initial searches found the dense-phase result in Budd--Curien and explicit statements that dilute dual transience remains open in Curien--Marzouk and Marzouk's HDR. No resolution established yet.

## Literature and source audit

- Saved the complete 104-page Peccot preprint as plain text. The question is on PDF page 93, printed page 89; Chapter VIII is printed pp. 86--90. Its type-2 convention is restricted to the explicit gamma-function family. This is an earlier 2016-course draft, not the 2023 book; do not silently equate versions.
- Downloaded and extracted Budd--Curien (2017), Budd--Curien--Marzouk (2018), Curien--Marzouk (2020, 2021), Gurel-Gurevich--Nachmias (2013), Bjornberg--Stefansson, Budd's peeling paper and mini-course, and Kammerer's relevant 2025--2026 papers. PDFs were processed in RAM; none retained. Provenance and SHA256 values are in data/fetch_manifest*.json and the text headers.
- Budd--Curien: Lemma 3.1, Proposition 5.1, Corollary 5.2, Theorem 4.2, Lemma 6.1. Cauchy paper: Open question 1 (p. 754), Proposition 3 and Theorem 3.
- Searched author pages and targeted combinations of Boltzmann/stable maps, dual, recurrence/transience, resistance growth, Kammerer, Budd, Budzinski--Curien, Bjornberg--Stefansson, and 2024--2026. Relevant recent results concern distances/geodesics or scaling limits; no resolution located. Curien--Marzouk explicitly calls dilute dual transience open.
- The Saint-Flour Dropbox link on Curien's current teaching page returns a deleted-file response. Attempting alternate author/preprint URLs; the source with the requested question and exact PDF page 93 is already saved.
- Existing process niceness is 15. A request to change it to 10 was denied because that would raise priority; scripts remain at nice 15, meeting the intended nice >= 10 constraint.

## Proof work

- Re-derived the dense flow using a quantile bound E[X 1_A] >= P(A)^2/2 for an exponential edge weight X, without assuming A independent of X.
- Distinguished a divergent upper bound on energy from actual divergence of effective resistance. Neither FPP nonexplosion nor summability of the usual layer Nash-Williams lower bound decides the question.
- Working on an explicit sufficient criterion using the tree of newly discovered faces, deleting gluing edges and finite fillings. Its finite uniform-boundary flow energy is a computable functional of the conditioned perimeter walk and uniform cyclic updates. This is a conditional reduction, not a proved subrange.
- Derived an exact rejection sampler for the canonical conditioned perimeter walk using two beta-geometric proposals; no tail truncation is needed. Layer simulation will use the exact (P,D,H) kernel of Budd--Curien equation (34).

## Source recovery and experiment results

- Recovered the complete Saint-Flour draft (252 pages) from https://dl.dropboxusercontent.com/s/bfjbuxiv4ms1gdl/StFlour.pdf and retained text only. Chapter 15, pp. 206--215, was read in full through the recurrence/transience discussion. Open Question 15.10 is on p. 213; Theorem 15.1 on p. 207; Corollary 15.8 on p. 211; Proposition 15.9 on p. 212. Type-a definition: Proposition 5.10, p. 81. The earlier Peccot question really is on PDF p. 93, printed p. 89.
- Corrected a search-engine metadata trap: Budd's mappeeling.pdf is dated 14 May 2017 in the document, although search metadata made it appear recent. Renamed the saved text and fetch entry accordingly.
- Layer experiment: 32 replicates for each a=1.8,2,2.2,2.4, 20,000 steps each (2,560,000 steps total), exact untruncated gamma-family transition law. One computational thread, inherited nice 15; 6.15 seconds reported runtime. CSV data and seed scheme saved.
- Skeleton experiment: 12 replicates per parameter, checkpoints 100/500/2000 steps. Run-length boundary handles huge faces without allocating each half-edge. Kept discovered C-edges and G-edges, omitted finite pockets, wired unfinished half-edges of resistance 1/2. This is not a full Boltzmann map simulation.
- Independent audit: 5,920 layer states agreed with direct cyclic boundary lists; beta-geometric/gamma probabilities agreed within 6.1e-10; proposal acceptance frequencies passed the analytic check; resistor solves agreed with dissipated energy to 3.2e-14 relative error. Analytic chain/parallel examples passed. No inferred asymptotic transience.

## Final audit and result

- REPORT.md starts PARTIAL. It explicitly says no new subrange is settled and no published resolution was located. The partial deliverable is the proved sufficient two-mark/tree-energy reduction, with its remaining condition stated as unproved.
- Rechecked resistance comparison directions, factors of two for half-edges, conditional versus annealed Fatou, frontier escape for the compactness proof, source-page offsets, root digon versus stationary rooted-face degree, and the difference between stable indices a-1 and a-1/2.
- Added the known recurrent dual examples with bounded/exponential face degrees at the generic endpoint; did not assert recurrence for all type-5/2 weights.
- Both numerical programs and the independent audit completed. All local report links resolve; sources contain plain text only; no PDFs retained. Source hashes and full inventory are in data/source_index.json and sources/INDEX.txt.
- Done: Open problem C0059, received 2026-11-13 06:59 +04. Literature review, exact source recovery, conditional proof, layer/cutset analysis, modest simulations, code and data saved locally. The original transience question remains unresolved by this work.
