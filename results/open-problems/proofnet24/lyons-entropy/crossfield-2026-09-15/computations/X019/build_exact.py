from explore import *
from refine import physical,norm
from pathlib import Path

BASE=Path('computations/X019')
data=json.load(open(BASE/'refined.json'))
T=np.array([[F(x) for x in row] for row in data['coeff']],dtype=object)
cons=[tuple(F(x) for x in row) for row in data['constraints']]
assert all(physical(v) for v in cons)
# Remove only constraints supplied with a fully checked exact nonnegative redundancy certificate.
keep=list(range(len(cons)));removed=[]
for oi in range(len(cons)):
 if oi not in keep:continue
 rest=[j for j in keep if j!=oi]
 H=np.array([[-x for x in cons[j][1:]] for j in rest],dtype=object);k=np.array([cons[j][0] for j in rest],dtype=object)
 h=np.array([-x for x in cons[oi][1:]],dtype=object);z=cons[oi][0]
 r=linprog(-np.array(h,dtype=float),A_ub=np.array(H,dtype=float),b_ub=np.array(k,dtype=float),bounds=[(None,None)]*4,method='highs')
 if not r.success or -r.fun>float(z)+1e-9:continue
 ix=np.flatnonzero(r.ineqlin.marginals < -1e-7)
 if not len(ix):continue
 M=sp.Matrix(H[ix].tolist()).T
 try:
  lam,free=M.gauss_jordan_solve(sp.Matrix(h.tolist()))
 except ValueError:continue
 if free.shape[0]:continue
 lam=[F(x) for x in lam]
 if min(lam)<0 or sum(lam[ii]*k[ix[ii]] for ii in range(len(ix)))>z:continue
 support=[rest[j] for j in ix]
 assert all(sum(lam[j]*cons[support[j]][col] for j in range(len(lam)))==cons[oi][col] for col in range(1,5))
 removed.append({'index':oi,'support':support,'lambda':[str(x) for x in lam]});keep.remove(oi)
print('irredundant',len(keep),'removed',len(removed),flush=True)
H=np.array([[-x for x in cons[j][1:]] for j in keep],dtype=object);k=np.array([cons[j][0] for j in keep],dtype=object)
vs=vertices(H,k)
assert set(vs)==set(tuple(F(x) for x in p) for p in data['vertices'])
print('vertices',len(vs),'combinations',math.comb(len(keep),4),flush=True)
json.dump({'constraints':[[str(x) for x in v] for v in cons],'keep':keep,'removed':removed,'vertices':[[str(x) for x in p] for p in vs]},open(BASE/'polytope.json','w'),indent=2)

# Exact sparse couplings, numerical LP used only to discover a support.
couplings=[]
for i,p in enumerate(vs):
 r,b=lp(T,p);assert r.success
 ix=np.flatnonzero(r.x>1e-9)
 M=sp.Matrix(D[:,ix].tolist());br=sp.Matrix((T@np.array([F(1),*p],dtype=object)).tolist())
 sol,free=M.gauss_jordan_solve(br)
 assert not free.shape[0]
 vals=[F(x) for x in sol];assert min(vals)>=0
 x=np.zeros(90,dtype=object);x[:]=F(0)
 for j,v in zip(ix,vals):x[j]=v
 assert np.array_equal(D@x,T@np.array([F(1),*p],dtype=object))
 assert sum(x)==1
 couplings.append({str(j):str(v) for j,v in zip(ix,vals) if v})
 if i%10==0:print('couplings',i,flush=True)
json.dump({'coeff':data['coeff'],'constraints':[[str(x) for x in v] for v in cons],'keep':keep,'removed':removed,'vertices':[[str(x) for x in p] for p in vs],'couplings':couplings},open(BASE/'certificate.json','w'),indent=2)
print('COMPLETE exact couplings',len(couplings),flush=True)
