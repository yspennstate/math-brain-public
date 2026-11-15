"""Independent exact-table and compressed filtration experiments. All outputs local."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
import itertools, json, math, sys, time, resource
import numpy as np

def phi(a,b):
    a,b=np.broadcast_arrays(np.asarray(a,float),np.asarray(b,float))
    out=np.zeros(a.shape)
    sel=(a>0)&(b>0)
    aa,bb=a[sel],b[sel]
    out[sel]=(aa*np.log1p(bb/aa)+bb*np.log1p(aa/bb))/math.log(2)
    return out

def wht(f):
    a=np.array(f,dtype=float,copy=True); N=a.shape[-1]
    k=1
    while k<N:
        shape=a.shape; z=a.reshape(*shape[:-1],-1,2,k)
        x=z[...,0,:].copy(); y=z[...,1,:].copy()
        z[...,0,:]=x+y;z[...,1,:]=x-y
        a=z.reshape(shape);k*=2
    return a/N

def zeta(v):
    a=np.array(v,copy=True);N=len(a);k=1
    while k<N:
        z=a.reshape(-1,2,k);z[:,1,:]+=z[:,0,:];k*=2
    return a

def masses(mu,i):
    idx=np.arange(len(mu)); lo=idx[((idx>>i)&1)==0]
    return mu[lo],mu[lo+(1<<i)]

def order_cost(p,q,order):
    a,b=zeta(p),zeta(q);R=0
    val=float(phi(a[0],b[0])); M=0.;delta=float(b[-1])
    for j in order:
        P=R;R|=1<<j
        val+=float(phi(max(0,a[R]-a[P]),max(0,b[R]-b[P])))
        if delta: M=max(M,(a[-1]-a[P])*b[R]/delta**2)
    return val,M

_plans={}
def best_order(p,q):
    m=(len(p)-1).bit_length();N=1<<m;a,b=zeta(p),zeta(q)
    if m not in _plans:
        idx=np.arange(N);pc=np.zeros(N,int)
        for j in range(m):pc+=(idx>>j)&1
        steps=[]
        for layer in range(1,m+1):
            ids=idx[pc==layer]
            for j in range(m):
                R=ids[((ids>>j)&1)==1];steps.append((j,R,R^(1<<j)))
        _plans[m]=steps
    d=np.full(N,np.inf);parent=np.zeros(N,int);d[0]=phi(a[0],b[0])
    for j,R,P in _plans[m]:
        c=d[P]+phi(np.maximum(a[R]-a[P],0),np.maximum(b[R]-b[P],0))
        improve=c<d[R];d[R[improve]]=c[improve];parent[R[improve]]=j
    R=N-1;order=[]
    while R:
        j=int(parent[R]);order.append(j);R^=1<<j
    return float(d[-1]),order[::-1]

def analyse(f,n,coords=None):
    mu=wht(f)**2;rows=[]
    for i in range(n) if coords is None else coords:
        p,q=masses(mu,i);delta=float(q.sum())
        if not delta:continue
        E=float(phi(p,q).sum());L,order=best_order(p,q)
        orig=[j for j in range(n) if j!=i]
        rows.append(dict(i=i,inf=delta,E=E/delta,F=L/delta,order=[orig[j] for j in order],M=order_cost(p,q,order)[1]))
    return dict(n=n,F=min(r['F'] for r in rows),E=min(r['E'] for r in rows),gap=min(r['F'] for r in rows)-min(r['E'] for r in rows),rows=rows)

def bits(n):return (np.arange(1<<n)[:,None]>>np.arange(n))&1
def truthhex(f):return format(sum(1<<j for j,x in enumerate(f) if x<0),'x')
def gate(kind,b):
    if kind=='AND':return b.all(axis=-1)
    if kind=='OR':return b.any(axis=-1)
    if kind=='XOR':return b.sum(axis=-1)%2==1
    if kind=='MAJ':return b.sum(axis=-1)*2>b.shape[-1]
    raise ValueError(kind)

def compose_table(F,gs):
    ns=[int(math.log2(len(g))) for g in gs];n=sum(ns);idx=np.arange(1<<n);arg=np.zeros(1<<n,int);off=0
    for j,(g,r) in enumerate(zip(gs,ns)):
        arg|=(g[(idx>>off)&((1<<r)-1)]<0).astype(int)<<j;off+=r
    return F[arg]

def block_order_check(rng, trials=200):
    """Compare all-coordinate DP with best fully contiguous block ordering."""
    counter=None;target_err=0.;count=0
    for t in range(trials):
        sizes=[2,2,2] if t%2 else [3,2,1]
        gs=[rng.choice([-1.,1.],1<<n) for n in sizes]
        F=rng.choice([-1.,1.],8);f=compose_table(F,gs);mu=wht(f)**2
        for i in range(sum(sizes)):
            p,q=masses(mu,i)
            if q.sum()==0:continue
            best,ordr=best_order(p,q);orig=[j for j in range(6) if j!=i];inv={j:k for k,j in enumerate(orig)}
            blocks=[];off=0;target=0
            for j,r in enumerate(sizes):
                blocks.append([inv[k] for k in range(off,off+r) if k!=i])
                if off<=i<off+r:target=j
                off+=r
            lastbest=math.inf;contig=math.inf;contig_order=None
            outside=[k for j,B in enumerate(blocks) if j!=target for k in B]
            for out in itertools.permutations(outside):
                for inner in itertools.permutations(blocks[target]):
                    val=order_cost(p,q,out+inner)[0];lastbest=min(lastbest,val)
            for perm in itertools.permutations(range(3)):
                for internals in itertools.product(*[list(itertools.permutations(B)) for B in blocks]):
                    order=tuple(k for j in perm for k in internals[j]);val=order_cost(p,q,order)[0]
                    if val<contig:contig=val;contig_order=order
            target_err=max(target_err,abs(best-lastbest));count+=1
            if contig>best+1e-11 and counter is None:
                counter=dict(trial=t,i=i,sizes=sizes,F=truthhex(F),gs=[truthhex(g) for g in gs],truth=truthhex(f),best=best,contiguous=contig,order=ordr,contiguous_order=contig_order)
        if counter:break
    return dict(coordinates=count,target_last_error=target_err,all_blocks_counterexample=counter)

def adaptive_energy(f,n,i,policy):
    """Bins by actual input-tree depth, not by a spectral label."""
    idx=np.arange(1<<n);lo=idx[((idx>>i)&1)==0];g=(f[lo]+f[lo+(1<<i)])/2;h=(f[lo]-f[lo+(1<<i)])/2
    m=n-1;A=[float(g.mean()**2)]+[0.]*m;B=[float(h.mean()**2)]+[0.]*m
    def visit(ids,remaining,depth,history):
        if not remaining:return
        j=policy(remaining,history)
        x=ids[((ids>>j)&1)==0];y=ids[((ids>>j)&1)==1]
        A[depth]+=len(ids)/len(g)*((g[x].mean()-g[y].mean())/2)**2
        B[depth]+=len(ids)/len(h)*((h[x].mean()-h[y].mean())/2)**2
        for val,sub in [(0,x),(1,y)]:visit(sub,[k for k in remaining if k!=j],depth+1,history+[(j,val)])
    visit(np.arange(1<<m),list(range(m)),1,[])
    return float(phi(A,B).sum()),A,B

def audit():
    rng=np.random.default_rng(191910);errors=dict(parseval=0.,martingale=0.,pair_A=0.,pair_B=0.,DP_brute=0.,data_processing=0.,trivial=0.,composition=0.)
    adaptive=None;cases=0
    for n in [2,3,4,5,6,7]:
        trials=256 if n<=3 else 80
        for t in range(trials):
            f=rng.choice([-1.,1.],1<<n);fh=wht(f);mu=fh**2;errors['parseval']=max(errors['parseval'],abs(mu.sum()-1))
            i=int(rng.integers(n));p,q=masses(mu,i);delta=float(q.sum())
            if not delta:continue
            m=n-1;order=list(rng.permutation(m));a,b=zeta(p),zeta(q);val,M=order_cost(p,q,order);E=float(phi(p,q).sum())
            errors['data_processing']=max(errors['data_processing'],E-val)
            errors['trivial']=max(errors['trivial'],val-float(phi(1-delta,delta)))
            idx=np.arange(1<<n);lo=idx[((idx>>i)&1)==0];g=(f[lo]+f[lo+(1<<i)])/2;h=(f[lo]-f[lo+(1<<i)])/2
            R=0;ag=gh=0.
            for j in order:
                old=R;R|=1<<j
                def conditional(v,mask):
                    key=np.arange(len(v))&mask;su=np.bincount(key,weights=v,minlength=len(v));co=np.bincount(key,minlength=len(v));return su[key]/co[key]
                G=conditional(g,R);G0=conditional(g,old);H=conditional(h,R)
                errors['martingale']=max(errors['martingale'],abs(np.mean((G-G0)**2)-(a[R]-a[old])))
                errors['pair_B']=max(errors['pair_B'],abs(np.mean(H**2)-b[R]))
                # Pair law conditionally independent given old revealed values.
                key=np.arange(len(g))&old;tail=0.;pivnon=0.;cross=0.
                for z in np.unique(key):
                    ids=np.flatnonzero(key==z);weight=len(ids)/len(g);gg=g[ids];hh=h[ids]
                    piv=np.mean(hh!=0);pivnon+=weight*piv*(1-piv)
                    cross+=weight*2*np.mean(gg==1)*np.mean(gg==-1)
                errors['pair_A']=max(errors['pair_A'],abs(a[-1]-a[old]-pivnon-2*cross))
            opt,oo=best_order(p,q)
            if n<=5:
                brute=min(order_cost(p,q,z)[0] for z in itertools.permutations(range(m)))
                errors['DP_brute']=max(errors['DP_brute'],abs(brute-opt))
            if n>=4 and adaptive is None:
                def policy(rem,hist):return rem[-1] if hist and hist[0][1] else rem[0]
                ad,A,B=adaptive_energy(f,n,i,policy)
                if E>ad+1e-9:adaptive=dict(n=n,i=i,truth=truthhex(f),E=E,adaptive=ad,A=A,B=B,policy='smallest remaining, except choose largest after first answer 1')
            cases+=1
    # Independent composition identities and target-block theorem.
    for t in range(100):
        g=rng.choice([-1.,1.],8);F=rng.choice([-1.,1.],8);f=compose_table(F,[g,np.array([1.,-1.]),np.array([1.,-1.])]);gh=wht(g)
        F0=(F[0::2]+F[1::2])/2;F1=(F[0::2]-F[1::2])/2;u,v=wht(F0),wht(F1);alpha=float(np.sum(v*v))
        for i in range(3):
            pg,qg=masses(gh**2,i);pf,qf=masses(wht(f)**2,i)
            lhs=float(phi(pf,qf).sum());rhs=alpha*(float(phi(pg,qg).sum())-float(phi(gh[0]**2,gh[1<<i]**2)))+float(phi((u+gh[0]*v)**2,gh[1<<i]**2*v*v).sum())
            errors['composition']=max(errors['composition'],abs(lhs-rhs))
    blocks=block_order_check(rng)
    return dict(cases=cases,errors=errors,adaptive_counterexample=adaptive,block_orders=blocks)

def structured():
    out=[]
    for n in [4,6,8,10,12,14,16]:
        x=bits(n);f=np.where(x.all(axis=1),-1.,1.)
        out.append(dict(name=f'AND_{n}',**analyse(f,n,[0])))
    for w,s in [(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(3,4),(3,5),(4,4)]:
        n=w*s;f=np.where(bits(n).reshape(-1,s,w).all(axis=2).any(axis=1),-1.,1.)
        out.append(dict(name=f'TRIBES_{w}x{s}',**analyse(f,n,[0])))
    for n in [3,5,7,9,11,13,15]:
        f=np.where(bits(n).sum(axis=1)*2>n,-1.,1.);out.append(dict(name=f'MAJ_{n}',**analyse(f,n,[0])))
    for w,r in [(2,3),(3,3),(4,3),(5,3),(2,5),(3,5),(2,7)]:
        n=w*r;x=bits(n).reshape(-1,w,r);inn=x.sum(axis=2)*2>r
        for kind in ['AND','XOR']:
            f=np.where(gate(kind,inn),-1.,1.);out.append(dict(name=f'{kind}{w}_MAJ{r}',**analyse(f,n,[0])))
    for q in [2,3,4]:
        n=2**q;x=bits(n)
        for seq in itertools.product(['AND','OR','XOR'],repeat=q):
            if q==4 and seq not in [('OR','AND','OR','AND'),('AND','OR','AND','OR'),('XOR','AND','OR','AND')]:continue
            v=x
            for k in seq:v=gate(k,v.reshape(len(v),-1,2))
            f=1.-2.*v[:,0];out.append(dict(name='_'.join(seq),**analyse(f,n,[0])))
    for n in [4,6,8,10,12,14,16]:
        x=bits(n);f=1.-2.*((x[:,::2]*x[:,1::2]).sum(axis=1)%2)
        out.append(dict(name=f'BENT_{n}',**analyse(f,n,[0])))
    # Fano lines: projective plane and Steiner triple system STS(7).
    lines=[]
    for a in range(1,8):
        for b in range(a+1,8):
            c=a^b
            if c>b:lines.append([a-1,b-1,c-1])
    x=bits(7);f=np.where(np.any([x[:,L].all(axis=1) for L in lines],axis=0),-1.,1.)
    out.append(dict(name='Fano_STS7_DNF',terms=lines,**analyse(f,7,[0])))
    # Affine STS(9), lines in F3^2.
    pts=list(itertools.product(range(3),repeat=2));lines=set()
    for a in pts:
        for d in pts[1:]:lines.add(tuple(sorted(pts.index(((a[0]+t*d[0])%3,(a[1]+t*d[1])%3)) for t in range(3))))
    x=bits(9);f=np.where(np.any([x[:,L].all(axis=1) for L in sorted(lines)],axis=0),-1.,1.)
    out.append(dict(name='Affine_STS9_DNF',terms=sorted(lines),**analyse(f,9,[0])))
    # PG(2,3), thirteen points, thirteen lines of size four.
    vecs=[]
    for p in itertools.product(range(3),repeat=3):
        if not any(p):continue
        first=next(z for z in p if z);canon=tuple(z*pow(first,-1,3)%3 for z in p)
        if canon not in vecs:vecs.append(canon)
    lines=[[j for j,v in enumerate(vecs) if sum(a*b for a,b in zip(w,v))%3==0] for w in vecs]
    x=bits(13);f=np.where(np.any([x[:,L].all(axis=1) for L in lines],axis=0),-1.,1.)
    out.append(dict(name='PG23_DNF',terms=lines,**analyse(f,13,[0])))
    for n,k in [(8,3),(10,3),(12,3),(14,4),(16,4)]:
        x=bits(n)
        for pat in [list(range(k)),[0,1,3] if k==3 else [0,1,3,6]]:
            terms=[[(j+a)%n for a in pat] for j in range(n)]
            f=np.where(np.any([x[:,L].all(axis=1) for L in terms],axis=0),-1.,1.)
            out.append(dict(name=f'CYCLIC_{n}_{pat}',terms=terms,**analyse(f,n,[0])))
    return out

def main():
    start=time.time();mode=sys.argv[1]
    data=audit() if mode=='audit' else structured()
    out=dict(mode=mode,seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,data=data)
    with open(mode+'.json','w') as fh:json.dump(out,fh,indent=2)
    print(json.dumps(out if mode=='audit' else {**out,'data':[{'name':r['name'],'n':r['n'],'F':r['F'],'E':r['E'],'gap':r['gap']} for r in data]},indent=2),flush=True)
if __name__=='__main__':main()
