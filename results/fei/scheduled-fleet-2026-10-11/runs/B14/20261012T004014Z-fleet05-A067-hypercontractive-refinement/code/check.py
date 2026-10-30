import argparse,json,time
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
ASSERTIONS=0
LOGCACHE={}
STATS={}

def check(test):
    global ASSERTIONS
    assert test
    ASSERTIONS+=1
    if time.perf_counter()-START>60:
        raise RuntimeError('Frozen 60-second job limit')

def ln_interval(x,terms=20):
    z=(x-1)/(x+1)
    check(0<=z<=Q(1,3))
    zz=z*z
    power=z
    acc=Q(0)
    for j in range(terms):
        acc+=2*power/(2*j+1)
        power*=zz
    tail=2*power/((2*terms+1)*(1-zz))
    return acc,acc+tail

LN2=ln_interval(Q(2))
def log2_interval(x):
    if x in LOGCACHE:
        return LOGCACHE[x]
    check(x>0)
    exponent=x.numerator.bit_length()-x.denominator.bit_length()
    u=x/(Q(2)**exponent)
    while u<1:
        exponent-=1;u*=2
    while u>=2:
        exponent+=1;u/=2
    lo,hi=ln_interval(u)
    # u>=1 means its logarithm is nonnegative; signed exponent is added after division.
    result=(exponent+lo/LN2[1],exponent+hi/LN2[0])
    LOGCACHE[x]=result
    return result

def eta(q):
    if not q:
        return Q(0),Q(0)
    lo,hi=log2_interval(q)
    return -q*hi,-q*lo

def add(*xs):
    return sum(x[0] for x in xs),sum(x[1] for x in xs)
def scale(x,c):
    return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def phi(x):
    return eta(x*x)
def fwht(values):
    a=list(values);step=1
    while step<len(a):
        for base in range(0,len(a),2*step):
            for j in range(base,base+step):
                u,v=a[j],a[j+step]
                a[j],a[j+step]=u+v,u-v
        step*=2
    return a
def info(values):
    key=tuple(values)
    if key in STATS:
        return STATS[key]
    size=len(values);n=size.bit_length()-1
    a=fwht(values)
    check(sum(x*x for x in a)==size*size)
    d=[s.bit_count() if v else -1 for s,v in enumerate(a)]
    for i in range(n):
        bit=1<<i
        for s in range(size):
            if not s&bit:
                d[s]=max(d[s],d[s|bit])
    influence=Q(sum(s.bit_count()*v*v for s,v in enumerate(a)),size*size)
    u=Q(sum(v*v*(d[s]-s.bit_count()) for s,v in enumerate(a) if s and v),size*size)
    physical=Q(sum(values[x]!=values[x^(1<<i)] for x in range(size) for i in range(n)),size)
    check(influence==physical)
    counts=Counter(v*v for v in a if v)
    entropy=add(*(scale(eta(Q(v,size*size)),c) for v,c in counts.items()))
    result={'a':a,'n':n,'I':influence,'U':u,'H':entropy}
    STATS[key]=result
    return result
