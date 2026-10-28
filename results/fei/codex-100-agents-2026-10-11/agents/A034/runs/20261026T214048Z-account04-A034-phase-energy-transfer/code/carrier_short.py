from pathlib import Path
import importlib.util,itertools,json,hashlib,time
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('helper',R/'code/check.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
start=time.monotonic();cases=0
for state in itertools.product((-1,0,1),repeat=6):
    xs,ys=state[:2],state[2:];nx=xs.count(-1);ny=ys.count(-1);vals=[];bits=[]
    for local in range(1<<ny):
        y=h.assign(ys,local);t=y&1;z=(y>>1)&3;a=y>>3&1
        label=z if t else 0;phase=a*((z>>(1 if t else 0))&1)
        for localx in range(1<<nx):
            p=phase^((h.assign(xs,localx)&label).bit_count()&1);bits.append(p);vals.append(1-2*p)
    anf=bits[:]
    for i in range(nx+ny):
        for mask in range(len(anf)):
            if mask>>i&1:anf[mask]^=anf[mask^(1<<i)]
    h.need(all(not b or mask.bit_count()<=3 for mask,b in enumerate(anf)),'global phase degree at most3')
    ey=h.influences(vals)[nx:];E=sum(ey);N=sum(e>0 for e in ey)
    h.need(all(e==0 or e>=h.Q(1,4) for e in ey),'nonzero Y influence at least1/4')
    h.need(N<=4*E,'active Y paid')
    h.need(h.bill(vals)[1]<=8*E,'complete source full rate8, stronger than K2')
    cases+=1
out=dict(status='PASS',cases=cases,assertions=h.CHECKS,seconds=time.monotonic()-start,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(R/'out/carrier_short.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
