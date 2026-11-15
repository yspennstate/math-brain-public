# T306 work log

Task received: 2026-11-14, approximately 22:11 local system time (18:11 Asia/Tbilisi if the system clock is UTC; exact timezone checked below). User: “push this problem forward by one checkable piece.”

## Initial orientation and literature check

- Read the memory index and compute governor state. The governor reported `warn`, `owner_away_open`, CPU saturated. No heavy computation is planned.
- Attempted `OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall "diffusion sampler iteration complexity probability flow Gaussian"`. It loaded ONNX and exceeded the requested memory ceiling (governor reported RSS 1269 MB). Sent TERM to that process, PID 44391, immediately upon seeing this. This was an execution mistake; no further semantic recall or ML libraries will be used.
- `nice -n 15` prints `setpriority: Operation not permitted` in this sandbox. Every subsequent program will still be launched through the requested command; actual inherited priority will be checked. Only small standard-library computations will be used.
- The task-specific instruction forbids writes outside this folder. Therefore no external mesh, checklist, or brain mutation is performed. No git or subagents are used.
- Web search started around 22:12 system time. Opened the arXiv pages for Yiwen Kou and Yimeng Wang, *Lower Bounds for Parallel Diffusion Sampling*, arXiv:2610.09166v2 (2 Nov 2026), and Zhiyang Xun and Eric Price, *Query Lower Bounds for Diffusion Sampling*, arXiv:2604.10857v2 (29 Sep 2026). Their abstracts respectively give near-isotropic d^(1/3) round bounds and general sqrt(d) query bounds, without a matching linear lower bound for the class in the question.
- Opened Xixian Wang and Zhongjian Wang, *A priori regularity of the reverse heat flow and dimension-dependent complexity of higher-order diffusion samplers*, arXiv:2609.24622. Its abstract imposes compact support and a dimension-uniform supporting-cap doubling assumption, with exact scores. This does not settle the stated L2 approximate-score model.
- Search also located Gen Li, Yuting Wei, Yuejie Chi and Yuxin Chen, *A Sharp Convergence Theory for The Probability Flow ODEs of Diffusion Models*, arXiv:2408.02320. The theorem assumptions, especially derivative error, are being checked.

URLs opened: https://arxiv.org/abs/2610.09166 ; https://arxiv.org/abs/2604.10857 ; https://arxiv.org/abs/2609.24622 ; https://arxiv.org/abs/2408.02320 . An attempted HTML URL for 2408.02320v2 returned 404.

## Literature decision and chosen piece (before proof work)

System command `OMP_NUM_THREADS=1 nice -n 15 date '+%Y-%m-%d %H:%M:%S %Z'` returned `2026-11-14 22:13:29 +04`: local time is Asia/Tbilisi, not UTC. The initial receipt time above is therefore about 22:11 Asia/Tbilisi.

The literature search took less than ten minutes. No resolution of the full bounded-condition-number minimax question was found. This is a limited search, not a completeness claim. The recent Kou–Wang paper explicitly says a polynomial gap remains. No SOLVED_ELSEWHERE.md is warranted.

