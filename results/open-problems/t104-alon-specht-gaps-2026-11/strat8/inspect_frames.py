"""NUMERICAL: project supplied frames to the first zero-weight endpoint.
No floating result produced here is a proof.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json
import itertools
import numpy as np
from terms_reference import terms
from zero_face import construct


def chart_frame(row):
    U=np.asarray(row['u'],float)
    U=U-U.mean(axis=0)
    U=np.linalg.qr(U)[0]
    r=row['r']
    H=np.outer(U[:,0],U[:,0])+r*np.outer(U[:,1],U[:,1])
    pairs=list(itertools.combinations(range(5),2))
    ds=np.array([-1-r-20*H[i,j] for i,j in pairs])
    k=int(ds.argmax())
    a=2/ds[k]
    la=(2+a*(1+r))/4
    edge=pairs[k]
    perm=[i for i in range(5) if i not in edge]+list(edge)
    # The Gram representation of G/lambda.
    Y=U*np.sqrt(np.array([a,a*r])/la)
    Y=Y[perm]
    t=5*np.dot(Y[3],Y[3])
    first=5*(Y@Y[3])
    second=5*np.linalg.det(np.stack([np.broadcast_to(Y[3],Y.shape),Y],axis=1))
    coords=np.array([t,first[0],second[0],first[1],second[1],second[4]])
    if coords[-1]<0: coords[[2,4,5]]*=-1
    V=np.array([[coords[1],coords[2]],[coords[3],coords[4]],
                [1-coords[0]-coords[1]-coords[3],-coords[5]-coords[2]-coords[4]],
                [coords[0],0],[-1,coords[5]]])
    M=V.T@V
    delta=np.linalg.det(M); D=20*t-np.trace(M)
    R=V@V.T
    Q=V@np.linalg.inv(M)@V.T
    P=np.eye(5)-np.ones((5,5))/5-Q
    G=2*R/D
    lam=10*t/D
    W=2*(t+R)/D; np.fill_diagonal(W,0)
    # g45 is exactly zero in these coordinates.
    W[3,4]=W[4,3]=0
    direct=2*(lam*np.trace(G)-np.trace(G@G))
    direct+=(10/3)*np.sum(P*G*G)
    direct+=(1-lam)/3*(2*np.trace(G)-(10/3)*np.sum(np.diag(P)*np.diag(G)))
    direct-=2*sum(W[i,j]*(P[i,i]+P[j,j]-2*P[i,j])*(G[i,i]+G[j,j]-2*G[i,j]) for i,j in pairs)
    tref=terms(W); tr=tref[1]+tref[2]+tref[3]-tref[4]
    return dict(r=r,a_zero=float(a),spectral_ceiling=2/(3-r),permutation=perm,
                coordinates=coords.tolist(),Delta=float(delta),D=float(D),
                T_trace=float(direct),T_reference=float(tr),
                min_weight=float(min(W[i,j] for i,j in pairs)),
                spectral_clearance=float(np.linalg.det(5*t*np.eye(2)-M)),
                input_T=row['T'],input_q=row['q'])


def main():
    p=construct()[-1]
    out=[]
    for row in json.load(open('far_end_frames.json'))['rows']:
        rec=chart_frame(row)
        x=rec['coordinates']
        c=sum(float(coeff)*np.prod(np.power(x,mon)) for mon,coeff in p.terms())
        rec['Cface_polynomial']=float(c)
        rec['T_polynomial']=float(c/(45*rec['D']**2*rec['Delta']))
        out.append(rec)
        print('NUMERICAL:', 'r=%.3f'%rec['r'],'a_zero=%.9f'%rec['a_zero'],
              'T=%.9g'%rec['T_trace'],'C=%.9g'%c,'coords='+str(np.round(x,5)))
    result=dict(status='NUMERICAL',note='Floating projection to the first zero-weight endpoint; no proof.',rows=out,
                max_reference_error=max(abs(x['T_trace']-x['T_reference']) for x in out),
                max_polynomial_error=max(abs(x['T_trace']-x['T_polynomial']) for x in out))
    with open('frame_evaluations.json','w') as f: json.dump(result,f,indent=2)
    print('NUMERICAL: minimum projected T',min(x['T_trace'] for x in out))
    print('NUMERICAL: maximum reference discrepancy',result['max_reference_error'])
    print('NUMERICAL: maximum polynomial discrepancy',result['max_polynomial_error'])

if __name__=='__main__': main()
