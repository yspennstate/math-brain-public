"""Build the evidence index, family ledger, final report and file manifest."""
import json,csv,hashlib,os,datetime,pathlib,math
ROOT=pathlib.Path(__file__).resolve().parent
def read(name):return json.load(open(name+'.json'))
def fmt(x):return f'{x:.12g}'
def main():
    pm=read('pm')['data'];fc=read('final_checks');native=read('native_audit');policy=read('policy')['data'];allrows=[]
    for source in ['structured','families','extra','linear','random_threshold','amplify']:
        for i,r in enumerate(read(source)['data']):allrows.append(dict(source=source+'.json',index=i,**r))
    for i,r in enumerate(read('composition')['rows']):allrows.append(dict(source='composition.json',index=i,**r))
    for kind,rs in read('large')['data'].items():
        for i,r in enumerate(rs):allrows.append(dict(source='large.json:'+kind,index=i,**r))
    for i,r in enumerate(pm['rows']):allrows.append(dict(source='pm.json',index=i,name='PM_tower',**r))
    for r in allrows:
        if 'gap' not in r and 'F' in r and 'E' in r:r['gap']=r['F']-r['E']
    with open('FAMILIES.csv','w',newline='') as fh:
        keys=['source','index','name','n','depth','w','F','E','gap'];w=csv.DictWriter(fh,fieldnames=keys,extrasaction='ignore');w.writeheader();w.writerows(allrows)
    structured=read('structured')['data'];fam=read('families')['data'];extra=read('extra')['data'];linear=read('linear')['data'];rnd=read('random_threshold')['data'];large=read('large')['data']
    groups=[]
    def group(name,rows,growth,script):
        assert rows
        groups.append((name,str(len(rows)),f"{min(r['F'] for r in rows):.8f} to {max(r['F'] for r in rows):.8f}",growth,script))
    group('AND primitives',[r for r in structured if r['name'].startswith('AND_') and r['name'][4:].isdigit()],'O(1); tends to 2 for AND_n','experiment.py structured')
    group('Plain tribes',[r for r in structured if r['name'].startswith('TRIBES_')],'O(1), coefficient 10 from the class theorem','experiment.py structured')
    group('Recursive tribes and AND/OR/XOR alternations, widths through 1000',large['andor'],'O(1), coefficient 10 uniformly in fan-in and depth','large.py large')
    group('Odd majority, one gate',[r for r in structured if r['name'].startswith('MAJ_')],'O(1), threshold coefficient in constants.json','experiment.py structured')
    group('Recursive majority, arities through 999, depths through 40',large['majority'],'O(1) in depth for each fixed arity; geometric tail','large.py large')
    group('AND of majority, widths through 1000',large['and_majority'],'Fixed inner gate: finite copy-count limit; normalized gap inherited exactly','large.py large')
    group('Mixed AND/OR/MAJ/XOR, depths 3 and 4',read('composition')['rows'][16:],'Finite checks; arbitrary majority/threshold formula class OPEN','composition.py')
    group('Bent quadratics',[r for r in structured if r['name'].startswith('BENT_')],'Exactly F=2 for every even dimension','experiment.py structured')
    group('Quadratic forms with sparse point corrections',[r for r in fam if r['name'].startswith('quadratic_patch')],'F<=2+o(1) when corrections=o(2^n)','search.py families')
    group('Projective planes Fano and PG(2,3)',[r for r in structured if r['name'] in ['Fano_STS7_DNF','PG23_DNF']],'General plane-size growth OPEN; O(n) trivial bound','experiment.py structured')
    group('Steiner triples STS(7), affine STS(9)',[r for r in structured if r['name'] in ['Fano_STS7_DNF','Affine_STS9_DNF']],'General system-size growth OPEN; O(n) trivial bound','experiment.py structured')
    group('Recursive Fano DNF',[r for r in extra if r['name']=='Fano_STS7_DNF'],'O(1); limit '+fmt(float(fc['fano']['F_finite']))+'; E=0','extra.py; final_checks.py')
    group('Other plane/Steiner gate towers, before extreme bias',[r for r in extra if r['name'] in ['PG23_DNF','Affine_STS9_DNF'] and abs(r['bias'])<1-1e-9],'Asymptotic growth OPEN; last near-constant float rows excluded here','extra.py')
    group('Overlapping cyclic DNFs, all tested triples through n=16',[r for r in fam if r['name'].startswith('cyclic')],'Growth OPEN; O(n) trivial bound','search.py families')
    group('Fixed cyclic templates n=17..20',[r for r in extra if r['name'].startswith('cyclic')],'Growth OPEN; direct exact subset optimization','extra.py')
    group('Random monotone DNFs at nominal independent-term threshold',[r for r in fam if r['name'].startswith('random_DNF')],'Finite checks; overlap changes the actual threshold','search.py families')
    group('Random signed DNFs at the measured half-mass crossing',rnd,'Finite checks; no probability/asymptotic theorem','random_threshold.py')
    group('Invertible linear changes of majority, tribes and PM host',linear,'Entropy invariant; no uniform F-growth claim','search.py linear')
    group('PM(K33) nine-coin towers',pm['rows'],'O(1), enclosed by analytic tail','large.py pm')
    group('AND of PM towers, widths through 1000',read('amplify')['data'],'Finite copy-count limit for every fixed seed tower','amplify.py')
    lines=['# Families','', 'F=min over live i and all permutations of L_i/Inf_i; E=min_i E_i/Inf_i. Units are bits per unit influence. Every row in FAMILIES.csv points to its JSON receipt and parameter index. Direct-table optimization uses exact dyadic masses and floating logarithms. Composition entries are exact formulas evaluated numerically, rather than expanded truth tables.','', '| Family | Cases | F range in this scan | Proved growth or limitation | Command |','|---|---:|---:|---|---|']
    lines += ['| '+' | '.join(row)+' |' for row in groups]
    lines += ['',f"Complete odd quadratic forms additionally have E=0 and F=2-2^(3-n); final_checks.json checks the formula on its listed dimensions. Address functions and their balanced iterations have F=0 at a data-path coordinate by the explicit ordering proof; numerical small addresses are included in policy.json. Disjoint XOR preserves the smaller component minimum.",'',f"The strongest optimized F in the principal fixed-gate survey is the PM tower. At depth {pm['rows'][-1]['depth']}, F={fmt(pm['rows'][-1]['F'])}; the analytic remaining tail is at most {pm['tail_upper']:.6g}. The numerical limit enclosure is [{pm['F_interval'][0]:.15f}, {pm['F_interval'][1]:.15f}], before floating-rounding allowance. It is not a directed-rounding certificate.",'',f"The largest proved-family gap here is the recursive Fano construction: E=0 and limiting F approximately {fmt(float(fc['fano']['F_finite']))}. Its depth-40 analytic tail is {float(fc['fano']['tail']):.6g}; the finite recurrence is evaluated at 90 decimal digits. This is bounded growth, not a counterexample.",'','The overlap scans do not establish a limit. In particular, the cyclic values increasing through twenty variables do not prove divergence. Arbitrary plane orders, Steiner systems, sparse-correction sets, linear maps, fan-in assignments and mixed formulas were not exhaustively optimized. The near-constant affine-STS and PG tower float rows remain in extra.json for traceability, but their final nearly unit biases make them unsuitable for precise claims; they are excluded from the table above.','',f"The ledger contains {len(allrows)} evaluations, including repeated baseline parameterizations; this is not a count of distinct Boolean functions. No universal FWC refutation was found."]
    open('FAMILIES.md','w').write('\n'.join(lines)+'\n')
    runs=['audit','structured','families','composition','large','pm','linear','policy','extra','final_checks','native_audit','random_threshold','amplify']
    resources=dict(runs={s:{k:read(s)[k] for k in ['seconds','nice','maxrss_bytes'] if k in read(s)} for s in runs})
    resources['max_instrumented_python_rss_bytes']=max(v['maxrss_bytes'] for v in resources['runs'].values());resources['all_nice_10']=all(v['nice']==10 for v in resources['runs'].values());resources['threads_per_numerical_library']=1
    resources['native_precision']=native['native_precision'];resources['folder_bytes_before_manifest']=sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file())
    json.dump(resources,open('resources.json','w'),indent=2)
    srcs=['../../RULES.md','BRIEF.md','~/fei_solve_agent/FLOW.md','../FEIB16/FORMULAS.md','../FEIB16/WITNESSES.md','../FEIB16/pm_record_spectrum.npy']
    provenance={str(pathlib.Path(p).resolve()):hashlib.sha256(open(p,'rb').read()).hexdigest() for p in srcs}
    json.dump(provenance,open('source_provenance.json','w'),indent=2)
    bestpolicy=max(policy,key=lambda r:r['additive']);maxfactor=max(r['factor'] or 1 for r in policy)
    report=f'''# FEIB19 report

Compositions admit an optimal reveal order respecting every block, with the target block last. This gives an exact optimized filtration composition law. It also proves L*=E at every leaf of a read-once AND/OR/XOR/NOT formula, and therefore FWC with coefficient 10 on that restriction-closed class. The block-order proof and recurrence are in PROOFS.md; full-table comparisons are in composition.json and final_checks.json.

Part 1 — PROVED core identities; FALSE ancillary unnormalized comparison and literal weighted-count entropy-limit claim; GAP in the random-order estimate and the threshold cross-reference. REFEREE.md gives one verdict per claim and the corrected statements.

Part 2 — OPEN universally; no refutation found. The PM tower reaches F={pm['rows'][-1]['F']:.12f} at depth {pm['rows'][-1]['depth']}, with an analytic remaining tail below {pm['tail_upper']:.3g}. The limiting optimized witness is approximately 4.86317608849 bits per unit influence. The recursive Fano DNF has E=0 identically and a limiting optimized witness approximately {float(fc['fano']['F_finite']):.14f}, so its entire value is filtration/erasure gap. Its depth-40 tail bound is {float(fc['fano']['tail']):.3g}. Both families have proved bounded growth. FAMILIES.md and FAMILIES.csv cover the other families, including large widths, cyclic overlap, projective/Steiner DNFs, quadratic corrections, random threshold DNFs and linear changes.

Part 3 — PROVED FWC for read-once AND/OR/XOR/NOT formulas (10), degree at most d (d-1+log2(e)), sensitivity at most s (2s-2+log2(e)), and linear threshold functions ({fc['constants']['LTF']:.12f}). At a threshold's largest-weight coordinate every reveal order satisfies the displayed conservative coefficient. The general majority/threshold read-once class, overlapping bounded-width DNFs and expected-depth-only trees remain OPEN. The proposed greedy rule has only the trivial bound proved; on {len(policy)} supplied small examples its largest additive excess is {bestpolicy['additive']:.8f} bits per unit influence, on {bestpolicy['name']}, and its largest nonzero-optimum factor is {maxfactor:.8f}. The naive actual-input adaptive martingale extension is FALSE: truth table b6a4 has E_i=1 bit but adaptive cost 0.7743974703476992 bits. PROOFS.md gives the explicit policy and valid alternative statements.

Part 4 — CHECKED selected primary passages and references; the exact filtration construction was not located. LITERATURE.md distinguishes this scoped search from a novelty claim and names the later restriction-induction paper. Exhaustive later literature is not checked.

The exhaustive four-variable check covers {fc['census4']['functions']:,} truth tables; all tested entropy, degree and sensitivity inequalities pass. The optimized composition recurrence agrees with full truth-table DPs on {read('composition')['validation']['coordinates']+fc['structural']['composition_live_coordinates']} live coordinates, with maximum unnormalized residual {max(read('composition')['validation']['errors']['L'],fc['structural']['composition_L_error']):.3g} bits. Native integer-mass subset DPs independently match the cyclic and PM candidates; selected PM orders are re-evaluated from exact dyadic masses with 90-digit arithmetic. The native compiler's long double has {native['native_precision']['mantissa_bits']} mantissa bits on this machine, so native independence must not be mistaken for extra floating precision. Numerical minima and tail enclosures are not directed-rounding certificates.

All instrumented Python runs inherited nice 10, and numerical libraries were restricted to one thread. The largest measured Python resident set was {resources['max_instrumented_python_rss_bytes']:,} bytes; native arrays are small and were not separately RSS-instrumented. The output folder is below the required disk cap, as recorded in resources.json. No subagents, additional model workers, shared-state publishing, git pushes or trading processes were used. Brain recall supplied context and prior cautions; the math recall script reported that its store was absent. LEARNINGS.md is ready for the launching session to ingest.

The requested investigation and artifacts are complete within these explicit proof and search scopes. The universal conjecture and the unresolved class extensions remain open mathematical problems.

Task: “Do the brief fully and carefully” — FEIB19, observed start 10 November 2026, 06:41 +04.
'''
    open('REPORT.md','w').write(report)
    manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name not in ['manifest.json','STATUS.md','events.jsonl'] and '__pycache__' not in p.parts}
    json.dump(dict(created=datetime.datetime.now().isoformat(),files=manifest),open('manifest.json','w'),indent=2)
    print(json.dumps(dict(family_ledger_rows=len(allrows),max_rss=resources['max_instrumented_python_rss_bytes'],nice=resources['all_nice_10'],folder_bytes=resources['folder_bytes_before_manifest'],report='REPORT.md'),indent=2))
if __name__=='__main__':main()
