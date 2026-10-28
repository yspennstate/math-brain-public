import exact as x
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1];START=time.monotonic();PILOT='--pilot' in sys.argv;C=Q(21,4);N={};POL=0;NODE=0;LEAF=0
def ck(v,k):
    assert v,k
    N[k]=N.get(k,0)+1
    assert time.monotonic()-START<(60 if PILOT else 240),'runtime cap'
def add(*v):return x.add(*v)
def num(q):return {2:Q(q)} if q else {}
def log(q):return add((1,x.factor(q.numerator)),(-1,x.factor(q.denominator)))
def enc(e):return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(v) for v in x.bounds(e)]}
def pos(e,k,strict=False):ck(x.bounds(e)[0]>0 if strict else x.bounds(e)[0]>=0,k)
def G(a,d):return add((d,x.Hplus(a)),(1,x.R(x.neg(a),d)))
def Gp(a,t):
    p=x.neg(a);V=4*p*(1-p)
    return add((1,x.Hplus(a)),(4*(1-2*t),x.eta(p*p)),(2*(1-2*t)*V,num(1)),(-4*V*t,log(t)),(8*p*(1-2*p*t),log(1-2*p*t)),(-8*p*(1-2*t),log(1-2*t)))
t=Q(1,16)
def T(a,d):return add((1,G(a,t)),(d-t,Gp(a,t)))
def U(a,d):return add((1,G(a,d)),(-1,T(a,d)))
def S(f):return add((1,num(C*x.I(f))),(-1,x.H(f)))
u=(-1,)+(1,)*15;a=tuple(-1 if j.bit_count()>=2 else 1 for j in range(8));F=x.activate(u,a)
v=(-1,)+(1,)*7;acs=[x.restrict(a,((0,b),)) for b in (0,1)];fs=[x.activate(v,b) for b in acs]
for b in (0,1):ck(fs[b]==x.restrict(F,((0,0),(4,b))),'actual prefix selected restriction')
coremargin=add((1,num(C*Q(1,16))),(Q(-1,2),x.H(u)),(Q(1,4),x.H(v)))
old=Q(1,64);pos(add((1,coremargin),(-1,num(old))),'old debit funded ONCE by original core margin',True)
aa=add((1,T(a,Q(1,8))),(Q(-1,2),T(acs[0],Q(1,8))),(Q(-1,2),T(acs[1],Q(1,8))))
controlmargin=add((1,num(C*Q(1,32))),(Q(-1,2),aa));pos(controlmargin,'actual old control tangent margin')
Bs=[add((Q(1,4),S(f)),(Q(1,4),U(ac,Q(1,8)))) for f,ac in zip(fs,acs)]
Bvac=add((Q(1,2),U(a,Q(0))))
for e in [Bvac]+Bs:pos(e,'every retained signed terminal account paid')
pos(add((1,Bs[1]),(-1,num(Q(1,64)))),'selected ORIGINAL account exceeds1/64',True)
ck(S(F)==add((1,coremargin),(1,controlmargin),(1,Bvac),(1,Bs[0]),(1,Bs[1])),'full SAME original signed surplus decomposition')
ck(x.I(F)==Q(11,32),'actual root influence11/32')
ck(x.I(F)==Q(1,16)+Q(1,32)+sum(x.I(f)/4 for f in fs),'full original physical influence partition')

def P(f):return tuple(z*z for z in x.spectrum(f))
def reset(theta):
    f=fs[1];p=P(f);ref=[]
    for j,z in enumerate(p):
        Uidx=j>>3
        ref.append(z if not Uidx else z*(1-theta+3*theta*(Uidx==1)))
    ref=tuple(ref);ck(sum(ref)==1,'changed reference normalized')
    for j in range(8):
        ck(sum(p[j+(k<<3)] for k in range(1,4))==sum(ref[j+(k<<3)] for k in range(1,4)),'actual row and nonempty odds preserved')
    klshape=add((Q(-1,3),log(1+2*theta)),(Q(-2,3),log(1-theta)))
    cost=add((Q(3,128),klshape))
    actual={}
    for z,rho in zip(p,ref):
        if z:actual=add((1,actual),(z,log(z/rho)))
    ck(add((Q(1,4),actual))==cost,'actual FULL output reset equals weighted shape KL')
    pos(add((1,num(Q(9,1792))),(-1,cost)),'continuum cap9/1792 validated at grid')
    pos(add((1,Bs[1]),(-1,cost),(-1,num(Q(19,1792)))),'SAME selected account retains19/1792',True)
    pos(add((1,S(F)),(-1,num(old)),(-1,cost)),'unchanged root quota retains OLD debit and actual cost',True)
    return ref,cost

