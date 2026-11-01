import json,time
from pilot import walsh,STAGE3,ROOT
start=time.monotonic();w=json.loads((STAGE3/'out/witness.json').read_text());out=[]
for J,h in enumerate(w['slices_h']):
    W=walsh(h);support=[s for s,v in enumerate(W) if v];base=support[0];active=0
    for s in support:active|=s^base
    bits=[i for i in range(4) if active>>i&1]
    def mask(u):return sum(1<<b for j,b in enumerate(bits) if u>>j&1)
    signs=[int(W[base^mask(u)]<0) for u in range(1<<len(bits))];a=signs.copy()
    for j in range(len(bits)):
        for u in range(len(a)):
            if u>>j&1:a[u]^=a[u^(1<<j)]
    mons=[mask(u) for u,v in enumerate(a) if v]
    for u,v in enumerate(signs):assert v==sum(1 for m in mons if mask(u)&m==m)%2
    z=sum(v*v for v in W);marg=[sum(v*v for s,v in enumerate(W) if s>>i&1) for i in range(4)]
    out.append({'row':J,'active_physical_frequency_bits':bits,'phase_monomials':mons,'maximum_degree':max((m.bit_count() for m in mons),default=0),'marginal_numerators':marg,'norm':z})
assert out[0]['maximum_degree']==3 and out[0]['phase_monomials']==[0,3,5,9,13]
assert min(out[0]['marginal_numerators'][0],out[0]['norm']-out[0]['marginal_numerators'][0])*17==out[0]['norm']
assert all(2*t==out[0]['norm'] for t in out[0]['marginal_numerators'][1:])
(ROOT/'out/phase_anf.json').write_text(json.dumps({'status':'PASS','rows':out,'seconds':time.monotonic()-start,'degree3_necessity':'analytic certificate in QUADRATIC_OBSTRUCTION.md'},indent=2));print(json.dumps(out))
