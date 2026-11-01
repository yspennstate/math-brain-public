exec(open('computations/C072/explore.py').read().split('rng=')[0])
U=np.array([[1,0,1],[0,1,1],[1,1,0],[1,-1,1],[2,1,-1],[1,2,1]],dtype=float)
for s in [10,100,1000,1e4,1e6,1e10,1e14]:
 G,C,H,J1,GN=matrices(s,U); dr=np.array([1,1,-.001]); print(s,'F',dr@C@dr,'I',dr@G@dr,'linear',dr@J1@dr,'eigsH',np.linalg.eigvalsh(H),'q13,23',H[0,2],H[1,2],flush=True)
