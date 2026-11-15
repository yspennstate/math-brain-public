# T090 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 01:20:02 +04. Prompt receipt time unavailable.

## Orientation and bounded literature check

Read the earlier REPORT.md, LOG.md, and SOLVED_ELSEWHERE.md in ~/codex_op_1114/briefs/T090. There is no earlier PROOF.md and no .py/.sh/.jl computation script. Read the existing memory index and compute governor file without invoking utilities that write outside this folder. The current task's restriction to this folder takes precedence over global mesh/checklist/brain writes. No git or subagents.

The governor reports status warn, mode owner_away_open, CPU 99.7%. Only tiny scalar calculations are planned. After the initial orientation reads, shell programs are invoked with OMP_NUM_THREADS=1 nice -n 15. The sandbox reports `nice: setpriority: Operation not permitted`; effective lowering of priority is not claimed. Initial read-only shell calls omitted that wrapper. No heavy job is started.

Web queries: `"KPZ" "2+1" "2026" rigorous exponents`; `"2610.31614"`; `site.arxiv.org "KPZ" "November" "2026" "two-dimensional"`; `two dimensional stochastic heat equation second moment Lyapunov exponent small noise 4 pi bound state`.

Opened primary sources https://arxiv.org/abs/2610.31614 and https://arxiv.org/html/2610.31614v1. Read Theorem 1.2, Remark 1.3, Theorem 1.6, and the critical-tuning formulas. No newer solution of fixed-coupling T090 found in this bounded check (less than five minutes). Search absence is not proof of absence.

## Independent recheck of earlier result

The earlier result holds as a scope statement. Independently invert its tuning formula:

    beta_N^2 = log(1 + (1 + theta/log N)/R_N), R_N ~ (log N)/pi.

Taylor expansion gives beta_N^2 log N -> pi and beta_N -> 0. For any fixed b != 0, `(exp(b*b)-1)*R_N -> infinity`, whereas the critical tuning requires convergence to 1. The continuum formula in the paper independently gives beta_epsilon^2 |log epsilon| -> 2*pi, also vanishing coupling. Thus its non-Gaussian critical distribution theorem cannot be applied to fixed coupling. This verifies scope, not the paper's entire proof. The earlier decision to stop on an advance that does not solve T090 is not reused here.

## Chosen extension, before doing it

Choose one fixed-coupling special case: the flat-initial-data multiplicative SHE on R^2 with generator (1/2)Delta and Gaussian spatial noise covariance R_s(x)=(4*pi*s)^(-1) exp(-|x|^2/(4*s)), s>0. Derive explicit scalar renewal upper and lower bounds for E[Z(t,0)^2], and use them to bound its annealed exponential growth rate. Gaussian conditioning appears to sandwich each ordered interaction integral between products of 1/[4*pi*(gap+s)] and 1/[4*pi*(gap+2*s)]. This would give bounds whose scalar rates differ by exactly a factor of two, and recover the weak-coupling logarithmic scale without addressing typical log-height fluctuations. This is new relative to the earlier folder, not claimed new to the literature. The chosen observable is an exponential height moment, not height variance.

Plan for audit: integrate Gaussian products independently via a covariance determinant; check the rate equation by two scalar integrals; inspect zero coupling, very short gaps, long gaps, and diffusion normalization. Every numerical result will be labelled illustrative rather than a certified interval.

## Derivation: renewal sandwich

Write g=b^2 and let D be the difference of two Brownian motions with generator (1/2)Delta, hence D has generator Delta and per-coordinate variance 2*t. Wick normalization cancels self-interactions, leaving M(t)=E_0 exp(g integral_0^t R_s(D_u)du).

For ordered time gaps d_i, multiplication by R_s and Gaussian integration preserve a centered Gaussian state. If the previous per-coordinate variance is v in [0,2*s], the next normalization is 1/[2*pi*(v+2*d_i+2*s)] and the next variance is 2*s*(v+2*d_i)/(v+2*d_i+2*s). Therefore every ordered product lies between products of 1/[4*pi*(d_i+2*s)] and 1/[4*pi*(d_i+s)]. This gives F_{2s}(t) <= M(t) <= F_s(t), where F_a=1+k_a*F_a and k_a(u)=g/[4*pi*(u+a)]. The bounds require the Gaussian covariance and flat initial condition.

