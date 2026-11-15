# T091 work log

Task: “Open problem T091: Uniqueness and regularity for the three-dimensional stochastic Navier–Stokes equations”; received in this session, first local clock reading 2026-11-14 20:55:11 +04 (Asia/Tbilisi).

## 2026-11-14 20:55–20:58 +04 — orientation and literature search

- Workspace initially contained PROMPT.md and runner files only; no prior mathematical deliverable.
- Read the startup memory and brain navigation index directly, and searched existing memory filenames/content for Navier–Stokes. The task-specific prohibition on writing outside this folder takes precedence over the global mesh/checklist/recall commands, which mutate external state. No mesh, checklist, brain write, git, or outside-folder write was performed.
- Read `~/.claude/compute/compute_state.json`: status `ok`, mode `owner_away_open`. No heavy computation is planned. Any Python check will use `OMP_NUM_THREADS=1`, `nice -n 15`, one process, and a memory/time cap.
- Used the web search tool with queries `3D stochastic Navier Stokes uniqueness law Leray Hopf additive noise 2025 2026 regularity`, `stochastic Navier Stokes global regularity smooth additive noise 2026 torus`, `stochastic Navier Stokes constant additive noise Galilean transformation uniqueness deterministic`, and `site:arxiv.org stochastic Navier Stokes additive noise Leray Hopf uniqueness 2026 2025`.
- Opened arXiv pages 2611.02557, 2606.28575, 2309.09753, and 1912.11841. Detailed scope checks follow below. Search snippets alone are not accepted as references.

## Choice, recorded before proof work

Prove an exact reduction for **spatially constant additive Gaussian noise**, allowing a nonzero covariance of any rank. A time-integrated Brownian spatial mean is a finite-variation translation. Subtracting that mean and translating should turn every stochastic Leray–Hopf solution into a deterministic Leray–Hopf trajectory, with the energy inequality preserved exactly. Conversely every deterministic trajectory should lift to a stochastic solution.

Target conclusions: (i) uniqueness of the velocity law for this stochastic equation is equivalent to uniqueness of deterministic Leray–Hopf trajectories for the centered initial datum; (ii) almost-sure global spatially strong solvability for smooth initial data is equivalent to deterministic global strong solvability. The law statement must cover all martingale solutions, including those with extra randomness, and recover the centered trajectory from the velocity alone. These are the points at which a merely formal change of variables would be insufficient.

Why this piece: it is a complete, checkable obstruction to regularization by one nonzero class of smooth additive noises. It makes the deterministic difficulty exact. This is an elementary reduction, with no claim of novelty, and does not settle nonconstant or nondegenerate mean-zero noise. The usual mean-zero phase space excludes constant noise; that limitation will be explicit.

## Literature outcome (search ended within the ten-minute allowance)

Opened and read the arXiv abstract pages, with authors checked against the pages:

