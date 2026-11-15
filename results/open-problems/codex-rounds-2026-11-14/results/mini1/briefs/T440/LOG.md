# T440 work log

Task: "push this problem forward by one checkable piece" (14 November 2026; session began about 22:16 Asia/Tbilisi).

## Scope and startup

All artifacts stay in this folder. No git or external writes. Read the startup memory index and compute state: status warn, mode owner_away_open, free memory 60 percent. The task-specific prohibition on outside writes supersedes mesh/checklist/memory writes; these records stay here. A read-only brain recall was attempted with bytecode disabled and BRAIN_RECALL_SERVER=0; its result is recorded below when available.

Commands: `pwd`; `rg --files -g '!.*' . ~/.claude ~/brain-views | head -60`; read startup MEMORY.md and compute_state.json; read the beginning of brain.py. Subsequent shell programs are invoked with OMP_NUM_THREADS=1 and nice -n 15. The inherited process appears already at low priority: nice reports `setpriority: Operation not permitted`; actual priority will be checked before computation. No heavy computation is planned.

## Literature check (began 22:17; bounded by ten minutes)

Web search queries:
- `"2606.15842"`
- `"Muller" "ratchet" "sharp" "diffusion" extinction prefactor 2026`
- `"Muller" "ratchet" "first passage" Haigh asymptotic`
- `"Muller's ratchet" "2026" "extinction" diffusion`
- `"Muller's ratchet" "Eyring" OR "prefactor" OR "quasipotential"`
- `"Heinzel" "Pfaffelhuber" "Wakolbinger" ratchet 2026 2027`

Opened arXiv abstract pages 2606.15842 and 1206.6782 and HTML 2606.15842v1. The former lists only v1 (14 June 2026); the latter lists v1 (28 June 2012). An attempted HTML URL for 1206.6782v2 failed; the actual abstract lists only v1. Search has not identified a later solution. This is a limited search, not a proof of absence.

## Choice, before calculation

Prove an explicit asymptotic lower bound for the original infinite-dimensional diffusion when 0 < lambda < alpha. Use mean(X) >= 1-X_0 to compare with the scalar Wright-Fisher diffusion having drift y[alpha(1-y)-lambda] and covariance y(1-y)/nu. Solve its mean extinction ODE exactly by a double integral, then evaluate the integral sharply by endpoint and saddle asymptotics. Transfer the bound directly by Ito's formula for its increasing mean-lifetime function, avoiding any unproved closure of X_0 or interchange of population and diffusion limits.

Why this piece: it has a complete one-dimensional calculation and a pathwise drift inequality valid for the full stated diffusion. It gives a positive explicit lower exponent in a genuine parameter region. It cannot determine the full model's sharp rate or prefactor.

## Literature check completed (within ten minutes)

Additional searches: `"Metastability between the clicks" Mariani Pardoux Velleret arxiv`; `"Muller" "ratchet" "2026" "asymptotics" diffusion click time`.
Opened https://arxiv.org/html/1206.6782v1 (successful), https://arxiv.org/abs/2512.24779, and the current Pfaffelhuber publication page. Opened arXiv:2007.14715 to check the quasistationarity result. No subsequent sharp first-click asymptotic for the specified diffusion was located. Tournament selection has a different closure and does not solve this problem. No SOLVED_ELSEWHERE.md is warranted.

The recall returned off-topic extinction/trading memories, no usable ratchet mathematics. Its output also mentioned a failed detached index-refresh attempt. No further brain command will run: all subsequent work and logs stay in this folder.

Priority probe: `OMP_NUM_THREADS=1 nice -n 15 python3 - ...` printed `nice 20`, Python 3.13.2, and mpmath/scipy/numpy available. Thus the nice warning comes from attempting to raise the inherited niceness from 20 to 15; the actual process is already below the requested priority. The numerical audit will be one thread and a short CPU limit.

## Derivation

Set d=alpha-lambda, q=1-lambda/alpha. For the scalar generator L=b(y)d/dy+y(1-y)/(2nu)d²/dy² with b=y[d-alpha y], the integrating exponent is F(y)=2alpha y+2lambda log(1-y). Solving Lu=-1 gives
u_nu(x)=2nu integral_0^x exp(-nu F(z)) integral_z^1 exp(nu F(y))/(y(1-y)) dy dz.
Here the symbol u_nu denotes a function, not the parameter nu. It is increasing, continuous and bounded on [0,1], with u_nu(0)=0 and u_nu'(1)=1/lambda. The full generator acting on u_nu(X_0) is at least -1, since its excess drift is alpha X_0 [mean(X)-(1-X_0)] >= 0.

Tentative scalar asymptotic, to be checked independently:
V=F(q)=2[alpha-lambda+lambda log(lambda/alpha)],
u_nu(exp(-lambda/alpha)) ~ alpha sqrt(pi)/(sqrt(lambda)(alpha-lambda)^2 sqrt(nu)) exp(nu V).
The same expression is therefore a lower asymptotic bound for E tau_nu, not an equality for the full diffusion.

