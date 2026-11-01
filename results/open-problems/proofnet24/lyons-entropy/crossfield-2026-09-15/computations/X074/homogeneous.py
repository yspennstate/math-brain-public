exec(open('computations/X074/series.py').read().split('for i in range(2):')[0])
coeff={}
for i in range(2):
 for j in range(i,2):
  xx=S.series(M[i,j],z,0,N+1).removeO().expand()
  coeff[i,j]=[S.factor(xx.coeff(z,n)) for n in range(0,N+1,2)]
for k in range(2,N//2+1):
 a,b,d=coeff[0,0][k],coeff[0,1][k],coeff[1,1][k]
 print(2*k,'det=',S.factor(a*d-b*b))
 print('eq',S.factor((a-b).subs(s,r)),S.factor((a+b).subs(s,r)))
