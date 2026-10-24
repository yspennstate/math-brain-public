from fractions import Fraction as Q
from pathlib import Path
import itertools, json, time, hashlib
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def ck(x):
    global checks
    checks+=1
    assert x, checks
def prod(xs):
    z=Q(1)
    for x in xs: z*=x
    return z
def spectrum(table, ps):
    n=len(ps); means=[2*p-1 for p in ps]; vs=[4*p*(1-p) for p in ps]
    cs={}; masses={}
    for s in range(1<<n):
        v=prod(vs[i] for i in range(n) if s>>i&1)
        if not v: continue
        a=Q(0)
        for x in range(1<<n):
            weight=prod(ps[i] if x>>i&1 else 1-ps[i] for i in range(n))
            a+=weight*table[x]*prod((1 if x>>i&1 else -1)-means[i] for i in range(n) if s>>i&1)
        cs[s]=a/v; masses[s]=a*a/v
    ck(sum(masses.values())==1)
    return cs,masses,vs
def logform(x):
    # Exact expansion ln(rational) in prime logs.
    out={}
    for integer,sign in [(x.numerator,1),(x.denominator,-1)]:
        d=2
        while d*d<=integer:
            while integer%d==0:
                out[d]=out.get(d,Q(0))+sign; integer//=d
            d+=1
        if integer>1: out[integer]=out.get(integer,Q(0))+sign
    return {p:a for p,a in out.items() if a}
def add(a,b,scale=Q(1)):
    z=dict(a)
    for p,c in b.items(): z[p]=z.get(p,Q(0))+scale*c
    return {p:c for p,c in z.items() if c}
def entropy(masses):
    z={}
    for a in masses:
        if a: z=add(z,logform(a),-a)
    return z
def stats(sp):
    cs,ms,vs=sp; hp={}; influence=Q(0); variance=Q(0)
    for s,a in ms.items():
        if not s: continue
        influence+=s.bit_count()*a; variance+=a
        if a: hp=add(hp,logform(prod(vs[i] for i in range(len(vs)) if s>>i&1)/a),a)
    return hp,influence,variance
def tab(n,fn): return [fn([(x>>i)&1 for i in range(n)]) for x in range(1<<n)]

# Exact A042 (3)-(4), all table/coordinate fixtures, including endpoints.
endpoint_cases=0
for n in [1,2]:
    for t in range(1<<(1<<n)):
        f=[1 if t>>x&1 else -1 for x in range(1<<n)]
        for i in range(n):
            others=[j for j in range(n) if j!=i]; ps=[Q(1,3)]*(n-1)
            children=[]
            for b in [0,1]:
                children.append([f[sum(((y>>k)&1)<<j for k,j in enumerate(others))+(b<<i)] for y in range(1<<(n-1))])
            sg,sh=[spectrum(ch,ps) for ch in children]
            cg,pg,vs=sg; ch,ph,_=sh
            D0=stats(sg)[1]-stats(sg)[2]
            L=Q(0); Qsum=Q(0)
            for s in cg:
                v=prod(vs[k] for k in range(n-1) if s>>k&1)
                d=ch[s]-cg[s]
                L+=2*(s.bit_count()-1)*v*cg[s]*d if s else 0
                L+=s.bit_count()*v*d*d
                if s: Qsum+=v*d*d
            for p in [Q(0),Q(1,8),Q(1,2),Q(7,8),Q(1)]:
                fullps=[Q(1,3)]*n; fullps[i]=p
                sf=spectrum(f,fullps); cf,pf,vf=sf
                for s in cg:
                    physical=sum(((s>>k)&1)<<j for k,j in enumerate(others))
                    v=prod(vs[k] for k in range(n-1) if s>>k&1)
                    ck(pf[physical]==v*((1-p)*cg[s]+p*ch[s])**2)
                    ck(cf[physical]==(1-p)*cg[s]+p*ch[s])
                    if p not in [0,1]:
                        ck(pf[physical|(1<<i)]==p*(1-p)*v*(ch[s]-cg[s])**2)
                        ck(cf[physical|(1<<i)]==(ch[s]-cg[s])/2)
                _,I,V=stats(sf); ck(I-V==D0+p*L-p*p*Qsum)
                endpoint_cases+=1

# Independent physical/spectral joint laws, with exact entropy identity.
fiber_cases=0
for n in [0,1]:
    tables=[[1 if t>>x&1 else -1 for x in range(1<<n)] for t in range(1<<(1<<n))]
    for g,h in itertools.product(tables,repeat=2):
        cg,pg,vs=spectrum(g,[Q(1,3)]*n); ch,ph,_=spectrum(h,[Q(1,3)]*n)
        for p in [Q(1,8),Q(1,2),Q(7,8)]:
            parent=tab(n+1,lambda x:g[sum(x[k+1]<<k for k in range(n))] if not x[0] else h[sum(x[k+1]<<k for k in range(n))])
            _,pf,_=spectrum(parent,[p]+[Q(1,3)]*n)
            q={s:(1-p)*pg[s]+p*ph[s] for s in pg}
            joint=[]
            for s in pg:
                ck(pf[s<<1]+pf[(s<<1)|1]==q[s])
                joint.extend([(1-p)*pg[s],p*ph[s]])
            M=add(entropy(pf.values()),entropy(q.values()),-1)
            J=add(add(entropy(q.values()),entropy(pg.values()),-(1-p)),entropy(ph.values()),-p)
            L=add(add(entropy(pf.values()),entropy(pg.values()),-(1-p)),entropy(ph.values()),-p)
            ck(L==add(M,J))
            ck(add(entropy(joint),entropy(q.values()),-1)==add(entropy([p,1-p]),J,-1))
            fiber_cases+=1

