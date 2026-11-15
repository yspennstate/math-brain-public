# Independent referee log: D0026

- Task received 2026-11-13, approximately 07:45 Asia/Tbilisi; first clock read 07:46:13.
- Scope: audit claim_files read-only, independently obtain source texts, audit Theorem A, run new simulations at q=0.55 and 0.7, deliver REPORT.md. No subagents, publication, git operations, PDFs or scans on disk. All writes stay in this directory.
- Read startup memory, recalled mathematical audit experience, and checked compute governor (warn/cpu_saturated, owner_away_open). Use a single simulation thread, nice at least 10, memory well below 4 GB. Shared mesh/checklist/brain mutations are outside the explicit directory-only scope; this log serves as the local task record.
- Read claim_files/REPORT.md lines 1–204 and LOG.md. The actual reduction does NOT claim the true time-s law has globally uniform distance moments: it fills the exterior of a growing interval with auxiliary zeros, then uses finite propagation. This distinction is central to the audit.
- Initial audit: the drift formula, B constant, and deterministic time cancellation appear correct. Next: independent primary-source downloads and checks, followed by a simulator written without reading claim_files/code.

## Primary-source check, approximately 07:48

- Downloaded all three requested arXiv PDFs into memory, piped bytes to pdftotext stdin, and retained only UTF-8 text with PDF page markers. SHA-256 digests, retrieval timestamps, and URLs are in sources/manifest.txt. No PDF file was created.
- BCMRT Theorem 2.1, p. 4, needs q>1/2, polynomial growth, centred local f, and sup_x E(theta_0^{d_x})<infinity. Remark 2.3 explicitly excludes deterministic single-seed configurations. Proposition 4.1 gives exactly the submitted lambda and B after algebraic simplification. Its proof and Theorem 2.1 proof, pp. 10–12, support uniformity for fixed theta and K.
- Mountford–Valle Theorem 1.1, p. 2, is single-seed convergence for q sufficiently close to 1. Remark 1.2, p. 3, extends to an exponential tail for distance from one fixed site to the nearest infection. Spin 1 is facilitating there; translated to this audit, infection is 0.
- Survey p. 2 and Section 4 read: all-q conjecture remains posed; the delta-West theorem requires small directional perturbation and well-distributed initial infections. Its generator is not FA-1f and cannot replace it.
- Independently wrote code/referee_sim.cpp without opening claim_files/code. It uses a binary tree of individual flip rates, healthy exterior boundaries, exact exponential waiting times, and one rate per facilitated site. No discretization or double-rate two-neighbour updates. Started q=0.55, 10,000 paths, t<=100, radius 1024; one thread at inherited nice 10.
- First source script attempted os.nice(0), which macOS sandbox rejected even though priority was already 10. Replaced it by a read-only priority assertion; no priority escalation attempted.

## Completed proof and computation checks, approximately 07:52

