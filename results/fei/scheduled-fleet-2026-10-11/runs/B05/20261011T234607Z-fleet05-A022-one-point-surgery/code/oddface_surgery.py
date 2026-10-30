from pathlib import Path
from fractions import Fraction as Q
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import combinations
import json,math,time,sys
RUN=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ['pilot','full']
START=time.perf_counter(); LIMIT=60 if MODE=='pilot' else 1800
ASSERTIONS=0; SIGN_COUNTS=Counter(); SCALE=1<<80
def ck(x):
    global ASSERTIONS
    assert x
    ASSERTIONS+=1
def guard():
    if time.perf_counter()-START>LIMIT:raise TimeoutError('frozen runtime cap')
def fwht(f):
    w=list(f);step=1
    while step<len(w):
        for i in range(0,len(w),2*step):
            for j in range(i,i+step):
                a,b=w[j],w[j+step];w[j]=a+b;w[j+step]=a-b
        step*=2
    return w
def ln_unit(y):
    z=(y-1)/(y+1);power=z;total=Q(0)
    for j in range(50):total+=2*power/(2*j+1);power*=z*z
    return total,total+2*power/(101*(1-z*z))
LN2=ln_unit(Q(2));LOG_E=(1/LN2[1],1/LN2[0])
@lru_cache(maxsize=16384)
def factors(x):
    ans=[];p=2
    while p*p<=x:
        power=0
        while x%p==0:x//=p;power+=1
        if power:ans.append((p,power))
        p=3 if p==2 else p+2
    if x>1:ans.append((x,1))
    return tuple(ans)