Important qualification from the opened full text of Li–Wei–Chi–Chen (https://arxiv.org/html/2408.02320v1): Theorem 1 assumes both mean-square score error and mean Jacobian error; it also has a step-count threshold. Section 3.2 already gives a discontinuous quantization example showing L2 error alone is insufficient for its discrete deterministic sampler. The general obstruction is therefore **known**; no novelty is claimed for it.

Chosen piece: prove and quantify a smooth continuous-time version of this obstruction. Use the stationary one-dimensional Gaussian OU target and score estimates `s_k(x)=-x+(c/k) sin(kx)`, with `0<c<1`. These are scores of uniformly strongly log-concave smooth densities and have uniform error at most `c/k`, with uniformly bounded Lipschitz constants. Nevertheless, the exactly integrated, unmodified reverse probability-flow ODE over unit time has a nonzero limiting TV error. Seek its exact limit and an explicit finite-frequency error bound. This isolates an obstruction in the pure-ODE clause of T306 even before discretization, and makes precise why a step-count answer under only L2 accuracy needs an extra qualification. It does not give a lower bound for arbitrary oracle algorithms or resolve dependence on dimension.

Additional opened sources: Daniel Zhengyu Huang, Jiaoyang Huang and Zhengjiang Lin, *Convergence Analysis of Probability Flow ODE for Score-based Generative Models*, arXiv:2404.09730v3, https://arxiv.org/html/2404.09730v3 ; Rama CONT, *Probability flow ODEs in score-based and reflected diffusion models*, arXiv:2610.03846v1, https://arxiv.org/html/2610.03846v1 . Their relevant regularity assumptions are checked to avoid misreading abstract-level L2 claims.

Attempt to inspect inherited priority with `OMP_NUM_THREADS=1 nice -n 15 ps -o pid,ni,rss,command -p $$ -p 44391` was blocked (`ps: Operation not permitted`). Small verification code will query its own priority using the standard library.

## Analytic result written

Wrote PROOF.md. The exact proposed limit is `D(c)=4/pi*atan(exp(c/2))-1`, also `2/pi*asin(tanh(c/2))`. A cellwise averaging argument gives the finite-frequency bound `|TV(P_k,gamma)-D(c)|<=sqrt(2*pi)/k`. The argument uses no limiting interchange and works on all of R. The target is stationary Gaussian, so positive smoothing time and initialization incur no error.

Checked the potentially conflicting positive result: Huang–Huang–Lin Assumption 3.3 controls the first **and second** derivatives of the estimated score; its Theorem 3.5 depends on that constant. In the construction the second derivative has norm `ck`, so there is no contradiction. Li–Wei–Chi–Chen assume a small Jacobian error; here that error does not vanish. The opened full texts support these qualifications.

Wrote verify_obstruction.py using only the Python standard library. It caps address space at 512 MiB and CPU time at 60 seconds. Planned independent checks: RK4 plus variational equation versus exact flow, source and target density quadratures versus the closed-form phase TV, a cosine-moment check, and direct real-line Gaussian TV quadrature at two resolutions. Data go into phase_checks.csv, gaussian_checks.csv, and verification_metadata.json.

First verification command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_obstruction.py > verification_output.txt 2>&1`. It exited immediately before any checks: macOS rejected `resource.setrlimit(RLIMIT_AS, (512 MiB, 512 MiB))` with `ValueError: current limit exceeds maximum limit`. The failed launch output is recorded here; the output file will be replaced by a successful rerun. Checking available resource limits before adjusting this nonportable guard.

Resource diagnostic: `OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os, resource; print("AS", resource.getrlimit(resource.RLIMIT_AS)); print("CPU", resource.getrlimit(resource.RLIMIT_CPU)); print("RSS", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss); print("nice", os.getpriority(os.PRIO_PROCESS,0))'` printed AS and CPU limits `(9223372036854775807, 9223372036854775807)`, RSS `11501568` bytes and **nice priority 20**. Thus the inherited priority is already lower than the requested priority 15; the warning comes from trying to increase an already-low priority. The verification script now records unavailable resource guards instead of failing, streams every grid with constant memory, and asserts measured peak RSS below 512 MiB. CPU-limit installation is attempted and recorded separately.

Second run of the same verification command completed the phase checks but failed the Gaussian two-grid agreement threshold of `5e-5`. Added the frequency and both quadrature values to the assertion diagnostic before deciding how much grid refinement is needed. This is an issue in numerical resolution, to be checked rather than assumed away.

Diagnostic third run located the grid disagreement at `k=64`: coarse TV `0.15759612574267487`, fine TV `0.15753714584092945`, difference `5.897990174541512e-05`. Increased both per-period resolutions fourfold (64/128 to 256/512) and tightened the agreement check to `5e-6`. The finite-frequency analytic bound has not changed.

Fourth run, same command, succeeded. Output: `D(1/2)=0.157522522023786`; at `k=1000`, RMS score error `0.000353553390593274`, numerical TV `0.157523213204538`, and analytic TV lower bound `0.155015893749155`. Maximum independent RK4 phase and Jacobian errors were `1.17e-11` and `4.46e-11`. Runtime was `2.0316` seconds, peak RSS `15122432` bytes, inherited nice priority `20`, CPU limit `60` seconds. AS limit was unavailable. The numeric integral's omitted tails are bounded by `9.60e-18`; discretization error is checked by grid refinement but is not certified. CSV and JSON data were written.

Added a corollary in PROOF.md for **every positive Euler step count N**, not just the continuous limit. Each phase Euler map has Jacobian at most `exp(c)` over the unit interval; a cosine test and Taylor's inequality give the uniform phase lower bound `B(c)=c(1-c/2)exp(-c)/4`. The same Gaussian-cell comparison loses only `sqrt(2*pi)/k`. Added independent numerical checks of its Jacobian and cosine inequalities and the exact one-step identity `phase_TV=c/pi`; these write euler_checks.csv. An initial patch insertion with an unmatched context failed without changing a file; the corollary was then inserted at the existing relation-to-literature heading.

Fifth verification run succeeded, including the Euler checks. The all-N analytic bound at `c=1/2,k=1000` is `0.054355621073428` (corrected from a transcription error when matching the output). The numerical phase TV values stayed above this lower bound for N=1,2,4,16,64,256 at all three c values. Runtime was `2.5496` seconds with `15859712` bytes peak RSS. Wrote AUDIT.md with separate forward-Jacobian and inverse-density derivations, a second independent all-N Euler lower bound using the Lipschitz inequality for sine, a factor-of-two audit of the Gaussian comparison, and explicit scope exclusions. Added numerical score RMS integration to complete the independent check of (3).

## Final verification and handoff

Final full command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_obstruction.py > verification_output.txt 2>&1`.

Exact substantive output (the output file also retains the sandbox's nice warnings):

```text
All deterministic checks passed.
D(1/2) = 0.157522522023786
k=1000: RMS score error = 0.000353553390593274
k=1000: numerical TV = 0.157523213204538
k=1000: analytic TV lower bound = 0.155015893749155
maximum RK4 phase error = 1.17e-11
maximum RK4 Jacobian error = 4.46e-11
Euler uniform bound at c=1/2, k=1000 = 0.054355621073428
Euler checks passed for c=0.1,0.5,0.9 and N=1,2,4,16,64,256.
Independent Gaussian score-error quadrature passed for k=1,4,1000.
```

Metadata: elapsed `2.6219232080038637` seconds, peak RSS `15990784` bytes, actual nice priority `20`, `OMP_NUM_THREADS=1`, CPU-time limit `60` seconds. Address-space hard-limit installation is unsupported in this environment; grids are streamed and peak RSS checked. No GPU, torch, MLX, parallelism, external publication, or git was used for the result.

Direct score RMS quadrature minus the analytic value was zero at k=1, `1.3877787807814457e-17` at k=4, and `5.421010862427522e-20` at k=1000. The final Gaussian-grid disagreement at k=1000 was `3.02278820316082e-06`; the analytic lower bounds do not depend on this quadrature.

Wrote REPORT.md with verdict PROVED for this narrow piece, prior-art qualification, failures, reproducible command, limits and a next step. Final artifact check read the report's first line, checked 11 requested result files are nonempty, read all four CSVs and the metadata JSON. Expected data counts: 3 phase rows, 9 Gaussian rows, 18 Euler rows, 3 score rows. The dimensional minimax problem is left unresolved; no SOLVED_ELSEWHERE.md was created.

Task completed locally: “push this problem forward by one checkable piece” — received approximately 2026-11-14 22:11 +04 (Asia/Tbilisi).
