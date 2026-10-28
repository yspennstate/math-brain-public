from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import sys,itertools,time,json
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
sys.path.insert(0,str(A/'runs/20261014T094139Z-account05-A091-composition-referee/code'))
import check as a
import exact as e
START=time.perf_counter();mode=sys.argv[1];states=edges=internal=roots=0;rows=[]
def watch():assert time.perf_counter()-START<55,'frozen runtime exceeded'
def mean(t):return sum(t,Q(0))/len(t)
def var(t):return 1-mean(t)**2
def H(t):return e.entropy(a.squares(t))
@lru_cache(4096)
def influences(t):
    return tuple(Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range((len(t)-1).bit_length()))
def partial(b,g,state):
    free=[i for i,v in enumerate(state) if v==-1]
    base=sum(v<<i for i,v in enumerate(state) if v>=0)
    exterior=tuple(b[base+sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free)))
    alive=1 not in state;t=Q(1,1<<len(free)) if alive else Q(0)
    F=tuple(v+(h-1 if alive and x==0 else 0) for h in g for x,v in enumerate(exterior))
    return F,free,t
def accounts(b,g,state,blocks):
    F,free,t=partial(b,g,state);iv=influences(F);slots=[]
    for block in blocks:
        rem=[i for i in block if i in free]
        slots.append(4*sum(iv[free.index(i)] for i in rem) if len(rem)==len(block) else Q(2*len(rem)))
    return F,free,t,slots
def audit_state(b,g,state,blocks):
    global states,edges,internal
    F,free,t,slots=accounts(b,g,state,blocks);states+=1
    for j,oi in enumerate(free):
        child=[]
        for bit in (0,1):
            st=list(state);st[oi]=bit
            child.append(accounts(b,g,tuple(st),blocks))
            e.check(child[-1][0],a.cut(F,j,bit))
        owner=next(k for k,block in enumerate(blocks) if oi in block)
        for k,slot in enumerate(slots):
            drop=slot-(child[0][3][k]+child[1][3][k])/2
            e.check(drop>=2 if k==owner else drop==0,True)
        release=sum(slots)-(sum(child[0][3])+sum(child[1][3]))/2
        _,D,_=a.local(F,j);e.nonnegative(e.add((1,a.const(release)),(-1,D)))
        ts=[x[2] for x in child];e.check(t,(ts[0]+ts[1])/2)
        # Original one-fine-core profile, nonzero U for the AND2 block supplement.
        e.check(e.add((t,H(g))),e.add(((ts[0]+ts[1])/2,H(g))))
        kappa=e.add((var(g),a.eta(t)),(-var(g)/2,a.eta(ts[0])),(-var(g)/2,a.eta(ts[1])))
        e.check(kappa,a.const(t*var(g))) # R and S have this same exterior release.
        e.check(5*t*sum(influences(g)),Q(5,2)*(ts[0]+ts[1])*sum(influences(g)))
        edges+=1
    ng=(len(g)-1).bit_length()
    for i in range(ng):
        cs=[accounts(b,a.cut(g,i,v),state,blocks) for v in (0,1)]
        for k,slot in enumerate(slots):e.check(slot,(cs[0][3][k]+cs[1][3][k])/2)
        internal+=1
    watch()
def quad(n,edgeset):return tuple((-1)**sum(((x>>i)&1)*((x>>j)&1) for i,j in edgeset) for x in range(1<<n))
def rank(n,edgeset,remove=()):
    keep=[i for i in range(n) if i not in remove];rr=[]
    for i in keep:rr.append(sum(1<<j for j,k in enumerate(keep) if (min(i,k),max(i,k)) in edgeset and i!=k))
    out=0
    for bit in range(len(keep)):
        p=next((j for j in range(out,len(rr)) if rr[j]>>bit&1),None)
        if p is None:continue
        rr[out],rr[p]=rr[p],rr[out]
        for j in range(len(rr)):
            if j!=out and rr[j]>>bit&1:rr[j]^=rr[out]
        out+=1
    return out
def integer_walsh(t):
    aa=list(t);s=1
    while s<len(aa):
        for j in range(0,len(aa),2*s):
            for k in range(j,j+s):aa[k],aa[k+s]=aa[k]+aa[k+s],aa[k]-aa[k+s]
        s*=2
    return tuple(aa)
