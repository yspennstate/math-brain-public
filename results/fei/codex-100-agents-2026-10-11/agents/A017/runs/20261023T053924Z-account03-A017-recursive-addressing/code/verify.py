"""Exact interacting-block/prefix verification; no floating point entropy signs."""
import argparse, hashlib, itertools, json, time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
R=Path(__file__).resolve().parents[1]
O=R/'out'
PR=(2,3,5,7,11,13,17,19,23,29,31)
def write(name,v):
    (O/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def factors(v):
    d={};p=2
    while p*p<=v:
        while v%p==0: d[p]=d.get(p,0)+1;v//=p
        p+=1
    if v>1:d[v]=d.get(v,0)+1
    return d
def walsh(t):
    a=list(t);step=1
    while step<len(a):
        for b in range(0,len(a),2*step):
            for j in range(step):
                x,y=a[b+j],a[b+j+step];a[b+j],a[b+j+step]=x+y,x-y
        step*=2
    return a
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,b): return tuple(x*b for x in a)
ZERO=(0,)*len(PR)
def entropy_vec(t):
    n=len(t).bit_length()-1;v=[0]*len(PR);v[0]=2*len(t)**2*n
    a=walsh(t)
    assert sum(x*x for x in a)==len(t)**2
    for x in a:
        if x:
            for p,e in factors(abs(x)).items():v[PR.index(p)]-=2*x*x*e
    return tuple(v)
@lru_cache(None)
def ln_interval(v):
    k=v.bit_length()-1;y=F(v,1<<k);t=(y-1)/(y+1)
    def series(t):
        s=F(0);power=t
        for r in range(48):s+=2*power/(2*r+1);power*=t*t
        return s,s+2*power/(97*(1-t*t))
    a,b=series(t)
    if k:
        c,d=series(F(1,3));a+=k*c;b+=k*d
    return a,b
def interval(v):
    lo=hi=F(0)
    for p,c in zip(PR,v):
        a,b=ln_interval(p)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def masks128():
    values={0,65535,0xaaaa,0x5555}
    values.update(range(60));s=17391
    while len(values)<128:s=(25173*s+13849)%65536;values.add(s)
    return sorted(values)
def freeze():
    O.mkdir(parents=True,exist_ok=True)
    if (O/'spec.json').exists() and read(O/'spec.json')['helper_sha256']!=digest(Path(__file__)):
        (O/'spec_v1_before_normalization_fix.json').write_bytes((O/'spec.json').read_bytes())
    write('spec.json',dict(helper_version='A017-interacting-tangent-prefix-v2',helper_sha256=digest(Path(__file__)),
      actual_Boolean_family='q=x0*x1+x2*x3 at n4; q=x0*x1+x2*x3+x2*x4+x3*x4 at n5; arbitrary specified inside-half masks and zero/one outside edit',
      parameter_domain={'n4_inside_masks':'all256','n4_outside_edits':'none','n5_inside_masks':masks128(),'n5_outside_edits':'none or one of16 outside vertices'},
      case_count=2432,adaptive_policies_per_parent={'n4':9,'n5':244},policy_rows=533248,
      symmetry='none; original physical coordinates throughout',arithmetic='integer Walsh, exact prime-log coefficient telescopes; rational atanh-series log intervals with proved tail',
      memory_estimate_MB=80,max_runtime_seconds=180,pilot='16 n4 parents and 4 n5 masks with first3 outside choices;28 parents'))
    old=R.parent/'20261021T213328Z-account03-A017-recursive-addressing/out/boolean_counterexample.json'
    write('witness_spec.json',dict(helper_sha256=digest(Path(__file__)),actual_Boolean_family='q=i*p+j*k; outside p0=(-1)^(j*k), inside p1=(-1)^z*h(k,r), inherited six-bit h',
      inherited_sha256=digest(old),case_count=1,n=10,selected_child_coordinate='original h coordinate0 after querying j=0',
      symmetry='none',arithmetic='integer Walsh, edge counts, exact prime-factor erasure products',memory_estimate_MB=35,max_runtime_seconds=30))
    print('FROZEN:2432 parents/533248 adaptive prefix rows; 1 actual 10-bit fixture')
def table(n,inside,outside):
    a=[]
    for x in range(1<<n):
        bit=lambda j:(x>>j)&1
        q=(bit(0)&bit(1))^(bit(2)&bit(3))
        if n==5:q^=(bit(2)&bit(4))^(bit(3)&bit(4))
        g=1-2*q
        if bit(1):
            k=(x&1)|((x>>2)<<1)
            if (inside>>k)&1:g=-g
        elif x==outside:g=-g
        a.append(g)
    return a
