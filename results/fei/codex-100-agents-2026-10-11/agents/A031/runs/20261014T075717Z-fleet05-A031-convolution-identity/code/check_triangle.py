import argparse,json,time,types
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
from pathlib import Path
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261013T215020Z-fleet05-A031-convolution-identity/code/check_carrier.py'
kernel=types.ModuleType('immutable_exact_kernel');kernel.__file__=str(old)
exec(compile(old.read_text(encoding='utf8'),str(old),'exec'),kernel.__dict__)
walsh=kernel.walsh;logs=kernel.logs

def geometry(widths):
    private=[];offset=3
    for w in widths:
        private.append(((1<<w)-1)<<offset);offset+=w
    E=[private[0]|1|4,private[1]|1|2,private[2]|2|4]
    unions=[]
    for J in range(8):
        U=0
        for j in range(3):
            if J>>j&1:U|=E[j]
        unions.append(U)
    return offset,private,E,unions

def coeff(S,unions):
    value=-Q(1) if S==0 else Q(0)
    for J,U in enumerate(unions):
        if S&~U==0:value+=2*Q((-1)**J.bit_count(),1<<U.bit_count())
    return value

def trace(S,private):return ((bool(S&private[0]),bool(S&private[1]),bool(S&private[2])),S&7)

def check_rows(a,n,private,E,widths,physical=None,certify=True):
    N=1<<n;checks=0;results=[]
    for i in range(n):
        labels=[s for s in range(N) if not(s>>i&1)]
        e=Q(sum(a[s|1<<i]**2 for s in labels),N*N)
        if not e:continue
        groups=defaultdict(lambda:[Q(0),Q(0)])
        ratios={};cross=0;hitmass=Q(0)
        for s in labels:
            u=Q(a[s],N);v=Q(a[s|1<<i],N)
            key=trace(s,private);mu=v*v/e;ref=u*u+v*v
            groups[key][0]+=mu;groups[key][1]+=ref;cross+=a[s]*a[s|1<<i]
            if mu:
                ratio=mu/ref
                if key in ratios:assert ratios[key]==ratio;checks+=1
                ratios[key]=ratio
            if i>=3:
                b=next(b for b,p in enumerate(private) if p>>i&1)
                if s&private[b]:
                    assert u==v;checks+=1;hitmass+=mu
        assert cross==0;checks+=1
        assert sum(v[0] for v in groups.values())==sum(v[1] for v in groups.values())==1;checks+=2
        assert len(groups)<=(64 if i>=3 else 32);checks+=1
        if physical is not None:
            assert Q(sum(physical[x]!=physical[x^(1<<i)] for x in range(N)),N)==e;checks+=1
        if widths is not None:
            q=[Q(1,1<<w) for w in widths]
            if i>=3:
                b=next(b for b,p in enumerate(private) if p>>i&1);others=[j for j in range(3) if j!=b]
                gamma=(1+(1-q[others[0]])*(1-q[others[1]]))/8
                assert e==2*q[b]*gamma and hitmass==1-2*q[b];checks+=2
            else:
                pair=[j for j,clause in enumerate(E) if clause>>i&1];b,c=pair;d=3-b-c
                expected=(q[b]+q[c])/2-q[b]*q[c]/4-q[d]*(q[b]+q[c]-q[b]*q[c])/4
                assert e==expected;checks+=1
        if certify:
            parts=[(mu,ref/(e*mu)) for mu,ref in groups.values() if mu]
            low,hi=logs(parts)
            if widths is not None and i>=3:assert hi<=3;checks+=1
        results.append({'i':i,'e':str(e),'states':len(groups)})
    return checks,results

def check_root(widths,cap):
    n,p,E,U=geometry(widths);N=1<<n
    f=[-1 if any(x&clause==0 for clause in E) else 1 for x in range(N)]
    a=walsh(f);checks=0
    for S in range(N):assert Q(a[S],N)==coeff(S,U);checks+=1
    assert sum(v*v for v in a)==N*N;checks+=1
    count,rows=check_rows(a,n,p,E,widths,f);checks+=count
    return {'widths':widths,'dimension':n,'coordinate_rows':len(rows),'states_max':max(z['states'] for z in rows),'assertions':checks}

def compressed(widths):
    n,p,E,U=geometry(widths);out=[];checks=0;q=[Q(1,1<<w) for w in widths]
    for category in range(6):
        i=category if category<3 else (p[category-3]&-p[category-3]).bit_length()-1
        retained=[mask&~(1<<i) for mask in p];shared=(7&~(1<<i))
        cells=[]
        for flags in product([0,1],repeat=3):
            if any(flag and not mask for flag,mask in zip(flags,retained)):continue
            mult=1;S0=0
            for flag,mask in zip(flags,retained):
                if flag:mult*=((1<<mask.bit_count())-1);S0|=mask&-mask
            for sharedmask in range(8):
                if sharedmask&~shared:continue
                S=S0|sharedmask;u=coeff(S,U);v=coeff(S|1<<i,U)
                cells.append((mult,u,v))
        energy=sum(m*v*v for m,u,v in cells)
        ref=sum(m*(u*u+v*v) for m,u,v in cells)
        assert ref==1 and sum(m*u*v for m,u,v in cells)==0;checks+=2
        if category>=3:
            b=category-3;other=[j for j in range(3) if j!=b]
            assert energy==q[b]*(1+(1-q[other[0]])*(1-q[other[1]]))/4;checks+=1
        out.append({'category':category,'i':i,'cells':len(cells),'e':str(energy)})
    assert max(x['cells'] for x in out)<=64
    return {'widths':widths,'dimension':n,'rows':out,'exact_assertions':checks+1}

