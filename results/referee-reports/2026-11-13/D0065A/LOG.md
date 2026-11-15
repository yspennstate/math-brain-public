# D0065 work log

Task received: 2026-11-13, approximately 10:46 +04 (Asia/Tbilisi): “Open problem D0065.”

## 10:49 +04 — working

Read startup memory and compute state (ok, owner away). No subagents. The current task's “work only in this directory” rule takes precedence over global requests to update external brain/checklist/mesh stores; all task records stay here. No publication or git operations. Literature first; sources will be plain text extracted from PDF bytes held in memory, with explicit PDF page boundaries. No PDF or page image will be written to disk. Computation will be one process at nice 10, with numerical library threads limited to one.

## Literature findings saved (first pass)

- Review downloaded and extracted into `sources/rhodes_vargas_1305.6221.txt`; Conjecture 6.5 is on PDF/printed p. 53. Covariance (2.12) has coefficient one; c_n is the variance, with an explicit warning that bad/nonstationary cutoffs leave it ambiguous (p. 50). There is no formally quantified cutoff class in Section 6.4.
- Madaule's published Theorem 1.1, p. 1371 (PDF p. 3), proves the maximum/derivative-chaos assertion for C^1 compactly supported star-scale kernels, every integer d >= 1; c_n=t exactly.
- DRZ Theorems 1.3–1.4 require microscopic and macroscopic covariance limits as well as log-correlation. Its Z is a discrete derivative-type limit; identifying it with a specified continuum normalization requires work.
- Normalization audit: a standard maximum Gumbel H has E exp(-s H)=Gamma(1+s), s>-1. The shift alpha^{-1} log(c M) produces c^{-q/alpha}, not c^{-q}. The review's constant is c=C^{1/alpha} if C is the coefficient in E exp(-C M exp(-alpha x)).
- Additional nonstationary issue: Biskup–Louidor's Theorem 2.9 identifies the intensity with critical LQG, which includes rad_D(x)^2 relative to fully variance-subtracted derivative chaos. DRSV Definition 11, Eq. (23), PDF p. 12, explicitly gives this factor. It cannot generally be hidden in a scalar.
- The “Ding–Gwynne–Wirth” author combination has not been located; searches instead return Ding–Gwynne–Zhuang (metrics) and Ding–Wirth / Ding–Wirth–Wu (level-set crossings). Will document the ambiguity rather than invent a citation.

## 10:55 +04 — report drafted, simulation complete

`REPORT.md` uses PARTIAL for the full requested scope, while explicitly recording the literature resolutions of the star-scale model in all dimensions and the normalized 2D DGFF. Added a complete perturbation counterexample for an unrestricted interpretation of cutoff approximation: alternating X_n and (1+a/n)X_n preserves the limiting generalized field but creates limiting centered maxima G and G−sqrt(2d)a. This does not assert membership in a fixed normalized mollifier class.

Simulation: 1,024 trees per dimension, d=1 b=2 depths 10/12/14/16; d=2 b=4 depths 5/6/7/8. Three disjoint sample groups for empirical SH mass mixture, location calibration, and validation. Saved all signed derivative sums without clipping. At largest depths mixture/plain CDF distances: d=1 0.0271/0.1755; d=2 0.0587/0.1626. Nice 10; one process/one library thread; peak RSS 420,511,744 bytes; runtime 3.65 s. Attempts to set RLIMIT_AS were rejected by macOS; bounded batches and an RSS guard are used. Early attempts stopped before simulation. Matplotlib cache redirected inside data/.

Publisher retrieval limitations: Euclid article URLs returned HTML security pages; IMS issue PDF returned an HTML security page to direct requests and 502 through web open. Their bytes were never saved as papers. arXiv primary texts were retained, and page references explicitly identify those versions. The published Madaule article and Junnila–Saksman–Webb reprint were retrieved successfully. Institutional Junnila–Saksman journal mirror returned 403; preprint remains available. No missing citation was guessed.

## 10:59 +04 — done

Final independent audit passed: 8,192 CSV records; all eight summary groups and CDF distances independently recomputed; Gamma formula agreement <3e-13; cutoff perturbation algebra checked two ways in d=1,2,3. Verified exact source page markers and corrected Biskup–Louidor Theorem 6.1 to PDF p. 36. Added Aïdékon–Shi Theorem 1.1, reprint PDF p. 4, to justify the BRW SH proxy normalization. Twenty-one source texts, all plain .txt; no PDF/DjVu/PostScript retained. Code, data, report, and log all remain in this workspace. No subagents, publication, commits, pushes, or external task-store writes.

Deliverable: REPORT.md, status PARTIAL for the full requested scope; literature resolutions precisely delimited, Gamma/constant proof, nonstationary spatial-weight audit, rigorous unrestricted-cutoff perturbation example, and small d=1,2 evidence simulations. General fixed-cutoff/graph scope is not overclaimed. Task: “Open problem D0065.” Received approximately 10:46 +04 on 2026-11-13.
