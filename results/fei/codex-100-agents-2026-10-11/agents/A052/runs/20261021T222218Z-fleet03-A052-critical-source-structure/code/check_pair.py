from pathlib import Path
from fractions import Fraction as F
import json, sys, time

ROOT=Path(__file__).resolve().parents[1]
def walsh(a):
    a=a[:]; h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def analyze(n,table):
    N=1<<n; f=[1-2*((table>>x)&1) for x in range(N)]
    a=walsh(f); a2=[x*x for x in a]
    p=[sum(a2[s] for s in range(N) if s>>i&1) for i in range(n)]
    costs=[sum(a2[s] for s in range(N) if (s&v).bit_count()%2) for v in range(N)]
    amin=all(x<=N*N//2 for x in p) and all(min(costs[v],N*N-costs[v])>=max(p[i] for i in range(n) if v>>i&1) for v in range(1,N))
    if not amin: return None
    pairs=[]
    def z(x,y): return F(4*x*y,x+y) if x+y else F(0)
    for i in range(n):
        for j in range(i):
            ci=cj=P=mi=mj=O=F(0)
            for t in range(N):
                if t&((1<<i)|(1<<j)): continue
                aa,bb,cc,dd=[a[t^s] for s in [0,1<<i,1<<j,(1<<i)|(1<<j)]]
                A,B,C,D=aa*aa,bb*bb,cc*cc,dd*dd; q=A+B+C+D
                if not q: continue
                ui=z(A,B)+z(C,D); uj=z(A,C)+z(B,D)
                vi=F(4*(aa*bb+cc*dd)**2,q); vj=F(4*(aa*cc+bb*dd)**2,q)
                ci+=ui; cj+=uj; mi+=ui-vi; mj+=uj-vj
                P+=F(4*(aa*dd+bb*cc)**2,q)
                O+=max(0,B-A)+max(0,D-C)+max(0,C-A)+max(0,D-B)
            Q=ci+cj+P-mi-mj
            pairs.append({'pair':[j,i],'gap_Q':str((Q-2*(ci+cj))/(N*N)),'gap_O':str((O-mi-mj)/(N*N)),'Q':str(Q/(N*N)),'Csum':str((ci+cj)/(N*N)),'O':str(O/(N*N)),'Msum':str((mi+mj)/(N*N))})
    return {'n':n,'table':table,'walsh':a,'influences':[str(F(v,N*N)) for v in p],'pairs':pairs}

def main():
    start=time.perf_counter(); ns=[4] if '--full' in sys.argv else [0,1,2,3]
    counts={}; failures=[]; worst=None; checks=0
    for n in ns:
        count=0
        for table in range(1<<(1<<n)):
            data=analyze(n,table); checks+=1
            if data is None: continue
            count+=1
            for pair in data['pairs']:
                gap=F(pair['gap_Q']); checks+=1
                if worst is None or gap>F(worst['detail']['gap_Q']): worst={'n':n,'table':table,'detail':pair}
                if gap>0 and len(failures)<8: failures.append(data); break
            if time.perf_counter()-start>52: raise RuntimeError('frozen runtime cap')
        counts[n]=count
    out={'counts':counts,'checked_tables':sum(1<<(1<<n) for n in ns),'checks':checks,'failures':failures,'worst':worst,'seconds':time.perf_counter()-start}
    (ROOT/'out'/('PAIR_FULL.json' if '--full' in sys.argv else 'PAIR_PILOT.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='failures'})); print('failures_saved',len(failures))
if __name__=='__main__': main()