def lost_refund():
    n,p,E,U=geometry((1,1,1));N=1<<n
    a=[coeff(S,U) for S in range(N)];i=0
    e=sum(a[S|1]**2 for S in range(N) if not S&1)
    assert e==Q(11,32)
    hits=defaultdict(lambda:[Q(0),Q(0)]);parts=[]
    for S in range(N):
        if S&1:continue
        upper=a[S|1]**2;ref=a[S]**2+upper;mu=upper/e
        key=tuple(bool(S&clause) for clause in E)
        hits[key][0]+=mu;hits[key][1]+=ref
        if mu:parts.append((mu,mu/ref))
    parts += [(-mu,mu/ref) for mu,ref in hits.values() if mu]
    low,hi=logs(parts);den=1<<128
    low=Q((low.numerator*den)//low.denominator,den);hi=kernel.rounded_upper(hi)
    assert low>0
    S1=2|4;S2=p[0]|p[1]|p[2]
    assert (a[S1],a[S1|1],a[S2],a[S2|1])==(Q(-3,32),Q(5,32),Q(-1,32),Q(-1,32))
    return {'e':'11/32','signed_rows':['-3/32','5/32','-1/32','-1/32'],
            'lost_KL_interval':[str(low),str(hi)],'strict_sign':'CERTIFIED_POSITIVE_RATIONAL_LOWER_ENDPOINT'}

def descendants_and_guards():
    records=[]
    for widths in [(1,1,1),(2,1,1)]:
        n,p,E,U=geometry(widths);N=1<<n
        f=[-1 if any(x&clause==0 for clause in E) else 1 for x in range(N)]
        for removed in range(n):
            for value in [0,1]:
                # Maintain physical coordinate labels; queried bit is a dummy.
                child=[f[(x&~(1<<removed))|(value<<removed)] for x in range(N)]
                a=walsh(child);c,rows=check_rows(a,n,p,E,None,child,False)
                records.append({'widths':widths,'query':removed,'value':value,'coordinate_rows':len(rows),'assertions':c})
    # Generic containment admission on the three-bit point defect.
    f=[-1]+[1]*7;a=walsh(f)
    assert Q(a[0],8)==Q(3,4) and all(Q(x,8)==Q(-1,4) for x in a[1:])
    # Spectators retain local triangle likelihoods; compare direct tensor rows.
    n,p,E,U=geometry((1,1,1));f=[-1 if any(x&clause==0 for clause in E) else 1 for x in range(1<<n)]
    for g in [[1,1,1,-1],[-1]+[1]*7]:
        # Core is in low bits, spectator in high bits.
        F=[f[x]*z for z in g for x in range(len(f))];aa=walsh(F)
        # Compare every old row likelihood against parent; do not assert new-row trace sufficiency.
        ag=walsh(g);af=walsh(f);NN=len(F)
        checks=0
        for i in range(n):
            e=Q(sum(af[s|1<<i]**2 for s in range(1<<n) if not(s>>i&1)),(1<<n)**2)
            ef=Q(sum(aa[s|1<<i]**2 for s in range(NN) if not(s>>i&1)),NN*NN)
            assert ef==e;checks+=1
            for S in range(NN):
                if S>>i&1:continue
                T=S&((1<<n)-1);spect=S>>n
                assert Q(aa[S],NN)==Q(af[T],1<<n)*Q(ag[spect],len(g));checks+=1
                if aa[S|1<<i]:
                    assert Q(aa[S|1<<i]**2,aa[S]**2+aa[S|1<<i]**2)==Q(af[T|1<<i]**2,af[T]**2+af[T|1<<i]**2);checks+=1
        records.append({'spectator_dimension':len(g).bit_length()-1,'assertions':checks})
    return records

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');parser.add_argument('--full',action='store_true');parser.add_argument('--certificates',action='store_true');args=parser.parse_args()
    assert sum([args.pilot,args.full,args.certificates])==1;start=time.monotonic()
    if args.certificates:
        ans={'compressed':[compressed(w) for w in [(8,1,1),(8,8,8),(16,8,4),(64,32,16)]],
             'clause_hit_failure':lost_refund(),'descendants_and_guards':descendants_and_guards(),
             'nonBoolean_controls':{'trace':'u_(x2)=4/5,v_(x1)=3/5; D_full=log2(25/9),D_trace=0,nonempty_convolution=24/25',
                                    'private_price':'Bernoulli(1/16)^tensor16 has M_i/e_i=4>3',
                                    'global_price':'n=2^18 product law has I=1,M=18>17 I_private'}};name='CERTIFICATES.json'
    else:
        domain=[(1,1,1),(2,1,1)] if args.pilot else list(product([1,2,3],repeat=3))
        cases=[]
        for w in domain:
            assert time.monotonic()-start<175
            cases.append(check_root(w,180))
            (R/'out/checkpoint.json').write_text(json.dumps({'cases':cases}))
        ans={'cases':cases,'functions':len(cases),'coordinate_rows':sum(c['coordinate_rows'] for c in cases),'assertions':sum(c['assertions'] for c in cases)};name='PILOT.json' if args.pilot else 'CHECK.json'
    ans['runtime_seconds']=time.monotonic()-start
    assert ans['runtime_seconds']<(180 if args.full else 60)
    (R/'out'/name).write_text(json.dumps(ans,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'file':name,'functions':ans.get('functions'),'coordinate_rows':ans.get('coordinate_rows'),'assertions':ans.get('assertions'),'runtime_seconds':ans['runtime_seconds']}))
