# Work log

Task: Open problems I0013 and I0014. Started 2026-11-13 14:27 Asia/Tbilisi (+04).

## 2026-11-13 14:30 +04 — literature acquisition

- Work is restricted to this directory; no publication, pushes, agents, or simulations.
- Inherited process priority checked: nice 10. All numerical work will use one process and capped library threads; memory limit 4 GB.
- Read startup memory index, identity card, mesh protocol and compute state. Shared brain recall/checklist/mesh commands normally write outside this directory; the task's explicit local-only restriction takes precedence, so progress and durable findings are recorded here instead.
- arXiv listing: Muneya Matsui, arXiv:2609.04638v1, submitted 2026-09-04 02:17:01 UTC. Listing title omits '(with related open problems)'. Only v1 listed.
- I0013 is in Remark 2.4(ii), not Remark 2.5. Corollary 2.3 specifies beta in (1/2,1), excluding the endpoint.
- Source license linked by arXiv is CC BY 4.0. Store attributed text only. PDFs will be streamed in memory for extraction and never written to disk; no page images.

## 2026-11-13 14:34 +04 — source and proof audit

- Saved full 17-page source as sources/matsui_2026v1.txt and TeX as sources/matsui_2026v1_tex.txt, with download URLs and SHA-256 in data/.
- Source PDF displays September 7, 2026 on page 1, but arXiv submission is September 4; distinguish these dates.
- Paper defines log = log_2 and << as O, not little-o. The formulas involving exp and Taylor expansions need a base audit.
- Exact obstructions to beta <= 1/2: p.15, sum i^(-2 beta); pp.15–16, existence of delta > 0 with delta < (4 beta-2)/(1-beta).
- [3] is Bradley (1987), The central limit question under rho-mixing, Rocky Mountain J. Math. 17(1), 95–114, DOI 10.1216/RMJ-1987-17-1-95. Bradley's 2005 survey records a correction at 17, p.891; must obtain it before accepting construction constants.
- Project Euclid currently serves a challenge iframe rather than full article/PDF at several standard URLs. Trying primary journal archives and alternative publisher endpoints.

## 2026-11-13 14:40 +04 — mathematical work and limitations

- Completed a direct conditional extension for I0014 under rho*(1)<1 (interlaced maximal correlation). A random-partition variance bound gives uniform L2 approximation by bounded truncations, and Ibragimov's CLT then applies. This is an established structural strengthening, not resolution under ordinary rho-mixing.
- Found an independent sharp upper-variance-envelope argument using the maximum of dyadic normalized L2 norms and polynomial logarithmic gaps. Writing out and auditing the recursion before claiming it.
- An exact-base audit finds real transcription/argument problems in the 2026 text: exp(-2 sum log(1-rho)) uses a log explicitly defined as base 2, but the subsequent Taylor series is for ln; the claimed comparison between Theorems 2.2 and 1.2 has the implication in the wrong direction; p.14 (3.23) prints an untruncated 2+delta moment despite only a weighted second-moment hypothesis. None of these observations alone disproves the corollary.
- Original Bradley [3], its correction, and original Peligrad 1987 remain unavailable from Project Euclid (challenge HTML at full and PDF endpoints). Crossref metadata for both Bradley items saved. Correction is pp.891–892, not just p.891 as abbreviated in the survey; DOI 10.1216/RMJ-1987-17-4-891.
- Primary author texts saved for Bradley's 2005 survey and Bradley–Jurek (2015). The latter's Appendix Theorem 6.4 explicitly identifies Utev (1990), Theorem 4.1, and its corrected variance assumption. Its displayed Lindeberg condition also has an apparent missing sigma factor; report only normalized form.
- Shao 1989 publisher PDF has no extractable text (seven form feeds only). No images saved; this is a text-access limitation, not evidence about its theorem.

## 2026-11-13 14:48 +04 — completed report and audit

- REPORT.md begins PARTIAL, with separate verdicts for I0014 and I0013 and an explicit statement that neither unrestricted question is resolved.
- Saved exact Corollary 2.3 wording, common hypotheses, theorem definitions, page numbers, author/version/timestamp, and the correction of I0013's location to Remark 2.4(ii).
- Proved the conditional CLT under rho*(1)<1 by an explicit variance comparison and bounded approximation. Identified it as an established stronger dependence assumption.
- Proved the uniform upper-variance envelope (E3) for every 0<beta<1 via a dyadic maximum recursion; all constants independent of the coordinatewise transform. This does not supply the missing lower-variance or CLT argument.
- Re-derived the scalar Bradley condition with the declared base-2 logarithm: its literal exp formulation has exponent gamma-d*alpha*ln(2), including a positive limiting constant at equality. This is not a construction verification or a numerical counterexample region.
- Exact rational and symbolic checks and 80-decimal constant checks passed. Latest peak RSS 59,555,840 bytes; nice 10; one numerical process, library threads capped at one. macOS rejected setrlimit changes, so measured RSS rather than an OS cap is reported.
- Literature table includes Ibragimov, Peligrad, Bradley, Shao, Utev, Peligrad–Utev and their precise verified theorem references, with unverified original theorem pages marked explicitly. A web extraction of Ibragimov's Russian original subsequently permitted verification of Theorem 2.1 p.135 and Theorem 2.2 p.136 and its f(0)>0 condition.
- No later resolving result found in the recorded bounded search. Original Bradley [3] and correction remain inaccessible; exact Theorem 1/Proposition 0 statements and A_j/B_tau constant tracking remain incomplete.
- data/source_manifest.json verifies 12 plain-text source/status files and hashes. No PDF or image files exist in the directory. No publication, pushes, subagents, simulations, or writes outside the task directory.

Task outcome: partial research artifact completed; original open problems remain unresolved as specified in REPORT.md.
