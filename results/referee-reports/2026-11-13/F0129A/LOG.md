# F0129 work log

Task: “Open problem F0129”, received 2026-11-13, approximately 11:11 +04 (Asia/Tbilisi; first local clock reading 11:11:25).

## 2026-11-13 11:12 +04 — scope and orientation

Read the startup memory and searched existing memory text for the problem. No relevant prior result found. Read compute state: status ok, owner away; existing machine load is high, so use one lightweight worker, nice 10, single-threaded numerical libraries. No subagents.

The task-specific instruction “Work only in this directory” takes precedence over global requests to update shared brain/mesh/checklist state. All task writes and task records stay here; no shared-state commands, publication, or git operations. Source PDFs will be downloaded into RAM and converted to text over pipes, never saved to disk. Sources will retain page delimiters and retrieval metadata.

Literature review starts with Pemantle, then the requested original papers and later work. Do not interpret a stationary-initial-environment theorem as a flat-initial-profile theorem.

## 2026-11-13 11:18 +04 — first source audit

Saved complete text for Pemantle (79 pages), Durrett–Rogers (13), Mountford–Tarrès (18), Tarrès–Tóth–Valkó (19-page IMS reprint), Horváth–Tóth–Vető (both requested papers), Benaïm–Ciotir–Gauthier, Gauthier (2017), Kleptsyn–Kurtzmann, and Giles–Gräfner (2025). All PDF bytes stayed in RAM; text form feeds identify PDF pages. Project Euclid returned an HTML interstitial for Cranston–Mountford; trying alternate official routes.

Pemantle p.57 contains the exact zero-speed conjecture. It contains no t^(2/3) conjecture; Section 6.3, pp.64–65, discusses the Tóth–Werner process. Durrett–Rogers, Theorem 2, p.338, proves positive liminf speed for nonnegative f with f(0)>0, not a strong law. Their Conjecture 1, also p.338, is the strong law. The survey's historical account is inaccurate on this point. Its Theorem 6.2 also has a sign typo (ax instead of -ax); use the displayed SDE and original sources.

Mountford–Tarrès, Theorem 1, p.34, proves a superballistic limit only for f(x)=x/(1+|x|^(1+beta)), 0<beta<1. Tarrès–Tóth–Valkó, Corollary 1, reprint p.5, proves zero speed for almost every Gaussian initial profile, with f=-b' and b smooth, integrable and positive definite. Neither statement covers the initial profile identically zero. Giles–Gräfner (2025), p.3, explicitly excludes the case omega identically zero.

Resource detail: inherited shell niceness is 10. An initial os.nice(10) failed because it attempted an additional priority change in this sandbox; replaced it with getpriority and a change only if below 10. All successful fetches run at inherited nice 10.

## 2026-11-13 11:22 +04 — scope of proof attempts

Completed the main literature pass before numerical work. Additional 2025/2026 searches found Kosygina–Peterson and Kosygina–Marêché–Mountford–Peterson on discrete true self-avoiding walks; these are not finite-range Brownian-polymer theorems. Cranston–Le Jan is available as archive OCR and is being saved as text. Cranston–Mountford remains blocked by publisher/JSTOR interstitials; do not invent its theorem number or adopt the survey's near-zero-only hypothesis without checking the original.

Analytic directions: reflection symmetry alone allows random ballistic signs; the Gaussian stationary method requires positive definiteness of the primitive and does not reach a deterministic flat initial field; a direct occupation-potential energy identity may give a quantitative flat-profile bound but does not yet give sublinearity. An explicit annular repulsive kernel has a primitive with a negative 3-by-3 covariance quadratic form, so positivity of the force does not imply the spectral assumption.

## 2026-11-13 11:28 +04 — partial proofs and first numerical checks

Saved full proofs in REPORT.md: reflection symmetry, an occupation-potential energy inequality and explicit speed bound for nonnegative positive-definite primitives from flat initial drift (including truncated sign), an explicit non-positive-definite annular primitive, and a finite-history Gaussian shift extension of the stationary zero-speed result. These do not prove subballisticity. Status PARTIAL refers to the weaker bounds and structural results, with no novelty claim.

Built single-thread C++ Euler/grid simulator. Its cached force matched direct summation over all past interpolated deposits within 5.4e-15; reflected increments gave reflected paths within 1.8e-15; occupation mass error was below 3.6e-15 in the short deterministic audit. Main run: 48 independent seeds per kernel, five repulsive kernels plus Brownian control, T=8192, dt=0.02, dx=0.05. Cached/grid force agreement at checkpoints is below 4.3e-14, but annular drifts produce steps exceeding the interaction range. Such paths cannot support an exponent claim without refinement. Saved coarse results and started paired time/space refinements.

The /usr/bin/time -l wrapper completed the coarse refinement but returned status 1 because sandbox access to sysctl kern.clockrate was denied. Repeated the small run directly to obtain an unambiguous process status. No simulation failure occurred. Matplotlib needed its font/cache directories redirected under data/; plotting uses a noninteractive backend.

## 2026-11-13 11:35–11:51 +04 — refinements and completed audit

Completed paired T=1024 refinements and a 64-path finer run to T=8192 (dt=0.005, dx=0.025). The smooth-bump long run also became stiff and is excluded along with the long annular run from the report's exponent table. No endpoint-based path exclusions. A shorter annular run at T=256, dt=0.00005, dx=0.0125 has maximum negative-slope product 0.0215 and drift step 0.00502; this is useful short-time evidence, not an asymptotic exponent. All stiff-run data are retained and flagged.

For truncated sign, spline and two bumps, the finer long-run RMS exponents over 256–8192 are respectively 0.6382, 0.7316 and 0.6759. RMS displacement divided by time at T=8192 is respectively 0.07306, 0.07719 and 0.08611. Whole-path bootstrap intervals and a second fit window are saved. The Brownian controls demonstrate sizeable finite-sample slope fluctuations; no 2/3 law is claimed.

Expanded the source audit through January/October 2026 compact-manifold and discrete-walk papers. Total 19 complete primary-source texts, with the Cranston–Mountford access limitation explicitly recorded. Source hashes all match; sources/ contains only UTF-8 plain-text files; no PDF files or PDF magic headers anywhere in the workspace. Generated figures are original simulation plots, not source page images.

Final audit independently recomputed RMS values and regression slopes with Python's standard library rather than NumPy; all agree within 1e-12 for exponents and 1e-10 for RMS. Verified the exact annular covariance obstruction with rational arithmetic and checked kernel normalization separately by quadrature. Simulator self-test peak RSS was 16,302,080 bytes; the arrays have fixed size in the long runs, and the simulator uses one thread at nice 10. No subagents, publication, pushes, or writes outside this workspace.

Completed REPORT.md with first line PARTIAL. It includes complete weaker proofs and the precise remaining gaps. Neither the full zero-speed conjecture nor the sharper scaling conjecture was proved or found resolved in the inspected literature.

Task completed: “Open problem F0129” — received approximately 2026-11-13 11:11 +04, first recorded local clock 11:11:25. Main mathematical question remains open in this report.
