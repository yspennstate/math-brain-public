# F0137 work log

Task received: “Open problem F0137”, 2026-11-13, 09:06 Asia/Tbilisi (first local observation; prompt carries no explicit time).

## 09:07 — orientation and scope

Read the startup memory index, compute governor, mesh protocol, and attempted targeted brain recall. Work is isolated in this directory. No subagents, publication, or pushes. The task-specific instruction to work only here takes precedence over global instructions to update shared brain/checklist stores; coordination state is therefore local in data/mesh, rather than a claimed global registration. This cannot exclude external concurrent claims, but this directory is the task's dedicated workspace.

Literature comes first. Initial arXiv checks: 1601.08219 has v1 only; 2501.06767 (Perrel–Sabot) has v1 only, January 2025, and its abstract explicitly assumes (T'). Neither abstract is being treated as a proof or an exhaustive literature search.

Sources will be fetched as PDF bytes in memory and converted directly to plain text. No PDF, scans, or page images will be written. Scripts run at nice 10 with one compute thread; numerical limits will be recorded explicitly.

## 09:10 — source reading and initial mathematical audit

Read all of overview Sections 4–6 (arXiv pages 11–19). Read BRS statements, conditions, and Section 4.2 proof of Theorem 5; CR definitions and Theorem 1.1; FK regeneration and main criteria; GR statement and uniform-ellipticity hypothesis; PS2025 Sections 2.2 and beginning of Section 6; Perrel2024 introduction and Section 1.3; Poudevigne renewal-range argument. Fetching the other named sources and their published versions as text.

Confirmed (6.1) is the L1 norm of the unnormalized drift exceeding 1, not a condition on kappa. Exact omitted set is 0 < ||d_alpha||_1 <= 1. All kappa <= 1 is omitted. Strong finite traps obstruct time moments, whereas (T) controls spatial excursions; a two-vertex trap alone cannot refute (T).

The first PDF extraction method emitted warnings and malformed whitespace for the old Tournier preprint. Switched to pdftotext with stdin/stdout, keeping all PDF bytes in memory; replaced poor extractions and fetched the published Tournier article separately. Source manifest retains both conversion hashes. Existing process priority was already nice 10; adding os.nice(10) was denied on this Mac. Fixed code to check current priority and set 10 only if needed.

No applicable proof of the full conjecture found yet. Modern checks include Poudevigne 2024 (no T assumption, subballistic stable limit), Perrel 2024 (assumes T for fluctuations), and PS2025 (assumes T' for 2D invariant measure). Search results about 2026 uniform elliptic ballisticity do not apply to Dirichlet laws and do not by themselves assert the needed spatial condition.

## 09:15 — finite-box proof and computations

Completed a quantitative re-derivation of the BRS small-backward-weight argument. Use the corrected forward ellipticity constant from BRS Eq. (1.1), bounded uniformly as the backward weight decreases. A deliberately oversized explicit constant avoids ambiguity in the extracted typesetting. Fresh transverse records give independent annealed first-step indicators; this is used unconditionally, without conditioning on the future exit event. First departures from virgin axial layers have backward probability b/(a+b). These facts give the explicit bound L b/(a+b) + exp(-35 p^2 L^3).

Simulated four parameter sets outside (6.1), two each in d=2 and d=3. Fixed-site gamma-generated Dirichlet probabilities, independent environment per replicate, 448,009,502 walk steps, one thread, nice 10. C++ wall time 25.84 s; Mac ru_maxrss 28,999,680 bytes. Raw exit counts retain censoring. Finite-horizon regeneration proxies are lower bounds on actual regeneration times; no false completed-renewal claims.

OpenAlex forward search for the published overview returned 24 records (saved verbatim as JSON), including 2026 citations; most concern other models or rough paths. Screening relevant follow-ups against their primary text. A broad search hit, arXiv:2601.06751, has no current PDF and its primary abstract says arXiv withdrew it for unverifiable authorship/affiliation; it is excluded as evidence. This explains the failed PDF fetch.

## 09:34 — final audit

REPORT.md is PARTIAL. Proved the explicit parameter-region statement by a quantitative version of the existing BRS argument, the unconditional endpoint divergence, and a later-iid-interval moment consequence of Poudevigne's stable limit via Laplace transforms. The later-interval result is not represented as a theorem about the unconditioned first renewal time. Exact finite-path certificates are implemented only on toy boxes below the seed scale.

Re-derived the fixed-total parameter-space omission using both simplex-volume algebra and uniform simplex samples. Audited the explicit region constants independently by quadrature of beta inverse moments: log10 C agrees with gamma-function evaluation to better than 1e-5 in both dimensions. Compared exact urn enumeration against independently sampled quenched transition matrices (maximum discrepancy 0.55 standard errors). Two-site trap survival checks have maximum discrepancy 2.19 standard errors among bins with expected count at least 10.

The initial full-report apply_patch was rejected because delete/add targeted the same file; it left the saved draft intact. Rewrote REPORT.md successfully, then audited the resulting file. No mathematical result was lost.

Forward-citation screening saved for 24 records. The 2023 survey was recovered from HAL after its publisher returned 403; it is about estimation and graph Dirichlet distributions. Sznitman 2002 was recovered from Springer and its equivalence proof checked. Sznitman 2001's original full text could not be retrieved, and this limitation is explicit in the report.

Artifact audit: 27 source files, all UTF-8 .txt; latest recorded text hashes match. No PDF files, PDF headers, paper images, or scans found anywhere in this workspace. Numerical figures are original SVG plots of the saved simulation data. All changes remained here; global shared stores were not updated. A local checklist mirrors completion without marking the author's seen checkbox.
