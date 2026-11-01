import json, math
import numpy as np

out={}
delta=1/18
c=0.5-math.sqrt(2*delta)-delta
out['mss_endpoint']={
    'delta':delta,
    'c_delta':c,
    'delta_over_c':delta/c,
    'density_constant_exact':24*math.sqrt(3)*math.e/(5*c),
    'simple_upper_23_over_c':23/c,
    'tail_threshold_c_over_16':c/16,
}

rows=[]
for r in [1.0,2.0,10.0]:
    n=np.array([1.,0.,0.])
    v1=np.array([1.,1.,0.])/math.sqrt(2)
    v2=np.array([0.,0.,1.])
    v3=np.array([1.,-1.,0.])/math.sqrt(2)
    V=np.vstack([v1,v2,v3])
    D=np.array([[0.,1/math.sqrt(1+r*r),0.],
                [1/math.sqrt(1+r*r),0.,0.],
                [0.,0.,1.]])
    L=np.vstack([r*n,V])
    A=L@D@L.T
    evals=np.linalg.eigvalsh(A)
    theta=abs(np.linalg.det(np.column_stack([n,v1,v2])))
    omega=theta**2
    detD=abs(np.linalg.det(D))
    bound=6*2**(2/3)*(r*r*detD*omega)**(-1/3)
    rows.append({
        'r':r,
        'eigenvalues':[float(x) for x in evals],
        'detD_abs':detD,
        'theta':theta,
        'Omega':omega,
        'bound':bound,
    })
out['tilted_plane_family']=rows
print(json.dumps(out,indent=2,sort_keys=True))
