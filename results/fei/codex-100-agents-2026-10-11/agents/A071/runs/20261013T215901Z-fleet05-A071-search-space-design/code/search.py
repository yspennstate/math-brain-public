import argparse, hashlib, json, math, time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCALE=1<<96; NAT=1<<128; TERMS=48
SEED_POINTS=(0,1,2,4,8,16,32,6,17,40)
SEED=sum(1<<x for x in SEED_POINTS)

def ln_unit(a,b):
    u,v=a-b,a+b
    low=sum(2*NAT*pow(u,2*j+1)//((2*j+1)*pow(v,2*j+1)) for j in range(TERMS))
    num=2*NAT*pow(u,2*TERMS+1)*v*v
    den=(2*TERMS+1)*pow(v,2*TERMS+1)*(v*v-u*u)
    return low,low+TERMS+(num+den-1)//den
LN2=ln_unit(2,1)

@lru_cache(None)
def log_int(n):
    assert n>0
    k=n.bit_length()-1
    if n==1<<k:return k*SCALE,k*SCALE
    a,b=ln_unit(n,1<<k)
    a+=k*LN2[0];b+=k*LN2[1]
    return a*SCALE//LN2[1],(b*SCALE+LN2[0]-1)//LN2[0]

@lru_cache(None)
def phi_pair(x,y):
    if not x or not y:return Q(0),Q(0)
    d=math.lcm(x.denominator,y.denominator)
    a=int(x*d);b=int(y*d);s=a+b
    sl,sh=log_int(s);al,ah=log_int(a);bl,bh=log_int(b)
    return Q(s*sl-a*ah-b*bh,d*SCALE),Q(s*sh-a*al-b*bl,d*SCALE)

def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(x,c):
    assert c>=0
    return x[0]*c,x[1]*c
def pack(x):return {'rational_bounds':[str(x[0]),str(x[1])],'display':[float(x[0]),float(x[1])]}
def sign(x):
    if x==(0,0):return 'zero'
    if x[1]<0:return 'negative'
    if x[0]>0:return 'positive'
    raise ArithmeticError('unresolved fixed-precision sign')
def fwht(a):
    a=list(a);step=1
    while step<len(a):
        for base in range(0,len(a),2*step):
            for j in range(base,base+step):
                u,v=a[j],a[j+step];a[j]=u+v;a[j+step]=u-v
        step*=2
    return a
def truth(n,mask):return [1-2*((mask>>x)&1) for x in range(1<<n)]

@lru_cache(None)
def outer(p):
    # Centered-bit expansion: c0=(1-p)u+p*v; c1=v-u.
    c=[Q(x) for x in truth(6,SEED)]
    for i in range(6):
        for s in range(64):
            if not(s>>i&1):
                u,v=c[s],c[s|(1<<i)]
                c[s]=(1-p)*u+p*v;c[s|(1<<i)]=v-u
    sq=[x*x*(p*(1-p))**s.bit_count() for s,x in enumerate(c)]
    assert sum(sq)==1
    v=4*p*(1-p)
    q=sum(sq[s] for s in range(64) if s&1)/v
    assert q==2*p*(1-p)**3*(2-p)
    alpha=(1-p)**4*(1+4*p-2*p*p)
    assert sq[0]==(1-2*alpha)**2
    return sq,q

@lru_cache(None)
def reserve(p,t):
    sq,q=outer(p);v=4*p*(1-p);m=1-2*p
    M=(Q(0),Q(0))
    for s in range(0,64,2):M=add(M,phi_pair(sq[s],t*sq[s+1]/v))
    R=sub(M,mul(phi_pair(m*m,t),q))
    return M,R

def cases(pilot):
    for n in range(3 if pilot else 4):
        for mask in range(1<<(1<<n)):yield n,mask,'all-small'
    edits=[SEED] if pilot else [SEED]+[SEED^(1<<x) for x in range(64)]
    for mask in edits:
        yield 6,mask,'seed-edit'
        if not pilot:yield 6,mask^((1<<64)-1),'seed-edit-complement'

def evaluate(n,mask):
    N=1<<n;a=truth(n,mask);cs=fwht(a)
    assert sum(c*c for c in cs)==N*N
    p=Q(mask.bit_count(),N);m=Q(cs[0],N)
    if p in (0,1):return {'n':n,'mask':mask,'p':str(p),'constant':True,'coordinates':[]}
    sq=[Q(c*c,N*N) for c in cs];outer_sq,q=outer(p)
    rows=[]
    for i in range(n):
        influence=sum(sq[s] for s in range(N) if s>>i&1)
        if not influence:continue
        assert influence==Q(sum(a[x]!=a[x^(1<<i)] for x in range(N)),N)
        B=(Q(0),Q(0))
        for s in range(N):
            if not(s>>i&1):B=add(B,phi_pair(sq[s],sq[s|(1<<i)]))
        t=sq[1<<i];M,R=reserve(p,t)
        BF=add(mul(B,q),R)
        rows.append({'i':i,'singleton':str(Q(cs[1<<i],N)),'influence_core':str(influence),
                     'influence_composed':str(q*influence),'reserve_sign':sign(R),
                     'reserve':pack(R),'E_core_coordinate':pack(mul(B,1/influence)),
                     'E_composed_coordinate':pack(mul(BF,1/(q*influence)))})
    ec=min(Q(r['E_core_coordinate']['rational_bounds'][0]) for r in rows),min(Q(r['E_core_coordinate']['rational_bounds'][1]) for r in rows)
    ef=min(Q(r['E_composed_coordinate']['rational_bounds'][0]) for r in rows),min(Q(r['E_composed_coordinate']['rational_bounds'][1]) for r in rows)
    delta=sub(ef,ec)
    return {'n':n,'mask':mask,'p':str(p),'q':str(q),'constant':False,'coordinates':rows,
            'E_core':pack(ec),'E_composed':pack(ef),'E_change':pack(delta),
            'E_change_class':'increase' if delta[0]>0 else 'decrease' if delta[1]<0 else 'equal-or-overlap'}

def main(pilot):
    start=time.perf_counter();cap=55 if pilot else 600
    target=ROOT/'out'/('pilot.jsonl' if pilot else 'cases.jsonl')
    counts={};neg=[];decrease=[];seed=None;coord=0;count=0
    with target.open('w',encoding='utf-8') as f:
        for n,mask,tag in cases(pilot):
            item=evaluate(n,mask);item['tag']=tag
            f.write(json.dumps(item)+'\n');f.flush();count+=1
            for r in item['coordinates']:
                coord+=1;s=r['reserve_sign'];counts[s]=counts.get(s,0)+1
                if s=='negative':neg.append([n,mask,r['i']])
            if item.get('E_change_class')=='decrease':decrease.append([n,mask])
            if n==6 and mask==SEED:seed=item
            if time.perf_counter()-start>cap:raise RuntimeError('frozen runtime cap')
    assert count==(23 if pilot else 408)
    result={'cases':count,'relevant_core_coordinates':coord,'reserve_sign_counts':counts,
            'negative_examples':neg[:20],'decreasing_E_cases':len(decrease),'decreasing_examples':decrease[:20],
            'seed':seed,'runtime_seconds':time.perf_counter()-start,
            'jsonl_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
            'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'log_precision_bits':96,'unresolved_reserve_signs':0}
    (ROOT/'out'/('pilot.json' if pilot else 'summary.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
