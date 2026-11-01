exec(open('computations/C072/explore_support.py').read().split('for s in')[0])
Z=np.eye(6)
for col,(i,j) in enumerate(combinations(range(3),2),3):Z[i,col]=-1;Z[j,col]=-1
G,C,H,D=calc(2**32);Gt,Ct,Ht,Dt=[Z.T@M@Z for M in [G,C,H,D]]
print('eigH-D transformed',np.linalg.eigvalsh(Ht-Dt));print('Ct',Ct);print('D',Dt)
G1,C1,H1,D1=calc(2**33)
E=Z.T@(C1-C)@Z
print('C width',E,'row widths',np.sum(abs(E),axis=1))
# Lower gram at s0 plus C interval crude row budget; q variation negligible.
print('lower crude eig',np.linalg.eigvalsh(Ht-Dt-np.diag(np.sum(abs(E),axis=1))))
print('mid lower eig',np.linalg.eigvalsh(Ht-Dt-E/2-np.diag(np.sum(abs(E),axis=1)/2)))
W=np.array([[Ct[1,2],-Ct[2,3]/2,-Ct[1,4]/2],[-Ct[2,3]/2,Ct[0,2],-Ct[0,5]/2],[-Ct[1,4]/2,-Ct[0,5]/2,Ct[0,1]]])
P=np.array([[0,0,1],[0,-1,0],[1,0,0]])
BI=[np.outer(U[:,i],U[:,j])-np.outer(U[:,j],U[:,i]) for i,j in combinations(range(3),2)]
DI=np.array([[np.sum(a*b) for b in BI] for a in BI]);print('imag gap',np.linalg.eigvalsh(2*P.T@W@P-DI),'W',W,'DI',DI)
print('imag quarter gap',np.linalg.eigvalsh(2*P.T@W@P-DI/4),'imag zero',np.linalg.eigvalsh(2*P.T@W@P))
