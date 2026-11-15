# Independent referee audit

Task received: 2026-11-13, approximately 19:57 +04 (Asia/Tbilisi). User: “Break it if it is wrong”; audit `paper/main.tex`, `paper/main.pdf`, and cited sources; deliver `REPORT.md`; do not edit `paper/`, publish, push, upload, or consult other reports.

## Scope and execution

- One agent, no subagents or language-model workers. No heavy computation planned. Requested `nice -n 10` was attempted; sandbox returned `setpriority: Operation not permitted`. Process inspection is also blocked. No parallel computational jobs are being launched.
- Startup memory consulted only for identity/orientation, not for this mathematical result or any previous assessment. No other report read.
- Shared mesh registration/digest and checklist attempted: readonly database / permission errors. Shared coordination state lies outside the writable workspace. Local work proceeds under the user's explicit directory restriction; no attempt to bypass the sandbox.
- Initial compute state: `warn`, `owner_away_open`; reads and lightweight document processing only.
- Initial SHA-256: `paper/main.tex`: `100538537ccac0d1617405f9675e639d004e84ee03147274db383e3eb0ce7ea3`; `paper/main.pdf`: `72b5b594f4d294e5ef51cc0b344557870870b4365c45202302df7e0bba92c20a`.

## Progress

- Read all 822 numbered lines of `paper/main.tex`, including protected bibliography/end matter (inspection only).
- Re-derived Lemma 3.1: critical equality gives `(1-a)(rho+1)=rho>0`; the displayed radius is independent of the domain norm of the center. Young's inequality constant checked by maximizing `h Z^b - delta Z`.
- Next: independently audit reference-operator upgrade, cutoff continuation, deterministic restarting, interpolation, and precise source hypotheses/locators; verify bibliography online.

- Checked the survey in both supplied versions. All numerical survey locators in the manuscript refer to the published 150-page NoDEA version, not the differently paginated arXiv v5. The cited theorem/equation numbers agree. Published locator examples: Proposition 2.1 p.18; Definitions 3.7/3.8 pp.27/28; Theorem 4.7 pp.42–43; Theorem 5.1 p.48; (5.5) pp.51–52; Theorem 5.7 pp.59–60; Problem 6 p.130.
- Independently checked the reference operator, both correction signs, and the constant in (4.3). No error found. The proof uses ordinary high-q maximal regularity only on the original couple.
- Audited cutoff local existence, stopped moment estimate on a fixed horizon, and Theorem 5.1(1). The cutoff has local parameters rho'=0 and beta' in (1-1/q,1); the criterion's hypotheses are met. The finite-horizon absorption excludes tau<=T and asserts no infinite-horizon uniform estimate.
- Audited measurable deterministic restarts, localization to initial events, endpoint uniqueness, nonseparable range reduction, countable removal of null sets, finite pasting, and mixed complex interpolation. No load-bearing gap found so far.
- Compared Part II Proposition 6.8 in full (published pp.76–80), the Navier–Stokes shifted bootstrap, the two reaction-diffusion source versions, and singular-times material. These do not directly imply the present theorem under its original-couple hypotheses. The threshold note's full-domain temporal regularity obstruction has a different spatial target.
- External bibliography checks used publisher/arXiv/institutional/MathNet records only. One general literature search returned an unrelated problem-list snippet; it was not opened or used. No prior report was consulted.
- Extracted the supplied PDF with pdftotext and checked its metadata and main statement against the TeX; it is a 10-page PDF and displays Theorem 2.3 and Corollary 6.1 as expected.
- Cross-checked all internal labels/references and bibliography keys by script: 36 labels, no duplicate labels, no unresolved internal references, no missing or uncited bibliography keys.
- Rechecked the critical estimate by direct integration and scalar maximization; rechecked the reference construction by polar decomposition and the initial-data constant by a separate triangle-inequality calculation.
- Bibliography: the eight mathematical entries agree with the supplied sources and primary metadata. KR's 1979 original and 1981 translation were verified using MathNet and the author's institutional record. The protected final three entries were not externally audited or changed.
- End-matter inspection: writing-process sentences occur at TeX 751 and 759–761. No factual error established; no edits proposed to protected sections. The ERC identifier 101041711 exists and is a Horizon Europe ERC project at the Hebrew University; that public fact alone cannot verify the manuscript's personal funding attribution.

## Completion

- Wrote `REPORT.md`: verdict `MINOR`; no counterexample or load-bearing proof gap found. Three minor corrections concern the classical variational assumptions, the survey pagination convention, and whether the Part II continuation theorem is invoked directly or its method is reproduced.
- The report documents each lemma/proposition/theorem, the critical constants and interpolation exponents, every explicit mathematical source locator, all eight mathematical bibliography entries, the shifted-couple objection, and the threshold note. It also distinguishes a sign typo in the survey's Remark 5.8(1) from the correctly signed parameter discussion in the manuscript.
- Final process-priority inspection via `os.getpriority` succeeded: Python inherited niceness **20**, a lower scheduling priority than nice 10. The earlier attempted additional nice adjustment was rejected; no heavy computation or additional worker was started.
- Verified the report's first line is exactly `MINOR`, its three correction items include TeX locations and replacement LaTeX, and all code fences are paired.
- Final SHA-256 of both files in `paper/` matches the initial hashes above. No paper edits, git mutations, publication, push, upload, or external messages. Only `REPORT.md` and `LOG.md` were authored as task deliverables.
- Shared checklist/mesh completion and durable brain writes were not attempted again: their stores are outside the authorized writable directory and the initial calls were blocked. This local log is the task record.

Task: “Break it if it is wrong” — 13 November 2026, approximately 19:57 +04 (first locally recorded task time).
