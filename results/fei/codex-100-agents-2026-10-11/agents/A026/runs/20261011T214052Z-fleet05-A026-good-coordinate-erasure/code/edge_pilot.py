import json, time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def walsh(a):
    a=list(a)
    h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]
                a[k],a[k+h]=u+v,u-v
        h*=2
    return a

def ratios(w,n):
    result=[]
    for i in range(n):
        bit=1<<i
        den=sum(w[t|bit]**2 for t in range(1<<n) if not t&bit)
        num=2*sum(abs(w[t]*w[t|bit]) for t in range(1<<n) if not t&bit)
        if den: result.append((Fraction(num,den),i))
    return result

def main():
    start=time.perf_counter(); out=[]; assertions=0
    for n in range(1,5):
        N=1<<n; best=Fraction(0); witness=None; nonconstant=0
        for mask in range(1<<(N-1)):
            f=[1]+[1-2*((mask>>(j-1))&1) for j in range(1,N)]
            w=walsh(f)
            assert sum(x*x for x in w)==N*N; assertions+=1
            rr=ratios(w,n)
            if not rr: continue
            nonconstant+=1
            r,i=min(rr)
            if r>best:
                best=r; witness={'mask':mask,'walsh':w,'ratios':[{'i':i,'ratio':str(r)} for r,i in rr]}
            if time.perf_counter()-start>55: raise RuntimeError('frozen pilot limit')
        out.append({'n':n,'cases':1<<(N-1),'nonconstant':nonconstant,'max_min_amplitude_ratio':str(best),'witness':witness})
    result={'helper_version':'A026-edge-amplitude-v1','elapsed_seconds':time.perf_counter()-start,'assertions':assertions,'results':out}
    (ROOT/'out'/'edge_pilot.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
