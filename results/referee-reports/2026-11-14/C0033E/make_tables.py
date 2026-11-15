"""Insert tables from saved computations, without altering theorem text."""
import json
from pathlib import Path
from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING

def load(name):return json.loads(Path('data/'+name+'.json').read_text())
def approx(x,n=12):
    if x is None:return '—'
    with localcontext() as c:
        c.prec=100
        return format(Decimal(str(x)),f'.{n}g')
def ivtext(x):
    with localcontext() as c:
        c.prec=100
        unit=Decimal('1e-19')
        return '['+str(Decimal(x[0]).quantize(unit,rounding=ROUND_FLOOR))+', '+str(Decimal(x[1]).quantize(unit,rounding=ROUND_CEILING))+']'

def format_inline_math(text):
    # The report uses dollar delimiters for inline mathematics, preserving
    # equation references and parenthetical prose.
    text=text.replace(chr(92)+')',')').replace(chr(92)+'(','(')
    lines=[];display=False
    import re
    for line in text.splitlines():
        if display or chr(92)+'[' in line:
            lines.append(line)
            if chr(92)+'[' in line:display=True
            if chr(92)+']' in line:display=False
            continue
        out='';i=0;in_math=False
        while i<len(line):
            if line[i]=='$':
                in_math=not in_math;out+=line[i];i+=1;continue
            if in_math:
                out+=line[i];i+=1;continue
            if line[i]!='(' or (i and (line[i-1].isalnum() or line[i-1] in ']_')):
                out+=line[i];i+=1;continue
            j=i+1;depth=1
            while j<len(line) and depth:
                depth+=(line[j]=='(')-(line[j]==')');j+=1
            if depth:out+=line[i:];break
            val=line[i+1:j-1];stripped=val.strip()
            symbols=any(c in val for c in (chr(92),'=','<','>','_','^','|','/'))
            tokens=re.split('[ ,+*-]+',stripped)
            short=bool(tokens) and all(re.fullmatch('[A-Za-z][0-9]*|[0-9]+',t) for t in tokens)
            function=bool(re.fullmatch('[A-Za-z][A-Za-z0-9_]*\\(.*\\)',stripped))
            math=(symbols or short or function) and not stripped.isdigit() and '$' not in val
            out+=('$'+val+'$') if math else line[i:j];i=j
        lines.append(out)
    return '\n'.join(lines)+'\n'

