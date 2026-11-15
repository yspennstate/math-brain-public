# E0057 work log

Task received 2026-11-13, approximately 08:56 +04 (Asia/Tbilisi): “Open problem E0057.”

## 08:58 — orientation and scope

- Read the shared identity memory and compute governor. Governor status warn, mode owner_away_open; CPU saturated. Use one worker, nice 10, numerical libraries capped at one thread, no heavy sweep.
- Shared mesh hello/digest could not run: shared database is read-only in this sandbox. No live claim could be made. All task writes stay in this isolated directory, as expressly requested; no global checklist/memory writes attempted.
- Literature first. Need distinguish joint signal/shift quasi-MLE from marginal mixture MLE. Source's uniform-versus-arbitrary shifts and Fourier power correction must be read directly.
- Preliminary bibliographic correction: Abbe et al. 1710.02793 states sigma^4 for unknown aperiodic shifts, not sigma^2. Dihedral paper has different authors (Bendory–Edidin–Leeb–Sharon).
- No PDFs or images will be written to disk: download PDF bytes in memory, parse to plain text with page separators, retain text and provenance only.

## 09:01 — primary sources saved and estimator distinction confirmed

- Saved full lecture notes in text. Read Section 10, PDF/printed pp. 132–140; equations (108)–(110), pp. 136–137 define arbitrary unknown shifts and the pairwise joint alignment objective. Open Problem 10.4 is exactly p. 139 in this version.
- Saved named papers, with page markers and SHA256 provenance, using in-memory PDF parsing. Read Brunel Theorem 9 and proof (PDF pp. 9–10): all-signal marginal-MLE consistency. Generic sample complexity lower and upper bounds are Perry et al. Theorems 3.1 and 4.3.
- Important model difference: Bandeira–Rigollet–Weed's main rate results are for continuous phase shifts. Its Appendix B explicitly treats discrete cyclic shifts.
- Found the primary 2025 revision of Shahverdi–Ström–Andén, arXiv:2409.04868v2: population loss conjecture on the phase manifold remains. Need inspect exact scope before any conclusion.
- launch.sh already starts this Codex process at nice 10. A redundant child nice request was denied by the sandbox; children inherit the launch priority. Numerical libraries will be capped to one thread.

## Mathematical and numerical results, saved during work

- Report classification remains PARTIAL. Wrote complete proofs of (A) all-signal marginal-MLE strong consistency with arbitrary fixed shifts and consistently estimated-power constraints; (B) quasi-MLE uniform law and population-argmin reduction; (C) a 2 sigma sqrt(L) hard-alignment error bound; (D) single-Fourier-pair discrete moment order q and sample exponent 2q. These are standard/known consequences, not claimed novel resolutions.
- Confirmed inherited process nice=10 by os.getpriority. Explicit RLIMIT_AS requests were rejected by Darwin/sandbox; dimensions stay small and RSS is checked. One numerical thread, one experiment worker.
- First run: 168 data sets, 672 fits, 275 MB peak RSS; BLAS emitted arithmetic-status warnings although every saved result was finite. Replaced matrix multiplications with direct einsum contractions and recomputed the full experiment to resolve that concern. Second run finished without warnings: 267,599,872 bytes peak RSS; 79.17 user CPU seconds.
- L=5, sigma=.5 marginal median relative squared errors .016209 (n=200), .000863 (2000), .000104 (20000). Hard corrections improve strongly, but high-noise finite hard-iteration outputs do not uniformly follow sigma^6 collapse. These are local optimizers with two starts, not certified global solutions.
- Cubic invariant variance experiment: 100 repetitions x 20,000 samples at six noise levels. High-noise log-log MSE slope 5.911393961. Exact variance checked independently by multiplying Gaussian fourth and second moments. All raw summaries and seeds saved.
- Retained latest arXiv 2505.21435 is a 151-page revision dated 12 February 2026 with a changed title; the 2025 search abstract is not used to misidentify its theorem numbers. Retained 2409.04868v2 PDF uses section theorem numbering, unlike its HTML: Conjecture 3.8 and Theorem 3.9 in PDF correspond to Conjecture 23 and Theorem 24 in HTML.

## 09:13 +04 — final audit and completion

- Final classification: PARTIAL. General corrected quasi-MLE consistency remains unproved and unrefuted here; published marginal-MLE consistency and generic sigma^6 rates are separated from that claim.
- Recomputed the reported slope using scalar covariance/variance regression: 5.911393961125611 versus the original 5.911393961125613. Independently evaluated the mixture objective and its gradient: errors 4.44e-16 and 4.32e-11 respectively. Confirmed 168 unique cases / 672 estimates, all finite.
- Corrected bibliographic page mismatches during audit: Romanov Theorem 2.2 is PDF p.5; projected-MRA Theorem 1.1 and Corollary 1.2 are PDF p.5, precise Theorem 3.1 p.11. Confirmed retained manuscript lengths against actual extraction rather than inferred publication lengths.
- Verified source SHA256 hashes, first REPORT.md line exactly PARTIAL, and absence of PDFs or paper images anywhere in this directory. Source provenance and detailed reading record are in sources/manifest.json and sources/LITERATURE_AUDIT.txt.
- All requested artifacts are local. No publication, push, external messages, extra agents or persistent worker processes were created. Shared mesh/checklist/brain writes remained unavailable and were not bypassed.

Task: “Open problem E0057” — received 2026-11-13 approximately 08:56 +04; report completed 09:13 +04.
