import itertools
import math
import numpy as np


def matrices(eps):
    rt2 = math.sqrt(2.0)
    U = np.array([
        [1.0,0.0,0.0],
        [0.0,1/rt2,0.0],
        [0.0,0.5,0.5],
        [0.0,0.0,1/rt2],
        [0.0,-0.5,0.5],
    ])
    V = np.array([
        [-2/3, 2/15, 11/15],
        [ 2/3,-1/3,   2/3],
        [ 1/3,14/15,  2/15],
    ])
    M = U @ np.diag([eps,2.0,2.0]) @ V.T
    return U,V,M


def check(eps=1e-6):
    U,V,M = matrices(eps)
    print('U_orth_error', np.linalg.norm(U.T@U-np.eye(3)))
    print('V_orth_error', np.linalg.norm(V.T@V-np.eye(3)))
    print('detV', np.linalg.det(V))
    print('singular_values', np.linalg.svd(M,compute_uv=False))
    print('rank_delete_row1', np.linalg.matrix_rank(M[1:,:], tol=1e-12))
    dets=[]
    for rows in itertools.combinations(range(5),3):
        d=np.linalg.det(M[list(rows),:])
        if abs(d)>1e-12:
            dets.append((rows,d))
    print('nonzero_3minors')
    for x in dets: print(x)
    assert len(dets)==6 and all(0 in rows for rows,_ in dets)
    assert np.min(np.abs(M))>0
    print('min_abs_physical_cross_entry', np.min(np.abs(M)))
    print('E3_from_minors', sum(d*d for _,d in dets), 'exact_formula',16*eps*eps)

    A=np.zeros((9,9))
    A[0,0]=1.0
    A[1:6,6:9]=M
    A[6:9,1:6]=M.T
    eig=np.linalg.eigvalsh(A)
    print('spectrum',eig)
    print('count_abs_ge_1',np.sum(np.abs(eig)>=1-1e-12))

    gamma=0.25
    k=eps**2/(gamma**2+eps**2)
    theta=k+128/65
    D=4225*(1+16*eps**2)
    K=U@np.diag([k,64/65,64/65])@U.T
    print('ridge_diag',np.diag(K))
    print('theta',theta)
    print('D',D)
    bound=16*3**(-5/8)*math.sqrt(math.e)*math.sqrt(3*theta/(3*theta-4))*D**(-1/(4*theta))
    coarse=16*3**(-5/8)*math.sqrt(math.e)*math.sqrt(96/31)*4225**(-65/642)
    partner=3*math.sqrt(math.e)*(4*eps)**(-1/3)
    print('square_assisted_exact_bound',bound)
    print('uniform_coarse_bound_eps_le_1_over_4',coarse)
    print('partner_finite_bank_bound',partner)
    assert np.max(np.diag(K)) <= 0.5+1e-12
    assert theta>4/3
    assert coarse<10.033
    return 0

if __name__=='__main__':
    raise SystemExit(check())
