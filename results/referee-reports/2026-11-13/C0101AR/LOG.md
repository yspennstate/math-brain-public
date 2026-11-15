# C0101 independent referee log

Task: “Break it if it is wrong.” Received 2026-11-13, approximately 06:51 +04 (02:51 UTC, checked against the shell clock).

## Start

Read the claim report and log, startup memory and index, and compute governor state. Work is confined to this directory, as explicitly requested; mutating global brain, mesh, and checklist commands would write outside that scope and are not run. No subagents. Source PDFs will exist only in memory during extraction; sources/ will contain plain text only. Independent scripts will not import or execute claim_files/code.

Governor reports warn/cpu_saturated, owner_away_open. Use one numerical thread, inherited nice priority at least 10, and small bounded computations. The explicit nice increment is refused on this host; check inherited priority before computation.

Read claim_files/REPORT.md and LOG.md. Focus: exact source definitions and maximality terminology, residual geometry, closure/obstacle definition, ceiling bound and lifting, exact explicit point, subsequent literature. The supplied claim is already qualified; distinguish mathematical validity from its value as an answer to the survey problem.

## 06:56 +04 — source reading

Downloaded survey, LPS v4, LPS v1, GAFA paper, and published Annals article directly; PDFs parsed from memory into sources/*.txt. Read survey Section 6 (pp.21–22), open problem (4) (p.27), LPS Theorems 1.1–1.2, following paragraph, and Lemma 3.4 with proof (pp.8–9 of v4). The survey does not define maximality formally; its context identifies maxima with circle peaks. V4 uses the semidefinite order and explicitly mentions residual trace-zero matrices outside the union of downsets. It also says elsewhere that circles correspond to matrices maximal in that order, without an exclusion of residual maxima. V1 Theorem 1.1 omits the residual half-space entirely. Published Annals Theorem 1.1 and its following paragraph print 2; arXiv's own revision comment explicitly says “Typo in T1.1 corrected (2 -> 0).”

The claim's lifting argument survives initial checking: the contact normalization gives the ceiling bound, which removes positive improvements on extra diagonal entries; PSD then removes all mixed extra rows. The minimum over added coordinates works only after eliminating their affine slopes, which the claim does address. Next: independent symbolic derivation and a fresh packing enumeration.

## Independent computation and citation search

Wrote independent_check.py without reading, importing, or executing claim_files/code. Derived the three-step matrix from individual insertion maps, used an adjugate to derive eigenvector projections, reduced exact identities modulo t^4+4t^2−1, and found determinant 2 for the rational-circle exclusion. A separate recursive enumeration of both gaps in one full band period produced 9,834 circles with curvature at most 3,000. At 150 decimal digits all distance-minus-radius values were positive; minimum approximately 3.51122445348e-5. A 180-insertion sequence has center error approximately 2.93784949964e-84. Results saved in independent_results.json. Nice 15, one numerical thread, peak RSS approximately 59.4 MB.

Wrote check_certificates.py using only saved data. Exact integer-scaled quadratic evaluation, periodic corrections and boundary increments verify all 190 saved certificates on 180,704 torus sites, including their mean Laplacians. Peak RSS approximately 18.4 MB. These certificates support the ancillary numerical claims, not the irrationality or maximality proof.

Semantic Scholar citation endpoints for both arXiv identifiers returned successfully; full responses saved as sources/citations_*.txt. Screened titles and identifiers, including 2025–2026 entries; follow relevant papers to primary texts. Downloaded nine further papers as plain text: pattern stability, random initial sandpiles, dynamic dimensional reduction, F-lattice, higher-dimensional solitons, Kim–Wang, Selig–Zhu, exploding shape theorem, and tropical curves. Their relevant introductions and main results concern different lattices, initial conditions, or convergence, not a cubic-lattice peak classification. Kalinin explicitly notes the absent quadratic-form classification above dimension two. Citation metadata alone is not treated as proof of a paper's scope.

## 07:04 +04 — completed referee report

REPORT.md begins MINOR. The qualified ordinary-Loewner counterexample is valid; no fatal error was found. Three repairable gaps/clarifications are identified with claim-report line locations: the reverse definition inclusion, the stabilization/normalization bridge, and the lack of a formal alternative peak definition. Supplied full arguments for the first two. Verified the ceiling bound, removal of added affine slopes, attained integer minimum, and PSD elimination of all mixed extra coordinates. Verified irrationality, all-circles residual membership, and convergence of distinct maximal lifts. Checked the ancillary isolated integer family and saved certificates.

Literature record in sources/LITERATURE.txt documents both citation traversals (33 and 45 records, no next page), primary texts, Kim–Wang's changed model, additional planar lattices, shape-theorem distinctions, and search limits. No printed cubic-lattice classification was found through today. The claim answers the two literal yes/no questions negatively but does not classify all maxima or solve an intrinsically defined higher-dimensional peak problem.

Final artifact audit: all report links to local files resolve; sources/ contains .txt files only; no PDFs, page images, scans, or raster images exist anywhere in this directory. Removed two PDF-extraction control characters from text sources and added sanitization to the downloader. Reran exact algebra after checking all four eigenprojection rows. Verified result files report 9,834 finite packing checks and 190 positive certificate checks. No claim code was run, no subagents were started, and no computation remains running. All mutations stayed in this directory.

Task: “Break it if it is wrong.” — received 2026-11-13, approximately 06:51 +04.
