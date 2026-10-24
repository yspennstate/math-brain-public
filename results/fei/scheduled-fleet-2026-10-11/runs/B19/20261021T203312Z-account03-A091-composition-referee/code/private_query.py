import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261014T094139Z-account05-A091-composition-referee'/'code'
sys.path.insert(0,str(OLD))
import check as a
import exact as e
start=time.perf_counter()
def one(cores,r,bt):
    u,v,g=cores
    q=Q(1,1<<r);p=Q(sum(bt),len(bt))
    m,n,z=[Q(sum(t),len(t)) for t in cores]
    h=p*n+(1-p)*z;M=1-m*h
    vu,vv,vg=[1-x*x for x in (m,n,z)]
    vh=1-h*h;c=1-p
    S=p*vv+p*(1-p)*(vg+(n-z)**2)
    e.check(S,vh-c*c*vg)
    # Controls are Y, r A bits, then two B bits; each core occurs once.
    labels=[]
    for x in range(1<<(r+3)):
        y=x&1;aa=((x>>1)&((1<<r)-1))==((1<<r)-1)
        bb=bt[(x>>(r+1))&3]
        labels.append(2 if not y else (0 if aa else (1 if bb else 2)))
    labels=tuple(labels);F=a.compose(labels,cores)
    B,D,I=a.local(F,1);e.check(I,q*M/2)
    L=(1-q)*h+q*m;w=q*(m-h)
    root=e.add((Q(1,4),a.phi((z+L)**2,w*w)),(Q(1,4),a.phi((L-z)**2,w*w)))
    cp=e.add((Q(1,4),a.phi((1+(1-q)*c)**2,q*q*c*c)),(Q(1,4),a.phi(((1-q)*c-1)**2,q*q*c*c)))
    rhs=e.add((1,a.const((q-2*q*q)*M+q*q*vu)),(S/2,a.phi((1-q)**2,q*q)),(vg,cp),(1,root))
    e.check(B,rhs)
    # Check each load-bearing analytic majorization separately.
    assert vu<=2*M and vh<=2*M and c*vg<=vh and S>=0
    a.pos(e.add((1,a.const(q*M)),(-1,a.const((q-2*q*q)*M+q*q*vu))))
    a.pos(e.add((1,a.const(q*M)),(-1,root)))
    a.pos(e.add((1,a.const(q*(1-q)*S)),(-S/2,a.phi((1-q)**2,q*q))))
    a.pos(e.add((1,a.const(q*c*vg)),(-vg,cp)))
    a.pos(e.add((1,a.const(12*I)),(-1,B)))
    a.pos(e.add((1,a.const(15*I)),(-1,D)))
    # Actual physically merged reserve, including deterministic cores.
    kids=[tuple(labels[(x&1)+((x>>1)<<2)+(b<<1)] for x in range(len(labels)//2)) for b in (0,1)]
    release=e.add((1,a.reserve(labels,cores)),*[(-Q(1,2),a.reserve(k,cores)) for k in kids])
    k=e.add((1,a.eta(1-q)),(-Q(1,2),a.eta(1-2*q)))
    ss=(1+(1-q)*(1-p))/2;s0=(2-p)/2;s1=(1+(1-2*q)*(1-p))/2
    kg=e.add((1,a.eta(ss)),(-Q(1,2),a.eta(s0)),(-Q(1,2),a.eta(s1)))
    kap=e.add((1,a.const(q*vu/2)),(p*vv/2,k),(vg,kg))
    e.check(release,kap);a.pos(kap)
    return I==0
def main():
    pilot='--pilot' in sys.argv
    lo=int(sys.argv[1]);hi=int(sys.argv[2]);pool=tuple(e.tab(i,1) for i in range(4))
    cases=zeros=0
    for j,(cores,r,mask) in enumerate(itertools.product(itertools.product(pool,repeat=3),(1,2,3),range(16))):
        if not lo<=j<hi:continue
        bt=tuple((mask>>i)&1 for i in range(4));zeros+=one(cores,r,bt);cases+=1
        if time.perf_counter()-start>55:raise RuntimeError('frozen watchdog')
    if '--supplement' in sys.argv:
        base=((-1,-1,-1,1),(-1,1,1,1),(-1,-1,-1,1))
        for r in (1,2):
            zeros+=one(base,r,(0,1,1,1));cases+=1
            for j in range(3):
                for b in (0,1):
                    cs=list(base);cs[j]=a.cut(cs[j],0,b)
                    zeros+=one(tuple(cs),r,(0,1,1,1));cases+=1
    out={'status':'PASS','range':[lo,hi],'cases':cases,'zero_influence_cases':zeros,'exact_assertions':e.COUNT,'runtime_seconds':time.perf_counter()-start,'pilot':pilot,'arithmetic':'Fraction FWHT and prime-log identity; outward rational atanh log enclosure'}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/f'CHECK_{lo}_{hi}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
if __name__=='__main__':main()
