# Independent referee log

Task: “You are an independent referee… Break it if it is wrong.” First shell record: 2026-11-13 15:54 Asia/Tbilisi.

## 15:54–15:56 — orientation and initial audit

- Working alone, inside this directory. No subagents, publication, pushes, or external messages. The task-specific directory restriction takes precedence over global shared mesh/checklist/memory writes; this log is the local checklist. Read startup memory, mesh protocol, recalled the relevant earlier sandpile note, and inspected compute state. Compute mode was owner_away_open, status warn (CPU saturation); only small single-thread computations will be used, at inherited nice 10.
- Read the submitted REPORT.md in full. Its lower bound includes an actual discrete logarithmic supersolution and a dependent boundary event, beyond the variational heuristic described in the prompt.
- Read the staged companion Theorem 1.3 and pp.51–56, including (85)–(98), and parking Theorem 3.4. Independently opened both live arXiv abstract listings and HTML v1 texts. Both listings show v1 only, submitted 2 September 2026.
- Initial checks support the endpoint Laplace logarithm, Legendre cost, and supersolution comparison. No verdict yet. Particular checks pending: independent Green numerics, all uniform constants/time windows, stretched-exponential martingale truncation, and broader literature comparison.
- Existing sources/ contains plain text copies staged at task start. Will retain them and add independently fetched plain text; no PDFs or image files will be created.

## 15:56–15:59 — proof checks and independent code

- Retrieved fresh HTML and abstract listings, converted MathML alttext to plain text in sources/*-referee-live.txt. Provenance and hashes: data/referee_sources.json. Both live listings still contain only v1.
- Re-derived the critical Laplace upper bound, including lambda below one, outer square-sum cost, and the Chernoff choice. Re-derived inversion: Phi inverse at T has order T^(1/p)(log T)^((p-1)/p), giving loglog exponent 1-2/d.
- Rechecked the logarithmic barrier at every comparison step, all exterior neighbors, time monotonicity, and origin slack. Cost includes 1 per site, so t0 and atoms present no gap. FKG applies to decreasing events of finitely many independent coordinates; boundary odometers are not assumed independent.
- Audited the secondary proof's conditional martingale truncation. It uses a stretched-exponential moment, not an absolute exponential moment. The printed Proposition 6.3 permits gamma>0 syntactically, but retaining (85) makes its gamma<1 two-sided-tail application impossible; the report supplies a separate argument.
- Wrote code/referee_checks.py independently. It evaluates the actual infinite-lattice Green kernel by a Bessel-product integral, with exact lattice symmetry multiplicities, for d=5,6 and radii through 16. The first run exposed scipy.ive NaNs for arguments above 1e9; replaced that numerical tail by its four-term large-argument expansion above 1e6 and documented the correction in code. No claim code was inspected or reused.
- Final checks: 256/512 quadrature relative discrepancy below 1.5e-14, Green harmonicity residual below 1.9e-14, independent constrained optimization agrees within 8.3e-14. Doubling-annulus slopes approach the predicted constants. Checked the admissible hole profile including volume cost and the discrete barrier. Runtime about 0.12 seconds, one thread, inherited nice 10, peak RSS about 91 MB.
- Broader searches found no later endpoint treatment. Primary comparison sources located: Gantert–König–Shi (RWRS, critical tail separately delicate); van den Berg–Bolthausen–den Hollander (Swiss-cheese Wiener sausage); Donsker–Varadhan; Kirsch–Warzel and Leschke–Warzel (Lifshits quantum/classical transitions). These are comparisons, not sandpile endpoint theorems.

## Final audit and report

- Wrote REPORT.md with disposition ACCEPT. Both claimed mean orders withstand the independent audit; no proof-invalidating gap found.
- Supplied the full requested source inventory with every part of Theorem 1.3, Section 6 standing hypotheses, and all requested numbered results. Distinguished the incompatible gamma<1/exponential-moment assumptions from the separate valid heavy-tail argument.
- Recomputed the exact comparison-function inverse coefficient as well as the loglog exponent. Rechecked both directions of the discrete integration and bounded overshoot.
- Added independently fetched primary literature as plain text. For the author-hosted RWRS paper, PDF bytes were passed in memory to pdftotext through pipes; no PDF was written. Retrieved the earlier 2604.13968v1 and found no claimed quantitative mean theorem there.
- Recorded literature searches and their limits in data/referee_literature_search.txt. Novel relative to checked sources; no claim of exhaustive unpublished priority.
- Completed final checks: artifact inventory, all fresh source hashes, exact first line ACCEPT, and reported numerical values against saved outputs. sources/ contains only .txt files; no PDF/image files exist anywhere in this task directory.
- Final reread also checked strict/nonstrict tail conversion for atoms and the separate quadratic-plus-power variational comparison (submitted (7)–(8)). Neither changes the verdict. All authorized work complete; no publication or pushes.
- The final formatting check caught a mixed inline-math delimiter and missing escapes in prose formulas. Repaired those, then passed balanced inline/display delimiter and artifact checks. This was a report-format correction, not a change to a mathematical finding.
