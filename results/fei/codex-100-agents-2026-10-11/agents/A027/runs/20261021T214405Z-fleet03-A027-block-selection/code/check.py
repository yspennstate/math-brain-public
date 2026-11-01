import exact as x
import itertools,json,time,sys,hashlib
from pathlib import Path
Q=x.Q
run=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv
def log(q):
    return x.add((1,x.factor(q.numerator)),(-1,x.factor(q.denominator)))
def Ap(d):
    return x.add((4-8*d,{2:Q(1)}),(-4*d,log(d)),(4*(1-d),log(1-d)),(-4*(1-2*d),log(1-2*d)))
def D(p,d):
    return x.add((1,log(1-2*d)),(-(1-p),log(2*d)),(-p,log(1-2*p*d)),(p,log(p)))
def saved_expr(e):
    lo,hi=x.bounds(e)
    return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(lo),str(hi)]}
s=Q(1,16);b=Q(3,10)
tangent=x.add((1,x.R(Q(1,2),b)),(-1,x.R(Q(1,2),s)),(-(b-s),Ap(s)))
x.check(x.bounds(tangent)[0]>Q(17,1000),'exact positive endpoint tangent margin >17/1000')
scalar=[]
if not pilot:
    for d in [Q(k,64) for k in range(1,19)]+[Q(2,7)]:
        difference=x.add((1,D(Q(1,4),d)),(-1,D(Q(1,2),d)))
        formula=x.add((Q(1,4),log((1-d)**2/(d*(2-d)))))
        x.check(difference==formula,'independent controller curvature comparison formula')
        x.check(x.bounds(difference)[0]>0,'quarter-versus-balanced curvature sign')
        for p in [Q(1,2),Q(1,4),Q(1,8),Q(1,16)]:
            diff=x.add((1,D(p,d)),(-1,D(Q(1,2),d)))
            x.check(x.bounds(diff)[0]>=0,'eligible controller curvature comparison')
    excluded=x.add((1,D(Q(3,8),Q(2,7))),(-1,D(Q(1,2),Q(2,7))))
    x.check(x.bounds(excluded)[1]<0,'excluded middle controller range cannot use curvature comparison')
    scalar.append({'excluded_p':'3/8','d':'2/7',**saved_expr(excluded)})
sets=[set(),{0},{0,1,2},{0,1,2,3},{0,1,2,4}]
children=[tuple(-1 if i in z else 1 for i in range(16)) for z in sets]
controllers=[]
for n in range(3):
    controllers += [a for a in itertools.product((-1,1),repeat=1<<n) if x.neg(a)<=Q(1,4) or x.neg(a)==Q(1,2)]
controllers += [(-1,)+(1,)*7]
if pilot:
    children=children[2:4];controllers=[(-1,1)]
cases=0;positive=0;witness=None
for a in controllers:
    p=x.neg(a)
    for g,h in itertools.product(children,repeat=2):
        u=tuple((g[j>>3] if not(j&4) else h[j>>3]) if not(j&3) else 1 for j in range(128))
        f=x.identity(u,a);d=x.neg(u)
        x.check(d<=s,'actual root bias admission')
        local=[];qcore=Q(0);qact=Q(0)
        partial={}
        for fixed,w,j in [((),Q(1),0),(((0,0),),Q(1,2),1),(((0,0),(1,0)),Q(1,4),2)]:
            v=x.restrict(u,fixed);v0=x.restrict(u,tuple(sorted(fixed+((j,0),))));v1=x.restrict(u,tuple(sorted(fixed+((j,1),))))
            fv=x.identity(v,a);f0=x.identity(v0,a);f1=x.identity(v1,a)
            e=x.add((1,x.R(p,x.neg(v))),(Q(-1,2),x.R(p,x.neg(v0))),(Q(-1,2),x.R(p,x.neg(v1))))
            direct=x.add((1,x.H(fv)),(Q(-1,2),x.H(f0)),(Q(-1,2),x.H(f1)),(-p,x.H(v)),(p/2,x.H(v0)),(p/2,x.H(v1)))
            x.check(direct==e,'actual full local signed correction')
            partial=x.add((1,partial),(w,e))
            x.check(x.bounds(partial)[1]<=0,'SAME ancestor account nonnegative at every prefix')
            idx=j-sum(i<j for i,_ in fixed)
            qcore+=w*x.inf(v,idx);qact+=w*x.inf(fv,idx)
            local.append(e)
        leaves=[(((0,1),),Q(1,2)),(((0,0),(1,1)),Q(1,4)),(((0,0),(1,0),(2,0)),Q(1,8)),(((0,0),(1,0),(2,1)),Q(1,8))]
        leafH={};coreH={};leafI=Q(0);coreI=Q(0);mean=Q(0)
        for fixed,w in leaves:
            v=x.restrict(u,fixed);fv=x.identity(v,a);e=x.neg(v)
            x.check(x.restrict(f,fixed)==fv,'actual complete activated terminal')
            x.check(1-4*e+2*e*e>=0 and e<Q(1,2),'complete leaf endpoint band')
            leafH=x.add((1,leafH),(w,x.H(fv)));coreH=x.add((1,coreH),(w,x.H(v)))
            leafI+=w*x.I(fv);coreI+=w*x.I(v);mean+=w*e
        x.check(mean==d,'actual leaf bias martingale')
        x.check(qact==p*qcore,'physical data-query scaling')
        x.check(x.I(u)==qcore+coreI,'full core influence partition')
        x.check(x.I(f)==qact+leafI,'full activated influence partition')
        x.check(leafI==p*coreI+d*x.I(a),'original controller owner entirely retained')
        actual=x.add((1,x.H(f)),(-1,leafH),(-p,x.H(u)),(p,coreH))
        x.check(actual==partial,'full endpoint telescoping including BOTH terminals')
        x.check(x.bounds(actual)[1]<=0,'paid full signed endpoint correction')
        if x.bounds(local[-1])[0]>0:
            positive+=1
            if p==Q(1,2) and x.neg(g)==Q(3,16) and x.neg(h)==Q(1,4) and witness is None:
                witness={'root_bias':str(d),'controller_p':str(p),'positive_exit':saved_expr(local[-1]),'prior_refund':saved_expr(x.add((-1,local[0]),(Q(-1,2),local[1]))),'final_refund':saved_expr(x.add((-1,actual))),'full_terminal_entropy':saved_expr(leafH),'root_I':str(x.I(f)),'queried_I':str(qact),'full_terminal_I':str(leafI),'query_order':[0,1,2],'child_negative_sets':[sorted(sets[2]),sorted(sets[3])]}
        cases+=1
    for fn in [x.spectrum,x.H,x.inf,x.I,x.restrict,x.activate,x.identity]:fn.cache_clear()
x.check(witness is not None,'actual positive-exit same-owner witness exists')
result={'status':'PASS','cases':cases,'controllers':len(controllers),'positive_local_exits':positive,'assertions':sum(x.counts.values()),'counts':x.counts,'elapsed_seconds':time.monotonic()-x.START,'tangent_certificate':saved_expr(tangent),'hypothesis_stress':scalar,'witness':witness,'helper_sha256':hashlib.sha256((run/'code/exact.py').read_bytes()).hexdigest()}
(run/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['counts','witness','tangent_certificate','hypothesis_stress']}))
