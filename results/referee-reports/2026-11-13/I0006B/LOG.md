# I0006B work log

Task received: 2026-11-13, approximately 15:18 Asia/Tbilisi (first shell timestamp 15:18:24).
Owner's task: “Open problem I0006B, a borderline case left open in print.”

## 15:18–15:22 — orientation and sources

- Working alone, only in this directory; no subagents, pushes, publication, or simulation. Computations will run at nice 10 with numerical thread limits of one.
- Read the startup memory, identity and creativity cards, mesh protocol, and compute state. Compute status was `ok`. The task-specific instruction “Work only in this directory” and filesystem restrictions take precedence over the global instruction to write shared mesh/checklist/brain state. No external coordination or memory files are being edited. This file serves as the local task checklist and durable record.
- Both full plain-text v1 papers and arXiv listing texts were already staged in `sources/` at start. Verified titles, authors, v1 date, model normalization, and the requested Section 6 against the arXiv HTML pages. No PDF or image was downloaded or kept.
- Read the requested passage line by line: companion pp.51–56, Theorem 6.1, Corollary 6.2, Proposition 6.3, Lemmas 6.4–6.5, Theorem 6.6, including (85)–(98). Also checked Theorem 1.3(iii)(b), p.6, the exclusion on p.10, and parking Theorem 3.4, p.14.
- The only analytic strict-exponent step is Lemma 6.4's Laplace-transform summation, p.54. At p=d/2, q=p/(p-1)=d/(d-2), the inner sum is logarithmic. Retaining it gives log MGF <= C lambda^q log(e+lambda), hence tail cost s^p/(log s)^(p-1).
- Initial candidate: E u_n(0) is of order (log n)^(2/d) (log log n)^(1-2/d). This is a candidate, not yet a conclusion.
- Lower-bound idea: a negative profile of depth a/(1+|x|^2) out to radius sqrt(a), with a logarithmic supersolution a log(1+|x|^2). Boundary height is a log a; profile cost is a^(d/2) log a. This matches the upper-bound cost if the comparison and FKG boundary cost work.
- Literature search: searched both titles/identifier, critical/borderline/gamma and log-log variants, and both authors' publication pages. Current arXiv records show only v1. No later resolution found so far; continue source and literature audit before final classification.

## Proof development and deterministic checks

- Downloaded both arXiv v1 HTML responses into memory, extracted ordinary text with MathML `alttext` formulas, and saved only `.txt` files. Original staged paginated texts were retained. Hashes and provenance are in `data/source_manifest.json`; retrieval code is in `code/fetch_sources.py`.
- The exact discrete identity gives `(P-I) log(1+|x|^2) <= 1/(1+|x|^2)`. No continuum approximation is needed for the lower bound. With depths `2a/(1+|x|^2)` and `a log(1+a)=2 E u_n(0)+1`, comparison forces the next unreflected update at zero below `-(2-log 2)a`.
- FKG handles the dependent boundary conditions. Markov gives each boundary condition probability at least 1/2. Even the crude boundary count O(a^(d/2)) is lower order than the profile cost O(a^(d/2) log a).
- Upper bound: the critical log MGF is `C lambda^(d/(d-2)) log(e+lambda)`. Choosing `lambda=b (s/log(e+s))^(d/2-1)` gives the matching cost. Theorem 6.6's smoothing term costs exp(-c s^(d/2)), hence does not remove the logarithmic gain. Checked the time window, final integration, bounded increment overshoot, and inverse scale.
- Secondary problem: a self-contained truncation argument for Doob martingale differences gives uniform `exp(-c s^gamma)` concentration for coordinate-Lipschitz functions whose coordinate constants have bounded squared sum, whenever 0<gamma<1 and the inputs have a uniform stretched-exponential moment. Applied with Green coefficients, this yields the upper bound without an exponential moment of |eta|. The one-hole event plus FKG/Markov yields the matching lower bound.
- Ran `code/check_variational.py`: 20 finite Holder optimizers (including low-dimensional algebraic analogues), 12 radial quadratic-plus-power optimizers with quadrature refinement, 4 discrete-barrier grids, and 9 subunit-exponent one-site checks. All passed. These are deterministic checks, with zero random samples. The kernel used for numerical radial problems is an explicitly identified proxy, not a claimed exact lattice Green function.
- Measured inherited niceness 10, one thread, peak RSS 15,450,112 bytes. A redundant `nice -n 10` call was refused by the sandbox, but `os.getpriority` confirmed inherited nice 10 from `launch.sh`. macOS also rejected setting RLIMIT_AS; actual measured use is far below 4 GB. No heavy computation was needed.


## Final proof audit

- Rechecked the exponent independently by equal-cost dyadic annuli: each annulus contributes deficit of order a and costs a^(d/2); there are order log a annuli. Thus m is order a log a and the cost is m^(d/2)/(log m)^(d/2-1). Inversion gives the log-log power 1-2/d.
- Checked the barrier comparison from time zero through time n, the origin gap (2-log 2)a, exterior boundary coverage, and positive association rather than a false independence assumption.
- Checked strict/nonstrict tail conventions (atoms require no regularity), finite dependency of the Doob martingales, and uniform coordinate constants g_(n+1)<=G.
- Checked the secondary concentration proof: square summability controls the discarded-jump union bound uniformly in the number of coordinates. The exponential transform is used only on truncated differences, giving exponent s^gamma.
- Re-read the critical Green and smoothing proofs against the independently downloaded HTML. Read recalled sandpile-barrier and critical-exponent audit memories as cautions; neither supplied a theorem or assumption used here.
- Repaired inline-math delimiters and checked source references. No PDF/image artifacts are present.
- Literature-search scope saved in data/literature_search.txt. No later resolution found. A possible critical-tail hit, arXiv:2610.10233, concerns combinatorial structures.
- Completed: REPORT.md is classified PROVED. Critical order is (log n)^(2/d)(log log n)^(1-2/d). Secondary order for 0<gamma<1 is (log n)^(1/gamma), proved without an absolute exponential moment.
