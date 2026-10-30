from pathlib import Path
from fractions import Fraction as F
from math import comb, prod
from itertools import combinations, product
import json, sys, time, hashlib, importlib.util
sys.dont_write_bytecode = True
B = Path(__file__).resolve().parents[1]
O = B / 'out'
pilot = '--pilot' in sys.argv
start = time.monotonic()
checks = 0

def ck(x):
    global checks
    checks += 1
    assert x, checks
    if checks % 4096 == 0:
        assert time.monotonic()-start < (55 if pilot else 180)

def save(name, data):
    (O/name).write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8', newline='\n')

def spectrum(v):
    a = v[:]
    h = 1
    while h < len(a):
        for k in range(0, len(a), 2*h):
            for j in range(k,k+h):
                a[j],a[j+h] = a[j]+a[j+h],a[j]-a[j+h]
        h *= 2
    return a

def physical(v,n):
    return F(sum(v[x] != v[x^(1<<j)] for x in range(len(v)) for j in range(n)),len(v))

def family(w):
    r = 2**w; b = r*w; n = 2*b; N = 1<<n
    clauses = [((1<<w)-1)<<(w*c) for c in range(r)]
    U = [int(all(x&c for c in clauses)) for x in range(1<<b)]
    V = [int(any((y&c)==c for c in clauses)) for y in range(1<<b)]
    v = [2*U[x&((1<<b)-1)]*V[x>>b]-1 for x in range(N)]
    fw = spectrum(v); I = physical(v,n)
    eps = F(1,r); p=1-eps
    ck(sum(z*z for z in fw)==N*N)
    ck(sum(a.bit_count()*z*z for a,z in enumerate(fw))==I*N*N)
    ck(I==2*w*p**(r-1))
    # Recover COMPLETE monotone prime tables from actual truth, rather than candidates.
    pos=[]; neg=[]; full=N-1
    for x,val in enumerate(v):
        if val==1 and all(v[x^(1<<j)]==-1 for j in range(n) if x>>j&1):
            pos.append(x)
        if val==-1 and all(v[x^(1<<j)]==1 for j in range(n) if not x>>j&1):
            neg.append(full^x)
    wantpos=[]
    for choices in product(range(w),repeat=r):
        trans=sum(1<<(w*c+j) for c,j in enumerate(choices))
        for D in range(r): wantpos.append(trans|(clauses[D]<<b))
    wantneg=clauses+[sum(1<<(b+w*c+j) for c,j in enumerate(choices)) for choices in product(range(w),repeat=r)]
    ck(set(pos)==set(wantpos)); ck(set(neg)==set(wantneg))
    targets=0; transitions=0
    for C in range(r):
        for D in range(r):
            sup=clauses[C]|(clauses[D]<<b)
            for sx in range(1,1<<w):
                for sy in range(1,1<<w):
                    a=(sx<<(w*C))|(sy<<(b+w*D))
                    ck(F(fw[a]**2,N*N)==4*eps**4*p**(4*(r-1)))
                    targets+=1
            for g in pos:
                for h in pos:
                    xg=g&clauses[C]; xh=h&clauses[C]
                    attachments=g&h&sup
                    if xg!=xh and attachments:
                        ck((attachments&clauses[C])==0)
                        ck((h&(clauses[D]<<b))==(clauses[D]<<b))
                    transitions+=1
            # The target's induced negative-table coordinate components are one X
            # component and w separate Y components.
            vertices=[j for j in range(n) if sup>>j&1]
            adj={j:{k for k in vertices if any(g>>j&1 and g>>k&1 for g in neg)} for j in vertices}
            seen=set(); comps=[]
            for j in vertices:
                if j in seen: continue
                todo=[j]; found={j}
                while todo:
                    k=todo.pop()
                    for t in adj[k]-found: found.add(t); todo.append(t)
                seen|=found; comps.append(found)
            ck(sorted(map(len,comps))==[1]*w+[w])
    return {'w':w,'r':r,'inputs':N,'positive_primes':len(pos),'negative_primes':len(neg),'joint_targets':targets,'gate_pair_clause_tests':transitions,'I':str(I)}

rows=[family(w) for w in ([1] if pilot else [1,2])]
save('BOOLEAN_CHECKPOINT.json',rows)

# A different exact certificate for the source's generating-function step.
s=F(17,20)
phi_upper=sum((s**c/F((c+1)*(c+2)) for c in range(25)),F(0))+s**25/26
ck(phi_upper<F(79,100)<F(4,5))
ck(F(4,5)*(1+F(1,16))==s)
ck(F(4,5)/(1-F(1,20))==F(16,19))
# Exhaust tiny rational root-activity vectors and z to test the full D ratio.
rootcases=0
for size in range(1,4):
    for xs in product([F(1,4096),F(1,1024),F(1,512)],repeat=size):
        A=sum(xs,F(0)); D=prod(1+x for x in xs)-1
        for z in [F(1),F(2),F(4)]:
            if z*A>F(1,16): continue
            value=(prod(1+F(4,5)*z*x for x in xs)-1)/(z*D)
            ck(value<=F(16,19)); rootcases+=1
