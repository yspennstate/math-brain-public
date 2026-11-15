#!/usr/bin/env python3
"""Assemble the local report from checked proofs and saved numerical results."""
import datetime,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1];D=ROOT/'data'
def read(name,default):
    p=D/name
    return json.loads(p.read_text()) if p.exists() else default
summary=read('summary.json',[]);fits=read('fits.json',[]);comparisons=read('budget_comparisons.json',[]);audit=read('audit_math.json',{})
finished=all((D/f'{mode}_complete.json').exists() for mode in ['small','large','deep','sa'])
text='''PARTIAL

# E0053: maximum and minimum bisections of random regular graphs

No proof or counterexample for any fixed d>=3 was established here. The literature search through 13 November 2026 did not find a printed resolution of the requested identity. The known rigorous small-degree bounds do not contradict it. The elementary cases d=0,1,2 are proved below, together with reductions and a first-moment bound. The numerical study supplies feasible cut witnesses and small-graph exact optima; its confidence intervals are sampling intervals, not guarantees about optimization error.

## Statement and source

For even n and fixed nonnegative integer d, let G be uniform on labeled simple d-regular graphs on n vertices. For S of size n/2, let cut_G(S) count the edges between S and its complement, and let MaxBis and MinBis be the maximum and minimum of cut_G(S) over those S. The question is whether

    [MaxBis(G)+MinBis(G)]/n = d/2 + o_p(1)

for every fixed d. Convergence in probability is the interpretation used here; the expected formulation is equivalent by the concentration proof below. No almost-sure coupling across n is asserted.

The downloaded [October 10, 2016 notes](sources/bandeira_notes.pdf), PDF page 117 (printed page 117), Section 8.6, state this formula as Conjecture 8.5 and ask for its proof or disproof as Open Problem 8.5. The [MIT problem extract](sources/bandeira_problem_8_5.pdf) agrees. In particular, the source uses maximum **bisection**, and the error tends to zero with **n at fixed d**. Its statement about Dembo–Montanari–Sen concerns a separate large-d error, not a fixed-d proof.

## Literature outcome

The original Zdeborová–Boettcher paper offers a cavity-method argument and extremal-optimization evidence. Dembo–Montanari–Sen, Theorem 1.5, proves the expansions

    MinBis/n = d/4 - P_* sqrt(d)/2 + o_d(sqrt(d)) + o_n(1),
    MaxBis/n = d/4 + P_* sqrt(d)/2 + o_d(sqrt(d)) + o_n(1),

with P_* approximately 0.7632. Adding them leaves an o_d(sqrt(d)) term; it need not vanish at d=3 or d=4.

Three later results need particular care:

- Gheissari–Perkins–Yap (2025), Corollary 1.2, proves a positive-temperature analogue for inverse temperature below reconstruction. Its parameter range is bounded and does not reach the zero-temperature optima.
- Aronow–Lopatto (2026), Theorem 1.1, states E MaxCut - E MaxBis=o(n). This is a different conjecture and does not compare MinBis with either maximum. Its full proof has not been independently checked here, and no conclusion below depends on it.
- Csóka–Fekete–Nagy–Szemerédi (2025), Conjecture 1.1, still formulates the cut/bisection identity as a conjecture. Their Section 3.1 even records an opposing intuition that the sum could be smaller than the edge count, but gives no counterexample. Lichev–Mitsche's November 2026 revision explicitly says its cubic bounds do not settle this relation.

Thus RESOLVED_IN_LITERATURE is not justified by the sources inspected. A literature search cannot certify the absence of every possible later result. Exact references, versions, links and relevance are given below; source downloads and SHA-256 hashes are in [sources/manifest.json](sources/manifest.json).

## Rigorous small-degree bound comparison

All numbers in this section count edges **per vertex** unless explicitly stated otherwise. Bounds are asymptotic with high probability; an arbitrarily small slack may be added. The following conservative bounds are sufficient for the contradiction check:

| d | lower MinBis/n | upper MinBis/n | lower MaxBis/n | upper MaxBis/n | resulting interval for the sum/n | target |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 0.103295 | 0.139822 | 1.3377398280 | 1.385802 | [1.4410348280, 1.525624] | 1.5 |
| 4 | alpha_4 = 0.2200557289... | 1/3 | 5/3 | 1.735804 | [1.8867223955..., 2.0691373334...] | 2 |
| 5 | alpha_5 = 0.3652560085... | 0.496488 | 1.9879180882... | 2.086595 | [2.3531740967..., 2.583083] | 2.5 |

Cubic minimum bounds are Lichev–Mitsche, Theorem 1.1. Quartic minimum upper and maximum lower bounds follow from Lyons, Theorem 4.1 (also earlier algorithmic work). The other maximum-bisection lower bounds in the table use the same theorem. Alpha_d is the exact entropy root proved below. The degree-five minimum upper bound is Csóka et al., Theorem 1.2.

Maximum upper bounds use MaxBis<=MaxCut and Harangi, Theorem 1.2. His normalization is by **total edges**, m=dn/2. I independently substituted his printed Table 2 parameters into the formula with outward interval arithmetic, obtaining the edge fractions

    d=3: 0.9238674766043736381...
    d=4: 0.8679013142663060437...
    d=5: 0.8346377978544107843...

Multiplying the relaxed upper fractions 0.923868, 0.867902, 0.834638 by d/2 gives the table. This avoids treating truncated printed decimals as rigorous upper bounds. The enclosing intervals and parameter choices are saved in [data/harangi_intervals.json](data/harangi_intervals.json); [code/harangi_interval.py](code/harangi_interval.py) reproduces them. The analytic guarantee is Harangi's theorem; this calculation audits the numerical substitutions, not the theorem's full proof.

Neither the upper-bound sums fall below the target nor the lower-bound sums exceed it. For example, combining the cubic n/6 minimum upper bound with 1.385802n gives 1.5524687n, also above 1.5n. An upper bound on MinBis cannot be added to a lower bound on MaxBis to obtain an upper bound on their sum. Gamarnik–Li's 1.36000...n lower bound is for MaxCut; transporting it to MaxBis would require an additional result such as the 2026 theorem. Even that stronger lower bound, added to 0.103295n, remains below 1.5n.

A source discrepancy was checked visually: Díaz–Do–Serna–Wormald's abstract reports cubic 1.32697, while Theorem 3 of the downloaded author manuscript states 1.32595. Its Theorem 4 prints a universally quantified lower bound 5n/3+epsilon*n, which cannot hold for arbitrary epsilon as written. See [the saved page](sources/diaz_author_page3.png). I use Lyons's independent, unambiguous bounds for the comparisons above; I do not silently turn either discrepancy into a new theorem. The original minimum-bisection Theorems 1/2 give 1/3+epsilon for d=4 and 0.17404 for d=3.

The arithmetic and inequality directions are recorded independently in [data/bounds_audit.json](data/bounds_audit.json).

## Rigorous partial results and proofs

'''
proof=(D/'PROOFS.md').read_text().split('\n',2)[2]
text+=proof+'\n\n## Numerical study\n\n'
text+=('All planned batches have finished.\n\n' if finished else 'The numerical batches are still being saved; the tables below are a progress snapshot. No final numerical conclusion is claimed in this version.\n\n')
text+='''The sampler shuffles dn labeled half-edges and rejects the entire pairing whenever a loop or repeated edge occurs. Each simple labeled graph has exactly (d!)^n pairings, so this is exactly uniform sampling conditioned on simplicity, rather than an approximately uniform rewiring chain. Distinct graph seeds are saved. Edges, sampler attempts, all restarts and the balanced spin witnesses are retained in data/.

For n=12,16,20,24, all bisections modulo complementation were enumerated: 12 graphs per degree and size, 144 graphs altogether. Fixing vertex 0 on one side leaves exactly binom(n-1,n/2) partitions. A separately formulated binary ILP using HiGHS agrees on 12 of these graphs. Both optima were also solver-certified on 12 graphs at n=32 and six at n=48. All 162 small graphs' heuristic witnesses attained both certified optima. ILP status, objective bounds and gap are stored, rather than labeling an uncertified incumbent exact.

The larger search uses tau-extremal optimization with tau alternating between 1.2 and 1.3. The fitness is the negative number of unsatisfied incident edges: crossing edges for minimization, uncut edges for maximization. Bucket selection uses a rank law proportional to rank^(-tau), with uniform selection inside each sign/fitness bucket. Single-spin updates allow at most a two-vertex side-size difference; only perfectly balanced states can set a record. Each run ends with a complete improving exchange search over opposite-side vertex pairs. Python independently recomputes each saved crossing count and checks balance and parity.

The main batch contains 306 graphs and uses four independent restarts per objective, 2000 sweeps/restart through n=2048 and 1000 for larger sizes. The deeper batch uses 12 restarts of 6000 sweeps through n=1024 (four graphs per degree/size) and eight restarts of 4000 sweeps at n=2048,4096 (three graphs per degree/size). Pooled values retain the best witnesses across main and deep runs on these matched graphs. These pooled summaries are kept separate from the larger, uniform-budget main sample. The separate simulated-annealing check uses four restarts of 2000 sweeps on three graphs per degree/size at n=128,512,2048,8192. Its implementation uses uniformly chosen opposite-side exchanges (Kawasaki dynamics), geometrically cools T from 2 to 0.04 every 400 sweeps, and uses the same final exchange quench. Its purpose is a method check, not an assertion that annealing is exact.

Each endpoint mean has an approximate two-sided Student-t 95% interval across independent graphs. If the observed variance is zero, the interval is marked unestimable; identical observations do not establish zero population variance. The sum uses the paired per-graph difference Delta=(best_min+best_max)/n-d/2, preserving covariance. These intervals describe random-graph sampling of **algorithm outputs**. Min witnesses are upper bounds on the true minimum and max witnesses are lower bounds on the true maximum; their errors enter Delta with opposite signs. Consequently, cancellation can make an inaccurate pair of endpoints appear to satisfy the conjecture.

'''
def ci_fmt(x):return 'not estimable' if x is None else f'{x:.6f}'
text+='| batch | d | n | graphs | MinBis/n estimate | MaxBis/n estimate | Delta |\n|---|---:|---:|---:|---:|---:|---:|\n'
for r in summary:
    if r['mode']=='large' and r['n'] in [128,512,2048,8192,32768]:
        text+=f"| {r['mode']} | {r['d']} | {r['n']} | {r['samples']} | {r['min_mean']:.6f} ± {ci_fmt(r['min_ci95_half'])} | {r['max_mean']:.6f} ± {ci_fmt(r['max_ci95_half'])} | {r['delta_mean']:+.6f} ± {ci_fmt(r['delta_ci95_half'])} |\n"
