from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import sys,importlib.util,json,time,argparse
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1]
(RUN/'out').mkdir(exist_ok=True)
old=RUN.parents[0]/'20261011T223622Z-fleet05-A024-biased-child-stability/code/check.py'
loader=importlib.util.spec_from_file_location('a024_prior',old)
v=importlib.util.module_from_spec(loader); loader.loader.exec_module(v)
v.walsh=lru_cache(maxsize=512)(v.walsh)
v.L=lru_cache(maxsize=32768)(v.L)
v.erasure=lru_cache(maxsize=2048)(v.erasure)
assertions=0; signs=0; distinct_nodes=0
sign_certificates={}
deadline=float('inf')
def watchdog():
    if time.perf_counter()>deadline: raise RuntimeError('Frozen runtime cap reached; saved partial outputs retained')

def ck(a,b):
    global assertions
    assert a==b,(a,b)
    assertions+=1
def ln_bounds(x,n=24):
    z=(x-1)/(x+1); total=Q(0); power=z
    for j in range(n): total+=2*power/(2*j+1); power*=z*z
    return total,total+2*power/((2*n+1)*(1-z*z))
@lru_cache(None)
def log2_bounds(p,n=24):
    k=p.bit_length()-1; y=Q(p,1<<k)
    l,u=ln_bounds(y,n); l2,u2=ln_bounds(Q(2),n)
    return Q(k)+l/u2,Q(k)+u/l2
def bounds(expr,n=24):
    lo=hi=Q(0)
    for p,c in expr.items():
        a,b=log2_bounds(p,n)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi
def sign(expr):
    global signs
    signs+=1
    if not expr: return 0
    key=tuple(sorted(expr.items()))
    if key in sign_certificates: return sign_certificates[key]['sign']
    lo,hi=bounds(expr)
    terms=24
    if not (lo>0 or hi<0): lo,hi=bounds(expr,48); terms=48
    assert lo>0 or hi<0,('uncertified',expr,str(lo),str(hi))
    s=1 if lo>0 else -1
    sign_certificates[key]={'log_coefficients':{str(p):str(c) for p,c in expr.items()},'lower':str(lo),'upper':str(hi),'terms':terms,'sign':s}
    return s
@lru_cache(maxsize=4096)
def I(tab):
    n=(len(tab)).bit_length()-1
    cuts=sum(tab[x]!=tab[x|1<<i] for i in range(n) for x in range(len(tab)) if not x>>i&1)
    return Q(2*cuts,len(tab))
def odd_faces(tab):
    n=len(tab).bit_length()-1; faces=0
    for i in range(n):
        for j in range(i+1,n):
            for x in range(len(tab)):
                if not x>>i&1 and not x>>j&1:
                    faces+=tab[x]*tab[x|1<<i]*tab[x|1<<j]*tab[x|1<<i|1<<j]<0
    return Q(2*faces,len(tab))
def module():
    b=tuple((-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16))
    return tuple(-b[x>>1] if (x&1 and x>>1==0) else b[x>>1] for x in range(32))
C=module(); CM=Q(sum(C),len(C)); CI=I(C); CQ=odd_faces(C)
D=Q(1,16); BS=v.erasure(C,0)

def compose_gate(g,core,mask):
    nc=len(core).bit_length()-1
    return tuple(g[(core[x&((1<<nc)-1)]>0)+2*(mask[x>>nc]>0)] for x in range(len(core)*len(mask)))
