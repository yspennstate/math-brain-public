from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,sys,time
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('a081_prior',RUN/'out/source_snapshots/04_check.py')
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    if not x:raise AssertionError(COUNT)

def expr(p,q,scale=F(1)):
    out={}
    for a,b in zip(p,q):
        if a:
            ck(b>0);out[b]=out.get(b,F(0))+a*scale
    return {b:a for b,a in out.items() if a and b!=1}

def add(*terms):
    out={}
    for x,scale in terms:
        for b,a in x.items():out[b]=out.get(b,F(0))+a*scale
    return {b:a for b,a in out.items() if a and b!=1}

def interval(x):
    lo=F(0);hi=F(0)
    for b,a in x.items():
        l,h=lib.log2(1/b)
        lo+=a*(l if a>=0 else h);hi+=a*(h if a>=0 else l)
    return lo,hi

def probs(f):
    a=lib.walsh(f);p=[v*v for v in a]
    ck(sum(p)==1)
    ck(sum(i.bit_count()*v for i,v in enumerate(p))==lib.influence(f))
    return p

def canonical(f,labels,selector):
    j=labels.index(selector);source=lib.child(f,j,0)
    ck(source[0]==1)
    n=len(source).bit_length()-1;eps=F(1,1<<n);a=lib.walsh(source);supp=[i for i,v in enumerate(a) if v];W=2*eps-len(supp)*eps*eps
    ck(0<W<=1)
    q=[eps*eps for _ in f]
    for i in supp:
        ix=(i&((1<<j)-1))|((i>>j)<<(j+1));q[ix]=(1-W)*a[i]*a[i]
    ck(sum(q)==1)
    # Reconstruct the ACTUAL point-selector child in physical space.
    for x,v in enumerate(source):
        ix=(x&((1<<j)-1))|((x>>j)<<(j+1))
        ck(f[ix]==v);ck(f[ix+(1<<j)]==v*(-1 if x==0 else 1))
    p=probs(f);ck(all(qi>0 or pi==0 for pi,qi in zip(p,q)))
    return q,{'n':n,'support':len(supp),'W':str(W),'zero_reference_atoms':sum(x==0 for x in q)}