text+='\nAll sizes, small exact-graph means and follow-up batches are in [data/NUMERICS.md](data/NUMERICS.md). The plot also shows MinBis/n beside d/2-MaxBis/n so that cancellation is visible.\n\n![Heuristic densities and paired residuals](data/bisections.png)\n\n'
text+='''### Finite-size extrapolation and optimization uncertainty

For each degree I fit the two endpoint means and paired Delta to c+a*n^(-p) for p in {1/2,2/3,0.85,1}, and also c+a*n^(-2/3)+b/n. Fits are repeated after dropping sizes below 128,256,512 or 1024 when enough sizes remain. Additional window fits cap the largest included size at 1024,2048 or 4096, so that fixed-budget degradation at larger n is visible. Within-size paired bootstrap resampling gives conditional 95% sampling intervals for the intercepts. Weight floors prevent a zero observed variance from implying certainty. These are sensitivity calculations, not a proved scaling ansatz. Model spread and search-budget changes must be compared with any apparent nonzero intercept. All fits, chi-square diagnostics and bootstrap intervals are saved in data/fits.json.

'''
selected=[r for r in fits if r['mode'] in ['large','pooled'] and r['metric']=='delta' and r['nmin']==256 and len(r['powers'])==1]
if selected:
    text+='| batch | d | power p | fitted limiting Delta | bootstrap 95% sampling interval | chi-square / dof |\n|---|---:|---:|---:|---:|---:|\n'
    for r in selected:
        text+=f"| {r['mode']} | {r['d']} | {r['powers'][0]:.6g} | {r['limit']:+.6f} | [{r['bootstrap95_low']:+.6f}, {r['bootstrap95_high']:+.6f}] | {r['chi2']:.2f}/{r['dof']} |\n"
