"""Frozen exact tensor boundary ledger and actual entropy payment."""
import hashlib,itertools,json,sys,time
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1];O=R/'out'
OLD=R.parent/'20261021T213328Z-account03-A017-recursive-addressing/out/boolean_counterexample.json'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(n,x):(O/n).write_bytes((json.dumps(x,indent=2)+'\n').encode('utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def fw(t):
    a=list(t);d=1
    while d<len(a):
        for b in range(0,len(a),2*d):
            for j in range(d):x,y=a[b+j],a[b+j+d];a[b+j],a[b+j+d]=x+y,x-y
        d*=2
    return a
def direct(t):return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
def factors(z):
    d={};p=2
    while p*p<=z:
        while z%p==0:d[p]=d.get(p,0)+1;z//=p
        p+=1
    if z>1:d[z]=d.get(z,0)+1
    return d
def clean(d):return {p:v for p,v in d.items() if v}
def add(a,b,k=F(1)):
    d=dict(a)
    for p,v in b.items():d[p]=d.get(p,F(0))+k*v
    return clean(d)
def H(t,ind=False):
    a=direct(t) if ind else fw(t);N=len(t);d={2:F(2*(N.bit_length()-1))}
    assert sum(v*v for v in a)==N*N
    for v in a:
        if v:
            for p,e in factors(abs(v)).items():d[p]=d.get(p,F(0))-F(2*v*v*e,N*N)
    return clean(d)
def ln_bounds(v):
    k=v.bit_length()-1;t=(F(v,1<<k)-1)/(F(v,1<<k)+1)
    def series(x):
        s=F(0);a=x
        for j in range(48):s+=2*a/(2*j+1);a*=x*x
        return s,s+2*a/(97*(1-x*x))
    l,u=series(t);a,b=series(F(1,3));return l+k*a,u+k*b
def lower(d):
    s=F(0)
    for p,c in d.items():a,b=ln_bounds(p);s+=c*(a if c>=0 else b)
    return s
def split(t,labels,j):
    k=labels.index(j);a=[v for x,v in enumerate(t) if not(x&(1<<k))];b=[v for x,v in enumerate(t) if x&(1<<k)]
    return a,b,[x for x in labels if x!=j]
def influence(t,j):return F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t))
def totalI(t):return sum(influence(t,j) for j in range(len(t).bit_length()-1))
def derivative_metrics(a,b):
    d=[F(x-y,2) for x,y in zip(a,b)];N=len(d);w=fw(d)
    norm=sum(v*v for v in w)/N**2
    energy=sum(s.bit_count()*v*v for s,v in enumerate(w))/N**2
    # Independent real physical-edge energy, not another Walsh identity.
    edge=sum((d[x]-d[x^(1<<j)])**2 for j in range(N.bit_length()-1) for x in range(N))/(4*N)
    norm_edge=sum(v*v for v in d)/N
    assert norm==norm_edge and energy==edge
    return norm,energy
def B(t,j):
    w=fw(t);N=len(t);d={}
    for s in range(N):
        if s&(1<<j):continue
        u,v=w[s]**2,w[s^(1<<j)]**2
        for z,c in [(u+v,u+v),(u,-u),(v,-v)]:
            if z:
                for p,e in factors(z).items():d[p]=d.get(p,F(0))+F(c*e,N*N)
    return clean(d)
def make(h,t,tag):
    n=6*t;result=[]
    for x in range(1<<(n+2*tag)):
        v=1
        for k in range(t):v*=h[(x>>(6*k))&63]
        if tag:v=1 if not(x&(1<<n)) else (1-2*((x>>(n+1))&1))*v
        result.append(v)
    return result
def freeze():
    O.mkdir(parents=True,exist_ok=True)
    save('spec.json',dict(helper_version='A017-tensor-bad-query-ledger-v1',helper_sha256=sha(Path(__file__)),source_sha256=sha(OLD),
      actual_Boolean_family='b^tensor(t) and A_(b^tensor(t)) with fresh physical p,z; saved actual six-bit b; selected coordinate0 in each factor',
      parameter_domain='t=1,2; tag=0,1; all factor-query permutations and both actual children at each reached node',
      root_case_count=4,node_rows=14,pilot='t=1,tag=0,1;2 roots/2 node rows',
      symmetry='none used in finite validation; all-t proof handles adaptive permutations analytically',
      arithmetic='integer Walsh; exact Fraction physical edges, derivative energies, prime-log entropy coefficients;48-term rational logarithm bounds',
      comparison_rates=['4+2/ln(2)','8','16'],memory_estimate_MB=70,max_runtime_seconds=60))
    print('FROZEN:4 actual roots;14 reached query rows; two physical representations')
