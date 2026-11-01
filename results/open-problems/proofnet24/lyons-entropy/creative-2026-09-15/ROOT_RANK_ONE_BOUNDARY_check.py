"""Finite numerical checks of an analytic boundary normal form; not a universal proof."""
import json
from pathlib import Path
import numpy as np
u=np.array([1,2,2],dtype=complex)/3
V=np.array([[2,2],[-2,1],[1,-2]],dtype=complex)/3
Q=np.outer(u,u.conj()); p=.4
J2=np.array([[.7,.1+.12j],[.1-.12j,.3]])
J=V@J2@V.conj().T; d=np.linalg.det(J2).real
pairs=[(0,1),(0,2),(1,2)]
def cross(M,i,j):
 w=u[j]*np.eye(3)[:,i]-u[i]*np.eye(3)[:,j]
 return np.vdot(w,M@w).real
def det2(M): return (M[0,0]*M[1,1]-M[0,1]*M[1,0]).real
basis=[Q]
for z in [np.array([1,0]),np.array([1j,0]),np.array([0,1]),np.array([0,1j])]:
 v=V@z;basis.append(np.outer(u,v.conj())+np.outer(v,u.conj()))
for B in [np.array([[1,0],[0,0]]),np.array([[0,0],[0,1]]),np.array([[0,1],[1,0]]),np.array([[0,1j],[-1j,0]])]:basis.append(V@B@V.conj().T)
def jets(e,A):
 a=np.vdot(u,A@u).real;v=V.conj().T@A@u;B=V.conj().T@A@V
 tr=np.trace(np.linalg.solve(J2,B)).real
 f=e*e*p*d;fd=e*e*d*a+p*e*d*tr
 fs=2*e*d*(a*tr-np.vdot(v,np.linalg.solve(J2,v)).real)+2*p*det2(B)
 ip=[];id1=[];id2=[]
 for i,j in pairs:
  ip.append(e*p*cross(J,i,j)+e*e*det2(J[np.ix_([i,j],[i,j])]))
  id1.append(p*cross(V@B@V.conj().T,i,j)+e*(A[i,i]*J[j,j]+J[i,i]*A[j,j]-2*np.real(A[i,j]*J[j,i])).real)
  id2.append(2*det2(A[np.ix_([i,j],[i,j])]))
 pr=[(1-p)*(1-e*np.trace(J2).real+e*e*d)];dr=[-np.trace(A).real+sum(id1)-fd];dd=[sum(id2)-fs]
 for i in range(3):
  inds=[k for k,x in enumerate(pairs) if i in x]
  pr.append(p*abs(u[i])**2+e*J[i,i].real-sum(ip[k] for k in inds)+f)
  dr.append(A[i,i].real-sum(id1[k] for k in inds)+fd)
  dd.append(-sum(id2[k] for k in inds)+fs)
 pr += [z-f for z in ip]+[f];dr +=[z-fd for z in id1]+[fd];dd +=[z-fs for z in id2]+[fs]
 return np.array(pr),np.array(dr),np.array(dd)
def h(e,A):
 r,s,t=jets(e,A)
 assert min(r)>0
 return -np.sum(s*s/r+t*np.log(r))
def form(fun,bs):
 M=np.zeros((9,9))
 for i in range(9):M[i,i]=fun(bs[i])
 for i in range(9):
  for j in range(i):M[i,j]=M[j,i]=(fun(bs[i]+bs[j])-M[i,i]-M[j,j])/2
 return M
limit=np.zeros((9,9));limit[0,0]=-1/(p*(1-p))
for i in range(1,5):limit[i,i]=-2
limit[8,8]=-2*(1-p)
for i in range(5,8):
 for j in range(5,8):limit[i,j]=-p*sum(cross(basis[i],k,l)*cross(basis[j],k,l)/cross(J,k,l) for k,l in pairs)
out={'status':'finite floating-point evidence only','p':p,'u':[1/3,2/3,2/3],'limiting_max_eigenvalue':float(np.linalg.eigvalsh(limit)[-1]),'samples':[]}
for e in [1e-3,1e-6,1e-12,1e-24]:
 L=np.log(1/e);sc=[1]+[1/np.sqrt(L)]*4+[np.sqrt(e)]*3+[1/np.sqrt(L)]
 H=form(lambda A:h(e,A),[s*A for s,A in zip(sc,basis)])
 ev=np.linalg.eigvalsh(H)
 assert ev[-1]<0
 out['samples'].append({'epsilon':e,'scaled_hessian_max_eigenvalue':float(ev[-1]),'operator_distance_to_limit':float(np.linalg.norm(H-limit,2))})
Path(__file__).with_name('ROOT_RANK_ONE_BOUNDARY_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

# A second finite diagnostic approaches a rank-one projection at comparable rates.
projection={'status':'finite floating-point evidence only','h':.8,'samples':[]}
for e in [1e-3,1e-6,1e-12]:
 p=1-.8*e
 L=np.log(1/e);sc=[np.sqrt(e)]+[1/np.sqrt(L)]*4+[np.sqrt(e)]*3+[1]
 H=form(lambda A:h(e,A),[s*A for s,A in zip(sc,basis)])
 ev=np.linalg.eigvalsh(H)
 assert ev[-1]<0
 projection['samples'].append({'epsilon':e,'scaled_hessian_max_eigenvalue':float(ev[-1]),'pure_dark_curvature':h(e,basis[8])})
Path(__file__).with_name('ROOT_PROJECTION_BOUNDARY_results.json').write_text(json.dumps(projection,indent=2)+'\n')
print(json.dumps(projection,indent=2))
