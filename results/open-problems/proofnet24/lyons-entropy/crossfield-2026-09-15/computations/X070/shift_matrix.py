import mpmath as mp
mp.mp.dps=30
B=[]
for i in range(3):
 a=mp.zeros(3);a[i,i]=1;B.append(a)
for i,j in [(0,1),(0,2),(1,2)]:
 a=mp.zeros(3);a[i,j]=a[j,i]=1;B.append(a)
 a=mp.zeros(3);a[i,j]=1j;a[j,i]=-1j;B.append(a)


def adj(A):
 return A*A-mp.trace(A)*A+((mp.trace(A)**2-mp.trace(A*A))/2)*mp.eye(3)
# mpmath lacks trace
mp.trace=lambda A:sum(A[i,i] for i in range(A.rows))
adjs=[[adj(B[i]+B[j])-adj(B[i])-adj(B[j]) if i!=j else 2*adj(B[i]) for j in range(9)] for i in range(9)]

def Qmat(L,s):
 T=L+(1+s)*mp.eye(3);Z=mp.det(T); R=T**-1; K=mp.eye(3)-R
 w=[];scores=[]
 for mask in range(8):
  idx=[i for i in range(3) if mask>>i&1]
  if not idx:w.append(mp.mpf(1));scores.append([mp.mpf(0)]*9);continue
  J=mp.matrix([[L[i,j]+(s if i==j else 0) for j in idx] for i in idx]);U=J**-1
  w.append(mp.re(mp.det(J)))
  scores.append([mp.re(sum(U[x,y]*b[idx[y],idx[x]] for x in range(len(idx)) for y in range(len(idx)))) for b in B])
 C=mp.diag([mp.log(w[2]*w[4]/w[6]),mp.log(w[1]*w[4]/w[5]),mp.log(w[1]*w[2]/w[3])]);tau=mp.log(w[3]*w[5]*w[6]/(w[1]*w[2]*w[4]*w[7]))
 M=T*C*T+tau*(T*T-T)
 return mp.matrix(9,9,lambda i,j: 0) if False else mp.matrix([[mp.re((sum(w[x]*w[y]*(scores[x][i]-scores[y][i])*(scores[x][j]-scores[y][j]) for x in range(8) for y in range(x))-mp.trace(M*adjs[i][j]))/Z**2) for j in range(9)] for i in range(9)])

for name,L in [
 ('near_rank1',mp.matrix([[1,mp.mpf('.9'),mp.mpf('.85')],[mp.mpf('.9'),1,mp.mpf('.8')],[mp.mpf('.85'),mp.mpf('.8'),1]])),
 ('complex',mp.matrix([[mp.mpf('.4'),mp.mpf('.1'),mp.mpf('.15')*1j],[mp.mpf('.1'),mp.mpf('2'),mp.mpf('.6')],[mp.mpf('.15')*-1j,mp.mpf('.6'),mp.mpf('3')]])),
 ('real_mixed',mp.matrix([[mp.mpf('.4'),mp.mpf('.1'),mp.mpf('-.15')],[mp.mpf('.1'),mp.mpf('2'),mp.mpf('.6')],[mp.mpf('-.15'),mp.mpf('.6'),mp.mpf('3')]]))]:
 print(name,'base',*[float(x) for x in mp.eigsy(L)[0]] if name!='complex' else 'complex',flush=True)
 for k in range(4):
  Q=mp.diff(lambda s:Qmat(L,s),mp.mpf(0),k)*((-1)**k)
  ev,vec=mp.eigsy(Q);print(k,float(ev[0]),flush=True)
  if ev[0]<0:
   print('direction',[float(vec[i,0]) for i in range(9)],flush=True)
