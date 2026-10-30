from pathlib import Path
import sympy as s,json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
m=s.symbols('m',real=True);v=1-m*m;S=m*m+2*m-1;P=m**4+4*m**3+2*m*m-4*m-11
d0=(m-1)*(m+1)**3*(m+3)/16;C0=S*P/16
ratios=[(C0/d0)**2,((m-1)*(m+1)*(m+3)/S)**2,(S/(m+1))**2,(m+1)**2]
weights=[d0**2,S*S*(m+1)**2*(4*v*(m+1)**2+2*v*v)/256,v*v*(m+1)**4*(m+3)**2/256,
    (v*(m-1)**2*(m+1)**4*(m+3)**2+4*v*v*(m+1)**2*S*S+2*v**3*S*S+4*v**3*(m+1)**4+4*v**4*(m+1)**2+v**5)/256]
got=[s.Rational(0)]*4;checks=0
packets=json.loads((ROOT/'out'/'SYMBOLIC_PACKETS.json').read_text())['groups']
for row in packets:
    C=s.sympify(row['C'],locals={'m':m});d=s.sympify(row['d'],locals={'m':m})
    idx=[j for j,r in enumerate(ratios) if s.cancel(C*C/(d*d)-r)==0]
    assert len(idx)==1
    got[idx[0]]+=row['multiplicity']*v**row['degree']*d*d;checks+=1
for a,b in zip(got,weights):assert s.cancel(a-b)==0;checks+=1
assert s.cancel(sum(weights)-(1-m)*(m+1)**3*(m+3)/16)==0;checks+=1
out={'global_rational_polynomial_identities':checks,'packet_types':len(packets),'ratio_groups':4,'sum_weights_equals_q':True,'runtime_seconds':time.perf_counter()-start,'sympy_version':s.__version__,'scope':'Exact formal identities, not sampled polynomial checks; poles outside certificate domains treated by original packets.'}
(ROOT/'out'/'GROUPING_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out),flush=True)
