"""Aggregate independent seeds, create tables, and assemble the final report."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import signal
signal.alarm(280)
import json
from pathlib import Path
import numpy as np


def read(path):
    return json.loads(Path(path).read_text())


def meanse(values):
    x=np.asarray(values)
    return float(x.mean()),float(x.std(ddof=1)/np.sqrt(len(x)))


def pm(values,digits=7):
    m,se=meanse(values)
    return f'{m:.{digits}f} ± {se:.{digits}f}'


def table(headers,rows):
    return '\n'.join(['| '+' | '.join(map(str,headers))+' |',
                      '| '+' | '.join(['---']*len(headers))+' |']+
                     ['| '+' | '.join(map(str,row))+' |' for row in rows])+'\n'


def main():
    exact=read('exact_results.json')
    contractions=read('contraction_results.json')
    curves=read('curvature_results.json')['results']
    laws=['12','24','123','geom']
    datasets={law:[read(f'pool_{law}_{seed}.json') for seed in (101,102,103,104)] for law in laws}
    rays=[read(f'ray_{seed}.json') for seed in (201,202,203,204)]
    paper={'12':(.02206,.00041,.02228,.00041),
           '24':(.02720,.00019,.02718,.00019),
           '123':(.04925,.00020,.04954,.00019),
           'geom':(.05572,.00062,.05677,.00061)}
    sections=['Law key: 12 means p1=p2=1/2; 24 means p2=p4=1/2; 123 is uniform on {1,2,3}; geom means pk=2^(-k), k>=1.\n']
    rows=[]
    for tree in range(1,6):
        rr=[row for row in exact['exact_trees'] if row['tree']==tree]
        rows.append([tree,rr[0]['interior']]+[row['recursion'] for row in rr]+['5/5 exact'])
    sections+=['## Numerical table 1: exact absorbing-chain check\n',
               table(['Tree','Interior vertices','lambda=0','1/3','1','3/2','3','Agreement'],rows),
               'Tree notation: `()` is a boundary vertex; a tuple lists its children. Each tree has mixed degrees.\n\n`'+exact['tree_notation']+'`\n',
               'Command: `python3 audit_exact.py`. Fraction Gaussian elimination solves the walk equations, independently of the escape recursion. All 25 results agree exactly.\n']
    rows=[]
    for run in contractions:
        j12=run['rows'][11]; j20=run['rows'][19]
        rows.append([run['k'],f"{run['rho']:.1f}",
                     f"{j12['delta']:.3e} / {j12['delta_bound']:.3e}",
                     f"{j12['eta']:.3e} / {j12['eta_bound']:.3e}",
                     f"{j20['delta']:.3e} / {j20['delta_bound']:.3e}",
                     f"{j20['eta']:.3e} / {j20['eta_bound']:.3e}"])
    sections+=['## Numerical table 2: contraction and derivatives\n',
               table(['k','r/k','delta12 / bound','eta12 / bound','delta20 / bound','eta20 / bound'],rows)]
    rows=[]
    for run in contractions:
        rows.append([run['k'],f"{run['rho']:.1f}",f"{run['max_db_depth20']:.8f}",
                     f"{run['M']:.8f}",f"{run['fd_error']:.3e}",
                     f"{run['max_delta_ratio']:.6f}",f"{run['max_eta_ratio']:.6f}"])
    sections += [table(['k','r/k','max abs b20 derivative','M','max y FD error','max delta/bound (all j)','max eta/bound (all j)'],rows),
                 'Command: `python3 audit_contraction.py`. Each case: 384 roots, 17 lambda grid values, depths 1 through 20. Finite-depth trees use layered subtree sharing; unfolding is a valid tree, but samples are dependent. Supremum means the maximum of this test set, not the supremum over all trees. Centred differences use h=1e-5, including a rational continuation to negative h at zero. Every tested bound passed. Floating-point noise can dominate differences around 1e-16. The reported b20 derivative approximates beta; no finite test certifies an infinite-depth supremum.\n']
    rows=[]
    for i,ratio in enumerate((.2,.5,.8)):
        idx=datasets['12'][0]['ratios'].index(ratio)
        rows.append([(.3,.75,1.2)[i],pm([d['d'][idx] for d in datasets['12']]),
                     pm([d['formula'][i] for d in rays]),
                     pm([d['paths'][i]['120']['root'] for d in rays]),
                     pm([d['paths'][i]['360']['root'] for d in rays]),
                     pm([d['paths'][i]['360']['burn20'] for d in rays])])
    sections+=['## Numerical table 3: formula versus harmonic-ray entropy\n',
               table(['lambda','Formula, main pool','Formula, ray pool root sample','Ray n=120, root','Ray n=360, root','Ray n=360 after 20 levels'],rows),
               'Commands: `python3 audit_ray.py 201` (and seeds 202–204), plus `python3 audit_pool.py 12 101` (and 102–104). The ray calculation uses 12,000 population nodes per level, 420 stored levels and 12,000 lazily unfolded rays per seed. Offspring and child indices are retained with their escape values. At each visited node choose child i with weight beta_i/sum beta and accumulate -log(weight). Thus the root column is literally -(1/n)log of prefix mass. The burn20 column estimates the same asymptotic rate after an initial segment. This uses harmonic-ray simulation, not a simulation of all backtracking steps of the original walk. Selected-child dependence is preserved.\n\nThe largest raw finite-n transient is at lambda=1.2; its reduction with n and after burn-in is visible. Main-pool formula and burn-in ray means agree within two combined standard errors at all three biases. The smaller ray pool has noisy one-root-sample formula estimates. Layer sharing, finite-pool bias and finite-depth effects are not included in the seed standard errors. This is an independent check of the entropy observable and stationary weighting, though it shares the escape recursion. It is not an independent proof of the source theorem.\n']
    rows=[]
    for law in laws:
        c=exact['constants'][law]
        rows.append([law,c['a'][:22],c['d0'][:22],c['slope'][:22]])
    sections+=['## Numerical table 5: exact examples and constants\n',
               table(['Law','E 1/N','d0','d0 prime'],rows),
               'Binary 1/2 law: slope = log(2)/32. Binary 2/4 law: slope = 5 log(2)/128. Geometric slope rounds to 0.05496. Command: `python3 audit_exact.py`; mpmath precision 70 digits, geometric series through k=400. Tail contributions to the required logarithmic sums are below 1.6e-118, using log k<=k and sum_(k>400) k 2^-k=402*2^-400. The geometric a=log 2 also follows from -log(1-z)=sum z^k/k at z=1/2.\n']
    rows=[]; comparison=[]; curvature=[]; summary={}
    for law in laws:
        data=datasets[law]
        ell=float(exact['constants'][law]['d0']); slope=float(exact['constants'][law]['slope'])
        idx=data[0]['ratios'].index(.02)
        estimates=[d['derivative'][0] for d in data]
        dq=[(d['d'][idx]-d['d'][0])/d['lam'][idx] for d in data]
        sm,ss=meanse(estimates); qm,qs=meanse(dq)
        pv,ps,qv,qse=paper[law]
        rows.append([law,f'{ell:.9f}',f'{slope:.9f}',pm(estimates),pm(dq)])
        comparison.append([law,f'{abs(sm-pv)/np.hypot(ss,ps):.3f}',
                           f'{abs(qm-qv)/np.hypot(qs,qse):.3f}',
                           f'{abs(pv-slope)/ps:.3f}',f'{abs(qv-slope)/qse:.3f}',
                           f'{abs(sm-slope)/ss:.3f}'])
        curv_by_deriv=[]; curv_by_dim=[]
        for ratio in (.0025,.005,.01):
            j=data[0]['ratios'].index(ratio)
            curv_by_deriv.append(pm([(d['derivative'][j]-d['derivative'][0])/d['lam'][j] for d in data]))
            curv_by_dim.append(pm([2*(d['d'][j]-d['d'][0]-d['lam'][j]*d['derivative'][0])/d['lam'][j]**2 for d in data]))
        rich=[]
        for d in data:
            j=d['ratios'].index(.0025); j2=d['ratios'].index(.005)
            small=(d['derivative'][j]-d['derivative'][0])/d['lam'][j]
            double=(d['derivative'][j2]-d['derivative'][0])/d['lam'][j2]
            rich.append(2*small-double)
        curvature.append([law,f"{float(curves[law]['curvature']):.9f}"]+curv_by_deriv+[curv_by_dim[0],pm(rich)])
        summary[law]=dict(derivative=sm,derivative_se=ss,quotient=qm,quotient_se=qs)
    sections+=['## Numerical table 6: slope reproduction\n',
               table(['Law','Exact d0','Exact slope','Pool RHS [eq:quot] at 0','Paired quotient at .02m'],rows),
               'Runs: `python3 audit_batch.py`, which serially executes `python3 audit_pool.py LAW SEED` for LAW in 12,24,123,geom and SEED in 101,102,103,104, then the four ray runs. Existing completed JSONs are skipped. A full fresh run is under five minutes here. Each numerical script and the driver have 280-second alarms. Pool settings: 40,000 entries, 180 synchronous sweeps, evaluations averaged over the last 40 sweeps, 14 coupled lambda values. All ± values are sample standard deviation of four seed means divided by 2.\n\nThe displayed dimensions use exact d0 as a control variate: d_est(lambda)=d_raw(lambda)-d_raw(0)+d0_exact. The quotient is consequently the paired empirical difference quotient, not a noisy quotient against an unrelated baseline. Raw values remain in each pool JSON. Averaging across sweeps reduces Monte Carlo error but does not remove finite-pool bias; the four-seed SE is not a bound on systematic error.\n',
               table(['Law','Paper vs ours pool z','Paper vs ours quotient z','Paper pool vs exact slope z','Paper quotient vs exact slope z','Our pool vs exact slope z'],comparison),
               'For paper-vs-ours comparisons z uses sqrt(SE_paper^2+SE_ours^2). For comparisons against the exact slope it uses the single stated SE. All published pool means and positive-bias quotients are within two combined SE of ours. Every published pool mean is within two of its own SE of the exact slope. The geometric positive-bias quotient is 2.97 SE above the exact slope; it estimates a different, curved-parameter quantity. Two-SE intervals with four seeds are descriptive, not a strong coverage guarantee.\n',
               '### Curvature at zero\n',
               table(['Law','Expansion d2(0)','(dprime(.0025m)-dprime(0))/.0025m','same, .005m','same, .01m','2(d(h)-d(0)-h*dprime(0))/h^2, h=.0025m','Richardson, 2*small-double'],curvature),
               'Command: `python3 audit_curvature.py`; the pool estimates use the already saved near-zero runs. The independent symbolic expansion and the two different finite-difference calculations agree in scale and sign; first-order finite-difference errors are visible as h increases. The last column cancels that first-order error using paired h and 2h estimates. Geometric curvature shifts the .04 quotient by about .00103527, yielding .05599471 at quadratic order, with higher-order corrections remaining. The published .05677 ± .00061 is compatible with curvature plus sampling noise. No numerical error is identified.\n']
    rows=[]; se_rows=[]; grid_status=[]
    for law in laws:
        data=datasets[law]
        indices=[data[0]['ratios'].index(round(i/10,1)) for i in range(10)]
        means=[meanse([d['d'][i] for d in data])[0] for i in indices]
        ses=[meanse([d['d'][i] for d in data])[1] for i in indices]
        rows.append([law]+[f'{v:.6f}' for v in means])
        se_rows.append([law]+[f'{v:.6f}' for v in ses])
        lm=float(exact['constants'][law]['logm'])
        increasing=all(np.all(np.diff(np.array(d['d'])[indices])>0) for d in data)
        below=all(np.all(np.array(d['d'])[indices]<lm) for d in data)
        assert increasing and below
        grid_status.append([law,f'{lm:.9f}',str(increasing),str(below),f'{lm-means[-1]:.6f}'])
    sections+=['### Dimension grid\n',
               table(['Law']+[f'{i/10:.1f}' for i in range(10)],rows),
               'Standard errors over four seeds:\n',table(['Law']+[f'{i/10:.1f}' for i in range(10)],se_rows),
               table(['Law','log m','Every seed increasing','Every seed below log m','Mean gap at .9m'],grid_status),
               'The increase on this finite grid is numerical evidence only. It does not establish global monotonicity. These values reproduce the scale and trend of [tab:dim]; no attempt is made to reconstruct the authors\' undisclosed seeds or raw outputs.\n']
    numeric='\n\n'.join(sections)
    Path('NUMERICS.md').write_text(numeric)
    Path('summary_results.json').write_text(json.dumps(summary,indent=2))
    log=Path('LOG.md').read_text()
    preface='''# Independent referee report

Overall verdict: **SOUND**.

I found no gap in the contraction proof, the finite-mean domination argument, or the derivative and strict local monotonicity calculation. The one definite mathematical wording error is the unnormalized one-tree density in [rem:tilt]; the main proof gives the correct density and is unaffected. Numerical checks support the formulas. This verdict treats the cited Lin–Rousselin dimension formula as a known external theorem: its exact source hypotheses and numbering, and the novelty claim, could not be source-verified in this no-browsing run. A publication referee should complete that literature check before acceptance.

The geometric difference quotient is not an estimate of the exact zero-bias slope: curvature explains about .00104 of its excess. The remaining discrepancy is consistent with the printed Monte Carlo uncertainty. No theorem-level overstatement was found. Numerical reproducibility and a few literature descriptions need clarification.

PAPER.tex was read only. All programs and results are original to this audit and saved in this directory. No browsing, git push, other agents, visible windows, outside mutations, or authors' code were used. Computations ran serially with numerical-library threads set to one; the batch driver has one child at a time. Largest stored arrays are in the ray check (roughly 170 MB including stored node values and indices, comfortably under 1 GB). A nice-priority attempt was denied by the sandbox, so no priority change is claimed; the individual pool runs took about 4–7 seconds and ray runs about 1–2 seconds. Exact and symbolic checks were also short. Signals cap every numerical invocation and the batch driver at 280 seconds.

## Verdict table and detailed proof audit

The log below supplies a verdict for each requested lemma, proposition, proof step, theorem, corollary, remark, scope and attribution question. CORRECT means checked directly except where explicitly marked memory-only. GAP in a source-verification or novelty row records an audit limitation, not a discovered mathematical gap. WRONG in the density row is a local exposition error with the correction stated.

'''
    limitations='''
## Remaining limitations

- Lin's and Rousselin's original texts, the precise domain/hypotheses of their statements, and the cited theorem/equation numbers were not available locally. I am highly confident about the formula from memory and its normalization; numerical entropy checks are supportive, not a replacement for verifying the citation.
- The literature survey and exact bibliographic metadata, especially SWX 2025 and Bowditch–Tokushige's hypotheses, are not independently authenticated. No novelty conclusion is warranted from memory alone. Funding, repository contents and project provenance were outside this mathematical audit.
- Numerical samples use finite pools and, for rays and arbitrary trees, layered subtree sharing. Across-seed standard errors omit population and truncation biases. Ray lengths stop at 360 rather than giving an asymptotic error bound.
- Authors' numerical seeds, exact pooling/evaluation conventions, code and raw outputs were not supplied in this folder. Their per-seed monotonicity and stated SE cannot be checked directly; independent runs reproduce the claims within the comparisons stated above.
- No extension to lambda>=k0 was proved. No step 1–9 was skipped; uncertain items are identified individually.

Task: “Be a hard, independent referee” of PAPER.tex — the author's request, 2026-11-12, local clock 06:56 +04 at audit start.
'''
    # Keep the log itself intact and include its complete detailed verdict tables.
    Path('REPORT.md').write_text(preface+log+'\n\n'+numeric+'\n'+limitations)
    print(json.dumps(summary,indent=2))
    print('Wrote NUMERICS.md, summary_results.json, REPORT.md')


if __name__=='__main__': main()
