exec(open('computations/C053/search_separation.py').read().split('best=None')[0])
x=np.array([200,201,202,208]);r=np.array([600,1600,400,2000]);e1,e2,K,p,C,(S,T,V,noise)=calc(x,r)
print('e1vec',np.linalg.eigh(np.linalg.inv(S)-C)[1][:,0])
f=np.column_stack([masks]+[(masks[:,i]*masks[:,j])[:,None] for i,j in edges]);fbar=p@f; G=f.T@(p[:,None]*f)-np.outer(fbar,fbar)
P=np.zeros((10,10));P[:4,:4]=np.eye(4)
for e,(i,j) in enumerate(edges):P[4+e,i]=K[j,j];P[4+e,j]=K[i,i];P[4+e,4+e]=-2*K[i,j]
F=np.zeros((10,10));F[:4,:4]=C
for e,(i,j) in enumerate(edges):F[4+e,4+e]=-2*C[i,j]
M=P.T@np.linalg.solve(G,P)-F
print('full2 eig',eigvalsh(M))
N=masks.sum(axis=1);h=N-p@N;var=p@(h*h);print('varN',var)
rm=[];ds=[];cs=[]
for i,j in edges:
 idx=(masks[:,i]+2*masks[:,j]).astype(int); w=np.bincount(idx,weights=p,minlength=4)
 ph=np.bincount(idx,weights=p*h,minlength=4);I_e=(ph**2/w).sum()
 ds.append(2*(1+(w[1]+w[2])/(2*np.sqrt(w[0]*w[3]))));cs.append(C[i,j]);rm.append(I_e/var)
print('N ray endpoints',sum(c/d*a for c,d,a in zip(cs,ds,rm)),min(cs)*var+sum((c-min(cs))/d*a for c,d,a in zip(cs,ds,rm)))
