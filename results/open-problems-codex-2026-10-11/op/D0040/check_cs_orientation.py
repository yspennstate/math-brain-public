import pathlib,json
import numpy as np
P=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(400022)
result=[]
for n in [1,2,3,5,8,12]:
 N=1000
 p=rng.uniform(0.001,0.999,(N,n)); q=rng.uniform(0.001,0.999,(N,max(n-1,0)))
 previous=np.column_stack([np.zeros(N),q]); following=np.column_stack([q,np.zeros(N)])
 B=np.zeros((N,n,n)); C=B.copy(); i=np.arange(n)
 B[:,i,i]=np.sqrt(p*(1-previous)); C[:,i,i]=np.sqrt((1-p)*(1-previous))
 i=np.arange(n-1)
 B[:,i+1,i]=np.sqrt((1-p[:,:-1])*q)
 C[:,i+1,i]=-np.sqrt(p[:,:-1]*q)
 # All four primary-source blocks, constructed directly from Definition 1.6.
 B11=np.zeros_like(B); B12=B11.copy(); B21=B11.copy(); B22=B11.copy(); i=np.arange(n)
 B11[:,i,i]=np.sqrt(p*(1-following))[:,::-1]
 B21[:,i,i]=-np.sqrt((1-p)*(1-following))[:,::-1]
 B12[:,i,i]=np.sqrt((1-p)*(1-previous))[:,::-1]
 B22[:,i,i]=np.sqrt(p*(1-previous))[:,::-1]
 i=np.arange(n-1)
 B11[:,i,i+1]=-np.sqrt((1-p[:,1:])*q)[:,::-1]
 B21[:,i,i+1]=-np.sqrt(p[:,1:]*q)[:,::-1]
 B12[:,i+1,i]=np.sqrt(p[:,:-1]*q)[:,::-1]
 B22[:,i+1,i]=-np.sqrt((1-p[:,:-1])*q)[:,::-1]
 Q=np.concatenate([np.concatenate([B11,B12],axis=2),np.concatenate([B21,B22],axis=2)],axis=1)
 R=np.eye(n)[::-1]; S=np.diag((-1.)**np.arange(n))
 orientation_error=float(np.max(np.abs(B22-S@R@B.transpose(0,2,1)@R@S)))
 orthogonality_error=float(np.max(np.abs(Q@Q.transpose(0,2,1)-np.eye(2*n))))
 singular_error=float(np.max(np.abs(np.linalg.svd(B11,compute_uv=False)-np.linalg.svd(B22,compute_uv=False))))
 eigen_error=float(np.max(np.abs(np.linalg.eigvalsh(B@B.transpose(0,2,1))-np.linalg.eigvalsh(B11@B11.transpose(0,2,1)))))
 assert orientation_error==0
 assert max(orthogonality_error,singular_error,eigen_error)<1e-13
 result.append(dict(n=n,samples=N,orientation_error=orientation_error,orthogonality_error=orthogonality_error,B11_B22_singular_value_error=singular_error,model_eigenvalue_error=eigen_error))
(P/'cs_orientation_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
