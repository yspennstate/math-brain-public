import numpy as np

def phi_der(a,da,b,db):
 if a<=0 or b<=0:return np.nan
 return da*np.log1p(b/a)+db*np.log1p(a/b)
rng=np.random.default_rng(42)
mins={.5:(1e9,None),.1:(1e9,None),.9:(1e9,None)}
for j in range(3000):
 U=np.linalg.qr(rng.normal(size=(3,3)))[0]; V=U[:,:2]; w=U[:,2]
 a=rng.uniform(.02,.98);c=rng.uniform(-1,1)*np.sqrt(a*(1-a))*.99
 M=np.array([[a,c],[c,1-a]]);d=np.linalg.det(M)
 r=np.sum(V*V,axis=1); z=w*w;q=np.diag(V@M@V.T)
 for la in mins:
  der=sum(phi_der((1-la)*(q[i]-d*r[i]),-(1-la)*r[i],la*d*z[i],la*z[i])+phi_der((1-la)*d*z[i],(1-la)*z[i],la*((r[i]-q[i])-d*r[i]),-la*r[i]) for i in range(3))
  if der<mins[la][0]:mins[la]=(der,(a,c, w.tolist(),q.tolist(),r.tolist(),d))
print(mins)
