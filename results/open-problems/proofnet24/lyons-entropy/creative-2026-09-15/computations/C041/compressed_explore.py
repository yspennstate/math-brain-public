exec(open(__file__.replace('compressed_explore.py','explore.py')).read().split('edges=')[0])
f=[len(S)-min(2,len(set(i//2 for i in S))) for S in SS]
cs=[0,1,2,0,1,2]
K=sp.Matrix(6,6,lambda i,j:sp.Rational(1,2)*(int(cs[i]==cs[j])-sp.Rational(1,3)))
T=operator(K,f)
U=sp.Matrix(6,4,lambda i,j: 1 if j==0 else (int(i==j-1)-int(i==j+2)))
UP=list(it.combinations(range(4),2))
Q=sp.Matrix([[U.extract(ij,kl).det() for kl in UP] for ij in pairs])
TC=Q.T*T*Q
print('compT',TC,'spec',TC.eigenvals(),sep='\n')
TN=np.array(T,dtype=float);ev,V=np.linalg.eigh(TN)
v=V[:,0];print('full min',ev[0],'vec',v)
for d in [1,2,3,4,6,12,24]:
 z=sp.Matrix([round(float(x*d/max(abs(v)))) for x in v]);val=(z.T*T*z)[0]
 if val<0:print('witness',d,list(z),'q',val)
L0=sp.Matrix(6,6,lambda i,j:2 if i//2==j//2 else -1)
for eps in [sp.Rational(1,10),sp.Rational(1,100),sp.Rational(1,1000),sp.Rational(1,1000000)]:
 L=eps*sp.eye(n)+L0
 fl=[0 if not S else -sp.log(L.extract(S,S).det()) for S in SS]
 TL=operator(K,fl)
 print('eps',eps,'minfull',min(np.linalg.eigvalsh(np.array(TL,dtype=float))),'mincomp',min(np.linalg.eigvalsh(np.array(Q.T*TL*Q,dtype=float))))
