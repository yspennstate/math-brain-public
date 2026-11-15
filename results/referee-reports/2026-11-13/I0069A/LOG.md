# I0069 research log

Started 2026-11-13, 16:12 Asia/Tbilisi. Task: Open problem I0069, extrapolation of stochastic maximal regularity.

## Scope and working rules

All deliverables and source texts stay in this directory. No subagents, publication, pushes, simulations, PDF files, or page images. Downloaded PDF bytes are converted in memory through pdftotext stdin; only plain text is saved. Requested process priority is nice 10 (attempts were rejected by the sandbox, as recorded below); numerical-library thread limits are set in the fetch script. No heavy compute is planned.

Read the identity memory and compute governor state at startup. Governor reports owner_away_open, warn/cpu_saturated, ample available memory. The task's directory-only restriction and sandbox override the general instructions to mutate the shared mesh, checklist, or brain; local progress is recorded here instead.

## Literature-first phase

- Identified survey: Agresti–Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, NoDEA 32(6), article 123 (2025), DOI 10.1007/s00030-025-01090-2. arXiv:2501.18561, latest listed version v5, 27 August 2025. Need exact page and definition checks from full texts.
- Searches and source collection in progress. A search result or remembered theorem is not treated as proof.

### 16:16: full-text findings

- Survey v5 is 103 pages; Definitions 3.6–3.8 pp. 19–20, Theorems 3.12–3.14 pp. 22–23, Problem 3 p. 92. It uses deterministic time-independent A and B. The related critical-spaces Part I explicitly allows progressively measurable (t,omega)-dependent operators (Assumption 3.2, p. 18).
- Reference [29] in the published survey corresponds to [BV23] in arXiv v5: Sebastian Bechtel and Mark Veraar, arXiv:2311.01271, now v2 (3 July 2025); journal version Stoch. PDE: Anal. Comp. 13 (2025), 2000–2038, DOI 10.1007/s40072-025-00378-9. Read Assumptions 1.1/2.1 and Theorems 1.2/2.2. It proves a small interval above 2 under symmetry, allows random measurable coefficients, and explicitly says on p. 2 that unrestricted extrapolation with B nonzero is false, citing Brzezniak–Veraar.
- Brzezniak–Veraar 2012, arXiv:1104.2768v3, Theorem 4.1 pp. 13–14: A=-Delta, noise coefficient 2(alpha D+beta |D|), moment condition 2 alpha^2 + 2 beta^2(p-1)<1. Theorem 5.1 gives the L^q extension. Failure above the threshold is already printed. The survey itself mentions these failures in §3.6.3 (v5 p. 26).
- Still auditing the bridge from nonzero initial data in the printed theorem to the survey's zero-initial-data forcing definition. No novelty claim is justified by rediscovering this moment obstruction. The weaker question about an unspecified range is distinct from the false all-r assertion.
- Saved full plain texts for the survey v5, Bechtel–Veraar, Brzezniak–Veraar, Portal–Veraar, NVW 2012, critical spaces I/II, the periodic (t,omega)-dependent systems paper, Lorist–Veraar singular integrals, discrete SMR (2025/26), and necessary conditions (2026). Source URLs and hashes are in data/source_manifest.jsonl.
- Infrastructure limitations: sandbox rejects nice(10) with 'Operation not permitted'. Only lightweight fetching/text conversion is being done. A Delft repository connection timed out; Springer direct PDF URL returned an anti-bot HTML page (not a paper). Trying an alternate institutional URL. No PDF bytes have been saved.

### 16:18–16:29: completed literature review and exact-definition audit

- Obtained the published survey through pure.tudelft.nl: 150 article pages plus an institutional cover page. Exact locations: Problem 3 article p. 129; standing assumptions p. 26; Definitions 3.6/3.7 pp. 27–28; Definition 3.8 p. 28; reference [29] p. 135. The text and provenance are saved.
- Saved REPORT.md during work, then filled in the literature matrix, proof audit, source limitations and 2025–2026 follow-ups. First line RESOLVED_IN_LITERATURE is explicitly scoped to the false all-r assertion. The general coefficient-dependent range question is not claimed resolved.
- Verified zero initial data directly: A e_n=n^2 e_n on l^2, B=sigma A^(1/2), sigma^2<2. The variational energy estimate proves SMR^bullet_2 including the required supremum norm. A deterministic forcing pulse of duration 1/n^2 gives an exponentially diverging estimate ratio when r>1+2/sigma^2, and a linearly diverging ratio at equality. Checked the moment coefficient independently by the stochastic exponential and Itô's formula. The parameter conversion to the printed example is sigma=2 beta, alpha=0.
- Independently checked the p=2 energy and BDG constants in REPORT.md. They are uniform in the spectral cutoff and in starting, ending and stopping times. This closes the mismatch between the printed initial-data example and the survey's forcing definition. It is an audit of a known obstruction, not a novelty claim.
- Read the relevant statements and arguments of Portal–Veraar, Lorist–Veraar, NVW, critical spaces I/II, stability, periodic systems, [29], Brzezniak–Veraar and Bechtel–Mooney–Veraar. The report separates autonomous from random time-dependent coefficients, B=0 from critical multiplicative noise, and time/moment exponents from spatial exponents.
- Checked two survey-citing follow-ups: discrete SMR (arXiv:2505.22145v2, journal 2026) and necessary conditions (arXiv:2608.20266v2). The former is B=0; the latter concerns geometric sufficient conditions and failure at every p, not one-p-versus-another extrapolation. Also checked an October 2026 finite-element preprint; it is additive noise and does not cite the survey.
- OpenAlex citation query returned 21 records through the task date; saved metadata in data/citation_search.json. The index omitted the necessary-conditions preprint despite its direct citation of the survey, so no exhaustiveness claim is made.
- Historical full-text limit: original Sobolevskii, Cannarsa–Vespri and Dore papers were sought but not obtained in usable form (host failures / no institutional attachment / anti-bot responses). Saved and read Prüss–Simonett 2004, which independently identifies the historical attribution. The report gives exact verified theorem/page locations and explicitly withholds unverified original theorem pages. No access failure is passed off as a read paper.
- Removed failed HTML responses from sources/ and made fetch_text.py reject HTML before saving. Provenance log retains the failed-response metadata as retrieval history; the current source hashes all match successful PDF-to-text conversions.
- Artifact audit: python3 code/audit_artifacts.py passed 103 checks on the final run (102 before verification.json existed), including the report classification, scope caveat, 20 page anchors, current source hashes and absence of PDF/image artifacts. Results saved in data/verification.json. No simulation or numerical sweep was appropriate or run. All work remained local; no publication or push.

Result: The unrestricted extrapolation assertion is already disproved in print. The requested exact survey definition and [29] are identified. General pair-dependent range questions and the historical full-text access limits remain explicitly distinguished from that conclusion.
