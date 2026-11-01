from pathlib import Path
import runpy,json,time
from fractions import Fraction as Q
P=Path(__file__).resolve().parents[1]
h=runpy.run_path(str(P/'code'/'check.py'))
start=time.perf_counter()
g=(-1,1,1,1)
values=[]
for x in range(64):
    S,W,U,V=[(x>>k)&1 for k in range(4)]
    A=W*U*V or S*(U or V)
    values.append(1+A*(g[x>>4]-1))
v0=tuple(y for x,y in enumerate(values) if x>>4&1==0)
v1=tuple(y for x,y in enumerate(values) if x>>4&1==1)
spectra=[h['sp'](tuple(v)) for v in (values,v0,v1)]
H=[h['entropy_g'](tuple(v)) for v in (values,v0,v1)]
D=h['sub'](H[0],h['mul'](Q(1,2),h['add'](H[1],H[2])))
B=J=h['Z']
hmix=hc=h['Z']
for u,v in zip(spectra[1],spectra[2]):
    aa,bb=((u+v)/2)**2,((u-v)/2)**2
    B=h['add'](B,h['phi'](aa,bb))
    hmix=h['add'](hmix,h['term'](aa+bb))
    hc=h['add'](hc,h['mul'](Q(1,2),h['add'](h['term'](u*u),h['term'](v*v))))
J=h['sub'](hmix,hc)
record=h['data'](g,1,1,1,1,0)
assert h['fmt'](B)==record['B_data_bits'] and h['fmt'](J)==record['JS_data_bits']
assert h['influence'](tuple(values),4)==Q(7,32)
res=h['sub'](D,(Q(33,32),Q(33,32)))
assert res[0]>Q(3429,100000)
def masses(s):
    from collections import Counter
    return {str(k):v for k,v in sorted(Counter(t*t for t in s).items())}
out={'status':'PASS','family':'S,W,U,V single bits; g=(-1,1,1,1); query first core bit','dimension':6,'truth_table_evaluations':128,'spectral_mass_histograms':[masses(s) for s in spectra],'entropy_bits':[h['fmt'](x) for x in H],'decrement_bits':h['fmt'](D),'B_data_bits':h['fmt'](B),'JS_data_bits':h['fmt'](J),'pi_core_increment':'7/8','owned_release':'5/32','residual_bits':h['fmt'](res),'proved_residual_lower':'3429/100000','runtime_seconds':time.perf_counter()-start}
(P/'out'/'DIRECT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
