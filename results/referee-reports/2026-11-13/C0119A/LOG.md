# C0119 work log

Task: “Open problem C0119”, received 2026-11-13; work began 06:35 Asia/Tbilisi.

## 2026-11-13 06:36 +04 — orientation and literature first

Read the local startup memory index and compute state. Governor reports throttle/owner present; no simulation or heavy compute planned. Requested nice 10 at launch; the sandbox rejects reprioritization. A direct priority read later confirmed inherited nice 15, which is less intrusive. Text extraction uses one thread per process. No subagents, publication, pushes, or external messages. The task's specific instruction to work only in this directory takes precedence over global requests to mutate the shared checklist, mesh, or brain. Relevant recall was attempted; it is advisory only.

Confirmed arXiv:0810.4221v2 (16 December 2008), 63 pages. Began checking Alexander–Zygouras (2013), Graham (2010/2012), Chatterjee (2014 and 2022), and later chaos/localization work. PDFs will be downloaded only into process memory and piped to pdftotext; only extracted plain text is saved.

Provisional status: no conclusion yet. In particular, finite-temperature free energy superconcentration is not automatically a theorem about zero-temperature ground states.

## 2026-11-13 06:37 +04 — decisive literature result

Read arXiv:0810.4221 Sections 1, 3.1, 8, and 12(2). The actual problem is Gaussian ground-state chaos; it does not say finite temperature or impose a low-temperature phase. Its dimension convention counts total lattice dimension (the proved case is 1+1). Definition 1.5 and Theorem 3.2 make the small-OU-time overlap criterion exact.

Read Graham arXiv:0909.1352v3, Section 6, Theorem 6.1, preprint p.14 and proof pp.14–15: O(N/log N) ground-state variance on BOTH the orthant graph and nearest-neighbor space-time graph in every total dimension d>=2. The introduction, pp.3–4, explicitly identifies Chatterjee's higher-dimensional question and answers yes. This settles original C0119 by Chatterjee Theorem 3.2. No new attack or simulation is needed.

Read Alexander–Zygouras arXiv:1204.1819v2 Theorem 1.1, p.2: exponential tails at scale sqrt(N/log N), for point-to-line, simple-random-walk polymers in every spatial dimension, nearly gamma disorder and E exp(4 beta |omega|)<infinity. Gaussian disorder meets these hypotheses for every fixed finite beta. Integration gives Var(log Z_N)<=C N/log N. The OU gradient identity then gives finite-temperature small-overlap chaos as well. Chatterjee 2021/2022, Section 2.4, Theorem 2.4, p.9, independently confirms both attributions and supplies another finite-temperature proof.

Resource check: shell nice(10) emits a setpriority denial because the inherited nice level is already 15 (verified with os.getpriority). Work remains at nice 15, one thread per extraction, below 4 threads total. Only text files have been retained.

## 2026-11-13 06:43 +04 — report and bibliography audit

Saved the full report with status RESOLVED_IN_LITERATURE. It contains the exact ground-state closure, a self-contained finite-temperature OU proof including monotonicity and the converse, and the published variance theorem's hypotheses. Rechecked beta-squared, OU time normalization and tail-integration constant by a second derivation (Hermite expansion and direct tail integration). The explicit result is Q_n(t)/n <= C/((1-exp(-t)) log n), for every fixed positive finite beta and every spatial dimension.

Obtained Alexander–Zygouras's actual 28-page journal text and verified Theorem 1.1 on journal pp.2–3. Graham's publisher page confirms online date 6 October 2010 and issue pages 687–702 (2012); theorem numbering and precise page citations in the report refer explicitly to his accessible arXiv v3, not guessed journal offsets. A publisher PDF attempt returned HTML and was not saved. Some book/page fetches timed out or required subscription; no inaccessible theorem statements are claimed as read.

Searches included Chatterjee's 2014 book and disorder-chaos papers; Comets's 2017 book; Wei-Kuo Chen's spin-glass chaos work; Ganguly–Hegde and Basu–Ganguly–Hammond-related planar LPP papers; Bates–Chatterjee's endpoint and Gaussian localization papers; Bates's full-path localization; Lacoin's low-dimensional free-energy work; Junk–Lacoin 2024 and the 2025/2026 extension to unbounded environments; general-dimensional resampling LPP chaos; and July 2026 continuum temperature chaos. Full texts or publisher/author abstracts consulted are distinguished in REPORT.md. The full books were not accessible; the saved 2012 Nica lecture transcription is not represented as the 2014 book.

The final bibliography check corrected two draft metadata errors: the surface-growth article's publisher page gives RSA 62 (2023), 304–334; the endpoint preprint actually retrieved is v5, not v3. Neither affects the closure. The 2025 Junk–Lacoin extension, published Orbita Mathematica 3 (2026), 89–125, removes the earlier upper-bounded-environment restriction under its stated exponential-moment assumptions; this is kept distinct from chaos.

No new open-problem attack or simulation was run after confirming the literature resolution. All retained source files are plain text. No publication, git push, subagent, or external communication occurred.

## 2026-11-13 06:44:23 +04 — final verification

Ran `python3 code/audit_sources.py`: 15 source hashes/page counts and 16 theorem/page anchors passed. Report starts exactly RESOLVED_IN_LITERATURE. No PDF/image files found. Inherited nice remains 15. Data audit is saved in data/audit.json. Final proof audit found no remaining gap in the Gaussian free-endpoint statement.
