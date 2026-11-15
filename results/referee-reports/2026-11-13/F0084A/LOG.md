# F0084 working log

Task: “Open problem F0084 … Critical tail behavior”; received 2026-11-13 07:42 Asia/Tbilisi (first recorded local clock 07:42:33).

## 2026-11-13 07:43 +04 — started

- Scope: literature first; then gap analysis, complete proofs of any justified partial results, and evidence-only torus experiments if not resolved in print.
- No subagents, publication, git pushes, or external messages. All task writes confined to this directory. This specific restriction overrides shared-brain/checklist/mesh writes; startup memory, protocol, recall, and governor state consulted read-only where possible. Recall returned no relevant mathematical memory. Its automatic cache publication failed under the sandbox.
- Governor: warn / owner_away_open, host already CPU saturated. Use one numerical worker, nice 10, BLAS/OpenMP thread limits 1. No heavy computation yet.
- Initial searches: original 2006 paper and 2009 follow-up explicitly leave d >= 2 open; follow-up proves a critical bound only in d = 1. Broader search underway.
- Sources will be converted in memory with pdftotext; PDFs will never be written to disk.

## 2026-11-13 07:46 +04 — literature resolution found

- Reading the full HPPS Poisson Matching text (not only the abstract or theorem statement) found the decisive extension: Theorem 6(ii) applies to fair stable Poisson–Lebesgue allocations, explicitly stated on arXiv pp. 7–8; the proof adaptation is on arXiv p. 34 following Theorem 19.
- Bound: P(X > r) <= C(d) r^{-s(d)}, every d >= 1, with s(2) approximately 0.496 and s(3) approximately 0.449. Need verify published page/theorem numbering and exponent equation before final report.
- User explicitly ordered stopping if an upper bound is in print. No simulation or new proof search will follow once this is verified.
- Process niceness was independently checked with os.getpriority: inherited nice 10. Adding nice 10 attempted to raise the numeric niceness further and was denied; resource policy already satisfied.

## 2026-11-13 07:50:17 +0400 — report and verification complete

- Published PDF converted directly from memory to text: 22 pages. Theorem 6(ii) p. 269; explicit Lebesgue–Poisson extension p. 270; Theorem 19 / equation (21) p. 283; proof pp. 283–286; allocation adaptation p. 286.
- Independent corroboration: Markó–Timár (2016), arXiv v3 reprint p. 5 attributes the r^(-0.496...) bound to the stable allocation.
- REPORT.md now begins RESOLVED_IN_LITERATURE and contains definitions, exact references and a complete reconstruction of the published allocation proof.
- code/check_exponents.py evaluated the exponent by beta-function and direct-quadrature methods, with the separate d=2 gamma identity checked. Results saved in data/exponent_checks.json. Maximum method discrepancy across d=2,3,10,100: 4.8e-12; numerical checks are not claimed as interval certificates.
- User stopping rule applied: no simulation, no new research or exhaustive follow-on bibliography. Task complete subject to final file/source audit.

## 2026-11-13 07:51:01 +0400 — final audit passed

- Verified REPORT.md first line exactly RESOLVED_IN_LITERATURE. All 10 retained paper texts match their manifest SHA-256 hashes. No PDFs, PDF signatures, scans, or image files in the workspace. Retained sources total 1,223,289 bytes.
- Rechecked published pp. 269, 270, 283 and 286, and completed the original source section-location audit. No required work remains under the literature stopping rule.
- Done: “Open problem F0084 … Critical tail behavior” (received 2026-11-13 07:42 Asia/Tbilisi): resolved by HPPS (2009), Theorem 6(ii), Theorem 19 and the explicit allocation extension.
