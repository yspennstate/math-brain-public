"""Frozen A029-depth2-v1. Standard library; integer certified census."""
import argparse, json, time
from fractions import Fraction as F
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
P=1<<80
Q=256*P

def ln_interval(x,terms=90):
    z=(x-1)/(x+1)
    assert 0<=z<=F(1,3)
    s=F(0); power=z
    for k in range(terms):
        s+=2*power/(2*k+1); power*=z*z
    return s,s+2*power/((2*terms+1)*(1-z*z))

L2=ln_interval(F(2))
def log2_integer(x):
    if x==0:return (0,0)
    k=x.bit_length()-1
    if x==1<<k:return (k*P,k*P)
    lo,hi=ln_interval(F(x,1<<k))
    a=k+lo/L2[1]; b=k+hi/L2[0]
    return a.numerator*P//a.denominator, -((-b.numerator*P)//b.denominator)

LOG={w*w:log2_integer(w*w) for w in range(17)}

def fwht(a):
    a=a[:]; step=1
    while step<len(a):
        for start in range(0,len(a),2*step):
            for j in range(start,start+step):
                u,v=a[j],a[j+step]; a[j]=u+v; a[j+step]=u-v
        step*=2
    return a

def restrict(mask,n,i,b):
    out=0
    for y in range(1<<(n-1)):
        x=(y&((1<<i)-1))|((y>>i)<<(i+1))|(b<<i)
        out|=((mask>>x)&1)<<y
    return out

def record(mask,n):
    w=fwht([1 if mask>>x&1 else -1 for x in range(1<<n)])
    assert sum(t*t for t in w)==4**n
    factor=256//4**n
    low=2*n*Q-factor*sum(t*t*LOG[t*t][1] for t in w)
    high=2*n*Q-factor*sum(t*t*LOG[t*t][0] for t in w)
    infl=factor*sum(s.bit_count()*t*t for s,t in enumerate(w))
    coords=[factor*sum(t*t for s,t in enumerate(w) if s>>i&1) for i in range(n)]
    # independent physical boundary equality, per coordinate
    for i,d in enumerate(coords):
        assert d==256*sum(((mask>>x)^(mask>>(x^(1<<i))))&1 for x in range(1<<n))//(1<<n)
    return low,high,infl,coords

def less(a,b):return a[0]*b[1]<b[0]*a[1]
def min_rat(items,index):
    best=None
    for it in items:
        r=(it[index],it[2])
        if best is None or less(r,best):best=r
    return best

def search(maxn):
    start=time.monotonic(); data={}; options={}; results={}; winner=None; global_upper=(0,1)
    checked=0; tree_count=0
    for n in range(maxn+1):
        for mask in range(1<<(1<<n)):
            rec=record(mask,n); data[n,mask]=rec
            lo,hi,inf,coords=rec
            op=[(lo,hi,inf,-1)]
            locals_=[]; trees=[]
            if inf:
                for i,d in enumerate(coords):
                    if not d:continue
                    cm=restrict(mask,n,i,0); cp=restrict(mask,n,i,1)
                    ml,mh,mi,_=data[n-1,cm]; pl,ph,pi,_=data[n-1,cp]
                    assert inf-(mi+pi)//2==d
                    dl=lo-(mh+ph)//2; dh=hi-(ml+pl)//2
                    locals_.append((dl,dh,d,i))
                    op.append(((ml+pl)//2,(mh+ph)//2,(mi+pi)//2,i))
                    for a in options[n-1,cm]:
                        for b in options[n-1,cp]:
                            tl=lo-(a[1]+b[1])//2; th=hi-(a[0]+b[0])//2
                            ti=inf-(a[2]+b[2])//2
                            assert ti>0
                            trees.append((tl,th,ti,i,a[3],b[3]))
                r1l=min_rat(locals_,0); r1h=min_rat(locals_,1)
                r2l=min_rat(trees,0); r2h=min_rat(trees,1)
                gl=(r1l[0]*r2h[1]-r2h[0]*r1l[1],r1l[1]*r2h[1])
                gh=(r1h[0]*r2l[1]-r2l[0]*r1h[1],r1h[1]*r2l[1])
                if less(global_upper,gh):global_upper=gh
                if winner is None or less(winner['gap_lower_raw'],gl):
                    winner={'n':n,'mask':mask,'gap_lower_raw':gl,'gap_upper_raw':gh,
                        'r1_lower_raw':r1l,'r1_upper_raw':r1h,'r2_lower_raw':r2l,'r2_upper_raw':r2h,
                        'root_record':rec,'local_steps':locals_,
                        'best_tree':min(trees,key=lambda x:F(x[1],x[2]))}
                    (BASE/'out'/'checkpoint.json').write_text(json.dumps(winner,indent=2))
                checked+=1; tree_count+=len(trees)
                results[n,mask]=(gl,gh)
            options[n,mask]=op
        print(json.dumps({'n_complete':n,'elapsed':time.monotonic()-start,'nonconstant_checked':checked,'tree_count':tree_count}),flush=True)
    # Count maximizers compatible with intervals; certifies all other masks below winner lower.
    tied=[list(key) for key,(gl,gh) in results.items() if not less(gh,winner['gap_lower_raw'])]
    winner['possible_maximizers']=tied
    winner['global_upper_raw']=global_upper
    winner['checked_nonconstant']=checked; winner['candidate_trees']=tree_count
    winner['elapsed_seconds']=time.monotonic()-start
    winner['units']='raw ratios divided by 2^80; entropy raw divided by 256*2^80; influence raw divided by 256'
    def decimal(r):return float(F(r[0],r[1]*P))
    winner['display_only']={k:decimal(v) for k,v in winner.items() if k.endswith('_raw')}
    (BASE/'out'/f'census_n{maxn}.json').write_text(json.dumps(winner,indent=2))
    print(json.dumps({k:v for k,v in winner.items() if k not in ('possible_maximizers','local_steps')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--maxn',type=int,choices=[3,4],required=True)
    search(parser.parse_args().maxn)
