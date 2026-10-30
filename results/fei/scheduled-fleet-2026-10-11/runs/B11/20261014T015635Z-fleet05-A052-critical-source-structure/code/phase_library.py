"""A052 stage3: direct character rows and exact critical phase certificates."""
import ast,json,time,hashlib
from fractions import Fraction as F
from pathlib import Path
import exact_library as e
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    checks+=1
    if not x: raise AssertionError(checks)
def add(a,b,k=1):
    c=dict(a)
    for p,v in b.items(): c[p]=c.get(p,F(0))+k*v
    return {p:v for p,v in c.items() if v}
def lograt(x):
    return add({p:F(c) for p,c in e.factors(x.numerator).items()},
               {p:F(c) for p,c in e.factors(x.denominator).items()},-1)
def entropy(p):
    out={}
    for x in p:
        if x: out=add(out,lograt(x),-x)
    return out
def scale(a,k):return {p:k*v for p,v in a.items() if k*v}
def sg(a):return e.sign(a)
def enc(a):return {str(p):str(v) for p,v in a.items()}
def interval(a):
    lo,hi=e.enclosure(a); l2,h2=e.lnprime(2)
    v=[F(x,y) for x in (lo,hi) for y in (l2,h2)]
    return [str(min(v)),str(max(v))]
def stats(v):
    N=len(v); n=N.bit_length()-1
    w=e.direct(v); p=[F(x*x,N*N) for x in w]
    I=sum(s.bit_count()*x for s,x in enumerate(p))
    ck(sum(p)==1)
    ck(I==F(sum(v[x]!=v[x^(1<<i)] for x in range(N) for i in range(n)),N))
    return entropy(p),I,p
def block(v,A):
    n=len(v).bit_length()-1; ai=[i for i in range(n) if A>>i&1]; ci=[i for i in range(n) if not A>>i&1]
    m=1<<len(ai); d=1<<len(ci)
    children=[[v[e.unpack(a,ai)|e.unpack(c,ci)] for c in range(d)] for a in range(m)]
    rows=list(zip(*[[F(x,d) for x in e.direct(h)] for h in children]))
    H,I,p=stats(v); IA=sum((s&A).bit_count()*x for s,x in enumerate(p))
    q=[sum(x*x for x in row)/m for row in rows]
    B=add(H,entropy(q),-1); child=[stats(h) for h in children]
    L=dict(H)
    for h,_,_ in child:L=add(L,h,-F(1,m))
    J=add(L,B,-1); G={}; collision=F(0); phase_B={}; phase_I=F(0); rowrecords=[]
    for t,(row,mass) in enumerate(zip(rows,q)):
        if not mass:continue
        ratio=sum(x**4 for x in row)/(m*mass*mass)
        collision+=mass*(ratio-1); G=add(G,lograt(ratio),mass)
        co=[sum(row[a]*(-1 if (a&u).bit_count()%2 else 1) for a in range(m))/m for u in range(m)]
        conv=[sum(co[u]*co[u^z] for u in range(m)) for z in range(m)]
        ck(conv[0]==mass); ck(sum(x*x for x in conv)==sum(x**4 for x in row)/m)
        phase=[1 if x>=0 else -1 for x in row]; ph,pi,_=stats(phase)
        phase_B=add(phase_B,ph,mass);phase_I+=mass*pi
        phw=e.direct(phase)
        nu=[x*x/mass for x in co]; rho=[F(x*x,m*m) for x in phw]
        tv=sum(abs(x-y) for x,y in zip(nu,rho))/2
        mean_abs=sum(abs(x) for x in row)/m
        # TV^2<=tau^2, without computing sqrt(q).
        ck(mass*(2-tv*tv)**2>=4*mean_abs*mean_abs)
        c=ratio-1
        if c<2:ck(4*mean_abs*mean_abs>=mass*(2-c)**2)
        rowI=sum(u.bit_count()*x for u,x in enumerate(nu))
        ck(abs(pi-rowI)<=len(ai)*tv)
        fannes=add(entropy([tv,1-tv]),lograt(F(m-1)),tv)
        enu=entropy(nu)
        ck(sg(add(fannes,add(enu,ph,-1),-1))>=0)
        ck(sg(add(fannes,add(ph,enu,-1),-1))>=0)
        if ratio==1:
            ck(all(x*x==mass for x in row))
            # Rational squared coefficients suffice: no square-root evaluation.
            ck(all(co[u]*co[u]==mass*F(phw[u]**2,m*m) for u in range(m)))
        rowrecords.append({'row':t,'q':str(mass),'values':[str(x) for x in row],
                           'collision_ratio':str(ratio),'phase_truth':phase})
    ck(sg(J)>=0); ck(sg(add(G,J,-1))>=0);ck(sg(add(lograt(1+collision),G,-1))>=0)
    ck(I==IA+sum(x[1] for x in child)/m)
    if collision==0:
        ck(not G);ck(not J);ck(B==phase_B);ck(IA==phase_I)
    if len(ci)==1:ck(G==J);ck(add(B,G)==H)
    return dict(H=H,I=I,IA=IA,B=B,J=J,G=G,L=L,C=collision,children=child,rows=rowrecords)