endpoint_fits=[r for r in fits if r['mode'] in ['large','pooled'] and r['metric'] in ['min','max'] and r['nmin']==256 and r['powers']==[2/3]]
if endpoint_fits:
    text+='\nEndpoint extrapolations for p=2/3, n>=256 (algorithm outputs; systematic optimization error excluded):\n\n| batch | d | endpoint | fitted density | bootstrap 95% sampling interval | chi-square / dof |\n|---|---:|---|---:|---:|---:|\n'
    for r in endpoint_fits:
        text+=f"| {r['mode']} | {r['d']} | {r['metric']} | {r['limit']:.6f} | [{r['bootstrap95_low']:.6f}, {r['bootstrap95_high']:.6f}] | {r['chi2']:.2f}/{r['dof']} |\n"
    text+='\nThe large chi-square values for the main endpoint fits diagnose the fixed-budget upturn in the plot. They make these endpoint intercepts unsuitable as calibrated estimates of the true optimum densities. Different metrics use their own sampling weights, so their separate fitted intercepts need not add exactly to the directly fitted paired sum.\n'
if comparisons:
    text+='\nMatched-graph follow-up comparisons (best over main plus the indicated follow-up versus main alone; positive endpoint improvement means a better feasible cut):\n\n| batch | d | n | graphs | decrease in min estimate | increase in max estimate | change in Delta |\n|---|---:|---:|---:|---:|---:|---:|\n'
    for r in comparisons:
        if r['n'] in [512,1024,2048,4096,8192]:text+=f"| {r['mode']} | {r['d']} | {r['n']} | {r['samples']} | {r['mean_min_improvement']:+.6f} | {r['mean_max_improvement']:+.6f} | {r['mean_delta_shift']:+.6f} |\n"
