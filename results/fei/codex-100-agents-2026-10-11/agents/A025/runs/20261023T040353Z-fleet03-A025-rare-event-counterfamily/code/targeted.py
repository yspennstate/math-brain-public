"""Bounded t=3 target audit; exact GCD-log algebra, no phase factoring."""
from pathlib import Path
import time,json,math
import independent as A
from exact import fwht
from a022_source import qdata
F=A.F; root=Path(__file__).resolve().parents[1]
def law(f):
    n=len(f); return [F(w*w,n*n) for w in fwht(f)]
def Rlaw(a,d):
    r=[d*p for p in law(a)]; r[0]+=1-d; return r
def stats(nodes,depth,ref):
    Cs=[]; Hs=[]; Id=F(0); ndata=9-depth; M=2**ndata; labels=tuple(range(depth,9))
    for ff,fixed in nodes:
        p=law(ff); q=qdata(3,labels,fixed); T=[r*x for r in ref for x in q]
        Cs.append(A.cross(p,T)); Hs.append(A.ent(p)); Id+=sum((p[s]*(s&(M-1)).bit_count() for s in range(len(p))),F(0))/len(nodes)
    return A.mean(Cs),A.mean(Hs),Id
def main():
    start=time.perf_counter(); cases=0; delta=F(1,512); U=F(3,64)
    for v in (0,511):
        for table in range(16):
            a=tuple(1-2*((table>>z)&1) for z in range(4)); R=Rlaw(a,delta); L=A.scale(A.ent(law(a)),delta)
            f=[]
            for z in range(4):
                for x in range(512):
                    seed=math.prod(-1 if ((x>>(3*b))&7)==0 else 1 for b in range(3))
                    f.append(seed*(a[z] if x==v else 1))
            nodes=[(tuple(f),())]
            for depth in range(1,7):
                nodes=[(A.cut(ff,0,b),fixed+((depth-1,b),)) for ff,fixed in nodes for b in (0,1)]
                if depth not in (1,2,5,6): continue
                Cp,Hp,Ip=stats(nodes,depth,R); Bp=A.add(A.c(4*Ip-U),L,A.scale(Cp,-1))
                A.ge(A.add(Bp,A.c(-F(39,576))),'t3 original source admission')
                for i in (0,1):
                    ac=[A.cut(a,i,b) for b in (0,1)]; Rs=[Rlaw(ab,delta) for ab in ac]
                    vals=[stats([(A.cut(ff,9-depth+i,b),fixed) for ff,fixed in nodes],depth,Rs[b]) for b in (0,1)]
                    Cc=A.mean([r[0] for r in vals]); Hc=A.mean([r[1] for r in vals]); Ic=sum(r[2] for r in vals)/2
                    Lc=A.mean([A.scale(A.ent(law(ab)),delta) for ab in ac]); Bc=A.add(A.c(4*Ic-U),Lc,A.scale(Cc,-1))
                    gamma=A.add(A.overhead(F(sum(a),4),delta),A.scale(A.mean([A.overhead(F(sum(ab),2),delta) for ab in ac]),-1))
                    A.ck(Ip==Ic,'actual t3 influence preserved')
                    A.ck(A.same(A.add(Bc,A.scale(Bp,-1)),gamma),'t3 exact same-bank gain')
                    A.ge(gamma,'t3 controller overhead release')
                    A.ge(A.add(Bc,A.c(-F(39,576))),'t3 reserve retained')
                    A.ck(A.same(A.add(Bc,Cc,A.scale(Hc,-1),L,A.scale(Lc,-1),A.scale(Hp,-1),Hc),A.add(Bp,Cp,A.scale(Hp,-1))),'t3 BOTH terminal KL and source history')
                    cases+=1
                if time.perf_counter()-start>120: raise RuntimeError('bounded target cap')
    out={'status':'PASS','cases':cases,'assertions':A.count,'seconds':time.perf_counter()-start,'physical_phase_audit':False,'arithmetic':'GCD-refined rational-log exact identities/Fraction/FWHT'}
    (root/'out/targeted.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
if __name__=='__main__': main()
