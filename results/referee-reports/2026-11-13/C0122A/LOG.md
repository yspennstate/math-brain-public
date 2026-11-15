# C0122 work log

Task: “Open problem C0122” (received 2026-11-13, approximately 06:13 +04).
Scope: this directory only; no publication, pushes, or subagents.

## 2026-11-13 06:15 +04 — literature first

- Read startup memory and consulted brain recall for Gaussian chaos / multiple valleys. No directly applicable mathematical result was returned.
- Read compute state: owner away, CPU saturation warning. No simulations or heavy jobs started; any subsequent computation will use nice 10 and one thread.
- Shared mesh hello, digest, and write claim were attempted; each failed with `attempt to write a readonly database` (exit 2, not a live-claim conflict). The task's instruction to work only in this directory also precludes updating the shared checklist or brain. Local records serve as the task record here.
- Opened arXiv:0810.4221v2 and arXiv:1311.5592v2. Ding–Eldan–Zhai explicitly identify their Theorem 1.2 as solving Chatterjee's Open Problem 5. Need to check the published version, exact definitions, and implication from chaos before final classification.
- Search queries included Ding–Eldan–Zhai / nonnegative correlations, Chatterjee chaos multiple valleys negative correlations resolved, and the 2014 book / multiple peaks negative correlations.

## 2026-11-13 — resolution and audit

- Saved `sources/chatterjee_0810.4221v2.txt` and `sources/ding_eldan_zhai_1311.5592v2.txt`. PDF bytes were converted in memory with pdftotext; no PDF files retained. URLs and SHA-256 hashes are in `sources/manifest.json`.
- Read Chatterjee's Definitions 1.4–1.7, Theorems 1.8, 3.2, 3.7, the positivity step in equation (11), and Section 12 in full. Read the resolving theorem and its proof route in Section 2.
- Confirmed that Ding–Eldan–Zhai, Theorem 1.2 (arXiv v2 p. 2), explicitly solves Open Problem 5 (p. 3), with [4] identified as the specified Chatterjee preprint. Publication: Ann. Probab. 43(6), 2015, 3468–3493, DOI 10.1214/14-AOP963. Corroborated against Ding's publication list and Eldan's institutional record.
- Journal PDF endpoints and IMS full issue were inaccessible as PDFs; returned HTML. This limitation is disclosed in REPORT.md. The theorem was inspected in the saved version-pinned arXiv source, not the journal typesetting.
- Careful definition check: Chatterjee uses a one-sided covariance bound and height relative to the realized maximum; Ding–Eldan–Zhai use absolute covariance and height relative to its mean. REPORT.md gives the full conversion using Chebyshev and explicit parameters, after chaos implies superconcentration via Chatterjee's sign-independent Theorem 3.2.
- The report's parameter exponents are audited using rational arithmetic and independent direct numeric substitutions in `code/verify.py`; outputs go in `data/verification.json`. This is arithmetic verification, not Monte Carlo evidence.
- The attempted `nice -n 10` wrapper printed a permissions warning. A direct read of process priority showed inherited nice 15, already lower priority than nice 10; the scripts now preserve inherited nice >= 10 and only set 10 if necessary. No CPU-intensive jobs, worker pools, or simulations were run.

Final status: RESOLVED_IN_LITERATURE. Stopped new-research steps under the user's explicit instruction. No pushes or publication; all task artifacts are inside this directory. Shared checklist and durable-brain updates were not made because this task is directory-limited and the shared mesh store is read-only in the sandbox.
