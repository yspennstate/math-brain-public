from pathlib import Path
from fractions import Fraction as F
import json,sys,time,hashlib
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1]
sources=[[1],[-1]]+[[1 if mask&(1<<x) else -1 for x in range(2)] for mask in range(4)]+[[1 if mask&(1<<x) else -1 for x in range(4)] for mask in range(1,15)]+[[-1]+[1]*7,[(-1)**x.bit_count() for x in range(8)],[1 if x.bit_count()>=2 else -1 for x in range(8)]]
path_sources=sources[:6]+[[-1,1,1,1],[1,-1,-1,1],sources[-3],sources[-1]]
profile_domain=[(g,m) for g in sources for m in [3,5,8]]
path_domain=[(g,3,j) for g in path_sources for j in [0,1,2]]+[( [-1,1,1,1],5,j) for j in [0,1,2]]
mode=sys.argv[1]
if mode=='freeze_pilot':
    (RUN/'out').mkdir(exist_ok=True)
    old=OWN/'runs/20261023T110024Z-account03-A094-proof-chain-challenger/code/arithmetic.py'
    (RUN/'code/arithmetic.py').write_bytes(old.read_bytes())
    spec={'helper_version':'A094-stage20-v1, new full-source profile and positive-part path implementation','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_library_source':str(old),'arithmetic_library_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'Boolean_family':'actual arbitrary Boolean source full-point edit with m dummy bits and one fair selector; constants/a0 included','profiles':{'cases':len(profile_domain),'padding':[3,5,8],'sources':sources},'paths':{'cases':len(path_domain),'installed_floors':sum(len(g).bit_length() for g,m,j in path_domain),'domain':[{'g':g,'m':m,'incoming':j} for g,m,j in path_domain],'incoming_models':['canonical','half canonical subprobability','actual A011 floor based on source R=(P+uniform)/4']},'pilot':{'profiles':2,'paths':3,'installed_floors':9,'source':[-1,1,1,1],'profile_padding':[3,8],'path_padding':3},'symmetry':'padding coordinate permutations only; finite physical paths use first remaining source coordinate, analytic proof handles adaptive distinct source choices','arithmetic':'integer source Walsh/physical edge counts; Fraction full references and posterior normalizers; rigorous24-term atanh log intervals; exact multiplicity classes for large dummy stocks','memory_estimate_MB':120,'max_runtime_seconds_per_job':55,'pilot_max_seconds':55,'automatic_dimension_escalation':False}
    (RUN/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8');mode='pilot'
import arithmetic as A
def add(*xs):
    z=(F(0),F(0))
    for x in xs:z=A.add(z,x)
    return z
def zero(z):A.ck(z[0]<=0<=z[1])
def H(v):p=A.law(v);return A.ce(p,p)
def D(v,q):return A.sub(A.ce(A.law(v),q),H(v))
def dterm(p,q):return A.scale(A.lg(p/q),p) if p else (F(0),F(0))
def profile(g,m):
    a=(len(g)-1).bit_length();eps=F(1,1<<(a+m));u=F(1,1<<m);M=1<<(a+m)
    aa=[g[0]*x for x in A.fw(g) if x];N=len(aa);W=2*eps-N*eps*eps
    A.ck(N*eps<=u);A.ck(min(abs(x) for x in aa)>=F(1,1<<a))
    dc=add(*(dterm((x-eps)**2,(1-W)*x*x) for x in aa))
    df=add(*(dterm(x*x-2*eps*x+2*eps*eps,(x*x+3*eps*eps)/(1+3*eps)) for x in aa),A.scale(dterm(2*eps*eps,3*eps*eps/(1+3*eps)),M-N))
    C=F(1,2)+F(5043,128)*u
    A.ck(df[1]<C*eps)
    if m>=8:
        A.ck(A.sub(df,dc)[0]>F(23,512)*eps);A.ck(df[1]<F(91,128)*eps)
    # Independent direct-character source coefficients, no FWHT.
    direct=[sum(F(y*(-1 if (x&s).bit_count()%2 else 1),len(g)) for x,y in enumerate(g)) for s in range(len(g))]
    A.ck(direct==A.fw(g))
    return {'a':a,'g':g,'m':m,'epsilon':str(eps),'Dfloor_interval':[str(x) for x in df],'Dcan_interval':[str(x) for x in dc],'canonical_charge_interval':[str(x) for x in A.sub(df,dc)],'coefficient_C':str(C)}
def model(g,m,variant=0):
    a=(len(g)-1).bit_length();n=a+m;eps=F(1,1<<n)
    v=[g[x&((1<<a)-1)] for x in range(1<<(n+1))];v[1<<n]*=-1
    P=A.law(v);pg=A.law(g);N=sum(bool(x) for x in pg);W=2*eps-N*eps*eps
    if variant<2:Q=[((1-W)*pg[j] if j<len(pg) and pg[j] else eps*eps)/(2 if variant else 1) for j in range(len(v))]
    else:
        R=[(x+F(1,len(pg)))/4 for x in pg] if variant==2 else pg
        data=[((R[j] if j<len(R) else 0)+3*eps*eps)/(1+3*eps) for j in range(1<<n)]
        mu=[P[j]+P[j+(1<<n)] for j in range(1<<n)]
        Q=[data[j&((1<<n)-1)]*p/mu[j&((1<<n)-1)] for j,p in enumerate(P)]
    A.ck(all(not x or q>0 for x,q in zip(P,Q)))
    expected=F(1,2) if variant==1 else (F(1,2)+3*eps)/(1+3*eps) if variant==2 else F(1)
    A.ck(sum(Q)==expected)
    return v,Q
def inherit(v,Q,i):
    s=sum(Q);vv,qq=A.inherit(v,[x/s for x in Q],i,True)
    QQ=[[x*s for x in q] for q in qq]
    A.ck(all(sum(q)==s for q in QQ))
    cc=[A.ce(A.law(x),q) for x,q in zip(vv,QQ)]
    release=A.sub(A.ce(A.law(v),Q),A.scale(add(*cc),F(1,2)))
    A.ck(release[1]>=0)
    return vv,QQ,cc,release
def path(g,m,variant):
    a=(len(g)-1).bit_length();eps=F(1,1<<(a+m));u=F(1,1<<m);C=F(1,2)+F(5043,128)*u
    v,Q=model(g,m,variant);rootv=v;original=A.ce(A.law(v),Q);Ig=A.total(g)
    if variant==2 and Ig:
        pg=A.law(g);R=[(x+F(1,len(pg)))/4 for x in pg];c=A.ce(pg,R);C0=F((c[1]/Ig).__ceil__());K=4*C0+15;U=(C0+F(37,8))*Ig
        A.ck(K*A.total(v)-original[1]-U>=F(7,8)*Ig)
    else:K=U=None
    lam=F(1);G=(F(0),F(0));book=F(0);signed=(F(0),F(0));siblings=[];rows=[]
    for k in range(a+1):
        freshv,Qnew=model(g,m,3);A.ck(freshv==v)
        old=A.ce(A.law(v),Q);new=A.ce(A.law(v),Qnew)
        excess=A.scale(A.sub(new,old),lam);positive=max(F(0),excess[1]);book+=positive;signed=add(signed,excess)
        A.ck(positive<C*eps);A.ck(book<(k+1)*C*eps)
        total=add(G,*(A.scale(c,r) for r,c in siblings),A.scale(new,lam))
        zero(A.sub(total,add(original,signed)))
        if Ig:
            A.ck(book<C*u*Ig)
            if K is not None:A.ck(K*A.total(rootv)-original[1]-U-book>F(1613,8192)*Ig)
        rows.append({'depth':k,'reach':str(lam),'current_mass':str(sum(Q)),'actual_signed_excess_interval':[str(x) for x in excess],'positive_booking_upper':str(book)})
        Q=Qnew
        if k<a:
            vv,qq,cc,release=inherit(v,Q,0);G=add(G,A.scale(release,lam))
            siblings.append((lam/2,cc[1]));g=A.restrict(g,0,0);v,Q=vv[0],qq[0];lam/=2
    return {'initial_a':a,'m':m,'incoming':variant,'source_I':str(Ig),'book_upper':str(book),'rows':rows}
start=time.perf_counter();prows=[];hrows=[]
if mode in ['pilot','profiles']:
    domain=[([-1,1,1,1],m) for m in [3,8]] if mode=='pilot' else profile_domain
    prows=[profile(g,m) for g,m in domain]
if mode in ['pilot','paths']:
    domain=[([-1,1,1,1],3,j) for j in [0,1,2]] if mode=='pilot' else path_domain
    hrows=[path(g,m,j) for g,m,j in domain]
out={'status':'PASS','mode':mode,'profile_cases':len(prows),'path_cases':len(hrows),'installed_floors':sum(len(r['rows']) for r in hrows),'assertions':A.checks,'seconds':time.perf_counter()-start,'profiles':prows,'paths':hrows}
(RUN/'out'/f'{mode.upper()}_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['profiles','paths']}))
