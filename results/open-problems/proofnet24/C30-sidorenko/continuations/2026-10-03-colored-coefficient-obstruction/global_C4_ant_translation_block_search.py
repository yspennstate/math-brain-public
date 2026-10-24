#!/usr/bin/env python3
"""Independent Walsh-block C4 identity, gradients and beyond-eight-state search.

No author imports. Signed b is separately sphere-normalized: its magnitude
does not restrict the actual nonnegative-host SIGN question.
"""
import argparse,json,os
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

HERE=Path(__file__).resolve().parent

class Blocks:
    def __init__(self,q):
        assert q>0 and q&(q-1)==0
        self.q=q
        self.xor=np.bitwise_xor(np.arange(q)[:,None],np.arange(q)[None,:])
        self.H=np.array([[(-1)**((i&j).bit_count())for j in range(q)]for i in range(q)])
    def correlation(self,p):return self.H@(p[:,None]*p[self.xor])
    def matrices(self,a,b):
        Ra,Rb=self.correlation(a),self.correlation(b)
        X=b[None,:,None]*self.H[:,:,None]*Rb[:,self.xor]
        Y=b[None,:,None]*self.H[:,:,None]*Ra[:,self.xor]
        Z=a[None,:,None]*self.H[:,:,None]*Ra[:,self.xor]
        return X,Y,Z,Ra,Rb
    def raw(self,a,b,gradient=False):
        X,Y,Z,Ra,Rb=self.matrices(a,b)
        Z2=Z@Z;Z3=Z2@Z
        scale=5*self.q**5
        value=scale*np.einsum('cij,cji->',X,Y@Z3)
        if not gradient:return value
        GX=np.swapaxes(Y@Z3,1,2);GY=np.swapaxes(Z3@X,1,2)
        XY=X@Y
        GZ=np.swapaxes(Z2@XY+Z@XY@Z+XY@Z2,1,2)
        gb=np.sum(self.H*np.sum(GX*Rb[:,self.xor]+GY*Ra[:,self.xor],axis=2),axis=0)
        ga=np.sum(self.H*np.sum(GZ*Ra[:,self.xor],axis=2),axis=0)
        # Correlation derivatives after changing h to g XOR d.
        IX=np.take_along_axis(GX,self.xor[None,:,:],axis=2)
        IY=np.take_along_axis(GY,self.xor[None,:,:],axis=2)
        IZ=np.take_along_axis(GZ,self.xor[None,:,:],axis=2)
        GRb=np.sum(IX*(b[None,:]*self.H)[:,:,None],axis=1)
        GRa=np.sum(IY*(b[None,:]*self.H)[:,:,None]+IZ*(a[None,:]*self.H)[:,:,None],axis=1)
        def back(p,GR):
            GC=self.H.T@GR
            reflected=GC[self.xor,np.arange(self.q)[None,:]]
            return np.sum((GC+reflected)*p[self.xor],axis=1)
        ga+=back(a,GRa);gb+=back(b,GRb)
        return value,scale*ga,scale*gb
    def objective(self,z):
        q=self.q;u,v=z[:q],z[q:]
        a=np.exp(u-u.max());a/=a.sum()
        norm=np.linalg.norm(v);r=1/np.sqrt(q)
        b=r*v/norm
        value,ga,gb=self.raw(a,b,True)
        return value,np.r_[a*(ga-a@ga),r/norm*(gb-v*(v@gb)/(norm*norm))]

def exact_identities():
    rng=np.random.default_rng(106331)
    records=[]
    for q in (2,4,8):
        model=Blocks(q)
        for _ in range(3):
            a=rng.integers(1,6,size=q).astype(object)
            b=rng.integers(-4,5,size=q).astype(object)
            X,Y,Z,Ra,Rb=model.matrices(a,b)
            block_sum=sum(np.trace(X[c]@Y[c]@Z[c]@Z[c]@Z[c])for c in range(q))
            xx,yy=np.divmod(np.arange(q*q),q);kk,ll=xx,yy
            i=xx[:,None]^yy[:,None];j=xx[:,None]^ll[None,:];k=kk[None,:]^yy[:,None]
            fullX=b[i]*b[j]*b[k];fullY=b[i]*a[j]*a[k];fullZ=a[i]*a[j]*a[k]
            full=np.trace(fullX@fullY@fullZ@fullZ@fullZ)
            assert block_sum==full
            assert all(Ra[c,d]==Rb[c,d]==0 for c in range(q)for d in range(q)if model.H[c,d]==-1)
            A=a[model.xor];B=b[model.xor];reflection=0
            for z in range(q):
                Dz=np.diag(A[z])
                for w in range(q):
                    Dw=np.diag(A[:,w]);FF=B*(A@Dz@A@Dw@A)
                    reflection+=A[z,w]*np.trace(FF@B@FF@B)
            assert reflection==full
            records.append({'q':q,'a':list(map(int,a)),'b':list(map(int,b)),
                'raw_trace_exact':str(full),'translation_and_reflection_identities':True})
    return records

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--q',type=int,default=32)
    ap.add_argument('--starts',type=int,default=30);ap.add_argument('--iterations',type=int,default=250)
    ap.add_argument('--seed',type=int,default=331642);args=ap.parse_args()
    model=Blocks(args.q);rng=np.random.default_rng(args.seed+args.q)
    z=rng.normal(size=2*args.q);value,grad=model.objective(z);h=1e-5
    fd=np.array([(model.objective(z+h*np.eye(2*args.q)[i])[0]-model.objective(z-h*np.eye(2*args.q)[i])[0])/(2*h)
                 for i in range(2*args.q)])
    error=float(max(abs(fd-grad)));assert error<1e-5
    report={'scope':'C4 coefficient, Boolean convolution quotient q; arbitrary signed sphere b; finite search only',
        'q':args.q,'full_host_states':2*args.q,'gradient_error':error,
        'exact_independent_translation_reflection_checks':exact_identities(), 'searches':[]}
    out=HERE/f'global_C4_ant_translation_blocks_q{args.q}_checks.json'
    for trial in range(args.starts):
        z=np.r_[rng.normal(size=args.q)*rng.choice([.1,1,2,4,8]),rng.normal(size=args.q)]
        # Include sparse and sign-rich initial b directions.
        if trial%4==1:z[args.q:]=rng.choice([-1.,1.],size=args.q)
        if trial%4==2:z[args.q:]=rng.normal(size=args.q)*(rng.random(args.q)<.25)
        res=minimize(model.objective,z,jac=True,method='L-BFGS-B',
            options={'maxiter':args.iterations,'ftol':1e-14,'gtol':1e-9})
        u,v=res.x[:args.q],res.x[args.q:];a=np.exp(u-u.max());a/=a.sum();b=v/(np.sqrt(args.q)*np.linalg.norm(v))
        report['searches'].append({'trial':trial,'value':float(res.fun),'success':bool(res.success),
            'iterations':int(res.nit),'a':a.tolist(),'b':b.tolist()})
        report['minimum']=min(r['value']for r in report['searches'])
        out.write_text(json.dumps(report,indent=2)+'\n')
        print('q',args.q,'trial',trial,'minimum',report['minimum'],flush=True)
        if res.fun<-1e-8:break
    report['status']='numerical search completed; no theorem inferred'
    out.write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()
