# T085 work log

Task: “Open problem T085: Random Cayley graphs of the symmetric group are expanders.” Session started 2026-11-14, approximately 20:53 Asia/Tbilisi (UTC+4), from the local runner timestamp.

## Scope and initial checks

All writes stay in this directory. No git, agents, external messages, or global memory/checklist/mesh mutations: the task's explicit directory restriction takes precedence over the earlier global instructions. Read the startup memory index and compute governor state directly. Governor reported `status: ok`, `mode: owner_away_open`; substantial shared load already exists, so use only small, single-thread computations.

Commands: `pwd`; `ls -la`; read startup memory and `~/.claude/compute/compute_state.json`; `date "+%Y-%m-%d %H:%M:%S %Z"`. Output: workspace is the T085 directory; initial files are PROMPT.md, codex.log, run.pid; clock 2026-11-14 20:54:30 +04.

The first read-only orientation shell did not use nice; all subsequent shells use `OMP_NUM_THREADS=1 nice -n 15`. macOS prints `nice: setpriority: Operation not permitted` when an inherited priority is already lower; verify the actual inherited nice value before computation.

## Literature search, started 20:54

Web queries: “random two permutations symmetric group Cayley expander spectral gap 2025 2026”; “random Cayley graphs symmetric groups spectral gap Helfgott Seress Zuk solved”. Found a 2025/2026 strong-convergence survey explicitly describing the full Cayley problem as open and mentioning growing-tuple Schreier graphs. Opening primary sources to check the exact stronger theorem before choosing the piece.

Opened Harald A. Helfgott, Ákos Seress, Andrzej Zuk, arXiv:1311.6742; Ramon van Handel, arXiv:2507.00346v2 (11 February 2026), especially Theorems 5.7–5.8 and section 6.2; and Ramon van Handel, *Strong Convergence: A Short Survey*, DOI 10.1137/25M1807113. The latter states Cassidy's strong convergence for irreducible representations of dimension between 1 and exp(N^(1/21)), excluding dimension 1, and explicitly still calls the full Cayley gap open. Following the primary Cassidy citation, arXiv:2412.13941. No whole-problem solution found.

Resource verification command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -c 'import os, resource; print("nice", os.getpriority(os.PRIO_PROCESS, 0)); import numpy; print("numpy", numpy.__version__); import sympy; print("sympy", sympy.__version__); print("rss_bytes",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)'`. Output: inherited nice 20; NumPy 2.2.3; SymPy 1.13.1; RSS 61,734,912 bytes. The warning from nice does not raise priority. `ps` is sandbox-blocked; Python getpriority supplies the check.

## Chosen piece (before implementation)

Exhaustively compute the one-sided normalized spectral gaps for every ordered pair of permutations in S_n, 2 <= n <= 5, on the group the pair actually generates. Use simultaneous conjugacy to reduce the first generator to one representative per cycle type, retaining exact class-size weights so the data recover the uniform-pair distribution. Compare the full gap with the natural-action gap for pairs generating A_n or S_n; seek and exactly certify a witness showing whether the natural action misses the bottleneck. This gives a finite benchmark and checks a tempting route from Schreier expansion to Cayley expansion. It does not claim a new asymptotic theorem.

Convention: the four generators are a multiset, P=(R_sigma+R_sigma^-1+R_tau+R_tau^-1)/4, with loops and repeated edges retained. Compute the upper gap 1-lambda_2, not the absolute spectral gap; all-odd pairs have a forced eigenvalue -1. Treat the trivial group separately. Numerical exhaustive data will be labelled numerical; any exact witness will get a separate proof and independently checked characteristic polynomials.

Literature search ended at approximately 20:57, within the ten-minute limit. Cassidy v3, Ewan Cassidy, arXiv:2412.13941, Theorem 1.3: k_n <= n^alpha for any fixed alpha<1/20; near-optimal bound 2 sqrt(2r-1)+o(1). This is a substantial partial advance beyond the baseline. Details and opened sources are in SOLVED_ELSEWHERE.md; full problem still open.

Implemented `enumerate_pairs.py`. First run command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 enumerate_pairs.py > enumeration_output.txt`. Script additionally forces six numerical-library thread variables to 1, checks connectedness, symmetry, row sums, spectral traces, pair weights, and the all-odd eigenvalue -1. Output files: pairs.csv, summary.json, enumeration_output.txt. Starting the run now.

First run stopped immediately at the auxiliary `low_gap >= gap` assertion: at n=2, the sign twist of the standard representation is trivial, so it must be excluded from the nontrivial comparison. Corrected by including that twist only for n>=3. This is a small-degree exception, not a failure of the full-gap computation. Rerunning the same command.

Successful run: 0.5516955 seconds, peak RSS 35,487,744 bytes, actual nice 20. Complete stdout is saved in enumeration_output.txt. Weighted pair totals for n=2,3,4,5 are 4,36,576,14400, from 4,18,120,840 representative pairs. For S_5: 6840 generating pairs; minimum numerical gap 0.05616790728788024; natural-action gap strictly overestimates the full gap in 6720 pairs; standard, sign-twisted standard and sign together still miss it in 3840 pairs. For A_5: 2280 generating pairs; minimum numerical gap 0.05638318048828539; natural action misses in all 2280. These are preliminary until independently audited.

Next: direct enumeration of all ordered pairs with a different subgroup construction and a shifted Laplacian, comparing the complete weighted gap histogram and counts; then exact integer characteristic-polynomial and rational positive-definiteness certificates for a witness.

