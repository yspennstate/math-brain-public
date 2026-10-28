import base as b
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import json,time,sys
x=b.x;R=Path(__file__).resolve().parents[1];START=time.monotonic();PILOT='--pilot' in sys.argv;N={};POL=NODE=LEAF=DIFF=0;c=Q(4,9)
def ck(v,k):
    assert v,k
    N[k]=N.get(k,0)+1
    assert time.monotonic()-START<(60 if PILOT else 240),'runtime cap'
def add(*v):return x.add(*v)
def num(q):return b.num(q)
def pos(e,k):ck(x.bounds(e)[0]>=0,k)
def log(q):return b.log(q)
def enc(e):return b.enc(e)
def P(f):return tuple(z*z for z in x.spectrum(f))
def D(p,r):return add(*[(z,log(z/v)) for z,v in zip(p,r) if z])
def binary(k,l):return D((1-k,k),(1-l,l))
def ell(k,lam):return lam*k/(1+(lam-1)*k)
ck(Q(842,1215)>Q(9,13),'rational log lower certificate')
ck(Q(25,36)<Q(3,4),'rational log upper certificate')
ck(Q(1,64)-Q(9,1792)-Q(1,96)==Q(1,5376),'original residual exact1/5376')
ck(Q(3,256)-Q(19,1792)==Q(1,896),'old eta/2 insufficient for SAVED FLOOR only')
ks=[Q(0),Q(1,64),Q(1,2),Q(1)] if PILOT else [Q(j,64) for j in range(65)]
ls=[Q(1,2),Q(1),Q(2)] if PILOT else [Q(j,16) for j in range(8,33)]
for k in ks:
    for lam in ls:
        ee=ell(k,lam);d=binary(k,ee)
        ck(d==add((1,log(1+(lam-1)*k)),(-k,log(lam))),'binary relative-odds exact identity')
        pos(add((1,num(c*k)),(-1,d)),'rational4/9 scalar envelope')

@lru_cache(None)
def phase(f,rho,i):
    p=P(f);h=x.spectrum(f);n=len(f).bit_length()-1;ch=[x.restrict(f,((i,z),)) for z in (0,1)];raw=[[],[]]
    for k in range(1<<(n-1)):
        j=(k&((1<<i)-1))+((k>>i)<<(i+1));j1=j+(1<<i);q=p[j]+p[j1];rr=rho[j]+rho[j1]
        probs=[(h[j]+h[j1])**2/(2*q),(h[j]-h[j1])**2/(2*q)] if q else [Q(1,2),Q(1,2)]
        ck(sum(probs)==1,'phase kernel stochastic')
        for z in (0,1):
            ck(q*probs[z]==P(ch[z])[k]/2,'physical outcome FAIR, not reference-normalized')
            raw[z].append(rr*probs[z])
    zs=tuple(sum(z) for z in raw);ck(sum(zs)==1 and min(zs)>0,'both reference outcome masses retained')
    refs=tuple(tuple(v/zs[j] for v in raw[j]) for j in (0,1))
    refund=add((1,D(p,rho)),(Q(-1,2),D(P(ch[0]),refs[0])),(Q(-1,2),D(P(ch[1]),refs[1])))
    outcome=D((Q(1,2),Q(1,2)),zs);erased=add((1,refund),(-1,outcome))
    pos(outcome,'own output outcome KL refund');pos(erased,'actual erased-pair KL refund')
    return tuple(ch),refs,zs,refund

@lru_cache(None)
def state(v,a,ra,depth,mode):
    f=x.activate(v,a);p=P(f);m=len(v);gamma=x.neg(v);va=1-x.spectrum(a)[0]**2;eta=gamma*va;beta=1-ra[0]
    TT=add((gamma,D(P(a),ra)));vac=binary(va,beta);SS=add((gamma,vac));newT=add((1,TT),(1,num(c*eta)))
    ref=[Q(0)]*len(f);cost={}
    for t in range(m):
        q=sum(p[t+u*m] for u in range(len(a)));w=sum(p[t+u*m] for u in range(1,len(a)))
        if not q:continue
        k=w/q
        lam=Q(1) if depth==0 else (Q(2) if mode==0 else ([Q(1,2),Q(2)][t%2] if mode==1 else [Q(1,2),Q(1),Q(2)][(depth+t)%3]))
        ll=ell(k,lam);cost=add((1,cost),(q,binary(k,ll)));ref[t]=q*(1-ll)
        if ll:
            ck(beta>0,'nonempty external shape exists')
            for u in range(1,len(a)):ref[t+u*m]=q*ll*ra[u]/beta
    ref=tuple(ref);ck(sum(ref)==1,'full canonical target normalized')
    debt=D(p,ref);newS=add((1,SS),(1,num(c*eta)),(-1,cost))
    ck(debt==add((1,newT),(-1,newS)),'FULL debt Tnew-Snew exact, old shape retained')
    pos(newS,'nonnegative SAME eta reserve minus actual target cost')
    ck(eta<=gamma*x.I(a),'eta priced by actual control influence')
    return f,ref,debt,newT,newS,eta