The Laplace root r_a satisfies (g/(4*pi))*exp(a*r_a)*E1(a*r_a)=1, so r_a=x_g/a. A direct Volterra subsolution/supersolution proof gives lim t^{-1}log F_a(t)=r_a. Gaussian products starting away from zero are no larger than those starting at zero; the Markov property then makes log M subadditive, proving existence of its rate gamma. Consequently x_g/(2*s) <= gamma <= x_g/s. Full proof will be saved before numerical audit.

Opened Le Chen and Kunwoo Kim, *Nonlinear stochastic heat equation driven by spatially colored noise: moments and intermittency*, https://arxiv.org/abs/1510.06046 and its PDF. Its introduction already records absence of a second-moment phase transition in d=1,2. Thus positivity of this moment exponent is established background; the present contribution is an independently checkable Gaussian calculation with explicit scalar bounds relative to the earlier report, not a claim of a new intermittency theorem. This background lookup occurs after the bounded status check and concerns the chosen subproblem only.

## Proof saved; first numerical-audit launch

Saved PROOF.md with the Gaussian recursion, finite-time renewal sandwich, elementary Volterra rate argument, subadditivity proof of existence of the actual second-moment rate, and weak-coupling asymptotic. Independently checked diffusion conventions: the difference process has generator Delta, not (1/2)Delta. For diffusion coefficient d in the SHE, the weak-coupling logarithmic constant is -8*pi*d; the proof's normalized d=1/2 case has -4*pi. The Cole–Hopf relation to the prompt includes the deterministic Itô correction.

Created check_gaussian_renewal.py, using only the Python standard library, with Gaussian determinant and scalar integral audits. Command:

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_gaussian_renewal.py

First launch stopped immediately before calculation: `ValueError: current limit exceeds maximum limit` at resource.setrlimit(RLIMIT_AS, (256 MiB,256 MiB)). The sandbox also denied changing nice priority. This is a resource-limit portability failure, not a mathematical or numerical failure. Next change: attempt a soft limit without altering the hard limit; if unsupported, report that and measure the tiny script's peak RSS explicitly.

## Independent computational audit: passed

Reran the same command after making resource-limit handling portable. Address-space limiting is unavailable in this Darwin sandbox; a 90-second CPU limit was installed. No arrays larger than 12 by 12, no third-party imports, threads, subprocesses, or GPU. Measured peak RSS: 12.609 MiB. Measured runtime: 0.051 seconds. Priority lowering was again denied, so this was a tiny ordinary-priority calculation despite the requested nice invocation.

Output:

```text
Deterministic floating-point audit; seed=9090; s=1 for rates
b        log(x_g)          lower rate       upper rate       b^2 log(x_g)
0.25    -201.6391454946   1.34338898e-88   2.68677795e-88    -12.6024465934
0.5      -50.8426981223   4.15209006e-23   8.30418012e-23    -12.7106745306
1        -13.1435597156   9.79026725e-07   1.95805345e-06    -13.1435597156
2         -3.6078569517   1.35549412e-02   2.71098824e-02    -14.4314278067
4         -0.4248708866   3.26927101e-01   6.53854201e-01     -6.7979341850
8          1.4447705827   2.12043955e+00   4.24087910e+00     92.4653172897
max independent scalar-integral relative error: 1.238e-12
Gaussian recurrence vs covariance determinant: 515 cases PASS
max absolute log-product discrepancy: 9.663e-13
n=2 closed-form checks: 3 PASS
rate-equation covariance-time scaling: 4 PASS
PASS: numerical checks only; analytic argument is in PROOF.md
```

Independence of the checks: the proof uses sequential Gaussian reweighting; the script separately evaluates `A_n=(4*pi*s)^(-n)/det(I+C/s)`, `C_ij=min(t_i,t_j)`, using Cholesky elimination. It compares 515 deterministic cases, including nearly coincident observations, long gaps, mixed gaps, and three covariance scales. The two scalar evaluations use the E1 power series (or the original nonsingular integral) versus quadrature after logarithmic substitution. Root residuals are numerical checks, not rigorous interval enclosures. The proof establishes the inequalities without relying on these numbers.

