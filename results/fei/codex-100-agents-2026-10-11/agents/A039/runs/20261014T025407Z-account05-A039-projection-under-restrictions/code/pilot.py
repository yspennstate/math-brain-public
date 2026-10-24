from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time
R=Path(__file__).resolve().parents[1]
P=R.parents[1]/'runs/20261011T223903Z-account05-A039-projection-under-restrictions/code/baseline_check.py'
s=importlib.util.spec_from_file_location('logs',P);L=importlib.util.module_from_spec(s);s.loader.exec_module(L)
def mul(a,b):return min(x*y for x in a for y in b),max(x*y for x in a for y in b)
def div(a,b):assert b[0]>0;return mul(a,(1/b[1],1/b[0]))
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def sumiv(vals):
    vals=list(vals);return sum((v[0] for v in vals),F(0)),sum((v[1] for v in vals),F(0))
def log(a):return L.log2(a[0])[0],L.log2(a[1])[1]
def kl(p,q):return sumiv(mul((x,x),log(div((x,x),y))) for x,y in zip(p,q) if x)
def read(a):return [str(v) for v in a]
def diag(a):return [float(x) for x in a]
def spectrum(tab):return [F(sum(v*(-1 if (s&t).bit_count()%2 else 1) for t,v in enumerate(tab))**2,len(tab)**2) for s in range(len(tab))]
def child(tab,i,y):return [v for x,v in enumerate(tab) if (x>>i)&1==y]
def fuse(p,i):return [p[x]+p[x|(1<<i)] for x in range(len(p)) if not (x>>i)&1]
def reference(c):
    d=[F(1,2),F(1,2),F(1,8),F(1,8),F(1,8)];v=F(55,64);th=[mul(c,(x/v,x/v)) for x in d];out=[]
    for s in range(32):
        if not s:out.append((F(9,64),F(9,64)));continue
        z=(v,v)
        for j in range(5):z=mul(z,th[j] if s>>j&1 else sub((1,1),th[j]))
        out.append(div(z,c))
    return out
def main():
    start=time.perf_counter();lo,hi=F(3,4),F(1)
    def g(c):return 1-c-(1-F(32,55)*c)**2*(1-F(8,55)*c)**3
    assert g(lo)>0 and g(hi)<0
    for _ in range(48):
        mid=(lo+hi)/2
        if g(mid)>0:lo=mid
        else:hi=mid
    Q=reference((lo,hi))
    tab=[]
    for t in range(32):
        x,a,b,v0,v1=[(t>>i)&1 for i in range(5)]
        tab.append(-1 if x==0 and a else (-1 if x==1 and b and v0==v1==0 else 1))
    p=spectrum(tab);q=fuse(p,1);QT=sumiv([])
    qr=[sumiv([Q[x],Q[x|2]]) for x in range(32) if not x&2]
    root=kl(p,Q);res=kl(q,qr);release=sub(root,res)
    # More accurate direct fiber sum, independent of subtracting the two KLs.
    fiber=[]
    for t in range(32):
        if t&2:continue
        total=p[t]+p[t|2];qt=sumiv([Q[t],Q[t|2]])
        if total:
            for j in [t,t|2]:
                if p[j]:fiber.append(mul((p[j],p[j]),log(div((p[j]/total,p[j]/total),div(Q[j],qt)))))
    paid=sumiv(fiber)
    rho=sumiv([(F(2),F(2)),mul((F(21,32),F(21,32)),log((F(7),F(7)))),mul((F(-25,16),F(-25,16)),log((F(5),F(5))))])
    assert paid[1]>=release[0] and paid[0]<=release[1]
    out={'status':'PILOT_PASS','c_bracket':read((lo,hi)),'root_occupancy_KL':read(root),'residual_KL':read(res),'erasure_release':read(paid),'rho':read(rho),'release_minus_rho':read(sub(paid,rho)),'diagnostic_decimals':{'c':diag((lo,hi)),'root':diag(root),'residual':diag(res),'release':diag(paid),'rho':diag(rho),'gap':diag(sub(paid,rho))},'runtime_seconds':time.perf_counter()-start}
    assert out['runtime_seconds']<60
    (R/'out/PILOT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:out[k] for k in ['status','diagnostic_decimals','runtime_seconds']}))
if __name__=='__main__':main()
