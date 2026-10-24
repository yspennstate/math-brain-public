from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util, json, time, sys, hashlib
RUN=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('arith',RUN/'code/optimal_tree.py')
A=importlib.util.module_from_spec(sp); sp.loader.exec_module(A)
COUNT=0
def check(x):
    global COUNT
    COUNT+=1
    assert x,COUNT
def combine(*vs): return A.add(*vs)
def phi(x,y): return combine((1,A.mlog(x+y)),(-1,A.mlog(x)),(-1,A.mlog(y)))
def child(tab,i,y):
    return tuple(v for x,v in enumerate(tab) if ((x>>i)&1)==y)
def clean(tab):
    while len(tab)>1:
        n=len(tab).bit_length()-1
        irrelevant=next((i for i in range(n) if child(tab,i,0)==child(tab,i,1)),None)
        if irrelevant is None: break
        tab=child(tab,irrelevant,0)
    return tab
def transform(tab):
    if len(tab)==1: return list(tab)
    u,v=transform(tab[::2]),transform(tab[1::2])
    out=[]
    for x,y in zip(u,v): out.extend((x+y,x-y))
    return out
def truth(st):
    if st[0]=='C': return (1,)
    kind,a,b,t,r=st
    m=2*a+b+(kind=='D' and t==2)
    def value(x):
        if x>>m: return 1
        parity=sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(a))
        if kind=='P': parity+=sum((x>>(2*a+j))&1 for j in range(b))
        v=(-1 if parity%2 else 1)*(t if kind=='P' else 1)
        if kind=='D' and not x&((1<<(2*a+b))-1) and (t==1 or (x>>(2*a+b))&1): v=-v
        return v
    return tuple(value(x) for x in range(1<<(m+r)))
class Direct:
    def __init__(self,N):
        self.N=N; self.D=1<<(2*N); self.W=1<<N; self.den=self.D*self.W
        self.memo={}; self.alternatives=0
    def spectra(self,tab):
        n=len(tab).bit_length()-1
        return [v*v*(1<<(2*(self.N-n))) for v in transform(tab)]
    def debt(self,tab,i):
        p=self.spectra(tab); z={}
        for x in range(len(p)):
            if not (x>>i)&1: z=combine((1,z),(1,phi(p[x],p[x|(1<<i)])))
        return z
    def candidates(self,tab):
        n=len(tab).bit_length()-1
        result=[]
        for i in range(n):
            t0,t1=child(tab,i,0),child(tab,i,1)
            if t0==t1: continue
            v=combine((self.W,self.debt(tab,i)),(1,A.halfsum(self.solve(t0),self.solve(t1))))
            result.append((i,v))
            self.alternatives+=1
        return result
    def solve(self,tab):
        tab=clean(tab)
        if tab in self.memo: return self.memo[tab]
        if len(tab)==1: self.memo[tab]={}; return {}
        candidates=self.candidates(tab); best=candidates[0][1]
        for _,v in candidates[1:]:
            diff=combine((1,v),(-1,best)); lo,hi=A.iv(diff)
            if not diff: continue
            if hi<0: best=v
            else: check(lo>0)
        self.memo[tab]=best
        return best
def encode(v): return {str(p):str(e) for p,e in v.items()}
def main(k):
    start=time.perf_counter(); N=3*k+1; d=Direct(N)
    cert=json.loads((RUN/'out'/f'OPTIMALITY_CERTIFICATE_K{k}.json').read_text())
    root=('D',k//2,0,2,2*k)
    value=d.solve(truth(root)); original=json.loads((RUN/'out'/f'OPTIMUM_K{k}.json').read_text())
    check(encode(value)==original['optimal_cost_log_coefficients'])
    special=[]
    for rec in cert['records']:
        st=tuple(rec['state']); val=d.solve(truth(st))
        check(encode(val)==rec['value'])
        if st[0]=='D' and st[1:4]==(1,1,2) and st[4]>=4:
            tab=truth(st); candidates=dict(d.candidates(tab)); gap=combine((1,candidates[4]),(-1,val))
            check(A.iv(gap)[0]>0)
            optimum=[i for i,v in candidates.items() if v==val]
            check(optimum==[0,1])
            special.append({'state':list(st),'dimension':len(tab).bit_length()-1,'optimal_physical_coordinates':optimum,'control_gap':A.decimal(gap,d.den),'control_gap_log_coefficients':encode(gap),'cost_denominator':d.den})
    for p,b in cert['prime_log_intervals'].items():
        lo,hi=A.logs.log2(F(int(p))); check(int(b[0])<=lo*A.Q and int(b[1])>=hi*A.Q)
    elapsed=time.perf_counter()-start
    check(elapsed<(60 if k==2 else 1200))
    out={'status':'PASS','k':k,'assertions':COUNT,'full_truth_states':len(d.memo),'actual_coordinate_alternatives':d.alternatives,'canonical_states_checked':len(cert['records']),'same_exact_root_optimum':True,'spectral_representation':'recursive even/odd Walsh, all actual query coordinates','descendant_control_first_obstructions':special,'runtime_seconds':elapsed,'helper_sha256':hashlib.sha256(A.OLD.read_bytes()).hexdigest()}
    (RUN/'out'/f'INDEPENDENT_K{k}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({key:out[key] for key in ['status','k','assertions','full_truth_states','actual_coordinate_alternatives','canonical_states_checked','runtime_seconds']}))
if __name__=='__main__': main(int(sys.argv[1]))
