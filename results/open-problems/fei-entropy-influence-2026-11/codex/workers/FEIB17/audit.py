import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['VECLIB_MAXIMUM_THREADS']='1'
import numpy as np, math, json, time, resource
from pathlib import Path
LN2=math.log(2)
def eta(x):
    return -x*np.log2(np.maximum(x,1e-300))
def h(x):
    return eta(x)+eta(1-x)
def wht(f):
    a=np.array(f,dtype=float,copy=True);N=a.shape[-1];k=1
    while k<N:
        v=a.reshape(*a.shape[:-1],-1,2,k);x=v[...,0,:].copy();y=v[...,1,:].copy();v[...,0,:]=x+y;v[...,1,:]=x-y;k*=2
    return a/N
def entropy(f):return eta(wht(f)**2).sum(-1)
def info(f):
    c=wht(f);n=int(math.log2(c.shape[-1]));pop=np.array([j.bit_count() for j in range(1<<n)])
    return (c*c*pop).sum(-1)
def calc(f):
    B,N=f.shape;n=N.bit_length()-1;c=wht(f);mu=c*c;H=eta(mu).sum(1);pop=np.array([j.bit_count() for j in range(N)]);I=(mu*pop).sum(1)
    E=[];J=[];D=[];G=[];Inf=[];L=[];K=[];raw=[]
    for i in range(n):
        a=c.reshape(B,-1,2,1<<i)[:,:,0,:].reshape(B,-1);b=c.reshape(B,-1,2,1<<i)[:,:,1,:].reshape(B,-1)
        aa=a*a;bb=b*b;s=aa+bb;ap=(a+b)**2;am=(a-b)**2;delta=bb.sum(1)
        ee=(eta(aa)+eta(bb)-eta(s)).sum(1);jj=(eta(s)-.5*eta(ap)-.5*eta(am)).sum(1)
        gg=(bb*np.log2(np.maximum(s,1e-300)/np.maximum(bb,1e-300))).sum(1)
        ll=(bb*np.log2(1+ap/np.maximum(bb,1e-300))).sum(1)
        fparts=f.reshape(B,-1,2,1<<i);fp=fparts[:,:,0,:].reshape(B,-1);fm=fparts[:,:,1,:].reshape(B,-1)
        dd=H-.5*entropy(fp)-.5*entropy(fm)
        nu=bb/np.maximum(delta[:,None],1e-300);mix=(ap+bb)/(1+delta[:,None]);kl=(nu*np.log2(np.maximum(nu,1e-300)/np.maximum(mix,1e-300))).sum(1)
        kk=delta*(np.log2((1+delta)/np.maximum(delta,1e-300))-kl)
        raw.append(((bb>0)&(ap==0)).any(1));E.append(ee);J.append(jj);D.append(dd);G.append(gg);Inf.append(delta);L.append(ll);K.append(kk)
    return dict(c=c,mu=mu,H=H,I=I,E=np.array(E).T,J=np.array(J).T,D=np.array(D).T,G=np.array(G).T,Inf=np.array(Inf).T,L=np.array(L).T,K=np.array(K).T,raw=np.array(raw).T)
