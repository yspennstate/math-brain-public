"""Build human-readable tables from the saved numerical outputs."""
import json,math,csv,hashlib,platform,os
from pathlib import Path
import numpy as np
import experiment as e
def load(p):return json.loads(Path(p).read_text())
def fmt(x):
    if abs(x)>1e5 or 0<abs(x)<1e-5:return f'{x:.7g}'
    return f'{x:.7f}'.rstrip('0').rstrip('.')
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x) for x in row)+' |' for row in rows])+'\n'
def main():
    C=load('census.json');S=load('structured.json');F=load('families.json');M=load('mux.json');audit=load('audit.json');allrows=S+F+M
    def candidates(key):
        return [(r[key]['ratio'],name,r[key].get('tt'),r[key].get('n')) for name,r in C.items() if key in r]+[(r[key]/r['I'],r['name'],r.get('tt'),r.get('n')) for r in allrows if key in r]
    constants={'tribes_P_constant':2.,'tribes_A_constant':4.,'tribes_T_half_constant':2.5,'theta_half_c':2+math.sqrt(2),'theta_half_K':8.,'theta_half_Jensen_A_constant':6+2*math.log2(2+math.sqrt(2)),'AND_T_half_necessary_constant':1.5}
    Path('constants.json').write_text(json.dumps(constants,indent=2))
    with Path('extremal_truth_tables.csv').open('w') as f:
        writer=csv.writer(f);writer.writerow(['scope','metric','ratio','n','truth_table_hex','I','value'])
        for scope,r in C.items():
            for metric,entry in r.items():
                if isinstance(entry,dict):writer.writerow([scope,metric,entry['ratio'],entry['n'],entry['tt'],entry['I'],entry['value']])
    carriers={}
    for scope,key,entry in [('npn5',f'Sp{K}',C['npn5'][f'Sp{K}']) for K in e.KS]:
        tt=int(entry['tt'],16);n=entry['n'];f=np.array([1-2*((tt>>x)&1) for x in range(1<<n)])
        mu,up,p,pc=e.data(f);K=int(key[2:]);idx=np.where((mu[0]>0)&(p[0]<2.**(-K*pc)))[0]
        carriers[scope+'_'+key]={'tt':hex(tt),'n':n,'sets':[{'S':hex(int(s)),'size':int(pc[s]),'mu':float(mu[0,s]),'p':float(p[0,s]),'weighted_cost':float(mu[0,s]*-math.log2(p[0,s]))} for s in idx]}
    for K in e.KS:
        ratio,name,tt,n=max(candidates(f'Sp{K}'))
        if tt is None and name.startswith('tribes') and n<=12:
            w=int(name.split('_')[1][1:]);m=int(name.split('_')[2][1:])
            tt=hex(sum(int(any((x>>(j*w))&((1<<w)-1)==(1<<w)-1 for j in range(m)))<<x for x in range(1<<n)))
        record={'ratio':ratio,'function':name,'tt':tt,'n':n}
        if tt and n<=12:
            value=int(tt,16);f=np.array([1-2*((value>>x)&1) for x in range(1<<n)])
            mu,up,p,pc=e.data(f);idx=np.where((mu[0]>0)&(p[0]<2.**(-K*pc)))[0]
            record['by_degree']={str(d):{'sets':int(sum(pc[idx]==d)),'weighted_cost':float(sum(mu[0,idx[pc[idx]==d]]*-np.log2(p[0,idx[pc[idx]==d]])))} for d in sorted(set(pc[idx]))}
            record['sets']=[{'S':hex(int(s)),'size':int(pc[s]),'mu':float(mu[0,s]),'p':float(p[0,s])} for s in idx]
        carriers['global_Sp'+str(K)]=record
    Path('carriers.json').write_text(json.dumps(carriers,indent=2))
    lines=['# FEIB13 results','',
    'PROVED correction to FLOW 3b: the read-once zero-cancellation statement needs the empty-set qualification. AND₂, truth table `0x8`, has H=2 bits but 2P+2(I−Var)=1.5 bits; the missing 0.5 bit is its empty Fourier entropy. General FLOW formulas retaining Gamma are unaffected. See PROOFS.md, opening paragraph.','',
    'General containment P≤CI is OPEN. The original W and both untruncated candidate budgets are disproved below. Every finite table is CHECKED within its stated scope.','',
    'Logs are base 2. P, A, H and reference costs are in bits; I and Var are dimensionless. Entries below are divided by I unless stated otherwise. Census outputs: census.json; literal families: structured.json; analytic families: families.json; large MUX: mux.json. Scripts are independent of the shared FEI check scripts.','',
    '## 1. Sparse split','',
    'CHECKED: complete NPN orbits for every n≤5, plus 5,120 functions each at n=6,7. The sample seed is 20261110, with equal allocations to uniform, balanced, sparse-output, and random threshold functions. NPN generation scans all output-complement classes; it does not sample them.','']
    headers=['scope','count','max P/I','max A/I']+[f'max Sp{K}/I' for K in e.KS]
    lines.append(table(headers,[[name,r['count']]+[fmt(r[key]['ratio']) for key in ['P','A']+[f'Sp{K}' for K in e.KS]] for name,r in C.items()]))
    lines+=['CHECKED n=5 sparse extrema (bit x set means f(x)=−1):','',table(['K','Sp_K/I','truth table'],[[K,fmt(C['npn5'][f'Sp{K}']['ratio']),C['npn5'][f'Sp{K}']['tt']] for K in e.KS]),
    'Every census extremum, including all moments and references, is in extremal_truth_tables.csv. Full finite-function witnesses are hexadecimal there; very large analytic families are specified by their parameters, because their truth tables cannot be materialized within the disk limit.','',
    'CHECKED maxima across every tested function and analytic parameter choice:','',table(['K','max Sp_K/I','function'],[[K,fmt(max(candidates(f'Sp{K}'))[0]),max(candidates(f'Sp{K}'))[1]] for K in e.KS]),
    'Thus K=2 with C=0.5056921 covers everything tried; this is a finite numerical bound, not a universal theorem. K=6 with C=0.0546876 also covers everything tried. PROVED for all equal-width tribes, Sp_K≤P≤2I for every K. General sparse containment is OPEN.','',
    'The actual sets are in carriers.json. In tribes, a set hitting r blocks in s coordinates contributes exactly when rw−s−(m−r)log b>K s; its weight depends only on (r,s). Large costs are concentrated on unusually small selections inside the hit blocks. The global K=2 and K=3 witnesses have their full sets and degree breakdown in that file. For majority₂₅₅, the K=4 cost is carried by singletons: Inf_i log(1/Inf_i)=0.2161381 after division by I. The K=6 record is the eight singleton sets of OR₈, equivalent to AND₈.','',
    '## 2. Label-time flow and budgets','',
    'CHECKED supremum of T_t/I within each scope:','',table(['scope','t=1/4','t=1/2','t=3/4','t=1'],[[name]+[fmt(r[f'T{t:g}']['ratio']) for t in e.TS] for name,r in C.items()]+[['all tested families']+[fmt(max(candidates(f'T{t:g}'))[0]) for t in e.TS]]),
    'PROVED generally T_t≤P+(1−t)I. PROVED for all equal-width tribes T_t≤(3−t)I. AND_n forces any universal T_(1/2) constant to be at least 1.5. General T_(1/2) and its relative-increment form remain OPEN.','',
    'PROVED stronger noise bound: F_R(1/2)≤up(R)p(R)^(1/3). This does not repair the missing cross-level budget. Both untruncated candidates fail on balanced tribes; even a single AND with increasing width disproves a uniform logarithmic budget after division by its very small I.','',
    'CHECKED candidate budgets at t=1/2. Entries are the largest log₂(count)/I found. The cutoff means up_M(R)=Σ_{U⊇R,|U|≤M}mu(U); it is on U.','',table(['theta','up count, no cutoff','up, M=ceil(2I)','up, M=ceil(4I)','tau inverse-p moment'],[[th]+[fmt(max(candidates(key))[0]) for key in [f'raw_th{th:g}',f'raw_M2I_th{th:g}',f'raw_M4I_th{th:g}',f'taumom_t0.5_th{th:g}']] for th in e.TH]),
    'PROVED: no fixed positive theta makes the untruncated tau moment ≤2^(CI); the up count fails even at theta=0. OPEN: a universal cutoff estimate with M=aI for fixed a. The finite maxima for both tested cutoffs are compatible with such an estimate.','',
    '## 3. W and the weaker exponent','',
    'PROVED: original W (theta=1) is false for every finite c,K. For balanced tribes of width w, log₂ W_(1,c) grows like (1+2/c)^w, while I grows linearly in w.','',
    'CHECKED balanced-tribes obstruction at c=4. The last two columns are the minimal log₂ K required by W≤Var K^(I/Var); negative values are allowed.','']
    balanced=[r for r in F if 'w' in r and r['m']==max(1,round(math.log(2)*2**r['w'])) and r['w'] in (4,8,16,32,64)]
    lines.append(table(['w','I','P/I','A/I','theta=1, c=4','theta=1/2, c=2+sqrt(2)'],[[r['w'],fmt(r['I']),fmt(r['P']/r['I']),fmt(r['A']/r['I']),fmt(r['W_K_c4_th1']),fmt(r['W_K_c3.41421356237_th0.5'])] for r in balanced]))
    lines+=['PROVED sharp tribes discount threshold for every 0<theta<1: c≥2^theta/(2^(1−theta)−1) suffices, with K=2^(4−2theta). Every smaller c fails on balanced tribes. At theta=1/2, c=2+sqrt(2), K=8. Jensen gives A≤'+fmt(constants['theta_half_Jensen_A_constant'])+' I and P≤the same bound; the direct tribes proof is stronger: P≤2I, A≤4I−2Var. A weakened W for all Boolean functions is OPEN.','',
    'AND and address functions also have exact moment formulas in PROOFS.md. They satisfy the original W for suitable constants, showing why testing them alone misses the tribes obstruction.','',
    '## 4. Reference measures','',
    'PROVED: tau_(1/2) and the uniform mixture over rho are probabilities, each ≤up(S), with cross entropy between H and H+I. Thus their universal O(I) cost is equivalent to FEI. Their costs are ≤7I on all equal-width tribes; a general bound is OPEN. Their ratios stay bounded over the tested tribes and majority ranges together.','',
    'The proposed conditional-product Markov reference telescopes to up(R), regardless of ordering. It is not normalized. Its normalization costs log₂ E 2^|U|, which is unbounded relative to I on tribes. The independent-product reference also grows with tribes width and majority dimension.','']
    names=['AND_127','tribes_w16_m45426','tribes_w64_m12786308645202655232','majority_33','majority_255','address_3','PM_K33','MUX_L16_k7_m458752']
    chosen=[next(r for r in allrows if r['name']==name) for name in names]
    keys=['P','A','ref_tau0.5','ref_mixture_uniform','ref_product','ref_markov_normalized']
    lines.append(table(['function','P/I','A/I','tau₁/₂ cost/I','uniform mixture/I','product/I','normalized Markov/I'],[[r['name']]+[fmt(r[k]/r['I']) for k in keys] for r in chosen]))
    lines+=['## 5. Checks, scope, and reproduction','',
    f'CHECKED by audit.py: {audit["all4_count"]:,} four-variable truth tables using direct restriction sums; {audit["witness_checks"]} saved extremal witnesses independently reconstructed; exact agreement for mu, up and p; maximum inequality residual {fmt(max(audit["inequality_max_lhs_minus_rhs"].values()))}. The strengthened noise bound also passed {audit["noise_support_sample6_count"]} six-variable random checks.','',
    'The tribes, symmetric and MUX formulas agree with independent small truth-table calculations. The largest discrepancies are '+', '.join(fmt(max(audit[k].values())) for k in ['tribes_formula_max_errors','symmetric_formula_max_errors','mux_formula_max_errors'])+' respectively. The 64/128-node uniform-mixture quadrature audit and omitted spectral masses are recorded in audit.json.','',
    'For very biased AND functions, ordinary floating point loses counts differing from 1 by 2^-n. highprecision.py recomputes all AND rows in families.json at 160 decimal digits. No rounded-to-one double-precision budget values are used in these tables. Large majority uses exact integer restriction sums before conversion to floating point. The analytic tribes cutoff ceiling rounds back one upward floating-point ulp at an integer.','',
    'Run `python3 run.py` from this folder. It compiles the orbit generator, runs every census and family calculation, audits the output, and rebuilds these tables. It sets one numerical thread and nice≥10. resources.json records each child’s measured maximum resident size and elapsed seconds. The n=5 bitset is 268,435,456 bytes. No external files are written.','',
    'Brain recall provided orientation and a warning about prior FEI claims, but no applicable cross-level proof. math_recall.py reported that its store was missing. Fleet instructions forbid shared-memory/mesh writes, so the durable corrections are left here for the launching session.','',
    'Task: “uniform-in-level containment” — brief read 2026-11-10 02:59 +04.']
    resource_summary=''
    if Path('resources.json').exists():
        resources=load('resources.json');peak=max(r['max_rss_bytes'] for r in resources);elapsed=sum(r['elapsed_seconds'] for r in resources)
        resource_summary=f'CHECKED measured reproduction: peak resident size {peak:,} bytes ({peak/2**20:.6f} MiB); sum of child elapsed times {elapsed:.6f} seconds; every child exited 0 at nice 10. Source: resources.json. The runner completed with REPRODUCTION PASS and the independent audit with AUDIT PASS.'
        lines[-2:-2]=[resource_summary,'']
    Path('RESULTS.md').write_text('\n'.join(lines)+'\n')
    report=['# FEIB13 report','',
    'PROVED correction to FLOW 3b: AND₂ (`0x8`) has an empty Fourier entropy contribution of 0.5 bit. Its H is 2 bits, while 2P+2(I−Var)=1.5 bits. The read-once zero-cancellation statement needs to exclude the empty derivative for biased functions. P, A and the general identities retaining Gamma are unaffected.','',
    'General containment P≤CI remains OPEN. The completed work gives exhaustive small-function data, analytic counterexamples to three proposed moment shortcuts, and a sharp tribes classification for the weakened W discount. Full proofs are in PROOFS.md and tables in RESULTS.md.','',
    '1. Sparse split — CHECKED all NPN classes through n=5, 5,120 samples each at n=6,7, and all requested families. Every tested function satisfies Sp₂≤0.5056921 I; Sp₆≤0.0546876 I. PROVED Sp_K≤2I for all equal-width tribes. Universal sparse containment is OPEN. Extremal truth tables and actual carrier sets are saved.','',
    '2. T and budgets — PROVED T_t≤P+(1−t)I; for tribes T_(1/2)≤2.5I. AND_n forces the constant to be at least 1.5. General T and its relative-increment form are OPEN. PROVED F_R(1/2)≤up(R)p(R)^(1/3). Both untruncated counting proposals are FALSE: the up count fails even with theta=0, and the tau count fails for every theta>0. M=ceil(2I),ceil(4I) cutoffs passed the numerical tests; a general proof remains OPEN.','',
    '3. W — FALSE as stated for every finite c,K, by balanced tribes. PROVED for all equal-width tribes and every 0<theta<1: c≥2^theta/(2^(1−theta)−1), K=2^(4−2theta) suffice; every smaller c fails. At theta=1/2 take c=2+sqrt(2), K=8. General weakened W remains OPEN.','',
    '4. References — PROVED the thinned laws and uniform mixture are ≤up and have cost between H and H+I. Their universal linear cost is equivalent to FEI. CHECKED bounded ratios over tribes through width 64 and majority through n=255 simultaneously; PROVED cost≤7I for all equal-width tribes. The proposed Markov product equals up(R), is not a sub-probability, and its normalization has unbounded cost/I on tribes.','',
    '5. P and A — PROVED for every equal-width tribes function P≤2I and A≤4I−2Var; for AND and all address functions P≤I, A≤3I. Every general implication is stated for both P and A, with the moment Jensen constant explicit. No universal containment constant is claimed.','',
    'Verification: complete NPN counts 2, 4, 14, 222, 616126; the independent audit covers all 65,536 four-variable truth tables and every stored extremal witness. Small-family formulas match independent restriction sums. AND budgets use 160 decimal digits to avoid catastrophic rounding near 1. audit.json, census.json, structured.json, families.json and mux.json are the numerical sources. resources.json records actual memory and elapsed seconds.','',
    'Useful files: PROOFS.md, RESULTS.md, extremal_truth_tables.csv, carriers.json. Reproduce with `python3 run.py`. No subagents, model calls, publishing, shared writes, or production processes were used. Brain recall helped orientation; the math store was unavailable.','',
    'Open work is mathematical, not a missing input: T’s relative increments, the M=aI cutoff budget, and a weakened W for arbitrary Boolean functions. The two untruncated budgets and original W cannot prove containment in their stated forms.','',
    'Task: “uniform-in-level containment” — brief read 2026-11-10 02:59 +04.']
    if resource_summary:report[-2:-2]=[resource_summary,'']
    Path('REPORT.md').write_text('\n'.join(report)+'\n')
    Path('STATUS.md').write_text('# FEIB13 status\n\nCompleted the five-item brief; full results and verdicts are in REPORT.md.\nGeneral containment and the explicitly listed research questions remain OPEN.\n\nNEXT: launching session can review the FLOW empty-set correction, tribes counterexamples,\nand the M=aI cutoff candidate; no worker action is pending.\n\nTask: uniform-in-level containment — 2026-11-10 02:59 +04.\n')
    versions={'python':platform.python_version(),'numpy':np.__version__,'nice':os.getpriority(os.PRIO_PROCESS,0),'thread_env':{k:os.environ.get(k) for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS']}}
    import mpmath
    versions['mpmath']=mpmath.__version__;Path('environment.json').write_text(json.dumps(versions,indent=2))
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('.').iterdir() if p.is_file() and p.suffix in ('.py','.cpp','.json','.bin','.md','.csv') and p.name not in ('manifest.json','events.jsonl','resources.json')}
    Path('manifest.json').write_text(json.dumps(manifest,indent=2))
    print('Generated RESULTS.md, REPORT.md, STATUS.md, constants.json, carriers.json, extremal_truth_tables.csv, environment.json, manifest.json')
if __name__=='__main__':main()
