"""Small independent experiments for w341's ten assigned research problems.

Only files below this script's directory are written. Exact certificates use
fractions.Fraction; scipy output is explicitly numerical evidence, not a proof.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import random
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'measurements'
OUT.mkdir(exist_ok=True)
ORDER = ['P0288','C0034','C0151','P0127','P0456','C0058','C0082','C0126','P0014','P0042']

def save(name, value):
    (OUT/(name+'.json')).write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding='utf-8')

def solve(a, b):
    rows = [[F(x) for x in row]+[F(y)] for row,y in zip(a,b)]
    n = len(rows)
    for k in range(n):
        pivot = next(i for i in range(k,n) if rows[i][k])
        rows[k],rows[pivot] = rows[pivot],rows[k]
        z = rows[k][k]
        rows[k] = [x/z for x in rows[k]]
        for i in range(n):
            if i != k and rows[i][k]:
                z = rows[i][k]
                rows[i] = [x-z*y for x,y in zip(rows[i],rows[k])]
    return [row[-1] for row in rows]

def rank(a):
    rows = [[F(x) for x in row] for row in a]
    r = 0
    for k in range(len(rows[0])):
        inds = [i for i in range(r,len(rows)) if rows[i][k]]
        if not inds:
            continue
        i = inds[0]
        rows[r],rows[i] = rows[i],rows[r]
        z = rows[r][k]
        rows[r] = [x/z for x in rows[r]]
        for j in range(r+1,len(rows)):
            z = rows[j][k]
            if z:
                rows[j] = [x-z*y for x,y in zip(rows[j],rows[r])]
        r += 1
    return r

def check_P0288():
    cases = 0
    minors = []
    for v in [F(1,2),F(1),F(2),F(3)]:
        def lead(i,j):
            return F(max(i*j,0))+F(abs(i)+abs(j))/v+2/(v*v)
        mat = [[lead(i,j) for j in range(-4,5)] for i in range(-4,5)]
        assert rank(mat) == 2
        minor = lead(0,0)*lead(1,1)-lead(0,1)**2
        assert minor == 1/(v*v)
        minors.append({'v':str(v),'scaled_minor':str(minor),'rank':2})
        for sign in [1,-1]:
            def h(i):
                return F(max(sign*i,0))+1/v
            for i in range(-4,5):
                assert h(i+1)+h(i-1)-2*h(i)-(v*h(i) if i == 0 else 0) == 0
        for r in [F(1,2),F(1,3),F(2,3),F(3,4)]:
            s = r+1/r-2
            d = 1/r-r
            def res(i,j):
                return r**abs(i-j)/d-v*r**(abs(i)+abs(j))/(d*(d+v))
            for i,j in product(range(-3,4), repeat=2):
                val = (s+2+(v if i == 0 else 0))*res(i,j)-res(i-1,j)-res(i+1,j)
                assert val == int(i == j)
                cases += 1
    result = {'label':'exact checks','resolvent_recurrences':cases,'minor_cases':minors,'harmonic_identities':72}
    save('P0288_exact',result)
    try:
        from scipy.integrate import quad
    except ImportError:
        result['numerical']='scipy unavailable; not run'
        return result
    numeric = []
    for t in [20,80,320]:
        errors=[]
        for i,j in [(0,0),(0,1),(1,1),(1,-1)]:
            a,b=abs(i-j),abs(i)+abs(j)
            def integrand(x):
                th=x/math.sqrt(t)
                sn=math.sin(th)
                cb=math.cos(b*th)
                diff=-2*math.sin((a+b)*th/2)*math.sin((a-b)*th/2)
                bracket=diff+(4*sn*sn*cb+4*sn*math.sin(b*th))/(4+4*sn*sn)
                return math.exp(-4*t*math.sin(th/2)**2)*t*bracket/math.pi
            val,err=quad(integrand,0,min(12,math.pi*math.sqrt(t)),epsabs=1e-11)
            # The positive delta potential also has one high-energy atom.
            r=(math.sqrt(8)-2)/2
            atom=(1-r*r)/(1+r*r)*(-r)**(abs(i)+abs(j))*math.exp(-(2+math.sqrt(8))*t)
            val += t**1.5*atom
            predicted=(max(i*j,0)+(abs(i)+abs(j))/2+F(1,2))/(2*math.sqrt(math.pi))
            errors.append(abs(val-predicted))
            numeric.append({'t':t,'i':i,'j':j,'scaled_kernel':val,'limit':float(predicted),'absolute_error':abs(val-predicted),'quadrature_error_estimate':err})
        result.setdefault('max_error_by_t',{})[str(t)]=max(errors)
    assert result['max_error_by_t']['320'] < result['max_error_by_t']['20']
    save('P0288_spectral_integral',{'label':'numerical evidence','rows':numeric})
    return result

def maxflow_coupling(u,v):
    n=len(u)
    a=[x*x for x in u]
    q={(i,j):(u[i]*v[j]-u[j]*v[i])**2 for i,j in combinations(range(n),2)}
    cap={}
    adj={}
    def edge(x,y,c):
        cap[x,y]=F(c)
        cap[y,x]=F(0)
        adj.setdefault(x,[]).append(y)
        adj.setdefault(y,[]).append(x)
    for (i,j),mass in q.items():
        node=('pair',i,j)
        edge('s',node,mass)
        edge(node,('vertex',i),1)
        edge(node,('vertex',j),1)
    for i in range(n):
        edge(('vertex',i),'t',a[i])
    total=F(0)
    while True:
        parent={'s':None}
        todo=deque(['s'])
        while todo and 't' not in parent:
            x=todo.popleft()
            for y in adj[x]:
                if y not in parent and cap[x,y]>0:
                    parent[y]=x
                    todo.append(y)
        if 't' not in parent:
            break
        path=[]
        x='t'
        while x != 's':
            y=parent[x]
            path.append((y,x))
            x=y
        delta=min(cap[e] for e in path)
        for x,y in path:
            cap[x,y]-=delta
            cap[y,x]+=delta
        total+=delta
    assert total==1
    data=[]
    for (i,j),mass in q.items():
        node=('pair',i,j)
        data.append([i,j,str(mass),str(1-cap[node,('vertex',i)]),str(1-cap[node,('vertex',j)])])
    return data

def verify_coupling(cert):
    u=list(map(F,cert['u']))
    v=list(map(F,cert['v']))
    n=len(u)
    assert sum(x*x for x in u)==sum(x*x for x in v)==1
    assert sum(x*y for x,y in zip(u,v))==0
    a,b=[F(0)]*n,[F(0)]*n
    mass=F(0)
    for i,j,raw,xraw,yraw in cert['edges']:
        q,x,y=F(raw),F(xraw),F(yraw)
        # Independently recompute the 2x2 projection determinant.
        kii=u[i]**2+v[i]**2
        kjj=u[j]**2+v[j]**2
        kij=u[i]*u[j]+v[i]*v[j]
        assert q==kii*kjj-kij*kij
        assert x>=0 and y>=0 and x+y==q
        a[i]+=x; a[j]+=y
        b[j]+=x; b[i]+=y
        mass+=q
    assert mass==1
    assert a==[x*x for x in u] and b==[x*x for x in v]

def check_C0034():
    path=OUT/'C0034_certificates.jsonl'
    count=cuts=0
    naive=None
    with path.open('w',encoding='utf-8') as f:
        configs=[(n,trial) for n in range(2,8) for trial in range(10)]+[(n,None) for n in range(2,6)]
        for n,trial in configs:
            mat=[[F(int(i==j)) for j in range(n)] for i in range(n)]
            if trial is not None:
                rng=random.Random(n*100+trial)
                for step in range(2*n):
                    i,j=rng.sample(range(n),2)
                    c,s=(F(3,5),F(4,5)) if step%2 else (F(5,13),F(12,13))
                    oldi,oldj=mat[i][:],mat[j][:]
                    mat[i]=[c*x-s*y for x,y in zip(oldi,oldj)]
                    mat[j]=[s*x+c*y for x,y in zip(oldi,oldj)]
            u=[row[0] for row in mat]; v=[row[1] for row in mat]
            q={(i,j):(u[i]*v[j]-u[j]*v[i])**2 for i,j in combinations(range(n),2)}
            for mask in range(1<<n):
                inds=[i for i in range(n) if mask>>i&1]
                ua=sum((u[i]**2 for i in inds),F(0))
                va=sum((v[i]**2 for i in inds),F(0))
                ca=sum((u[i]*v[i] for i in inds),F(0))
                internal=sum((q[i,j] for i,j in combinations(inds,2)),F(0))
                assert internal==ua*va-ca*ca and internal<=ua
                cuts+=1
            cert={'n':n,'trial':trial,'u':list(map(str,u)),'v':list(map(str,v)),'edges':maxflow_coupling(u,v)}
            verify_coupling(cert)
            f.write(json.dumps(cert)+'\n'); f.flush()
            count+=1
            if naive is None:
                first=[F(0)]*n; second=[F(0)]*n
                for (i,j),mass in q.items():
                    den=u[i]**2+u[j]**2
                    if not mass:
                        continue
                    assert den>0
                    x=mass*u[i]**2/den; y=mass*u[j]**2/den
                    first[i]+=x; first[j]+=y; second[j]+=x; second[i]+=y
                tv1=sum((abs(first[i]-u[i]**2) for i in range(n)),F(0))/2
                tv2=sum((abs(second[i]-v[i]**2) for i in range(n)),F(0))/2
                if tv1 or tv2:
                    naive={'label':'exact counterexample','n':n,'u':list(map(str,u)),'v':list(map(str,v)),'first_marginal_tv':str(tv1),'second_marginal_tv':str(tv2),'tv_decimal':float(tv2)}
    # Replay the on-disk certificates, separately from the flow generator.
    with path.open(encoding='utf-8') as f:
        replayed=0
        for line in f:
            verify_coupling(json.loads(line)); replayed+=1
    assert replayed==count==64 and naive is not None
    save('C0034_naive_counterexample',naive)
    return {'label':'exact certificates','before_exact_certificates':0,'after_exact_certificates':count,'cut_inequalities':cuts,'replayed_certificates':replayed,'naive_counterexample_tv':naive['tv_decimal']}

def check_C0151():
    rows=[]
    for d in range(2,6):
        orders=list(permutations(range(d+1)))
        keep=sum(int(order[0]==min(order)) for order in orders)
        density=F(keep,len(orders))
        assert density==F(1,d+1)
        rows.append({'d':d,'rank_orders':len(orders),'local_minimum_density':str(density),'half_thinned_density':str(density/2)})
    return {'label':'finite boundary checks; thinning proof is separate','rows':rows,'endpoint_attainment':'not inferred from downward closure','gap_conditional_bounds':['5/4','7/4']}

def dirs(d):
    return [tuple(sign if j==i else 0 for j in range(d)) for i in range(d) for sign in [-1,1]]

def plus(a,b):
    return tuple(x+y for x,y in zip(a,b))

def canon_edge(a,b):
    return tuple(sorted((a,b)))

def check_P0127():
    rows=[]
    for d in range(1,5):
        root=(0,)*d
        hist=Counter()
        for first in dirs(d):
            e1=canon_edge(root,first)
            vertices=[root,first]
            frontier=[canon_edge(v,plus(v,step)) for v in vertices for step in dirs(d) if plus(v,step) not in vertices]
            assert len(frontier)==2*(2*d-1)
            for e2 in frontier:
                hist[tuple(sorted((e1,e2)))]+=1
        histories=sum(hist.values()); trees=len(hist)
        tv=sum((abs(F(k,histories)-F(1,trees)) for k in hist.values()),F(0))/2
        assert tv==F(1,6)
        rows.append({'d':d,'histories':histories,'trees':trees,'tv_from_uniform':str(tv),'history_multiplicities':dict(Counter(hist.values()))})
    return {'label':'exact counterexample to uniform frontier growth','rows':rows,'one_dimensional_uniform_rule':'n vertices: choose L uniformly from 0,...,n-1; output interval [-L,n-1-L]'}

def bilateral(n,k,edge_order):
    weight={edge:rank for rank,edge in enumerate(edge_order)}
    choices=[]
    for i in range(n):
        choices.append(set(sorted((j for j in range(n) if j!=i),key=lambda j:weight[tuple(sorted((i,j)))])[:k]))
    adj=[set() for _ in range(n)]
    for i,j in weight:
        if j in choices[i] and i in choices[j]:
            adj[i].add(j); adj[j].add(i)
    return adj

def connected(adj):
    seen={0}; todo=[0]
    while todo:
        for j in adj[todo.pop()]:
            if j not in seen:
                seen.add(j); todo.append(j)
    return len(seen)==len(adj)

def check_P0456():
    rows=[]; checked=0
    for n in range(2,5):
        edges=list(combinations(range(n),2))
        allorders=list(permutations(edges))
        for k in range(1,n):
            iso=deg=conn=noiso=0
            for order in allorders:
                adj=bilateral(n,k,order)
                degrees=list(map(len,adj))
                iso+=sum(d==0 for d in degrees); deg+=degrees[0]
                conn+=connected(adj); noiso+=all(degrees)
                if k==1:
                    assert max(degrees)<=1
                    if n>2:
                        assert not connected(adj)
                checked+=1
            expected=F(iso,len(allorders))
            if k==1:
                assert expected==F(n*(n-2),2*n-3)
            rows.append({'n':n,'k':k,'orders':len(allorders),'expected_isolated':str(expected),'root_mean_degree':str(F(deg,len(allorders))),'connected_probability':str(F(conn,len(allorders))),'no_isolates_probability':str(F(noiso,len(allorders)))})
    n=6
    edges=list(combinations(range(n),2))
    order=sorted(edges,key=lambda e:(not (e[0]//3==e[1]//3),e))
    adj=bilateral(6,2,order)
    assert all(len(x)==2 for x in adj) and not connected(adj)
    save('P0456_no_isolates_counterexample',{'n':6,'k':2,'edge_order':order,'adjacency':[sorted(x) for x in adj]})
    return {'label':'exact finite cases; no asymptotic connectivity claim','checked_graphs':checked,'rows':rows,'disconnected_minimum_degree_example':2}

def coloring_law(partition,p):
    classes=sorted(set(partition)); result=Counter()
    for bits in product([0,1],repeat=len(classes)):
        mass=F(1)
        for bit in bits:
            mass*=p if bit else 1-p
        colors=dict(zip(classes,bits))
        result[tuple(colors[x] for x in partition)]+=mass
    return result

def check_C0058():
    rows=[]
    for p in [F(1,2),F(1,3),F(2,3)]:
        shared=coloring_law([0,1,0,2],p)
        distinct=coloring_law([0,1,2,3],p)
        tv=sum((abs(shared[x]-distinct[x]) for x in set(shared)|set(distinct)),F(0))/2
        assert tv==2*p*(1-p)
        rows.append({'p':str(p),'shared_partition':[0,1,0,2],'distinct_partition':[0,1,2,3],'same_word':'UUUU','law_tv':str(tv),'same_vertex_conditional_black':'1','distinct_vertex_conditional_black':str(p)})
    return {'label':'exact state-compression counterexample','rows':rows,'needed_state':'boundary incidence partition as well as colours for nonsimple boundaries'}

def anchored_cycles(kind,d,length):
    root=(0,)*d if kind=='lattice' else 0
    visit={root}; counts=Counter()
    steps=dirs(d) if kind=='lattice' else list(range(d))
    def distance(x):
        return sum(map(abs,x)) if kind=='lattice' else x.bit_count()
    def go(x,remaining,active):
        for step in steps:
            y=plus(x,step) if kind=='lattice' else x^(1<<step)
            axis=next(i for i,z in enumerate(step) if z) if kind=='lattice' else step
            newactive=active|{axis}
            if remaining==1:
                if y==root:
                    counts[len(newactive)]+=1
                continue
            if y in visit or distance(y)>remaining-1:
                continue
            visit.add(y); go(y,remaining-1,newactive); visit.remove(y)
    go(root,length,set())
    assert all(x%2==0 for x in counts.values())
    return {str(k):v//2 for k,v in counts.items()}

def choose(n,k):
    return math.comb(n,k) if n>=k else 0

def check_C0082():
    rows=[]
    for d in range(1,5):
        degree=2*d
        l4=anchored_cycles('lattice',d,4); l6=anchored_cycles('lattice',d,6)
        q4=anchored_cycles('cube',degree,4); q6=anchored_cycles('cube',degree,6)
        assert sum(l4.values())==4*choose(d,2)
        assert sum(q4.values())==choose(degree,2)
        assert l6.get('2',0)==12*choose(d,2)
        assert l6.get('3',0)==96*choose(d,3)
        assert sum(q6.values())==12*choose(degree,3)
        assert sum(l6.values())-sum(q6.values())==-F(9,2)*degree*(degree-2)
        rows.append({'lattice_dimension':d,'common_degree':degree,'lattice_squares':sum(l4.values()),'cube_squares':sum(q4.values()),'lattice_hexagons_by_axes':l6,'cube_hexagons_by_axes':q6})
    return {'label':'exact short-cycle counts, not critical-probability coefficients','graph_pairs':4,'rows':rows,'first_different_pc_coefficient':'not determined'}

def resistance(edges,source,sink):
    vertices=sorted(set(x for edge in edges for x in edge)-{sink})
    index={x:i for i,x in enumerate(vertices)}
    a=[[0]*len(vertices) for _ in vertices]
    for x,y in edges:
        if x!=sink: a[index[x]][index[x]]+=1
        if y!=sink: a[index[y]][index[y]]+=1
        if x!=sink and y!=sink:
            a[index[x]][index[y]]-=1; a[index[y]][index[x]]-=1
    rhs=[int(x==source) for x in vertices]
    return solve(a,rhs)[index[source]]

def check_C0126():
    diamond=[(0,1),(0,2),(1,3),(2,3)]
    assert resistance(diamond,0,3)==1
    return_two=F(1,2)*F(1,2)+F(1,2)*F(1,2)
    assert return_two==F(1,2)
    rows=[]
    for m in range(1,5):
        edges=[]; current=0; last=0
        for _ in range(m):
            a,b,c,z=last+1,last+2,last+3,last+4
            edges.extend([(current,a),(current,b),(a,c),(b,c),(c,z)])
            current=last=z
        val=resistance(edges,0,current)
        assert val==2*m and val>=m
        rows.append({'diamonds':m,'singleton_cut_edges':m,'resistance':str(val)})
    return {'label':'exact counterexample and deterministic resistance checks','diamond_two_step_return':str(return_two),'forward_only_return':'0','rows':rows,'random_IIC_tail_estimates':'not proved'}

def check_P0014():
    from scipy.optimize import linprog
    rows=[]; solves=0; maxres=0; producterr=0
    for n in range(2,10):
        m=n//2
        vals=[]
        for mask in range(1<<m):
            included=[s for s in range(1,m+1) if mask>>(s-1)&1]
            a=[[1]*(m+1)]+[[math.cos(2*math.pi*j*s/n) for j in range(m+1)] for s in included]
            b=[1]+[0]*len(included)
            c=[-n]+[0]*m
            res=linprog(c,A_eq=a,b_eq=b,bounds=(0,None),method='highs')
            assert res.success
            residual=max(abs(sum(x*y for x,y in zip(row,res.x))-rhs) for row,rhs in zip(a,b))
            assert residual<1e-8 and min(res.x)>-1e-9
            maxres=max(maxres,residual)
            vals.append(-res.fun); solves+=1
        for mask,theta in enumerate(vals):
            producterr=max(producterr,abs(theta*vals[(1<<m)-1-mask]-n))
        expectation=sum(vals)/len(vals)
        if n==2: assert abs(expectation-1.5)<1e-8
        if n==3: assert abs(expectation-2)<1e-8
        if n==4: assert abs(expectation-2.25)<1e-8
        if n==5: assert abs(expectation-(3+math.sqrt(5))/2)<1e-8
        rows.append({'n':n,'graphs':len(vals),'expected_theta':expectation,'ratio_to_sqrt_n':expectation/math.sqrt(n)})
        save('P0014_n'+str(n),{'label':'floating-point Fourier LP evidence','theta_by_mask':vals,'expectation':expectation,'n':n})
    assert producterr<1e-7
    return {'label':'numerical evidence; Fourier reduction is proved separately','solved_LPs':solves,'max_constraint_residual':maxres,'max_complement_product_error':producterr,'rows':rows}

def root_core(d,k,q,x):
    return q*sum((F(choose(d,j))*x**j*(1-x)**(d-j) for j in range(d-k+1,d+1)),F(0))

def check_P0042():
    # Exact fixed points and the critical saddle-node; no simulation inference.
    q=F(8,9); x=F(3,4)
    assert q*(3*x*x-2*x*x*x)==x
    assert q*(6*x-6*x*x)==1
    critical_root=root_core(4,2,q,x)
    assert critical_root==F(21,32)
    q2=F(9,10); x2=F(5,6)
    assert q2*(3*x2*x2-2*x2*x2*x2)==x2
    assert root_core(4,2,q2,x2)==F(25,32)
    q3=F(3,4); x3=F(2,3)
    assert q3*(2*x3-x3*x3)==x3
    assert root_core(3,2,q3,x3)==F(5,9)
    numeric=[]
    for d,qf in [(3,.49),(3,.5),(3,.75),(4,.8),(4,8/9),(4,.9)]:
        xf=qf
        for _ in range(2000):
            xf=qf*(2*xf-xf*xf) if d==3 else qf*(3*xf*xf-2*xf*xf*xf)
        numeric.append({'degree':d,'vacancy_q':qf,'directed_survival_after_2000':xf})
    return {'label':'exact recursion algebra plus numerical iterations','tree3_threshold':'1/2','tree4_threshold_infimum':'1/9','tree4_critical_vacant_root_probability':str(critical_root),'tree4_complete_at_threshold':False,'numerical_iterations':numeric,'general_group_characterization':'not proved'}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--problem',choices=ORDER)
    args=parser.parse_args()
    targets=[args.problem] if args.problem else ORDER
    summary={}
    for pid in targets:
        started=time.perf_counter()
        print('START',pid,flush=True)
        try:
            result=globals()['check_'+pid]()
            result['status']='PASS'
        except Exception as exc:
            result={'status':'FAIL','exception':type(exc).__name__+': '+str(exc)}
            save(pid,result)
            print(json.dumps({'problem':pid,**result}),flush=True)
            raise
        result['seconds']=round(time.perf_counter()-started,3)
        save(pid,result); summary[pid]=result
        with (OUT/'runs.jsonl').open('a',encoding='utf-8') as f:
            f.write(json.dumps({'problem':pid,**result})+'\n')
        print(json.dumps({'problem':pid,**result}),flush=True)
    save('summary',summary)

if __name__=='__main__':
    main()
