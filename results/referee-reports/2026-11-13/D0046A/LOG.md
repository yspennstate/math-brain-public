# D0046 work log

Task received: 2026-11-13 10:46 +04 (Asia/Tbilisi), “Open problem D0046.”

## 2026-11-13 10:48 +04 — working

Literature first, then a fully proved partial result if no published operator-process theorem closes the question, then bounded numerical evidence. All deliverables stay in this directory; no publication or pushes. No subagents. Source PDFs will be converted through memory/stdin directly into plain text; no PDF or page image is stored.

Read the identity memory and relevant brain recall. Recall found no D0040/D0043 cards; their unavailable contents will not be invented or cited. The directory-only restriction takes precedence over global checklist/mesh/memory writes outside this directory, so this log is the local task record. Compute governor at start: status ok, owner_away_open; numerical jobs will use nice 10 and at most four BLAS threads, with substantially smaller than 4 GB working memory.

Initial search found an especially relevant 2024 paper by Edelman–Jeong–Nissim, arXiv:2411.01633: fixed-size tridiagonal corner limits and a conjectural dynamical SAO. It must be read in full before making any claim about resolution.

## 10:52 +04 — literature checkpoint

Virág source fetched and converted to sources/virag_1804.06953.txt, 28 pages. Exact Question 8 verified on PDF page 25. Fetched full texts of Holcomb–Paquette (1707.02700) and Edelman–Jeong–Nissim (2411.01633v3, 19 Feb 2026). The latter's Theorem 3.1 is a fixed-corner entry-process result; Problem 4 on p.18 leaves the operator question open; Remark 5.6 on pp.19–20 explains failure of their space-dependent OU-white-noise candidate perturbatively. A printed denominator in its final long-time asymptotic appears inconsistent with its own displayed integral; re-derive instead of copying.

A different proof target is emerging: independent OU/radial-OU tridiagonal dynamics has exactly stationary GUE eigenvalue marginals, but its edge eigenvalues freeze on the true DBM edge clock. A reversible Dirichlet-form increment bound reduces this to delocalization of the top tridiagonal eigenvector. An elementary Rayleigh/gradient estimate may suffice and avoids unproved dynamic operator convergence.

Resource note: explicit nice -n 10 reports setpriority denied by sandbox. The job launcher already started this agent at nice 10; do not infer a successful renice. Inspect inherited niceness in Python before numerical work. No outside workspace mutation will be attempted.

## 2026-11-13T10:59:43+04:00 — proof checkpoint

Literature pass completed before experiments. Saved REPORT.md with Theorem A: stationary independent OU/radial-OU GUE tridiagonal dynamics freezes uniformly in time on the DBM edge clock. Proof: explicit Gaussian concentration + min-max + discrete Sobolev delocalization, eigenvalue gradient energy, forward/backward reversible maximal inequality. Corollary covers bounded entry covariance. Status PARTIAL for D0046; obstruction only. Corrected the premise about canonical invariant tridiagonalization being non-Markov: the orbit quotient is Markov. Numerical stage begins next. Inherited niceness verified by os.getpriority: 10.

## 2026-11-13T11:05:14+04:00 — numerical audit

Exact-transition pilot passed. Full simulations running at nice 10 with one BLAS thread, two top eigenvalues, lags s=0, 0.25, 1, 3, n=64 through 2048. Literal Hermitian Brownian motion is simulated at u=exp(2*s*n^(-1/3)), then divided by sqrt(u); this is exactly stationary matrix OU and is compared with (2). Independent radial transitions use noncentral chi-square variables.

Math audit passed: GUE entry moments, conditional radial moments, eigenvalue gradient energy by finite differences in Gaussian coordinates, and min-max/Sobolev inequalities on sampled matrices. Initial Airy-asymptotic numerical tolerance at t=100 was too tight (23.889873 versus limit 24); extending to t=300 gives 23.987598 and confirms convergence. This was a finite-t audit threshold issue, recorded rather than hidden. Added a pointwise lower bound forcing entry covariance to diverge for exact Jacobi DBM realizations.

## 2026-11-13T11:13:43+04:00 — done

Task completed with status PARTIAL. REPORT.md states Question 8 exactly and gives a complete proof of a dynamical obstruction, not a purported solution of the general operator-limit question. It also proves a necessary covariance-growth bound for exact Jacobi DBM realizations. Literature review includes 28 retained primary-source plain texts, with theorem/page references, metadata hashes, and search log. No checked theorem met RESOLVED_IN_LITERATURE.

Numerical work completed: 3,416 independent Hermitian Brownian paths and 12,000 independent tridiagonal paths, n=64..2048, top two eigenvalues at four times. 123,328 raw sample rows, 72 summary rows; one requested BLAS/vecLib thread, inherited nice 10, 692.6 MB peak RSS, 305.6 seconds. The n=2048 dense sample has only 12 replicates and is marked as a pilot. Plot and reproducible code saved.

Final audit: independent math.fsum reconstruction agreed with NumPy correlations within 4.45e-16 and mean squared increments within 2.23e-16; source hashes and page counts checked; all source files are text, no PDF files or PDF-magic files; SVG parsed; code compiled. Full math audit passed. No publication, push, subagent, or external message. All task deliverables stayed in this directory.

Task: “Open problem D0046.” Received 2026-11-13 10:46 +04 (Asia/Tbilisi).
