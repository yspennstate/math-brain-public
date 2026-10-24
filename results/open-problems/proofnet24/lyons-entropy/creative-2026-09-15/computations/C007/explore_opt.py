exec(open('/workspace/scratch/f042dae27852/creative-lyons-20260915/computations/C007/explore.py').read().split('rng=np.random')[0])
rng=np.random.default_rng(7700720260915)
basis=[np.array([[1,0],[0,0]],complex),np.array([[0,0],[0,1]],complex),np.array([[0,1],[1,0]],complex),np.array([[0,1j],[-1j,0]],complex)]
best=(float('inf'),None)
for it in range(100000):
 A=randk(rng);u=rng.normal(size=2)+1j*rng.normal(size=2);u/=np.linalg.norm(u);Q=np.outer(u,u.conjugate());f=fisher(A,Q)
 ds=[fish_der(A,Q,E) for E in basis]
 G=np.array([[ds[0],(ds[2]+1j*ds[3])/2],[(ds[2]-1j*ds[3])/2,ds[1]]]); ev,U=np.linalg.eigh(G);B=(U*(ev>0))@U.conj().T
 val=(2*f+fish_der(A,Q,A-B))/f
 if val<best[0]:best=val,(A,B,Q,f)
 if val<-.01:print('FOUND',it,val,flush=True);break
print(best[0]);
for x in best[1]:print(x)
np.savez('/workspace/scratch/f042dae27852/creative-lyons-20260915/computations/C007/fisher_opt_search.npz',A=best[1][0],B=best[1][1],Q=best[1][2],f=best[1][3],ratio=best[0])