def truth(codes,n):return 1-2*((codes[:,None]>>np.arange(1<<n,dtype=np.uint64))&1).astype(float)
def make_bank(n,count,seed):
    rng=np.random.default_rng(seed);N=1<<n;f=[]
    for k in range(count):
        kind=k%6
        if kind<4:g=np.where(rng.random(N)<[.5,.2,.05,.01][kind],-1.,1.)
        elif kind==4:
            coeff=rng.normal(size=n);bits=1-2*((np.arange(N)[:,None]>>np.arange(n))&1);g=np.where((bits*coeff).sum(1)>rng.normal(),1.,-1.)
        else:
            bits=((np.arange(N)[:,None]>>np.arange(n))&1);p=rng.permutation(n);g=np.where(np.any(bits[:,p[:2*(n//2)]].reshape(N,-1,2).all(2),1),-1.,1.)
        f.append(g)
    return np.array(f)
def checks(f,blocks=True):
    o=calc(f);B,N=f.shape;n=N.bit_length()-1;I=o['I'];E=o['E'];J=o['J'];G=o['G'];delta=o['Inf'];H=o['H'];Hm=E.sum(1)
    out={}
    out['split_residual']=float(abs(o['D']-E-J).max());out['pair_soft_KL_residual']=float(abs(o['L']-o['K']).max())
    out['J_nonnegative_violation']=float(max(0.,-J.min()));out['J_bound_violation']=float(max(0.,(J-2/LN2*delta).max()))
    out['Han_violation']=float(max(0.,(Hm-H).max()));out['G_lower_violation']=float(max(0.,(G.sum(1)-Hm).max()));out['G_upper_violation']=float(max(0.,(Hm-G.sum(1)-I/LN2).max()))
    out['pair_error_violation']=float(max(0.,(abs(E-o['L'])-(math.log2(3)+1/LN2)*delta).max()))
    out['pair_improved_error_violation']=float(max(0.,(abs(E-o['L'])-(math.log2((3+math.sqrt(5))/2)+1/LN2)*delta).max()))
    out['raw_KL_singular_coordinate_instances']=int(o['raw'].sum())
    edgekl=np.zeros(B);Qnorm=np.zeros(B)
    for i in range(n):
        ids=np.array([j for j in range(N) if not (j>>i&1)]);a=o['mu'][:,ids];b=o['mu'][:,ids+(1<<i)];q=(a+b)/n;p=b/np.maximum(I[:,None],1e-300)
        edgekl+=(p*np.log2(np.maximum(p,1e-300)/np.maximum(q,1e-300))).sum(1);Qnorm+=q.sum(1)
    rhs=I*(np.log2(n/np.maximum(I,1e-300))-edgekl)
    out['edge_identity_residual']=float(abs(G.sum(1)-rhs).max());out['Q_normalization_residual']=float(abs(Qnorm-1).max())
    out['max_Hm_over_I']=float(np.max(Hm/np.maximum(I,1e-300)));out['max_Ji_over_Infi']=float(np.max(J/np.maximum(delta,1e-300)))
    out['block_first_violation']=0.;out['block_corrected_violation']=0.;out['block_bad_simplification_witness']=None
    if blocks:
        ids=np.arange(N)
        for i in range(n):
            choices=[x for x in range(N) if not(x>>i&1)] if n<=4 else [0,((1<<n)-1)^(1<<i),1<<((i+1)%n)]
            for mask in choices:
                meets=(ids&mask)!=0;pin=((ids>>i)&1)!=0
                A=o['mu'][:,meets].sum(1);et=o['mu'][:,pin&~meets].sum(1);d=delta[:,i]
                exact=A*h(np.clip((d-et)/np.maximum(A,1e-300),0,1))+(1-A)*h(np.clip(et/np.maximum(1-A,1e-300),0,1))
                first=A*h(np.clip((d-et)/np.maximum(A,1e-300),0,1))+h(et)
                correct=d*np.log2(math.e*np.maximum(A+et,1e-300)/np.maximum(d,1e-300))+et*np.log2(math.e/np.maximum(et,1e-300))
                out['block_first_violation']=max(out['block_first_violation'],float((E[:,i]-exact).max()),float((exact-first).max()))
                out['block_corrected_violation']=max(out['block_corrected_violation'],float((first-correct).max()))
                bad=d*np.log2(math.e*np.maximum(A,1e-300)/np.maximum(d,1e-300))+et*np.log2(math.e/np.maximum(et,1e-300))
                j=int(np.argmax(first-bad))
                if first[j]-bad[j]>1e-8 and out['block_bad_simplification_witness'] is None:
                    out['block_bad_simplification_witness']=dict(i=i,mask=mask,A=float(A[j]),eta=float(et[j]),delta=float(d[j]),E=float(E[j,i]),first=float(first[j]),bad=float(bad[j]),truth_hex=hex(sum((int(x<0)<<k) for k,x in enumerate(f[j]))))
    return out

def tree(f,depth=0):
    n=f.size.bit_length()-1
    if n==0 or np.all(f==f[0]):return 0.,0.
    o=calc(f[None,:]);live=np.flatnonzero(o['Inf'][0]>0)
    # Adaptive: alternate largest-influence and largest-D query, using branch-dependent tables.
    i=int(live[np.argmax(o['Inf'][0,live] if depth%2==0 else o['D'][0,live])]);v=f.reshape(-1,2,1<<i)
    Hp,Ip=tree(v[:,0,:].reshape(-1),depth+1);Hm,Im=tree(v[:,1,:].reshape(-1),depth+1)
    return o['D'][0,i]+(Hp+Hm)/2,o['Inf'][0,i]+(Ip+Im)/2

def main():
    start=time.time();out={};agg=None
    for s in range(0,65536,2048):
        z=checks(truth(np.arange(s,s+2048,dtype=np.uint64),4));
        if agg is None:agg=z
        else:
            for k,v in z.items():
                if isinstance(v,(float,int)):
                    agg[k]=agg[k]+v if k=='raw_KL_singular_coordinate_instances' else max(agg[k],v)
                elif agg[k] is None:agg[k]=v
    agg['function_count']=65536;out['all4']=agg;print('all4',json.dumps(agg),flush=True);Path('audit_results.json').write_text(json.dumps(out,indent=2))
    for n in [6,7,8]:
        f=make_bank(n,3000,17100+n);z=checks(f);z['function_count']=len(f);z['seed']=17100+n;out['sample'+str(n)]=z;print('sample',n,json.dumps(z),flush=True);Path('audit_results.json').write_text(json.dumps(out,indent=2))
    errH=errI=0.;count=0
    for n in [4,6,7,8]:
        f=make_bank(n,100,17300+n)
        for g in f:
            ht,it=tree(g);errH=max(errH,abs(ht-float(entropy(g))));errI=max(errI,abs(it-float(info(g))));count+=1
    out['adaptive_tree']=dict(count=count,entropy_residual=errH,influence_residual=errI)
    out['elapsed_seconds']=time.time()-start;out['maxrss_bytes_macos']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;out['nice']=os.getpriority(os.PRIO_PROCESS,0)
    Path('audit_results.json').write_text(json.dumps(out,indent=2));print('DONE',out['adaptive_tree'],out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
