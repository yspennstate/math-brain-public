"""Direct character sums and literal all-cut CE audit; no primary kernel call."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
import check as c
ROOT=Path(__file__).resolve().parents[1]
count=0
def ok(b):
    global count
    count+=1
    assert b,count
def direct(t):
    return [F(sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(len(t)))**2,len(t)**2) for s in range(len(t))]
def maximum(xs):
    m=xs[0]
    for x in xs[1:]:m=c.add(m,c.pos(c.sub(x,m)))
    return m
def audit():
    start=time.perf_counter(); transactions=0
    for n,masks in [(2,range(16)),(3,[0,1,23,64,105,127,150,235,255])]:
      for mask in masks:
        t=[-1 if mask>>x&1 else 1 for x in range(2**n)]
        P=direct(t); N=len(P); H=c.entropy(P); U=[F(1,N)]*N
        refs=[P,c.productref(P),U,[(x+y)/2 for x,y in zip(P,U)],[F(s+1,N*(N+1)//2) for s in range(N)]]
        for i in range(n):
          children=[direct([t[x] for x in range(N) if (x>>i)&1==e]) for e in range(2)]
          for Q in refs:
            # Erase reference and recover coherent joint from ACTUAL child spectra.
            p=[(x+y)/2 for x,y in zip(*children)]; q=[F(0)]*(N//2)
            for s,x in enumerate(Q):q[c.erase_index(s,i)]+=x
            joint=[[q[s]*children[e][s]/(2*p[s]) if p[s] else q[s]/2 for s in range(N//2)] for e in range(2)]
            ts=[sum(row) for row in joint]; qs=[[x/ts[e] for x in joint[e]] for e in range(2)]
            K=c.kl(P,Q); C=c.add(H,K); O=c.kl([F(1,2)]*2,ts)
            Cs=[c.add(c.entropy(p1),c.kl(p1,q1)) for p1,q1 in zip(children,qs)]
            Js=[c.sub(c.kl(p1,c.productref(p1)),c.kl(p1,q1)) for p1,q1 in zip(children,qs)]
            R=c.sub(c.sub(C,O),c.scale(c.suml(Cs),F(1,2)))
            # Fixed coupled lottery: reset child0 only at z0, child1 only at z1.
            acts=[(1,0),(0,1)]
            # After i: each child either stops now, or reveals z and chooses
            # before/after installation independently at both actual leaves.
            child_options=[]
            for e in range(2):
                opts=[Cs[e]]
                for flags in product(range(2),repeat=2):
                    v=c.scale(c.suml([c.add(Cs[e],c.scale(Js[e],acts[z][e]*flags[z])) for z in range(2)]),F(1,2))
                    opts.append(v)
                child_options.append(opts)
            after=[C]+[c.add(O,c.scale(c.add(x,y),F(1,2))) for x in child_options[0] for y in child_options[1]]
            # Before i: at each z stop before querying, or query and pick
            # before/after installation separately in the two physical outcomes.
            z_options=[]
            for z in range(2):
                opts=[C]
                for flags in product(range(2),repeat=2):
                    opts.append(c.add(O,c.scale(c.suml([c.add(Cs[e],c.scale(Js[e],acts[z][e]*flags[e])) for e in range(2)]),F(1,2))))
                z_options.append(opts)
            before=[C]+[c.scale(c.add(x,y),F(1,2)) for x in z_options[0] for y in z_options[1]]
            ls=[c.scale(c.suml([c.scale(c.pos(Js[e]),acts[z][e]) for e in range(2)]),F(1,2)) for z in range(2)]
            pa=c.add(C,c.pos(c.sub(c.scale(c.suml(ls),F(1,2)),R)))
            pb=c.add(C,c.scale(c.suml([c.pos(c.sub(l,R)) for l in ls]),F(1,2)))
            ok(len(after)==len(before)==26)
            ok(maximum(after)==pa);ok(maximum(before)==pb);ok(c.ge(pb,pa))
            transactions+=1
    # A087 exact heterogeneous installed reference, including both real children.
    p4=direct([-1]+[1]*15); p3=direct([-1]+[1]*7)
    t=[(-1 if x==0 else 1)*(-1 if y==0 else 1) for y in range(8) for x in range(16)]
    P=direct(t); Q=[x*y for y in c.productref(p3) for x in p4]
    ok(sum(Q)==1); H4=c.entropy(p4);H3=c.entropy(p3);M3=c.add(H3,c.kl(p3,c.productref(p3)))
    actual=c.add(c.entropy(P),c.kl(P,Q));ok(actual==c.add(H4,M3))
    gap1=c.sub(actual,c.add(H4,H3));gap2=c.sub(actual,c.scale(M3,F(3,2)))
    ok(c.ge(gap1,c.const(F(1,5))));ok(c.ge(gap2,c.const(F(1,5))))
    for e in range(2):
        ct=[t[x] for x in range(128) if (x&1)==e]; cp=direct(ct)
        pointchild=direct([(-1 if x==0 else 1) if e==0 else 1 for x in range(8)])
        cq=[x*y for y in c.productref(p3) for x in pointchild]
        ok(sum(cq)==1);ok(c.kl(cp,cq)==c.sub(M3,H3))
    # Genuine relevant-coordinate inherited-reference example, R=log2(32/31).
    lifted=[(-1 if x&1 else 1)*([-1]+[1]*7)[x>>1] for x in range(16)]
    pl=direct(lifted);ql=[p3[s>>1]*(F(31,32) if s&1 else F(1,32)) for s in range(16)]
    K=c.kl(pl,ql);ok(K==c.logq(F(32,31)))
    T=c.sub(M3,H3); lam=c.scale(T,F(1,8))
    ok(c.ge(K,lam));ok(c.ge(T,K));ok(c.ge(K,c.Z))
    before=c.scale(c.sub(T,K),F(1,8));ok(c.ge(before,c.const(F(1,50))))
    # Proves the queried coordinate is relevant, with influence exactly1.
    ok(all(lifted[x]!=lifted[x^1] for x in range(16)))
    # Minimal exact actual outcome-charge guard.
    t2=[-1,1,1,1];q2=[F(j,10) for j in range(1,5)]
    pp=direct(t2);children=[direct([t2[x] for x in range(4) if x&1==e]) for e in range(2)]
    pe=[(a+b)/2 for a,b in zip(*children)]
    qe=[q2[0]+q2[1],q2[2]+q2[3]]
    pred=[sum((qe[s]*children[e][s]/(2*pe[s]) for s in range(2)),F(0)) for e in range(2)]
    ok(pred==[F(7,10),F(3,10)])
    outcome=c.kl([F(1,2)]*2,pred)
    ok(outcome==c.scale(c.logq(F(25,21)),F(1,2)));ok(c.ge(outcome,c.const(F(1,10))))
    originalK=c.kl(pp,q2);eraseE=c.sub(originalK,c.kl(pe,qe))
    ok(originalK==c.add(eraseE,outcome))
    ok(originalK!=eraseE) # actual omitted-O mutation must fail, not just compile
    result={'status':'PASS','checks':count,'transactions':transactions,'cuts_per_order':26,
      'guard':{'claim':'A087-HETEROGENEOUS-SELECTED-CUT-ENDPOINT-GUARD@1','gap_over_root':str(gap1),'gap_over_completed':str(gap2),'certified_both_gaps_gt':'1/5'},
      'data_fixture':{'source':'character_i*point3','Inf_i':'1','reference':'Ber(31/32) tensor actual point3 spectrum','D':'0','E':'log2(32/31)','O':'0','reset_probability':'1/8','after_extra':'0','before_extra_gt':'1/50'},
      'outcome_guard':{'source':'point2','reference':[str(x) for x in q2],'O':'log2(25/21)/2','certified_gt':'1/10'},
      'seconds':round(time.perf_counter()-start,6)}
    (ROOT/'out'/'AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['guard','data_fixture','outcome_guard']}))
if __name__=='__main__':audit()