ZERO=0
def split(f,q,labels,label):
    global ZERO
    j=labels.index(label);p=probs(f);ff=[lib.child(f,j,b) for b in [0,1]];pp=[probs(v) for v in ff];raw=[[],[]]
    for i in range(len(f)//2):
        ix=(i&((1<<j)-1))|((i>>j)<<(j+1));mass=p[ix]+p[ix+(1<<j)];r=q[ix]+q[ix+(1<<j)]
        ck(mass==(pp[0][i]+pp[1][i])/2)
        if mass:
            ck(r>0)
            for b in [0,1]:raw[b].append(r*pp[b][i]/mass)
        else:
            ZERO+=int(r>0)
            for b in [0,1]:raw[b].append(r)
    Z=[sum(v) for v in raw];ck(sum(Z)==2);ck(all(z>0 for z in Z));qq=[[v/Z[b] for v in raw[b]] for b in [0,1]]
    for i in range(len(f)//2):
        ix=(i&((1<<j)-1))|((i>>j)<<(j+1));mass=p[ix]+p[ix+(1<<j)];r=q[ix]+q[ix+(1<<j)]
        for b in [0,1]:
            if pp[b][i]:ck(pp[b][i]/qq[b][i]==mass/r*Z[b])
    release=add((expr(p,q),F(1)),(expr(pp[0],qq[0]),F(-1,2)),(expr(pp[1],qq[1]),F(-1,2)))
    if release:ck(interval(release)[0]>=0)
    ck(lib.influence(f)==F(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f))+(lib.influence(ff[0])+lib.influence(ff[1]))/2)
    return ff,qq,labels[:j]+labels[j+1:],release,[str(z) for z in Z]

def run_case(w,m,d,eta,policy):
    gg,f,q,p=lib.root(w,m);n=w+2+m;selector=n
    ck(probs(f)==p)
    rootexpr=expr(p,q);rootlo,roothi=interval(rootexpr);I=lib.influence(f);Slo=4*I-roothi
    ck(Slo>F(451,256))
    releases={};terminals={};charges=[];bookings=[];normalizers=[];boundary=[];wrong_diff=False
    def terminal(ff,qq,reach):
        nonlocal terminals
        terminals=add((terminals,F(1)),(expr(probs(ff),qq),reach))
    def query(ff,qq,labels,label,reach):
        nonlocal releases
        ff2,qq2,ll,rel,Z=split(ff,qq,labels,label);normalizers.append(Z)
        releases=add((releases,F(1)),(rel,reach))
        return ff2,qq2,ll
    def resets(ff,qq,labels,reach):
        nonlocal terminals,wrong_diff
        kids,old,ll=query(ff,qq,labels,w,reach)
        terminal(kids[1],old[1],reach/2)
        qcan,meta=canonical(kids[0],ll,selector);boundary.append(meta)
        q1=[(1-eta)*v+eta/F(len(qcan)) for v in qcan];ck(sum(q1)==1)
        C1=expr(probs(kids[0]),q1);cold=expr(probs(kids[0]),old[0]);e1=add((C1,reach/2),(cold,-reach/2));charges.append(e1)
        e1lo,e1hi=interval(e1);bookings.append(max(F(0),e1hi));ck(reach/2*interval(C1)[1]<F(5,4))
        kids2,old2,ll2=query(kids[0],q1,ll,w+1,reach/2)
        # This is deliberately a different account from transporting pre-reset Q.
        _,wrong,_,_,_=split(kids[0],old[0],ll,w+1)
        wrong_diff=old2[0]!=wrong[0]
        terminal(kids2[1],old2[1],reach/4)
        q2,meta2=canonical(kids2[0],ll2,selector);boundary.append(meta2)
        C2=expr(probs(kids2[0]),q2);cold2=expr(probs(kids2[0]),old2[0]);e2=add((C2,reach/4),(cold2,-reach/4));charges.append(e2)
        e2lo,e2hi=interval(e2);bookings.append(max(F(0),e2hi));ck(reach/4*interval(C2)[1]<F(1,2))
        terminal(kids2[0],q2,reach/4)
    def visit(ff,qq,labels,reach,depth,onpath):
        if depth==d or (policy=='zero_spine' and not onpath):
            if onpath:resets(ff,qq,labels,reach)
            else:terminal(ff,qq,reach)
            return
        available=[label for label in labels if label<w]
        label=available[0] if onpath else available[-1]
        kids,qq2,ll=query(ff,qq,labels,label,reach)
        for b in [0,1]:visit(kids[b],qq2[b],ll,reach/2,depth+1,onpath and b==0)
    visit(f,q,list(range(n+1)),F(1),0,True)
    ledger=add((releases,F(1)),(terminals,F(1)))
    expected=add((rootexpr,F(1)),(charges[0],F(1)),(charges[1],F(1)))
    ck(ledger==expected)
    conservative=Slo-sum(bookings);ck(conservative>F(3,256));ck(4*I-interval(ledger)[1]>F(3,256))
    # Product-compatible zero-fiber terminal: retain BOTH terminal reference atoms.
    Rh=[F(1,3),F(2,3)];Ph=[F(0),F(1)]
    qp=[x*y for y in Rh for x in q];pp=[x*y for y in Ph for x in p]
    ck(expr(pp,qp)!=rootexpr)
    prodlo,prodhi=interval(expr(pp,qp));hlo,hhi=interval(expr(Ph,Rh));ck(prodlo<=roothi+hhi and prodhi>=rootlo+hlo)
    return {'w':w,'m':m,'d':d,'eta':str(eta),'policy':policy,'root_I':str(I),'root_bank_lower':str(Slo),'conservative_final_reserve_lower':str(conservative),'signed_reset_intervals':[[str(a) for a in interval(x)] for x in charges],'booked_positive_upper':[str(x) for x in bookings],'actual_after_first_reset_reference_differs_from_stale_reference':wrong_diff,'boundary_models':boundary,'child_normalizers':normalizers}

def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv
    domain=[(4,0,0,F(0),'zero_spine'),(4,0,4,F(1,4),'zero_spine')] if pilot else [(w,m,d,e,p) for w,m in [(4,0),(4,1),(5,0)] for d in range(w+1) for e in [F(0),F(1,8),F(1,4)] for p in ['zero_spine','full_prefix']]
    rows=[run_case(*args) for args in domain]
    ck(any(x['actual_after_first_reset_reference_differs_from_stale_reference'] for x in rows))
    ck(any(z['W']=='1' and z['zero_reference_atoms']==1 for x in rows for z in x['boundary_models']))
    for mm in range(101):ck(16*mm+17<=17*(1<<mm))
    out={'status':'PASS','assertions':COUNT,'library_assertions_not_added':lib.COUNT,'seconds':time.perf_counter()-start,'case_count':len(rows),'reference_only_zero_fibers_retained':ZERO,'rung':'exact finite certificate plus independent all-parameter reconstruction in REVIEW.md; full theorem not Lean-checked','cases':rows}
    (RUN/'out'/('PILOT.json' if pilot else 'EXACT_RESETS.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
if __name__=='__main__':main()
