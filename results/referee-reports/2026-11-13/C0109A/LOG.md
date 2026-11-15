# C0109 work log

Task received: 2026-11-13 09:00 Asia/Tbilisi (clock at first inspection: 09:00:40).
Request: investigate the optimal circular-law convergence exponent under a finite (2+epsilon)-moment assumption, literature first, then rigorous partial results and numerical evidence.

## Scope and environment

- Work is confined to this directory, as explicitly requested. No subagents, pushes, publication, or shared-brain/checklist/mesh writes outside this directory. Startup memory and the mesh protocol were read; brain recall returned no useful prior result.
- Initial governor: warn / owner_away_open, CPU saturated. Numerical work will use nice 10 and one BLAS thread, one matrix at a time; no more than 4 GB.
- Source PDFs will only pass through memory to pdftotext via stdin. Only plain text is stored in sources/; no page images.

## Literature stage (in progress)

- Located original arXiv:0810.2994 and Götze–Jalowy arXiv:1807.00489, Jalowy arXiv:2111.03595 and arXiv:1912.09300.
- Located a 2020 Williams SMALL 2018 manuscript claiming an unspecified absolute constant times min(epsilon,1) exponent; this is not yet an optimality theorem.

### Source correction

Original Section 6, p.22 has no named metric and does not itself assert an optimal exponent. It states existence of some polynomial exponent with unclear dependence on epsilon. The cited [54] must be read to identify the metric and probability mode.

The suggested inference “large heavy-tailed entries create outlier eigenvalues” is invalid for nonnormal matrices. BCCT (2018) and Bordenave–Chafaï–García-Zelada (2022) give no-outlier results; these will be checked and included.

The launcher already gives this process nice 10 (verified with os.getpriority). Invoking nice -n 10 attempts an additional change and is denied by sandbox; run directly at inherited nice 10.

### Literature stage conclusion before numerical work

No checked reference resolves the exact optimal exponent under only finite (2+epsilon) moments. Götze–Jalowy v3 Theorems 6–7 require all moments and explicitly describe their result as a partial answer in Section 2.3. Theorem 8 requires 4+delta moments and restricts discs to the bulk. Jalowy's Wasserstein Theorem 1 also requires all moments. Source text includes exact statements and numbered pages.

Williams manuscript fetch returned HTTP 403. Browser-indexed Proposition 1 claims an absolute unspecified kappa times min(epsilon,1), not an optimal exponent. Do not rely on it as a verified proof.

Saved an initial PARTIAL report before simulations. Planned proof: fixed-law multiscale rare-variance construction, using Götze–Jalowy's all-moment theorem only for each finite truncation. For epsilon<2/3 this obstructs any universal exponent greater than 2epsilon/(2+epsilon) in probability. This is an upper restriction on admissible exponents, not an upper convergence estimate.

### Rigorous partial result saved

code/lower_bound_proof.txt proves a fixed-law obstruction: for 0<epsilon<2/3, any exponent delta>2epsilon/(2+epsilon) fails even in probability for some fixed symmetric variance-one law with finite p=2+epsilon moment and infinite every higher moment. It applies to the original orthant metric and disk discrepancy. The proof uses printed Götze–Jalowy Theorems 6–7 only for each fixed finite truncation, with inductively chosen sizes. The obstruction is missing variance, not outlier eigenvalues. No optimality or matching upper bound is claimed.

### Explicit upper rate derived

A direct route avoids the inadmissible all-moment truncation step. Götze–Tikhomirov Theorem 2.2 gives an expected Hermitized CDF rate n^{-min(epsilon,1)/12}; row bounded differences promote it to a random CDF rate; Tao–Vu Theorem 2.1 permits logarithmic integration; Fubini plus deterministic logarithmic-potential integrability yields L^r control; Götze–Jalowy smoothing yields every delta<min(epsilon,1)/24. Full proof and all probability quantifiers saved in code/upper_bound_proof.txt. A concrete exponent is min(epsilon,1)/25. This is nonoptimal and does not close the gap to the lower construction.

### Final audit and result (2026-11-13, approximately 09:18 Asia/Tbilisi)

- REPORT.md is complete and begins exactly PARTIAL. It contains the original source/metric correction, a theorem-by-theorem literature table, valid truncation estimates and the local-law hypothesis gap, full upper and lower proofs, a separate matching Ginibre W_1 order, numerical methods/results, and reproducibility commands.
- Upper proof was re-derived from the mean Hermitized CDF exponent and smoothing optimization; care taken not to infer simultaneous-in-z smallest-singular-value control or take a supremum of a logarithmic potential at eigenvalues.
- Lower proof was audited for a fixed law, finite endpoint moment, divergence of every higher moment, the no-tail coupling probability, dilation invariance, and the marginal derivative constant. It proves a subsequence obstruction, not an all-n asymptotic or matching upper rate.
- 60 numerical matrices completed, n=128 through 2048, epsilon=.25,.5,1,2, 3 replicates. Peak reported RSS 440.8125 MiB; inherited nice 10; configured one numerical thread. Total measured computation time 73.26 s. Fitted slopes and last-three-size fits saved in data/fits.json.
- Independent checks: orthant metric equals brute-force corner counting; disk CDF agrees with quadrature within 7.57e-10; normalization within 2.4e-13; derivative check within 9.36e-12.
- 17 paper texts saved, 2,632,856 total source bytes including notes/metadata. Every manifest hash verified. No PDFs, page images, scans, or raster images retained. data/convergence.svg is an original plot of simulation data.
- Read the 2024 Bai–Hu convergence theorem and 2025 Osman sparse-bulk theorem as later checks. Also distinguished AEK's 1612.07776 bulk paper from its 1907.13631 edge paper used by Götze–Jalowy.
- Exact optimal delta(epsilon) remains unresolved in this work; no checked printed reference resolves it. No publication, pushes, subagents, or external shared-state writes were performed.

Task completed locally: “Open problem C0109” — received approximately 2026-11-13 09:00 Asia/Tbilisi (first clock 09:00:40).
