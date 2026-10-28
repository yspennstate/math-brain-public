from pathlib import Path
from fractions import Fraction as Q
import json,time
R=Path(__file__).resolve().parents[1];ns=0
def ck(x):
    global ns
    ns+=1
    assert x,ns
def spec(t):
    return tuple(Q(sum(v*(-1 if (i&s).bit_count()%2 else 1) for i,v in enumerate(t))**2,len(t)**2) for s in range(len(t)))
def influence(t):return sum(Q(sum(t[i]!=t[i^(1<<z)] for i in range(len(t))),len(t)) for z in range(len(t).bit_length()-1))
def main():
    start=time.perf_counter();blocks=[]
    for k in range(1,7):
        d=Q(1,2**k);t=(-1,)+(1,)*(2**(k+1)-1);p=spec(t);ck(p[0]==(1-d)**2);ck(all(x==d*d for x in p[1:]));ck(influence(t)==(k+1)*d)
        # Summation directly over all original control FREQUENCIES.
        r1=sum(x for i,x in enumerate(p) if i>>k&1);ck(r1==d);blocks.append({'k':k,'R_essential':str(r1),'CE':k,'I':1})
    cases=0
    for b in (1,2):
        rho=Q(1,2**b)
        for M in range(4):
            for sigma in (-1,1):
                ncore=b+1+M;n=2**ncore
                def cv(i):
                    u=1-2*(i&1);pad=((i>>1)&(2**b-1))==0
                    g=1 if M==0 else (-1)**M*(-1 if (i>>(b+1)).bit_count()%2 else 1)
                    return sigma if pad and g==-1 else u
                core=tuple(cv(i) for i in range(n));truth=tuple(1 if not(i&1) else core[(i>>1)&(n-1)]*(-1,1,1,1)[i>>(ncore+1)] for i in range(n*8));p=spec(truth)
                ck(4*influence(truth)==6+(b-1-Q(sigma,2))*rho*(M>0)+rho*M)
                for k in range(1,7):
                    d=Q(1,2**k);mu=(1-d)**3;pp=rho*(1-mu)/2
                    rr=[d**s.bit_count()*(1-d)**(M-s.bit_count()) for s in range(2**M)]
                    qr=[Q(0)]*n;qr[1]=(1-2*pp)/2;qr[0]+=Q(1,2)
                    for s in range(2**M):
                        for uv in range(2**(b+1)):qr[uv+(s<<(b+1))]+=rho*rho*(rr[s]+(1-2*mu if not s else 0))/8
                    ref=[qr[(i>>1)&(n-1)]/16+(Q(1,4) if (i>>1)==0 else 0) for i in range(n*8)]
                    ck(sum(ref)==sum(p)==1);ck(min(ref)>=0)
                    mass=Q(0);cost=Q(0)
                    for i,x in enumerate(p):
                        if x and (((i>>1)&(n-1))>>(b+1)):
                            ck(x==rho*rho/64);ck(ref[i]==rho*rho*d**M/128)
                            mass+=x;cost+=x*(2*b+7+k*M)
                    ck(mass==(rho/4 if M else 0));ck(cost==(rho*(2*b+7+k*M)/4 if M else 0));cases+=1
    result={'status':'PASS','exact_assertions':ns,'blocks':blocks,'sector_profiles':cases,'seconds':time.perf_counter()-start,'independence':'Direct characters and full physical truth tables; no main checker/helper imports.'}
    ck(result['seconds']<60);(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n');print(json.dumps({x:result[x] for x in ['status','exact_assertions','sector_profiles','seconds']}))
if __name__=='__main__':main()
