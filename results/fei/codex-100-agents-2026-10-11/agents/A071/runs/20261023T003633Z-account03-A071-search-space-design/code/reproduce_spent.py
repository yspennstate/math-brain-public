"""Independent direct character sums and product-law orthogonal moment transform."""
from continue_spent import *

@lru_cache(None)
def independent_core(t):
    a=[sum(F(y*(-1 if (s&x).bit_count()%2 else 1),len(t)) for x,y in enumerate(t)) for s in range(len(t))]
    ps=[z*z for z in a];ck(sum(ps)==1)
    I=sum(F(s.bit_count())*p for s,p in enumerate(ps))
    ck(I==sum(F(sum(t[x]!=t[x^2**i] for x in range(len(t))),len(t)) for i in range((len(t)-1).bit_length())))
    return a[0],ent(ps),I

@lru_cache(None)
def independent(ts):
    data=[independent_core(t) for t in ts];mus=[d[0] for d in data];vs=[1-m*m for m in mus]
    J=tuple(-H[x^1] for x in range(64));a=list(map(F,J))
    # Each 2x2 tensor maps a function to its unnormalized centered moments.
    for j,m in enumerate(mus):
        pp=(1+m)/2;pm=(1-m)/2
        for x in range(64):
            if x>>j&1:continue
            u,v=a[x],a[x|1<<j]
            a[x]=pp*u+pm*v
            a[x|1<<j]=pp*(1-m)*u+pm*(-1-m)*v
    masses=[]
    for T,z in enumerate(a):
        v=F(1)
        for j in range(6):
            if T>>j&1:v*=vs[j]
        if v==0:ck(z==0);masses.append(F(0))
        else:masses.append(z*z/v)
    ck(sum(masses)==1)
    h=ent(masses);I=F(0)
    for j,(m,hg,ig) in enumerate(data):
        if vs[j]==0:ck(ig==0);continue
        q=sum(masses[T] for T in range(64) if T>>j&1)/vs[j]
        h=plus(h,scale(sub(hg,ent([vs[j],1-vs[j]])),q));I+=q*ig
    return h,I,sub(const(4*I),h)

def main():
    start=time.perf_counter();root,first,second,third,debits,D,e1,e2,e3=setup()
    nodes=[root,*first,*second,*third]
    def compare(p):
        h,I,s=independent(p['ts']);ck(I==p['I']);overlaps(h,p['H']);overlaps(s,p['S'])
        return h,I,s
    for p in nodes:compare(p)
    saved=json.loads((ROOT/'out/CONTINUATION_CASES.json').read_text(encoding='utf-8'))
    rows=[]
    for r in saved:
        b,j,i=r['terminal'],r['block'],r['coordinate'];p=third[b];cs,e,d=split(p,j,i)
        vals=[compare(c) for c in cs];hp,ip,sp=compare(p)
        ei=sub(sub(hp,avg([x[0] for x in vals])),const(4*d));overlaps(ei,r['e'])
        # Original selected debit has already exhausted terminal0's full bank.
        # For terminal1 its debit is 2tau; it is never replaced by full M.
        T=plus(debits[b],ei);B=avg([x[2] for x in vals]);overlaps(T,r['required_T'])
        ck(all(s[2][0]>0 for s in vals));ck(T[0]>0)
        if b==1:ck(sub(B,T)[0]>0)
        V=avg([c['V'] for c in r['children']]);need=sub(T,V)
        rows.append(dict(terminal=b,block=j,coordinate=i,selected_only_shortfall=need,
                         full_children=[v[2] for v in vals],mean_remaining=sub(B,T)))
        ck(time.perf_counter()-start<55)
    result=dict(version='A071-direct-product-moment-reproduction-v1',cases=len(rows),
      independent_states=independent.cache_info().currsize,engine_checks=engine.tests,
      runtime_seconds=time.perf_counter()-start,
      selected_only_failure_cases=sum(r['selected_only_shortfall'][0]>0 for r in rows),
      cases_detail=rows)
    (ROOT/'out/REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases_detail'}))

if __name__=='__main__':main()
