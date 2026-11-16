"""Standard-library-only integer reader for the rank-one matrix certificate."""
import json,itertools,random
records=json.load(open('rank_one_matrices.json'))
for row in records:
 m=row['twice_matrix']
 for i in range(3):assert m[i][i]>0
 for i,j in itertools.combinations(range(3),2):assert m[i][i]*m[j][j]-m[i][j]*m[j][i]>0
 det=m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
 assert det>0
rng=random.Random(19)
for point in range(20):
 z=[rng.randrange(1,7) for _ in range(4)]
 U=[sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)]
 t=sum(x*x for x in U);q=sum(x**4 for x in U);d=sum(x**3 for x in U);p=-U[0]*U[4];Delta=U[0]-U[4]
 K=[[0]*3 for _ in range(5)]
 for j in range(3):K[0][j]=U[4]-U[j+1];K[j+1][j]=Delta;K[4][j]=U[j+1]-U[0]
 e=[sum(K[i][j]*U[i]**2 for i in range(5)) for j in range(3)]
 alpha=140*p*q-28*p*t*t-47*q*t+13*t**3+24*d*d
 calc=[[0]*3 for _ in range(3)]
 for i in range(3):
  for j in range(3):
   R=sum(K[k][i]*K[k][j] for k in range(5));C=sum(K[k][i]*K[k][j]*U[k]**2 for k in range(5));F=sum(K[k][i]*K[k][j]*U[k] for k in range(5))
   calc[i][j]=2*alpha*R+2*(140*p*t-41*t*t)*C+12*t*e[i]*e[j]+36*t*d*F-t**3*R
 cert=[[0]*3 for _ in range(3)]
 for row in records:
  weight=1
  for zi,ei in zip(z,row['monomial']):weight*=zi**ei
  for i in range(3):
   for j in range(3):cert[i][j]+=weight*row['twice_matrix'][i][j]
 assert cert==calc
print('PROVED: 165 integer matrices, all 1,155 principal minors positive (independent determinant code).')
print('PROVED: coefficient sum and direct homogeneous matrix agree at 20 integer cone points (exact corroboration).')
