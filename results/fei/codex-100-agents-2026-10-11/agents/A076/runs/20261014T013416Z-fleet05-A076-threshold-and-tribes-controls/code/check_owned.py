"""A076 owned-pivot v1: actual Boolean spectra, edges, and stopped trees."""
from pathlib import Path
import argparse,json,time,hashlib
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
exec(compile((ROOT/'code/arithmetic.py').read_text(encoding='utf-8'),str(ROOT/'code/arithmetic.py'),'exec'))
parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
start=time.perf_counter();limit=55 if args.pilot else 600
# Trees repeatedly revisit identical restrictions; cache exact immutable results.
H=lru_cache(maxsize=4096)(H);B=lru_cache(maxsize=8192)(B)
I=lru_cache(maxsize=4096)(I);inf=lru_cache(maxsize=8192)(inf)
def enc(e):return [[str(x),str(c)] for x,c in sorted(e.items())]
def mux(g,h):return tuple(v for a,b in zip(g,h) for v in [a,b])
def actual_inf(t,i):
    return F(sum(t[z]!=t[z^(1<<i)] for z in range(len(t))),len(t))
@lru_cache(maxsize=8192)
def collision(g,h,i):
    cg=coeff(g);ch=coeff(h)
    expression={}
    for s in range(len(g)):
        if s>>i&1:continue
        u,a,v,b=cg[s],cg[s|(1<<i)],ch[s],ch[s|(1<<i)]
        expression=plus((expression,F(1)),(Phi((u+v)**2,(a+b)**2),F(1,4)),(Phi((u-v)**2,(a-b)**2),F(1,4)))
    return expression
@lru_cache(maxsize=4096)
def potential(g,h):
    return plus(*[(phi((u+v)**2/4),F(1)) for u,v in zip(coeff(g),coeff(h))],
                *[(phi((u-v)**2/4),F(1)) for u,v in zip(coeff(g),coeff(h))],(H(g),F(-1,2)),(H(h),F(-1,2)))
def ispoint(g):return len(set(g))==1 or min(g.count(1),g.count(-1))==1
records=[];nodes=0;tree_cases=0
def run_tree(g0,h0,descending,mode,fixture):
    global nodes,tree_cases
    tree_cases+=1;todo=[(g0,h0,F(1),0)];bg={};bh={};bf={};dt={};term={};coreterm={};potterm={}
    ph=pg0=pg1=lif=lig=lih=F(0);majorant=F(0);quadbound=F(0)
    while todo:
        if time.perf_counter()-start>limit:raise RuntimeError('frozen runtime limit')
        g,h,w,depth=todo.pop();n=len(g).bit_length()-1;f=mux(g,h)
        ih=[inf(h,i) for i in range(n)];ig=[inf(g,i) for i in range(n)]
        active=[i for i in range(n) if ih[i]];gactive=[i for i in range(n) if ig[i]]
        stop=(not active and not gactive) or (mode=='one' and depth>=1) or (mode=='H' and not active)
        if stop:
            term=plus((term,F(1)),(H(f),w));coreterm=plus((coreterm,F(1)),(H(g),w/2),(H(h),w/2))
            potterm=plus((potterm,F(1)),(potential(g,h),w));lif+=w*I(f);lig+=w*I(g);lih+=w*I(h)
            if mode=='complete':
                eq(len(set(g))==1 and len(set(h))==1,True)
                equal_expr(H(f));equal_expr(B(f,0))
            continue
        candidates=active if active else gactive;i=candidates[-1] if descending else candidates[0]
        nodes+=1;di=inf(f,i+1);eq(di,(ig[i]+ih[i])/2)
        eq(di,actual_inf(f,i+1));eq(ih[i],actual_inf(h,i));eq(ig[i],actual_inf(g,i))
        bb=B(f,i+1);gg=B(g,i);hh=B(h,i)
        equal_expr(plus((bb,F(1)),(collision(g,h,i),F(-1))))
        correction=plus((bb,F(1)),(gg,F(-1,2)),(hh,F(-1,2)))
        leq(bb,F(1));leq(plus((gg,F(1,2)),(hh,F(1,2))),F(1))
        if active:
            eq(ih[i]>=F(1,2),True);ph+=w*ih[i];pg1+=w*ig[i];majorant+=w
            leq(bb,4*di)
        else:
            pg0+=w*ig[i];majorant+=w*ig[i]
            leq(correction,ig[i]);leq(plus((correction,F(-1))),ig[i])
            if fixture:
                eq(ispoint(g),True);leq(gg,3*ig[i]);leq(bb,5*di)
        for out,e in [('bg',gg),('bh',hh),('bf',bb),('dt',correction)]:
            if out=='bg':bg=plus((bg,F(1)),(e,w))
            elif out=='bh':bh=plus((bh,F(1)),(e,w))
            elif out=='bf':bf=plus((bf,F(1)),(e,w))
            else:dt=plus((dt,F(1)),(e,w))
        todo.extend((child(g,i,b),child(h,i,b),w/2,depth+1) for b in range(2))
    eq(ph+lih,I(h0));eq(pg0+pg1+lig,I(g0))
    eq((ph+pg0+pg1)/2+lif,I(mux(g0,h0)))
    budget=2*ph+pg0;eq(majorant<=budget,True)
    equal_expr(plus((bf,F(1)),(bg,F(-1,2)),(bh,F(-1,2)),(dt,F(-1))))
    equal_expr(plus((term,F(1)),(coreterm,F(-1)),(potterm,F(-1))))
    leq(dt,budget);leq(plus((dt,F(-1))),budget)
    if fixture and mode=='complete':leq(bf,5*I(mux(g0,h0)))
    return dict(order='descending' if descending else 'ascending',stop=mode,H_spent=str(ph),G_suffix_spent=str(pg0),
                G_prefix_spent=str(pg1),H_leafI=str(lih),G_leafI=str(lig),budget=str(budget),
                signed_correction=enc(dt),B=enc(bf),inherited_G_B=enc(bg),inherited_H_B=enc(bh),terminal_H=enc(term))
