# D0036 work log

- Task received 2026-11-13, approximately 10:12 +04: investigate Bradley Question 8, literature first, then proofs and numerical evidence if needed.
- Scope: this directory only; no publication or pushes; no subagents. All computational scripts run at nice 10, with numerical library thread limits of 1 (at most 4 allowed), and small memory footprints.
- Read startup memory, recalled Bradley-related past work, and read the mesh protocol. Recall found no D0036 result. The explicit directory-only restriction and filesystem sandbox prevent updating the global mesh/checklist/brain; this local log is the task record. No shared project files will be edited.
- Compute state at start: warn/cpu_saturated, owner_away_open. Work will remain lightweight and serial.
- Retrieved the source in the web reader; local text extraction next. Literature search has already surfaced Helson–Sarason's past/future theorem, which concerns r, not the interlaced coefficient r*; it must not be mistaken for an answer.

## Literature stage (saved before proof work)

- Saved Bradley 2005 full extracted text and read §§6.1–6.6, especially equations (6.1)–(6.8), Theorems 6.1–6.5, and Question 8. Exact location: journal p.131 (PDF p.25) for Theorem 6.5; journal p.132 (PDF p.26) for Question 8.
- Saved Bingham arXiv:1108.0368 and the published 2012 HTML text. The published §7.1, p.309, is about past/future rho mixing, not rho*. The user attribution to Simon is a bibliographic slip: Bingham is the author, Simon the author of the works it surveys.
- Saved Bradley's later Philipp-volume paper. Remark 1.5(g), preprint p.6, points to 2007 vol.3 Theorems 25.47 and 28.38; Remark 1.15, pp.12–13, points to vol.3 Chapter 28 and Bradley–Utev, and discusses unresolved spectral questions for continuous-index fields. This is not an answer to Question 8.
- Publisher contents for all three Bradley volumes saved: vol.1 Chapter 8 (second order properties), vol.2 Chapter 23 (linear dependence conditions), vol.3 Chapters 27–28 (Gaussian processes; linear dependence and spectral density). Full book chapters were not accessible; no claim to have read them.
- Bradley 1983 (Equivalent measures of dependence), Bradley 1992, Bradley 2002, Bradley 2003, Helson–Sarason, Sarason addendum, Peller–Khrushchev, Ibragimov–Rozanov, Kolmogorov–Rozanov, and Miller searched. Several full texts are inaccessible. Project Euclid returns an anti-bot page, Springer provides subscription previews, Math-Net links redirect or return 403. Helson–Sarason PDF received in memory is image-only and yields zero extracted characters: no PDF or image retained. This limitation is recorded rather than treating a blank extraction as a read paper.
- Searched later work with interlaced/rho-star/r*/spectral-density/characterization terms and date terms through 2026; results include limit-theorem papers, Bradley 2011/2014/2015 constructions, Tone 2011/2013, and unrelated spectral results. No exact published resolution located. This is a search outcome, not proof the problem is still open.
- Fetch utilities inherit nice=10 from launch.sh. Applying `nice -n 10` again produced a sandbox setpriority warning; confirmed inherited priority 10 using os.getpriority. No extra workers launched.
- Proceeding to proof work with provisional status PARTIAL; do not assert a general polynomial-times-positive-continuous characterization without proving its necessity.
- Source-fetch correction: the EMIS published-Bingham endpoint returned PDF bytes despite an HTML request. Detected the malformed extraction immediately and replaced it; fetcher now checks PDF magic regardless of requested mode. Final retained files contain readable plain text only. Image-only sources are explicitly marked as unreadable.

## Proof stage

- Saved REPORT.md with provisional PARTIAL status and complete arguments for polynomial-factor sufficiency, a finite-power-zero equivalence, and two explicit examples.
- Key necessity argument in the restricted class: Helson–Sarason (as precisely stated in Bradley Theorem 6.2) plus the fact that a conjugate Poisson integral of a continuous function is o(log(1/(1-r))). Radial logarithmic order therefore must equal twice an integer polynomial multiplicity.
- Continuous counterexample chosen to permit exact checks: f=(pi/4)|1-z|, covariance gamma(k)=1/(1-4k^2), block variance sum_{j=1}^L 1/(2j-1), and an r*(n) lower bound 1/2 for every n.
- General characterization remains unproved. Next: numerical canonical correlations with correct interlaced-set constraints, independent covariance checks, then proof and source audit.

## Numerical stage and checks

- Completed exact support maximization in a window of 12 for gaps 1,2,3,4,6, for eight models. For each S, all allowable T may be included because enlarging a span cannot lower its maximal correlation, reducing exhaustive search to 2^12 supports.
- Completed larger-window support-family computations (windows 64,128,256,512; gaps 1,2,4,8,16,32,64), plus exact-covariance block-sum computations through L=262144. Saved CSV data and metadata.
- Main run: nice 10, one numerical thread, 3.1 seconds, peak resident memory about 175 MB. Analytic Fourier coefficients independently checked by quadrature; Cholesky/SVD correlations checked by a generalized eigenvalue method; difference checkerboard values checked against cos(pi/(W+1)); atom-plus-white-noise block values checked against L/(L+1). Largest recorded discrepancy below 2e-15.
- The first generalized-eigenvalue cross-check produced NumPy matmul floating-point flag warnings despite finite matching results. Replaced that small independent multiplication with direct einsum and added an explicit finite-value assertion; full rerun passes without numerical warnings. No regularization or eigenvalue truncation is used.
- Plot generated as data/correlations.svg. It is a numerical figure, not a page image. Larger-window values are labeled sampled lower bounds. In particular, the cusp's W=512 lower bounds decrease below 1/2 as n increases even though the proved full coefficient is at least 1/2 for every n. This finite-window trap is explicitly documented.
- Read the accessible full Peller 1998 §10 account: Theorem 10.1, printed p.95, confirms the VMO factorization concerns past/future complete regularity. Saved full extracted text; this helps verify the classical dependency and provides an independent VMO check on the power-zero necessity argument.

## Final audit and result

- Completed REPORT.md (first line exactly PARTIAL), consolidated sources/LITERATURE_LEDGER.txt, code, CSV data, reproducibility metadata, and standalone numerical plots.
- Rechecked the finite-power theorem by both the radial conjugate-Poisson argument and the VMO mean-oscillation obstruction; the latter has explicit nonzero constant 8/e - 4 log 2. The result is restricted to the stated two-sided power asymptotics, not merely comparable bounds or oscillating quotients.
- Rechecked differenced-white-noise covariances, its interlaced correlation-one witness, and its past/future boundary mode. Rechecked the cusp normalization, covariance signs, harmonic-sum block variance, and fixed-gap limiting correlation. General polynomial-factor necessity is still unproved.
- Flagged the survey's VMO gloss: the precise classical condition is on the logarithm after removal of a polynomial factor, not on f itself. The accessible Peller Theorem 10.1 is used for the independent audit.
- Numerical plot visually inspected. The large-window curves are expressly lower bounds; no numerical decay claim is promoted to proof.
- Format audit: sources/ contains only readable .txt files, no NUL bytes or PDF magic. No PDFs, paper images, or scans retained anywhere in this directory. Final report has no pending placeholders. No publication, git changes, pushes, subagents, or shared-brain mutations.
- Task completed as a partial investigation: full sufficiency of f=|P|^2 g with continuous positive g; exact equivalence for finitely many power-law zeros; explicit continuous Lipschitz counterexample to weaker candidates; general Question 8 and inaccessible-literature status remain unresolved.
- Task: “Open problem D0036” — received 2026-11-13, approximately 10:12 +04.
