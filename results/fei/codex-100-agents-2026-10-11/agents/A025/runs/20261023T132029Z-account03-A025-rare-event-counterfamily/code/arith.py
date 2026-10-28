"""Independent reconstruction: no local imports, direct DFT, physical pivots."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,sys,math
ROOT=Path(__file__).resolve().parents[1]; count=0; RECEIPTS=None
def ck(ok,tag):
    global count
    count+=1
    if not ok: raise AssertionError((count,tag))
def add(*terms):
    d={}
    for term in terms:
        for p,v in term.items(): d[p]=d.get(p,F(0))+v
    return {p:v for p,v in d.items() if v}
def scale(d,s): return {p:v*s for p,v in d.items() if v*s}
def c(s): return {2:F(s)} if s else {}
def reduce_logs(expr):
    """Exact atom refinement; termination decreases product of integer bases.

    Split log(a),log(b) at gcd(a,b) until remaining bases are pairwise
    coprime. After clearing rational coefficients, unique factorization
    proves zero iff all coefficients cancel. NO large prime search.
    """
    d=dict(expr)
    while True:
        keys=list(d); found=False
        for j,a in enumerate(keys):
            for b in keys[j+1:]:
                g=math.gcd(a,b)
                if g==1: continue
                x,y=d.pop(a),d.pop(b)
                for base,v in ((a//g,x),(b//g,y),(g,x+y)):
                    if base>1: d[base]=d.get(base,F(0))+v
                d={p:v for p,v in d.items() if v}; found=True; break
            if found: break
        if not found: return d
def same(a,b): return not reduce_logs(add(a,scale(b,-1)))
def logq(x):
    x=F(x)
    return add({x.numerator:F(1)} if x.numerator>1 else {},{x.denominator:F(-1)} if x.denominator>1 else {})
def ent(ps): return add(*(scale(logq(p),-p) for p in ps if p))
def cross(p,q):
    ck(len(p)==len(q),'complete reference dimension')
    ck(sum(q)==1,'complete normalized reference')
    ck(all(r>0 for x,r in zip(p,q) if x),'all true atoms supported')
    return add(*(scale(logq(r),-x) for x,r in zip(p,q) if x))
def divg(p,q): return add(cross(p,q),scale(ent(p),-1))
def mean(xs): return scale(add(*xs),F(1,len(xs)))
@lru_cache(None)
def logbound(p):
    k=p.bit_length()-1
    def ln(x):
        z=(x-1)/(x+1); a=F(0); power=z
        for j in range(48): a+=2*power/(2*j+1); power*=z*z
        return a,a+2*power/(97*(1-z*z))
    lo,hi=ln(F(p,2**k)); ll,lh=ln(F(2)); return k+lo/lh,k+hi/ll
def bounds(e):
    l=h=F(0)
    for p,v in reduce_logs(e).items():
        a,b=logbound(p)
        if v<0: a,b=b,a
        l+=v*a; h+=v*b
    return l,h
def ge(e,tag): ck(bounds(e)[0]>=0,tag)
@lru_cache(None)
def amplitudes(f):
    return tuple(F(sum(val*(-1 if (s&x).bit_count()%2 else 1) for x,val in enumerate(f)),len(f)) for s in range(len(f)))
def law(f): return tuple(x*x for x in amplitudes(tuple(f)))
def cut(f,i,b): return tuple(v for x,v in enumerate(f) if (x>>i)&1==b)
def physical(f,i): return F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def ref(a,delta):
    p=list(scale_dummy(law(a),delta)); p[0]+=1-delta; return tuple(p)
def scale_dummy(xs,q): return [x*q for x in xs]
def overhead(s,d):
    return add(ent([1-d+d*s*s]),scale(ent([s*s]),-d),scale(logq(1/d),d*(1-s*s)))
def scalar():
    start=time.perf_counter()
    for delta in (F(1,8),F(1,64),F(1,512)):
        for j in range(-8,9):
            for k in range(-8,9):
                a,b=F(j,8),F(k,8)
                e=add(overhead((a+b)/2,delta),scale(mean([overhead(a,delta),overhead(b,delta)]),-1))
                ge(e,'867 frozen rare Jensen pairs')
    witnesses=[]
    for r in range(5,11):
        actual=tuple(-1 if z==0 else 1 for z in range(2**r))
        s=F(sum(actual),2**r); cs=[F(sum(cut(actual,0,b)),2**(r-1)) for b in (0,1)]
        ck(s==1-F(1,2**(r-1)) and cs==[1-F(1,2**(r-2)),F(1)],'actual Boolean density counterfamily')
        gap=add(overhead(s,F(1,2)),scale(mean([overhead(x,F(1,2)) for x in cs]),-1))
        ck(bounds(gap)[1]<0,'dense extension must FAIL for each frozen r')
        witnesses.append({'r':r,'delta':'1/2','mean':str(s),'child_means':list(map(str,cs)),'gap':{str(k):str(v) for k,v in gap.items()},'gap_upper':str(bounds(gap)[1])})
    result={'status':'PASS','assertions':count,'rare_pairs':867,'dense_boolean_witness':witnesses,'seconds':time.perf_counter()-start}
    (ROOT/'out/SCALAR.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:v for k,v in result.items() if k!='dense_boolean_witness'}))
def qdata(labels,fixed):
    result=[]
    for S in range(2**len(labels)):
        v=F(1)
        for B in range(2):
            free=[i for i in range(3*B,3*B+3) if i in labels]
            mark=sum(((S>>labels.index(i))&1)<<j for j,i in enumerate(free))
            assigned=[fixed[i] for i in range(3*B,3*B+3) if i in fixed]
            if len(assigned)==0: v*=F(9 if mark==0 else 1,16)
            elif len(assigned)==1: v*=F(1,4) if assigned[0]==0 else F(13 if mark==0 else 1,16)
            elif len(assigned)==2: v*=F(15 if mark==int(not any(assigned)) else 1,16)
        result.append(v)
    return result
def fixture(vertex,A,depth,policy):
    delta=F(1,64); U=F(1,32); labels=list(range(depth,6)); nc=len(labels); control_dim=len(A).bit_length()-1
    state_cache={}
    def state(fixedctrl):
        key=tuple(sorted(fixedctrl.items()))
        if key in state_cache: return state_cache[key]
        ctrls=[i for i in range(control_dim) if i not in fixedctrl]
        a=[]
        for z in range(2**len(ctrls)):
            original=sum(b<<i for i,b in fixedctrl.items())+sum(((z>>j)&1)<<i for j,i in enumerate(ctrls))
            a.append(1-2*A[original])
        a=tuple(a); R=ref(a,delta); L=scale(ent(law(a)),delta); Hs=[]; Cs=[]; infl=F(0); rows=[]
        for h in range(2**depth):
            fixeddata={i:(h>>i)&1 for i in range(depth)}; q=qdata(labels,fixeddata)
            f=[]
            for z in range(2**len(ctrls)):
                for x in range(2**nc):
                    xx=h+sum(((x>>j)&1)<<i for j,i in enumerate(labels))
                    base=(-1 if (xx&7)==0 else 1)*(-1 if ((xx>>3)&7)==0 else 1)
                    f.append(base*(a[z] if xx==vertex else 1))
            f=tuple(f); P=law(f); T=[r*v for r in R for v in q]
            Cs.append(cross(P,T)); Hs.append(ent(P)); infl+=sum(physical(f,i) for i in range(nc))/2**depth
            rows.append((f,T))
        C,H=mean(Cs),mean(Hs); D=add(C,scale(H,-1)); bank=add(c(4*infl-U),L,scale(C,-1))
        out={'R':R,'L':L,'C':C,'H':H,'D':D,'B':bank,'I':infl,'a':a,'rows':rows,'ctrls':ctrls}
        state_cache[key]=out; return out
    def walk(fixedctrl):
        p=state(fixedctrl); free=p['ctrls']
        stop=not free or (policy=='adaptive' and 1 in fixedctrl and fixedctrl[1]==0) or (policy.startswith('one') and bool(fixedctrl))
        if stop: return p['B'],p['L'],p['H'],p['D'],{}
        i=int(policy[-1]) if policy.startswith('one') else (free[0] if policy=='complete' else (1 if 1 in free else free[-1]))
        cs=[state(dict(fixedctrl,**{} )|{i:b}) for b in (0,1)]
        child_bank=mean([r['B'] for r in cs]); gamma=add(child_bank,scale(p['B'],-1))
        sm=F(sum(p['a']),len(p['a'])); sg=[F(sum(r['a']),len(r['a'])) for r in cs]
        ck(same(gamma,add(overhead(sm,delta),scale(mean([overhead(s,delta) for s in sg]),-1))),'independent all-tree exact bank gap')
        ge(gamma,'actual common-controller tree earns reserve')
        ck(p['I']==sum(r['I'] for r in cs)/2,'actual edge data influence retained')
        for row,(f,T) in enumerate(p['rows']):
            idx=nc+free.index(i); amp=amplitudes(f); P=law(f)
            pairs=[(s,s|(1<<idx)) for s in range(len(f)) if not s&(1<<idx)]
            ps=[P[s]+P[t] for s,t in pairs]; rs=[T[s]+T[t] for s,t in pairs]
            er=add(divg(P,T),scale(divg(ps,rs),-1)); ge(er,'independent actual erasure')
            rhos=[]; ds=[]; dt=[]; ka=[]
            for b in (0,1):
                jnt=[]
                for s,t in pairs:
                    den=amp[s]*amp[s]+amp[t]*amp[t]
                    prob=(amp[s]+(-1)**b*amp[t])**2/(2*den) if den else F(1,2)
                    jnt.append((T[s]+T[t])*prob)
                rho=sum(jnt); ck(rho>0,'independent positive branch normalizer'); rhos.append(rho)
                pp=law(cut(f,idx,b)); target=cs[b]['rows'][row][1]
                ds.append(divg(pp,[v/rho for v in jnt])); dt.append(divg(pp,target)); ka.append(add(dt[-1],scale(ds[-1],-1)))
            ou=divg([F(1,2)]*2,rhos); ge(ou,'independent outcome refund')
            ck(same(divg(P,T),add(er,ou,mean(ds))),'independent BOTH inherited KL chain')
            ck(same(add(mean(ka),scale(er,-1),scale(ou,-1)),add(mean(dt),scale(divg(P,T),-1))),'actual signed target conversion retained')
            if RECEIPTS is not None:
                ser=lambda e:{str(k):str(v) for k,v in reduce_logs(e).items()}
                RECEIPTS.append({'control_index':i,'data_row':row,'actual_rho':list(map(str,rhos)),
                                 'raw_kappa':ser(mean(ka)),'erasure_E':ser(er),'outcome_O':ser(ou),
                                 'net_sigma':ser(add(mean(dt),scale(divg(P,T),-1))),
                                 'raw_kappa_bounds':list(map(str,bounds(mean(ka))))})
        children=[walk(fixedctrl|{i:b}) for b in (0,1)]
        BL,LL,HL,DL,EE=[mean([r[j] for r in children]) for j in range(5)]
        dL=add(p['L'],scale(mean([r['L'] for r in cs]),-1)); dH=add(p['H'],scale(mean([r['H'] for r in cs]),-1))
        return BL,LL,HL,DL,add(EE,dL,scale(dH,-1))
    root=state({}); BL,LL,HL,DL,E=walk({})
    ge(add(root['B'],c(-F(26,576))),'original paid reserve independently reconstructed')
    ge(add(BL,scale(root['B'],-1)),'all adaptive leaves from SAME source')
    ck(same(add(BL,DL,E),add(root['B'],root['D'])),'all terminal debts plus entire signed history')
    if policy=='complete': ck(not reduce_logs(LL),'full original controller entropy has been spent, not erased')
    return len(state_cache)
def main():
    start=time.perf_counter(); cases=nodes=0
    ctrls=[(0,)*8,(1,0,0,0,0,0,0,0),tuple(int(z.bit_count()>=2) for z in range(8)),(0,1,0,0,1,1,0,1)]
    for v in (0,63):
        for A in ctrls:
            for d in (1,2,5):
                for policy in ('complete','adaptive'):
                    nodes+=fixture(v,A,d,policy); cases+=1
                    if time.perf_counter()-start>120: raise RuntimeError('frozen cap')
    result={'status':'PASS','cases':cases,'controller_states':nodes,'assertions':count,'seconds':time.perf_counter()-start,'production_imports':False}
    (ROOT/'out/REPLAY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps(result))
if __name__=='__main__': scalar() if sys.argv[-1]=='scalar' else main()
