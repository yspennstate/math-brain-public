"""Exact local-hull admission capital; no floating-point decisions."""
from arithmetic import F,Q,log2,ceildiv,ROOT
from functools import lru_cache
from itertools import product
import json,time,sys

CHECKS=0
def ck(b):
    global CHECKS
    assert b
    CHECKS+=1
def add(*ps):
    d={}
    for p in ps:
        for k,v in p.items():d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def scale(p,r):return {k:v*r for k,v in p.items() if v*r}
def sub(a,b):return add(a,scale(b,-1))
def mean(ps):return scale(add(*ps),F(1,len(ps)))
def factor(n):
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def entropy(ps):
    out={}
    for p in ps:
        if not p:continue
        for k,v in factor(p.numerator).items():out=add(out,{k:-p*v})
        for k,v in factor(p.denominator).items():out=add(out,{k:p*v})
    return out
@lru_cache(None)
def logp(k):return log2(F(k))
def interval(p):
    lo=hi=0
    for k,v in p.items():
        a,b=logp(k)
        if v<0:a,b=b,a
        lo+=a*v.numerator//v.denominator
        hi+=ceildiv(b*v.numerator,v.denominator)
    return lo,hi
def compare(a,b):
    d=sub(a,b)
    if not d:return 0
    lo,hi=interval(d)
    if lo>0:return 1
    if hi<0:return -1
    raise ArithmeticError('unresolved exact comparison')
def maximum(rows):
    ans=rows[0]
    for row in rows[1:]:
        if compare(row[1],ans[1])>0:ans=row
    return ans
