#!/usr/bin/env python3
import numpy as np


def make(B1,R,B2,B3):
    I=np.eye(2)
    return np.block([[B1,R,I],[R.T,B2,I],[I,I,B3]])

def det3(G,rows,cols):
    return float(np.linalg.det(G[np.ix_(rows,cols)]))

def check_once(rng):
    A=rng.normal(size=(2,2)); B1=(A+A.T)/2
    R=rng.normal(size=(2,2))
    A=rng.normal(size=(2,2)); B2=(A+A.T)/2
    A=rng.normal(size=(2,2)); B3=(A+A.T)/2
    G=make(B1,R,B2,B3)
    # Family A: rows X,X,Y_i; cols Y_j,Z,Z => B2_ij-R_ij.
    for i in range(2):
        for j in range(2):
            d=det3(G,[0,1,2+i],[2+j,4,5])
            assert abs(d-(B2[i,j]-R[i,j]))<1e-9
    # Family B: rows Y,Y,X_i; cols X_j,Z,Z => B1_ij-R^T_ij.
    for i in range(2):
        for j in range(2):
            d=det3(G,[2,3,i],[j,4,5])
            assert abs(d-(B1[i,j]-R.T[i,j]))<1e-9
    # Identity-edge families: I-B3 B1 and I-B3 B2.
    for i in range(2):
        for j in range(2):
            d1=det3(G,[0,1,4+i],[j,4,5])
            d2=det3(G,[2,3,4+i],[2+j,4,5])
            assert abs(d1-(np.eye(2)-B3@B1)[i,j])<1e-9
            assert abs(d2-(np.eye(2)-B3@B2)[i,j])<1e-9
    # Full third compound dominates the four disjoint selected families.
    z=0.0
    from itertools import combinations
    for rows in combinations(range(6),3):
        for cols in combinations(range(6),3):
            z += det3(G,list(rows),list(cols))**2
    defect=(np.linalg.norm(B2-R,'fro')**2+
            np.linalg.norm(B1-R.T,'fro')**2+
            np.linalg.norm(np.eye(2)-B3@B1,'fro')**2+
            np.linalg.norm(np.eye(2)-B3@B2,'fro')**2)
    assert z+1e-8>=defect
    return z,defect

def exact_endpoint(rng):
    A=rng.normal(size=(2,2)); S=(A+A.T)/2
    while abs(np.linalg.det(S))<0.2:
        A=rng.normal(size=(2,2)); S=(A+A.T)/2
    G=make(S,S,S,np.linalg.inv(S))
    sv=np.linalg.svd(G,compute_uv=False)
    assert sv[2]<1e-9
    # Exact factorization q=(x+y+S^{-1}z)^T S (x+y+S^{-1}z).
    L=np.hstack([np.eye(2),np.eye(2),np.linalg.inv(S)])
    G2=L.T@S@L
    assert np.linalg.norm(G-G2)<1e-9
    return sv

if __name__=='__main__':
    rng=np.random.default_rng(20260923)
    ratios=[]
    for _ in range(2000):
        z,d=check_once(rng)
        if d>0: ratios.append(z/d)
    sv=exact_endpoint(rng)
    print('QFORM_COMMONPLANE_LATENT_COMPLETION_CHECK_PASS')
    print('min_Z3_over_selected_defect=',min(ratios))
    print('exact_endpoint_singular_values=',sv.tolist())
