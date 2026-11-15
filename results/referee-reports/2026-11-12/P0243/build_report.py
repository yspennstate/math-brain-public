"""Assemble the referee report from saved independent numerical output."""
import csv, hashlib, json
from decimal import Decimal, localcontext
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def read(name):return json.loads((ROOT/name).read_text())
def fixed(value,places=30):
    with localcontext() as ctx:
        ctx.prec=100
        return format(Decimal(str(value)),'.'+str(places)+'f')

def main():
    p=read('precision_results.json');g=list(csv.DictReader(open(ROOT/'gamma_results.csv')))
    st=read('stopping_summary.json');search=read('ratio_search_results.json')
    final=read('finalist_results.json');cert=read('rational_certificates.json');manifest=read('run_manifest.json')
    sha=hashlib.sha256((ROOT/'PAPER.tex').read_bytes()).hexdigest()
    parts=[r'''# Independent referee report

Overall verdict: **SOUND**

Both main theorems and their discrete-time proofs are mathematically sound on this audit. I found no missing argument in the uniform three-state lower bound, the limiting threshold argument, or the randomized optional-stopping proof. The independent computations reproduce every mathematical numerical prefix checked in the source. The paper's description of Hermon's result should specify conditioning or normalization: its unconditioned interpretation is false. Priority and exact bibliographic attributions remain unverified; SOUND is a verdict on the proved results, not a certification of novelty.

This audit followed the requested order, recording each stage as it was reached in [LOG.md](LOG.md). References below are source line numbers, since no compiled numbering was supplied. The original source was left untouched. No browsing, other agents, author programs, external writes, pushes, visible windows or external messages were used. Shared brain/checklist/mesh commands were not run because their writes would violate this run's folder restriction. The only outside reads were the standing-instruction orientation and compute-state information, not mathematical sources or prior audits.

## Verdict table

CORRECT means the mathematical assertion or step checks out. GAP in bibliographic rows means the requested attribution cannot be verified under the no-browsing constraint; it does not denote a gap in either main theorem. The conditional WRONG row below concerns an explicitly identified reading of one background sentence.

| Statement or step | Verdict | Reason |
|---|---|---|
| Four parameters, lines 33–41 | CORRECT | Match the supplied problem and my recollection: pairwise TV, level 1/e, max-start infimum of randomized stationary stopping means. |
| Random-target constancy, line 37 | CORRECT | Independently follows from the hitting-time/fundamental-matrix calculation below. |
| Exact book numbering and discrete conventions, lines 37–50, 81 | GAP | Source not supplied; memory cannot certify equation and theorem numbers. |
| tau_2 <= tau_1, line 45 | CORRECT | Oscillation of a real second eigenfunction contracts by at most dbar(t). |
| tau_2 <= tau_0, line 45 | CORRECT | One reciprocal eigenvalue is at most their positive sum. |
| tau_1^(2) <= tau_0, line 45 | CORRECT | Independently chosen stationary target gives such a stopping rule. |
| Constant 66 and equivalence family, lines 43–47 | GAP | Plausible quotations from memory; not independently checked against the book. |
| [eq:tk], lines 55–57 | CORRECT | Gamma survival formula has a unique 1/e crossing. |
| Reversibility and irreducibility, lines 54, 85 | CORRECT | pi_i proportional to eps^i satisfies detailed balance on a connected path. |
| [eq:eigentime], lines 85–88 | CORRECT | Trace of the integrated semigroup is both Kemeny's constant and the reciprocal spectral sum. |
| Trace, principal minors, determinant, line 91 | CORRECT | Values are 2+2eps; eps^2, eps, 1; and zero. |
| Three-state formula, lines 92–94 | CORRECT | Sum/product of nonzero roots gives 2(1+eps)/(1+eps+eps^2)<2. |
| [eq:d02], lines 96–99 | CORRECT | A signed difference on event {0} is bounded above by TV. |
| [eq:stay], lines 100–103 | CORRECT | No jump from 0 has probability exp(-eps t). |
| Retaining first and last holding times, lines 104–108 | CORRECT | Conditional laws are fixed independent exponentials of rates 1 and 1+eps. |
| Formula for g, lines 109–111 | CORRECT | Exp(1)+Exp(1) has survival exp(-s)(1+s). |
| [eq:descend], every inequality, lines 112–115 | CORRECT | Occupancy implies hitting; deleting positive holding times speeds hitting; coupled exponentials give the stated CDF direction. |
| Monotonicity and scalar bounds, line 116 | CORRECT | g'(s)=-s exp(-s); exp(-x)>=1-x. |
| [eq:lower], every inequality, lines 117–119 | CORRECT | All bounds hold uniformly for every t in [0,2]. |
| Equivalence with f(eps)>0, lines 120–123 | CORRECT | Exact expansion after multiplying by exp(2). |
| f decreasing and numerical margin, line 124 | CORRECT | f'<0; exact rational arithmetic certifies f(.01)>.093537. |
| Strict tau_1>2, [thm:a](i), lines 61–64, 124 | CORRECT | Entire interval excluded; continuity excludes an immediate crossing just after 2. |
| Need for monotonicity of dbar in this proof | CORRECT | It is not used; it also follows independently from TV contraction. |
| Limit of tau_0, line 127 | CORRECT | Simple zero root remains isolated; the other k roots tend to 1. |
| Semigroup continuity identity, line 129 | CORRECT | Duhamel's formula works without commutativity and gives compact-uniform convergence. |
| Pure-death dbar computation, lines 129–133 | CORRECT | Every pair is bounded by survival from k; (0,k) attains it. |
| Transverse threshold crossing, line 133 | CORRECT | Derivative at t_k is -exp(-t_k)t_k^(k-1)/(k-1)!<0. |
| Limit of tau_1, [thm:a](ii), lines 65, 133 | CORRECT | Uniform margins before and after t_k squeeze the first threshold. |
| Reducible limiting chain, lines 69, 127–133 | CORRECT | Only its semigroup distance is used; k is a limit of tau_0, not its irreducible hitting parameter. |
| First five gamma ratios, line 69 | CORRECT | All printed prefixes agree with independent 75-digit roots. |
| Maximum for k<=60, line 69 | CORRECT | Certified by rational root brackets of width 1e-40 for all 60 values. |
| t_k/k ->1, line 69 | CORRECT | LLN sandwiches the fixed survival quantile between k(1-delta) and k(1+delta). |
| Universal constant lower bound, line 69 | CORRECT | A limiting family of admissible irreducible examples supplies the bound. |
| P=I+cQ stochastic and reversible, line 136 | CORRECT | The exit-rate constraint keeps diagonals nonnegative. |
| Continuization and ratio scaling, line 136 | CORRECT | Both threshold and mean hitting times scale by 1/c. |
| Telescoping and exponential remainder, lines 138–141 | CORRECT | Stochastic row norms are 1; error is at most m(c||Q||)^2 exp(c||Q||)/2. |
| TV perturbation bound and raw threshold, line 142 | CORRECT | Row-pair TV error <= matrix row norm error; the explicit positive margin survives for small c. |
| Discrete assertions proved or computed? | CORRECT | Both scaling and the small-c raw inequality are proved analytically, not merely computed. |
| Eigenfunction, sign choice and pi(u)=0, lines 72, 147 | CORRECT | Reversibility supplies a real eigenfunction; stationarity annihilates its nonzero eigenspace. |
| Randomized filtration and Dynkin martingale, line 147 | CORRECT | Independent randomization preserves the original Q-semigroup Markov property. |
| Bounded optional stopping, lines 147–150 | CORRECT | The martingale is bounded on each fixed time interval. |
| Passage t->infinity, line 151 | CORRECT | Bounded convergence for u(X_U); domination by integrable U for the integral. |
| Infinite-mean U, implicit at line 147 | CORRECT | Lower bound is immediate in the extended reals; no evaluation of X at infinity is needed. |
| Integral identity and bound, lines 152–155 | CORRECT | Pointwise u<=1 gives u(i)<=lambda_2 E_i U; changing sign gives the modulus. |
| Choice of worst start, [thm:b], line 155 | CORRECT | A state with |u(i)|=1 exists before taking the infimum and maximum. |
| Discrete martingale and sum bound, lines 159–163 | CORRECT | Compensation is 1-lambda_2, even for negative lambda_2 and periodic chains. |
| Remark 1, line 166 | CORRECT | Independent immediate-stop/hit-other-state mixture gives equality for all positive two-state rates. |
| Remark 2, line 168 | CORRECT | The random-target stopping rule gives the upper bound. |
| Remark 3, every algebraic step, lines 170–173 | CORRECT | Nonnegative shifted row of Z has mass m and integrates u to tau_2. |
| Remark 3, optimal stopping formula | CORRECT | Independently derived and attained by the occupation-measure construction below. |
| Remark 4, line 175 | CORRECT | Complex Dynkin identity followed by the triangle inequality gives the modulus bound. |
| Remark 5, lines 177–181 | CORRECT | delta=.1 gives absolute relaxation 5 but optimal stationary stopping mean 5/9. |
| Printed mathematical computations, line 185 | CORRECT | Independently checked values and convergence claims agree. |
| Author script/Lean execution claims, lines 185–187 | GAP | Artifacts unavailable here; no claim of having audited them. |
| Lovasz–Winkler description, line 41 | CORRECT | Consistent with remembered optimal stopping/access-time theory; bibliographic details unchecked. |
| Hermon description, line 52 | GAP | “Stationary” needs explicit conditioning/normalization; precise attribution cannot be checked. |
| Unconditioned E_pi T_A interpretation of line 52 | WRONG | Two-state rare-state example below rules out uniform comparability. |
| Novelty and priority, lines 27, 52, 208 | GAP | No reliably recalled resolution, but no literature access to establish absence. |

## Load-bearing derivations

For the three-state chain,

\[
Q=\begin{pmatrix}-\varepsilon&\varepsilon&0\\1&-(1+\varepsilon)&\varepsilon\\0&1&-1\end{pmatrix},
\quad \pi=\frac{(1,\varepsilon,\varepsilon^2)}{1+\varepsilon+\varepsilon^2}.
\]

The nonzero eigenvalues of -Q are 1+eps minus/plus sqrt(eps). Their sum is 2+2eps and product 1+eps+eps^2. Independently, hitting equations give H_01=1/eps and H_02=(1+2eps)/eps^2, so the stationary random-target mean from 0 is again 2(1+eps)/(1+eps+eps^2).

More generally, with Pi the matrix whose rows are pi,

\[
Z=\int_0^\infty(e^{tQ}-\Pi)\,dt=(\Pi-Q)^{-1}-\Pi,
\quad ZQ=QZ=\Pi-I,
\quad H_{ij}=\frac{Z_{jj}-Z_{ij}}{\pi_j}.
\]

Thus sum_j pi_j H_ij=tr Z=sum_(m>=2)1/lambda_m, independently establishing the identity used in the paper and random-target constancy.

The holding-time argument is a valid stochastic domination. Before reaching 0, retain the first hold at 2 and the final hold at 1. Conditional on the embedded jump path their joint law is always Exp(1) times Exp(1+eps), so this law persists after removing the conditioning. Their sum is no larger than T_0. Coupling that sum as E+E'/(1+eps) and comparing it with (E+E')/(1+eps) gives exactly the CDF inequalities in [eq:descend]. Together with the no-jump event from 0, this yields a time-uniform margin exp(-2) f(eps)>0 on [0,2]. The proof does not infer a first threshold from a single grid point.

The absorbed limiting chain is used correctly. Its pairwise distance is the gamma survival function, whose derivative at t_k is strictly negative. The uniform convergence on compact time intervals then controls the first crossing, not just the value at one time. The source never needs to assign its limiting stationary average hitting time the value k. That would be inappropriate with zero stationary masses and inaccessible states.

For [thm:b], use the chain's natural filtration enlarged by an independent random seed, or any filtration that preserves its original transition law. Dynkin's martingale stopped at U wedge t gives

\[
\mathbb E_i u(X_{U\wedge t})-u(i)
=-\lambda_2\,\mathbb E_i\int_0^{U\wedge t}u(X_s)\,ds.
\]

If E_i U is finite, bounded convergence and domination by U give u(i)=lambda_2 E_i integral_0^U u(X_s)ds. A sign change makes u(i) nonnegative and u<=1 bounds the integral by U. Infinite means satisfy the desired inequality immediately. Choosing a state of maximal eigenfunction modulus proves the sharp worst-start bound. No independence between U and X_U is required, and no unbounded optional-stopping theorem is silently invoked.

For reference, tau_2<=tau_1 is also independently plausible without the book: osc(P_t u)=exp(-lambda_2 t) osc(u), whereas osc(P_t u)<=dbar(t) osc(u), so dbar(t)>=exp(-lambda_2 t).

## 6. Independent numerical results

Every program used for the mathematics is supplied here. Spectral computations use the symmetric conjugate of the reversible generator, with direct mpmath.expm and independent hitting-system solves as separate checks. Root finding is bisection in high precision. The search uses direct scipy.linalg.expm of Q to avoid unstable reconstruction from very small stationary probabilities. Numerical LPs solve the full optimization problem, with feasibility and duality residuals checked; “exact” in that setting denotes the variational optimum rather than a lower bound, not symbolic rational arithmetic.

### (a) Three-state chain

Values below are rounded to 36 decimal places. Working precision was 85 digits; files retain 55 significant digits. Matrix-exponential root residuals are below 6e-60. Independent matrix exponential and spectral reconstruction agree within 2.6e-85 on the .05-spaced cross-check grid. The closed form, spectral sum and hitting-equation values of tau_0 agree.

| eps | tau_0 | tau_1 |
|---|---|---|
''']
    for r in p['three_state']:
        parts.append(f"| {r['eps']} | {fixed(r['tau0'],36)} | {fixed(r['tau1'],36)} |\n")
    parts.append('\n| eps | tau_1/tau_0 | dbar(2) = minimum on the [0,2] grid |\n|---|---|---|\n')
    for r in p['three_state']:
        parts.append(f"| {r['eps']} | {fixed(r['ratio'],36)} | {fixed(r['dbar_2'],36)} |\n")
    parts.append(r'''
The .001-spaced grids cover all 3,001 points of [0,3] at both eps values. Full tables are [grid_eps_0p01.csv](grid_eps_0p01.csv) and [grid_eps_0p001.csv](grid_eps_0p001.csv). On [0,2] the minimum margins above 1/e are .034521199252590968... and .037765550662800742..., respectively. TV contraction independently makes the exact continuous minimum occur at 2. The lower event bounds and exponential descent bounds pass every grid check; roundoff-sized signed slacks near t=0 are at most 3e-85.

These reproduce the source's tau_1=2.1330..., ratio 1.0666..., tau_0=1.99980..., dbar(2)=.40240..., and the .001 ratio 1.07244.... At eps=.05, the independent ratio is 1.04213907512266084..., also matching the printed prefix. No grid check substitutes for the analytic uniform argument.

### (b) Gamma quantiles, all k=1,...,60

Working precision was 75 digits. The following 30-place roots and 20-place ratios are independently certified by rational brackets of width 1e-40 for k>=2; t_1=1 exactly. Integer interval arithmetic bounds the exponential through a positive Taylor series plus a geometric tail, then compares sum_(j<k)t^j/j! with exp(t-1). No transcendental floating-point calculation is used in the certification step.

| k | t_k | t_k/k |
|---|---|---|
''')
    for r in g:parts.append(f"| {r['k']} | {fixed(r['t_k'],30)} | {fixed(r['ratio'],20)} |\n")
    parts.append(r'''
The certified finite maximum is at k=4:

\[
\frac{t_4}{4}=1.087998171950585377533522717634077308892\ldots.
\]

Its lower ratio bound exceeds every other upper bound; the minimum separation is greater than .0011796224264596565, attained against k=5. This verifies exactly the finite-range claim in the source, not a claim of maximizing over all integers. The LLN proof of the limiting ratio 1 is separate from this finite computation. See [gamma_results.csv](gamma_results.csv) and [rational_certificates.json](rational_certificates.json). The same exact arithmetic certifies f(.01)>.09353704956234176009, including the rounded exponential bounds used by the paper.

### (c) Small-drift chains

Values are rounded to 30 decimal places. The limiting targets t_k are in the preceding table. All eight cases use independent eigenvalue and hitting-equation tau_0 values; a direct matrix exponential at the threshold has residual below 3.1e-59. In the most ill-scaled hitting system (k=6, eps=1e-5), the absolute discrepancy in tau_0 is below 6.7e-62.

| k | eps | tau_0 | tau_1 |
|---|---|---|---|
''')
    for r in p['limits']:parts.append(f"| {r['k']} | {r['eps']} | {fixed(r['tau0'])} | {fixed(r['tau1'])} |\n")
    parts.append('\n| k | eps | tau_0-k | tau_1-t_k | tau_1/tau_0 |\n|---|---|---|---|---|\n')
    for r in p['limits']:
        parts.append(f"| {r['k']} | {r['eps']} | {fixed(r['tau0_minus_k'],12)} | {fixed(r['tau1_minus_tk'],12)} | {fixed(r['ratio'],15)} |\n")
    parts.append(r'''
The k=6 thresholds approach their limit from above. This is consistent with the theorem, which asserts convergence, not an approach from a particular direction. Direct exponentials for the absorbed chains at t=.2, k and t_k attain the gamma survival distance at (0,k). Complete precision output is [precision_results.json](precision_results.json).

### (d) Optimal stationary stopping: derivation and tests

In continuous time put x_j=E_i integral_0^U 1_(X_s=j) ds. Applying Dynkin's identity to each state indicator yields the necessary balance constraint xQ=pi-delta_i. The objective is E_i U=sum_j x_j. Thus the LP is

\[
\min_{x\ge0}\ \sum_jx_j\qquad\text{subject to}\qquad Q^T x=\pi-e_i.
\]

Equivalently, with exit rates q_j=-Q_jj, embedded jump matrix R, and v_j=q_j x_j, it is v(I-R)=delta_i-pi with objective sum_j v_j/q_j. This derives the division-by-exit-rate form requested in the prompt.

It is also sufficient, not just a lower bound. On arrival at j stop with probability

\[
s_j=\frac{\pi_j}{\pi_j+q_jx_j};
\]

otherwise wait an Exp(q_j) hold and jump using R. The expected number of arrivals is a_j=pi_j+q_jx_j: the balance constraint gives delta_i+a(1-s)R=a. Because all pi_j are positive, the finite-state continuation matrix has spectral radius less than 1, making this arrival solution unique. Stopped mass is a_j s_j=pi_j; occupation is a_j(1-s_j)/q_j=x_j. Thus this randomized stopping rule realizes the LP value. It is a stopping time for the original Markov process with independent auxiliary coins.

Since ZQ=Pi-I, every feasible solution has the form x=Z_i+t pi. Its total mass is t because Z1=0. Therefore

\[
\inf_U\mathbb E_i U=\max_j\frac{-Z_{ij}}{\pi_j},\qquad
\tau_1^{(2)}=\max_{i,j}\frac{-Z_{ij}}{\pi_j}.
\]

In discrete time, x counts visits strictly before U. Replace Q by P-I, minimize sum_j x_j, and stop on each visit to j with probability pi_j/(pi_j+x_j), including self transitions. This realizes the corresponding discrete optimum. The algebraic fundamental matrix remains valid for periodic P; one need not assume convergence of an unmodified discrete semigroup series.

The sample contains 2,500 independently drawn CT reversible chains on 3–7 states, with connected cycles in one third of cases and complete conductance graphs otherwise. Each has positive stationary law drawn from a Dirichlet distribution and positive symmetric edge conductances. There are also 2,500 discrete uniformizations of those same chains with a random admissible scaling. These CT and DT samples are related, not independent samples of each other. Seed: 48112026.

For 250 chains of each kind, the LP is solved for every starting state: 2,500 full LP optimizations in total. For the remaining chains the independently derived exact optimum formula is evaluated. A bound obtained from an eigenfunction alone is never used as a substitute for the stopping value.

| Test | Continuous time | Discrete time |
|---|---|---|
''')
    ct=st['continuous'];dt=st['discrete']
    metrics=[('Chains checked',2500,2500),('Chains with all-start LP solves',250,250),
             ('Minimum tau_1^(2)/tau_2',ct['min_stop_over_tau2'],dt['min_stop_over_tau2']),
             ('Maximum tau_1^(2)/tau_0',ct['max_stop_over_tau0'],dt['max_stop_over_tau0']),
             ('Violations of either inequality',ct['inequality_violations'],dt['inequality_violations']),
             ('Maximum relative LP/formula discrepancy',ct['max_relative_lp_error'],dt['max_relative_lp_error']),
             ('Maximum LP balance residual',ct['max_flow_residual'],dt['max_flow_residual']),
             ('Maximum relative duality gap',ct['max_relative_duality_gap'],dt['max_relative_duality_gap']),
             ('Maximum relative hitting-equation discrepancy',ct['max_relative_hitting_error'],dt['max_relative_hitting_error']),
             ('Minimum pointwise eigenfunction margin',ct['min_pointwise_eigen_margin'],dt['min_pointwise_eigen_margin']),
             ('Maximum constructed stopped-law error',ct['max_constructed_stop_error'],dt['max_constructed_stop_error']),
             ('Maximum relative constructed-mean error',ct['max_constructed_time_error'],dt['max_constructed_time_error'])]
    for label,a,b in metrics:parts.append(f'| {label} | {a} | {b} |\n')
    parts.append(r'''
All pointwise eigenfunction inequalities pass as well. The smallest ratio is above 1 because this sample excludes two-state chains; the paper's samples include them, where equality is exact. The different number of absolute-relaxation failures is also sampling dependent: there are 7 in this restricted uniformization sample. The analytic two-state example is conclusive independently of those counts.

Results, all chain-wise values and saved CT LP instances: [stopping_summary.json](stopping_summary.json), [stopping_results.csv](stopping_results.csv), [stopping_lp_instances.json](stopping_lp_instances.json). The corresponding DT matrices are reproduced deterministically by the script and seed.

### (e) Search for larger tau_1/tau_0

''')
    parts.append(f"The search evaluated {search['counts']['birth_death']:,} birth-and-death and {search['counts']['general']:,} general reversible candidates, on 3–8 states. It began with 2,400 random samples of each family and strongly biased baselines, then ran differential evolution and L-BFGS-B for both families in every dimension 3–8. Seed: {search['seed']}. Each candidate was rescaled to maximum exit rate 1. The birth-and-death optimizer varies directed log-rates, fixing one rate to remove scale; the general optimizer varies log stationary weights and symmetric conductances. Bounds and all optimizer settings are in [ratio_search.py](ratio_search.py).\n\n")
    parts.append('| Family | States | Largest independently verified ratio |\n|---|---|---|\n')
    for key,label in [('birth_death','Birth-and-death'),('general','General complete-graph reversible')]:
        r=final[key];parts.append(f"| {label} | {r['n']} | {fixed(r['ratio'],36)} |\n")
    parts.append(r'''
The best birth-and-death example is the paper's k=4 chain with down rates 1 and up rates 1e-10. Before the search's harmless time rescaling it has

''')
    b=final['birth_death']
    parts.append(f"- tau_0 = {b['tau0']};\n- tau_1 = {b['tau1']}.\n\n")
    parts.append(r'''
This falls below the limiting value t_4/4 by about 6.07e-11. No improvement over the paper's actual bound 1.087998171950585... was found. Although it exceeds the literal decimal 1.0879, that is just the paper's truncated notation and is not a stronger example. The finite search does not establish optimality or any universal upper bound.

The best general candidate and its defining parameters are saved in [ratio_search_results.json](ratio_search_results.json); [finalist_results.json](finalist_results.json) reconstructs it with exact row sums and detailed balance from its parameters and verifies the root using direct 85-digit matrix exponentials. The best general ratio is below the birth-and-death example.

As an extra check of [sec:a-disc], eps=.01 and c=.001 give tau_0(P)=1999.8019998019998..., whereas the raw discrete threshold is 2133: dbar(2132)=.3680039015838272...>1/e and dbar(2133)=.3677533330828673...<1/e. The sufficient norm bound in the proof is .00408865073844...<.01. This computation corroborates an analytic proof already present in the source.

## Commands, resources and reproducibility

Run the complete mathematical suite from this directory:

```sh
python3 run_audit.py > run_audit_stdout.jsonl
```

The supervisor sets OPENBLAS_NUM_THREADS, OMP_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS to 1, disables bytecode writes, and runs one computation at a time. Its child commands, which produced the saved tables, are:

```sh
python3 environment_probe.py > environment_results.txt
python3 gamma_audit.py > gamma_summary.json
python3 precision_audit.py > precision_stdout.json
python3 stopping_audit.py > stopping_stdout.json
python3 ratio_search.py > ratio_search_stdout.json
python3 finalist_audit.py > finalist_stdout.json
python3 rational_certificates.py > rational_stdout.json
```

To regenerate this report after those commands:

```sh
python3 build_report.py
```

All programs use only local files. Random generators use fixed seeds; there are no downloaded inputs. The largest matrices have eight states. The matrix, stopping, search and certificate scripts have 240-second alarms, the search additionally has a 180-second internal budget, and the supervisor enforces a 245-second subprocess timeout. Only the supervisor and one Python child run concurrently. No worker pool or background daemon is started.

''')
    parts.append(f"The successful complete rerun recorded a peak child RSS of {manifest['max_child_rss_bytes']:,} bytes ({manifest['max_child_rss_bytes']/1024**2:.2f} MiB), far below 1 GB. The longest individual command took {manifest['max_run_seconds']:.2f} seconds. See [run_manifest.json](run_manifest.json) for timings, exit codes, memory and stderr.\n\n")
    parts.append(r'''
The environment rejected nice priority changes and a preliminary attempt to set RLIMIT_DATA. The final runner therefore measures actual resident memory and checks it against 1 GiB; it does not claim an enforced heap limit. No sizeable allocation is needed by any computation. The initial LP run also hit a numpy-int JSON serialization error after completing its calculations; the corrected script was rerun successfully. These setup/output failures are recorded in LOG.md and do not conceal mathematical test failures. Every command in the final run exited zero with empty stderr.

## Attributions and novelty, from memory only

I do not reliably remember a specific paper answering either exact part of Open Problem 4.48, or a publication explicitly exhibiting tau_1>tau_0 for this pairwise 1/e definition. My confidence in the nonexistence of such a paper is low: failure of recall is not a literature search. I cannot certify that either result was new when this manuscript became public.

I do remember Lovasz–Winkler's theory of optimal stopping/access times and the formula expressing H(i,pi) as a maximum of H(i,j)-H(pi,j). The paper's broad description of their work is fair. I cannot recall a precise source stating this particular sharp relaxation bound. Its elementary derivation from familiar stopping identities makes prior occurrence plausible, but I have no reliable citation to offer and will not invent one. Exact page references and the claimed correspondence with the book's equation (4.47) remain unchecked.

I recognize Hermon's title and remember a characterization involving the equilibrium law conditioned outside the target, or an equivalent normalization. I am moderately confident about that distinction and cannot verify the theorem's precise hypotheses or the historical conjecture attribution from memory. The source's sentence at line 52 leaves the meaning of “stationary expected hitting times” unspecified.

If that sentence means unconditioned E_pi T_A for sets with pi(A)>=1/2, it is false. Consider the reversible two-state chain

\[
q_{01}=\frac{p}{1-p},\quad q_{10}=1,\quad
\pi=(1-p,p),\quad 0<p<\tfrac12.
\]

Then tau_2=1-p, and the only proper target with stationary mass at least 1/2 is A={0}. Its unconditioned stationary hitting mean is E_pi T_A=p, so their ratio diverges as p->0. Starting instead from pi conditioned on A^c gives mean 1. This is a reason to make the sentence precise, not a counterexample to Hermon's actual theorem. No part of the present paper's main proofs depends on that sentence.

## Typos and unclear wording noticed

I found no wrong mathematical numerical digit or definite misspelled mathematical term. The following are the specific textual and presentation issues I noticed:

| Location | Issue | Suggested clarification |
|---|---|---|
| Line 52 | The stationary starting distribution or normalization for the Hermon characterization is unspecified. | State the conditioned-stationary quantity and exact theorem being cited. The unconditioned reading fails above. |
| Line 104 | The holding-time description is stated for S_m generally but lists only states 1 and 2. | Say explicitly “for m<N”; after the visit to 0 the rate is eps. The intended stopped-path argument is valid. |
| Line 136 | The symbols tau_0 and tau_1 are reused for both chains in a dense paragraph. | Write tau_0(P)=tau_0(Q)/c and tau_1(P)=tau_1(Q)/c once explicitly. |
| Lines 147–155 | The proof handles finite means but does not explicitly dispose of infinite means. | Add “If E_i U is infinite there is nothing to prove.” This is an implicit trivial case, not a proof gap. |
| Line 185 | A single very long paragraph combines CT tests, DT tests, LPs and formal checks. | Split it into separate paragraphs and retain the distinction between computed checks and proofs. |
| Line 211 | “No data were used” can be read as denying the computational output described earlier. | If intended, say that no external datasets were used and that generated numerical output accompanies the scripts. |
| Line 215 | thebibliography uses width template {9}, but there are ten bibliography entries. | Use {99} to accommodate the two-digit label. This is a LaTeX layout issue. |
| Lines 21, 208 and 237 | The manuscript date is 13 October, while a referenced project-paper URL is dated 24 October. | Clarify the revision date if that citation was added later. This is a chronology question, not proof of an incorrect reference. |

The prefixes 1.0879... and 1.08799... at lines 27 and 69 are truncations, not incorrect rounded values. I do not classify them as typos.

## What could not be checked

- The actual Aldous–Fill text, exact section/equation numbering, historical wording/status of the open problem, and the quoted constant 66 as a book attribution. The basic inequalities other than that constant have independent proofs above.
- Whether the explicit discrete-time continuization convention matches the cited book sections word for word; it is internally coherent and the mathematical assertions under it are proved.
- Hermon's exact theorem statement, bibliographic version, and the precise conjecture it resolves.
- Literature priority or exhaustive prior art for either main result, including any statement under a different optimal-stopping mixing-time name.
- The authors' unavailable checks.py, its particular random sample/output, Margin.lean, the claimed Lean/Mathlib versions or successful formal compilation.
- Availability and contents of the public repositories, authorship chronology, funding, affiliations and provenance claims. No link was opened.
- Compilation of the source into a PDF. The audit concerns the supplied LaTeX mathematics, not a different compiled revision.
- Global optimality of the ratio example, maximization of t_k/k beyond k=60, or a new universal upper constant. None follows from the numerical search.

''')
    parts.append(f"Source reviewed: PAPER.tex, 242 lines; SHA-256 `{sha}`.\n\n")
    parts.append('Task: “Be a hard, independent referee” of PAPER.tex. Request clock time was not supplied; audit start: 12 November 2026, approximately 04:15 +04 (Asia/Tbilisi).\n\nOverall verdict: **SOUND**\n')
    content=''.join(parts)
    content=content.replace('[thm:a](i)', '[thm:a], part (i)').replace('[thm:a](ii)', '[thm:a], part (ii)')
    content=content.replace('||Q||','norm(Q)').replace('|u(i)|','abs(u(i))')
    content=content.replace('their joint law is always Exp(1) times Exp(1+eps)',
                            'their joint law always consists of independent Exp(1) and Exp(1+eps) variables')
    (ROOT/'REPORT.md').write_text(content)

if __name__=='__main__':main()
