from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib,time
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
    global checks
    assert x;checks+=1
def bent(x):return -1 if ((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))%2 else 1
summary=json.loads((RUN/'out/full_RESULTS.json').read_text())
reconstructed={};worst_min={};rows=0
for r in [0,2,4]:
    count=Counter()
    for line in (RUN/'out'/f'full_r{r}_patterns.jsonl').read_text().splitlines():
        row=json.loads(line);D=set(row['D']);s=row['size'];count[s]+=1
        A=sum(bent(v)*bent(v^(1<<i)) for v in D for i in range(4) if (v^(1<<i)) not in D)
        S=sum(bent(v) for v in D)
        influence=Q(2+Q(3*r,4)+Q(A+r*S+s,16),1<<r)
        ck(row['root']['mu']==str(Q(s,16*(1<<r))))
        ratios=[]
        for order,entry in row['orders'].items():
            ck(Q(entry['I'])==influence)
            ratio=Q(entry['bad_credit'])/influence;ck(Q(entry['bad_credit_over_I'])==ratio)
            ck(Q(entry['bad_credit'])<=Q(entry['Q']))
            if order=='control_data_selector':ck(entry['n_bad']==0)
            key=f'r={r},s={s},order={order}'
            if key not in reconstructed or ratio>reconstructed[key][0]:reconstructed[key]=[ratio,row['D'],1]
            elif ratio==reconstructed[key][0]:reconstructed[key][2]+=1
            ratios.append(ratio)
        low,high=map(Q,row['root']['gap_interval']);ck(0<=low<=high)
        key=f'r={r},s={s}';val=min(ratios)
        if key not in worst_min or val>worst_min[key][0]:worst_min[key]=[val,row['D'],1]
        elif val==worst_min[key][0]:worst_min[key][2]+=1
        rows+=1
    ck(dict(count)=={1:16,2:120,3:560,4:1820})
for key,(ratio,D,ties) in reconstructed.items():
    saved=summary['maxima_per_order'][key]
    ck(Q(saved['ratio'])==ratio);ck(saved['D']==D);ck(saved['ties']==ties)
for key,(ratio,D,ties) in worst_min.items():
    saved=summary['maxima_after_min_four_orders'][key]
    ck(Q(saved['ratio'])==ratio);ck(saved['D']==D);ck(saved['ties']==ties)
ck(rows==7548)
ck(max(v[0] for v in reconstructed.values())==Q(4,29))
witness=json.loads((RUN/'out/WITNESS_TRANSPORT.json').read_text())
lo,hi=map(Q,witness['limiting_B_over_d_interval']);ck(lo>Q(4157,1000));ck(hi<Q(4158,1000))
ck(witness['signed_walsh_ratios_at_vertex']==[2,6,2,-2,-2,2,-2,2])
ck((RUN/'ODDFACE_GAP.tex').read_text().count('\\end{document}')==1)
out={'checks_passed':checks,'rows_independently_aggregated':rows,'runtime_seconds':time.perf_counter()-start,
     'scope':'second implementation by A022; not independent agent acceptance',
     'maximum_ratio':'4/29','all_control_data_selector_bad_node_counts_zero':True,
     'influence_formula_checked_on_every_pattern':True,'prime_log_limit_between':'4157/1000 and 4158/1000'}
(RUN/'out/ARTIFACT_CHECK.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
