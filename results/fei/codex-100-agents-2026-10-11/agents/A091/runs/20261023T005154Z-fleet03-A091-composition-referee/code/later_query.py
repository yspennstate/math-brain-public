import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R.parent/'20261014T094139Z-fleet05-A091-composition-referee'/'code'))
import check as a
import exact as e
start=time.perf_counter()
def one(cores,r,at,fine=False,pt=None):
    u,v,g=cores
    if fine:
        gs=((1,),g);G=a.compose((0,1),gs);cs=(u,v)+gs
        zg=(1-Q(sum(g),len(g))**2)/2
    else:G=g;cs=cores;zg=1-Q(sum(g),len(g))**2
    m,n,z=[Q(sum(t),len(t)) for t in (u,v,G)]
    p=Q(sum(at),4);c=1-p;q=Q(1,1<<r) if pt is None else Q(sum(pt),2*len(pt));delta=n-z;M=1-n*z
    vv=1-n*n;vg=1-z*z;P=a.phi((1-q)**2,q*q)
    H=(1-q)*z+q*n
    K=p*m+c*H;w=q*c*delta
    root=e.add((Q(1,4),a.phi((z+K)**2,w*w)),(Q(1,4),a.phi((K-z)**2,w*w)))
    gp=e.add((Q(1,4),a.phi((1+c*(1-q))**2,q*q*c*c)),(Q(1,4),a.phi((1-c*(1-q))**2,q*q*c*c)))
    mp=a.phi((m-z-q*delta)**2,q*q*delta*delta)
    nc=r+3+int(fine);labels=[]
    for x in range(1<<nc):
        y=x&1;aa=at[(x>>1)&3]
        bb=((x>>3)&((1<<r)-1))==((1<<r)-1) if pt is None else bool(x&8) and pt[(x>>4)&3]
        fallback=2+((x>>(r+3))&1) if fine else 2
        labels.append(fallback if not y else (0 if aa else (1 if bb else fallback)))
    labels=tuple(labels);F=a.compose(labels,cs)
    B,D,d=a.local(F,3);e.check(d,q*c*M/2)
    base=(q-2*q*q)*c*M+q*q*c*vv
    rhs=e.add((1,a.const(base)),(p*c*vg/2,P),(p*c/2,mp),(vg,gp),(1,root))
    e.check(B,rhs)
    assert vv<=2*M and vg<=2*M and abs(delta)<=M and abs(m-H)<=2
    a.pos(e.add((1,a.const(q*c*M)),(-1,a.const(base))))
    a.pos(e.add((1,a.const(q*c*M)),(-1,root)))
    a.pos(e.add((1,a.const(q*c*vg)),(-vg,gp)))
    a.pos(e.add((1,a.const(p*c*q*(1-q)*vg)),(-p*c*vg/2,P)))
    a.pos(e.add((1,a.const(2*p*c*q*abs(delta))),(-p*c/2,mp)))
    a.pos(e.add((1,a.const(16*d)),(-1,B)))
    a.pos(e.add((1,a.const(19*d)),(-1,D)))
    if '--sharp' in sys.argv:
        a.pos(e.add((1,a.const((8+8*p)*d)),(-1,B)))
        a.pos(e.add((1,a.const((11+8*p)*d)),(-1,D)))
    kids=[a.cut(labels,3,b) for b in (0,1)]
    kap=e.add((1,a.reserve(labels,cs)),*[(-Q(1,2),a.reserve(k,cs)) for k in kids])
    ss=(1+c*(1-q))/2;s0=(1+c)/2;s1=(1+c*(1-2*q))/2
    kg=e.add((1,a.eta(ss)),(-Q(1,2),a.eta(s0)),(-Q(1,2),a.eta(s1)))
    expected=e.add((1,a.const(c*q*vv/2)),(zg,kg))
    e.check(kap,expected);a.pos(kap)
    return d==0
def main():
    cases=zeros=0
    if '--pilot' in sys.argv:
        for at,r in [((0,1,1,0),1),((0,1,1,1),2)]:
            zero=one(((-1,1),(-1,-1,-1,1),(1,-1)),r,at)
            assert not zero;cases+=1
        name='PILOT';domain='two nonzero-influence fixtures'
    elif '--arbitrary-p' in sys.argv:
        pool=tuple(e.tab(k,1) for k in range(4))
        for cores,mask in itertools.product(itertools.product(pool,repeat=3),range(16)):
            zeros+=one(cores,3,(0,1,1,0),pt=tuple((mask>>i)&1 for i in range(4)));cases+=1
            if time.perf_counter()-start>55:raise RuntimeError('frozen watchdog')
        name='ARBITRARY_P';domain='all16 P indicators times all64 sign-core triples, XOR2 A'
    else:
        lo,hi=map(int,sys.argv[1:3]);pool=tuple(e.tab(k,1) for k in range(4))
        for j,(cores,r,mask) in enumerate(itertools.product(itertools.product(pool,repeat=3),(1,2,3),range(16))):
            if not lo<=j<hi:continue
            zeros+=one(cores,r,tuple((mask>>i)&1 for i in range(4)));cases+=1
            if time.perf_counter()-start>55:raise RuntimeError('frozen watchdog')
        if '--supplement' in sys.argv:
            base=((-1,-1,-1,1),(-1,1,1,1),(-1,-1,-1,1))
            for r in (1,2):
                zeros+=one(base,r,(0,1,1,1));cases+=1
                for j in range(3):
                    for b in (0,1):
                        cs=list(base);cs[j]=a.cut(cs[j],0,b)
                        zeros+=one(tuple(cs),r,(0,1,1,1));cases+=1
            for mask in range(8):
                zeros+=one(base,1,tuple((mask>>i)&1 for i in range(4)),True);cases+=1
        name=f'CHECK_{lo}_{hi}';domain=[lo,hi]
    name+= '_SHARP' if '--sharp' in sys.argv else ''
    out={'status':'PASS','domain':domain,'cases':cases,'zero_influence_cases':zeros,'exact_assertions':e.COUNT,'seconds':time.perf_counter()-start,'arithmetic':'Fraction FWHT, prime-log identities, rational outward atanh enclosure','scope':'B<=(8+8EA)d and D<=(11+8EA)d' if '--sharp' in sys.argv else 'B<=16d, D<=19d, original fine reserve and grouped identity'}
    (R/'out').mkdir(exist_ok=True)
    (R/'out'/f'{name}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
