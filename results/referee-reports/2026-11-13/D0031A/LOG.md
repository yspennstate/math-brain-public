# D0031 work log

Task received: “Open problem D0031”, 2026-11-13, approximately 04:29 +04 (first local clock reading 04:29:40).

## 2026-11-13 04:30 +04 — setup and literature stage

Working only in this directory, without subagents, publication, or pushes. All local research commands use nice 10; no heavy computation planned. Startup memory and compute state read; machine reports warn/owner_away_open, so keep work lightweight. The later directory restriction takes precedence over global brain/mesh/checklist writes outside this directory; this log records task progress locally.

Plan: download and read Bradley (2005), trace its references and later citations through 2026, then either document a verified published resolution or attempt a rigorous partial result/construction. Search-engine timestamps are not publication dates. No claim of resolution from search absence.

## 2026-11-13 04:33 +04 — source checks

- Survey downloaded from arXiv and Section 2.5–2.7 plus Markov/Gaussian sections read. Question 3 is on printed p. 117 / PDF p. 11; the definition starts on p. 116.
- Bradley (2010), ALEA 7, p. 382 explicitly identifies the real-state example as book Vol. 2, Theorem 24.14; absolute regularity obstruction is Vol. 1, Proposition 5.17. Book publisher table of contents saved. Full book text not obtained yet.
- Downloaded the 2023 Kułaga-Przymus–Lemańczyk paper, 2020 Oberwolfach workshop report, Lyons FIID paper, and Lemańczyk thesis as follow-up sources. None so far supplies a finite-state rho-mixing resolution.
- AMS PDF requests returned 403. Springer requests for the 1975 and 1996 full papers returned HTML access pages, retained with .html extensions; they are not PDFs and have not been read as full papers.
- A third-party citation pointed to DTIC ADA160322. Title-page check shows this is Bradley–Bryc–Janson, Remarks on the foundations of measures of dependence, not the bilateral paper. Excluded as evidence; retained original download to document the mismatch. Archive title search found the correct identifier, ADA152856, now downloading.
- Scheduling checked using os.getpriority: inherited nice value is already 10. Sandbox denies setpriority/ps, so extra nice invocations merely emitted warnings; no scheduling escalation or heavy work occurred. Subsequent children inherit nice 10.

## 2026-11-13 04:35 +04 (approximate) — original construction recovered

Correct original preprint downloaded: UNC Center for Stochastic Processes TR 91B (February 1985), DTIC ADA152856. Read Theorem 1, Lemma 2, equations (2.3)–(2.11), Claims 1–7, and stationarization (3.1)–(3.4). Rendered and visually checked printed p. 13 to settle indices obscured by OCR.

Key deduction to prove in REPORT: the stationary coordinate contains Y_0^(k); its decoded W_0 bits are iid fair. For each M these form an iid M-bit factor over time k. Thus this construction has infinite Kolmogorov–Sinai entropy and cannot admit a finite generator. This is an obstruction for this construction and invertible recodings only, not for its noninvertible finite factors or for the open problem in general.

Searches through dated 2026 material still yield no verified resolution. The 2026 Denker survey (arXiv:2606.17857v2) has no occurrence of bilateral determinism and supplies no answer. Full BDS paper and full 2007 book remain access limitations; identify exact references from primary abstracts and Bradley’s own later cross-references, without pretending to have read inaccessible text.

## 2026-11-13 04:42 +04 — proofs and computation saved

REPORT now contains full restricted proofs: positive entropy bound, beta and rho-star obstructions, infinite-entropy iid factors of the original construction, finite-order Markov impossibility, Gaussian double-tail triviality and its bounded-window factors, scalar Haar/linear subgroup obstruction, and an infinite masking-channel example explaining the nonlinear decoding gap.

Exact rational computation checked 18 finite masking-channel cases, with Bayes errors independently recomputed as binomial tails. No infinite-process conclusion is inferred from the numerical checks. Search notes record queries, primary sources, inaccessible full texts, and rejected wrong-source downloads. Final audit next: inspect every proof dependency, first-line status, local links, source identities, formula signs/indices, and file hashes.

## 2026-11-13 04:43 +04 — reference audit correction

Crossref lookup rejected an initially inferred AMS DOI suffix. Exact-title Crossref search identifies the correct journal DOI as 10.1090/S0002-9947-1986-0819945-0 (also JSTOR DOI 10.2307/2000128), not the guessed suffix -2. Corrected REPORT and search notes; exact-title metadata retained. The preprint DOI is 10.21236/ADA152856. Journal PDF request now repeated using the verified identifier. This correction affects the link, not the verified title, pages, or preprint proof.

## 2026-11-13 04:44:17 +0400 — final audit and result

Status PARTIAL. No literature resolution verified and no general existence or impossibility proof obtained. Restricted proofs have been checked for scope: the Gaussian result uses Gaussian conditional laws; the linear result uses a scalar closed subgroup and Haar law; the finite-factor entropy argument excludes only invertible finite generators of the original construction. Fixed a statement about rare shared events to specify two-atom generated fields, since richer fields can have larger alpha. The finite channel table was independently derived by binomial majority voting as well as exact joint probabilities.

The correct AMS DOI was confirmed by Crossref; even the corrected journal PDF URL returns 403, so direct proof inspection relies on the original technical report. Full BDS/book access limitations remain explicit. All report local links and TeX delimiters passed checks; all retained PDFs have valid PDF signatures. Source SHA-256 manifest refreshed (33 files). Computation uses one standard-library Python thread and inherited nice 10; audit process RSS measured about 28 MB, far below 4 GB. No publication or pushes.

Task done for this attempt: “Open problem D0031”, received approximately 2026-11-13 04:29 +04. Deliverables: REPORT.md, LOG.md, sources/ with search notes and manifest, and code/ with exact finite checks. General problem unresolved by this work.
