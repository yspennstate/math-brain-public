# C0033 research log

All times use Asia/Tbilisi (UTC+4). Task received 2026-11-13, approximately 01:35.

## 2026-11-13 01:37

- Scope: finite DPP entropy concavity, real and complex kernels, including circulant families. No subagents. Computations will use one BLAS thread and run at nice 10 or greater.
- Workspace initially contained only PROMPT.md and runner files. Shared mesh registration, digest, claim and checklist writes were attempted; the shared SQLite store is read-only under the sandbox. All research mutations are confined to this isolated workspace. No live conflicting claim was reported.
- Compute governor: status ok, owner_away_open. Numerical libraries available: NumPy 2.2.3, SciPy 1.15.2, mpmath 1.3.0. clang++ and pdftotext available.
- Brain recall located prior work on the two-point theorem and fourth-order behavior at block diagonal kernels. Read the complete three relevant memory nodes. They are leads to audit, not accepted proofs.
- Retrieved web versions of Gu's report, Lyons 2003, and Lyons's ICM 2014 survey. Bibliographical correction: the finite conjecture is Conjecture 9.2 in Lyons 2003; Conjecture 5.3 is the entropy-rate conjecture in the 2014 survey.
- Simultaneous diagonalization by an arbitrary unitary does not turn a DPP into a coordinate product measure. Coordinate-diagonal kernels do give products.

## 2026-11-13 01:44

- Re-derived and symbolically verified the two-point Hessian determinant identity with SymPy. A short estimate using xy <= 1/4 and exp(l)-1 >= l^3/6 proves the required positivity. This proof is distinct from the published local paper's direction-by-direction proof, but the two-point theorem itself is prior work.
- Located the public prior paper through the connected GitHub tool, read paper/main.tex, and saved it with its blob SHA in sources/. Its two-point and sharp quartic theorems will be attributed as prior results; no novelty claim for them.
- Derived conditional-kernel lifting: an m-coordinate supported perturbation reduces to conditional m-point kernels. Combined with the two-point theorem this proves all directions supported on two coordinate indices in arbitrary dimension.
- Main search: 3,000 full Hessians (n=2..6, real/complex, uniform and extreme spectra); 8,060 directional and midpoint trials (n=3..14); 16,036 Nelder–Mead evaluations of the largest full Hessian eigenvalue (n=3..5). No substantial positive curvature or negative midpoint gap.
- Targeted search: 10,285 evaluations of circulant-symbol Hessians (n=3,4,6,8) and 2,000 genuine rank-two midpoint tests (n=3,4,6,8,10). Largest apparent optimized positive value approximately 7.4e-10, at an ill-conditioned circulant kernel; all optimized witnesses are being re-evaluated at 80 and 120 decimal digits.
- The first numerical pass exposed floating-point exception flag warnings in this host's Accelerate complex matrix multiplication despite finite results. Replaced spectral reconstruction by explicit contractions, added finite-input/output checks, and reran the entire main search. Reported numbers will use this rerun. Inherited process priority is already nice 10; attempts to increase it were refused by the sandbox. One numerical process at a time except brief overlap of main and targeted searches; one BLAS thread per process, no pools. Main search peak RSS about 94 MB.

## 2026-11-13 01:53 — completed deliverables

- REPORT.md begins PARTIAL. It contains complete proofs of the complex two-point theorem, conditional-coordinate lifting, ambient Hessian decomposition at block diagonal kernels, and the sharp explicit fourth-order formula at arbitrary coordinate product kernels. General n=3, arbitrary rank-two, commuting, cyclic/Toeplitz, and entropy-rate concavity remain unresolved.
- Final numerical runs: 3,000 full Hessians; 8,060 directional/general midpoint trials; 16,036 full-Hessian optimization evaluations; 10,285 circulant-symbol optimization evaluations; 2,000 genuine rank-two midpoint tests. No negative midpoint gaps. No rejected numerical evaluations.
- All 14 saved optimized witnesses were independently evaluated at 80 and 120 decimal digits. All curvatures were negative. Largest apparent positive double value: 7.388840613197159e-10 (complex circulant n=6); at 120 digits it is approximately -1.1996122583386526e-11. The two precisions agree within 3.1996e-77 in absolute curvature.
- Independent checks: 96 random kernels, Mobius atoms vs determinant atoms (maximum absolute discrepancy 3.3033e-16); C++ directional curvature vs NumPy full Hessian (1.2435e-14); normalization of derivatives (2.332e-15). Rational complex direct entropy second differentiation agrees to 3.715e-96. Conditional kernels and entropy chain rule agree within 1.12e-15. Product-kernel formulas were checked in 200 random cases and by a direct 100-digit fourth derivative with zero printed residual.
- Final main-search peak RSS 98.88 MiB; targeted peak 89.55 MiB. All code compiles/imports. Final computation logs have no numerical exception warnings or tracebacks. The final rerun explicitly projects real circulants onto real matrices, eliminating residual imaginary roundoff in the real-labeled witnesses.
- Downloaded all ten primary PDFs in sources/manifest.json, including Lyons and Gu; saved source texts, URL/hash manifest, and the existing two-point preprint source with its GitHub blob SHA. No general solution was found in the targeted literature search; no novelty claim is made for prior theorems.
- Durable mathematical observation: conditional kernels depend affinely on an updated coordinate block when its complement and cross entries are fixed. This lifts any m-point concavity theorem to m-coordinate changes in arbitrary dimension. At a product kernel, the t^2 probability score is a sum of orthogonal centered pair statistics, giving the explicit sharp quartic formula even when the perturbation graph has odd cycles. Shared brain write-back and checklist completion cannot be published from this sandbox because their stores are read-only; these results are retained here with proofs and reproducible data.
- No shared repository changes, publication, deployments, subagents, or extra model workers. All research artifacts are in this workspace.
