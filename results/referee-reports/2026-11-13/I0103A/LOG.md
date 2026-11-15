# I0103 work log

Task received 2026-11-13 21:34 +04: “Open problem I0103” (Paley ETF, Randomstrasse101 Conjecture 29).

## 2026-11-13 21:36 +04 — scope and orientation

- Work is confined to this directory. No agents, publication, pushes, or external state changes. Global brain/mesh/checklist commands that write outside this directory are not run under this task's narrower instruction. Startup memory, relevant Paley memory, mesh protocol, and compute status were read without mutation.
- Compute state reports warn/cpu_saturated, not distress. Use one compute thread, nice 10, small matrices; no large search.
- Sources will be stored as plain text. PDF response bodies will only pass through memory into pdftotext; no PDF files or page images will be created.
- Source correction found: the 2025 open-problem collection is arXiv:2603.29571 (submitted 31 March 2026), distinct from the 2024 collection arXiv:2504.20539.
- Located BFMW arXiv:1202.1234; BMM arXiv:1410.6457 (IMRN 2017, 372–381); Satake arXiv:2011.02907; Kunisky–Yu arXiv:2211.02713; Kümmerle–Mixon arXiv:2611.14475. Exact statements and page references pending text extraction.

## 2026-11-13 21:39 +04 — literature and first exact obstruction

- Downloaded the named papers directly from arXiv and converted in memory. Hashes, retrieval times, versions, and text page counts are in data/source_manifest.jsonl. Metadata pages retained as text.
- Process already has nice 20. Attempt to add 10 failed because it would exceed the permitted range; fetch code now preserves an existing nice >=10. No heavy work ran at elevated priority.
- Read Kümmerle–Mixon Sections 1–4 and the barrier statements: Theorem 1 p.3; Lemma 3 pp.5–6; equation (9) p.6; Theorem 4 pp.6–7; Theorem 6 p.10; Lemma 7 and Proposition 8 p.11; bound (16) p.12; Proposition 10 pp.12–13. The graph is elliptic affine polar VO^-_4(q), not the Paley graph.
- Exact Paley obstruction: for every s-column restriction, the absolute off-diagonal Gram matrix is p^{-1/2}(J_s-I_s), with norm (s-1)/sqrt(p). Thresholding has only two cases: all edges or no edges. No choice of column subset changes this. Thus neither excluding cliques nor selecting a large sub-dictionary makes the phase-agnostic method work above sqrt(p).
- Corrections to supplied background: BFMW Theorems 20,23 and Conjecture 25 do not establish clique bound => RIP. BMM Theorem 2.3 establishes discrepancy => RIP => a clique bound. The general explicit-RIP record was also improved by Ford–Kutzarova–Shakan (2022), arXiv:2108.01794, Theorem 1 p.2.
- Recent and adjacent texts acquired: Kunisky spectral pseudorandomness arXiv:2303.16475; Satake extractor arXiv:2405.08608; Gaar–Pucher arXiv:2412.12958v2 (2025 revision); King arXiv:2505.00160v3 (2026 revision); Cai–Zeng–Zhang arXiv:2606.08913; Zahl arXiv:2002.11677. No settlement of full Paley RIP found in the bounded literature search so far.

## 2026-11-13 21:40 +04 — signed sub-dictionary route

- Found a promising unconditional application of mixed Burgess sums to an interval of Paley columns. Heath-Brown–Pierce arXiv:1404.1677, Theorem 1.4 p.5 gives a bound uniform in real linear phase: for r=3 and H<p^{5/8}, |sum_{n<=H} chi(n)e(theta n)| << H^{2/3}p^{1/8+eta}.
- A consecutive-column Gram deviation is Toeplitz. Its symbol is 2 Re sum_{1<=h<N} chi(h)e(theta h), so its norm is at most twice this uniform mixed-sum bound divided by sqrt(p).
- Candidate rigorous partial theorem: N=floor(p^{9/16-rho}) finite columns, plus the special column if desired, have full Gram norm deviation O_rho(p^{-rho/3}+sqrt(N/p)). Thus every subset is uniformly well conditioned, including sparsity p^{1/2+eps} for eps<1/16-rho. This would be p^{1-delta} columns with delta=7/16+rho, not a positive fraction. It is a tall sub-dictionary and does not settle full-frame RIP. Proof and independent audit next.