text+='''
The main cubic p=2/3 paired fit is approximately -0.000388, with conditional bootstrap interval [-0.000731,-0.000100]. The corresponding main d=4 and d=5 intervals include zero. The pooled deeper cubic fit includes zero. The pooled deeper d=5 fit over n>=256 instead gives +0.003334 with interval [+0.001676,+0.004928]; dropping n=256 changes it to +0.001712 with interval [-0.000380,+0.003747]. Thus the apparent sign/significance depends on the search budget and size window.

At n=4096, adding the deeper cubic runs decreases the minimum estimate by 0.001953 and increases the maximum estimate by 0.000814 on matched graphs, shifting their paired sum by -0.001139. This observed budget effect exceeds the magnitude of the main cubic fitted residual. The remaining gap to either true optimum is unknown. The numerics therefore do not establish a nonzero limiting deviation of the true-optimum sum beyond total uncertainty.

A nonzero residual outside a sampling interval would still not refute the conjecture: finite-size terms and optimization bias remain. The current methods do not supply a rigorous or calibrated narrow error interval for the infinite-n **true-optimum** sum. No numerical counterexample is claimed.

## Reproduction, resource use and audit

All work is local. There were no subagents, pushes, commits, deployments or publication. The process inherited nice=15 (more yielding than nice=10); the sandbox refuses priority changes, so that setting was retained. The C++ optimizer is single-threaded. Python sets BLAS/OpenMP/HiGHS thread limits to one. A governor-aware runner stops its own child on detecting distress and restricts it to a 20% wall-clock run allowance in throttle/owner-present mode. Main runs are sequential. Recorded resident memory is far below 4 GB.

From this directory:

```sh
clang++ -O3 -std=c++17 code/archive/bisection_initial.cpp -o code/bisection_initial
clang++ -O3 -std=c++17 code/bisection.cpp -o code/bisection
clang++ -O3 -std=c++17 code/bisection_fast.cpp -o code/bisection_fast
python3 code/experiments.py small
python3 code/experiments.py large
python3 code/experiments.py deep
python3 code/experiments.py sa
python3 code/bounds.py
python3 code/harangi_interval.py
python3 code/audit_math.py
python3 code/analyze.py
python3 code/write_report.py
```

The runner requires inherited nice>=10; launch it through nice -n 10 if needed and permitted. On this session it already inherits 15. Python packages used are NumPy, SciPy/HiGHS, mpmath, matplotlib and pypdf (the latter only for source extraction); installed versions are recorded in data/environment.json. Follow-ups use code/bisection_fast.cpp, which integrates the same rank law over buckets and was checked against the original for identical-seed witness equality. The small batch's initial source snapshot is preserved in code/archive/bisection_initial.cpp; every experiment row records its source SHA-256. A source hash identifies an implementation, not an optimality certificate.

'''
if audit:text+=f"The final finite check record currently covers {audit.get('recorded_experiments_checked',0)} experiment records and {audit.get('witnesses_checked',0)} witnesses, including {audit.get('graphs_with_both_optima_certified',0)} graphs with both optima certified. See [data/audit_math.json](data/audit_math.json) and the [final audit](data/final_audit.json).\n\n"
text+='## References and search coverage\n\n'+(ROOT/'sources/LITERATURE.md').read_text().split('\n',2)[2]
text+='\n\nTask: “Open problem E0053” — received 13 November 2026, 05:17 +04 (Asia/Tbilisi).\n'
(ROOT/'REPORT.md').write_text(text)
print('Wrote REPORT.md; final batches complete:',finished)
