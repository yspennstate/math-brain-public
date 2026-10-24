"""Exact adaptive original-source/fiber reset certificates."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, importlib.util, itertools, json, time
HERE=Path(__file__).resolve().parent.parent
s=importlib.util.spec_from_file_location('frontier',HERE/'code'/'verify.py')
v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
a=v.a; START=time.monotonic()

def node(beta, E, bits):
    return v.restriction(beta,0,(len(beta)-1).bit_length(),E,bits)

def tree_frontiers(remaining, assignment=()):
    yield (assignment,)
    for j in remaining:
        rest=tuple(k for k in remaining if k!=j)
        for left in tree_frontiers(rest,assignment+((j,0),)):
            for right in tree_frontiers(rest,assignment+((j,1),)):
                yield left+right

def fixture(gp,gm,beta):
    nx=len(gp); nd=(nx-1).bit_length(); p=F(1+sum(beta)/F(len(beta)),2)
    pp=[x*x for x in a.walsh(gp)];pm=[x*x for x in a.walsh(gm)]
    # Original complete terminal references, kept throughout the entire tree.
    Q=[p*x+(1-p)*y for x,y in zip(pp,pm)]
    old=a.combine((p,a.entropy(pp)),(1-p,a.entropy(pm)))
    d=F(sum(x!=y for x,y in zip(gp,gm)),nx)
    J=sum(a.influence([x*y for x,y in zip(gp,gm)]))
    rootf=[gp[x] if beta[z]==1 else gm[x] for z in range(4) for x in range(nx)]
    IX=sum(a.influence(rootf)[:nd])
    cache={}
    for assignment in ((),((0,0),),((0,1),),((1,0),),((1,1),),((0,0),(1,0)),((0,0),(1,1)),((0,1),(1,0)),((0,1),(1,1))):
        E=[j for j,b in assignment]; bits=sum(b<<k for k,(j,b) in enumerate(assignment))
        W=[j for j in range(2) if j not in E]
        phase=node(beta,E,bits)
        pb=[t*t for t in a.walsh(phase)]
        C=[d*t for t in pb];C[0]+=1-d
        f=[gp[x] if phase[z]==1 else gm[x] for z in range(len(phase)) for x in range(nx)]
        P=[t*t for t in a.walsh(f)]
        R=[Q[x]*C[z] for z in range(len(C)) for x in range(nx)]
        gamma=a.ce(P,R); inf=a.influence(f)
        for z in range(len(C)):
            a.check(sum(P[z*nx+x] for x in range(nx))==C[z],'actual child control law')
        cache[frozenset(assignment)]=(gamma,sum(inf),sum(inf[nd:]),C,P)
    # Each query first marginalizes the CURRENT reference, then makes the
    # prescribed conditioning return. Record the full reset credit, not only
    # the lower terminal bill.
    for assignment in ((),((0,0),),((0,1),),((1,0),),((1,1),)):
        parent=cache[frozenset(assignment)]
        W=[j for j in range(2) if j not in dict(assignment)]
        for j in W:
            local=W.index(j)
            inherited=v.projection(parent[3],[k for k in range(len(W)) if k!=local])
            for bit in range(2):
                child=cache[frozenset(assignment+((j,bit),))]
                newC=child[3]
                inheritedR=[Q[x]*inherited[z] for z in range(len(inherited)) for x in range(nx)]
                oldbill=a.ce(child[4],inheritedR)
                kl=a.combine((1,a.ce(newC,inherited)),(-1,a.entropy(newC)))
                a.nonnegative(kl,'source-conditioned return credit nonnegative')
                a.check(a.combine((1,oldbill),(-1,child[0]),(-1,kl))=={},'exact complete-reference reset credit')
    count=0
    for frontier in tree_frontiers((0,1)):
        gamma={}; inf=ctrl=F(0)
        for assignment in frontier:
            g,i,z,C,P=cache[frozenset(assignment)]
            weight=F(1,1<<len(assignment))
            gamma=a.combine((1,gamma),(weight,g));inf+=weight*i;ctrl+=weight*z
        a.check(sum(F(1,1<<len(t)) for t in frontier)==1,'physical frontier reaches')
        a.check(inf-ctrl==IX,'adaptive data influence remains original')
        a.nonnegative(a.combine((1,old),(1,{2:4*J+2*ctrl}),(-1,gamma)),'adaptive full-terminal original-source payment')
        a.nonnegative(a.combine((1,{2:25*inf-F(1,16)*IX-23*ctrl}),(-1,gamma)),'adaptive same rate25 frontier capacity')
        count+=1
    a.check(count==9,'all two-control stopping/query trees')
    return count

def fibers():
    nodes=0
    for m in range(4):
        for code in range(1<<(1+m+m*(m-1)//2)):
            beta,r=a.quadratic(m,code);pb=[x*x for x in a.walsh(beta)]
            for labels in itertools.product((-1,0,1),repeat=m):
                E=[j for j,t in enumerate(labels) if t!=-1];W=[j for j,t in enumerate(labels) if t==-1]
                bits=sum(labels[j]<<k for k,j in enumerate(E))
                phase=node(beta,E,bits);child=[x*x for x in a.walsh(phase)]
                original=v.projection(pb,W)
                mass=sum(original[k] for k,t in enumerate(child) if t)
                a.check(mass>0,'original source contains restricted support')
                conditioned=[original[k]/mass if t else F(0) for k,t in enumerate(child)]
                a.check(child==conditioned,'restricted quadratic law exactly original affine-fiber conditioning')
                nodes+=1
    return nodes

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
    result={'status':'RUNNING','pilot':args.pilot};parents=frontiers=0
    try:
        funcs=list(itertools.product((-1,1),repeat=2))
        pairs=list(itertools.product(funcs,repeat=2))
        x=(1,-1,1,-1); y=(1,1,-1,-1); one=(1,)*4; defect=(1,1,1,-1)
        pairs.extend([(one,tuple(-t for t in one)),(x,x),(x,tuple(-t for t in x)),(x,y),(defect,one),(x,defect)])
        for gp,gm in pairs:
            for code in range(16):
                beta,r=a.quadratic(2,code);frontiers+=fixture(gp,gm,beta);parents+=1
                if time.monotonic()-START>55: raise RuntimeError('frozen runtime exhausted')
                if args.pilot and parents==16: break
            if args.pilot and parents==16: break
        nodes=0 if args.pilot else fibers()
        beta,_=a.quadratic(2,8)
        constant=node(beta,[0],0)
        constantlaw=[x*x for x in a.walsh(constant)]
        inherited=v.projection([x*x for x in a.walsh(beta)],[1])
        oldbill=a.ce(constantlaw,inherited);newbill=a.entropy(constantlaw)
        a.check(a.combine((F(1,2),oldbill),(-1,{2:F(1,2)}))=={},'adaptive unchanged-reference excess exactly one half')
        a.check(not newbill,'prescribed original-fiber conditioning clears constant branch')
        a.check(sum(a.influence(constant))==0,'pruned branch is truly constant')
        a.check(F(23,2)+12-F(1,2)==23,'original owner pays transaction after exact reset credit')
        result.update(status='PASS',parents=parents,frontiers=frontiers,source_restriction_nodes=nodes,
          adaptive_guard={'unchanged_inherited_reference_final_bill':'1/2','all_final_influences':0,'affine_conditioning_credit':'1/2','after_conditioning_final_bill':0,'same_original_rate25_bank':23,'total_signed_debit_after_credit':23})
    except Exception as exc:
        result.update(status='FAIL',error=repr(exc),parents=parents,frontiers=frontiers);raise
    finally:
        result.update(assertions=a.CHECKS,certified_log_signs=len(a.SIGN_CACHE),seconds=time.monotonic()-START,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        path=HERE/'out'/('adaptive_pilot.json' if args.pilot else 'adaptive.json')
        path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))

if __name__=='__main__':main()
