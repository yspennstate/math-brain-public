# Progress log

2026-11-12 23:43 +04 — Task received: prove the centered DTCS Sackin limit and all-moment convergence, inspect the two supplied texts, and verify exact recurrences through n >= 8000 for k <= 6, under 4 GB.

2026-11-12 23:44 +04 — Read startup memory, compute state, mesh protocol, REPORT_P0347.md, Aldous–Janson §§4.8–4.9, and Brandenberger–Chin–Mossel introduction/Proposition 1.3/Corollaries 1.4–1.5. Shared mesh and checklist writes are blocked by the filesystem sandbox (readonly database / Operation not permitted); no claim was obtained. Work stays in this isolated task directory. No subagents.

2026-11-12 23:45 +04 — General induction appears to close after subtracting u_(k-1,n) from the term linear in the centered split toll. Higher powers have integrable entropy factors. A factorial majorant seems available using sum x^a(1-x)^b <= 1 and the endpoint cancellation; proof and independent numerical checks in progress.

2026-11-12 23:46 +04 — Full central recursions for S and C completed through n=8000, k=6. Planned storage 2,072,704 bytes; reported peak RSS 2,293,760 bytes. Binary64 long double confirmed (8 bytes). New constants a5=0.366233676893089714..., a6=0.819173199226021623.... The general factorial estimate is |a_k| <= 2^k k!, with a uniform inductive factor <= 0.773722 < 1.

2026-11-12 23:48 +04 — Independent rational raw-moment recursion through n=20 and 60-digit Decimal raw recursion through n=200 agree with all six central moments (worst relative discrepancy 1.35e-13 on nonzero moments). The Decimal verifier initially encountered Decimal's undefined 0**0 at a zero Colless toll; corrected to construct powers starting at 1, then reran successfully.

2026-11-12 23:49 +04 — Computed unforced inverse-log polynomial fits (degrees 2,3,4; lower cutoffs 256,1000,2000) against independently derived constants. Cubic fits over [1000,8000] have intercept errors below 1.5%; quartic fits can be worse despite smaller residuals. These fits support slow convergence but are not a proof of a rate or a certified extrapolation.

2026-11-12 23:50 +04 — Second full raw-moment recursion, using all ordered splits and centering afterward, completed through n=8000, k=6. Maximum relative discrepancy across all nontrivial n/orders is 6.47e-8 (raw sixth-moment cancellation); at n=8000 it is 1.08e-9. Peak RSS 3,473,408 bytes. Independent 55-digit entropy quadrature, direct generator coefficients, and 512/1024-point Gauss–Legendre calculation agree for a2,...,a6 (mesh error <=2.54e-11).

2026-11-12 23:50 +04 — Additional primary-source check: Kolesnik arXiv:2404.16021 studies one sampled leaf, not total leaf depth. Chorbadzhiyska–Minchev–Savov arXiv:2608.18320 studies tagged-leaf heights, occupation probabilities, total continuous length, and maximum continuous height; full-text searches found no Sackin, Colless, or path-length theorem. No global priority claim is made.

2026-11-12 23:56 +04 — REPORT.md written with status PROVED. Full theorem includes convergence of all real positive absolute moments, a common Sackin/Colless limit, and uniqueness of the characteristic/Laplace equation among centered laws with an exponential moment. No density formula, sharp rate, or unrestricted heavy-tail uniqueness is asserted.

2026-11-12 23:58 +04 — Final independent proof audit: the four finite toll categories agree with the full recursion to 1.77e-13 on the normalized scale; the parent subtraction preserves the linear term to 7.75e-13 relatively. Exact Fraction polynomial integration verifies psi(k)=h_(k-1) for all k=2,...,24. The first-six-moment Hankel matrix is positive definite. All 21 report links resolve. Final audit RSS about 98 MB; plotting RSS about 114 MB. CSV/dictionary memory budgets were conservatively revised to 128 MB to include Python object overhead.

2026-11-12 23:58 +04 — Rechecked the load-bearing proof: the only linear endpoint term uses exact E B=0; uniform lower-moment errors require no rate; c>=2 errors lose a logarithm; signed transfer covers odd moments; the factorial bound yields exponential integrability only after a tight subsequential limit is constructed. This avoids assuming existence or determinacy from a formal moment recursion. Recomputed a2 and a3 from zeta formulas, and higher constants by canceled/direct-generator recurrences. All numerical assertions passed. Source and JSON syntax, balanced math delimiters and equation tags passed. Shared-brain writeback remains unavailable under this sandbox; the durable result and its evidence are contained in REPORT.md and the audit files.

Task completed: “prove that (S_n - E S_n)/(n log n) converges in distribution, identify the limit … and prove convergence of all moments” — received 12 November 2026, approximately 23:43 Asia/Tbilisi.