def chars(t):return tuple(Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
if mode in ('pilot','pairs'):
    lo,hi=(0,1) if mode=='pilot' else (int(sys.argv[2]),int(sys.argv[3]))
    optional=[(0,2),(0,3),(1,2),(1,3)];blocks=((0,1),(2,3))
    for mask in range(lo,hi):
        b=quad(4,[(0,1),(2,3)]+[ij for k,ij in enumerate(optional) if mask>>k&1])
        e.check(b[0],1);e.check(all(b[1<<i]==1 for i in range(4)),True)
        for gmask in range(1 if mode=='pilot' else 4):
            original=e.tab(gmask,1)
            gs=[original] if mode=='pilot' else [original,(original[0],),(original[1],)]
            for g in gs:
                for st in itertools.product((-1,0,1),repeat=4):audit_state(b,g,st,blocks)
            roots+=1
elif mode=='blocks':
    maj=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
    b=tuple(maj[x&7]*maj[x>>3] for x in range(64));blocks=((0,1,2),(3,4,5))
    for block in blocks:
        other=[i for i in range(6) if i not in block]
        for mask in range(8):
            st=tuple(-1 if i in block else (mask>>other.index(i))&1 for i in range(6))
            co,_,_=partial(b,(1,),st);e.check(sum(influences(co)),Q(3,2))
    for g in (tuple(-1 if x==0 else 1 for x in range(4)),(1,-1)):
        for st in itertools.product((-1,0,1),repeat=6):audit_state(b,g,st,blocks)
        roots+=1
elif mode=='structural':
    positions=(3,5,6,7)
    for mask in range(16):
        p=tuple((mask>>positions.index(x))&1 if x in positions else 0 for x in range(8))
        b=tuple((-1)**(((z&7)&(z>>3)).bit_count()+p[z&7]) for z in range(64))
        e.check(mean(b),Q(1,8));e.check(b[0],1);e.check(all(b[1<<i]==1 for i in range(6)),True)
        for j in range(3):
            pair=(j,j+3);other=[i for i in range(6) if i not in pair]
            for val in range(16):
                base=sum(((val>>k)&1)<<i for k,i in enumerate(other))
                e.check(e.prod(b[base+((q&1)<<pair[0])+((q>>1)<<pair[1])] for q in range(4)),-1)
        roots+=1;watch()
elif mode=='ranks':
    mandatory=((0,1),(2,3),(4,5));optional=[(i,j) for i in range(6) for j in range(i+1,6) if (i,j) not in mandatory]
    histogram={}
    for mask in range(4096):
        es=set(mandatory)|{ij for k,ij in enumerate(optional) if mask>>k&1}
        ranks=tuple(rank(6,es,z) for z in ((),(0,),(0,1)))
        b=quad(6,es);ww=integer_walsh(b);r=ranks[0]
        e.check(sum(v!=0 for v in ww),1<<r);e.check(set(v*v for v in ww if v),{1<<(12-r)})
        e.check(ranks[0]-ranks[2]<=4,True)
        histogram[str(ranks)]=histogram.get(str(ranks),0)+1
        roots+=1;watch()
    rows.append(histogram)
elif mode=='sharp':
    es=((0,1),(2,3),(4,5),(3,4),(2,5),(0,2),(1,3));b=quad(6,es)
    e.check(tuple(rank(6,set(es),z) for z in ((),(0,),(0,1))),(6,4,2));e.check(mean(b),Q(1,8))
    e.check(sum(influences(b)[:2]),Q(1))
    for bit in (0,1):
        k=a.cut(b,0,bit);e.check(H(k),a.const(4));e.check(a.local(b,0)[1],a.const(2))
        for v in (0,1):e.check(H(a.cut(k,0,v)),a.const(2))
        e.check(a.local(k,0)[1],a.const(2))
    g=tuple(-1 if y==0 else 1 for y in range(8))
    W=tuple(g[y] if x==0 else (g[y] if z==0 else b[z]) for y in range(8) for z in range(64) for x in (0,1))
    _,Dy,_=a.local(W,7);low,high=e.interval(Dy);e.check(low>0,True)
    ykids=[a.cut(W,7,v) for v in (0,1)]
    def owner(t):return 4*sum(influences(t)[1:3])
    e.check(owner(W),(owner(ykids[0])+owner(ykids[1]))/2)
    sy=ykids[1];sx=[a.cut(sy,0,v) for v in (0,1)]
    e.check(owner(sy),(4*sum(influences(sx[0])[:2])+4*sum(influences(sx[1])[:2]))/2)
    e.check(4*sum(influences(sx[1])[:2]),Q(4))
    _,Dx,dx=a.local(sy,0)
    scale=Q(65,128);ig=sum(influences(g))
    oldQ=21*scale*(ig-(sum(influences(a.cut(g,0,0)))+sum(influences(a.cut(g,0,1))))/2)
    e.check(oldQ,21*influences(W)[7])
    e.nonnegative(e.add((1,a.const(oldQ)),(-1,Dy)))
    e.check(6*influences(W)[0],3*(influences(ykids[0])[0]+influences(ykids[1])[0]))
    def exteriorE(t):return 4*sum(influences(t)[1:7])
    e.check(exteriorE(W),(exteriorE(ykids[0])+exteriorE(ykids[1]))/2)
    e.check(exteriorE(sy),2*(sum(influences(sx[0])[:6])+sum(influences(sx[1])[:6])))
    e.check(dx,Q(7,16));e.nonnegative(e.add((1,a.const(6*dx)),(-1,Dx)))
    terms=[]
    for aa in (0,1):
        t=a.cut(sx[1],0,aa);e.check(a.local(sx[1],0)[1],a.const(2))
        for bb in (0,1):
            leaf=a.cut(t,0,bb);e.check(H(leaf),a.const(2));terms.append((Q(1,16),H(leaf)))
    terminal=e.add((Q(1,2),H(ykids[0])),(Q(1,4),H(sx[0])),*terms)
    e.check(e.add((1,H(W)),(-1,terminal)),e.add((1,Dy),(Q(1,2),Dx),(1,a.const(1))))
    # Literal full P=Q+sourceS+exteriorE; original fine U/R are zero for constant-core point-test g.
    proot=21*scale*ig+6*influences(W)[0]+exteriorE(W)
    pold=21*scale*sum(influences(a.cut(g,0,0)))+6*influences(ykids[0])[0]+exteriorE(ykids[0])
    plast=[]
    for aa in (0,1):
        for bb in (0,1):
            leaf=a.cut(a.cut(sx[1],0,aa),0,bb)
            plast.append(4*sum(influences(leaf))) # both OTHER original pairs untouched; selected owner exhausted.
    bankrelease=proot-pold/2-sum(plast)/16
    e.nonnegative(e.add((1,a.const(bankrelease)),(-1,H(W)),(1,terminal)))
    rows.append({'old_internal_debit_interval':[str(low),str(high)],'old_nonconstant_sibling_entropy':{str(p):str(v) for p,v in H(ykids[0]).items()},'root_selected_owner':str(owner(W)),'old_Q_release':str(oldQ),'full_original_P_root':str(proot),'full_nonconstant_old_sibling_P':str(pold),'full_exterior_terminal_P':[str(v) for v in plast],'literal_H_minus_P_terminal_ledger_checked':True,'terminal_profile_retained':True})
    roots=1
elif mode=='nonfloor':
    for m in (4,8,12):
        N=1<<m;c=Q(1,N);s=Q(1,1<<(m//2));np=(N+(1<<(m//2)))//2;nm=N-np
        rootH=e.add((np,a.eta((s-c)**2)),(nm,a.eta((s+c)**2)),(N,a.eta(c*c)))
        minusH=e.add((np,a.eta((s-2*c)**2)),(nm,a.eta((s+2*c)**2)))
        D=e.add((1,rootH),(-Q(m,2),a.const(1)),(-Q(1,2),minusH))
        e.nonnegative(e.add((1,D),(-1,a.const(c*(m-1)))))
        # Both designated pair coordinates have actual physical influence c.
        if m in (4,8):
            b=quad(m,tuple((i,i+1) for i in range(0,m,2)))
            F=tuple((-1)**z.bit_count() if x==N-1 else b[x] for z in range(4) for x in range(N))
            wc=chars(F);e.check(H(F),e.entropy(tuple(v*v for v in wc)));e.check(H(F),rootH)
            e.check(influences(F)[m:],(c,c))
            leaves=[a.cut(a.cut(F,m,v),m,w) for v in (0,1) for w in (0,1)]
            e.check(e.add((1,H(F)),*[(-Q(1,4),H(t)) for t in leaves]),D)
        rows.append({'m':m,'designated_pair_influence':str(2*c),'debit_over_pair_influence_lower_bound':str(Q(m-1,2))});roots+=1;watch()
    bad=(1,-1,-1,-1);F=(-1,-1,-1,-1)
    e.check(influences(F),(Q(0),Q(0)));e.check(a.local(F,0)[1],{})
    e.check(Q(0)-(Q(2)+Q(2))/2,Q(-2))
else:raise ValueError(mode)
tag=mode+('_'+sys.argv[2]+'_'+sys.argv[3] if mode=='pairs' else '')
out={'status':'PASS','mode':mode,'roots':roots,'states':states,'exterior_edges':edges,'internal_harmonic_edges':internal,'exact_assertions':e.COUNT,'runtime_seconds':time.perf_counter()-START,'rows':rows,'formal_status':'ANALYTIC_AND_EXACT_CERTIFICATES; NOT_LEAN_VERIFIED'}
(R/'out'/('CHECK_'+tag+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