def packed(p):return {str(k):str(v) for k,v in sorted(p.items())}
def record(p):return {'prime_log':packed(p),'bounds_2pow192':interval(p)}
def save(name,v):
    (ROOT/'out'/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')

@lru_cache(None)
def spectrum(t):
    N=len(t);n=N.bit_length()-1;W=list(t);h=1
    while h<N:
        for j in range(0,N,2*h):
            for k in range(j,j+h):a,b=W[k],W[k+h];W[k],W[k+h]=a+b,a-b
        h*=2
    ck(sum(w*w for w in W)==N*N)
    for x in range(N):
        ck(sum(w*(-1 if (x&s).bit_count()%2 else 1) for s,w in enumerate(W))==N*t[x])
    ds=[];edges=[]
    for i in range(n):
        e=sum(t[x]!=t[x|1<<i] for x in range(N) if not x>>i&1)
        d=F(2*e,N);ck(d==sum(F(w*w,N*N) for s,w in enumerate(W) if s>>i&1))
        ds.append(d);edges.append(e)
    # No entropy is constructed until all integer checks above pass.
    H=entropy([F(w*w,N*N) for w in W]);I=sum(ds,F(0))
    return {'W':W,'H':H,'I':I,'S':sub({2:I},H),'edges':edges}

def engine(t):
    n=len(t).bit_length()-1;ALL=(1<<n)-1
    @lru_cache(None)
    def state(p):
        free=[i for i,b in enumerate(p) if b<0];fix=sum((b==1)<<i for i,b in enumerate(p))
        tt=tuple(t[fix|sum((x>>j&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free)))
        z=spectrum(tt);return dict(z,truth=tt,free=free,need=maximum([('zero',{}),('stop',scale(z['S'],-1))])[1])
    def children(p,i):return tuple(p[:i]+(b,)+p[i+1:] for b in [0,1])
    @lru_cache(None)
    def hull(p,M):
        z=state(p);choices=[('stop',z['need'])]
        for i in z['free']:
            if M>>i&1:choices.append((i,mean([hull(c,M) for c in children(p,i)])))
        return maximum(choices)[1]
    @lru_cache(None)
    def capital(p,M):
        z=state(p);rows=[(('stop',),z['need'])]
        for i in z['free']:
            if M>>i&1:
                cs=children(p,i);rs=[hull(c,M) for c in cs];r=mean(rs)
                for b,c in enumerate(cs):rows.append((('query',i,b),sub(capital(c,M)[1],sub(rs[b],r))))
            else:rows.append((('admit',i),capital(p,M|1<<i)[1]))
        return maximum(rows)
    root=(-1,)*n
    return dict(root=root,ALL=ALL,state=state,children=children,hull=hull,capital=capital)

def audit_witness(t):
    e=engine(t);p=e['root'];M=0;R=e['hull'](p,e['ALL']);T=e['capital'](p,M)[1]
    # Independent forward enumeration of all admission/query/stop paths.
    payoffs=[];count=0
    def walk(p,M,offset,path):
        nonlocal count
        count+=1;z=e['state'](p);payoffs.append((path,sub(z['need'],offset)))
        for i in z['free']:
            if M>>i&1:
                cs=e['children'](p,i);rs=[e['hull'](c,M) for c in cs];r=mean(rs)
                for b,c in enumerate(cs):walk(c,M,add(offset,sub(rs[b],r)),path+[('query',i,b)])
            else:walk(p,M|1<<i,offset,path+[('admit',i)])
    walk(p,0,{},[])
    path,required=maximum(payoffs);ck(required==T)
    # Full-mask initialization needs exactly its own hull: no admission damage.
    ck(e['capital'](p,e['ALL'])[1]==R)
    rows=[];credit=R;mask=0
    for action in path:
        z=e['state'](p);before=credit
        if action[0]=='admit':mask|=1<<action[1];delta={}
        else:
            _,i,b=action;cs=e['children'](p,i);rs=[e['hull'](c,mask) for c in cs]
            delta=sub(rs[b],mean(rs));credit=add(credit,delta);p=cs[b]
        rows.append({'action':action,'credit_before':record(before),'delta':record(delta),'credit_after':record(credit),'state_after':list(p),'mask_after':mask})
    shortage=sub(e['state'](p)['need'],credit);ck(compare(shortage,{})>0);ck(shortage==sub(T,R))
    sp=spectrum(t)
    return {'truth':t,'integer_Walsh':sp['W'],'edge_counts':sp['edges'],'I':str(sp['I']),'H':record(sp['H']),'S':record(sp['S']),'full_hull':record(R),'robust_capital':record(T),'extra_capital':record(sub(T,R)),'attaining_path':rows,'terminal_need':record(e['state'](p)['need']),'terminal_shortage':record(shortage),'forward_path_nodes':count,'forward_stopping_payoffs':len(payoffs)}

def main():
    start=time.perf_counter()
    if '--constructed' in sys.argv:
        t=tuple((-1 if (x>>1).bit_count()%2 else 1)*(-1 if x==0 else 1) for x in range(16))
        w=audit_witness(t);w['checks']=CHECKS;w['runtime_seconds']=time.perf_counter()-start
        save('CONSTRUCTED_WITNESS.json',w)
        print(json.dumps({'constructed':'PASS','extra_capital':w['extra_capital'],'checks':CHECKS,'runtime_seconds':w['runtime_seconds']}));return
    n=2 if '--pilot' in sys.argv else 3;cases=[];witness=None
    for code in range(1<<(1<<n)):
        ck(time.perf_counter()-start<(60 if n==2 else 180))
        t=tuple(-1 if code>>x&1 else 1 for x in range(1<<n));e=engine(t);p=e['root']
        R=e['hull'](p,e['ALL']);T=e['capital'](p,0)[1];c=compare(T,R);ck(c>=0)
        cases.append({'truth_code_negative_bits':code,'full_hull':packed(R),'robust_capital':packed(T),'verdict':'STRICT' if c else 'EQUAL'})
        if c and witness is None:
            witness=audit_witness(t);witness['truth_code_negative_bits']=code
            save('PILOT_WITNESS.json' if n==2 else 'WITNESS.json',witness)
        e['hull'].cache_clear();e['capital'].cache_clear();e['state'].cache_clear()
    result={'n':n,'rate':1,'case_count':len(cases),'strict':sum(z['verdict']=='STRICT' for z in cases),'checks':CHECKS,'spectrum_cache':spectrum.cache_info()._asdict(),'runtime_seconds':time.perf_counter()-start,'cases':cases}
    save('PILOT.json' if n==2 else 'EXHAUSTIVE.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
if __name__=='__main__':main()