# Three small actual Boolean compositions, all induced child biases unequal.
gates={
    'majority':lambda y:1 if sum(y)>=2 else -1,
    'xor-and':lambda y:1 if y[0]^(y[1]&y[2]) else -1,
    'or':lambda y:1 if any(y) else -1
}
childdefs={'and':(2,lambda x:1 if all(x) else -1),'or':(2,lambda x:1 if any(x) else -1),'literal':(1,lambda x:2*x[0]-1),'xor':(2,lambda x:1 if x[0]^x[1] else -1)}
fixtures=[('majority',['and','literal','literal']),('xor-and',['or','and','literal']),('or',['and','xor'])]
compositions=[]
for name,names in fixtures:
    sizes=[childdefs[c][0] for c in names]; offsets=[sum(sizes[:i]) for i in range(len(sizes))]; n=sum(sizes)
    biases=[Q(1,3),Q(2,5),Q(1,4),Q(3,7),Q(2,3)][:n]
    childsp=[]; eta=[]
    for i,c in enumerate(names):
        sz,fn=childdefs[c]; sp=spectrum(tab(sz,fn),biases[offsets[i]:offsets[i]+sz]); childsp.append(sp); eta.append((1+sp[0][0])/2)
    ck(len(set(eta))==len(eta)); outer=spectrum(tab(len(names),gates[name]),eta)
    full=tab(n,lambda x:gates[name]([int(childdefs[c][1](x[offsets[i]:offsets[i]+sizes[i]])==1) for i,c in enumerate(names)]))
    actual=spectrum(full,biases); pred={}
    for s in range(1<<n):
        masks=[(s>>offsets[i])&((1<<sizes[i])-1) for i in range(len(names))]
        A=sum((1<<i) for i,m in enumerate(masks) if m)
        coefficient=outer[0][A]*prod(childsp[i][0][m] for i,m in enumerate(masks) if m)
        ck(actual[0][s]==coefficient)
        pred[s]=outer[1][A]*prod(childsp[i][1][m]/outer[2][i] for i,m in enumerate(masks) if m)
        ck(actual[1][s]==pred[s])
    Ho,Io,Vo=stats(outer); Hf,If,Vf=stats(actual); Hpred=Ho; Ipred=Q(0); Dpred=Io-Vo
    alphas=[]
    for i,sp in enumerate(childsp):
        alpha=sum(a for s,a in outer[1].items() if s>>i&1)/outer[2][i]; alphas.append(alpha)
        H,I,V=stats(sp); Hpred=add(Hpred,H,alpha); Ipred+=alpha*I; Dpred+=alpha*(I-V)
    ck(Hf==Hpred); ck(If==Ipred); ck(Vf==Vo); ck(If-Vf==Dpred)
    compositions.append({'gate':name,'children':names,'biases':[str(p) for p in biases],'induced_biases':[str(p) for p in eta],'alphas':[str(a) for a in alphas],'all_identities':'PASS','I':str(If),'Var':str(Vf)})

# Repeated-variable and physical/spectral-conditioning certificates.
_,dup,_=spectrum([1,1],[Q(1,3)]) # XOR sign repeated variable is constant +1.
ind=spectrum(tab(2,lambda x:1 if x[0]==x[1] else -1),[Q(1,3)]*2)[1]
ck(dup=={0:Q(1),1:Q(0)}); ck(ind[0]==Q(1,81)); ck(ind[3]==Q(64,81))
andtab=tab(2,lambda x:1 if all(x) else -1)
_,andlaw,_=spectrum(andtab,[Q(1,2)]*2)
ck(all(a==Q(1,4) for a in andlaw.values()))
# Spectral conditioning S lacks bit0: masses 1/2,1/2 on residual bit; physical x0=0 is constant.
physical=spectrum([-1,-1],[Q(1,2)])[1]; spectral=[andlaw[0]/(andlaw[0]+andlaw[2]),andlaw[2]/(andlaw[0]+andlaw[2])]
ck(physical[0]==1 and spectral==[Q(1,2),Q(1,2)])
out={'helper_version':'A045-independent-rational-v1','assertions':checks,'endpoint_fixtures':endpoint_cases,'fiber_fixtures':fiber_cases,'compositions':compositions,'guards':{'reused_XOR_independent_empty_mass':'1/81','reused_XOR_actual_empty_mass':'1','physical_AND_child_mass':['1','0'],'spectrally_conditioned_AND_mass':['1/2','1/2']},'runtime_seconds':time.perf_counter()-start,'status':'PASS'}
(ROOT/'out'/'CHECK_OUTPUT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