save('MOMENT_CHECKPOINT.json',{'phi_upper':str(phi_upper),'rational_root_vectors':rootcases})

# Independently reconstruct connector spectra, signs, physical boundary and all-root mass.
connect=[]
for m in ([2] if pilot else [2,3,4]):
    n=4*m; N=1<<n; t=F(1,2**m); lam=F(1,2*m)
    E=tuple((i,m+j) for i in range(m) for j in range(m))+tuple((2*m+i,3*m+j) for i in range(m) for j in range(m))
    xy=(0,3*m)
    f=[1 if any((x>>a&1) and (x>>b&1) for a,b in E) else -1 for x in range(N)]
    g=[1 if f[x]==1 or (x>>xy[0]&1 and x>>xy[1]&1) else -1 for x in range(N)]
    delta=[g[x]-f[x] for x in range(N)]
    W=(1<<0)|(((1<<m)-1)<<m)|(((1<<m)-1)<<(2*m))|(1<<(3*m))
    ones=(1<<0)|(1<<(3*m)); zeroes=W^ones
    ck(all(delta[x]==2*int((x&ones)==ones and (x&zeroes)==0) for x in range(N)))
    dw=spectrum(delta); sq=F(0); energy=F(0)
    for a,c in enumerate(dw):
        ck(abs(c)==(2*N//2**(2*m+2) if a&~W==0 else 0))
        sq+=F(c*c,N*N); energy+=F(a.bit_count()*c*c,N*N)
    ck(sq==t*t); ck(energy==(m+1)*t*t)
    I0=physical(f,n); I1=physical(g,n)
    ck(I0==8*m*t*t*(1-t)*(2-t))
    ck(I1==I0-(m-1)*t*t)
    ck(I1>=F(19,2)*m*t*t and I0/I1<=F(21,19))
    D0=(1+lam/4)**(2*m*m)-1; D1=(1+lam/4)**(2*m*m+1)-1
    ck(D0>=F(m,4)); ck(D1/D0<=F(19,16))
    count=0
    for k in range(1,m+1):
        # Explicit independent labels for the remaining singleton-owned gates.
        mass=F(0)
        for choices in product(range(m),repeat=k-1):
            mass+=(lam/48)*(lam/32)**(k-1); count+=1
        ck(mass==F(2,3*m)*F(1,64)**k)
    ck(3*m<=2**(m+1))
    ck(F(1491,76)+F(91,38)+F(9,32)==F(13555,608)<23)
    connect.append({'m':m,'I0':str(I0),'I1':str(I1),'cylinder_energy':str(energy),'fixed_first_double_root_choices':count})
    save('CONNECTOR_CHECKPOINT.json',connect)

insertion=0
if not pilot:
    path=B.parent/'20261021T161852Z-fleet03-A010-universal-residual-falsifier/code/check.py'
    sp=importlib.util.spec_from_file_location('own_parent_map',path); mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
    E=((0,2),(0,3),(1,2),(1,3),(4,6),(4,7),(5,6),(5,7)); Ep=E+((0,6),)
    for k in [1,2,3]:
        for vs in combinations(range(8),k):
            A=sum(1<<v for v in vs); a,_=mod.full(A,E,8); b,_=mod.full(A,Ep,8)
            ck(all(b.get(T,F(0))==c for T,c in a.items()))
            ck(all(T in a for T in b if T<256))
            lam=F(1,4)
            ck(sum(c*lam**T.bit_count() for T,c in b.items())>=sum(c*lam**T.bit_count() for T,c in a.items()))
            insertion+=1

# New representation-budget bound: these are exact scalar checks of a proved
# induction, not truth tables at these dimensions or an exhaustive weight search.
tradeoff=[]
for w in range(64,81 if pilot else 257):
    ck((48*w)**4<=2**w)
    ck(2**w-1>=F(w*w,8))
    ck((w//2)-1>=F(w,4))
    for L in [1,2,2**(w//4)]:
        # Avoid irrational 2^(w/2) by squaring both sides.
        ck((48*L*w)**2<=2**w)
        tradeoff.append([w,L])
    # Exact monotonicity proving the all-w fourth-power induction.
    ck(2*w**4>(w+1)**4)

out={'status':'PASS','helper':'A010-multireference-review-v1','pilot':pilot,'assertions':checks,'seconds':time.monotonic()-start,'families':rows,'moment_root_cases':rootcases,'connector':connect,'exact_insertion_outputs':insertion,'budget_scalar_pairs':len(tradeoff),'phi_upper':str(phi_upper),'new_theorem_scope':'w>=64; at most floor(2^(w/4)) positive original-prime queues; any fixed negative-prime mixture; all feasible weights/orders/posteriors'}
save('PILOT.json' if pilot else 'CHECK.json',out)
print(json.dumps(out))
