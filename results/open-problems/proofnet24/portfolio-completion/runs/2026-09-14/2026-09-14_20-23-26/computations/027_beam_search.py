"""Worker 027: deterministic exploratory 50:50 beam-splitter entropy search.

All optimization values are floating-point evidence, never certificates.
Run from this file's directory (imports the shared read-only dpp_core).
"""
import argparse
import itertools
import json
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize
from dpp_core import entropy, random_contraction


def shannon(p):
    p = np.asarray(p).ravel()
    p = p[p > 1e-28]
    return -float(p @ np.log(p))


def beam(K, L):
    A, B = (K + L) / 2, (K - L) / 2
    return np.block([[A, B], [B, A]])


def subsets(n, r):
    return np.array(list(itertools.combinations(range(n), r)), dtype=int).reshape(-1, r)


def proj_probs(U):
    n, r = U.shape
    if r == 0:
        return np.ones(1)
    return abs(np.linalg.det(U[subsets(n, r), :])) ** 2


def pgap(U, V):
    W = np.block([[U, V], [U, -V]]) / np.sqrt(2)
    return shannon(proj_probs(W)) - shannon(proj_probs(U)) - shannon(proj_probs(V))


def frame(G, r):
    return np.linalg.qr(G)[0][:, :r]


def vec_frame(x, n, r, complex_case):
    G = x[: n * r].reshape(n, r)
    if complex_case:
        G = G + 1j * x[n * r :].reshape(n, r)
    return frame(G, r)


def projection_search(seed=27001, trials=100, optimize=12):
    rng = np.random.default_rng(seed)
    summaries = []
    for n, r, s in [(3, 1, 2), (4, 1, 2), (4, 2, 2), (5, 2, 2), (5, 2, 3), (6, 3, 3)]:
        for complex_case in [False, True]:
            dim1, dim2 = n * r * (1 + complex_case), n * s * (1 + complex_case)
            def unpack(x):
                return vec_frame(x[:dim1], n, r, complex_case), vec_frame(x[dim1:], n, s, complex_case)
            def fun(x):
                return pgap(*unpack(x))
            candidates = []
            for _ in range(trials):
                x = rng.normal(size=dim1 + dim2)
                candidates.append((fun(x), x))
            candidates.sort(key=lambda t:t[0])
            best = candidates[0]
            results=[]
            for _, x in candidates[:optimize]:
                result=minimize(fun,x,method='BFGS',options={'maxiter':250,'gtol':1e-7})
                results.append(float(result.fun))
                if result.fun < best[0]:
                    best=(float(result.fun), result.x)
            U,V=unpack(best[1])
            item={'n':n,'r':r,'s':s,'complex':complex_case,'trials':trials,'optimized':optimize,
                  'initial_min':float(candidates[0][0]),'final_min':best[0],
                  'optimized_values':results,'projector_distance':float(np.linalg.norm(U@U.conj().T-V@V.conj().T)),
                  'U_real':U.real.tolist(),'U_imag':U.imag.tolist(),
                  'V_real':V.real.tolist(),'V_imag':V.imag.tolist()}
            summaries.append(item)
            print(json.dumps(item),flush=True)
    return summaries


def tetrahedral():
    # Four unit Bloch-sphere tetrahedron vectors form a tight 2-frame.
    z=np.exp(2j*np.pi/3)
    F=np.array([[1,0],[1/np.sqrt(3),np.sqrt(2/3)],
                [1/np.sqrt(3),np.sqrt(2/3)*z],
                [1/np.sqrt(3),np.sqrt(2/3)*z*z]],complex)/np.sqrt(2)
    P=F@F.conj().T
    e,Q=np.linalg.eigh(np.eye(4)-P)
    G=Q[:,e>.5]
    return {'input_probabilities':proj_probs(F).tolist(),
            'input_entropy_sum':2*shannon(proj_probs(F)),
            'output_entropy':shannon(proj_probs(np.block([[F,G],[F,-G]])/np.sqrt(2))),
            'gap':pgap(F,G)}


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--trials',type=int,default=60)
    ap.add_argument('--optimize',type=int,default=4)
    ap.add_argument('--only-tetrahedral',action='store_true')
    args=ap.parse_args()
    print(json.dumps({'tetrahedral':tetrahedral()}),flush=True)
    if not args.only_tetrahedral:
        projection_search(trials=args.trials,optimize=args.optimize)
