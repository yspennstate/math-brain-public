import argparse,itertools,json,time
from collections import Counter
from functools import lru_cache
from fractions import Fraction as R
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
PREC=1<<100; DEN=4096; UNIT=PREC*DEN
ASSERTIONS=0
def ck(condition):
    global ASSERTIONS
    ASSERTIONS+=1
    if not condition:raise AssertionError(ASSERTIONS)
def ln_bounds(x):
    z=(x-1)/(x+1); power=z; total=R(0)
    for k in range(120):total+=2*power/(2*k+1);power*=z*z
    return total,total+2*power/(241*(1-z*z))
L2=ln_bounds(R(2))
def logint(x):
    if not x:return 0,0
    k=x.bit_length()-1
    if x==1<<k:return k*PREC,k*PREC
    lo,hi=ln_bounds(R(x,1<<k));lo=k+lo/L2[1];hi=k+hi/L2[0]
    return lo.numerator*PREC//lo.denominator,(hi.numerator*PREC+hi.denominator-1)//hi.denominator
LOG={w*w:logint(w*w) for w in range(65)}
def fwht(a):
    a=list(a);step=1
    while step<len(a):
        for base in range(0,len(a),2*step):
            for j in range(base,base+step):
                u,v=a[j],a[j+step];a[j]=u+v;a[j+step]=u-v
        step*=2
    return tuple(a)
@lru_cache(None)
def rec(n,mask):
    tab=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));w=fwht(tab)
    ck(sum(v*v for v in w)==4**n)
    mult=DEN//4**n
    lo=2*n*UNIT-mult*sum(v*v*LOG[v*v][1] for v in w)
    hi=2*n*UNIT-mult*sum(v*v*LOG[v*v][0] for v in w)
    d=tuple(mult*sum(v*v for s,v in enumerate(w) if s>>i&1) for i in range(n))
    for i,di in enumerate(d):ck(di==DEN*sum(tab[x]!=tab[x^(1<<i)] for x in range(1<<n))//(1<<n))
    return lo,hi,sum(d),d,w
def maskof(tab):return sum((int(v==1)<<x) for x,v in enumerate(tab))
def function(seed):return tuple((-1 if (x&y).bit_count()%2 else 1)*(1 if seed>>y&1 else -1) for y in range(8) for x in range(8))
def restricted(tab,state):
    free=[i for i,v in enumerate(state) if v==-1]
    fixed=sum(v<<i for i,v in enumerate(state) if v!=-1)
    t=[tab[fixed+sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free))]
    return free,maskof(t)
def core(seed,state,t):
    P=[i for i in range(3) if state[i]==state[i+3]==-1]
    U=[i for i in range(3) if state[i]!=-1 and state[i+3]==-1]
    base=sum(state[i+3]<<i for i in range(3) if state[i+3]!=-1)
    base+=sum(((t>>j)&1)<<i for j,i in enumerate(P))
    table=[]
    for z in range(1<<len(U)):
        y=base+sum(((z>>j)&1)<<i for j,i in enumerate(U))
        parity=sum(((z>>j)&1)*state[i] for j,i in enumerate(U))%2
        table.append((1 if seed>>y&1 else -1)*(-1 if parity else 1))
    return rec(len(U),maskof(table))
