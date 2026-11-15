# E0065 research log

Task received: 2026-11-13, approximately 08:49 Asia/Tbilisi (session clock).
Request: “Open problem E0065 ... Find the exact value of lambda_m for every m >= 3.”

## Orientation (2026-11-13) — orientation and scope

Working only in this directory; no subagents, publication, pushes, or PDF/image files. Numerical jobs will use nice 10 and BLAS thread caps, no more than four threads and under 4 GB.
Read compute state: warn/cpu_saturated, owner_away_open; use one numerical worker.
Consulted shared brain recall and mesh protocol. Mesh hello failed with “attempt to write a readonly database”; global coordination/checklist/memory writes are outside this task's directory and filesystem permissions. Use this local log as the task record. A startup memory node was unavailable; brain recall located related QSO work, which is only a hint and not evidence for this problem.

Literature first. Located arXiv:0902.4207v2, two-author 2009 survey (14 pages), distinct from the expanded three-author 2011 journal survey. Will preserve both definitions and numbering.

## Literature search — source correction and access notes
The 2009 text has no proof of Theorem 7. Original citation: R. N. Ganikhodzhaev and A. T. Sarymsakov, A simple criterion for regularity of quadratic stochastic operators, Dokl. Akad. Nauk UzSSR (1988), no. 11, pp. 5–6 (Russian). The expanded 2011 text uses Theorem 2.28 / Problem 2.29, journal p. 290, reference 40, and explicitly says regularity has a unique common limiting fixed point. Accessed this through the author-uploaded published text indexed at Academia. Direct local download returns 403; retain a verified transcription of the relevant passage if a full text cannot be obtained. Springer 2015 chapter 2 is pp. 7–30 but only metadata/references accessible, not a full chapter.
The process already inherits nice 10 (os.getpriority verified). Calling nice -n 10 attempts to increase it to 20 and is denied by the sandbox; use inherited nice 10 directly.

## Literature phase result — literature phase result; begin derivations
Searched 2009–2026 regularity, positive coefficients, contractive QSOs, alpha_m/lambda_m, Zhamilov/Jamilov, Mukhamedov–Saburov, F-QSOs, later surveys. No exact all-dimension threshold found. This is a bounded search result, not a proof of absence. Saburov's 2017/2018 positive results impose doubly stochastic structure. F-QSOs have zero coefficients, so do not answer the uniform-positive threshold. Relevant newer framework: Fasino–Tudisco, Ergodicity coefficients for higher-order stochastic processes, SIAM J. Math. Data Sci. 2(3) (2020), 740–769, arXiv:1907.04841. Saved full text.
A preliminary algebraic audit flags a factor-two discrepancy in the survey's binary threshold: for f(x)=ax²+2bx(1-x)+c(1-x)², fixed-point discriminant D=(2b-1)²+4c(1-a). On [l,1-l]^3 its maximum is 5-12l+8l², whose equality to 4 gives (3-sqrt(7))/4. Need independent verification and complete convergence argument.
Found a potential improved upper bound from symmetry plus restriction to x_k>=l: Lipschitz factor <=2(1-ml)(1-l). Verify before final reporting.
Started one-worker SLSQP searches for m=3,4, proper two-cycles and distinct fixed points, gaps .02/.002, 12 starts per case, analytic Jacobians. All jobs inherit nice 10 and numerical libraries are capped to one thread.

## Exact candidate family discovered from constrained optimisation
The m=3 two-cycle search approached lambda=1/12; a distinct-fixed-point search did too. The swap-symmetric family uses two outer types (1,3), neutral parent class B={2,4,...,m}, and a residual deterministic Q: AA and AB produce C; CC and CB produce A; AC and BB produce type 2. Put P=l+(1-ml)Q. Writing t=1-ml, z=mass(B), d=x1-x3 gives d'=-t(1+z)d. A swap cycle has z=1/t-1 and outer coordinates u,v with u+v=2-1/t and uv=l/t. Its discriminant is positive precisely when t>(1+1/sqrt(m+1))/2, i.e. l<L_m=(1-1/sqrt(m+1))/(2m). Remaining neutral types sit at l. All coefficients >=l. This proves lambda_m>=L_m and, with lambda_m<=1/(2m), the asymptotic lambda_m~1/(2m). Need audit full identities and strict-threshold quantifiers.
Numerical first pass (12 starts/gap) is exploratory: m=3 cycle .0833052 and distinct fixed .08333305; m=4 fixed .06907488, close to L4=.06909830. Some starts failed. Runtime warnings on bounded matrix products need independent scalar verification; no floats will be used as certificates.

## Stronger upper bound and exact checks
A Fisher–Rao argument improves the upper bound to C_m=2/(3m+2+sqrt(m²+12m+4)), giving C3=1/9 and C4=(7-sqrt(17))/32. For P=l+tQ, the symmetric quadratic map Q has differential Fisher norm at most sqrt(2); the uniform-mixture channel q -> l*1+t*q has differential norm at most t/sqrt(t+2l) on zero-sum directions. Thus V contracts whenever 2t²<t+2l. The report will include an elementary proof of the mixture inequality and the complete-metric argument.
Exact symbolic identities checked: binary f²-x factorisation, binary discriminant bound and corrected root, all-dimension cycle discriminant, critical lower/upper formulas, and explicit radical cycles at m3 l=2/25 and m4 l=11/160. Both cycles are attracting by exact trace/determinant Schur inequalities; no interval approximation is needed for those certificates.
Refined the nonlinear two-point search to 36 starts per gap (.02,.002,.0002), plus 24 fixed-point instability starts per dimension. First pass data retained separately. Numerical jobs use one thread; measured peak RSS of the refined two-point search was 117,850,112 bytes.

## Final audit and result
REPORT.md finalized with first line PARTIAL. Proved L_m <= lambda_m <= C_m, where L_m=(1-1/sqrt(m+1))/(2m) and C_m=2/(3m+2+sqrt(m²+12m+4)); hence 2m lambda_m -> 1. Exact lambda_3 and lambda_4 remain unproved. Fully re-derived binary threshold (3-sqrt7)/4 and identified the discrepancy with the survey; cannot supply a proof of its printed doubled value.
Completed 432 refined two-point optimization solves and 48 fixed-point spectral-radius solves, plus the retained first pass. Exact symbolic checks all passed; independent scalar residual and derivative audits passed (Jacobian error <=7.21e-11). Exact two-cycle substitution and attraction certificates pass for m3 floor 2/25 and m4 floor 11/160. No global numerical optimality is asserted.
Literature access gaps remain explicit: 1988 original not obtained, Kesten original full text not obtained, Lyubich book and 2015 book chapter bodies inaccessible. The survey itself contains no proof of Theorem 7/Theorem 2.28. Sources and search ledger are saved as plain text.
Final folder audit found no PDF, page-image or scan files. Peak numerical RSS ~118MB, inherited nice 10, one numerical worker/thread. No publication, pushes, subagents, or changes outside the task directory were made by the research workflow. Global mesh hello had failed on its read-only database; no global checklist or brain writes were attempted afterward. Durable mathematical results are left here in REPORT.md because the task confines writes to this directory.
Task: “Open problem E0065 ... Find the exact value of lambda_m for every m >= 3.” Received 2026-11-13 about 08:49 Asia/Tbilisi; exact user-message timestamp unavailable. Completed research attempt with a partial result.