- No defect found in A1–A4. At positive distance, upward jumps have size at most one and rate at most p; downward jump rate is at least q. At distance zero, the generator upper bound is p(theta-1), exactly matching -lambda+q(theta-1)/theta. Frozen-zero finite approximations preserve the bound, and Fatou handles the unbounded distance function.
- Rechecked deterministic split 100 a delta - lambda(1-delta)=-lambda/2. On the growing interval the filled law has moments <= B+1 past the claimed threshold; outside, the moment is exactly 1. Fixed theta and K give fixed BCMRT constants despite the law depending on t. No stopping-time or future-conditioning issue.
- The true single-seed law at every fixed finite time still fails the GLOBAL gap-moment condition. On the event of no infection births at the two initial neighbours (probability exp(-2qu)), it is still the initial seed, giving E(theta^{d_x}) >= exp(-2qu) theta^{|x-z|}. The proof avoids this failure by modifying the exterior and coupling only during the shorter final interval.
- The clock-path series is valid without attractiveness. For m=ceil(100s), rho=2e/100, its sum is <= rho^m/(1-rho), hence <= (1-rho)^(-1) exp(-291.2023 s). A factor 2||f|| enters the expectation comparison and is absorbed into constants.
- Main independent simulations completed: 10,000 paths per q, 31,518,341 flips total, maximum visited distance 61 (q=.55) and 91 (q=.7), zero endpoint infections, peak RSS below 2.5 MiB, nice 10. At t=100: .5527 (SE .0049724) and .6954 (SE .0046026).
- Five-site verification at each q: 80,000 new paths, full terminal distribution compared with an enumerated 31-state generator evaluated by Poisson uniformization. Maximum histogram deviations 2.013 and 2.880 SE across 31 cells; origin time-series deviations at most 1.863 SE. Row-sum residual <=2.23e-16, detailed balance <=6.94e-18, stationary residual <=2.78e-17.
- Generator inequality exhaustively checked in every nonempty nine-site configuration at all nine observation sites: 4,599 checks per q, at q=.5001,.55,.7,.99. All residuals nonpositive. Split and published-lambda identities independently checked. An initially overstrict absolute-tolerance assertion for B near q=.5001 failed due to cancellation; relative tolerance resolved this numerical audit artifact, with the symbolic identity unchanged.
- Independently obtained the 2026 SIAM survey via its DOI landing-page full text after /full and /pdf URLs timed out. Conjecture 2.11 still poses the all-q problem, and reference 48 cites arXiv:2510.20461. Saved primary extracted text in sources/Martinelli_ICM_2026_web.txt.
- Additional primary texts obtained: Blondel–Deshayes–Toninelli 1803.08761, Shapira 2005.13327, Hartarsky–F. Toninelli 2212.08437, Hartarsky–C. Toninelli 2025 book, and Mareche thesis. Ertul publisher URL returned 400; obtained arXiv:2103.00019 instead. Blondel thesis URL returned 404; no claim about unread thesis content.

## Final audit, approximately 07:56–07:57

- Verdict written: ACCEPT as the claimed partial result. The exact auxiliary-law reduction is valid; no proof correction required. Restricted Conjecture 1 follows for q>1/2. The all-q conjecture is not resolved. Exact printed priority for the whole q>1/2 arbitrary-seed statement was not established; near-one coverage is already in Mountford–Valle, and the extension is a corollary of BCMRT estimates.
- After writing the independent simulator and completing its main and finite-state checks, read the supplied simulator. Its legal flip rates agree with the intended generator. Recomputed its summary's 24 terminal standardized residuals: maximum absolute z=2.093418017422043. Did not rerun its large experiments.
- Removed stray low control characters introduced by pdftotext math extraction, preserving tabs/newlines and all printable text; updated source-text hashes and the download script's normalizer. All sources are .txt files. PDF input hashes continue to identify the original in-memory downloads.
- code/check_artifacts.py passed: first report line exactly ACCEPT; all three required texts present; all source text hashes match; supplied claim_files snapshot unchanged; no PDF or raster image anywhere in this folder; all independent CSV means and SE recomputed successfully. The pre-existing claim SVG is a simulation chart, not a source-page scan.
- All numerical work ran serially at inherited nice 10, with numerical library thread caps set to one. No simulation workers remain. No shared brain/checklist writes, publication, messages to peers, git commits, or pushes.

Reproduction (run from this directory, at nice >=10):

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/fetch_sources.py
clang++ -O2 -std=c++17 code/referee_sim.cpp -o code/referee_sim
./code/referee_sim 0.55 10000 1024 260001 100 data/unused.csv > data/q055.csv 2> data/q055_run.txt
./code/referee_sim 0.7 10000 1024 260002 100 data/unused.csv > data/q070.csv 2> data/q070_run.txt
./code/referee_sim 0.55 80000 2 260003 5 data/check055_hist.csv > data/check055.csv 2> data/check055_run.txt
./code/referee_sim 0.7 80000 2 260004 5 data/check070_hist.csv > data/check070.csv 2> data/check070_run.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/validate_sim.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/audit_algebra.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/check_artifacts.py
```

- Task done: “You are an independent referee. … Break it if it is wrong.” — received approximately 07:45, 13 November 2026, Asia/Tbilisi.
