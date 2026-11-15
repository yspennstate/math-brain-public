# C0153 work log

Task received 2026-11-13, approximately 10:34 +04 (Asia/Tbilisi): “Open problem C0153.”

## 2026-11-13 10:35 +04 — literature first

Read the startup memory and recalled prior random-cluster work. Compute governor reports status ok. No helpers, simulations, publication, git operations, or external messages started. The current task's instruction to work only in this directory supersedes global requests to write checklist, mesh, and brain state outside it; coordination records stay here. Initial literature search finds a directly relevant paper by Basak–Dembo–Sly (arXiv:2312.16008) and a 2025 follow-up by Du–Zhou (arXiv:2505.24283). These are leads, not yet conclusions. Fetching the actual statements and Pete's current source next.

Only plain-text paper extractions will be stored. PDF responses are parsed from memory, without creating PDF files or page images. All shell research programs run at nice 10, with numerical thread counts limited to one.

## 2026-11-13 10:39 +04 — exact question and decisive theorem located

Pete's live URL returns the April 3, 2024 notes, 243 PDF pages. Question 14.19 is on printed/PDF page 215. It asks about all FK(p,q) models; there is no restriction to a percolative regime and no exclusion of the free measure. The following paragraph explicitly asks whether the limit can be strictly dominated by wired.

Basak–Dembo–Sly, arXiv:2312.16008v2, Theorem 1.12(ii), pp. 6–7, gives a FREE local limit in the nonuniqueness/disordered region, under Assumption 1.4 (p. 3). For d-regular locally tree-like zero-field graphs this assumption is supplied by Bencs–Borbényi–Csikvári, Theorem 1.1. Helmuth–Jenssen–Perkins already supplies a direct older result for d>=5 and sufficiently large real q: Theorem 1(4), arXiv p. 5, with beta_u<beta_c discussed on p. 6. Verifying published pagination and an exact small-parameter example before finalizing. Per the user's step-1 stopping rule, no Monte Carlo campaign will be run once verified.

The shell already inherits nice 10 (verified by os.getpriority). Calling `nice -n 10` attempted to add another 10 and was denied by the sandbox; the lightweight fetches still ran at inherited nice 10. Subsequent programs preserve that setting directly. No heavy computation has run.

## 2026-11-13 10:49 +04 — published resolution and exact witness saved

Retrieved the BDS version of record as plain text. Theorem 1.12(ii) is on article/PDF p. 8; the final version uses Proposition 1.4 rather than v2's assumption. BBC Theorem 1.1 is on published p. 205. Both the hypothesis and B=0 normalization were checked. REPORT.md now begins RESOLVED_IN_LITERATURE and contains the theorem application, an exact rational witness q=3, p=17/23, and an explicit high-girth finite cubic Cayley sequence.

code/verify_witness.py passed: wired message (9/17,4/17,4/17); free density 17/35; wired density 113/215; gap 12/301; exp(2(Phi_free-Phi_wired))=14749/14739>1. Independently checked the wired density by summing endpoint-color weights and the pressure sign by direct logarithms. Data saved to data/witness_verification.json. Monotone BP iteration is only an audit, not a substitute for the exact inequalities.

Found and read 2025 Can–van der Hofstad, Du–Zhou, and Borbényi talk texts, plus 2026 Blanca–Gheissari–Park–Zhang. Important scope distinctions: BBC proves a pressure limit, not on its own a local-law limit; Borbényi's broader noninteger-q local result is marked ongoing work; Du–Zhou's displayed critical theorems use positive external field. The report will not silently extend these to unsupported zero-field critical claims. No sampling campaign follows the verified step-1 stop.

## Final audit — completed

REPORT.md records the negative resolution, the theorem and exact published page, the open q=3 cubic counterexample interval, the rational witness, the deterministic finite cubic Cayley construction, the Ising/FK distinction, and a parameter/scope table. Twenty source extractions are in sources/, all plain text; data/source_manifest.json records URLs, response hashes and text hashes. No PDF or image was retained. Local artifact links and Python syntax checked. Exact arithmetic and the independent density/pressure checks passed; data/witness_verification.json records nice=10. Scripts now also ensure nice>=10 when invoked from another shell.

Retrieval limitations: Pete's URL timed out in the browser tool but succeeded through in-memory HTTP retrieval; the direct HJP publisher path returned HTML and NSF timed out, so its arXiv and author-manuscript texts were used with explicitly versioned page references. The Lyons PDF URL redirected to HTML; a guessed Jonasson author URL timed out. Neither unavailable full text is used as proof. The source manifest includes successful text extractions only.

No Monte Carlo campaign was run, in accordance with the explicit step-1 stop after a published theorem decides the question. No background work, publication or pushes remain. All task artifacts were written only inside this workspace; no global checklist, mesh or memory writes were made by this task's code.

Task: “Open problem C0153.” Received 2026-11-13, approximately 10:34 +04 (Asia/Tbilisi).
