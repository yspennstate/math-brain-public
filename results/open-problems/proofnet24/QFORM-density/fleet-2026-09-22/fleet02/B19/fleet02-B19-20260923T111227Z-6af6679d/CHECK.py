import math
import numpy as np

m=8
eps=1/16
rows=[]; labels=[]
for _ in range(m): rows.append([1/math.sqrt(m),0,0]); labels.append('E1')
rows.append([0,math.sqrt(1-eps),0]); labels.append('hub')
for _ in range(m): rows.append([0,math.sqrt(eps/m),0]); labels.append('E2r')
for _ in range(m): rows.append([0,0,1/math.sqrt(m)]); labels.append('E3')
R=np.array(rows,float)
M=np.array([[1,0,0],[0,0,1],[0,1,0]],float)
A=R@M@R.T
nz=np.linalg.eigvalsh(A); nz=nz[np.abs(nz)>1e-10]
h=m
leaf=np.delete(np.delete(A,h,axis=0),h,axis=1)
lnz=np.linalg.eigvalsh(leaf); lnz=lnz[np.abs(lnz)>1e-10]
pairmax=max(abs(np.linalg.det(A[np.ix_([i,j],[i,j])])) for i in range(len(A)) for j in range(i+1,len(A)))
rng=np.random.default_rng(20260923)
maxerr=0.0; maxpi=0.0
for _ in range(5000):
    assign=rng.integers(0,3,len(A)); I=np.flatnonzero(assign==1); J=np.flatnonzero(assign==2)
    if not len(I) or not len(J): continue
    s=np.linalg.svd(A[np.ix_(I,J)],compute_uv=False)
    pi=float(np.prod(s[:3])) if len(s)>=3 else 0.0
    aI=sum(float(R[i]@R[i]) for i in I if labels[i]=='E1'); aJ=sum(float(R[i]@R[i]) for i in J if labels[i]=='E1')
    bI=sum(float(R[i]@R[i]) for i in I if labels[i] in ('hub','E2r')); bJ=sum(float(R[i]@R[i]) for i in J if labels[i] in ('hub','E2r'))
    cI=sum(float(R[i]@R[i]) for i in I if labels[i]=='E3'); cJ=sum(float(R[i]@R[i]) for i in J if labels[i]=='E3')
    formula=math.sqrt(aI*aJ*bI*bJ*cI*cJ)
    maxerr=max(maxerr,abs(pi-formula)); maxpi=max(maxpi,pi)
print('gram_error',np.max(np.abs(R.T@R-np.eye(3))))
print('spectrum',nz)
print('diagmax',np.max(np.abs(np.diag(A))))
print('pairdetmax',pairmax)
print('leaf_spectrum',lnz)
print('random_cut_formula_maxerr',maxerr)
print('random_cut_max_Pi3',maxpi)
print('proved_universal_cut_cap',math.sqrt(eps)/4)
assert maxerr<1e-12
assert maxpi<=math.sqrt(eps)/4+1e-12
print('QFORM_B19_STAR_CROSSVOLUME_OBSTRUCTION_CHECK_PASS')
