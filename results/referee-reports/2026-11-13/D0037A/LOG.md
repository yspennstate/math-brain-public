# D0037 work log

Task received: 2026-11-13, approximately 05:31 Asia/Tbilisi (workspace launch time). User: “Open problem D0037.” Literature first; Gaussian angle reduction; spectral characterization attempts; counterexamples and optional numerics. All artifacts stay here. No subagents, publication, or pushes.

## 2026-11-13 05:33 +04 — orientation and source

- Read startup memory and compute state. Machine is CPU saturated; use one numerical worker, nice 10, with small matrices and no heavy sweeps.
- Consulted brain recall for Gaussian interlaced mixing; returned adjacent Bradley problems, no answer to Question 9. No recalled result is treated as a proof.
- Global mesh registration/digest failed with “attempt to write a readonly database.” The sandbox and current task restrict writes to this directory. Created a **local-only** mesh in `data/mesh/`, registered `codex-d0037a`, and claimed this workspace. This does not constitute registration in the global mesh. Global brain/checklist writes will not be attempted; local records preserve the work.
- Downloaded arXiv:math/0511078 into `sources/bradley_2005_survey.pdf` and extracted `sources/bradley_2005_survey.txt`.
- Read definitions, Section 7, and relevant Section 6 statements. The target definition is rho-star(n) tending to zero, not merely less than one at some lag.
- Important existing partial results: survey Theorems 6.3–6.5, identity (7.1), and Theorem 7.1. The survey itself states Question 8 for linear interlaced correlations and Question 9 for Gaussian sequences.
- Immediate counterexample to lower boundedness as a necessary condition: differenced white noise has density `|1-z|^2` and rho-star(n)=0 for n>=2. This will receive a full proof after the literature pass.

## Literature search in progress

Searches so far: Bradley Gaussian rho-star/interlaced mixing spectral characterization; exact question wording; Bradley 1992 and 1993; Miller 1994. No later resolution located yet. This is a search result, not a claim that the problem is still open.

## 2026-11-13 05:38 +04 — literature pass saved

