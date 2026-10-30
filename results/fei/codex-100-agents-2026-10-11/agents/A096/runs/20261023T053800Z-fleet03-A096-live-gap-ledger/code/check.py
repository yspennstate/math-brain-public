"""Exact phase-funded profile transaction checker; no author source helper imports."""
import argparse,functools,hashlib,importlib.util,json,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'
primitive=ROOT.parents[1]/'runs/20261023T010221Z-fleet03-A096-live-gap-ledger/code/check.py'
spec=importlib.util.spec_from_file_location('own_stage18_primitives',primitive)
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
original_log=v.lg
@functools.lru_cache(None)
def dyadic_log(q):
    lo,hi=original_log(q); scale=1<<80
    return F((lo.numerator*scale)//lo.denominator,scale),F(-((-hi.numerator*scale)//hi.denominator),scale)
v.lg=dyadic_log
Arow=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
Brow=[1-z*z for z in Arow]
A=v.spectrum(Arow); B=v.spectrum(Brow); beta=F(sum(Brow),16)
C=sum(a*a*b*b for a,b in zip(A,B)); D=sum(a*b**3 for a,b in zip(A,B)); E=sum(b**4 for b in B)
G=C-D*D/E if E else F(0)
CHECKS=0; POSITIVE=0; WITNESS=None; PAID=0
DEADLINE=float('inf')
def ck(x):
    global CHECKS
    CHECKS+=1
    if not x:raise AssertionError(CHECKS)
def ce(p,q):return v.ce(p,q)
def plus(*items):
    z=(F(0),F(0))
    for t in items:z=v.add(z,t)
    return z
def minus(a,b):return plus(a,v.scale(-1,b))
def save(name,x):
    (OUT/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def wrapper(f,sgn):return [Arow[k%16]+sgn*Brow[k%16]*f[k//16] for k in range(16*len(f))]
def coherent(f,R,sgn):
    m=F(sum(f),len(f)); q=[]
    for T in range(len(f)):
        q.extend([(a+sgn*m*b)**2 if T==0 else b*b*R[T] for a,b in zip(A,B)])
    ck(sum(q)==1 and all(z>=0 for z in q));return q
def transaction(f,R,sgn,j,target):
    global POSITIVE,WITNESS,PAID
    if time.perf_counter()>DEADLINE:raise TimeoutError('Frozen runtime deadline')
    mean=F(sum(f),len(f)); coeff=v.spectrum(f)[1<<j]; x=G*coeff*coeff
    parent=wrapper(f,sgn); p=v.law(parent); Q=coherent(f,R,sgn)
    qbar=v.marginal(Q,4+j); Rbar=v.marginal(R,j)
    old=ce(p,Q); cost=v.erase(p,4+j)
    children=[]; refunds=[]; extras=[]; energies=[];cal_identity=True
    for bit in (0,1):
        child=v.restrict(f,j,bit); mu=F(sum(child),len(child)); law=v.law(wrapper(child,sgn))
        Rc=v.calibrate(Rbar,mu*mu); base=coherent(child,Rc,sgn)
        tau=beta*(1-mu*mu); Rnew=Rc[:]
        eps=x/(tau+x) if tau and x else F(0)
        if eps:
            label=target if target<len(Rc) else len(Rc)-1
            for k in range(1,len(Rc)):Rnew[k]=(1-eps)*Rc[k]+eps*(1-mu*mu)*(k==label)
        new=coherent(child,Rnew,sgn)
        basecost=ce(law,base); newcost=ce(law,new); inheritedcost=ce(law,qbar)
        cal_identity=cal_identity and base==qbar
        refund=minus(inheritedcost,basecost); extra=minus(newcost,basecost)
        if x:
            invln=lg_inv_ln2()
            ck(extra[1]<=x*invln[1])
            if extra[0]>0:
                POSITIVE+=1
                if WITNESS is None:
                    WITNESS={'seed':f,'incoming_seed_reference':list(map(str,R)),'sign':sgn,'query_seed_bit':j,'outcome':bit,'target_label':target,'child_seed':child,'epsilon':str(eps),'x':str(x),'tail_mass':str(tau),'old_child_reference':list(map(str,base)),'new_child_reference':list(map(str,new)),'strict_signed_profile_cost_lower_bound':str(extra[0]),'semantics':'Actual positive profile-only reset; preceding query/coherent calibration pays it. Both child full costs retained.'}
        refunds.append(refund); extras.append(extra); energies.append(x)
        cost=plus(cost,v.scale(F(1,2),newcost)); children.append((child,Rnew))
    increment=minus(cost,old)
    if x:
        bound=-x*lg_inv_ln2()[0]
        ck(increment[1]<bound)
        ck((refunds[0][0]+refunds[1][0])/2>=2*x*lg_inv_ln2()[0])
        PAID+=1
    else:
        if increment[1]<=0:ck(True)
        else:
            # When log intervals straddle zero, certify EXACT equality structurally:
            # no coherent calibration change and identical occupancy conditionals.
            bitmask=1<<(4+j)
            zero_occ=all(p[k]*Q[k|bitmask]==p[k|bitmask]*Q[k] for k in range(len(p)) if not k&bitmask)
            ck(cal_identity and zero_occ)
    return children,increment
@functools.lru_cache(None)
def lg_inv_ln2():
    # ln2=2*atanh(1/3), exact rational enclosure with positive tail.
    y=F(1,3); lo=2*sum(y**(2*j+1)/F(2*j+1) for j in range(18)); hi=lo+2*y**37/(37*(1-y*y))
    return 1/hi,1/lo
def all_seeds(n):
    count=0
    for mask in range(1<<(1<<n)):
        f=[1 if (mask>>k)&1 else -1 for k in range(1<<n)]; p=v.law(f)
        for mode in (0,1):
            R=v.reference(p,mode)
            for sgn in (-1,1):
                for j in range(n):
                    for target in (1,(1<<(n-1))-1):
                        transaction(f,R,sgn,j,target);count+=1
                        if count%256==0:
                            save('PRIMARY_CHECKPOINT.json',{'dimension':n,'completed_policies':count,'assertions':CHECKS+v.COUNT,'strict_phase_paid_transactions':PAID,'positive_profile_resets':POSITIVE,'status':'PARTIAL_NOT_A_FULL_PASS'})
    return count
def fixture():
    f=[-1 if k in (0,1,2,4) else 1 for k in range(16)]
    initial=v.reference(v.law(f),1); nodes=0
    for sign in (-1,1):
        frontier=[(f,initial)]
        for depth in range(3):
            nxt=[]
            for child,R in frontier:
                kids,inc=transaction(child,R,sign,0,(len(child)//2)-1)
                nxt.extend(kids);nodes+=1
            frontier=nxt
    return nodes
def parity_obstruction():
    f=[-1 if k.bit_count()%2 else 1 for k in range(8)]
    R=v.law(f); parent=wrapper(f,1); Q=coherent(f,R,1); P=v.law(parent)
    ck(Q==P and v.spectrum(f)[1]==0)
    ck(all(P[k]==0 or P[k|16]==0 for k in range(len(P)) if not k&16))
    qbar=v.marginal(Q,4); increases=[]
    for bit in (0,1):
        child=v.restrict(f,0,bit); p=v.law(wrapper(child,1))
        ck(p==qbar)
        r=v.law(child); ck(r[3]==1)
        new=r[:]; new[3]=F(63,64);new[1]=F(1,64)
        delta=minus(ce(p,coherent(child,new,1)),ce(p,qbar))
        ck(delta[0]>0)
        increases.append(delta)
    return {'seed':'parity3','query_influence':1,'singleton_coefficient':0,'erasure':0,'occupancy_refund':0,'calibration_refund':0,'positive_reset_formula':'(3/8)*log2(64/63)','certified_positive_lower_bound':str(min(t[0] for t in increases)),'scope':'Refutes fixed positive profile strength funded solely from every relevant current query; not FEI.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
    ck(G==F(9,3584)); start=time.perf_counter();DEADLINE=start+(60 if args.pilot else 240)
    count=all_seeds(2 if args.pilot else 3)
    seq=0 if args.pilot else fixture()
    if not args.pilot:save('PARITY_OBSTRUCTION.json',parity_obstruction())
    result={'status':'PASS','helper_version':'A096-phase-profile-v2','dimension':2 if args.pilot else 3,'truth_tables':16 if args.pilot else 256,'query_target_policies':count,'sequential_fixture_query_nodes':seq,'strict_phase_paid_transactions':PAID,'strict_positive_profile_reset_occurrences':POSITIVE,'assertions':CHECKS+v.COUNT,'controller_gram':{'C':str(C),'D':str(D),'E':str(E),'Gamma':str(G),'beta':str(beta)},'primitive_path':str(primitive),'primitive_sha256':hashlib.sha256(primitive.read_bytes()).hexdigest(),'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction, rational log bounds outward-rounded to80-bit dyadics; no floating sign test','independent_review':'PENDING'}
    save('PILOT.json' if args.pilot else 'VALIDATION.json',result)
    if WITNESS:save('POSITIVE_PROFILE_WITNESS.json',WITNESS)
    print(json.dumps(result))