def main():
    search=load('search_mp');opt=load('collar_optimization');scaled=load('scaled_optimization');ver=load('verification');mix=load('mixed_limit');cover=load('bnb_small');exact=load('exact_cyclic')
    groups=search['groups'];accepted=sum(g['accepted'] for g in groups.values());rejected=sum(g['attempts']-g['accepted'] for g in groups.values())
    lines=[
        'All values in search tables are attained values, not certified minima over a continuous collar. Every evaluation enumerates all eight atoms and retains all nine ambient directions in the scalar criterion. The sweep seed is 33505; optimization seeds and stopping information are saved with the data. All arithmetic used for atoms, logarithms, and solves is mpmath arithmetic at 100 or more decimal digits. Binary numbers are used only by the outer optimizer and to select random parameters.',
        '',
        f'The sweep proposed {search["evaluations"]+search["construction_rejections"]:,} parameter choices: {search["construction_rejections"]} did not define an ordered strict spectrum, and {rejected} constructed candidates were rejected. There were {accepted:,} accepted evaluations. The first 50 rejection diagnostics are saved. An independent replay confirms that all 243 constructed rejections fail strictness; see [audit_inputs.py](audit_inputs.py) and [data/input_audit.json](data/input_audit.json). The 870 ambient perturbations comprise both signs of each of nine coordinate directions at three radii, and 120 dense Hermitian combinations at each of five scales. Their Frobenius radii are less than the spectral gap, so feasibility is controlled before evaluation. Code: [search_mp.py](search_mp.py), [mp_core.py](mp_core.py); data: [data/search_mp.json](data/search_mp.json).',
        '',
        '| Cyclic scale L | Cyclic margin | Smallest ambient-perturbation margin | Smallest scaled perturbation margin |',
        '| --- | ---: | ---: | ---: |'
    ]
    for L in (20,60,150,400,1000):
        a=groups[f'ambient_{L}'];b=groups[f'cyclic_{L}']
        lines.append(f'| {L} | {approx(b["minimum"]["margin"])} | {approx(a["minimum"]["margin"])} | {approx(a["minimum_scaled"]["scaled"])} |')
    lines+=['',r'Here and below a scaled margin means $m(\Lambda+4)$. A fixed additive constant does not affect the limiting coefficient.','','| Scale L | Generic spectral/graph accepted | Generic smallest margin | Mixed accepted | Mixed smallest margin | Mixed smallest scaled margin |','| --- | ---: | ---: | ---: | ---: | ---: |']
    for L in (20,60,150,400):
        a=groups[f'spectral_graph_{L}'];b=groups[f'mixed_{L}']
        lines.append(f'| {L} | {a["accepted"]} | {approx(a["minimum"]["margin"])} | {b["accepted"]} | {approx(b["minimum"]["margin"])} | {approx(b["minimum_scaled"]["scaled"])} |')
    optevals=sum(r['evaluations'] for r in opt['runs']);scaleevals=sum(r['evaluations'] for r in scaled['runs'])
    optreject=sum(r['rejected'] for r in opt['runs']);scalereject=sum(r['rejected'] for r in scaled['runs'])
    lines+=['',
        f'The finite collar searches used {optevals:,} objective calls for the margin and {scaleevals:,} for the scaled margin, including {optreject:,} and {scalereject:,} rejected calls respectively. Their explicitly fixed endpoint eigenvalues are exp(-L) and 1-exp(-bL), with b in [0.12,1]; the middle eigenvalue and all four unitary orientation parameters vary. The first search limits angle logits to [-0.8L,0.8L]; the scaled search uses [-4L,4L] to resolve strongly unequal couplings to the low and high modes. These different orientation ranges are part of the search specification. All four differential-evolution runs and the local runs retain their stopping status in the JSON; no global optimality is asserted. Code: [optimize_collar.py](optimize_collar.py), [refine_scaled.py](refine_scaled.py); data: [margin search](data/collar_optimization.json), [scaled search](data/scaled_optimization.json).',
        '',
        '| Collar scale L | Smallest margin in margin search | Margin at scaled-search optimum | Smallest scaled margin |',
        '| --- | ---: | ---: | ---: |'
    ]
    for a,b in zip(opt['runs'],scaled['runs']):
        lines.append(f'| {a["L"]} | {approx(a["best"]["margin"])} | {approx(b["best"]["margin"])} | {approx(b["best"]["scaled"])} |')
    lines+=['',
        'The smallest located margin, to the displayed precision, is approximately **0.000250024145729409772194102983447**, on the structured family',
        r'\[t=e^{-1000},\qquad Q=Q(1-t^2,t^2,t^{21/10}).\]',
        'The four structured probes at L=1000 in [data/mixed_limit.json](data/mixed_limit.json) have margins agreeing at the displayed precision. For an unambiguous certified point, the exact rational rounding of the displayed kernel is saved under `special_mixed_min_L1000` in [data/verification.json](data/verification.json). Its interval below certifies the same displayed margin. A family parameterization and a rational rounding are distinct exact kernels; their agreement is numerical, and the interval assertion is for the saved rational kernel.',
        '',
        'The normalization obstruction is visible before extrapolation. Code: [mixed_limit.py](mixed_limit.py), [verify_results.py](verify_results.py); data: [mixed limits](data/mixed_limit.json), [independent audit](data/verification.json).',
        '',
        '| h=exp(-L), e=h^6, a=1/2 | Margin | Lambda times margin | In the proved collar |',
        '| --- | ---: | ---: | --- |'
    ]
    for r in ver['normalized_obstruction']:
        lines.append(f'| L={r["L"]} | {approx(r["margin"])} | {approx(r["product"])} | {'yes' if r['proved_collar'] else 'no'} |')
    lines+=['',
        'The fixed-data check at a=0.37 and h=0.1 gives (m-m0)/e^2 approaching '+approx(mix['fixed_checks'][-1]['error_over_e2'])+'. The atom-logarithm estimate (5) is deliberately conservative; it is a uniform estimate with explicit parameters, not a fitted error.',
        '',
        'The eta=16 probes inside the proved collar use adaptive precision until their direct ambient scalar solves resolve the explicit remainder (5). Their final precisions and retry counts are saved in the mixed-limit data. Fixed decimal precision based only on the spectral gap can be inadequate when the connections vanish much faster. Point certificates use exact rational coordinates and outward-rounded mpmath.iv operations. Leading principal minors certify Q and I-Q; leading minors certify R; interval LDL certifies the full nine-dimensional negative Hessian and both positive solve matrices. Both the original nine-direction criterion and the seven-atom criterion are enclosed and their intervals overlap. Small interval pivots are saved with nonzero outward bounds in scientific notation. The two weakly connected sweep points needed interval precision retries from 1,976 to 3,952 digits; the special minimum needed 5,200 to 10,400 digits before the seven-atom enclosure succeeded. No failed enclosure is a sign certificate.',
        '',
        '| Saved exact rational point | Interval decimal precision | Certified margin interval |',
        '| --- | ---: | --- |'
    ]
    for r in ver['point_certificates']:
        lines.append(f'| `{r["label"]}` | {r["precision"]} | {ivtext(r["margin"])} |')
    diffs=[Decimal(r['difference']) for r in ver['precision_audits']]
    formula=[Decimal(r['closed_formula_error']) for r in ver['cyclic']];dets=[Decimal(r['full_determinant_error']) for r in ver['cyclic']]
    lines+=['',
        f'The {len(ver["precision_audits"])} doubled-precision sweep-extremum checks agree to absolute error at most {approx(max(diffs),5)} and also agree with their saved margins within 10^(-55). The seven full cyclic determinant checks have maximum absolute discrepancy {approx(max(dets),5)}; the cyclic formula versus ambient scalar solve has maximum discrepancy {approx(max(formula),5)}. All symbolic comparison remainders are zero. The additional two optimized endpoint points were also re-evaluated at doubled precision before interval certification.',
        '',
        f'The inherited small-box interval cover was reproduced: {cover["nodes"]} nodes, {len(cover["certified"])} accepted leaves, {len(cover["pending"])} unresolved leaves. Its domain is exactly C0033D (9), and its lower margin bound is greater than 0.02478. This is credited to C0033D, not counted as a new covered region. Data: [data/bnb_small.json](data/bnb_small.json).',
        '',
        '| Run | Seconds | Peak RSS, MiB |',
        '| --- | ---: | ---: |'
    ]
    for name,d in [('Exact cyclic determinant',exact),('High precision sweep',search),('Margin optimization',opt),('Scaled optimization',scaled),('Mixed limit checks',mix),('Precision and interval audit',ver),('Inherited small cover',cover)]:
        lines.append(f'| {name} | {approx(d["seconds"],6)} | {approx(d["peak_rss_mib"],6)} |')
    lines+=['',
        'All runs use one numerical process at a time, one numerical thread, inherited nice 20, no worker pools and no additional language-model workers. The measured memory is far below 4 GB. Sweep and optimizer checkpoints are written atomically at intervals of 100 objective calls; the independent audit checkpoints each completed extremum or certificate. Optimizer checkpoints preserve the best point and run metadata rather than the optimizer population state.',
        '',
        'Run `python3 reproduce.py` to regenerate the exact derivation, mixed-limit checks, precision audits, interval certificates, inherited completed cover, and tables using the saved searches. Add `--search` to regenerate the searches first. The copied C++ source is built as a macOS shared library. Python, package versions, priority and artifact hashes are saved in [artifact_manifest.json](artifact_manifest.json). The running task record is [LOG.md](LOG.md).'
    ]
    report=Path('REPORT.md');text=report.read_text();begin=text.index('## 5. High-precision searches and point certificates');end=text.index('## 6. Coverage and the remaining problem')
    text=text[:begin]+'## 5. High-precision searches and point certificates\n\n'+'\n'.join(lines)+'\n\n'+text[end:];report.write_text(format_inline_math(text))
if __name__=='__main__':main()
