import argparse,json,time
from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
import importlib.util
R=Path(__file__).resolve().parents[1]
old=R.parents[0]/'20261013T215020Z-account05-A031-convolution-identity/code/check_carrier.py'
spec=importlib.util.spec_from_file_location('old_exact_kernel',old);kernel=importlib.util.module_from_spec(spec);spec.loader.exec_module(kernel)
walsh=kernel.walsh;logs=kernel.logs

def tribes(w,t):
    n=w*t;mask=(1<<w)-1
    return [1 if all(((x>>(b*w))&mask)!=0 for b in range(t)) else -1 for x in range(1<<n)]

def row(a,i):
    N=len(a);n=N.bit_length()-1
    labels=[s for s in range(N) if not(s>>i&1)]
    e=Q(sum(a[s|1<<i]**2 for s in labels),N*N)
    return e,{s:Q(a[s|1<<i]**2,N*N)/e for s in labels},{s:Q(a[s]**2+a[s|1<<i]**2,N*N) for s in labels}

def check_table(w,t):
    f=tribes(w,t);N=len(f);n=w*t;a=walsh(f);q=Q(1,1<<w);s=1-q;c=2*s**t-1;e=2*q*s**(t-1)
    asserts=0
    assert Q(a[0],N)==c;asserts+=1
    for label in range(1,N):
        j=sum(bool(label&(((1<<w)-1)<<(b*w))) for b in range(t))
        assert Q(a[label],N)==2*(-q)**j*s**(t-j);asserts+=1
    assert sum(x*x for x in a)==N*N;asserts+=1
    for i in range(n):
        ee,mu,r=row(a,i);assert ee==e
        assert sum(mu.values())==sum(r.values())==1
        assert Q(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N)==e;asserts+=3
        own=(((1<<w)-1)<<((i//w)*w))^(1<<i)
        mc=[Q(0)]*3;rc=[Q(0)]*3;ratios={}
        cross=0
        for label in mu:
            z=0 if label==0 else 2 if label&own else 1
            mc[z]+=mu[label];rc[z]+=r[label]
            cross+=a[label]*a[label|(1<<i)]
            if mu[label]:
                ratio=mu[label]/r[label]
                if z in ratios:assert ratios[z]==ratio;asserts+=1
                ratios[z]=ratio
        assert cross==0;asserts+=1  # signed mixed Parseval before grouped squares
        expected_m=[e,2*q-e,1-2*q]
        expected_r=[c*c+e*e,e*(2*q-e)*(s*s+q*q)/(q*q),2*e*(1-2*q)]
        assert mc==expected_m and rc==expected_r;asserts+=2
        for z in ratios:assert ratios[z]==mc[z]/rc[z];asserts+=1
    return {'w':w,'blocks':t,'dimension':n,'coordinate_rows':n,'assertions':asserts}

def formulas():
    records=[]
    for w in [4,5,6,7,8]:
        t=1<<w;q=Q(1,t);s=1-q;e=2*q*s**(t-1);c=2*s**t-1
        mu=[e,2*q-e,1-2*q];r=[c*c+e*e,e*(2*q-e)*(s*s+q*q)/(q*q),2*e*(1-2*q)]
        assert sum(mu)==sum(r)==1 and e<=q
        parts=[(e,(c*c+e*e)/(e*e)),(2*q-e,(s*s+q*q)/(q*q)),(1-2*q,Q(2))]
        lo,hi=logs(parts)
        upper=kernel.rounded_upper(hi)
        assert upper<=1+6*w*q<=Q(5,2)
        records.append({'w':w,'blocks':t,'M_over_I_lower_outward':str(Q((lo.numerator*(1<<128))//lo.denominator,1<<128)),
                        'M_over_I_upper_outward':str(upper),'analytic_upper':str(1+6*w*q)})
    return records

def activation():
    seeds=[('dictator',[1,-1]),('point3',[1]+[-1]*7),('bent2',[1,1,1,-1]),('tribes22',tribes(2,2))]
    records=[]
    for name,g in seeds:
        ng=len(g).bit_length()-1;ag=walsh(g)
        for k in [1,2]:
            core_n=ng+2;n=core_n+k;coremask=(1<<core_n)-1
            F=[]
            for x in range(1<<n):
                z=(x>>ng)&3;h=g[x&((1<<ng)-1)]*(-1 if z.bit_count()%2 else 1)
                F.append(h if x>>core_n==0 else 1)
            a=walsh(F);q=Q(1,1<<k);checks=0
            for i in range(ng):
                eg,mg,rg=row(ag,i)
                if not eg:continue
                ef,mf,rf=row(a,i);assert ef==q*eg;checks+=1
                assert sum(m for lab,m in mf.items() if lab&coremask)==1
                assert sum(r for lab,r in rf.items() if lab&coremask)==q;checks+=2
                for lab,m in mf.items():
                    if m:
                        oldlab=lab&((1<<ng)-1)
                        assert m/rf[lab]==(mg[oldlab]/rg[oldlab])/q;checks+=1
            records.append({'seed':name,'k':k,'dimension':n,'assertions':checks})
    return records

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');p.add_argument('--full',action='store_true');p.add_argument('--formula',action='store_true');args=p.parse_args()
    assert sum([args.pilot,args.full,args.formula])==1
    start=time.monotonic()
    if args.formula:
        ans={'balanced':formulas(),'activation':activation(),'nonBoolean':{'n':64,'theta':'1/64','M_over_I':'6','Boolean_bound':'5/2','signed_shift_nonzero':'2 sqrt(63)/64'}};name='CERTIFICATES.json'
    else:
        pairs=[(1,1),(2,2),(3,2)] if args.pilot else [(1,1),(2,2),(3,2),(1,3),(2,3),(3,3),(4,2),(4,3)]
        rows=[check_table(w,t) for w,t in pairs]
        ans={'tables':rows,'cases':len(rows),'coordinate_rows':sum(x['coordinate_rows'] for x in rows),'assertions':sum(x['assertions'] for x in rows)};name='PILOT.json' if args.pilot else 'CHECK.json'
    ans['runtime_seconds']=time.monotonic()-start
    assert ans['runtime_seconds']<(120 if args.full else 60)
    (R/'out'/name).write_text(json.dumps(ans,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'file':name,'cases':ans.get('cases'),'rows':ans.get('coordinate_rows'),'assertions':ans.get('assertions'),'runtime_seconds':ans['runtime_seconds']}))