## Proof written

Created PROOF.md with: the exact scalar mean-lifetime integral; endpoint regularity at 0 and 1; the stopped Ito lower-bound transfer; and a four-region proof of the Laplace asymptotic. The last region is necessary because F(x_0) can be negative, so a naive global bound by the saddle integral would fail. The scalar prefactor simplifies to alpha sqrt(pi)/(sqrt(lambda) d^2). The full claim is only a liminf lower bound. Next: independent numerical and flux checks.

## Numerical audit script prepared

Wrote audit.py. Two positive quadratures evaluate the exact scalar integral in opposite integration orders. A separate quadrature integrates 2b/a to check V. A boundary-flux calculation checks the constant without using the original double integral, and time rescaling checks the alpha power. Four parameter pairs and five noise levels will be used. These are checks of the scalar calculation, not simulations or estimates of the full diffusion. CPU capped at 120 seconds; all library thread counts one; actual inherited niceness 20.

Exact command to run:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1`

## Numerical audit completed

Command above exited 0. Complete output:

```text
nice: setpriority: Operation not permitted
Python 3.13.2 nice 20
CPU cap 120 seconds; all numerical library thread counts = 1
a=1 l=0.25 nu= 25 ratio=1.0263356373 order_gap=3.04e-12
a=1 l=0.25 nu= 50 ratio=1.0126605642 order_gap=1.23e-16
a=1 l=0.25 nu=100 ratio=1.0062170505 order_gap=3.5e-16
a=1 l=0.25 nu=200 ratio=1.0030816165 order_gap=2.11e-15
a=1 l=0.25 nu=400 ratio=1.0015342418 order_gap=4.57e-15
a=1 l=0.5 nu= 25 ratio=1.1110971271 order_gap=5.98e-16
a=1 l=0.5 nu= 50 ratio=1.0471269847 order_gap=1.25e-10
a=1 l=0.5 nu=100 ratio=1.0220556604 order_gap=1.3e-15
a=1 l=0.5 nu=200 ratio=1.0107082454 order_gap=2.63e-15
a=1 l=0.5 nu=400 ratio=1.0052796413 order_gap=3.97e-15
a=1 l=0.8 nu= 25 ratio=1.0742835753 order_gap=5.01e-16
a=1 l=0.8 nu= 50 ratio=1.3754534536 order_gap=7.37e-16
a=1 l=0.8 nu=100 ratio=1.3077524793 order_gap=5.48e-16
a=1 l=0.8 nu=200 ratio=1.1305976679 order_gap=1.79e-15
a=1 l=0.8 nu=400 ratio=1.0560932697 order_gap=1.12e-10
a=2 l=1 nu= 25 ratio=1.0471269847 order_gap=1.25e-10
a=2 l=1 nu= 50 ratio=1.0220556604 order_gap=1.3e-15
a=2 l=1 nu=100 ratio=1.0107082454 order_gap=2.63e-15
a=2 l=1 nu=200 ratio=1.0052796413 order_gap=3.97e-15
a=2 l=1 nu=400 ratio=1.0026218041 order_gap=9.37e-15
maximum order-of-integration gap 1.248482103298407e-10
maximum barrier error 1.1102230246251565e-16
maximum prefactor error 1.1102230246251565e-16
elapsed_seconds 0.411
peak_rss_bytes 72613888
PASS: 20 scalar checks; no full-diffusion simulation or rate estimate.
```

Data: audit_data.csv (20 rows). Peak RSS 72,613,888 bytes; runtime 0.411 seconds. The largest disagreement between the two integration orders was 1.25e-10 relative. The ratio to the scalar asymptotic at nu=400 was 1.00153424 for (alpha,lambda)=(1,0.25), 1.00527964 for (1,0.5), and 1.05609327 for (1,0.8). The larger error near lambda/alpha=1 agrees with the stated lack of uniformity; monotone convergence of finite-nu ratios is not claimed.

## Final audit and report

Wrote CHECKS.md and REPORT.md. The independent flux calculation gives J=d A at the absorbing boundary, with bulk normalization A=a(q) exp(-nu V) sqrt(nu |F''(q)|/(2pi)); its reciprocal reproduces C. Time rescaling (alpha,lambda,nu) -> (1,lambda/alpha,alpha nu) independently reproduces the alpha^(-3/2) multiplier scaling. Reviewed the sign of the generator inequality, finite stopping, the inward boundary at 1, the logarithmic derivative at 0, the critical case lambda=alpha, the zero-mutation case, and the region beyond the saddle. No matching upper bound or equality for the full diffusion is claimed. No further literature search or compute is needed.

The report gives a possible next step using an increasing two-coordinate test function and the exact bound m >= 2(1-X_0)-X_1; this is a suggestion, not a result proved here. All produced artifacts stay in this folder.

Final artifact audit: all seven deliverables exist and are nonempty; audit.py parses; CSV contains a header plus 20 records; saved output contains PASS; REPORT.md begins with the required VERDICT line. No numerical rerun.
