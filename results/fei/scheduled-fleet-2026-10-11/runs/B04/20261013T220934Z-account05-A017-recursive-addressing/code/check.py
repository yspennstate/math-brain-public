"""A017-two-edit-v1: frozen exact tests; imports read-only rational utility."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util, json, hashlib, time, itertools, argparse
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
old=ROOT.parents[0]/'20261011T234546Z-account05-A017-recursive-addressing'/'code'/'check.py'
sp=importlib.util.spec_from_file_location('rational_utility',old)
U=importlib.util.module_from_spec(sp); sp.loader.exec_module(U)
N=0; TREES=0; NODES=0; REVIEW=0; BAD2=0; digest=hashlib.sha256()
def req(ok,msg=''):
    global N
    N+=1
    if not ok: raise AssertionError((N,msg))
def signcheck(v,msg=''):
    lo,hi=v.interval(); req(lo>=0,msg)
def restrict(vals,n,i,bit):
    return [vals[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(1<<(n-1))]
def phase_inf(vals,n):
    return [F(sum(vals[x]!=vals[x^(1<<i)] for x in range(1<<n)),1<<n) for i in range(n)]
def root_case(n,rows,code,u,v):
    linear,edges,Q=U.parameters(n,code); base=U.signs(n,linear,edges)
    labels=[U.addr(rows,x) for x in range(1<<n)]
    req(labels[u]==labels[v],'one shared fiber')
    g=base.copy();g[u]*=-1;g[v]*=-1
    spec=U.spectrum(g,labels); base_spec=U.spectrum(base,labels)
    for z,ws in spec.items():
        for s,w in enumerate(ws):
            correction=2*(base[u]*(-1)**U.parity(s&u)+base[v]*(-1)**U.parity(s&v)) if z==labels[u] else 0
            req(w==base_spec[z][s]-correction,'coherent signed two-edit ledger')
    inf,pairs,C,dc=U.spectral_metrics(spec,n)
    pi,pp,pdc=U.physical(g,labels,n)
    req(inf==pi and pairs==pp and dc==pdc,'independent physical edge/face moments')
    h=u^v
    for i in range(n):
        active=any(row&(1<<i) for row in rows)
        initial=F(1,2) if active or Q[i] else F((linear>>i)&1)
        change=F(0) if active or h==1<<i else F(2,1<<n)*sum((-1)**(((linear>>i)&1)^U.parity(Q[i]&w)) for w in [u,v])
        req(inf[i]==initial+change,'signed physical influence ledger')
        req(C[i]==2*(inf[i]+sum(pairs[min(i,j),max(i,j)] for j in range(n) if i!=j)),'data-retaining boundary ledger')
    H=U.entropy(spec,n); r=U.rank(rows)
    fiber_cost=U.LF(2*r)
    for z in set(labels):
        restricted=[g[x] for x in range(1<<n) if labels[x]==z]
        # Enumerating an affine kernel in increasing order gives a linear parameterization
        # for a single row (the frozen finite domain); independent general proof in DERIVATION.
        req(len(restricted)==1<<(n-r))
        fiber_cost.add(U.entropy({0:U.fwht(restricted)},n-r),F(1,1<<r))
    req(H==fiber_cost,'one data label: exact fiber entropy')
    before_nodes=NODES
    spent,terminal=tree(g,base,labels,list(range(n)),Q,depth=0)
    req(spent+terminal==sum(inf),'terminal-inclusive influence telescoping')
    signcheck(U.LF(7*sum(inf)).add(H,-1),'global rational constant 7')
    digest.update(json.dumps([n,rows,code,u,v,H.d.__repr__(),[str(x) for x in inf],NODES-before_nodes],sort_keys=True).encode()+b'\n')
def tree(g,base,labels,ids,Q,depth):
    global TREES,NODES,BAD2
    n=len(ids); spec=U.spectrum(g,labels); H=U.entropy(spec,n)
    inf=U.spectral_metrics(spec,n)[0]; edits=sum(a!=b for a,b in zip(g,base))
    active=[i for i in range(n) if any(labels[x]!=labels[x^(1<<i)] for x in range(1<<n))]
    polar=[i for i in range(n) if Q[ids[i]] & sum(1<<j for j in ids)]
    if not active and (not edits or not polar):
        TREES+=1
        req(len(set(labels))==1,'leaf has exactly one data label')
        signcheck(U.LF(4*sum(inf)).add(H,-1),'terminal quadratic / character-times-affine-defect paid')
        return F(0),sum(inf)
    i=active[0] if active else polar[0]; NODES+=1
    req(inf[i]==0 or inf[i]>=F(1,4),'positive queried influence window')
    B=U.erasure(spec,n,i)
    signcheck(U.LF(4*inf[i]).add(B,-1),'zero K4 bad-node bill')
    if U.LF(2*inf[i]).add(B,-1).interval()[1]<0: BAD2+=1
    children=[(restrict(g,n,i,b),restrict(base,n,i,b),restrict(labels,n,i,b)) for b in [0,1]]
    delta=U.LF().add(H)
    for cg,cb,cl in children:delta.add(U.entropy(U.spectrum(cg,cl),n-1),-F(1,2))
    klower=4+2/U.LN2[1]
    signcheck(U.LF(klower*inf[i]).add(delta,-1),'entropy decrement budget')
    results=[tree(cg,cb,cl,ids[:i]+ids[i+1:],Q,depth+1) for cg,cb,cl in children]
    spent=inf[i]+sum(x[0] for x in results)/2
    terminal=sum(x[1] for x in results)/2
    req(spent+terminal==sum(inf),'node influence telescoping')
    return spent,terminal
def internal_masks(mask):
    ids=[i for i in range(mask.bit_length()) if mask>>i&1]
    if len(ids)<=1:return []
    left=sum(1<<i for i in ids[:len(ids)//2]);right=mask^left
    return [mask]+internal_masks(left)+internal_masks(right)
def review_subcube(n,vals,Z,zstar):
    global REVIEW
    allmask=(1<<n)-1;Y=allmask^Z;r=Z.bit_count();rho=F(1,1<<r)
    mz,my=internal_masks(Z),internal_masks(Y)
    def cost(s):return 1+2*int(s!=0)+2*sum(bool(s&m) for m in mz+my)
    def wy(s):return 2*sum(bool(s&m) for m in my)
    f=[-a if x&Z==zstar else a for x,a in enumerate(vals)]
    delta=[b-a for a,b in zip(vals,f)]
    wg=U.fwht(vals); wd=U.fwht(delta);wf=U.fwht(f);den=1<<(2*n)
    yids=[i for i in range(n) if Y>>i&1]
    embed=lambda t:sum(((t>>j)&1)<<i for j,i in enumerate(yids))
    h=[vals[zstar|embed(t)] for t in range(1<<len(yids))];wh=U.fwht(h)
    core=F(sum(a*a*wy(embed(t)) for t,a in enumerate(wh)),1<<(2*len(yids)))
    mean=F(sum(h),len(h));UZ=sum(2*(1-F(1,1<<m.bit_count())) for m in mz)
    energy=F(sum(a*a*cost(s) for s,a in enumerate(wd)),den)
    req(energy==4*rho*(1+2*(1-rho*mean*mean)+UZ+core),'A069 S1 independently reconstructed')
    parent=F(sum(a*a*wy(s) for s,a in enumerate(wg)),den)
    req(rho*core<=parent,'restricted core paid once')
    average=F(0)
    for z in range(1<<n):
        if z&Y:continue
        restricted=[vals[z|embed(t)] for t in range(1<<len(yids))]
        w=U.fwht(restricted)
        average+=rho*F(sum(a*a*wy(embed(t)) for t,a in enumerate(w)),1<<(2*len(yids)))
    req(average==parent,'A069 S2 partial Parseval')
    req(energy<=4*parent+4*rho*(2*r+1),'A069 S3')
    gamma=lambda w:F(sum(a*a*cost(s) for s,a in enumerate(w)),den)
    req(gamma(wf)<=2*gamma(wg)+2*energy<=2*gamma(wg)+8*parent+8*rho*(2*r+1),'A069 S4')
    a,b=phase_inf(vals,n),phase_inf(f,n)
    for i in range(n):req(a[i]+b[i]>=2*rho if Z>>i&1 else a[i]==b[i],'A069 S5 physical edges')
    REVIEW+=1
def fixtures():
    records=[]
    for n,edges in [(4,[(0,1),(0,2),(1,2)]),(6,[(0,j) for j in range(1,5)]+[(1,2),(3,4)])]:
        code=U.poly_code(n,edges);base=U.signs(n,0,edges);g=base.copy();g[0]*=-1;g[1]*=-1
        child=restrict(g,n,0,1);D=n-1;sp=U.spectrum(child,[0]*(1<<D));inf,_,C,_=U.spectral_metrics(sp,D)
        rr=[]
        for i in range(D):
            B=U.erasure(sp,D,i);margin=U.LF().add(B).add(U.LF(2*inf[i]),-1)
            rr.append(dict(i=i,influence=str(inf[i]),boundary=str(C[i]),B=B.json(),K2_excess=margin.json()))
        if n==4:
            req(inf[0]==F(1,4) and C[0]==1)
            B=U.erasure(sp,D,0)
            expected=U.LF(1).log(5,F(5,8)).log(3,-F(9,8))
            req(B==expected,'explicit K2 obstruction exact prime-log form')
            req(16*5**5>3**9,'integer sign certificate')
        records.append(dict(n=n,edges=edges,edits=[0,1],split=dict(coordinate=0,value=1,weight='1/2'),child=rr))
    (ROOT/'out'/'K2_OBSTRUCTIONS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf8')
def cases(pilot):
    for n in range(1,3 if pilot else 4):
        for code in range(1<<(n+n*(n-1)//2)):
            for u in range(1<<n):
                for v in range(u+1,1<<n):
                    for rows in [[]]+[[row] for row in range(1<<n) if not U.parity(row&(u^v))]:
                        yield n,rows,code,u,v
    if not pilot:
        for n in [4,5,6]:
            for code in U.graph_codes(n):
                for linear in [0,(1<<n)-1]:
                    for v in range(1,1<<n):
                        for rows in [[],[(1<<n)-1]]:
                            if all(not U.parity(row&v) for row in rows):yield n,rows,code|linear,0,v
        for n,edges in [(4,[(0,1),(0,2),(1,2)]),(6,[(0,j) for j in range(1,5)]+[(1,2),(3,4)])]:
            yield n,[],U.poly_code(n,edges),0,1
def main():
    start=time.perf_counter();pilot=argparse.ArgumentParser();pilot.add_argument('--pilot',action='store_true');args=pilot.parse_args()
    roots=0
    for c in cases(args.pilot):root_case(*c);roots+=1
    for n in [2] if args.pilot else [2,3]:
        for code in range(1<<(1<<n)):
            vals=[(-1 if code>>x&1 else 1) for x in range(1<<n)]
            for Z in range(1,(1<<n)-1):
                for z in range(1<<n):
                    if not z&(~Z):review_subcube(n,vals,Z,z)
    fixtures()
    result=dict(status='PASS',helper_version='A017-two-edit-v1',pilot=args.pilot,root_cases=roots,stopping_leaves=TREES,queried_nodes=NODES,K2_bad_nodes_observed=BAD2,K4_bad_nodes=0,A069_subcube_review_cases=REVIEW,assertions=N,utility_assertions=U.CHECKS,coverage_sha256=digest.hexdigest(),elapsed_seconds=time.perf_counter()-start,utility_sha256=hashlib.sha256(old.read_bytes()).hexdigest())
    (ROOT/'out'/('pilot.json' if args.pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps(result))
if __name__=='__main__':main()