- Created `sources/SEARCH.md` with exact source roles, queries, and access limitations. In particular, the 2007 full book chapters were not available. No claim that every 2005–2026 paper has been ruled out.
- Read Sarason's 1975 Section 3 directly: it concerns past/future, not interlaced sets. It uses a weighted class W0 rather than claiming the density itself must simply lie in VMO.
- Downloaded official Helson–Sarason scan, Samorodnitsky's 2006 survey, Bradley's 2011/2012 random-field paper, and Bradley–Tone's 2015 preprint. Springer metadata/abstracts verified for Bradley 1992 and Miller 1994. Project Euclid responses were HTML, renamed so they are not mistaken for PDFs.
- Local checklist entry `T-20261113-001` records the ask (global store cannot be written under this task's directory restriction).
- Numerical child reports inherited nice=15. This is lower priority than the requested nice=10; do not attempt to raise it. Explicit `nice -n 10` printed an OS error under the inherited priority; ordinary children already run politely.
- Begin proof work: Gaussian chaos reduction, polynomial filtering, wrong-candidate counterexamples, and finite Toeplitz checks. Existing sharp distinctions from Theorems 6.4–6.5 will be cited precisely.

## 2026-11-13 05:53 +04 — proofs and numerical audit

- Saved the full report with first line PARTIAL. No necessary-and-sufficient characterization is claimed.
- Proved the Gaussian angle reduction using canonical Gaussian coordinates and Hermite expansions, then finite exhaustion and the spectral isometry.
- Reproved the classical rho-star(1)<1 / bounded-positive-density equivalence. A residue-class sign argument also gives the upper bound f <= N(1+c)/(1-c) Var(X_0) if rho-star(N)=c<1.
- Proved sufficiency of f=|P|^2 g with g continuous strictly positive, and equivalence of this class to relative approximation by nonnegative trigonometric polynomials. Necessity for rho-star mixing is explicitly left open.
- Counterexamples: differenced white noise has rho-star(1)=1 and rho-star(n)=0 for n>=2; f=1+a sign(cos t) has rho-star(n)=a for every lag. The latter lower bound was checked by a shifted Hilbert-kernel sum and an independent logarithmic integral calculation.
- Constructed explicit continuous odd v from F(z)=log log(4/(1-z)). Its conjugate is unbounded. f=exp(Hv) is continuous with one slow zero and is ordinary rho-mixing, but rho-star(n)=1 at every lag. Proved the last assertion twice: Bradley Theorem 6.4(c), and a direct periodic-block/Fejer construction. The reciprocal is integrable and unbounded and also has every rho-star(n)=1.
- Periodic-block proof also excludes f=|1-e^{it}|^alpha for 0<alpha<1; this is not extended without proof to other exponents.
- Numerics: 324 finite matrix checks and 108 periodic limits. SVD vs generalized eigenvalues agreed within 3.34e-16; differenced-noise exact singular values checked independently. Final run with Python warnings treated as errors passed. Runtime 0.55 seconds, peak RSS 92,127,232 bytes, one BLAS thread, inherited nice 15.
- Initial NumPy matmul calls emitted floating-status warnings despite finite matching results. Replaced that product by explicit einsum summation and required all solve entries to be finite; final warning-as-error run passed. The backend cause was not established.
- Visually read the Helson–Sarason image scan: Theorem 5 pp. 10–12 and Theorem 6 pp. 14–15. Sarason 1975 Section 3 independently confirms the continuous u,v refinement.
- Reference audit corrected Rosenblatt's relevant 1972 item to the Sixth Berkeley Symposium paper, vol. 2, pp. 551–561. The survey's Sarason bibliography year is 1974; publisher document/DOI give 1975, used in REPORT.md.
- Several write-tool attempts to replace the report failed validation or JavaScript parsing before mutation. The report was then saved in two sequential shell heredoc writes and checked; no partial tool failure is treated as a saved result.

## 2026-11-13 05:56 +04 — source-count correction and independent theorem check

- The `file` command's quick PDF counts were misleading: pypdf reports 15 pages for Sarason and 62 for Shaw, and full pdftotext confirms them. Corrected SEARCH.md, which had mistakenly called Sarason ten pages and Shaw only front matter. No missing pages were actually downloaded.
- Read Shaw's abstract, contents, discrete-index Theorems 3.1–3.5, proof of Theorem 3.3(C)=>(A), and continuous-index Theorem 4.1. They independently confirm the lag-one-qualified boundedness/continuity statements used in the report. No full Gaussian interlaced spectral characterization appears in these statements. Added the exact dissertation reference.
- The proof audit checked complexification, Gaussian nonlinear/linear equality, normalization by dt/(2 pi), the distance loss under filtering, the step-density Fourier signs and logarithmic integral constant pi, and the order of limits in the periodic argument. The gap masks have exactly 2(n-1) residues per period and distance exactly n.

## 2026-11-13 05:57 +04 — final saved result

- REPORT.md begins exactly PARTIAL. It contains definitions, literature outcome and access limitations, full proofs, candidate verdicts, numerical checks, and 20 exact references.
- `sources/MANIFEST.json` records source URLs where available, SHA-256 hashes, and parser-verified PDF counts. `data/audit.json` confirms valid local report links, Python syntax, 324 finite-set checks, 108 periodic checks, valid set separations, unit-interval correlations, and the compute limits.
- Local checklist T-20261113-001 marked done with the partial research result; no owner “seen” mark changed. Closing the local-only mesh releases this workspace claim. Global coordination/memory writes remain unavailable and were not bypassed.
- Result: no full iff characterization; proved counterexamples to the suggested necessities and continuity-only repair, a substantial sufficient class, and an explicit continuous ordinary-rho-mixing density with every rho-star coefficient equal to one.

Task: “Open problem D0037.” Received 13 November 2026, approximately 05:31 Asia/Tbilisi.
