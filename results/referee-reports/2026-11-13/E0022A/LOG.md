# E0022 work log

- 2026-11-13T10:58:15.703800+04:00: Started E0022: literature first, then analytic criteria and complete proofs of partial results. No subagents, publication or pushes.
- Workspace restriction: all task writes stay here; global mesh/checklist/memory writes are excluded by the user's directory-only instruction. Read startup memory, brain navigation, mesh protocol and compute state (status ok). Global coordination has not been registered; no private mesh is represented as the shared mesh.
- Located survey: Hu–Sun, arXiv:1908.06825 (2019), published Acta Math. Sin. 37 (2021), 491–508.

- 2026-11-13T11:01:42.326604+04:00: Survey text saved with all 27 PDF-page markers and source SHA256; PDF existed only in memory. Question 1 confirmed on p.15, section 3.2 assumes n>1. Lemma 3.1 p.13 proves forward projection direction; Theorems 3.6 pp.16–17 and 3.7 pp.17–18 give conditional converses.
- Important source correction: Remark 3.8 p.18 adds an orthogonal-complement projection hypothesis to the 2018 sums paper Lemma 3.5; its unrestricted printed lemma must not be used. Sum/compound-Poisson theorem remains valid.
- Read relevant brain scar about sector failure: an unbounded sector ratio is not evidence that (H) fails. The prior note contains a heuristic polarity assertion; not adopted as a theorem.
- Shell processes inherit nice 10 (verified by getpriority); nested nice tried to change priority and was denied. macOS rejected RLIMIT_AS setup, so removed it; small text-only extraction uses bounded downloads (25 MiB) and no heavy computation.

- 2026-11-13T11:20:48.687755+04:00: Literature inventory and full analytic/proof sections saved in REPORT.md. Conditional proofs: uniform directional sector with resolvent densities; finite jumps outside a subspace containing the Gaussian range; symmetric stable noise plus drift/compound-Poisson family. These rederive known consequences; no novelty or general resolution claimed.
- Independently noticed that the literal 2018 Lemma 3.5 also omits Gaussian-range containment: the survey coordinate Gaussian example refutes a repair that adds only the complementary projection hypothesis. The report explicitly retains the Gaussian containment assumption.
- Numerical evidence saved: 196 exact rational covariance identities, four 3,600-direction ray grids, exact/near exceptional directions, and five 720×121 stable-noise grids. All analytic bounds passed; one numerical thread, nice 10, peak RSS 19,021,824 bytes. Finite grids are not proofs of (H).
- Independent pdftotext extraction confirmed statement/page markers but initially failed the plain-text control-byte audit. Removed extraction control characters (also 128 in the 2026 paper from pypdf); source hashes refer to unchanged in-memory PDF input. Re-running the source audit after fixing its sanitizer.

- 2026-11-13T11:23:44.289685+04:00: Final audit passed: independent PDF hash and pp.15–18 statement locators; all 10 source artifacts UTF-8 plain text; no PDFs or page images anywhere in workspace; syntax of all four scripts; all 80 exact energy-identity cases. Proof audit saved as data/proof_audit.txt.
- Publisher 2021 full-text retrieval returned access-denial HTML/403 rather than a PDF. No file was saved from it; report explicitly limits the directly read survey inventory to the 2019 arXiv version.
- DONE for this authorized attempt: REPORT.md starts PARTIAL and records exact question, literature theorems/pages, sufficient/necessary criteria, complete conditional proofs, rejected candidate families, numerical evidence and remaining gap. No general resolution claimed; no publication or pushes. Global brain/mesh/checklist writes remain excluded by the directory-only scope.