## 2026-11-13 21:43 +04 — proof audit and numerical checks

- Verified the mixed-sum theorem is unconditional at degree 1: Heath-Brown–Pierce Theorem 1.4 p.5 explicitly follows from the elementary degree-1 Vinogradov mean-value estimate. Its implicit constant is independent of the real linear phase. With r=3, the allowed length is H<p^{5/8}; the bound is H^{2/3}p^{1/8+eta}. The interval length p^{9/16-rho} is strictly inside that range.
- Re-derived the exponent in exact fractions: (2/3)(9/16-rho)+1/8+rho/3-1/2 = -rho/3. Independently, at rho=1/32 the raw exponent before eta is -1/48. The special column adds a border of norm sqrt(N/p).
- Full proof uses the Fourier integral identity for the Toeplitz quadratic form, then the mixed-sum bound, a block-matrix triangle inequality for the special column, and principal-submatrix compression for all subsets. No numerical assumption enters it.
- code/check_paley.py passed independent Fourier/Legendre Gram checks, exact conference identities at p=101,257, affine-progression identities, a finite circulant compression bound, and Fourier quadrature checks of the Toeplitz Rayleigh identity. Five primes through 2017; one thread, nice 20, about 36 MB peak RSS. Initial NumPy complex BLAS calls emitted floating-point status warnings despite finite correct results; replaced those verification products by direct einsum contractions and reran cleanly.
- Bounded search: three seed types, 40 swap proposals per seed, two sparsity exponents, five primes. Saved the best witnesses and eigenvalues; no counterexample conclusion drawn.
- Obtained the CCC 2023 published text: Kunisky–Yu's main lower bound is Theorem 2, p.30:4 (Theorem 1.2 p.4 in the expanded arXiv v2). This bounds the SOS relaxation value, not the actual clique number.
- Additional primary manuscripts checked: Wang–Shen–Kobzar (undated author copy), Theorem 3.4 p.9 and Corollary 3.10 p.11; Kaplan–Pohl–Boche (SampTA 2019), Theorem 6 p.3, which concerns a different concatenation of two bases and structured supports.
- Literature search was bounded and primary-text based. Searches covered exact titles, “Paley ETF RIP 2025 2026”, “Paley graph discrepancy 2025 2026”, “explicit RIP square-root bottleneck 2025 2026”, and the proposed Burgess/interval connection. No settlement of full Conjecture 29 or existing statement of the specific interval corollary was found. No novelty claim is made for a direct consequence of a 2014 theorem.

## 2026-11-13 21:49 +04 — completed

- REPORT.md completed with first line PARTIAL, exact source identity, the unconditional interval sub-dictionary theorem and full proof, the precise failure of the absolute-value argument on all Paley restrictions, a quantified conditional discrepancy reduction, and exact numbered primary references with pagination conventions.
- Independent final numerical audit reconstructed all ten saved search witnesses directly from Fourier columns and used SVD. Their squared singular values and conditions agree with the character-Gram calculation to 1.65e-14. The audit used one thread, nice 20, 37.6 MB peak RSS.
- Verified hashes for 22 retained primary-source texts, source metadata index, Python syntax, report math delimiters, and absence of PDFs or page images. Two formatting issues found during readback (first inline math delimiters and a leftover checkpoint sentence) were corrected.
- Result: explicit floor(p^{9/16-rho})+1-column Paley sub-dictionary with all subset condition numbers tending uniformly to 1, for every fixed 0<rho<1/16. Its fraction tends to zero and it is tall. Full Conjecture 29 remains unresolved in this work; no actual growing-condition counterexample was proved.
- All requested files are local. No subagents, publication, pushes, global brain/checklist writes, or other external mutations.
