# D0034 work log

2026-11-13T04:59:36.086526+04:00 — Started literature-first investigation of Bradley Question 6. Read startup memory index and compute state (status ok); no subagents. All writes confined to this workspace as requested; live brain/mesh/checklist stores outside it are not modified. No background tasks or publication. Shell research work runs at nice 10.

Exact source checked online: Section 3.3, journal p. 122, PDF p. 16. The known negative examples are psi-star-mixing, not psi-mixing.

Saved original survey, Berbee–Bradley (1984), Holroyd–Liggett, and Holroyd–Hutchcroft–Levy PDFs and extracted texts. Read Berbee–Bradley Lemma 4.1 and Remark 4.3: its product-minorant obstruction is explicitly satisfied by psi-mixing processes. Therefore applying that obstruction to 1-dependent colorings cannot settle the question.

Resource check: inherited OS nice is 15. Requesting an additional nice increment reports Operation not permitted; actual process priority remains 15, already below normal and at least 10. No numerical workload or extra workers.

Saved interim REPORT.md with status PARTIAL and the verified literature distinctions before proceeding to mathematical analysis.

2026-11-13T05:08:59.232057+04:00 — Completed literature screen and mathematical report. OpenAlex cursor pagination initially returned HTTP 401; ordinary page pagination succeeded without credentials. Five saved pages contain 929 distinct citing works, including 671 available abstracts. No candidate resolution found by title/abstract screening; 258 abstracts missing and full-text coverage incomplete.

Read Berbee (1986, 1987) and Spinka (2020) relevant statements. Publisher contents obtained for Bradley (2007); full books unavailable. Original 1989/1993 block-factor PDFs returned non-PDF gateway responses, so report explicitly distinguishes primary metadata from full-text reading.

Mathematical analysis: proved failure of iid past-chain irreducibility; derived absolute regularity of mixing Harris observations, including periodic hidden chains; verified every psi-mixing process passes the original product-minorant test; supplied iid block-window and finite-order Markov positive cases. OR bridge example checked by 16-case exact enumeration and independently by conditional probabilities 1/8 divided by 3/4. These do not solve the universal representation problem.

Final REPORT.md status PARTIAL. Audited definition, quantifier order, period, state-space scope, beta normalization, coding integrability, unique citation counts, and PDF page location. Saved SHA-256 manifest. No universal construction or counterexample, and no claim of exhaustive literature resolution.

Final resource measurement: /usr/bin/time -l could not read sandboxed kern.clockrate (the example computation itself completed). Switched to Python resource.getrusage; direct reruns both exited 0. Measured peak Python RSS: exact checks 15024128 bytes; cached citation screen 53051392 bytes. Both inherited nice 15. Citation rerun used saved pages and made no network calls.
