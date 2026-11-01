exec(open('computations/C046/search.py').read().split('best=(0,None)')[0])
real=[0,1,2,3,5,7]
best=(0,None)
for d in np.linspace(.025,.975,39):
    for b in np.linspace(-.45,.45,73):
        K=(d-b)*np.eye(3)+b*np.ones((3,3))
        ev=np.linalg.eigvalsh(K)
        if ev.min()<=.00001 or ev.max()>=.99999:continue
        p,g,h,mu=jets(K);r=p/mu
        for s in [0,.01,.1,1,10,100,1e4]:
            U=np.einsum('si,sj,s->ij',g,g,1/mu/(r+s)**2)-np.einsum('sij,s->ij',h,1/(r+s))
            w,v=np.linalg.eigh(U[np.ix_(real,real)]*(1+s)**2)
            if w[0]<best[0]:
                a=np.zeros(9);a[real]=v[:,0]
                best=(w[0],{'d':float(d),'b':float(b),'s':s,'eigenvalue_scaled':float(w[0]),'direction':a.tolist()})
print('real structured',best)
Path('computations/C046/refine_result.json').write_text(json.dumps(best[1],indent=2))