@lru_cache(maxsize=8192)
def prime_log(p):
    if p==2:return SCALE,SCALE
    k=p.bit_length()-1;y=Q(p,1<<k);lo,hi=ln_unit(y)
    lo=lo/LN2[1]+k;hi=hi/LN2[0]+k
    low=(lo*SCALE).numerator//(lo*SCALE).denominator
    high=-((-hi*SCALE).numerator//(-hi*SCALE).denominator)
    return low,high
PRIME_RECEIPTS={}
def expr_interval(expr):
    low=high=0
    for p,c in expr:
        a,b=prime_log(p);PRIME_RECEIPTS[p]=[a,b]
        if c>=0:low+=c*a;high+=c*b
        else:low+=c*b;high+=c*a
    return low,high
@lru_cache(maxsize=8192)
def sign_expr(expr):
    if not expr:SIGN_COUNTS['exact_zero']+=1;return 0
    low,high=expr_interval(expr)
    if low>0:SIGN_COUNTS['interval_positive']+=1;return 1
    if high<0:SIGN_COUNTS['interval_negative']+=1;return -1
    guard()
    num=den=1
    for p,c in expr:
        if c>0:num*=pow(p,c)
        elif c<0:den*=pow(p,-c)
    SIGN_COUNTS['exact_product_fallback']+=1
    return (num>den)-(num<den)
def canonical(c):return tuple(sorted((p,v) for p,v in c.items() if v))
def packet_expr(f):
    N=len(f);w=fwht(f);expr=Counter();influence_num=0
    ck(sum(a*a for a in w)==N*N)
    for S in range(0,N,2):
        a=w[S]**2;b=w[S+1]**2;q=a+b
        influence_num+=b
        for x,c in [(q,q),(a,-a),(b,-b)]:
            if x:
                for p,e in factors(x):expr[p]+=c*e
    return canonical(expr),influence_num
def edgecount(f):
    n=(len(f)-1).bit_length()
    return sum(f[x]!=f[x^(1<<j)] for x in range(len(f)) for j in range(n) if (x>>j)&1==0)
def direct_odd(f):
    n=(len(f)-1).bit_length()
    return sum(f[x]*f[x^(1<<i)]*f[x^(1<<j)]*f[x^(1<<i)^(1<<j)]==-1
        for i in range(n) for j in range(i+1,n) for x in range(len(f)) if x&(1<<i)==0 and x&(1<<j)==0)
@lru_cache(maxsize=4096)
def ledger(f):
    N=len(f)
    if min(f)==max(f):return (0,0,0,0,0)
    guard()
    g=f[0::2];h=f[1::2];M=N//2
    mismatch=sum(a!=b for a,b in zip(g,h))
    expr,inf_num=packet_expr(f)
    ck(inf_num==mismatch*2*N)
    test=Counter(dict(expr));test[2]-=4*inf_num
    bad=sign_expr(canonical(test))>0
    product=tuple(a*b for a,b in zip(g,h));boundary=edgecount(product)
    left=ledger(g);right=ledger(h)
    # All numerators are over the local cube size N; the child 1/2 cancels normalization.
    I_num=2*mismatch+left[0]+right[0]
    Q_num=2*boundary+left[1]+right[1]
    bad_num=(2*boundary if bad else 0)+left[2]+right[2]
    n_bad=int(bad)+left[3]+right[3]
    n_nodes=1+left[4]+right[4]
    ck(0<=bad_num<=Q_num)
    return I_num,Q_num,bad_num,n_bad,n_nodes
def bent(x):return -1 if ((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))%2 else 1
def orders(r):
    y=4+r;data=list(range(4));ctrl=list(range(4,4+r))
    return {'selector_first':[y]+ctrl+data,'control_first':ctrl+[y]+data,
        'data_first':data+ctrl+[y],'control_data_selector':ctrl+data+[y]}
@lru_cache(maxsize=12)
def mapping(r,name):
    od=orders(r)[name]
    return tuple(sum(((x>>i)&1)<<bit for i,bit in enumerate(od)) for x in range(1<<len(od)))
def table(D,r,name):
    mask=sum(1<<v for v in D);ans=[]
    for full in mapping(r,name):
        x=full&15;z=(full>>4)&((1<<r)-1);y=(full>>(4+r))&1
        ans.append(1 if z else bent(x)*(-1 if y and ((mask>>x)&1) else 1))
    return tuple(ans)
def root_certificate(D,r):
    # In selector-first layout the root query is the selector.
    f=table(D,r,'selector_first');N=len(f);expr,inf_num=packet_expr(f)
    low,high=expr_interval(expr);B=(Q(low,SCALE*N*N),Q(high,SCALE*N*N))
    residual_N=N//2;mu=Q(len(D),residual_N)
    internal=sum(1 for v in D for i in range(4) if v<(v^(1<<i)) and (v^(1<<i)) in D)
    boundary=(4+r)*len(D)-2*internal;credit=Q(boundary,residual_N)
    ck(boundary==edgecount(tuple(a*b for a,b in zip(f[::2],f[1::2]))))
    gap=(credit+mu*LOG_E[0]-B[1],credit+mu*LOG_E[1]-B[0])
    ck(gap[0]>=0)
    test=Counter(dict(expr));test[2]-=4*inf_num
    return {'mu':str(mu),'boundary_credit':str(credit),'internal_edges':internal,
        'B_interval':[str(v) for v in B],'gap_interval':[str(v) for v in gap],
        'B_prime_expression':list(expr),'B_denominator':N*N,'root_bad':sign_expr(canonical(test))>0}

maxima={};worst_min={};total_patterns=total_trees=0
rr=[0,2] if MODE=='pilot' else [0,2,4]
ss=[1,2] if MODE=='pilot' else [1,2,3,4]
for r in rr:
    output=RUN/'out'/f'{MODE}_r{r}_patterns.jsonl'
    with output.open('w',encoding='utf-8') as fp:
        for s in ss:
            for D in combinations(range(16),s):
                row={'data_bits':4,'r':r,'D':list(D),'size':s,'root':root_certificate(D,r),'orders':{}}
                ratios=[]
                for name in orders(r):
                    f=table(D,r,name);I_num,Q_num,bad_num,n_bad,n_nodes=ledger(f)
                    ratio=Q(bad_num,I_num) if I_num else Q(0)
                    row['orders'][name]={'I':str(Q(I_num,len(f))),'Q':str(Q(Q_num,len(f))),
                        'bad_credit':str(Q(bad_num,len(f))),'bad_credit_over_I':str(ratio),'n_bad':n_bad,'n_live_nodes':n_nodes}
                    ratios.append(ratio);key=f'r={r},s={s},order={name}'
                    item=maxima.get(key)
                    if item is None or ratio>Q(item['ratio']):
                        maxima[key]={'ratio':str(ratio),'D':list(D),'ties':1,'row':row['orders'][name]}
                    elif ratio==Q(item['ratio']):item['ties']+=1
                    total_trees+=1
                key=f'r={r},s={s}';val=min(ratios);item=worst_min.get(key)
                if item is None or val>Q(item['ratio']):worst_min[key]={'ratio':str(val),'D':list(D),'ties':1,'orders':row['orders']}
                elif val==Q(item['ratio']):item['ties']+=1
                ck(len({v['I'] for v in row['orders'].values()})==1)
                ck(len({v['Q'] for v in row['orders'].values()})==1)
                # Independent full edge/face reconstruction on first and last patterns per size.
                if D==tuple(range(s)) or D==tuple(range(16-s,16)):
                    f=table(D,r,'selector_first');vals=ledger(f)
                    ck(vals[0]==2*edgecount(f));ck(vals[1]==2*direct_odd(f))
                fp.write(json.dumps(row,separators=(',',':'))+'\n');fp.flush()
                total_patterns+=1
                if total_patterns%200==0:
                    (RUN/'out'/f'{MODE}_CHECKPOINT.json').write_text(json.dumps({'patterns':total_patterns,'elapsed_seconds':time.perf_counter()-START,'maxima':maxima,'worst_min':worst_min},indent=2))
                    print(f'{MODE}: {total_patterns} patterns, {time.perf_counter()-START:.3f}s',flush=True)
                guard()
out={'helper_version':'A022-oddface-surgery-v2','mode':MODE,'patterns':total_patterns,'tree_ledgers':total_trees,
    'assertions_passed':ASSERTIONS,'sign_methods':dict(SIGN_COUNTS),'elapsed_seconds':time.perf_counter()-START,
    'maxima_per_order':maxima,'maxima_after_min_four_orders':worst_min,
    'log_scale':str(SCALE),'prime_log_intervals':{str(p):[str(a),str(b)] for p,(a,b) in PRIME_RECEIPTS.items()},
    'ln2_interval':[str(v) for v in LN2],'cache_info':str(ledger.cache_info()),'full_fei':'OPEN'}
(RUN/'out'/f'{MODE}_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['maxima_per_order','maxima_after_min_four_orders','prime_log_intervals','ln2_interval']},indent=2))
