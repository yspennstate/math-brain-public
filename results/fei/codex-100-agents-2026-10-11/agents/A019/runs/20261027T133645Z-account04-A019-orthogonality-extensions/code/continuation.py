import importlib.util,json,time
from pathlib import Path
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('p',R/'code/check_essential.py');p=importlib.util.module_from_spec(s);s.loader.exec_module(p)
start=time.perf_counter();n=0;cases=0
def ck(x):
    global n
    n+=1
    assert x,n
for b in (1,2):
    rho=Q(1,2**b)
    for L in range(4):
        for phase in (-1,1):
            for sigma in (-1,1):
                core=[]
                for i in range(2**(b+1+L)):
                    u=1-2*(i&1);G=phase*(-1 if (i>>(b+1)).bit_count()%2 else 1)
                    core.append(sigma if ((i>>1)&(2**b-1))==0 and G==-1 else u)
                full=tuple(1 if e==0 else core[i]*(-1,1,1,1)[w] for w in range(4) for i in range(len(core)) for e in (0,1))
                a=rho/2 if L else (rho if phase==-1 else Q(0))
                physical=4*p.edges(full);exact=6+2*(b-1)*a+rho*L-sigma*a
                ck(physical==exact);ck(physical<=6+2*b*rho+rho*L)
                pp=p.spectrum(full);mass=sum(v for i,v in enumerate(pp) if (((i>>1)&(len(core)-1))>>(b+1)))
                ck(mass==(rho/4 if L else 0));cases+=1
for k in (8,16,32,64):
    for K in (4,5,6):
        rho=Q(1,2**k);mean_initial=16/rho
        threshold=K*(6+2*k*rho)/(rho*(k-K))
        ck(threshold/mean_initial==K*(6+2*k*rho)/(16*(k-K)))
result={'status':'PASS','cases':cases,'assertions':n,'seconds':time.perf_counter()-start,'scope':'Exact terminal physical edges/sector; all-policy necessity follows by finite averaging, not sampling.'}
ck(result['seconds']<60);(R/'out/CONTINUATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n');print(json.dumps(result))
