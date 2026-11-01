import runpy,json,time
from pathlib import Path
R=Path(__file__).resolve().parents[1];H=runpy.run_path(str(R/'code/conversion.py'),run_name='a047_helpers')
Q,add,mul,hb,cert,expr=(H[n] for n in ('Q','add','mul','hb','cert','expr'))
start=time.perf_counter();rows=[]
for r in range(1,17):
    assert time.perf_counter()-start<55
    delta=Q(1,1<<r);removed=2*delta
    o=add(hb(delta),mul(hb(2*delta),Q(-1,2)))
    gamma=add({2:Q(1)},mul(o,-1))
    rows.append({'r':r,'removed':str(removed),'output_info':expr(o),'incompatible_conversion':expr(gamma),'ratio_conversion_over_2removed':cert(mul(gamma,Q(1,2)/removed))})
    (R/'out/SIDEINFO_BOUNDARY.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
assert Q(rows[-1]['ratio_conversion_over_2removed']['lower'])>16000
main=json.loads((R/'out/CHECK.json').read_text())
(R/'out/HALF_I_COUNTEREXAMPLE.json').write_text(json.dumps(main['half_I_conversion_counterexample'],indent=2),encoding='utf8')
print('PASS: 16 exact future-side-info boundaries; r=16 ratio >16000; compatible half-I counterexample r',main['half_I_conversion_counterexample']['r'])
print('compatible r=5 Gamma/(2I):',main['half_I_conversion_counterexample']['Gamma_over_2I']['display'])
