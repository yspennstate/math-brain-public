"""Independent conditional DATA transforms; imports no production helper."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
root=Path(__file__).resolve().parents[1]
start=time.monotonic();checks=0;paths=0
delta=Q(1,64)
def character(s,x):return -1 if (s&x).bit_count()%2 else 1
def b(x):return (-1 if (x&7)==0 else 1)*(-1 if (x>>3)==0 else 1)
H=[Q(sum(b(x)*character(S,x) for x in range(64)),64) for S in range(64)]
for am,cm in [(15,23),(15,232),(15,240),(23,105)]:
    a=[1 if am>>j&1 else -1 for j in range(8)]
    c=[1 if cm>>j&1 else -1 for j in range(8)]
    corr=Q(sum(x*y for x,y in zip(a,c)),8)
    rows=[]
    for z in range(8):
        f=[a[z] if x==0 else -c[z] if x==1 else b(x) for x in range(64)]
        rows.append([Q(sum(f[x]*character(S,x) for x in range(64)),64) for S in range(64)])
    for S in range(64):
        e=character(S,1);B=H[S]-delta*(1-e)
        mean=Q(sum(row[S] for row in rows),8)
        marginal=Q(sum(row[S]**2 for row in rows),8)
        assert mean==B;checks+=1
        assert marginal==B*B+delta*delta*(2-2*e*corr);checks+=1
    for j in range(3):
        u=Q(sum(a[z]*character(1<<j,z) for z in range(8)),8)
        v=Q(sum(c[z]*character(1<<j,z) for z in range(8)),8)
        w=Q(sum(a[z]*c[z]*character(1<<j,z) for z in range(8)),8)
        if abs(u)>Q(1,2) or abs(v)>Q(1,2):continue
        for lam in [Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)]:
            s,t,r=lam*u,lam*v,corr+lam*w
            # Joint-law positivity includes boundary and degenerate correlations.
            for av in (-1,1):
                for cv in (-1,1):assert 1+av*s+cv*t+av*cv*r>=0;checks+=1
            for S in range(64):
                e=character(S,1);B=H[S]-delta*(1-e)
                A=B+delta*(s-e*t)
                M=B*B+2*delta*B*(s-e*t)+delta*delta*(2-2*e*r)
                Mp=2*delta*B*(u-e*v)-2*e*delta*delta*w
                assert abs(A)>=delta and M>=A*A;checks+=1
                assert abs(Mp)/M<=4*(abs(u)+abs(v))+2*abs(w);checks+=1
            paths+=1
assert Q(3,2)*(Q(1,32)+Q(1,8)+72)+Q(5,64)<110;checks+=1
assert 6*13+3*55+6*13==321<336;checks+=1
out={'status':'PASS','assertions':checks,'sampled_light_paths':paths,'seconds':time.monotonic()-start,'representation':'direct conditional DATA character sums; actual joint-law moments; exact Fraction; no production imports','scope':'independent implementation by author, not independent-person acceptance'}
(root/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
