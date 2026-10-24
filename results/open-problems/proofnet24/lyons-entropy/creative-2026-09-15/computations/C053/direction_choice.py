exec(open('computations/C053/degree2_numeric.py').read().split("print('full2 eig'")[0])
a=np.array([2,3,1,3]);u=-np.linalg.solve(M[4:,4:],M[4:,:4]@a);u=np.round(u,3);d=np.r_[a,u];AA=np.diag(a.astype(float))
for v,(i,j) in zip(u,edges):AA[i,j]=AA[j,i]=v
print('u',u,'eigsA',eigvalsh(AA));print('I1,F,I2',a@np.linalg.solve(S,a),d@F@d,d@(M+F)@d,'surplus',d@M@d)
