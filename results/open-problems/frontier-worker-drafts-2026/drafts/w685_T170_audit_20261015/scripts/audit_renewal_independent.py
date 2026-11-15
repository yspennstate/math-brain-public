"""Self-audit with coordinate closure, killed-walk counts, and a new error bound.

No production producer is imported. This is not independent-model approval.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter, deque
from functools import lru_cache
from math import factorial, isqrt
from datetime import datetime, timezone
import argparse, ctypes, hashlib, json, os, sys, time

for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audits'
def read(path): return json.loads(path.read_text(encoding='utf-8'))
def fraction(obj,key): return F(int(obj[key]['n']),int(obj[key]['d']))
def freeze(x): return tuple(map(freeze,x)) if isinstance(x,list) else x
def emit(name,obj):
    obj.update(at=datetime.now(timezone.utc).isoformat(),independent_model_approval=False)
    with (OUT/(name+'.json')).open('w',encoding='utf-8',newline='\n') as handle:
        json.dump(obj,handle,indent=2);handle.write('\n')
    print(name, json.dumps({k:v for k,v in obj.items() if k in ('states','rows','dimensions','rho_upper','result','seconds')}),flush=True)
def canonical(word):
    labels={}
    return tuple((labels.setdefault(axis,len(labels)),sign) for axis,sign in word)
def coordinates(word):
    size=max(a for a,s in word)+1
    out=[(0,)*size]
    for axis,sign in word:
        nxt=list(out[-1]);nxt[axis]+=sign;out.append(tuple(nxt))
    return out
def description(word,selected,p):
    pts=coordinates(word);n=len(word);q=2*((n-3)//2)
    distance=lambda i,j:sum(abs(x-y) for x,y in zip(pts[i],pts[j]))
    chords=[i for i in range(n-2) if distance(i,i+3)==1]
    cover=[sum(i<=j<i+3 for i in chords) for j in range(n)]
    touched={i if i%2==0 else i+3 for i in chords}
    dirty={b for endpoint in touched for b in (endpoint-2,endpoint)}
    for b in range(0,n-3,2):
        if distance(b,b+4)<=2:dirty.update((b,b+2))
    eligible={b:word[b][0]!=word[b+1][0] and b not in dirty for b in range(0,n-1,2)}
    pending=list(range(q,n-1,2))
    state=(n%2,canonical(word[-3:]),tuple(cover[q:]),tuple(eligible[b] for b in pending),
           (n-n%2) in touched,tuple(b+1 in selected and b+3<=n for b in pending),q-1 in selected,p)
    return state,q,cover,eligible
def no_short_return(word):
    pts=coordinates(word)
    return all(pts[-1]!=pts[-1-k] for k in (2,4) if len(word)>=k)

def graph_audit():
    started=time.monotonic();graph=read(ROOT/'scripts/height_renewal_graph.json')
    states=list(map(freeze,graph['states']));index={s:i for i,s in enumerate(states)}
    assert len(index)==len(states)==len(graph['rows'])
    witnesses={};queue=deque();actual_seeds=set()
    def remember(word,chosen,p):
        state=description(word,chosen,p)[0]
        assert state in index,('missing coordinate state',word,chosen,p,state)
        i=index[state]
        if i not in witnesses:witnesses[i]=(word,chosen,p);queue.append(i)
        return i
    def seed(word):
        if len(word)==4:
            actual_seeds.add(remember(word,frozenset(),0))
            if word[1][1]==word[2][1]==1 and word[1][0]!=word[2][0]:remember(word,frozenset({1}),0)
            return
        for axis in range(max((a for a,s in word),default=-1)+2):
            for sign in (-1,1):
                full=word+((axis,sign),)
                if no_short_return(full):seed(full)
    seed(());seed_states=len(witnesses);row_checks=0;transitions=0;max_witness=4
    while queue:
        i=queue.popleft();word,chosen,p=witnesses[i];n=len(word)
        state,q0,_,_=description(word,chosen,p);assert state==states[i]
        old_axes=sorted({a for a,s in word[-3:]});fresh=max(a for a,s in word)+1
        for mark in (0,1):
            expected=[]
            for axis in old_axes+[fresh]:
                for sign in (-1,1):
                    full=word+((axis,sign),)
                    if not no_short_return(full):continue
                    chosen2=chosen
                    if mark and n%2==0 and word[-1][1]==sign==1 and word[-1][0]!=axis:
                        chosen2=chosen|{n-1}
                    proto,q1,cover,eligible=description(full,chosen2,0)
                    final=int(q1!=q0);r=0 if axis in old_axes else len(old_axes)
                    moments=(0,1) if final and proto[6] else ((0,) if final else (p,))
                    for qp in moments:
                        j=remember(full,frozenset(chosen2),qp)
                        if final:
                            row=(j,sign,r,1,cover[q0],cover[q0+1],int(eligible[q0]),int(q0+1 in chosen2),int(state[6]),p,qp)
                        else:row=(j,sign,r,0,0,0,0,0,int(state[6]),p,p)
                        expected.append(row)
            actual=list(map(tuple,graph['rows'][i][mark]))
            assert Counter(expected)==Counter(actual),('transition inventory mismatch',i,mark,Counter(expected)-Counter(actual),Counter(actual)-Counter(expected))
            row_checks+=1;transitions+=len(expected)
        max_witness=max(max_witness,n)
    assert len(witnesses)==len(states),('unreconciled states',set(range(len(states)))-set(witnesses))
    emit('graph_coordinate_closure',dict(result='PASS',states=len(states),rows=row_checks,transitions=transitions,
         seed_states=seed_states,actual_false_flag_seed_states=len(actual_seeds),maximum_witness_length=max_witness,
         method='Full-coordinate witness for every state; every legal old-axis/fresh-axis, sign, mark and moment branch compared as a multiset; closure exhausts the graph.',
         graph_sha256=hashlib.sha256((ROOT/'scripts/height_renewal_graph.json').read_bytes()).hexdigest(),seconds=time.monotonic()-started))

@lru_cache(None)
def pair_integral(a,c0,c1,E,O,I,p,q):
    poly={(p,0,0):F(1)}
    for active,terms in ((E,((0,0,0),(1,0,0),(0,1,0))),(O,((0,0,0),(0,1,0),(0,0,1)))):
        if not active:continue
        nxt={}
        for powers,value in poly.items():
            for term in terms:
                key=tuple(x+y for x,y in zip(powers,term));nxt[key]=nxt.get(key,F(0))+value
        poly=nxt
    x,y=a+c0+I+E,a+c1+E+O
    raw=sum(value*factorial(e0)*factorial(e1)/x**(e0+1)/y**(e1+1)
            for (e0,e1,e2),value in poly.items() if e2==q)
    return a**(1+p-q)*raw

def killed_counts(K):
    counts=[[0]*(K+1) for _ in range(K+1)];counts[1][1]=1
    for height in range(2,K+1):
        v=[0]*(height+1);v[1]=1
        for n in range(2,K+1):
            counts[n][height]=v[height-1]
            v=[0]+[v[j-1]+v[j+1] for j in range(1,height)]+[0]
    return counts

def case(d):return ROOT if d==21 else ROOT/'dimension_extension'/('d'+str(d))
def arithmetic_audit(d):
    started=time.monotonic();base=case(d);point=read(base/'logs/height_bridge_tail_certificate.json')
    graph=read(base/'scripts/height_renewal_graph.json');states=graph['states'];a=fraction(point,'s')+1;z=fraction(point,'z');t=F(7,5)
    assert int(point.get('d',d))==d
    assert (base/'scripts/height_renewal_graph.json').read_bytes()==(ROOT/'scripts/height_renewal_graph.json').read_bytes()
    assert z>1 and a>1
    r=d*(z+t**4/z)/(a*t);ceiling=F(9,10) if d==21 else F(91,100)
    assert r<ceiling<1
    w=[(a/(a+s[6]))**(s[7]+1) for s in states];norm_rows=0
    for i,both in enumerate(graph['rows']):
        for rows in both:
            for sign in (-1,1):
                total=F(0)
                for j,sgn,fresh,final,c0,c1,E,O,I,p,q in rows:
                    if sgn!=sign:continue
                    assert I==states[i][6] and p==states[i][7]
                    assert states[j][6]==(O if final else I) and states[j][7]==q
                    value=pair_integral(a,c0,c1,E,O,I,p,q) if final else 1/a
                    total+=(d-fresh if fresh else 1)*value*w[j]
                assert total<=F(d,1)/a*w[i];norm_rows+=1
    K=400;counts=killed_counts(K);R=a.numerator*z.denominator;b=d*a.denominator
    bp=[b**n for n in range(K+1)];zp=[z.numerator**n for n in range(K+1)];dp=[z.denominator**n for n in range(K+1)]
    A=[0]*(K+1);B=[0]*(K+1);units=0;scale=10**40
    for n in range(1,K+1):
        A[n]=bp[n]*sum(counts[n][h]*zp[h]*dp[n-h] for h in range(1,n+1))
        B[n]=A[n]-sum(B[j]*A[n-j] for j in range(1,n))
        assert B[n]>=0
        units+=B[n]*scale//R**n
    scalar=read(base/'logs/scalar_bridge_mass_certificate.json')
    lower=F(units,scale);upper=lower+F(K,scale)+t*ceiling**(K+1)/(1-ceiling)
    assert fraction(scalar,'total_lower')==lower and fraction(scalar,'total_upper')==upper
    assert t*ceiling**401/(1-ceiling)<F(1,10**15)
    # Independent downward log/square-root arithmetic; positive series terms.
    s=a-1;u=(z-1)/(z+1);log_floor=2*sum(u**(2*j+1)/F(2*j+1) for j in range(50))
    sqrt_floor=F(isqrt(d*10**48),10**24);ratio=sqrt_floor*log_floor/s
    floor12=ratio.numerator*10**12//ratio.denominator
    emit('arithmetic_d'+str(d),dict(result='PASS',d=d,rows=norm_rows,scalar_lengths=K,
         ratio_floor_12=floor12,r=str(r),tail_ceiling=str(ceiling),seconds=time.monotonic()-started,
         method='Coordinate graph input; polynomial dictionary factorial integrals; all norm rows rational; killed-walk DP instead of reflection counts; 400 exact renewal coefficients; independent positive log series and integer square root.'))

def enumerate_profiles(K):
    out=[];stack=[((),0,(1,))]
    while stack:
        word,height,visits=stack.pop()
        if len(word)==K:continue
        for step in (-1,1):
            new=height+step
            if new<=0:continue
            cnt=list(visits)
            if new==len(cnt):cnt.append(0)
            full=word+(step,)
            if cnt[new]==0 and all(c>=2 for c in cnt[1:new]):out.append((full,new))
            cnt[new]+=1;stack.append((full,new,tuple(cnt)))
    return out

def operator_audit(d):
    import numpy as np
    class MEMORY(ctypes.Structure):
        _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong),('total',ctypes.c_ulonglong),('available',ctypes.c_ulonglong),('rest',ctypes.c_ulonglong*5)]
    mem=MEMORY();mem.length=ctypes.sizeof(mem);assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem))
    assert mem.available>=2*1024**3,'WAIT: less than 2GB free'
    started=time.monotonic();base=case(d);point=read(base/'logs/height_bridge_tail_certificate.json')
    a=fraction(point,'s')+1;z=fraction(point,'z');graph=read(base/'scripts/height_renewal_graph.json');states=graph['states'];n=len(states)
    assert read(OUT/('arithmetic_d'+str(d)+'.json'))['result']=='PASS'
    words=enumerate_profiles(21);cnt=Counter((len(word),h) for word,h in words);counts=killed_counts(21);irreducible={}
    for length in range(1,22):
        for h in range(1,length+1):
            value=counts[length][h]-sum(irreducible.get((j,k),0)*counts[length-j][h-k]
                  for j in range(1,length) for k in range(1,h))
            assert value>=0 and value==cnt[(length,h)]
            irreducible[(length,h)]=value
    assert len(words)==8912
    selected=read(base/'logs/height_renewal_measure_K21.json');ids=[i for i,state in enumerate(states) if state[1][-1][1]==1]
    assert selected['boundary_ids']==ids;v=np.asarray(selected['vector'],dtype=np.float64);assert len(v)==len(ids) and np.isfinite(v).all() and (v>0).all()
    def ceil_binary(exact):
        x=float(exact)
        if F.from_float(x)<exact:x=float(np.nextafter(x,np.inf))
        assert F.from_float(x)>=exact
        return x
    matrices={};u=F(1,2**53)
    for mark in (0,1):
        for sign in (-1,1):
            rows=[]
            for both in graph['rows']:
                row=[]
                for j,sgn,fresh,final,c0,c1,E,O,I,p,q in both[mark]:
                    if sgn!=sign:continue
                    factor=pair_integral(a,c0,c1,E,O,I,p,q) if final else 1/a
                    exact=(d-fresh if fresh else 1)*z**sign*factor
                    assert exact>0;row.append((j,ceil_binary(exact)))
                rows.append(row)
            width=max(map(len,rows));data=np.zeros((width,n));targets=np.zeros((width,n),dtype=np.int64)
            for i,row in enumerate(rows):
                for k,(j,coef) in enumerate(row):data[k,i]=coef;targets[k,i]=j
            positive=data[data>0];assert positive.min()>2.0**-400 and positive.max()<2.0**400
            # Each positive summand has one product and at most width additions.
            matrices[(mark,sign)]=(data,targets,ceil_binary((1-u)**(-width-1)))
    assert np.finfo(np.float64).nmant==52
    assert sys.float_info.radix==2 and sys.float_info.mant_dig==53 and sys.float_info.rounds==1
    def widen(vector,factor):
        out=vector*factor;mask=out>0
        assert np.isfinite(out).all()
        out[mask]=np.nextafter(out[mask],np.inf)
        return out
    def upper_dot(key,vector):
        data,targets,correction=matrices[key];positive=vector[vector>0]
        if len(positive):assert positive.min()>2.0**-400 and positive.max()<2.0**400
        total=np.zeros(n)
        for coef,target in zip(data,targets):
            prod=coef*vector[target]
            assert not ((coef>0)&(vector[target]>0)&(prod==0)).any()
            total=total+prod
        assert np.isfinite(total).all()
        return widen(total,correction)
    initial=np.zeros(n);initial[ids]=v;cache={():initial}
    def suffix(word):
        if word not in cache:cache[word]=upper_dot((0,word[0]),suffix(word[1:]))
        return cache[word]
    bins={}
    for word,h in words:
        level=0;value=suffix(word[1:])
        while level in bins:value=bins.pop(level)+value;level+=1
        bins[level]=value
    total=np.zeros(n)
    for level in sorted(bins):total=total+bins[level]
    # Every leaf crosses at most log2(N) carry additions and log2(N)+1
    # final-bin additions. This bound does not assume a library sum order.
    budget=2*len(words).bit_length()+2
    total=widen(total,ceil_binary((1-u)**(-budget)))
    short_vector=upper_dot((1,1),total)[ids]
    assert len(cache)*n*8+256000000<1000000000
    scalar=read(base/'logs/scalar_bridge_mass_certificate.json')
    short=sum(F(count)*(F(d,1)/a)**length*z**h for (length,h),count in cnt.items())
    tail=fraction(scalar,'total_upper')-short;assert tail>0
    w=[(a/(a+state[6]))**(state[7]+1) for state in states]
    C=max(F.from_float(float(v[k]))/w[i] for k,i in enumerate(ids))
    ratios=[(F.from_float(float(short_vector[k]))+tail*C*w[i])/F.from_float(float(v[k])) for k,i in enumerate(ids)]
    assert max(ratios)<1
    original=read(base/'logs/height_renewal_interval_certificate.json')
    stated=fraction(original,'rho_upper')
    assert max(ratios)<=stated,('independent enclosure does not reach original stated kappa',d,float(max(ratios)),float(stated))
    upper=(max(ratios).numerator*10**18+max(ratios).denominator-1)//max(ratios).denominator
    emit('operator_d'+str(d),dict(result='PASS',d=d,rows=len(ids),profiles=len(words),cached_suffixes=len(cache),rho_upper=str(upper)+'/10^18',
         seconds=time.monotonic()-started,available_memory=mem.available,estimated_peak_bytes=len(cache)*n*8+256000000,
         original_rho_upper=str(stated),original_stated_upper_verified=True,
         method='Independent implementation; ordinary explicit positive sums with a binary-bin profile sum enclosed by exact (1-2^-53)^(-operation budget) correction, upward coefficient conversion and final nextafter; no producer imported.'))

def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=('graph','arithmetic','operator'));parser.add_argument('--d',type=int,choices=(21,19,18),default=21);args=parser.parse_args()
    OUT.mkdir(exist_ok=True)
    if args.phase=='graph':graph_audit()
    elif args.phase=='arithmetic':arithmetic_audit(args.d)
    else:operator_audit(args.d)
if __name__=='__main__':main()
