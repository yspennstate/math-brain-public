from pathlib import Path
import hashlib
helper=Path(__file__).resolve().parents[2]/'20261014T054454Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py'
source=helper.read_text(encoding='utf-8')
exec(compile(source.split("rows=[];candidates=0;sets=0;wins=")[0],str(helper),'exec'))

# Independent recursive matching generator, replacing edge-subset enumeration.
def matchings(edges,A):
    neighbors={v:{w for e in edges if v in e for w in e if w!=v} for v in range(A.bit_length())}
    vertices={v for v in neighbors if A>>v&1}
    def rec(todo,M,U):
        if not todo:
            if all(not(neighbors[u]&U) for u in U):yield M
            return
        u=min(todo);rest=todo-{u}
        yield from rec(rest,M,U|{u})
        for v in sorted(rest&neighbors[u]):yield from rec(rest-{v},M+[(u,v)],U)
    return list(rec(vertices,[],set()))

def spectrum(values):
    w=walsh(values);return [F(x*x,len(values)**2) for x in w]

def restriction(values,i,b):
    return [values[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(values)//2)]

def terminal_costs(values,q,parent):
    n=(len(values)-1).bit_length();out=[]
    for i in range(n):
        child=[]
        def lift(T):return (T&((1<<i)-1))|((T>>i)<<(i+1))
        qi=q[1<<i];qb=[F(0)]+[(q[lift(T)]+q[lift(T)|(1<<i)])/(1-qi) for T in range(1,1<<(n-1))]
        ck(sum(qb)==1)
        for b in (0,1):
            p=spectrum(restriction(values,i,b));v=1-p[0]
            Q=[1-v]+[v*x for x in qb[1:]];ck(sum(Q)==1)
            child.append(CE(p,Q))
        avg=((child[0][0]+child[1][0])/2,(child[0][1]+child[1][1])/2)
        # Cross entropy is separated by a substantial positive gap in these graph cases.
        ck(parent[0]>=avg[1])
        out.append({'coordinate':i,'average_full_child_CE':outward(avg),'root_minus_children':outward((parent[0]-avg[1],parent[1]-avg[0]))})
    return out

candidates=[]
if args.pilot:
    n=4;universe=list(itertools.combinations(range(n),2))
    candidates=[(n,[e for j,e in enumerate(universe) if mask>>j&1]) for mask in range(64)]
else:
    n=5;universe=list(itertools.combinations(range(n),2))
    candidates=[(n,[e for j,e in enumerate(universe) if mask>>j&1]) for mask in range(1024)]
    n=6;universe=list(itertools.combinations(range(n),2));path=[(i,i+1) for i in range(5)]
    for mask in range(32):
        missing={e for j,e in enumerate(path) if mask>>j&1}
        candidates.append((n,[e for e in universe if e not in missing]))
    n=8;universe=list(itertools.combinations(range(n),2));perfect=[(0,1),(2,3),(4,5),(6,7)]
    for t in (1,2,4):candidates.append((n,[e for e in universe if e not in perfect[:t]]))

rows=[];sets=0;theorems=0;queries=0;skipped=0
for index,(n,edges) in enumerate(candidates):
    degrees=[sum(v in e for e in edges) for v in range(n)];delta=min(degrees);d=n-1-delta
    if not delta:skipped+=1;continue
    lam=F(1,n-1);a=lam/48;b=delta*lam/48;em=[sum(1<<v for v in e) for e in edges]
    C=[int(not any(x&e==e for e in em)) for x in range(1<<n)]
    values=[1-2*c for c in C];p=spectrum(values);s=F(sum(C),1<<n);v=1-p[0]
    I=sum((x.bit_count()*mass for x,mass in enumerate(p)),F(0));ck(sum(p)==1);ck(v==4*s*(1-s))
    mu=F(sum(x.bit_count()*c for x,c in enumerate(C)),sum(C));ck(I==2*s*(n-2*mu));ck(mu<=d+1)
    masses=[F(0)]
    for A in range(1,1<<n):
        k=A.bit_count();Ms=matchings(edges,A);r0=max(0,(k-2*d-1)//2)
        ck(len(Ms)>=math.factorial(r0));ck(all(r0<=len(M)<=r0+d+1 for M in Ms))
        mass=occupation(n,edges,A,lam,F(1));lower=math.factorial(r0)*a**(r0+d+1)*b**(2*d+2)
        ck(mass>=lower>0);masses.append(mass);sets+=1
    Z=sum(masses)
    # Analytic proof gives log2 Z <= n/4. A stronger rational test where available.
    ck(Z**4<=2**n)
    ck(Z<=(1+n*lam/32)**n*(1+lam/12)**len(edges))
    q=[F(0)]+[z/Z for z in masses[1:]];ck(sum(q)==1)
    row={'n':n,'edges':edges,'complement_max_degree':d,'s':str(s),'v':str(v),'I':str(I),'Z_F':str(Z),'density_hypothesis':n>=4*(d+1)}
    if n>=4*(d+1):
        theorems+=1;ck(s<=F(1,2));ck(I>=s*n);ck(v/I<=F(4,n))
        root=[1-v]+[v*z for z in q[1:]];cost=CE(p,root);ln=lg(n)
        kappa=(F((d+1))*v/I*(ln[0]+20),F((d+1))*v/I*(ln[1]+20))
        ck(cost[1]<=(24+kappa[0])*I)
        terms=terminal_costs(values,q,cost);queries+=n
        row.update(complete_CE_over_I=outward((cost[0]/I,cost[1]/I)),kappa=outward(kappa),full_projected_children=terms)
        # All original normalized masses; D cancels exactly, not heuristically.
        D=(1+lam/4)**len(edges)-1;raw=[z/D for z in masses[1:]]
        ck(all(x/sum(raw)==q[j+1] for j,x in enumerate(raw)))
        row['complete_original_q']=[str(x) for x in q[1:]]
    rows.append(row)
    if len(rows)%40==0:
        (R/'out/checkpoint.json').write_text(json.dumps({'graphs':len(rows),'assertions':assertions,'elapsed_seconds':time.monotonic()-start})+'\n',encoding='utf-8',newline='\n')

# Check BOTH inequalities for J beyond the family dimensions, including unbalanced exponents.
for aa in range(33):
    for bb in range(33):
        J=F(math.factorial(aa)*math.factorial(bb),(aa+bb+1)**2*(aa+bb+2))
        ck(F(1,2*6**(aa+bb))<=J<=math.factorial(aa)*math.factorial(bb))

out={'helper_version':'A014-dense-defect-v1','source_helper_sha256':hashlib.sha256(source.encode('utf-8')).hexdigest(),'mode':'pilot' if args.pilot else 'full','candidates':len(candidates),'selected_graphs':len(rows),'isolated_vertex_skips':skipped,'sets':sets,'theorem_graphs':theorems,'full_child_queries':queries,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'rows':rows}
(R/('out/pilot.json' if args.pilot else 'out/check.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