def root_grid(pilot):
    rows=[]
    gate_masks=range(1) if pilot else range(16)
    for kg in gate_masks:
        watchdog()
        g=v.table(2,kg)
        for kh in range(16):
            h=v.table(2,kh); f=compose_gate(g,C,h)
            gamma=int(g[0]*g[1]*g[2]*g[3]<0)
            a=tuple(Q(g[0 if hh<0 else 2]+g[1 if hh<0 else 3],2) for hh in h)
            b=tuple(Q(g[1 if hh<0 else 3]-g[0 if hh<0 else 2],2) for hh in h)
            t=sum(bb*bb for bb in b)/4
            wsign=tuple(1-2*bb*bb for bb in b)
            ck(I(wsign),gamma*I(h))
            other=Q(0)
            for cc in C:
                i=int(cc>0); der=Q(g[i+2]-g[i],2); other+=der*der/32
            ck(I(f),t*CI+other*I(h))
            ck(odd_faces(f),t*CQ+other*odd_faces(h)+Q(gamma,2)*CI*I(h))
            aa,bb=v.walsh(a),v.walsh(b)
            for i in range(7):
                children=[v.restrict(f,7,i,z) for z in [0,1]]
                d=Q(sum(x!=y for x,y in zip(*children)),len(children[0]))
                q=I(tuple(x*y for x,y in zip(*children)))/2
                BF=v.erasure(f,i)
                bad=sign(v.add(BF,v.scalar(-4*d)))>0
                if i<5:
                    cc=[v.restrict(C,5,i,z) for z in [0,1]]
                    dc=Q(sum(x!=y for x,y in zip(*cc)),len(cc[0]))
                    qc=I(tuple(x*y for x,y in zip(*cc)))/2
                    beta=Q(sum(cc[0])-sum(cc[1]),2*len(cc[0]))
                    ck(q,t*qc+dc*I(wsign)/2)
                    ck(d,t*dc)
                    residual=v.add(*(v.L(x+CM*y,beta*y) for x,y in zip(aa,bb)),v.scale(-t,v.L(CM,beta)))
                    ck(BF,v.add(v.scale(t,v.erasure(C,i)),residual))
                else:
                    hh=[v.restrict(h,2,i-5,z) for z in [0,1]]
                    dh=Q(sum(x!=y for x,y in zip(*hh)),len(hh[0]))
                    qh=I(tuple(x*y for x,y in zip(*hh)))/2
                    ck(q,other*qh+Q(gamma,2)*dh*CI)
                    ck(d,other*dh)
                if i==0:
                    if t: assert bad
                    rows.append({'gate_mask':kg,'second_child_mask':kh,'gamma':gamma,'t':str(t),'bad_K4':bad,'credit':str(q),'influence':str(I(f)),'credit_over_root_I':str(q/I(f)) if I(f) else None,'B_minus_4d_logform':{str(p):str(c) for p,c in v.add(BF,v.scalar(-4*d)).items()}})
        (RUN/'out/ROOT_GRID.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    (RUN/'out/ROOT_GRID.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    return rows
def family(l,n):
    bits=5*l+n
    return tuple(1 if ((x>>(5*l)).bit_count()&1) else __import__('functools').reduce(lambda a,j:a*C[(x>>(5*j))&31],range(l),1) for x in range(1<<bits))
def reorder(tab,order):
    return tuple(tab[sum(((x>>i)&1)<<coord for i,coord in enumerate(order))] for x in range(len(tab)))
@lru_cache(maxsize=4096)
def tree(tab):
    global distinct_nodes
    distinct_nodes+=1
    if distinct_nodes%100==0: watchdog()
    if all(x==tab[0] for x in tab): return Q(0),Q(0),Q(0),0,0
    n=len(tab).bit_length()-1
    g,h=[v.restrict(tab,n,0,z) for z in [0,1]]
    d=Q(sum(x!=y for x,y in zip(g,h)),len(g)); q=I(tuple(x*y for x,y in zip(g,h)))/2
    B=v.erasure(tab,0); bad=sign(v.add(B,v.scalar(-4*d)))>0
    c0,c1=tree(g),tree(h)
    return ((q if bad else Q(0))+(c0[0]+c1[0])/2,q+(c0[1]+c1[1])/2,d+(c0[2]+c1[2])/2,int(bad)+c0[3]+c1[3],1+c0[4]+c1[4])
def trees(pilot):
    domains=[(1,1)] if pilot else [(1,1),(1,2),(1,4),(2,1),(2,2),(2,4)]
    rows=[]
    for l,n in domains:
        f=family(l,n); mi=CM**l
        expected=(l*CI+(1-mi)*n)/2
        ck(I(f),expected)
        expectedq=l*CQ/2+Q(l,2)*CI*n
        selectors=[5*j for j in range(l)]
        data=[5*j+i for j in range(l) for i in range(1,5)]
        parity=list(range(5*l,5*l+n))
        for ordername,order in [('selectors-first',selectors+data+parity),('parity-first',parity+selectors+data)]:
            result=tree(reorder(f,order)); bill,qtotal,ispent,nbad,nodes=result
            ck(qtotal,expectedq); ck(ispent,expected)
            if ordername=='parity-first': ck(bill,Q(l,8))
            else: assert bill>=Q(l,32)*(4+n)
            rows.append({'L':l,'N':n,'order':ordername,'I':str(expected),'bad_credit':str(bill),'bad_credit_over_I':str(bill/expected),'total_Q':str(qtotal),'expanded_bad_nodes':nbad,'expanded_internal_nodes':nodes,'terminal_entropy':0})
            (RUN/'out/TREE_LEDGER.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    return rows
def main():
    global deadline
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    start=time.perf_counter()
    deadline=start+(60 if args.pilot else 300)
    if args.pilot and (RUN/'out/ROOT_GRID.json').exists() and not (RUN/'out/METHOD1_PARTIAL_ROOT_GRID.json').exists():
        (RUN/'out/METHOD1_PARTIAL_ROOT_GRID.json').write_bytes((RUN/'out/ROOT_GRID.json').read_bytes())
    ck(CM,Q(3,16));ck(CI,Q(37,16))
    ck(I(tuple(a*b for a,b in zip(v.restrict(C,5,0,0),v.restrict(C,5,0,1))))/2,Q(1,4))
    assert sign(v.add(BS,v.scalar(-Q(1,4))))>0
    nonempty=v.add(BS,v.scale(-1,v.L(CM,D)),v.scalar(-Q(1,4)))
    assert sign(nonempty)>0
    product_certificate={'module_B_margin':{'left':str((1<<192)*13**156),'right':str(5**200*3**180)},'nonempty_B_margin':{'left':str((1<<182)*13**156),'right':str(5**210*3**162)}}
    for row in product_certificate.values(): assert int(row['left'])>int(row['right'])
    ck(v.add(BS,v.scalar(-Q(1,4))),{2:Q(192,256),13:Q(156,256),5:-Q(200,256),3:-Q(180,256)})
    ck(nonempty,{2:Q(182,256),13:Q(156,256),5:-Q(210,256),3:-Q(162,256)})
    (RUN/'out/INTEGER_CERTIFICATES.json').write_text(json.dumps(product_certificate,indent=2),encoding='utf-8')
    bslo,bshi=bounds(v.add(BS,v.scalar(-Q(1,4))))
    rows=root_grid(args.pilot); ledger=trees(args.pilot)
    symbolic=[]
    for l in range(1,33):
        n=l*l; inf=(l*CI+(1-CM**l)*n)/2
        badlower=Q(l,32)*(4+n); goodbill=Q(l,8)
        assert badlower/inf>=Q(l,53); assert goodbill/inf<=Q(4,37)
        symbolic.append({'L':l,'N':n,'I':str(inf),'selectors_first_lower_ratio':str(badlower/inf),'parity_first_exact_ratio':str(goodbill/inf),'signed_mean_bank_upper':str(Q(l*(2*l+4),16**(l+1)))})
    (RUN/'out/SYMBOLIC_ROWS.json').write_text(json.dumps(symbolic,indent=2),encoding='utf-8')
    (RUN/'out/SIGN_CERTIFICATES.json').write_text(json.dumps(list(sign_certificates.values()),indent=2),encoding='utf-8')
    res={'status':'PASS','exact_assertions':assertions,'certified_log_signs':signs,'root_compositions':len(rows),'root_physical_splits':len(rows)*7,'root_bad_selectors':sum(z['bad_K4'] for z in rows),'complete_trees':len(ledger),'distinct_tree_states':distinct_nodes,'module_margin_lower':str(bslo),'module_margin_upper':str(bshi),'seconds':time.perf_counter()-start,'terminal_entropy':0,'arithmetic':'integer spectra, exact Fraction edge/face/credit ledgers, rational prime-log interval signs'}
    (RUN/'out'/('PILOT_V2.json' if args.pilot else 'VALIDATION.json')).write_text(json.dumps(res,indent=2),encoding='utf-8')
    print(json.dumps({k:z for k,z in res.items() if not k.startswith('module_margin')}))
if __name__=='__main__': main()