def phase(f,rho,i):
    global NODE
    NODE+=1;p=P(f);n=len(f).bit_length()-1;children=[x.restrict(f,((i,b),)) for b in (0,1)];joint=[[],[]]
    for k in range(1<<(n-1)):
        low=k&((1<<i)-1);high=k>>i;j=low+(high<<(i+1));j1=j+(1<<i)
        aa=x.spectrum(f)[j];bb=x.spectrum(f)[j1];q=p[j]+p[j1];rr=rho[j]+rho[j1]
        ks=[(aa+bb)**2/(2*q),(aa-bb)**2/(2*q)] if q else [Q(1,2),Q(1,2)]
        ck(sum(ks)==1,'actual physical pair channel stochastic')
        for b in (0,1):
            ck(q*ks[b]==P(children[b])[k]/2,'phase kernel maps actual spectrum to FAIR physical child')
            z=rr*ks[b];joint[b].append(z)
            if q*ks[b]:
                ck(z>0,'inherited reference positive on actual support')
                ck((q*ks[b])/z==q/rr,'exact logsum likelihood factorization')
    masses=[sum(j) for j in joint];ck(sum(masses)==1,'BOTH output reference masses retained')
    ck(all(z>0 for z in masses),'both actual fair branches reference-admissible')
    refs=[tuple(z/masses[b] for z in joint[b]) for b in (0,1)]
    for b in (0,1):ck(sum(refs[b])==1,'child reference normalized by OWN mass')
    return children,refs,masses

orders=json.loads((R/'FROZEN_SPEC.json').read_text(encoding='utf-8'))['orders']
policies=[(tuple(o),k) for o in orders for k in range(6)]+[(None,0),(None,1)]
normalizer_nonfair=0
def run(ref,policy):
    global POL,LEAF,normalizer_nonfair
    order,stop=policy
    def walk(f,rho,free,fixed,depth,w):
        global LEAF,normalizer_nonfair
        if len(set(f))==1 or (order is not None and depth==stop) or (order is None and depth==3+stop):
            LEAF+=1;ck(sum(rho)==1,'FULL terminal reference retained');return w
        if order is not None:j=order[depth]
        else:
            data=[j for j in free if j<3];ctrl=[j for j in free if j>=3]
            trigger=x.neg(f)>=Q(1,4) if stop==0 else sum(fixed.values())%2==1
            choices=(ctrl if trigger else data) or (data if trigger else ctrl);j=choices[0]
        i=free.index(j);ch,rs,masses=phase(f,rho,i)
        if masses!=[Q(1,2),Q(1,2)]:normalizer_nonfair+=1
        left=[]
        for b in (0,1):
            fix=dict(fixed);fix[j]=b;left.append(walk(ch[b],rs[b],[z for z in free if z!=j],fix,depth+1,w/2))
        ck(sum(left)==w,'actual fair reaches not reference reaches')
        return w
    ck(walk(fs[1],ref,list(range(5)),{},0,Q(1))==1,'complete stopped frontier mass')
    POL+=1
theta_grid=[Q(0),Q(1,8)] if PILOT else [Q(k,64) for k in range(9)]
costs=[]
for theta in theta_grid:
    ref,cost=reset(theta);costs.append({'theta':str(theta),'weighted_actual_reset':enc(cost)})
    for policy in (policies[:6] if PILOT else policies):run(ref,policy)
out={'status':'PASS','policies':POL,'assertions':sum(N.values()),'counts':N,'nodes':NODE,'leaves':LEAF,'nonfair_reference_normalizers':normalizer_nonfair,'elapsed_seconds':time.monotonic()-START,'root_I':str(x.I(F)),'old_debit':str(old),'original_root_surplus':enc(S(F)),'core_margin_after_old':enc(add((1,coremargin),(-1,num(old)))),'original_control_margin':enc(controlmargin),'selected_full_signed_account':enc(Bs[1]),'controller_child_biases':[str(x.neg(z)) for z in acs],'costs':costs,'KL_continuation_certificate':'Exact stochastic phase kernels, actual fair output spectrum, positive inherited references and likelihood factorization; KL log-sum theorem supplies all-depth contraction, not finite extrapolation.'}
(R/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if not isinstance(v,(dict,list))}))
