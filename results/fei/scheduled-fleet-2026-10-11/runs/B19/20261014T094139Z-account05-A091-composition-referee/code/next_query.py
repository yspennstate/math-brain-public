import check as a
import exact as e
from fractions import Fraction as Q
from pathlib import Path
import itertools,json,time,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
def case(us,r):
    u,v,g=us;cores=(u,v,(1,),g)
    # Other controls are B and the actual private G activation, followed by u,v,G data.
    Hl=tuple(1 if z&1 else 2+((z>>1)&1) for z in range(4));Gl=tuple(2+((z>>1)&1) for z in range(4));Ul=(0,)*4
    H=a.compose(Hl,cores);G=a.compose(Gl,cores);U=a.compose(Ul,cores)
    fine=[]
    for x in range((1<<(r+1))*len(H)):
        y=x&1;A=((x>>1)&((1<<r)-1))==((1<<r)-1);z=(x>>(r+1))&3
        fine.append(Gl[z] if not y else (0 if A else Hl[z]))
    F=a.compose(tuple(fine[:1<<(r+3)]),cores) # labels on Y,A,B,G controls, then disjoint actual data
    labels=tuple(fine[:1<<(r+3)]);q=Q(1,1<<r);p=Q(1,2);m=sum(u,Q(0))/len(u);n=sum(H,Q(0))/len(H)
    B,D,I=a.local(F,1);e.check(I,q*(1-m*n)/2)
    uc,hc,gc=map(a.coeff,(U,H,G)); terms=[]
    for uu,hh,gg in zip(uc,hc,gc):
        L=(1-q)*hh+q*uu;w=q*(uu-hh)
        terms.extend([(1,a.phi((gg+L)**2/4,w*w/4)),(1,a.phi((L-gg)**2/4,w*w/4))])
    rhs=e.add((1,a.const((q-2*q*q)*(1-m*n))),*terms);e.check(B,rhs)
    k=e.add((1,a.eta(1-q)),(-Q(1,2),a.eta(1-2*q)))
    s=(1+(1-q)*(1-p))/2;s0=(2-p)/2;s1=(1+(1-2*q)*(1-p))/2
    kg=e.add((1,a.eta(s)),(-Q(1,2),a.eta(s0)),(-Q(1,2),a.eta(s1)))
    vu=1-m*m;vv=1-(sum(v,Q(0))/len(v))**2;zg=(1-(sum(g,Q(0))/len(g))**2)/2
    kap=e.add((1,a.const(q*vu/2)),(p*vv/2,k),(zg,kg))
    lc=[tuple(labels[(x&1)+((x>>1)<<2)+(b<<1)] for x in range(len(labels)//2)) for b in [0,1]]
    actual=e.add((1,a.reserve(labels,cores)),*[(-Q(1,2),a.reserve(l,cores)) for l in lc]);e.check(actual,kap);a.pos(kg)
def main():
    pool=tuple(e.tab(mask,1) for mask in range(4));cases=0
    for idx,us in enumerate(itertools.product(pool,repeat=3)):
        if pilot and idx>=2:break
        for r in [1,2,3]:case(us,r);cases+=1
    if not pilot:
        base=((-1,-1,-1,1),(-1,-1,-1,1),(-1,-1,-1,1))
        for r in [1,2]:
            case(base,r);cases+=1
            for j in range(3):
                for b in [0,1]:
                    us=list(base);us[j]=a.cut(us[j],0,b);case(tuple(us),r);cases+=1
    out={'status':'PASS','cases':cases,'exact_assertions':e.COUNT,'seconds':time.perf_counter()-start,'pilot':pilot,'scope':'exact unpaid first-private-query erasure and merged reserve only; no uniform payment asserted'}
    (R/'out'/('NEXT_PILOT.json' if pilot else 'NEXT_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
