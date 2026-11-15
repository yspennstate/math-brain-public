# Independent referee log

Task: “Break it if it is wrong” — F0126 partial claim audit. Received 2026-11-13, approximately 10:02 +04 (Asia/Tbilisi); first shell timestamp 10:03:34 +04.

## 2026-11-13 10:04 +04 — scope and orientation

- Read the submitted REPORT.md, LITERATURE.md and LOG.md. Treat their references and numerical claims as unverified reports.
- Read startup memory and mesh protocol; consulted brain recall and compute state. Compute state is okay/owner away. No subagents. Resource limits: one process/thread for numerical work, nice >=10, comfortably below 4 GB.
- All task outputs stay in this directory. The explicit directory restriction precludes writes to the external mesh, checklist and brain databases; local task tracking is here. Submitted claim files remain untouched.
- Located the actual 13-page published survey at https://arxiv.org/pdf/math/0608219. Older institutional versions are not interchangeable with it.
- Initial proof reading finds no algebraic fault. Main questions: exact scope of equivalence; proper-subgroup versus nonirreducibility; measurable success events; novelty versus elementary kernel invariance.

Checklist: primary source extraction pending; proof audit in progress; independent computation pending; literature audit in progress; report pending.

## 2026-11-13 10:08 +04 — main findings

- Independently downloaded arXiv math/0608219 and extracted all 13 pages in memory to sources/survey_2006.txt. PDF-byte SHA256 matches the submitted manifest; the source is authentic. Section 1 permits infinite F, requires semigroup generation of Z^d, and has finite G. Section 3 uses only the forward color record. Theorem 3.3 indeed has the strict-superset glyph ⊋.
- Verified Theorems A/B analytically, including conditioning, disjoint coordinate pairs, and the measure-preserving symmetry map. No use of fair colors, label permutation, negative times, or observed increments is needed.
- Independent standard-library code PASS: exact enumeration of 4^7 paths for each of two fixed biased sceneries; 120,000 independent records per scenery and transform; 10,000 paired paths per example; recurrence counts through time 24. Runtime 2.89 seconds; peak RSS 20,611,072 bytes; one thread; nice 10. Broken-symmetry controls have positive TV.
- The full eight-element linear kernel group has only two Euclidean elements (±I). Thus the same argument actually gives success <=1/4, a strengthening rather than a defect in the claimed <=1/2.
- Printed prior art found: Finucane–Tamuz–Yaari (2014), §3.2 and Lemma 3.2, explicitly couple a kernel-preserving non-geometric group automorphism to obtain identical records. This is a close precedent for Theorem B's mechanism; exact infinite-lattice matrix example not located.
- Bibliographic error found: submitted branching paper is AAP 27(2) (2017), 651–685, not 877–897; author order Matzinger, Pachon, Popov. Confirmed against IMS issue contents, arXiv, and institutional records.
- Original Lindenstrauss download via CiteSeer returned 403. Continue with author-hosted route; distinguish full text, accessible theorem extraction and indirect citations in final report.

## 2026-11-13 10:20 +04 — final verification

- REPORT.md completed with first line MINOR. Both formal theorems survive. Five numbered corrections/qualifications distinguish headline scope, the reachable-semigroup bridge, interpretation of the quotient, omitted printed prior art, and an incorrect bibliographic citation. No fatal proof gap found.
- Retrieved Lindenstrauss's author-hosted PostScript into memory only, read the abstract and Theorem 2.1 on preprint p.6 from its text strings, and retained reading notes only. No PostScript, DVI, PDF or image file was saved. This is not claimed as a full journal-text extraction.
- Added and verified four inequivalent kernel-symmetry representatives; their product-space argument improves the success bound to 1/4. Final independent run PASS: 3.542746792 seconds, peak RSS 21,397,504 bytes, one thread, nice 10. Its complete output is data/independent_check.json and data/check_stdout.txt.
- Recomputed histogram normalization and empirical total variation from retained integer counts, separately from the simulation's floating-point summaries. Binary empirical TV 0.0148833333333; three-color TV 0.0158. Exact record-law TV is zero; controls breaking the kernel symmetry have TV 0.4160318 and 0.3443191.
- All 12 downloaded full-text manifest entries pass SHA256 verification. There are 14 UTF-8 plain-text source files including the manifest and reading notes. The published survey's PDF-byte hash independently matches the submitted source manifest.
- Recursive audit finds no PDF, PS, EPS, DVI, page-image or scan files anywhere in this directory. No subagents, publication, push, or mutation of submitted claim files. No shared-memory/checklist/mesh writes attempted outside the task directory, apart from the startup recall tool's blocked routine cache/log activity.
- data/referee_audit.json records PASS, source checks, independent computation limits, recomputed statistics, and final input/code hashes. Existing claimant code was neither executed nor reused. The independent code uses only the standard library; the separate source extractor uses pypdf with bytes held in memory.
- Literature conclusion: the general question with all walk-kernel symmetries admitted remains unresolved by these results; no full resolution was located in the checked literature through 2026. Exact-matrix priority not established. Printed kernel-automorphism coupling precedent verified in Finucane–Tamuz–Yaari (2014), §3.2 and Lemma 3.2.

Checklist: primary text DONE; proof audit DONE; independent computation DONE; bounded literature audit DONE with access limitations; REPORT.md DONE; final artifact audit PASS.

Task: “Break it if it is wrong” — independent referee audit of F0126. Received 2026-11-13 approximately 10:02 +04 (Asia/Tbilisi).
