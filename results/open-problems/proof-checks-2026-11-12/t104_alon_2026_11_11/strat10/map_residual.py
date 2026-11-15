"""NUMERICAL: sample every filter of STRAT9 region (11), never a proof."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,itertools,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
PAIRS=list(itertools.combinations(range(5),2))
RECS=json.load(open('moment_cells.json'))+json.load(open('allN_optimized_cells.json'))
from fractions import Fraction as F
from cells import vector_from_record
BANK=[(float(F(c['rlo'])),float(F(c['rhi'])),np.array(list(map(float,vector_from_record(c))))) for c in RECS]
BOXES=np.array([[[float(F(v)) for v in p] for p in c['box']] for c in json.load(open('face_boxes.json'))])

def moments(u,w):
    return np.array([np.sum(u**4,axis=-1),np.sum(w**4,axis=-1),np.sum(u*u*w*w,axis=-1),np.sum(u**3,axis=-1),np.sum(u*u*w,axis=-1),np.sum(u*w*w,axis=-1),np.sum(w**3,axis=-1)])

def value(m,a,r):
    A,B,C,d,e,f,h=m;fm=A+r*B+(1+r)*C
    L=(11*fm-2*(1+r))/8
    H=(100*(1+r)*fm-1600*(A+r*r*B)-1280*(1+r*r)*C-640*r*C+415*(1+r*r)-66*r)/320
    R=3*d*d+3*r*r*h*h+(1+4*r)*e*e+(r*r+4*r)*f*f+2*(1+r)*(d*f+r*h*e)
    return .1125+a*L+a*a*(H+R)

def bound(m,a,r,vec):
    A,B,C=m[:3];fm=A+r*B+(1+r)*C;lam=(2+a*(1+r))/4
    val=.1125+a*(11*fm-2*(1+r))/8+a*a*(100*(1+r)*fm-1600*(A+r*r*B)-1280*(1+r*r)*C-640*r*C+415*(1+r*r)-66*r)/320
    td=vec[20];z1,z2,z3,z4=vec[21:]
    val-=a*a*(z1*(A-.2)+z2*(B-.2)+(z3+z4)*C)+a*2*lam*td/5
    for i,(alpha,beta) in enumerate(((1,1),(1,0),(0,1),(1,-1))):
        theta,q,c,v,dd=vec[5*i:5*i+5]
        mm=alpha*(A+r*C)+beta*(C+r*B);kk=alpha*alpha*A+2*alpha*beta*C+beta*beta*B
        ss=a*(alpha+beta*r-mm)-lam*(alpha+beta)/5
        val+=a*(a*(2*q*mm-(1+r)*c)-theta*lam*(alpha*alpha+beta*beta-kk)/5+v*ss-dd/2)
    return val

def ceilings(r):
    out=np.full_like(np.asarray(r),.56)
    for c in RECS[:10]:out=np.where((r>=float(F(c['rlo'])))&(r<=float(F(c['rhi']))),np.maximum(out,float(F(c['ahi']))),out)
    return out

def endpoint(u,w,r):
    ds=np.array([-1-r-20*(u[...,i]*u[...,j]+r*w[...,i]*w[...,j])for i,j in PAIRS])
    return 2/np.maximum(3-r,np.max(ds,axis=0)),np.argmax(ds,axis=0)

def chart_excluded(u,w,r,E,tol=2e-10):
    lam=(2+E*(1+r))/4;gap=E*(np.outer(u,u)+r*np.outer(w,w))
    weights=lam/5+gap
    edges=[(i,j)for i,j in PAIRS if abs(weights[i,j])<tol]
    charts=0
    for edge in edges:
        for k,j in (edge,edge[::-1]):
            first=5*gap[k]/lam;t=first[k]
            second=5*E*np.sqrt(r)/lam*(u[k]*w-w[k]*u)
            for rest in itertools.permutations([v for v in range(5)if v not in edge]):
                for sign in (-1,1):
                    x=np.array([t,first[rest[0]],sign*second[rest[0]],first[rest[1]],sign*second[rest[1]],sign*second[j]])
                    if np.any(np.all((x>=BOXES[:,:,0]-tol)&(x<=BOXES[:,:,1]+tol),axis=1)):return False,charts
                    charts+=1
    return charts>0,charts

def residual(u,w,r,a,check_charts=True):
    E,edge=endpoint(u,w,r);m=moments(u,w)
    if not(.15<r<=1 and ceilings(r)<a<=E+1e-12 and E<2/(3-r)-1e-10):return None
    vals=[(bound(m,a,r,v),bound(m,E,r,v))for lo,hi,v in BANK if lo<=r<=hi]
    pa,pe=np.max(vals,axis=0)
    if max(pa,pe)>=-1e-10:return None
    excluded,charts=chart_excluded(u,w,r,E) if check_charts else (True,None)
    if not excluded:return None
    T=float(value(m,a,r));lam=(2+a*(1+r))/4
    weights=[float(lam/5+a*(u[i]*u[j]+r*w[i]*w[j]))for i,j in PAIRS]
    if min(weights)<-1e-10:return None
    return dict(u=u.tolist(),w=w.tolist(),r=float(r),a=float(a),E=float(E),a_over_E=float(a/E),T=T,T_over_a2=T/a**2,zero_edge_at_E=list(PAIRS[int(edge)]),min_weight=min(weights),largest_moment_at_a=float(pa),largest_moment_at_E=float(pe),excluded_charts=charts)

def main():
    rng=np.random.default_rng(101113);start=time.monotonic();samples=[];proposals=0;stages={}
    # 160,000 independent rays; endpoint and two strictly inward scales each.
    for batch in range(40):
        n=4000;x=rng.normal(size=(n,5,2));x-=x.mean(axis=1,keepdims=True);q=np.linalg.qr(x)[0];u,w=q[:,:,0],q[:,:,1]
        r=.15+.85*rng.random(n);r[:n//4]=1-.85*rng.random(n//4)**4
        E,edges=endpoint(u,w,r);ce=ceilings(r);m=moments(u,w)
        pa=np.full(n,-np.inf)
        for lo,hi,v in BANK:pa=np.maximum(pa,np.where((r>=lo)&(r<=hi),bound(m,E,r,v),-np.inf))
        mask=(E>ce+1e-9)&(E<2/(3-r)-1e-9)&(pa<-1e-9)
        for i in np.flatnonzero(mask):
            for frac in (1.,float(rng.beta(6,1)),float(rng.random())):
                aa=ce[i]+frac*(E[i]-ce[i]);rec=residual(u[i],w[i],r[i],aa)
                if rec is not None:samples.append(rec)
        proposals+=n
        if batch%5==4:
            msg=f'NUMERICAL: mapped {proposals} rays; {len(samples)} points pass all numerical (11) filters.'
            print(msg,flush=True)
            with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
    assert samples
    raw_min=min(samples,key=lambda p:p['T']);raw_scaled=min(samples,key=lambda p:p['T_over_a2'])
    # Smooth local searches on centered QR frames, rejecting any exit from (11).
    seeds=sorted(samples,key=lambda p:p['T'])[:12]+sorted(samples,key=lambda p:p['T_over_a2'])[:12]
    refined=[]
    for si,seed in enumerate(seeds):
        x0=np.r_[np.column_stack((seed['u'],seed['w'])).ravel(),seed['r'],seed['a_over_E']]
        scaled=si>=12
        def decode(x):
            v=x[:10].reshape(5,2);v=v-v.mean(axis=0);q=np.linalg.qr(v)[0];rr=x[10];ee,_=endpoint(q[:,0],q[:,1],rr)
            return q[:,0],q[:,1],rr,x[11]*ee
        def obj(x):
            if not(.150000001<x[10]<=1 and .5<x[11]<=1):return 100+np.sum((x-x0)**2)
            uu,ww,rr,aa=decode(x);p=residual(uu,ww,rr,aa,False)
            if p is None:return 10+np.sum((x-x0)**2)
            return p['T_over_a2']if scaled else p['T']
        sol=minimize(obj,x0,method='Nelder-Mead',options=dict(maxiter=1700,xatol=1e-9,fatol=1e-11))
        rec=residual(*decode(sol.x))
        if rec is not None:rec['search']='local NUMERICAL';refined.append(rec)
        if si%4==3:
            msg=f'NUMERICAL: completed {si+1}/24 local searches; best T {min([p["T"] for p in samples+refined]):.12g}.'
            print(msg,flush=True)
            with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
    allp=samples+refined
    minima={key:min(allp,key=lambda p:p[key])for key in ('T','T_over_a2')}
    by_ratio=[]
    for j in range(15,100,5):
        pp=[p for p in allp if j/100<=p['r']<=(j+5)/100]
        if pp:by_ratio.append(dict(rlo=j/100,rhi=(j+5)/100,count=len(pp),min_T=min(p['T']for p in pp),min_T_over_a2=min(p['T_over_a2']for p in pp),min_a_over_E=min(p['a_over_E']for p in pp)))
    np.savez_compressed('residual_samples.npz',u=np.array([p['u']for p in samples]),w=np.array([p['w']for p in samples]),r=np.array([p['r']for p in samples]),a=np.array([p['a']for p in samples]))
    result=dict(label='NUMERICAL',seed=101113,proposed_rays=proposals,accepted_points=len(samples),minima=minima,raw_min_T=raw_min,raw_min_T_over_a2=raw_scaled,by_ratio=by_ratio,refined=refined,least_points=sorted(allp,key=lambda p:p['T'])[:60],seconds=time.monotonic()-start,filters='Every condition in STRAT9 (11), evaluated in floating arithmetic with conservative tolerances; not exact membership or a proof.')
    Path('residual_map.json').write_text(json.dumps(result,indent=2)+'\n')
    with open('LOG.md','a')as f:f.write('\nNUMERICAL: mapping saved residual_map.json and residual_samples.npz; minima '+str({k:v[k]for k,v in minima.items()})+'. No finite sample is a sign certificate.\n')
    print(json.dumps(minima,indent=2),flush=True)
    if minima['T']['T']<0:raise RuntimeError('NEGATIVE CANDIDATE: stop discovery and certify exactly')
if __name__=='__main__':main()
