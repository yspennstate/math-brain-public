# Referee log

- 2026-11-13, Asia/Tbilisi: Read all eight PDF pages, in order, before source or ancillary-file inspection, using `pdftotext -layout paper/main.pdf -`.
- Saved the pages 1–2 assessment in REFEREE.md before beginning the detailed proof/source audit.
- Read the startup orientation and compute state. The task-specific instruction to work only here takes precedence over global checklist, mesh, and brain writes; no outside-directory state was changed and no subagents were started.
- `nice -n 10` reported `Operation not permitted` in the sandbox. Subsequent computation will remain small, single-process, with BLAS/OpenMP limited to one thread. No background tasks or external publication are authorised.
- Independently rederived all proof steps through Proposition 5.7. Saved a line-by-line mathematical audit, including the scale factor, odd-parity joint independence induction, Dixon–Anderson Jacobian, Killip–Nenciu parameter conventions, and both Gaussian implications.
- Initial fixable issues: “entrywise product” terminology; erroneous independent-Dirichlet-components phrasing; source attribution for the classical Dixon–Anderson identity and the antisymmetric/Laguerre connection. No failed load-bearing proof identified at this stage.
- Retrieved missing Ramírez–Rider–Virág full text and Bufetov–Kawamoto (2025) full text directly to text, keeping PDF bytes only in memory. Retrieved Kwak arXiv:2610.35808 (26 October 2026) the same way. No PDF files were added.
- Verified all 13 printed arXiv identifiers against their landing pages. Saved Crossref metadata and checked unmatched/failed results against publisher and author records; did not misidentify title-only search hits as the cited work.
- Read-only GitHub plugin calls verified the three fixed template references and retrieved their README/main.tex text. No external writes occurred.
- Trotter full text remains inaccessible after publisher, CiteSeer and publisher API attempts. Publisher metadata/abstract and Princeton bibliography support the only cited historical claim; this access limitation is explicit in REFEREE.md.
- Confirmed `os.getpriority(os.PRIO_PROCESS,0) == 10`: the shell already inherits nice 10. The warnings from `nice -n 10` were attempted additional niceness changes, not evidence that work ran at normal priority. There was at most one network-fetch process and one tiny exact-arithmetic process at a time; no numerical-library threads were used.
- Saved the complete citation table for all 18 references, including exact theorem/equation checks and version/access qualifications.
- Added the 2025 Bufetov–Kawamoto and 2026 Kawamoto–Shibukawa fixed-parameter kernels, with an explicit support/recurrence distinction; added 2026 spectral-measure, perturbed-corners and operator-coupling comparisons. No checked recent source establishes the same literal fixed-beta Jacobi-prefix theorem.
- Saved voice/first-definition/end-matter findings. Preserved the author-template end matter and all three fixed bibliography items.
- Exact arithmetic checks passed. Rechecked main parameter matching against trace and determinant normalisation identities, odd-parity shapes against the size-three case and trace shape, and the KN moments directly against source beta laws.
- Final recommendation: MINOR. No theorem-changing mathematical error found. Full Trotter access remains limited; this is disclosed without pretending that unavailable full text was inspected.
- 2026-11-13 15:18 +04: Final artifact audit complete. REFEREE.md begins MINOR; 28 line-referenced findings plus all 18 bibliography comparisons are saved. The manuscript was not edited. code/audit_manifest.json records the reviewed main.tex/main.pdf hashes. sources/ contains text only; the original paper/main.pdf is the sole retained PDF. All audit subprocesses have completed.

Task: “You are a referee for a probability journal” — 2026-11-13, approximately 15:06 +04 (launch minute).
