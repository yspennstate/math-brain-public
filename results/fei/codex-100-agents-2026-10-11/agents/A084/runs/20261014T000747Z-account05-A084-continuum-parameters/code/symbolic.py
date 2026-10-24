from pilot import WH,ROOT
import sympy as s,json,time
from collections import defaultdict
start=time.perf_counter();m=s.symbols('m',real=True);groups=defaultdict(list)
for T in range(0,64,2):
    k=T.bit_count();C=s.Rational(0);d=s.Rational(0)
    for W in range(64):
        if W&T==T:C+=s.Rational(WH[W],64)*m**(W.bit_count()-k)
        if W&(T|1)==T|1:d+=s.Rational(WH[W],64)*m**(W.bit_count()-k-1)
    key=(k,str(s.factor(C)),str(s.factor(d)))
    groups[key].append(T)
rows=[]
for (k,C,d),T in groups.items():
    row={'multiplicity':len(T),'masks':T,'degree':k,'C':C,'d':d};rows.append(row)
    print(row,flush=True)
q=s.factor(sum(len(T)*(1-m*m)**k*s.sympify(d,locals={'m':m})**2 for (k,C,d),T in groups.items()))
assert s.simplify(q-(1-m)*(1+m)**3*(3+m)/16)==0
out={'groups':rows,'q':str(q),'m':'1-2p','U':'(1-m^2)^degree*C(m)^2','D':'(1-m^2)^degree*d(m)^2','runtime_seconds':time.perf_counter()-start}
(ROOT/'out'/'SYMBOLIC_PACKETS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('q:',q,'groups:',len(rows),flush=True)
