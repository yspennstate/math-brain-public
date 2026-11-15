"""Exact spectra and exact subset optimization of the full last-r statistic.
Masses are dyadic floats, logarithms ordinary binary64. No model workers.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,math,itertools,json,time,resource
import numpy as np
sys.path.insert(0,os.path.abspath('inputs'))
from experiment import phi,wht,zeta,masses,best_order

def window_cost(p,q,order,r):
    ids=np.arange(len(p),dtype=np.int64);key=np.zeros(len(p),np.int64);cnt=np.zeros(len(p),np.int8)
    for j in order: # nearest end first
        take=(((ids>>j)&1)!=0)&(cnt<r)
        key[take]|=1<<j;cnt+=take
    pp=np.bincount(key,weights=p,minlength=len(p));qq=np.bincount(key,weights=q,minlength=len(p))
    return float(phi(pp,qq).sum())

def block_cost(p,q,B):
    idx=np.arange(len(p));mask=sum(1<<j for j in B);key=idx&mask
    return float(phi(np.bincount(key,weights=p,minlength=len(p)),np.bincount(key,weights=q,minlength=len(p))).sum())

def best_window(p,q,r):
    m=(len(p)-1).bit_length();N=len(p);idx=np.arange(N,dtype=np.int64);full=N-1
    pc=np.zeros(N,dtype=np.int8)
    for j in range(m):pc+=(idx>>j)&1
    base=float(phi(p[pc<r],q[pc<r]).sum())
    ap=zeta(p)[full^idx];aq=zeta(q)[full^idx]
    edges=np.zeros((m,N),float)
    for K in itertools.combinations(range(m),r):
        mask=sum(1<<j for j in K);Rs=idx[(idx&mask)==mask]
        pp=np.zeros(len(Rs));qq=np.zeros(len(Rs))
        for take in range(1<<r):
            sub=sum(1<<K[j] for j in range(r) if (take>>j)&1)
            sign=-1 if (r-take.bit_count())%2 else 1
            pp+=sign*ap[Rs^sub];qq+=sign*aq[Rs^sub]
        c=phi(np.maximum(pp,0),np.maximum(qq,0))
        for j in K:edges[j,Rs]+=c
    d=np.full(N,np.inf);parent=np.zeros(N,np.int8);d[0]=base
    for layer in range(1,m+1):
        ids=idx[pc==layer]
        for j in range(m):
            Rs=ids[((ids>>j)&1)!=0];prev=Rs^(1<<j)
            v=d[prev]+edges[j,Rs];yes=v<d[Rs]
            d[Rs[yes]]=v[yes];parent[Rs[yes]]=j
    R=full;od=[]
    while R:
        j=int(parent[R]);od.append(j);R^=1<<j
    od.reverse()
    return float(d[-1]),od

def truth_dnf(n,terms):
    idx=np.arange(1<<n,dtype=np.int64);v=np.zeros(len(idx),bool)
    for T in terms:
        mask=sum(1<<j for j in T);v|=(idx&mask)==mask
    return 1.-2.*v

def tree(w,D):
    L=w-1;nz=D*L;n=1+nz+nz*(D-1)*L;terms=[]
    for t in range(D):terms.append([0]+list(range(1+t*L,1+(t+1)*L)))
    pos=1+nz
    for z in range(1,1+nz):
        for _ in range(D-1):terms.append([z]+list(range(pos,pos+L)));pos+=L
    return n,terms

def validate():
    rng=np.random.default_rng(2101);rows=[]
    for n in range(2,7):
        for t in range(8):
            f=rng.choice([-1.,1.],1<<n);mu=wht(f)**2;p,q=masses(mu,t%n)
            for r in range(1,min(3,n-1)+1):
                v,od=best_window(p,q,r);direct=window_cost(p,q,od,r)
                brute=min(window_cost(p,q,perm,r) for perm in itertools.permutations(range(n-1)))
                assert max(abs(v-direct),abs(v-brute))<1e-11
                if r==1:assert abs(v-best_order(p,q)[0])<1e-11
                rows.append(dict(n=n,trial=t,r=r,DP=v,brute=brute,residual=max(abs(v-brute),abs(v-direct))))
    return rows

def run_case(name,n,terms=None,f=None,coords=None,rmax=3):
    if f is None:f=truth_dnf(n,terms)
    mu=wht(f)**2;rows=[]
    for i in range(n) if coords is None else coords:
        p,q=masses(mu,i);delta=float(q.sum())
        if not delta:continue
        row=dict(i=i,delta=delta,E=float(phi(p,q).sum())/delta)
        for r in range(1,min(rmax,n-1)+1):
            v,od=best_window(p,q,r);actual=window_cost(p,q,od,r)
            assert abs(v-actual)<1e-10,(name,i,r,v,actual)
            row['L'+str(r)]=v/delta;row['order'+str(r)]=od
        if terms:
            neighbours=set(j for T in terms if i in T for j in T if j!=i)
            orig=[j for j in range(n) if j!=i];B=[orig.index(j) for j in neighbours]
            row['block_neighbours']=len(B);row['block']=block_cost(p,q,B)/delta
        rows.append(row)
    out=dict(name=name,n=n,terms=terms,coordinate_scope='all' if coords is None else coords,rows=rows)
    out['minima']={k:min(z[k] for z in rows) for k in ['E','L1','L2','L3','block'] if rows and k in rows[0]}
    print(json.dumps(dict(name=name,n=n,minima=out['minima'])),flush=True)
    return out

def scan():
    rng=np.random.default_rng(2102);rows=[]
    for w,D in [(2,2),(2,3),(3,2)]:
        n,terms=tree(w,D);rows.append(run_case(f'tree_w{w}_D{D}',n,terms,rmax=3))
    # Full depth-three binary incidence tree, width 2: 15 variables.
    terms=[[j,2*j+1] for j in range(7)]+[[j,2*j+2] for j in range(7)]
    rows.append(run_case('tree_graph_depth3',15,terms,coords=[0,1,3,7],rmax=2))
    for n in [7,9,11,13]:
        terms=[[j,(j+1)%n,(j+2)%n] for j in range(n)]
        rows.append(run_case('cyclic_run3_'+str(n),n,terms,coords=[0],rmax=3))
        # Highly overlapping width roughly n/2 terms.
        w=(n+1)//2
        terms=[[(j+k)%n for k in range(w)] for j in range(n)]
        rows.append(run_case('cyclic_run'+str(w)+'_'+str(n),n,terms,coords=[0],rmax=3))
    for n in [8,10,12]:
        for w in [3,n//2]:
            terms=sorted(set(tuple(sorted(rng.choice(n,w,replace=False).tolist())) for _ in range(round(.69*2**w))))
            rows.append(run_case(f'random_dnf_{n}_{w}',n,terms,rmax=2))
    for n,w in [(18,7),(22,9)]:
        terms=[[(j+k)%n for k in range(w)] for j in range(n)]
        rows.append(run_case(f'cyclic_run{w}_{n}',n,terms,coords=[0],rmax=2))
    # PM(K33) host supplied in the previous worker's exact record, 18-variable gate.
    spec=np.load('inputs/pm_record_spectrum.npy');mu=spec**2
    pp=[]
    for i in [0,9]:
        p,q=masses(mu,i);delta=float(q.sum());entry=dict(i=i,delta=delta,E=float(phi(p,q).sum())/delta)
        for r in [1,2]:
            v,od=best_window(p,q,r);entry['L'+str(r)]=v/delta;entry['order'+str(r)]=od
        pp.append(entry)
    rows.append(dict(name='PM_K33_host',n=18,coordinate_scope='representatives 0(core),9(other)',rows=pp,minima={k:min(z[k] for z in pp) for k in ['E','L1','L2']}))
    return rows

if __name__=='__main__':
    start=time.time();mode=sys.argv[1];rows=validate() if mode=='validate' else scan()
    out=dict(mode=mode,rows=rows,seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    json.dump(out,open('windows_'+mode+'.json','w'),indent=2)