Independent audit command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 audit_pairs.py > audit_output.txt`. It enumerates all 15,016 ordered pairs directly, with a multiplication table and left-generator closure; computes the least eigenvalue of I-P+2J/|H| instead of subtracting the second adjacency eigenvalue; compares the entire gap histogram rounded to eight decimals, every group-order count, and every miss count. Run completed successfully (details in audit_output.txt and audit.json).

Exact witness chosen: sigma=(4 5), tau=(1 2 3 4 5), generating S_5; numerical gap 0.09380648259317326 versus 0.3454915028125265 from standard, sign-twisted standard and sign. First `exact_witness.py` run computed matching full characteristic polynomials by integer-matrix charpoly and independently by exact word-return counts plus Newton identities, then failed the hypothesis that the top factor occurs in the ordinary two-subset action. This hypothesis was not part of the claimed result. Added the sign-twisted two-subset action to locate the actual factor; rerunning.

Audit output: all pair counts and complete eight-decimal gap histograms agree for all four degrees. Direct minima: S_5 0.05616790728788046; A_5 0.05638318048828524. Miss counts agree exactly: S_4 natural 216; S_5 natural 6720, low 3840; A_5 natural and low 2280. Audit: 6.0137865 seconds, peak RSS 33,423,360 bytes, nice 20.

Second exact run ruled out the sign-twisted two-subset action too. Its top factor is cubic; the full regular bottleneck is the quartic `x^4-3*x^3-9*x^2+20*x+16`, appearing with multiplicity six. Added the exterior square of the standard representation, computed both by oriented pairs in dimension ten and by 2x2 minors in the basis e_i-e_5 in dimension six. These distinguish the ordinary two-subset action from the exterior-square action. No claim about where the top factor occurs is retained without an exact check.

Exact S_5 witness now passes: command `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 exact_witness.py > exact_output.txt`. Complete certificate in exact_witness.json: upper gap between 3911711/41699794 and 9094767/96952436, i.e. 0.0938064825931754 to 0.0938064825931759. The top quartic lies in the exterior square of standard. All 120 characteristic coefficients agree between matrix and word-return/Newton methods. Runtime 0.5006776 seconds, RSS 59,801,600 bytes, nice 20.

Convention audit: the S_5 witness uses an involution, so the multiset convention duplicates an edge. To give a certificate that also applies verbatim to the simple Cayley graph, selecting an additional witness from the same completed enumeration with four distinct generators: sigma=(3 4 5), tau=(1 5 4 2 3), generating A_5. Numerical gap 0.09549150281252494 versus natural gap 0.4409830056250532. Added exact_a5.py, reusing only exact-certificate helpers, with a fresh 60-dimensional characteristic polynomial and independent 60-step word-return calculation. Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 exact_a5.py > exact_a5_output.txt`.

Exact A_5 output: order 60, four distinct generators. Regular characteristic polynomial:
`(x-4)*(x-1)^4*(x+1)^4*x^6*(x^2-5*x+5)^3*(x^2-5)^4*(x^2+3*x+1)^8*(x^3-x^2-7*x+4)^5`.
Natural polynomial: `(x-4)*(x-1)*(x+1)*(x^2-5)`.
Two-subset polynomial: natural polynomial times `(x^2+3*x+1)*(x^3-x^2-7*x+4)`.
Exterior square of standard: `x^2*(x^2-5*x+5)*(x^2+3*x+1)`.
Every regular characteristic coefficient agrees with the independent word-return/Newton calculation. First eight traces: 0,240,120,1920,2520,18720,40320,210240. Added all 60 traces, returns and coefficients to exact_a5_newton.csv and reran the same exact_a5.py command successfully. First successful run took 0.1011907 seconds, peak RSS 57,917,440 bytes; latest metrics are in exact_a5.json.

Threshold audit command: a short `OMP_NUM_THREADS=1 nice -n 15 python3` CSV reader subtracted the full gap from natural_gap and low_gap for each n=5 row. Output: smallest positive difference for A_5 is 0.05901699437494745 and for S_5 is 0.059016994374947895; largest residual among numerical ties is 2.1094237467877974e-15. The classification threshold 1e-8 lies far between these scales.

Wrote PROOF.md with the exact A_5 finite certificate. Rechecked the generated-group order by a separate Sylow/index-two argument, rather than relying only on enumeration. Root ordering needs only f(3)=1, f'(3)=14 and f''(x)>0 for f=x^3-x^2-7*x+4 on x>=3. Thus the full top eigenvalue is (5+sqrt(5))/2, the normalized gap is (3-sqrt(5))/8, and every nontrivial unordered-subset eigenvalue is below 3/4. Complement equivariance covers subset sizes 3,4,5. All generators are even, so sign twists add nothing in this example.

Wrote REPORT.md with a COMPUTED verdict, numerical/exact distinctions, reproduction commands, failure record and next steps. No asymptotic result is claimed. All task outputs remain in this directory.

Final consistency command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_certificate.py > final_check.txt`. This standard-library-only verifier checks the totals and audit flags, all saved Newton identities, an independent integer-list expansion of the stated A_5 polynomial, and agreement of radical formulas with the enumeration row. Output:

```text
PASS: 15016 pairs; 982 weighted representatives; all audit comparisons match.
PASS: all 60 Newton identities and integer expansion of the reported factorization.
PASS: exact radical gaps agree with the independently enumerated A5 witness.
PASS: required reports and data are present; verdict is COMPUTED.
gap_A5 = 0.09549150281252627 natural_gap = 0.44098300562505255
latest_exact_run_seconds = 0.10577487497357652 rss_bytes = 57786368
```

Added the conjugacy-weight coverage argument to PROOF.md. Final audit passes. Task completed: “push this problem forward by one checkable piece” (T085), requested approximately 20:53 Asia/Tbilisi, 14 November 2026.