def run(pilot):
    spec=read(O/'spec.json');assert sha(Path(__file__))==spec['helper_sha256'] and sha(OLD)==spec['source_sha256']
    h=read(OLD)['truth_table'];start=time.monotonic();assertions=0
    assert totalI(h)==F(9,4) and H(h)=={2:F(21,4)} and H(h,True)==H(h);assertions+=3
    c0,c1,_=split(h,list(range(6)),0);p,E=derivative_metrics(c0,c1)
    assert (p,E)==(F(1,8),F(5,16));assertions+=1
    delta=add(H(h),add(H(c0),H(c1)),F(-1,2))
    comparisons={}
    for name,rate in [('K',None),('8',8),('16',16)]:
        expr=add({2:F(1,2) if rate is None else F(rate,8)},delta,F(-1))
        margin=lower(expr)+(F(1,4) if rate is None else 0)
        comparisons[name]={'passes':margin>=0,'natural_margin_lower':str(margin)}
    b=B(h,0);assert lower(add(b,{2:F(1,2)},F(-1)))>0;assertions+=1
    rows=[];roots=[]
    for t in ([1] if pilot else [1,2]):
        for tag in (0,1):
            root=make(h,t,tag);n=6*t+2*tag
            assert totalI(root)==(F(9*t,4) if not tag else 1+F(9*t,8));assertions+=1
            assert H(root)=={2:F(21*t,4) if not tag else 2+F(21*t,8)};assertions+=1
            for perm in itertools.permutations(range(t)):
                frontier=[(root,list(range(n)),F(1))];bill=F(0);spent=F(0);terminal_entropy={}
                for level,factor in enumerate(perm):
                    nxt=[];levelbill=F(0)
                    for tt,labels,weight in frontier:
                        a,bb,rest=split(tt,labels,6*factor);piv,energy=derivative_metrics(a,bb)
                        assert piv==(F(1,8) if not tag else F(1,16));assertions+=1
                        localb=B(tt,labels.index(6*factor))
                        assert localb=={prime:value/(2 if tag else 1) for prime,value in b.items()};assertions+=1
                        localdelta=add(H(tt),add(H(a),H(bb)),F(-1,2))
                        assert localdelta=={prime:value/(2 if tag else 1) for prime,value in delta.items()};assertions+=1
                        levelbill+=weight*2*energy;spent+=weight*piv
                        nxt.extend([(a,rest,weight/2),(bb,rest,weight/2)])
                    expected=F(9*t+1,16)-F(level,32)
                    if tag:expected=expected/2+F(3,16)
                    assert levelbill==expected;assertions+=1
                    rows.append({'t':t,'tag':tag,'permutation':list(perm),'level':level,'boundary_bill':str(levelbill)})
                    bill+=levelbill;frontier=nxt
                expectedbill=F(35*t*t+5*t,64) if not tag else F(35*t*t+29*t,128)
                assert bill==expectedbill;assertions+=1
                assert spent==F(t,8*(2 if tag else 1));assertions+=1
                assert sum(weight*totalI(tt) for tt,_,weight in frontier)+spent==totalI(root);assertions+=1
                for tt,_,weight in frontier:terminal_entropy=add(terminal_entropy,H(tt),weight)
                actualdebit=add(H(root),terminal_entropy,F(-1))
                assert actualdebit=={prime:value*F(t,2 if tag else 1) for prime,value in delta.items()};assertions+=1
                roots.append({'t':t,'tag':tag,'permutation':list(perm),'boundary_bill':str(bill),'spent_original_influence':str(spent),
                  'full_terminal_influence':str(sum(weight*totalI(tt) for tt,_,weight in frontier)),
                  'full_terminal_entropy_natural_coefficients':{str(p):str(v) for p,v in terminal_entropy.items()}})
            assert time.monotonic()-start<spec['max_runtime_seconds']
    result=dict(status='PASS',pilot=pilot,assertions=assertions,query_rows=sum(1 if r['level']==0 else 2 for r in rows),
      base_derivative_norm='1/8',base_derivative_energy='5/16',base_delta_natural_coefficients={str(p):str(v) for p,v in delta.items()},
      actual_entropy_rate_checks=comparisons,rows=rows,roots=roots,elapsed_seconds=time.monotonic()-start,
      independent_representation='Derivative Walsh energy rechecked by direct physical real-edge energy at every actual node; base entropy via direct characters.')
    save('pilot.json' if pilot else 'certificate.json',result)
    print(json.dumps({k:result[k] for k in ['status','pilot','assertions','query_rows','base_delta_natural_coefficients','elapsed_seconds']}))
    print(json.dumps({'rate_checks':{k:v['passes'] for k,v in comparisons.items()}}))
if __name__=='__main__':
    if '--freeze' in sys.argv:freeze()
    else:run('--pilot' in sys.argv)