def serial(r):
    return {k:enc(v) if k in ('H','B','J','G','L') else str(v) for k,v in r.items() if k not in ('children','rows')}|{'rows':r['rows']}
def main():
    start=time.perf_counter(); count=blocks=critical=zero_critical=ratio_critical_zero=0
    distribution={}
    for n in (1,2,3):
        ct=cb=0
        for code in range(1<<(1<<n)):
            v=[1 if code>>x&1 else -1 for x in range(1<<n)]
            H,I,_=stats(v); count+=1
            if not I:continue
            D=add(H,{2:2*I},-1); iscritical=(n==3 and sg(D)>0)
            rr=[]
            for A in range(1,(1<<n)-1):
                r=block(v,A); blocks+=1; rr.append(r)
                if iscritical:
                    for hc,ic,_ in r['children']:ck(sg(add(hc,{2:2*ic},-1))<=0)
                    ck(r['C']>0)
                    ck(sg(add(add(r['B'],r['G']),{2:2*r['IA']},-1))-0>=0)
                    ck(sg(add(add(add(r['B'],r['G']),{2:2*r['IA']},-1),D,-1))>=0)
                if n==2:ck(sg(D)<=0)
            ratio_crit=all(sg(add(scale(H,ic),scale(hc,I),-1))>=0 for r in rr for hc,ic,_ in r['children'])
            if ratio_crit and any(r['C']==0 and r['IA']>0 for r in rr):ratio_critical_zero+=1
            if iscritical:critical+=1;ct+=1;cb+=len(rr)
        distribution[str(n)]={'K2_violations_with_lower_dimension_certified':ct,'critical_blocks':cb}
    tree=ast.literal_eval('(((((), ()), (), ()), ()), ())')
    v=[2*x-1 for x in e.table(tree)]; nr=[]
    source=json.loads((Path(r'~\brain_workers\FEI100_20261011\agents\A051\runs\20261013T215311Z-fleet05-A051-near-extremizer-definition\out\CONTROL_NAND6_case0006.json')).read_text())
    ck(hashlib.sha256(bytes(e.table(tree))).hexdigest()==source['truth_sha256'])
    for A in range(1,63):
        r=block(v,A); cost=add(r['B'],r['G']); gap=add(scale(cost,r['I']),scale(r['H'],r['IA']),-1)
        nr.append({'mask':A,'affordable':sg(gap)<0,'cost_per_IA':interval(scale(cost,1/r['IA']))})
        if A&(A-1)==0:ck(sg(add(cost,{2:F(319,100)*r['IA']},-1))>0)
        if A==48:
            ck(sg(add(cost,{2:F(47,20)},-1))<0); ck(sg(add(r['H'],{2:F(12,5)*r['I']},-1))>0)
            ck(sg(add(r['L'],{2:F(23,10)},-1))<0)
            for key in ('H','B','J','Gamma'):
                ours=r['G' if key=='Gamma' else key]
                ck(enc(ours)==source['selected'][key])
            hc,ic,_=r['children'][3];childdef=add(hc,scale(r['H'],ic/r['I']),-1)
            ck(sg(childdef)>0);ck(add(scale(childdef,F(1,4)),add(scale(r['H'],r['IA']/r['I']),r['L'],-1),-1)=={})
            (ROOT/'out/NAND48.json').write_text(json.dumps(serial(r)|{'cost_per_IA':interval(cost),'child_deficit':interval(childdef)},indent=2))
    ck([x['mask'] for x in nr if x['affordable']]==[48])
    # Physical-descendant criticality alone permits a full-factor zero channel.
    quad=lambda x:-1 if (x&1) and (x&2) else 1
    tensor=[quad(x&3)*quad(x>>2) for x in range(16)]
    H,I,_=stats(tensor);ck(H=={2:F(4)});ck(I==2)
    for A in range(1,15):
        r=block(tensor,A)
        for hc,ic,_ in r['children']:ck(sg(add(hc,{2:2*ic},-1))<=0)
        if A==3:ck(r['C']==0);ck(r['IA']==1);ck(r['B']=={2:F(2)})
    result={'status':'PASS','tables':count,'small_proper_blocks':blocks,'K2_dimension_minimal_violators_n3':critical,
            'distribution':distribution,'ratio_critical_tables_with_relevant_zero_channel_block_n_le3':ratio_critical_zero,
            'named_NAND_blocks':nr,'quadratic_tensor_zero_channel_counterexample':'PASS',
            'assertions':checks,'runtime_seconds':time.perf_counter()-start}
    (ROOT/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='named_NAND_blocks'}))
if __name__=='__main__':main()