def table(n,mask):return tuple(1-2*((mask>>z)&1) for z in range(1<<n))
roots=[]
for n in range(3):
    for a in range(1<<(1<<n)):
        for b in range(1<<(1<<n)):roots.append((dict(n=n,Gmask=a,Hmask=b),table(n,a),table(n,b),False))
if not args.pilot:
    for a in range(256):
        for sign in [1,-1]:
            h=tuple(sign*(-1)**(((z&1)*((z>>1)&1))^((z>>2)&1)) for z in range(8))
            roots.append((dict(n=3,Gmask=a,Hprofile='b0*b1+b2',sign=sign),table(3,a),h,False))
    for k in [2,4,6]:
        g=tuple(-1 if z==0 else 1 for z in range(1<<(k+1)))
        h=tuple((-1)**sum(((z>>j)&1)*((z>>(j+1))&1) for j in range(0,k,2)) for z in range(len(g)))
        roots.append((dict(n=k+1,fixture='A078',k=k),g,h,True))
for label,g,h,fixture in roots:
    eq(sum(v*v for v in coeff(mux(g,h))),F(1))
    equal_expr(plus((H(mux(g,h)),F(1)),(H(g),F(-1,2)),(H(h),F(-1,2)),(potential(g,h),F(-1))))
    rr=[run_tree(g,h,d,m,fixture) for d in [False,True] for m in ['complete','one','H']]
    records.append(dict(root=label,trees=rr))
    if len(records)%100==0:
        (ROOT/'out/CHECKPOINT.json').write_text(json.dumps(dict(completed_roots=len(records),last_root=label,elapsed_seconds=time.perf_counter()-start))+'\n',encoding='utf-8')
name='PILOT' if args.pilot else 'FULL'
result=dict(status='PASS',helper_version='owned-pivot-v1c',roots=len(roots),tree_cases=tree_cases,nodes=nodes,
 exact_assertions=checks,elapsed_seconds=time.perf_counter()-start,memory_estimate_MB=180,
 arithmetic='Fraction spectra/edge counts; exact rational prime-exponent identities; rigorous rational log intervals')
(ROOT/'out'/f'{name}_LEDGERS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
(ROOT/'out'/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