def verify_parent(n,t):
    J=tuple(range(2,n));N=len(t);checks=0
    @lru_cache(None)
    def state(key):
        fixed=dict(key);labels=[j for j in range(n) if j not in fixed]
        a=tuple(t[x] for x in range(N) if all(((x>>j)&1)==v for j,v in key))
        counts={j:sum(a[x]!=a[x^(1<<labels.index(j))] for x in range(len(a))) for j in J if j not in fixed}
        return a,mul(entropy_vec(a),1<<len(key)),counts
    @lru_cache(None)
    def policies(key):
        a,h,counts=state(key);result=[(0,h,sum(counts.values()))]
        for j,c in counts.items():
            k0=tuple(sorted(key+((j,0),)));k1=tuple(sorted(key+((j,1),)))
            for x in policies(k0):
                for y in policies(k1):result.append((c+x[0]+y[0],add(x[1],y[1]),x[2]+y[2]))
        return tuple(result)
    _,H,counts=state(())
    for j,c in counts.items():assert c*16>=3*N;checks+=1
    original=sum(counts.values())
    final=ZERO
    for v in itertools.product((0,1),repeat=len(J)):final=add(final,state(tuple(zip(J,v)))[1])
    delta=sub(H,final)
    # N^2 times natural-log margin K I_J - Delta.
    margin=list(mul(delta,-1));margin[0]+=4*N*original
    lower=interval(tuple(margin))[0]+2*N*original
    assert lower>=0;checks+=1
    rows=policies(())
    assert len(rows)==(9 if n==4 else 244)
    for spent,leaf,remaining in rows:
        assert spent+remaining==original
        d=sub(H,leaf);r=sub(leaf,final)
        assert add(d,r)==delta
        checks+=2
    # Nonnegativity of all local increments implies every prefix/completion has nonnegative debt.
    for key in all_keys(J):
        _,hs,cs=state(key)
        for j in cs:
            a=state(tuple(sorted(key+((j,0),))))[1]
            b=state(tuple(sorted(key+((j,1),))))[1]
            assert interval(sub(hs,add(a,b)))[0]>=0 or sub(hs,add(a,b))==ZERO
            checks+=1
    return len(rows),checks,lower
def all_keys(J):
    for vals in itertools.product((-1,0,1),repeat=len(J)):
        yield tuple((j,v) for j,v in zip(J,vals) if v!=-1)
def run(pilot):
    spec=read(O/'spec.json');assert spec['helper_sha256']==digest(Path(__file__))
    started=time.monotonic();parents=rows=checks=0;minmargin=None;coverage=hashlib.sha256()
    family=[(4,range(16) if pilot else range(256),[-1]),
      (5,spec['parameter_domain']['n5_inside_masks'][:4] if pilot else spec['parameter_domain']['n5_inside_masks'],
       [-1,0,1] if pilot else [-1]+[x for x in range(32) if not(x&2)])]
    for n,masks,outs in family:
        for m in masks:
            for o in outs:
                t=table(n,m,o);r,c,lb=verify_parent(n,t);parents+=1;rows+=r;checks+=c
                coverage.update(bytes([n])+m.to_bytes(2,'little')+bytes([o+1]))
                minmargin=lb if minmargin is None else min(lb,minmargin)
                assert time.monotonic()-started<spec['max_runtime_seconds'],'frozen runtime cap exceeded'
    result=dict(status='PASS',pilot=pilot,parents=parents,adaptive_prefix_rows=rows,assertions=checks,
      minimum_scaled_natural_margin=str(minmargin),coverage_sha256=coverage.hexdigest(),elapsed_seconds=time.monotonic()-started,
      log_interval_terms=48,log_tail='2*t^97/(97*(1-t^2)); t<=1/3')
    write('pilot.json' if pilot else 'certificate.json',result)
    print(json.dumps(result))
def erasure(t,j):
    a=walsh(t);d={}
    for s in range(len(a)):
        if s&(1<<j):continue
        u,v=a[s]**2,a[s^(1<<j)]**2
        for z,c in [(u+v,u+v),(u,-u),(v,-v)]:
            if z:
                for p,e in factors(z).items():d[p]=d.get(p,0)+c*e
    return {p:F(c,len(t)**2) for p,c in d.items() if c}
def witness():
    spec=read(O/'witness_spec.json');assert spec['helper_sha256']==digest(Path(__file__))
    old=R.parent/'20261021T213328Z-account03-A017-recursive-addressing/out/boolean_counterexample.json'
    assert digest(old)==spec['inherited_sha256'];h=read(old)['truth_table']
    # h occupies bits0..5 (selected k=0); i=6,p=7,j=8,z=9.
    a=[];edits=[]
    for x in range(1024):
        i,p,j,z=((x>>b)&1 for b in (6,7,8,9));k=x&1
        g=(1-2*(j*k)) if p==0 else (1-2*z)*h[x&63]
        q=(i*p)^(j*k)
        if g!=1-2*q:edits.append(x);assert p==1
        a.append(g)
    child=[a[x] for x in range(1024) if not(x&256)]
    B=erasure(h,0);Bc=erasure(child,0)
    assert Bc=={p:v/2 for p,v in B.items()}
    def inf(t,j):return F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t))
    assert inf(h,0)==F(1,8) and inf(child,0)==F(1,16)
    assert inf(a,8)==F(1,4) and inf(a,0)==F(5,16)
    assert 17**136*5**120>2**832
    expected={2:F(-704,256),17:F(136,256),5:F(120,256)}
    assert B==expected
    result=dict(status='PASS',n=10,truth_table=a,inside_edit_count=len(edits),outside_edit_count=0,
      root_selected_influences={'j':'1/4','k':'5/16'},child_influence='1/16',
      child_erasure_natural_coefficients={str(p):str(v) for p,v in Bc.items()},
      exact_bad_sign='17^136*5^120>2^832',assertions=10,
      interpretation='Hereditary singleton K4 fails; committed interacting block at SAME K remains paid.')
    write('bad_intermediate_query.json',result);print('PASS: actual 10-bit parent, bad physical child query, exact tagged erasure scaling')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');p.add_argument('--pilot',action='store_true');p.add_argument('--witness',action='store_true');args=p.parse_args()
    if args.freeze:freeze()
    elif args.witness:witness()
    else:run(args.pilot)
