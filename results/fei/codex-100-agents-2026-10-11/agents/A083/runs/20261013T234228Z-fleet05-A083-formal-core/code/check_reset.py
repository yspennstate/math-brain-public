from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from functools import lru_cache
import json,time,sys,itertools
R=Path(__file__).resolve().parents[1]
mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
domain=[1] if mode=='pilot' else [1,2,3,4,5]
spec={'helper_version':'check_reset.py v1','family':'Boolean product of r disjoint two-bit AND signs; prescribed essential pair-first computing tree','domain':domain,'case_count':len(domain),'symmetry':'none','arithmetic':'integer Walsh, direct physical table, Fraction coherent joint and exact prime-log entropy forms','memory_estimate_MB':80,'maximum_runtime_seconds':60,'formal_boundary':'Lean checks local rational row transport, not entropy or Fourier transforms'}
(R/f'out/RESET_{mode.upper()}_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1
@lru_cache(None)
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def add(*terms):
    out=defaultdict(Q)
    for scale,form in terms:
        for p,c in form.items(): out[p]+=scale*c
    return {p:c for p,c in out.items() if c}
def entropy(ps):
    ps=list(ps); eq(sum(ps),Q(1))
    out=defaultdict(Q)
    for p in ps:
        assert p>=0
        if p:
            for v,c in factors(p.denominator).items(): out[v]+=p*c
            for v,c in factors(p.numerator).items(): out[v]-=p*c
    return {p:c for p,c in out.items() if c}
def const(x): return {2:Q(x)} if x else {}
def serial(form): return {str(k):str(v) for k,v in sorted(form.items())}
def fwht(vals):
    a=list(vals); width=1
    while width<len(a):
        for i in range(0,len(a),2*width):
            for j in range(i,i+width):
                u,v=a[j],a[j+width]; a[j],a[j+width]=u+v,u-v
        width*=2
    return a
def block_sign(x,r):
    return (-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(r))
def spectrum(vals,rem):
    N=len(vals); w=fwht(vals); out={}
    for s,v in enumerate(w):
        phys=sum(1<<q for j,q in enumerate(rem) if (s>>j)&1)
        out[phys]=Q(v,N)
    eq(sum(c*c for c in out.values()),Q(1))
    return out
def restricted(truth,n,fixed):
    rem=[i for i in range(n) if i not in fixed]
    base=sum(v<<i for i,v in fixed.items())
    vals=[truth[base+sum(((x>>j)&1)<<q for j,q in enumerate(rem))] for x in range(1<<len(rem))]
    return vals,rem
def transcript(x,r):
    return tuple(0 if not ((x>>(2*j))&1) else 1+((x>>(2*j+1))&1) for j in range(r))
def actual_joint(r):
    n=2*r; truth=[block_sign(x,r) for x in range(1<<n)]
    coeff=spectrum(truth,list(range(n))); root={s:c*c for s,c in coeff.items() if c}
    joint=defaultdict(Q); yjoint=defaultdict(Q); js={}; nodes=0; zero_rows=0
    def walk(fixed,code,block,need_second,weights):
        nonlocal js,nodes,zero_rows
        vals,rem=restricted(truth,n,fixed); coeff=spectrum(vals,rem)
        prob=sum(weights.values())
        projected=defaultdict(Q)
        rem_mask=sum(1<<i for i in rem)
        for s,w in weights.items(): projected[s&rem_mask]+=w/prob
        eq(dict(projected),{s:c*c for s,c in coeff.items() if c})
        if block==r:
            eq(set(vals),{vals[0]}); eq(entropy([c*c for c in coeff.values()]),{})
            for s,w in weights.items(): joint[s,code]+=w
            yjoint[code,vals[0]]+=prob
            return
        i=2*block+int(need_second); nodes+=1
        children=[]
        for b in [0,1]:
            nxt=dict(fixed); nxt[i]=b
            cv,cr=restricted(truth,n,nxt); children.append((nxt,spectrum(cv,cr)))
        q={s:c*c+coeff.get(s|(1<<i),Q(0))**2 for s,c in coeff.items() if not (s>>i)&1}
        positive_q={s:w for s,w in q.items() if w}
        packet_joint={(b,t):children[b][1][t]**2/2 for t in q for b in [0,1] if children[b][1][t]}
        eq(sum(packet_joint.values()),Q(1))
        node_j=add((Q(1),const(1)),(Q(1),entropy(positive_q.values())),(-Q(1),entropy(packet_joint.values())))
        js=add((Q(1),js),(prob,node_j))
        child_weights=[defaultdict(Q),defaultdict(Q)]
        for s,w in weights.items():
            t=(s&rem_mask)&~(1<<i); denom=q[t]
            assert denom>0
            for b in [0,1]: child_weights[b][s]+=w*children[b][1][t]**2/(2*denom)
        zero_rows+=sum(not v for v in q.values())
        for b in [0,1]:
            child_weights[b]={s:w for s,w in child_weights[b].items() if w}
            eq(sum(child_weights[b].values()),prob/2)
            nxt=children[b][0]
            if need_second: walk(nxt,code+(1+b,),block+1,False,child_weights[b])
            elif b==0: walk(nxt,code+(0,),block+1,False,child_weights[b])
            else: walk(nxt,code,block,True,child_weights[b])
    walk({},(),0,False,root)
    eq(sum(joint.values()),Q(1)); eq(js,const(r))
    actual_p=defaultdict(Q); actual_y=defaultdict(Q)
    for x,y in enumerate(truth):
        c=transcript(x,r); actual_p[c]+=Q(1,1<<n); actual_y[c,y]+=Q(1,1<<n)
    proj=defaultdict(Q)
    for (s,c),w in joint.items(): proj[c]+=w
    eq(dict(proj),dict(actual_p)); eq(dict(yjoint),dict(actual_y))
    # A different representation: tensor the explicitly derived six-entry base law.
    base=[(0,0,Q(1,4)),(1,0,Q(1,4)),(2,1,Q(1,8)),(2,2,Q(1,8)),(3,1,Q(1,8)),(3,2,Q(1,8))]
    tensor=defaultdict(Q)
    for row in itertools.product(base,repeat=r):
        s=sum(v[0]<<(2*j) for j,v in enumerate(row)); c=tuple(v[1] for v in row); w=Q(1)
        for v in row: w*=v[2]
        tensor[s,c]+=w
    eq(dict(joint),dict(tensor))
    HS=entropy(root.values()); HP=entropy(proj.values()); HSP=entropy(joint.values())
    hy=defaultdict(Q)
    for (c,y),p in yjoint.items(): hy[y]+=p
    HY=entropy(hy.values()); HPY=entropy(yjoint.values())
    eq(HS,const(2*r)); eq(HP,const(Q(3*r,2))); eq(HSP,const(Q(5*r,2)))
    eq(HPY,HP)
    hproot=add((Q(1),HSP),(-Q(1),HS))
    hpout=add((Q(1),HPY),(-Q(1),HY))
    Croot=add((Q(1),hpout),(-Q(1),hproot))
    Creset=add((Q(1),hpout),(-Q(1),HP))
    eq(add((Q(1),Croot),(Q(1),HY)),const(r))
    eq(add((Q(1),Creset),(Q(1),HY)),{})
    eq(add((Q(1),Croot),(-Q(1),Creset)),const(r))
    edgeI=Q(sum(truth[x]!=truth[x^(1<<i)] for x in range(1<<n) for i in range(n)),1<<n)
    spectralI=sum(Q(s.bit_count())*p for s,p in root.items())
    eq(edgeI,spectralI); eq(edgeI,Q(r)); eq(HY,entropy([Q((1<<r)-1,1<<(r+1)),Q((1<<r)+1,1<<(r+1))]))
    if r==1:
        eq(Croot,{2:Q(-1),3:Q(3,4)}); eq(Creset,{2:Q(-2),3:Q(3,4)})
        assert 3**3>2**4 and 3**3<2**8
    return {'r':r,'variables':n,'truth_table':truth if r==1 else None,'nodes':nodes,'joint_nonzero_atoms':len(joint),'zero_rows_handled':zero_rows,'joint':[{ 'S':s,'Pi':list(c),'mass':str(w)} for (s,c),w in joint.items()] if r==1 else None,'H_Pi_given_root':serial(hproot),'C_root':serial(Croot),'C_terminal_reset':serial(Creset),'reset_gap_bits':r,'I':str(edgeI),'sum_weighted_JS':serial(js),'terminal_spectral_entropy':{} }
start=time.perf_counter(); rows=[]
for r in domain:
    rows.append(actual_joint(r))
    (R/f'out/RESET_{mode.upper()}_RESULT.json').write_text(json.dumps({'status':'IN_PROGRESS','checks':checks,'cases':rows},indent=2),encoding='utf-8')
elapsed=time.perf_counter()-start; assert elapsed<60
result={'status':'PASS','mode':mode,'checks':checks,'cases':rows,'elapsed_seconds':elapsed,'strict_one_block_sign_certificate':'27>16 and 27<256; all entropy identities exact prime-log coefficient maps','full_FEI':'OPEN'}
(R/f'out/RESET_{mode.upper()}_RESULT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