- Felix Brandt and Igor Kukavica, *Regularizing the Navier-Stokes Equations by One Noise Component*, [arXiv:2611.02557](https://arxiv.org/abs/2611.02557), submitted 2 November 2026. Also opened the HTML paper. One-component **multiplicative** Itô noise gives global existence with probability tending to one at large intensity, under conditions depending on whether the coefficient is linear or nonlinear. This is a relevant recent advance, but it is neither the stated additive-noise result nor an almost-sure assertion at a fixed noise intensity.
- Antonio Agresti, Federico Butori, and Eliseo Luongo, *Global smooth solutions by high mode Lie-Transport noise for Logarithmically Hyperdissipative Navier-Stokes equations*, [arXiv:2606.28575](https://arxiv.org/abs/2606.28575). The model has logarithmic hyperviscosity and Lie-transport noise; its high-probability conclusion does not settle either part here.
- Theresa Lange, Marco Rehmeier, and Andre Schenke, *Non-uniqueness of Leray--Hopf solutions for the 3D fractional Navier--Stokes equations perturbed by transport noise*, [arXiv:2412.16532](https://arxiv.org/abs/2412.16532). Also opened the HTML paper. Fractional dissipation and transport noise, with pathwise energy inequality asserted on a random initial interval, do not give the standard additive-noise torus counterexample.
- Elia Brué, Rui Jin, Yachun Li, and Deng Zhang, *Non-uniqueness in law of Leray solutions to 3D forced stochastic Navier-Stokes equations*, [arXiv:2309.09753](https://arxiv.org/abs/2309.09753). Opened abstract confirms the extra constructed force and Euclidean domain.
- Martina Hofmanová, Rongchan Zhu, and Xiangchan Zhu, *Non-uniqueness in law of stochastic 3D Navier--Stokes equations*, [arXiv:1912.11841](https://arxiv.org/abs/1912.11841). Opened abstract explicitly states the constructed solutions violate the corresponding energy inequality.
- Y.-X. Lin and Y.-G. Wang, *Global pathwise solutions of an abstract stochastic equation*, [arXiv:2407.00722](https://arxiv.org/abs/2407.00722). Opened abstract discusses multiplicative noise and small-data results; it must not be read as an arbitrary-data additive-noise theorem.

Additional exact-term searches for `site:arxiv.org "Navier" "additive" "2026" "uniqueness in law"` and `site:arxiv.org "Navier" "additive" "2026" "global regularity"` returned no results. No verified settlement of the whole stated problem was found. This is a bounded literature check, not an exhaustive absence theorem. No SOLVED_ELSEWHERE.md is warranted. Continue with the recorded reduction.

## Proof written

Created PROOF.md with the full reduction, including a spatial-mollification justification at weak regularity, an exact energy-defect identity, a measurable recovery map from the velocity path alone, and the strong-lifetime consequence. No probabilistic independence of the recovered deterministic-PDE trajectory is assumed. The distinction between a random trajectory solving a deterministic PDE and a nonrandom trajectory is explicit.

The proof fixes normalized torus volume, arbitrary initial mean, any finite-dimensional constant covariance, and the pathwise Leray–Hopf energy inequality. The limitation for formulations imposing only expected energy inequalities is stated. Next: independently check translation signs in Fourier variables and the Itô trace coefficient, then audit the law and mean-zero caveats.

## Independent finite checks prepared

Created audit_reduction.py (standard library only). It uses exact rational complex Fourier arithmetic to expand the full projected nonlinearity, rather than copying the coordinate-change calculation. It checks cancellation of the mean advection, covariance of nonlinear convolution under translation, Parseval energy splitting, and a deliberately wrong translation sign. A separate enumeration of symmetric finite increments computes the quadratic mean-energy expectation, independently checking the factor one half in the Itô trace term, including degenerate and redundant covariance representations. These increments are a moment identity, not a Brownian-path or PDE simulation.

The script sets a 30-second alarm, a 512 MiB data-segment cap, and a 768 MiB RSS limit, checks OMP_NUM_THREADS=1, and records its measured peak RSS. It writes only audit_results.json in this folder.

## First audit invocation failed before computation

Exact command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_reduction.py
```

Output:

```text
nice: setpriority: Operation not permitted
Traceback (most recent call last):
  File ".../T091/audit_reduction.py", line 19, in <module>
    resource.setrlimit(resource.RLIMIT_DATA, (512 * 1024**2, 512 * 1024**2))
ValueError: current limit exceeds maximum limit
```

No algebra trials ran and no result data were written. The managed sandbox rejected the priority adjustment and the requested resource hard-limit setting. Before another attempt, inspect the inherited priority and existing resource limits. Do not silently run the computation at normal priority.

The second invocation used the same command after preserving resource hard limits and adding an inherited-priority guard. It again failed at the data-segment cap before algebra trials:

```text
nice: setpriority: Operation not permitted
ValueError: current limit exceeds maximum limit
```

The new guard did **not** reject the inherited priority, so the process was already running at nice >= 15. Revised the script to print that priority explicitly, retain the guard, and record unsupported Darwin memory-limit calls instead of failing on them. The fixed finite test has at most 9 input Fourier modes and 81 pairs per convolution; measured peak RSS must be below 1 GiB. The 30-second alarm remains active. No priority restriction is being bypassed: computation proceeds only if its actual inherited nice value meets the user's bound.

## Exact audit passed

Exact command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_reduction.py
```

Output:

```text
nice: setpriority: Operation not permitted
Inherited nice: 20
PASS: 6 exact Fourier drift, translation, and energy-splitting trials
PASS: 5 exact quadratic-increment averages (covariance ranks 0 through 3)
PASS: wrong translation sign and wrong nonzero Ito trace coefficient rejected
Data: audit_results.json
Peak RSS: 16154624 bytes
```

Exit status 0; wall time reported by the command tool was under one second. The failed attempt to adjust priority did not raise the inherited nice value: actual nice 20 satisfies the requirement nice >= 15, and the script checks that before any trials. Both memory-limit calls were unavailable on this managed Darwin process; measured peak RSS was 16,154,624 bytes, well below 1 GB. No subprocesses, worker pool, external libraries, or GPU were used. All output data are in audit_results.json.

## Analytic self-audit finished

Created AUDIT.md. Re-derived the translation sign from an explicit Fourier Stokes mode, the Itô trace coefficient both by the quadratic generator and by increment moments, and energy splitting both in physical space and by Parseval. Hand-checked the five trace/mean-increment values, the redundant covariance rank (determinant 4), and the 41-mode count by the unique integer relation among the four base frequencies.

Checked the vulnerable cases: weak path regularity, random choice of deterministic-PDE trajectories, velocity law versus joint law, nonzero initial mean, degenerate covariance, exceptional energy starting times, the forbidden inference from a zero-probability zero-noise path, and the mean-zero phase-space exclusion. No gap was found in the theorem as explicitly scoped. Neither nonconstant mean-zero additive noise nor an energy class defined only by expected inequalities is covered.

## Final deliverables

Wrote REPORT.md with verdict `PROVED an exact deterministic reduction for spatially constant additive noise`. Deliverables: PROOF.md, AUDIT.md, audit_reduction.py, audit_results.json, REPORT.md, and this log. Main T091 remains unresolved. The report states the mean-zero and pathwise-energy limitations, the bounded literature-search outcome, the two resource-setup failures, the successful exact checks, and the proposed next piece. No git commands or external writes were used.
