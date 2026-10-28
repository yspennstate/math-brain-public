"""Fixed-cut inherited-reference certificates. All decisions are exact."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, importlib.util, itertools, json, time

HERE=Path(__file__).resolve().parent.parent
OLD=HERE.parent/'20261022T211502Z-account03-A068-antichain-beyond-one-order'/'code'/'verify.py'
assert hashlib.sha256(OLD.read_bytes()).hexdigest()=='af436c9eaac4e0f2617d170517f163636ef03d669d83b7e93ca41ee3f0fde5d0'
spec=importlib.util.spec_from_file_location('arithmetic', OLD)
a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
START=time.monotonic()

def deadline():
    if time.monotonic()-START>55: raise RuntimeError('frozen runtime exhausted')

def projection(p, keep):
    out=[F(0)]*(1<<len(keep))
    for mask,v in enumerate(p):
        out[sum(((mask>>j)&1)<<k for k,j in enumerate(keep))]+=v
    return out

def restriction(truth, ndata, m, exposed, assignment):
    keep=[j for j in range(m) if j not in exposed]
    result=[]
    for z in range(1<<len(keep)):
        old=sum(((assignment>>k)&1)<<j for k,j in enumerate(exposed))
        old+=sum(((z>>k)&1)<<j for k,j in enumerate(keep))
        result.extend(truth[(old<<ndata)+x] for x in range(1<<ndata))
    return result

def test_parent(gp,gm,beta):
    nx=len(gp); nd=(nx-1).bit_length(); m=(len(beta)-1).bit_length()
    pp=[t*t for t in a.walsh(gp)]; pm=[t*t for t in a.walsh(gm)]
    pb=[t*t for t in a.walsh(beta)]
    p=F(1+sum(beta)/F(len(beta)),2)
    d=F(sum(x!=y for x,y in zip(gp,gm)),nx)
    M=[p*x+(1-p)*y for x,y in zip(pp,pm)]
    C=[d*t for t in pb]; C[0]+=1-d
    f=[gp[x] if beta[z]==1 else gm[x] for z in range(len(beta)) for x in range(nx)]
    physical=a.influence(f); IX=sum(physical[:nd]); J=sum(a.influence([x*y for x,y in zip(gp,gm)]))
    refs=[(pp,pm),([F(1,nx)]*nx,[(x+F(1,nx))/2 for x in pm])]
    cases=0
    for emask in range(1,1<<m):
        E=[j for j in range(m) if emask>>j&1]; W=[j for j in range(m) if not emask>>j&1]
        CW=projection(C,W); pbw=projection(pb,W)
        remaining=sum(physical[nd+j] for j in W)
        avgP=[F(0)]*(nx*len(CW)); avgI=F(0)
        for assignment in range(1<<len(E)):
            child=restriction(f,nd,m,E,assignment)
            P=[t*t for t in a.walsh(child)]
            for k,t in enumerate(P): avgP[k]+=t/F(1<<len(E))
            avgI+=sum(a.influence(child))/F(1<<len(E))
        a.check(avgI==IX+remaining,'physical remaining influence')
        for x in range(nx):
            a.check(sum(avgP[z*nx+x] for z in range(len(CW)))==M[x],'fixed-cut data marginal')
        for z in range(len(CW)):
            a.check(sum(avgP[z*nx+x] for x in range(nx))==CW[z],'fixed-cut inherited control marginal')
        for qp,qm in refs:
            Q=[p*x+(1-p)*y for x,y in zip(qp,qm)]
            R=[Q[x]*CW[z] for z in range(len(CW)) for x in range(nx)]
            a.check(sum(R)==1,'original projected reference normalized')
            gamma=a.ce(avgP,R)
            old=a.combine((p,a.ce(pp,qp)),(1-p,a.ce(pm,qm)))
            root=a.combine((1,a.ce(M,Q)),(1,a.entropy(C)))
            a.check(a.combine((1,gamma),(-1,a.ce(M,Q)),(-1,a.entropy(CW)))=={},'exact average full cost')
            a.check(a.combine((1,root),(-1,gamma),(-1,a.entropy(C)),(1,a.entropy(CW)))=={},'exact old-debit erasure identity')
            a.nonnegative(a.combine((1,old),(1,{2:4*J+2*remaining}),(-1,gamma)),'old full bills plus disagreement and remaining influence')
            # Exact terminal spectral references satisfy the required rate bound
            # throughout this two-bit domain. Other refs test the general theorem.
            if qp==pp and qm==pm:
                a.nonnegative(a.combine((1,{2:F(143,16)*IX}),(-1,old)),'terminal rate premise on finite domain')
                a.nonnegative(a.combine((1,{2:25*avgI-F(1,16)*IX-23*remaining}),(-1,gamma)),'same rate-25 original account frontier reserve')
        cases+=1
    return cases

def projections():
    phases=cuts=0
    for m in range(5):
        for code in range(1<<(1+m+m*(m-1)//2)):
            beta,r=a.quadratic(m,code); pb=[t*t for t in a.walsh(beta)]; inf=a.influence(beta)
            for mask in range(1<<m):
                W=[j for j in range(m) if mask>>j&1]; law=projection(pb,W)
                support=[x for x in law if x]
                a.check(all(x==F(1,len(support)) for x in support),'uniform affine projection')
                a.check(len(support)&(len(support)-1)==0,'projection cardinality power of two')
                k=(len(support)-1).bit_length()
                a.check(k<=sum(inf[j]==F(1,2) for j in W),'projection dimension at most varying coordinates')
                a.check(k<=2*sum(inf[j] for j in W),'projection entropy remaining influence')
                a.check(a.combine((1,a.entropy(law)),(-1,{2:F(k)}))=={},'projection rank entropy exact')
                cuts+=1
            phases+=1
            if phases%64==0: deadline()
    return phases,cuts

def guards():
    beta,_=a.quadratic(2,8)
    a.check(beta==[1,1,1,-1],'Boolean quadratic guard')
    # Root reference is uniform on four spectral atoms. After the first
    # physical query both children inherit the SAME uniform two-atom law.
    p=[t*t for t in a.walsh(beta)]
    a.check(p==[F(1,4)]*4,'guard root flat law')
    child0=restriction(beta,0,2,[0],0); child1=restriction(beta,0,2,[0],1)
    q=[F(1,2)]*2
    c0=a.ce([x*x for x in a.walsh(child0)],q)
    c1=a.ce([x*x for x in a.walsh(child1)],q)
    a.check(c0==c1=={2:F(1)},'both inherited terminal bills retained')
    a.check(sum(a.influence(child0))==0 and sum(a.influence(child1))==1,'constant and character children')
    a.check(F(25)*sum(a.influence(child0))-1==-1,'negative individual capacity')
    for rate in (F(2),F(9),F(25),F(100)):
        rootbank=rate-2
        first=rate/2-1
        second_negative=F(-1,2)
        second_positive=(rate-1)/2
        a.check(first+second_positive-rootbank==F(1,2),'positive-only overdraft')
        a.check(first+second_negative+second_positive==rootbank,'signed same-owner account closes')
    return {'phase':'(-1)^(z0 z1)','root_rate25_bank':23,'first_positive_debit':'23/2','second_positive_expected_debit':12,'second_negative_expected_release':'-1/2','total_positive':'47/2','positive_overdraft':'1/2','signed_total':23,'constant_child_capacity':-1,'all_rate_statement':'for every K>=2, positive spend K-3/2 exceeds bank K-2 by 1/2'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
    HERE.joinpath('out').mkdir(exist_ok=True)
    parents=cuts=0
    result={'status':'RUNNING','pilot':args.pilot}
    try:
        functions=list(itertools.product((-1,1),repeat=4))
        for gp in functions:
            for gm in functions:
                for code in range(16):
                    beta,r=a.quadratic(2,code)
                    cuts+=test_parent(gp,gm,beta);parents+=1
                    if parents%32==0: deadline()
                    if args.pilot and parents==128: break
                if args.pilot and parents==128: break
            if args.pilot and parents==128: break
        phases,projected=(0,0) if args.pilot else projections()
        result.update(status='PASS',parents=parents,cuts=cuts,projection_phases=phases,projections=projected,guard=guards())
    except Exception as exc:
        result.update(status='FAIL',parents=parents,cuts=cuts,error=repr(exc))
        raise
    finally:
        result.update(assertions=a.CHECKS,certified_log_signs=len(a.SIGN_CACHE),seconds=time.monotonic()-START,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        dest=HERE/'out'/('pilot.json' if args.pilot else 'verification.json')
        dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result))

if __name__=='__main__': main()