def min_leaf_cut(records,depth):
    @lru_cache(None)
    def solve(state,left):
        lo,hi,inf,_,_=records[state]
        low=2*inf*PREC-hi; high=2*inf*PREC-lo
        if left:
            for i,v in enumerate(state):
                if v!=-1:continue
                s=list(state);s[i]=0;a=solve(tuple(s),left-1)
                s[i]=1;b=solve(tuple(s),left-1)
                low=min(low,(a[0]+b[0])//2);high=min(high,(a[1]+b[1])//2)
        return low,high
    return solve((-1,)*6,depth)
def explicit_tree(records):
    nodes=[];leaves=[]
    def visit(state):
        free_x=[i for i in range(3) if state[i]==-1]
        if free_x:i=free_x[0]
        elif all(state[j]==0 for j in range(3)):
            leaves.append((state,3));return
        else:
            free_y=[i for i in range(3,6) if state[i]==-1]
            if not free_y:leaves.append((state,6));return
            i=free_y[0]
        depth=sum(v!=-1 for v in state);nodes.append((state,i,depth))
        for b in range(2):
            s=list(state);s[i]=b;visit(tuple(s))
    visit((-1,)*6)
    leaf_hlo=sum(R(records[s][0],2**d) for s,d in leaves)
    leaf_hhi=sum(R(records[s][1],2**d) for s,d in leaves)
    leaf_i=sum(R(records[s][2],2**d) for s,d in leaves)
    node_d=sum(R(records[s][3][[j for j,v in enumerate(s) if v==-1].index(i)],2**d) for s,i,d in nodes)
    node_hlo=R(0);node_hhi=R(0)
    for s,i,d in nodes:
        t=list(s);t[i]=0;a=records[tuple(t)];t[i]=1;b=records[tuple(t)]
        lo,hi,*_=records[s]
        node_hlo+=R(lo-(a[1]+b[1])//2,2**d)
        node_hhi+=R(hi-(a[0]+b[0])//2,2**d)
    ck(node_d==3*DEN-leaf_i)
    ck(node_hlo<=6*UNIT-leaf_hlo and node_hhi>=6*UNIT-leaf_hhi)
    ck(len(leaves)==57 and len(nodes)==56)
    pi_h=(6*UNIT-leaf_hhi,6*UNIT-leaf_hlo);pi_i=3*DEN-leaf_i
    lo=R(pi_h[0],pi_i*PREC);hi=R(pi_h[1],pi_i*PREC)
    ck(hi<2);ck(4-hi>R(203,100));ck(3**5<2**8)
    return {'leaves':len(leaves),'internal_nodes':len(nodes),'leaf_H_interval_raw':[int(leaf_hlo),int(leaf_hhi)],
     'leaf_I_exact':str(leaf_i/DEN),'Pi_I_exact':str(pi_i/DEN),'ratio_interval':[str(lo),str(hi)],
     'gain_lower':str(4-hi),'display_only_ratio':float((lo+hi)/2),'display_only_gain_lower':float(4-hi),
     'tree_definition':'all x; stop x=0; complete all y elsewhere'}
def main(pilot):
    start=time.monotonic();seedlist=[254] if pilot else range(256)
    states=list(itertools.product((-1,0,1),repeat=6));allcases=0;depth2cases=0;witness={}
    for seed in seedlist:
        tab=function(seed);records={}
        for state in states:
            free,mask=restricted(tab,state);n=len(free);rr=rec(n,mask);records[state]=rr
            lo,hi,inf,d,w=rr
            P=[i for i in range(3) if state[i]==state[i+3]==-1]
            U=[i for i in range(3) if state[i]!=-1 and state[i+3]==-1]
            V=[i for i in range(3) if state[i]==-1 and state[i+3]!=-1]
            ell=sum(state[i+3] for i in V);p=len(P)
            cores=[core(seed,state,t) for t in range(1<<p)]
            hlo=2*p*UNIT+sum(c[0] for c in cores)//(1<<p)
            hhi=2*p*UNIT+sum(c[1] for c in cores)//(1<<p)
            ipred=(p+ell)*DEN+sum(c[2] for c in cores)//(1<<p)
            ck(inf==ipred);ck(lo<=hhi and hlo<=hi)
            expected=Counter()
            for c in cores:
                for val in c[4]:expected[R(val*val,4**(p+len(U)))]+=1<<p
            expected[R(0)]+=2**n-2**(2*p+len(U))
            ck(Counter(R(v*v,4**n) for v in w)==+expected)
            if sum(v!=-1 for v in state)<=2:
                ck(2*inf*PREC-hi>=0);depth2cases+=1
            allcases+=1
        root=records[(-1,)*6];ck(root[0]==root[1]==6*UNIT);ck(root[2]==3*DEN)
        ck(all(abs(v)==8 for v in root[4]));ck(all(di==DEN//2 for di in root[3]))
        for i in range(6):
            s=[-1]*6;s[i]=0;a=records[tuple(s)];s[i]=1;b=records[tuple(s)]
            ck(a[0]==a[1]==b[0]==b[1]==4*UNIT)
        if seed==254:
            witness=explicit_tree(records)
            witness['truth_mask_decimal']=str(maskof(tab));witness['truth_values']=list(tab)
            witness['min_leaf_D2_by_depth']={}
            for depth in range(1,7):
                low,high=min_leaf_cut(records,depth)
                witness['min_leaf_D2_by_depth'][str(depth)]={'low_raw':low,'high_raw':high,
                 'certified_negative':high<0,'certified_nonnegative':low>=0,'display_only':float(R(low+high,2*UNIT))}
            (BASE/'out'/'witness.json').write_text(json.dumps(witness,indent=2))
        if not pilot and (seed+1)%64==0:print(json.dumps({'seeds_done':seed+1,'elapsed':time.monotonic()-start}),flush=True)
    out={'status':'PASS','pilot':pilot,'seeds':len(seedlist),'physical_restrictions':allcases,
     'codim_le2_restrictions':depth2cases,'assertions':ASSERTIONS,'elapsed_seconds':time.monotonic()-start,
     'record_cache':rec.cache_info()._asdict(),'entropy_unit':str(UNIT),'influence_unit':DEN,
     'witness_ratio_display_only':witness.get('display_only_ratio')}
    (BASE/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args();main(args.pilot)