orders=[[0,1,2,3,4],[3,4,0,1,2],[0,3,1,4,2],[3,0,4,1,2],[0,4,3,1,2],[4,3,0,1,2],[2,1,0,3,4],[4,3,2,1,0]]
policies=[(o,k) for o in orders for k in range(6)]+[(None,0),(None,1)]
receipts=[]
def run(theta,mode,policy):
    global POL,NODE,LEAF,DIFF
    a=b.acs[1];v=b.v;pa=P(a);ra=tuple(z if u==0 else z*(1-theta+3*theta*(u==1)) for u,z in enumerate(pa))
    root=state(v,a,ra,0,mode);oldshape=add((Q(1,4),D(P(root[0]),root[1])))
    pos(add((1,b.Bs[1]),(-1,oldshape),(-1,num(Q(1,96))),(-1,num(Q(1,5376)))),'same ORIGINAL B pays old shape and ONE all-history odds envelope')
    order,stop=policy;release={};terminal={};Dleaves={};eta_release=Q(0)
    def walk(v,a,ra,free,fixed,depth,w):
        nonlocal release,terminal,Dleaves,eta_release
        global NODE,LEAF,DIFF
        f,rho,debt,TT,SS,eta=state(v,a,ra,depth,mode)
        if len(set(f))==1 or (order is not None and depth==stop) or (order is None and depth==3+stop):
            LEAF+=1;terminal=add((1,terminal),(w,SS));Dleaves=add((1,Dleaves),(w,debt));return
        if order is not None:j=order[depth]
        else:
            data=[j for j in free if j<3];ctrl=[j for j in free if j>=3];trigger=x.neg(f)>=Q(1,4) if stop==0 else sum(fixed.values())%2==1
            j=((ctrl if trigger else data) or (data if trigger else ctrl))[0]
        idx=free.index(j);nc=len(v).bit_length()-1
        out_ch,out_refs,out_z,refund=phase(f,rho,idx)
        if j<3:vs=[x.restrict(v,((idx,z),)) for z in (0,1)];aa=[a,a];rr=[ra,ra];expected_eta_release=Q(0)
        else:
            aa,rr,controller_z,_=phase(a,ra,idx-nc);vs=[v,v];expected_eta_release=x.neg(v)*x.spectrum(a)[1<<(idx-nc)]**2
            if controller_z!=out_z:DIFF+=1
        cs=[state(vs[z],aa[z],rr[z],depth+1,mode) for z in (0,1)]
        for z in (0,1):ck(cs[z][0]==out_ch[z],'actual child target and physical inheritance agree')
        dr=eta-(cs[0][5]+cs[1][5])/2;ck(dr==expected_eta_release,'exact eta martingale/release, no renewed owner')
        eta_release+=w*dr
        rel=add((1,TT),(Q(-1,2),cs[0][3]),(Q(-1,2),cs[1][3]));pos(rel,'old T plus reached eta share supermartingale')
        release=add((1,release),(w,rel))
        sigma=add((Q(1,2),cs[0][2]),(Q(1,2),cs[1][2]),(-1,debt))
        raw=add((Q(1,2),cs[0][2]),(Q(1,2),cs[1][2]),(Q(-1,2),D(P(out_ch[0]),out_refs[0])),(Q(-1,2),D(P(out_ch[1]),out_refs[1])))
        ck(raw==add((1,sigma),(1,refund)),'RAW reconstruction equals SIGNED target change plus OWN refunds')
        NODE+=1
        for z in (0,1):
            ff=dict(fixed);ff[j]=z;walk(vs[z],aa[z],rr[z],[k for k in free if k!=j],ff,depth+1,w/2)
    walk(v,a,ra,list(range(5)),{},0,Q(1))
    ck(Dleaves==add((1,root[3]),(-1,release),(-1,terminal)),'complete all-frontier signed original account')
    pos(add((1,root[3]),(-1,Dleaves)),'entire terminal CE paid by ONE original allowance')
    POL+=1
for theta in ([Q(1,8)] if PILOT else [Q(0),Q(1,8)]):
    for mode in ([0] if PILOT else range(3)):
        for policy in (policies[:6] if PILOT else policies):run(theta,mode,policy)
out={'status':'PASS','policies':POL,'assertions':sum(N.values()),'counts':N,'inherited_original_prefix_checks':sum(b.N.values()),'nodes':NODE,'leaves':LEAF,'controller_output_normalizer_differences':DIFF,'elapsed_seconds':time.monotonic()-START,'scalar_points':len(ks)*len(ls),'original_selected_B':enc(b.Bs[1]),'old_core_debit_margin':enc(add((1,b.coremargin),(-1,num(Q(1,64))))),'rate':'21/4','old_debit':'1/64','first_shape_cap':'9/1792','ONE_weighted_odds_allowance':'1/96','remaining_original_floor':'1/5376','sharp_binary_row_coefficient':'1/ln(2)-1','rational_majorant':'4/9'}
(R/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if not isinstance(v,(list,dict))}))