## Attempts to break the result

1. Derived the multivariate determinant formula independently on paper, not just numerically; added it and the explicit n=2 formula to PROOF.md. At n=1 the interaction is exactly 1/[4*pi*(u+s)], yielding the first expansion term `(g/(4*pi))*log(1+t/s)`. Its derivative at zero is g*R_s(0), agreeing with the moment PDE and catching a potential factor-of-two error.
2. Coincident gaps: the recursion remains bounded as gaps tend to zero; the lower bound is conservative at the first observation because v_0=0. Long gaps: both denominators have the same leading 4*pi*u, which is the source of the shared weak-coupling exponent. Boundary times have integration measure zero. The script checked near-coincident and strongly separated gaps explicitly.
3. Zero coupling is excluded from the root definition. At b=0 the equation has Z=1 and gamma=0, consistent with the limit of the bound. Negative b gives the same moment by symmetry of the noise. The singular s=0 limit is not covered. Gaussian isotropy and flat initial data are used; replacing the covariance or initial condition without a new argument is unjustified.
4. The inequality `Phi(x)<1/x` implies x_g<g/(4*pi), so the proposed upper rate is smaller than the immediate pathwise bound g*R_s(0). This checks magnitude. Weak-coupling root logs approach the independently derived -4*pi scale; the b=4 and b=8 rows are not in that asymptotic regime.
5. Rechecked the Volterra lower comparison carefully: for r below the root, the exponential trial function is a subsolution only after choosing its small prefactor using T. Iterating leaves a factorially vanishing remainder on each finite interval. Rechecked the rate-existence argument: spatial maximization at zero gives subadditivity, not superadditivity.
6. Tried to infer a height-variance bound from the positive annealed exponent; this does not follow. An explicit obstruction at the level of random variables: for any c>0, let Z_t=e^(2*c*t) with probability p=e^(-3*c*t), and Z_t=(1-e^(-c*t))/(1-p) otherwise. Then E Z_t=1, t^(-1)log E Z_t^2 -> c, but Var(log Z_t)=p*(1-p)*(2*c*t-log((1-e^(-c*t))/(1-p)))^2 -> 0. This is not a model counterexample; it shows why a moment estimate alone cannot prove T090. No estimate of beta, alpha, or a limiting height law was obtained.

No mathematical counterexample to the stated Gaussian proposition was found. Its general phenomenon is known; novelty of the particular factor-two presentation has not been investigated or claimed.

## Sources and final report

Primary sources actually opened:

- Quentin Berger, Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu, Shuta Nakajima, Rongfeng Sun, Li-Cheng Tsai, Zuodi Xie, and Nikos Zygouras, *The Critical 2D KPZ Process*, arXiv:2610.31614v1, submitted 22 October 2026. https://arxiv.org/abs/2610.31614 and https://arxiv.org/html/2610.31614v1. Used only for rechecking the earlier critical-regime scope.
- Le Chen and Kunwoo Kim, *Nonlinear stochastic heat equation driven by spatially colored noise: moments and intermittency*, arXiv:1510.06046. https://arxiv.org/abs/1510.06046 and https://arxiv.org/pdf/1510.06046. Used to identify existing moment-intermittency background, not as a substitute for the proof here.

REPORT.md records the proved special-case lemma under a PARTIAL verdict for T090. No SOLVED_ELSEWHERE.md was created because no solution of the stated problem was identified. No claim about the novelty of these inequalities in the wider literature is made. All created files are in this folder. The earlier folder was only read.

Final artifact check at 2026-11-15 01:27:17 +04:

    OMP_NUM_THREADS=1 nice -n 15 sh -c 'head -1 REPORT.md; wc -c REPORT.md PROOF.md LOG.md check_gaussian_renewal.py; rg -n "VERDICT|Next worker|Task:|What failed|Limits and uncertainty" REPORT.md; date "+%Y-%m-%d %H:%M:%S %z"'

Confirmed the required first line, all four nonempty deliverables, the command, failed launch and resource limitations, scope, and next-worker instruction. No further computation was necessary after the successful independent audit; subsequent changes only added written derivations and reporting.
