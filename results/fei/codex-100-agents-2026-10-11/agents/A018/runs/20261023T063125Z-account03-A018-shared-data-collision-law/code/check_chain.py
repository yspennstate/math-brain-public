from pathlib import Path
import importlib.util,json,sys,time,hashlib,math
R=Path(__file__).resolve().parents[1]
H=R.parents[1]/'runs/20261022T202507Z-account03-A018-shared-data-collision-law/code/check_equal_mean.py'
assert hashlib.sha256(H.read_bytes()).hexdigest()=='a577c9c1b6dfd1df442a70010cfdec0377d1810816ebf9df7df2926c53884467'
sp=importlib.util.spec_from_file_location('own_exact',H);c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
F,ck,add,sc,lg=c.F,c.ck,c.add,c.sc,c.lg
ONE=lg(F(2))
def scalar(x):return sc(x,ONE)
def positive(v):return c.interval(v)[0]>0
def pack(v):return {str(p):str(x) for p,x in v.items()}
def cut(i,b):return (i&((1<<b)-1))|((i>>(b+1))<<b)
def fold(Q,b):
    out=[F(0)]*(len(Q)//2)
    for i,q in enumerate(Q):out[cut(i,b)]+=q
    ck(sum(out)==1);return tuple(out)
def tt(l,constant=False):
    return tuple(1 if (not constant and j//2==0) else 1-2*(j%2) for j in range(2**(l+1)))
def fw(t):
    a=list(t);stride=1
    while stride<len(a):
        for start in range(0,len(a),2*stride):
            for j in range(start,start+stride):a[j],a[j+stride]=a[j]+a[j+stride],a[j]-a[j+stride]
        stride*=2
    return tuple(F(x,len(a)) for x in a)
def activation(a,Q,literal=False):
    s=(F(1,2),F(-1,2),F(-1,2),F(-1,2));out=[];ref=[]
    for m,b in enumerate(s):
        for i,x in enumerate(a):
            g=b*x;data=m*len(a)+i
            alpha=(F(int(data==0))+g)/2;beta=(F(int(data==0))-g)/2
            mass=alpha*alpha+beta*beta;qr=(Q[i]/4+int(data==0))/2
            frac=alpha*alpha/mass if mass else F(1)
            out.extend((alpha,beta));ref.extend((qr*frac,qr*(1-frac)))
    P=c.probs(out);ck(sum(P)==sum(ref)==1)
    C=c.ce(P,ref)
    formula=add(sc(F(1,2),c.ce(c.probs(a),Q)),ONE,c.psi(a[0]/2),sc(-1,c.refund(a[0]**2/4,Q[0]/4)))
    ck(C==formula)
    if literal:
        # Inverse core transform; literal Boolean truth-table gate followed by character sums.
        vals=tuple(sum(v*(-1 if (i&j).bit_count()%2 else 1) for j,v in enumerate(a)) for i in range(len(a)))
        ck(all(v in (-1,1) for v in vals))
        full=tuple(v for mask in (-1,1,1,1) for h in vals for v in (1,h*mask))
        ck(tuple(out)==c.walsh(full))
    return C,P,tuple(ref)
def run(pilot=False):
    start=time.perf_counter();details=[];nodes=0
    endpoint=add(c.psi(F(1,8)),sc(-F(1,2),add(c.psi(F(0)),c.psi(F(1,4)))))
    endpoint_gap=add(scalar(F(1,16)),sc(-1,endpoint));ck(positive(endpoint_gap))
    ck(positive(add(ONE,c.psi(F(1,2)),scalar(-2))))
    certificates={'A019_profile_endpoint_gap':pack(endpoint_gap)}
    for k in ([2] if pilot else range(2,8)):
        e=F(1,2**k);a=fw(tt(k));P=c.probs(a);Q=c.refs(P)[1];cu=c.ce((F(0),F(1)),(F(1,2),F(1,2)))
        ck(cu==ONE)
        ck(a==c.walsh(tt(k)))
        ck(a[1]==1-e and all(abs(x)==e for j,x in enumerate(a) if j!=1))
        ck(sum(F(j.bit_count())*p for j,p in enumerate(P))==1+(k-1)*e)
        ck(c.ent(P)==add(c.ent(((1-e)**2,)),scalar(4*k*e-2*k*e*e)))
        ck(c.nonneg(add(ONE,sc(-1,c.kl(P,Q)))))
        bank=add(scalar(F(7,4)+(k-1)*e),sc(-F(1,4),c.ce(P,Q)))
        C0,_,_=activation(a,Q,k<=3);Cprev,Pprev,Qprev=activation(a,Q)
        char=tuple(1-2*(j%2) for j in range(len(a)));au=fw(char);Pu=c.probs(au);Qu=c.refs(Pu)[1]
        Cq0,_,_=activation(au,Qu);ah,Qh=c.lift(au,a,Qu,Q)
        Croot,_,_=activation(ah,Qh)
        Tq=add(Croot,sc(-F(1,2),add(Cq0,C0)),scalar(-e))
        ck(positive(add(scalar(F(1,4)),sc(-1,Tq))))
        Tplus=Tq if positive(Tq) else {};ck(positive(Tq) or c.interval(Tq)[1]<=0)
        spent={};leaf={};Dfirst=None;conversions=[]
        for t in range(1,k+1):
            l=k-t;d=2**t*e;Q=fold(Q,1)
            expected=tuple(e*d/2+F(int(j==0),2)+F(1-2*e,2)*int(j==1) for j in range(len(Q)))
            ck(Q==expected)
            alive=fw(tt(l));dead=fw(tt(l,True))
            if k<=3:ck(alive==c.walsh(tt(l)));ck(dead==c.walsh(tt(l,True)))
            Ca,Pa,Qa=activation(alive,Q,k<=3);Cu,Pu,Qu=activation(dead,Q,k<=3)
            Ract=fold(Qprev,2)
            ck(tuple((x+y)/2 for x,y in zip(Pa,Pu))==fold(Pprev,2))
            ka=add(c.ce(Pa,Ract),sc(-1,Ca));ku=add(c.ce(Pu,Ract),sc(-1,Cu))
            ck(c.nonneg(ka));ck(c.nonneg(ku))
            marginal=add(*(sc(p,lg(Ract[cut(i,2)]/Qprev[i])) for i,p in enumerate(Pprev) if p))
            ck(c.nonneg(marginal))
            D=add(Cprev,sc(-F(1,2),add(Ca,Cu)))
            ck(D==add(marginal,sc(F(1,2),add(ka,ku))))
            ck(c.nonneg(D));nodes+=1
            if t==1:
                Dfirst=D;ck(positive(add(scalar(F(77,64)),sc(-1,D))))
                ck(positive(add(bank,scalar(-F(1,8)),sc(-1,Tplus),sc(-F(1,2),D),scalar(-F(3,128)))))
            spent=add(spent,sc(F(1,2**t),D));leaf=add(leaf,sc(F(1,2**t),Cu))
            ck(c.nonneg(add(Cu,scalar(-3))))
            if t==k:leaf=add(leaf,sc(e,Ca));ck(positive(add(Ca,scalar(-2))))
            conversions.append({'depth':t,'conversion_KL':pack(sc(F(1,2),add(ka,ku))),'full_query_decrement':pack(D)})
            Cprev,Pprev,Qprev=Ca,Pa,Qa
            if time.perf_counter()-start>55:raise RuntimeError('Frozen55s cap')
        ck(spent==sc(F(1,2),add(C0,sc(-1,leaf))))
        ck(positive(add(leaf,scalar(-(3-e)))))
        remaining=add(bank,scalar(-F(1,8)),sc(-1,Tplus),sc(-1,spent))
        ck(positive(add(remaining,scalar(-F(1,8)))))
        if k==2:
            gap=add(remaining,scalar(-F(1,8)))
            denominator=math.lcm(*(x.denominator for x in gap.values()))
            exponents={p:int(x*denominator) for p,x in gap.items()}
            lhs=math.prod(p**x for p,x in exponents.items() if x>0)
            rhs=math.prod(p**(-x) for p,x in exponents.items() if x<0)
            ck(lhs>rhs)
            certificates['k2_final_margin_gap']={'prime_log':pack(gap),'clearing_denominator':denominator,'integer_exponents':exponents,'left_gt_right':lhs>rhs,'left_bits':lhs.bit_length(),'right_bits':rhs.bit_length(),'left_integer':str(lhs),'right_integer':str(rhs)}
        if k>=3:ck(F(5,4)-(k+3)*e>=F(1,2))
        details.append({'k':k,'nodes':k,'remaining_after_all_old_and_new_debits':pack(remaining),'remaining_gt_one_eighth':True,'complete_stopped_leaf_average_CE':pack(leaf),'total_data_charge_original_reach':pack(spent),'first_v_query_A019_HOLDS':True,'conversion_terms':conversions})
        (R/'out/CHECKPOINT.json').write_text(json.dumps({'completed_k':k,'nodes':nodes,'assertions':c.checks}),encoding='utf-8')
    result={'status':'PASS','pilot':pilot,'chains':len(details),'nodes':nodes,'assertions':c.checks,'seconds':time.perf_counter()-start,'details':details}
    (R/'out'/('PILOT.json' if pilot else 'CHECKS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    (R/'out'/('PILOT_CERTIFICATES.json' if pilot else 'CERTIFICATES.json')).write_text(json.dumps(certificates,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='details'}))
if __name__=='__main__':run('--pilot' in sys.argv)