def children(values,i):
    mask=(1<<i)-1
    return [[values[(x&mask)|((x&~mask)<<1)|(b<<i)] for x in range(len(values)//2)] for b in [0,1]]

def tree(values,labels,padding_labels):
    root=info(values)
    if root['U']<=root['I']:
        return {'QH':(Q(0),Q(0)),'QI':Q(0),'leafH':root['H'],'leafI':root['I'],'nodes':0,'max_ratio':(Q(0),Q(0)),'leaf_predicate':True}
    relevant=[i for i in range(root['n']) if any(v and s&(1<<i) for s,v in enumerate(root['a']))]
    check(bool(relevant))
    i=next((i for i in relevant if labels[i] in padding_labels),relevant[0])
    cs=children(values,i)
    ci=[info(x) for x in cs]
    edge=Q(sum(values[x]!=values[x^(1<<i)] for x in range(len(values))),len(values))
    check(edge>0)
    delta=add(root['H'],scale(ci[0]['H'],-Q(1,2)),scale(ci[1]['H'],-Q(1,2)))
    check(delta[1]>=0)
    check(root['I']==edge+(ci[0]['I']+ci[1]['I'])/2)
    rest=labels[:i]+labels[i+1:]
    sub=[tree(x,rest,padding_labels) for x in cs]
    qh=add(delta,scale(sub[0]['QH'],Q(1,2)),scale(sub[1]['QH'],Q(1,2)))
    qi=edge+(sub[0]['QI']+sub[1]['QI'])/2
    leafh=scale(add(sub[0]['leafH'],sub[1]['leafH']),Q(1,2))
    leafi=(sub[0]['leafI']+sub[1]['leafI'])/2
    check(root['I']==qi+leafi)
    total=add(qh,leafh)
    check(total[0]<=root['H'][1] and total[1]>=root['H'][0])
    ratio=scale(delta,1/edge)
    maxratio=max([ratio]+[s['max_ratio'] for s in sub],key=lambda x:x[1])
    return {'QH':qh,'QI':qi,'leafH':leafh,'leafI':leafi,'nodes':1+sum(s['nodes'] for s in sub),'max_ratio':maxratio,'leaf_predicate':all(s['leaf_predicate'] for s in sub)}

def encode(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items() if k!='a'}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def seed(kind):
    if kind=='dictator':return [1,-1],1
    if kind=='and2':return [-1]+[1]*3,2
    if kind=='maj3':return [1 if x.bit_count()<=1 else -1 for x in range(8)],3
    if kind=='address2':
        return [(-1 if x&(1<<(2+(x&3))) else 1) for x in range(64)],6
    raise ValueError(kind)

def padding_node(values,m,r):
    parent=[values[x&((1<<m)-1)] for x in range(1<<(m+r))]
    parent[0]*=-1
    ps=info(parent)
    cs=children(parent,m)
    child=[info(c) for c in cs]
    d=Q(1,1<<(m+r-1))
    delta=add(ps['H'],scale(child[0]['H'],-Q(1,2)),scale(child[1]['H'],-Q(1,2)))
    a=info(values)['a'];s=values[0];p=Q(1,1<<(m+r));t=2*p
    formula=(8*p*(1+Q(m+r-3,1<<r)),)*2
    for aa in a:
        b=Q(s*aa,1<<m)
        formula=add(formula,phi(b-t),scale(phi(b),-Q(1,2)),scale(phi(b-2*t),-Q(1,2)))
    check(delta[0]<=formula[1] and formula[0]<=delta[1])
    # Exact coefficient and influence ledgers validate the analytic formula's ingredients.
    check(ps['I']==d+(child[0]['I']+child[1]['I'])/2)
    edited_base=list(values);edited_base[0]*=-1
    edited_seed=info(edited_base)
    original=info(values)
    delta_pad=Q(1,1<<r)
    full_drop=add(ps['H'],scale(original['H'],-(1-delta_pad)),scale(edited_seed['H'],-delta_pad))
    core=ps['I']-r*d
    check(core==(1-delta_pad)*original['I']+delta_pad*edited_seed['I'])
    check(core>=m*d)
    reserve_upper=1+6/LN2[0]
    check(full_drop[1]<=4*r*d+reserve_upper*core)
    return {'family':'fixed_seed','m':m,'r':r,'ratio':scale(delta,1/d),'formula':formula,'full_padding_drop':full_drop,'queried_influence':r*d,'retained_core_influence':core,'reserve_bound':4*r*d+reserve_upper*core}

def run(mode):
    rows=[]
    for n in ([2,3] if mode=='pilot' else range(2,11)):
        values=[(1 if not x&1 else -1)*(-1 if x==0 else 1) for x in range(1<<n)]
        result=tree(values,list(range(n)),set(range(1,n)))
        check(result['max_ratio'][1]<=5)
        check(result['QI']==Q(n-2,1<<(n-1)))
        check(result['leafI']==1)
        rows.append({'family':'dictator_surgery','n':n,'tree':result})
    for n in ([1,3] if mode=='pilot' else range(1,9)):
        values=[(1 if (x&7).bit_count()<=1 else -1)*(-1 if (x>>3)==0 else 1) for x in range(1<<(n+3))]
        result=tree(values,list(range(n+3)),set(range(3,n+3)))
        check(result['max_ratio'][1]<=5)
        if n>=2:
            check(result['QI']==Q(n-2,1<<(n-1)))
            check(result['leafI']==Q(3,2)+Q(1,1<<(n-2)))
        rows.append({'family':'majority_tensor_defect','n':n,'tree':result})
    for blocks in ([2] if mode=='pilot' else [2,3]):
        m=2*blocks
        base=[-1 if any(((x>>(2*j))&3)==0 for j in range(blocks)) else 1 for x in range(1<<m)]
        for r in ([2] if mode=='pilot' else range(2,6)):
            edited=[base[x&((1<<m)-1)] for x in range(1<<(m+r))]
            edited[0]*=-1
            result=tree(edited,list(range(m+r)),set(range(m,m+r)))
            check(result['leaf_predicate'])
            rows.append({'family':'edited_tribes','blocks':blocks,'r':r,'tree':result})
    for kind in ['dictator','and2','maj3','address2']:
        base,m=seed(kind)
        for r in ([2] if mode=='pilot' else range(2,7)):
            result=padding_node(base,m,r)
            result['family']=kind
            rows.append(result)
    return rows

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['pilot','full']);args=parser.parse_args()
    rows=run(args.mode)
    output={'complete':True,'mode':args.mode,'case_count':len(rows),'assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START,'log_terms':20,'log_proof':'ln u=2 sum z^(2j+1)/(2j+1), 0<=z<=1/3; positive remainder bounded by 2 z^(2M+1)/((2M+1)(1-z^2)); exponent added after division by positive ln2 interval','rows':rows}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/('check_'+args.mode+'.json')).write_text(json.dumps(encode(output),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in output.items() if k!='rows'},indent=2))
