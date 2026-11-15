# Independent audit of I0071

Task: “You are an independent referee … Break it if it is wrong.” Received 13 November 2026, approximately 19:56 Asia/Tbilisi (workspace run marker; exact user-message time unavailable).

## 13 November 2026, 19:58–20:00

- Read the entire submitted report, its source manifest, and its algebra-check code. The submitted source texts are not evidence for the independent source audit.
- Read startup memory and compute state. Work is single-agent, with small sequential algebra/source-extraction jobs. No publication, push, background worker, or external write is authorized.
- The current task's directory-only restriction takes precedence over global instructions to write shared brain/checklist/mesh state. Coordination claims use a directory-local mesh; no shared brain records are modified.
- Initial mathematical finding: the specially constructed Hessian, unlike a generic positive mixed Hessian, has tunably small normalized off-diagonal entries. Therefore unequal transport alone is not a counterexample to its estimate (11).
- Began independent retrieval from arXiv and current literature search. PDF content will be streamed through pdftotext; no PDF or image will be saved.

## 20:00–20:03

- Independently retrieved survey v5, both AV transport papers, both Milesis–Salins versions, Fellner–Morgan–Tang, Morgan–Tang, Fitzgibbon–Morgan–Tang–Yin, delayed-blow-up, Agresti–Germ–Veraar v2/v3, Blessing et al., Földes–Stacy, Souplet, and Agresti–Kniely–Tang (August 2026). Provenance and hashes are in data/retrievals.jsonl.
- Springer direct download returned HTML; the published survey was independently obtained from Delft's institutional repository, with one added cover page.
- Verified the survey's reversed parabolicity sign and the correct sign in AV local Assumption 2.1(3). Verified the vector multiplication in the triangular condition and the flexible blow-up criterion, including its independent continuation parameters.
- Found a generic-Hessian counterexample: nu_1=nu_2=1, b_1=1, b_2=-1, H=ones, z=(1,-1) gives Q=-2 despite parabolicity margin mu=1. This does not contradict the report, whose normalized mixed entries are tunable.
- Re-derived the report's cone recursion and Hessian midpoint identity; no algebraic failure found. Wrote independent exact checks without importing submitted code.
- Identified missing deterministic polynomial-energy attribution: Fitzgibbon–Morgan–Tang–Yin (2021), equations (2.9)–(2.10), Lemma 2.4, and diffusion estimate. This is a close deterministic predecessor, not a stochastic transport theorem.

## 20:04–20:08

- Read AV global Assumption 5.1 and Theorem 5.2 exactly. The energy bounds have the required strength, but the report only states the verification for smooth initial data, whereas Assumption 5.1 quantifies over Hölder initial data with an L^m moment. The short initial-time extension is omitted; this affects the extra stability assertion, not the global-existence proof starting at positive time.
- Verified local positivity for positive distributions using AV local Theorem 2.13, and the actual Hilbert trace L^2 using its Propositions 7.1–7.2.
- Screened every named modern citation against independently fetched full text; extracted theorem locators. The detailed special-model noise inequalities agree with AV global.
- Original Morgan PDFs returned 403. Pierre's legacy archive failed certificate validation, then returned 404 on a public-file-only retry; no original text was obtained. Their contextual statements are checked through the survey and Milesis–Salins reproductions, with this limitation retained.
- The independent finite algebra checks passed. Expanded the checks to unequal diffusivities and two Brownian modes. All jobs inherit nice 20; no job exceeds one compute thread.
- The candidate verdict is MINOR: the periodic nonexplosion proof survives, with missing deterministic attribution and a small extra-stability quantifier gap. No exact stochastic transport resolution found in the checked literature through today's date.

## 20:09–20:15

- Completed REPORT.md with verdict MINOR. It gives complete mathematical restatements of the source hypotheses and used theorems, two- and three-species hand calculations, an explicit generic-Hessian counterexample, a second derivation of estimate (11), and a stopped-martingale integrability bound.
- The auxiliary-parameter inequalities in the continuation argument were re-derived explicitly. They do not require the original initial datum to lie in a stronger auxiliary trace space.
- The final independent computation passed 24,063 counted exact checks: 23,814 full quadratic-form evaluations plus 249 cone, midpoint and differentiation checks. Nice level recorded as 20.
- Added the August 2026 Agresti–Kniely–Tang comparison and the omitted whole-space scope of deterministic Fellner–Morgan–Tang to the revision list. Neither changes the main mathematical verdict.
- Original-source limitations remain confined to inaccessible old Morgan/Pierre texts. Sixteen independently retrieved primary-source texts are retained, all plain text, fifteen from arXiv and the published survey from Delft's repository.
- Final file, provenance, delimiter, input-immutability and artifact-format checks passed and are recorded in data/final_audit.json. All 27 submitted files are unchanged; the audit directory is about 7.3 MB including submitted material. No new numerical testing was needed after the passing checks, since no mathematical implementation changed.
- Completed the authorized local referee task. Final verdict: MINOR; the stated periodic global-existence proof survives. Four revision items, detailed verification, accepted scope, literature comparison and old-source access limits are documented in REPORT.md. No publication or push.
