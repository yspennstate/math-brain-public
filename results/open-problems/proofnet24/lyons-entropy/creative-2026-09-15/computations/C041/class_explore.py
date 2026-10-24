exec(open(__file__.replace('class_explore.py','explore.py')).read().split('edges=')[0])
K=sp.Matrix(6,6,lambda i,j:sp.Rational(1,2)*(int(i//2==j//2)-sp.Rational(1,3)))
f=[len(S)-min(2,len(set(i//2 for i in S))) for S in SS]
T=operator(K,f)
print('sameclass K spec',T.eigenvals())
K2=sp.Matrix(6,6,lambda i,j:sp.Rational(1,2)*(int(i//2==j//2)-sp.Rational(1,3))*(-1)**(i+j))
T2=operator(K2,f)
print('anti K spec',T2.eigenvals())
for ev,mul,V in T2.eigenvects():
 if ev<0: print('negative ev',ev,'basis',V)
for eps in [sp.Rational(1,100),sp.Rational(1,10),1]:
 L=eps*sp.eye(n)+6*K
 fl=[0 if not S else -sp.log(L.extract(S,S).det()) for S in SS]
 for name,KK in [('same',K),('anti',K2)]:
  TN=np.array(operator(KK,fl),dtype=float)
  print('eps',eps,name,'spec',np.linalg.eigvalsh(TN))
